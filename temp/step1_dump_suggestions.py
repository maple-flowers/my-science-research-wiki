# -*- coding: utf-8 -*-
"""Step 1: 打印所有 papers 的「🆕 新概念/实体建议」章节原始内容，核对解析完整性。"""
import re
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
PAPERS_DIR = REPO / 'wiki' / 'papers'

def read(p):
    return p.read_text(encoding='utf-8', errors='replace')

for p in sorted(PAPERS_DIR.glob('*.md')):
    text = read(p)
    m = re.search(r'##\s*🆕\s*新概念/实体建议(.*?)(?=\n##\s|\Z)', text, re.DOTALL)
    if not m:
        continue
    sec = m.group(1)
    # 只打印含反引号 slug 的行
    lines = [ln for ln in sec.splitlines() if '`' in ln]
    if lines:
        print(f"### {p.stem}")
        for ln in lines:
            print(f"  {ln.strip()}")
        print()
