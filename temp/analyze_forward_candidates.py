# -*- coding: utf-8 -*-
"""扫描 papers 正文「新概念/实体建议」及反引号 slug，识别已建成正式页但未建立双链的正向缺失。"""
import re, json
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

def parse_scalar_field(fm, key):
    m = re.search(rf'^{key}:\s*(.+?)\s*$', fm, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"\'').strip()
    return ''

def extract_wikilinks(text):
    links = []
    for m in re.finditer(r'(?<!\!)\[\[([^\]]+)\]\]', text):
        links.append(m.group(1))
    return links

def classify_wikilink(target):
    for typ, prefix in [('concepts', '../concepts/'), ('entities', '../entities/'), ('papers', '../papers/')]:
        if target.startswith(prefix):
            slug = target[len(prefix):].split('|')[0].split('#')[0].strip()
            if slug and not slug.startswith('/'):
                return typ, slug
    return None, None

# 扫描 concepts/entities 正式页映射
def scan_dir(d, typ):
    pages = {}
    for p in sorted(d.glob('*.md')):
        slug = p.stem
        text = read_utf8(p)
        fm, _b = split_frontmatter(text)
        formal = False
        title = ''
        if fm is not None:
            t = parse_scalar_field(fm, 'type')
            if t == typ:
                formal = True
                title = parse_scalar_field(fm, 'title')
        key = slug.lower()
        if key not in pages or (formal and not pages[key]['formal']):
            pages[key] = {'slug': slug, 'formal': formal, 'title': title, 'path': str(p)}
    return pages

concept_pages = scan_dir(CONCEPTS_DIR, 'concept')
entity_pages = scan_dir(ENTITIES_DIR, 'entity')

# 扫描 papers 正文反引号 slug
backtick_pat = re.compile(r'[-\s](?:概念|实体|图表|项目)\s*`([^`]+)`')

forward_candidates = []  # 反引号 slug 已建成正式页但正文无双链
seen_backtick = set()

for p in sorted(PAPERS_DIR.glob('*.md')):
    citekey = p.stem
    text = read_utf8(p)
    fm, body = split_frontmatter(text)
    if fm is None:
        continue
    # 正文所有 wikilink 已链接的 slug
    linked = {'concepts': set(), 'entities': set()}
    for t in extract_wikilinks(body):
        typ, slug = classify_wikilink(t)
        if typ in ('concepts', 'entities'):
            linked[typ].add(slug.lower())
    # 提取反引号条目
    for m in backtick_pat.finditer(body):
        kind = m.group(0).strip().split()[0]  # 概念/实体/图表/项目
        slug = m.group(1).strip()
        if kind not in ('概念', '实体'):
            continue
        typ = 'concepts' if kind == '概念' else 'entities'
        pages = concept_pages if typ == 'concepts' else entity_pages
        key = slug.lower()
        if key not in pages:
            continue
        page = pages[key]
        if not page['formal']:
            continue  # 中间产物保持原样
        # 正文是否已链接？
        if key in linked[typ]:
            continue
        pair = (citekey, typ, key)
        if pair in seen_backtick:
            continue
        seen_backtick.add(pair)
        forward_candidates.append({
            'citekey': citekey, 'type': typ,
            'backtick_slug': slug, 'actual_slug': page['slug'],
            'label': page['title'],
        })

print(f"正向缺失候选（反引号 slug 已建成正式页但正文未链接）: {len(forward_candidates)}")
from collections import Counter
print("分布:", dict(Counter(x['type'] for x in forward_candidates)))

# 保存
out_path = OUT / 'forward_candidates.json'
out_path.write_text(json.dumps(forward_candidates, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"已写入: {out_path}")

print("\n=== 候选示例（前 50）===")
for x in forward_candidates[:50]:
    print(f"  {x['citekey']} [{x['type']}] `{x['backtick_slug']}` -> {x['actual_slug']} 标签 {x['label'][:40]!r}")
