# -*- coding: utf-8 -*-
"""检查 46 个反向缺失涉及正式页的「相关论文」节结构，以及 chowdhury 的 Wiki 双链章节。只读。"""
import json, re
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
OUT = Path(r"C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp")

d = json.loads((OUT / 'bidirectional_analysis.json').read_text(encoding='utf-8'))
bw = d['backward_missing']

pages = {}
for x in bw:
    typ = x['type']
    slug = x['slug']
    pages[(typ, slug)] = pages.get((typ, slug), []) + [x['citekey']]

def read(p):
    return p.read_text(encoding='utf-8', errors='replace')

for (typ, slug), citekeys in sorted(pages.items()):
    dname = 'concepts' if typ == 'concepts' else 'entities'
    p = REPO / 'wiki' / dname / f'{slug}.md'
    if not p.exists():
        print(f"[缺失文件] {typ}/{slug}")
        continue
    t = read(p)
    # 找相关论文节
    m = re.search(r'^##\s*📚\s*相关论文.*$', t, re.MULTILINE)
    has_section = m is not None
    # 找 frontmatter papers 字段
    fm = re.match(r'^---\s*\r?\n(.*?)\r?\n---', t, re.DOTALL)
    fm_text = fm.group(1) if fm else ''
    papers_line = re.search(r'^papers:\s*\[(.*?)\]', fm_text, re.MULTILINE)
    papers_multi = re.search(r'^papers:\s*\n', fm_text, re.MULTILINE)
    fmt = 'inline' if papers_line else ('multi' if papers_multi else 'NONE')
    print(f"{typ}/{slug} 相关论文节={has_section} papers字段格式={fmt} 需补 {len(citekeys)} 个")
    if not has_section:
        # 打印正文末尾 500 字符看结构
        print(f"   末尾: ...{t[-300:]!r}")
