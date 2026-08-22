#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""机械批次：删除 concepts/entities 页尾的 AI 免责声明模板行。

只删除整行 `*（内容由AI生成，仅供参考）*` 及其造成的尾部空行；
不触碰任何其他内容。幂等，可重跑。
"""
import glob
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

MARK = '*（内容由AI生成，仅供参考）*'

changed = 0
skipped_midfile = []
for f in sorted(glob.glob(str(REPO / 'wiki/concepts/*.md')) + glob.glob(str(REPO / 'wiki/entities/*.md'))):
    p = Path(f)
    text = p.read_text(encoding='utf-8')
    if MARK not in text:
        continue
    lines = text.splitlines()
    hits = [i for i, l in enumerate(lines) if l.strip() == MARK]
    # 只处理独占一行的情形；若与正文同行（理论上不存在）则跳过并报告
    if len(hits) != text.count(MARK):
        skipped_midfile.append(p.relative_to(REPO).as_posix())
        continue
    kept = [l for i, l in enumerate(lines) if i not in hits]
    while kept and not kept[-1].strip():
        kept.pop()
    p.write_text('\n'.join(kept) + '\n', encoding='utf-8', newline='')
    changed += 1

print(f'已清除 {changed} 页的 AI 免责声明行')
if skipped_midfile:
    print('跳过（非独占行，需人工看）:')
    for s in skipped_midfile:
        print('  ', s)
