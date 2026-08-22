---
tags: [concept, ferroelectric, multiferroic, symmetry-breaking]
title: '几何铁电性 / Geometric Ferroelectricity'
type: concept
status: developing
domain: [ferroelectricity, multiferroics, symmetry-breaking]
mechanism: "极化来自多面体协同旋转/倾斜等几何畸变模式的耦合，而非 B 位离子偏心位移或孤对电子，因此可与磁性所需的部分填充 d 轨道共存"
related_concepts: [ferroelectricity, improper-ferroelectricity, hybrid-improper-ferroelectricity, multiferroicity, d0-rule, magnetoelectric-coupling, octahedral-rotation, charge-ordered-ferroelectricity]
related_entities: [YMnO3, CrSBr, LiOsO3, BiMnO3]
papers: ['hillWhyAreThere2000a', 'spaldinRenaissanceMagnetoelectricMultiferroics2005', 'fiebigEvolutionMultiferroics2016', 'rameshMultiferroicsProgressProspects2007', 'yuFerroelectricControlMagnetism2026', 'bhowalPolarMetalsPrinciples2023b']
updated: 2026-08
---

# 几何铁电性 / Geometric Ferroelectricity

几何铁电性（geometric ferroelectricity）指**由结构几何约束而非孤对电子或电荷有序直接驱动**的铁电极化机制：极化作为**空间群对称性的必然结果**出现，源于多面体协同旋转/倾斜等几何畸变模式，其本身并不依赖 B 位离子的偏心位移（d⁰ 规则失效的情形）。典型代表是六方钙钛矿 YMnO₃ 与层状混合非本征（hybrid improper）体系。它属于多铁性四大起源机制之一（孤对电子、几何、电荷有序、自旋驱动）。

## 👵 太奶导读

一般铁电体靠"中心原子坐歪"产生电（像跷跷板一边压下去）；但有些材料里原子坐得很正，却在**整体"拧麻花"**——氧八面体集体旋转、层与层错位堆叠，这种"拧"出来的不对称也能产生电场。这就叫几何铁电性。它的好处是：不需要牺牲磁性需要的 d 电子，给"又有电又有磁"的多铁材料开了条新路。

## 🧩 起源机制：几何畸变与对称性降维

几何铁电性的核心是**非极性畸变模式的耦合**：多个旋转/倾斜模式（如 a⁻a⁻c⁺）在界面或块体中共存时，其二次耦合项可诱导出极性模式（K_3 等），从而在**对称性不允许单个离子偏心**的结构中生成极化。这类机制使铁电极化与**磁性所需的部分填充 d 轨道可以共存**——这正是 d⁰ 规则（[[../concepts/d0-rule|d⁰规则]]）制约下铁电-铁磁互斥的一种突破路径（[[../papers/hillWhyAreThere2000a|Hill 2000]]）。Spaldin 在复兴磁电多铁的纲领性论述中，将几何铁电列为单相非常规机制的核心方向之一（[[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005|Spaldin 2005]]）。

## 📚 分类体系：四大起源之一

Fiebig 等以"I 类/II 类多铁"为主线，系统梳理了铁电性四大起源——孤对电子、几何、电荷有序、自旋驱动，其中**几何铁电**与**电荷有序铁电**均绕开 d⁰ 规则，是实现铁电-磁序共存的关键非常规机制（[[../papers/fiebigEvolutionMultiferroics2016|Fiebig 2016]]）。Ramesh 等则在薄膜层面总结了"单相薄膜—水平异质结—垂直异质结"三种架构，指出几何铁电在异质结界面工程中的潜力（[[../papers/rameshMultiferroicsProgressProspects2007|Ramesh 2007]]）。

## 🔬 最新进展：二维与插层设计

- **二维多铁插层**：Yu 等通过卤素离子 F 插层将双层 CrSBr"融合"为单层 Cr₄S₄FBr₂，利用 F 位移诱导的 Jahn–Teller 畸变打破反演对称——一种**人工几何/轨道驱动的铁电极化**，并在 CSFB/CrSBr/CSFB 隧道结中实现极化翻转驱动的 4.8×10³% 巨磁阻（[[../papers/yuFerroelectricControlMagnetism2026|Yu 2026]]）。
- **铁电金属中的几何起源**：LiOsO₃ 等铁电金属的极化被归因于结构畸变模式，几何驱动图像对理解"极性+金属"共存至关重要（[[../papers/bhowalPolarMetalsPrinciples2023b|Bhowal 2023]]）。

## 🧭 近邻概念辨析

