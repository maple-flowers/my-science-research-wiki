---
tags: [entity, charge-density-wave, density-functional-theory, 2D-materials, fermi-surface-nesting, wannier-function, spin-orbit-coupling, superconductivity, 2d-materials, strong-coupling, dielectric-function]
title: WIEN2k
type: entity
status: developing
year: 2006
papers: [Barnett2006coexistence, Johannes2008fermi, Koley2020charge, gajdosLinearOpticalProperties2006, songEvidenceSinglelayerVan2022]
updated: 2026-08-18
---

# WIEN2k

本文档围绕 **WIEN2k** 汇集 5 篇论文的证据，覆盖其结构、物性与机制等多方面信息。

## 👵 太奶导读

乖孙，这一条讲的是「WIEN2k」，由多篇论文的证据共同支撑。
一句话记住它的发现：2H-TMDs的低能电子结构由次近邻跃迁（t₂）主导，远超最近邻跃迁（t₁）。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：角分辨光电子能谱（ARPES）实验反复观察到，在2H-TMDs（如2H-TaSe₂）进入公度CDW相后，其费米面上并未打开预期的能隙，依然存在无隙的电子激发，这与传统CDW理论（认为CDW会导致费米面全打开能隙，材料变为绝缘体）形成尖锐矛盾。同时，关于CDW的驱动机理（费米面嵌套矢量）也存在定量争议。
- **核心问题**：作者旨在解决一个核心的定性矛盾：为何在2H-TMDs中，公度CDW相的费米面上观察不到能隙的打开？作者试图找到一个简洁的物理机制，以解释“无隙激发”与“公度CDW”这一反常共存现象。
- **主要结论**：2H-TMDs的低能电子结构由次近邻跃迁（t₂）主导，远超最近邻跃迁（t₁）。这一反常特性导致其三角晶格可近似解耦为三个独立的子晶格。在CDW畸变中，只有一个子晶格保持未畸变，与之相关的电子能带因此不打开能隙，从而在费米面上保留了无隙激发，完美解释了公度CDW与金属性共存的实验现象。；1. 派尔斯机制中的纯电子不稳定性极其脆弱，易被温度、散射和微小几何偏差破坏。2. 在NbSe₂、TaSe₂和CeTe₃等典型材料中，费米面嵌套的峰值与实际的CDW波矢不一致，不具有预测能力。3. CDW的本质是电子-声子耦合驱动的结构相变，电子和离子子系统协同作用，不可分割。4. 因此，在物理上无法对“CDW”和“非公度晶格转变 (ILT)”做出有意义的区分。；非磁性无序通过破坏CDW的长程有序性，尤其是团簇无序，能有效促进超导电性的重入和增强。其机制是，在强耦合图像下，无序破坏了“预成型激子”的凝聚，从而压制了CDW，而s波超导性由于安德森定理对非磁性无序具有鲁棒性，因此得以显现并占据主导。DFT+DMFT计算成功复现了TaSeS合金在~5K的超导转变。；成功推导的PAW纵向表达式，在标准PAW势下即可获得与全电子APW+LO方法高度一致的静态和动态介电函数，其精度和收敛速度均显著优于传统的横向表达式。横向表达式在标准势下的误差源于其忽略了一个关键的偶极矩修正项，而纵向表达式自然地包含了这一修正。密度泛函微扰理论的结果与对导带求和的结果完全一致，进一步验证了新理论框架的自洽性。；在单层二碘化镍中，一种特定的螺旋磁序（proper-screw）能够在21 K以下稳定存在，它打破了空间反演对称性和三重旋转对称性，从而直接诱导出沿特定晶轴方向的铁电极化。这种多铁性态在从块材到单层的演化中持续存在，其相变温度随层数减少而单调降低，揭示了层间交换耦合在稳定该多铁序中的重要作用。
- **领域贡献**：1. 解决了困扰领域二十年的ARPES实验谜题。2. 揭示了“次近邻跃迁主导”这一反常电子结构特征。3. 提出了“子晶格解耦”这一普适性物理图像，为理解其他复杂CDW体系提供了新范式。；1. 澄清了“费米面嵌套”和“派尔斯CDW”等核心概念的模糊性，并设定了严格的适用条件。2. 通过理论和计算，有力地解构了旧范式，确立了电子-声子耦合在CDW形成中的核心地位。3. 提供了方法论上的警示，即仅凭费米面拓扑或χ′′(q) 判断CDW是错误的，必须分析χ′(q) 和整个能带的贡献。；1) 提出了一个自洽的强耦合理论范式，将CDW视为预成型激子的凝聚，成功解释了TMDs中无序诱导SC增强的实验现象。2) 揭示了无序“类型”（团簇vs.随机）在调控竞争序中的关键作用。3) 通过BdG和DFT+DMFT两种互补方法，从唯象和第一性原理层面共同验证了理论，架起了模型计算与真实材料物理之间的桥梁。；提供了一套在PAW方法中计算光学性质的精确闭合公式，将PAW方法的光学计算精度提升到了全电子方法水平。阐明了纵、横向表达式在PAW框架下差异的物理根源，即PAW球内的偶极矩修正。为在VASP等主流PAW软件中实现高精度光学性质计算奠定了理论基础，并对后续GW-BSE等高级计算具有重要支撑作用。；1. 实验上确立了单层二碘化镍作为本征二维多铁体的地位，开创了“范德华多铁性”这一新研究方向。2. 发展了一套用于表征二维极限下复杂多铁序（同时含磁序、极性序、手性序）的多模态光学方法学范本。3. 定量揭示了层间交换作用和磁各向异性在稳定二维多铁性中的关键作用，为设计新型二维多铁材料提供了理论指导。
- **研究意义**：理论层面，解决了一个长期存在的实验谜题，提出了“子晶格解耦”这一新颖的物理机制来解释CDW态中的金属性，更新了对2H-TMDs类材料电子结构的传统认知。方法论层面，展示了第一性原理计算与简约模型思维的有机结合，是从复杂计算提炼核心物理的典范。

