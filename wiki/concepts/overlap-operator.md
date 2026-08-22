---
tags: [concept, density-functional-theory, paw-method, pseudopotential, lapw, projector-functions, norm-conserving-pseudopotential, projector-augmented-wave, frozen-core-approximation, augmentation-charge]
title: overlap-operator
type: concept
status: stub
year: 1994
papers: [blochlProjectorAugmentedwaveMethod1994b, kresseUltrasoftPseudopotentialsProjector1999c]
updated: 2026-08-18
---

# overlap-operator

> [!warning] 本页内容待重写
> 本页的「太奶导读」与「相关论文」贡献句均为自动生成的占位内容——导读描述的是某篇论文的研究对象，
> 而非本条目本身。**请勿引用本页结论**。已按 SCHEMA 降级为 `stub`。（标记于 2026-08-21）


本文档围绕 **overlap-operator** 汇集 2 篇论文的证据，覆盖其结构、物性与机制等多方面信息。

## 👵 太奶导读

乖孙，这一条讲的是「overlap-operator」，由多篇论文的证据共同支撑。
一句话记住它的发现：PAW方法成功弥合了全电子方法和赝势方法之间的鸿沟。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：电子结构计算方法是精确预测材料性质的核心，但主流方法存在鸿沟：全电子方法（如LAPW）精度高但计算复杂，赝势方法效率高但对许多元素（如过渡金属）精度受限或变得“硬”。迫切需要一种能结合二者优势的新方法。
- **核心问题**：如何构建一个统一的电子结构计算框架，既能像赝势方法那样利用平滑波函数进行高效计算，又能像LAPW方法那样精确重构出全电子波函数，从而在保持高精度的同时实现高质量的分子动力学模拟？
- **主要结论**：PAW方法成功弥合了全电子方法和赝势方法之间的鸿沟。它能够以中等的计算代价（如30 Ry平面波截断）获得与最先进全电子方法相当的精度，并可以进行高质量的分子动力学模拟。其精度和效率优于传统赝势，尤其在处理“硬”元素时。
- **领域贡献**：1. 提出了PAW方法这一革命性的理论框架，成为现代高精度DFT计算（如VASP软件）的基石。2. 深刻揭示了不同电子结构计算方法之间的内在联系与统一性。3. 提供了可操作的“配方”来构建分波和投影函数，为方法普及铺平了道路。
- **研究意义**：首次在理论上统一了增强波方法和赝势方法，证明LAPW是其特例，赝势是其近似。提供了一个兼具全电子精度和赝势效率的全新计算范式，并首次实现了基于全电子波函数的、能量守恒的分子动力学模拟。

## 📚 相关论文 (Related Papers)

- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：1. 提出了PAW方法这一革命性的理论框架，成为现代高精度DFT计算（如VASP软件）的基石。
- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]：为本文档提供核心证据。

## 🔗 关联概念与实体 (Related)

- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/paw-method|paw-method]]
- [[../concepts/pseudopotential|pseudopotential]]
- [[../concepts/projector-functions|projector-functions]]
- [[../concepts/augmentation-region|augmentation-region]]
- [[../concepts/compensation-charge-density|compensation-charge-density]]
- [[../concepts/frozen-core-approximation|frozen-core-approximation]]
- [[../concepts/additive-augmentation|additive-augmentation]]
- [[../concepts/norm-conservation|norm-conservation]]
- [[../concepts/pulay-force|pulay-force]]
- [[../entities/VASP|VASP]]
- [[../entities/LMTO|LMTO]]
- [[../entities/MnFO3|MnFO3]]
- [[../entities/Fe2|Fe2]]
- [[../entities/Wannier90|Wannier90]]
- [[../concepts/norm-conserving-pseudopotential|norm-conserving-pseudopotential]]
