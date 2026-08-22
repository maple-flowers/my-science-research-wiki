# -*- coding: utf-8 -*-
"""扫描 papers 与 concepts/entities 的双向链接现状，输出缺失清单。只读分析，不修改任何文件。"""
import os, re, json
from pathlib import Path

REPO = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
PAPERS_DIR = Path(REPO) / "wiki" / "papers"
CONCEPTS_DIR = Path(REPO) / "wiki" / "concepts"
ENTITIES_DIR = Path(REPO) / "wiki" / "entities"
OUT = Path(r"C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp")

FM_RE = re.compile(r'^---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)', re.DOTALL)

def read_utf8(p):
    return p.read_text(encoding='utf-8', errors='replace')

def split_frontmatter(text):
    m = FM_RE.match(text)
    if m:
        return m.group(1), text[m.end():]
    return None, text

def parse_inline_list(s):
    items = []
    for part in s.split(','):
        part = part.strip().strip('"').strip("'").strip()
        if part:
            items.append(part)
    return items

def parse_list_field(fm, key):
    """解析 frontmatter 列表字段（行内 [a,b] 或多行 - item）。"""
    result = []
    m = re.search(rf'^{key}:\s*\[(.*?)\]\s*$', fm, re.MULTILINE)
    if m:
        result = parse_inline_list(m.group(1))
        return result
    m = re.search(rf'^{key}:\s*\n((?:[ \t]+-\s+.*\n?)+)', fm, re.MULTILINE)
    if m:
        for line in m.group(1).splitlines():
            line = line.strip()
            if line.startswith('-'):
                result.append(line[1:].strip().strip('"\''))
    return result

