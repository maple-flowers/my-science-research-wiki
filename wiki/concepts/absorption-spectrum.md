---
tags: [concept, photophysics, spectroscopy]
title: 吸收光谱 / Absorption Spectrum
type: concept
status: developing
domain: [spectroscopy, photophysics, analytical-chemistry]
mechanism: 分子吸收特定频率的光子，从低能态跃迁至高能态的过程
related_concepts: [photoluminescence, solvatochromism, extinction-coefficient, electronic-transition]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence]
updated: 2026-08
---

# 吸收光谱 / Absorption Spectrum

吸收光谱（Absorption Spectrum）是指当电磁辐射穿过某种物质时，由于该物质的选择性吸收而形成的频率或波长依赖的光强度分布。

## 👵 太奶导读

太奶啊，这就好比一个**“挑食的分子”**。这分子在阳光（各种颜色的光）底下待着，它并不是什么光都要，它只挑自己合胃口的颜色（波长）给吃进去（吸收）。咱们科学家就是拿一个仪器测一测，这阳光过去之后少了哪些颜色。少了的那些，就是被分子吃掉的“菜”。看它吃什么、吃多少，咱们就能知道这个分子的脾气秉性和内部结构。

## 🏗️ 物理实质

吸收光谱记录的是电子从基态 $S_0$ 到各个激发态（$S_1, S_2 \dots$）的垂直跃迁能：
*   **最低能吸收峰**：通常对应于第一电子激发态的零-零振动跃迁（$S_0 \to S_1$）。
*   **不敏感特性**：在许多 [[../concepts/ict-mechanism|分子内电荷转移 (ICT)]] 型探针中，吸收光谱对外部环境（如溶剂极性）表现出显著的**钝感性**。例如，探针 P1 的吸收峰在所有极性溶剂中均稳定在 401–419 nm 之间 [[../papers/Huang2019solvatochromic]]。

## 🧩 紫外-可见吸收光谱 (UV-Vis)

紫外-可见吸收光谱是研究有机分子电子结构最常用的手段。其核心公式为比尔-朗伯定律 (Beer-Lambert Law)：
$$ A = \epsilon c l $$
其中 $A$ 为吸光度，$\epsilon$ 为摩尔消光系数（衡量分子吸收能力的强弱），$c$ 为浓度，$l$ 为光程。

## 🔬 实验表征：吸收-发射分离

在研究环境敏感探针时，吸收光谱通常作为发射光谱的对照：
*   如果吸收光谱位置不变而发射光谱大幅红移，则证明发光起源于具有巨大偶极矩差异的激发态过程（如 [[../concepts/tict-mechanism|TICT]]）。
*   **P1 探针案例**：通过吸收谱的恒定，排除了基态溶剂化作用的可能，从而确证了其巨大的 [[../concepts/stokes-shift|斯托克斯位移]] 完全源于激发态的能量弛豫 [[../papers/Huang2023two]]。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：提供了 P1 探针在 10 种不同极性溶剂中的归一化吸收光谱。
- [[../papers/Huang2019solvatochromic]]：对比了二甲氨基和二苯氨基衍生物在吸收谱特性上的异同。
- [[../papers/H2017fluorescence]]：利用吸收光谱的稳定性作为论证 ICT 机制的关键依据。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/photoluminescence|光致发光]]
- [[../concepts/solvatochromism|溶剂化显色]]
- [[../concepts/stokes-shift|斯托克斯位移]]
- [[../concepts/ict-mechanism|ICT 机制]]
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]
