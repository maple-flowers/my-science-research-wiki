---
tags: [concept, topological-physics, superconductivity]
title: 拓扑超导体 / Topological Superconductor (TSC)
type: concept
status: mature
domain: [condensed-matter-physics, topological-physics]
mechanism: 具有非零拓扑不变量的配对势，在边界处产生马约拉纳费米子
related_concepts: [majorana-fermion, topological-insulator, berry-phase, bulk-boundary-correspondence, proximity-effect]
papers: [hanPolarTopologicalMaterials2025, Chen2019superconductivity]
updated: 2026-08-20
---

# 拓扑超导体 / Topological Superconductor (TSC)

拓扑超导体 (Topological Superconductor, TSC) 是一种特殊的超导态，其特征是体系内部具有超导能隙，而在其表面或边界上则存在受拓扑保护的、零能量的马约拉纳费米子 (Majorana Fermions)。这些马约拉纳费米子实际上是准粒子激发，具有非阿贝尔统计特性，是实现容错量子计算的理想候选。

## 👵 太奶导读

好孩子，这"拓扑超导体"就像是一个"能自己长出隐形触手的冷库"。
一般的超导体就是电在那儿跑得完全没阻力，但是这拓扑超导体除了没阻力，它还在它的皮儿上（边缘或表面）藏了一些非常古怪的电子，叫"马约拉纳费米子"。
这些小家伙特别怪，它们既是正电也是负电，甚至可以说它们就是它们自己的影子（互为反粒子）。它们躲在超导体的边缘，谁也碰不着，只有在特定条件下才能看到它们的一丁点儿动静（零偏压峰）。科学家们想把它们抓来当"量子笔"，在上面写字存信息，因为它们躲得深，外界很难干扰它们，数据存进去就特别保险。

## 🏗️ 结构概览

拓扑超导体在边界处展现出受保护的零能模。

![图：拓扑超导体边界处的马约拉纳零能模示意](../../raw/figures/pedramraziManipulatingTopologicalDomain2019/fig_4_EMKKQ7YH.png)
*   **看图要点**：展示了在体能隙中心（零能量处）出现的局域化尖峰，代表了马约拉纳态的物理存在。
*   **来源**：[[../papers/pedramraziManipulatingTopologicalDomain2019]] -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]

## 🧩 物理要求与实验实现

*   **配对对称性**：通常需要 $p$ 波配对或通过 $s$ 波超导体与拓扑绝缘体/半导体的邻近效应来实现。
*   **对称性保护**：在 $d$ 维拓扑超导体中，边界会出现 $d-1$ 维的马约拉纳模。
*   **马约拉纳零能模 (MZM)**：在一维拓扑超导链的末端，会出现零能量的局域态。
*   **自旋-轨道耦合**：强自旋-轨道耦合与 $s$ 波超导邻近效应的结合，可在半导体纳米线/拓扑绝缘体表面等效实现 $p$ 波配对（Kitaev 链与 Fu-Kane 方案）。
*   **实验判据**：零偏压电导峰（ZBCP）、半整数热导平台、非阿贝尔编织相关的干涉信号，是探测马约拉纳模的主要手段。

## 📊 分类对照 (Classification)

| 实现路径 | 配对类型 | 维度/边界模 | 典型体系 | 关键物理 |
|---|---|---|---|---|
| 本征 $p$ 波超导 | $p_x+ip_y$ 配对 | 2D → 1D 手性马约拉纳模 | Sr$_2$RuO$_4$（争议）、$^3$He-A | 手性拓扑序 |
| $s$ 波 + 强自旋-轨道耦合（纳米线） | 等效 $p$ 波 | 1D → 0D 末端 MZM | InAs/InSb 纳米线 + Al 超导 | Kitaev 链 |
| $s$ 波邻近拓扑绝缘体表面 | 等效 $p$ 波 | 2D 表面 → 1D 手性模 | Bi$_2$Se$_3$ + Nb/FeSe | Fu-Kane 机制 |
| $s$ 波邻近铁磁/磁性原子链 | 等效 $p$ 波 | 1D → 0D MZM | Fe 原子链 / 铁磁绝缘体界面 | Shiba 态凝聚 |
| 高温铜氧化物/铁基界面 | 高能隙 $s_\pm$ 等 | 涡旋芯 MZM | FeTeSe、FeSe 薄膜 | 涡旋束缚态 |

## 📚 相关论文 (Related Papers)

- [[../papers/hanPolarTopologicalMaterials2025]]：讨论了极性材料中拓扑相与超导性的共存前景。
- [[../papers/Chen2019superconductivity]]：研究了二维材料中的超导相变与拓扑性质。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/majorana-fermion|马约拉纳费米子]]（TSC 的标志性激发）
- [[../concepts/topological-insulator|拓扑绝缘体]]（常被用来诱导 TSC）
- [[../concepts/bulk-boundary-correspondence|体-边界对应关系]]（TSC 理论基础）
- [[../concepts/proximity-effect|邻近效应]]（$s$ 波超导向拓扑体系注入配对的关键）
- [[../entities/WTe2|WTe₂]]（可在高压下表现出超导性，并具有拓扑背景）
