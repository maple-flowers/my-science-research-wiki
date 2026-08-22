---
tags: [concept]
title: 'migdal-eliashberg-theory'
type: concept
status: developing
papers: ['CastroNeto2001charge', 'Goswami2011multiferroic', 'Islam2025enhancement', 'Johannes2008fermi', 'Laverock2005fermi', 'Li2013bonding', 'Perugu2024morphology', 'Zhang2003a', 'caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025', 'deSousa2008electrical', 'duUltrasensitiveOptoelectronicBiosensor2025', 'gaoStrainEngineeringFerroelectric2024', 'guoAdvancesTwodimensionalFerroelectric2025', 'hanPolarTopologicalMaterials2025', 'huProgressProspectsLowdimensional2019', 'kawakamiChargedensityWaveAssociated2023', 'laiTwodimensionalFerromagnetismDriven2019', 'liMonolayerPuckeredPentagonal2022', 'martinThinfilmFerroelectricMaterials2016', 'mostovoyMultiferroicsDifferentRoutes2024', 'nicholsonUniaxialStraininducedPhase2021', 'pengStrainEngineering2D2020', 'songEvidenceSinglelayerVan2022', 'vanvleckSurveyTheoryFerromagnetism1945', 'wangTunableD0Topological2025b', 'wongEvidenceMetallic1T', 'wuElectrostaticGatingIntercalation2022', 'xuTunableFerroelectricTopological2022', 'xuTwodimensionalFerroelasticityVan2021', 'yanagizawaSwitchingChargedensityWave2023', 'yangStrainEngineeringTwodimensional2021', 'zhangNonvolatileControlTopological2025', 'zhengAnisotropicSuperconductivityTwodimensional2025', 'zhongHighthroughputExfoliationMultiferroic2025']
updated: 2026-08-18
---

# migdal-eliashberg-theory

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


Migdal-Eliashberg（ME）理论是**基于电子-声子耦合的强耦合超导微观理论**，超越 BCS 弱耦合极限：通过求解 Migdal 方程（电子自能）与 Eliashberg 方程（配对自能）获得超导能隙、临界温度 T_C 与同位素指数等。它是计算常规超导体（元素、合金、氢化物高温超导）T_C 的标准框架。

## 👵 太奶导读

太奶啊，BCS 理论解释了"电子怎么配对变超导"，但只适合"牵绊很轻"的情况。有的材料里电子和晶格振动"缠得很紧"（强耦合），BCS 算不准。Migdal-Eliashberg 理论是升级版：把"电子怎么被振动拖累"（自能）和"怎么被振动撮合配对"（配对自能）两条方程一起严格求解，能算出高温超导氢化物（像 LaH₁₀）的转变温度，是目前最成功的"常规超导计算器"。

## 🧩 核心内容与机制 (Core Content)

- **物理内容**：电子自能（质量重整、寿命）与配对自能（配对能隙函数 Δ(ω)）由 Eliashberg 函数 α²F(ω) 与库仑赝势 μ* 决定。
- **关键方程**：Migdal 方程给出电子-声子耦合下的格林函数；Eliashberg 方程在 Matsubara 或实频率轴上求解（本库超导论文的 T_C 计算）。
- **输入量**：α²F(ω) 由第一性原理电子-声子耦合（electron-phonon-coupling）计算获得（DFPT + 声子谱），μ* 为经验参数。
- **强耦合效应**：能隙比（2Δ/k_BT_C）大于 BCS 值 3.53，同位素指数可偏离 0.5，声子谱展宽明显。
- **氢化物超导**：预言并解释了高压氢化物（LaH₁₀、H₃S 等）的高温超导（本库高温超导氢化物论文）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/electron-phonon-coupling|电子-声子耦合]]：ME 理论的核心输入。
- [[../concepts/superconductivity|超导]]：ME 理论解释的现象。
- [[../concepts/strong-coupling|强耦合]]：ME 理论超越 BCS 的方向。

## 📚 相关论文 (Related Papers)

