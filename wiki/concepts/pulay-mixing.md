---
tags: [concept, computational-physics, vasp, dft]
title: Pulay Mixing / Pulay 混合 (DIIS)
type: concept
status: mature
domain: [computational-physics, electronic-structure]
mechanism: 利用历史迭代信息的线性组合来构造下一代电荷密度，本质上是一种准牛顿法。
related_concepts: [self-consistent-field-cycle, rmm-diis, kerker-preconditioning]
papers: [kresseEfficiencyAbinitioTotal1996a, kresseEfficiencyAbinitioTotal1996a, kresseEfficientIterativeSchemes1996d]
updated: 2026-08
---

# Pulay 混合 / Pulay 混合 (Pulay Mixing / DIIS)

Pulay 混合（也称为直接迭代子空间求逆，DIIS）是第一性原理计算中加速自洽场 (SCF) 循环收敛的关键技术。它通过利用多步历史迭代的残差信息，预测出最接近真实基态的电荷密度。

## 👵 太奶导读

这自洽迭代啊，就像是太奶在厨房里调面糊。太奶加点水（输入密度），搅一搅看看稀稠（输出密度），如果不合适就得再调。

传统的办法是只看最后一次调得怎么样（线性混合），但这样往往得调几十次。Pulay 混合就聪明了：太奶把最近好几次调面糊的经验（历史记录）都攒着，然后算一算：要是把前几次的比例按一定分量和在一起，是不是一下就能调准了？事实证明，这招特别灵，原本要调几十步的，现在十几步就搞定了，尤其是处理那些容易“晃荡”的金属体系时，特别管用！

## 🏗️ 结构概览

在自洽循环中，电荷密度的收敛是判断计算成功的标准。

![图：fcc-Al 自洽能量收敛情况](../../raw/figures/kresseEfficientIterativeSchemes1996d/fig_6_D9VHA5DL.png)
*   **看图要点**：图中对比了不同混合方案。Pulay 混合配合合适的预条件，能让不同尺寸体系的迭代步数保持一致，极大地抑制了电荷晃动。
*   **来源** [[../papers/kresseEfficientIterativeSchemes1996d]] -> [[../figures/mathematical-models-computational|计算方法与泛函]]

## 🧩 算法机制

### 1. 历史残差的最小化
Pulay 混合的核心思想是将下一代的输入密度 $\rho_{in}^{new}$ 表示为历史输入密度 $\rho_{in}^i$ 的线性组合：
$$ \rho_{in}^{new} = \sum a_i \rho_{in}^i $$
系数 $a_i$ 通过最小化历史残差向量 $|R\rangle = \rho_{out} - \rho_{in}$ 的范数来获得。

### 2. 准牛顿加速 (Quasi-Newton Acceleration)
从数学上看，Pulay 混合等价于一种准牛顿方法，它在迭代过程中隐式地构建并优化了介电矩阵（逆雅可比矩阵）的信息。这使得它在接近基态时具有二阶收敛的特征。

### 3. 处理电荷晃动 (Charge Sloshing)
在金属或表面体系中，低波数（长波）电荷密度的微小变化会导致有效势的剧烈振荡，这被称为“电荷晃动”。Pulay 混合通常与 **Kerker 预条件** 配合使用，通过对长波分量施加更强的阻尼，使计算能稳定收敛。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseEfficientIterativeSchemes1996d]]：详细对比了 Pulay 混合与 Broyden 混合在 VASP 中的表现。
- [[../papers/kresseEfficiencyAbinitioTotal1996a]]：讨论了在复杂金属表面体系中 Pulay 混合的鲁棒性。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[self-consistent-field-cycle|自洽场循环 (SCF)]]：混合步是 SCF 循环的最后一步核心动作。
- [[rmm-diis|RMM-DIIS]]：对角化与混合是 SCF 这一台大戏的两位“主角”。
- Kerker 预条件 (concept)：Pulay 混合在金属体系中的“黄金搭档”。
- VASP (entity)：通过 IMIX 和 AMIX 等参数控制。
 luxury
