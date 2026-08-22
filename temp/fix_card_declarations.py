#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 wiki/papers/ 卡片 frontmatter 里 concepts:/entities: 的失效声明。

映射来源：tools/audit_wiki_pages.py --papers-xref 的三类 dangling，逐条人工核定。
默认 dry-run，加 --apply 才写盘。只改 concepts:/entities: 两个字段，其余逐字保留。幂等。
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PAPERS = REPO / 'wiki' / 'papers'
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

# 目标写法：'concepts/<slug>' 或 'entities/<slug>'；None = 库中确无对应页，保留不动
MAP = {
    # ── 层写错（页存在于另一层）──
    'entities/LAPW': 'concepts/LAPW',
    'entities/Car-Parrinello': 'concepts/Car-Parrinello',
    'entities/PBE-functional': 'concepts/PBE-functional',
    'concepts/max-phase': 'entities/MAX-phase',
    'concepts/sc2co2': 'entities/Sc2CO2',
    # ── 单复数 / 词序 / 拼写变体 ──
    'concepts/domain-walls': 'concepts/domain-wall',
    'concepts/skyrmions': 'concepts/skyrmion',
    'concepts/bessel-beams': 'concepts/bessel-beam',
    'entities/MAX-phases': 'entities/MAX-phase',
    'entities/carbon-nanotubes': 'entities/carbon-nanotube',
    'concepts/kittels-law': 'concepts/kittel-law',
    'concepts/landau-ginzburg': 'concepts/ginzburg-landau',
    'concepts/pseudo-gap': 'concepts/pseudogap',
    'concepts/optical-bandgap': 'concepts/optical-band-gap',
    'concepts/charge-ordering': 'concepts/charge-order',
    'concepts/excitonic-condensation': 'concepts/exciton-condensation',
    'concepts/locally-excited-state': 'concepts/local-excited-state',
    'concepts/depolarizing-field': 'concepts/depolarization-field',
    'concepts/evanescent-wave': 'concepts/evanescent-field',
    'concepts/kosterlitz-thouless-transition': 'concepts/kosterlitz-thouless',
    'concepts/soft-mode-phonon': 'concepts/phonon-soft-mode',
    'concepts/soft-phonon-mode': 'concepts/phonon-soft-mode',
    'concepts/magnetic-anisotropy-energy': 'concepts/magnetic-anisotropy',
    'concepts/electronic-band-structure': 'concepts/band-structure',
    'concepts/bader-charge-analysis': 'concepts/bader-analysis',
    'concepts/mulliken-population-analysis': 'concepts/mulliken-population',
    'concepts/resistive-switching-memory': 'concepts/resistive-switching',
    'concepts/self-consistent-field': 'concepts/self-consistent-field-cycle',
    'concepts/dft-plus-u': 'concepts/DFT-U',
    'concepts/car-parrinello-method': 'concepts/Car-Parrinello',
    'concepts/peierls-transition': 'concepts/peierls-distortion',
    'concepts/helical-spin-order': 'concepts/helical-magnetism',
    'concepts/inverse-dm-interaction': 'concepts/inverse-dzyaloshinskii-moriya',
    'concepts/llg-equation': 'concepts/landau-lifshitz-equation',
    'concepts/first-order-transition': 'concepts/first-order-phase-transition',
    # ── 缩写 ↔ 全称（机器匹配不到，人工核定）──
    'concepts/projector-augmented-wave': 'concepts/paw-method',
    'concepts/polar-vortices': 'concepts/polar-vortex',
    'concepts/twisted-intramolecular-charge-transfer': 'concepts/tict-mechanism',
    'concepts/ab-initio-molecular-dynamics': 'concepts/aimd',
    'concepts/type-ii-multiferroics': 'concepts/type-i-type-ii-multiferroics',
    'concepts/type-ii-multiferroic': 'concepts/type-i-type-ii-multiferroics',
    'concepts/pfm-piezoresponse-force-microscopy': 'entities/PFM',
    'concepts/pump-probe-technique': 'entities/pump-probe',
    'concepts/cneb': 'concepts/nudged-elastic-band',
    'concepts/gga-functional': 'concepts/exchange-correlation-functional',
    # ── 推拉结构的四种写法 ──
    'concepts/d-pi-a-structure': 'concepts/d-pi-a-architecture',
    'concepts/donor-pi-acceptor': 'concepts/d-pi-a-architecture',
    'concepts/donor-acceptor-push-pull': 'concepts/d-pi-a-architecture',
    'concepts/push-pull-chromophore': 'concepts/d-pi-a-architecture',
    # ── 材料实体 ──
    'entities/gold': 'entities/Au',
    'entities/titanium-sapphire-laser': 'entities/Ti-sapphire-laser',
    'entities/Ti-Sa-laser': 'entities/Ti-sapphire-laser',
    'concepts/half-metal': 'concepts/half-metallicity',
    # ── 库中确无对应页，等新建后再回填 ──
    'concepts/higher-order-topology': None,
}

