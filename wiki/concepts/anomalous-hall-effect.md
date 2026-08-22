---
tags: [concept, topological-physics, transport]
title: 反常霍尔效应 / Anomalous Hall Effect (AHE)
type: concept
status: mature
domain: [condensed-matter-physics, topological-physics]
mechanism: 磁性材料中贝里曲率或不均匀散射诱导的横向霍尔电压
related_concepts: [berry-curvature, spin-orbit-coupling, time-reversal-symmetry, weyl-semimetal, magnetic-anisotropy, chern-number]
papers: [wangTunableD0Topological2025b, sharmaRoomtemperatureFerroelectricSemimetal2019, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, zhaoOpticalFingerprintsTwodimensional2024]
updated: 2026-08
---

# 反常霍尔效应 / Anomalous Hall Effect (AHE)

反常霍尔效应 (Anomalous Hall Effect, AHE) 是指在磁性材料中，即使不施加外加磁场，仅依靠材料自身的自发磁化也能产生横向霍尔电压的现象。它主要由两种机制决定：本征机制（由动量空间中的贝里曲率决定）和外在机制（由杂质引起的侧跳 skew-scattering 和侧移 side-jump 决定）。

## 👵 太奶导读

好孩子，这"反常霍尔效应"就像是在没有风（外磁场）的时候，材料里的"帆船"自己就会打偏。
普通的霍尔效应需要你用一个特别强的磁铁从外面去照，电子才会往旁边拐。而这反常霍尔效应呢，材料自己就是个磁铁。因为材料里面有"贝里曲率"（也就是看不见的转弯力）和很强的自旋-轨道耦合（电子自己的自转和公转碰头了），所以你只要顺着材料通电，电子就会自发地往两边分，一边多一边少，产生了电压。
这就好比一个熟练的杂技演员，不用别人推，自己走两步就能借着惯性往旁边飘。

## 🏗️ 结构概览

反常霍尔效应的本征贡献来自于费米面附近贝里曲率的积分。当时间反演对称被磁序破缺、但体系仍保留晶体对称性时，占据态在动量空间呈现非零的贝里曲率分布，从而产生横向反常速度。AHE 是探测磁性材料电子结构、磁序与拓扑性质的核心输运手段，也是量子反常霍尔效应的经典极限。

![图：反常霍尔效应中电子发生偏转示意图](../../raw/figures/wangTunableD0Topological2025b/fig_3_UYVUXL8I.png)
*   **看图要点**：图中自旋偏转与系统的局域磁矩及贝里曲率密切相关。
*   **来源**：[[../papers/wangTunableD0Topological2025b]] -> [[../figures/electronic-bands-cdw-transport|CDW与输运性质]]

## 🧩 核心内容与机制

*   **本征机制 (Intrinsic)**：电子由于波函数的几何性质（由贝里曲率描述）在电场下获得一个反常速度。霍尔电导率正比于布里渊区内被占据态贝里曲率的总和：
    $$\sigma_{xy}^{int} = -\frac{e^2}{\hbar} \int_{BZ} \frac{d^3k}{(2\pi)^3} f(k) \Omega_z(k)$$
*   **斜散射 (Skew scattering)**：外在机制，电子在碰撞非磁性杂质时，由于自旋-轨道耦合导致向左和向右散射的不对称性。
*   **侧移 (Side jump)**：外在机制，电子在通过杂质势场时，波包发生横向的空间位移。

### 材料与调控视角

- **铁电极化/应变调控**：铁电极化驱动的磁电耦合可调控磁性材料的自旋织构与输运，为 AHE 提供电场调控通道（[[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025|Cai 2025]]）。
- **二维磁性体系**：应变可调谐二维磁性材料的能带与贝里曲率分布，进而调制反常输运（[[../papers/wangTunableD0Topological2025b|Wang 2025]]）。
- **光谱指纹**：光学响应可提供二维磁性体系中磁序与能带几何的指纹信息，与 AHE 输运互为印证（[[../papers/zhaoOpticalFingerprintsTwodimensional2024|Zhao 2024]]）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 霍尔电导率 σxy | 横向电导 | 本征项 ∝ 贝里曲率积分 |
| 贡献机制 | 本征/外在 | Berry 曲率 vs 杂质散射 |
| 自旋-轨道耦合 | 外在散射根源 | 重元素体系更强 |
| 磁化方向 | AHE 符号/大小 | 随磁矩翻转 |
| 体系要求 | 时间反演破缺 | 磁性有序 |

## 🔀 近邻概念辨析

- **AHE vs 普通霍尔效应**：普通霍尔效应依赖外磁场，AHE 依赖自发磁化/时间反演破缺。
- **AHE vs 量子反常霍尔效应 (QAHE)**：AHE 是耗散体相输运；QAHE 中霍尔电导精确量子化为 $C\cdot e^2/h$，边缘态无耗散。
- **AHE vs 自旋霍尔效应**：AHE 产生净电荷横向电压（磁序诱导）；自旋霍尔效应产生纯自旋流（无需磁性，靠自旋-轨道耦合）。

## 📚 相关论文 (Related Papers)

- [[../papers/wangTunableD0Topological2025b]]：通过应变和铁电极化调控自旋织构，进而有望调控 AHE 输运。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：讨论了极性外尔体系中的输运。
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：铁电极化驱动磁电耦合对磁性输运的调控。
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：二维磁性体系的光学指纹与输运关联。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/berry-curvature|贝里曲率]]（本征贡献来源）
- [[../concepts/spin-orbit-coupling|自旋-轨道耦合]]（外在散射的物理根源）
- [[../concepts/chern-number|陈数]]（QAHE 中量子化霍尔电导的来源）
- [[../concepts/quantum-anomalous-hall-effect|量子反常霍尔效应]]（AHE 的无耗散量子化版本）
- [[../concepts/weyl-semimetal|外尔半金属]]（动量空间贝里曲率单极子体系）
- [[../entities/Fe3GeTe2|Fe₃GeTe₂]]（展现强 AHE 的明星二维磁性材料）
