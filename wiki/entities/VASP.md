---
tags: [entity]
title: 'VASP'
type: entity
status: developing
papers: ['Delley2000', 'Johannes2008fermi', 'Li2013bonding', 'Mińkowski2021cation', 'aiFerroelectricityCoexistedPorbital2022', 'aminiAtomicscaleVisualizationMultiferroicity2024', 'blochlProjectorAugmentedwaveMethod1994b', 'caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025', 'chen3dLevelSymmetry2025', 'chenFerromagneticNonmagnetic1T2022', 'chenStrongSlidingFerroelectricity2024', 'chowdhuryReviewTheoreticalComputational', 'cossuStackingChargedensityWaves2024', 'cuiIntercorrelatedInplaneOutofplane2018a', 'dingPredictionIntrinsicTwodimensional2017a', 'duUltrasensitiveOptoelectronicBiosensor2025', 'fengFerroelectricityMultiferroicityTwodimensional2020', 'gajdosLinearOpticalProperties2006', 'gaoGiantChiralMagnetoelectric2024a', 'gaoStrainEngineeringFerroelectric2024', 'gongAbsenceCriticalThickness2023', 'guanRecentProgressTwoDimensional2020', 'hanTunableSlidingFerroelectricity2025', 'heSwitchingTwodimensionalSliding2025', 'heUltrafastSwitchingDynamics2024', 'henkelmanClimbingImageNudged2000c', 'huProgressProspectsLowdimensional2019', 'huangPolarPhaseDomain2019', 'kaurRecentAdvancesTheoretical2025a', 'khazaeiNovelElectronicMagnetic2013', 'king-smithTheoryPolarizationCrystalline1993', 'kresseEfficiencyAbinitioTotal1996a', 'kresseEfficientIterativeSchemes1996d', 'kresseInitiomolecularDynamicsLiquid1993', 'kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994', 'kresseUltrasoftPseudopotentialsProjector1999c', 'krishnamurthiSpinChargeDensity2020', 'laiTwodimensionalFerromagnetismDriven2019', 'liFerroelasticityDomainPhysics2016', 'liMonolayerPuckeredPentagonal2022', 'liPhaseTransitions2D2021', 'martinThinfilmFerroelectricMaterials2016', 'miaoMagneticFerroelectricMetal2024', 'monkhorstSpecialPointsBrillouinzone1976', 'neumayerCompetingPolarPhases2025', 'nicholsonUniaxialStraininducedPhase2021', 'perdewGeneralizedGradientApproximation1996a', 'sharmaRoomtemperatureFerroelectricSemimetal2019', 'shenEmergenceMultipleFerroelectric2025', 'shishkinImplementationPerformanceFrequencydependentGWmethod2006', 'songEvidenceSinglelayerVan2022', 'sunSlidingFerroelectricityTwodimensional2025', 'tangCombiningIntrinsicSlidinginduced2025', 'tangGridbasedBaderAnalysis2009', 'tianRoomtemperatureTwodimensionalMultiferroic2026', 'wangTunableD0Topological2025b', 'wangTwodimensionalFerroelectricMetal2025', 'wongEvidenceMetallic1T', 'wuCoexistenceFerroelectricityAntiferroelectricity2024', 'wuNonvolatileSwitchableHalfmetallicity2024', 'wuSlidingFerroelectricity2D2021a', 'xuTunableFerroelectricTopological2022', 'xunCoexistingMagnetismFerroelectric2024', 'yanDecipheringStabilityTwodimensional2025', 'yangRipplingFerroicPhase2021', 'yangStrainEngineeringTwodimensional2021', 'yuFerroelectricControlMagnetism2026', 'zhangNonvolatileControlTopological2025', 'zhaoOpticalFingerprintsTwodimensional2024', 'zhaoRealization2DMultiferroic2024', 'zhongHighthroughputExfoliationMultiferroic2025', 'zhouFirstprinciplesPredictionRedox2004']
updated: 2026-08-18
---

