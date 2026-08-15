---
tags: [concept, topological-physics]
title: 四极矩绝缘体 / Quadrupole Insulator
type: concept
status: developing
domain: [condensed-matter-physics, topological-physics]
mechanism: 具有非零拓扑四极矩的二阶拓扑绝缘体，特征为角点处的局域电荷
related_concepts: [high-order-topology, bulk-boundary-correspondence, berry-phase, topological-charge, corner-state]
papers: [hanPolarTopologicalMaterials2025, pedramraziManipulatingTopologicalDomain2019]
updated: 2026-08
---

# 四极矩绝缘体 / Quadrupole Insulator

四极矩绝缘体 (Quadrupole Insulator) 是一种典型的二阶拓扑绝缘体。在一个常规的一阶拓扑绝缘体中，材料内部表现出非零的偶极矩（Dipole Moment），从而在边缘导致受保护的态。而在四极矩绝缘体中，材料内部的偶极矩为零，但具有受拓扑保护的非零四极矩（Quadrupole Moment $q_{xy}$）。这种拓扑性质导致其一维边缘仍然是绝缘的，但在其二维材料的四个角点上会出现受保护的零维角态（Corner States），每个角点承载 $\pm e/2$ 的电荷。

## 👵 太奶导读

好孩子，这“四极矩绝缘体”就像是一个“守口如瓶的盒子，只有四个角漏风”。
一般的拓扑绝缘体，它的整个边框（边缘）都是导电的。但这个四极矩绝缘体特别奇怪，它的内部是死的（绝缘），它的四条边也都是死的（绝缘），可是那四个角上却像是开了天眼一样，能冒出电荷来，而且这电荷还是半个半个的（分数电荷）。
这就好比你搬一个大柜子，柜面和柜边都打不开，只有那四个拐角处能塞进东西去。这种材料能把能量极度精准地锁在四个针尖大的地方，非常适合做那种精细到极点的量子开关。

## 🏗️ 结构概览

四极矩绝缘体通常在具有交叉耦合磁通量的方晶格模型（Benalcazar-Bernevig-Hughes 模型）中实现。

![图：四极矩绝缘体及其对应的零维角态示意](../../raw/figures/pedramraziManipulatingTopologicalDomain2019/fig_3_RZS9DWGU.png)
*   **看图要点**：图中虽然不是直接的四极矩模型，但展示了电荷在特定拓扑点上的局域化现象。
*   **来源**：[[../papers/pedramraziManipulatingTopologicalDomain2019]] -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]

## 🧩 物理特性

*   **分数电荷**：每个角点承载 $1/2$ 或 $1/4$ 个基元电荷。
*   **对称性要求**：通常需要特定的晶格镜像对称性或反转对称性来稳定拓扑四极矩。
*   **实验实现**：目前已在声子晶体、电路模拟系统以及部分二维材料异质结中被观测到。

## 📚 相关论文 (Related Papers)

- [[../papers/hanPolarTopologicalMaterials2025]]：极性材料中的高阶拓扑缺陷与多极矩物理。
- [[../papers/pedramraziManipulatingTopologicalDomain2019]]：一维畴界作为局域态载体的物理研究。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/high-order-topology|高阶拓扑]]（四极矩绝缘体所属的大类）
- [[../concepts/berry-phase|贝里相位]]（计算四极矩的数学基础）
- [[../concepts/topological-charge|拓扑荷]]（角态电荷的一种形式）
- [[../entities/SnTe|SnTe]]（被预测可实现高阶拓扑态的材料之一）
