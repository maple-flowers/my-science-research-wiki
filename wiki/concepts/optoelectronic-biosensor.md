---
tags: [concept, sensor, optoelectronics, biology]
title: 光电生物传感器 (Optoelectronic Biosensor)
type: concept
status: mature
domain: [biosensing, optoelectronics, nanotechnology]
mechanism: 将生物识别事件（如酶切、杂交）转化为可测量的光电信号（如光电流、光电压）的器件
related_concepts: [2d-materials, dielectric-response, photoresponsivity, crispr-cas12a]
papers: [duUltrasensitiveOptoelectronicBiosensor2025, duUltrasensitiveOptoelectronicBiosensor2025]
updated: 2026-08
---

# 光电生物传感器 / Optoelectronic Biosensor

光电生物传感器是一种集成了光电转换机制与生物识别功能的先进检测平台。它利用光作为探测手段或能量源，通过观测生物分子与传感器表面相互作用导致的光电流、光电压或光谱变化，实现对靶标分子（如 DNA、RNA、蛋白质）的高灵敏度、特异性定量检测。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“光电生物传感器”其实就是一个超级灵敏的“探照灯”。想象你手里有一盏灯，照在一块神奇的板子上，板子就能产生电（光电流）。
> 
> 现在你想测测水里有没有某种病毒。咱们在板子上放一些特殊的“钩子”（生物识别分子）。如果病毒上钩了，它就会像一把遮阳伞或者是改变了板子表面的环境，让你的灯照上去产生的电变多或者变少。咱们只要盯着电表看，就知道病毒来没来，来了多少。这种法子比以前那种要等好几天的化验快得多，而且哪怕只有一丁点病毒也能被发现。

## 🏗️ 结构概览

现代光电生物传感器常结合二维材料、等离激元纳米天线和生物分子机器（如 CRISPR-Cas12a）构建。

![图：基于转角石墨烯与 CRISPR 的光电生物传感器架构](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_1_BXNBIMFM.png)
*   **看图要点**：图中展示了传感器阵列的层级结构：基底上的扭曲双层石墨烯（tBLG）提供光电转换，金纳米盘增强局部场，CRISPR 蛋白负责特异性识别，而 DNA 折纸结构确保了纳米尺度的精确组装。
*   **来源**：[[../papers/duUltrasensitiveOptoelectronicBiosensor2025]] -> [[../figures/electronic-devices-sensors|传感器与探测器]]

## 🧩 工作原理与关键性能

### 信号转导机制
1.  **介电调制**：生物分子结合改变了局域介电常数，影响载流子迁移率或激子解离。
2.  **能量/电荷转移**：利用生物识别触发纳米颗粒（如金纳米颗粒）的释放或结合，调制光敏层的激子-等离激元耦合强度，产生显著的光电流变化。

### 核心指标
*   **灵敏度 (LOD)**：检测限可达阿摩尔 ($aM, 10^{-18} M$) 级别。
*   **动态范围**：检测浓度通常跨越 5-7 个数量级。
*   **特异性**：能够区分单个碱基的错配 (Single-nucleotide mismatch)。

### 典型体系
基于扭曲双层石墨烯 (tBLG) 的传感器利用其特有的范霍夫奇点 (VHS) 增强光吸收，结合 CRISPR-Cas12a 的特异性切割，实现了免扩增的超灵敏检测。

## 📚 相关论文 (Related Papers)

- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]：详细介绍了利用转角石墨烯和 CRISPR 系统构建的超灵敏生物传感器。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dielectric-response|介电响应]]
- [[../concepts/photoresponsivity|光响应度]]
- [[../concepts/van-hove-singularity|范霍夫奇点]]
- [[../concepts/crispr-cas12a|CRISPR-Cas12a]]
- [[../entities/twisted-bilayer-graphene|扭曲双层石墨烯]]
- [[../entities/gold-nanodisks|金纳米盘]]
