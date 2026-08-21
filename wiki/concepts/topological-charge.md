---
tags: [concept, topological-physics, mathematics]
title: 拓扑荷 / Topological Charge
type: concept
status: mature
year: 2025
domain: [condensed-matter-physics, topological-physics, spintronics]
mechanism: 实空间极化/自旋织构或动量空间能带流形中拓扑映射的卷绕数，被量子化为整数或半整数
related_concepts: [berry-curvature, skyrmion, polar-vortex, bulk-boundary-correspondence, chern-number, polar-skyrmion, weyl-semimetal, topological-defects, flux-closure-domain, meron, electric-dmi, multiferroicity, polarization-switching, anomalous-hall-effect, domain-wall]
papers: [hanPolarTopologicalMaterials2025, wangTunableD0Topological2025b, gomez-ortizKittelLawDomain2023, gongAbsenceCriticalThickness2023, zhangNonvolatileControlTopological2025, Jia2023polymerization]
updated: 2026-08-19
---

# 拓扑荷 / Topological Charge

拓扑荷 (Topological Charge, 通常用 $Q$ 或 $N$ 表示) 是量化特定场结构（如实空间的自旋织构、极化织构，或者动量空间的能带结构）拓扑不平庸程度的整数或半整数。它是描述拓扑性质的核心不变量，保证了拓扑结构在微扰下的稳定性。

## 👵 太奶导读

好孩子，这"拓扑荷"就像是一个绳结的"缠绕圈数"。
你想，你拿一根绳子打个死结，不论你怎么拉扯、揉捏这根绳子（只要你不拿剪刀剪断），这个结（拓扑荷）都会一直在那儿。
在极性材料（如铁电体、磁铁）中，原子的极化方向或者磁铁的自旋方向如果手拉手排成一个圈（涡旋），这个圈转了多少度、怎么转的，就被量化成了拓扑荷。比如，头尾相接转满一圈可能对应电荷 $0.5$ 或 $1$。只要你不用极端的手段（比如电极化彻底反转或者加热到极高温度），这个圈数就不会凭空消失。所以它是极其稳定且安全的，特别适合用来给未来的电脑存数据。

## 🏗️ 结构概览

在铁电纳米岛中，通过极化矢量的旋转可以定义拓扑荷。

![图：不同极性拓扑结构及其对应的拓扑荷](../../raw/figures/hanPolarTopologicalMaterials2025/fig_2_LS5XEME2.png)
*   **看图要点**：展示了畴壁（$Q=0$）、通量闭合（$Q=0$）、涡旋/反涡旋（$Q=\pm0.5$）、斯格明子（$Q=\pm1$）的拓扑电荷分类。
*   **来源**：[[../papers/hanPolarTopologicalMaterials2025]]

## 🧩 核心机制：卷绕数如何从场构型中读出

### 1. 实空间拓扑自旋/极化织构

对于二维极化或自旋矢量场 $\hat{P}(x, y)$，拓扑荷量化公式为：
$$Q = \frac{1}{4\pi} \iint \hat{P} \cdot \left( \frac{\partial \hat{P}}{\partial x} \times \frac{\partial \hat{P}}{\partial y} \right) dx dy$$

- **斯格明子 (Skyrmion)**：$Q = \pm 1$，极化从边缘（向上）平滑过渡到核心（向下）。
- **涡旋 (Vortex)** / **半子 (Meron)**：$Q = \pm 0.5$。
- **通量闭合 (Flux Closure) / 畴壁**：$Q = 0$，虽看似弯曲但整体卷绕数为零。

### 2. 动量空间拓扑荷

在自旋半金属（如外尔半金属）中，外尔点是贝里曲率的单极子：
$$C = \frac{1}{2\pi} \oint_{S} \Omega \cdot d\vec{S} = \pm 1$$

代表外尔点的手性，也是其作为贝里曲率"源/汇"的拓扑荷。整个布里渊区贝里曲率的积分即陈数（Chern Number），决定量子化霍尔电导。

## 📋 典型结构参数表

| 拓扑结构 | 拓扑荷 $Q$ | 典型材料/体系 | 稳定机制 |
|---|---|---|---|
| 斯格明子 | $\pm 1$ | 铁磁薄膜、极性纳米岛 | DMI / 梯度能对抗退极化场 |
| 涡旋/反涡旋 | $\pm 0.5$ | PbTiO₃ 超晶格纳米岛 | 退极化场 + 弹性边界 |
| 半子 (Meron) | $\pm 0.5$ | 铁电/磁性异质结 | 部分穿透的涡旋 |
| 通量闭合/畴壁 | $0$ | 常规铁电畴 | 退极化能最小化 |
| 外尔点 | $\pm 1$（手性） | WTe₂、TaAs 族 | 能带线性交叉 + 对称性破缺 |

## 🔀 近邻概念辨析

- **拓扑荷 vs 陈数**：拓扑荷是广义的卷绕数（可表征实空间织构或动量空间能带），陈数是动量空间带结构上的特定拓扑荷（整数量子化的霍尔电导标尺）。
- **拓扑荷 vs 贝里曲率**：贝里曲率是局域的几何场（"力"），拓扑荷是其全局积分（"圈数"）；曲率在布里渊区的积分给出陈数型拓扑荷。

## 📚 相关论文 (Related Papers)

- [[../papers/hanPolarTopologicalMaterials2025]]：综述极性拓扑结构的能量竞争设计原理与拓扑荷分类。
- [[../papers/wangTunableD0Topological2025b]]：d0 磁性单层 In₂NO₂ 中拓扑磁态的电场调控。
- [[../papers/gomez-ortizKittelLawDomain2023]]：Kittel 定律与畴结构的能量标度关系。
- [[../papers/gongAbsenceCriticalThickness2023]]：极性斯格明子打破 Kittel 定律的临界厚度研究。
- [[../papers/zhangNonvolatileControlTopological2025]]：铁电极化对磁性拓扑结构与 DMI 的非易失调控。

## 🔗 关联概念与实体 (Related)

- [[../concepts/berry-curvature|berry-curvature]]
- [[../concepts/chern-number|chern-number]]
- [[../concepts/skyrmion|skyrmion]]
- [[../concepts/polar-skyrmion|polar-skyrmion]]
- [[../concepts/polar-vortex|polar-vortex]]
- [[../concepts/meron|meron]]
- [[../concepts/topological-defects|topological-defects]]
- [[../concepts/weyl-semimetal|weyl-semimetal]]
- [[../concepts/bulk-boundary-correspondence|bulk-boundary-correspondence]]
- [[../concepts/multiferroicity|multiferroicity]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../entities/BiFeO3|BiFeO3]]
- [[../entities/PbTiO3|PbTiO3]]
