---
tags: [concept, computational-physics, vasp, dft]
title: RMM-DIIS / 残差最小化-迭代子空间直接反演
type: concept
status: mature
domain: [computational-physics, electronic-structure]
mechanism: 通过最小化残差向量的范数而非 Rayleigh 商来加速哈密顿矩阵的迭代对角化。
related_concepts: [self-consistent-field-cycle, pulay-mixing, plane-wave-basis]
papers: [kresseEfficientIterativeSchemes1996d, kresseEfficiencyAbinitioTotal1996a]
updated: 2026-08
---

# RMM-DIIS / 残差最小化-迭代子空间直接反演 (Residual Minimization Method - Direct Inversion in the Iterative Subspace)

RMM-DIIS 是 VASP 等平面波第一性原理计算软件中最高效的迭代对角化算法之一。它通过最小化残差向量的范数来寻找 Kohn-Sham 方程的本征态，其核心优势在于避免了昂贵的显式正交化过程，从而将计算复杂度从 $O(N^3)$ 降低到接近 $O(N^2)$。

## 👵 太奶导读

这 RMM-DIIS 啊，就像是太奶在给一群小重孙子排队，但重孙子实在太多了（就像大体系里的电子能带），如果太奶每次都要盯着每个人，让他们互相别撞着（这叫“正交化”，特别费劲），那太奶得累坏了。

好在，RMM-DIIS 想了个巧办法：太奶给每个重孙子划了个大概的位置，然后只盯着他们是不是站歪了（这就是看“残差”）。只要每个人都不站歪，他们自然就各就各位了，不用非得每次都把所有人拎出来互相打比对。这样一来，重孙子再多，太奶也能管得过来，效率高得不得了！

## 🏗️ 结构概览

在 RMM-DIIS 算法中，我们关注的是残差向量 $|R\rangle$ 的演化。

![图：RMM-DIIS 对不同尺寸金刚石超胞的能量收敛情况](../../raw/figures/kresseEfficientIterativeSchemes1996d/fig_2_K2M97DMS.png)
*   **看图要点**：图中显示了从 1 个晶胞到 8 个晶胞（对应不同原子数）的收敛曲线。可以看到，无论体系变大多少倍，达到相同精度所需的迭代步数几乎是一样的。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]] -> [[../figures/mathematical-models-computational|计算方法与泛函]]

## 🧩 算法机制

### 1. 最小化残差范数 (Minimizing Residual Norm)
传统的对角化方法（如共轭梯度法）通常最小化 Rayleigh 商 $\langle\phi|H|\phi\rangle/\langle\phi|S|\phi\rangle$。但在 RMM-DIIS 中，目标函数变成了残差的平方范数：
$$ \min \langle R|R \rangle, \quad |R\rangle = (H - \epsilon S)|\phi\rangle $$
由于残差范数在每个本征态处都有一个局部极小值（为 0），因此在理想情况下，不同能带的优化是相互解耦的，这大大减少了能带间显式正交化的频率。

### 2. 子空间迭代 (Iterative Subspace)
RMM-DIIS 结合了 DIIS（直接迭代子空间求逆）的思想。在每一步迭代中，算法会保留历史的试探波函数和残差，通过求解一个小维度的线性方程组来找到最优的组合系数，从而加速收敛。

### 3. $O(N^2)$ 标度与并行性
由于避免了每一步都进行 $O(N^3)$ 的 Gram-Schmidt 正交化，RMM-DIIS 的主导步骤变成了哈密顿量作用于波函数（FFT 操作，标度为 $N^2 \ln N$）。这使得它在处理包含数百个原子的“大型”体系时，比传统的 Davidson 方法快得多，且非常适合大规模并行计算。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseEfficientIterativeSchemes1996d]]：系统论述了 RMM-DIIS 在 VASP 中的实现与标度优势。
- [[../papers/kresseEfficiencyAbinitioTotal1996a]]：VASP 算法框架的基石论文，详细对比了 RMM-DIIS 与其他对角化方法。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[self-consistent-field-cycle|自洽场循环 (SCF)]]：RMM-DIIS 通常作为 SCF 循环内部的电子步对角化引擎。
- [[pulay-mixing|Pulay 混合]]：与 RMM-DIIS 配合使用的电荷密度混合技术。
- [[plane-wave-basis|平面波基组]]：RMM-DIIS 效率发挥的前提。
- VASP (entity)：该算法的核心实现平台。
