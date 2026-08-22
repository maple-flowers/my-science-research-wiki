---
tags: [concept, density-functional-theory, machine-learning-potential, subspace-alignment, nose-thermostat]
title: conjugate-gradient-minimization
type: concept
status: stub
year: 1993
papers: [kresseInitiomolecularDynamicsLiquid1993, kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994]
updated: 2026-08-18
---

# conjugate-gradient-minimization

> [!warning] 本页内容待重写
> 本页的「太奶导读」与「相关论文」贡献句均为自动生成的占位内容——导读描述的是某篇论文的研究对象，
> 而非本条目本身。**请勿引用本页结论**。已按 SCHEMA 降级为 `stub`。（标记于 2026-08-21）


本文档围绕 **conjugate-gradient-minimization** 汇集 2 篇论文的证据，覆盖其结构、物性与机制等多方面信息。

## 👵 太奶导读

乖孙，这一条讲的是「conjugate-gradient-minimization」，由多篇论文的证据共同支撑。
一句话记住它的发现：通过共轭梯度电子基态极小化和子空间对齐波函数预测，实现了对液态Na和Ge的从头算MD模拟，能量漂移分别小于1 meV和4 meV，时间步长可达3 fs。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：Car-Parrinello方法（1985）统一了电子结构和离子动力学，但其虚拟电子动力学在金属中因电子-离子频率共振和能级交叉导致能量漂移，需周期性能量最小化或电子热浴来维持绝热性。本文提出直接在每个MD步计算Kohn-Sham基态，使用共轭梯度极小化、Kerker电荷混合和Nosé热浴，从根本上消除非绝热性，为液态金属的精确模拟开辟新途径。
- **核心问题**：如何在金属体系中实现绝热性可控、能量守恒且计算可行的从头算分子动力学，以替代不稳定的Car-Parrinello方法，获得液态金属的准确结构和电子性质。
- **主要结论**：通过共轭梯度电子基态极小化和子空间对齐波函数预测，实现了对液态Na和Ge的从头算MD模拟，能量漂移分别小于1 meV和4 meV，时间步长可达3 fs。模拟结果准确再现了实验的配对相关函数、扩散系数（Na：6×10⁻⁵ cm²/s）和电子态密度（Ge赝能隙），揭示了液态Ge中sp³杂化破坏与四面体残留短程有序，证实了方法的可靠性和先进性。
- **领域贡献**：提供了一种稳定、高效的精确基态AIMD方案，克服了Car-Parrinello方法在金属中的根本困难；发展了共轭梯度极小化、子空间对齐、Kerker混合等技术组合，为后续第一性原理分子动力学（如VASP软件的实现）奠定了算法基础；深化了对液态金属和液态半导体短程有序与电子结构的理解。
- **研究意义**：证明了无需虚构电子动力学即可在金属中实现稳定、精确的AIMD；方法对液态Na和Ge的结构因子、配位数、键角分布、扩散系数和电子态密度的模拟结果与实验高度吻合，展示了该方法在液态金属、半导体和非晶态材料研究中的巨大潜力，并奠定了现代精确基态AIMD算法的基础。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseInitiomolecularDynamicsLiquid1993]]：提供了一种稳定、高效的精确基态AIMD方案，克服了Car-Parrinello方法在金属中的根本困难；发展了共轭梯度极小化、子空间对齐、Kerker混合等技术组合，为后续第一性原理分子动力学（如VASP软件的实现）奠定了算法基础；深化了对液态金属和液态半导体短程有序与电子结构的理解。
- [[../papers/kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994]]：为本文档提供核心证据。

## 🔗 关联概念与实体 (Related)

- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/machine-learning-potential|machine-learning-potential]]
- [[../concepts/subspace-alignment|subspace-alignment]]
- [[../concepts/nose-thermostat|nose-thermostat]]
- [[../concepts/pair-correlation-function|pair-correlation-function]]
- [[../concepts/born-oppenheimer-md|born-oppenheimer-md]]
- [[../concepts/pseudopotential|pseudopotential]]
- [[../entities/SnTe|SnTe]]
- [[../entities/VASP|VASP]]
