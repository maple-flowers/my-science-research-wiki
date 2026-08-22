---
tags: [concept, ferroelectricity]
title: 铁电畴 / Ferroelectric Domain
type: concept
status: mature
domain: [condensed-matter-physics, ferroelectricity]
mechanism: 晶体内部具有相同自发极化取向的微观连续区域
related_concepts: [domain-wall, polarization-switching, domain-wall-nucleation]
papers: [Chen2016electrical, wuSlidingFerroelectricity2D2021a, huangPolarPhaseDomain2019, cuiIntercorrelatedInplaneOutofplane2018a, houStrainbasedRoomtemperatureNonvolatile2019, sattarFunctionalizedDoubleTransition2025, shenEmergenceMultipleFerroelectric2025]
updated: 2026-08
---

# 铁电畴 / Ferroelectric Domain

铁电畴是指在铁电晶体内部，自发极化矢量 $\mathbf{P}_s$ 指向完全一致的微观区域。为了降低体系的总自由能（包括静电能和弹性能），铁电体通常不会以整体单畴的形式存在，而是自发分裂为多个取向不同的铁电畴阵列。

## 👵 太奶导读

太奶啊，您就把这铁电畴想象成咱村里分的地。
虽然整块地都是种庄稼的（都是同一种材料），但为了方便打理，大家把地分成了好多个小方块。有的地块，禾苗（自发极化小箭头）全是往东倒的；隔壁那一块，禾苗就全是往西倒的。
每一个箭头方向都整整齐齐的小地块，就叫一个“铁电畴”。
而地块与地块之间那一层窄窄的田埂，就是科学家们最爱研究的“畴壁”。我们给这块地通个电（施加电场），那些箭头就会像变戏法一样，原本往东指的也跟着往西掉头，这就叫极化翻转，咱们现在的电脑硬盘存数据，靠的就是这手变戏法的本事。

## 🏗️ 结构概览：多向铁电畴取向

在具有复杂对称性的晶体中，铁电畴的取向种类繁多。

![图：BiFeO₃ 晶胞中沿四条体对角线的 8 种铁电畴极化方向示意](../../raw/figures/Chen2016electrical/fig_1_ZZASGZCF.png)
*   **看图要点**：图中展示了菱方相 BiFeO₃ 的典型畴取向。极化矢量 $P$ 可以指向立方体的 8 个顶点（$P_1$ 到 $P_4$ 向上，$P_{-1}$ 到 $P_{-4}$ 向下）。这种多取向特性导致了 71°、109° 和 180° 等不同类型的畴壁能量差异。
*   **来源**：[[../papers/Chen2016electrical]] -> [[../figures/domain-walls-structures|畴结构与畴壁]]

## 🧩 动力学特性：畴翻转路径

*   **畴壁成核 (Nucleation)**：当外加驱动力（电场或机械力）达到阈值时，新畴通常优先在原有的畴壁、台阶或缺陷处产生种子。
*   **畴壁运动 (Domain Wall Motion)**：极化的反转通常不是整体瞬间完成的，而是通过畴壁的横向扩展来“吞并”旧畴。
*   **两步翻转 (Two-step Switching)**：在某些体系（如 BiFeO₃）中，180° 的直接极化翻转往往被分解为两步连续的铁弹翻转（例如 $71^\circ + 109^\circ$），以降低路径上的能量势垒。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 畴取向种类 | 极化方向 | 与晶体对称性相关 |
| 畴壁类型 | 取向差 | 71° / 109° / 180° |
| 翻转路径 | 动力学机制 | 成核-畴壁运动-两步翻转 |
| 畴尺寸 | 特征尺度 | 受 Kittel 定律约束 |
| 调控手段 | 电场/应力/温度 | 决定开关与存储 |

## 🔀 近邻概念辨析

- **铁电畴 vs 畴壁**：畴是均匀极化区，畴壁是畴间过渡界面；畴壁本身可承载导电等新奇性质。
- **铁电畴 vs 铁弹畴**：铁电畴由极化取向区分，铁弹畴由应变取向区分；二者常耦合共存。
- **铁电畴 vs 磁畴**：铁电畴靠极化序，磁畴靠磁化序；动力学机制类似（成核-畴壁运动）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 畴取向种类 | 极化方向 | 与晶体对称性相关 |
| 畴壁类型 | 取向差 | 71° / 109° / 180° |
| 翻转路径 | 动力学机制 | 成核-畴壁运动-两步翻转 |
| 畴尺寸 | 特征尺度 | 受 Kittel 定律约束 |
| 调控手段 | 电场/应力/温度 | 决定开关与存储 |

## 🔀 近邻概念辨析

- **铁电畴 vs 畴壁**：畴是均匀极化区，畴壁是畴间过渡界面；畴壁本身可承载导电等新奇性质。
- **铁电畴 vs 铁弹畴**：铁电畴由极化取向区分，铁弹畴由应变取向区分；二者常耦合共存。
- **铁电畴 vs 磁畴**：铁电畴靠极化序，磁畴靠磁化序；动力学机制类似（成核-畴壁运动）。

## 📚 相关论文 (Related Papers) Papers)

- [[../papers/Chen2016electrical]]：详细原位观测了 70 nm BiFeO₃ 薄膜中铁电畴在电场和针尖力作用下的成核、分解与重组演化。
- [[../papers/huangPolarPhaseDomain2019]]：讨论了极性相中畴结构的稳定性及其对物性的影响。
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]
- [[../papers/wuSlidingFerroelectricity2D2021a]]
- [[../papers/houStrainbasedRoomtemperatureNonvolatile2019]]
- [[../papers/sattarFunctionalizedDoubleTransition2025]]
- [[../papers/shenEmergenceMultipleFerroelectric2025]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/domain-wall|畴壁]]（界面层）
- [[../concepts/polarization-switching|极化翻转]]
- [[../concepts/ferroelasticity|铁弹性]]（应变耦合畴）
- [[../entities/BiFeO3|铁酸铋 (BiFeO₃)]]
