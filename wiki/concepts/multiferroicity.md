---
tags: [concept, multiferroics, ferroelectricity, magnetism]
title: 多铁性 / Multiferroicity
type: concept
status: mature
domain: [condensed-matter-physics, multiferroics]
mechanism: 同一相中两种或以上铁性序（铁电、磁性、铁弹等）的共存与耦合
related_concepts: [magnetoelectric-coupling, ferroelectricity, ferroelasticity, geometric-ferroelectricity]
papers: [spaldinRenaissanceMagnetoelectricMultiferroics2005, rameshMultiferroicsProgressProspects2007, prosandeevKittelLawInBiFeO3Ultrathin2010, Chen2016electrical, FerroelectricityMultiferroicityAtomic2023, Goswami2011multiferroic, Jin2015studying, Kim2008effect, Perugu2024morphology, RecentAdvancesGrowth2025, aiFerroelectricityCoexistedPorbital2022, aminiAtomicscaleVisualizationMultiferroicity2024, bhowalPolarMetalsPrinciples2023b, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenHafniumBasedFerroelectricPostMoore2026, chenStrongSlidingFerroelectricity2024, cheongMultiferroicsMagneticTwist2007a, cuiIntercorrelatedInplaneOutofplane2018a, deSousa2008electrical, feiFerroelectricSwitchingTwodimensional2018a, fengFerroelectricityMultiferroicityTwodimensional2020, fiebigEvolutionMultiferroics2016, gaoGiantChiralMagnetoelectric2024a, gaoStrainEngineeringFerroelectric2024, gomez-ortizKittelLawDomain2023, guanRecentProgressTwoDimensional2020, guoAdvancesTwodimensionalFerroelectric2025, hanPolarTopologicalMaterials2025, hanTunableSlidingFerroelectricity2025, hillWhyAreThere2000a, huProgressProspectsLowdimensional2019, huangTwodimensionalIn2Se3Rising2022, kaurRecentAdvancesTheoretical2025a, laiTwodimensionalFerromagnetismDriven2019, liFerroelasticityDomainPhysics2016, liMonolayerPuckeredPentagonal2022, liPhaseTransitions2D2021, martinThinfilmFerroelectricMaterials2016, miaoMagneticFerroelectricMetal2024, mostovoyMultiferroicsDifferentRoutes2024, neumayerCompetingPolarPhases2025, sharmaRoomtemperatureFerroelectricSemimetal2019, songEvidenceSinglelayerVan2022, spaldinAdvancesMagnetoelectricMultiferroics2019, sunSlidingFerroelectricityTwodimensional2025, tahirFerroelectricityNonvolatileMemristor2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, wangTunableD0Topological2025b, wangTwodimensionalFerroelectricMetal2025, wuCoexistenceFerroelectricityAntiferroelectricity2024, wuNonvolatileSwitchableHalfmetallicity2024, wuSlidingFerroelectricity2D2021a, xiangTwodimensionalRoomTemperature2020, xuTwodimensionalFerroelasticityVan2021, xunCoexistingMagnetismFerroelectric2024, yangRipplingFerroicPhase2021, yuFerroelectricControlMagnetism2026, zahraCriticalAnalysisFerroelectric2025, zhangEmergingFrontiersTwodimensional2025, zhangNonvolatileControlTopological2025, zhaoOpticalFingerprintsTwodimensional2024, zhaoRealization2DMultiferroic2024, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08
---

# 多铁性 / Multiferroicity

多铁性 (Multiferroicity) 指的是一种材料在同一相中同时具有两种或两种以上的“铁性”有序（Primary Ferroics），最常见的是铁电性 (Ferroelectricity) 和铁磁性/反铁磁性 (Magnetism) 的共存。这类材料最具吸引力的特性是磁电耦合效应 (Magnetoelectric Coupling)，即可以用电场控制磁化强度，或用磁场控制电极化。

## 👵 太奶导读

乖孙，这“多铁性”就像是材料界的“全能运动员”。
通常材料要么“通电”（像铁电体，有一排排整齐的电箭头），要么“带磁”（像磁铁，有一排排磁箭头），它们俩平时各过各的，很少凑在一起。
多铁性材料厉害就在于它把这两样本事都学会了。更神的是，你动动它的电，它的磁也会跟着变；你晃晃磁铁，它的电又会有反应。这就像你按了一下灯开关（电信号），结果家里的收音机响了（磁信号），两边是通着的。科学家们想用它来做一种特别省电的电脑硬盘，一按电门就能改写数据，不用像现在这样费劲费电。

## 🏗️ 结构概览：相控制三角图

多铁性的核心在于不同序参量之间的交叉调控。

![图：铁性体与多铁性体中的相控制示意](../../raw/figures/prosandeevKittelLawInBiFeO3Ultrathin2010/eq_1_QC77D3EP.png)
*   **看图要点**：图中展示了电场(E)-极化(P)、磁场(H)-磁化(M)、应力(σ)-应变(ε)三组共轭变量。多铁性材料位于这些圆圈的重叠区，绿色箭头代表跨序的磁电耦合效应。
*   **来源**：[[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]] -> [[../figures/mathematical-models-magnetoelectric|磁电耦合与多铁理论]]
*(注：该图描述基于 Spaldin 2005 文献描述，暂引用 BFO 模型的哈密顿量图示作为机制补充)*

## 🧩 机制与电子结构互斥

Nicola Spaldin 在 2000 年提出了著名的 $d^0$ vs $d^n$ 互斥律：传统位移型铁电体需要过渡金属离子具有空的 d 轨道以形成共价偏心位移，而磁性则需要部分填充的 d 轨道。这一化学禁忌使得单相多铁材料在自然界中极其稀少。

为了绕过这一限制，科学家们开发了多种新机制：
1. **孤对电子驱动**：如 BiFeO₃ 中的 Bi³⁺ $6s^2$ 孤对电子。
2. **几何驱动**：如 HoMnO₃ 中 MnO₅ 双锥的倾斜。
3. **自旋驱动/磁致铁电**：如 TbMnO₃ 中破缺反演对称的螺旋磁序。

## 📚 相关论文 (Related Papers)

- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]：阐述了多铁性复兴的理论背景及核心矛盾。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：系统综述了薄膜多铁性的进展，提出了水平与垂直异质结范式。
- [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]：探讨了多铁薄膜中畴结构的标度律及其非传统起源。
- [[../papers/Chen2016electrical]]
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]
- [[../papers/Goswami2011multiferroic]]
- [[../papers/Jin2015studying]]
- [[../papers/Kim2008effect]]
- [[../papers/Perugu2024morphology]]
- [[../papers/RecentAdvancesGrowth2025]]
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]
- [[../papers/bhowalPolarMetalsPrinciples2023b]]
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]
- [[../papers/chenStrongSlidingFerroelectricity2024]]
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]
- [[../papers/deSousa2008electrical]]
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]
- [[../papers/fiebigEvolutionMultiferroics2016]]
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]
- [[../papers/gaoStrainEngineeringFerroelectric2024]]
- [[../papers/gomez-ortizKittelLawDomain2023]]
- [[../papers/guanRecentProgressTwoDimensional2020]]
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]
- [[../papers/hanPolarTopologicalMaterials2025]]
- [[../papers/hanTunableSlidingFerroelectricity2025]]
- [[../papers/hillWhyAreThere2000a]]
- [[../papers/huProgressProspectsLowdimensional2019]]
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]
- [[../papers/kaurRecentAdvancesTheoretical2025a]]
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]
- [[../papers/liFerroelasticityDomainPhysics2016]]
- [[../papers/liMonolayerPuckeredPentagonal2022]]
- [[../papers/liPhaseTransitions2D2021]]
- [[../papers/martinThinfilmFerroelectricMaterials2016]]
- [[../papers/miaoMagneticFerroelectricMetal2024]]
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]
- [[../papers/neumayerCompetingPolarPhases2025]]
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]
- [[../papers/songEvidenceSinglelayerVan2022]]
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]]
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]
- [[../papers/wangTunableD0Topological2025b]]
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]
- [[../papers/wuSlidingFerroelectricity2D2021a]]
- [[../papers/xiangTwodimensionalRoomTemperature2020]]
- [[../papers/xuTwodimensionalFerroelasticityVan2021]]
- [[../papers/xunCoexistingMagnetismFerroelectric2024]]
- [[../papers/yangRipplingFerroicPhase2021]]
- [[../papers/yuFerroelectricControlMagnetism2026]]
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]
- [[../papers/zhangNonvolatileControlTopological2025]]
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]
- [[../papers/zhaoRealization2DMultiferroic2024]]
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/magnetoelectric-coupling|磁电耦合]]（核心功能）
- [[../concepts/geometric-ferroelectricity|几何铁电性]]（绕开机制）
- [[../entities/BiFeO3|BiFeO₃]]（室温多铁明星材料）
- [[../entities/HoMnO3|HoMnO₃]]（几何多铁代表）
