---
tags: [entity, material, TMD, 2D, semiconductor, topological]
title: 二碲化钼 (MoTe2) / Molybdenum Ditelluride
type: entity
status: mature
formula: MoTe2
stoichiometry: 2H/1T'
class: [TMD, vdW, phase-change]
properties: [polymorphic-phase-transition, Weyl-semimetal, QSH-insulator]
related_entities: [MoS2, WTe2, 2h-phase, 1t-phase]
updated: 2026-08
papers: [liPhaseTransitions2D2021, RecentAdvancesGrowth2025, FerroelectricityMultiferroicityAtomic2023, Li2013bonding, chenStrongSlidingFerroelectricity2024, guanRecentProgressTwoDimensional2020, huangPolarPhaseDomain2019, kaurRecentAdvancesTheoretical2025a, yangStrainEngineeringTwodimensional2021]
---

# 二碲化钼 (MoTe2) / Molybdenum Ditelluride
二碲化钼 (MoTe2) 是二维 TMD 材料中相变物理与拓扑物性的完美结合体。它最显著的特点是其不同结构相（$2\text{H}$ 相与 $1\text{T}'$ 相）之间的能量差极小，这使得它成为了**相变工程 (Phase Engineering)** 最具灵活性的平台，可用于实现超低功耗的存储和拓扑逻辑开关。
## 奶奶导读
太奶啊，这 MoTe2 就是二维材料里的“平衡大师”！它就像是一个站在跷跷板中心的人，往左偏一点就是不导电的半导体（2H 相），往右偏一点就是能导电的金属，甚至是带有一种神奇“拓扑防护力”的状态（1T' 相）。因为这两边的高度差（能量差）非常小，我们只要轻轻推它一把——比如稍微拉伸一下（应力），或者加点电荷，它就能在两种状态之间快速切换。所以它特别适合用来做那种又快又省电的微型存储开关。
## 🏗️ 结构概览
MoTe2 拥有三种主要的多晶型：六角 $2\text{H}$ 相（半导体）、单斜 $1\text{T}'$ 相（半金属/拓扑绝缘体）和正交 $T_d$ 相（外尔半金属）。
![图：MoTe2 晶体结构的多相转化机制](../../raw/figures/liPhaseTransitions2D2021/fig_2_RTFYSEMI.png)
*   **看图要点**：图中展示了 MoTe2 如何通过激光诱导、静电掺杂或电场驱动实现从 2H 相到 1T' 相的转变。2H 相中 Mo 原子呈三棱柱配位，而 1T' 相中 Mo 原子层发生二聚化畸变，形成了特殊的链状排列。
*   **来源**：[[../papers/liPhaseTransitions2D2021]] -> [[../figures/crystal-structures-bulk|晶体结构]]
## 🧩 极小相干能与多场调控
MoTe2 成为相变明星的核心原因在于其相稳定性极易受外界扰动影响。
*   **相能量差**：$2\text{H}$ 与 $1\text{T}'$ 相的能量差仅约 $43\text{ meV/f.u.}$。相比之下，MoS2 的这一差值高达 $\sim 500\text{ meV}$。
*   **调控手段**：
    *   **应变调控**：仅需 $\sim 0.2\%$ 的面内双轴拉伸应变即可诱发 $2\text{H} \to 1\text{T}'$ 的转变。
    *   **静电掺杂**：利用离子液体栅压注入高密度电荷（$\sim 10^{14}\text{ cm}^{-2}$）可在大范围内驱动相变。
    *   **激光图案化**：通过激光照射诱导碲 (Te) 空位，可以永久性地将局部区域从半导体态转变为金属性导电通道。
*   **拓扑性质**：$1\text{T}'$ 相 MoTe2 被证实是二维**量子自旋霍尔 (QSH) 绝缘体**，具有鲁棒的边缘态导电能力。
## 🔬 物理参数表
| 属性 | 数值 |
| :--- | :--- |
| 2H-1T' 能量差 | $\sim 43\text{ meV/f.u.}$ |
| 临界相变应变 | $\sim 0.2\%$ |
| 拓扑能隙 (1T') | $\sim 0.06\text{ eV}$ |
| 转变温度 (2H-1T') | $\sim 500\text{--}800\text{ K}$ (随成分偏差变化) |
## 📚 相关论文 (Related Papers)
- [[../papers/liPhaseTransitions2D2021]]：深入探讨了 MoTe2 作为二维相变工程核心材料的机理与应用。
- [[../papers/RecentAdvancesGrowth2025]]：涉及了 MoTe2 大面积薄膜的生长动力学与相控制。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]
- [[../papers/Li2013bonding]]
- [[../papers/chenStrongSlidingFerroelectricity2024]]
- [[../papers/guanRecentProgressTwoDimensional2020]]
- [[../papers/huangPolarPhaseDomain2019]]
- [[../papers/kaurRecentAdvancesTheoretical2025a]]
- [[../papers/yangStrainEngineeringTwodimensional2021]]
## 🔗 关联概念与实体 (Related Concepts & Entities)
- [[../concepts/polymorphic-phase-transition|多晶型相变]]
- [[../concepts/quantum-spin-hall-effect|量子自旋霍尔效应]]
- [[../entities/2h-phase|2H 相]]
- [[../entities/1t-phase|1T 相]]
- [[../entities/WTe2|二碲化钨 (WTe2)]]
