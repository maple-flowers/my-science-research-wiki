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

--strict 时对 status 非法值、raw/note 直链、断链、缺失图片等按错误计数并置非零退出码。
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
SEC_REL = re.compile(r'^##\s*.*关联概念与实体', re.M)
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

    # 正文 paper links
    rec['papers_body'] = sorted(set(PAPER_LINK.findall(body)))

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
        if target not in all_slugs.get('concepts', set()):
            rec['broken_links'].append(f'concepts/{target}')
    for target in ENTITY_LINK.findall(body):
        if target not in all_slugs.get('entities', set()):
            rec['broken_links'].append(f'entities/{target}')

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

    return rec


def build_incoming_index(all_md_files):
    """扫描全库 .md，建立 目标路径 -> [来源路径] 反链索引。"""
    incoming = {}
    for src in all_md_files:
        try:
            text = src.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        src_rel = src.relative_to(REPO).as_posix()
        for target in WIKILINK.findall(text):
            target = target.strip()
            # 归一化：../concepts/x、concepts/x、x
            t = target
            if t.startswith('../'):
                t = t[3:]
            # 去掉可能的 .md
            if t.endswith('.md'):
                t = t[:-3]
            # 只统计指向 concepts/entities 页面的链接
            if t.startswith('concepts/') or t.startswith('entities/'):
                incoming.setdefault(t, []).append(src_rel)
    return incoming


def main():
    ap = argparse.ArgumentParser(description='只读审计 wiki/concepts 与 wiki/entities 页面')
    ap.add_argument('--summary', action='store_true', help='输出汇总统计')
    ap.add_argument('--json', metavar='PATH', help='输出完整 JSON 到指定路径')
    ap.add_argument('--paths', nargs='+', metavar='FILE', help='只审计指定页面（相对仓库根）')
    ap.add_argument('--strict', action='store_true', help='严格模式：存在错误时退出码非 0')
    args = ap.parse_args()

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
        print('===== 身份分布 =====')
        for k, v in sorted(identity_dist.items()):
            print(f'  {k}: {v}')
        print('===== status 分布 =====')
        for k, v in sorted(status_dist.items()):
            print(f'  {k}: {v}')

    if args.strict:
        errs = n_broken + n_raw + n_missing_img + n_no_fm + n_no_status
        if errs > 0:
            print(f'STRICT: 发现 {errs} 个错误项', file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
