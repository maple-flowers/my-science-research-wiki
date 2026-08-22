---
tags: [concept]
title: '霍尔效应 / Hall Effect'
type: concept
status: mature
domain: [condensed-matter-physics, transport]
mechanism: 载流子在垂直磁场中受洛伦兹力偏转而建立横向霍尔电压
related_concepts: [anomalous-hall-effect, spin-hall-effect, edelstein-effect, spin-transport, topological-insulator, 2d-materials]
papers: ['ivanovskiOscillationStructureHall1994', 'xunCoexistingMagnetismFerroelectric2024', 'pengStrainEngineering2D2020', 'kaurRecentAdvancesTheoretical2025a']
updated: 2026-08
---

# 霍尔效应 / Hall Effect

霍尔效应（Hall effect）指**载流子在垂直磁场中受洛伦兹力偏转而在样品横向建立起霍尔电压**的经典输运现象。其量子与拓扑变体——反常霍尔效应、自旋霍尔效应、量子霍尔效应——是探测电子结构、磁序与拓扑性质的核心实验手段。在二维多铁与滑动铁电体系中，霍尔测量用于表征磁电耦合与自旋输运。

## 👵 太奶导读

给一条通电的扁条加上垂直磁场，里面的电子会被"横向推开"，在扁条两侧积起电压——这就是霍尔效应，简单说就是"磁场让电流走偏"。科学家用这个"走偏程度"反推材料里有多少电荷、磁性多强、甚至有没有奇特的拓扑结构，是研究材料的"万用表"之一。

## 🏗️ 结构概览

霍尔效应是输运测量最基本的探针之一。经典霍尔系数 $R_H = 1/(ne)$ 直接给出载流子密度与符号；其量子化版本（整数量子霍尔、量子反常霍尔）揭示了拓扑不变量；磁性体系中的反常霍尔效应与自旋轨道体系中的自旋霍尔效应则把霍尔测量拓展到磁序与自旋自由度探测。霍尔测量在二维多铁、滑动铁电、应变调控体系中用于表征磁电耦合与自旋输运。

## 🧩 霍尔效应的经典与界面效应

在两种磁导率不同的介质接触面引入 δ 函数势垒后，两侧准朗道态通过共振欠势垒相互作用产生能级避免交叉，直接导致**霍尔电流的振荡与方向翻转**（[[../papers/ivanovskiOscillationStructureHall1994|Ivanovski 1994]]）——表明界面细节可显著调制霍尔响应。

## 🧩 二维多铁与应变体系中的霍尔效应

- **滑移多铁中的磁电表征**：双层 GdI₂ 滑移多铁中，磁性、铁电与铁谷性共存且耦合，霍尔测量是表征其磁序与谷极化的关键手段（[[../papers/xunCoexistingMagnetismFerroelectric2024|Xun 2024]]）。
- **应变调控输运**：单轴/双轴/局部应变可连续调控二维 TMDC 与石墨烯的能带结构，从而调制其霍尔与磁输运性质（[[../papers/pengStrainEngineering2D2020|Peng 2020]]）。
- **滑动铁电理论框架**：第一性原理方法（DFT+Berry phase+NEB）支撑滑动铁电体中自旋轨道耦合相关输运计算（[[../papers/kaurRecentAdvancesTheoretical2025a|Kaur 2025]]）。

## 📋 关键参数表

| 参数 | 含义 | 特征 |
|---|---|---|
| 霍尔系数 $R_H$ | 载流子密度与符号 | $1/(ne)$ |
| 霍尔角 | 电流偏转程度 | 迁移率×磁场 |
| 量子化电导 | 拓扑霍尔 | $C\cdot e^2/h$ |
| 界面势垒 | 霍尔振荡 | 能级避免交叉调制 |

## 🔀 近邻概念辨析

- **霍尔效应 vs 反常霍尔效应**：霍尔需外磁场、非磁性即可；反常霍尔靠自发磁化/贝里曲率、无需外磁场。
- **霍尔效应 vs 自旋霍尔效应**：霍尔产生净电荷横向电压；自旋霍尔产生纯自旋流（无净电荷）。
- **霍尔效应 vs 量子霍尔效应**：经典霍尔为耗散体相响应；量子霍尔为强磁场下的拓扑态，边缘无耗散。

## 📚 相关论文 (Related Papers)

- [[../papers/ivanovskiOscillationStructureHall1994]] — The oscillation structure of the Hall current in the presence of a contact surface
- [[../papers/xunCoexistingMagnetismFerroelectric2024]] — Coexisting Magnetism, Ferroelectric, and Ferrovalley Multiferroic in Stacking-Dependent Two-Dimensional Materials
- [[../papers/pengStrainEngineering2D2020]] — Strain engineering of 2D semiconductors and graphene
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/anomalous-hall-effect|反常霍尔效应]]：磁性体系中的霍尔变体。
- [[../concepts/spin-hall-effect|自旋霍尔效应]]：自旋流-电荷流转换。
- [[../concepts/edelstein-effect|Edelstein 效应]]：自旋轨道耦合的逆过程。
- [[../concepts/spin-transport|自旋输运]]：霍尔测量的应用对象。
- [[../concepts/topological-insulator|拓扑绝缘体]]：霍尔效应研究的拓扑平台。
- [[../concepts/2d-materials|二维材料]]：霍尔效应表征的对象。
- [[../entities/GdI2|GdI₂]]：滑移多铁霍尔表征体系。
- [[../entities/graphene|石墨烯]]：应变调控霍尔输运的经典体系。
*（内容由AI生成，仅供参考）*