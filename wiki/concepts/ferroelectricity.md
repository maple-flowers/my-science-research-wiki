---
tags: [concept]
title: 'ferroelectricity'
type: concept
status: developing
papers: ['FerroelectricityMultiferroicityAtomic2023', 'Perugu2024morphology', 'RecentAdvancesGrowth2025', 'aminiAtomicscaleVisualizationMultiferroicity2024', 'chenHafniumBasedFerroelectricPostMoore2026', 'chenStrongSlidingFerroelectricity2024', 'cheongMultiferroicsMagneticTwist2007a', 'cuiIntercorrelatedInplaneOutofplane2018a', 'dingPredictionIntrinsicTwodimensional2017a', 'feiFerroelectricSwitchingTwodimensional2018a', 'fiebigEvolutionMultiferroics2016', 'gongAbsenceCriticalThickness2023', 'guanRecentProgressTwoDimensional2020', 'guoAdvancesTwodimensionalFerroelectric2025', 'hillWhyAreThere2000a', 'huProgressProspectsLowdimensional2019', 'huangPolarPhaseDomain2019', 'huangTwodimensionalIn2Se3Rising2022', 'junqueraCriticalThicknessFerroelectricity2003', 'kaurRecentAdvancesTheoretical2025a', 'king-smithTheoryPolarizationCrystalline1993', 'miaoMagneticFerroelectricMetal2024', 'nahasFrustrationSelfOrderingTopological2016', 'rameshMultiferroicsProgressProspects2007', 'sattarFunctionalizedDoubleTransition2025', 'sharmaRoomtemperatureFerroelectricSemimetal2019', 'shenEmergenceMultipleFerroelectric2025', 'spaldinAdvancesMagnetoelectricMultiferroics2019', 'sunSlidingFerroelectricityTwodimensional2025', 'tahirFerroelectricityNonvolatileMemristor2025', 'tangMultiferroicityTwodimensionalVan2025', 'tianRoomtemperatureTwodimensionalMultiferroic2026', 'wuCoexistenceFerroelectricityAntiferroelectricity2024', 'wuSlidingFerroelectricity2D2021a', 'xiangTwodimensionalRoomTemperature2020', 'xuTwodimensionalFerroelasticityVan2021', 'xunCoexistingMagnetismFerroelectric2024', 'yuFerroelectricControlMagnetism2026', 'zahraCriticalAnalysisFerroelectric2025']
updated: 2026-08-18
---

# ferroelectricity

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


铁电性（ferroelectricity）指材料在某一温度范围内存在**自发极化**，且该极化方向可被外加电场翻转的性质。它源于晶体中正负电荷中心的不重合（极性空间群），与压电性、热释电性同属极性晶体家族；当铁电转变温度以下极化呈现滞回行为时，材料可作为非易失存储与逻辑器件的基础。

## 👵 太奶导读

太奶啊，铁电性就是材料内部自己"带电分家"：正电荷中心和负电荷中心本来应该重合，但在某些材料里它们天生错开，于是在材料里形成一个固定的电偶极子。更神奇的是，你用外加电场一拉，这个偶极子的方向能整个翻转过来，翻完还能"记住"——断电了也不变。这一"记性"让铁电材料能当存储、做开关。近年二维材料里也发现了铁电（甚至只有一层原子厚），还能靠层与层之间"滑一滑"就翻转极化，叫滑动铁电。

## 🏗️ 结构概览

铁电性是有序极性相的一种，与压电、热释电、铁弹及多铁序紧密关联；其稳定性由退极化场、尺寸效应与材料对称性共同决定。

- **材料谱系**：钙钛矿氧化物（BaTiO₃、BiFeO₃）、HfO₂ 基、有机/聚合物与二维范德华铁电（In₂Se₃、滑动铁电）。
- **维度效应**：体相铁电在超薄膜中受退极化场抑制（临界厚度），二维与滑动铁电体系突破该限制（[[../papers/junqueraCriticalThicknessFerroelectricity2003|Junquera 2003]]）。
- **与其它有序态**：与磁性共存→多铁体；与弹性应变耦合→铁弹性。

