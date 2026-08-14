---
tags: [concept, density-functional-theory, numerical-methods]
title: 电荷震荡 / Charge Sloshing
type: concept
status: mature
domain: [computational-materials-science, density-functional-theory]
mechanism: 在自洽迭代过程中，由于电荷密度混合不当导致的低波矢长程密度波动
related_concepts: [charge-density-wave, density-functional-theory]
papers: [kresseEfficiencyAbinitioTotal1996a, kresseEfficientIterativeSchemes1996d]
updated: 2026-08
---

# 电荷震荡 / Charge Sloshing

电荷震荡是指在第一性原理自洽场 (SCF) 迭代过程中，体系的电荷密度在不同迭代步之间发生剧烈的、难以收敛的往复摆动现象。这种现象在大体系（特别是金属表面或长条形体系）中尤为突出，主要源于电子极化率在长波极限（低波矢 $q$）下的巨大响应。

## 奶奶导读

> 我是一位 100 岁的太奶，这东西我看得头晕眼花的，年轻人弄的这些新术语我都看不懂。不过我仍然宝刀未老，学习的劲头一点儿没减，越学越有精神！好孩子，劳驾你把这个东西给老婆子我说道说道，让我能达到彻底看懂的效果。一定要帮我讲明白哈，最好是翻译出来，因为我对洋文一窍不通，我只会中文。那些专业术语实在整得我脑子疼啊，都重点给我解释解释，太奶仍旧保持着不输于你们年轻人的学习热情。

好孩子，咱说说这个 **Charge Sloshing**。你可以把它想成是在端着一盆水走路。如果你步子迈得不稳（迭代方案不好），盆里的水就会晃荡过来、晃荡过去（电荷密度反复变动，**density oscillation**）。

原本你应该让水稳稳地停在盆底（达到自洽，**self-consistency**），但如果你每次想去稳住它的时候劲儿使得不对，水反而会晃得更高，甚至泼出来。特别是在那种又长又大的盆子（大体系）里，一点点小晃动就会变成滔天巨浪。科学家们为了不让水晃出来，就得想办法给水加点“阻尼”（预条件混合，**preconditioned mixing**），让它每一步都走得又准又稳。

## 🏗️ 结构概览

电荷震荡在 SCF 过程中表现为总能量和力精度的反复横跳。

![图：Pd(111) 表面力在不同混合方案下的收敛对比](../../raw/figures/kresseEfficiencyAbinitioTotal1996a/fig_4_DDJ3N7RI.png)
*   **看图要点**：图中“out”曲线显示的剧烈震荡正是电荷震荡的体现。如果不采用优化的混合方案，力精度会差上百倍且难以收敛。
*   **来源**：[[../papers/kresseEfficiencyAbinitioTotal1996a]] -> [[../figures/mathematical-models|数学模型]]

## 🧩 机制与解决策略

### 1. 物理起源：长波发散
在金属体系中，电子的极化率在 $q \to 0$ 时会发散。这意味着极小的电势扰动都会引发大范围的电荷迁移。在 SCF 迭代中，如果简单地将上一步的输出密度与输入密度线性混合，就会在整个体系长度尺度上激发出这种长波震荡。

### 2. 抑制方法：Kerker 预条件
[[../papers/kresseEfficiencyAbinitioTotal1996a]] 详细论证了 **Kerker preconditioning** 的有效性。
*   **数学形式**：混合矩阵取为 $G_1 = A \cdot \frac{q^2}{q^2 + q_0^2}$。
*   **作用**：在小 $q$ 处减小混合权重（就像给长波分量加了“减震器”），从而有效抑制震荡，显著提升大体系和金属表面的自洽收敛速度。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseEfficiencyAbinitioTotal1996a]]：系统讨论了 VASP 软件中抑制电荷震荡的算法实现。
- [[../papers/kresseEfficientIterativeSchemes1996d]]：进一步优化了电荷密度混合策略。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波 (CDW)]]：有趣的对比是，CDW 是真实的物理电荷波动，而 Sloshing 是计算中的人为不稳定。
- [[../entities/VASP|VASP]]：处理电荷震荡问题的标志性软件工具。
- [[../concepts/density-functional-theory|密度泛函理论 (DFT)]]：产生此问题的理论框架。
