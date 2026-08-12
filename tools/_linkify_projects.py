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

# Load project names from files
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

    # Find project connection section (include optional 项目双链 subsection)
    m = re.search(r"## 🔬 项目连接\s*\n(.*?)(?:\n## 🔗 项目双链\s*\n(.*?))?(?=\n## |\Z)", txt, re.DOTALL)
    if not m:
        continue
    section = m.group(1)
    start_pos = m.start()
    end_pos = m.end()

    # Check if already linked (check both main section and 双链 subsection)
    if "[[../projects/" in section or "[[../projects/" in (m.group(2) or ""):
        stats["already"] += 1
        continue

    # Find unique project-N references (preserve order, deduplicate)
    found = []
    seen = set()
    for pm in re.finditer(r"project-(\d+)", section):
        num = pm.group(0)
        if num not in seen:
            seen.add(num)
            found.append(num)

    if not found:
        stats["no_project"] += 1
        continue

    # Build replacement section
    # Strategy: add a "## 🔗 项目双链" subsection at the end of the project connection section
    link_lines = "\n## 🔗 项目双链\n"
    for num in found:
        slug = PROJ_SLUGS.get(num, num)
        name = proj_names.get(num, num)
        link_lines += "- 项目 [[../projects/{}|{}]]\n".format(slug, name)
        stats["links"] += 1

    new_section = section.rstrip() + link_lines
    new_txt = txt[:start_pos] + "## 🔬 项目连接\n" + new_section + txt[end_pos:]

    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_txt)
    stats["files"] += 1

print(json.dumps(stats, ensure_ascii=False, indent=1))
