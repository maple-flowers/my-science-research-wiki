---
tags: [concept, computational-physics, vasp, dft]
title: Methfessel-Paxton Smearing / Methfessel-Paxton 展宽
type: concept
status: mature
domain: [computational-physics, electronic-structure]
mechanism: 使用 Hermite 多项式展开阶跃函数，用于处理金属体系布里渊区积分中的部分占据问题。
related_concepts: [self-consistent-field-cycle, monkhorst-pack-grid, plane-wave-basis]
papers: [kresseEfficiencyAbinitioTotal1996a, kresseEfficientIterativeSchemes1996d]
updated: 2026-08
---

# Methfessel-Paxton 展宽 / Methfessel-Paxton Smearing

Methfessel-Paxton (MP) 展宽是第一性原理计算中处理金属体系电子占据数的标准方法。它通过引入平滑的分布函数来模拟费米面附近的电子分布，从而显著加速倒空间的收敛。

## 👵 太奶导读

太奶啊，咱们在算金属的时候，电子就像一池子水。在绝对零度时，这池水本来应该有个齐刷刷的水面（这叫“费米面”）。但在计算机里算的时候，如果水面太齐了，积分起来就特别费劲，得撒特别多的网（k点）才行。

这 Methfessel-Paxton 展宽啊，就像是往水面上洒了一层薄薄的泡沫，把那个硬邦邦的水面给变软、变糊了一点。这样一来，咱们用少一点的网也能把水深算准了。最厉害的是，这个办法算出来的能量和力特别合拍，不会像别的办法那样顾头不顾屁股。

## 🏗️ 结构概览

![图：自由能随展宽参数 sigma 的收敛情况](../../raw/figures/kresseEfficiencyAbinitioTotal1996a/fig_1_D42XHL87.png)
*   注：此处引用论文中图1说明收敛性，实际图中对比了高斯展宽与 MP 展宽。
*   **看图要点**：随着展宽参数 $\sigma$ 增大，MP 展宽（$N \ge 1$）的自由能在很大范围内保持平稳，这意味着我们可以使用较大的展宽而不会损失太多精度。
*   **来源**：[[../papers/kresseEfficiencyAbinitioTotal1996a]] -> [[../figures/mathematical-models-computational|计算方法与泛函]]

## 🧩 物理机制

### 1. Hermite 多项式展开
不同于简单的高斯展宽（N=0），Methfessel-Paxton 方法使用高阶 Hermite 多项式来修正分布函数。当阶数 $N$ 增加时，其描述的分布在远离费米面时会产生轻微的过冲（负占据），但在物理上这能极大地消除能量对展宽参数 $\sigma$ 的依赖。

### 2. 能量-力一致性 (Energy-Force Consistency)
在金属体系的结构优化中，受力必须是自由能的精确导数。MP 展宽引入了一个虚熵项 $S$，通过最小化自由能 $F = E - \sigma S$，可以保证计算出的原子力与总能量的变化是完全自洽的。这使得它在计算声子谱和分子动力学时表现极佳。

### 3. $O(\sigma^{N+2})$ 的收敛速度
理论证明，对于 $N$ 阶 MP 展宽，计算出的自由能与真实零温能量的偏差随着 $\sigma$ 的 $N+2$ 次方衰减。这意味着即使 $\sigma$ 设置得比较大（例如 0.2 eV），只要阶数够高，结果依然非常可靠。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseEfficiencyAbinitioTotal1996a]]：详细对比了 MP 展宽与其他展宽方案在金属（如 Al、V、Rh）中的效率。
- [[../papers/kresseEfficientIterativeSchemes1996d]]：讨论了部分占据数对自洽收敛性的影响。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[monkhorst-pack-grid|Monkhorst-Pack 网格]]：展宽法通常与 k 点网格密度配合进行收敛性测试。
- [[self-consistent-field-cycle|自洽场循环]]：展宽决定了每步迭代中能带的占据权重。
- VASP (entity)：ISMEAR = 1, 2 对应 Methfessel-Paxton 展宽。
