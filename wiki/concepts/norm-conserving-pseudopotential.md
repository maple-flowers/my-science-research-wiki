---
tags: [concept]
title: '模守恒赝势 / Norm-Conserving Pseudopotential'
type: concept
status: developing
papers: ['kresseUltrasoftPseudopotentialsProjector1999c', 'shishkinImplementationPerformanceFrequencydependentGWmethod2006', 'chowdhuryReviewTheoreticalComputational', 'Li2013bonding', 'king-smithTheoryPolarizationCrystalline1993', 'niuDirectVisualizationLargeScale2021']
updated: 2026-08-18
---

# 模守恒赝势 / Norm-Conserving Pseudopotential

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


模守恒赝势（norm-conserving pseudopotential, NCPP）是**保证赝波函数与真实全电子波函数在芯区外具有相同模（norm）与散射性质**的离子赝势。它由 Hamann、Schlüter 与 Chiang 于 1979 年系统提出，通过约束赝波函数在截断半径 r_c 内平滑化、并在 r_c 外与原波函数一致，确保赝势在较大能量范围内精确再现真实散射相移，从而给出可靠的能带与总能量。它与超软赝势（US-PP）、投影增强波（PAW）共同构成第一性原理计算中处理离子-电子相互作用的三大主流方案。

## 👵 太奶导读

原子的"芯电子"又紧又多，直接算特别费劲，就像要精确画出一座冰山的水下部分。模守恒赝势的做法是：把"水下冰山"（芯电子）用一个平滑的"浮标"代替，只保证"吃水线以上"（价电子区）的形状和"排水量"（电子数）完全一样——浮标的"排水量"和真冰山一模一样，这样算海浪（成键）就既快又准。它的代价是"浮标"做得越精细越费算力，于是后来有了更省劲的"超软"和 PAW 方法。

## 🧩 核心思想：模守恒约束

模守恒赝势的关键约束是**赝波函数与全电子波函数的模守恒**：对每个角动量通道 l，要求 ∫₀^{r_c}|R^{PS}_{l}(r)|² r² dr = ∫₀^{r_c}|R^{AE}_{l}(r)|² r² dr。这一约束保证了：
- 赝势在**多个能量**下再现真实散射相移（广义模守恒）；
- 赝波函数与真实波函数在 r_c 外**完全相同**；
- 由此得到的总能量、电荷密度与力在化学环境下可靠。

模守恒赝势因此成为**平面波基组**（[[../concepts/plane-wave-basis|平面波基组]]）DFT 计算的经典标准，也是后续更高效方案（US-PP、PAW）的参照基准。

## 🔬 与超软赝势、PAW 的关系

Kresse 与 Joubert 严格证明了 **US-PP 是 PAW 的线性化近似**：超软赝势的总能量泛函可由稍作修改的 Blöchl PAW 泛函对两个原子中心项作一阶线性化得到，并给出在现有 US-PP 平面波程序中实现 PAW 的最简路径（[[../papers/kresseUltrasoftPseudopotentialsProjector1999c|Kresse & Joubert 1999]]）。三者中 NCPP 精度与传输性经典、实现直观，US-PP/PAW 以更小的基组换取计算效率，是现代 VASP 等程序的主流选择。在 PAW 框架内，还可实现全频率依赖的 G₀W₀ 准粒子计算（[[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006|Shishkin 2006]]），即 [[../concepts/gw-approximation|GW 近似]]。

## 📐 在材料模拟中的应用

赝势选择直接影响第一性原理结果的可靠性：

- **电荷密度波计算**：二维 TMDs（如 TaS₂、TaSe₂）的 CDW 模拟中，泛函/赝势选择是决定电子-声子耦合与结构弛豫准确性的关键策略之一（[[../papers/chowdhuryReviewTheoreticalComputational|Chowdhury 综述]]）。
- **力学性质**：单层 TMD 的应力-应变曲线与极限强度模拟依赖可靠的价电子描述（[[../papers/Li2013bonding|Li 2013]]）。
- **极化理论**：贝里相位/极化计算（[[../papers/king-smithTheoryPolarizationCrystalline1993|King-Smith 1993]]）同样建立在精确价态波函数之上，与赝势的传输性密切相关。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]] — From ultrasoft pseudopotentials to the projector augmented-wave method
- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]] — Implementation and performance of the frequency-dependent GW method within the PAW framework
- [[../papers/chowdhuryReviewTheoreticalComputational]] — Computational Methods for Charge Density Waves in 2D Materials
- [[../papers/Li2013bonding]] — Bonding Charge Density and Ultimate Strength of Monolayer Transition Metal Dichalcogenides
- [[../papers/king-smithTheoryPolarizationCrystalline1993]] — Theory of polarization of crystalline solids
- [[../papers/niuDirectVisualizationLargeScale2021]] — Direct Visualization of Large-Scale Intrinsic Atomic Lattice Structure and Its Collective Anisotropy in Air-Sensitive Monolayer 1T'-WTe2

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/pseudopotential|赝势]]：模守恒赝势是赝势家族中约束最严格的一支。
- [[../concepts/density-functional-theory|密度泛函理论]]：赝势方法所依赖的第一性原理框架。
- [[../concepts/plane-wave-basis|平面波基组]]：NCPP 最常用的基组表示。
- [[../concepts/gw-approximation|GW 近似]]：基于 PAW/赝势框架的准粒子修正。
- [[../concepts/charge-density-wave|电荷密度波]]：对赝势/泛函选择敏感的电子不稳定性计算。
- [[../entities/WTe2|WTe₂]]：1T′ 相二维材料，赝势模拟的典型体系。
