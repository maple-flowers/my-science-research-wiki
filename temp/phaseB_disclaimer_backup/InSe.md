---
tags: [entity, material, 2D, vdW, ferroelectric]
title: 硒化铟 (InSe) / Indium Selenide
type: entity
formula: InSe
class: [vdW, III-VI-chalcogenide, semiconductor]
status: mature
properties: [sliding-ferroelectricity, piezoelectricity]
related_concepts: [sliding-ferroelectricity, piezoelectricity, stacking-engineered-ferroelectricity]
related_entities: [GaSe, In2Se3]
papers: [sunSlidingFerroelectricityTwodimensional2025, wuSlidingFerroelectricity2D2021a, zhangEmergingFrontiersTwodimensional2025]
updated: 2026-08
---



# 硒化铟 (InSe) / Indium Selenide

InSe（硒化铟）是 III-VI 族层状半导体，常见多型为六方结构（如 4H/γ 相），层间为范德华相互作用。γ-InSe 单层因其非中心对称堆垛被理论预测并在实验上验证为**滑动铁电体**，是 III-VI 族滑动铁电材料的代表之一。其面外极化可通过层间滑移翻转，且体系兼具良好压电响应（Y 掺杂 γ-InSe 的 $d_{33}$ 可达约 7.5 pm/V），在超薄铁电器件与压电-铁电耦合应用中具有潜力。

## 👵 太奶导读

太奶，InSe（硒化铟，铟和硒组成的层状材料）也是像"花格子布"一样可以**搓一搓就带电**的材料（滑动铁电）。不过它还有个特别之处：它天生是"**歪着叠**"的（γ 相，非中心对称堆垛），也就是说不用您动手搓，它天然就带着一层不均匀的电荷分布，有淡淡的电性；您再动手一搓，这电性就能翻转方向。

而且它"身板"特别软乎（柔性、机械性能好），对它施加压力，它就能把机械形变直接变成电信号（这叫**压电效应**）——好比捏一下橡皮泥，它就发出一个电脉冲。科学家正在琢磨怎么用它做既灵活又能记能感应的"电子皮肤"和超薄芯片。

## 🏗️ 结构概览

InSe 为 III-VI 族层状半导体，单层由 Se–In–In–Se 四原子层构成，层间为范德华相互作用。γ-InSe（4H 多型）的**非中心对称堆垛**使其在单层/少层极限下具有面外极性，是滑动铁电的结构基础（[[../papers/sunSlidingFerroelectricityTwodimensional2025]]）。

![图：二维滑动铁电材料谱系时间线（含 γ-InSe）](../../raw/figures/sunSlidingFerroelectricityTwodimensional2025/fig_2_668MSTBJ.png)
- **看图要点**：二维滑动铁电体从理论预测到实验验证的发展时间线与材料谱系，γ-InSe 属实验验证行列。
- **来源**：[[../papers/sunSlidingFerroelectricityTwodimensional2025]] -> [[../figures/crystal-structures-bulk|体相晶体结构]]

## 🧩 滑动铁电机制

- γ-InSe 单层因非中心对称堆垛具有本征面外极性，极化强度为 **pC/m 量级**，可通过层间滑移实现极化翻转（[[../papers/sunSlidingFerroelectricityTwodimensional2025]]）。
- 作为 III-VI 族代表，其滑动铁电机制与 III-VI 族层状化合物的堆垛工程（3R 菱方堆叠路径）直接相关，可与 GaSe 等姊妹体系横向比较。

## 🧩 压电-铁电耦合

- Y 掺杂 γ-InSe 的压电系数 $d_{33}$ 可达约 **7.5 pm/V**，体现了滑动铁电体系在机械-电学耦合方面的应用价值（[[../papers/sunSlidingFerroelectricityTwodimensional2025]]）。
- 铁电极化与压电响应的耦合使 InSe 成为柔性传感、能量收集与铁电器件交叉应用的候选材料。

## 🔬 物理参数表

| 属性 | 数值 | 方法与来源 |
| :--- | :--- | :--- |
| 单层面外极化 | pC/m 量级 | 理论预测/实验（[[../papers/sunSlidingFerroelectricityTwodimensional2025]]） |
| 压电系数 $d_{33}$（Y 掺杂） | ~7.5 pm/V | 计算/实验（[[../papers/sunSlidingFerroelectricityTwodimensional2025]]） |
| 堆垛类型 | 4H / γ 非中心对称 | 结构（[[../papers/sunSlidingFerroelectricityTwodimensional2025]]） |

> 注：上表为理论/实验典型结果，适用对象与条件已在数值中标注，详细来源见 📚 相关论文 节。

## 🧭 近邻体系辨析

- **与 GaSe 的区别**：GaSe 与 InSe 同为 III-VI 族层状半导体，GaSe 滑动铁电极化约 6.19 pC/m（作为 III-VI 族参照较强）；InSe（γ 相）为实验验证的滑动铁电体，两者互为姊妹体系，堆垛构型与极化强度可横向对比。
- **与 In₂Se₃ 的区别**：α-In₂Se₃ 是"偶极锁定"型铁电（面内与面外极化互锁、翻转伴随层间剪切滑移）；InSe（γ 相）是纯滑动铁电（极化直接由非中心对称堆垛产生），二者机制不同但同属 In-Se 家族，需注意区分。
- **与 HgI₂、ReS₂ 的区别**：HgI₂ 极化为 μC/cm² 量级、ReS₂ 极化随层数累积至 0.68 pC/m；InSe（γ 相）极化在 pC/m 量级，强度适中但兼具压电响应与 III-VI 族柔性平台优势。

## 📚 相关论文 (Related Papers)

- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：系统综述了滑动铁电的原理、材料谱系与器件应用，将 γ-InSe 列为实验验证的 III-VI 族滑动铁电体并给出压电数据。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：从综述角度梳理了「Sliding ferroelectricity in 2D van der Waals materials」，为 InSe 类滑动铁电体系提供了通用物理框架。
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]：从综述角度梳理了「二维滑动铁电体的新兴前沿」，涵盖 InSe 等体系的最新进展。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/piezoelectricity|压电性]]
- [[../concepts/stacking-engineered-ferroelectricity|堆垛工程铁电]]
- [[../entities/GaSe|GaSe]]
- [[../entities/In2Se3|In2Se3]]
*（内容由AI生成，仅供参考）*
