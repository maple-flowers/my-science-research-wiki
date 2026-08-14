---
tags: [entity, phase, material-structure, TMD]
title: Td 相 / Td-phase
type: entity
status: mature
formula: "MX2"
stoichiometry: Td
class: [structure-phase, TMD]
properties: [orthorhombic, non-centrosymmetric, Weyl-semimetal, ferroelectric-metal]
related_entities: [1t-phase, WTe2, MoTe2]
papers: [sharmaRoomtemperatureFerroelectricSemimetal2019, liPhaseTransitions2D2021]
updated: 2026-08
---

# Td 相 / Td-phase

$T_d$ 相是过渡金属硫族化合物 (TMD) 的一种低对称性正交结构相。它是从 $1\text{T}'$ 相衍生而来的，但与 $1\text{T}'$ 相不同的是，$T_d$ 相彻底打破了空间反演对称性，成为了一种本征的**极性相 (Polar phase)**。这一结构特征使 $T_d$ 相成为了实现外尔半金属态与铁电金属性的绝佳舞台。

## 奶奶导读

太奶啊，这 $T_d$ 相就是 TMD 家族里的“反骨仔”。大家都说金属材料是对称的、平衡的，可这个 $T_d$ 相偏偏要把原子的位置坐歪。它就像是原本整齐的原子队伍，突然所有人都往同一个方向挪了半步（打破了中心对称）。这个“挪动”非常关键，因为它让材料在能导电的同时，内部还产生了一股像指南针一样的极化能量。这就是为什么科学家们能用它做出那种神奇的“铁电金属”。

## 🏗️ 结构概览

$Td$ 相属于正交晶系，空间群通常为 $Pmn2_1$。其基本单元是高度畸变的八面体，金属原子在层内形成了锯齿状的金属链。

![图：WTe2 的 Td 相原子排布与镜面对称性](../../raw/figures/sharmaRoomtemperatureFerroelectricSemimetal2019/fig_1_NDNYXQ2A.png)
*   **看图要点**：图中展示了 $T_d$ 相的结构特征。与 $1\text{T}'$ 相相比，$T_d$ 相消除了层间的反演中心。W 原子沿 $a$ 轴的锯齿链位移是其极性起源的核心。
*   **来源**：[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] -> [[../figures/crystal-structures-bulk|晶体结构]]

## 🧩 拓扑物性与极性序

$T_d$ 相的物理特性在凝聚态物理中具有里程碑意义：

*   **外尔半金属 (Weyl Semimetal)**：由于缺乏反演对称性，$T_d$ 相的 WTe2 和 MoTe2 被证实为 II 型外尔半金属，拥有受拓扑保护的费米弧边缘态。
*   **铁电金属性 (Ferroelectric Metallicity)**：$T_d$ 相是少数能在块体状态下支持室温铁电性的金属体系。其极化主要源于晶格的不对称畸变，且由于载流子浓度较低，电场仍能部分穿透并驱动极化翻转。
*   **相变演化**：在 MoTe2 等体系中，$T_d$ 相与 $1\text{T}'$ 相的能量差极小，随温度升高会发生从 $T_d$（低温极性相）到 $1\text{T}'$（高温非极性相）的结构转变。

## 🔬 结构对比表

| 特征 | Td 相 | 1T' 相 |
| :--- | :--- | :--- |
| 晶系 | 正交 (Orthorhombic) | 单斜 (Monoclinic) |
| 反演对称性 | 缺失 (Non-centrosymmetric) | 具备 (Centrosymmetric) |
| 空间群 | $Pmn2_1$ | $P2_1/m$ |
| 铁电性 | 本征铁电 | 非铁电 |

## 📚 相关论文 (Related Papers)

- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：详细研究了 $T_d$ 相 WTe2 中的室温铁电金属性。
- [[../papers/liPhaseTransitions2D2021]]：归纳了二维材料中多晶型相变的演化逻辑。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/weyl-semimetal|外尔半金属]]
- [[../concepts/ferroelectric-metal|铁电金属]]
- [[../entities/WTe2|二碲化钨 (WTe2)]]
- [[../entities/MoTe2|二碲化钼 (MoTe2)]]
