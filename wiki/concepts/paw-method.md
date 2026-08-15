---
tags: [concept, dft, quantum-chemistry]
title: 投影增强波法 / Projector Augmented-Wave Method (PAW)
type: concept
status: mature
domain: [computational-physics, density-functional-theory]
mechanism: 通过从平滑赝波函数到全电子波函数的线性变换，兼顾全电子 LAPW 方法的高精度与平面波赝势方法的高效率
related_concepts: [density-functional-theory, pseudopotential, frozen-core-approximation, overlap-operator, projector-functions]
papers: [blochlProjectorAugmentedwaveMethod1994b, kresseUltrasoftPseudopotentialsProjector1999c, gajdosLinearOpticalProperties2006, shishkinImplementationPerformanceFrequencydependentGWmethod2006]
updated: 2026-08
---

# 投影增强波法 / Projector Augmented-Wave Method (PAW)

投影增强波法（Projector Augmented-Wave Method, PAW）是第一性原理电子结构计算中精度最高且最主流的方法学框架之一。它由 Peter Blöchl 于 1994 年提出。PAW 通过引入一个数学上的线性变换，成功将全电子（All-Electron, AE）方法（如线性增强平面波 LAPW 方法）在原子核附近的无损高精度，同赝势（Pseudopotential）方法在价电子区的极高计算效率完美结合起来。它是现代第一性原理计算软件（如 VASP）的基石。

## Grandma 👵 太奶导读

太奶，这“投影增强波方法”听着像洋人的黑科技，其实道理就像咱们给**近视眼配眼镜**，或者给复杂的拼图**分块打磨**。
在研究材料里那层层叠叠的电子（波函数）时，科学家遇到了个死结：
贴近原子核那里的电子，像是一片惊涛骇浪，振荡得极快，你非得用极细极密的尺子去量（这叫全电子法），但这样算起来慢死人；而外层的价电子，就像是一潭平静的池水，拿把粗木尺（平面波）一量就完事（这叫赝势法）。
PAW 方法聪明在哪呢？它发明了一个“数学魔术箱”（线性变换）。
在核外面，它用粗木尺算，快得很（算“赝波函数”）；一走到核附近（缀加区域），它就把眼镜一戴，立刻把粗线条还原成原本那个惊涛骇浪的细致模样（重构出“全电子波函数”）。
这样一来，既有了最先进放大镜的惊人精度，又省下了大笔算盘钱，算起复杂的金属材料来又快又准！

## 🏗️ 物理公式与数学模型

### 1. 核心线性变换
PAW 方法的核心在于一个从平滑的**赝（PS）波函数 $|\tilde{\Psi}\rangle$** 映射到真实的**全电子（AE）物理波函数 $|\Psi\rangle$** 的线性算符 $T$：

$$|\Psi\rangle = T |\tilde{\Psi}\rangle = |\tilde{\Psi}\rangle + \sum_{R} T_R |\tilde{\Psi}\rangle$$

其中局域算符 $T_R$ 仅在以核 $R$ 为中心的**增强区域（Augmentation region / Muffin-tin 核心区）**内起作用。利用一组原子全电子分波 $|\varphi_i\rangle$、对应的平滑赝分波 $|\tilde{\varphi}_i\rangle$ 以及[[../concepts/projector-functions|投影函数]] $\langle\tilde{p}_i|$（满足双正交关系 $\langle\tilde{p}_i|\tilde{\varphi}_j\rangle = \delta_{ij}$），变换算符写为：

$$T = 1 + \sum_{i} (|\varphi_i\rangle - |\tilde{\varphi}_i\rangle) \langle\tilde{p}_i|$$

由此，真实的物理波函数被完全展开为：

$$|\Psi\rangle = |\tilde{\Psi}\rangle + \sum_{i} (|\varphi_i\rangle - |\tilde{\varphi}_i\rangle) \langle\tilde{p}_i|\tilde{\Psi}\rangle$$

这被称为**加法缀加（Additive augmentation）**。

### 2. 重叠算符与非共线性
由于 PAW 放弃了范数守恒（Norm-conservation）的要求（这使赝分波可以更加平滑，大大降低了平面波截断能），使得体系的能量极小化问题必须在一个非平凡的[[../concepts/overlap-operator|重叠算符]] $S$ 下求解：

$$H |\tilde{\Psi}\rangle = E S |\tilde{\Psi}\rangle$$

$$S = 1 + \sum_{ij} |\tilde{p}_i\rangle (\langle\varphi_i|\varphi_j\rangle - \langle\tilde{\varphi}_i|\tilde{\varphi}_j\rangle) \langle\tilde{p}_j|$$

## 🧩 为什么 PAW 优于传统赝势？

*   **全电子波函数重构**：传统赝势在增强区内丢失了物理波函数的节点信息。PAW 在保留平面波效率的同时，可以通过原子径向网格上的三中心展开，**100% 重构核区真实的波函数**。这对于计算超精细相互作用、核磁共振（NMR）谱、EPR 谱或核心空穴谱至关重要。
*   **能量守恒的分子动力学**：由于 PAW 中推导出的原子受力（含 Pulay 力）与总能量严格一致，它成功克服了早期超软赝势在 Car-Parrinello 分子动力学（CPMD）中能量漂移的硬伤。

## 📚 相关论文 (Related Papers)

- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：PAW 方法的奠基性理论论文，给出了详尽的推导与原子/分子测试基准。
- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]：将 PAW 形式化引入 VASP 软件，并论证了其与 Vanderbilt 超软赝势的等价性与优越性。
- [[../papers/gajdosLinearOpticalProperties2006]]
- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]]
- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]：论证了 PAW 是 US-PP 的线性化泛函，并确立了其在 VASP 中的核心地位。
- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：PAW 方法的原创论文，奠定了理论基础。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/density-functional-theory|密度泛函理论 (DFT)]]
- [[../concepts/frozen-core-approximation|冻结芯近似]]
- [[../concepts/projector-functions|投影函数]]
- [[../concepts/overlap-operator|重叠算符]]
- [[../entities/VASP|VASP]]（核心载体工具）
- [[ultrasoft-pseudopotential|超软赝势 (US-PP)]]：PAW 的前身和简化版本。
- [[plane-wave-basis|平面波基组]]：PAW 运行的主要数学舞台。
- VASP (entity)：PAW 势库最完备、使用最广泛的计算软件。
- [[../concepts/DFT-U]]：PAW 与 U 修正结合是处理强关联过渡金属氧化物的标准方案。

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

## 🏷️ 专业名词别名

- `projector-augmented-wave`（concepts）
