---
tags: [concept, nonlinear-transport, berry-phase, topological-physics, polar-metals, 2D-materials]
title: 非线性霍尔效应 / Nonlinear Hall Effect
type: concept
status: mature
year: 2023
domain: [condensed-matter-physics, nonlinear-transport, topological-physics]
mechanism: 动量空间中贝里曲率偶极子或高阶几何量对电场的一阶响应，产生与电流方向/极化解耦的二阶或三阶横向电压
related_concepts: [hall-effect, berry-curvature, berry-curvature-dipole, anomalous-hall-effect, nonlinear-transport, polar-metals, symmetry-breaking, spin-texture, third-order-nonlinearity]
papers: [bhowalPolarMetalsPrinciples2023b]
updated: 2026-08-19
---

# 非线性霍尔效应 / Nonlinear Hall Effect

非线性霍尔效应 (Nonlinear Hall Effect, NLHE) 指横向（霍尔）响应与外加电场呈非线性（通常二阶）关系的一类输运现象。其核心微观机制是动量空间中的贝里曲率偶极子 (Berry curvature dipole)：当体系破坏时间反演或空间反演对称性、且贝里曲率在费米面附近不均匀分布时，纵向电流会诱导一个与电流方向相关的横向电压，无需外加磁场即可出现。

## 👵 太奶导读

乖孙，普通霍尔效应是在磁场下电子被"拐弯"产生横向电压；而"非线性霍尔效应"更邪门——不用磁场，光靠"电流本身"就能让电子自己往旁边偏。原因是材料的"动量空间"不是平的，有些地方"弯"得厉害（贝里曲率大），电子在这些地方会不由自主地偏转，而且这种偏转跟你电流的方向有关：电流反着流，偏转跟着反，这就是"非线性"。一句话：**"不用磁场，电流自己就能把电子掰弯"**。

## 🏗️ 结构概览

非线性霍尔效应把"贝里曲率"这一几何量转化为可测量的直流/整流信号。

![图：极性材料中电子结构与非对称输运响应示意](../../raw/figures/bhowalPolarMetalsPrinciples2023b/fig_4_BAD5B403.png)
*   **看图要点**：展示了极性异质结构中对称性破缺与输运响应的关系。
*   **来源**：[[../papers/bhowalPolarMetalsPrinciples2023b]]

## 🧩 核心机制：贝里曲率偶极子

### 1. 二阶非线性霍尔电流

在时间反演对称性破缺（磁性）或空间反演对称性破缺（极性）体系中，贝里曲率 $\Omega(\boldsymbol{k})$ 在动量空间的分布可形成非零偶极矩 $D_{ab} = \sum_n \int_k f_n \partial_{k_a}\Omega^b_n$。在纵向电场 $E_a$ 驱动下产生横向电流 $j_b \propto D_{ab} E_a^2$，即二阶非线性霍尔效应。

### 2. 对称性约束

- 需要破缺空间反演或时间反演至少其一；
- 偶极矩的方向由晶体对称性决定，极性金属/铁电材料中极化方向直接控制偶极子取向，从而可实现"电控非线性霍尔"。

### 3. 高阶与延伸效应

二阶以上（如三阶）非线性霍尔由更高的几何量（四极子）驱动，可在对称性要求更宽松的体系中出现；非线性霍尔电流可用于太赫兹整流、频率转换与对称性/拓扑探测。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 贝里曲率偶极子 $D$ | 非线性霍尔序参量 | 依赖费米面附近 $\Omega$ 分布 |
| 响应阶数 | 电流-电场关系 | 二阶（主要）/ 三阶 |
| 对称性 | 出现条件 | 破缺反演或时间反演 |
| 外场 | 驱动 | 无需磁场 |
| 应用 | 器件功能 | 整流、太赫兹探测、拓扑表征 |

## 🔀 近邻概念辨析

- **非线性霍尔 vs 线性（反常）霍尔**：反常霍尔效应是电场一阶、需贝里曲率净积分（陈数/磁化）；非线性霍尔是电场二阶、只需贝里曲率偶极子，可在无磁化体系中出现。
- **非线性霍尔 vs 磁电阻整流**：磁电阻整流来自电阻随电流的非线性（焦耳热/接触效应）；非线性霍尔来自几何相位，方向由对称性决定、具有确定的角依赖。

## 📚 相关论文 (Related Papers)

- [[../papers/bhowalPolarMetalsPrinciples2023b]]：讨论极性金属平台中对称性破缺如何产生贝里曲率偶极子与非线性霍尔等非线性输运。

## 🔗 关联概念与实体 (Related)

- [[../concepts/hall-effect|hall-effect]]
- [[../concepts/berry-curvature|berry-curvature]]
- [[../concepts/berry-curvature-dipole|berry-curvature-dipole]]
- [[../concepts/anomalous-hall-effect|anomalous-hall-effect]]
- [[../concepts/polar-metal|polar-metal]]
- [[../concepts/spin-texture|spin-texture]]
- [[../entities/WTe2|WTe2]]
- [[../entities/TMDs|TMDs]]
