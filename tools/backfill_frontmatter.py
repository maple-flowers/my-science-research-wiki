"""Backfill YAML frontmatter into early per-paper records that lack it.

For each tools/ingest_papers/<citekey>.md that does NOT already start with
'---', build a frontmatter from:
  * metadata in raw/note/<citekey>.md (YAML header + Zotero metadata table)
  * the ten literature-matrix fields from tools/ingest_papers/_matrix.json
  * wiki double-links already present in the record body
  * the 项目连接 section to derive projects[] + relevance/project-N/<level>
  * a small keyword dictionary to infer methods[] / topics[]

The body is left untouched. Output is UTF-8 with '\\n' line endings.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
INGEST = REPO / "tools" / "ingest_papers"
NOTES = REPO / "raw" / "note"
MATRIX = json.loads((INGEST / "_matrix.json").read_text(encoding="utf-8"))

MATRIX_FIELDS = [
    "领域基础知识", "研究背景", "作者的问题意识", "主要研究对象",
    "主要研究方法", "研究意义", "研究结论", "对领域的贡献",
    "未来研究方向提及", "未来研究方向思考",
]

PROJECTS = {
    "project-1": ("双光子", "core"),
    "project-2": ("Mn多铁", "strong"),
    "project-3": ("机械发光", "medium"),
    "project-4": ("TTF", "strong"),
    "project-5": ("SnTe", "strong"),
    "project-6": ("湿度", "strong"),
    "project-7": ("CDW", "core"),
}

# Relevance-level keywords scanned inside each project's paragraph.
LEVEL_HINTS = [
    ("core", ["核心", "旗舰", "必须引用", "直接是项目", "core"]),
    ("strong", ["强相关", "直接参考", "直接可复用", "高度相关", "strong"]),
    ("medium", ["中等", "方法学参考", "明确类比", "可借鉴", "medium"]),
    ("weak", ["弱", "形式上", "间接", "边缘", "weak"]),
]

# Methods recognised by keyword in the full body (kebab output form).
METHOD_KEYWORDS = {
    "dft": ["dft", "密度泛函", "vasp", "quantum espresso", "abinit", "wien2k", "第一性原理"],
    "dft-plus-u": ["dft+u", "ldau", "dudarev"],
    "berry-phase": ["berry", "贝里", "极化理论", "born effective", "玻恩有效电荷"],
    "gw": [" gw ", "g0w0", "evgw"],
    "md": ["分子动力学", "molecular dynamics", " md ", "lammps", "moldy"],
    "mlip": ["机器学习势", "深度势", "deep potential", "neural network potential", "mlip", "dp-gen", "gaussian approximation potential", "gap"],
    "eam": ["嵌入原子", "eam", "embedded atom"],
    "dfpt": ["dfpt", "密度泛函微扰", "线性响应"],
    "neb": ["nudged elastic band", "neb", "过渡态"],
    "monte-carlo": ["monte carlo", "蒙特卡洛", "mc "],
    "stm-mbe": ["stm", "扫描隧道", "mbe", "分子束外延"],
    "afm-pfm": ["pfm", "压电力显微镜", "afm", "原子力显微镜"],
    "mfm": ["mfm", "磁力显微镜"],
    "tem": ["tem", "透射电镜", "stem", "haadf", "saed"],
    "xrd": ["xrd", "x射线衍射", "pxrd", "rsm", "倒易空间"],
    "raman": ["拉曼", "raman"],
    "xps": ["xps", "x射线光电子"],
    "squid": ["squid", "vsm", "磁强计"],
    "muon-sr": ["μsr", "musr", "muon", "缪子"],
    "arpes": ["arpes"],
    "xanes": ["xanes", "xas", "exafs", "x射线吸收", "xrs", "拉曼"],
    "epr": [" epr", "esr", "电子顺磁", "电子自旋共振"],
    "nmr": ["nmr", "核磁共振"],
    "fdtd": ["fdtd", "有限差分时域"],
    "device-i-v": ["i-v", "电流-电压", "开关比", "光电流", "阻抗", "nyquist"],
    "spectroscopy": ["吸收光谱", "光致发光", "荧光", "紫外可见", "椭圆偏振"],
    "phase-field": ["相场", "phase-field", "tdgl", "ginzburg-landau"],
    "tight-binding": ["紧束缚", "tight-binding"],
    "rw-cpa": ["coherent potential"],
}

TOPIC_KEYWORDS = {
    "multiferroics": ["多铁", "multiferroic", "磁电耦合", "magnetoelectric"],
    "2d-materials": ["二维", "2d", "单层", "monolayer", "van der waals", "vdw", "范德华"],
    "ferroelectricity": ["铁电", "ferroelectric", "极化翻转", "polarization switching"],
    "ferromagnetism": ["铁磁", "ferromag", "反铁磁", "antiferromag"],
    "charge-density-wave": ["电荷密度波", "cdw", "charge density wave", "peierls", "派尔斯"],
    "superconductivity": ["超导", "superconduc"],
    "topological-defects": ["斯格明子", "skyrmion", "涡旋", "vortex", "domain wall", "畴壁", "topological"],
    "strain-engineering": ["应变工程", "strain engineer", "失配应变", "压电"],
    "humidity-sensing": ["湿度", "moisture", "humidity", "水吸附"],
    "two-photon-fluorescence": ["双光子", "two-photon", "tpa", "tpef"],
    "molecular-crystal": ["分子晶体", "molecular crystal", "ttf", "bedt-ttf", "电荷转移盐"],
    "ml-interatomic-potential": ["机器学习势", "深度势", "neural network potential", "mlip"],
    "mxene": ["mxene", "max相"],
    "mof": ["mof", "金属有机框架", "metal-organic framework"],
    "domain-walls": ["畴壁", "domain wall"],
    "polarization": ["极化", "polarization"],
    "optical-spectra": ["光学性质", "介电函数", "吸收谱", "optical"],
    "phase-transition": ["相变", "phase transition"],
}


def parse_note_meta(note_path: Path) -> dict:
    text = note_path.read_text(encoding="utf-8", errors="replace")
    meta: dict = {}
    # YAML header at very top
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"([^:]+):\s*(.*)", line)
            if mm:
                meta[mm.group(1).strip()] = mm.group(2).strip()
    # Metadata table: |key|value|
    table = {}
    for tm in re.finditer(r"^\s*>\s*\|([^|\n]+)\|(.*)\|$", text, re.M):
        key = tm.group(1).strip()
        val = tm.group(2).strip()
        if key and key not in ("Key", "--:", ":--"):
            table[key] = val
    return {"yaml": meta, "table": table, "text": text}


def md_list(items: list[str]) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(items) + "]"


def yq(s: str) -> str:
    """Quote a scalar for YAML."""
    s = s.strip().replace('"', "'")
    return f'"{s}"'


def extract_authors(table: dict) -> list[str]:
    raw = table.get("作者", "")
    names = re.findall(r"\[\[([^\]]+)\]\]", raw)
    if not names:
        # fall back: split by commas / 、
        names = [p.strip() for p in re.split(r"[、,，]", raw) if p.strip()]
    return names[:8]


def extract_doi(table: dict) -> str:
    raw = table.get("DOI", "")
    m = re.search(r"10\.\d{3,9}/[^\s\])]+", raw)
    return m.group(0) if m else ""


def extract_year(table: dict, note_text: str, citekey: str) -> int | None:
    for key in ("日期", "年份", "year"):
        v = table.get(key, "")
        m = re.search(r"(19|20)\d{2}", v)
        if m:
            return int(m.group(0))
    m = re.search(r"(19|20)\d{2}", citekey)
    if m:
        return int(m.group(0))
    m = re.search(r"(19|20)\d{2}", note_text[:2000])
    return int(m.group(0)) if m else None


def parse_links(body: str) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {"concepts": [], "entities": [], "figures": [], "writes": [], "projects": []}
    for m in re.finditer(r"\[\[\.\./\.\./wiki/(concepts|entities|figures|write|projects)/([^\]|]+)", body):
        kind = m.group(1)
        name = m.group(2).rstrip("/").strip()
        if kind == "write":
            key = "writes"
        else:
            key = kind
        if name not in out[key]:
            out[key].append(name)
    return out


def parse_project_section(body: str) -> dict[str, str]:
    """Return {project-N: level} by reading the 项目连接 bullet block."""
    m = re.search(r"\*\*项目连接\*\*[:：]?\s*(.+?)(?=\n- \*\*|\n## |\Z)", body, re.S)
    if not m:
        return {}
    block = m.group(1)
    result: dict[str, str] = {}
    # split into project chunks
    chunks = re.split(r"(?=(?:project-\d|Project-\d|project\s*\d))", block)
    for ch in chunks:
        pm = re.match(r"\s*(?:project-|Project-|project\s*)(\d)", ch, re.I)
        if not pm:
            continue
        pid = f"project-{pm.group(1)}"
        level = "medium"
        for lvl, hints in LEVEL_HINTS:
            if any(h in ch for h in hints):
                level = lvl
                break
        if "无" in ch[:40] and "相关" in ch[:40]:
            continue
        result[pid] = level
    return result


def collect_keywords(body: str, mapping: dict[str, list[str]]) -> list[str]:
    low = body.lower()
    found = []
    for tag, kws in mapping.items():
        if any(k.lower() in low for k in kws):
            found.append(tag)
    return found


def infer_paper_type(table: dict, body: str) -> str:
    genre = table.get("文献类型", "").lower()
    if "review" in genre or "综述" in body[:2000]:
        return "review"
    if "perspective" in genre or "perspective" in body[:2000].lower():
        return "perspective"
    methods = collect_keywords(body[:4000], METHOD_KEYWORDS)
    if not any(m in methods for m in ("stm-mbe", "tem", "xrd", "raman", "xps", "afm-pfm", "squid", "muon-sr", "arpes", "device-i-v", "epr", "nmr", "spectroscopy")):
        return "theory"
    if "dft" in methods or "md" in methods or "mlip" in methods:
        return "experiment"  # mixed
    return "experiment"


def build_frontmatter(citekey: str, body: str, meta: dict) -> str:
    table = meta["table"]
    title = table.get("标题", "").strip() or meta["yaml"].get("中文标题", citekey)
    short = table.get("短标题", "").strip()
    authors = extract_authors(table)
    journal = table.get("期刊名称", "")
    journal = re.sub(r"^\[\[|\]\]$", "", journal).strip()
    doi = extract_doi(table)
    year = extract_year(table, meta["text"], citekey)

    links = parse_links(body)
    proj_levels = parse_project_section(body)
    methods = collect_keywords(body, METHOD_KEYWORDS)
    topics = collect_keywords(body, TOPIC_KEYWORDS)
    paper_type = infer_paper_type(table, body)

    materials: list[str] = []
    for ent in links["entities"]:
        if ent.lower() not in ("vasp", "wannier90", "quantum-espresso", "abinit", "lammps"):
            materials.append(ent)

    lines = ["---"]
    lines.append(f"citekey: {citekey}")
    lines.append(f"title: {yq(title)}")
    if short:
        lines.append(f"title_zh: {yq(short)}")
    lines.append(f"authors: {md_list(authors)}")
    if year:
        lines.append(f"year: {year}")
    if journal:
        lines.append(f"journal: {yq(journal)}")
    if doi:
        lines.append(f'doi: "{doi}"')
        lines.append(f'url: "https://doi.org/{doi}"')
    lines.append(f"paper_type: {paper_type}")
    lines.append("status: ingested")
    lines.append("year_read: 2026")
    lines.append(f'original_note: "[[../../raw/note/{citekey}]]"')
    lines.append(f"projects: {md_list(sorted(proj_levels))}")
    lines.append(f"concepts: {md_list(sorted(set(links['concepts'])))}")
    lines.append(f"entities: {md_list(sorted(set(links['entities'])))}")
    lines.append(f"methods: {md_list(sorted(set(methods)))}")
    lines.append(f"materials: {md_list(sorted(set(materials)))}")
    lines.append(f"figures: {md_list(sorted(set(links['figures'])))}")

    mx = MATRIX.get(citekey, {})
    for f in MATRIX_FIELDS:
        val = mx.get(f, "")
        if not val:
            val = "（原始笔记未提供该字段，待第二步重写时补全）"
        # YAML folded block scalar
        lines.append(f'"{f}": >-')
        for para in val.split("\n"):
            lines.append(f"  {para}")

    lines.append("tags:")
    lines.append("  - paper")
    lines.append(f"  - type/{paper_type}")
    if year:
        lines.append(f"  - year/{year}")
    for pid in sorted(proj_levels):
        lines.append(f"  - project/{pid}")
        lines.append(f"  - relevance/{pid}/{proj_levels[pid]}")
    for c in sorted(set(links["concepts"])):
        lines.append(f"  - concept/{c}")
    for e in sorted(set(links["entities"])):
        lines.append(f"  - entity/{e}")
    for mt in sorted(set(methods)):
        lines.append(f"  - method/{mt}")
    for mat in sorted(set(materials)):
        lines.append(f"  - material/{mat}")
    for t in sorted(set(topics)):
        lines.append(f"  - topic/{t}")
    lines.append("---")
    return "\n".join(lines)


def main() -> None:
    count = 0
    skipped = 0
    for md in sorted(INGEST.glob("*.md")):
        if md.name.startswith("_"):
            continue
        text = md.read_text(encoding="utf-8")
        if text.startswith("---"):
            skipped += 1
            continue
        citekey = md.stem
        note_path = NOTES / f"{citekey}.md"
        if not note_path.exists():
            print(f"WARN: no note for {citekey}")
            continue
        meta = parse_note_meta(note_path)
        fm = build_frontmatter(citekey, text, meta)
        md.write_text(fm + "\n\n" + text.lstrip(), encoding="utf-8", newline="\n")
        count += 1
        print(f"backfilled {citekey}")
    print(f"\ndone: backfilled {count}, already-had-frontmatter {skipped}")


if __name__ == "__main__":
    main()
