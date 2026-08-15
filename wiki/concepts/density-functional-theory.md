---
tags: [concept, dft, methodology]
title: 密度泛函理论 / Density Functional Theory (DFT)
type: concept
status: developing
domain: [computational-chemistry, condensed-matter-physics]
mechanism: 基于 Hohenberg-Kohn 定理，将多电子体系的基态性质映射为电子密度的泛函，从而将 3N 维薛定谔方程简化为 3 维电子密度求解
related_concepts: [kohn-sham-equations, exchange-correlation-functional, paw-method, pseudopotential, tight-binding]
papers: [blochlProjectorAugmentedwaveMethod1994b, perdewGeneralizedGradientApproximation1996a, kresseEfficientIterativeSchemes1996d, Barnett2006coexistence, Delley2000, Jin2015studying, Johannes2008fermi, Koley2020charge, Li2013bonding, Mińkowski2021cation, Wei2021, Wu2018, Wu2021, Xie2024isostructural, Zhang2019a, aiFerroelectricityCoexistedPorbital2022, aminiAtomicscaleVisualizationMultiferroicity2024, bhowalPolarMetalsPrinciples2023b, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chen3dLevelSymmetry2025, chenFerromagneticNonmagnetic1T2022, chenHafniumBasedFerroelectricPostMoore2026, chowdhuryReviewTheoreticalComputational, cossuStackingChargedensityWaves2024, dingPredictionIntrinsicTwodimensional2017a, duUltrasensitiveOptoelectronicBiosensor2025, dudarevElectronenergylossSpectraStructural1998a, fengFerroelectricityMultiferroicityTwodimensional2020, gajdosLinearOpticalProperties2006, gaoGiantChiralMagnetoelectric2024a, gaoStrainEngineeringFerroelectric2024, gongAbsenceCriticalThickness2023, guoAdvancesTwodimensionalFerroelectric2025, hallEnvironmentalControlCharge, hanTunableSlidingFerroelectricity2025, heUltrafastSwitchingDynamics2024, henkelmanClimbingImageNudged2000c, hillWhyAreThere2000a, huProgressProspectsLowdimensional2019, huangPolarPhaseDomain2019, junqueraCriticalThicknessFerroelectricity2003, kaurRecentAdvancesTheoretical2025a, khazaeiNovelElectronicMagnetic2013, king-smithTheoryPolarizationCrystalline1993, kresseEfficiencyAbinitioTotal1996a, kresseInitiomolecularDynamicsLiquid1993, kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994, kresseUltrasoftPseudopotentialsProjector1999c, krishnamurthiSpinChargeDensity2020, laiTwodimensionalFerromagnetismDriven2019, lezoualchStudyChargeDensity, liFerroelasticityDomainPhysics2016, liMonolayerPuckeredPentagonal2022, liPhaseTransitions2D2021, martinThinfilmFerroelectricMaterials2016, miaoMagneticFerroelectricMetal2024, monkhorstSpecialPointsBrillouinzone1976, naguib25thAnniversaryArticle2013a, neumayerCompetingPolarPhases2025, nicholsonUniaxialStraininducedPhase2021, pedramraziManipulatingTopologicalDomain2019, pengStrainEngineering2D2020, rameshMultiferroicsProgressProspects2007, sharmaRoomtemperatureFerroelectricSemimetal2019, shenEmergenceMultipleFerroelectric2025, shishkinImplementationPerformanceFrequencydependentGWmethod2006, shuTwoDimensionalBlackArsenic2020, spaldinAdvancesMagnetoelectricMultiferroics2019, sunSlidingFerroelectricityTwodimensional2025, tangGridbasedBaderAnalysis2009, tianRoomtemperatureTwodimensionalMultiferroic2026, wangTunableD0Topological2025b, wangTwodimensionalFerroelectricMetal2025, wernetSpectroscopicCharacterizationMicroscopic2005, wongEvidenceMetallic1T, wuNonvolatileSwitchableHalfmetallicity2024, wuSlidingFerroelectricity2D2021a, xuTunableFerroelectricTopological2022, yanDecipheringStabilityTwodimensional2025, yanagizawaSwitchingChargedensityWave2023, yangRipplingFerroicPhase2021, yuFerroelectricControlMagnetism2026, zahraCriticalAnalysisFerroelectric2025, zhaoRealization2DMultiferroic2024, zhengAnisotropicSuperconductivityTwodimensional2025, zhongHighthroughputExfoliationMultiferroic2025, zhouFirstprinciplesPredictionRedox2004]
updated: 2026-08
---

