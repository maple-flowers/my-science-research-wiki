---
tags: [concept, topological-physics, mathematics]
title: 贝里曲率 / Berry Curvature
type: concept
status: mature
year: 2019
domain: [condensed-matter-physics, topological-physics]
mechanism: 动量空间中布洛赫波函数相位演化产生的有效几何场，对电子施加强度与贝里曲率成正比的横向力
related_concepts: [berry-phase, anomalous-hall-effect, topological-charge, chern-number, weyl-semimetal, fermi-arc, quantum-anomalous-hall-effect, spin-texture, topological-insulator]
papers: [sharmaRoomtemperatureFerroelectricSemimetal2019, wangTunableD0Topological2025b, hanPolarTopologicalMaterials2025]
updated: 2026-08-19
---

# 贝里曲率 / Berry Curvature

贝里曲率 (Berry Curvature, $\Omega$) 是动量空间中波函数几何相位（贝里相位）的微分表现形式。它可以类比为动量空间中的"磁场"，会对电子的运动产生类似于洛伦兹力的效果，从而导致反常输运现象，如反常霍尔效应 (AHE)。

## 👵 太奶导读

好孩子，这"贝里曲率"听着像洋人的名字，其实它描述的是一种"看不见的转弯力"。
想象你在一个凹凸不平的操场上跑（这就是动量空间），虽然你觉得自己是走直线，但因为地是弯的，你总会不由自主地往一边斜（这就是贝里曲率在推你）。
在微观世界里，电子跑的时候，它的波函数会随着位置变来变去，产生一种"相位"。这个相位就像是电子带的导航仪，如果导航仪本身是弯曲的，电子就会感受到一股劲儿把它推向旁边。这就好比你在旋转木马上想走直线，总会觉得被一股力甩开一样。外尔半金属里的那些"出水口"和"入水口"，其实就是这股"转弯力"最强的地方。

## 🏗️ 结构概览

贝里曲率在布里渊区中的分布决定了体系的拓扑不变量。

![图：贝里曲率在动量空间的分布示意](../../raw/figures/sharmaRoomtemperatureFerroelectricSemimetal2019/fig_4_F86EWZ63.png)
*   **看图要点**：图中展示了 WTe₂ 能带交叉处附近贝里曲率的显著增强。
*   **来源**：[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]

## 🧩 核心机制：几何相位如何变成横向力

### 1. 数学定义

$$\Omega_n(k) = \nabla_k \times \langle u_n(k) | i \nabla_k | u_n(k) \rangle$$

贝里曲率 $\Omega_n(k)$ 是第 $n$ 个能带在动量空间 $k$ 处的有效"磁场"，由布洛赫波函数 $u_n(k)$ 的相位变化决定。

### 2. 反常速度与横向输运

受贝里曲率影响，电子的运动方程增加一项反常速度：
$$\dot{r} = \frac{1}{\hbar} \frac{\partial \epsilon_n(k)}{\partial k} + \dot{k} \times \Omega_n(k)$$

这一项垂直于电场与磁场方向，产生与洛伦兹力类似的横向偏转，是反常霍尔效应的微观起源。

### 3. 拓扑联系

- **陈数**：贝里曲率在整个布里渊区的积分即为陈数 (Chern Number)，是一个整数量子化的拓扑不变量。
- **外尔点**：在拓扑半金属中外尔点是贝里曲率的单极子（源/汇），手性对应拓扑荷 $\pm 1$。
- **对称性约束**：空间反演与时间反演对称性共同保护下 $\Omega(-k)=-\Omega(k)$ 可对称性抵消；打破其一即可获得净贝里曲率。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| $\Omega_n(k)$ | 动量空间有效磁场 | 单位：面积（Å² 量级） |
| 反常速度 | 贝里曲率诱导的横向速度 | $\dot{k} \times \Omega$ |
| 陈数 $C$ | 全布里渊区积分 | 整数（拓扑不变量） |
| 手性 | 外尔点单极子荷 | $\pm 1$ |
| 对称性 | 非零条件 | 破缺反演或时间反演之一 |

## 🔀 近邻概念辨析

- **贝里曲率 vs 贝里相位**：贝里相位是闭合路径上的积分相位（标量、可整体规范变换），贝里曲率是其局域微分（矢量场、规范不变），类似"矢势 vs 磁场"的关系。
- **贝里曲率 vs 陈数**：贝里曲率是局域几何场，陈数是其在闭合流形上的积分（全局拓扑量）。

## 📚 相关论文 (Related Papers)

- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：利用 Berry phase 方法计算 WTe₂ 的总极化，关联铁电与拓扑。
- [[../papers/wangTunableD0Topological2025b]]：研究 Berry 曲率在 d0 磁性体系中对拓扑磁态的作用。
- [[../papers/hanPolarTopologicalMaterials2025]]：极性拓扑结构中的相位贡献与器件设计。

## 🔗 关联概念与实体 (Related)

- [[../concepts/berry-phase|berry-phase]]
- [[../concepts/anomalous-hall-effect|anomalous-hall-effect]]
- [[../concepts/topological-charge|topological-charge]]
- [[../concepts/chern-number|chern-number]]
- [[../concepts/weyl-semimetal|weyl-semimetal]]
- [[../concepts/fermi-arc|fermi-arc]]
- [[../concepts/quantum-anomalous-hall-effect|quantum-anomalous-hall-effect]]
- [[../concepts/spin-texture|spin-texture]]
- [[../concepts/topological-insulator|topological-insulator]]
- [[../entities/WTe2|WTe2]]
- [[../entities/VASP|VASP]]
