#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B 阶段：为 10 个 mature 页替换 AIGC 水印 frontmatter 为合规 frontmatter。
只改 frontmatter 块，正文逐字节保留。幂等：已合规页跳过。
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

FM = {
"wiki/concepts/ferroelectric-metal.md": """tags: [concept, ferroelectric, metal, polar-metal]
title: 铁电金属 / Ferroelectric Metal
type: concept
status: mature
domain: [ferroelectricity, polar-metals, 2d-materials]
mechanism: "金属导电性与可电场翻转的自发极化共存；极化多由层间滑移或极性声子软模提供，导电电子与极性畸变在实空间/轨道空间解耦，屏蔽不完全"
related_concepts: [polar-metal, metallic-ferroelectricity, hyper-ferroelectric-metal, sliding-ferroelectricity, ferroelectricity]
related_entities: [WTe2, LiOsO3]
papers: [feiFerroelectricSwitchingTwodimensional2018a, bhowalPolarMetalsPrinciples2023b, zhaoRealization2DMultiferroic2024, wangTwodimensionalFerroelectricMetal2025, miaoMagneticFerroelectricMetal2024, sharmaRoomtemperatureFerroelectricSemimetal2019]
updated: 2026-08""",

"wiki/concepts/interlayer-polarization-coupling.md": """tags: [concept, ferroelectric, 2D, stacking]
title: 层间极化耦合 / Interlayer Polarization Coupling
type: concept
status: mature
domain: [ferroelectricity, 2d-materials, stacking-engineering]
mechanism: "范德华层间的堆垛构型决定层间电荷转移与轨道畸变，使各层极化相互约束、叠加或补偿，总极化随层数与堆垛序演化"
related_concepts: [sliding-ferroelectricity, interlayer-coupling, polarization-switching, stacking-engineered-ferroelectricity]
related_entities: [ReS2, HgI2]
papers: [tangCombiningIntrinsicSlidinginduced2025, chenStrongSlidingFerroelectricity2024, kaurRecentAdvancesTheoretical2025a]
updated: 2026-08""",

"wiki/concepts/magnetic-polar-metal.md": """tags: [concept, multiferroic, metal, magnetism]
title: 磁性极性金属 / Magnetic Polar Metal
type: concept
status: mature
domain: [multiferroics, polar-metals, 2d-magnetism]
mechanism: "在同一金属相中同时破缺空间反演（极性畸变）与时间反演（磁有序），三种序参量（导电性、极化、磁化）共存并通过自旋-轨道耦合互相调控"
related_concepts: [multiferroicity, magnetoelectric-coupling, polar-metal, ferroelectric-metal, sliding-ferroelectricity]
related_entities: [Fe3GeTe2, WTe2]
papers: [miaoMagneticFerroelectricMetal2024, wuNonvolatileSwitchableHalfmetallicity2024, tianRoomtemperatureTwodimensionalMultiferroic2026]
updated: 2026-08""",

"wiki/concepts/metallic-ferroelectricity.md": """tags: [concept, ferroelectric, metal]
title: 金属铁电性 / Metallic Ferroelectricity
type: concept
status: mature
domain: [ferroelectricity, polar-metals, 2d-materials]
mechanism: "自由载流子存在时仍能保留可翻转极化：极性自由度与导电通道在实空间或轨道上分离，使载流子屏蔽不足以消灭极化双稳态"
related_concepts: [ferroelectric-metal, polar-metal, hyper-ferroelectric-metal, sliding-ferroelectricity, ferroelectricity]
related_entities: [WTe2]
papers: [zhaoRealization2DMultiferroic2024, feiFerroelectricSwitchingTwodimensional2018a, wuSlidingFerroelectricity2D2021a, bhowalPolarMetalsPrinciples2023b, wangTwodimensionalFerroelectricMetal2025]
updated: 2026-08""",

"wiki/concepts/polar-metal.md": """tags: [concept, metal, polar, symmetry-breaking]
title: 极性金属 / Polar Metal
type: concept
status: mature
domain: [polar-metals, ferroelectricity, symmetry-breaking]
mechanism: "金属态中发生极性结构相变、空间反演对称性破缺，但极化不要求可被电场翻转；成因包括几何/位移型极性畸变与轨道选择性解耦"
related_concepts: [ferroelectric-metal, metallic-ferroelectricity, hyper-ferroelectric-metal, geometric-ferroelectricity, inversion-symmetry-breaking]
related_entities: [LiOsO3, WTe2, Ca3Ru2O7]
papers: [bhowalPolarMetalsPrinciples2023b, feiFerroelectricSwitchingTwodimensional2018a, huangPolarPhaseDomain2019, wuSlidingFerroelectricity2D2021a, sharmaRoomtemperatureFerroelectricSemimetal2019]
updated: 2026-08""",

"wiki/concepts/sliding-ferroelectricity.md": """tags: [concept, ferroelectric, 2D, stacking, sliding-ferroelectricity]
title: 滑动铁电性 / Sliding Ferroelectricity
type: concept
status: mature
domain: [ferroelectricity, 2d-materials, stacking-engineering]
mechanism: "范德华层间侧向滑移改变堆垛构型、破缺空间反演对称性，通过层间电荷转移与轨道畸变感生面外极化；属纯电子起源，而非单胞内离子位移"
related_concepts: [dipole-locking, moire-superlattice, interlayer-polarization-coupling, stacking-engineered-ferroelectricity, depolarization-field]
related_entities: [In2Se3, HgI2, ReS2, WTe2]
papers: [wuSlidingFerroelectricity2D2021a, huangTwodimensionalIn2Se3Rising2022, feiFerroelectricSwitchingTwodimensional2018a, sunSlidingFerroelectricityTwodimensional2025, kaurRecentAdvancesTheoretical2025a, chenStrongSlidingFerroelectricity2024, FerroelectricityMultiferroicityAtomic2023, RecentAdvancesGrowth2025, bhowalPolarMetalsPrinciples2023b, guanRecentProgressTwoDimensional2020, guoAdvancesTwodimensionalFerroelectric2025, hanTunableSlidingFerroelectricity2025, heSwitchingTwodimensionalSliding2025, heUltrafastSwitchingDynamics2024, huProgressProspectsLowdimensional2019, huangPolarPhaseDomain2019, kimObservationPhaseTransition1997, liPhaseTransitions2D2021, martinThinfilmFerroelectricMaterials2016, miaoMagneticFerroelectricMetal2024, neumayerCompetingPolarPhases2025, shenEmergenceMultipleFerroelectric2025, tangCombiningIntrinsicSlidinginduced2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, xunCoexistingMagnetismFerroelectric2024, zhangEmergingFrontiersTwodimensional2025, zhaoOpticalFingerprintsTwodimensional2024]
updated: 2026-08""",

"wiki/entities/HgI2.md": """tags: [entity, material, 2D, vdW, ferroelectric]
title: 碘化汞 (HgI2) / Mercury Iodide
type: entity
formula: HgI2
class: [vdW, layered-halide, semiconductor]
status: mature
properties: [sliding-ferroelectricity, rashba-effect, spin-texture]
related_concepts: [sliding-ferroelectricity, rashba-effect, interfacial-charge-rearrangement, polarization-switching, spin-texture]
related_entities: [WTe2, ReS2, GaSe]
papers: [chenStrongSlidingFerroelectricity2024, kaurRecentAdvancesTheoretical2025a, sunSlidingFerroelectricityTwodimensional2025, zhangEmergingFrontiersTwodimensional2025, tangMultiferroicityTwodimensionalVan2025]
updated: 2026-08""",

"wiki/entities/InSe.md": """tags: [entity, material, 2D, vdW, ferroelectric]
title: 硒化铟 (InSe) / Indium Selenide
type: entity
formula: InSe
class: [vdW, III-VI-chalcogenide, semiconductor]
status: mature
properties: [sliding-ferroelectricity, piezoelectricity]
related_concepts: [sliding-ferroelectricity, piezoelectricity, stacking-engineered-ferroelectricity]
related_entities: [GaSe, In2Se3]
papers: [sunSlidingFerroelectricityTwodimensional2025, wuSlidingFerroelectricity2D2021a, zhangEmergingFrontiersTwodimensional2025]
updated: 2026-08""",

"wiki/entities/LiOsO3.md": """tags: [entity, material, oxide, perovskite, polar-metal]
title: 锇酸锂 (LiOsO₃) / Lithium Osmate
type: entity
formula: LiOsO3
class: [perovskite, oxide, metal]
status: mature
properties: [polar-metal, ferroelectric-like-metal]
related_concepts: [polar-metal, ferroelectric-metal, metallic-ferroelectricity, ferroelectricity]
related_entities: [WTe2, BaTiO3, PbTiO3]
papers: [bhowalPolarMetalsPrinciples2023b, huProgressProspectsLowdimensional2019]
updated: 2026-08""",

"wiki/entities/ReS2.md": """tags: [entity, material, 2D, TMD, ferroelectric]
title: 二硫化铼 (ReS2) / Rhenium Disulfide
type: entity
formula: ReS2
stoichiometry: 1T'
class: [TMD, vdW, semiconductor]
status: mature
properties: [sliding-ferroelectricity, ferroelasticity]
related_concepts: [sliding-ferroelectricity, ferroelasticity, interlayer-polarization-coupling, polarization-switching]
related_entities: [WTe2, SnS]
papers: [kaurRecentAdvancesTheoretical2025a, sunSlidingFerroelectricityTwodimensional2025, tangMultiferroicityTwodimensionalVan2025, guanRecentProgressTwoDimensional2020]
updated: 2026-08""",
}

FM_RE = re.compile(r'\A---\s*\r?\n.*?\r?\n---[ \t]*(\r?\n)', re.DOTALL)

changed = []
for rel, fm in FM.items():
    p = REPO / rel
    raw = p.read_text(encoding='utf-8')
    m = FM_RE.match(raw)
    if not m:
        print(f"SKIP  {rel}: 未找到 frontmatter 块")
        continue
    if 'AIGC:' not in m.group(0):
        print(f"SKIP  {rel}: frontmatter 已无 AIGC 水印，未改动")
        continue
    nl = '\r\n' if '\r\n' in m.group(0) else '\n'
    body = raw[m.end():]
    new_fm = '---' + nl + fm.replace('\n', nl) + nl + '---' + nl
    p.write_text(new_fm + body, encoding='utf-8', newline='')
    changed.append(rel)
    print(f"OK    {rel}")

print(f"\n改动 {len(changed)} 页")
