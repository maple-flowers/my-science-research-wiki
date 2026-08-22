---
tags: [concept]
title: '电荷密度 / Charge Density'
type: concept
status: mature
domain: [condensed-matter-physics, electronic-structure]
mechanism: 单位体积内电子电荷的空间分布，DFT 自洽循环的基本变量
related_concepts: [charge-density-wave, charge-transfer, ferroelectricity, density-functional-theory, bader-analysis, charge-order]
papers: ['PChandra2011mechanoluminescence', 'blochlProjectorAugmentedwaveMethod1994b', 'chenStrongSlidingFerroelectricity2024', 'cossuStackingChargedensityWaves2024', 'dudarevElectronenergylossSpectraStructural1998a', 'guoAdvancesTwodimensionalFerroelectric2025', 'hanTunableSlidingFerroelectricity2025', 'kresseInitiomolecularDynamicsLiquid1993', 'sharmaRoomtemperatureFerroelectricSemimetal2019', 'shenEmergenceMultipleFerroelectric2025', 'shishkinImplementationPerformanceFrequencydependentGWmethod2006', 'shuTwoDimensionalBlackArsenic2020', 'tangCombiningIntrinsicSlidinginduced2025', 'tangGridbasedBaderAnalysis2009', 'tianRoomtemperatureTwodimensionalMultiferroic2026', 'wangTwodimensionalFerroelectricMetal2025', 'wongEvidenceMetallic1T', 'wuSlidingFerroelectricity2D2021a', 'zhangEmergingFrontiersTwodimensional2025', 'zhangNonvolatileControlTopological2025', 'zhengAnisotropicSuperconductivityTwodimensional2025']
updated: 2026-08
---

# 电荷密度 / Charge Density

电荷密度（charge density）描述单位体积内电荷的空间分布 ρ(r)，是电子结构与第一性原理计算的核心物理量。在 DFT 中，电荷密度由占据波函数平方求和得到，既是自洽循环求解的基本变量，也是分析化学键、成键/反键特征、电荷转移、磁性及铁电极化机理的直接工具。

## 👵 太奶导读

太奶啊，原子里的电子在空间怎么分布，就是"电荷密度"。有的地方电子多（像人多的地方）、有的地方少。科学家算出电荷密度图，就像看一张"电子分布热力图"：哪里电子挤在一起说明那里成键强，哪里电子跑了说明发生了"搬家"（电荷转移）。铁电、磁性、电荷密度波这些现象，归根结底都能从电荷怎么排看出来。

## 🏗️ 结构概览

电荷密度是电子结构理论的"底层地图"：DFT 通过自洽求解 Kohn-Sham 方程得到电荷密度，再反过来用新的电荷密度更新势场，如此迭代至收敛。一切可观测量（总能量、力、应力、极化）都由电荷密度（及其一阶响应）导出。分析层面，差分电荷密度与 Bader 分析是解读成键、电荷转移与极化机理的标准工具，也是理解滑动铁电、CDW、多铁等量子物态的基础。

## 🧩 核心内容与机制 (Core Content)

- **DFT 基本变量**：自洽 Kohn-Sham 循环迭代电荷密度直至收敛（本库 kresse1993、blochl1994、shishkin2006）；Bader 分析（[[../papers/tangGridbasedBaderAnalysis2009|Tang 2009]]）据此划分原子电荷与电荷转移量。
- **成键分析**：差分电荷密度（Δρ）揭示成键/反键与极化方向；TMD 等二维材料的键合强度与力学性能分析依赖电荷密度。
- **铁电极化与电荷**：铁电体中极化起源于离子位移与电子电荷重排的耦合；滑动铁电（[[../papers/wuSlidingFerroelectricity2D2021a|Wu 2021]]、[[../papers/hanTunableSlidingFerroelectricity2025|Han 2025]]、[[../papers/tangCombiningIntrinsicSlidinginduced2025|Tang 2025]]）强调层间电荷重分布的贡献；铁电金属中金属性与铁电畸变共存亦体现在电荷密度分布（[[../papers/wangTwodimensionalFerroelectricMetal2025|Wang 2025]]、[[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026|Tian 2026]]）。
- **电荷密度波（CDW）**：费米面嵌套导致的周期性电荷调制，可通过电荷密度分布直接可视化（[[../papers/cossuStackingChargedensityWaves2024|Cossu 2024]]、[[../papers/wongEvidenceMetallic1T|Wong]]）。
- **实验对应**：X 射线衍射精修、电子能量损失谱（EELS，[[../papers/dudarevElectronenergylossSpectraStructural1998a|Dudarev 1998]]）等可间接探测电荷分布。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| ρ(r) | 单位体积电荷密度 | DFT 核心变量 |
| Δρ | 差分电荷密度 | 揭示电荷重排/转移 |
| Bader 电荷 | 原子分属电荷 | 定量电荷转移 |
| 自洽收敛 | 密度迭代判据 | 能量/密度阈值 |
| 极化 P | 电荷重排+离子位移 | 铁电与滑动铁电 |

## 🔀 近邻概念辨析

- **电荷密度 vs 电荷有序**：电荷密度是连续空间分布；电荷有序是电荷在格点上周期性"扎堆"的有序态（电荷密度的周期调制特例）。
- **电荷密度 vs 电荷密度波 (CDW)**：CDW 是电荷密度具有特定波矢的周期性调制，常伴随晶格畸变与能隙打开。
- **电荷密度 vs 极化**：极化是电荷密度分布的一阶矩（位移×电荷），二者通过 Berry 相位在现代极化理论中严格关联。

## 📚 相关论文 (Related Papers)

- [[../papers/wuSlidingFerroelectricity2D2021a]] — 滑动铁电中电荷重排与极化机制（综述）。
- [[../papers/hanTunableSlidingFerroelectricity2025]] — 可调滑动铁电的电荷/极化调控。
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]] — 内禀与滑移诱导机制结合的电荷分析。
- [[../papers/cossuStackingChargedensityWaves2024]] — 堆叠相关电荷密度波中的电荷分布。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] — 铁电半金属的电子结构与电荷分布。
- [[../papers/tangGridbasedBaderAnalysis2009]] — Bader 电荷分析方法。
- [[../papers/blochlProjectorAugmentedwaveMethod1994b]] — PAW 方法（电荷密度计算基础）。
- [[../papers/kresseInitiomolecularDynamicsLiquid1993]] — VASP 第一性原理方法（电荷密度迭代）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]：电荷密度的周期性调制态。
- [[../concepts/charge-order|电荷有序]]：格点电荷周期分布的有序态。
- [[../concepts/charge-transfer|电荷转移]]：原子间/层间电荷重分配。
- [[../concepts/ferroelectricity|铁电性]]：极化与电荷重排密切关联。
- [[../concepts/density-functional-theory|密度泛函理论]]：电荷密度是 DFT 的核心变量。
- [[../concepts/bader-analysis|Bader 分析]]：从电荷密度划分原子电荷的方法。
- [[../entities/TMDs|TMDs]]：CDW/键合分析典型二维体系。
- [[../entities/HgI2|HgI₂]]：滑动铁电电荷重排体系。
*（内容由AI生成，仅供参考）*