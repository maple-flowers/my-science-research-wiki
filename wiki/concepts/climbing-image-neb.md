---
tags: [concept, nudged-elastic-band, minimum-energy-path, saddle-point, transition-state-theory, 2D-materials, altermagnetism, berry-phase, binding-strength, bond-density]
title: climbing-image-neb
type: concept
status: stub
year: 2000
papers: [henkelmanClimbingImageNudged2000c, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08-18
---

# climbing-image-neb

> [!warning] 本页内容待重写
> 本页的「太奶导读」与「相关论文」贡献句均为自动生成的占位内容——导读描述的是某篇论文的研究对象，
> 而非本条目本身。**请勿引用本页结论**。已按 SCHEMA 降级为 `stub`。（标记于 2026-08-21）


本文档围绕 **climbing-image-neb** 汇集 2 篇论文的证据，覆盖其结构、物性与机制等多方面信息。

## 👵 太奶导读

乖孙，这一条讲的是「climbing-image-neb」，由多篇论文的证据共同支撑。
一句话记住它的发现：CI-NEB方法能够在不增加计算成本的情况下，将一幅图像精确地收敛到鞍点，同时保留其他图像对MEP的精确描述。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：寻找MEP和鞍点是计算反应速率的核心挑战。已有的**微动弹性带（NEB）**方法能有效描绘MEP，但其图像是离散的，通常不会恰好落在鞍点上，必须通过插值来估算鞍点能量，这在能垒狭窄时会导致严重的误差，从而影响速率常数的精确计算。
- **核心问题**：如何改进NEB方法，使其能够在保留MEP描绘能力的同时，以零额外的计算成本，让一个图像严格收敛于鞍点，从而消除插值误差，并进一步提升路径在能垒区域的分辨率？
- **主要结论**：CI-NEB方法能够在不增加计算成本的情况下，将一幅图像精确地收敛到鞍点，同时保留其他图像对MEP的精确描述。结合可变弹簧常数，该方法能进一步优化图像分布，显著提升对狭窄能垒的分辨率，从而获得比常规NEB插值更精确的活化能。
- **领域贡献**：1. 提出了一种“攀登图像”概念，以极小的代价解决了NEB方法的鞍点定位不准问题。 2. 系统性地将“真实力”和“弹簧力”解耦，为后续的路径优化方法提供了理论基础。 3. 提供了一种“能量自适应”的图像分布策略，提升了计算资源的利用效率。 4. 该方法已成为计算化学和材料科学中寻找过渡态的标准工具之一。
- **研究意义**：提出了一个简单、高效且通用的改进算法，解决了NEB方法在实际应用中的一个关键痛点，使得精确计算活化能变得更为直接和可靠，对推动基于TST的速率理论计算在催化、材料科学等领域的应用具有重要意义。

## 📚 相关论文 (Related Papers)

- [[../papers/henkelmanClimbingImageNudged2000c]]：1. 提出了一种“攀登图像”概念，以极小的代价解决了NEB方法的鞍点定位不准问题。
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：为本文档提供核心证据。

## 🔗 关联概念与实体 (Related)

- [[../concepts/nudged-elastic-band|nudged-elastic-band]]
- [[../concepts/minimum-energy-path|minimum-energy-path]]
- [[../concepts/saddle-point|saddle-point]]
- [[../concepts/transition-state-theory|transition-state-theory]]
- [[../concepts/potential-energy-surface|potential-energy-surface]]
- [[../concepts/rare-events|rare-events]]
- [[../concepts/force-projection|force-projection]]
- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/harmonic-tst|harmonic-tst]]
- [[../concepts/variable-spring-constant|variable-spring-constant]]
- [[../entities/VASP|VASP]]
- [[../entities/Ir-111|Ir-111]]
- [[../entities/Si-100|Si-100]]
- [[../concepts/altermagnetism|altermagnetism]]
- [[../concepts/berry-phase|berry-phase]]
- [[../concepts/binding-strength|binding-strength]]
