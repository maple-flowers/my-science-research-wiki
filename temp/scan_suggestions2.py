# -*- coding: utf-8 -*-
"""修正 D 类：去掉 .md 后缀、大小写归一化后重新比对，输出最终分类清单。"""
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

# 重新解析建议条目（含 .md 后缀处理）
suggestions = []
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
    for line in sec.splitlines():
        line = line.strip()
        mm = re.match(r'^-\s*(概念|实体)\s*`([^`]+)`\s*[:：]?\s*(.*)$', line)
        if mm:
            typ = 'concepts' if mm.group(1) == '概念' else 'entities'
            raw_slug = mm.group(2).strip()
            slug = raw_slug[:-3] if raw_slug.endswith('.md') else raw_slug
            desc = mm.group(3).strip()
            suggestions.append({'citekey': citekey, 'type': typ, 'slug': slug, 'raw': raw_slug, 'desc': desc})

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

print(f"总条目: {len(suggestions)}")
for k in ['A', 'B', 'C', 'D']:
    print(f"  {k}: {len(cat[k])}")

print("\n=== B（已有正式页但正文未链接）===")
for s in cat['B']:
    print(f"  {s['citekey']} [{s['type']}] {s['slug']} -> {s['actual_slug']}")

print("\n=== C（已有中间产物页但正文未链接）===")
for s in cat['C']:
    print(f"  {s['citekey']} [{s['type']}] {s['slug']} -> {s['actual_slug']}")

print("\n=== D（无对应页面，需新建）===")
for s in cat['D']:
    print(f"  {s['citekey']} [{s['type']}] {s['slug']} | {s['desc'][:50]}")

(OUT / 'suggestions_final.json').write_text(json.dumps({'cat': {k: v for k, v in cat.items()}}, ensure_ascii=False, indent=2), encoding='utf-8')
