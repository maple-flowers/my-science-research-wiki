#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""删除 frontmatter 末尾的 AIGC 水印块（键 + 其缩进子键），其余字段与正文逐字保留。幂等。"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

TARGETS = [
    "wiki/concepts/antiferromagnetism.md",
    "wiki/concepts/d0-rule.md",
    "wiki/concepts/vdW-heterostructure.md",
    "wiki/concepts/weak-ferromagnetism.md",
]

FM_RE = re.compile(r'\A(---\s*\r?\n)(.*?)(\r?\n---[ \t]*\r?\n)', re.DOTALL)
# AIGC: 起，连同后续所有缩进行（其子键）一并删除；遇到下一个顶格键即停止
AIGC_BLOCK = re.compile(r'(?:\r?\n)?^AIGC[ \t]*:[ \t]*\r?\n(?:^[ \t]+\S[^\n]*\r?\n?)*', re.M)

for rel in TARGETS:
    p = REPO / rel
    raw = p.read_text(encoding='utf-8')
    m = FM_RE.match(raw)
    if not m:
        print(f"SKIP  {rel}: 无 frontmatter")
        continue
    head, fm, tail = m.group(1), m.group(2), m.group(3)
    if 'AIGC' not in fm:
        print(f"SKIP  {rel}: 已无 AIGC 块")
        continue
    new_fm = AIGC_BLOCK.sub('', fm).rstrip('\r\n')
    if 'AIGC' in new_fm:
        print(f"FAIL  {rel}: AIGC 块未被完全删除，跳过不写入")
        continue
    p.write_text(head + new_fm + tail + raw[m.end():], encoding='utf-8', newline='')
    print(f"OK    {rel}: frontmatter {len(fm.splitlines())} 行 -> {len(new_fm.splitlines())} 行")
