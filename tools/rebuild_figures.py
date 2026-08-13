#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rebuild wiki/figures pages from classified entries.
- 9 top-level categories
- Categories >60 entries auto-split into subpages
- Updates paper links and frontmatter figures: field
- Updates _index.md
"""
import json, re, os, sys
from collections import defaultdict, Counter

sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES_DIR = os.path.join(WIKI_DIR, "wiki", "figures")
PAPERS_DIR = os.path.join(WIKI_DIR, "wiki", "papers")

# ── Category metadata ──
# `label` is the display name used for the category itself (hub page title and
# index entry). `desc` is the one-line scope note shown under the title.
CATEGORY_META = {
    "crystal-structures": {"name": "结构与原子构型", "label": "晶体结构与原子构型", "desc": "晶体结构、晶格、原子构型、空间群、键长键角、XRD衍射、相变与相图"},
    "heterostructures-stacking": {"name": "结构与原子构型", "label": "异质结与堆叠", "desc": "异质结、堆叠、范德华异质结构、莫尔超晶格、界面结构"},
    "domain-walls": {"name": "结构与原子构型", "label": "铁电畴与畴壁", "desc": "铁电畴、畴壁、极化翻转、电滞回线、压电响应"},
    "electronic-bands": {"name": "能带结构与光谱", "label": "电子结构与输运", "desc": "能带结构、态密度、费米面、CDW、输运与磁性质"},
    "vibrational-spectra": {"name": "能带结构与光谱", "label": "振动光谱", "desc": "声子谱、拉曼光谱、红外光谱、振动模式"},
    "optical-spectra": {"name": "能带结构与光谱", "label": "光学光谱", "desc": "吸收/透射/反射光谱、荧光/发光、SHG、光学常数"},
    "electronic-devices": {"name": "器件与实验装置", "label": "器件与电学特性", "desc": "传感器、存储器、晶体管、器件特性"},
    "experimental-setups": {"name": "器件与实验装置", "label": "实验装置与表征方法", "desc": "实验装置、测量系统、制备工艺、表征方法"},
    "mathematical-models": {"name": "理论模型", "label": "理论模型与计算方法", "desc": "理论公式、计算方法、数值模拟"},
}

# Top-level section grouping (for _index.md)
SECTIONS = [
    ("🔬 结构与原子构型", ["crystal-structures", "heterostructures-stacking", "domain-walls"]),
    ("📈 能带结构与光谱", ["electronic-bands", "vibrational-spectra", "optical-spectra"]),
    ("🔌 器件与实验装置", ["electronic-devices", "experimental-setups"]),
    ("📐 理论模型", ["mathematical-models"]),
]

# ── Sub-category splits for large categories (>60) ──
SUBCATEGORIES = {
    "electronic-bands": [
        {
            "slug": "electronic-bands-band-structures",
            "name": "能带结构与带隙",
            "keywords": ["能带", "band structure", "带隙", "band gap", "bandgap",
                         "价带", "导带", "色散曲线", "能带图", "能带结构",
                         "HOMO", "LUMO", "能隙", "能级图"],
        },
        {
            "slug": "electronic-bands-dos-fermi",
            "name": "态密度与费米面",
            "keywords": ["态密度", "DOS", "PDOS", "费米面", "Fermi surface",
                         "费米能级", "Fermi level", "费米", "Fermi", "ARPES",
                         "投影态密度", "Fermi contours", "电荷密度", "电子密度",
                         "差分电荷密度", "电荷分布", "电荷转移", "LDOS"],
        },
        {
            "slug": "electronic-bands-cdw-transport",
            "name": "CDW与输运性质",
            "keywords": ["CDW", "电荷密度波", "磁化率", "susceptibility", "自能",
                         "self-energy", "电阻率", "电阻随温度", "超导", "superconduct",
                         "霍尔", "Hall", "磁阻", "磁电阻", "自旋", "spin", "磁矩",
                         "BCS", "DMFT", "电荷磁化率", "波函数", "轨道", "orbital",
                         "磁荷", "磁场线", "磁结构"],
        },
    ],
    "mathematical-models": [
        {
            "slug": "mathematical-models-computational",
            "name": "计算方法与泛函",
            "keywords": ["DFT", "第一性原理", "密度泛函", "计算方法", "收敛", "k点",
                         "k网格", "k-space", "布里渊区", "自洽", "PAW", "pseudopotential",
                         "赝势", "截断能", "截断半径", "机器学习势", "DP模型", "神经网络势",
                         "PAW 数据集", "US-PP", "数据集", "分波", "泛函", "交换关联",
                         "增强因子", "原子化能", "Bader", "在网法", "近网法",
                         "EAM总势能", "对势", "电子密度函数", "嵌入能", "EAM势参数",
                         "Hubbard", "LDA+U", "GGA"],
        },
        {
            "slug": "mathematical-models-simulations",
            "name": "模拟与数值结果",
            "keywords": ["数值模拟", "分子动力学", "蒙特卡洛", "Monte Carlo", "相场",
                         "有限元", "模拟结果", "计算结果", "吸附能", "表面能", "总能量",
                         "能量-温度", "能量随", "受力", "Mulliken", "布居", "孤子",
                         "soliton", "概率演化", "均方位移", "扩散系数", "形核", "过冷度",
                         "平均能量", "熔化温度", "理论相图", "构型", "元胞", "CA",
                         "组织演化", "晶粒尺寸", "冷速", "Zener", "对分布函数",
                         "杜隆", "NEB", "能垒", "自由能阶梯", "ORR", "OER"],
        },
        {
            "slug": "mathematical-models-elasticity-strain",
            "name": "应变、弹性与力学模型",
            "keywords": ["应变", "strain", "应力", "stress", "弹性", "elastic",
                         "杨氏模量", "泊松比", "剪切", "应变张量", "应变矩阵",
                         "铁弹", "ferroelastic", "畴物理", "力学", "模量",
                         "Kittel", "力常数", "压缩", "拉伸", "弯曲", "褶皱",
                         "转变应变"],
        },
        {
            "slug": "mathematical-models-magnetoelectric",
            "name": "磁电耦合与多铁理论",
            "keywords": ["磁电", "magnetoelectric", "多铁", "multiferroic",
                         "自由能", "Landau", "朗道", "对称性", "symmetry",
                         "反演", "时间反演", "序参量", "order parameter",
                         "DM", "Dzyaloshinskii", "交换伸缩", "螺旋磁", "螺旋态",
                         "spin spiral", "自旋螺旋", "非公度螺旋",
                         "Onsager", "Lifshitz", "极化-磁化", "磁化率",
                         "LLG", "拓扑荷", "自旋哈密顿", "Thiele", "斯格明子",
                         "居里点", "反铁磁", "铁磁", "磁矩", "磁各向异性", "MAE"],
        },
        {
            "slug": "mathematical-models-formulas",
            "name": "光学、输运与其他解析公式",
            "keywords": ["公式", "方程", "表达式", "解析解", "哈密顿", "hamiltonian",
                         "eq", "理论模型", "理论框架", "费曼图", "微扰", "截面",
                         "传递函数", "标量", "张量",
                         "倏逝", "高斯光束", "束宽", "贝塞尔", "Tauc",
                         "Kubelka", "调制深度", "相位差", "折射率",
                         "CDW", "超导", "输运", "渗流", "涡旋", "Little-Parks",
                         "紧束缚", "色散", "电子-声子", "耦合矩阵元",
                         "饱和水汽压", "经验公式", "校准", "反演"],
        },
    ],
    "crystal-structures": [
        {
            "slug": "crystal-structures-bulk",
            "name": "体相晶体结构",
            "keywords": ["晶体结构", "crystal structure", "晶格", "lattice", "单胞",
                         "unit cell", "原胞", "晶面", "晶向", "空间群", "space group",
                         "键长", "键角", "配位", "多面体", "八面体", "四面体",
                         "球棍模型", "结构模型", "原子位置", "原子坐标", "投影结构",
                         "俯视图", "分子结构", "分子构型", "构象", "极性结构", "极性金属",
                         "晶体", "crystal", "结构示意", "结构图"],
        },
        {
            "slug": "crystal-structures-surfaces-defects",
            "name": "表面、缺陷与形貌",
            "keywords": ["表面", "吸附", "缺陷", "defect", "空位", "vacancy",
                         "位错", "dislocation", "掺杂", "doping", "形貌", "morphology",
                         "晶粒", "grain", "吸附位置", "原子对", "重构", "表面能"],
        },
        {
            "slug": "crystal-structures-xrd-phases",
            "name": "XRD与相变",
            "keywords": ["XRD", "X射线衍射", "衍射图", "衍射峰", "衍射", "相变",
                         "phase transition", "相图", "phase diagram", "结构相变",
                         "中子衍射", "精修", "Rietveld", "FullProf", "晶体取向",
                         "织构", "DSC", "偏振显微"],
        },
    ],
    "electronic-devices": [
        {
            "slug": "electronic-devices-sensors",
            "name": "传感器与探测器",
            "keywords": ["传感器", "sensor", "探测器", "detector", "湿度传感器",
                         "气体传感器", "压力传感器", "灵敏度", "响应时间", "恢复时间",
                         "湿敏", "感湿"],
        },
        {
            "slug": "electronic-devices-memory-transistors",
            "name": "存储器与晶体管",
            "keywords": ["存储器", "memory", "阻变", "RRAM", "忆阻", "晶体管",
                         "transistor", "FET", "MOSFET", "二极管", "diode", "LED",
                         "发光二极管", "太阳能电池", "电池", "存储", "写入", "读取",
                         "擦除", "STT-RAM", "PCM", "DRAM", "主存", "缓存", "电极",
                         "栅极", "源极", "漏极", "I-V", "电流-电压", "输出特性",
                         "转移特性", "开关比", "电路", "电容器", "器件结构", "器件示意",
                         "器件", "性能对比"],
        },
    ],
    "domain-walls": [
        {
            "slug": "domain-walls-structures",
            "name": "畴结构与畴壁",
            "keywords": ["畴", "domain", "畴壁", "domain wall", "铁电畴", "磁畴",
                         "电畴", "畴结构", "畴图", "版式插图", "版式横幅"],
        },
        {
            "slug": "domain-walls-switching-properties",
            "name": "极化翻转与铁电性能",
            "keywords": ["极化翻转", "极化分布", "极化方向", "极化-电场", "电滞回线",
                         "P-E回线", "蝴蝶回线", "铁电", "ferroelectric", "压电",
                         "piezoelectric", "压电响应", "翻转", "switching", "开关",
                         "PFM", "压电曲面"],
        },
    ],
}

SPLIT_THRESHOLD = 60


def assign_subcategory(entry, cat_slug):
    """Assign entry to a subcategory within a split category."""
    subs = SUBCATEGORIES.get(cat_slug)
    if not subs:
        return cat_slug  # no split

    alt = entry.get("alt", "")
    desc = entry.get("desc", "")
    feat = entry.get("feat", "")
    text = f"{alt} {desc} {feat}"

    best_sub = None
    best_score = 0
    for sub in subs:
        score = 0
        for kw in sub["keywords"]:
            if kw in alt:
                score += 3
            elif kw in desc:
                score += 2
            elif kw in feat:
                score += 1
        if score > best_score:
            best_score = score
            best_sub = sub

    if best_sub is None:
        # Fallback: assign to first subcategory
        best_sub = subs[0]

    return best_sub["slug"]


def build_pages(entries):
    """Build figure pages from classified entries."""
    # Group entries by top-level category
    by_category = defaultdict(list)
    for e in entries:
        cat = e["new_slug"]
        # Determine the top-level category
        top_cat = cat
        # Check if this is already a subcategory slug
        for parent in SUBCATEGORIES:
            for sub in SUBCATEGORIES[parent]:
                if cat == sub["slug"]:
                    top_cat = parent
                    break
        by_category[top_cat].append(e)

    # For each category, determine final slug for each entry
    # and group by final slug
    page_entries = defaultdict(list)  # final_slug -> [entries]

    for cat_slug, cat_entries in by_category.items():
        if len(cat_entries) > SPLIT_THRESHOLD and cat_slug in SUBCATEGORIES:
            # Split into subcategories
            for e in cat_entries:
                sub_slug = assign_subcategory(e, cat_slug)
                e["final_slug"] = sub_slug
                page_entries[sub_slug].append(e)
        else:
            # Single page
            for e in cat_entries:
                e["final_slug"] = cat_slug
                page_entries[cat_slug].append(e)

    # Report distribution
    print("=== Page Distribution ===")
    for slug in sorted(page_entries.keys()):
        print(f"  {slug}: {len(page_entries[slug])} entries")

    return page_entries


def format_entry(idx, entry):
    """Format a single figure entry as markdown."""
    alt = entry.get("alt", "")
    img = entry.get("img", "")
    paper = entry.get("paper", "")
    desc = entry.get("desc", "")
    feat = entry.get("feat", "")

    # Clean up feat: remove leading "- **关键特征**：" if present
    if feat.startswith("- **关键特征**："):
        feat = feat[len("- **关键特征**："):].strip()
    elif feat.startswith("**关键特征**："):
        feat = feat[len("**关键特征**："):].strip()

    # Clean up desc
    if desc.startswith("- **图示描述**："):
        desc = desc[len("- **图示描述**："):].strip()
    elif desc.startswith("**图示描述**："):
        desc = desc[len("**图示描述**："):].strip()

    lines = []
    lines.append(f"### {idx}. {alt}")
    lines.append(f"![{alt}]({img})")
    lines.append(f"*   **来源**：[[../papers/{paper}]]")
    if desc:
        lines.append(f"*   **图示描述**：{desc}")
    if feat:
        lines.append(f"*   **关键特征**：{feat}")
    return "\n".join(lines)


def generate_page(slug, entries, is_hub=False, sub_info=None):
    """Generate markdown for a figure page."""
    cat_slug = slug
    # Find parent category for subpages
    parent_cat = slug
    for parent in SUBCATEGORIES:
        for sub in SUBCATEGORIES[parent]:
            if slug == sub["slug"]:
                parent_cat = parent
                break

    meta = CATEGORY_META.get(parent_cat, {"name": slug, "label": slug, "desc": ""})
    label = meta.get("label", meta.get("name", slug))

    lines = []
    # Frontmatter
    lines.append("---")
    lines.append("tags:")
    lines.append("  - type/figure-collection")
    lines.append("---")
    lines.append("")

    if is_hub:
        # Hub page for split category
        lines.append(f"# {label}")
        lines.append("")
        lines.append(f"> {meta['desc']}")
        lines.append("")
        lines.append("## 子页面")
        lines.append("")
        for sub in SUBCATEGORIES[parent_cat]:
            count = len([e for e in entries if e["final_slug"] == sub["slug"]])
            lines.append(f"- [[{sub['slug']}|{sub['name']}]]（{count} 条）")
        lines.append("")
    else:
        # Content page (either single category or subpage)
        if sub_info:
            lines.append(f"# {label}：{sub_info['name']}")
            lines.append("")
            # Breadcrumb, not the parent's scope note — the parent desc would
            # misdescribe a narrower subpage.
            lines.append(f"> 属于 [[{parent_cat}|{label}]]")
        else:
            lines.append(f"# {label}")
            lines.append("")
            lines.append(f"> {meta['desc']}")
        lines.append("")
        lines.append("## 条目")
        lines.append("")

        # Sort entries by paper, then by figure number
        def sort_key(e):
            alt = e.get("alt", "")
            # Extract figure number from alt text
            m = re.search(r'(?:图|公式|式|表|Fig\.?)\s*(\d+)', alt)
            fig_num = int(m.group(1)) if m else 999
            return (e.get("paper", ""), fig_num)

        sorted_entries = sorted(entries, key=sort_key)

        for idx, e in enumerate(sorted_entries, 1):
            lines.append(format_entry(idx, e))
            lines.append("")

    return "\n".join(lines)


def write_figure_pages(page_entries):
    """Write all figure pages to wiki/figures/."""
    # Determine which categories are split (have hub pages)
    split_cats = set()
    for slug in page_entries:
        for parent in SUBCATEGORIES:
            if slug.startswith(parent + "-"):
                split_cats.add(parent)
                break

    written = []
    for slug, entries in page_entries.items():
        # Check if this is a subpage
        is_sub = False
        sub_info = None
        for parent in SUBCATEGORIES:
            for sub in SUBCATEGORIES[parent]:
                if slug == sub["slug"]:
                    is_sub = True
                    sub_info = sub
                    break

        content = generate_page(slug, entries, is_hub=False, sub_info=sub_info)
        filepath = os.path.join(FIGURES_DIR, f"{slug}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        written.append((slug, len(entries)))
        print(f"  Written: {slug}.md ({len(entries)} entries)")

    # Write hub pages for split categories
    for parent_cat in split_cats:
        # Collect all entries for this parent category
        all_entries = []
        for sub in SUBCATEGORIES[parent_cat]:
            sub_slug = sub["slug"]
            if sub_slug in page_entries:
                all_entries.extend(page_entries[sub_slug])

        # Find sub_info for each sub
        subs_with_counts = []
        for sub in SUBCATEGORIES[parent_cat]:
            count = len(page_entries.get(sub["slug"], []))
            subs_with_counts.append((sub, count))

        content = generate_page(parent_cat, all_entries, is_hub=True)
        filepath = os.path.join(FIGURES_DIR, f"{parent_cat}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        written.append((parent_cat, len(all_entries)))
        print(f"  Written hub: {parent_cat}.md ({len(all_entries)} entries)")

    return written


def generate_index(page_entries, written_slugs):
    """Generate _index.md content."""
    lines = []
    lines.append("---")
    lines.append("tags:")
    lines.append("  - type/figure-index")
    lines.append("---")
    lines.append("")
    lines.append("# 图表索引")
    lines.append("")
    lines.append("> 按论文图表内容重新分类的图表集合索引。所有分类以 `wiki/papers` 中的图表描述为准。")
    lines.append("")

    total = 0
    for section_title, cat_slugs in SECTIONS:
        lines.append(f"## {section_title}")
        lines.append("")
        for cat_slug in cat_slugs:
            meta = CATEGORY_META.get(cat_slug, {"name": cat_slug, "label": cat_slug, "desc": ""})
            label = meta.get("label", meta.get("name", cat_slug))
            if cat_slug in SUBCATEGORIES:
                # Split category: hub + subpages
                sub_count = 0
                sub_lines = []
                for sub in SUBCATEGORIES[cat_slug]:
                    count = len(page_entries.get(sub["slug"], []))
                    sub_count += count
                    sub_lines.append(f"    - [[{sub['slug']}|{sub['name']}]]（{count} 条）")
                lines.append(f"- **[[{cat_slug}|{label}]]**（{sub_count} 条，{len(SUBCATEGORIES[cat_slug])} 个子页面）")
                lines.extend(sub_lines)
                total += sub_count
            else:
                count = len(page_entries.get(cat_slug, []))
                lines.append(f"- **[[{cat_slug}|{label}]]**（{count} 条）")
                total += count
        lines.append("")

    lines.append(f"> 共 **{total}** 个图表条目，来自 `wiki/papers` 中的论文图表描述。")
    lines.append("")

    return "\n".join(lines)


def cleanup_old_pages(written_slugs):
    """Delete old figure pages that are no longer used."""
    # Build set of valid filenames
    valid_files = {"_index.md"}
    for slug in written_slugs:
        valid_files.add(f"{slug}.md")

    deleted = []
    if os.path.exists(FIGURES_DIR):
        for f in os.listdir(FIGURES_DIR):
            if f.endswith(".md") and f not in valid_files:
                filepath = os.path.join(FIGURES_DIR, f)
                os.remove(filepath)
                deleted.append(f)
                print(f"  Deleted: {f}")

    return deleted


def main():
    # Load classified entries
    with open(os.path.join(WIKI_DIR, "tools", "figure_classified.json"), "r", encoding="utf-8") as f:
        entries = json.load(f)

    print(f"Loaded {len(entries)} classified entries")

    # Build pages
    page_entries = build_pages(entries)

    print(f"\n=== Writing Figure Pages ===")
    written = write_figure_pages(page_entries)

    written_slugs = [slug for slug, _ in written]
    print(f"\n=== Done: {len(written)} pages written ===")

    # Generate _index.md
    print(f"\n=== Writing _index.md ===")
    index_content = generate_index(page_entries, written_slugs)
    index_path = os.path.join(FIGURES_DIR, "_index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"  Written: _index.md")

    # Cleanup old pages
    print(f"\n=== Cleaning up old pages ===")
    deleted = cleanup_old_pages(written_slugs)
    print(f"  Deleted {len(deleted)} old pages")

    # Save final slug mapping for paper updates
    slug_map = {}
    for e in entries:
        img = e.get("img", "")
        final_slug = e.get("final_slug", e.get("new_slug"))
        slug_map[img] = final_slug

    with open(os.path.join(WIKI_DIR, "tools", "figure_slug_map.json"), "w", encoding="utf-8") as f:
        json.dump(slug_map, f, ensure_ascii=False, indent=2)
    print(f"\nSaved slug map to tools/figure_slug_map.json ({len(slug_map)} entries)")


if __name__ == "__main__":
    main()
