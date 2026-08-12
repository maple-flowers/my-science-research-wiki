---
name: bond-density
description: 一种识别非范德华材料可剥离晶面的物理判据，定义为单位面积内穿过晶面的化学键数量。
metadata:
  type: concept
---

# 键密度 / Bond Density ($\rho$)

**键密度** 是由 [[../papers/zhongHighthroughputExfoliationMultiferroic2025|Zhong 2025]] 提出的一种普适性几何-物理判据，用于识别非范德华（non-vdW）三维块体材料中潜在的可剥离晶面。该判据为从非层状氧化物中获得二维单层提供了理性设计的理论基础。

## 1. 定义与公式

键密度定义为某一特定晶面上，单位面积内需要切断的化学键数目：

$$\rho = \frac{N(R_i, R_j)}{A}$$

其中：
- $N(R_i, R_j)$：穿过目标切面且满足成键条件的原子对数量。
- $A$：该切面在单位周期内的面积。

## 2. 剥离判据

在识别可剥离晶面时，[[../papers/zhongHighthroughputExfoliationMultiferroic2025|Zhong 2025]] 确定了关键阈值：
- **阈值**：$\rho \le 0.3 \text{ bonds/Å}^2$。
- **物理意义**：较低的键密度意味着剥离单层时需要克服的化学键能垒较小。在 $ABO_3$ 钙钛矿体系中，符合该条件的单层剥离能通常低于 $0.13 \text{ eV/Å}^2$，与石墨烯、$\text{MoS}_2$ 等范德华材料处于同量级。

## 3. 应用价值

- **高通量筛选**：该指标不依赖于特定的化学组分或对称性，已成功应用于扫描 Materials Project 和 ICSD 数据库中的 831 种三元氧化物，筛选出 35 种稳定可剥离单层。
- **代表性案例**：
    - **[[../entities/NaZnO3|NaZnO3]]**：剥离能仅 $0.049 \text{ eV/Å}^2$，是筛选中剥离能最低的氧化物之一。
    - **[[../entities/BiFeO3|BiFeO3]]**：剥离能为 $0.109 \text{ eV/Å}^2$，证明了在单晶胞厚度下保持多铁性的潜力。
    - **[[../entities/SrOsO3|SrOsO3]]**：剥离能为 $0.134 \text{ eV/Å}^2$，展现了高转变温度的变换磁性特征。

## 4. 相关概念
- [[binding-strength|结合强度 Binding Strength]]
- [[../entities/SrOsO3|SrOsO3]]
- [[2D-materials|二维范德华材料与低维铁性]]
