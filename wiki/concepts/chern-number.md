---
tags: [concept, topological-physics, mathematics]
title: 陈数 / Chern Number
type: concept
status: developing
domain: [condensed-matter-physics, topological-physics]
mechanism: 贝里曲率在整个二维布里渊区上的积分，量化能带的全局拓扑属性
related_concepts: [berry-curvature, topological-charge, bulk-boundary-correspondence, anomalous-hall-effect, quantum-anomalous-hall-effect]
papers: [hanPolarTopologicalMaterials2025, wangTunableD0Topological2025b, sharmaRoomtemperatureFerroelectricSemimetal2019]
updated: 2026-08
---

# 陈数 / Chern Number

陈数 (Chern Number, 通常记作 $C$) 是描述二维能带结构全局拓扑性质的整数不变量。在物理上，它等于贝里曲率在整个第一布里渊区内的总通量。陈数的非零取值是量子化反常霍尔效应的根源，标志着体系处于拓扑非平庸态。

## 👵 太奶导读

好孩子，这“陈数”是用咱们中国大数学家陈省身先生的名字命名的，它是用来数“能带里的旋儿”的。
想象一下，材料里的电子云像是一块布。如果这块布是平平整整缝在球上的，它的陈数就是 $0$。但如果这块布被拧了一下，缝成了一个像甜甜圈（托鲁斯）那样的形状，那它就带了一个“旋儿”，陈数就是 $1$。
这个数必须是整数（$1, 2, 3...$），不能有半个旋儿。只要这个数不是 $0$，这个材料就是“拓扑非平庸”的。在外面看来，这就意味着材料的边缘一定会有那种永远停不下来的电流，而且电流的大小跟这个陈数是严格对应的。

## 🏗️ 结构概览

陈数的计算涉及对动量空间贝里曲率的闭合积分。

![图：贝里曲率流场示意图](../../raw/figures/sharmaRoomtemperatureFerroelectricSemimetal2019/fig_4_F86EWZ63.png)
*   **看图要点**：展示了能带交叉点作为贝里曲率的单极子，其强度的总和与陈数相关。
*   **来源**：[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]

## 🧩 数学定义与物理表现

*   **定义**：对于第 $n$ 条能带，陈数定义为：
    $$C_n = \frac{1}{2\pi} \int_{BZ} \Omega_n(k) d^2k$$
*   **量子化霍尔电导**：在量子反常霍尔绝缘体中，霍尔电导率被量子化为：
    $$\sigma_{xy} = C \cdot \frac{e^2}{h}$$
    其中 $C$ 为所有占据带的陈数之和。
*   **稳健性**：只要不关闭并重新打开能隙（即不发生拓扑相变），陈数的大小就不会改变。

## 📚 相关论文 (Related Papers)

- [[../papers/hanPolarTopologicalMaterials2025]]：极性材料中的拓扑分类与陈数概念。
- [[../papers/wangTunableD0Topological2025b]]：计算二维磁性材料的拓扑性质。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：通过贝里相位方法（陈数的物理表现）计算电极化。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/berry-curvature|贝里曲率]]（被积分函数）
- [[../concepts/topological-insulator|拓扑绝缘体]]（由 $Z_2$ 或陈数描述）
- [[../concepts/quantum-anomalous-hall-effect|量子反常霍尔效应]]（陈数的直接表现）
- [[../concepts/bulk-boundary-correspondence|体-边界对应关系]]（陈数决定边缘态数量）
