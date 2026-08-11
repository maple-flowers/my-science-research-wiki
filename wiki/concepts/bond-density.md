---
name: bond-density
description: 一种识别非范德华材料可剥离晶面的物理判据，定义为单位面积内穿过晶面的化学键数量。
metadata:
  type: concept
---

# 键密度 / Bond Density ($\rho$)

**键密度** 是由 Zhong 等人提出的一种普适性物理判据，用于识别非范德华 (non-vdW) 三维块体材料中潜在的可剥离晶面 [[../../raw/note/zhongHighthroughputExfoliationMultiferroic2025|Zhong et al. 2025]]。

## 1. 定义与公式

键密度定义为某一特定晶面上，单位面积内需要切断的化学键数目：

$$\rho = \frac{N(R_i, R_j)}{A}$$

其中：
- $N(R_i, R_j)$：穿过平面的化学键数量。
- $A$：该平面在单位周期内的面积。

## 2. 剥离判据

在识别可剥离晶面时，通常遵循以下阈值：
- **阈值**：$\rho \le 0.3 \text{ bonds/Å}^2$。
- **物理意义**：较低的键密度意味着剥离单层时需要克服的化学键阻力较小，剥离能在能量上更易达成。

## 3. 应用价值

- **高通量筛选**：不依赖于特定的化学组分或对称性，可用于大规模扫描 Materials Project 等数据库。
- **非范德华剥离**：为从 $ABO_3$ 钙钛矿等非层状氧化物中获得二维单层提供了理论指导。

## 4. 相关概念
- [[binding-strength|结合强度 (Binding Strength)]]
- [[../../entities/SrOsO3|SrOsO3 (典型剥离案例)]]
