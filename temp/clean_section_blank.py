# -*- coding: utf-8 -*-
"""清理相关论文节内追加条目导致的空行瑕疵：把节内连续空行压缩为单个换行。"""
import re, json
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
TEMP = Path(r"C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp")

d = json.loads((TEMP / 'bidirectional_analysis.json').read_text(encoding='utf-8'))
bw = d['backward_missing']
pages = {}
for x in bw:
    pages.setdefault((x['type'], x['slug']), []).append(x['citekey'])
for x in [
    {'citekey': 'chowdhuryReviewTheoreticalComputational', 'type': 'entities', 'slug': 'TaS2'},
    {'citekey': 'chowdhuryReviewTheoreticalComputational', 'type': 'entities', 'slug': 'TaSe2'},
]:
    pages.setdefault((x['type'], x['slug']), []).append(x['citekey'])

def clean_section(t):
    """把「相关论文」节内容中的连续空行压缩为单个换行。返回 (新文本, 是否修改)。"""
    m = re.search(r'^(##\s*📚\s*相关论文[^\n]*\n)(.*?)(?=^## |\Z)', t, re.MULTILINE | re.DOTALL)
    if not m:
        return t, False
    head = m.group(1)
    body = m.group(2)
    new_body = re.sub(r'\n{2,}', '\n', body)
    if new_body == body:
        return t, False
    return t[:m.start()] + head + new_body + t[m.end():], True

changed = 0
for (typ, slug) in pages:
    dname = 'concepts' if typ == 'concepts' else 'entities'
    p = REPO / 'wiki' / dname / f'{slug}.md'
    t = p.read_text(encoding='utf-8', errors='replace')
    t2, modified = clean_section(t)
    if modified:
        p.write_text(t2, encoding='utf-8')
        changed += 1

print(f"清理了 {changed} 个页面的相关论文节空行")
