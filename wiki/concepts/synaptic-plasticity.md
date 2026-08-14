---
tags: [concept, biology, neuroscience]
title: 突触可塑性 (Synaptic Plasticity)
type: concept
status: mature
domain: [neurobiology, biophysics, neuromorphic-engineering]
mechanism: 生物突触根据活动强度的变化而增强或减弱其连接强度的能力
related_concepts: [neuromorphic-computing, synaptic-weight, memristor, LTP-LTD]
papers: [chenHafniumBasedFerroelectricPostMoore2026, xueEmergingNonvolatileMemories2011]
updated: 2026-08
---

# 突触可塑性 / Synaptic Plasticity

突触可塑性是指生物神经元之间的连接（突触）能够根据神经元活动的强弱改变其传递信号效率的性质。它是大脑学习和记忆的微观物理基础。在神经形态工程中，突触可塑性被抽象为电学器件电导（或电阻）的连续可调特性。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“突触可塑性”就是咱脑子里的“熟能生巧”。你想啊，两个脑细胞之间有一条走水的小沟（突触）。如果你天天走这条路，琢磨同一件事（活动频繁），那水流就会越来越大，把沟冲得越来越宽，以后水一放就过去了（连接变强，就是记住了）。如果你好久不想不练（活动减少），这沟就会慢慢淤积，水也流不过去了（连接变弱，就是忘掉了）。
> 
> 现在科学家用那些能变阻的小零件（比如铁电晶体管、忆阻器），也是想在里面通一通电（施加脉冲），让它里头的电阻一会儿大、一会儿小，就像脑子里冲沟一样，能把学过的东西记下来，或者是慢慢忘掉，这就是用机器学人脑。

## 🏗️ 结构概览

在微电子器件中，通常通过施加连续的电压脉冲来调控器件的电导状态，模拟生物突触的各种行为。

![图：基于铁电器件模拟的突触可塑性](../../raw/figures/chenHafniumBasedFerroelectricPostMoore2026/fig_8_49WAIQHG.png)
*   **看图要点**：图中展示了通过不同电压脉冲序列在铁电器件上实现的突触响应。包括双脉冲易化 (PPF)、长时程增强/抑制 (LTP/LTD) 曲线，完美模拟了生物突触的渐进电导演化。
*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 物理模型与实现

### 短时程可塑性 (STP)
短时程可塑性包括：
*   **EPSC (兴奋性突触后电流)**：单个刺激脉冲引起的瞬态电导响应。
*   **PPF (双脉冲易化)**：两个相近脉冲引起的响应，第二个通常大于第一个，对应大脑的短期记忆或注意。

### 长时程可塑性 (LTP/LTD)
长时程增强 (LTP) 和长时程抑制 (LTD) 是突触连接强度的持久性增加或减小。在硬件中，通过铁电极化的非均匀成核或氧空位通道的连续移动，实现电导在多次读写循环中的稳定多态变化。

### 脉冲时间依赖可塑性 (STDP)
一种赫布学习规则 (Hebbian rule)，突触权重的改变取决于前后神经元发放脉冲的相对时间差。

## 📚 相关论文 (Related Papers)

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：系统评估了铁电器件在模拟 LTP/LTD 和 STDP 规则时的表现。
- [[../papers/xueEmergingNonvolatileMemories2011]]：提及了忆阻器在模拟突触特性中的巨大潜力。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/neuromorphic-computing|神经形态计算]]
- [[../concepts/synaptic-weight|突触权重]]
- [[../concepts/memristor|忆阻器]]
- [[../entities/FeFET|FeFET]]
- [[../entities/FTJ|FTJ]]
