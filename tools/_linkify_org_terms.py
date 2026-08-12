import os, re, io, sys, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
PAP = os.path.join(BASE, "wiki", "papers")
CON = os.path.join(BASE, "wiki", "concepts")
ENT = os.path.join(BASE, "wiki", "entities")

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

stats = {"files": 0, "linked": 0, "already": 0, "no_match": 0}

for fn in sorted(os.listdir(PAP)):
    if not fn.endswith(".md"):
        continue
    citekey = fn[:-3]
    p = os.path.join(PAP, fn)
    txt = open(p, encoding="utf-8").read()

    # Find 组织与用词 section
    m = re.search(r"## 📝 组织与用词\s*\n(.*?)(?=\n## |\Z)", txt, re.DOTALL)
    if not m:
        continue
    section = m.group(1)
    start_pos = m.start()
    end_pos = m.end()

    # Check if already fully linked
    plain = [l for l in section.split("\n") if l.strip().startswith("- ") and "[[" not in l and "值得" not in l]
    if not plain:
        stats["already"] += 1
        continue

    # Process bullets
    new_section = section
    linked = 0
    for line in section.split("\n"):
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        if "值得" in stripped and "术语" in stripped:
            continue
        if "[[" in stripped:
            continue

        # Remove English in parentheses/brackets, then split by 、 / ,
        clean = re.sub(r"（[^）]*）", "", stripped)
        clean = re.sub(r"\([^)]*\)", "", clean)
        clean = re.sub(r"^[-\s]+", "", clean)
        parts = [p.strip() for p in re.split(r"[、，/,]", clean) if p.strip()]

        new_line = stripped
        for part in parts:
            if part in cn_map:
                slug, typ = cn_map[part]
                link = "[[../{}/{}|{}]]".format(typ + "s", slug, part)
                new_line = new_line.replace(part, part + " " + link, 1)
                linked += 1
                break

        if new_line != stripped:
            new_section = new_section.replace(stripped, new_line, 1)

    if linked == 0:
        stats["no_match"] += 1
        continue

    new_txt = txt[:start_pos] + "## 📝 组织与用词\n" + new_section + txt[end_pos:]
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_txt)
    stats["files"] += 1
    stats["linked"] += linked

print(json.dumps(stats, ensure_ascii=False, indent=1))
