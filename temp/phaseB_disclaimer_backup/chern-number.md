---
tags: [concept, topological-physics, mathematics]
title: 陈数 / Chern Number
type: concept
status: mature
domain: [condensed-matter-physics, topological-physics]
mechanism: 贝里曲率在整个二维布里渊区上的积分，量化能带的全局拓扑属性
related_concepts: [berry-curvature, topological-charge, bulk-boundary-correspondence, anomalous-hall-effect, quantum-anomalous-hall-effect, berry-phase]
papers: [hanPolarTopologicalMaterials2025, wangTunableD0Topological2025b, sharmaRoomtemperatureFerroelectricSemimetal2019]
updated: 2026-08
---

# 陈数 / Chern Number

陈数 (Chern Number, 通常记作 $C$) 是描述二维能带结构全局拓扑性质的整数不变量。在物理上，它等于贝里曲率在整个第一布里渊区内的总通量。陈数的非零取值是量子化反常霍尔效应的根源，标志着体系处于拓扑非平庸态。

## 👵 太奶导读

好孩子，这"陈数"是用咱们中国大数学家陈省身先生的名字命名的，它是用来数"能带里的旋儿"的。
想象一下，材料里的电子云像是一块布。如果这块布是平平整整缝在球上的，它的陈数就是 $0$。但如果这块布被拧了一下，缝成了一个像甜甜圈（托鲁斯）那样的形状，那它就带了一个"旋儿"，陈数就是 $1$。
这个数必须是整数（$1, 2, 3...$），不能有半个旋儿。只要这个数不是 $0$，这个材料就是"拓扑非平庸"的。在外面看来，这就意味着材料的边缘一定会有那种永远停不下来的电流，而且电流的大小跟这个陈数是严格对应的。

## 🏗️ 结构概览

陈数把"能带带了多少个量子旋涡"变成一个整数。二维布里渊区是环面（torus），贝里曲率在其上的总通量必然是 $2\pi$ 的整数倍，这个整数就是陈数。它决定量子化霍尔电导 $\sigma_{xy} = C\cdot e^2/h$，并通过体-边界对应关系决定边缘态数目。陈数在连续形变（不关闭能隙）下不变，是能带拓扑分类的基本不变量。

![图：贝里曲率流场示意图](../../raw/figures/sharmaRoomtemperatureFerroelectricSemimetal2019/fig_4_F86EWZ63.png)
*   **看图要点**：展示了能带交叉点作为贝里曲率的单极子，其强度的总和与陈数相关。
*   **来源**：[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]

## 🧩 数学定义与物理表现

*   **定义**：对于第 $n$ 条能带，陈数定义为：
    $$C_n = \frac{1}{2\pi} \int_{BZ} \Omega_n(k) d^2k$$
    其中 $\Omega_n(k)$ 为第 $n$ 条带的贝里曲率。
*   **量子化霍尔电导**：在量子反常霍尔绝缘体中，霍尔电导率被量子化为：
    $$\sigma_{xy} = C \cdot \frac{e^2}{h}$$
    其中 $C$ 为所有占据带的陈数之和。
*   **稳健性**：只要不关闭并重新打开能隙（即不发生拓扑相变），陈数的大小就不会改变。
*   **体-边界对应**：非零陈数体系必然承载手性边缘态，边缘态数目等于陈数绝对值。

### 材料与调控视角

- **极性拓扑材料**：极性材料中拓扑分类与陈数概念结合，扩展了能带拓扑的材料库（[[../papers/hanPolarTopologicalMaterials2025|Han 2025]]）。
- **二维磁性体系**：应变/铁电调控二维磁性材料的能带，可设计具有不同陈数的拓扑相（[[../papers/wangTunableD0Topological2025b|Wang 2025]]）。
- **贝里相位计算**：陈数（贝里曲率积分）的物理表现亦见于电极化与极性输运的贝里相位计算（[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019|Sharma 2019]]）。

## 📋 关键参数表

| 参数 | 含义 | 特征 |
|---|---|---|
| 陈数 $C$ | 贝里曲率总通量/2π | 整数，拓扑不变量 |
| 霍尔电导 σxy | 量子化电导 | $C\cdot e^2/h$ |
| 边缘态数目 | 体-边界对应 | = \|C\| |
| 拓扑相变 | 能隙关闭/重开 | 陈数改变 |

## 🔀 近邻概念辨析

- **陈数 vs Z₂ 不变量**：陈数描述破坏时间反演的体系（如量子反常霍尔、量子霍尔）；Z₂ 描述保时间反演的拓扑绝缘体。
- **陈数 vs 贝里曲率**：曲率是局域（k 点）几何量，陈数是其全局积分——曲率是"密度"，陈数是"总数"。
- **陈数 vs 拓扑荷**：陈数即能带拓扑荷的特例（$C$ 为整数）；外尔点等奇点携带半整数或整数拓扑荷，与陈数来源一致（贝里曲率单极子）。

## 📚 相关论文 (Related Papers)

- [[../papers/hanPolarTopologicalMaterials2025]]：极性材料中的拓扑分类与陈数概念。
- [[../papers/wangTunableD0Topological2025b]]：计算二维磁性材料的拓扑性质。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：通过贝里相位方法（陈数的物理表现）计算电极化。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/berry-curvature|贝里曲率]]（被积分函数）
- [[../concepts/topological-insulator|拓扑绝缘体]]（由 Z₂ 或陈数描述）
- [[../concepts/quantum-anomalous-hall-effect|量子反常霍尔效应]]（陈数的直接表现）
- [[../concepts/bulk-boundary-correspondence|体-边界对应关系]]（陈数决定边缘态数量）
- [[../concepts/anomalous-hall-effect|反常霍尔效应]]（陈数量子化的经典极限）
- [[../concepts/berry-phase|贝里相位]]（陈数的相位学根源）
*（内容由AI生成，仅供参考）*