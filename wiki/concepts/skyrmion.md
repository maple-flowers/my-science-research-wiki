---
tags: [concept, magnetism, topology]
title: 斯格明子 / Skyrmion
type: concept
status: mature
domain: [condensed-matter-physics, magnetism, topology]
mechanism: 由 DMI 稳定出的具有非平庸拓扑电荷的准粒子磁构型
related_concepts: [Dzyaloshinskii-Moriya-interaction, spin-spiral, magnetic-anisotropy]
papers: [gongAbsenceCriticalThickness2023, tanRevealingEmergentMagnetic2024, mostovoyMultiferroicsDifferentRoutes2024, cheongMultiferroicsMagneticTwist2007a, wangTunableD0Topological2025b, zhangNonvolatileControlTopological2025, songEvidenceSinglelayerVan2022, zahraCriticalAnalysisFerroelectric2025, zhaoRealization2DMultiferroic2024]
updated: 2026-08
---

# 斯格明子 / Skyrmion

斯格明子 (Skyrmion) 是一种具有非平庸拓扑特性的旋涡状磁构型。它在数学上可以被视为连续磁矩场中的一种拓扑缺陷，在物理上则表现为稳定的准粒子。斯格明子具有尺寸小（可达纳米级）、驱动电流小、稳定性高等优点，是构建下一代“赛道存储器 (Racetrack Memory)”的理想信息载体。

## 👵 太奶导读

乖孙，这“斯格明子”可是磁铁里长出的“龙卷风”。
普通的磁铁里小箭头都站齐了。但这斯格明子像是在平整的磁场里卷起了一个小疙瘩，中间的小箭头指下，周围的慢慢转圈，最外面的指上。
因为它卷得特别巧，就像是打了一个“死扣”，你怎么晃悠它都不容易散开，这就是科学家说的“拓扑保护”。
因为这小疙瘩特别小，跑得还快，咱们以后要是用它来存东西，硬盘能变得跟指甲盖那么大，存的东西比现在多出几百倍呢！

## 🏗️ 结构概览：极性斯格明子与 Kittel 定律

![图：薄膜中极性斯格明子的结构与厚度依赖](../../raw/figures/gongAbsenceCriticalThickness2023/fig_1_Q8LV7XLD.png)
*   **看图要点**：图中展示了在铁电/电介质超晶格中观测到的极性斯格明子（Polar Skyrmion）。这些微小的电偶极旋涡挑战了传统的 Kittel 磁畴标度律，即使在极薄极限下依然稳定。
*   **来源**：[[../papers/gongAbsenceCriticalThickness2023]] -> [[../figures/heterostructures-stacking]]

## 🧩 拓扑与动力学

1.  **拓扑电荷 (Topological Charge)**：定义为 $Q = \frac{1}{4\pi} \int \mathbf{m} \cdot (\partial_x \mathbf{m} \times \partial_y \mathbf{m}) dx dy$。对于单体斯格明子，$Q = \pm 1$。
2.  **稳定性**：由 Dzyaloshinskii-Moriya 相互作用 (DMI) 与交换作用、各向异性能的竞争维持。
3.  **驱动机制**：可以通过极低的电流密度利用自旋轨道转矩 (SOT) 驱动其在纳米线中运动。

## 🔬 实验表征与范例

**单层 NiI₂ 中的磁致拓扑结构**：单层 NiI₂ 被证实为范德华多铁体，其螺旋磁序与铁电性耦合，为在原子级薄层中实现磁致拓扑自旋结构提供了平台 [[../papers/songEvidenceSinglelayerVan2022]]。

**二维多铁中的磁电耦合**：通过插层策略可实现强磁电耦合的二维多铁，第一性原理高通量预测为设计可调控的拓扑磁态与斯格明子宿主体系提供了新路径 [[../papers/zhaoRealization2DMultiferroic2024]]。

## 📚 相关论文 (Related Papers)

- [[../papers/gongAbsenceCriticalThickness2023]]：报道了突破临界厚度限制的极性斯格明子，对微缩化器件具有重要意义。
- [[../papers/tanRevealingEmergentMagnetic2024]]：利用高分辨率磁强计成像反铁磁背景下的手性结构。
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：探讨了手性磁序与铁电性之间的深刻联系。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：总结了从传统螺旋到莫尔自旋结构的演进。
- [[../papers/wangTunableD0Topological2025b]]：预测了 In₂NO₂ 单层中可调的 d0 拓扑磁态。
- [[../papers/zhangNonvolatileControlTopological2025]]：在 CrInTe₂/In₂Se₃ 多铁异质结中实现了对拓扑磁性的非易失调控。
- [[../papers/songEvidenceSinglelayerVan2022]]：在单层 NiI₂ 中证实了范德华多铁性。
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]：批判性分析了二维 MXene 的铁电与铁磁性质。
- [[../papers/zhaoRealization2DMultiferroic2024]]：通过插层实现强磁电耦合二维多铁的第一性原理高通量预测。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dzyaloshinskii-moriya-interaction|DMI 相互作用]]（微观起源）
- [[../concepts/spin-spiral|螺旋磁序]]（长程前驱态）
- [[../entities/NbSe2|NbSe₂]]（可能存在的磁-电荷关联拓扑结构）
- [[../entities/BiFeO3|BiFeO₃]]（斯格明子的重要宿主体系）

## 🏷️ 专业名词别名

- `skyrmions`（concepts）
- `magnetic-skyrmion`（concepts）