## 📚 相关论文 (Related Papers)

- [[../papers/Barnett2006coexistence]]：1. 解决了困扰领域二十年的ARPES实验谜题。
- [[../papers/Johannes2008fermi]]：1. 澄清了“费米面嵌套”和“派尔斯CDW”等核心概念的模糊性，并设定了严格的适用条件。
- [[../papers/Koley2020charge]]：1) 提出了一个自洽的强耦合理论范式，将CDW视为预成型激子的凝聚，成功解释了TMDs中无序诱导SC增强的实验现象。
- [[../papers/gajdosLinearOpticalProperties2006]]：提供了一套在PAW方法中计算光学性质的精确闭合公式，将PAW方法的光学计算精度提升到了全电子方法水平。
- [[../papers/songEvidenceSinglelayerVan2022]]：1. 实验上确立了单层二碘化镍作为本征二维多铁体的地位，开创了“范德华多铁性”这一新研究方向。

## 🔗 关联概念与实体 (Related)

- [[../concepts/charge-density-wave|charge-density-wave]]
- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/fermi-surface-nesting|fermi-surface-nesting]]
- [[../concepts/wannier-function|wannier-function]]
- [[../concepts/tight-binding|tight-binding]]
- [[../concepts/sublattice-decoupling|sublattice-decoupling]]
- [[../concepts/hopping-integral|hopping-integral]]
- [[../concepts/gapless-excitation|gapless-excitation]]
- [[../concepts/electron-phonon-coupling|electron-phonon-coupling]]
- [[../concepts/commensurate-cdw|commensurate-cdw]]
- [[../concepts/phase-interference|phase-interference]]
- [[../entities/TMDs|TMDs]]
- [[../entities/2H-TaSe2|2H-TaSe2]]
- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/hidden-nesting|hidden-nesting]]
- [[../concepts/electronic-susceptibility|electronic-susceptibility]]