| 对比对象 | 关键区别 |
| :--- | :--- |
| [[../concepts/ferroelectricity\|本征位移型铁电]] | 极化即一级序参量，由 B 位离子偏心软模直接驱动（需 d⁰ 构型）；几何铁电的极化是几何畸变的**次级产物** |
| 孤对电子机制（[[../entities/BiMnO3\|BiMnO₃]] 类） | 靠 A 位 Bi³⁺ 6s² 孤对与 O 2p 的强共价键提供铁电驱动力，属**化学驱动**；几何铁电靠离子半径与容忍因子稳定非中心对称骨架，属**结构驱动**（[[../papers/hillWhyAreThere2000a\|Hill 2000]]） |
| [[../concepts/hybrid-improper-ferroelectricity\|混合非本征铁电 HIFE]] | HIFE 特指**两个及以上非极性畸变模式二次耦合**才生成极化（RP 相/双钙钛矿层状体系）；几何铁电是更宽的类别，含 YMnO₃ 这类单一几何骨架即非中心对称的情形 |
| [[../concepts/charge-ordered-ferroelectricity\|电荷有序铁电]] | 极化源于电荷/价态在晶位间的不等价排布；与几何铁电同为绕开 d⁰ 规则的路径，但机制无关（[[../papers/fiebigEvolutionMultiferroics2016\|Fiebig 2016]]） |
| [[../concepts/spin-driven-ferroelectricity\|自旋驱动铁电]] | 属 II 类多铁，极化由磁序直接诱导、随磁序一同消失；几何铁电属 I 类，极化与磁序**独立起源** |

## 🔬 关键参数表

| 参数 | 数值 | 对象与条件 | 证据类型 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| 垂直极化 | 1.1 pC/m | 单层 Cr₄S₄FBr₂，F 原子位移诱导 | 第一性原理计算 | [[../papers/yuFerroelectricControlMagnetism2026]] |
| 极化翻转势垒 | 0.11 eV | 单层 Cr₄S₄FBr₂ | 第一性原理计算 | [[../papers/yuFerroelectricControlMagnetism2026]] |
| 铁电居里温度 | 334 K | 单层 Cr₄S₄FBr₂ | 计算预测 | [[../papers/yuFerroelectricControlMagnetism2026]] |
| Néel 温度 | 469 K | 单层 Cr₄S₄FBr₂（A 型完全补偿亚铁磁） | 计算预测 | [[../papers/yuFerroelectricControlMagnetism2026]] |
| 隧道磁电阻 | 4.8 × 10³ % | CSFB/CrSBr/CSFB 多铁隧道结，纯电场驱动 | 计算预测 | [[../papers/yuFerroelectricControlMagnetism2026]] |

> ⚠️ 证据边界：上表全部来自同一篇计算工作对 Cr₄S₄FBr₂ 这一**预测材料**的结果，尚无实验值；YMnO₃ 等经典六方几何铁电的极化与 T_C 在本库现有论文中只有定性讨论、无可核验数值，故未列入。

## 📚 相关论文 (Related Papers)

- [[../papers/hillWhyAreThere2000a]] — Why Are There so Few Magnetic Ferroelectrics?：提出 d⁰ 规则并明确指出「结构驱动」是绕开该规则的两条路径之一，以小半径 Y³⁺ 稳定本身非中心对称的六方 YMnO₃ 结构为例，是本页机制的原始出处。
- [[../papers/fiebigEvolutionMultiferroics2016]] — The evolution of multiferroics：以 I 类/II 类为主线确立了铁电四大起源分类（孤对电子、几何、电荷有序、自旋驱动），为本页在分类体系中定位提供权威框架。
- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]] — The Renaissance of Magnetoelectric Multiferroics：把「单相探索新机制」列为磁电多铁复兴的两大范式之一，几何铁电即该范式下的核心非常规机制。
- [[../papers/rameshMultiferroicsProgressProspects2007]] — Multiferroics: progress and prospects in thin films：提出「单相薄膜—水平异质结—垂直异质结」三种架构范式，指出几何铁电在界面与应变工程中的可调空间。
- [[../papers/yuFerroelectricControlMagnetism2026]] — Ferroelectric Control of Magnetism and Giant Magnetoresistance...：本页唯一提供完整定量数据的工作，用 F 插层诱导 Jahn–Teller 畸变破缺反演对称，实现极化-自旋-Chern 数锁定。
- [[../papers/bhowalPolarMetalsPrinciples2023b]] — Polar Metals: Principles and Prospects：把几何铁电列为「极化与导电电子解耦」的机制之一，说明几何起源对理解 LiOsO₃ 这类极性金属的必要性。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：几何铁电是铁电性的非常规起源之一。
- [[../concepts/improper-ferroelectricity|非本征铁电性]]：几何铁电多为非本征（极化为次级序参量）性质。
- [[../concepts/hybrid-improper-ferroelectricity|混合非本征铁电性]]：旋转-倾斜双模耦合诱导极化的具体子机制。
- [[../concepts/octahedral-rotation|八面体旋转]]：几何畸变的主要模式载体。
- [[../concepts/charge-ordered-ferroelectricity|电荷有序铁电]]：与几何铁电并列的另一条绕开 d⁰ 的路径。
- [[../concepts/spin-driven-ferroelectricity|自旋驱动铁电]]：II 类多铁对照机制，用于区分极化是否独立于磁序。
- [[../concepts/multiferroicity|多铁性]]：几何铁电与磁序共存的核心价值。
- [[../concepts/d0-rule|d⁰规则]]：几何铁电绕开的那条限制。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：几何铁电体系实现电场调控磁性的基础。
- [[../entities/YMnO3|YMnO₃]]：六方几何铁电的原型材料。
- [[../entities/CrSBr|CrSBr]]：插层诱导对称性破缺实现几何铁电的二维母体。
- [[../entities/LiOsO3|LiOsO₃]]：几何畸变驱动极性、且保持金属性的极性金属实例。
- [[../entities/BiMnO3|BiMnO₃]]：孤对电子机制对照体系。
