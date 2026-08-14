---
tags: [concept, ferroelectricity, polarization]
title: 极化翻转 / Polarization Switching
type: concept
status: mature
domain: [ferroelectricity, dielectric-physics]
mechanism: 外加电场驱动下，铁电自发极化偶极子克服势垒重定向的过程
related_concepts: [ferroelectricity, sliding-ferroelectricity, domain-wall-motion, depolarization-field]
papers: [huangTwodimensionalIn2Se3Rising2022, heUltrafastSwitchingDynamics2024, zhangEmergingFrontiersTwodimensional2025, Chen2016electrical, FerroelectricityMultiferroicityAtomic2023, Jin2015studying, Kim2008effect, RecentAdvancesGrowth2025, aiFerroelectricityCoexistedPorbital2022, bhowalPolarMetalsPrinciples2023b, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenHafniumBasedFerroelectricPostMoore2026, chenStrongSlidingFerroelectricity2024, cheongMultiferroicsMagneticTwist2007a, cuiIntercorrelatedInplaneOutofplane2018a, deSousa2008electrical, dingPredictionIntrinsicTwodimensional2017a, feiFerroelectricSwitchingTwodimensional2018a, fengFerroelectricityMultiferroicityTwodimensional2020, fiebigEvolutionMultiferroics2016, gaoStrainEngineeringFerroelectric2024, gomez-ortizKittelLawDomain2023, gongAbsenceCriticalThickness2023, guanRecentProgressTwoDimensional2020, guoAdvancesTwodimensionalFerroelectric2025, hanPolarTopologicalMaterials2025, hanTunableSlidingFerroelectricity2025, heSwitchingTwodimensionalSliding2025, houStrainbasedRoomtemperatureNonvolatile2019, huProgressProspectsLowdimensional2019, huangPolarPhaseDomain2019, junqueraCriticalThicknessFerroelectricity2003, kaurRecentAdvancesTheoretical2025a, king-smithTheoryPolarizationCrystalline1993, laiTwodimensionalFerromagnetismDriven2019, liPhaseTransitions2D2021, martinThinfilmFerroelectricMaterials2016, miaoMagneticFerroelectricMetal2024, mostovoyMultiferroicsDifferentRoutes2024, neumayerCompetingPolarPhases2025, rameshMultiferroicsProgressProspects2007, sharmaRoomtemperatureFerroelectricSemimetal2019, shenEmergenceMultipleFerroelectric2025, spaldinRenaissanceMagnetoelectricMultiferroics2005, sunSlidingFerroelectricityTwodimensional2025, tahirFerroelectricityNonvolatileMemristor2025, tangCombiningIntrinsicSlidinginduced2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, wangTunableD0Topological2025b, wangTwodimensionalFerroelectricMetal2025, wuCoexistenceFerroelectricityAntiferroelectricity2024, wuNonvolatileSwitchableHalfmetallicity2024, wuSlidingFerroelectricity2D2021a, xiangTwodimensionalRoomTemperature2020, xuTunableFerroelectricTopological2022, xuTwodimensionalFerroelasticityVan2021, xueEmergingNonvolatileMemories2011, yangRipplingFerroicPhase2021, yuFerroelectricControlMagnetism2026, zahraCriticalAnalysisFerroelectric2025, zhangNonvolatileControlTopological2025, zhaoRealization2DMultiferroic2024, zhaoOpticalFingerprintsTwodimensional2024]
updated: 2026-08
---

# 极化翻转 / Polarization Switching

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
- [[../papers/Chen2016electrical]]
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]
- [[../papers/Jin2015studying]]
- [[../papers/Kim2008effect]]
- [[../papers/RecentAdvancesGrowth2025]]
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]
- [[../papers/bhowalPolarMetalsPrinciples2023b]]
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]
- [[../papers/chenStrongSlidingFerroelectricity2024]]
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]
- [[../papers/deSousa2008electrical]]
- [[../papers/dingPredictionIntrinsicTwodimensional2017a]]
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]
- [[../papers/fiebigEvolutionMultiferroics2016]]
- [[../papers/gaoStrainEngineeringFerroelectric2024]]
- [[../papers/gomez-ortizKittelLawDomain2023]]
- [[../papers/gongAbsenceCriticalThickness2023]]
- [[../papers/guanRecentProgressTwoDimensional2020]]
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]
- [[../papers/hanPolarTopologicalMaterials2025]]
- [[../papers/hanTunableSlidingFerroelectricity2025]]
- [[../papers/heSwitchingTwodimensionalSliding2025]]
- [[../papers/houStrainbasedRoomtemperatureNonvolatile2019]]
- [[../papers/huProgressProspectsLowdimensional2019]]
- [[../papers/huangPolarPhaseDomain2019]]
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]
- [[../papers/kaurRecentAdvancesTheoretical2025a]]
- [[../papers/king-smithTheoryPolarizationCrystalline1993]]
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]
- [[../papers/liPhaseTransitions2D2021]]
- [[../papers/martinThinfilmFerroelectricMaterials2016]]
- [[../papers/miaoMagneticFerroelectricMetal2024]]
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]
- [[../papers/neumayerCompetingPolarPhases2025]]
- [[../papers/rameshMultiferroicsProgressProspects2007]]
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]
- [[../papers/shenEmergenceMultipleFerroelectric2025]]
- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]]
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]]
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]
- [[../papers/wangTunableD0Topological2025b]]
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]
- [[../papers/wuSlidingFerroelectricity2D2021a]]
- [[../papers/xiangTwodimensionalRoomTemperature2020]]
- [[../papers/xuTunableFerroelectricTopological2022]]
- [[../papers/xuTwodimensionalFerroelasticityVan2021]]
- [[../papers/xueEmergingNonvolatileMemories2011]]
- [[../papers/yangRipplingFerroicPhase2021]]
- [[../papers/yuFerroelectricControlMagnetism2026]]
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]
- [[../papers/zhangNonvolatileControlTopological2025]]
- [[../papers/zhaoRealization2DMultiferroic2024]]
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]（横向滑移翻转）
- [[../concepts/domain-wall-motion|畴壁运动]]（翻转主要途径）
- [[../concepts/depolarization-field|退极化场]]（阻碍翻转的长程力）
- [[../entities/In2Se3|In₂Se₃]]（典型翻转材料）
