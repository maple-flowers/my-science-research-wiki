---
tags: [concept]
title: 'density-of-states'
type: concept
status: developing
papers: ['Chen2019superconductivity', 'Islam2025enhancement', 'Kang2012dimer', 'Koley2020charge', 'Li2013bonding', 'cossuStackingChargedensityWaves2024', 'gorkovStrongElectronlatticeCoupling2012', 'khazaeiNovelElectronicMagnetic2013', 'kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994', 'miaoMagneticFerroelectricMetal2024', 'naguib25thAnniversaryArticle2013a', 'neumayerCompetingPolarPhases2025', 'zahraCriticalAnalysisFerroelectric2025']
updated: 2026-08-18
---

# density-of-states

态密度（density of states, DOS）描述单位能量区间内可容纳的量子态数目，是连接电子结构计算与实验测量的桥梁。它决定了电子占据统计、输运、磁性、光学等大量物性，是材料电子结构分析中最常用的量之一。

## 👵 太奶导读

太奶啊，态密度就好比"一个小区里每一层楼能住多少人"。能量是楼层，态密度就是每层楼有多少间房子。哪层房子多，电子就爱往哪挤；房子满不满（费米面位置），决定了材料是导电的金属还是绝缘体。看态密度图就能大概猜出材料"脾气"：金属、半导体、磁性，都能从这张图上看出来。

## 🧩 核心内容与机制 (Core Content)

- **定义与计算**：DOS(E) = Σᵢ δ(E − Eᵢ)，在 DFT 中通过布里渊区 k 点求和（如四面体法、展宽法）得到，是能带计算的直接产物。
- **费米面与稳定性**：费米能级处的高态密度常伴随电子不稳定性，容易诱发电荷密度波（CDW）、磁性或超导等相变——本库多篇 CDW 论文都以费米面嵌套与态密度讨论为出发点。
- **分波态密度**：按轨道（s/p/d）投影的 DOS 可揭示磁性来源（如 d 带填充与 Stoner 判据）、成键/反键特征。
- **实验对应**：扫描隧道谱（STS）直接测量局域态密度；角分辨光电子谱（ARPES）给出动量分辨的谱函数，与理论 DOS/能带互为印证。
- **典型应用**：判断金属-绝缘体转变、掺杂改性的能隙工程、MXene/TMD 等二维材料的导电性与磁性起源分析。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/band-structure|能带结构]]：DOS 由能带信息积分而来。
- [[../concepts/charge-density-wave|电荷密度波]]：费米面嵌套与高 DOS 不稳定的结果。
- [[../entities/ARPES|ARPES]]：实验测量电子结构的直接手段。
- [[../entities/MXenes|MXene]]：常见的高态密度二维导电材料。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2019superconductivity]] — Discommensuration-driven superconductivity in the charge density wave phases of transition-metal dichalcogenides
- [[../papers/Islam2025enhancement]] — Pressure-induced enhancement of superfluid density in transition metal dichalcogenides with and without charge density wave
- [[../papers/Kang2012dimer]] — Dimer impurity scattering, reconstructed Fermi-surface nesting, and density-wave diagnostics in iron pnictides
- [[../papers/Koley2020charge]] — Charge density wave and superconductivity in transition metal dichalcogenides
- [[../papers/Li2013bonding]] — Bonding Charge Density and Ultimate Strength of Monolayer Transition Metal Dichalcogenides
- [[../papers/cossuStackingChargedensityWaves2024]] — Stacking of charge-density waves in 2H-NbSe₂ bilayers
- [[../papers/gorkovStrongElectronlatticeCoupling2012]] — Strong electron-lattice coupling as the mechanism behind charge density wave transformations in transition-metal dichalcogenides
- [[../papers/khazaeiNovelElectronicMagnetic2013]] — Novel Electronic and Magnetic Properties of Two-Dimensional Transition Metal Carbides and Nitrides
- [[../papers/kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994]] — <i>Ab initio</i> molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transition in germanium
- [[../papers/miaoMagneticFerroelectricMetal2024]] — Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding
- [[../papers/naguib25thAnniversaryArticle2013a]] — 25th Anniversary Article: MXenes: A New Family of Two‐Dimensional Materials
- [[../papers/neumayerCompetingPolarPhases2025]] — Competing polar phases in 2D ferroelectric transition metal thio- and selenophosphates
- [[../papers/zahraCriticalAnalysisFerroelectric2025]] — A critical analysis of ferroelectric and ferromagnetic properties in two-dimensional MXene