## 🧩 核心内容与机制 (Core Content)

- **自发极化与翻转**：铁电体的自发极化可被外电场重新取向，极化-电场曲线呈滞回线，这是铁电性与普通介电/压电体的核心区别。
- **居里转变**：温度高于居里温度时材料进入顺电相，自发极化消失，伴随结构相变（如钙钛矿的立方→四方→正交→菱方序列）。
- **现代极化理论**：极化不能被简单理解为"束缚电荷密度"，需用 Berry 相（现代极化理论，King-Smith–Vanderbilt 形式）严格定义，因而与拓扑、Berry 相位概念紧密相连。
- **临界厚度问题**：经典观点认为铁电性在超薄膜中会被退极化场抑制（如钙钛矿存在临界厚度），而二维与滑动铁电体系在原子极限下仍可保持极化，突破了这一限制。
- **与多铁性的关系**：铁电序与磁序共存的材料即多铁体；电极化可与磁性耦合（磁电耦合），是低功耗自旋电子器件的核心素材。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/multiferroicity|多铁性]]：铁电序与磁序共存的宏观现象。
- [[../concepts/berry-phase|Berry 相]]：现代极化理论中极化的严格定义手段。
- [[../concepts/sliding-ferroelectricity|滑动铁电]]：二维层状材料中依赖层间滑移产生的铁电。
- [[../concepts/2d-materials|二维材料]]：原子极限下铁电性得以保留的材料平台。
- [[../concepts/charge-density-wave|电荷密度波]]：常与铁电/多铁序竞争的电子晶格序。
- [[../entities/BaTiO3|BaTiO₃]]：钙钛矿型铁电体的原型材料。
- [[../entities/BiFeO3|BiFeO₃]]：室温多铁体，铁电与反铁磁共存。
- [[../entities/In2Se3|In₂Se₃]]：二维铁电半导体，面内/面外极化共存。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 自发极化 P_s | 零场极化强度 | BaTiO₃ 约 26 µC/cm² |
| 居里温度 T_C | 铁电-顺电转变 | 材料相关（可达数百 K） |
| 矫顽场 | 极化翻转阈值 | 决定写入电压/功耗 |
| 临界厚度 | 铁电消失厚度 | 钙钛矿纳米级；2D 可至单层 |
| 极化翻转方式 | 调控手段 | 电场、应变、滑移、离子迁移 |

## 🔀 近邻概念辨析

- **铁电 vs 压电 vs 热释电**：压电材料有压电系数但无自发极化；热释电有自发极化且温度可调；铁电更进一步——自发极化可被电场翻转（滞回线）。
- **铁电 vs 反铁电**：铁电净极化非零且可翻转；反铁电相邻极化反排、净极化为零，呈双回线。
- **铁电 vs 多铁**：铁电只含极性序；多铁同时含铁电序与磁（或铁弹）序，是铁电与磁耦合的平台。

## 📚 相关论文 (Related Papers)