FM_RE = re.compile(r'\A(---\s*\r?\n)(.*?)(\r?\n---[ \t]*\r?\n)', re.DOTALL)


def parse_field(fm, key):
    """返回 (items, kind, span)；kind 为 'inline'/'block'/None。"""
    m = re.search(r'^' + re.escape(key) + r'[ \t]*:[ \t]*(.*)$', fm, re.M)
    if not m:
        return [], None, None
    inline = m.group(1).strip()
    if inline:
        body = inline[1:-1] if inline.startswith('[') and inline.endswith(']') else inline
        items = [x.strip().strip('"\'') for x in body.split(',') if x.strip()]
        return items, 'inline', (m.start(), m.end())
    items, end = [], m.end()
    rest = fm[m.end():]
    # 跳过字段行末尾的换行，否则首个 splitlines 元素为空行会立刻终止解析
    lead = re.match(r'\r?\n', rest)
    if lead:
        end += lead.end()
        rest = rest[lead.end():]
    for line in rest.splitlines(keepends=True):
        if re.match(r'^\s*-\s+', line):
            items.append(re.sub(r'^\s*-\s+', '', line).strip().strip('"\''))
            end += len(line)
        elif line.strip() and not line.startswith((' ', '\t')):
            break
        elif not line.strip():
            break
        else:
            end += len(line)
    return items, 'block', (m.start(), end)


def render(key, items, kind, nl='\n'):
    if kind == 'inline':
        return f"{key}: [{', '.join(items)}]"
    # block：span 覆盖到最后一项的行尾换行，故这里必须补回换行，否则会与下个字段粘连
    return f"{key}:{nl}" + nl.join(f'  - {x}' for x in items) + nl


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='真正写盘（默认 dry-run）')
    args = ap.parse_args()

    total_fix = 0
    touched = []
    for card in sorted(PAPERS.glob('*.md')):
        raw = card.read_text(encoding='utf-8')
        m = FM_RE.match(raw)
        if not m:
            continue
        head, fm, tail = m.group(1), m.group(2), m.group(3)
        fields = {}
        for key in ('concepts', 'entities'):
            items, kind, span = parse_field(fm, key)
            fields[key] = {'items': items, 'kind': kind, 'span': span}
        moves = {'concepts': [], 'entities': []}
        changes = []
        for key in ('concepts', 'entities'):
            newitems = []
            for it in fields[key]['items']:
                tgt = MAP.get(f'{key}/{it}')
                if tgt is None:
                    newitems.append(it)
                    continue
                tlayer, tslug = tgt.split('/', 1)
                changes.append(f'{key}/{it} -> {tgt}')
                if tlayer == key:
                    newitems.append(tslug)
                else:
                    moves[tlayer].append(tslug)
            fields[key]['new'] = newitems
        for key in ('concepts', 'entities'):
            for s in moves[key]:
                if s not in fields[key]['new']:
                    fields[key]['new'].append(s)
        if not changes:
            continue
        # 去重保序
        for key in ('concepts', 'entities'):
            seen, out = set(), []
            for x in fields[key]['new']:
                if x not in seen:
                    seen.add(x)
                    out.append(x)
            fields[key]['new'] = out
        # 从后往前替换，避免 span 失效
        newfm = fm
        for key in sorted(('concepts', 'entities'),
                          key=lambda k: -(fields[k]['span'][0] if fields[k]['span'] else -1)):
            f = fields[key]
            if f['span'] is None or f['new'] == f['items']:
                continue
            s, e = f['span']
            nl = '\r\n' if '\r\n' in fm else '\n'
            newfm = newfm[:s] + render(key, f['new'], f['kind'], nl) + newfm[e:]
        total_fix += len(changes)
        touched.append((card.name, changes))
        if args.apply and newfm != fm:
            card.write_text(head + newfm + tail + raw[m.end():], encoding='utf-8', newline='')

    for name, changes in touched:
        print(f'{name}')
        for c in changes:
            print(f'    {c}')
    print(f'\n涉及卡片 {len(touched)} 张，修复声明 {total_fix} 条'
          + ('（已写盘）' if args.apply else '（dry-run，未写盘）'))


if __name__ == '__main__':
    main()
