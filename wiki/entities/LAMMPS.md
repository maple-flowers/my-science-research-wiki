---
tags: [entity, density-functional-theory, machine-learning-potential, molecular-dynamics, embedded-atom-method, pair-distribution-function, 2d-materials, strain-engineering, topological-defects, berry-phase, ferroelasticity]
title: LAMMPS
type: entity
status: stub
year: 2019
papers: [Zhang2019a, xuTunableFerroelectricTopological2022, yangRipplingFerroicPhase2021]
updated: 2026-08-18
---

# LAMMPS

> [!warning] 本页内容待重写
> 本页的「太奶导读」与「相关论文」贡献句均为自动生成的占位内容——导读描述的是某篇论文的研究对象，
> 而非本条目本身。**请勿引用本页结论**。已按 SCHEMA 降级为 `stub`。（标记于 2026-08-21）


本文档围绕 **LAMMPS** 汇集 3 篇论文的证据，覆盖其结构、物性与机制等多方面信息。

## 👵 太奶导读

乖孙，这一条讲的是「LAMMPS」，由多篇论文的证据共同支撑。
一句话记住它的发现：二维PbX材料的基态是顺电相。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：已发现的极性拓扑结构（如涡旋、斯格明子）几乎仅限于钙钛矿氧化物超晶格薄膜，其制备复杂且难以实现高度集成。二维（2D）材料的兴起为解决此问题提供了机遇，但其本征的原子级厚度和柔性也带来了新挑战：如何在二维体系中诱导并调控复杂的极性拓扑构图尚属空白。目前已发现多种二维铁电材料，但极少数报道存在极性拓扑结构。PbX（X=S, Se, Te）的基态为高度对称的顺电相，这与传统铁电体不同，暗示其晶格可能对应变有特殊响应。
- **核心问题**：能否利用应变工程，在高度柔性且基态为顺电相的二维材料中，通过设计非均匀应变场，诱导出可调控、可逆的类斯格明子铁电拓扑缺陷结构？这一策略是否能打破极性拓扑态仅存在于钙钛矿体系的限制，为未来纳米电子器件开辟新路径？
- **主要结论**：二维PbX材料的基态是顺电相。施加超过临界值的单轴或剪切应变可诱导其发生可逆的顺电-铁电相变，该过程由声子软模驱动，并伴随巨压电效应。通过建立极化-应变相图，可实现对极化态的精确控制。分子动力学模拟证实，机械压痕产生的非均匀应变场能在薄膜中形成涡旋极性拓扑结构。有限元模拟进一步表明，通过设计基底孔洞形状和薄膜取向，可产生反涡旋、通量闭合等多种可调谐的拓扑极性图案。应变工程是实现二维材料中可设计、可逆极性拓扑态的有效策略。；波纹在二维铁性中扮演双重角色：1）在温度诱导相变中，波纹能稳定高温相的短程铁性序，形成极性纳米微区，这些微区可作为异质形核点，从而显著提高铁性相变温度；2）在应力诱导畴翻转中，波纹将畴翻转从长程协同的雪崩式集体行为，转变为由波纹局域化应力驱动的独立随机过程，表现为应力降统计从幂律分布变为高斯分布。
- **领域贡献**：1. 开辟了“二维材料中的应变驱动拓扑极性态”这一新研究方向。2. 提供了一套完整的多尺度计算方法论，从第一性原理到机器学习再到有限元，为研究力-电耦合下的复杂结构演化提供了范例。3. 发现并系统解释了二维PbX中应变诱导的顺电-铁电相变现象及其物理机制。4. 绘制了首个应变-极化相图，为后续实验和理论研究提供了“设计蓝图”。5. 预测了多种可通过简单力学设计实现的拓扑结构，展示了该技术的巨大应用潜力。；1）揭示了一种二维材料中普遍存在的物理机制，即波纹通过稳定短程有序和局域化长程相互作用来调控铁性相变与畴翻转；2）提出了“波纹工程”的概念，为主动设计二维材料的铁性提供了新的策略；3）为理解一系列实验中观察到的层数依赖的相变行为提供了新的理论框架。
- **研究意义**：理论层面，该研究首次证明了极性拓扑结构并非钙钛矿氧化物所独有，可在二维范德华材料中实现，拓展了极性拓扑物理的认知边界。同时，它建立了“应变场设计-相变控制-拓扑图案编写”的新范式，揭示了力-电-拓扑耦合的新机制。实践层面，为开发基于二维材料的超薄、柔性、高密度、可擦写的拓扑电子学器件（如存储器、传感器）提供了坚实的理论依据和清晰的设计路线图。

## 📚 相关论文 (Related Papers)

- [[../papers/Zhang2019a]]：为本文档提供核心证据。
- [[../papers/xuTunableFerroelectricTopological2022]]：1. 开辟了“二维材料中的应变驱动拓扑极性态”这一新研究方向。
- [[../papers/yangRipplingFerroicPhase2021]]：1）揭示了一种二维材料中普遍存在的物理机制，即波纹通过稳定短程有序和局域化长程相互作用来调控铁性相变与畴翻转；2）提出了“波纹工程”的概念，为主动设计二维材料的铁性提供了新的策略；3）为理解一系列实验中观察到的层数依赖的相变行为提供了新的理论框架。

## 🔗 关联概念与实体 (Related)

- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/machine-learning-potential|machine-learning-potential]]
- [[../concepts/molecular-dynamics|molecular-dynamics]]
- [[../concepts/embedded-atom-method|embedded-atom-method]]
- [[../concepts/pair-distribution-function|pair-distribution-function]]
- [[../concepts/common-neighbor-analysis|common-neighbor-analysis]]
- [[../concepts/icosahedral-structure|icosahedral-structure]]
- [[../concepts/hcp-structure|hcp-structure]]
- [[../concepts/fcc-structure|fcc-structure]]
- [[../concepts/bcc-structure|bcc-structure]]
- [[../concepts/surface-premelting|surface-premelting]]
- [[../concepts/size-dependent-melting|size-dependent-melting]]
- [[../concepts/dulong-petit-law|dulong-petit-law]]
- [[../concepts/five-fold-twinning|five-fold-twinning]]
- [[../concepts/geometric-shell-closure|geometric-shell-closure]]
- [[../concepts/structural-phase-transition|structural-phase-transition]]
