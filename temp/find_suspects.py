# -*- coding: utf-8 -*-
"""识别疑似丢失正文描述章节的论文页：只有双链类 H2、缺少描述类 H2。只读。"""
import re
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
PAPERS = REPO / 'wiki' / 'papers'

FM_RE = re.compile(r'^---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)', re.DOTALL)

# 描述类章节关键词（历史完整版本应包含）
DESC_KEYWORDS = ['📄 元数据', '💡 一句话', '📊 关键图表', '📝 组织与用词', '✏️ 可写入', '🔬 项目连接', '🔗 项目双链']

def read(p):
    return p.read_text(encoding='utf-8', errors='replace')

suspects = []
full = []
for p in sorted(PAPERS.glob('*.md')):
    t = read(p)
    m = FM_RE.match(t)
    body = t[m.end():] if m else t
    h2 = re.findall(r'^##\s+([^\n]+)$', body, re.MULTILINE)
    h2_names = [x.strip() for x in h2]
    desc_count = sum(1 for h in h2_names if any(k in h for k in DESC_KEYWORDS))
    has_title_h2 = any(not h.startswith(('📄', '💡', '🔗', '📊', '🔬', '📝', '✏️', '🏗', '🧩', '🆕')) for h in h2_names)
    if desc_count == 0:
        suspects.append({'citekey': p.stem, 'h2': h2_names})
    else:
        full.append({'citekey': p.stem, 'h2_count': len(h2_names), 'desc': desc_count})

print(f"总论文数: {len(suspects) + len(full)}")
print(f"疑似丢失描述章节（desc 关键词命中 0）: {len(suspects)}")
print(f"完整页面: {len(full)}")

print("\n=== 疑似丢失清单 ===")
for s in suspects:
    print(f"  {s['citekey']}: {s['h2']}")
