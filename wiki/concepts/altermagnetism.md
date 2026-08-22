---
tags: [concept, magnetism, spintronics, altermagnetism, 2d-materials]
title: 交变磁性 / Altermagnetism
type: concept
status: mature
year: 2025
domain: [condensed-matter-physics, magnetism, spintronics]
mechanism: 净磁化严格为零（类反铁磁）但能带自旋劈裂显著（类铁磁）的新型磁性相，自旋劈裂呈动量依赖的交变符号结构（d 波对称）
related_concepts: [ferromagnetism, antiferromagnetism, spin-splitting, magnetic-anisotropy, magnetoelectric-coupling, spin-orbit-coupling, spintronics, two-dimensional-magnetism]
papers: [zhongHighthroughputExfoliationMultiferroic2025, yuFerroelectricControlMagnetism2026, kaurRecentAdvancesTheoretical2025a]
updated: 2026-08-19
---

# 交变磁性 / Altermagnetism

交变磁性（altermagnetism）指**一类净磁化严格为零（类反铁磁）、但能带自旋劈裂显著（类铁磁）的新型磁性相**。其自旋劈裂呈动量依赖的交变符号结构（交替的 d 波/类 d 波对称性），兼具反铁磁的零杂散场与铁磁的自旋极化操控潜力，是自旋电子学与磁性材料研究的新前沿。

## 👵 太奶导读

以前磁性分两派：铁磁（磁矩全朝一个方向，有净磁化）和反铁磁（磁矩两两反着排，净磁化为零）。交变磁性是"第三派"——磁矩虽然也是反着排、净磁化为零，但能带里"自旋朝上"和"自旋朝下"的电子能量却分开了（自旋劈裂），就像反铁磁的身体装了铁磁的"自旋大脑"，特别适合做新型自旋电子器件。

## 🏗️ 结构概览

交变磁性在对称性上位于铁磁与反铁磁之间：晶格平移-自旋旋转复合对称性使净磁化抵消，同时允许动量空间交变的自旋劈裂。

## 🧩 核心内容与机制 (Core Content)

### 1. 自旋劈裂的磁性单层

高通量筛选预测出多种 ABO₃ 三元氧化物单层（剥离能低至 0.049 eV/Å²）具有高磁转变温度（最高 315 K）与巨自旋劈裂（最高 0.606 eV），其晶格-电子-自旋强耦合可通过微小应变（约 1.2%）在半导体/半金属态、反铁磁/铁磁之间切换（[[../papers/zhongHighthroughputExfoliationMultiferroic2025|Zhong 2025]]）——这类"零净磁化 + 大自旋劈裂"的能带特征与交变磁性高度契合。

### 2. 磁性范式的中间态

从交换作用看，真实磁体介于海森堡定域模型与斯托纳巡游模型之间（[[../papers/vanvleckSurveyTheoryFerromagnetism1945|Van Vleck 1945]]），交变磁性正是在这一谱系中涌现的对称性驱动新相。

### 3. 与磁电调控的结合

单层 Cr₄S₄FBr₂ 是一种高 Néel 温度（469 K）的 A 型完全补偿亚铁磁金属，其自旋极化与自旋纹理可通过翻转铁电极化完全反转，Chern 数可在 -2 与 +2 之间切换，基于该材料的多铁隧道结可实现纯电场驱动的巨磁阻（高达 4.8×10³%）（[[../papers/yuFerroelectricControlMagnetism2026|Yu 2026]]）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 净磁化 | 宏观磁性 | 严格为零 |
| 自旋劈裂 | 能带劈裂 | 最高约 0.6 eV |
| 磁转变温度 | 磁性稳定上限 | 最高约 315 K（单层筛选） |
| 劈裂对称性 | 动量空间结构 | d 波/类 d 波交变符号 |
| 调控手段 | 实现切换 | 应变、铁电极化 |

## 🔀 近邻概念辨析

- **交变磁性 vs 铁磁性**：铁磁有净磁化且自旋劈裂非交变；交变磁性净磁化为零但自旋劈裂与铁磁类似，兼具"零杂散场 + 自旋极化读出"优势。
- **交变磁性 vs 反铁磁**：反铁磁通常自旋简并、无净自旋劈裂；交变磁性的关键突破正是"零磁化但有自旋劈裂"，可被电学/光学手段读出。

## 📚 相关论文 (Related Papers)

- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：高通量筛选 ABO₃ 单层中的高转变温度磁性半金属。
- [[../papers/yuFerroelectricControlMagnetism2026]]：铁电控制完全补偿亚铁磁金属的自旋纹理与拓扑。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：滑移铁电与层间自由度的理论进展。

### ⚠️ 已撤回的引文

以下条目原列于本节，经核对其 `raw/note` 原始笔记后确认无据，于 2026-08-21 撤回：

- `vanvleckSurveyTheoryFerromagnetism1945`：该 1945 年综述早于 altermagnetism 概念提出（约 2022 年）。笔记中唯一近似串「交错磁格子」实指反铁磁的交错子晶格（staggered sublattice），属术语撞名，非交变磁性。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferromagnetism|铁磁性]]
- [[../concepts/antiferromagnetism|反铁磁性]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../concepts/spin-orbit-coupling|自旋-轨道耦合]]
- [[../concepts/two-dimensional-magnetism|二维磁性]]
- [[../entities/Fe3GeTe2|Fe3GeTe2]]
