import os, re, io, sys, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
PAP = os.path.join(BASE, "wiki", "papers")
CON = os.path.join(BASE, "wiki", "concepts")
ENT = os.path.join(BASE, "wiki", "entities")

PROJ_SLUGS = {
    "project-1": "project-1-two-photon",
    "project-2": "project-2-mn-multiferroics",
    "project-3": "project-3-mechanoluminescence-nn",
    "project-4": "project-4-ttf-molecular-calc",
    "project-5": "project-5-snte-ferroelectric-sim",
    "project-6": "project-6-humidity-sensor",
    "project-7": "project-7-cdw-charge-density-wave",
}

proj_names = {}
for num, slug in PROJ_SLUGS.items():
    p = os.path.join(BASE, "wiki", "projects", slug + ".md")
    if os.path.exists(p):
        txt = open(p, encoding="utf-8").read()
        m = re.search(r"^# (.+)$", txt, re.M)
        if m:
            proj_names[num] = m.group(1)

# Build Chinese -> (slug, type) map from concept/entity H1 titles
cn_map = {}
for d, typ in [(CON, "concept"), (ENT, "entity")]:
    for fn in os.listdir(d):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        txt = open(os.path.join(d, fn), encoding="utf-8").read()
        m = re.match(r"^# ([^/\(]+)", txt)
        if m:
            cn = m.group(1).strip()
            if cn and cn not in cn_map:
                cn_map[cn] = (slug, typ)

# Also index existing wikilink text in papers
for fn in os.listdir(PAP):
    if not fn.endswith(".md"):
        continue
    txt = open(os.path.join(PAP, fn), encoding="utf-8").read()
    for m in re.finditer(r"\[\[../(?:concepts|entities)/([^\]|]+)\|([^\]]+)\]\]", txt):
        cn = m.group(2)
        if cn not in cn_map:
            cn_map[cn] = (m.group(1), "concept")

print("Loaded {} term mappings".format(len(cn_map)))

stats = {"files": 0, "links": 0, "already": 0, "no_project": 0}

for fn in sorted(os.listdir(PAP)):
    if not fn.endswith(".md"):
        continue
    citekey = fn[:-3]
    p = os.path.join(PAP, fn)
    txt = open(p, encoding="utf-8").read()
    original_txt = txt
    changed = False

    # === PART 1: Project double-link ===
    # Only add if NO 项目双链 section exists anywhere in the file
    if "## 🔗 项目双链" not in txt:
        # Determine authoritative projects from frontmatter
        authoritative = []
        fm = re.search(r"^---\n(.*?)\n---", txt, re.DOTALL)
        if fm:
            pm = re.search(r"^projects:\s*\[(.*?)\]", fm.group(1), re.M | re.DOTALL)
            if pm:
                seen = set()
                for pn in re.findall(r"project-\d+", pm.group(1)):
                    if pn not in seen:
                        seen.add(pn)
                        authoritative.append(pn)

        # If no frontmatter, parse connection section (skip exclusionary)
        if not authoritative:
            conn_m = re.search(r"## 🔬 项目连接\s*\n(.*?)(?=\n## |\Z)", txt, re.DOTALL)
            if conn_m:
                conn = conn_m.group(1)
                for line in conn.split("\n"):
                    line = line.strip()
                    if not line.startswith("- "):
                        continue
                    if any(kw in line for kw in ["无关", "不评", "无直接连接", "无直接", "间接呼应"]):
                        continue
                    for pn in re.findall(r"project-\d+", line):
                        if pn not in authoritative:
                            authoritative.append(pn)

        if authoritative:
            link_block = "## 🔗 项目双链\n"
            for num in authoritative:
                name = proj_names.get(num, num)
                link_block += "- 项目 [[../projects/{}|{}]]\n".format(PROJ_SLUGS.get(num, num), name)
                stats["links"] += 1

            # Insert after 项目连接 section
            conn_m = re.search(r"## 🔬 项目连接\s*\n(.*?)(?=\n## |\Z)", txt, re.DOTALL)
            if conn_m:
                insert_pos = conn_m.end()
                txt = txt[:insert_pos] + "\n" + link_block + txt[insert_pos:]
                changed = True
                stats["files"] += 1

    # === PART 2: Linkify terms in 组织与用词 ===
    org_m = re.search(r"## 📝 组织与用词\s*\n(.*?)(?=\n## |\Z)", txt, re.DOTALL)
    if org_m:
        section = org_m.group(1)
        new_section = section
        linked_in_section = 0

        for line in section.split("\n"):
            stripped = line.strip()
            if not stripped.startswith("- "):
                continue
            if "值得" in stripped and "术语" in stripped:
                continue
            if "[[" in stripped:
                continue  # already linked

            # Remove English in parentheses/brackets
            clean = re.sub(r"（[^）]*）", "", stripped)
            clean = re.sub(r"\([^)]*\)", "", clean)
            clean = re.sub(r"^[-\s]+", "", clean)
            parts = [p.strip() for p in re.split(r"[、，,/]", clean) if p.strip()]

            new_line = stripped
            for part in parts:
                if part in cn_map:
                    slug, typ = cn_map[part]
                    link = "[[../{}/{}|{}]]".format(typ + "s", slug, part)
                    new_line = new_line.replace(part, part + " " + link, 1)
                    linked_in_section += 1
                    break

            if new_line != stripped:
                new_section = new_section.replace(stripped, new_line, 1)

        if linked_in_section > 0:
            start_pos = org_m.start()
            end_pos = org_m.end()
            txt = txt[:start_pos] + "## 📝 组织与用词\n" + new_section + txt[end_pos:]
            changed = True
            stats["links"] += linked_in_section

    if changed:
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(txt)
        stats["files"] += 1

# Count how many were already done (changed=False)
for fn in sorted(os.listdir(PAP)):
    if not fn.endswith(".md"):
        continue
    p = os.path.join(PAP, fn)
    txt = open(p, encoding="utf-8").read()
    if "## 🔗 项目双链" in txt and "## 📝 组织与用词" in txt:
        # Check if org terms have links
        org_m = re.search(r"## 📝 组织与用词\s*\n(.*?)(?=\n## |\Z)", txt, re.DOTALL)
        if org_m and "[[" in org_m.group(1):
            stats["already"] += 1

print(json.dumps(stats, ensure_ascii=False, indent=1))
