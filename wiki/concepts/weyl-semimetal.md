---
tags: [concept, topological-physics, semimetal]
title: 外尔半金属 / Weyl Semimetal (WSM)
type: concept
status: mature
year: 2019
domain: [condensed-matter-physics, topological-physics]
mechanism: 破缺空间反演对称或时间反演对称导致的能带线性交叉点（外尔点），为贝里曲率的拓扑荷源/汇
related_concepts: [berry-curvature, anomalous-hall-effect, topological-charge, fermi-arc, chern-number, dirac-semimetal, topological-insulator, ferroelectricity, polar-metal, sliding-ferroelectricity, quantum-spin-hall-effect, spin-orbit-coupling]
papers: [sharmaRoomtemperatureFerroelectricSemimetal2019, hanPolarTopologicalMaterials2025, wangTunableD0Topological2025b, feiFerroelectricSwitchingTwodimensional2018a, huangPolarPhaseDomain2019]
updated: 2026-08-19
---

# 外尔半金属 / Weyl Semimetal (WSM)

外尔半金属 (Weyl Semimetal, WSM) 是一种拓扑半金属，其能带结构在离散的点（外尔点）处发生线性交叉。这些外尔点表现为布里渊区中的拓扑荷（源/汇），并由贝里曲率 (Berry Curvature) 产生的磁单极子特性。为了形成外尔点，系统必须破缺空间反演对称性 (Inversion Symmetry) 或时间反演对称性 (Time-Reversal Symmetry)。

## 👵 太奶导读

好孩子，这"外尔半金属"就像是个电子版的"沙漏"。
平常的材料，导电能带和不导电能带之间通常有个大深沟（能隙）。但在外尔半金属里，这两个带子在几个特定的点上碰头了，长得就像咱们计时的沙漏一样。这些碰头的点就是"外尔点"。
外尔点特别神奇，它们像是有正负极的磁铁一样，一个是"出水口"，一个是"入水口"（拓扑荷）。电子经过这些点的时候，就像是光子一样，跑得飞快，还没有质量负担（零有效质量）。而且，这些材料表面还会形成一种像彩虹一样的弧形导电道（费米弧），这在普通材料里是绝对看不到的。

## 🏗️ 结构概览

WTe₂ 是典型的 II 型外尔半金属，其外尔点处的交叉是倾斜的。

![图：WTe₂ 的能带结构与外尔点示意](../../raw/figures/sharmaRoomtemperatureFerroelectricSemimetal2019/fig_4_F86EWZ63.png)
*   **看图要点**：图中展示了 Td-WTe₂ 的能带，导带和价带在费米面附近线性相交。
*   **来源**：[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]

## 🧩 核心机制：外尔点作为贝里曲率的源与汇

### 1. 线性交叉与外尔方程

外尔点是三维动量空间中导带与价带的线性接触点，低能激发由两分量外尔方程描述（零有效质量、固定手性）。外尔点必须成对出现（尼尔森定理），每个外尔点携带手性 $\chi = \pm 1$。

### 2. 拓扑荷与费米弧

- **手性 = 拓扑荷**：外尔点是贝里曲率的单极子，对包围它的闭合面做贝里曲率积分得 $C = \pm 1$，即外尔点的手性。
- **费米弧 (Fermi Arc)**：连接表面布里渊区内不同手性外尔点投影的开放表面态弧线，是外尔半金属的指纹特征。
- **手性反常 (Chiral Anomaly)**：平行电场与磁场下电子在不同手性外尔点间转移，导致负磁阻。

### 3. 铁电外尔半金属

WTe₂ 同时是铁电金属与 II 型外尔半金属：室温下其极性可被电场翻转，为"铁电 + 拓扑"耦合提供了天然平台，极化翻转可能调控外尔点位置与输运响应。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 外尔点手性 $\chi$ | 贝里曲率单极子荷 | $\pm 1$ |
| 外尔点配对 | 能带拓扑约束 | 偶数个、总手性为零 |
| 费米弧长度 | 表面态延伸 | 连接不同手性投影 |
| 交叉类型 | I/II 型 | 直立 vs 倾斜（WTe₂ 为 II 型） |
| 磁阻响应 | 手性反常标志 | 负磁阻（E ∥ B） |

## 🔀 近邻概念辨析

- **外尔半金属 vs 狄拉克半金属**：狄拉克点由两个手性相反的外尔点重合而成，通常需要额外对称性保护；外尔点本身不需要对称性保护，只要时间反演或空间反演之一破缺。
- **外尔半金属 vs 拓扑绝缘体**：拓扑绝缘体是体态绝缘、表面有狄拉克锥；外尔半金属是体态半金属（零能隙点），表面有费米弧。

## 📚 相关论文 (Related Papers)

- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：证实 WTe₂ 作为室温铁电外尔半金属，PFM 观测可翻转极化。
- [[../papers/hanPolarTopologicalMaterials2025]]：讨论外尔点作为极性拓扑研究的背景与器件前景。
- [[../papers/wangTunableD0Topological2025b]]：拓扑半金属态与多铁性的耦合调控。
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]：二维金属 WTe₂ 的铁电翻转实验。
- [[../papers/huangPolarPhaseDomain2019]]：极性相与拓扑相共存下的物理。

## 🔗 关联概念与实体 (Related)

- [[../concepts/berry-curvature|berry-curvature]]
- [[../concepts/topological-charge|topological-charge]]
- [[../concepts/anomalous-hall-effect|anomalous-hall-effect]]
- [[../concepts/fermi-arc|fermi-arc]]
- [[../concepts/chern-number|chern-number]]
- [[../concepts/dirac-semimetal|dirac-semimetal]]
- [[../concepts/topological-insulator|topological-insulator]]
- [[../concepts/ferroelectricity|ferroelectricity]]
- [[../concepts/polar-metal|polar-metal]]
- [[../concepts/sliding-ferroelectricity|sliding-ferroelectricity]]
- [[../entities/WTe2|WTe2]]
- [[../entities/MoTe2|MoTe2]]
