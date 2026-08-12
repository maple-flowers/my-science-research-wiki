import json, os, sys
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

# Verify uniqueness
for name, sub in [('sub1', sub1), ('sub2', sub2), ('sub3', sub3)]:
    ck = [e['citekey'] for e in sub]
    dupes = [k for k in set(ck) if ck.count(k) > 1]
    if dupes:
        print(f'WARNING {name} dupes: {dupes}')
    else:
        print(f'{name}: OK, {len(sub)} entries, all unique citekeys')

print(f'Total: {len(sub1)+len(sub2)+len(sub3)}/148')
