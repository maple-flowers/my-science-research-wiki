import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

LIST_KEYS = ["concepts", "entities", "methods", "materials"]
SCALAR_KEYS = ["year", "journal", "paper_type"]


def field(fm, key):
    """Return a YAML field value, handling both inline [a, b] and block '- a' lists."""
    m = re.search(r'^%s:[ \t]*(.*)$' % key, fm, re.M)
    if not m:
        return None
    inline = m.group(1).strip()
    if inline:
        return inline
    # block list: consume following indented '- item' lines
    rest = fm[m.end():].split('\n')[1:]
    items = []
    for line in rest:
        s = line.strip()
        if s.startswith('- '):
            items.append(s[2:].strip())
        elif s == '':
            continue
        else:
            break
    return "[" + ", ".join(items) + "]" if items else ""


files = sys.argv[1:]
out = []
for f in files:
    try:
        t = open("wiki/papers/%s.md" % f, encoding="utf-8").read()
    except FileNotFoundError:
        out.append("########## MISSING " + f)
        continue
    out.append("########## " + f)
    fm = t.split('---', 2)[1]
    for k in SCALAR_KEYS + LIST_KEYS:
        v = field(fm, k)
        if v is not None:
            out.append("%s: %s" % (k, v))
    m = re.search(r'## .. 一句话\n(.*?)\n## ', t, re.S)
    if m:
        out.append("[ONELINE] " + m.group(1).strip())
    m = re.search(r'## .. 可写入 Wiki 的要点\n(.*)', t, re.S)
    if m:
        out.append("[POINTS]\n" + m.group(1).strip())
print("\n".join(out))
