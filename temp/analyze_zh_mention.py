# -*- coding: utf-8 -*-
"""扫描 papers 正文是否以中文名提及正式页概念/实体但未建立双链。只读分析。"""
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
    return re.findall(r'(?<!\!)\[\[([^\]]+)\]\]', text)

def classify_wikilink(target):
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

def chinese_part(title):
    """提取 title 的中文部分（取 '/' 前的部分，过滤非中文）。"""
    if not title:
        return ''
    left = title.split('/')[0].strip()
    # 提取连续中文片段
    m = re.search(r'[\u4e00-\u9fff][\u4e00-\u9fff\s()（）0-9A-Za-z₀-₉₂₃]*', left)
    return m.group(0).strip() if m else ''

# 构建正式页名称映射
formal_names = []  # (typ, actual_slug, title, zh_part)
for pages, typ in [(concept_pages, 'concepts'), (entity_pages, 'entities')]:
    for key, pg in pages.items():
        if pg['formal']:
            zh = chinese_part(pg['title'])
            formal_names.append((typ, pg['slug'], pg['title'], zh))

# 过滤：中文部分至少 2 个汉字，且不是过短常见词
def valid_zh(zh):
    han = re.findall(r'[\u4e00-\u9fff]', zh)
    return len(han) >= 2

formal_names = [x for x in formal_names if valid_zh(x[3])]

print(f"正式页中文名特征数: {len(formal_names)}")

# 扫描 papers 正文
mention_missing = []
for p in sorted(PAPERS_DIR.glob('*.md')):
    citekey = p.stem
    text = read_utf8(p)
    fm, body = split_frontmatter(text)
    if fm is None:
        continue
    # 已链接
    linked = {'concepts': set(), 'entities': set()}
    for t in extract_wikilinks(body):
        typ, slug = classify_wikilink(t)
        if typ in ('concepts', 'entities'):
            linked[typ].add(slug.lower())
    for typ, slug, title, zh in formal_names:
        if zh in linked[typ] and False:
            pass
        if slug.lower() in linked[typ]:
            continue  # 已链接
        # 正文中是否出现中文名（排除 wikilink 内部）
        # 简单：直接搜索 body
        cnt = body.count(zh)
        if cnt > 0:
            mention_missing.append({
                'citekey': citekey, 'type': typ, 'slug': slug,
                'zh': zh, 'title': title, 'count': cnt,
            })

# 去重
seen = set()
deduped = []
for x in mention_missing:
    k = (x['citekey'], x['type'], x['slug'].lower())
    if k not in seen:
        seen.add(k)
        deduped.append(x)
mention_missing = deduped

print(f"中文名提及但未链接候选: {len(mention_missing)}")
from collections import Counter
print("分布:", dict(Counter(x['type'] for x in mention_missing)))

out_path = OUT / 'zh_mention_missing.json'
out_path.write_text(json.dumps(mention_missing, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"已写入: {out_path}")

print("\n=== 候选示例（前 60）===")
for x in mention_missing[:60]:
    print(f"  {x['citekey']} [{x['type']}] `{x['zh']}` -> {x['slug']} (出现 {x['count']} 次)")
