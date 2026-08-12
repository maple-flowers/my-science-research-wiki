---
tags: [concept, 2D, vdW, materials, multiferroicity, phase-locked]
category: [D02, Z01]
---

# 二维范德华材料与低维铁性 / Two-Dimensional Van Der Waals Materials

原子级厚度（单层至数层）的晶体材料，其层内通过强共价键/离子键结合，而层间通过弱范德华（van der Waals, vdW）力堆叠。二维材料的出现打破了传统三维体材料中铁性极化的“临界厚度”（Critical Thickness）限制，并绕开了传统多铁性中铁电与铁磁化学互斥的 **d⁰ 规则 (d⁰ rule)**。通过层间滑动、莫尔超晶格及磁结构诱导，二维体系展现出高度集成的“相锁定”物性调控能力。

## 相锁定属性与多场耦合 (Phase-Locked Properties)

在二维极限下，晶格、电子与自旋自由度表现出极强的相干性，形成**相锁定（Phase-Locked）**响应特征。这意味着微小的外部激励（如应变、电场）可以同时重构材料的多种序参量：

1.  **电子-晶格锁定 (Electronic-Lattice Locking)**：
    - **滑动铁电性 (Sliding Ferroelectricity)**：在 [[../entities/h-BN|h-BN]] 或 [[../entities/TMDs|TMDs]] 双层中，极化状态由层间堆垛方式（如 AB/BA）决定。机器学习势模拟显示，畴壁的类孤子运动是实现皮秒级超快翻转的关键，其翻转电场比单畴直接翻转低两个数量级 ([[../papers/heUltrafastSwitchingDynamics2024]])。
    - **应变介导耦合**：在 Fe₃GaTe₂/P(VDF-TrFE) 异质结中，利用铁电聚合物的逆压电效应诱导面内应变，可实现室温下对垂直磁各向异性（PMA）的非易失性电学控制 ([[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]])。

2.  **电子-自旋锁定 (Electronic-Spin Locking)**：
    - **巨自旋劈裂与 Rashba 效应**：在极性单层如 **SrOsO₃** 中，强 p-d 杂化与反演对称性破缺锁定了高达 0.606 eV 的巨自旋劈裂。通过 ~1.2% 的应变驱动序-序相变，可实现半导体-金属转变与自旋纹理的同步重构 ([[../papers/zhongHighthroughputExfoliationMultiferroic2025]])。
    - **电磁振子 (Electromagnon)**：作为动态磁电耦合的指纹，电磁振子模式（如 NiI₂ 中的 34 和 37 cm⁻¹ 模式）展现出强烈的拉曼光学活性 (ROA)，标志着磁振子与电偶极激发的强杂化 ([[../papers/songEvidenceSinglelayerVan2022]])。

## 二维材料的扩展与筛选

为了突破 vdW 晶格的天然限制，研究者提出了通用的**非范德华剥离 (Non-vdW Exfoliation)** 判据：
- **键密度判据**：剥离晶面需满足 $\rho \le 0.3$ bonds/Å²。
- **强度判据**：面外结合强度 $\xi_\perp$ 必须小于面内结合强度 $\xi_\parallel$。
基于此范式，已高通量预测出 35 种具有室温磁性与铁电性的稳定单层氧化物（如 [[../entities/SrOsO3|SrOsO₃]]、[[../entities/BiFeO3|BiFeO₃]]），剥离能低至 0.049 eV/Å²，与石墨烯同量级 ([[../papers/zhongHighthroughputExfoliationMultiferroic2025]])。

## 代表性体系与表征技术

- **本征 II 型多铁**：以单层 **NiI₂** 为代表，其螺旋磁序通过逆 DM 机制直接诱导极化 ([[../papers/songEvidenceSinglelayerVan2022]])。
- **人工多铁设计**：通过插层（Intercalation）、界面调制（如晶圆级 **Cr₂S₃**）或构建范德华异质结，人工组装 FM/FE/FA 序 ([[../papers/tangMultiferroicityTwodimensionalVan2025]], [[../papers/RecentAdvancesGrowth2025]])。
- **关键技术**：二次谐波产生 (SHG) 用于判定反演对称性破缺；圆偏振拉曼用于探测磁手性；反常霍尔效应 (AHE) 用于室温磁电逻辑演示 ([[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]])。

## 关联概念与实体

- [[sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[multiferroicity|多铁性 Multiferroicity]]
- [[magnetoelectric-coupling|磁电耦合 Magnetoelectric Coupling]]
- [[../entities/NiI2|二碘化镍 NiI2]]
- [[../entities/Cr2S3|硫化铬 Cr2S3]]
- [[../entities/SrOsO3|锇酸锶 SrOsO3]]
- [[../entities/Fe3GeTe2|Fe3GeTe2 及其同构体]]
