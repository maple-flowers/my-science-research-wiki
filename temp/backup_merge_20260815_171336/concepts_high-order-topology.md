---
tags: [concept, topological-physics]
title: 高阶拓扑 / Higher-order Topology
type: concept
status: developing
domain: [condensed-matter-physics, topological-physics]
mechanism: 体-边界对应关系的推广，d 维拓扑非平庸体在 d-2 维或更低维边界上表现出受保护的零维/一维边界态
related_concepts: [topological-insulator, bulk-boundary-correspondence, quadrupole-insulator, hinge-state, edge-state]
papers: [hanPolarTopologicalMaterials2025, pedramraziManipulatingTopologicalDomain2019]
updated: 2026-08
---

# 高阶拓扑 / Higher-order Topology

高阶拓扑 (Higher-order Topology) 是经典拓扑绝缘体和体-边界对应关系 (Bulk-Boundary Correspondence) 的重大推广。对于一个常规的 $d$ 维拓扑绝缘体（一阶），其物理边界上会出现 $d-1$ 维的受保护无能隙态。而一个 $d$ 维的 $n$ 阶拓扑绝缘体，其 $d-1, d-2, \dots, d-n+1$ 维边界都是绝缘的，只有在更低维的 $d-n$ 维边界上才会出现受保护的无能隙态。例如，一个二维的二阶拓扑绝缘体会具有绝缘的边缘，但其角点上会出现零维的受保护角态。

## 👵 太奶导读

好孩子，这“高阶拓扑”就像是“剥洋葱，剥到最后才漏出那点儿核心”。
一阶拓扑材料（普通拓扑绝缘体）像是个电容，整个表面都能跑电。但高阶拓扑材料就不一样了。
如果是二阶的二维材料，它的“身子”（体相）和“边儿”（边缘）都是绝缘的、死气沉沉的，但它那几个“尖角”（角点）上却能导电，会长出亮晶晶的零维角态。
如果是三阶的三维材料，那它不仅身子和面子是绝缘的，甚至棱上都是绝缘的，只有那几个尖锐的“顶角”才能通电。这种材料能把电荷极度精准地局域在特定的角落里，将来可以用来做精度极高的电子开关，或者是制造非常稳定的量子芯片。

## 🏗️ 结构概览

高阶拓扑的一个经典预言是三维高阶拓扑绝缘体中的一维铰链态 (Hinge States)。

![图：二阶拓扑绝缘体中的角态与铰链态示意](../../raw/figures/pedramraziManipulatingTopologicalDomain2019/fig_3_RZS9DWGU.png)
*   **看图要点**：在普通界面上是绝缘的，而在特定畴壁相交的点或棱角（铰链）处出现了一维导电通道。
*   **来源**：[[../papers/pedramraziManipulatingTopologicalDomain2019]] -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]

## 🧩 物理分类与特征

*   **二阶二维拓扑绝缘体**：具有绝缘的体能带和一维边缘态，但在物理角点上存在受保护的零维角态（Corner States）。
*   **二阶三维拓扑绝缘体**：具有绝缘的体能带和表面态，但在物理铰链（Hinges，即两个面交界处）上存在受保护的一维铰链态（Hinge States）。
*   **多极矩不变量**：高阶拓扑的物理机制通常可以用动量空间的四极矩 (Quadrupole) 或八极矩 (Octupole) 不变量来描述。

## 📚 相关论文 (Related Papers)

- [[../papers/hanPolarTopologicalMaterials2025]]：极性材料中的复杂拓扑相和多极矩物理。
- [[../papers/pedramraziManipulatingTopologicalDomain2019]]：一维畴界处的局域化性质提供了类似高阶拓扑的局部边界态物理。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/quadrupole-insulator|四极矩绝缘体]]（典型的二阶拓扑绝缘体模型）
- [[../concepts/hinge-state|铰链态]]（三维二阶 TI 的边界特征）
- [[../concepts/bulk-boundary-correspondence|体-边界对应关系]]（高阶拓扑将其进行了推广）
- [[../entities/Bi4Br4|Bi₄Br₄]]（被预言和实验验证的高阶拓扑绝缘体材料）
