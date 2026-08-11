---
name: binding-strength
description: 比较晶面内与晶面间的结合强度，用于预判非范德华材料的剥离各向异性。
metadata:
  type: concept
---

# 结合强度 / Binding Strength ($\xi$)

**结合强度** 是继 [[bond-density|键密度]] 之后，判断非范德华材料是否可剥离的第二个关键指标 [[../../raw/note/zhongHighthroughputExfoliationMultiferroic2025|Zhong et al. 2025]]。

## 1. 物理含义

该判据通过比较不同方向上的原子轨道重叠程度来评估结合的各向异性：
- **面外结合强度 ($\xi_\perp$)**：垂直于晶面方向的轨道波函数求和。
- **面内结合强度 ($\xi_\parallel$)**：平行于晶面方向的轨道波函数求和。

## 2. 剥离判据条件

当满足以下条件时，晶面被认为具有剥离潜力：
$$\xi_\perp < \xi_\parallel$$

这表明层间的相互作用力弱于层内，从而在施加外力时，材料更倾向于沿该晶面解理，而不是破坏层内结构。

## 3. 计算方法
通常利用晶体轨道哈密顿布居 (COHP) 或轨道波函数重叠程度进行积分得到。

## 4. 相关概念
- [[bond-density|键密度 (Bond Density)]]
- [[strain-engineering|应变工程 (用于调控结合强度)]]
