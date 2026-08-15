---
tags: [entity, material, TMD, 2D, semiconductor]
title: 二硫化钨 (WS2) / Tungsten Disulfide
type: entity
status: mature
formula: WS2
stoichiometry: 2H
class: [TMD, vdW, semiconductor]
properties: [spin-orbit-coupling, exciton-effect]
related_entities: [MoS2, WS2, 2h-phase]
papers: [liPhaseTransitions2D2021, RecentAdvancesGrowth2025, FerroelectricityMultiferroicityAtomic2023, Li2013bonding, liuSpintronicsTwoDimensionalMaterials2020b, sunSlidingFerroelectricityTwodimensional2025]
updated: 2026-08
---

# 二硫化钨 (WS2) / Tungsten Disulfide

二硫化钨 (WS2) 是一种与 MoS2 结构类似，但拥有更强**自旋-轨道耦合 (SOC)** 的过渡金属硫族化合物。这使得它在能谷电子学 (Valleytronics) 和自旋电子学 (Spintronics) 的应用中展现出更加显著和宽温区的物理效应。

## 奶奶导读

太奶啊，这 WS2 就像是 MoS2 的“升级加强版大表哥”。它也有着极薄的发光片状结构，但是因为里面换成了更重、更稳沉的钨 (W) 原子，它的自旋-轨道耦合效应（也就是电子转动和它轨道运动的绑定力量）要强得多。这使得它的电子能量坑（能谷）分得更开，在里面跑动的电子方向感更强，能更好地被光和电来指挥，非常适合用来做那种精密的量子光电开关。

## 🏗️ 结构概览

WS2 常见的最稳定结构为 2H 相（三棱柱配位，属于空间群 $P6_3/mmc$）。

![图：2D 过渡金属硫族化合物晶格结构](../../raw/figures/RecentAdvancesGrowth2025/fig_1_NDNYXQ2A.png)
*   **看图要点**：图中展示了 WS2 单层的高分辨晶格结构和范德华异质结堆垛方式。W 原子和 S 原子呈完美的六角蜂窝状排布。
*   **来源**：[[../papers/RecentAdvancesGrowth2025]] -> [[../figures/crystal-structures-bulk|晶体结构]]

## 🧩 强自旋-轨道劈裂与能谷物理

由于 W 原子的强相对论效应，WS2 展现出极其显著的能带特征：

*   **自旋-轨道劈裂 (SOC splitting)**：在价带顶（$K$ 点），其自旋轨道耦合导致的能带劈裂可达 $\sim 400\text{ meV}$，远大于 MoS2 的 $\sim 150\text{ meV}$。这能有效防止自旋散射，提高了能谷偏振的稳定性。
*   **异质结构建**：WS2 常与 MoS2 或石墨烯结合构建范德华异质结，利用其极高的光子吸收截面和超快的电荷转移特性开发高响应度的光电探测器。

## 🔬 物理参数表

| 属性 | 数值 (单层) |
| :--- | :--- |
| 带隙 (Bandgap) | $\sim 2.1\text{ eV}$ (直接) |
| 价带顶 SOC 劈裂量 | $\sim 400\text{ meV}$ |
| 激子结合能 | $\sim 0.32\text{ eV}$ |

## 📚 相关论文 (Related Papers)

- [[../papers/RecentAdvancesGrowth2025]]：讨论了高结晶性单层 WS2 薄膜的化学气相沉积 (CVD) 生长动力学。
- [[../papers/liPhaseTransitions2D2021]]：归纳了 WS2 所在 TMD 家族在二维尺度下的普遍相变与对称性破缺。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]
- [[../papers/Li2013bonding]]
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-orbit-coupling|自旋-轨道耦合 (SOC)]]
- [[../entities/MoS2|二硫化钼 (MoS2)]]
- [[../entities/2h-phase|2H 相]]
