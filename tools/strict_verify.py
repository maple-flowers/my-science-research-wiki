import os, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
WIKI = os.path.join(BASE, "wiki")
DIRS = ["concepts", "entities", "figures", "papers", "projects", "topics", "write"]

# 1. collect all markdown files + their slug (basename minus .md)
all_files = []   # absolute paths
slug_to_paths = {}  # slug -> [abs paths]
for d in DIRS:
    root = os.path.join(WIKI, d)
    if not os.path.isdir(root): continue
    for dp, _, fns in os.walk(root):
        for fn in fns:
            if fn.endswith(".md"):
                p = os.path.join(dp, fn)
                all_files.append(p)
                slug = fn[:-3]
                slug_to_paths.setdefault(slug, []).append(p)

def exists_rel(from_file, target):
    """Resolve a relative wikilink target like ../concepts/foo or ../../raw/note/bar."""
    base = os.path.dirname(from_file)
    p = os.path.normpath(os.path.join(base, target))
    if p.endswith(".md"):
        return os.path.isfile(p)
    return os.path.isfile(p + ".md") or os.path.isdir(p)

broken = []
raw_violations = []
image_missing = []
ai_residue = []
self_links = []
placeholder = []
total_wikilinks = 0
total_checked = 0

for p in sorted(all_files):
    rel = os.path.relpath(p, BASE).replace("\\", "/")
    is_paper = rel.startswith("wiki/papers/")
    txt = open(p, encoding="utf-8").read()

    if re.search(r"笔记回链|AI文献解读|由批量 ?AI ?解读|重新解读自动生成|GPT 自定", txt):
        ai_residue.append(rel)

    citekey = os.path.basename(p)[:-3] if is_paper else None
    if citekey and re.search(r"\[\[" + re.escape(citekey) + r"(\||\]\])", txt):
        self_links.append(rel)

    if re.search(r"PLHD|<citekey>|TODO|FIXME|待补", txt):
        placeholder.append(rel)

    # images
    for m in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", txt):
        link = m.group(1).strip()
        if link.startswith("http"): continue
        base = os.path.dirname(p)
        ip = os.path.normpath(os.path.join(base, link))
        if not os.path.isfile(ip):
            image_missing.append((rel, link))

    # wikilinks
    for m in re.finditer(r"\[\[([^\]]+)\]\]", txt):
        total_wikilinks += 1
        inner = m.group(1)
        target = inner.split("|")[0].split("#")[0].strip()
        if not target: continue
        if target.startswith("http"): continue

        # raw/note access policy
        if "raw/note" in target or "raw/figures" in target:
            if target.endswith(".png") or target.endswith(".jpg") or "/figures/" in target:
                # image asset references via ![]() handled above; a [[..raw/figures..]] wikilink is odd
                if not is_paper:
                    raw_violations.append((rel, target))
                continue
            if not is_paper:
                raw_violations.append((rel, target))
            # for papers, check it resolves
            if not exists_rel(p, target):
                broken.append((rel, target))
            continue

        total_checked += 1
        # relative path form
        if target.startswith("../") or target.startswith("../../") or "/" in target:
            if not exists_rel(p, target):
                broken.append((rel, target))
            continue

        # bare slug -> Obsidian resolves by basename anywhere in vault
        if target in slug_to_paths:
            continue
        # vault-absolute like 科研Wiki/wiki/...
        if target.startswith("科研Wiki/"):
            cand = os.path.join(BASE, target[len("科研Wiki/"):])
            if os.path.isfile(cand) or os.path.isfile(cand + ".md"):
                continue
        broken.append((rel, target))

print("=== STRICT WIKI VERIFICATION ===")
print(f"markdown files scanned: {len(all_files)}")
print(f"wikilinks total: {total_wikilinks} (resolved/checked: {total_checked})")
print(f"BROKEN links: {len(broken)}")
for r, t in broken[:80]:
    print(f"   {r}  ->  [[{t}]]")
if len(broken) > 80: print(f"   ... and {len(broken)-80} more")
print(f"FORBIDDEN raw/note links (non-paper pages): {len(raw_violations)}")
for r, t in raw_violations[:40]:
    print(f"   {r}  ->  [[{t}]]")
print(f"MISSING image files: {len(image_missing)}")
for r, t in image_missing[:40]:
    print(f"   {r}  ->  {t}")
print(f"AI residue pages: {len(ai_residue)}")
for r in ai_residue[:40]: print(f"   {r}")
print(f"self-link pages: {len(self_links)}")
for r in self_links[:40]: print(f"   {r}")
print(f"placeholder pages: {len(placeholder)}")
for r in placeholder[:40]: print(f"   {r}")
print("================================")
