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
- [[../papers/Chen2016electrical]]
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]
- [[../papers/Goswami2011multiferroic]]
- [[../papers/Jin2015studying]]
- [[../papers/Perugu2024morphology]]
- [[../papers/RecentAdvancesGrowth2025]]
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]
- [[../papers/bhowalPolarMetalsPrinciples2023b]]
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]
- [[../papers/deSousa2008electrical]]
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]
- [[../papers/fiebigEvolutionMultiferroics2016]]
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]
- [[../papers/guanRecentProgressTwoDimensional2020]]
- [[../papers/hanPolarTopologicalMaterials2025]]
- [[../papers/hanTunableSlidingFerroelectricity2025]]
- [[../papers/hillWhyAreThere2000a]]
- [[../papers/huProgressProspectsLowdimensional2019]]
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]
- [[../papers/kaurRecentAdvancesTheoretical2025a]]
- [[../papers/krishnamurthiSpinChargeDensity2020]]
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]
- [[../papers/liMonolayerPuckeredPentagonal2022]]
- [[../papers/liPhaseTransitions2D2021]]
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]
- [[../papers/martinThinfilmFerroelectricMaterials2016]]
- [[../papers/miaoMagneticFerroelectricMetal2024]]
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]
- [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]
- [[../papers/rameshMultiferroicsProgressProspects2007]]
- [[../papers/songEvidenceSinglelayerVan2022]]
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]
- [[../papers/wangTunableD0Topological2025b]]
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]
- [[../papers/wuSlidingFerroelectricity2D2021a]]
- [[../papers/xiangTwodimensionalRoomTemperature2020]]
- [[../papers/xunCoexistingMagnetismFerroelectric2024]]
- [[../papers/yuFerroelectricControlMagnetism2026]]
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]
- [[../papers/zhangNonvolatileControlTopological2025]]
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]
- [[../papers/zhaoRealization2DMultiferroic2024]]
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/multiferroicity|多铁性]]（载体性质）
- [[../concepts/rashba-effect|Rashba 效应]]（自旋电子学耦合）
- [[../concepts/strain-engineering|应变工程]]（核心手段）
- [[../entities/Fe3GeTe2|Fe₃GaTe₂ / Fe₃GeTe₂]]（典型二维铁磁体）
- [[../entities/BiFeO3|BiFeO₃]]（单相磁电耦合典型）