# VASP

VASP（Vienna Ab initio Simulation Package，维也纳第一性原理模拟包）是**基于平面波基组与赝势的密度泛函理论（DFT）计算软件**，支持结构优化、电子结构、声子、分子动力学、GW/BSE、杂化泛函与含自旋轨道（SOC）等计算，是材料科学、凝聚态物理与化学领域应用最广泛的第一性原理工具之一（本库绝大多数计算论文的主力软件）。

## 👵 太奶导读

太奶啊，VASP 是"材料计算界最常用的算盘"：科学家想知道一种新材料的电子结构、能不能铁电、超导温度多高，就把原子坐标"喂"给 VASP，它用密度泛函理论"硬算"出来。全世界海量论文的"计算图"都是 VASP 画的。你在这个 Wiki 里看到的各种能带、声子、形成能，大多出自它手。

## 🧩 核心内容与机制 (Core Content)

- **方法**：平面波基组 + PAW 赝势 + DFT（LDA/GGA/PBE、杂化 HSE、DFT+U）（本库 DFT 计算论文）。
- **功能**：结构优化、能带（band-structure）、态密度、声子（有限位移/DFPT）、弹性、磁性、GW/BSE 激发态与分子动力学（本库计算论文）。
- **物理量**：形成能（formation-energy）、能带对齐（band-alignment）、极化（born-effective-charge）、电子-声子耦合（electron-phonon-coupling，与 EPW 联动）（本库迁移与势垒论文）。
- **进阶**：自旋轨道耦合（spin-orbit-coupling）与拓扑不变量、NEB 过渡态、应力-应变。
- **生态**：与 Wannier90（紧束缚/输运）、Phonopy（声子）等联动（本库 Wannier 与声子论文）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/density-functional-theory|密度泛函理论]]：VASP 的理论基础。
- [[../entities/Wannier90|Wannier90]]：VASP 的能带插值伙伴。
- [[../concepts/band-structure|能带结构]]：VASP 的核心输出。
- [[../concepts/formation-energy|形成能]]：VASP 的缺陷计算。

## 📚 相关论文 (Related Papers)

