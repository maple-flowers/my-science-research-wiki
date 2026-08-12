import os, re, io, sys, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
PAP = os.path.join(BASE, "wiki", "papers")

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

stats = {"files": 0, "links": 0, "already": 0, "no_project": 0}

for fn in sorted(os.listdir(PAP)):
    if not fn.endswith(".md"):
        continue
    citekey = fn[:-3]
    p = os.path.join(PAP, fn)
    txt = open(p, encoding="utf-8").read()

    # Determine authoritative project list: frontmatter first
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

    # If no frontmatter, parse connection section (skip exclusionary bullets)
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

    if not authoritative:
        stats["no_project"] += 1
        continue

    # Build link block
    link_block = "## 🔗 项目双链\n"
    for num in authoritative:
        name = proj_names.get(num, num)
        link_block += "- 项目 [[../projects/{}|{}]]\n".format(PROJ_SLUGS.get(num, num), name)
        stats["links"] += 1

    # Find insertion point: after the entire ## 🔬 项目连接 section content
    conn_m = re.search(r"## 🔬 项目连接\s*\n(.*?)(?=\n## |\Z)", txt, re.DOTALL)
    if conn_m:
        insert_pos = conn_m.end()
        # Idempotency: check if ANY 项目双链 block already exists after 项目连接
        after = txt[insert_pos : insert_pos + 300]
        if "## 🔗 项目双链" in after:
            stats["already"] += 1
            continue
        new_txt = txt[:insert_pos] + "\n" + link_block + txt[insert_pos:]
    else:
        # No 项目连接 section - append at end
        if link_block.rstrip() in txt:
            stats["already"] += 1
            continue
        new_txt = txt.rstrip() + "\n\n" + link_block

    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_txt)
    stats["files"] += 1

print(json.dumps(stats, ensure_ascii=False, indent=1))