def parse_scalar_field(fm, key):
    m = re.search(rf'^{key}:\s*(.+?)\s*$', fm, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"\'').strip()
    return ''

def extract_wikilinks(text):
    """提取所有 [[...]]，排除 ![[。返回 target 列表（未剥离 | 和 #）。"""
    links = []
    for m in re.finditer(r'(?<!\!)\[\[([^\]]+)\]\]', text):
        links.append(m.group(1))
    return links

def classify_wikilink(target):
    """返回 (type, slug) 或 (None, None)。type: concept/entity/paper/other"""
    for typ, prefix in [('concepts', '../concepts/'), ('entities', '../entities/'), ('papers', '../papers/')]:
        if target.startswith(prefix):
            slug = target[len(prefix):].split('|')[0].split('#')[0].strip()
            if slug and not slug.startswith('/'):
                return typ, slug
    return None, None

# ---- 扫描 papers ----
papers = {}
for p in sorted(PAPERS_DIR.glob('*.md')):
    citekey = p.stem
    text = read_utf8(p)
    fm, body = split_frontmatter(text)
    if fm is None:
        print(f"[WARN] 无 frontmatter: {p.name}")
        continue
    declared = {
        'concepts': set(parse_list_field(fm, 'concepts')),
        'entities': set(parse_list_field(fm, 'entities')),
    }
    linked = {'concepts': set(), 'entities': set()}
    for t in extract_wikilinks(body):
        typ, slug = classify_wikilink(t)
        if typ in ('concepts', 'entities'):
            linked[typ].add(slug)
    papers[citekey] = {'declared': declared, 'linked': linked, 'path': str(p)}

# ---- 扫描 concepts/entities ----
def scan_dir(d, typ):
    pages = {}
    for p in sorted(d.glob('*.md')):
        slug = p.stem
        text = read_utf8(p)
        fm, _body = split_frontmatter(text)
        formal = False
        papers_field = set()
        title = ''
        if fm is not None:
            t = parse_scalar_field(fm, 'type')
            if t == typ:
                formal = True
                papers_field = set(parse_list_field(fm, 'papers'))
                title = parse_scalar_field(fm, 'title')
        key = slug.lower()
        if key not in pages or (formal and not pages[key]['formal']):
            pages[key] = {'slug': slug, 'formal': formal, 'papers': papers_field, 'title': title, 'path': str(p)}
    return pages

concept_pages = scan_dir(CONCEPTS_DIR, 'concept')
entity_pages = scan_dir(ENTITIES_DIR, 'entity')

# ---- 计算缺失 ----
forward_missing = []   # paper 声明正式页 slug 但正文未链接
backward_missing = []  # paper 引用集合中的正式页，其 papers 字段缺 citekey
declared_nonexistent = []  # 声明 slug 磁盘上既无正式页也无中间产物

for citekey, info in papers.items():
    for typ in ('concepts', 'entities'):
        pages = concept_pages if typ == 'concepts' else entity_pages
        declared = info['declared'][typ]
        linked = info['linked'][typ]
        # 引用集合 = declared ∪ linked
        ref_slugs = set(declared) | set(linked)
        linked_lower = {s.lower() for s in linked}
        for slug in sorted(ref_slugs):
            key = slug.lower()
            if key not in pages:
                if slug in declared:
                    declared_nonexistent.append({'citekey': citekey, 'type': typ, 'slug': slug})
                continue
            page = pages[key]
            if not page['formal']:
                # 中间产物：保持原样，不处理
                continue
            # 正向缺失：声明了正式页但正文没有对应双链
            if slug in declared and key not in linked_lower:
                forward_missing.append({
                    'citekey': citekey, 'type': typ,
                    'declared_slug': slug, 'actual_slug': page['slug'],
                    'label': page['title'],
                })
            # 反向缺失：正式页 papers 缺 citekey
            if citekey not in page['papers']:
                backward_missing.append({
                    'citekey': citekey, 'type': typ,
                    'slug': page['slug'], 'label': page['title'],
                })

# 去重（同一对可能因 declared 与 linked 大小写不同重复）
def dedup(items, keyfn):
    seen = set()
    out = []
    for it in items:
        k = keyfn(it)
        if k not in seen:
            seen.add(k)
            out.append(it)
    return out

forward_missing = dedup(forward_missing, lambda x: (x['citekey'], x['type'], x['actual_slug'].lower()))
backward_missing = dedup(backward_missing, lambda x: (x['citekey'], x['type'], x['slug'].lower()))

# ---- 输出 ----
formal_concept = sum(1 for v in concept_pages.values() if v['formal'])
formal_entity = sum(1 for v in entity_pages.values() if v['formal'])
inter_concept = sum(1 for v in concept_pages.values() if not v['formal'])
inter_entity = sum(1 for v in entity_pages.values() if not v['formal'])

print("=== 双向链接审计统计 ===")
print(f"papers 总数: {len(papers)}")
print(f"concepts 正式页: {formal_concept}，中间产物: {inter_concept}")
print(f"entities 正式页: {formal_entity}，中间产物: {inter_entity}")
print(f"正向缺失（paper 声明正式页但正文未链接）: {len(forward_missing)}")
print(f"反向缺失（正式页 papers 缺 citekey 反链）: {len(backward_missing)}")
print(f"声明 slug 磁盘不存在: {len(declared_nonexistent)}")

# 分布
from collections import Counter
fw_c = Counter(x['type'] for x in forward_missing)
bw_c = Counter(x['type'] for x in backward_missing)
print(f"  正向缺失分布: {dict(fw_c)}")
print(f"  反向缺失分布: {dict(bw_c)}")

result = {
    'forward_missing': forward_missing,
    'backward_missing': backward_missing,
    'declared_nonexistent': declared_nonexistent,
}
out_path = OUT / 'bidirectional_analysis.json'
out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"\n清单已写入: {out_path}")

print("\n=== 正向缺失示例（前 30）===")
for x in forward_missing[:30]:
    print(f"  {x['citekey']} [{x['type']}] 声明 {x['declared_slug']!r} -> 实际 {x['actual_slug']!r} 标签 {x['label'][:40]!r}")

print("\n=== 反向缺失示例（前 30）===")
for x in backward_missing[:30]:
    print(f"  {x['slug']} [{x['type']}] 缺反链 citekey {x['citekey']} 标签 {x['label'][:40]!r}")

print("\n=== 声明 slug 磁盘不存在（前 30）===")
for x in declared_nonexistent[:30]:
    print(f"  {x['citekey']} [{x['type']}] {x['slug']!r}")