- [[../papers/Delley2000]] — From molecules to solids with the DMol3 approach
- [[../papers/Johannes2008fermi]] — Fermi surface nesting and the origin of charge density waves in metals
- [[../papers/Li2013bonding]] — Bonding Charge Density and Ultimate Strength of Monolayer Transition Metal Dichalcogenides
- [[../papers/Mińkowski2021cation]] — Cation interstitial diffusion in lead telluride and cadmium telluride studied by means of neural network potential based molecular dynamics simulations
- [[../papers/aiFerroelectricityCoexistedPorbital2022]] — Ferroelectricity coexisted with p-orbital ferromagnetism and metallicity in two-dimensional metal oxynitrides
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] — Atomic-Scale Visualization of Multiferroicity in Monolayer NiI2
- [[../papers/blochlProjectorAugmentedwaveMethod1994b]] — Projector augmented-wave method
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]] — Ferroelectricity-driven strain-mediated magnetoelectric coupling in two-dimensional multiferroic heterostructure
- [[../papers/chen3dLevelSymmetry2025]] — 3d-level symmetry between metal layers governing the electronic configuration of Mn2N MXenes and enabling modulation between half-metallicity and semiconductivity
- [[../papers/chenFerromagneticNonmagnetic1T2022]] — Ferromagnetic and nonmagnetic 1T′ charge density wave states in transition metal dichalcogenides: Physical mechanisms and charge doping induced reversible transition
- [[../papers/chenStrongSlidingFerroelectricity2024]] — Strong Sliding Ferroelectricity and Interlayer Sliding Controllable Spintronic Effect in Two-Dimensional HgI₂ Layers
- [[../papers/chowdhuryReviewTheoreticalComputational]] — Computational Methods for Charge Density Waves in 2D Materials
- [[../papers/cossuStackingChargedensityWaves2024]] — Stacking of charge-density waves in 2H-NbSe₂ bilayers
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]] — Intercorrelated In-Plane and Out-of-Plane Ferroelectricity in Ultrathin Two-Dimensional Layered Semiconductor In2Se3
- [[../papers/dingPredictionIntrinsicTwodimensional2017a]] — Prediction of intrinsic two-dimensional ferroelectrics in In2Se3 and other III2-VI3 van der Waals materials
- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]] — Ultrasensitive optoelectronic biosensor arrays based on twisted bilayer graphene superlattice
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in two-dimensional Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/gajdosLinearOpticalProperties2006]] — Linear optical properties in the projector-augmented wave methodology
- [[../papers/gaoGiantChiralMagnetoelectric2024a]] — Giant chiral magnetoelectric oscillations in a van der Waals multiferroic
- [[../papers/gaoStrainEngineeringFerroelectric2024]] — Strain engineering of ferroelectric polarization and domain in the two-dimensional multiferroic semiconductor
- [[../papers/gongAbsenceCriticalThickness2023]] — Absence of critical thickness for polar skyrmions with breaking the Kittel’s law
- [[../papers/guanRecentProgressTwoDimensional2020]] — Recent Progress in Two‐Dimensional Ferroelectric Materials
- [[../papers/hanTunableSlidingFerroelectricity2025]] — Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers
- [[../papers/heSwitchingTwodimensionalSliding2025]] — Switching Two-Dimensional Sliding Ferroelectrics by Mechanical Bending
- [[../papers/heUltrafastSwitchingDynamics2024]] — Ultrafast switching dynamics of the ferroelectric order in stacking-engineered ferroelectrics
- [[../papers/henkelmanClimbingImageNudged2000c]] — A climbing image nudged elastic band method for finding saddle points and minimum energy paths
- [[../papers/huProgressProspectsLowdimensional2019]] — Progress and prospects in low‐dimensional multiferroic materials
- [[../papers/huangPolarPhaseDomain2019]] — Polar and phase domain walls with conducting interfacial states in a Weyl semimetal MoTe2
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/khazaeiNovelElectronicMagnetic2013]] — Novel Electronic and Magnetic Properties of Two-Dimensional Transition Metal Carbides and Nitrides
- [[../papers/king-smithTheoryPolarizationCrystalline1993]] — Theory of polarization of crystalline solids
- [[../papers/kresseEfficiencyAbinitioTotal1996a]] — Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set
- [[../papers/kresseEfficientIterativeSchemes1996d]] — Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set
- [[../papers/kresseInitiomolecularDynamicsLiquid1993]] — <i>Ab initio</i> molecular dynamics for liquid metals
- [[../papers/kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994]] — <i>Ab initio</i> molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transition in germanium
- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]] — From ultrasoft pseudopotentials to the projector augmented-wave method
- [[../papers/krishnamurthiSpinChargeDensity2020]] — Spin/charge density waves at the boundaries of transition metal dichalcogenides
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]] — Two-dimensional ferromagnetism and driven ferroelectricity in van der Waals CuCrP₂S₆
- [[../papers/liFerroelasticityDomainPhysics2016]] — Ferroelasticity and domain physics in two-dimensional transition metal dichalcogenide monolayers
- [[../papers/liMonolayerPuckeredPentagonal2022]] — Monolayer puckered pentagonal VTe2: An emergent two-dimensional ferromagnetic semiconductor with multiferroic coupling
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials
- [[../papers/martinThinfilmFerroelectricMaterials2016]] — Thin-film ferroelectric materials and their applications
- [[../papers/miaoMagneticFerroelectricMetal2024]] — Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding
- [[../papers/monkhorstSpecialPointsBrillouinzone1976]] — Special points for Brillouin-zone integrations
- [[../papers/neumayerCompetingPolarPhases2025]] — Competing polar phases in 2D ferroelectric transition metal thio- and selenophosphates
- [[../papers/nicholsonUniaxialStraininducedPhase2021]] — Uniaxial strain-induced phase transition in the 2D topological semimetal IrTe2
- [[../papers/perdewGeneralizedGradientApproximation1996a]] — Generalized Gradient Approximation Made Simple
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] — A room-temperature ferroelectric semimetal
- [[../papers/shenEmergenceMultipleFerroelectric2025]] — Emergence of multiple ferroelectric states in multilayer black phosphorus
- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]] — Implementation and performance of the frequency-dependent GW method within the PAW framework
- [[../papers/songEvidenceSinglelayerVan2022]] — Evidence for a single-layer van der Waals multiferroic
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]] — Combining intrinsic and sliding-induced polarizations for multistates in two-dimensional ferroelectrics
- [[../papers/tangGridbasedBaderAnalysis2009]] — A grid-based Bader analysis algorithm without lattice bias
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]] — Room-temperature two-dimensional multiferroic metal with voltage-controllable magnetic order
- [[../papers/wangTunableD0Topological2025b]] — Tunable d0 topological magnetic states in multiferroic monolayer In2NO2
- [[../papers/wangTwodimensionalFerroelectricMetal2025]] — Two-dimensional ferroelectric metal CuCrX2 (X = S, Se) for efficient electrocatalysis
- [[../papers/wongEvidenceMetallic1T]] — Metallic 1T Phase, 3d1 Electronic Configuration and Charge Density Wave Order in Molecular Beam Epitaxy Grown Monolayer Vanadium Ditelluride
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]] — Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]] — Nonvolatile switchable half-metallicity and magnetism in the MXene Hf₂MnC₂O₂/Sc₂CO₂ multiferroic heterostructure
- [[../papers/wuSlidingFerroelectricity2D2021a]] — Sliding ferroelectricity in 2D van der Waals materials: Related physics and future opportunities
- [[../papers/xuTunableFerroelectricTopological2022]] — Tunable ferroelectric topological defects on 2D topological surfaces: strain engineering skyrmion-like polar structures in 2D materials
- [[../papers/xunCoexistingMagnetismFerroelectric2024]] — Coexisting Magnetism, Ferroelectric, and Ferrovalley Multiferroic in Stacking-Dependent Two-Dimensional Materials
- [[../papers/yanDecipheringStabilityTwodimensional2025]] — Deciphering the stability of two-dimensional III-V semiconductors: Building blocks and their versatile assembly
- [[../papers/yangRipplingFerroicPhase2021]] — Rippling Ferroic Phase Transition and Domain Switching In 2D Materials
- [[../papers/yangStrainEngineeringTwodimensional2021]] — Strain engineering of <scp>two‐dimensional</scp> materials: Methods, properties, and applications
- [[../papers/yuFerroelectricControlMagnetism2026]] — Ferroelectric Control of Magnetism and Giant Magnetoresistance Via Intercalation-Induced Symmetry Breaking in Two-Dimensional Multiferroics with Strong Magnetoelectric Coupling
- [[../papers/zhangNonvolatileControlTopological2025]] — Nonvolatile control of topological magnetism in two-dimensional CrInTe2/In2Se3 multiferroic heterostructures
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]] — Optical fingerprints of two-dimensional interlayer-sliding multiferroic materials
- [[../papers/zhaoRealization2DMultiferroic2024]] — Realization of 2D multiferroic with strong magnetoelectric coupling by intercalation: a first-principles high-throughput prediction
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] — High-throughput exfoliation of multiferroic ternary oxide monolayers with high transition temperature and giant spin splitting
- [[../papers/zhouFirstprinciplesPredictionRedox2004]] — First-principles prediction of redox potentials in transition-metal compounds with LDA+U
