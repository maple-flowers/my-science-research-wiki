---
tags: [concept, ferroelectricity, polarization]
title: 极化翻转 / Polarization Switching
type: concept
status: developing
domain: [ferroelectricity, dielectric-physics]
mechanism: 外加电场驱动下，铁电自发极化偶极子克服势垒重定向的过程
related_concepts: [ferroelectricity, sliding-ferroelectricity, domain-wall-motion, depolarization-field]
papers: [huangTwodimensionalIn2Se3Rising2022, heUltrafastSwitchingDynamics2024, zhangEmergingFrontiersTwodimensional2025, Chen2016electrical, FerroelectricityMultiferroicityAtomic2023, Jin2015studying, Kim2008effect, RecentAdvancesGrowth2025, aiFerroelectricityCoexistedPorbital2022, bhowalPolarMetalsPrinciples2023b, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenHafniumBasedFerroelectricPostMoore2026, chenStrongSlidingFerroelectricity2024, cheongMultiferroicsMagneticTwist2007a, cuiIntercorrelatedInplaneOutofplane2018a, deSousa2008electrical, dingPredictionIntrinsicTwodimensional2017a, feiFerroelectricSwitchingTwodimensional2018a, fengFerroelectricityMultiferroicityTwodimensional2020, fiebigEvolutionMultiferroics2016, gaoStrainEngineeringFerroelectric2024, gomez-ortizKittelLawDomain2023, gongAbsenceCriticalThickness2023, guanRecentProgressTwoDimensional2020, guoAdvancesTwodimensionalFerroelectric2025, hanPolarTopologicalMaterials2025, hanTunableSlidingFerroelectricity2025, heSwitchingTwodimensionalSliding2025, houStrainbasedRoomtemperatureNonvolatile2019, huProgressProspectsLowdimensional2019, huangPolarPhaseDomain2019, junqueraCriticalThicknessFerroelectricity2003, kaurRecentAdvancesTheoretical2025a, king-smithTheoryPolarizationCrystalline1993, laiTwodimensionalFerromagnetismDriven2019, liPhaseTransitions2D2021, martinThinfilmFerroelectricMaterials2016, miaoMagneticFerroelectricMetal2024, mostovoyMultiferroicsDifferentRoutes2024, neumayerCompetingPolarPhases2025, rameshMultiferroicsProgressProspects2007, sharmaRoomtemperatureFerroelectricSemimetal2019, shenEmergenceMultipleFerroelectric2025, spaldinRenaissanceMagnetoelectricMultiferroics2005, sunSlidingFerroelectricityTwodimensional2025, tahirFerroelectricityNonvolatileMemristor2025, tangCombiningIntrinsicSlidinginduced2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, wangTunableD0Topological2025b, wangTwodimensionalFerroelectricMetal2025, wuCoexistenceFerroelectricityAntiferroelectricity2024, wuNonvolatileSwitchableHalfmetallicity2024, wuSlidingFerroelectricity2D2021a, xiangTwodimensionalRoomTemperature2020, xuTunableFerroelectricTopological2022, xuTwodimensionalFerroelasticityVan2021, xueEmergingNonvolatileMemories2011, yangRipplingFerroicPhase2021, yuFerroelectricControlMagnetism2026, zahraCriticalAnalysisFerroelectric2025, zhangNonvolatileControlTopological2025, zhaoRealization2DMultiferroic2024, zhaoOpticalFingerprintsTwodimensional2024]
updated: 2026-08
---

# 极化翻转 / Polarization Switching

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


极化翻转 (Polarization Switching) 是铁电材料在外加足够大电场（矫顽电场）作用下，其内部自发极化方向发生可逆改变的物理过程。它是铁电体在非易失性数据存储、压电换能及多态逻辑器件中应用的基础。

## 👵 太奶导读

孩子，这个“极化翻转”其实就像是阅兵式上的队伍转方向。
在铁电材料内部，住着一排排排得整整齐齐的“小箭头”（电偶极子），它们可能全都指着上方（这就是极化向上）。
当你在外面接上电，施加一个反向电场时，这电场就像是教官喊了一声“齐步掉头！”
于是，这些小箭头就会刷地一下全掉过头来，指着下方了（这就是极化翻转）。
传统的翻转是让原子在格子里上下跳，而最新的“滑移翻转”则像是指尖搓两层纸，只要轻轻一滑，这小箭头就掉过头去了，既省力又好用。

## 🏗️ 结构概览：协同翻转路径

在二维铁电材料（如 α-In₂Se₃）中，极化翻转表现出高度的层间协同性。

![图：α-In₂Se₃ 的极化翻转势垒与路径（单步 vs 三步协同）](../../raw/figures/huangTwodimensionalIn2Se3Rising2022/fig_8_EC7NT7IT.png)
*   **看图要点**：图中对比了两种翻转路径。直接单步跳跃的势垒极高（~0.85 eV/u.c.），而通过上三层集体滑动、经过 β' 中间相、再让 Se(m) 旋转的三步协同路径，其势垒仅为 0.066 eV/u.c.。这在理论上解释了该材料能实现超快翻转的原因。
*   **来源**：[[../papers/huangTwodimensionalIn2Se3Rising2022]] -> [[../figures/mathematical-models|数学模型与物理公式]]

