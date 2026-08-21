---
tags: [concept, multiferroics, spintronics]
title: 磁电耦合 / Magnetoelectric Coupling
type: concept
status: mature
domain: [condensed-matter-physics, multiferroics, spintronics]
mechanism: 电场调控磁性（逆磁电效应）或磁场调控极化（直接磁电效应）的现象
related_concepts: [multiferroicity, ferroelectricity, spin-orbit-coupling, rashba-effect, exchange-bias]
papers: [caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenStrongSlidingFerroelectricity2024, spaldinRenaissanceMagnetoelectricMultiferroics2005, cheongMultiferroicsMagneticTwist2007a, Chen2016electrical, FerroelectricityMultiferroicityAtomic2023, Goswami2011multiferroic, Jin2015studying, Perugu2024morphology, RecentAdvancesGrowth2025, aiFerroelectricityCoexistedPorbital2022, aminiAtomicscaleVisualizationMultiferroicity2024, bhowalPolarMetalsPrinciples2023b, deSousa2008electrical, fengFerroelectricityMultiferroicityTwodimensional2020, fiebigEvolutionMultiferroics2016, gaoGiantChiralMagnetoelectric2024a, guanRecentProgressTwoDimensional2020, hanPolarTopologicalMaterials2025, hanTunableSlidingFerroelectricity2025, hillWhyAreThere2000a, huProgressProspectsLowdimensional2019, huangTwodimensionalIn2Se3Rising2022, kaurRecentAdvancesTheoretical2025a, krishnamurthiSpinChargeDensity2020, laiTwodimensionalFerromagnetismDriven2019, liMonolayerPuckeredPentagonal2022, liPhaseTransitions2D2021, liuSpintronicsTwoDimensionalMaterials2020b, martinThinfilmFerroelectricMaterials2016, miaoMagneticFerroelectricMetal2024, mostovoyMultiferroicsDifferentRoutes2024, prosandeevKittelLawInBiFeO3Ultrathin2010, rameshMultiferroicsProgressProspects2007, songEvidenceSinglelayerVan2022, spaldinAdvancesMagnetoelectricMultiferroics2019, sunSlidingFerroelectricityTwodimensional2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, wangTunableD0Topological2025b, wangTwodimensionalFerroelectricMetal2025, wuCoexistenceFerroelectricityAntiferroelectricity2024, wuNonvolatileSwitchableHalfmetallicity2024, wuSlidingFerroelectricity2D2021a, xiangTwodimensionalRoomTemperature2020, xunCoexistingMagnetismFerroelectric2024, yuFerroelectricControlMagnetism2026, zahraCriticalAnalysisFerroelectric2025, zhangEmergingFrontiersTwodimensional2025, zhangNonvolatileControlTopological2025, zhaoOpticalFingerprintsTwodimensional2024, zhaoRealization2DMultiferroic2024, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08
---

# 磁电耦合 / Magnetoelectric Coupling

磁电耦合 (Magnetoelectric Coupling, ME) 是指材料的电学序参量（如电极化 $P$）与磁学序参量（如磁化强度 $M$）之间相互感应、相互调控的物理现象。它分为直接磁电效应（磁场诱导极化）和逆磁电效应（电场诱导磁化）。在现代信息技术中，利用逆磁电效应实现超低功耗的电控磁存储和逻辑器件是该领域的核心驱动力。

## 👵 太奶导读

好孩子，这“磁电耦合”听着玄乎，其实就像是咱家里的那个老式连通器。
以前电是电，磁是磁，就像两个互不相干的水箱。你要想让磁水箱里的水（磁信号）动一动，就得费劲去摇晃磁铁。
现在有了磁电耦合，这两个水箱之间接通了一根管子。你只要轻轻按一下电水箱这边的开关（电信号），磁水箱那边的水就会跟着起反应。
科学家们最稀罕的就是这种本事，因为用电来管磁，比直接用磁铁去管磁要省电得多，速度还快。以后咱们的手机、电脑用上这种技术，可能充一次电就能用好几个星期呢！

## 🏗️ 结构概览：二维多铁异质结中的磁电耦合

在二维范德华材料中，磁电耦合常通过构建异质结来实现，利用界面效应绕开单相材料的互斥限制。

![图：二维多铁异质结中的非对称双栅磁电调控示意](../../raw/figures/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025/fig_1_A3L3NFIH.png)
*   **看图要点**：图中展示了由 Fe₃GaTe₂ 铁磁层与 P(VDF-TrFE) 铁电层构成的垂直异质结。底栅极的逆压电效应产生面内应变，通过范德华界面传递至铁磁层，改变其磁各向异性常数 $K_1$。
*   **来源**：[[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 物理机制分类

磁电耦合根据微观机制可分为以下几类：
1.  **应变介导 (Strain-mediated)**：通过压电/铁电层产生的晶格形变传递至自旋序，改变磁各向异性。这是目前二维多铁异质结中实现室温、非易失性调控的主流方案。
2.  **电荷介导 (Charge-mediated)**：通过电场效应改变磁性界面处的载流子浓度或轨道占据，从而调控交换相互作用。
3.  **自旋-轨道耦合介导 (SOC-mediated)**：利用铁电极化翻转打破界面反演对称性，反转 Rashba 场或 Dzyaloshinskii-Moriya 相互作用 (DMI)，实现对自旋纹理的操控。

## 📚 相关论文 (Related Papers)

- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：演示了基于应变介导机制的超低功耗 (0.5 aJ) 二维逻辑器件。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：探讨了滑动铁电中极化翻转对 Rashba 自旋纹理的电荷/对称性调控。
- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]：综述了磁电多铁性的物理起源与挑战。
- [[../papers/Chen2016electrical]]：从实验研究角度梳理了「Electrical and mechanical switching of ferroelectric polarization in the 70 nm BiFeO3 film」。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：从综述角度梳理了「Ferroelectricity and multiferroicity down to the atomic thickness」。
- [[../papers/Goswami2011multiferroic]]：从实验研究角度梳理了「Multiferroic coupling in nanoscale BiFeO3」。
- [[../papers/Jin2015studying]]：从实验研究角度梳理了「Studying the Polarization Switching in Polycrystalline BiFeO3 Films by 2D Piezoresponse Force Microscopy」。
- [[../papers/Perugu2024morphology]]：从实验研究角度梳理了「Synthesis, Structural, Morphology and Magnetic Properties: Effect of La on Multiferroic Nature of BiFeO3 Nanoparticles」。
- [[../papers/RecentAdvancesGrowth2025]]：从综述角度梳理了「二维多铁性材料的生长、表征及应用研究进展」。
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]：从理论分析角度梳理了「二维金属氮氧化物中的铁电性与p轨道铁磁性和金属丰度共存」。
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]：从实验研究角度梳理了「Atomic-Scale Visualization of Multiferroicity in Monolayer NiI2」。
- [[../papers/bhowalPolarMetalsPrinciples2023b]]：从综述角度梳理了「极性金属：原理与展望」。
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：从理论分析角度梳理了「多铁性：铁电的磁扭曲」。
- [[../papers/deSousa2008electrical]]：从理论分析角度梳理了「Electrical control of magnon propagation in multiferroic BiFeO3 films」。
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]：从理论分析角度梳理了「二维 Sc₂P₂Se₆ 与 ScCrP₂Se₆ 单层的铁电性与多铁性」。
- [[../papers/fiebigEvolutionMultiferroics2016]]：从综述角度梳理了「多铁性的演化」。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：从实验研究角度梳理了「范德瓦尔斯多铁材料中的巨手征磁电振荡」。
- [[../papers/guanRecentProgressTwoDimensional2020]]：从综述角度梳理了「Recent Progress in Two‐Dimensional Ferroelectric Materials」。
- [[../papers/hanPolarTopologicalMaterials2025]]：从综述角度梳理了「Polar topological materials and devices: Prospects and challenges」。
- [[../papers/hanTunableSlidingFerroelectricity2025]]：从理论分析角度梳理了「Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers」。
- [[../papers/hillWhyAreThere2000a]]：从理论分析角度梳理了「为什么磁性铁电体这么少？」。
- [[../papers/huProgressProspectsLowdimensional2019]]：从综述角度梳理了「低维多铁性材料的研究进展与展望」。
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]：从综述角度梳理了「Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage」。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：从综述角度梳理了「Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials」。
- [[../papers/krishnamurthiSpinChargeDensity2020]]：从理论分析角度梳理了「过渡金属二元化合物界面上的自旋/电荷密度波」。
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]：从实验研究角度梳理了「范德华 CuCrP₂S₆ 中的二维铁磁性和驱动铁电性」。
- [[../papers/liMonolayerPuckeredPentagonal2022]]：从理论分析角度梳理了「单层折叠五边形VTe2:一种具有多铁性耦合的二维铁磁半导体」。
- [[../papers/liPhaseTransitions2D2021]]：从综述角度梳理了「Phase transitions in 2D materials」。
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：从综述角度梳理了「Spintronics in Two-Dimensional Materials」。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：从综述角度梳理了「铁电薄膜材料及其应用」。
- [[../papers/miaoMagneticFerroelectricMetal2024]]：从理论分析角度梳理了「Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding」。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：从综述角度梳理了「多铁性：磁电耦合的不同途径」。
- [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]：从理论分析角度梳理了「Kittel Law in BiFeO3 Ultrathin Films: A First-Principles-Based Study」。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：从综述角度梳理了「多铁性：薄膜研究进展与展望」。
- [[../papers/songEvidenceSinglelayerVan2022]]：从实验研究角度梳理了「Evidence for a single-layer van der Waals multiferroic」。
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：从综述角度梳理了「磁电多铁性材料研究进展」。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：从综述角度梳理了「Sliding ferroelectricity in two-dimensional materials and device applications」。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：从综述角度梳理了「二维范德华材料的多铁性：挑战与机遇」。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：从实验研究角度梳理了「具有电压可控磁序的室温二维多铁金属」。
- [[../papers/wangTunableD0Topological2025b]]：从理论分析角度梳理了「Tunable d0 topological magnetic states in multiferroic monolayer In2NO2」。
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]：从理论分析角度梳理了「Two-dimensional ferroelectric metal CuCrX2 (X = S, Se) for efficient electrocatalysis」。
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]：从实验研究角度梳理了「Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic」。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：从实验研究角度梳理了「MXene Hf₂MnC₂O₂/Sc₂CO₂ 多铁异质结中的非易失可开关半金属性与磁性」。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：从综述角度梳理了「二维范德华材料中的滑动铁电性：相关物理和未来机遇」。
- [[../papers/xiangTwodimensionalRoomTemperature2020]]：从综述角度梳理了「Towards two-dimensional room temperature multiferroics」。
- [[../papers/xunCoexistingMagnetismFerroelectric2024]]：从理论分析角度梳理了「Coexisting Magnetism, Ferroelectric, and Ferrovalley Multiferroic in Stacking-Dependent Two-Dimensional Materials」。
- [[../papers/yuFerroelectricControlMagnetism2026]]：从实验研究角度梳理了「强磁电耦合二维多铁性材料中嵌入诱导对称破缺对磁性和巨磁电阻的铁电控制」。
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]：从综述角度梳理了「二维MXene铁电和铁磁性质的临界分析」。
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]：从综述角度梳理了「二维滑动铁电体的新前沿」。
- [[../papers/zhangNonvolatileControlTopological2025]]：从理论分析角度梳理了「Nonvolatile control of topological magnetism in two-dimensional CrInTe2/In2Se3 multiferroic heterostructures」。
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]
- [[../papers/zhaoRealization2DMultiferroic2024]]
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/multiferroicity|多铁性]]（载体性质）
- [[../concepts/rashba-effect|Rashba 效应]]（自旋电子学耦合）
- [[../concepts/strain-engineering|应变工程]]（核心手段）
- [[../entities/Fe3GeTe2|Fe₃GaTe₂ / Fe₃GeTe₂]]（典型二维铁磁体）
- [[../entities/BiFeO3|BiFeO₃]]（单相磁电耦合典型）
