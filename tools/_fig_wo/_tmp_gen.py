import json, os, sys, re
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

base = r'E:\swan_goose\宝宝\笔记库\sgg\科研Wiki'
with open(os.path.join(base, 'tools', '_fig_wo', 'crystal-structures.json'), 'r', encoding='utf-8') as f:
    entries = json.load(f)

distort_kw = [
    'CDW', '畸变', '畸变子晶格', 'Peierls', '磁超胞', '自旋螺旋',
    'Td 相', 'T_CDW', 'RTe₃', '铁素体晶粒', '铁素体转变', '奥氏体',
    '渗碳体', '形核', 'Ae3', 'Fe-C', '相变存储', 'Sb₂Te₃-GeTe',
    'Jahn-Teller', 'ZrI₂ T0', '声子谱', 'Wannier', '畴变体',
    'Kittel', '极化构型', 'PTO/STO', 'SrRuO₃', '超晶格',
    '铁电超导', '拓扑磁结构', 'd-K 相图', '磁性拓扑', '半子',
    '斯格明子', '涡旋畴', '磁环矩', '通量闭合畴', '高温多铁',
    '多铁隧道结', '自旋构型', 'Mulliken布居差', 'Mülliken布居',
]
surface_kw = [
    'STM 形貌', 'STM 针尖', 'HRTEM', 'X射线粉末', '重构',
    '吸附', '表面能', 'PDF', 'CsₓSi', '预熔', 'AFM', '原子堆积',
    'TEM', 'SAED', 'XRD', '光学显微', '形貌表征',
    '吸附构型', '表面吸附', '表面Mulliken', 'LPE制备',
]
table_kw = ['表', 'Table 1', 'tab_']
bulk_kw = ['ABO₃', '钙钛矿', 'perovskite', 'NiO', 'LiOsO', 'SrRuO', 'BTO',
           'BaTiO', 'SrTiO', '铁电超导', 'BiFeO', 'BiMnO', 'LuFeO',
           'BST', 'Ca₃Ru', 'CrSBr', 'CSFB', '超导穹顶', 'E-t 相图',
           'e-t 相图', '相图', 'LSDA', 'Kohn-Sham', 'RMM-DIIS',
           'WTe₂', 'NbSe', 'NbS', 'WTe2', 'IrTe2', 'IrTe₂',
           'BdG', '一维范霍夫', 'MTB原子']
computing_kw = ['泛函基准', '原子化能', 'PBE GGA', '键长平面波', 'PAW',
                'Pulay', '正交化', '过渡态', '偶极子', 'Kittel',
                'Mulliken布居差', 'Mulliken', '电荷密度差', 'Bader', '在网法',
                'Li₂', '小分子键长', 'Fe/Co/Ni 块体']

def cat(e):
    text = e['alt'] + ' ' + e['filename']
    fn = e['filename']
    if fn.startswith('tab_') or any(k in text for k in table_kw):
        return 'tables'
    surface_score = sum(1 for k in surface_kw if k in text)
    distort_score = sum(1 for k in distort_kw if k in text)
    if surface_score > distort_score:
        return 'surface'
    if distort_score > 0:
        return 'distort'
    return 'monomer'

sub1, sub2, sub3 = [], [], []
for e in entries:
    c = cat(e)
    if c == 'tables':
        sub3.append(e)
    elif c == 'surface':
        sub3.append(e)
    elif c == 'distort':
        sub2.append(e)
    else:
        sub1.append(e)

# split sub1
sub1_a, sub1_b, sub1_c = [], [], []
for e in sub1:
    text = e['alt'] + ' ' + e['filename']
    if any(k.lower() in text.lower() for k in computing_kw):
        sub1_c.append(e)
    elif any(k.lower() in text.lower() for k in bulk_kw):
        sub1_b.append(e)
    else:
        sub1_a.append(e)

print(f'sub1_a={len(sub1_a)}, sub1_b={len(sub1_b)}, sub1_c={len(sub1_c)}')
print(f'sub2={len(sub2)}, sub3={len(sub3)}')
total = len(sub1_a)+len(sub1_b)+len(sub1_c)+len(sub2)+len(sub3)
print(f'total={total}')

# Verify no duplicates within each
for name, sub in [('sub1a', sub1_a), ('sub1b', sub1_b), ('sub1c', sub1_c), ('sub2', sub2), ('sub3', sub3)]:
    ck = [e['citekey'] for e in sub]
    dupes = [k for k in set(ck) if ck.count(k) > 1]
    if dupes:
        print(f'WARN {name} dupes: {dupes}')

# Save
with open(os.path.join(base, 'tools', '_fig_wo', '_categorized.json'), 'w', encoding='utf-8') as f:
    json.dump({
        'sub1_a': sub1_a, 'sub1_b': sub1_b, 'sub1_c': sub1_c,
        'sub2': sub2, 'sub3': sub3
    }, f, ensure_ascii=False, indent=2)
print('Saved _categorized.json')
