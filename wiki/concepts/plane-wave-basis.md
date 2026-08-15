---
tags: [concept, computational-physics, vasp, dft]
title: Plane-Wave Basis / 平面波基组
type: concept
status: mature
domain: [computational-physics, electronic-structure]
mechanism: 利用傅里叶级数将周期性体系中的电子波函数展开，在倒空间进行高效计算。
related_concepts: [monkhorst-pack-grid, projector-augmented-wave, rmm-diis]
papers: [kresseEfficiencyAbinitioTotal1996a, kresseEfficientIterativeSchemes1996d]
updated: 2026-08
---

# Plane-Wave Basis / 平面波基组 (Plane-Wave Basis Set)

平面波基组是固体第一性原理计算中最常用的基组类型。得益于 Bloch 定理，平面波天然适合描述具有三维周期性对称性的晶体体系，并且能通过快速傅里叶变换 (FFT) 极大地提高数值计算效率。

## 👵 太奶导读

太奶，这平面波基组啊，就像是用一堆整整齐齐的“音叉”（也就是波，有长有短，有快有慢）来合成一首复杂的交响乐（也就是电子波函数）。

因为晶体就像是一排排整齐的路灯（周期性），电子在里面走，受到的力也是一停一顿、有规律的。平面波这种“音叉”天然就带着这种节奏感，拿它来拼电子的形状最省事。而且，音叉好就好在干净：你只要把声音放得足够大，高音低音配齐了，它什么调子都能拼出来（这叫基组完备性，没有轨道重叠误差）。再配合上“快速傅里叶变换”这个数学账本，电脑能把乘法变加法算，快得跟飞一样！

## 🏗️ 结构概览

在平面波基组下，计算的精度由一个关键参数——平面波截断能（ENCUT）控制。

![图：总能量随 k 点采样与展宽参数的收敛](../../raw/figures/kresseEfficiencyAbinitioTotal1996a/fig_2_K2M97DMS.png)
*   **看图要点**：在平面波体系中，波函数截断能和布里渊区采样点数（Monkhorst-Pack）是决定精度的两大生死线，图示为能量随 k 点网格收敛的趋势。
*   **来源**：[[../papers/kresseEfficiencyAbinitioTotal1996a]] -> [[../figures/mathematical-models-computational|计算方法与泛函]]

## 🧩 数学与算法逻辑

### 1. Bloch 定理与展开
根据 Bloch 定理，周期性势场中的单电子波函数可以写成：
$$ \psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r}) $$
其中 $u$ 是一个与晶格同周期的函数。因此，我们可以将 $u$ 展开为一组倒格矢 $\mathbf{G}$ 的平面波级数：
$$ \psi_{n\mathbf{k}}(\mathbf{r}) = \sum_{\mathbf{G}} C_{n\mathbf{k}}(\mathbf{G}) e^{i(\mathbf{k}+\mathbf{G})\cdot\mathbf{r}} $$

### 2. 截断能 (Kinetic Energy Cutoff)
在实际计算中，我们不可能使用无限多项平面波，必须将动能大于某一阈值的平面波截断：
$$ \frac{\hbar^2 |\mathbf{k}+\mathbf{G}|^2}{2m} \le E_{cut} $$
这个 $E_{cut}$ 就是 INCAR 中的 ENCUT 选项。它的大小直接决定了基组的大小和计算精度。

### 3. 双空间技术与 FFT (Double Grid and FFT)
平面波基组之所以极度高效，核心在于哈密顿量算符在不同的表象中是对角化的：
- **动能项**：在倒空间（傅里叶空间）是对角的，计算只需 $O(N_{pw})$ 步乘法。
- **局域势能项**：在实空间是对角的。
利用**快速傅里叶变换 (FFT)**，计算程序可以在实空间和倒空间之间进行极速切换。这避免了直接计算巨大的耦合矩阵，将算符施加在波函数上的计算复杂度降低到 $O(N_{pw} \ln N_{pw})$。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseEfficiencyAbinitioTotal1996a]]：系统阐述了平面波基组下的双空间 FFT 算法以及与超软赝势的结合。
- [[../papers/kresseEfficientIterativeSchemes1996d]]：讨论了在大体系中，平面波基组配合 Gram-Schmidt 正交化的操作数标度。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[monkhorst-pack-grid|Monkhorst-Pack 网格]]：在倒空间对平面波基组进行采样的标准网格。
- [[../concepts/paw-method]]：用于消除平面波在核区不收敛问题的终极武器。
- VASP (entity)：最成功的周期性平面波第一性原理计算软件。
