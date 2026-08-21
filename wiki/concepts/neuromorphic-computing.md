---
tags: [concept, computing, brain-inspired]
title: 神经形态计算 (Neuromorphic Computing)
type: concept
status: mature
domain: [artificial-intelligence, computer-architecture, neuroscience]
mechanism: 模拟生物神经系统（神经元与突触）的并行、异步、存算一体计算范式
related_concepts: [synaptic-plasticity, in-memory-computing, memristor, synaptic-weight]
papers: [chenHafniumBasedFerroelectricPostMoore2026, xueEmergingNonvolatileMemories2011, huangTwodimensionalIn2Se3Rising2022, sunSlidingFerroelectricityTwodimensional2025, tahirFerroelectricityNonvolatileMemristor2025, zhangNonvolatileControlTopological2025]
updated: 2026-08
---

# 神经形态计算 / Neuromorphic Computing

神经形态计算是一种借鉴生物神经系统原理构建的新型计算范式。它旨在通过模拟神经元（处理器）和突触（存储与通信权重）的结构与功能，实现高能效、大规模并行的信息处理。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“神经形态计算”其实就是让机器学着像咱们脑瓜子一样去思考。现在的电脑像个刻板的小会计，算个数得在算盘（CPU）和账本（内存）之间来回跑，累得够呛还费电。
> 
> 咱这脑瓜子可不一样，记东西和想事情是在一块儿的，而且千万个“脑细胞”（神经元）能同时干活。这个新技术就是想做一种芯片，里头的零件就像咱的神经元和它们之间的接头（突触），能一边记着数儿一边把活儿干了。这样电脑就能像人一样，看一眼就能认出熟人，还没那么费电。

## 🏗️ 结构概览

神经形态硬件的核心是能够模拟“突触”权重的多态存储器件阵列，如 FeFET 或忆阻器阵列。

![图：神经形态系统集成与应用总览](../../raw/figures/chenHafniumBasedFerroelectricPostMoore2026/fig_1_3VD9GL58.png)
*   **看图要点**：展示了从铁电材料到器件阵列，再到实现神经形态计算（如图像识别）的完整层级结构。
*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 核心特征与物理实现

### 存内计算 (In-Memory Computing)
神经形态计算打破了冯·诺依曼架构的瓶颈。在硬件阵列中，通过欧姆定律和基尔霍夫定律，可以原位实现向量-矩阵乘法 (VMM)，这是神经网络最基础的操作。

### 突触可塑性模拟
利用铁电极化的部分翻转或忆阻器导电丝的微调，可以实现电导的连续变化。这种模拟特性能完美对应生物突触的长时程增强 (LTP) 和长时程抑制 (LTD)。

### 典型架构
*   **SNN (脉冲神经网络)**：模拟神经元的发放 (Spiking) 机制，仅在有信号时触发计算，极大降低功耗。
*   **Crossbar 阵列**：高密度的交叉点阵，利用非易失器件作为连接权重。

## 📚 相关论文 (Related Papers)

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：详细介绍了基于铪基铁电器件的神经形态系统实现。
- [[../papers/xueEmergingNonvolatileMemories2011]]：讨论了忆阻器在模拟突触功能中的应用。
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]：从综述角度梳理了「Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage」。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]]
- [[../papers/zhangNonvolatileControlTopological2025]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/synaptic-plasticity|突触可塑性]]
- [[../concepts/in-memory-computing|存内计算]]
- [[../concepts/synaptic-weight|突触权重]]
- [[../concepts/memristor|忆阻器]]
- [[../entities/FeFET|FeFET]]
- [[../entities/FTJ|FTJ]]
