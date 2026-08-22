# -*- coding: utf-8 -*-
"""全面扫描 papers 正文「提到但未链接」的概念/实体（含正式页与中间产物页）。
特征：中文名（>=3 汉字）+ 英文名（>=2 词）+ slug 空格变体。排除 wikilink 内部。只读分析。"""
import re, json
from pathlib import Path
from collections import Counter

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
PAPERS_DIR = REPO / 'wiki' / 'papers'
CONCEPTS_DIR = REPO / 'wiki' / 'concepts'
ENTITIES_DIR = REPO / 'wiki' / 'entities'
OUT = Path(r"C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp")

FM_RE = re.compile(r'^---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)', re.DOTALL)

def read(p):
    return p.read_text(encoding='utf-8', errors='replace')

def split_fm(text):
    m = FM_RE.match(text)
    return (m.group(1), text[m.end():]) if m else (None, text)

def parse_scalar(fm, key):
    m = re.search(rf'^{key}:\s*(.+?)\s*$', fm, re.MULTILINE)
    return m.group(1).strip().strip('"\'').strip() if m else ''

def extract_zh(title):
    """提取 title 中最长连续中文片段（含括号内中文）。"""
    if not title:
        return ''
    left = title.split('/')[0]
    # 找所有连续中文片段（允许中间夹空格/括号/数字/字母）
    segs = re.findall(r'[\u4e00-\u9fff][\u4e00-\u9fff\s()（）0-9A-Za-z₀-₉₂₃]*', left)
    if not segs:
        return ''
    # 取含汉字最多的片段
    best = max(segs, key=lambda s: len(re.findall(r'[\u4e00-\u9fff]', s)))
    return best.strip()

def extract_en(title):
    """提取 title 中英文名：'/' 后部分或括号内英文。"""
    if not title:
        return ''
    right = title.split('/')[-1] if '/' in title else ''
    # 优先取 '/' 后
    if right:
        m = re.search(r'[A-Za-z][A-Za-z\s\-()]*', right)
        if m:
            return m.group(0).strip()
    # 否则取括号内英文
    m = re.search(r'[（(]([A-Za-z][A-Za-z\s\-()]*)[)）]', title)
    if m:
        return m.group(1).strip()
    return ''

def scan_dir(d, typ):
    pages = {}
    for p in sorted(d.glob('*.md')):
        slug = p.stem
        text = read(p)
        fm, _ = split_fm(text)
        formal = fm is not None and re.search(rf'^type:\s*{typ}\s*$', fm, re.MULTILINE) is not None
        title = parse_scalar(fm, 'title') if fm else ''
        key = slug.lower()
        if key not in pages:
            pages[key] = {'slug': slug, 'formal': formal, 'title': title, 'path': str(p)}
    return pages

concept_pages = scan_dir(CONCEPTS_DIR, 'concept')
entity_pages = scan_dir(ENTITIES_DIR, 'entity')
print(f"concepts 页: {len(concept_pages)}（正式 {sum(1 for v in concept_pages.values() if v['formal'])}）")
print(f"entities 页: {len(entity_pages)}（正式 {sum(1 for v in entity_pages.values() if v['formal'])}）")

# 构建特征集
features = []  # (typ, slug, zh, en, slug_variant)
for pages, typ in [(concept_pages, 'concepts'), (entity_pages, 'entities')]:
    for key, pg in pages.items():
        zh = extract_zh(pg['title'])
        en = extract_en(pg['title'])
        slug_variant = pg['slug'].replace('-', ' ')
        features.append((typ, pg['slug'], zh, en, slug_variant, pg['formal']))

# 过滤：中文名 >=3 汉字；英文名 >=2 词
def zh_ok(zh):
    return len(re.findall(r'[\u4e00-\u9fff]', zh)) >= 3
def en_ok(en):
    words = en.split()
    return len(words) >= 2 and len(en) >= 8

# 统计特征可用性
zh_feats = [f for f in features if zh_ok(f[2])]
en_feats = [f for f in features if en_ok(f[3])]
print(f"中文名特征(>=3字): {len(zh_feats)}，英文名特征(>=2词): {len(en_feats)}")

# 扫描 papers
candidates = []  # (citekey, typ, slug, matched_term, count)
for p in sorted(PAPERS_DIR.glob('*.md')):
    citekey = p.stem
    text = read(p)
    fm, body = split_fm(text)
    if fm is None:
        continue
    # 已链接 slug 集合
    linked = {'concepts': set(), 'entities': set()}
    for m in re.finditer(r'(?<!\!)\[\[([^\]]+)\]\]', body):
        tgt = m.group(1)
        for typ, prefix in [('concepts', '../concepts/'), ('entities', '../entities/')]:
            if tgt.startswith(prefix):
                slug = tgt[len(prefix):].split('|')[0].split('#')[0].strip()
                if slug:
                    linked[typ].add(slug.lower())
    # 屏蔽 wikilink 内部文字
    masked = re.sub(r'(?<!\!)\[\[[^\]]+\]\]', ' [[LINK]] ', body)
    masked_lower = masked.lower()
    for typ, slug, zh, en, sv, formal in features:
        if slug.lower() in linked[typ]:
            continue
        matched = None
        cnt = 0
        if zh_ok(zh):
            c = masked.count(zh)
            if c > 0:
                matched, cnt = zh, c
        if matched is None and en_ok(en):
            c = masked_lower.count(en.lower())
            if c > 0:
                matched, cnt = en, c
        if matched is None:
            # slug 空格变体（如 kohn anomaly）
            c = masked_lower.count(sv.lower())
            if c > 0:
                matched, cnt = sv, c
        if matched is not None:
            candidates.append({'citekey': citekey, 'type': typ, 'slug': slug,
                               'term': matched, 'count': cnt, 'formal': formal})

# 去重（同 citekey+slug 只留一次）
seen = set()
dedup = []
for c in candidates:
    k = (c['citekey'], c['type'], c['slug'].lower())
    if k not in seen:
        seen.add(k)
        dedup.append(c)
candidates = dedup

print(f"\n候选总数: {len(candidates)}")
print("按类型:", dict(Counter(c['type'] for c in candidates)))
print("按正式/中间产物:", dict(Counter('正式' if c['formal'] else '中间产物' for c in candidates)))
print("涉及论文数:", len(set(c['citekey'] for c in candidates)))

# 按 slug 聚合高频
by_slug = Counter((c['type'], c['slug']) for c in candidates)
print("\n高频被提及 slug（前 30）:")
for (t, s), n in by_slug.most_common(30):
    print(f"  {t}/{s}: {n} 篇")

out = OUT / 'mention_candidates.json'
out.write_text(json.dumps(candidates, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"\n已写入: {out}")