## 🧩 机制：畴壁运动与滑移

在宏观上，极化翻转很少通过整畴直接均匀跳跃完成，而是通过畴壁运动 (Domain Wall Motion) 实现。

![图：h-BN 双层中 0° 与 90° 铁电畴壁运动过程](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_6_IH4EUPKK.png)
*   **关键特征**：在剪切力/电场作用下，不同极化的畴壁（如 AB 畴与 BA 畴的边界）发生移动。畴壁运动所需的临界驱动电场比单畴直接翻转低两个数量级，这揭示了低矫顽场的物理起源，并展示了皮秒量级的超快开关动力学。
*   **来源**：[[../papers/heUltrafastSwitchingDynamics2024]] -> [[../figures/domain-walls-structures|畴结构与畴壁]]

## 📚 相关论文 (Related Papers)

- [[../papers/huangTwodimensionalIn2Se3Rising2022]]：研究了 α-In₂Se₃ 中“再成键”和“偶极锁定”主导的翻转机制。
- [[../papers/heUltrafastSwitchingDynamics2024]]：利用机器学习势大尺度模拟了滑移铁电中畴壁运动的超快动力学。
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]：综述了滑动铁电体系中多样化的层间翻转行为和多态存储潜力。
- [[../papers/Chen2016electrical]]：从实验研究角度梳理了「Electrical and mechanical switching of ferroelectric polarization in the 70 nm BiFeO3 film」。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：从综述角度梳理了「Ferroelectricity and multiferroicity down to the atomic thickness」。
- [[../papers/Jin2015studying]]：从实验研究角度梳理了「Studying the Polarization Switching in Polycrystalline BiFeO3 Films by 2D Piezoresponse Force Microscopy」。
- [[../papers/Kim2008effect]]：从实验研究角度梳理了「Effect of epitaxial strain on ferroelectric polarization in multiferroic BiFeO3 films」。
- [[../papers/RecentAdvancesGrowth2025]]：从综述角度梳理了「二维多铁性材料的生长、表征及应用研究进展」。
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]：从理论分析角度梳理了「二维金属氮氧化物中的铁电性与p轨道铁磁性和金属丰度共存」。
- [[../papers/bhowalPolarMetalsPrinciples2023b]]：从综述角度梳理了「极性金属：原理与展望」。
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：从实验研究角度梳理了「二维多铁异质结构中的铁电驱动应变介导磁电耦合」。
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：从综述角度梳理了「Hafnium-Based Ferroelectric Post-Moore Electronics: Device Physics, Integration Architectures, and Neuromorphic System Implementation」。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：从理论分析角度梳理了「Strong Sliding Ferroelectricity and Interlayer Sliding Controllable Spintronic Effect in Two-Dimensional HgI₂ Layers」。
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：从理论分析角度梳理了「多铁性：铁电的磁扭曲」。
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]：从实验研究角度梳理了「Intercorrelated In-Plane and Out-of-Plane Ferroelectricity in Ultrathin Two-Dimensional Layered Semiconductor In2Se3」。
- [[../papers/deSousa2008electrical]]：从理论分析角度梳理了「Electrical control of magnon propagation in multiferroic BiFeO3 films」。
- [[../papers/dingPredictionIntrinsicTwodimensional2017a]]：从理论分析角度梳理了「Prediction of intrinsic two-dimensional ferroelectrics in In2Se3 and other III2-VI3 van der Waals materials」。
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]：从实验研究角度梳理了「Ferroelectric switching of a two-dimensional metal」。
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]：从理论分析角度梳理了「二维 Sc₂P₂Se₆ 与 ScCrP₂Se₆ 单层的铁电性与多铁性」。
- [[../papers/fiebigEvolutionMultiferroics2016]]：从综述角度梳理了「多铁性的演化」。
- [[../papers/gaoStrainEngineeringFerroelectric2024]]：从理论分析角度梳理了「Strain engineering of ferroelectric polarization and domain in the two-dimensional multiferroic semiconductor」。
- [[../papers/gomez-ortizKittelLawDomain2023]]：从理论分析角度梳理了「Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices」。
- [[../papers/gongAbsenceCriticalThickness2023]]：从实验研究角度梳理了「违反Kittel定律的极地Skyrmion临界厚度的缺失」。
- [[../papers/guanRecentProgressTwoDimensional2020]]：从综述角度梳理了「Recent Progress in Two‐Dimensional Ferroelectric Materials」。
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]：从综述角度梳理了「二维铁电材料的研究进展」。
- [[../papers/hanPolarTopologicalMaterials2025]]：从综述角度梳理了「Polar topological materials and devices: Prospects and challenges」。
- [[../papers/hanTunableSlidingFerroelectricity2025]]：从理论分析角度梳理了「Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers」。
- [[../papers/heSwitchingTwodimensionalSliding2025]]：从理论分析角度梳理了「机械弯曲切换二维滑动铁电体」。
- [[../papers/houStrainbasedRoomtemperatureNonvolatile2019]]：从实验研究角度梳理了「应变型室温非挥发MoTe2铁电相变晶体管」。
- [[../papers/huProgressProspectsLowdimensional2019]]：从综述角度梳理了「低维多铁性材料的研究进展与展望」。
- [[../papers/huangPolarPhaseDomain2019]]：从实验研究角度梳理了「Polar and phase domain walls with conducting interfacial states in a Weyl semimetal MoTe2」。
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]：从理论分析角度梳理了「Critical thickness for ferroelectricity in perovskite ultrathin films」。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：从综述角度梳理了「Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials」。
- [[../papers/king-smithTheoryPolarizationCrystalline1993]]：从理论分析角度梳理了「Theory of polarization of crystalline solids」。
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]：从实验研究角度梳理了「范德华 CuCrP₂S₆ 中的二维铁磁性和驱动铁电性」。
- [[../papers/liPhaseTransitions2D2021]]：从综述角度梳理了「Phase transitions in 2D materials」。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：从综述角度梳理了「铁电薄膜材料及其应用」。
- [[../papers/miaoMagneticFerroelectricMetal2024]]：从理论分析角度梳理了「Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding」。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：从综述角度梳理了「多铁性：磁电耦合的不同途径」。
- [[../papers/neumayerCompetingPolarPhases2025]]：从综述角度梳理了「二维铁电过渡金属硫代和硒酸盐中的竞争极性相」。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：从综述角度梳理了「多铁性：薄膜研究进展与展望」。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：从实验研究角度梳理了「一种室温铁电半金属」。
- [[../papers/shenEmergenceMultipleFerroelectric2025]]：从实验研究角度梳理了「多层黑磷中多铁电态的出现」。
- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]：从综述角度梳理了「磁电多铁性的复兴」。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：从综述角度梳理了「Sliding ferroelectricity in two-dimensional materials and device applications」。
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]]：从实验研究角度梳理了「自由基二维碳化铌的铁电性和非易失性忆阻应用：自由基MXene在电子器件中的新前沿」。
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]]：从理论分析角度梳理了「Combining intrinsic and sliding-induced polarizations for multistates in two-dimensional ferroelectrics」。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：从综述角度梳理了「二维范德华材料的多铁性：挑战与机遇」。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：从实验研究角度梳理了「具有电压可控磁序的室温二维多铁金属」。
- [[../papers/wangTunableD0Topological2025b]]：从理论分析角度梳理了「Tunable d0 topological magnetic states in multiferroic monolayer In2NO2」。
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]：从理论分析角度梳理了「Two-dimensional ferroelectric metal CuCrX2 (X = S, Se) for efficient electrocatalysis」。
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]：从实验研究角度梳理了「Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic」。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：从实验研究角度梳理了「MXene Hf₂MnC₂O₂/Sc₂CO₂ 多铁异质结中的非易失可开关半金属性与磁性」。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：从综述角度梳理了「二维范德华材料中的滑动铁电性：相关物理和未来机遇」。
- [[../papers/xiangTwodimensionalRoomTemperature2020]]：从综述角度梳理了「Towards two-dimensional room temperature multiferroics」。
- [[../papers/xuTunableFerroelectricTopological2022]]：从理论分析角度梳理了「Tunable ferroelectric topological defects on 2D topological surfaces: strain engineering skyrmion-like polar structures in 2D materials」。
- [[../papers/xuTwodimensionalFerroelasticityVan2021]]：从实验研究角度梳理了「Two-dimensional ferroelasticity in van der Waals β'-In2Se3」。
- [[../papers/xueEmergingNonvolatileMemories2011]]：从综述角度梳理了「新兴非易失性存储器」。
- [[../papers/yangRipplingFerroicPhase2021]]：从理论分析角度梳理了「Rippling Ferroic Phase Transition and Domain Switching In 2D Materials」。
- [[../papers/yuFerroelectricControlMagnetism2026]]：从实验研究角度梳理了「强磁电耦合二维多铁性材料中嵌入诱导对称破缺对磁性和巨磁电阻的铁电控制」。
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]：从综述角度梳理了「二维MXene铁电和铁磁性质的临界分析」。
- [[../papers/zhangNonvolatileControlTopological2025]]
- [[../papers/zhaoRealization2DMultiferroic2024]]
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]（横向滑移翻转）
- [[../concepts/domain-wall-motion|畴壁运动]]（翻转主要途径）
- [[../concepts/depolarization-field|退极化场]]（阻碍翻转的长程力）
- [[../entities/In2Se3|In₂Se₃]]（典型翻转材料）
