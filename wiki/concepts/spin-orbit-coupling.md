---
tags: [concept]
title: 'spin-orbit-coupling'
type: concept
status: developing
papers: ['Blessing2026optical', 'Johannes2008fermi', 'Mińkowski2021cation', 'RecentAdvancesGrowth2025', 'Xie2024isostructural', 'aiFerroelectricityCoexistedPorbital2022', 'aminiAtomicscaleVisualizationMultiferroicity2024', 'bhowalPolarMetalsPrinciples2023b', 'caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025', 'chen3dLevelSymmetry2025', 'chenStrongSlidingFerroelectricity2024', 'cheongMultiferroicsMagneticTwist2007a', 'chowdhuryReviewTheoreticalComputational', 'fengFerroelectricityMultiferroicityTwodimensional2020', 'fiebigEvolutionMultiferroics2016', 'gaoGiantChiralMagnetoelectric2024a', 'guanRecentProgressTwoDimensional2020', 'guoAdvancesTwodimensionalFerroelectric2025', 'hallEnvironmentalControlCharge', 'hanTunableSlidingFerroelectricity2025', 'huProgressProspectsLowdimensional2019', 'huangPolarPhaseDomain2019', 'kaurRecentAdvancesTheoretical2025a', 'laiTwodimensionalFerromagnetismDriven2019', 'liMonolayerPuckeredPentagonal2022', 'liPhaseTransitions2D2021', 'liuSpintronicsTwoDimensionalMaterials2020b', 'mostovoyMultiferroicsDifferentRoutes2024', 'niuDirectVisualizationLargeScale2021', 'pedramraziManipulatingTopologicalDomain2019', 'pengStrainEngineering2D2020', 'rameshMultiferroicsProgressProspects2007', 'sharmaRoomtemperatureFerroelectricSemimetal2019', 'songEvidenceSinglelayerVan2022', 'spaldinAdvancesMagnetoelectricMultiferroics2019', 'sunSlidingFerroelectricityTwodimensional2025', 'tangMultiferroicityTwodimensionalVan2025', 'tianRoomtemperatureTwodimensionalMultiferroic2026', 'vanvleckSurveyTheoryFerromagnetism1945', 'wangTunableD0Topological2025b', 'wongEvidenceMetallic1T', 'wuCoexistenceFerroelectricityAntiferroelectricity2024', 'wuElectrostaticGatingIntercalation2022', 'wuNonvolatileSwitchableHalfmetallicity2024', 'wuSlidingFerroelectricity2D2021a', 'xueEmergingNonvolatileMemories2011', 'xunCoexistingMagnetismFerroelectric2024', 'yangStrainEngineeringTwodimensional2021', 'yuFerroelectricControlMagnetism2026', 'zahraCriticalAnalysisFerroelectric2025', 'zhangEmergingFrontiersTwodimensional2025', 'zhangNonvolatileControlTopological2025', 'zhaoOpticalFingerprintsTwodimensional2024', 'zhaoRealization2DMultiferroic2024', 'zhongHighthroughputExfoliationMultiferroic2025']
updated: 2026-08-18
---

# spin-orbit-coupling

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


自旋轨道耦合（spin-orbit coupling, SOC）指**电子自旋与轨道角动量之间的相对论相互作用**，其大小随原子序数 Z⁴ 增大。SOC 是能带自旋劈裂（Rashba/Dresselhaus）、拓扑绝缘体、Weyl 半金属、磁各向异性、Dzyaloshinskii-Moriya 相互作用（DMI）与自旋电子器件的微观根源。

## 👵 太奶导读

太奶啊，电子的"自旋"（像个小陀螺）和它绕原子核转的"轨道"之间有"牵连"——这就是自旋轨道耦合。重元素里这个"牵连"特别强。它一强就出大事：让能带"自旋分家"（不同自旋的电子能量不同）、搞出拓扑绝缘体（表面导电内部绝缘）、让磁针"拧成螺旋"（DMI）……自旋电子学、拓扑物理的基础都从它来。

## 🏗️ 结构概览

自旋-轨道耦合是凝聚态物理的核心相对论效应，其强度随原子序数 Z 增大（∝ Z⁴）。按物理后果分型：能带劈裂（Rashba/Dresselhaus）、拓扑态（TI、Weyl）、磁性各向异性与 DMI。按体系分：重元素体相、界面与二维材料。

## 🧩 核心内容与机制 (Core Content)

