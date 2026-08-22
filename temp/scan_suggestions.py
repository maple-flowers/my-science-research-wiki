# -*- coding: utf-8 -*-
"""扫描 papers 正文「🆕 新概念/实体建议」章节的反引号 slug，与 concepts/entities 现有页面比对分类。
分类：A=已有正式页且正文已链接；B=已有正式页但正文未链接；C=已有中间产物页但正文未链接；D=无对应页面。
只读分析。"""
import re, json
from pathlib import Path
from collections import Counter, defaultdict

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
print(f"concepts: {len(concept_pages)} 页（正式 {sum(1 for v in concept_pages.values() if v['formal'])}）")
print(f"entities: {len(entity_pages)} 页（正式 {sum(1 for v in entity_pages.values() if v['formal'])}）")

# 扫描每篇 paper 的「新概念/实体建议」章节反引号 slug
suggestions = []  # (citekey, type, slug, desc)
for p in sorted(PAPERS_DIR.glob('*.md')):
    citekey = p.stem
    text = read(p)
    fm, body = split_fm(text)
    if fm is None:
        continue
    # 提取「新概念/实体建议」章节
    m = re.search(r'^##\s*🆕\s*新概念/实体建议[^\n]*\n(.*?)(?=^## |\Z)', body, re.MULTILINE | re.DOTALL)
    if not m:
        continue
    sec = m.group(1)
    # 匹配行：  - 概念 `slug`：说明  或   - 实体 `slug`：说明
    for line in sec.splitlines():
        line = line.strip()
        mm = re.match(r'^-\s*(概念|实体)\s*`([^`]+)`\s*[:：]?\s*(.*)$', line)
        if mm:
            typ = 'concepts' if mm.group(1) == '概念' else 'entities'
            slug = mm.group(2).strip()
            desc = mm.group(3).strip()
            suggestions.append({'citekey': citekey, 'type': typ, 'slug': slug, 'desc': desc})

print(f"\n「新概念/实体建议」反引号条目总数: {len(suggestions)}")

# 分类
cat = {'A': [], 'B': [], 'C': [], 'D': []}
for s in suggestions:
    pages = concept_pages if s['type'] == 'concepts' else entity_pages
    key = s['slug'].lower()
    if key in pages:
        pg = pages[key]
        # 检查正文是否已链接该 slug
        pfile = PAPERS_DIR / f"{s['citekey']}.md"
        t = read(pfile)
        linked = f'[[../{s["type"]}/{pg["slug"]}]]' in t or f'[[../{s["type"]}/{pg["slug"]}|' in t
        if pg['formal']:
            cat['A' if linked else 'B'].append({**s, 'actual_slug': pg['slug']})
        else:
            cat['C' if linked else 'C'].append({**s, 'actual_slug': pg['slug']})
    else:
        cat['D'].append(s)

for k in ['A', 'B', 'C', 'D']:
    print(f"  {k}: {len(cat[k])} 条")

# 保存
out = {'suggestions': suggestions, 'cat': {k: v for k, v in cat.items()}}
(OUT / 'suggestions_classified.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')

print("\n=== B（已有正式页但正文未链接）===")
for s in cat['B'][:40]:
    print(f"  {s['citekey']} [{s['type']}] {s['slug']} -> {s['actual_slug']} | {s['desc'][:40]}")
print("\n=== C（已有中间产物页但正文未链接）===")
for s in cat['C'][:40]:
    print(f"  {s['citekey']} [{s['type']}] {s['slug']} -> {s['actual_slug']} | {s['desc'][:40]}")
print("\n=== D（无对应页面，需新建）===")
for s in cat['D'][:60]:
    print(f"  {s['citekey']} [{s['type']}] {s['slug']} | {s['desc'][:40]}")
