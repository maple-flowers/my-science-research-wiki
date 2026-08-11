---
tags: [entity, material, 2D, In2Se3, ferroelectric, ferroelastic]
category: [D02, Z01]
---

# 硒化铟 / Indium Selenide (In₂Se₃)

$\text{In}_2\text{Se}_3$ 是一种具有多种晶相的 III-VI 族二维范德华半导体材料，其 $\alpha$ 相是目前研究最广泛的二维本征铁电体之一。其独特的层间滑动与极化耦合特性，使其在非挥发性存储、逻辑器件及多铁异质结领域具有重要地位。

## 晶体结构与相变

$\text{In}_2\text{Se}_3$ 的基本结构单元为 **五元层 (Quintuple Layer, QL)**，原子排列顺序为 $\text{Se-In-Se-In-Se}$。每个 QL 内的两个 In 原子层和三个 Se 原子层通过强共价键结合，层间则由弱范德华力维系。

### 主要相态
1. **$\alpha\text{-In}_2\text{Se}_3$ (铁电相)**：具有本征的铁电性，常见堆垛方式包括 2H 和 3R 相。在室温下稳定，具有显著的压电响应。
2. **$\beta'\text{-In}_2\text{Se}_3$ (反铁电/铁弹相)**：表现出由面内反铁电畸变驱动的二维铁弹性，具有纳米条纹超结构 [[../../raw/note/xuTwodimensionalFerroelasticityVan2021|xu2021]]。
3. **$\beta\text{-In}_2\text{Se}_3$ (顺电相)**：高温相（> 700 K），具有更高的对称性（六方晶格）。

## 核心物理特性

### 1. 本征面内与面外极化联动 (IP-OOP Coupling)
$\alpha\text{-In}_2\text{Se}_3$ 最显著的特征是其 **面内 (In-plane, IP)** 与 **面外 (Out-of-plane, OOP)** 极化的强耦合联动 [[../../raw/note/cuiIntercorrelatedInplaneOutofplane2018a|cui2018]]。
- **机制**：反转面外极化 $P_z$ 会强制驱动中间 Se 原子的横向滑动，从而同步反转面内极化 $P_{xy}$。这种“锁死”的耦合特性在理论上由 [[../../raw/note/dingPredictionIntrinsicTwodimensional2017a|ding2017]] 预测并被后续实验证实。
- **翻转势垒**：极化翻转路径通常遵循“三步协同运动”模型。其极化反转势垒 ($P_S$) 约为 $38\text{--}71 \text{ meV/f.u.}$，远低于从顺电相到铁电相的相变势垒 ($P_I \approx 271 \text{ meV/f.u.}$) [[../../raw/note/dingPredictionIntrinsicTwodimensional2017a|ding2017]]。

### 2. 二维铁弹性 (2D Ferroelasticity)
在 $\beta'$ 相中，$\text{In}_2\text{Se}_3$ 展现出显著的二维铁弹性。
- **自发应变**：源于面内反铁电畸变，主应变值约为 $\pm 0.49\%$。
- **机械切换**：存在三种能量简并的畴变体 (Domain Variants)，可通过 $\le 0.5\%$ 的外部单轴拉伸应变实现畴的可逆切换 [[../../raw/note/xuTwodimensionalFerroelasticityVan2021|xu2021]]。

### 3. 多态极化与层数效应
$\text{In}_2\text{Se}_3$ 的铁电性具有显著的厚度依赖性：
- **奇偶层效应 (Odd-even effect)**：不同堆垛方式下，极化强度和稳定性随层数奇偶发生变化。
- **多态切换 (Multistates)**：通过协同利用本征铁电性与滑动诱导铁电性，双层 $\alpha\text{-In}_2\text{Se}_3$ 可实现 6 个极化态，三层可实现 10 个极化态，为高密度多值存储提供了基础 [[../../raw/note/tangCombiningIntrinsicSlidinginduced2025|tang2025]]。

## 异质结与多铁性调控

$\text{In}_2\text{Se}_3$ 常作为铁电基底与其他二维磁性材料构筑 **多铁异质结**：
- **拓扑磁性控制**：在 $\text{CrInTe}_3/\text{In}_2\text{Se}_3$ 异质结中，利用 $\text{In}_2\text{Se}_3$ 的极化反转可以非挥发性地调控界面处的拓扑磁性（如斯格明子状态） [[../../raw/note/zhangNonvolatileControlTopological2025|zhang2025]]。
- **应变工程**：利用其铁弹畴壁与晶格应变的相互作用，可以实现对界面激子或自旋态的局域调控 [[../../raw/note/wangTunableD0Topological2025b|wang2025]]。

## 本库相关代表性论文

- [[../../raw/note/tangCombiningIntrinsicSlidinginduced2025|tangCombiningIntrinsicSlidinginduced2025]] (2025)：揭示了 $\text{In}_2\text{Se}_3$ 中本征铁电与滑动铁电的叠加机制及多态存储潜力。
- [[../../raw/note/tangMultiferroicityTwodimensionalVan2025|tangMultiferroicityTwodimensionalVan2025]] (2025)：探讨了基于 $\text{In}_2\text{Se}_3$ 的二维多铁性及其电磁耦合特性。
- [[../../raw/note/zhangNonvolatileControlTopological2025|zhangNonvolatileControlTopological2025]] (2025)：演示了通过铁电极化对二维异质结中拓扑磁性的非挥发控制。
- [[../../raw/note/wangTunableD0Topological2025b|wangTunableD0Topological2025b]] (2025)：研究了 $\text{In}_2\text{Se}_3$ 异质结中可调控的 $d^0$ 拓扑性质。
- [[../../raw/note/huangTwodimensionalIn2Se3Rising2022|huangTwodimensionalIn2Se3Rising2022]] (2022)：综述了 $\text{In}_2\text{Se}_3$ 在光电与铁电器件方面的研究进展。
- [[../../raw/note/xuTwodimensionalFerroelasticityVan2021|xuTwodimensionalFerroelasticityVan2021]] (2021)：首次实验证实了 $\beta'\text{-In}_2\text{Se}_3$ 中的二维铁弹性。
- [[../../raw/note/cuiIntercorrelatedInplaneOutofplane2018a|cuiIntercorrelatedInplaneOutofplane2018a]] (2018)：报道了面内与面外极化的强相关性及其在非对称光响应中的应用。
- [[../../raw/note/dingPredictionIntrinsicTwodimensional2017a|dingPredictionIntrinsicTwodimensional2017a]] (2017)：理论预测了 $\text{In}_2\text{Se}_3$ 的本征二维铁电性及其翻转机制。

## 关联概念

- [[../concepts/sliding-ferroelectricity|滑动铁电性 (Sliding Ferroelectricity)]]
- [[../concepts/2D-materials|二维范德华材料 (2D Materials)]]
- [[../concepts/multiferroics|二维多铁性 (2D Multiferroics)]]
