---
tags: [concept, topological-physics, mathematics]
title: 贝里曲率 / Berry Curvature
type: concept
status: developing
domain: [condensed-matter-physics, topological-physics]
mechanism: 动量空间中布洛赫波函数相位演化产生的有效几何场
related_concepts: [berry-phase, anomalous-hall-effect, topological-charge, chern-number, weyl-semimetal]
papers: [sharmaRoomtemperatureFerroelectricSemimetal2019, wangTunableD0Topological2025b, hanPolarTopologicalMaterials2025]
updated: 2026-08
---

# 贝里曲率 / Berry Curvature

贝里曲率 (Berry Curvature, $\Omega$) 是动量空间中波函数几何相位（贝里相位）的微分表现形式。它可以类比为动量空间中的“磁场”，会对电子的运动产生类似于劳伦兹力的效应，从而导致反常输运现象，如反常霍尔效应 (AHE)。

## 👵 太奶导读

好孩子，这“贝里曲率”听着像洋人的名字，其实它描述的是一种“看不见的转弯力”。
想象你在一个凹凸不平的操场上跑（这就是动量空间），虽然你觉得自己是走直线，但因为地是弯的，你总会不由自主地往一边斜（这就是贝里曲率在推你）。
在微观世界里，电子跑的时候，它的波函数会随着位置变来变去，产生一种“相位”。这个相位就像是电子带的导航仪，如果导航仪本身是弯曲的，电子就会感受到一股劲儿把它推向旁边。这就好比你在旋转木马上想走直线，总会觉得被一股力甩开一样。外尔半金属里的那些“出水口”和“入水口”，其实就是这股“转弯力”最强的地方。

## 🏗️ 结构概览

贝里曲率在布里渊区中的分布决定了体系的拓扑不变量。

![图：贝里曲率在动量空间的分布示意](../../raw/figures/sharmaRoomtemperatureFerroelectricSemimetal2019/fig_4_F86EWZ63.png)
*   **看图要点**：图中展示了 WTe₂ 能带交叉处附近贝里曲率的显著增强。
*   **来源**：[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]

## 🧩 物理效应与数学定义

*   **定义**：$\Omega_n(k) = \nabla_k \times \langle u_n(k) | i \nabla_k | u_n(k) \rangle$。
*   **反常速度**：受贝里曲率影响，电子的运动速度增加了一项 $\dot{r} = \frac{1}{\hbar} \frac{\partial \epsilon_n(k)}{\partial k} + \dot{k} \times \Omega_n(k)$。
*   **拓扑联系**：贝里曲率在整个布里渊区的积分即为陈数 (Chern Number)，是一个拓扑不变量。

## 📚 相关论文 (Related Papers)

- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：利用 Berry phase 方法计算 WTe₂ 的总极化。
- [[../papers/wangTunableD0Topological2025b]]：研究了 Berry 相位在 d0 磁性体系中的作用。
- [[../papers/hanPolarTopologicalMaterials2025]]：极性拓扑结构中的相位贡献。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/berry-phase|贝里相位]]（曲率的积分形式）
- [[../concepts/anomalous-hall-effect|反常霍尔效应]]（最直接的观测效应）
- [[../concepts/chern-number|陈数]]（全局拓扑指标）
- [[../concepts/weyl-semimetal|外尔半金属]]（贝里曲率的单极子源）
