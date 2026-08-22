---
tags: [concept, ferroic, mechanics]
title: 铁弹性 / Ferroelasticity
type: concept
status: developing
related_concepts: [ferroelectricity, domain-wall, structural-phase-transition, ferroic-order, 2d-materials]
papers: [Chen2016electrical, FerroelectricityMultiferroicityAtomic2023, Jin2015studying, RecentAdvancesGrowth2025, bhowalPolarMetalsPrinciples2023b, chenFerromagneticNonmagnetic1T2022, fengFerroelectricityMultiferroicityTwodimensional2020, fiebigEvolutionMultiferroics2016, gaoStrainEngineeringFerroelectric2024, gomez-ortizKittelLawDomain2023, guanRecentProgressTwoDimensional2020, hanPolarTopologicalMaterials2025, heSwitchingTwodimensionalSliding2025, hillWhyAreThere2000a, houStrainbasedRoomtemperatureNonvolatile2019, huProgressProspectsLowdimensional2019, huangPolarPhaseDomain2019, kaurRecentAdvancesTheoretical2025a, liFerroelasticityDomainPhysics2016, liMonolayerPuckeredPentagonal2022, liPhaseTransitions2D2021, mostovoyMultiferroicsDifferentRoutes2024, pedramraziManipulatingTopologicalDomain2019, rameshMultiferroicsProgressProspects2007, sharmaRoomtemperatureFerroelectricSemimetal2019, spaldinAdvancesMagnetoelectricMultiferroics2019, spaldinRenaissanceMagnetoelectricMultiferroics2005, sunSlidingFerroelectricityTwodimensional2025, tangMultiferroicityTwodimensionalVan2025, wangFormationMechanismTwin2019, wuSlidingFerroelectricity2D2021a, xuTunableFerroelectricTopological2022, xuTwodimensionalFerroelasticityVan2021, xunCoexistingMagnetismFerroelectric2024, yangRipplingFerroicPhase2021, yangStrainEngineeringTwodimensional2021, zahraCriticalAnalysisFerroelectric2025, zhangEmergingFrontiersTwodimensional2025, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08
---

# ferroelasticity

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


铁弹性（ferroelasticity）指材料存在**两个及以上等价取向态（畴）**，可通过外加应力在取向态之间切换，并呈现应力-应变滞回线的现象。铁弹体、铁电体与铁磁体同属"铁性体（ferroics）"，铁弹性常与铁电性、铁磁性耦合共存，是多铁材料研究的重要组分。

## 👵 太奶导读

太奶啊，铁弹材料像一块"记性好"的橡皮泥：它内部被分成方向不同的小块（畴），你用力捏它，能把某一块"捏转方向"（畴切换），而且捏完之后它会"记得"新方向（有滞回，类似磁性材料的磁滞）。这种"记得住应力"的性质，让铁弹材料能当机械开关，还常和铁电（记得住电压）、铁磁（记得住磁场）搭伙出现。

## 🏗️ 结构概览

铁弹性属于"铁性体"（ferroic）家族，与铁电、铁磁并列；其核心是应变序参量的多稳态。铁弹体通常伴随结构相变出现，按维度分为体相铁弹与二维铁弹（β'-In₂Se₃、WTe₂ 孪晶界）。

## 🧩 核心内容与机制 (Core Content)

- **铁性体家族**：铁弹、铁电、铁磁共属"铁性体"，皆由序参量的多稳态与滞回开关定义（本库 ferroic-order 相关）；同时具备两种以上铁性的材料即多铁（multiferroic）。
- **铁弹畴**：不同应变取向的畴以孪晶界（twin boundary）分隔；应力驱动畴切换，产生应力-应变滞回线。
- **与铁电的耦合**：多数铁电体本身也是铁弹体（极化-应变耦合），畴结构同时受电场与应力调控（本库 TMD 铁弹性与畴物理论文、In₂Se₃ 双铁性）。
- **二维体系**：二维材料（如 β'-In₂Se₃、WTe₂ 孪晶界）中铁弹畴与电子/拓扑性质关联（本库 xuTwodimensional2021、wangFormation2019）。
- **表征与应用**：压电力显微镜（PFM）、偏光显微镜与 X 射线衍射表征畴；铁弹畴切换可用于机械存储与可重构器件。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：铁弹常与铁电共存耦合。
- [[../concepts/domain-wall|畴壁]]：铁弹畴的界面。
- [[../concepts/structural-phase-transition|结构相变]]：铁弹序源于结构相变。
- [[../concepts/ferroic-order|铁性序]]：铁弹属铁性体家族。
- [[../concepts/2d-materials|二维材料]]：二维铁弹体系。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 序参量 | 应变取向 | 多稳态铁弹畴 |
| 滞回线 | 应力-应变响应 | 应力驱动畴切换 |
| 孪晶界 | 铁弹畴界面 | 可移动、可重构 |
| 耦合序 | 与铁电/磁性耦合 | 多铁性基础 |
| 调控手段 | 应力/电场 | 机械存储、可重构器件 |

## 🔀 近邻概念辨析

- **铁弹 vs 铁电**：铁弹以应变序参量、应力翻转；铁电以极化序参量、电场翻转；多数铁电体同时铁弹。
- **铁弹 vs 弹性**：弹性是线性可逆应力-应变；铁弹有多稳态与非线性的滞回开关。
- **铁弹 vs 多铁**：铁弹是单一铁性序；多铁需两种以上铁性序共存。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 序参量 | 应变取向 | 多稳态铁弹畴 |
| 滞回线 | 应力-应变响应 | 应力驱动畴切换 |
| 孪晶界 | 铁弹畴界面 | 可移动、可重构 |
| 耦合序 | 与铁电/磁性耦合 | 多铁性基础 |
| 调控手段 | 应力/电场 | 机械存储、可重构器件 |

## 🔀 近邻概念辨析

- **铁弹 vs 铁电**：铁弹以应变序参量、应力翻转；铁电以极化序参量、电场翻转；多数铁电体同时铁弹。
- **铁弹 vs 弹性**：弹性是线性可逆应力-应变；铁弹有多稳态与非线性的滞回开关。
- **铁弹 vs 多铁**：铁弹是单一铁性序；多铁需两种以上铁性序共存。

## 📚 相关论文 (Related Papers) Papers)

- [[../papers/Chen2016electrical]] — Electrical and mechanical switching of ferroelectric polarization in the 70 nm BiFeO3 film
- [[../papers/FerroelectricityMultiferroicityAtomic2023]] — Ferroelectricity and multiferroicity down to the atomic thickness
- [[../papers/Jin2015studying]] — Studying the Polarization Switching in Polycrystalline BiFeO3 Films by 2D Piezoresponse Force Microscopy
- [[../papers/RecentAdvancesGrowth2025]] — Recent advances in growth, characterization, and application of two-dimensional multiferroic materials
- [[../papers/bhowalPolarMetalsPrinciples2023b]] — Polar Metals: Principles and Prospects
- [[../papers/chenFerromagneticNonmagnetic1T2022]] — Ferromagnetic and nonmagnetic 1T′ charge density wave states in transition metal dichalcogenides: Physical mechanisms and charge doping induced reversible transition
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in two-dimensional Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/fiebigEvolutionMultiferroics2016]] — The evolution of multiferroics
- [[../papers/gaoStrainEngineeringFerroelectric2024]] — Strain engineering of ferroelectric polarization and domain in the two-dimensional multiferroic semiconductor
- [[../papers/gomez-ortizKittelLawDomain2023]] — Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices
- [[../papers/guanRecentProgressTwoDimensional2020]] — Recent Progress in Two‐Dimensional Ferroelectric Materials
- [[../papers/hanPolarTopologicalMaterials2025]] — Polar topological materials and devices: Prospects and challenges
- [[../papers/heSwitchingTwodimensionalSliding2025]] — Switching Two-Dimensional Sliding Ferroelectrics by Mechanical Bending
- [[../papers/hillWhyAreThere2000a]] — Why Are There so Few Magnetic Ferroelectrics?
- [[../papers/houStrainbasedRoomtemperatureNonvolatile2019]] — Strain-based room-temperature non-volatile MoTe2 ferroelectric phase change transistor
- [[../papers/huProgressProspectsLowdimensional2019]] — Progress and prospects in low‐dimensional multiferroic materials
- [[../papers/huangPolarPhaseDomain2019]] — Polar and phase domain walls with conducting interfacial states in a Weyl semimetal MoTe2
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/liFerroelasticityDomainPhysics2016]] — Ferroelasticity and domain physics in two-dimensional transition metal dichalcogenide monolayers
- [[../papers/liMonolayerPuckeredPentagonal2022]] — Monolayer puckered pentagonal VTe2: An emergent two-dimensional ferromagnetic semiconductor with multiferroic coupling
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]] — Multiferroics: different routes to magnetoelectric coupling
- [[../papers/pedramraziManipulatingTopologicalDomain2019]] — Manipulating Topological Domain Boundaries in the Single-Layer Quantum Spin Hall Insulator 1T′–WSe₂
- [[../papers/rameshMultiferroicsProgressProspects2007]] — Multiferroics: progress and prospects in thin films
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] — A room-temperature ferroelectric semimetal
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]] — Advances in magnetoelectric multiferroics
- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]] — The Renaissance of Magnetoelectric Multiferroics
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications
- [[../papers/tangMultiferroicityTwodimensionalVan2025]] — Towards Multiferroicity in Two-Dimensional Van Der Waals Materials: Challenges and Opportunities
- [[../papers/wangFormationMechanismTwin2019]] — Formation mechanism of twin domain boundary in 2D materials: The case for WTe2
- [[../papers/wuSlidingFerroelectricity2D2021a]] — Sliding ferroelectricity in 2D van der Waals materials: Related physics and future opportunities
- [[../papers/xuTunableFerroelectricTopological2022]] — Tunable ferroelectric topological defects on 2D topological surfaces: strain engineering skyrmion-like polar structures in 2D materials
- [[../papers/xuTwodimensionalFerroelasticityVan2021]] — Two-dimensional ferroelasticity in van der Waals β'-In2Se3
- [[../papers/xunCoexistingMagnetismFerroelectric2024]] — Coexisting Magnetism, Ferroelectric, and Ferrovalley Multiferroic in Stacking-Dependent Two-Dimensional Materials
- [[../papers/yangRipplingFerroicPhase2021]] — Rippling Ferroic Phase Transition and Domain Switching In 2D Materials
- [[../papers/yangStrainEngineeringTwodimensional2021]] — Strain engineering of <scp>two‐dimensional</scp> materials: Methods, properties, and applications
- [[../papers/zahraCriticalAnalysisFerroelectric2025]] — A critical analysis of ferroelectric and ferromagnetic properties in two-dimensional MXene
- [[../papers/zhangEmergingFrontiersTwodimensional2025]] — Emerging frontiers in two-dimensional sliding ferroelectrics
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] — High-throughput exfoliation of multiferroic ternary oxide monolayers with high transition temperature and giant spin splitting
