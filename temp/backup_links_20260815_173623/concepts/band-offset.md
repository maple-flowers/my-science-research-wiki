---
tags: [concept, physics, semiconductor]
title: 能带偏移 (Band Offset)
type: concept
status: mature
domain: [semiconductor-physics, heterostructures]
mechanism: 异质结界面处导带或价带能量的突跳（跳变值）
related_concepts: [band-alignment, schottky-barrier, work-function, proximity-effect]
papers: [duUltrasensitiveOptoelectronicBiosensor2025, chenHafniumBasedFerroelectricPostMoore2026]
updated: 2026-08
---

# 能带偏移 / Band Offset ($\Delta E$)

能带偏移是指在异质结界面处，两种不同材料的相应能带（导带底或价带顶）之间存在的能量差值。它包含导带偏移 ($\Delta E_c$) 和价带偏移 ($\Delta E_v$)。能带偏移决定了异质结势垒的高度，是控制半导体器件中载流子限域和输运的最关键定量参数。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“能带偏移”就是两家地基之间的“台阶高度”。如果说“能带对齐”是看两座楼怎么对齐的，那“能带偏移”就是量一量那个具体的台阶到底有多高。
> 
> 你从这一家往那一家搬砖（电子），这台阶（偏移）越高，你就越费劲，砖头就越容易被挡在外面。科学家们非要把这个高度算得清清楚楚，就是为了知道要加多大的电（电压），才能让电子蹦过这个台阶，或者是把电子关在这个“坑”里别让它乱跑。这高度差哪怕只变了一丁点，芯片的性能可能就天差地别了。

## 🏗️ 结构概览

能带偏移直接定义了量子阱的深度或异质结势垒的高度。

![图：二维异质结界面处的能带偏移与载流子注入](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_1_BXNBIMFM.png)
*   **看图要点**：图中暗示了石墨烯与金电极或不同转角石墨烯层间的能级差异。$\Delta E$ 决定了光激发产生的电子是否有足够的能量跨越界面，从而转化为可测量的电流。
*   **来源**：[[../papers/duUltrasensitiveOptoelectronicBiosensor2025]] -> [[../figures/electronic-devices-sensors|传感器与探测器]]

## 🧩 物理机制与计算

### 偏移的组成
$$\Delta E_c = \chi_1 - \chi_2$$
$$\Delta E_v = (E_{g2} + \chi_2) - (E_{g1} + \chi_1)$$
这是基于真空能级对齐的理想模型。在实际界面，电荷转移导致的电偶极子层会进一步修正这些数值。

### 二维材料中的特殊性
在范德华异质结中，由于缺乏强共价键，能带偏移受应力和层间转角的影响极大。通过改变转角（莫尔工程），可以有效地连续调节能带偏移，实现对激子行为的精准操控。

### 计算方法
*   **DFT 计算**：通过构建超胞模型，计算界面电势分布，提取宏观平均电势，从而确定能带偏移。
*   **实验测量**：主要手段包括 X 射线光电子能谱 (XPS) 和紫外光电子能谱 (UPS)。

## 📚 相关论文 (Related Papers)

- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]：利用转角调控 VHS 位置，实质上是利用了层间转角对能带偏移的调制作用。
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：探讨了极化电荷如何诱导额外的静电势，从而动态改变有效能带偏移。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/band-alignment|能带对齐]]
- [[../concepts/schottky-barrier|肖特基势垒]]
- [[../concepts/work-function|功函数]]
- [[../concepts/van-der-waals-heterostructure|vdW 异质结]]
