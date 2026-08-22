# -*- coding: utf-8 -*-
"""Step 0: 备份所有受影响文件到 temp，并输出论文标题映射。"""
import re, json, shutil
from pathlib import Path
from datetime import datetime

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

# 加载扫描结果
data = json.loads((OUT / 'suggestions_full.json').read_text(encoding='utf-8'))
cat = data['cat']

# 收集所有受影响的 paper citekey 与页面
paper_citekeys = set()
pages_to_backup = set()  # (path, kind) kind: formal/intermediate
for k in ['B', 'C', 'D']:
    for s in cat[k]:
        paper_citekeys.add(s['citekey'])
        if k == 'B':
            pages_to_backup.add((s['type'], s['actual_slug'], 'formal'))
        elif k == 'C':
            pages_to_backup.add((s['type'], s['actual_slug'], 'intermediate'))

# 备份目录
ts = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_dir = OUT / f"backup_suggestions_{ts}"
backup_dir.mkdir(parents=True, exist_ok=True)

# 备份 papers
papers_backup = backup_dir / 'papers'
papers_backup.mkdir(exist_ok=True)
for ck in sorted(paper_citekeys):
    src = PAPERS_DIR / f"{ck}.md"
    if src.exists():
        shutil.copy2(src, papers_backup / f"{ck}.md")

# 备份 concepts/entities 页面
pages_backup = backup_dir / 'pages'
pages_backup.mkdir(exist_ok=True)
for typ, slug, kind in sorted(pages_to_backup):
    d = CONCEPTS_DIR if typ == 'concepts' else ENTITIES_DIR
    src = d / f"{slug}.md"
    if src.exists():
        shutil.copy2(src, pages_backup / f"{typ}_{slug}.md")

# 论文标题映射
titles = {}
for ck in sorted(paper_citekeys):
    src = PAPERS_DIR / f"{ck}.md"
    if src.exists():
        fm, _ = split_fm(read(src))
        m = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm, re.MULTILINE) if fm else None
        titles[ck] = m.group(1).strip() if m else ck

print(f"备份目录: {backup_dir}")
print(f"受影响论文数: {len(paper_citekeys)}")
print(f"受影响页面数: {len(pages_to_backup)}")
print("\n=== 论文标题映射 ===")
for ck, t in sorted(titles.items()):
    print(f"  {ck}: {t}")

# 保存批次信息
(OUT / 'batch_info.json').write_text(json.dumps({
    'backup_dir': str(backup_dir),
    'paper_citekeys': sorted(paper_citekeys),
    'titles': titles,
    'pages_to_backup': sorted([list(x) for x in pages_to_backup]),
}, ensure_ascii=False, indent=2), encoding='utf-8')
print("\n已保存 batch_info.json")
