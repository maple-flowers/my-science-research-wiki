---
tags: [entity, material, 2D, In2Se3, ferroelectric, ferroelastic]
category: [D02, Z01]
---

# 硒化铟 / Indium Selenide (In2Se3)

**In2Se3** 是一种具有多种晶相的 III-VI 族二维范德华半导体材料，其 $\alpha$ 相是目前研究最广泛的二维本征铁电体之一。其独特的层间滑动与极化耦合特性，使其在非挥发性存储、逻辑器件及多铁异质结领域具有核心地位。

## 1. 晶体结构与主要相态
In2Se3 的基本单元为 **五元层 (Quintuple Layer, QL)**，原子顺序为 $\text{Se-In-Se-In-Se}$。
- **$\alpha\text{-In}_2\text{Se}_3$ (铁电相)**：具有本征铁电性（2H 或 3R 堆垛），室温稳定且具显著压电响应。
- **$\beta'\text{-In}_2\text{Se}_3$ (反铁电/铁弹相)**：表现出由面内反铁电畸变驱动的二维铁弹性，具有典型的纳米条纹超结构 [[../papers/gaoStrainEngineeringFerroelectric2024]]。
- **$\beta\text{-In}_2\text{Se}_3$ (顺电相)**：高温相（$> 700\text{ K}$），具有中心对称的六方晶格。

## 2. 核心物理特性
### 2.1 本征面内与面外极化联动 (IP-OOP Coupling)
$\alpha\text{-In}_2\text{Se}_3$ 的面内（In-plane）与面外（Out-of-plane）极化存在强耦合联动 [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]：
- **物理机制**：面外极化 $P_z$ 的翻转必然驱动中间 Se 原子的横向位移，从而同步翻转面内极化 $P_{xy}$。
- **翻转势垒**：理论预测其极化反转势垒约 **$38\text{--}71\text{ meV/f.u.}$**，远低于顺电-铁电相变势垒（$271\text{ meV/f.u.}$） [[../papers/dingPredictionIntrinsicTwodimensional2017a]]。

### 2.2 二维铁弹性与应变调控
在 $\beta'$ 相中，In2Se3 展现出显著的二维铁弹性 [[../papers/gaoStrainEngineeringFerroelectric2024]]：
- **自发应变**：源于面内畸变，主应变约 $\pm 0.49\%$。
- **应变编程**：利用铁弹-铁电耦合，通过机械应变（约 $2\%$）可显著降低相变势垒，实现极化方向的可逆旋转及 60°/180° 畴壁的构型切换。

### 2.3 多态极化与层数效应
- **多态切换 (Multistates)**：通过协同利用本征铁电性与滑动诱导铁电性，双层 $\alpha\text{-In}_2\text{Se}_3$ 可实现 6 个不同的极化态，为高密度多值存储提供可能。
- **矫顽电压**：实验测得其矫顽电压约 **$1\text{--}1.5\text{ V}$** [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]。

## 3. 异质结与多铁调控
In2Se3 常作为铁电基底构建多铁异质结：
- **拓扑磁性控制**：在 CrInTe3/In2Se3 异质结中，利用 In2Se3 的极化反转可以非挥发性地调控界面处的**磁斯格明子 (Skyrmions)** 状态。
- **界面激子调控**：利用其畴壁处的局域应变场调控界面激子的各向异性输运。

## 4. 本库相关代表性论文
- [[../papers/gaoStrainEngineeringFerroelectric2024]]：APL 2024，论证应变对 In2Se3 铁电极化与畴的编程控制。
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]：Nano Lett. 2018，报道面内与面外极化的强相关性。
- [[../papers/dingPredictionIntrinsicTwodimensional2017a]]：Nat. Commun. 2017，理论预测 In2Se3 的本征二维铁电性。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：作为二维多铁性对比体系引用。

## 5. 关联概念
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/ferroelasticity|铁弹性 Ferroelasticity]]
- [[../concepts/strain-engineering|应变工程 Strain Engineering]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]] (对比材料)
