---
tags: [concept, memory, technology]
title: 非易失性存储器 (Non-Volatile Memory)
type: concept
status: mature
domain: [electronics, computing, materials-science]
mechanism: 基于物理状态（极化、相变、磁矩）而非电荷电位存储信息，断电不丢失
related_concepts: [ferroelectric-memory, phase-change-memory, resistive-switching, magnetic-tunnel-junction]
papers: [xueEmergingNonvolatileMemories2011, chenHafniumBasedFerroelectricPostMoore2026]
updated: 2026-08
---

# 非易失性存储器 / Non-Volatile Memory (NVM)

非易失性存储器 (NVM) 是指在断电后仍能保留所存储信息的计算机存储器。与 SRAM 和 DRAM 等易失性存储器不同，NVM 依赖于材料的物理状态（如铁电极化、晶体相态、磁化方向或氧空位分布）来记录二进制数据。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“非易失性存储器”其实就像咱家那本手写的账本。你像现在的电脑内存（易失性存储），就像是在黑板上写字，电源一断，就像有人拿黑板擦抹了一下，啥都没了。而这“非易失”的宝贝，就像是用笔划拉在纸上，哪怕你把灯关了、睡觉去了，明天早上起来，那字儿还稳稳当当地在纸上待着呢。
> 
> 现在科学家们研究的这些新玩意儿，比如用磁铁翻个面、让石头变个样（相变），或者是让电荷在里头“安家”，都是为了让电脑记性更好，还不用一直费电供着。这样你的手机照片、存的电影，哪怕电池没电了也丢不了。

## 🏗️ 结构概览

新兴非易失性存储器通常采用交叉阵列 (Crossbar) 结构或 1T1R (一个晶体管、一个电阻/存储元件) 配置，以实现高密度集成。

![图：典型非易失性存储器（PCM）单元与阵列结构](../../raw/figures/xueEmergingNonvolatileMemories2011/fig_1_YA2TDDV5.png)
*   **看图要点**：展示了相变存储器 (PCM) 的单元结构，包含加热器和相变材料（GST）。右侧展示了其在位线/字线交叉阵列中的集成方式。
*   **来源**：[[../papers/xueEmergingNonvolatileMemories2011]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 核心机制与分类

### 物理存储机制
新兴 NVM 不再单纯依赖电容里的电荷，而是利用材料的结构或物性变化：
*   **铁电 (FeRAM/FeFET)**：利用铁电材料的自发极化方向。
*   **磁性 (STT-MRAM)**：利用磁隧道结 (MTJ) 中自由层的磁化方向。
*   **阻变 (RRAM)**：利用氧化物中导电细丝（如氧空位）的形成与断裂。
*   **相变 (PCM)**：利用材料在非晶态（高阻）与晶态（低阻）之间的转换。

### 性能挑战
虽然 NVM 具有非易失性，但在推向大规模应用时面临“读写不对称性”、“写耐久性”和“能效权衡”等挑战。例如，PCM 的写操作通常比读操作慢且耗能。

## 📚 相关论文 (Related Papers)

- [[../papers/xueEmergingNonvolatileMemories2011]]：系统梳理了 PCM、STT-RAM 和忆阻器的器件物理与系统挑战。
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：探讨了铪基铁电在下一代存储中的应用。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/in-memory-computing|存内计算]]
- [[../concepts/write-endurance|写耐久性]]
- [[../entities/FeFET|FeFET]]
- [[../entities/FTJ|FTJ]]
- [[../concepts/memristor|忆阻器]]
- [[../concepts/phase-change-memory|相变存储器]]
- [[../concepts/stt-ram|STT-RAM]]
