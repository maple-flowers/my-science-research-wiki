import re, os, io, sys, glob
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

PAPERS = "wiki/papers"

def frontmatter(text):
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    return parts[1] if len(parts) > 2 else ""

def field(fm, key):
    """Return list of values for a frontmatter key (inline [a, b] or block '- a')."""
    m = re.search(r'^%s:[ \t]*(.*)$' % key, fm, re.M)
    if not m:
        return []
    rest = m.group(1).strip()
    if rest.startswith('['):
        return [x.strip().strip('"\'') for x in rest[1:-1].split(',') if x.strip()]
    if rest:
        return [rest.strip('"\'')]
    # block list
    tail = fm[m.end():]
    out = []
    for line in tail.split('\n')[1:]:
        if re.match(r'^\s*-\s+', line):
            out.append(re.sub(r'^\s*-\s+', '', line).strip().strip('"\''))
        elif line.strip() == '':
            continue
        else:
            break
    return out

corpus = []
for path in sorted(glob.glob(os.path.join(PAPERS, "*.md"))):
    t = open(path, encoding='utf-8', errors='replace').read()
    fm = frontmatter(t)
    if re.search(r'multiferro|magnetoelectric', fm, re.I):
        corpus.append((os.path.basename(path)[:-3], fm))

print("matched papers: %d / %d (frontmatter contains 'multiferro' or 'magnetoelectric', case-insensitive)"
      % (len(corpus), len(glob.glob(os.path.join(PAPERS, '*.md')))))

def report(key, topn):
    c = Counter()
    where = {}
    for ck, fm in corpus:
        for v in field(fm, key):
            c[v] += 1
            where.setdefault(v, []).append(ck)
    print("\n===== %s (top %d, distinct=%d) =====" % (key, topn, len(c)))
    for v, n in c.most_common(topn):
        print("%3d  %-42s %s" % (n, v, ", ".join(where[v][:3])))

report("methods", 30)
report("materials", 15)
report("entities", 15)
report("concepts", 20)

for key in ("year", "paper_type", "journal"):
    c = Counter()
    for ck, fm in corpus:
        for v in field(fm, key):
            c[v] += 1
    print("\n===== %s =====" % key)
    items = sorted(c.items()) if key == "year" else c.most_common(12)
    for v, n in items:
        print("%3d  %s" % (n, v))
