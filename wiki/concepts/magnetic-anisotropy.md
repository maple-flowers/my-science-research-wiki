---
tags: [concept, magnetism]
title: 磁各向异性 / Magnetic Anisotropy
type: concept
status: mature
domain: [condensed-matter-physics, magnetism]
mechanism: 磁性能随晶格方向不同而表现出的差异，源于晶体场和自旋-轨道耦合
related_concepts: [spin-orbit-coupling, magnetoelectric-coupling, easy-axis, easy-plane]
papers: [caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenStrongSlidingFerroelectricity2024, prosandeevKittelLawInBiFeO3Ultrathin2010, hanTunableSlidingFerroelectricity2025, songEvidenceSinglelayerVan2022, wangTunableD0Topological2025b]
updated: 2026-08
---

# 磁各向异性 / Magnetic Anisotropy

磁各向异性 (Magnetic Anisotropy) 指的是材料的磁学性质（如磁化能、矫顽力等）在空间不同方向上表现出差异的特性。这意味着自旋倾向于指向某些特定方向（易磁化轴）而非其他方向（难磁化轴）。它是实现非易失性磁存储的物理前提。

## 👵 太奶导读

好孩子，这“各向异性”就像是给磁铁里的小箭头找了个“舒适区”。
通常情况下，小箭头往哪儿指都行。但因为材料的原子排布是有讲究的，有些方向就像是宽敞的大道（易轴），小箭头呆在那儿最省力；有些方向就像是窄小的胡同（难轴），非要往那儿指就得费老鼻子劲了。
要是没有这种偏心眼，咱们硬盘里的数据就像沙子一样随风倒，根本存不住。科学家们现在想方设法用应变或者电场去改这个“舒适区”，好让小箭头能听话地翻转。

## 🏗️ 结构概览：应变调控磁各向异性

在二维 Fe₃GaTe₂ 中，磁各向异性能 (MAE) 随面内应变发生显著变化。

![图：Fe3GaTe2 的磁各向异性能随应变翻转示意](../../raw/figures/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025/fig_2_BQHGIU8F.png)
*   **看图要点**：图中 (f) 展示了 DFT 计算得到的 MAE。在零应变下，面外方向 (mz) 能量最低；随着拉伸应变增加，面内方向 (mx) 变为能量最低，实现了易轴的 90° 翻转。
*   **来源**：[[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]] -> [[../figures/vibrational-spectra]]

## 🧩 能量项与来源

总磁能通常表示为：
$$ E_a = K_u \sin^2 \theta $$
其中 $K_u$ 为磁各向异性常数。

主要来源包括：
1.  **磁晶各向异性 (Magnetocrystalline Anisotropy)**：核心来源，由自旋-轨道耦合 (SOC) 将自旋方向与晶体轴绑定。
2.  **形状各向异性 (Shape Anisotropy)**：由磁静电能决定，倾向于使磁矩沿长轴排列。
3.  **磁弹各向异性 (Magnetoelastic Anisotropy)**：由应变改变轨道占据和能级分裂引起。

## 📚 相关论文 (Related Papers)

- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：定量研究了应变对 Fe₃GaTe₂ 磁各向异性的调控。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：分析了 SOC 对滑动铁电中各向异性的贡献。
- [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]：探讨了薄膜中畴壁能与各向异性的标度关系。
- [[../papers/hanTunableSlidingFerroelectricity2025]]
- [[../papers/songEvidenceSinglelayerVan2022]]
- [[../papers/wangTunableD0Topological2025b]]
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]] — Ferroelectricity-driven strain-mediated magnetoelectric coupling in two-dimensional multiferroic heterostructure
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in two-dimensional Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/hanTunableSlidingFerroelectricity2025]] — Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers
- [[../papers/liMonolayerPuckeredPentagonal2022]] — Monolayer puckered pentagonal VTe2: An emergent two-dimensional ferromagnetic semiconductor with multiferroic coupling
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]] — Spintronics in Two-Dimensional Materials
- [[../papers/rameshMultiferroicsProgressProspects2007]] — Multiferroics: progress and prospects in thin films
- [[../papers/songEvidenceSinglelayerVan2022]] — Evidence for a single-layer van der Waals multiferroic
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]] — Advances in magnetoelectric multiferroics
- [[../papers/tangMultiferroicityTwodimensionalVan2025]] — Towards Multiferroicity in Two-Dimensional Van Der Waals Materials: Challenges and Opportunities
- [[../papers/wangTunableD0Topological2025b]] — Tunable d0 topological magnetic states in multiferroic monolayer In2NO2
- [[../papers/wuElectrostaticGatingIntercalation2022]] — Electrostatic gating and intercalation in 2D materials
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]] — Nonvolatile switchable half-metallicity and magnetism in the MXene Hf₂MnC₂O₂/Sc₂CO₂ multiferroic heterostructure
- [[../papers/zhangNonvolatileControlTopological2025]] — Nonvolatile control of topological magnetism in two-dimensional CrInTe2/In2Se3 multiferroic heterostructures
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] — High-throughput exfoliation of multiferroic ternary oxide monolayers with high transition temperature and giant spin splitting

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-orbit-coupling|自旋-轨道耦合]]（微观推手）
- [[../concepts/easy-axis|易轴]]（能量最低方向）
- [[../entities/Fe3GeTe2|Fe₃GaTe₂]]（具有强垂直各向异性的二维材料）
- [[../entities/CrI3|CrI₃]]（首个二维铁磁体，具强各向异性）

## 🏷️ 专业名词别名

- `magnetic-anisotropy-energy`（concepts）
