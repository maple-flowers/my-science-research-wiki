import json, io, os
done = ['wiki/concepts/goodenough-kanamori-anderson-rules.md',
        'wiki/concepts/surface-premelting.md',
        'wiki/concepts/mixed-valence.md',
        'wiki/concepts/monolithic-integration.md',
        'wiki/entities/black-phosphorus.md',
        'wiki/entities/GaN.md']
p = 'temp/phaseH_placeholder_manifest.json'
m = json.load(io.open(p, encoding='utf-8'))
before = len(m)
norm = set(done)
m = [e for e in m if e['path'].replace(os.sep, '/') not in norm]
json.dump(m, io.open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(before, '->', len(m))
for d in done:
    if '本页内容待重写' in io.open(d, encoding='utf-8').read():
        print('SENTINEL LEFT', d)