- **相对论起源**：电子绕核运动感受到磁场，与自旋磁矩耦合；有效强度 ∝ Z⁴，重元素（Pb、Bi、W、Pt）显著（本库重元素化合物论文）。
- **能带效应**：反演对称破缺时产生 Rashba/Dresselhaus 自旋劈裂（本库 Rashba 与自旋劈裂论文）；SOC 也影响磁各向异性（magnetic-anisotropy）与 g 因子。
- **拓扑态**：SOC 驱动拓扑绝缘体（topological-insulator）、Weyl/狄拉克半金属与拓扑金属（本库 Mn₂N、WTe₂ 等拓扑论文）。
- **磁性效应**：SOC 是磁各向异性、Dzyaloshinskii-Moriya 相互作用（DMI，见 helical-magnetism）与斯格明子稳定的来源。
- **计算**：DFT 计算需显式含 SOC（本库 VASP 自旋轨道计算论文）；对称性分析选择 SOC 方向。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/topological-insulator|拓扑绝缘体]]：SOC 驱动的拓扑态。
- [[../concepts/dzyaloshinskii-moriya-interaction|Dzyaloshinskii-Moriya 相互作用]]：SOC 的磁性效应。
- [[../concepts/magnetic-anisotropy|磁各向异性]]：SOC 决定易磁化轴。
- [[../concepts/inversion-symmetry-breaking|反演对称破缺]]：Rashba 劈裂的条件。
- [[../concepts/band-structure|能带结构]]：SOC 修正能带。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| SOC 强度 | 耦合强度 | ∝ Z⁴，重元素显著 |
| 劈裂能 | Rashba/Dresselhaus 劈裂 | 界面可达 meV 级 |
| 拓扑序 | Z2 不变量 | 区分平庸/拓扑 |
| 磁性效应 | 磁各向异性/DMI | 决定易磁化轴、斯格明子 |
| 计算处理 | DFT 需含 SOC | 全相对论/标量相对论 |

## 🔀 近邻概念辨析

- **Rashba vs Dresselhaus**：Rashba 源于结构反演破缺（界面/外场），Dresselhaus 源于体相各向异性，二者可共存叠加。
- **SOC vs 交换作用**：SOC 是单电子相对论自旋-轨道耦合；交换作用是电子间静电相互作用，共同决定磁结构。
- **SOC vs 自旋劈裂（无 SOC）**：无 SOC 时自旋简并，SOC 破缺简并并耦合轨道序。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| SOC 强度 | 耦合强度 | ∝ Z⁴，重元素显著 |
| 劈裂能 | Rashba/Dresselhaus 劈裂 | 界面可达 meV 级 |
| 拓扑序 | Z2 不变量 | 区分平庸/拓扑 |
| 磁性效应 | 磁各向异性/DMI | 决定易磁化轴、斯格明子 |
| 计算处理 | DFT 需含 SOC | 全相对论/标量相对论 |

## 🔀 近邻概念辨析

- **Rashba vs Dresselhaus**：Rashba 源于结构反演破缺（界面/外场），Dresselhaus 源于体相各向异性，二者可共存叠加。
- **SOC vs 交换作用**：SOC 是单电子相对论自旋-轨道耦合；交换作用是电子间静电相互作用，共同决定磁结构。
- **SOC vs 自旋劈裂（无 SOC）**：无 SOC 时自旋简并，SOC 破缺简并并耦合轨道序。

## 📚 相关论文 (Related Papers) Papers)

