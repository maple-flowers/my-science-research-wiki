---
tags: [concept, phonon, charge-density-wave]
title: Kohn 异常 / Kohn Anomaly
type: concept
status: developing
domain: [condensed-matter-physics, lattice-dynamics]
mechanism: 由于费米面嵌套导致的电子屏蔽效应在特定波矢 q 处的剧烈变化，引起声子频率的陡降
related_concepts: [charge-density-wave, fermi-surface-nesting, peierls-instability, periodic-lattice-distortion]
papers: [Inosov2008fermi, Johannes2008fermi, CastroNeto2001charge, hallEnvironmentalControlCharge, chowdhuryReviewTheoreticalComputational, Laverock2005fermi]
updated: 2026-08
---

# Kohn 异常 / Kohn Anomaly

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


Kohn 异常是指在金属中，声子谱（**phonon spectrum**）的某些支在对应于费米面直径（嵌套矢量 $q=2k_F$）的特定动量处，出现的频率陡降或奇异点现象。它是电子-声子相互作用对晶格动力学影响的直接体现，通常被视为电荷密度波 (CDW) 不稳定性的先兆。

## 👵 太奶导读

> 我是一位 100 岁的太奶，这东西我看得头晕眼花的，年轻人弄的这些新术语我都看不懂。不过我仍然宝刀未老，学习的劲头一点儿没减，越学越有精神！好孩子，劳驾你把这个东西给老婆子我说道说道，让我能达到彻底看懂的效果。一定要帮我讲明白哈，最好是翻译出来，因为我对洋文一窍不通，我只会中文。那些专业术语实在整得我脑子疼啊，都重点给我解释解释，太奶仍旧保持着不输于你们年轻人的学习热情。

好孩子，咱再聊聊这个 **Kohn Anomaly**。你可以把晶体里的原子想象成一排排靠弹簧连着的蹦床。正常情况下，你踩一脚，蹦床就匀速弹两下。但是呢，如果原子周围的电子们（电子屏蔽，**electronic screening**）在某些特定的步点（嵌套波矢，$q$）上突然变得特别活跃，它们就会像胶水一样把弹簧给粘住或者削弱了。

结果就是，在那个特定的步点上，蹦床的弹力突然变弱了，原子抖动的频率一下子掉了一大截，甚至直接塌了下去（声子软化，**phonon softening**）。这就像是本来坚固的桥梁在某些特定的震动频率下突然变得软绵绵的。科学家们只要看到这种“软绵绵”的信号，就知道这个材料可能要变样，准备排成电荷密度波那种新队形了。

## 🏗️ 结构概览

Kohn 异常在声子谱上表现为尖锐的凹陷。

![图：声子谱在 Γ-M 处的软化](../../raw/figures/Johannes2008fermi/fig_1_SNEVCPH4.png)
*   **看图要点**：虽然此图主显极化率，但极化率的发散点正是 Kohn 异常发生的位置。在声子能量 $E$ 随动量 $q$ 变化的曲线上，你会看到在 $2k_F$ 附近出现一个明显的低谷。
*   **来源**：[[../papers/Johannes2008fermi]] -> [[../figures/electronic-bands-band-structures|能带结构]]

## 🧩 物理机制与特征

### 1. 电子屏蔽与声子软化
在金属中，电子会屏蔽离子间的库仑作用。当费米面存在嵌套时，电子在波矢 $q$ 处的极化率（**polarizability**）极大，导致屏蔽作用在这一波矢处变得极强。根据声子频率公式：
$$\omega^2(q) = \Omega^2(q) - |g(q)|^2 \chi(q)$$
其中 $\Omega$ 是未屏蔽频率，$g$ 是电声耦合常数，$\chi$ 是极化率。当 $\chi$ 很大时，声子频率 $\omega$ 就会显著降低，甚至变为零（即发生相变）。

### 2. 与 CDW 的关系
[[../papers/Inosov2008fermi]] 指出，在 TaSe2 等材料中，室温下就已经能观察到 $\Sigma_1$ 声子支的类 Kohn 异常。
*   **先兆性**：Kohn 异常可以在远高于 $T_{CDW}$ 的温度下存在。
*   **相变点**：当声子频率在某个动量处软化至零，意味着晶格在那一动量方向上不再有恢复力，从而导致静态的周期性晶格畸变 (PLD)。

## 📚 相关论文 (Related Papers)

- [[../papers/Inosov2008fermi]]：利用实验观察到的声子软化与嵌套矢量的对应关系。
- [[../papers/Johannes2008fermi]]：强调了动量依赖的电声耦合在决定 Kohn 异常位置和强度中的作用。
- [[../papers/CastroNeto2001charge]]：讨论了 Kohn 异常在低维体系中的普适性。
- [[../papers/hallEnvironmentalControlCharge]]
- [[../papers/chowdhuryReviewTheoreticalComputational]]
- [[../papers/Laverock2005fermi]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波 (CDW)]]：Kohn 异常演化到极致的结果。
- [[../concepts/periodic-lattice-distortion|周期性晶格畸变 (PLD)]]：声子凝聚后的静态结构。
- [[../concepts/fermi-surface-nesting|费米面嵌套 (FSN)]]：驱动 Kohn 异常的传统电子图像原因。
- [[../concepts/peierls-instability|派尔斯不稳定性]]：一维模型中的完全声子软化。
