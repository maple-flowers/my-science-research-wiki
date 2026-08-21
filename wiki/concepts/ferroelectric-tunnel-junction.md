---
tags: [concept, device, ferroelectricity]
title: 铁电隧道结 / Ferroelectric Tunnel Junction (FTJ)
type: concept
status: mature
related_concepts: [ferroelectricity, polarization-switching, magnetic-tunnel-junction, resistive-switching, memristor]
papers: [FerroelectricityMultiferroicityAtomic2023, RecentAdvancesGrowth2025, chenHafniumBasedFerroelectricPostMoore2026, guanRecentProgressTwoDimensional2020, guoAdvancesTwodimensionalFerroelectric2025, hanPolarTopologicalMaterials2025, huProgressProspectsLowdimensional2019, huangTwodimensionalIn2Se3Rising2022, junqueraCriticalThicknessFerroelectricity2003, liPhaseTransitions2D2021, martinThinfilmFerroelectricMaterials2016, neumayerCompetingPolarPhases2025, sunSlidingFerroelectricityTwodimensional2025, tangCombiningIntrinsicSlidinginduced2025, xueEmergingNonvolatileMemories2011, zahraCriticalAnalysisFerroelectric2025, zhangEmergingFrontiersTwodimensional2025]
updated: 2026-08
---

# ferroelectric-tunnel-junction

铁电隧道结（ferroelectric tunnel junction, FTJ）是**以超薄铁电薄膜作为隧穿势垒**的两端器件，通过铁电极化的两个取向态调制势垒形状（高度/宽度/界面态），产生电阻态差异（隧穿电致电阻，TER），是实现非易失存储与神经形态计算的核心器件结构。

## 👵 太奶导读

太奶啊，想象两片金属电极中间夹着一层极薄的铁电"门帘"。电子要"穿门帘"（量子隧穿）才能从一边到另一边，而这门帘"记不记得住方向"（极化朝上还是朝下）会改变穿过的难易——一个方向好穿（电阻低），反方向难穿（电阻高）。于是这层门帘就像一个能记住"开关状态"的电阻，断电也不忘，是新一代存储芯片的种子器件。

## 🏗️ 结构概览

FTJ 属于"铁电序驱动的功能器件"家族，与其并行的还有阻变存储、忆阻器与多铁隧穿结。按势垒材料可分为钙钛矿型（BaTiO₃、BiFeO₃）、HfO₂ 基与二维铁电（In₂Se₃）型；按读写机制可分为纯隧穿（TER）与界面态主导型。

## 🧩 核心内容与机制 (Core Content)核心内容与机制 (Core Content)

- **TER 机制**：极化反转改变势垒形状与界面静电势（去极化场、界面电荷），使隧穿电阻显著变化（本库 Fei2018 二维金属铁电开关、In₂Se₃ 隧穿结相关）。
- **结构与材料**：金属/铁电/金属三明治，铁电层可为钙钛矿（BaTiO₃、BiFeO₃）或二维铁电（In₂Se₃）；势垒厚度需在隧穿区间（纳米级）。
- **与磁性隧穿结（MTJ）类比**：FTJ 与磁性隧穿结（magnetic-tunnel-junction）结构相似，一个以极化调控、一个以磁化调控，可组合为多铁隧穿结（multiferroic-tunnel-junction）。
- **器件优势**：非易失、低功耗、尺寸微缩潜力大，可用于阻变存储（resistive-switching）与突触器件（memristor）。
- **表征**：导电原子力显微镜（C-AFM）、电流-电压（I-V）滞回与极化翻转测试。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：FTJ 的势垒材料。
- [[../concepts/polarization-switching|极化翻转]]：FTJ 开关的物理机制。
- [[../concepts/magnetic-tunnel-junction|磁性隧穿结]]：结构对应的类比器件。
- [[../concepts/resistive-switching|阻变存储]]：FTJ 的存储应用。
- [[../concepts/memristor|忆阻器]]：FTJ 的神经形态应用。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| TER 比 | 高低阻态比值 | 可达 10²–10⁴ |
| 势垒厚度 | 铁电层厚度 | 纳米级（隧穿区间） |
| 阻态保持 | 非易失性 | 断电保持 |
| 开关电压 | 极化翻转电压 | 与矫顽场相关 |
| 结构 | 电极/铁电/电极 | 钙钛矿、HfO₂、2D |

## 🔀 近邻概念辨析

- **FTJ vs MTJ**：FTJ 以铁电极化调控隧穿电阻，MTJ 以磁化方向调控；二者可组合为多铁隧穿结。
- **FTJ vs 阻变存储（RRAM）**：FTJ 基于极化本征翻转、均匀且可微缩；RRAM 基于导电细丝，离散性强。
- **FTJ vs 忆阻器**：FTJ 可呈现连续电阻态（突触权重），忆阻器是广义可调电阻器件，FTJ 是其中一种物理实现。

## 📚 相关论文 (Related Papers)

- [[../papers/FerroelectricityMultiferroicityAtomic2023]] — Ferroelectricity and multiferroicity down to the atomic thickness
- [[../papers/RecentAdvancesGrowth2025]] — Recent advances in growth, characterization, and application of two-dimensional multiferroic materials
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]] — Hafnium-Based Ferroelectric Post-Moore Electronics: Device Physics, Integration Architectures, and Neuromorphic System Implementation
- [[../papers/guanRecentProgressTwoDimensional2020]] — Recent Progress in Two‐Dimensional Ferroelectric Materials
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]] — Advances in two-dimensional ferroelectric materials
- [[../papers/hanPolarTopologicalMaterials2025]] — Polar topological materials and devices: Prospects and challenges
- [[../papers/huProgressProspectsLowdimensional2019]] — Progress and prospects in low‐dimensional multiferroic materials
- [[../papers/huangTwodimensionalIn2Se3Rising2022]] — Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]] — Critical thickness for ferroelectricity in perovskite ultrathin films
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials
- [[../papers/martinThinfilmFerroelectricMaterials2016]] — Thin-film ferroelectric materials and their applications
- [[../papers/neumayerCompetingPolarPhases2025]] — Competing polar phases in 2D ferroelectric transition metal thio- and selenophosphates
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]] — Combining intrinsic and sliding-induced polarizations for multistates in two-dimensional ferroelectrics
- [[../papers/xueEmergingNonvolatileMemories2011]] — Emerging non-volatile memories
- [[../papers/zahraCriticalAnalysisFerroelectric2025]] — A critical analysis of ferroelectric and ferromagnetic properties in two-dimensional MXene
- [[../papers/zhangEmergingFrontiersTwodimensional2025]] — Emerging frontiers in two-dimensional sliding ferroelectrics
