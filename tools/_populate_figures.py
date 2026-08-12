import os, re, json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
FIG = os.path.join(BASE, "wiki", "figures")
PAP = os.path.join(BASE, "wiki", "papers")
WO_DIR = os.path.join(BASE, "tools", "_fig_wo")

# Theme keywords for H2 section assignment
THEME_RULES = [
    ("🔬 实验成像与表征", ["stm", "tem", "sem", "afm", "pfm", "xrd", "xps", "表征", "成像", "显微镜", "衍射", "测量", "装置", "实验", "制备", "光路"]),
    ("💻 计算模拟", ["dft", "neb", "cineb", "模拟", "计算", "第一性原理", "md", "分子动力", "势函数", "赝势", "收敛"]),
    ("📐 物理模型与公式", ["公式", "equation", "eq_", "势垒", "势能", "哈密顿", "耦合", "模型", "唯象"]),
]

def theme_for(alt, fname):
    low = (alt + " " + fname).lower()
    for theme, kws in THEME_RULES:
        for kw in kws:
            if kw.lower() in low:
                return theme
    return "📊 图表与数据"

def make_entry(idx, item):
    alt = item["alt"]
    path = item["path"]
    citekey = item["citekey"]
    fname = item["filename"]

    # Determine prefix
    if fname.startswith("eq_") or "公式" in alt or "equation" in alt.lower():
        prefix = "公式"
    elif fname.startswith("tab_") or alt.startswith("表"):
        prefix = "表"
    else:
        prefix = "图"

    # Short title from alt (strip "图N " prefix, keep rest)
    title = re.sub(r'^(图\S*\s+|表\S*\s+|Fig\.\S*\s+|Table\S*\s+)', '', alt).strip()
    if not title:
        title = alt

    # Build entry
    entry = "### {}. {}\n".format(idx, title)
    entry += "\n"
    if prefix == "公式":
        entry += "![{}：{}]({})\n".format(prefix, alt, path)
    elif prefix == "表":
        entry += "![{}：{}]({})\n".format(prefix, alt, path)
    else:
        entry += "![图：{}]({})\n".format(alt, path)
    entry += "*   **来源**：[[../papers/{}]]\n".format(citekey)
    return entry

stats = {"files": 0, "entries": 0}

for fn in sorted(os.listdir(WO_DIR)):
    if not fn.endswith(".json"):
        continue
    slug = fn[:-5]
    page_path = os.path.join(FIG, slug + ".md")
    if not os.path.exists(page_path):
        print("SKIP {} (no page)".format(slug))
        continue

    with open(os.path.join(WO_DIR, fn), "r", encoding="utf-8") as f:
        items = json.load(f)
    if not items:
        continue

    txt = open(page_path, "r", encoding="utf-8").read()

    # Check if already fully processed
    existing_imgs = set(re.findall(r'!\[[^\]]*\]\(\.\./\.\./raw/figures/[^)]+/([^)/]+\.png)\)', txt))
    new_items = [it for it in items if it["filename"] not in existing_imgs]
    if not new_items:
        continue

    # Group new items by theme
    themes = {}
    for it in new_items:
        t = theme_for(it["alt"], it["filename"])
        themes.setdefault(t, []).append(it)

    # For each theme, find or create H2 section, then append H3 entries
    # We collect all new content to append at the end of the file
    # (simple approach: add new H2 sections at the end)
    new_content = "\n"
    for theme, theme_items in sorted(themes.items()):
        new_content += "## {} ({})\n\n".format(theme, theme.split(" ", 1)[1] if " " in theme else theme)
        for i, it in enumerate(theme_items, 1):
            new_content += make_entry(i, it)
            new_content += "\n"

    # Write updated page
    txt = txt.rstrip() + "\n" + new_content
    with open(page_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)
    stats["files"] += 1
    stats["entries"] += len(new_items)
    print("{}: +{} entries".format(slug, len(new_items)))

print("\nDone: {} files, {} entries added".format(stats["files"], stats["entries"]))
