# -*- coding: utf-8 -*-
"""恢复后核对 38 篇正文完整性：H2 章节数、描述章节存在性、domain-wall 链接类型、frontmatter 标签。"""
import re
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
SUSPECTS = [
    'aminiAtomicscaleVisualizationMultiferroicity2024','bhowalPolarMetalsPrinciples2023b',
    'Chen2016electrical','Chen2019superconductivity','chenHafniumBasedFerroelectricPostMoore2026',
    'cheongMultiferroicsMagneticTwist2007a','fiebigEvolutionMultiferroics2016',
    'gaoGiantChiralMagnetoelectric2024a','gaoStrainEngineeringFerroelectric2024',
    'gomez-ortizKittelLawDomain2023','guanRecentProgressTwoDimensional2020',
    'guoAdvancesTwodimensionalFerroelectric2025','hanPolarTopologicalMaterials2025',
    'heSwitchingTwodimensionalSliding2025','heUltrafastSwitchingDynamics2024',
    'huangPolarPhaseDomain2019','huangTwodimensionalIn2Se3Rising2022',
    'huProgressProspectsLowdimensional2019','Jin2015studying','krishnamurthiSpinChargeDensity2020',
    'liFerroelasticityDomainPhysics2016','liPhaseTransitions2D2021',
    'martinThinfilmFerroelectricMaterials2016','mostovoyMultiferroicsDifferentRoutes2024',
    'neumayerCompetingPolarPhases2025','pedramraziManipulatingTopologicalDomain2019',
    'prosandeevKittelLawInBiFeO3Ultrathin2010','rameshMultiferroicsProgressProspects2007',
    'sharmaRoomtemperatureFerroelectricSemimetal2019','spaldinAdvancesMagnetoelectricMultiferroics2019',
    'spaldinRenaissanceMagnetoelectricMultiferroics2005','tanRevealingEmergentMagnetic2024',
    'wangFormationMechanismTwin2019','wuCoexistenceFerroelectricityAntiferroelectricity2024',
    'xuTunableFerroelectricTopological2022','yangRipplingFerroicPhase2021',
    'yuFerroelectricControlMagnetism2026','zhangEmergingFrontiersTwodimensional2025',
]

problems = []
for citekey in SUSPECTS:
    p = REPO / 'wiki' / 'papers' / f'{citekey}.md'
    t = p.read_text(encoding='utf-8', errors='replace')
    h2 = re.findall(r'^## .*$', t, re.MULTILINE)
    has_meta = '📄 元数据' in t
    has_one_liner = '💡 一句话' in t
    has_key_fig = '📊 关键图表' in t
    bad_entity_link = '../entities/domain-wall' in t
    # frontmatter 中残留 entity/domain-wall 标签
    fm_match = re.match(r'^---\s*\r?\n(.*?)\r?\n---', t, re.DOTALL)
    fm = fm_match.group(1) if fm_match else ''
    bad_tag = bool(re.search(r'^  - entity/domain-wall\s*$', fm, re.MULTILINE))
    if len(h2) < 5 or not has_meta or not has_one_liner or not has_key_fig or bad_entity_link or bad_tag:
        problems.append((citekey, len(h2), has_meta, has_one_liner, has_key_fig, bad_entity_link, bad_tag))

print(f"总篇数: {len(SUSPECTS)}")
print(f"异常篇数: {len(problems)}")
for x in problems:
    print("  [异常]", x)
if not problems:
    print("全部通过：H2>=5、含📄元数据/💡一句话/📊关键图表、无 entity/domain-wall 残留")
