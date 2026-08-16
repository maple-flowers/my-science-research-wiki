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
    m = re.search(r'^%s:[ \t]*(.*)$' % key, fm, re.M)
    if not m:
        return []
    rest = m.group(1).strip()
    if rest.startswith('['):
        return [x.strip().strip('"\'') for x in rest[1:-1].split(',') if x.strip()]
    if rest:
        return [rest.strip('"\'')]
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


# Z01 corpus: anything with a computational/simulation footprint
PAT = re.compile(
    r'\bdft\b|density-functional|first-principles|molecular-dynamics|\baimd\b|\bmd\b|'
    r'machine-learning|high-throughput|monte-carlo|\bneb\b|phonon|tight-binding|'
    r'berry-phase|dftb|lammps|phase-field|micromagnetic|second-principles|'
    r'effective-hamiltonian|wannier|pseudopotential|\bgw\b|\bdfpt\b',
    re.I)

allp = sorted(glob.glob(os.path.join(PAPERS, "*.md")))
corpus = []
for path in allp:
    t = open(path, encoding='utf-8', errors='replace').read()
    fm = frontmatter(t)
    blob = "\n".join(field(fm, k) for k in () ) if False else \
        " ".join(field(fm, 'methods') + field(fm, 'concepts') + field(fm, 'entities'))
    if PAT.search(blob):
        corpus.append((os.path.basename(path)[:-3], fm))

print("Z01 corpus: %d / %d papers" % (len(corpus), len(allp)))


def report(key, topn):
    c = Counter()
    where = {}
    for ck, fm in corpus:
        for v in field(fm, key):
            c[v] += 1
            where.setdefault(v, []).append(ck)
    print("\n===== %s (top %d, distinct=%d) =====" % (key, topn, len(c)))
    for v, n in c.most_common(topn):
        print("%3d  %-40s %s" % (n, v, ", ".join(where[v][:3])))


report("methods", 45)
report("entities", 30)
report("concepts", 30)

for key in ("year", "paper_type"):
    c = Counter()
    for ck, fm in corpus:
        for v in field(fm, key):
            c[v] += 1
    print("\n===== %s =====" % key)
    items = sorted(c.items()) if key == "year" else c.most_common(12)
    for v, n in items:
        print("%3d  %s" % (n, v))
