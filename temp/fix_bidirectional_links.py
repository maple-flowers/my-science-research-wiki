# -*- coding: utf-8 -*-
"""批量补齐双向链接：反向缺失 46 对 + 正向反引号 2 对（含对应的 TaS2/TaSe2 反链）。
先备份所有受影响文件到 temp，再执行修复，最后输出统计。"""
import re, json, shutil, time
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
TEMP = Path(r"C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp")

d = json.loads((TEMP / 'bidirectional_analysis.json').read_text(encoding='utf-8'))
bw = d['backward_missing']

# 汇总：正式页 -> 需补 citekey 列表
page_citekeys = {}
for x in bw:
    key = (x['type'], x['slug'])
    page_citekeys.setdefault(key, []).append(x['citekey'])

# 正向反引号 2 个（chowdhury -> TaS2/TaSe2），同时补对应的反向
forward_extra = [
    {'citekey': 'chowdhuryReviewTheoreticalComputational', 'type': 'entities', 'slug': 'TaS2'},
    {'citekey': 'chowdhuryReviewTheoreticalComputational', 'type': 'entities', 'slug': 'TaSe2'},
]
for x in forward_extra:
    key = (x['type'], x['slug'])
    page_citekeys.setdefault(key, []).append(x['citekey'])

# 备份目录
backup_dir = TEMP / f"backup_bidir_{time.strftime('%Y%m%d_%H%M%S')}"
backup_dir.mkdir(parents=True, exist_ok=True)

files_to_modify = set()
for (typ, slug) in page_citekeys:
    dname = 'concepts' if typ == 'concepts' else 'entities'
    files_to_modify.add(REPO / 'wiki' / dname / f'{slug}.md')
files_to_modify.add(REPO / 'wiki' / 'papers' / 'chowdhuryReviewTheoreticalComputational.md')

for p in files_to_modify:
    shutil.copy2(p, backup_dir / p.name)

print(f"已备份 {len(files_to_modify)} 个文件到: {backup_dir}")

# ---- 修复函数 ----
def read(p):
    return p.read_text(encoding='utf-8', errors='replace')

def write(p, t):
    p.write_text(t, encoding='utf-8')

def append_fm_papers(t, citekey):
    """frontmatter papers 行内列表追加 citekey。返回 (新文本, 是否修改)。"""
    m = re.search(r'^(papers:\s*\[)(.*?)(\]\s*)$', t, re.MULTILINE)
    if not m:
        # 尝试多行
        m2 = re.search(r'^(papers:\s*\n)((?:\s*-\s+.*\n?)*)', t, re.MULTILINE)
        if not m2:
            return t, False
        existing = set()
        for line in m2.group(2).splitlines():
            s = line.strip().lstrip('-').strip().strip('"\'').strip()
            if s:
                existing.add(s.lower())
        if citekey.lower() in existing:
            return t, True
        new_block = m2.group(2).rstrip('\n') + f'\n  - {citekey}\n'
        return t[:m2.start()] + m2.group(1) + new_block + t[m2.end():], True
    inner = m.group(2)
    existing = set()
    for s in inner.split(','):
        s = s.strip().strip('"\'').strip()
        if s:
            existing.add(s.lower())
    if citekey.lower() in existing:
        return t, True
    if inner.strip():
        new_inner = inner.rstrip()
        if new_inner.endswith(','):
            new_inner += f' {citekey}'
        else:
            new_inner += f', {citekey}'
    else:
        new_inner = f' {citekey}'
    new_line = m.group(1) + new_inner + m.group(3)
    return t[:m.start()] + new_line + t[m.end():], True

