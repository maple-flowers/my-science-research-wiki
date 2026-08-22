# -*- coding: utf-8 -*-
"""扫描 wiki/papers 下所有 .md 的正文长度与 H2 章节，识别内容异常（正文过短/缺描述章节）。只读。"""
import re
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
PAPERS = REPO / 'wiki' / 'papers'

FM_RE = re.compile(r'^---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)', re.DOTALL)

def read(p):
    return p.read_text(encoding='utf-8', errors='replace')

rows = []
for p in sorted(PAPERS.glob('*.md')):
    t = read(p)
    m = FM_RE.match(t)
    if m:
        body = t[m.end():]
    else:
        body = t
    # 正文长度（去掉空白）
    body_stripped = body.strip()
    body_chars = len(body_stripped)
    # H2 章节标题
    h2 = re.findall(r'^##\s+([^\n]+)$', body, re.MULTILINE)
    h2_names = [x.strip() for x in h2]
    rows.append({
        'citekey': p.stem,
        'file_size': p.stat().st_size,
        'body_chars': body_chars,
        'h2_count': len(h2),
        'h2_names': h2_names,
    })

# 排序：按 body_chars 升序
rows.sort(key=lambda x: x['body_chars'])

print(f"总论文数: {len(rows)}")
print("\n=== 正文最短的 40 篇 ===")
for r in rows[:40]:
    print(f"  {r['citekey']}: body={r['body_chars']} chars, size={r['file_size']}B, H2={r['h2_count']} {r['h2_names'][:3]}")

print("\n=== 正文长度分布 ===")
buckets = {'0': 0, '1-500': 0, '501-2000': 0, '2001-5000': 0, '5001-10000': 0, '10000+': 0}
for r in rows:
    c = r['body_chars']
    if c == 0: buckets['0'] += 1
    elif c <= 500: buckets['1-500'] += 1
    elif c <= 2000: buckets['501-2000'] += 1
    elif c <= 5000: buckets['2001-5000'] += 1
    elif c <= 10000: buckets['5001-10000'] += 1
    else: buckets['10000+'] += 1
for k, v in buckets.items():
    print(f"  {k}: {v}")
