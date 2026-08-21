---
tags: [concept, ferroelectricity, polarization-switching, ferroelectric-tunnel-junction, neuromorphic-computing, in-memory-computing, density-functional-theory, exchange-correlation-functional, generalized-gradient-approximation, local-spin-density-approximation, pbe-functional]
title: enhancement-factor
type: concept
status: developing
year: 2026
papers: [chenHafniumBasedFerroelectricPostMoore2026, perdewGeneralizedGradientApproximation1996a]
updated: 2026-08-18
---

# enhancement-factor

本文档围绕 **enhancement-factor** 汇集 2 篇论文的证据，覆盖其结构、物性与机制等多方面信息。

## 👵 太奶导读

乖孙，这一条讲的是「enhancement-factor」，由多篇论文的证据共同支撑。
一句话记住它的发现：作者成功构建了一个名为PBE的简化GGA泛函。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：当时最先进的GGA泛函是Perdew-Wang 1991 (PW91)，它虽然成功，但存在推导冗长复杂、形式不透明、参数过多、交换-关联势产生虚假波动、在高密度标度极限下行为不正确、以及对均匀电子气线性响应描述不佳等问题。这些问题源于PW91试图满足过多对能量贡献微小的形式化精确条件。
- **核心问题**：作者旨在解决PW91泛函的六大问题，提出一个更简单、更透明、只满足能量上最关键的物理条件的GGA泛函。其核心问题是：能否在不牺牲计算精度的前提下，从基本原理出发，推导出一个不含任何经验参数、形式简洁优美的GGA泛函？
- **主要结论**：作者成功构建了一个名为PBE的简化GGA泛函。该泛函的所有参数均为基本物理常数，无经验参数。其推导过程清晰，形式简洁，解决了PW91的多个理论缺陷，并产生了更平滑的势能。对小分子原子化能的计算证明，PBE的精度与PW91相当，平均绝对误差约为8 kcal/mol，远优于LSD。
- **领域贡献**：1.提供一个推导清晰、形式简洁、无经验参数且精度优异的GGA泛函，成为电子结构计算的标准工具。2.修正了PW91泛函的关键理论缺陷，尤其是在线性响应和高密度标度极限方面。3.确立了一种“少即是多”的物理建模思想，即通过满足重要物理极限而非所有形式条件来构建高效模型。
- **研究意义**：该研究成功证明了通过满足少数能量上关键的物理约束，可以构建出与复杂泛函精度相当的简化泛函，为DFT泛函开发提供了新的哲学范式。PBE泛函的诞生极大地推动了DFT计算在物理、化学和材料科学等领域的广泛应用，成为该领域最经典的泛函之一。

## 📚 相关论文 (Related Papers)

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：为本文档提供核心证据。
- [[../papers/perdewGeneralizedGradientApproximation1996a]]：1.提供一个推导清晰、形式简洁、无经验参数且精度优异的GGA泛函，成为电子结构计算的标准工具。

## 🔗 关联概念与实体 (Related)

- [[../concepts/ferroelectricity|ferroelectricity]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/ferroelectric-tunnel-junction|ferroelectric-tunnel-junction]]
- [[../concepts/neuromorphic-computing|neuromorphic-computing]]
- [[../concepts/in-memory-computing|in-memory-computing]]
- [[../concepts/synaptic-plasticity|synaptic-plasticity]]
- [[../concepts/doping-engineering|doping-engineering]]
- [[../concepts/strain-engineering|strain-engineering]]
- [[../concepts/oxygen-vacancy|oxygen-vacancy]]
- [[../concepts/phase-transition|phase-transition]]
- [[../concepts/domain-wall-motion|domain-wall-motion]]
- [[../concepts/cmos-compatibility|cmos-compatibility]]
- [[../concepts/multiferroicity|multiferroicity]]
- [[../concepts/2d-materials|2d-materials]]
- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/wake-up-effect|wake-up-effect]]