# 密度泛函理论 / Density Functional Theory (DFT)

密度泛函理论（Density Functional Theory, DFT）是现代量子力学中处理多粒子体系（特别是电子系统）最成功且应用最广的理论框架。其核心思想是：一个体系的所有基态物理性质（如总能量、磁矩、几何结构等）都由其三维**电子密度 $\rho(\mathbf{r})$** 唯一决定，而不必去求解极其复杂的 $3N$ 维多体波函数。

## 👵 太奶导读

太奶，这“密度泛函理论”其实是在教我们怎么**偷懒算大账**。
您想啊，材料里有成千上万个电子（这就是那个多体问题）。如果您想数清楚每个电子在哪儿、干什么，那这辈子都算不完。
这时候，两位聪明人（Hohenberg 和 Kohn）说：其实咱们不用管每个电子具体在哪儿！咱们只要盯着材料里那一团**电子云的厚薄分布**（这就是电子密度）就行了。
这就像是一个高明的厨子，他不用数锅里有多少粒米，只要看锅里粥的稠稀程度（密度），就能断定这锅粥熟透没熟透、好不好吃。
这就是 DFT 的本事——把一个数不清的麻烦账，变成了一道看“云图”就能解的数学题。现在咱们模拟新材料、设计新电池，全靠这个厨子的“粥论”！

## 🏗️ 核心公理：Hohenberg-Kohn 定理

1.  **第一定理**：体系的基态能量 $E$ 是电子密度 $\rho(\mathbf{r})$ 的唯一泛函。也就是说，知道了密度分布，我们就知道了这个体系的所有秘密。
2.  **第二定理**：对于正确的基态密度，泛函能量 $E[\rho]$ 达到全局最小值。这为寻找基态密度提供了变分法判据。

为了实现数值求解，Walter Kohn 和沈吕九（Sham）提出了 **Kohn-Sham 方程**。他们将相互作用的多电子体系等效为一个无相互作用的虚拟电子系统。在这种描述下，所有复杂的量子力学相互作用（交换与关联）都被打包塞进了一个叫作**交换关联泛函（Exchange-Correlation functional）**的“黑盒子”里。

## 🧩 计算层次与近似

由于“黑盒子”（交换关联泛函）的精确解析形式尚不可知，DFT 的精度高度依赖于所选的近似级别：

*   **LDA (局域密度近似)**：假设某点处的交换关联能仅取决于该点的局域电子密度，像是一层平铺的草坪。
*   **GGA (广义梯度近似)**：不仅考虑局域密度，还考虑了密度的坡度（梯度），像是有起伏的丘陵（代表作：[[../papers/perdewGeneralizedGradientApproximation1996a|PBE]]）。
*   **Hybrid (杂化泛函)**：掺入了一定比例的 Hartree-Fock 精确交换能，精度更高但计算更慢（代表作：B3LYP, HSE06）。

## 📚 相关论文 (Related Papers)

- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：探讨了 DFT 在全电子精度重构中的应用。
- [[../papers/perdewGeneralizedGradientApproximation1996a]]：提出了最经典的 GGA 泛函 PBE。
- [[../papers/kresseEfficientIterativeSchemes1996d]]：奠定了 DFT 大规模高效迭代求解的算法基础。
- [[../papers/Barnett2006coexistence]]
- [[../papers/Delley2000]]
- [[../papers/Jin2015studying]]
- [[../papers/Johannes2008fermi]]
- [[../papers/Koley2020charge]]
- [[../papers/Li2013bonding]]
- [[../papers/Mińkowski2021cation]]
- [[../papers/Wei2021]]
- [[../papers/Wu2018]]
- [[../papers/Wu2021]]
- [[../papers/Xie2024isostructural]]
- [[../papers/Zhang2019a]]
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]
- [[../papers/bhowalPolarMetalsPrinciples2023b]]
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]
- [[../papers/chen3dLevelSymmetry2025]]
- [[../papers/chenFerromagneticNonmagnetic1T2022]]
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]
- [[../papers/chowdhuryReviewTheoreticalComputational]]
- [[../papers/cossuStackingChargedensityWaves2024]]
- [[../papers/dingPredictionIntrinsicTwodimensional2017a]]
- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]
- [[../papers/dudarevElectronenergylossSpectraStructural1998a]]
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]
- [[../papers/gajdosLinearOpticalProperties2006]]
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]
- [[../papers/gaoStrainEngineeringFerroelectric2024]]
- [[../papers/gongAbsenceCriticalThickness2023]]
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]
- [[../papers/hallEnvironmentalControlCharge]]
- [[../papers/hanTunableSlidingFerroelectricity2025]]
- [[../papers/heUltrafastSwitchingDynamics2024]]
- [[../papers/henkelmanClimbingImageNudged2000c]]
- [[../papers/hillWhyAreThere2000a]]
- [[../papers/huProgressProspectsLowdimensional2019]]
- [[../papers/huangPolarPhaseDomain2019]]
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]
- [[../papers/kaurRecentAdvancesTheoretical2025a]]
- [[../papers/khazaeiNovelElectronicMagnetic2013]]
- [[../papers/king-smithTheoryPolarizationCrystalline1993]]
- [[../papers/kresseEfficiencyAbinitioTotal1996a]]
- [[../papers/kresseInitiomolecularDynamicsLiquid1993]]
- [[../papers/kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994]]
- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]
- [[../papers/krishnamurthiSpinChargeDensity2020]]
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]
- [[../papers/lezoualchStudyChargeDensity]]
- [[../papers/liFerroelasticityDomainPhysics2016]]
- [[../papers/liMonolayerPuckeredPentagonal2022]]
- [[../papers/liPhaseTransitions2D2021]]
- [[../papers/martinThinfilmFerroelectricMaterials2016]]
- [[../papers/miaoMagneticFerroelectricMetal2024]]
- [[../papers/monkhorstSpecialPointsBrillouinzone1976]]
- [[../papers/naguib25thAnniversaryArticle2013a]]
- [[../papers/neumayerCompetingPolarPhases2025]]
- [[../papers/nicholsonUniaxialStraininducedPhase2021]]
- [[../papers/pedramraziManipulatingTopologicalDomain2019]]
- [[../papers/pengStrainEngineering2D2020]]
- [[../papers/rameshMultiferroicsProgressProspects2007]]
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]
- [[../papers/shenEmergenceMultipleFerroelectric2025]]
- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]]
- [[../papers/shuTwoDimensionalBlackArsenic2020]]
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]
- [[../papers/tangGridbasedBaderAnalysis2009]]
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]
- [[../papers/wangTunableD0Topological2025b]]
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]
- [[../papers/wernetSpectroscopicCharacterizationMicroscopic2005]]
- [[../papers/wongEvidenceMetallic1T]]
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]
- [[../papers/wuSlidingFerroelectricity2D2021a]]
- [[../papers/xuTunableFerroelectricTopological2022]]
- [[../papers/yanDecipheringStabilityTwodimensional2025]]
- [[../papers/yanagizawaSwitchingChargedensityWave2023]]
- [[../papers/yangRipplingFerroicPhase2021]]
- [[../papers/yuFerroelectricControlMagnetism2026]]
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]
- [[../papers/zhaoRealization2DMultiferroic2024]]
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]
- [[../papers/zhouFirstprinciplesPredictionRedox2004]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/paw-method|PAW 方法]]（高效实现）
- [[../concepts/exchange-correlation-functional|交换关联泛函]]（核心近似）
- [[../entities/VASP|VASP]] / [[../entities/WIEN2k|WIEN2k]]（实现载体）
