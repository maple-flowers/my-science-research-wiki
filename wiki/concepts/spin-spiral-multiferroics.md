---
tags: [concept, multiferroics, magnetism, ferroelectricity]
title: 自旋螺旋多铁性 / Spin-Spiral Multiferroics
type: concept
status: mature
domain: [condensed-matter-physics, multiferroics, magnetism]
mechanism: 非共线螺旋磁序通过反 Dzyaloshinskii-Moriya 机制打破空间反演对称性诱导铁电极化
related_concepts: [spin-spiral, ferroelectricity, polarization-switching, chirality, skyrmion, magnetic-anisotropy]
papers: [cheongMultiferroicsMagneticTwist2007a, mostovoyMultiferroicsDifferentRoutes2024]
updated: 2026-08-20
---

# 自旋螺旋多铁性 / Spin-Spiral Multiferroics

自旋螺旋多铁性（spin-spiral multiferroics）指一类**铁电性由磁性（非共线自旋螺旋/摆线磁序）诱导**的多铁性材料，属于第二类多铁（type-II multiferroics）。其核心机制是螺旋磁序在空间上打破反演对称性，通过**反 Dzyaloshinskii-Moriya（逆 DM）相互作用**或交换伸缩在相邻磁离子间产生净电极化，从而实现"磁序-铁电"之间的强耦合。典型代表包括 TbMnO$_3$、Ni$_3$V$_2$O$_8$、正交相 HoMnO$_3$ 等，其磁电耦合强度远超传统第一类多铁，但居里温度普遍较低。

## 👵 太奶导读

乖孙，这一条讲的是「自旋螺旋多铁性」——一种"磁性当爹、电性当儿"的奇材。
一般材料里小磁针要么都朝一个方向，要么乱糟糟。可有些材料里的小磁针会排成"螺旋楼梯"一样的队形，一圈一圈拧着转。妙就妙在：这一拧，竟然把材料的"电学对称性"也拧坏了，凭空变出了电极化（就是材料两头带上正负电）。科学家管这叫"磁生电"。这样一来，你只要用磁场拨一下螺旋的拧法，材料的电极化就会跟着变——磁场和电场就这样打通了，做传感器、存储器都特别有想象力。可惜这种"拧出来"的电往往很弱，而且在很低的温度下才有，这是目前最大的短板。

## 🏗️ 结构概览

自旋螺旋多铁性的"磁序-铁电"耦合链：螺旋磁序 → 反演对称性破缺 → 净电极化。

![图：磁扭转铁电性的机制示意](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_1_D8A9TF3K.png)
*   **看图要点**：示意自旋螺旋/摆线磁序如何打破空间反演对称性，从而诱导铁电极化（"磁的扭转带来电的极化"）。
*   **来源**：[[../papers/cheongMultiferroicsMagneticTwist2007a]]

## 🧩 核心内容与机制 (Core Content)

- **逆 DMI 机制**：相邻自旋 $\mathbf{S}_i, \mathbf{S}_j$ 的螺旋排列使反演对称性在实空间被破坏，离子位移产生极化 $\mathbf{P} \propto \mathbf{e}_{ij} \times (\mathbf{S}_i \times \mathbf{S}_j)$，极化方向由自旋手性与螺旋传播方向共同决定。
- **交换伸缩机制**：某些体系中（如 $E$-type 反铁磁序），自旋序通过交换伸缩破坏反演对称性产生更大极化。
- **磁电耦合**：螺旋序的波矢、手性对外磁场敏感，磁场可翻转手性进而翻转极化，实现磁场写入/电场读取（磁电忆阻）。
- **相变序**：典型材料（TbMnO$_3$）经历顺磁 → 正弦波磁序（非铁电）→ 螺旋磁序（铁电）的序参量链，极化随螺旋序出现而出现。
- **温度瓶颈**：螺旋多铁的居里/尼尔温度多在 30-70 K 量级，室温实现仍待新机制（如应变、层叠、f-d 耦合工程）。

## 📊 参数对照 (Parameters)

| 材料 | 磁序类型 | 极化来源 | 铁电温度 | 磁电耦合特征 |
|---|---|---|---|---|
| TbMnO$_3$ | 摆线螺旋（bc 面） | 逆 DMI | ~28 K | 磁场翻转极化，经典 type-II |
| Ni$_3$V$_2$O$_8$ | 螺旋/正弦多相 | 逆 DMI | ~9 K | 多磁相变驱动 |
| 正交 HoMnO$_3$ | $E$-type 反铁磁 | 交换伸缩 | ~39 K | 大极化、强耦合 |
| MnWO$_4$ | 螺旋 | 逆 DMI | ~13 K | 手性可调 |
| CuO | 摆线 | 逆 DMI | ~230 K | 相对高温 type-II |

## 📚 相关论文 (Related Papers)

- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：系统阐述"磁的扭转产生铁电性"——螺旋磁序通过逆 DMI 诱导极化，确立 type-II 多铁的概念框架。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：梳理通向磁电耦合的不同机制路径（自旋-序致电极化、电荷/轨道序、界面与动态磁电效应等），对比各路径的强度与可行性。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-spiral|自旋螺旋]]：驱动铁电性的非共线磁序。
- [[../concepts/ferroelectricity|铁电性]]：被磁序诱导出的电极化序。
- [[../concepts/polarization-switching|极化翻转]]：磁-电耦合下的翻转行为。
- [[../concepts/chirality|手性]]：决定极化方向的螺旋手性。
- [[../concepts/skyrmion|斯格明子]]：由螺旋序拓扑化而来的相关织构。
- [[../concepts/magnetic-anisotropy|磁各向异性]]：约束螺旋取向与稳定性。
