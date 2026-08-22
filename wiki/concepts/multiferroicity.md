---
tags: [concept, multiferroics, ferroelectricity, magnetism]
title: 多铁性 / Multiferroicity
type: concept
status: developing
domain: [condensed-matter-physics, multiferroics]
mechanism: 同一相中两种或以上铁性序（铁电、磁性、铁弹等）的共存与耦合
related_concepts: [magnetoelectric-coupling, ferroelectricity, ferroelasticity, geometric-ferroelectricity]
papers: [spaldinRenaissanceMagnetoelectricMultiferroics2005, rameshMultiferroicsProgressProspects2007, prosandeevKittelLawInBiFeO3Ultrathin2010, Chen2016electrical, FerroelectricityMultiferroicityAtomic2023, Goswami2011multiferroic, Jin2015studying, Kim2008effect, Perugu2024morphology, RecentAdvancesGrowth2025, aiFerroelectricityCoexistedPorbital2022, aminiAtomicscaleVisualizationMultiferroicity2024, bhowalPolarMetalsPrinciples2023b, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenHafniumBasedFerroelectricPostMoore2026, chenStrongSlidingFerroelectricity2024, cheongMultiferroicsMagneticTwist2007a, cuiIntercorrelatedInplaneOutofplane2018a, deSousa2008electrical, feiFerroelectricSwitchingTwodimensional2018a, fengFerroelectricityMultiferroicityTwodimensional2020, fiebigEvolutionMultiferroics2016, gaoGiantChiralMagnetoelectric2024a, gaoStrainEngineeringFerroelectric2024, gomez-ortizKittelLawDomain2023, guanRecentProgressTwoDimensional2020, guoAdvancesTwodimensionalFerroelectric2025, hanPolarTopologicalMaterials2025, hanTunableSlidingFerroelectricity2025, hillWhyAreThere2000a, huProgressProspectsLowdimensional2019, huangTwodimensionalIn2Se3Rising2022, kaurRecentAdvancesTheoretical2025a, laiTwodimensionalFerromagnetismDriven2019, liFerroelasticityDomainPhysics2016, liMonolayerPuckeredPentagonal2022, liPhaseTransitions2D2021, martinThinfilmFerroelectricMaterials2016, miaoMagneticFerroelectricMetal2024, mostovoyMultiferroicsDifferentRoutes2024, neumayerCompetingPolarPhases2025, sharmaRoomtemperatureFerroelectricSemimetal2019, songEvidenceSinglelayerVan2022, spaldinAdvancesMagnetoelectricMultiferroics2019, sunSlidingFerroelectricityTwodimensional2025, tahirFerroelectricityNonvolatileMemristor2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, wangTunableD0Topological2025b, wangTwodimensionalFerroelectricMetal2025, wuCoexistenceFerroelectricityAntiferroelectricity2024, wuNonvolatileSwitchableHalfmetallicity2024, wuSlidingFerroelectricity2D2021a, xiangTwodimensionalRoomTemperature2020, xuTwodimensionalFerroelasticityVan2021, xunCoexistingMagnetismFerroelectric2024, yangRipplingFerroicPhase2021, yuFerroelectricControlMagnetism2026, zahraCriticalAnalysisFerroelectric2025, zhangEmergingFrontiersTwodimensional2025, zhangNonvolatileControlTopological2025, zhaoOpticalFingerprintsTwodimensional2024, zhaoRealization2DMultiferroic2024, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08
---

# 多铁性 / Multiferroicity

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


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
- [[../papers/Chen2016electrical]]：从实验研究角度梳理了「Electrical and mechanical switching of ferroelectric polarization in the 70 nm BiFeO3 film」。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：从综述角度梳理了「Ferroelectricity and multiferroicity down to the atomic thickness」。
- [[../papers/Goswami2011multiferroic]]：从实验研究角度梳理了「Multiferroic coupling in nanoscale BiFeO3」。
- [[../papers/Jin2015studying]]：从实验研究角度梳理了「Studying the Polarization Switching in Polycrystalline BiFeO3 Films by 2D Piezoresponse Force Microscopy」。
- [[../papers/Kim2008effect]]：从实验研究角度梳理了「Effect of epitaxial strain on ferroelectric polarization in multiferroic BiFeO3 films」。
- [[../papers/Perugu2024morphology]]：从实验研究角度梳理了「Synthesis, Structural, Morphology and Magnetic Properties: Effect of La on Multiferroic Nature of BiFeO3 Nanoparticles」。
- [[../papers/RecentAdvancesGrowth2025]]：从综述角度梳理了「二维多铁性材料的生长、表征及应用研究进展」。
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]：从理论分析角度梳理了「二维金属氮氧化物中的铁电性与p轨道铁磁性和金属丰度共存」。
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]：从实验研究角度梳理了「Atomic-Scale Visualization of Multiferroicity in Monolayer NiI2」。
- [[../papers/bhowalPolarMetalsPrinciples2023b]]：从综述角度梳理了「极性金属：原理与展望」。
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：从实验研究角度梳理了「二维多铁异质结构中的铁电驱动应变介导磁电耦合」。
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：从综述角度梳理了「Hafnium-Based Ferroelectric Post-Moore Electronics: Device Physics, Integration Architectures, and Neuromorphic System Implementation」。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：从理论分析角度梳理了「Strong Sliding Ferroelectricity and Interlayer Sliding Controllable Spintronic Effect in Two-Dimensional HgI₂ Layers」。
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：从理论分析角度梳理了「多铁性：铁电的磁扭曲」。
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]：从实验研究角度梳理了「Intercorrelated In-Plane and Out-of-Plane Ferroelectricity in Ultrathin Two-Dimensional Layered Semiconductor In2Se3」。
- [[../papers/deSousa2008electrical]]：从理论分析角度梳理了「Electrical control of magnon propagation in multiferroic BiFeO3 films」。
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]：从实验研究角度梳理了「Ferroelectric switching of a two-dimensional metal」。
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]：从理论分析角度梳理了「二维 Sc₂P₂Se₆ 与 ScCrP₂Se₆ 单层的铁电性与多铁性」。
- [[../papers/fiebigEvolutionMultiferroics2016]]：从综述角度梳理了「多铁性的演化」。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：从实验研究角度梳理了「范德瓦尔斯多铁材料中的巨手征磁电振荡」。
- [[../papers/gaoStrainEngineeringFerroelectric2024]]：从理论分析角度梳理了「Strain engineering of ferroelectric polarization and domain in the two-dimensional multiferroic semiconductor」。
- [[../papers/gomez-ortizKittelLawDomain2023]]：从理论分析角度梳理了「Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices」。
- [[../papers/guanRecentProgressTwoDimensional2020]]：从综述角度梳理了「Recent Progress in Two‐Dimensional Ferroelectric Materials」。
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]：从综述角度梳理了「二维铁电材料的研究进展」。
- [[../papers/hanPolarTopologicalMaterials2025]]：从综述角度梳理了「Polar topological materials and devices: Prospects and challenges」。
- [[../papers/hanTunableSlidingFerroelectricity2025]]：从理论分析角度梳理了「Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers」。
- [[../papers/hillWhyAreThere2000a]]：从理论分析角度梳理了「为什么磁性铁电体这么少？」。
- [[../papers/huProgressProspectsLowdimensional2019]]：从综述角度梳理了「低维多铁性材料的研究进展与展望」。
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]：从综述角度梳理了「Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage」。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：从综述角度梳理了「Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials」。
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]：从实验研究角度梳理了「范德华 CuCrP₂S₆ 中的二维铁磁性和驱动铁电性」。
- [[../papers/liFerroelasticityDomainPhysics2016]]：从理论分析角度梳理了「二维过渡金属二硫族化物单层的铁弹性和畴物理」。
- [[../papers/liMonolayerPuckeredPentagonal2022]]：从理论分析角度梳理了「单层折叠五边形VTe2:一种具有多铁性耦合的二维铁磁半导体」。
- [[../papers/liPhaseTransitions2D2021]]：从综述角度梳理了「Phase transitions in 2D materials」。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：从综述角度梳理了「铁电薄膜材料及其应用」。
- [[../papers/miaoMagneticFerroelectricMetal2024]]：从理论分析角度梳理了「Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding」。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：从综述角度梳理了「多铁性：磁电耦合的不同途径」。
- [[../papers/neumayerCompetingPolarPhases2025]]：从综述角度梳理了「二维铁电过渡金属硫代和硒酸盐中的竞争极性相」。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：从实验研究角度梳理了「一种室温铁电半金属」。
- [[../papers/songEvidenceSinglelayerVan2022]]：从实验研究角度梳理了「Evidence for a single-layer van der Waals multiferroic」。
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：从综述角度梳理了「磁电多铁性材料研究进展」。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：从综述角度梳理了「Sliding ferroelectricity in two-dimensional materials and device applications」。
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]]：从实验研究角度梳理了「自由基二维碳化铌的铁电性和非易失性忆阻应用：自由基MXene在电子器件中的新前沿」。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：从综述角度梳理了「二维范德华材料的多铁性：挑战与机遇」。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：从实验研究角度梳理了「具有电压可控磁序的室温二维多铁金属」。
- [[../papers/wangTunableD0Topological2025b]]：从理论分析角度梳理了「Tunable d0 topological magnetic states in multiferroic monolayer In2NO2」。
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]：从理论分析角度梳理了「Two-dimensional ferroelectric metal CuCrX2 (X = S, Se) for efficient electrocatalysis」。
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]：从实验研究角度梳理了「Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic」。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：从实验研究角度梳理了「MXene Hf₂MnC₂O₂/Sc₂CO₂ 多铁异质结中的非易失可开关半金属性与磁性」。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：从综述角度梳理了「二维范德华材料中的滑动铁电性：相关物理和未来机遇」。
- [[../papers/xiangTwodimensionalRoomTemperature2020]]：从综述角度梳理了「Towards two-dimensional room temperature multiferroics」。
- [[../papers/xuTwodimensionalFerroelasticityVan2021]]：从实验研究角度梳理了「Two-dimensional ferroelasticity in van der Waals β'-In2Se3」。
- [[../papers/xunCoexistingMagnetismFerroelectric2024]]：从理论分析角度梳理了「Coexisting Magnetism, Ferroelectric, and Ferrovalley Multiferroic in Stacking-Dependent Two-Dimensional Materials」。
- [[../papers/yangRipplingFerroicPhase2021]]：从理论分析角度梳理了「Rippling Ferroic Phase Transition and Domain Switching In 2D Materials」。
- [[../papers/yuFerroelectricControlMagnetism2026]]：从实验研究角度梳理了「强磁电耦合二维多铁性材料中嵌入诱导对称破缺对磁性和巨磁电阻的铁电控制」。
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]：从综述角度梳理了「二维MXene铁电和铁磁性质的临界分析」。
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]：从综述角度梳理了「二维滑动铁电体的新前沿」。
- [[../papers/zhangNonvolatileControlTopological2025]]：从理论分析角度梳理了「Nonvolatile control of topological magnetism in two-dimensional CrInTe2/In2Se3 multiferroic heterostructures」。
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]
- [[../papers/zhaoRealization2DMultiferroic2024]]
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/magnetoelectric-coupling|磁电耦合]]（核心功能）
- [[../concepts/geometric-ferroelectricity|几何铁电性]]（绕开机制）
- [[../entities/BiFeO3|BiFeO₃]]（室温多铁明星材料）
- [[../entities/HoMnO3|HoMnO₃]]（几何多铁代表）
