#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
只读审计工具：扫描 wiki/concepts 与 wiki/entities 全量页面，输出 DoD 缺口与基线数据。

默认不修改任何页面，只扫描并输出到 stdout。
用法：
    python tools/audit_wiki_pages.py --summary
    python tools/audit_wiki_pages.py --json <path>
    python tools/audit_wiki_pages.py --paths wiki/concepts/pl-quenching.md wiki/entities/GaSe.md
    python tools/audit_wiki_pages.py --strict

--strict 时对 status 非法值、raw/note 直链、断链、缺失图片、frontmatter 水印噪音等按错误计数并置非零退出码。
"""
import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
CONCEPTS = WIKI / "concepts"
ENTITIES = WIKI / "entities"
PAPERS = WIKI / "papers"

FM_RE = re.compile(r'^---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)', re.DOTALL)
VALID_STATUS = {"stub", "developing", "mature"}
VALID_TYPES = {"concept", "entity"}

# 章节关键词（按标题匹配）
SEC_TAINAI = re.compile(r'^##\s*.*太奶导读', re.M)
SEC_STRUCT = re.compile(r'^##\s*.*结构概览', re.M)
SEC_MECH = re.compile(r'^##\s*.*(物理实质|物理机制|物理分类|机制|物性|物理与算法|物理起源|物理本质|微观机制)', re.M)
SEC_RELPAPER = re.compile(r'^##\s*.*相关论文', re.M)
# 「📚 相关论文」小节内的条目行：- [[../papers/xxx]]…
RELPAPER_ITEM = re.compile(r'^\s*[-*]\s*\[\[[^\]]*papers/[^\]]+\]\](.*)$', re.M)
SEC_REL = re.compile(r'^##\s*.*关联概念与实体', re.M)
# 占位文本：批量生成时留下的模板句，能通过「章节存在 / 中文字数够」的检查，
# 但按 DoD 属于未完成内容，必须单独识别。
# 只认「批量生成」独有的固定串。注意：`乖孙，这一条讲的是「…」` 这个开头本身
# 也被人工撰写的好页面使用（如 rashba-effect），不能单凭它判占位。
PLACEHOLDER_TAINAI = re.compile(
    r'这是一篇论文的研究主题|这篇论文为它提供了关键证据'
    r'|一句话记住它的发现|由多篇论文的证据共同支撑|这一条要讲的核心对象是')
PLACEHOLDER_CONTRIB = re.compile(r'为本文档提供核心证据|提供了核心证据支持|为本页提供核心证据')
PARAM_TABLE = re.compile(r'^\|.*\|.*\|.*\|.*\|.*\|$', re.M)  # 5 列参数表
# 真正违规的 raw 链接：raw/note 裸链接（concept/entity 禁止直链 note），
# 或以 wikilink 形式 [[...raw/(note|figures)/...]] 链接 raw 层。
# 图片嵌入 ![..](<../../raw/figures/...>) 属于 SCHEMA 允许的资源引用，不视为违规。
RAW_LINK = re.compile(r'raw/note/|\[\[[^\]]*raw/(?:note|figures)/')
IMG_LINK = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
WIKILINK = re.compile(r'\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]')
PAPER_LINK = re.compile(r'\[\[\.\./papers/([^\]|#]+)')
CONCEPT_LINK = re.compile(r'\[\[\.\./concepts/([^\]|#]+)')
ENTITY_LINK = re.compile(r'\[\[\.\./entities/([^\]|#]+)')

# frontmatter 水印/元数据噪音键：外部 AI 写作工具（AIGC 标识块）粘回页面时带入，
# SCHEMA 要求 frontmatter 只保留可查询的结构化字段，此类键须清除。
NOISE_FM_RE = re.compile(
    r'^[ \t]*(AIGC|Label|ContentProducer|ContentPropagator|ProduceID|PropagateID'
    r'|ReservedCode\d*)[ \t]*:', re.M)


def parse_frontmatter(text):
    """返回 (frontmatter dict 或 None, 正文)。"""
    m = FM_RE.match(text)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    return fm, text[m.end():]


def parse_list_field(v):
    """解析 [a, b, c] 或 'a, b, c' 或 YAML 列表。"""
    if v is None:
        return []
    v = v.strip()
    if v.startswith('[') and v.endswith(']'):
        v = v[1:-1]
    items = [x.strip().strip('"\'') for x in v.split(',') if x.strip()]
    return items


def slug_of(path):
    return path.stem


# 形式缺陷判据。前两条是 wiki/format-spec.md 明令禁止的写法，第三条是把英文标题
# 直接塞进「」冒充贡献句；第四条把「有中文但没说清具体贡献」的门槛从 6 字提到 15 字
# ——实测 `— PAW 方法（电荷密度计算基础）。` 这类只有 10 字，旧阈值放行了 100 余条。
CONTRIB_DASH_TITLE = re.compile(r'^\s*[—–-]\s*[A-Z]')
CONTRIB_REVIEW_BOILER = re.compile(r'从综述角度梳理了')
CONTRIB_EN_TITLE = re.compile(r'「[A-Za-z][^」]{20,}」')
CONTRIB_MIN_CJK = 15


def contrib_defects(tail):
    """返回单条贡献句的形式缺陷标签集合。"""
    flags = set()
    if CONTRIB_DASH_TITLE.search(tail) and len(re.findall(r'[一-鿿]', tail)) < 6 \
            and len(re.findall(r'\b[A-Za-z][A-Za-z-]{2,}\b', tail)) >= 3:
        flags.add('dash-title')
    if CONTRIB_REVIEW_BOILER.search(tail):
        flags.add('review-boiler')
    if CONTRIB_EN_TITLE.search(tail):
        flags.add('en-title-quoted')
    n = len(re.findall(r'[一-鿿]', tail))
    if n < 6:
        flags.add('no-contrib')
    elif n < CONTRIB_MIN_CJK:
        flags.add('too-short')
    return flags


def relpaper_contrib_stats(body):
    """统计「相关论文」小节里贡献句的缺失与形式缺陷。

    DoD 要求每篇论文双链后跟一句该论文对本页的具体贡献。返回
    (条目总数, 完全没有贡献句的条数, 有形式缺陷的条数, 缺陷标签计数)。
    """
    m = re.search(r'^##[^\n]*相关论文[^\n]*\n(.*?)(?=^##\s|\Z)', body, re.M | re.S)
    if not m:
        return 0, 0, 0, {}
    total = 0
    missing = 0
    weak = 0
    kinds = {}
    for tail in RELPAPER_ITEM.findall(m.group(1)):
        total += 1
        flags = contrib_defects(tail)
        if 'no-contrib' in flags:
            missing += 1
        elif flags:
            weak += 1
        for f in flags:
            kinds[f] = kinds.get(f, 0) + 1
    return total, missing, weak, kinds


def relpaper_placeholder_count(body):
    """统计「相关论文」小节里有多少条目的贡献句是占位模板句。"""
    m = re.search(r'^##[^\n]*相关论文[^\n]*\n(.*?)(?=^##\s|\Z)', body, re.M | re.S)
    if not m:
        return 0
    return sum(1 for tail in RELPAPER_ITEM.findall(m.group(1))
               if PLACEHOLDER_CONTRIB.search(tail))


def tainai_is_placeholder(body):
    """判断太奶导读小节是否只有占位模板句。"""
    m = re.search(r'^##[^\n]*太奶导读[^\n]*\n(.*?)(?=^##\s|\Z)', body, re.M | re.S)
    if not m:
        return False
    return bool(PLACEHOLDER_TAINAI.search(m.group(1)))


def clean_target(t):
    """归一化 wikilink 目标：去空白，并去掉表格内转义竖线 `[[x\\|别名]]` 残留的反斜杠。

    Obsidian 在 markdown 表格单元格里必须把别名分隔符写成 `\\|`，否则会被解析成
    列分隔符。因此 `[[../concepts/x\\|别名]]` 是合法写法，捕获到的目标会带尾部反斜杠，
    必须剥离后再判断存在性，否则合法链接会被误报为断链。
    """
    return t.strip().rstrip('\\').strip()


def scan_page(path, all_slugs, all_paths, incoming):
    """扫描单个页面，返回审计记录 dict。"""
    text = path.read_text(encoding='utf-8', errors='replace')
    fm, body = parse_frontmatter(text)
    lines = text.splitlines()
    rel = path.relative_to(REPO).as_posix()
    layer = 'concepts' if path.parent == CONCEPTS else 'entities'
    slug = slug_of(path)

    rec = {
        'path': rel,
        'layer': layer,
        'slug': slug,
        'has_frontmatter': fm is not None,
        'lines': len(lines),
        'chars': len(text),
        'h1': None,
        'title': None,
        'type': None,
        'status': None,
        'tags': [],
        'relpaper_items': 0,
        'relpaper_missing_contrib': 0,
        'relpaper_weak_contrib': 0,
        'relpaper_contrib_defects': {},
        'relpaper_placeholder_contrib': 0,
        'tainai_placeholder': False,
        'fm_noise_keys': [],
        'has_tainai': bool(SEC_TAINAI.search(body)),
        'has_struct': bool(SEC_STRUCT.search(body)),
        'has_mech': bool(SEC_MECH.search(body)),
        'has_relpaper': bool(SEC_RELPAPER.search(body)),
        'has_rel': bool(SEC_REL.search(body)),
        'has_param_table': bool(PARAM_TABLE.search(body)),
        'papers_fm': [],
        'papers_body': [],
        'raw_links': [],
        'images': [],
        'missing_images': [],
        'broken_links': [],
        'incoming_total': 0,
        'incoming_papers': 0,
        'incoming_wiki': 0,
        'cross_layer_collision': False,
        'identity': None,
        'dod_gaps': [],
    }

    # H1
    m = re.search(r'^#\s+(.+)$', body, re.M)
    if m:
        rec['h1'] = m.group(1).strip()

    if fm:
        rec['title'] = fm.get('title')
        rec['type'] = fm.get('type')
        rec['status'] = fm.get('status')
        rec['tags'] = parse_list_field(fm.get('tags'))
        rec['papers_fm'] = parse_list_field(fm.get('papers'))
        fm_block = FM_RE.match(text)
        if fm_block:
            rec['fm_noise_keys'] = sorted(set(NOISE_FM_RE.findall(fm_block.group(1))))

    # 正文 paper links
    rec['papers_body'] = sorted(set(clean_target(t) for t in PAPER_LINK.findall(body)))

    # raw/note 违规链接
    rec['raw_links'] = sorted(set(RAW_LINK.findall(body)))

    # 图片链接与存在性
    for img in IMG_LINK.findall(body):
        img = img.strip()
        rec['images'].append(img)
        # markdown 允许 <path> 尖括号包裹链接目标，解析存在性时去掉尖括号
        clean = img.strip('<>')
        p = (path.parent / clean).resolve()
        if not p.exists():
            rec['missing_images'].append(img)

    # 双链断链（concept/entity 目标存在性）
    for target in CONCEPT_LINK.findall(body):
        target = clean_target(target)
        if target not in all_slugs.get('concepts', set()):
            rec['broken_links'].append(f'concepts/{target}')
    for target in ENTITY_LINK.findall(body):
        target = clean_target(target)
        if target not in all_slugs.get('entities', set()):
            rec['broken_links'].append(f'entities/{target}')

    # 相关论文条目的贡献句覆盖
    (rec['relpaper_items'], rec['relpaper_missing_contrib'],
     rec['relpaper_weak_contrib'], rec['relpaper_contrib_defects']) = relpaper_contrib_stats(body)
    rec['relpaper_placeholder_contrib'] = relpaper_placeholder_count(body)
    rec['tainai_placeholder'] = tainai_is_placeholder(body)

    # 入链
    rec['incoming_total'] = len(incoming.get(rel, []))
    rec['incoming_papers'] = sum(1 for s in incoming.get(rel, []) if s.startswith('wiki/papers/'))
    rec['incoming_wiki'] = rec['incoming_total'] - rec['incoming_papers']

    # 同 slug 跨层碰撞（任一侧为 stub 即视为占位/迁移说明页，不构成内容冲突，予以豁免）
    other = 'entities' if layer == 'concepts' else 'concepts'
    if slug in all_slugs.get(other, set()) and rec.get('status') != 'stub':
        other_path = REPO / 'wiki' / other / (slug + '.md')
        other_is_stub = False
        if other_path.exists():
            other_fm, _ = parse_frontmatter(other_path.read_text(encoding='utf-8', errors='replace'))
            other_is_stub = (other_fm is not None and other_fm.get('status') == 'stub')
        if not other_is_stub:
            rec['cross_layer_collision'] = True

    # 身份类型候选
    if not fm:
        rec['identity'] = 'short-aggregation'
    elif rec['lines'] <= 10:
        rec['identity'] = 'alias-or-stub'
    else:
        rec['identity'] = 'canonical'

    # DoD 缺口
    if not fm:
        rec['dod_gaps'].append('no-frontmatter')
    else:
        if not rec['title']:
            rec['dod_gaps'].append('no-title')
        if not rec['type'] or rec['type'] not in VALID_TYPES:
            rec['dod_gaps'].append('no-valid-type')
        if not rec['status']:
            rec['dod_gaps'].append('no-status')
        elif rec['status'] not in VALID_STATUS:
            rec['dod_gaps'].append('invalid-status')
        if not rec['tags'] or rec['tags'][0] not in VALID_TYPES:
            rec['dod_gaps'].append('no-valid-tags')
        if rec['fm_noise_keys']:
            rec['dod_gaps'].append('fm-watermark-noise')
    if not rec['has_tainai']:
        rec['dod_gaps'].append('no-tainai')
    if not rec['has_relpaper']:
        rec['dod_gaps'].append('no-relpaper-section')
    if not rec['has_rel']:
        rec['dod_gaps'].append('no-rel-section')
    if rec['raw_links']:
        rec['dod_gaps'].append('raw-link')
    if rec['missing_images']:
        rec['dod_gaps'].append('missing-image')
    if rec['broken_links']:
        rec['dod_gaps'].append('broken-link')
    if rec['has_relpaper'] and not rec['papers_body'] and not rec['papers_fm']:
        rec['dod_gaps'].append('relpaper-no-papers')
    if rec['relpaper_missing_contrib']:
        rec['dod_gaps'].append('relpaper-no-contrib')
    if rec['relpaper_weak_contrib']:
        rec['dod_gaps'].append('relpaper-weak-contrib')
    if rec['relpaper_placeholder_contrib']:
        rec['dod_gaps'].append('relpaper-placeholder-contrib')
    if rec['tainai_placeholder']:
        rec['dod_gaps'].append('placeholder-tainai')

    return rec


def build_incoming_index(all_md_files):
    """扫描全库 .md，建立 目标路径 -> [来源路径] 反链索引。

    键统一归一化为 `wiki/<concepts|entities>/<slug>.md`，与 scan_page 中
    `path.relative_to(REPO)` 的形式一致（否则查表恒为空、入链计数恒为 0）。
    """
    incoming = {}
    for src in all_md_files:
        try:
            text = src.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        src_rel = src.relative_to(REPO).as_posix()
        for target in WIKILINK.findall(text):
            t = clean_target(target)
            # 归一化：剥离任意层级的 ../
            while t.startswith('../'):
                t = t[3:]
            # 剥离 wiki/ 之前的仓库名等前缀（如 科研Wiki/wiki/concepts/x）
            idx = t.find('wiki/')
            if idx > 0:
                t = t[idx:]
            if t.startswith('wiki/'):
                t = t[5:]
            if t.endswith('.md'):
                t = t[:-3]
            # 只统计指向 concepts/entities 页面的链接
            if t.startswith('concepts/') or t.startswith('entities/'):
                incoming.setdefault(f'wiki/{t}.md', []).append(src_rel)
    return incoming


def fm_list_field(fm_text, key):
    """从 frontmatter 原文里取列表字段，兼容 inline `[a, b]` 与 block `- a` 两种写法。"""
    m = re.search(r'^' + re.escape(key) + r'[ \t]*:[ \t]*(.*)$', fm_text, re.M)
    if not m:
        return []
    inline = m.group(1).strip()
    if inline:
        return parse_list_field(inline)
    # block 写法：紧随其后的缩进 `- item` 行
    rest = fm_text[m.end():]
    items = []
    for line in rest.splitlines():
        if re.match(r'^\s*-\s+', line):
            items.append(re.sub(r'^\s*-\s+', '', line).strip().strip('"\''))
        elif line.strip() and not line.startswith((' ', '\t')):
            break
    return items


def _slug_tokens(s):
    """slug 词元集合：小写、按 -/_ 切词、逐词去尾部复数 s。"""
    out = set()
    for w in re.split(r'[-_]+', s.lower()):
        if not w:
            continue
        out.add(w[:-1] if w.endswith('s') and len(w) > 3 else w)
    return out


def _norm_slug(s):
    """slug 归一化键：词元去复数后排序拼接，可吃掉词序差异（landau-ginzburg / ginzburg-landau）。"""
    return '|'.join(sorted(_slug_tokens(s)))


def papers_xref(all_md_files):
    """papers 层 ↔ concepts/entities 层的双向一致性核查。

    三类不一致：
      dangling    : 卡片 frontmatter 声明的 slug 在库中不存在（错标/改名残留）
      not_cited   : 卡片声明了某页，但该页正文并未引用这篇论文
      not_declared: 某页正文引用了这篇论文，但卡片 frontmatter 未声明该页
    slug 匹配大小写不敏感（库内存在 2D-materials / 2d-materials 之类差异）。
    """
    real = {}   # (layer, slug.lower()) -> 实际 slug
    body = {}   # (layer, slug.lower()) -> 该页正文引用的 citekey 集合
    for layer, d in (('concepts', CONCEPTS), ('entities', ENTITIES)):
        for p in sorted(d.glob('*.md')):
            key = (layer, p.stem.lower())
            real[key] = p.stem
            text = p.read_text(encoding='utf-8', errors='replace')
            body[key] = set(clean_target(t) for t in PAPER_LINK.findall(text))

    res = {'dangling_layer_swap': [], 'dangling_near_miss': [], 'dangling_unknown': [],
           'not_cited': [], 'not_declared': [], 'cards': 0}
    # 近似同名索引：归一化键 -> [(layer, 实际 slug)]
    approx = {}
    for (layer, slug_l), actual in real.items():
        approx.setdefault(_norm_slug(actual), []).append((layer, actual))

    declared_map = {}
    for card in sorted(PAPERS.glob('*.md')):
        citekey = card.stem
        text = card.read_text(encoding='utf-8', errors='replace')
        m = FM_RE.match(text)
        if not m:
            continue
        res['cards'] += 1
        fm_text = m.group(1)
        for layer, field in (('concepts', 'concepts'), ('entities', 'entities')):
            for slug in fm_list_field(fm_text, field):
                slug = slug.strip()
                if not slug:
                    continue
                key = (layer, slug.lower())
                declared_map.setdefault(key, set()).add(citekey)
                if key in real:
                    if citekey not in body[key]:
                        res['not_cited'].append((citekey, f'{layer}/{real[key]}'))
                    continue
                other = 'entities' if layer == 'concepts' else 'concepts'
                if (other, slug.lower()) in real:
                    res['dangling_layer_swap'].append(
                        (citekey, f'{layer}/{slug}', f'{other}/{real[(other, slug.lower())]}'))
                    continue
                cand = [f'{l}/{s}' for l, s in approx.get(_norm_slug(slug), [])]
                if not cand:
                    # 退一步：词元子集/超集匹配（soft-phonon-mode ⊃ soft-mode）
                    toks = _slug_tokens(slug)
                    if len(toks) >= 2:
                        for (l2, s2_l), actual2 in real.items():
                            t2 = _slug_tokens(actual2)
                            if len(t2) >= 2 and (toks <= t2 or t2 <= toks):
                                cand.append(f'{l2}/{actual2}')
                        cand = cand[:4]
                if cand:
                    res['dangling_near_miss'].append((citekey, f'{layer}/{slug}', ' | '.join(cand)))
                else:
                    res['dangling_unknown'].append((citekey, f'{layer}/{slug}'))

    for key, cites in body.items():
        for citekey in cites:
            if citekey not in declared_map.get(key, set()):
                res['not_declared'].append((citekey, f'{key[0]}/{real[key]}'))
    return res


# ---------------------------------------------------------------------------
# 无据引文扫描：页面声明了某篇论文，但该论文的 raw/note 通篇没提这个页面主题。
# 起因是实测到两类真实错误：
#   1) gajdos2006 被列为 WIEN2k 的使用者，实则文中 "Wien" 全来自作者单位地址（维也纳）；
#   2) FePS3 / NiPS3 页各列 3 篇论文并配了具体贡献句，而三篇原始笔记均未提及该材料。
# 只对「语言无关」的页名生效（含数字或化学式型），因为纯英文词组页名常在中文笔记里
# 以译名出现（飞秒激光、金纳米颗粒…），字面零命中并不代表无据。
# ---------------------------------------------------------------------------
SUBDIGIT = str.maketrans('₀₁₂₃₄₅₆₇₈₉',
                         '0123456789')
AFFIL_RE = re.compile(
    r'University|Universit|Department|Institute|Institut|Academy|Laborator|Laboratoire'
    r'|作者单位|参考文献|REFERENCES|致谢|Acknowledg|E-?mail|Corresponding author'
    r'|^\s*>?\s*\[?\d{1,3}[\].]\s', re.I)


def _flatten(s):
    return re.sub(r'[\s\-_–—:()]+', '', s.translate(SUBDIGIT)).lower()


def _language_independent(slug):
    return bool(re.search(r'\d', slug)) or bool(
        re.match(r'^[A-Z][A-Za-z]*\d*([A-Z][a-z]?\d*)+$', slug))


def unsourced_scan(root=None):
    root = Path(root or REPO)
    zero, affil_only, skipped = [], [], 0
    for sub in ('concepts', 'entities'):
        for f in sorted((root / 'wiki' / sub).glob('*.md')):
            text = f.read_text(encoding='utf-8', errors='replace')
            fm = FM_RE.match(text)
            if not fm:
                continue
            block = fm.group(1)
            keys = fm_list_field(block, 'papers')
            if not keys:
                continue
            if not _language_independent(f.stem):
                skipped += 1
                continue
            names = {f.stem} | set(fm_list_field(block, 'aliases'))
            m = re.search(r'^title:\s*(.+)$', block, re.M)
            if m:
                names.add(m.group(1).strip())
            flat = {_flatten(n) for n in names}
            flat = {n for n in flat if len(n) >= 3}
            if not flat:
                skipped += 1
                continue
            total = affil = present = 0
            for key in keys:
                note = root / 'raw' / 'note' / f'{key}.md'
                if not note.exists():
                    continue
                present += 1
                for line in note.read_text(encoding='utf-8', errors='replace').splitlines():
                    if any(n in _flatten(line) for n in flat):
                        total += 1
                        if AFFIL_RE.search(line):
                            affil += 1
            if not present:
                continue
            rel = f.relative_to(root).as_posix()
            if total == 0:
                zero.append((rel, keys))
            elif affil == total:
                affil_only.append((rel, keys, total))
    return {'zero': zero, 'affil_only': affil_only, 'skipped_language_dependent': skipped}

def main():
    ap = argparse.ArgumentParser(description='只读审计 wiki/concepts 与 wiki/entities 页面')
    ap.add_argument('--summary', action='store_true', help='输出汇总统计')
    ap.add_argument('--json', metavar='PATH', help='输出完整 JSON 到指定路径')
    ap.add_argument('--paths', nargs='+', metavar='FILE', help='只审计指定页面（相对仓库根）')
    ap.add_argument('--strict', action='store_true', help='严格模式：存在错误时退出码非 0')
    ap.add_argument('--papers-xref', action='store_true',
                    help='只做 papers 层与 concepts/entities 层的双向一致性核查并退出')
    ap.add_argument('--unsourced', action='store_true',
                    help='扫描无据引文：页面声明的论文其 raw/note 通篇未提该页主题')
    args = ap.parse_args()

    if args.unsourced:
        res = unsourced_scan()
        print('===== 无据引文扫描（仅语言无关页名）=====')
        print(f"跳过（页名为英文词组，中文笔记里多以译名出现，字面比对不可靠）: "
              f"{res['skipped_language_dependent']}")
        print(f"零命中（声明的论文全都没提这个主题）: {len(res['zero'])}"
              '  ← 必须逐条人工核；化学式/相名的上下标、撇号、译名写法都会造成假阳性')
        for rel, keys in res['zero']:
            print(f'  {rel}  <- {", ".join(keys)}')
        print(f"仅出现在单位/参考文献行（疑似把地名、软件名、被引文献当成使用证据）: "
              f"{len(res['affil_only'])}")
        for rel, keys, n in res['affil_only']:
            print(f'  {rel}  命中{n}  <- {", ".join(keys)}')
        return 0

    if args.papers_xref:
        res = papers_xref(None)
        print('===== papers ↔ concepts/entities 双向一致性 =====')
        print(f"扫描卡片: {res['cards']}")
        print(f"dangling·层写错（页在另一层）: {len(res['dangling_layer_swap'])}")
        print(f"dangling·近似同名（疑似别名/改名残留）: {len(res['dangling_near_miss'])}")
        print(f"dangling·查无此页: {len(res['dangling_unknown'])}")
        print(f"not_cited（卡片声明了该页、页内却没引这篇）: {len(res['not_cited'])}")
        print(f"not_declared（页内引了这篇、卡片却没声明该页；信息项，不计错误）: {len(res['not_declared'])}")
        for name in ('dangling_layer_swap', 'dangling_near_miss', 'dangling_unknown', 'not_cited'):
            if not res[name]:
                continue
            print(f'--- {name}（最多列 30 条）---')
            for row in res[name][:30]:
                print('  ' + ' -> '.join(row))
        if args.json:
            jpath = Path(args.json)
            jpath.parent.mkdir(parents=True, exist_ok=True)
            jpath.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f'JSON 已写入: {jpath}')
        if args.strict and (res['dangling_layer_swap'] or res['dangling_near_miss']
                            or res['dangling_unknown'] or res['not_cited']):
            sys.exit(1)
        return

    # 收集全库 .md（用于入链索引与断链判断）
    all_md_files = [p for p in REPO.rglob('*.md') if '.git' not in p.parts]
    all_slugs = {
        'concepts': {p.stem for p in CONCEPTS.glob('*.md')},
        'entities': {p.stem for p in ENTITIES.glob('*.md')},
    }
    incoming = build_incoming_index(all_md_files)

    # 确定扫描目标
    if args.paths:
        targets = []
        for rel in args.paths:
            p = (REPO / rel).resolve()
            if p.exists():
                targets.append(p)
            else:
                print(f'WARN: 路径不存在，跳过: {rel}', file=sys.stderr)
    else:
        targets = sorted(list(CONCEPTS.glob('*.md')) + list(ENTITIES.glob('*.md')))

    records = [scan_page(p, all_slugs, all_md_files, incoming) for p in targets]

    # 汇总
    total = len(records)
    n_concepts = sum(1 for r in records if r['layer'] == 'concepts')
    n_entities = sum(1 for r in records if r['layer'] == 'entities')
    n_no_fm = sum(1 for r in records if not r['has_frontmatter'])
    n_no_status = sum(1 for r in records if r['has_frontmatter'] and not r['status'])
    n_no_tainai = sum(1 for r in records if not r['has_tainai'])
    n_no_relpaper = sum(1 for r in records if not r['has_relpaper'])
    n_broken = sum(len(r['broken_links']) for r in records)
    n_raw = sum(len(r['raw_links']) for r in records)
    n_missing_img = sum(len(r['missing_images']) for r in records)
    n_collision = sum(1 for r in records if r['cross_layer_collision'])
    n_fm_noise = sum(1 for r in records if r['fm_noise_keys'])
    n_no_contrib_pages = sum(1 for r in records if r['relpaper_missing_contrib'])
    n_no_contrib_items = sum(r['relpaper_missing_contrib'] for r in records)
    n_weak_pages = sum(1 for r in records if r['relpaper_weak_contrib'])
    n_weak_items = sum(r['relpaper_weak_contrib'] for r in records)
    defect_kinds = {}
    for r in records:
        for k, v in (r.get('relpaper_contrib_defects') or {}).items():
            defect_kinds[k] = defect_kinds.get(k, 0) + v
    n_ph_tainai = sum(1 for r in records if r['tainai_placeholder'])
    n_ph_contrib_pages = sum(1 for r in records if r['relpaper_placeholder_contrib'])
    n_ph_contrib_items = sum(r['relpaper_placeholder_contrib'] for r in records)

    status_dist = {}
    for r in records:
        if r['has_frontmatter'] and r['status']:
            status_dist[r['status']] = status_dist.get(r['status'], 0) + 1
    identity_dist = {}
    for r in records:
        identity_dist[r['identity']] = identity_dist.get(r['identity'], 0) + 1

    summary = {
        'total': total,
        'concepts': n_concepts,
        'entities': n_entities,
        'no_frontmatter': n_no_fm,
        'no_status': n_no_status,
        'no_tainai': n_no_tainai,
        'no_relpaper_section': n_no_relpaper,
        'broken_links': n_broken,
        'raw_links': n_raw,
        'missing_images': n_missing_img,
        'cross_layer_collision_pages': n_collision,
        'fm_watermark_noise_pages': n_fm_noise,
        'relpaper_no_contrib_pages': n_no_contrib_pages,
        'relpaper_no_contrib_items': n_no_contrib_items,
        'relpaper_weak_contrib_pages': n_weak_pages,
        'relpaper_weak_contrib_items': n_weak_items,
        'relpaper_contrib_defect_kinds': defect_kinds,
        'placeholder_tainai_pages': n_ph_tainai,
        'relpaper_placeholder_contrib_pages': n_ph_contrib_pages,
        'relpaper_placeholder_contrib_items': n_ph_contrib_items,
        'status_dist': status_dist,
        'identity_dist': identity_dist,
    }

    if args.json:
        out = {'summary': summary, 'pages': records}
        jpath = Path(args.json)
        jpath.parent.mkdir(parents=True, exist_ok=True)
        jpath.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'JSON 已写入: {jpath}')

    if args.summary or not (args.json or args.paths):
        print('===== 审计汇总 =====')
        for k, v in summary.items():
            print(f'{k}: {v}')
        if n_fm_noise:
            print('===== frontmatter 水印噪音页 =====')
            for r in records:
                if r['fm_noise_keys']:
                    print(f"  {r['path']}: {', '.join(r['fm_noise_keys'])}")
        print('===== 身份分布 =====')
        for k, v in sorted(identity_dist.items()):
            print(f'  {k}: {v}')
        print('===== status 分布 =====')
        for k, v in sorted(status_dist.items()):
            print(f'  {k}: {v}')

    if args.strict:
        errs = n_broken + n_raw + n_missing_img + n_no_fm + n_no_status + n_fm_noise
        if errs > 0:
            print(f'STRICT: 发现 {errs} 个错误项', file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
