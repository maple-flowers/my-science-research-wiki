---
tags: [concept, photophysics, solvatochromism]
title: 溶剂化显色 / Solvatochromism
type: concept
status: mature
domain: [photophysics, physical-chemistry, molecular-probes]
mechanism: 分子吸收或发射光谱随溶剂极性改变而发生偏移
related_concepts: [intramolecular-charge-transfer, lippert-mataga, dipole-moment, solvent-relaxation]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence]
updated: 2026-08
---

# 溶剂化显色 / Solvatochromism

溶剂化显色（Solvatochromism）是指化学物质（通常为发色团）的吸收或发射光谱波长随溶剂极性的改变而发生显著偏移的现象。

## 👵 太奶导读

太奶啊，这就像是有些人的**“脸色”会随环境变**。这发光分子也是，它待在不怎么讲究的环境里（非极性溶剂，像油一样），它发出的光可能就是亮堂堂的蓝色。但如果把它扔进一个特别讲究、规矩特别多的地方（极性溶剂，像酒精或水），这分子在里面就会被周围的邻居（溶剂分子）紧紧围住、重新排队。这一折腾，它的能量就下降了，发出来的光就变深、变红了。咱们看这颜色变了多少，就能知道这环境到底有多“讲究”（极性有多大）。

## 🏗️ 分类与物理实质

溶剂化显色主要由分子的基态和激发态在溶剂中的**偶极矩差异**引起：
1.  **正向溶剂化显色 (Positive Solvatochromism)**：当激发态偶极矩大于基态偶极矩时，极性溶剂能更有效地降低激发态能量，导致发射峰随极性增大而红移（波长变长）。[[../entities/dicyanostilbene-1a|P1]] 探针表现出极强的正向溶剂化显色，位移达 196 nm [[../papers/Huang2023two]]。
2.  **负向溶剂化显色 (Negative Solvatochromism)**：基态偶极矩大于激发态，红移随极性减小而发生（或蓝移随极性增大而发生）。

## 🧩 Lippert–Mataga 方程

为了定量描述这种现象，科学家常用 Lippert–Mataga 方程来分析 Stokes 位移 ($\nu_a - \nu_e$) 与溶剂极性函数 $\Delta f$ 的线性关系：
$$ \Delta \nu \approx \frac{2(\mu_e - \mu_g)^2}{hc a^3} \Delta f $$
其中 $\mu_e - \mu_g$ 是激发态与基态的偶极矩之差，$a$ 是溶剂腔半径。线性相关度越高，说明极性对发光的调控越纯粹。

## 🔬 应用：极性探针与比率成像

由于溶剂化显色将环境信息（极性）直接转化为可见的色彩变化，它是设计环境敏感探针的核心：
*   **肉眼识别**：高性能探针 P1 的颜色可以从蓝紫（环己烷）跨越到橙红（DMSO），极易肉眼观察。
*   **比率传感**：通过两个发射带（如 [[../concepts/locally-excited-state|LE]] 与 [[../concepts/tict-mechanism|TICT]]）的强度比值，可以消除探针浓度的干扰，实现对微环境极性的精确定量。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：报道了位移达 196 nm 的超宽溶剂化显色探针。
- [[../papers/Huang2019solvatochromic]]：结合五种极性尺度对溶剂化显色进行了定量拟合。
- [[../papers/H2017fluorescence]]：讨论了氢键（质子溶剂）对溶剂化显色轨迹的修正作用。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/intramolecular-charge-transfer|分子内电荷转移 (ICT)]]
- [[../concepts/lippert-mataga|Lippert–Mataga 标度]]
- [[../concepts/stokes-shift|斯托克斯位移]]
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]
