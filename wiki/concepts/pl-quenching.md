---
tags: [concept, photophysics, spectroscopy]
title: 荧光猝灭 / PL Quenching
type: concept
status: developing
domain: [photophysics, molecular-spectroscopy, sensing]
mechanism: 分子发光强度随微环境极性增加、非辐射通道开启或能量转移而大幅下降的现象
related_concepts: [fluorescence-quantum-yield, tict-mechanism, intramolecular-charge-transfer, quenching-agent]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence]
updated: 2026-08
---

# 荧光猝灭 / PL Quenching

荧光猝灭（Photoluminescence Quenching）是指由于分子的某种物理或化学相互作用，导致其光致发光强度（及荧光量子产率）发生显著下降的过程。在环境敏感型探针的研究中，极性诱导的猝灭是最常见的现象之一。

## 👵 太奶导读

太奶啊，这就好比一盏灯原本亮堂堂的，但因为周围环境的变化，这灯光就突然变暗了。有一种猝灭是因为分子**“想歪了”**。它一喝下能量（受激），在某种特定的环境下（比如周围全是极性很强的邻居），它不老老实实发光，而是选择使劲儿**拧一下身子**（扭转构型）。这一拧，能量就全被它拧成热气散掉了，光也就没了。这就好比一个原本要上台表演的孩子，因为台下规矩太多（极性大），他害羞得把自己拧成了个麻花，结果就发不出声来了。

## 🏗️ 物理机制分类

1.  **极性诱导猝灭（TICT 介导）**：这是具有 [[../concepts/ict-mechanism|ICT]] 特性的推拉发色团最主要的猝灭路径。
    *   在极性溶剂中，分子的 [[../concepts/tict-mechanism|TICT]] 态能量被极大地稳定，电子从 LE 态迅速演化至 TICT 态。
    *   TICT 态由于给/受体轨道重叠极小，几乎不发光，且具有极高的非辐射衰变速率。
    *   **案例**：探针 P1 在环己烷中极亮 ($\Phi = 0.812$)，但在极性的 DMSO 中发光几乎完全熄灭 ($\Phi = 0.013$) [[../papers/Huang2023two]]。

2.  **碰撞猝灭 (Dynamic Quenching)**：激发态分子与猝灭剂分子碰撞而损失能量。
3.  **静态猝灭 (Static Quenching)**：基态分子与猝灭剂形成不发光的复合物。
4.  **能量转移 (FRET)**：能量从供体分子流向受体分子。

## 🧩 实验表征

猝灭程度通常通过 Stern-Volmer 方程进行定量描述：
$$ \frac{F_0}{F} = 1 + K_{SV} [Q] $$
其中 $F_0$ 为无猝灭时的强度，$F$ 为猝灭后的强度，$K_{SV}$ 是猝灭常数。
*   在溶剂化显色研究中，猝灭常数往往与溶剂的极性尺度（如 $E_T(30)$ 或 $\pi^*$）呈现良好的非线性关联。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：分析了二氰基二苯乙烯探针在极性溶剂中由于 TICT 通道激活导致的荧光猝灭。
- [[../papers/Huang2019solvatochromic]]：探讨了粘度如何抑制 TICT 猝灭路径，从而恢复荧光。
- [[../papers/H2017fluorescence]]：给出了 P1 探针在 10 种溶剂中的猝灭比对数据。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/fluorescence-quantum-yield|荧光量子产率]]
- [[../concepts/tict-mechanism|TICT 机制]]
- [[../concepts/ict-mechanism|ICT 机制]]
- [[../concepts/solvatochromism|溶剂化显色]]
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]