def append_related_papers(t, citekey):
    """正文「相关论文」节追加 - [[../papers/<citekey>]]。返回 (新文本, 是否修改)。"""
    m = re.search(r'^(##\s*📚\s*相关论文[^\n]*\n)', t, re.MULTILINE)
    if not m:
        return t, False
    sec_start = m.end()
    next_h2 = re.search(r'^## ', t[sec_start:], re.MULTILINE)
    sec_end = sec_start + next_h2.start() if next_h2 else len(t)
    section = t[sec_start:sec_end]
    # 检查是否已含该 citekey（大小写不敏感）
    pat = re.compile(re.escape(f'../papers/{citekey}'), re.IGNORECASE)
    if pat.search(section):
        return t, True
    new_line = f'- [[../papers/{citekey}]]\n'
    insert_pos = sec_end
    prefix = t[:insert_pos]
    if not prefix.endswith('\n'):
        prefix += '\n'
    return prefix + new_line + t[insert_pos:], True

# ---- 执行修复 ----
stats = {'fm_added': 0, 'fm_existed': 0, 'sec_added': 0, 'sec_existed': 0, 'fm_missing_section': 0, 'sec_missing_section': 0}

for (typ, slug), citekeys in page_citekeys.items():
    dname = 'concepts' if typ == 'concepts' else 'entities'
    p = REPO / 'wiki' / dname / f'{slug}.md'
    t = read(p)
    orig = t
    for citekey in citekeys:
        t, modified = append_fm_papers(t, citekey)
        if modified:
            stats['fm_added'] += 1
        else:
            stats['fm_existed'] += 1
    for citekey in citekeys:
        t2, modified = append_related_papers(t, citekey)
        if modified:
            stats['sec_added'] += 1
            t = t2
        else:
            stats['sec_existed'] += 1
    if t != orig:
        write(p, t)

# ---- chowdhury 正向：Wiki 双链章节补 TaS2/TaSe2 ----
pc = REPO / 'wiki' / 'papers' / 'chowdhuryReviewTheoreticalComputational.md'
tc = read(pc)
old = '  - 实体 [[../entities/VASP]]\n'
new = '  - 实体 [[../entities/VASP]]\n  - 实体 [[../entities/TaS2]]\n  - 实体 [[../entities/TaSe2]]\n'
if old in tc and '  - 实体 [[../entities/TaS2]]' not in tc:
    tc = tc.replace(old, new, 1)
    write(pc, tc)
    fwd_added = 2
else:
    fwd_added = 0

print(f"\n=== 修复统计 ===")
print(f"反向：frontmatter papers 字段新增 citekey {stats['fm_added']} 个，已存在跳过 {stats['fm_existed']} 个")
print(f"反向：正文相关论文节新增双链 {stats['sec_added']} 个，已存在跳过 {stats['sec_existed']} 个")
print(f"正向：chowdhury 正文新增实体双链 {fwd_added} 个")

# ---- 验证：重新读取并核对 ----
print("\n=== 验证 ===")
ok = True
for (typ, slug), citekeys in page_citekeys.items():
    dname = 'concepts' if typ == 'concepts' else 'entities'
    p = REPO / 'wiki' / dname / f'{slug}.md'
    t = read(p)
    fm_match = re.match(r'^---\s*\r?\n(.*?)\r?\n---', t, re.DOTALL)
    fm = fm_match.group(1) if fm_match else ''
    sec_match = re.search(r'^##\s*📚\s*相关论文[^\n]*\n(.*?)(?=^## |\Z)', t, re.MULTILINE | re.DOTALL)
    sec = sec_match.group(1) if sec_match else ''
    for citekey in citekeys:
        in_fm = citekey.lower() in fm.lower()
        in_sec = citekey.lower() in sec.lower()
        if not in_fm or not in_sec:
            ok = False
            print(f"  [FAIL] {typ}/{slug} citekey={citekey} fm={in_fm} sec={in_sec}")

# 验证 chowdhury
tc2 = read(pc)
for slug in ['TaS2', 'TaSe2']:
    if f'[[../entities/{slug}]]' not in tc2:
        ok = False
        print(f"  [FAIL] chowdhury 缺 {slug} 双链")

print("验证结果:", "全部通过" if ok else "存在失败项，请检查")
