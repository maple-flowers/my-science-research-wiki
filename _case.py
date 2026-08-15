import re, io, os, sys, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
tracked = set(subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.split('\n'))
p = sys.argv[1].replace('\\', '/')
t = open(p, encoding='utf-8').read()
base = os.path.dirname(p)
bad = []
for m in re.finditer(r'\[\[([^\]|#]+?)(?:\\?\|[^\]]*)?\]\]', t):
    tgt = m.group(1).strip().rstrip('\\').strip()
    rel = os.path.normpath(os.path.join(base, tgt + '.md')).replace('\\', '/')
    if rel not in tracked:
        bad.append(rel)
print("case-exact mismatches:", len(set(bad)))
for b in sorted(set(bad)):
    print("  ", b)
