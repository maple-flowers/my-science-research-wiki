---
tags: [concept, computational-physics, vasp, dft]
title: Monkhorst-Pack Grid / Monkhorst-Pack 网格
type: concept
status: mature
domain: [computational-physics, electronic-structure]
mechanism: 通过均匀划分布里渊区，生成一组特殊的 k 点集，用于数值积分计算电荷密度和总能量。
related_concepts: [plane-wave-basis, self-consistent-field-cycle, methfessel-paxton-smearing]
papers: [monkhorstSpecialPointsBrillouinzone1976, kresseEfficiencyAbinitioTotal1996a]
updated: 2026-08
---

# Monkhorst-Pack 网格 / Monkhorst-Pack Grid

Monkhorst-Pack (MP) 网格是第一性原理计算中布里渊区积分的工业标准。它通过在倒空间建立均匀的采样点集，利用晶体对称性极大地减少了计算开销，同时保证了数值积分的高精度。

## 👵 太奶导读

太奶，这倒空间里的布里渊区就像是咱们的一个大菜园子。咱们想算算这园子里一共结了多少果子（这就是求总能量或者电荷密度的积分），如果一个坑一个坑地数（连续积分），那这辈子也数不完。

Monkhorst-Pack 网格就像是在菜园子里均匀地插了一排排的小旗子（k 点采样）。太奶只需要数数旗子底下的果子是多少，然后把它们加起来求个平均，就能八九不离十地算出整个菜园子的产额了。而且啊，这法子特别聪明，如果菜园子是对称的，有些旗子底下的情况肯定是一模一样的，太奶只要数一个点，然后给它多算几份功劳（这叫对称性权重），活儿一下子就轻省了！

## 🏗️ 结构概览

在 VASP 中，k 点采样是在 KPOINTS 文件中定义的。

![图：不同体系下 k 点采样的收敛性基准](../../raw/figures/kresseEfficiencyAbinitioTotal1996a/fig_2_K2M97DMS.png)
*   注：此处使用图2展示收敛性。
*   **看图要点**：图中展示了总能量随 k 点密度的变化。可以看到，当网格增加到一定程度（如 6x6x6 或 8x8x8）后，能量趋于平稳，这标志着计算达到了“k 点收敛”。
*   **来源**：[[../papers/kresseEfficiencyAbinitioTotal1996a]] -> [[../figures/mathematical-models-computational|计算方法与泛函]]

## 🧩 数学与算法逻辑

### 1. 均匀采样与定义
Monkhorst-Pack 网格将布里渊区在三个倒格矢方向上分别进行 $q$ 等分。其生成的波矢点集可表示为：
$$ \mathbf{k}_{prs} = u_p \mathbf{b}_1 + u_r \mathbf{b}_2 + u_s \mathbf{b}_3 $$
其中 $u_p$ 是均匀间隔的数值（例如对于 $q$ 个点，取 $u_p = (2p - q - 1)/(2q)$，其中 $p = 1, \dots, q$）。

### 2. 对称性约化 (Symmetry Reduction)
在实际计算中，不需要在所有 $q^3$ 个点上进行计算。利用晶体的空间群对称性（如旋转、镜像），许多 k 点在物理上是等效的。MP 方法会自动寻找这些等效点，仅在**不可约楔形区 (Irreducible Wedge)** 内进行采样，并为每个独立点赋予相应的权重。这能将计算量降低数十倍。

### 3. 奇数 vs 偶数网格 (Odd vs Even Grids)
- **奇数网格**（如 3x3x3）：中心通常包含布里渊区的原点（$\Gamma$ 点）。这对于具有 $\Gamma$ 点物理特性的半导体非常重要。
- **偶数网格**（如 4x4x4）：中心偏离原点。Monkhorst 和 Pack 在原论文中证明，偶数网格通常比同规模的奇数网格具有更好的积分误差抵消效果，尤其是在立方晶系中。

## 📚 相关论文 (Related Papers)

- [[../papers/monkhorstSpecialPointsBrillouinzone1976]]：Monkhorst-Pack 方法的奠基之作，系统论述了网格生成与正交性。
- [[../papers/kresseEfficiencyAbinitioTotal1996a]]：讨论了 MP 网格在金属体系中与展宽技术（Smearing）的协同收敛问题。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[methfessel-paxton-smearing|MP 展宽]]：处理金属费米面采样不连续问题的必备搭档。
- [[plane-wave-basis|平面波基组]]：平面波计算的“精度三基石”之一（另外两个是截断能和赝势）。
- VASP (entity)：KPOINTS 文件是用户与 MP 网格交互的主战场。
