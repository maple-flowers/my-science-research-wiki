# -*- coding: utf-8 -*-
"""完整解析「新概念/实体建议」章节：提取每行内所有反引号 slug（含同行多实体），输出原始章节供核对。"""
import re, json
from pathlib import Path
from collections import defaultdict

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

def scan_dir(d, typ):
    pages = {}
    for p in sorted(d.glob('*.md')):
        slug = p.stem
        fm, _ = split_fm(read(p))
        formal = fm is not None and re.search(rf'^type:\s*{typ}\s*$', fm, re.MULTILINE) is not None
        key = slug.lower()
        if key not in pages or (formal and not pages[key]['formal']):
            pages[key] = {'slug': slug, 'formal': formal, 'path': str(p)}
    return pages

concept_pages = scan_dir(CONCEPTS_DIR, 'concept')
entity_pages = scan_dir(ENTITIES_DIR, 'entity')

# 解析建议章节：每行提取所有反引号 slug
suggestions = []
raw_sections = {}
for p in sorted(PAPERS_DIR.glob('*.md')):
    citekey = p.stem
    text = read(p)
    fm, body = split_fm(text)
    if fm is None:
        continue
    m = re.search(r'^##\s*🆕\s*新概念/实体建议[^\n]*\n(.*?)(?=^## |\Z)', body, re.MULTILINE | re.DOTALL)
    if not m:
        continue
    sec = m.group(1)
    raw_sections[citekey] = sec.strip()
    for line in sec.splitlines():
        line = line.strip()
        if not line.startswith('-'):
            continue
        # 判断类型前缀
        typ = None
        rest = line[1:].strip()
        if rest.startswith('概念'):
            typ = 'concepts'
            rest = rest[2:].lstrip('：: ')
        elif rest.startswith('实体'):
            typ = 'entities'
            rest = rest[2:].lstrip('：: ')
        if typ is None:
            continue
        # 提取行内所有反引号 slug
        slugs = re.findall(r'`([^`]+)`', rest)
        for raw_slug in slugs:
            slug = raw_slug.strip()
            if not slug:
                continue
            # 去掉 .md 后缀
            if slug.endswith('.md'):
                slug = slug[:-3]
            # 去掉可能的显示名（如 `slug|显示名`）
            slug = slug.split('|')[0].strip()
            suggestions.append({'citekey': citekey, 'type': typ, 'slug': slug, 'raw': raw_slug, 'line': line[:80]})

print(f"完整解析条目总数: {len(suggestions)}")

# 分类
cat = {'A': [], 'B': [], 'C': [], 'D': []}
for s in suggestions:
    pages = concept_pages if s['type'] == 'concepts' else entity_pages
    key = s['slug'].lower()
    if key in pages:
        pg = pages[key]
        pfile = PAPERS_DIR / f"{s['citekey']}.md"
        t = read(pfile)
        linked = f'[[../{s["type"]}/{pg["slug"]}]]' in t or f'[[../{s["type"]}/{pg["slug"]}|' in t
        if pg['formal']:
            cat['A' if linked else 'B'].append({**s, 'actual_slug': pg['slug']})
        else:
            cat['C'].append({**s, 'actual_slug': pg['slug']})
    else:
        cat['D'].append(s)

for k in ['A', 'B', 'C', 'D']:
    print(f"  {k}: {len(cat[k])}")

print("\n=== B（正式页未链接）===")
for s in cat['B']:
    print(f"  {s['citekey']} [{s['type']}] {s['slug']} -> {s['actual_slug']}")

print("\n=== C（中间产物页未链接）===")
for s in cat['C']:
    print(f"  {s['citekey']} [{s['type']}] {s['slug']} -> {s['actual_slug']}")

print("\n=== D（需新建）===")
for s in cat['D']:
    print(f"  {s['citekey']} [{s['type']}] {s['slug']}")

# 保存
(OUT / 'suggestions_full.json').write_text(json.dumps({'cat': {k: v for k, v in cat.items()}, 'raw_sections': raw_sections}, ensure_ascii=False, indent=2), encoding='utf-8')
print("\n已保存 suggestions_full.json")
