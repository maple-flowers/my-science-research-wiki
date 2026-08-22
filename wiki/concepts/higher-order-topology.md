---
tags: [concept, topology, band-topology]
title: '高阶拓扑 / Higher-Order Topology'
type: concept
status: stub
domain: [topological-matter, band-topology, 2d-materials]
mechanism: "d 维拓扑相的受保护边界态出现在余维数 ≥2 的边界上（棱/铰链、角），而非常规拓扑绝缘体的 (d−1) 维表面"
related_concepts: [topological-insulator, hinge-state, weyl-semimetal, domain-wall, topological-defects, berry-phase]
related_entities: [MoTe2]
papers: [huangPolarPhaseDomain2019]
updated: 2026-08
---

# 高阶拓扑 / Higher-Order Topology

高阶拓扑（higher-order topology）指这样一类拓扑相：**受拓扑保护的导电边界态不出现在 $(d-1)$ 维的表面上，而出现在余维数 $\geq 2$ 的更低维边界上**——三维体系中是**铰链态**（hinge state，沿棱的一维导电通道），二维体系中是**角态**（corner state，零维）。常规拓扑绝缘体（[[../concepts/topological-insulator|拓扑绝缘体]]）是"一阶"的：三维体绝缘、二维表面导电；二阶拓扑绝缘体则是体与表面都绝缘、只有棱导电。

## 👵 太奶导读

太奶，您想象一块方糖。普通的"拓扑绝缘体"就像这块糖：里头是干的，只有**六个面**是湿的、能导电。高阶拓扑更奇怪：里头干、六个面也干，**只有十二条棱是湿的**——导电只发生在棱上；再高一阶，就只剩八个角。为什么科学家在意这个？因为这些棱和角上的导电通道是被材料内部的"对称性"锁住的，不容易被划伤、杂质破坏，所以有可能拿来做很稳的导线或器件。

## 🧩 阶数与边界维度

| 阶数 | 体（$d$ 维） | 受保护边界 | 三维实例中的表现 |
| :--- | :--- | :--- | :--- |
| 一阶（常规） | 绝缘 | $(d-1)$ 维表面 | 表面狄拉克锥 |
| 二阶 | 绝缘 | $(d-2)$ 维棱/铰链 | [[../concepts/hinge-state\|铰链态]] |
| 三阶 | 绝缘 | $(d-3)$ 维角 | 角态 |

## 🔬 本库中的实验线索：MoTe₂

本库目前唯一涉及高阶拓扑的实验工作是 MoTe₂ 的畴壁研究（[[../papers/huangPolarPhaseDomain2019|Huang 2019]]）：

- MoTe₂ 低温为极性 T_d 相（[[../concepts/weyl-semimetal|Weyl 半金属]]），高温为非极性 1T′ 相，**1T′ 相被认为是高阶拓扑绝缘体**；
- 相变过程中 T_d/1T′ 相畴壁沿 c 轴自组装成类超晶格结构；
- 扫描隧道谱学在 T_d/1T′ **相畴壁处测到增强的导电态**，作者认为它**可能对应**高阶拓扑相预言的铰链态。

> ⚠️ 证据边界与限定语：上述铰链态归属是作者基于谱学特征提出的**可能性判断**，不是已被确证的结论；原文亦未给出体/表面/棱三者能隙的完整分层证据。本页据此保持 `status: stub`——库中尚无以高阶拓扑为**主要研究对象**的论文（无拓扑不变量计算、无对称性指标分析、无角态观测），因此本页只界定概念与已有线索，不展开理论细节。

## 🧭 近邻概念辨析

| 对比对象 | 关键区别 |
| :--- | :--- |
| [[../concepts/topological-insulator\|拓扑绝缘体]]（一阶） | 导电态在 $(d-1)$ 维表面；高阶拓扑的表面同样绝缘，导电只在棱或角 |
| [[../concepts/weyl-semimetal\|Weyl 半金属]] | 体态本身在离散 Weyl 点处闭合、有费米弧表面态；高阶拓扑相的体是**有能隙**的。二者可在同一材料的不同相中出现（MoTe₂ 的 T_d vs 1T′） |
| [[../concepts/domain-wall\|畴壁]]导电性 | 畴壁导电可以来自极化不连续、缺陷或载流子聚集等常规机制；只有当导电通道由体拓扑不变量强制要求时，才属高阶拓扑铰链态——两者在实验上需要额外判据区分，这正是 MoTe₂ 案例中"可能"一词的由来 |

## 📚 相关论文 (Related Papers)

- [[../papers/huangPolarPhaseDomain2019]]：本库唯一提供高阶拓扑实验线索的工作。用原位低温 TEM/STEM 与 STM 结合第一性原理，在极性 Weyl 半金属 MoTe₂ 中揭示 T_d↑/T_d↓ 极性畴壁与 T_d/1T′ 相畴壁（后者自组装为沿 c 轴类超晶格），演示电子束可逆操控极性畴壁，并在相畴壁处探测到**可能对应高阶拓扑铰链态**的增强电导；其中 1T′ 相被指认为高阶拓扑绝缘体。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/topological-insulator|拓扑绝缘体]]：高阶拓扑的一阶对照，区别见辨析表。
- [[../concepts/hinge-state|铰链态]]：二阶拓扑相在三维体系中的受保护边界态，本页的核心观测对象。
- [[../concepts/weyl-semimetal|Weyl 半金属]]：MoTe₂ 极性 T_d 相所属的拓扑相，与高阶拓扑的 1T′ 相在同一材料中共存。
- [[../concepts/domain-wall|畴壁]]：本库线索出现的场所——相畴壁而非样品外表面。
- [[../concepts/topological-defects|拓扑缺陷]]：更广的拓扑保护结构类别。
- [[../concepts/berry-phase|Berry 相]]：计算拓扑不变量与边界极化的基础工具。
- [[../entities/MoTe2|MoTe₂]]：本页唯一的实验体系。
