import io, sys, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
tracked = set(subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.split('\n'))
names = [x.strip() for x in open('_cand.txt', encoding='utf-8').read().split('\n') if x.strip()]
ok, no = [], []
for n in names:
    if ('wiki/concepts/%s.md' % n) in tracked: ok.append('concepts/' + n)
    elif ('wiki/entities/%s.md' % n) in tracked: ok.append('entities/' + n)
    else: no.append(n)
print("=== HAVE (%d) ===" % len(ok))
print("\n".join(ok))
print("=== MISSING (%d) ===" % len(no))
print("\n".join(no))
