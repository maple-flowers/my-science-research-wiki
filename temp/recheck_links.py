# -*- coding: utf-8 -*-
"""修复后复检：重新计算正向/反向缺失，应归零。"""
import re, json
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
PAPERS_DIR = REPO / 'wiki' / 'papers'
CONCEPTS_DIR = REPO / 'wiki' / 'concepts'
ENTITIES_DIR = REPO / 'wiki' / 'entities'

FM_RE = re.compile(r'^---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)', re.DOTALL)

def read(p):
    return p.read_text(encoding='utf-8', errors='replace')

def split_fm(text):
    m = FM_RE.match(text)
    return (m.group(1), text[m.end():]) if m else (None, text)

def parse_list_field(fm, key):
    """解析行内或行内跨行列表字段。"""
    if fm is None:
        return []
    result = []
    m = re.search(rf'^{key}:\s*\[(.*?)\]\s*$', fm, re.MULTILINE)
    if m:
        for s in m.group(1).split(','):
            s = s.strip().strip('"\'').strip()
            if s:
                result.append(s)
        return result
    m = re.search(rf'^{key}:\s*\n((?:[ \t]+-\s+.*\n?)+)', fm, re.MULTILINE)
    if m:
        for line in m.group(1).splitlines():
            line = line.strip()
            if line.startswith('-'):
                result.append(line[1:].strip().strip('"\''))
    return result

def extract_wikilinks(text):
    return re.findall(r'(?<!\!)\[\[([^\]]+)\]\]', text)

def classify(target):
    for typ, prefix in [('concepts', '../concepts/'), ('entities', '../entities/')]:
        if target.startswith(prefix):
            slug = target[len(prefix):].split('|')[0].split('#')[0].strip()
            if slug and not slug.startswith('/'):
                return typ, slug
    return None, None

def scan_dir(d, typ):
    pages = {}
    for p in sorted(d.glob('*.md')):
        slug = p.stem
        fm, _ = split_fm(read(p))
        formal = fm is not None and re.search(rf'^type:\s*{typ}\s*$', fm, re.MULTILINE) is not None
        key = slug.lower()
        if key not in pages or (formal and not pages[key]['formal']):
            pages[key] = {'slug': slug, 'formal': formal, 'papers': set(parse_list_field(fm, 'papers'))}
    return pages

concept_pages = scan_dir(CONCEPTS_DIR, 'concept')
entity_pages = scan_dir(ENTITIES_DIR, 'entity')

forward_missing = []
backward_missing = []
n_papers = 0
for p in sorted(PAPERS_DIR.glob('*.md')):
    citekey = p.stem
    text = read(p)
    fm, body = split_fm(text)
    if fm is None:
        continue
    n_papers += 1
    declared = {'concepts': parse_list_field(fm, 'concepts'), 'entities': parse_list_field(fm, 'entities')}
    linked = {'concepts': [], 'entities': []}
    for t in extract_wikilinks(body):
        typ, slug = classify(t)
        if typ in ('concepts', 'entities'):
            linked[typ].append(slug)
    linked_lower = {'concepts': {s.lower() for s in linked['concepts']}, 'entities': {s.lower() for s in linked['entities']}}
    for typ in ('concepts', 'entities'):
        pages = concept_pages if typ == 'concepts' else entity_pages
        ref_slugs = set(declared[typ]) | set(linked[typ])
        for slug in ref_slugs:
            key = slug.lower()
            if key not in pages:
                continue
            pg = pages[key]
            if not pg['formal']:
                continue
            if slug in declared[typ] and key not in linked_lower[typ]:
                forward_missing.append({'citekey': citekey, 'type': typ, 'slug': slug})
            if citekey not in pg['papers'] and citekey.lower() not in {x.lower() for x in pg['papers']}:
                backward_missing.append({'citekey': citekey, 'type': typ, 'slug': slug})

print(f"papers: {n_papers}")
print(f"正向缺失（frontmatter 声明但正文未链接）: {len(forward_missing)}")
print(f"反向缺失（正文/声明引用正式页但该页 papers 缺 citekey）: {len(backward_missing)}")
if backward_missing:
    for x in backward_missing[:20]:
        print("  ", x)