- [[../papers/CastroNeto2001charge]] — Charge Density Wave, Superconductivity, and Anomalous Metallic Behavior in 2D Transition Metal Dichalcogenides
- [[../papers/Goswami2011multiferroic]] — Multiferroic coupling in nanoscale BiFeO3
- [[../papers/Islam2025enhancement]] — Pressure-induced enhancement of superfluid density in transition metal dichalcogenides with and without charge density wave
- [[../papers/Johannes2008fermi]] — Fermi surface nesting and the origin of charge density waves in metals
- [[../papers/Laverock2005fermi]] — Fermi surface nesting and charge-density wave formation in rare-earth tritellurides
- [[../papers/Li2013bonding]] — Bonding Charge Density and Ultimate Strength of Monolayer Transition Metal Dichalcogenides
- [[../papers/Perugu2024morphology]] — Synthesis, Structural, Morphology and Magnetic Properties: Effect of La on Multiferroic Nature of BiFeO3 Nanoparticles
- [[../papers/Zhang2003a]] — A cellular automaton investigation of the transformation from austenite to ferrite during continuous cooling
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]] — Ferroelectricity-driven strain-mediated magnetoelectric coupling in two-dimensional multiferroic heterostructure
- [[../papers/deSousa2008electrical]] — Electrical control of magnon propagation in multiferroic BiFeO3 films
- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]] — Ultrasensitive optoelectronic biosensor arrays based on twisted bilayer graphene superlattice
- [[../papers/gaoStrainEngineeringFerroelectric2024]] — Strain engineering of ferroelectric polarization and domain in the two-dimensional multiferroic semiconductor
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]] — Advances in two-dimensional ferroelectric materials
- [[../papers/hanPolarTopologicalMaterials2025]] — Polar topological materials and devices: Prospects and challenges
- [[../papers/huProgressProspectsLowdimensional2019]] — Progress and prospects in low‐dimensional multiferroic materials
- [[../papers/kawakamiChargedensityWaveAssociated2023]] — Charge-density wave associated with higher-order Fermi-surface nesting in monolayer VS2
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]] — Two-dimensional ferromagnetism and driven ferroelectricity in van der Waals CuCrP₂S₆
- [[../papers/liMonolayerPuckeredPentagonal2022]] — Monolayer puckered pentagonal VTe2: An emergent two-dimensional ferromagnetic semiconductor with multiferroic coupling
- [[../papers/martinThinfilmFerroelectricMaterials2016]] — Thin-film ferroelectric materials and their applications
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]] — Multiferroics: different routes to magnetoelectric coupling
- [[../papers/nicholsonUniaxialStraininducedPhase2021]] — Uniaxial strain-induced phase transition in the 2D topological semimetal IrTe2
- [[../papers/pengStrainEngineering2D2020]] — Strain engineering of 2D semiconductors and graphene: from strain fields to band-structure tuning and photonic applications
- [[../papers/songEvidenceSinglelayerVan2022]] — Evidence for a single-layer van der Waals multiferroic
- [[../papers/vanvleckSurveyTheoryFerromagnetism1945]] — A Survey of the Theory of Ferromagnetism
- [[../papers/wangTunableD0Topological2025b]] — Tunable d0 topological magnetic states in multiferroic monolayer In2NO2
- [[../papers/wongEvidenceMetallic1T]] — Metallic 1T Phase, 3d1 Electronic Configuration and Charge Density Wave Order in Molecular Beam Epitaxy Grown Monolayer Vanadium Ditelluride
- [[../papers/wuElectrostaticGatingIntercalation2022]] — Electrostatic gating and intercalation in 2D materials
- [[../papers/xuTunableFerroelectricTopological2022]] — Tunable ferroelectric topological defects on 2D topological surfaces: strain engineering skyrmion-like polar structures in 2D materials
- [[../papers/xuTwodimensionalFerroelasticityVan2021]] — Two-dimensional ferroelasticity in van der Waals β'-In2Se3
- [[../papers/yanagizawaSwitchingChargedensityWave2023]] — Switching of charge-density wave by carrier tuning in monolayer TiTe₂
- [[../papers/yangStrainEngineeringTwodimensional2021]] — Strain engineering of <scp>two‐dimensional</scp> materials: Methods, properties, and applications
- [[../papers/zhangNonvolatileControlTopological2025]] — Nonvolatile control of topological magnetism in two-dimensional CrInTe2/In2Se3 multiferroic heterostructures
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] — Anisotropic superconductivity in the two-dimensional metal-organic kagome framework Cu 3 ( CO ) 6
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] — High-throughput exfoliation of multiferroic ternary oxide monolayers with high transition temperature and giant spin splitting
