---
tags: [concept, computational-physics, vasp, dft]
title: Ultrasoft Pseudopotential / 超软赝势 (US-PP)
type: concept
status: mature
domain: [computational-physics, electronic-structure]
mechanism: 放松模守恒约束并引入增强电荷，显著降低计算第一周期元素和过渡金属所需的平面波截断能。
related_concepts: [projector-augmented-wave, plane-wave-basis, density-functional-theory]
papers: [kresseUltrasoftPseudopotentialsProjector1999c, kresseEfficiencyAbinitioTotal1996a, kresseEfficientIterativeSchemes1996d]
updated: 2026-08
---

# Ultrasoft Pseudopotential / 超软赝势 (US-PP / Vanderbilt Pseudopotentials)

超软赝势（US-PP）是由 D. Vanderbilt 提出的一种革命性赝势技术。它极大地降低了计算含 3d 过渡金属或氧、氮等元素的体系时所需的计算资源，是 90 年代第一性原理计算普及的关键功臣。

##  Grandma-style / 奶奶导读

奶奶啊，以前咱们算那些特别硬的原子（比如铁啊、氧啊）时，得用特别细的筛子（特别高的截断能）来过筛电子。筛子眼越细，计算量就越大，电脑累得呼哧呼哧的。

这超软赝势啊，就像是给这些硬骨头原子套上了一个“减震垫”。它把核附近那些像刺猬一样扎人的电子波函数给磨圆滑了，而且还故意放宽了要求（不用模守恒了）。这样一来，咱们用粗得多的筛子也能把这活给干了。虽然省了事，但为了保准，它在核附近加了个叫“增强电荷”的补丁。在 PAW 方法出来之前，这可是大家伙儿最爱用的省钱秘籍！

## 🏗️ 结构概览

US-PP 的核心在于引入了重叠算符 $S$ 和增强电荷。

![图：US-PP 非局域势强度与 PAW 的线性关系](../../raw/figures/kresseUltrasoftPseudopotentialsProjector1999c/eq_35_SUNR7ATM.png)
*   **看图要点**：图中展示了 US-PP 的强度项是如何与原子参考态关联的。US-PP 可以看作是 PAW 方法的一种简化（一阶线性化）。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]] -> [[../figures/mathematical-models-computational|计算方法与泛函]]

## 🧩 算法机制

### 1. 放宽模守恒 (Relaxing Norm-conservation)
传统的模守恒赝势要求赝波函数在切断半径内的电荷总量与全电子波函数完全相等。US-PP 放宽了这一限制，允许赝波函数在核区极其平滑（即“超软”），从而大幅降低截断能（ENCUT）。

### 2. 增强电荷 (Augmentation Charge)
为了弥补放宽模守恒带来的电荷缺失，US-PP 引入了增强电荷项。这些电荷被定义在各原子的局域区域内，使得总的物理电荷分布仍然是正确的。

### 3. 广义本征值方程
由于基组不再正交（引入了 $S$ 算符），原本的 Kohn-Sham 方程变成了广义本征值方程：
$$ H|\psi\rangle = \epsilon S|\psi\rangle $$
这要求在计算电荷密度和力时，必须显式计入 $S$ 算符及其对坐标的导数。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]：深刻揭示了 US-PP 是 PAW 的线性化近似，并指出了其在强磁性体系中的局限性。
- [[../papers/kresseEfficiencyAbinitioTotal1996a]]：展示了 US-PP 在过渡金属和半导体体系中的巨大效率优势。
- [[../papers/kresseEfficientIterativeSchemes1996d]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/paw-method]]：现代计算中已全面取代 US-PP 的更高精度方法。
- [[plane-wave-basis|平面波基组]]：US-PP 诞生的初衷就是为了拯救高昂的平面波基组开销。
- VASP (entity)：早期 VASP 版本的核心竞争力之一就是高效的 US-PP 支持。
