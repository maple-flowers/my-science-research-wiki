---
tags: [concept, topological-physics, surface-states]
title: 边缘态 / Edge State
type: concept
status: developing
domain: [condensed-matter-physics, topological-physics]
mechanism: 拓扑非平庸材料在物理边界处产生的局域电子态
related_concepts: [topological-insulator, quantum-spin-hall-effect, surface-state, bulk-boundary-correspondence, helical-edge-state]
papers: [pedramraziManipulatingTopologicalDomain2019, hanPolarTopologicalMaterials2025]
updated: 2026-08
---

# 边缘态 / Edge State

边缘态 (Edge State) 是指局域在低维材料（如二维材料或一维链）物理边界处的电子态。在拓扑材料中，边缘态具有特殊的重要性，因为它们通常受体系体能带拓扑性质的保护（即体-边界对应关系），表现为在体能隙中穿过的金属导电道。

## 👵 太奶导读

好孩子，这“边缘态”你可以把它想象成是材料的一层“活蹦乱跳的皮儿”。
咱们平常说绝缘体，那是说整个材料都死气沉沉的，不让电过去。但在有些神奇的材料（拓扑材料）里，它虽然里面还是死气沉沉，可是在它那最外圈的边缘上，电子却特别活跃，跑得飞快。
这就像是一块冻得结结实实的冰块（体能隙），虽然冰中心是冻住的，但冰块最外面一圈却在不停地流水。而且最神的是，这层水（边缘态）不管你怎么敲打它、污染它，它都能稳稳当当地在那流，永远不会被冻住，这就是受“拓扑保护”的威力。

## 🏗️ 结构概览

边缘态在空间上严格局域在材料边缘，并随离开边缘的距离呈指数衰减。

![图：1T'-WSe₂ 中的边缘态 LDOS mapping](../../raw/figures/pedramraziManipulatingTopologicalDomain2019/fig_3_RZS9DWGU.png)
*   **看图要点**：图中 (b-e) 显示了在不同能量下，电子态密度 (LDOS) 集中在 1T'-WSe₂ 与 1H 相或真空的交界处。
*   **来源**：[[../papers/pedramraziManipulatingTopologicalDomain2019]] -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]

## 🧩 分类与特征

*   **螺旋边缘态 (Helical Edge States)**：见于量子自旋霍尔绝缘体，相反自旋的电子向相反方向运动，受时间反演对称性保护。
*   **手性边缘态 (Chiral Edge States)**：见于量子反常霍尔绝缘体，电子只能单向运动（类似高速公路），受空间反演破缺或磁性保护。
*   **平庸边缘态 (Trivial Edge States)**：由表面势场或缺陷产生，不具有拓扑保护性，容易受散射影响。

## 📚 相关论文 (Related Papers)

- [[../papers/pedramraziManipulatingTopologicalDomain2019]]：通过 STM/STS 区分了拓扑保护的边缘态与平庸的畴界态。
- [[../papers/hanPolarTopologicalMaterials2025]]：讨论了边缘态在拓扑器件中的应用。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/surface-state|表面态]]（三维材料的对应物）
- [[../concepts/bulk-boundary-correspondence|体-边界对应关系]]（产生原理）
- [[../concepts/quantum-spin-hall-effect|量子自旋霍尔效应]]（典型表现）
- [[../entities/WSe2|WSe₂]]（其 1T' 相具有显著的螺旋边缘态）
- [[../entities/MoS2|MoS₂]]（可在其边缘产生平庸或拓扑态）