- [[../papers/Blessing2026optical]] — Optical investigation of tin telluride (SnTe) thin films grown at different deposition voltage
- [[../papers/Johannes2008fermi]] — Fermi surface nesting and the origin of charge density waves in metals
- [[../papers/Mińkowski2021cation]] — Cation interstitial diffusion in lead telluride and cadmium telluride studied by means of neural network potential based molecular dynamics simulations
- [[../papers/RecentAdvancesGrowth2025]] — Recent advances in growth, characterization, and application of two-dimensional multiferroic materials
- [[../papers/Xie2024isostructural]] — Isostructural doping for organic persistent mechanoluminescence
- [[../papers/aiFerroelectricityCoexistedPorbital2022]] — Ferroelectricity coexisted with p-orbital ferromagnetism and metallicity in two-dimensional metal oxynitrides
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] — Atomic-Scale Visualization of Multiferroicity in Monolayer NiI2
- [[../papers/bhowalPolarMetalsPrinciples2023b]] — Polar Metals: Principles and Prospects
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]] — Ferroelectricity-driven strain-mediated magnetoelectric coupling in two-dimensional multiferroic heterostructure
- [[../papers/chen3dLevelSymmetry2025]] — 3d-level symmetry between metal layers governing the electronic configuration of Mn2N MXenes and enabling modulation between half-metallicity and semiconductivity
- [[../papers/chenStrongSlidingFerroelectricity2024]] — Strong Sliding Ferroelectricity and Interlayer Sliding Controllable Spintronic Effect in Two-Dimensional HgI₂ Layers
- [[../papers/cheongMultiferroicsMagneticTwist2007a]] — Multiferroics: a magnetic twist for ferroelectricity
- [[../papers/chowdhuryReviewTheoreticalComputational]] — Computational Methods for Charge Density Waves in 2D Materials
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in two-dimensional Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/fiebigEvolutionMultiferroics2016]] — The evolution of multiferroics
- [[../papers/gaoGiantChiralMagnetoelectric2024a]] — Giant chiral magnetoelectric oscillations in a van der Waals multiferroic
- [[../papers/guanRecentProgressTwoDimensional2020]] — Recent Progress in Two‐Dimensional Ferroelectric Materials
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]] — Advances in two-dimensional ferroelectric materials
- [[../papers/hallEnvironmentalControlCharge]] — Environmental Control of Charge Density Wave Order in Monolayer 2H-TaS₂
- [[../papers/hanTunableSlidingFerroelectricity2025]] — Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers
- [[../papers/huProgressProspectsLowdimensional2019]] — Progress and prospects in low‐dimensional multiferroic materials
- [[../papers/huangPolarPhaseDomain2019]] — Polar and phase domain walls with conducting interfacial states in a Weyl semimetal MoTe2
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]] — Two-dimensional ferromagnetism and driven ferroelectricity in van der Waals CuCrP₂S₆
- [[../papers/liMonolayerPuckeredPentagonal2022]] — Monolayer puckered pentagonal VTe2: An emergent two-dimensional ferromagnetic semiconductor with multiferroic coupling
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]] — Spintronics in Two-Dimensional Materials
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]] — Multiferroics: different routes to magnetoelectric coupling
- [[../papers/niuDirectVisualizationLargeScale2021]] — Direct Visualization of Large-Scale Intrinsic Atomic Lattice Structure and Its Collective Anisotropy in Air-Sensitive Monolayer 1T'-WTe2
- [[../papers/pedramraziManipulatingTopologicalDomain2019]] — Manipulating Topological Domain Boundaries in the Single-Layer Quantum Spin Hall Insulator 1T′–WSe₂
- [[../papers/pengStrainEngineering2D2020]] — Strain engineering of 2D semiconductors and graphene: from strain fields to band-structure tuning and photonic applications
- [[../papers/rameshMultiferroicsProgressProspects2007]] — Multiferroics: progress and prospects in thin films
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] — A room-temperature ferroelectric semimetal
- [[../papers/songEvidenceSinglelayerVan2022]] — Evidence for a single-layer van der Waals multiferroic
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]] — Advances in magnetoelectric multiferroics
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications
- [[../papers/tangMultiferroicityTwodimensionalVan2025]] — Towards Multiferroicity in Two-Dimensional Van Der Waals Materials: Challenges and Opportunities
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]] — Room-temperature two-dimensional multiferroic metal with voltage-controllable magnetic order
- [[../papers/vanvleckSurveyTheoryFerromagnetism1945]] — A Survey of the Theory of Ferromagnetism
- [[../papers/wangTunableD0Topological2025b]] — Tunable d0 topological magnetic states in multiferroic monolayer In2NO2
- [[../papers/wongEvidenceMetallic1T]] — Metallic 1T Phase, 3d1 Electronic Configuration and Charge Density Wave Order in Molecular Beam Epitaxy Grown Monolayer Vanadium Ditelluride
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]] — Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic
- [[../papers/wuElectrostaticGatingIntercalation2022]] — Electrostatic gating and intercalation in 2D materials
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]] — Nonvolatile switchable half-metallicity and magnetism in the MXene Hf₂MnC₂O₂/Sc₂CO₂ multiferroic heterostructure
- [[../papers/wuSlidingFerroelectricity2D2021a]] — Sliding ferroelectricity in 2D van der Waals materials: Related physics and future opportunities
- [[../papers/xueEmergingNonvolatileMemories2011]] — Emerging non-volatile memories
- [[../papers/xunCoexistingMagnetismFerroelectric2024]] — Coexisting Magnetism, Ferroelectric, and Ferrovalley Multiferroic in Stacking-Dependent Two-Dimensional Materials
- [[../papers/yangStrainEngineeringTwodimensional2021]] — Strain engineering of <scp>two‐dimensional</scp> materials: Methods, properties, and applications
- [[../papers/yuFerroelectricControlMagnetism2026]] — Ferroelectric Control of Magnetism and Giant Magnetoresistance Via Intercalation-Induced Symmetry Breaking in Two-Dimensional Multiferroics with Strong Magnetoelectric Coupling
- [[../papers/zahraCriticalAnalysisFerroelectric2025]] — A critical analysis of ferroelectric and ferromagnetic properties in two-dimensional MXene
- [[../papers/zhangEmergingFrontiersTwodimensional2025]] — Emerging frontiers in two-dimensional sliding ferroelectrics
- [[../papers/zhangNonvolatileControlTopological2025]] — Nonvolatile control of topological magnetism in two-dimensional CrInTe2/In2Se3 multiferroic heterostructures
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]] — Optical fingerprints of two-dimensional interlayer-sliding multiferroic materials
- [[../papers/zhaoRealization2DMultiferroic2024]] — Realization of 2D multiferroic with strong magnetoelectric coupling by intercalation: a first-principles high-throughput prediction
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] — High-throughput exfoliation of multiferroic ternary oxide monolayers with high transition temperature and giant spin splitting
