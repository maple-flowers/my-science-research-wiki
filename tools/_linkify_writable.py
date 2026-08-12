import os, re, io, sys, glob, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
PAP = os.path.join(BASE, "wiki", "papers")

# Build Chinese term -> (slug, type) map from concept/entity H1 titles
cn_map = {}
for d, typ in [("wiki/concepts", "concept"), ("wiki/entities", "entity")]:
    for fn in os.listdir(os.path.join(BASE, d)):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        t = open(os.path.join(BASE, d, fn), encoding="utf-8-sig").read()
        m = re.search(r"^# (.+)$", t, re.M)
        if m:
            zh = m.group(1).split("/")[0].strip()
            if zh and zh not in cn_map:
                cn_map[zh] = (slug, typ)

# Harvest existing |中文]] aliases used in papers
for p in glob.glob(os.path.join(PAP, "*.md")):
    t = open(p, encoding="utf-8").read()
    for m in re.finditer(r"\[\[\.\./(concepts|entities)/([^\]|]+)\|([^\]]+)\]\]", t):
        zh = m.group(3).strip()
        if zh and zh not in cn_map:
            cn_map[zh] = (m.group(2), m.group(1)[:-1])

# Filter: only keep terms that contain at least one CJK char and are >=2 chars.
# Drop generic / overly short ambiguous terms.
STOP = {
    "相", "铁电", "多铁", "磁性", "极化", "应变", "畴", "畴壁", "带隙",
    "自旋", "电子", "空穴", "声子", "光子", "轨道", "晶格", "相变", "晶体",
    "材料", "结构", "性质", "方法", "模型", "理论", "实验", "计算", "效应",
    "能量", "温度", "压力", "时间", "频率", "波长", "强度", "方向", "过程",
    "系统", "问题", "结果", "数据", "分析", "研究", "论文", "作者", "本文",
    "我们", "他们", "可以", "进行", "通过", "由于", "因此", "其中", "以及",
    "金属", "半导体", "绝缘体", "薄膜", "表面", "界面", "缺陷", "掺杂",
    "双折射",  # too generic / common word fragment
    "面内", "面外", "纵向", "横向", "内建", "内建电场",  # ambiguous modifiers
    "上", "下", "中", "间", "前", "后",  # single chars / fragments
    "本文中", "研究中",
}
# Minimum length for a CJK term to be auto-linked without boundary concern.
# Terms shorter than this are too risky as substrings.
MIN_LEN = 3
terms = []
for zh, (slug, typ) in cn_map.items():
    if len(zh) < MIN_LEN:
        continue
    if not re.search(r"[\u4e00-\u9fff]", zh):
        continue
    if zh in STOP:
        continue
    # skip terms that are mostly digits/symbols
    if re.fullmatch(r"[\u4e00-\u9fffA-Za-z0-9 \-\.·₀-₉⁰-⁹]+", zh) is None:
        continue
    terms.append((zh, slug, typ))

# Longest first so multi-word terms win
terms.sort(key=lambda x: -len(x[0]))
print("Eligible terms:", len(terms))

# Segment mask: protect wikilinks, inline/block math, code, markdown image/url.
PROTECT = re.compile(
    r"(\[\[[^\]]+\]\]"          # wikilinks
    r"|\$\$[^\$]+\$\$"           # block math
    r"|\$[^\$\n]+\$"             # inline math
    r"|`[^`]+`"                  # inline code
    r"|!\[[^\]]*\]\([^)]+\)"     # images
    r"|https?://\S+)",           # urls
)

def find_term(text, term):
    """Find first occurrence of term not part of a longer dictionary term.

    A match is rejected only if extending one char left/right (CJK adjacency)
    yields a longer term already in cn_map. This prevents '面内' matching
    inside '界面内建' while allowing '挠曲电效应' after '为'.
    """
    idx = 0
    tlen = len(term)
    while True:
        i = text.find(term, idx)
        if i < 0:
            return -1
        before = text[i - 1] if i > 0 else ""
        after = text[i + tlen] if i + tlen < len(text) else ""
        blocked = False
        if "一" <= before <= "鿿":
            if (before + term) in cn_map:
                blocked = True
        if "一" <= after <= "鿿":
            if (term + after) in cn_map:
                blocked = True
        if not blocked:
            return i
        idx = i + 1

def linkify_section(section):
    # Tokenize into protected spans vs plain text
    parts = []
    last = 0
    for m in PROTECT.finditer(section):
        if m.start() > last:
            parts.append(("text", section[last:m.start()]))
        parts.append(("prot", m.group(0)))
        last = m.end()
    if last < len(section):
        parts.append(("text", section[last:]))

    used = set()
    total_added = 0
    out = []
    for kind, seg in parts:
        if kind == "prot":
            out.append(seg)
            continue
        text = seg
        for zh, slug, typ in terms:
            if zh in used:
                continue
            i = find_term(text, zh)
            if i < 0:
                continue
            link = "[[../{}/{}|{}]]".format(typ + "s", slug, zh)
            text = text[:i] + link + text[i + len(zh):]
            used.add(zh)
            total_added += 1
        out.append(text)
    return "".join(out), total_added

stats = {"files": 0, "links": 0, "no_section": 0}
for fn in sorted(os.listdir(PAP)):
    if not fn.endswith(".md"):
        continue
    p = os.path.join(PAP, fn)
    txt = open(p, encoding="utf-8").read()

    # Find 可写入 Wiki 的要点 section (from H2 to next H2 or EOF)
    m = re.search(r"(## ✏️ 可写入 Wiki 的要点\s*\n)(.*?)(?=\n## |\Z)", txt, re.DOTALL)
    if not m:
        stats["no_section"] += 1
        continue

    header = m.group(1)
    body = m.group(2)

    # Idempotency: if section already heavily linked (has concept/entity links), skip
    if "[[../concepts/" in body or "[[../entities/" in body:
        continue

    new_body, added = linkify_section(body)
    if added == 0:
        continue

    start = m.start(2)
    end = m.end(2)
    txt = txt[:start] + new_body + txt[end:]
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)
    stats["files"] += 1
    stats["links"] += added

print(json.dumps(stats, ensure_ascii=False, indent=1))
