---
tags: [concept, computational-physics, vasp, dft]
title: Projector-Augmented Wave / 投影增强波方法 (PAW)
type: concept
status: mature
domain: [computational-physics, electronic-structure]
mechanism: 通过线性变换将平滑的赝波函数与剧烈振荡的全电子波函数联系起来，兼具平面波效率与全电子精度。
related_concepts: [density-functional-theory, ultrasoft-pseudopotential, plane-wave-basis]
papers: [kresseUltrasoftPseudopotentialsProjector1999c, blochlProjectorAugmentedwaveMethod1994b]
updated: 2026-08
---

# Projector-Augmented Wave / 投影增强波方法 (PAW)

PAW 方法是现代密度泛函理论计算的事实标准。它由 P. Blöchl 提出并由 G. Kresse 等人在 VASP 中发扬光大。PAW 巧妙地结合了平面波基组的高效性和全电子方法（如 FLAPW）的高精度。

## 👵 太奶导读

太奶，这电子在原子核附近就像是坐上了疯狂的过山车，晃得特别厉害（波函数振荡剧烈），但在离原子核远一点的地方，它们就像是在平地上走道，特别平稳。

以前的办法要么是嫌核附近太麻烦，直接把那块给“抹平”了（这叫赝势），虽然快但不够准；要么是硬着头皮一点点算，虽然准但慢得要命。

PAW 就像是给电子发了两套衣服：一套是平时穿的休闲装（平滑的波函数），在外面逛街（晶格空间）时穿；一套是原子核附近的专用铠甲（原子补丁）。平时咱们只算休闲装怎么穿，等需要看核附近真章的时候，就用一套数学魔术把铠甲给套上去。这样一来，咱们既跑得快，又能看清核附近的细节，真是两全其美！

## 🏗️ 结构概览

PAW 的核心是将物理量拆解为三部分。

![图：PAW 线性变换与电荷密度分解](../../raw/figures/kresseUltrasoftPseudopotentialsProjector1999c/eq_2_FQCU82JS.png)
*   **看图要点**：公式描述了如何通过原子参考态从赝波函数 $\tilde{\psi}$ 恢复全电子波函数 $\psi$。在增强球（Augmentation sphere）外，两者是一致的；在球内，通过补丁项进行修正。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]] -> [[../figures/mathematical-models-computational|计算方法与泛函]]

## 🧩 物理机制

### 1. 线性变换与映射
PAW 建立了一个从赝波函数空间到全电子空间的线性映射。计算过程主要在平滑的赝波函数空间中进行（使用平面波基组），这保留了 FFT 带来的计算效率。

### 2. 电荷密度的三项分解
在 PAW 中，总电荷密度 $n$ 被表示为：
$$ n = \tilde{n} + n^1 - \tilde{n}^1 $$
- $\tilde{n}$：平面波网格上的平滑赝密度。
- $n^1$：原子球内的高分辨率全电子密度（在径向网格上计算）。
- $\tilde{n}^1$：原子球内的平滑赝密度（用于消除重复计数）。

### 3. 全电子精度与磁性描述
相比于超软赝势 (US-PP)，PAW 是一种“全势”方法，它显式处理了核心电子的势场。这使得它在描述强关联体系、磁性体系（如 Fe、Co、Ni 的磁矩）以及超精细相互作用时具有极高的精度，与 FLAPW 方法相当。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]：论证了 PAW 是 US-PP 的线性化泛函，并确立了其在 VASP 中的核心地位。
- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：PAW 方法的原创论文，奠定了理论基础。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[ultrasoft-pseudopotential|超软赝势 (US-PP)]]：PAW 的前身和简化版本。
- [[plane-wave-basis|平面波基组]]：PAW 运行的主要数学舞台。
- VASP (entity)：PAW 势库最完备、使用最广泛的计算软件。
- [[dft-plus-u|DFT+U]]：PAW 与 U 修正结合是处理强关联过渡金属氧化物的标准方案。
