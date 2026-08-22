---
tags: [concept, photophysics, excited-state]
title: 激基复合物 / Exciplex
type: concept
status: developing
domain: [photophysics, physical-chemistry, molecular-spectroscopy]
mechanism: 一个处于激发态的分子与另一个处于基态的分子相互作用，形成一个在激发态稳定、基态不稳定的二聚复合物
related_concepts: [photoluminescence, tict-mechanism, quenching]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence, WRZYSZCZYNSKI2010initiators, Xie2024isostructural]
updated: 2026-08
---

# 激基复合物 / Exciplex

激基复合物（Exciplex，即 Excited Complex 的缩写）是指一种特殊的分子间复合物。它由一个处于激发态的分子（$M^*$）与另一个处于基态的不同分子（$A$，或者相同分子的另一个基态实体）通过电荷转移等作用力在激发态缔合而成。该复合物仅在激发态稳定存在，一旦退激发释放光子，便会解离为两个独立的基态分子。

## 👵 太奶导读

太奶啊，这就好比是**“临时搭伙儿”**。这分子在一个人安安静静待着（基态）的时候，对邻居爱答不理的。可一旦其中一个分子受了光照（受激态），它就突然变得特别热情，拉着旁边一个没受激的基态邻居的手，俩人“临时搭伙”（形成激基复合物）过日子。这一搭伙，俩人分担能量，发出来的光就变成了一种特别深、特别温暖的颜色。等这股光发出去（退激发）之后，俩人就立刻松开手，继续各过各的，互不相干。

## 🏗️ 物理特征与光谱指纹

由于激基复合物在基态是不稳定的（无化学键结合，排斥势能），其发光具有以下独特性质：
*   **无结构的宽带发射**：由于基态没有稳定的势阱，其辐射跃迁对应的基态能级是连续的。这导致激基复合物的发光光谱（E 带）通常是非常对称、没有精细结构的宽带。
*   **显著的红移**：相比于单体发光，激基复合物的发光通常位于明显更长波长（低能量）的区域。
*   **浓度与粘度敏感性**：激基复合物的形成极其依赖于分子间的扩散碰撞：
    *   **浓度依赖**：浓度越高，分子间碰撞概率越大，Exciplex 信号越强 [[../papers/Huang2019solvatochromic]]。
    *   **粘度阻碍**：在极高粘度（如纯甘油）中，由于扩散运动被冻结，Exciplex 发光会完全消失。

## 🧩 双光子激发三重荧光

在高性能探针 P1 的光物理研究中，科学家首次在双光子激发（790 nm）下观察到了由 **LE（单体局域激发）、TICT（单体扭曲电荷转移）和 Exciplex（分子间激基复合物，~542 nm）** 共同构成的“三重荧光”现象 [[../papers/Huang2023two]]。
*   这一现象之所以在单光子下不明显，是因为双光子激发的紧密焦点处具有极高的局部激发态浓度，极大地加速了分子间 Exciplex 的缔合过程 [[../papers/H2017fluorescence]]。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：报道了双光子特异性激基复合物三重发光的机制。
- [[../papers/Huang2019solvatochromic]]：通过变浓度和变粘度实验，确立了位于 542 nm 处 E 带的 Exciplex 归属。
- [[../papers/H2017fluorescence]]：探讨了溶剂弛豫对激基复合物形成动力学的影响。
- [[../papers/WRZYSZCZYNSKI2010initiators]]
- [[../papers/Xie2024isostructural]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/photoluminescence|光致发光]]
- [[../concepts/tict-mechanism|TICT 机制]]
- [[../concepts/locally-excited-state|局域激发态 (LE)]]
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]
