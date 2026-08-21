---
tags: [concept]
title: 'inversion-symmetry'
type: concept
status: developing
papers: ['CastroNeto2001charge', 'cossuStackingChargedensityWaves2024', 'feiFerroelectricSwitchingTwodimensional2018a', 'fengFerroelectricityMultiferroicityTwodimensional2020', 'guoAdvancesTwodimensionalFerroelectric2025', 'huangTwodimensionalIn2Se3Rising2022', 'krishnamurthiSpinChargeDensity2020', 'spaldinAdvancesMagnetoelectricMultiferroics2019', 'xuTunableFerroelectricTopological2022', 'zhaoOpticalFingerprintsTwodimensional2024']
updated: 2026-08-18
---

# inversion-symmetry

反演对称（inversion symmetry）指物理体系在**空间反演操作（r→-r）下保持不变的对称性**。它是晶体的基本空间对称性之一，决定能带简并（Kramers 简并）、电子偶极矩是否允许存在、铁电/压电/非线性光学等物性是否出现，是分析材料物性的第一性判断依据。

## 👵 太奶导读

太奶啊，"反演对称"就是材料"以任意一点为中心，把左右、上下、前后都翻个个儿，材料看起来跟没翻一样"。这样的材料"太正派"，不允许有电偶极矩（没有铁电、压电那些"偏心"本事）。反过来，一旦材料"不满足"这个对称（反演破缺），就解锁一堆新功能。所以看一种新材料，先问一句：它反演对称吗？

## 🧩 核心内容与机制 (Core Content)

- **空间群判定**：晶体点群中是否含反演中心（-1 操作）决定有无反演对称；230 个空间群中约 70 个为有心空间群。
- **能带简并**：反演对称 + 时间反演共同保证能带在 k 和 -k 处的自旋简并（Kramers 简并），决定自旋劈裂（Rashba 效应需反演破缺，本库 spin-orbit-coupling 相关）。
- **物性约束**：反演对称体系不允许净极化（无铁电/压电/二阶非线性响应），磁电效应与 DMI 螺旋磁序也被禁止。
- **反演破缺的途径**：结构畸变、表面/界面、应变与二维异质堆垛可打破反演对称（inversion-symmetry-breaking）。
- **拓扑性质**：反演对称与拓扑不变量（如 Z₂ 指标）密切相关，其与时间反演的组合决定拓扑绝缘体分类（topological-insulator）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/inversion-symmetry-breaking|反演对称破缺]]：对称性降低及其后果。
- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：与反演对称共同决定能带。
- [[../concepts/topological-insulator|拓扑绝缘体]]：反演对称相关的拓扑分类。
- [[../concepts/ferroelectricity|铁电性]]：被反演对称禁止的物性。

## 📚 相关论文 (Related Papers)

- [[../papers/CastroNeto2001charge]] — Charge Density Wave, Superconductivity, and Anomalous Metallic Behavior in 2D Transition Metal Dichalcogenides
- [[../papers/cossuStackingChargedensityWaves2024]] — Stacking of charge-density waves in 2H-NbSe₂ bilayers
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]] — Ferroelectric switching of a two-dimensional metal
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in two-dimensional Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]] — Advances in two-dimensional ferroelectric materials
- [[../papers/huangTwodimensionalIn2Se3Rising2022]] — Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage
- [[../papers/krishnamurthiSpinChargeDensity2020]] — Spin/charge density waves at the boundaries of transition metal dichalcogenides
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]] — Advances in magnetoelectric multiferroics
- [[../papers/xuTunableFerroelectricTopological2022]] — Tunable ferroelectric topological defects on 2D topological surfaces: strain engineering skyrmion-like polar structures in 2D materials
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]] — Optical fingerprints of two-dimensional interlayer-sliding multiferroic materials
