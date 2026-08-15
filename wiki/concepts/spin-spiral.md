---
tags: [concept, magnetism, multiferroics]
title: 螺旋磁序 / Spin Spiral
type: concept
status: mature
domain: [condensed-matter-physics, magnetism]
mechanism: 相邻自旋之间由于非对称交换相互作用导致的周期性螺旋排列
related_concepts: [multiferroicity, magnetoelectric-coupling, Dzyaloshinskii-Moriya-interaction, skyrmion]
papers: [cheongMultiferroicsMagneticTwist2007a, mostovoyMultiferroicsDifferentRoutes2024, fiebigEvolutionMultiferroics2016, Goswami2011multiferroic, aminiAtomicscaleVisualizationMultiferroicity2024, RecentAdvancesGrowth2025, rameshMultiferroicsProgressProspects2007]
updated: 2026-08
---

# 螺旋磁序 / Spin Spiral

螺旋磁序 (Spin Spiral) 是一种非共线的磁有序状态，其中原子的自旋方向沿特定空间方向呈周期性旋转。这种结构通常由海森堡交换作用与 Dzyaloshinskii-Moriya 相互作用 (DMI) 的竞争产生。在多铁性领域，螺旋磁序因能自发打破反演对称性而诱导铁电极化，是第二类多铁性（磁致铁电）的核心机制。

## 👵 太奶导读

好孩子，你可以把“螺旋磁序”想象成操场上正在做广播体操的小人儿。
普通的磁铁就像大家都站得笔直，所有人的手都指向同一个方向（共线磁序）。
但在螺旋磁序里，排队的小人儿每个人转的角度都比前一个人偏一点点。你从队头往队尾看过去，就像看到了一道旋转的“人肉旋风”或者是一根拧着的麻花。
因为这种磁序是扭着的，它就能把材料里原本平衡的电荷分布给扭歪了，从而产生电极化。科学家们就是用这种“磁扭曲”的方法，在一些本来不通电的材料里变出了电性。

## 🏗️ 结构概览：气旋式螺旋磁序

螺旋磁序可根据旋转轴与波矢的关系分为旋性螺旋（Cycloidal）和螺旋线（Helical）等。

![图：TbMnO3 中的螺旋磁序诱导极化示意](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_1_G5K2M3NX.png)
*   **看图要点**：图中展示了自旋在 $bc$ 平面内旋转并沿 $b$ 轴传播的旋性螺旋序。这种手性结构导致电荷中心偏离，产生沿 $c$ 轴的极化 $P$。
*   **来源**：[[../papers/cheongMultiferroicsMagneticTwist2007a]] -> [[../figures/mathematical-models-magnetoelectric|磁电耦合与多铁理论]]
*(注：引用自 Cheong 2007 经典综述图示)*

## 🧩 物理起源与分类

1.  **DMI 驱动**：在缺乏反演中心的环境下，非对称交换作用倾向于使相邻自旋垂直排列，与海森堡作用竞争形成长程螺旋。
2.  **磁阻挫驱动**：由于晶格几何结构或近邻/次近邻相互作用竞争，自旋无法同时满足所有最低能态，从而折中形成螺旋结构。

螺旋磁序诱导极化的普遍公式为：
$$ \mathbf{P} \propto \mathbf{r}_{ij} \times (\mathbf{S}_i \times \mathbf{S}_j) $$
其中 $\mathbf{r}_{ij}$ 是连接相邻格点的矢量。

## 🔬 实验表征/特征与范例

**磁致铁电的经典范例（TbMnO₃ 等）**：在正交稀土锰氧化物 TbMnO₃、TbMn₂O₅ 中，磁场可剧烈调控电极化——实现 90° 极化翻转、约 500% 的巨磁介电效应以及 180° 可逆极化翻转。磁阻挫是这类磁致铁电的关键，实验判据为居里-外斯温度远高于磁有序温度（|T_CW| ≫ T_N）[[../papers/cheongMultiferroicsMagneticTwist2007a]]。

**磁电耦合的不同路径**：第 I 类多铁（如 BiFeO₃）极化强、温度高但耦合弱；第 II 类多铁（如 RMnO₃、NiI₂）耦合强但极化弱、温度低。微观机制可统一为对称交换伸缩与逆 DMI 等少数核心机制，并伴随电磁子（electromagnon）与磁斯格明子等元激发与拓扑缺陷 [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]。

**二维螺旋磁序的实验实现**：单层/少层 NiI₂ 通过 SHG、圆偏振拉曼等光学手段证实螺旋磁序诱导的本征第二类多铁性；二维多铁材料可通过 CVD、PVD、MBE、ALD 等气相方法生长，并用 STM、SHG、拉曼、双折射、TEM 等表征 [[../papers/RecentAdvancesGrowth2025]]。

**多铁薄膜背景**：多铁性薄膜（BiFeO₃、YMnO₃ 等）的经典综述，涵盖单相薄膜、水平/垂直异质结构三种架构 [[../papers/rameshMultiferroicsProgressProspects2007]]。

## 📚 相关论文 (Related Papers)

- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：首次系统阐述了磁扭曲诱导铁电性的物理图像。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：总结了从传统螺旋到莫尔自旋结构的演进。
- [[../papers/fiebigEvolutionMultiferroics2016]]：讨论了螺旋磁序在非平衡态下的动态调控。
- [[../papers/Goswami2011multiferroic]]：研究了纳米尺度 BiFeO₃ 中的多铁耦合。
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]：在单层 NiI₂ 中原位可视化多铁性。
- [[../papers/RecentAdvancesGrowth2025]]：综述了二维多铁材料的生长、表征与应用。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：多铁性薄膜领域的经典综述。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dzyaloshinskii-moriya-interaction|DMI 相互作用]]（微观动力）
- [[../concepts/skyrmion|斯格明子]]（局域手性拓扑）
- [[../concepts/multiferroicity|多铁性]]（宏观表现）
- [[../entities/NbSe2|NbSe₂ / TMDs]]（可能存在的 CDW-自旋螺旋共存）

## 🏷️ 专业名词别名

- `spiral-magnetic-order`（concepts）
- `spiral-magnetism`（concepts）
- `spiral-spin-structure`（concepts）
