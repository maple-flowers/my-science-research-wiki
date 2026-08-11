---
title: Strain Engineering
type: concept
tags: [2D-materials, phase-transition, multiferroicity]
---

# 应变工程 / Strain Engineering

**应变工程**是指通过改变材料的晶格参数（拉伸或压缩）来调控其物理化学性质的技术手段。在二维材料和氧化物薄膜研究中，应变是调制电子能带结构、磁序、极化以及触发相变的核心工具。

## 1. 基本原理

应变通过改变化学键的键长和键角，直接影响原子轨道之间的重叠程度（即轨道杂化强度），进而重塑材料的能量景观。
- **面内应变 ($\epsilon_{ab}$)**：通过衬底晶格失配或柔性器件拉伸施加。
- **对称性破缺**：非均匀应变（梯度应变）可以打破空间反演对称性，诱导产生挠曲电效应（Flexoelectricity）或调制拓扑缺陷。

## 2. 2025 年新进展：相锁定切换 (Phase-interlocked Switching)

在非范德华 $ABO_3$ 氧化物单层中，微小的应变可以驱动低能垒的结构相变，并同步控制多种物理属性 [[../../raw/note/zhongHighthroughputExfoliationMultiferroic2025|Zhong et al. 2025]]：

- **结构畸变调控**：通过应变调节 $ABO_3$ 单层中五面体/八面体的扭转角（Twist angle, $\theta$）。
- **典型案例：SrOsO₃**
    - 施加 **1.2%** 的双轴拉伸应变可诱导 $P4bm \to P4mm$ 相变。
    - 该过程通过增强面外 $Os-O$ 键（由 $pCOHP$ 分析证实）来补偿应变能。
    - 相变导致自旋劈裂能从 $0.606\text{ eV}$ 剧降，实现了自旋特性的电学模拟开关。

## 3. 应用领域

- **带隙工程**：通过应变连续调节半导体带隙。
- **磁电调控**：在多铁性材料中，利用应变作为媒介实现电场对磁性的间接控制。
- **超快器件**：相变驱动的开关速度可达飞秒（fs）量级，且能耗极低（$\sim 10^{-3} \text{ fJ/switch}$）。

## 4. 本库相关文献

- [[../../raw/note/zhongHighthroughputExfoliationMultiferroic2025|Zhong et al. 2025]]：应变诱导的相锁定切换机制。
- [[../../raw/note/neumayerCompetingPolarPhases2025|Neumayer et al. 2025]]：竞争极性相中的应变调控。
- [[../../raw/note/martinThinfilmFerroelectricMaterials2016|Martin 2016]]：氧化物薄膜应变工程综述。
