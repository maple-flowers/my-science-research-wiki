---
tags: [concept]
title: 'order-parameter'
type: concept
status: developing
papers: ['CastroNeto2001charge', 'Chen2019superconductivity', 'Kang2012dimer', 'Koley2020charge', 'aminiAtomicscaleVisualizationMultiferroicity2024', 'chowdhuryReviewTheoreticalComputational', 'fiebigEvolutionMultiferroics2016', 'gorkovStrongElectronlatticeCoupling2012', 'guoAdvancesTwodimensionalFerroelectric2025', 'kaurRecentAdvancesTheoretical2025a', 'lvUnconventionalHystereticTransition2022', 'majumdarInterplayChargeDensity2020', 'mostovoyMultiferroicsDifferentRoutes2024', 'rameshMultiferroicsProgressProspects2007', 'spaldinAdvancesMagnetoelectricMultiferroics2019', 'spaldinRenaissanceMagnetoelectricMultiferroics2005', 'xuTunableFerroelectricTopological2022']
updated: 2026-08-18
---

# order-parameter

序参量（order parameter）是**描述有序相"有序程度"的物理量**：在无序相为零、进入有序相时非零，其非零值标志对称性破缺。极化、磁化、超导能隙、CDW 振幅与应变等皆可为序参量，是相变理论（Landau/Ginzburg-Landau）与材料物性描述的核心概念。

## 👵 太奶导读

太奶啊，序参量就是"衡量材料里'整齐程度'的仪表盘"。比如铁磁体里，所有小磁针方向有多一致，用一个数表示（磁化强度）；高温时是 0（乱），降温后慢慢变成非 0（齐了）。这个"从 0 变非 0"的过程就是相变。科学家用这一把"尺子"统一描述各种相变——铁电看极化、超导看能隙、CDW 看电荷调制，都是同一套思路。

## 🧩 核心内容与机制 (Core Content)

- **定义**：对称性破缺后出现的、在无序相消失的宏观量；可为标量（极化强度）、矢量（磁化）、复数（超导波函数）或张量（应变、向列序）。
- **与相变的关系**：序参量在临界点连续（二级相变）或不连续（一级相变，first-order-phase-transition）出现；Ginzburg-Landau 自由能以其为变量（ginzburg-landau）。
- **多序参量耦合**：铁电+铁磁+铁弹等多序参量共存耦合构成多铁与交叉调控（本库 ferroic-order、magnetoelectric-coupling 论文）。
- **空间变化**：序参量的空间分布（畴、涡旋、缺陷）由梯度能描述，产生 topological-defects 与畴壁结构。
- **软模图像**：序参量的动力学对应软模（soft-mode），相变伴随声子软化。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/phase-transition|相变]]：序参量描述相变。
- [[../concepts/ginzburg-landau|Ginzburg-Landau 理论]]：序参量的唯象理论。
- [[../concepts/ferroic-order|铁性序]]：铁电/铁磁序参量家族。
- [[../concepts/soft-mode|软模]]：序参量的动力学对应。

## 📚 相关论文 (Related Papers)

- [[../papers/CastroNeto2001charge]] — Charge Density Wave, Superconductivity, and Anomalous Metallic Behavior in 2D Transition Metal Dichalcogenides
- [[../papers/Chen2019superconductivity]] — Discommensuration-driven superconductivity in the charge density wave phases of transition-metal dichalcogenides
- [[../papers/Kang2012dimer]] — Dimer impurity scattering, reconstructed Fermi-surface nesting, and density-wave diagnostics in iron pnictides
- [[../papers/Koley2020charge]] — Charge density wave and superconductivity in transition metal dichalcogenides
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] — Atomic-Scale Visualization of Multiferroicity in Monolayer NiI2
- [[../papers/chowdhuryReviewTheoreticalComputational]] — Computational Methods for Charge Density Waves in 2D Materials
- [[../papers/fiebigEvolutionMultiferroics2016]] — The evolution of multiferroics
- [[../papers/gorkovStrongElectronlatticeCoupling2012]] — Strong electron-lattice coupling as the mechanism behind charge density wave transformations in transition-metal dichalcogenides
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]] — Advances in two-dimensional ferroelectric materials
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/lvUnconventionalHystereticTransition2022]] — Unconventional Hysteretic Transition in a Charge Density Wave
- [[../papers/majumdarInterplayChargeDensity2020]] — Interplay of charge density wave and multiband superconductivity in layered quasi-two-dimensional materials: The case of 2H-NbS₂ and 2H-NbSe₂
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]] — Multiferroics: different routes to magnetoelectric coupling
- [[../papers/rameshMultiferroicsProgressProspects2007]] — Multiferroics: progress and prospects in thin films
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]] — Advances in magnetoelectric multiferroics
- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]] — The Renaissance of Magnetoelectric Multiferroics
- [[../papers/xuTunableFerroelectricTopological2022]] — Tunable ferroelectric topological defects on 2D topological surfaces: strain engineering skyrmion-like polar structures in 2D materials
