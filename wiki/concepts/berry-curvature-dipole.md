---
tags: [concept, 2D-materials, berry-phase, nonlinear-transport, quantum-geometry]
title: 贝里曲率偶极 / Berry Curvature Dipole (BCD)
type: concept
status: mature
year: 2015
domain: [condensed-matter-physics, topological-physics, nonlinear-transport]
mechanism: 反演破缺体系中贝里曲率在费米面附近的不对称分布诱导二阶非线性霍尔电流
related_concepts: [berry-curvature, nonlinear-hall-effect, inversion-symmetry, time-reversal-symmetry]
papers: [wuSlidingFerroelectricity2D2021a, liPhaseTransitions2D2021]
updated: 2026-08
---

# 贝里曲率偶极 / Berry Curvature Dipole (BCD)

贝里曲率偶极 (Berry Curvature Dipole, BCD) 指**贝里曲率在费米面附近动量空间的偶极矩分布 $D_{ab} = \sum_n \int_k f_n \partial_{k_a}\Omega_{n,b}$**，是反演对称破缺体系中产生二阶非线性霍尔效应（NLHE）的微观机制。其核心物理是：当体系同时满足时间反演破缺（或借助外场）与反演破缺时，费米面附近的贝里曲率分布不再中心对称，从而对外加电场产生与 $E^2$ 成正比的横向电流。

## 👵 太奶导读

乖孙，一般霍尔效应要磁场，反常霍尔效应要磁性材料。那如果既没有磁场、材料又不是磁的，还有没有别的"霍尔"？有！这就是"贝里曲率偶极"的本事。
贝里曲率可以理解成电子在能带里"自带转弯的脾气"。如果材料里"转弯的能力"左右不对称（叫反演对称破缺），那么电子流过去的时候，往左转的和往右转的就不一样多了——这种"不对称的转弯能力"在动量空间里的分布，就是"偶极"。有了它，即便材料不磁、不加磁场，一通大电流也能冒出横向电压，而且电压跟电流的平方成正比，非常特别。

## 🏗️ 结构概览

贝里曲率偶极属于量子几何非线性输运家族。线性霍尔效应 ∝ 贝里曲率总和（需磁序）；非线性霍尔效应 ∝ 贝里曲率偶极（需反演破缺）。BCD 的物理根源是贝里曲率随动量变化的梯度，它只在同时具备时间反演与反演破坏（或借助打破时间反演的外场）的体系中非零。二维低对称材料、滑移铁电体、莫尔体系因天然具备反演破缺与高可调性，是 BCD 探测的活跃平台。

## 🧩 核心内容与机制 (Core Content)

- **定义**：贝里曲率偶极张量
  $$D_{ab} = \sum_n \int \frac{d^dk}{(2\pi)^d} f_n(k)\, \partial_{k_a}\Omega_{n,b}(k)$$
  其中 $f_n$ 为费米分布，$\Omega_{n,b}$ 为第 $n$ 条带的贝里曲率 $b$ 分量。
- **非线性霍尔电流**：在外加电场 $\mathbf{E}$ 下，BCD 诱导的二阶横向电流
  $$j_a = e\tau\,\epsilon_{abc}\, D_{bd}\, E_c E_d$$
  电流正比于 $E^2$，且与散射时间 $\tau$ 有关，可通过对电场频率/温度依赖的测量与常规线性霍尔区分。
- **对称性要求**：非线性霍尔效应需要反演对称破缺；当体系有时间反演对称时，还需借助外磁场/磁序打破时间反演。磁性二维体系与反演破缺的二维材料是理想载体。
- **滑移铁电中的表现**：层状二维材料层间滑移可产生可切换的电极化与反演破缺，为调控贝里曲率偶极与非线性输运提供新自由度（[[../papers/wuSlidingFerroelectricity2D2021a|Wu 2021]]）；二维相变的多样性与相变工程则提供了在低对称相中实现显著 BCD 的平台（[[../papers/liPhaseTransitions2D2021|Li 2021]]）。

## 📋 关键参数表

| 参数 | 含义 | 特征 |
|---|---|---|
| 偶极张量 $D_{ab}$ | 贝里曲率动量分布 | 需反演破缺非零 |
| 非线性电流 $j_a$ | 二阶响应 | ∝ $E^2$、∝ $\tau$ |
| 对称性要求 | 反演破缺 | 时间反演可破缺（磁） |
| 探测手段 | 二次谐波输运 | 温度/频率依赖区分 |

## 🔀 近邻概念辨析

- **BCD vs 线性反常霍尔效应**：AHE 需要净贝里曲率（磁序、时间反演破缺），BCD 需要贝里曲率动量分布不对称（反演破缺）——两者可共存，机制独立。
- **BCD vs 贝里曲率本身**：贝里曲率是局域几何量（规范不变标量场）；BCD 是其动量梯度在费米面的统计矩，需体系不对称。

## 📚 相关论文 (Related Papers)

- [[../papers/wuSlidingFerroelectricity2D2021a]] — 滑动铁电体中滑移可调控电极化与反演破缺，为 BCD 调控提供平台。
- [[../papers/liPhaseTransitions2D2021]] — 二维相变与相变工程提供低对称相实现显著贝里曲率偶极的体系。

## 🔗 关联概念与实体 (Related)

- [[../concepts/berry-curvature|贝里曲率]]：偶极的原函数。
- [[../concepts/nonlinear-hall-effect|非线性霍尔效应]]：BCD 的直接物理表现。
- [[../concepts/inversion-symmetry|反演对称]]：其破缺是 BCD 非零的必要条件。
- [[../concepts/berry-phase|贝里相位]]：量子几何的相位根源。
- [[../concepts/sliding-ferroelectricity|滑动铁电]]：调控反演破缺的二维机制。
- [[../entities/TMDs|TMDs]]：低对称二维平台。
- [[../entities/WSe2|WSe₂]]：二维非线性输运研究体系。