- [[../papers/FerroelectricityMultiferroicityAtomic2023]] — Ferroelectricity and multiferroicity down to the atomic thickness
- [[../papers/Perugu2024morphology]] — Synthesis, Structural, Morphology and Magnetic Properties: Effect of La on Multiferroic Nature of BiFeO3 Nanoparticles
- [[../papers/RecentAdvancesGrowth2025]] — Recent advances in growth, characterization, and application of two-dimensional multiferroic materials
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] — Atomic-Scale Visualization of Multiferroicity in Monolayer NiI2
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]] — Hafnium-Based Ferroelectric Post-Moore Electronics: Device Physics, Integration Architectures, and Neuromorphic System Implementation
- [[../papers/chenStrongSlidingFerroelectricity2024]] — Strong Sliding Ferroelectricity and Interlayer Sliding Controllable Spintronic Effect in Two-Dimensional HgI₂ Layers
- [[../papers/cheongMultiferroicsMagneticTwist2007a]] — Multiferroics: a magnetic twist for ferroelectricity
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]] — Intercorrelated In-Plane and Out-of-Plane Ferroelectricity in Ultrathin Two-Dimensional Layered Semiconductor In2Se3
- [[../papers/dingPredictionIntrinsicTwodimensional2017a]] — Prediction of intrinsic two-dimensional ferroelectrics in In2Se3 and other III2-VI3 van der Waals materials
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]] — Ferroelectric switching of a two-dimensional metal
- [[../papers/fiebigEvolutionMultiferroics2016]] — The evolution of multiferroics
- [[../papers/gongAbsenceCriticalThickness2023]] — Absence of critical thickness for polar skyrmions with breaking the Kittel’s law
- [[../papers/guanRecentProgressTwoDimensional2020]] — Recent Progress in Two‐Dimensional Ferroelectric Materials
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]] — Advances in two-dimensional ferroelectric materials
- [[../papers/hillWhyAreThere2000a]] — Why Are There so Few Magnetic Ferroelectrics?
- [[../papers/huProgressProspectsLowdimensional2019]] — Progress and prospects in low‐dimensional multiferroic materials
- [[../papers/huangPolarPhaseDomain2019]] — Polar and phase domain walls with conducting interfacial states in a Weyl semimetal MoTe2
- [[../papers/huangTwodimensionalIn2Se3Rising2022]] — Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]] — Critical thickness for ferroelectricity in perovskite ultrathin films
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/king-smithTheoryPolarizationCrystalline1993]] — Theory of polarization of crystalline solids
- [[../papers/miaoMagneticFerroelectricMetal2024]] — Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding
- [[../papers/nahasFrustrationSelfOrderingTopological2016]] — Frustration and Self-Ordering of Topological Defects in Ferroelectrics
- [[../papers/rameshMultiferroicsProgressProspects2007]] — Multiferroics: progress and prospects in thin films
- [[../papers/sattarFunctionalizedDoubleTransition2025]] — Functionalized double transition metal Mo2Ti2C3Tx ferroelectric MXene and laser-reduced graphene based flexible memristors for next-generation two-dimensional ferrotronics
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] — A room-temperature ferroelectric semimetal
- [[../papers/shenEmergenceMultipleFerroelectric2025]] — Emergence of multiple ferroelectric states in multilayer black phosphorus
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]] — Advances in magnetoelectric multiferroics
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]] — Ferroelectricity and Nonvolatile Memristor Applications of Free‐Standing 2D Niobium Carbide: A New Frontier of Free‐Standing MXene in Electronic Devices
- [[../papers/tangMultiferroicityTwodimensionalVan2025]] — Towards Multiferroicity in Two-Dimensional Van Der Waals Materials: Challenges and Opportunities
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]] — Room-temperature two-dimensional multiferroic metal with voltage-controllable magnetic order
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]] — Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic
- [[../papers/wuSlidingFerroelectricity2D2021a]] — Sliding ferroelectricity in 2D van der Waals materials: Related physics and future opportunities
- [[../papers/xiangTwodimensionalRoomTemperature2020]] — Towards two-dimensional room temperature multiferroics
- [[../papers/xuTwodimensionalFerroelasticityVan2021]] — Two-dimensional ferroelasticity in van der Waals β'-In2Se3
- [[../papers/xunCoexistingMagnetismFerroelectric2024]] — Coexisting Magnetism, Ferroelectric, and Ferrovalley Multiferroic in Stacking-Dependent Two-Dimensional Materials
- [[../papers/yuFerroelectricControlMagnetism2026]] — Ferroelectric Control of Magnetism and Giant Magnetoresistance Via Intercalation-Induced Symmetry Breaking in Two-Dimensional Multiferroics with Strong Magnetoelectric Coupling
- [[../papers/zahraCriticalAnalysisFerroelectric2025]] — A critical analysis of ferroelectric and ferromagnetic properties in two-dimensional MXene
