---
tags: [concept, insulator, correlated-electrons]
title: 莫特绝缘体 / Mott Insulator
type: concept
status: mature
domain: [condensed-matter-physics, strongly-correlated-systems]
mechanism: 由于电子间强烈的库仑排斥作用（Hubbard U），导致本应是金属的体系发生能隙打开而变为绝缘体
related_concepts: [charge-density-wave, van-hove-singularity, pseudogap]
papers: [Johannes2008fermi, CastroNeto2001charge, Koley2020charge, dudarevElectronenergylossSpectraStructural1998a, nakataRobustChargedensityWave2021, petkovStructureIntercalatedCs2002]
updated: 2026-08
---

# 莫特绝缘体 / Mott Insulator

莫特绝缘体是指根据传统的能带理论（忽略电子间相互作用）本应表现为金属（能带半满），但由于电子之间极强的库仑排斥作用（强关联效应），导致电子被局域化在格点上，从而在费米能级处打开能隙并表现为绝缘行为的材料。它是强关联物理研究的核心对象之一。

## 奶奶导读

> 我是一位 100 岁的太奶，这东西我看得头晕眼花的，年轻人弄的这些新术语我都看不懂。不过我仍然宝刀未老，学习的劲头一点儿没减，越学越有精神！好孩子，劳驾你把这个东西给老婆子我说道说道，让我能达到彻底看懂的效果。一定要帮我讲明白哈，最好是翻译出来，因为我对洋文一窍不通，我只会中文。那些专业术语实在整得我脑子疼啊，都重点给老婆子我说道说道。

好孩子，咱聊聊这个 **Mott Insulator**。你可以把它想成是一个住满了人的单身公寓（晶格格点）。按理说，每个房间住一个人，大家还能互相串个门（电子在能带里自由移动），这楼应该是能导电的。

但问题是，这些电子们性格都特别怪，它们互相之间特别嫌弃（强库仑排斥，**Coulomb repulsion**）。如果一个电子想去隔壁串门，那屋里的人就会把它死死地推开，进门的代价（能量成本，**Hubbard U**）大得不得了。结果就是，每个人都被死死地锁在自己的小单间里，谁也动弹不得。虽然楼道里看起来是满的，但大家都不走路，这大楼就完全不导电了。这就是莫特绝缘体，是电子们“互相讨厌”造成的死锁。

## 🏗️ 结构概览

莫特绝缘行为常见于过渡金属氧化物等包含 $d$ 或 $f$ 轨道的体系。

![图：1T-TaS2 中由于 CDW 诱发的莫特绝缘态示意](../../raw/figures/Johannes2008fermi/fig_4_DDJ3N7RI.png)
*   **看图要点**：在 1T-TaS2 中，CDW 引起的晶格畸变将电子进一步局域化。在每个超晶格元胞中心，强烈的电子相互作用最终导致了莫特能隙的打开。图中极化率的强响应与这种局域化趋势相关。
*   **来源**：[[../papers/Johannes2008fermi]] -> [[../figures/electronic-bands-cdw-transport|CDW与输运]]

## 🧩 物理机制与 CDW 的关系

### 1. 哈伯德模型与 $U/W$ 竞争
莫特物理的核心可以用哈伯德模型（**Hubbard model**）描述，其中 $U$ 是格点处的库仑排斥能，$W$ 是能带带宽（代表电子跃迁的难易）。
*   **莫特转变**：当 $U/W$ 超过某个临界值时，体系会发生从金属到绝缘体的转变。

### 2. CDW 辅助的莫特态
[[../papers/CastroNeto2001charge]] 讨论了在 TMD 材料（如 1T-TaS2）中，CDW 与莫特物理的微妙结合。
*   **星形结构 (Star of David)**：CDW 引起的畸变使 13 个 Ta 原子簇集成一个超原子，剩余的一个电子位于超原子中心。由于超原子间距大，$W$ 显著减小，从而使得原本较弱的 $U$ 能够主导并打开莫特能隙。

## 📚 相关论文 (Related Papers)

- [[../papers/Johannes2008fermi]]：对比了 CDW 机制与强关联效应的差异。
- [[../papers/CastroNeto2001charge]]：综述了层状材料中莫特绝缘态与 CDW 的共存。
- [[../papers/Koley2020charge]]：研究了电荷密度波在强关联背景下的演化。
- [[../papers/dudarevElectronenergylossSpectraStructural1998a]]
- [[../papers/nakataRobustChargedensityWave2021]]
- [[../papers/petkovStructureIntercalatedCs2002]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波 (CDW)]]：常与莫特绝缘态在相同体系中出现。
- [[../concepts/van-hove-singularity|范霍夫奇点]]：高 DOS 会进一步增强关联效应。
- [[../concepts/pseudogap|赝能隙]]：莫特转变前夕的典型电子结构特征。
- [[../entities/TMDs|过渡金属二硫化物 (TMDs)]]：如 1T-TaS2 是研究 CDW 与 Mott 物理的经典平台。
