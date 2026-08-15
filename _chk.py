import re, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
path = sys.argv[1]
base = os.path.dirname(path)
t = open(path, encoding='utf-8').read()
bad = []; seen = set()
for m in re.finditer(r'\[\[([^\]|#]+?)(?:\\?\|[^\]]*)?\]\]', t):
    tgt = m.group(1).strip().rstrip('\\').strip()
    if tgt in seen: continue
    seen.add(tgt)
    p = os.path.normpath(os.path.join(base, tgt + '.md'))
    if not os.path.exists(p): bad.append(tgt)
print("total unique links:", len(seen))
print("DANGLING (%d):" % len(bad))
for b in bad: print("  ", b)
