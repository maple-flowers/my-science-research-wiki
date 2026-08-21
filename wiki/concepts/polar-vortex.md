---
tags: [concept, ferroelectricity, topological-defects]
title: 极化涡旋 / Polar Vortex
type: concept
status: mature
domain: [condensed-matter-physics, ferroelectricity]
mechanism: 去极化场、界面弹性能与畴壁能竞争下极化矢量呈环形涡旋分布
related_concepts: [ferroelectricity, topological-defects, superlattice, domain-wall, polarization-switching, polar-skyrmion]
papers: [gongAbsenceCriticalThickness2023, hanPolarTopologicalMaterials2025, xuTunableFerroelectricTopological2022, gomez-ortizKittelLawDomain2023]
updated: 2026-08-20
---

# polar-vortex

极化涡旋（polar vortex）指**铁电/极性体系中极化矢量呈涡旋状（环形）空间分布**的拓扑结构，常在铁电超晶格、铁电纳米结构与受限几何中出现，以抵消去极化场并降低静电与弹性能。极化涡旋及其反涡旋、畴壁网络是"拓扑铁电"与铁电斯格明子（polar skyrmion）研究的核心对象。

## 👵 太奶导读

太奶啊，铁电材料里的"电箭头"（极化）通常齐刷刷朝一个方向；但在超薄多层堆叠（超晶格）里，这些箭头会被迫"绕圈"——排成一个个小漩涡（极化涡旋），像水面打转的水涡。为什么要打转？因为这样最省能量，还能躲开"自己拆自己"的去极化场。这种涡旋本身成了新的"信息单元"，是铁电里的拓扑物态。

## 🏗️ 结构概览

极化涡旋的形成是**去极化场、界面弹性能与畴壁能**三方竞争的结果：超薄铁电层被顺电层夹持时，面外极化产生强去极化场，体系通过极化"绕圈"（面内环形分量）消除净束缚电荷，代价是局部梯度能与弹性能。

![图：PbTiO₃/SrTiO₃ 超晶格中的极化涡旋与畴形成](../../raw/figures/gomez-ortizKittelLawDomain2023/fig_1_I73SSRGV.png)
*   **看图要点**：示意超晶格中极化涡旋（通量闭合）结构的形成及其与层厚的尺度关系。
*   **来源**：[[../papers/gomez-ortizKittelLawDomain2023]]

## 🧩 核心内容与机制 (Core Content)

- **形成机制**：铁电/顺电超晶格（如 PbTiO₃/SrTiO₃）中，去极化场、界面弹性与畴壁能的竞争迫使极化呈涡旋/闭域结构（本库超晶格极化涡旋论文）。
- **拓扑分类**：涡旋（vortex）、反涡旋（antivortex）、极化斯格明子（polar skyrmion）与域拓扑缺陷（topological-defects）具整数拓扑荷，稳定且可迁移。
- **畴壁网络**：涡旋核心与畴壁构成导电/非导电网络，可被电场操控（本库拓扑畴壁与铁电畴论文）。
- **超晶格调控**：组分厚度比、应变与电场调控涡旋尺寸与稳定性（本库 PbTiO₃/SrTiO₃ 超晶格论文）。
- **应用前景**：涡旋作为超小尺寸信息载体与拓扑电子学元件（存算一体）。

## 📊 参数对照 (Parameters)

| 结构 | 拓扑荷 | 尺度规律 | 稳定性来源 | 调控 |
|---|---|---|---|---|
| 极化涡旋 vortex | 1 | 畴宽 ∝ √层厚（Kittel 律，可被破坏） | 去极化场+弹性能 | 厚度比、电场 |
| 反涡旋 antivortex | -1 | 与涡旋成对出现 | 阻挫/图案化 | 应变 |
| 极性斯格明子 | 1 | 可低于临界厚度存在 | 梯度能+去极化场 | 应变、厚度 |
| 通量闭合域 | 0 | 宏观畴尺度 | 静电+弹性能 | 电场 |

## 📚 相关论文 (Related Papers)

- [[../papers/gongAbsenceCriticalThickness2023]] — Absence of critical thickness for polar skyrmions with breaking the Kittel's law
- [[../papers/hanPolarTopologicalMaterials2025]] — Polar topological materials and devices: Prospects and challenges
- [[../papers/xuTunableFerroelectricTopological2022]] — Tunable ferroelectric topological defects on 2D topological surfaces: strain engineering skyrmion-like polar structures in 2D materials
- [[../papers/gomez-ortizKittelLawDomain2023]] — Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：极化涡旋的序基础。
- [[../concepts/topological-defects|拓扑缺陷]]：涡旋的拓扑性质。
- [[../concepts/superlattice|超晶格]]：极化涡旋的平台。
- [[../concepts/domain-wall|畴壁]]：涡旋伴随的畴结构。
- [[../concepts/polarization-switching|极化翻转]]：涡旋态的电场调控通道。
- [[../concepts/polar-skyrmion|极性斯格明子]]：涡旋的拓扑亲缘结构。
