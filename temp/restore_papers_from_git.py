# -*- coding: utf-8 -*-
"""从 git 历史 8b027c0 恢复 38 篇论文页被 b94beee 误删的正文描述章节。
策略：保留 b94beee（当前）的 frontmatter 校准，恢复 8b027c0 的正文；
恢复后修正正文中 domain-wall 的 entity→concept 链接类型。
先备份当前文件，再合并写入，最后验证 H2 章节数。"""
import re, subprocess, shutil, time
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
TEMP = Path(r"C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp")

SUSPECTS = [
    'aminiAtomicscaleVisualizationMultiferroicity2024',
    'bhowalPolarMetalsPrinciples2023b',
    'Chen2016electrical',
    'Chen2019superconductivity',
    'chenHafniumBasedFerroelectricPostMoore2026',
    'cheongMultiferroicsMagneticTwist2007a',
    'fiebigEvolutionMultiferroics2016',
    'gaoGiantChiralMagnetoelectric2024a',
    'gaoStrainEngineeringFerroelectric2024',
    'gomez-ortizKittelLawDomain2023',
    'guanRecentProgressTwoDimensional2020',
    'guoAdvancesTwodimensionalFerroelectric2025',
    'hanPolarTopologicalMaterials2025',
    'heSwitchingTwodimensionalSliding2025',
    'heUltrafastSwitchingDynamics2024',
    'huangPolarPhaseDomain2019',
    'huangTwodimensionalIn2Se3Rising2022',
    'huProgressProspectsLowdimensional2019',
    'Jin2015studying',
    'krishnamurthiSpinChargeDensity2020',
    'liFerroelasticityDomainPhysics2016',
    'liPhaseTransitions2D2021',
    'martinThinfilmFerroelectricMaterials2016',
    'mostovoyMultiferroicsDifferentRoutes2024',
    'neumayerCompetingPolarPhases2025',
    'pedramraziManipulatingTopologicalDomain2019',
    'prosandeevKittelLawInBiFeO3Ultrathin2010',
    'rameshMultiferroicsProgressProspects2007',
    'sharmaRoomtemperatureFerroelectricSemimetal2019',
    'spaldinAdvancesMagnetoelectricMultiferroics2019',
    'spaldinRenaissanceMagnetoelectricMultiferroics2005',
    'tanRevealingEmergentMagnetic2024',
    'wangFormationMechanismTwin2019',
    'wuCoexistenceFerroelectricityAntiferroelectricity2024',
    'xuTunableFerroelectricTopological2022',
    'yangRipplingFerroicPhase2021',
    'yuFerroelectricControlMagnetism2026',
    'zhangEmergingFrontiersTwodimensional2025',
]

FM_START = re.compile(r'^---\s*\r?\n')
FM_END = re.compile(r'\r?\n---\s*(\r?\n|$)')

def git_show(commit, relpath):
    r = subprocess.run(
        ['git', 'show', f'{commit}:{relpath}'],
        cwd=str(REPO), capture_output=True, text=True, encoding='utf-8', errors='replace',
    )
    if r.returncode != 0:
        raise RuntimeError(f"git show 失败: {commit}:{relpath} -> {r.stderr}")
    return r.stdout

def split_fm(text):
    """返回 (frontmatter 内容, 正文起始位置)。frontmatter 内容不含 --- 标记。"""
    m1 = FM_START.match(text)
    if not m1:
        return None, 0
    m2 = FM_END.search(text, m1.end())
    if not m2:
        return None, 0
    fm = text[m1.end():m2.start()]
    body_start = m2.end()
    return fm, body_start

backup_dir = TEMP / f"restore_backup_{time.strftime('%Y%m%d_%H%M%S')}"
backup_dir.mkdir(parents=True, exist_ok=True)

stats = {'restored': 0, 'skipped_no_full': 0, 'domain_wall_fixed': 0}
h2_before_after = []

for citekey in SUSPECTS:
    fpath = REPO / 'wiki' / 'papers' / f'{citekey}.md'
    rel = f'wiki/papers/{citekey}.md'
    cur = fpath.read_text(encoding='utf-8', errors='replace')

    # 备份当前文件
    shutil.copy2(fpath, backup_dir / f'{citekey}.md')

    # 获取 8b027c0 完整版
    try:
        full = git_show('8b027c0', rel)
    except Exception as e:
        stats['skipped_no_full'] += 1
        print(f"[跳过] {citekey}: {e}")
        continue

    fm_cur, _ = split_fm(cur)
    fm_full, body_full_start = split_fm(full)
    if fm_cur is None or fm_full is None:
        stats['skipped_no_full'] += 1
        print(f"[跳过] {citekey}: frontmatter 解析失败")
        continue

    body_full = full[body_full_start:]

    # 修正正文中 domain-wall 链接类型（entity→concept）
    fixed = 0
    if '../entities/domain-wall' in body_full:
        fixed = body_full.count('../entities/domain-wall')
        body_full = body_full.replace('../entities/domain-wall', '../concepts/domain-wall')
    if 'entities/domain-wall' in body_full and '../concepts/domain-wall' not in body_full.replace('../concepts/domain-wall', ''):
        # 处理可能的其他形式（如裸 entities/domain-wall）
        fixed += body_full.count('entities/domain-wall')
        body_full = body_full.replace('entities/domain-wall', 'concepts/domain-wall')
    stats['domain_wall_fixed'] += fixed

    # 合并：b94beee frontmatter + 8b027c0 正文（frontmatter 后固定空行）
    merged = '---\n' + fm_cur.rstrip() + '\n---\n\n' + body_full.lstrip('\r\n')
    fpath.write_text(merged, encoding='utf-8')

    # 统计 H2
    h2_before = len(re.findall(r'^## ', cur, re.MULTILINE))
    h2_after = len(re.findall(r'^## ', merged, re.MULTILINE))
    h2_before_after.append((citekey, h2_before, h2_after))
    stats['restored'] += 1

print(f"\n=== 恢复统计 ===")
print(f"已恢复: {stats['restored']}")
print(f"跳过: {stats['skipped_no_full']}")
print(f"domain-wall 链接修正: {stats['domain_wall_fixed']} 处")

print("\n=== H2 章节数变化 ===")
for citekey, b, a in h2_before_after:
    print(f"  {citekey}: {b} -> {a}")

print(f"\n备份目录: {backup_dir}")
