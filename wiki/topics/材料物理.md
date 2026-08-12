---
category: [D01]
tags: [materials-physics, 2d-materials, symmetry-breaking, multiferroics, electronic-transport, sliding-ferroelectricity]
---

# D01 材料物理 (Materials Physics)

> 大会调研报告：[[../../../爱调研的猫猫/厦门中国材料学大会/D 功能材料/D01 材料物理/D01 材料物理]]

## 主题概述
材料物理的研究正处于从“结构决定性质”到“按需设计结构”的范式转型期。在 2024-2026 年间，核心突破集中在**二维非层状材料的稳定性破译**、**滑动铁电（Sliding Ferroelectricity）的普适化理论**以及**“铁电金属”**等新型凝聚态相的实证。研究重点在于如何利用对称性破缺（如层间滑移、非对称电荷转移）打破传统物理禁忌，实现超高载流子迁移率、室温多铁性及电控拓扑态。

## 发展里程碑 (2024-2026)

| 时间 | 关键进展 | 核心文献 | 物理贡献 |
|---|---|---|---|
| **2026.06** | **室温二维多铁金属实证** | [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]] | 实验实证双层 $CrTe_2$ 为室温空气稳定多铁金属，提出“电子填充驱动层间电荷转移”新机制。 |
| **2025.07** | **非层状二维材料稳定性准则** | [[../papers/yanDecipheringStabilityTwodimensional2025]] | 提出“积木块（LEGO）”组装规则，预测 TT-GaSb 具有 $10^8$ 量级的超高空穴迁移率。 |
| **2025.05** | **滑动物理理论框架完备化** | [[../papers/kaurRecentAdvancesTheoretical2025a]] | 系统建立滑动铁电与交变磁性（Altermagnetism）、量子反常霍尔效应耦合的理论地图。 |
| **2025.02** | **新型磁性滑动铁电体预测** | [[../papers/hanTunableSlidingFerroelectricity2025]] | 预测 $RuX_2$ 系列为极低翻转势垒（~7 meV）的磁性滑动铁电体，实现电调控磁序。 |
| **2024.11** | **超快畴壁动力学模拟** | [[../papers/heUltrafastSwitchingDynamics2024]] | 利用机器学习势揭示 h-BN 畴壁运动可将翻转场降低 2 个数量级，实现皮秒级翻转。 |
| **2024.08** | **磁性铁电金属态预测** | [[../papers/miaoMagneticFerroelectricMetal2024]] | 预测双层 $Fe_3GeTe_2$ 中的磁性铁电金属态及其四态操控逻辑。 |

## 关键物理机制与概念

### 1. 结构演化：从“试错”到“积木组装”
二维非层状材料（如 III-V 族）的稳定性不再遵循高对称性直觉。
- **LEGO 组装准则**：稳定结构可解构为四面体（sp³）、三角形（sp²）和扭曲三角形的线性组合 [[../papers/yanDecipheringStabilityTwodimensional2025]]。
- **轨道-应变解耦**：通过特定轨道分布（如 VBM 仅由 $p_x$ 占据）使形变势常数 $E_1$ 骤降，从而获得超高迁移率 [[../papers/yanDecipheringStabilityTwodimensional2025]]。

### 2. 滑动铁电性（Sliding Ferroelectricity）的泛化
极化起源从传统的“离子位移”转向“纯电子效应”。
- **电子起源机制**：层间不对称堆叠导致的电荷重新分布是极化的本质，与层间轨道杂化（如 $p_z$ 轨道畸变）紧密相关 [[../papers/kaurRecentAdvancesTheoretical2025a]]。
- **多场耦合效应**：滑动可诱导**交变磁性（Altermagnetism）**、切换**量子反常霍尔（QAH）**手性，甚至在 h-BN 中产生**动态多铁性** [[../papers/kaurRecentAdvancesTheoretical2025a]]。

### 3. “铁电金属”佯谬的二维突破
打破了“极化与导电金属性互斥”的传统范式。
- **层间电荷转移 (ICT)**：利用 FM 层与 AFM 层间的电子填充差异产生自发极化，实现“面内导电、面外绝缘”的稳定多铁金属 [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]。
- **电写磁读**：利用 PFM 写入铁电畴、MFM 读取对应磁畴，验证了磁电耦合的非易失性操控 [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]。

### 4. 畴壁物理与超快翻转
- **畴壁宽度效应**：由于极低翻转势垒与高面内刚度，二维滑动铁电畴壁宽度（10-40nm）远超传统铁电体 [[../papers/heUltrafastSwitchingDynamics2024]]。
- **缺陷钉扎机制**：揭示了理想扭转莫尔结构的“超顺电”本质，以及缺陷钉扎如何诱导实验观察到的回滞行为 [[../papers/heUltrafastSwitchingDynamics2024]]。

## 概念与实体索引
- **核心概念**：[[../concepts/lego-assembly]] (新), [[../concepts/sliding-ferroelectricity]], [[../concepts/interlayer-charge-transfer]], [[../concepts/altermagnetism]], [[../concepts/deformation-potential]]。
- **前沿材料**：[[../entities/CrTe2]] (室温多铁), [[../entities/GaSb]] (超高迁移率), [[../entities/h-BN]] (滑动原型), [[../entities/RuI2]] (多铁候选)。

## 领域未来挑战
1. **实验制备**：通过 MBE/CVD 精确调控层数与堆叠序，实现理论预测的 TT 或 E4 等高迁移率新相。
2. **多态存储**：利用多铁金属的四态逻辑（P↑↓, M↑↓）设计超低功耗存储单元。
3. **量子关联物理**：在强关联体系中探索滑动铁电与非常规超导、拓扑物态的深度耦合。
