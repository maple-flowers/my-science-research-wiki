---
tags: [concept, topological-physics, mathematics]
title: 拓扑荷 / Topological Charge
type: concept
status: developing
domain: [condensed-matter-physics, topological-physics, spintronics]
mechanism: 实空间极化/自旋织构或动量空间能带流形中拓扑映射的卷绕数
related_concepts: [berry-curvature, skyrmion, polar-vortex, bulk-boundary-correspondence, chern-number]
papers: [hanPolarTopologicalMaterials2025, wangTunableD0Topological2025b, gomez-ortizKittelLawDomain2023, gongAbsenceCriticalThickness2023, zhangNonvolatileControlTopological2025, Jia2023polymerization]
updated: 2026-08
---

# 拓扑荷 / Topological Charge

拓扑荷 (Topological Charge, 通常用 $Q$ 或 $N$ 表示) 是量化特定场结构（如实空间的自旋织构、极化织构，或者动量空间的能带结构）拓扑不平庸程度的整数或半整数。它是描述拓扑性质的核心不变量，保证了拓扑结构在微扰下的稳定性。

## 👵 太奶导读

好孩子，这“拓扑荷”就像是一个绳结的“缠绕圈数”。
你想，你拿一根绳子打个死结，不论你怎么拉扯、揉捏这根绳子（只要你不拿剪刀剪断），这个结（拓扑荷）都会一直在那儿。
在极性材料（如铁电体、磁铁）中，原子的极化方向或者磁铁的自旋方向如果手拉手排成一个圈（涡旋），这个圈转了多少度、怎么转的，就被量化成了拓扑荷。比如，头尾相接转满一圈可能对应电荷 $0.5$ 或 $1$。只要你不用极端的手段（比如电极化彻底反转或者加热到极高温度），这个圈数就不会凭空消失。所以它是极其稳定且安全的，特别适合用来给未来的电脑存数据。

## 🏗️ 结构概览

在铁电纳米岛中，通过极化矢量的旋转可以定义拓扑荷。

![图：不同极性拓扑结构及其对应的拓扑荷](../../raw/figures/hanPolarTopologicalMaterials2025/fig_2_LS5XEME2.png)
*   **看图要点**：展示了畴壁（$Q=0$）、通量闭合（$Q=0$）、涡旋/反涡旋（$Q=\pm0.5$）、斯格明子（$Q=\pm1$）的拓扑电荷分类。
*   **来源**：[[../papers/hanPolarTopologicalMaterials2025]] -> [[../figures/domain-walls-structures|畴结构与畴壁]]

## 🧩 数学定义与物理意义

### 1. 实空间拓扑自旋/极化织构
对于二维极化或自旋矢量场 $\hat{P}(x, y)$，拓扑荷量化公式为：
$$Q = \frac{1}{4\pi} \iint \hat{P} \cdot \left( \frac{\partial \hat{P}}{\partial x} \times \frac{\partial \hat{P}}{\partial y} \right) dx dy$$
*   **斯格明子 (Skyrmion)**：$Q = \pm 1$，极化从边缘（向上）平滑过渡到核心（向下）。
*   **涡旋 (Vortex)** / **半子 (Meron)**：$Q = \pm 0.5$。

### 2. 动量空间拓扑荷
在自旋半金属（如外尔半金属）中，外尔点是贝里曲率的单极子：
$$C = \frac{1}{2\pi} \oint_{S} \Omega \cdot d\vec{S} = \pm 1$$
代表外尔点的手性。

## 📚 相关论文 (Related Papers)

- [[../papers/hanPolarTopologicalMaterials2025]]：给出了极性涡旋、斯格明子的统一拓扑荷分类。
- [[../papers/wangTunableD0Topological2025b]]：通过微磁学模拟计算了单层材料中斯格明子的拓扑不变量。
- [[../papers/gomez-ortizKittelLawDomain2023]]
- [[../papers/gongAbsenceCriticalThickness2023]]
- [[../papers/zhangNonvolatileControlTopological2025]]
- [[../papers/Jia2023polymerization]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/skyrmion|斯格明子]]（典型的 $Q=\pm1$ 织构）
- [[../concepts/polar-vortex|极性涡旋]]（典型的 $Q=\pm0.5$ 织构）
- [[../concepts/chern-number|陈数]]（全局积分对应的拓扑荷）
- [[../entities/BiFeO3|BiFeO₃]]（可承载多种极性拓扑荷的铁电氧化物）
