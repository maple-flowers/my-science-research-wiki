---
tags: [concept, berry-phase, berry-connection, wannier-function, born-effective-charge]
title: modern-polarization-theory
type: concept
status: developing
year: 1993
papers: [king-smithTheoryPolarizationCrystalline1993, sunSlidingFerroelectricityTwodimensional2025]
updated: 2026-08-18
---

# modern-polarization-theory

本文档围绕 **modern-polarization-theory** 汇集 2 篇论文的证据，覆盖其结构、物性与机制等多方面信息。

## 👵 太奶导读

乖孙，这一条讲的是「modern-polarization-theory」，由多篇论文的证据共同支撑。
一句话记住它的发现：: 建立了绝对极化差值与“相位弛豫图”的等效性。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：晶体极化的实验有广泛应用在铁电、压电中，但原子论框架下直接计算“极化变化量”长期未解，J*没有以协变方式定义“绝对极化”，导致形式化理论与现代多体第一性原理计算脱节。本文旨在提供可实现的理论框架。
- **核心问题**：主要在于为理论与计算摇篮间的鸿沟架桥——如何从原子论层面严格推导一个在实际DFT基计算机语境下能用局部价波函数**数值计算**并限定“任意相位”干扰下的的极化变化?
- **主要结论**：: 建立了绝对极化差值与“相位弛豫图”的等效性；“规范自由度”的剩余被化为`归一化模`（量子）；实际数值优于。并与线性响应理论计算结果偏差<5，进而明确说明电子响应对综合死电物理的特征独立。；滑动铁电性是二维范德华材料中普遍存在的一种通过层间滑移产生垂直极化并实现翻转的机制。它具有原子级厚度、极低的翻转能垒、超快开关速度和本征的抗疲劳特性，这些优势源于其独特的、不涉及强离子位移的物理过程。通过控制层数、堆叠构型（如3R相）和扭转角，可以对极化进行有效调控。该特性已在多种材料中得到实验验证，并在FeFET、FTJ、突触模拟等原型器件中展现出卓越性能，有望克服传统铁电材料的局限性，并推动存算一体等新型计算架构的发展。
- **领域贡献**：为后续边界IP（现代极化理论）到达原始发初端点；提供了α标准处理方法；发表了现代实现对“自发极化极值算法”的评价基石（如现代铁电材料构型研究），同时引入相位几何的概念影响到拓扑物理。；本综述最重要的贡献是提供了一个构建该领域知识体系的系统性框架。它将滑动铁电性从基本原理、材料数据库、制备与表征工具箱，到器件应用谱系进行了全面整合与逻辑重构，清晰地连接了“物理机制-材料体系-功能器件”三大板块。特别是，它明确划分了实现滑动铁电性的三种主要途径（3R相、扭转角、莫尔超晶格），并系统比较了不同材料体系的性能和优劣，为后续研究者提供了一个快速入门的导航图和构建新研究的参考基准。
- **研究意义**：实现对**宏观极化**由量子力学波函数直接积分并进行一定粟子；为铁电/压电材料的第一性原理计算设计了一种不依赖于激发态的超衬底从而具有普适性；是穴坐现代“Polarization geometry”的基础。

## 📚 相关论文 (Related Papers)

- [[../papers/king-smithTheoryPolarizationCrystalline1993]]：为后续边界IP（现代极化理论）到达原始发初端点；提供了α标准处理方法；发表了现代实现对“自发极化极值算法”的评价基石（如现代铁电材料构型研究），同时引入相位几何的概念影响到拓扑物理。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：本综述最重要的贡献是提供了一个构建该领域知识体系的系统性框架。

## 🔗 关联概念与实体 (Related)

- [[../concepts/berry-phase|berry-phase]]
- [[../concepts/berry-connection|berry-connection]]
- [[../concepts/wannier-function|wannier-function]]
- [[../concepts/born-effective-charge|born-effective-charge]]
- [[../concepts/polarization-quantum|polarization-quantum]]
- [[../concepts/piezoelectricity|piezoelectricity]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/ferroelectricity|ferroelectricity]]
- [[../entities/GaAs|GaAs]]
- [[../entities/VASP|VASP]]
- [[../entities/Wannier90|Wannier90]]
- [[../entities/Quantum-ESPRESSO|Quantum-ESPRESSO]]
