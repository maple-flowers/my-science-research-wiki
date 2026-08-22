---
tags: [concept, ferroelectricity, mechanical-response, 2d-materials, strain-engineering]
title: 压电性 / Piezoelectricity
type: concept
status: mature
year: 2021
domain: [condensed-matter-physics, ferroics, mechanical-engineering]
mechanism: 非中心对称晶体中机械应力通过离子/电子位移诱导电极化（正压电），或外电场诱导应变（逆压电）
related_concepts: [ferroelectricity, ferroelasticity, pyroelectricity, strain-engineering, born-effective-charge, modern-polarization-theory, ferroelectric-domain]
papers: [king-smithTheoryPolarizationCrystalline1993, yangStrainEngineeringTwodimensional2021]
updated: 2026-08-19
---

# 压电性 / Piezoelectricity

压电性（piezoelectricity）指**非中心对称晶体在外加机械应力下产生电极化**（正压电效应），或反之**在外电场作用下产生机械应变**（逆压电效应）的线性机电耦合特性。它是铁电、铁弹等极性功能材料的基础物性之一，广泛用于传感器、致动器、能量采集与射频滤波。

## 👵 太奶导读

太奶啊，有种材料很"会来事"：你用力捏它，它脸上就会生出电（正压电）；反过来你给它充上电，它就会鼓起来或缩下去（逆压电）。这就好比"捏一捏出电、充一充变形"。打火机的打火石、医院 B 超的探头、手机里调频率的滤波器，靠的都是这个本事。

## 🏗️ 结构概览

压电性是晶体对称性的直接后果：仅**非中心对称**（无空间反演中心）的 20 类点群可具有压电性，其中 10 类同时为极性点群（可具热释电）。按材料谱系分为：钙钛矿氧化物（BaTiO₃、PZT、LiNbO₃）、纤锌矿（AlN、ZnO）、聚合物（PVDF）与二维压电（TMD、In₂Se₃）。

## 🧩 核心内容与机制 (Core Content)

### 1. 物理图像

应力打破正负电荷中心的重合，产生净极化；其线性耦合张量由压电系数 d/e 表征。微观看，极化由离子位移与电子响应共同贡献，严格计算需借助现代极化理论（[[../papers/king-smithTheoryPolarizationCrystalline1993|King-Smith & Vanderbilt 1993]]）——将极化变化定义为绝热路径上的 Berry 相位，从而绕开"任意相位"问题。

### 2. 与铁电、铁弹的关系

- 铁电体必为压电体（极化可翻转，故可被应力诱导）；压电体不一定铁电（无滞回）。
- 铁弹体因应变-极化耦合也常具压电响应。
- 压电-铁电耦合使应变成为调控二维材料光、电、磁性能的有效手段（[[../papers/yangStrainEngineeringTwodimensional2021|Yang 2021]]）。

### 3. 二维压电与应变工程

二维非中心对称材料（如单层 MoS₂、In₂Se₃）展现增强的柔性压电，可用于柔性传感器与能量采集；应变工程通过界面传递高效调控其带隙、迁移率与压电/压阻响应（[[../papers/yangStrainEngineeringTwodimensional2021|Yang 2021]]）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 压电系数 d | 应变↔极化线性耦合 | pm/V 或 pC/N 量级 |
| 机电耦合系数 | 机电能量转换效率 | 依赖材料与模式 |
| 居里点 | 压电性消失温度 | 与铁电相变相关 |
| 对称性要求 | 必要条件 | 非中心对称（20 类点群） |
| 维数 | 体相/二维 | 2D 柔性可弯折 |

## 🔀 近邻概念辨析

- **压电 vs 铁电**：压电是被动线性响应、无滞回；铁电要求自发极化可被电场翻转（滞回线），且铁电必压电。
- **压电 vs 热释电**：热释电是温度变化诱导极化（需极性点群）；压电是应力诱导极化（仅需非中心对称）。
- **压电 vs 应变工程**：应变工程是"以应变作为调控手段"的方法学，压电是其中可利用的物理效应之一。

## 📚 相关论文 (Related Papers)

- [[../papers/king-smithTheoryPolarizationCrystalline1993]]：现代极化理论奠基，为压电极化的严格量子力学定义提供框架。
- [[../papers/yangStrainEngineeringTwodimensional2021]]：二维材料应变工程综述，覆盖压电/压阻效应与柔性器件。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/ferroelasticity|铁弹性]]
- [[../concepts/strain-engineering|应变工程]]
- [[../concepts/born-effective-charge|Born 有效电荷]]
- [[../concepts/modern-polarization-theory|现代极化理论]]
- [[../concepts/ferroelectric-domain|铁电畴]]
- [[../entities/BaTiO3|BaTiO₃]]
