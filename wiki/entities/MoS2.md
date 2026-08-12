---
title: 二硫化钼 / Molybdenum Disulfide (MoS2)
type: entity
tags: [TMDs, 2D-materials, sliding-ferroelectricity, semiconductor, dichalcogenide]
category: [D02, Z01]
---

# 二硫化钼 / Molybdenum Disulfide (MoS2)

**MoS₂** 是最典型的过渡金属二硫族化合物（TMD），因其层状范德华结构、直接带隙单层半导体特性以及多晶相（2H、1T、3R、1T'）可调性，成为二维电子学、铁电学和自旋电子学的核心研究平台。

## 核心物理特性

### 滑动铁电性
- **3R 相 MoS₂**：3R 堆垛的 MoS₂ 双层/多层天然具备非中心对称结构，表现出面外滑动铁电极化，极化强度约 **0.05 μC/cm²**，可在室温下电场切换 [[../papers/chenStrongSlidingFerroelectricity2024]]。
- **堆叠工程铁电**：两个相同的 MoS₂ 单层平行堆叠即可在室温观测到铁电回滞；交替堆叠 MoS₂/WS₂ 无需转角即可破缺对称性获得面外铁电 [[../papers/FerroelectricityMultiferroicityAtomic2023]]。
- **抗疲劳机制**：3R-MoS₂ 器件的抗疲劳性源于硫空位迁移能垒（层内 2.6 eV，层间 4.6 eV）远高于极化切换能垒（~136 meV），单个硫空位无法钉扎畴壁，可稳定响应 53 ns 超短脉冲 [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]。

### 1T 相与应变铁电
- **d1T-MoS₂**：理论预测的二维铁电材料，通过三聚化畸变破缺中心对称，产生本征面内极化 [[../papers/guanRecentProgressTwoDimensional2020]]。
- **应变工程**：MoS₂ 的应变输出约 5.8%，作为二维驱动材料的典型对比基准 [[../papers/chenFerromagneticNonmagnetic1T2022]]。

### 器件应用
- **FeFET**：MoS₂ 作为沟道材料与铁电层（PZT、CuInP2S6）构成铁电场效应晶体管，实现非易失存储与光电探测 [[../papers/guanRecentProgressTwoDimensional2020]]。
- **后摩尔铁电器件**：MoS₂ 作为沟道材料用于 HfO₂ 基铁电 FET，是后摩尔非易失存储的重要候选 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 主要物性参数

| 参数 | 数值 | 备注 |
| :--- | :--- | :--- |
| 单层带隙 | ~1.8 eV (直接) | 单层；块体为间接带隙 ~1.2 eV |
| 滑动铁电极化 (3R) | ~0.05 μC/cm² | 双层 |
| 晶体结构 | 2H / 3R / 1T / 1T' | 多晶相可调 |

## Related Papers

- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：综述，堆叠工程铁电中 MoS₂ 的角色
- [[../papers/guanRecentProgressTwoDimensional2020]]：d1T-MoS₂ 理论铁电预测
- [[../papers/chenStrongSlidingFerroelectricity2024]]：3R-MoS₂ 极化强度作为对比基准
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]：3R-MoS₂ 抗疲劳机制与器件性能
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：MoS₂ 沟道铁电 FET
- [[../papers/chenFerromagneticNonmagnetic1T2022]]：MoS₂ 应变输出对比
- [[../papers/Li2013bonding]]：MoS₂ 化学键分析

## 关联概念与实体

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/2D-materials|二维范德华材料]]
- [[../entities/TMDs|过渡金属硫族化合物 TMDs]]
- [[../entities/MoTe2|碲化钼 MoTe₂]]
- [[../entities/WTe2|碲化钨 WTe₂]]
