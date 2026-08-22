---
tags: [concept, photophysics, nonlinear-optics]
title: 双光子吸收 / Two-Photon Absorption (TPA)
type: concept
status: mature
domain: [nonlinear-optics, biophotonics, photophysics]
mechanism: 分子在极短时间内（~10^-15 s）同时吸收两个光子，从基态跃迁到高能激发态
related_concepts: [two-photon-absorption-cross-section, two-photon-fluorescence, second-harmonic-generation, nonlinear-optics]
papers: [Nakanishi2009full, H2017fluorescence, Huang2019solvatochromic, Huang2023two, WRZYSZCZYNSKI2010initiators, Gittard2013polymerization, Kumar2017microstructuring, Unknown2014passive, Unknown2022polymerization, Khitrov2000holographic, Khitrov2002internal, Zhang2008synthesis]
updated: 2026-08
---

# 双光子吸收 / Two-Photon Absorption (TPA)

双光子吸收（Two-Photon Absorption, TPA）是一种非线性光学现象。在极高功率的光场（如飞秒激光脉冲）作用下，分子可以在一个近乎瞬时的过程（约 $10^{-15}$ 秒）内同时吸收两个光子，并跃迁到一个能量等于这两个光子能量总和的激发态。

## 👵 太奶导读

太奶啊，这就好比您要上一堵很高很高的墙（高能级态），但这堵墙太高了，您一步（一个光子）跨不上去。在咱们平时（单光子吸收），如果跨不上去您就只能待在原地。但在“双光子”这种特殊情况下，就好像是突然来了两个力气很大的人，**同时**各推了您一把，让您这两股劲儿合在一块儿，“噌”地一下就跳上去了。这两股劲儿加起来，正好抵得上一步跨上去所需的力气。这种招数得在人特别多、力气特别大的地方（强激光）才能玩得转。

## 🏗️ 物理特征与优势

TPA 最显著的物理特征是其**概率与入射光强度的平方成正比**（$I^2$ 依赖性）。这意味着只有在激光焦点处（光强最高点）才会发生有效的吸收。

*   **深层穿透**：TPA 通常使用近红外光（700–1000 nm）作为激发源，这属于“生物光学窗口”，光子在组织中的散射和自发吸收极小，能够深入生物组织。
*   **高空间分辨率**：由于吸收仅发生在这个极其微小的焦点区域，TPA 具有天然的光学切片能力，无需物理光阑即可实现高分辨率的三维成像。
*   **低光损伤**：焦点外的组织几乎不吸收能量，极大地降低了光漂白和光毒性。

## 🧩 双光子吸收截面 (δ)

双光子吸收截面（Two-Photon Absorption Cross Section）是衡量分子吸收两个光子能力大小的物理量，单位为 **GM** ($1 \text{ GM} = 10^{-50} \text{ cm}^4 \cdot \text{s} \cdot \text{photon}^{-1}$)。
*   **分子设计**：具有 [[../concepts/d-pi-a-architecture]] 推拉电子结构的分子通常具有较大的 δ 值。在二苯乙烯骨架上引入强吸电子基团（如双氰基）能显著提升该数值。
*   **典型数值**：高性能探针 P1 在非极性溶剂中的峰值 δ 可高达 5560–6670 GM [[../papers/Huang2019solvatochromic]]。

## 🔬 应用场景

*   **双光子显微镜 (TPM)**：生物组织内部的高分辨率三维成像。
*   **双光子光聚合物 (2PP)**：超精密 3D 打印技术。
*   **双光子治疗 (PDT)**：精确定位的肿瘤光动力治疗。

## 📚 相关论文 (Related Papers)

### 机制与截面（TPA 本体）

- [[../papers/Nakanishi2009full]]：本页唯一的量子光学层面处理——用双光子波函数给出 P₂ 与光子对 T/τ 比值成正比，增强时间关联可大幅提升 P₂；并指出矩形波函数存在「魔法」条件（Δ·τ = π(2n+1)）使单光子吸收概率 P₁ 严格为零而 P₂ 非零，是「TPA 可与单光子过程解耦」的理论依据。
- [[../papers/H2017fluorescence]]：给出本页 δ 的最高实测值——探针 P1 在非极性溶剂中峰值 δ 达 5560 GM，并给出其发射峰 445→641 nm 的极宽溶剂化变色区间与 E_T(30) 线性关系。
- [[../papers/Huang2019solvatochromic]]：在二苯乙烯骨架上引入双氰基与二甲氨基构建 P1，系统测量溶剂极性/黏度/温度依赖的双光子激发谱与截面，并首次在黏度实验中观察到 LE / TICT / 激基复合物三重荧光。
- [[../papers/Huang2023two]]：证明**双氰基对激发态电荷分离的稳定作用**是大 δ 的分子设计来源，1a/1b 表现出极性依赖的大 δ 与双光子激发下的三重荧光。
- [[../papers/WRZYSZCZYNSKI2010initiators]]：给出 δ 增强的普适分子设计判据——D-π-D、D-π-A 等推拉结构可极大增强 δ，并说明大 δ 引发剂配合飞秒激光即可实现真正的三维「体」加工、抑制氧阻聚。

### 以 TPA 为基础的应用（非 TPA 本体证据）

- [[../papers/Gittard2013polymerization]]：说明 TPA 的**阈值特性**如何转化为加工能力——2PP 借此获得微纳尺度精确几何控制，用于再生医学支架与假体制造。
- [[../papers/Kumar2017microstructuring]]：证明 TPA 的非线性阈值不依赖飞秒源——亚纳秒激光配合 SU-8/AR-N 4340 + 光引发剂即可达约 500 nm 线宽，并给出功率/写入速度对线宽的定量规律。
- [[../papers/Unknown2014passive]]：TPA 三维加工能力的应用实例——双光子聚合制成螺旋桨叶式微混合器，单级 12 μl/min 下混合效率 >80%。
- [[../papers/Unknown2022polymerization]]：TPA 加工用于传感器制造——在光纤尖端制出带可动镜面的 Fabry–Pérot 腔，对温度与折射率高灵敏。

### ⚠️ 证据存疑，暂不作为本页依据

- [[../papers/Khitrov2000holographic]]：标题为全息双光子聚合光栅（液晶畴 20–200 nm），但其 card「研究结论」记录的是**氢化金刚石表面导电性**，标题与结论明显错配，疑为 `raw/note` 侧 PDF 配错。
- [[../papers/Khitrov2002internal]]：标题为双光子诱导光致发光观测内部缺陷，card 结论却是 Si/SiGe 纳米线、碳纳米管杨氏模量、ZnSe 缺陷成像、GaN ELD 的会议论文集合辑，无法定位本页所需的具体证据。
- [[../papers/Zhang2008synthesis]]：三支化双光子发色团的合成与非线性光学性质，但 card 中已自注「笔记 AI 解读部分因 PDF 错配不可参考」，故 σ₂ 数值与聚合阈值均不引用。

> 上述三条属 `raw/note` 层的资料错配，按铁律**未改动 raw**，仅在此登记；修复后可回填为正式证据。
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/two-photon-absorption-cross-section|双光子吸收截面]]
- [[../concepts/two-photon-fluorescence|双光子荧光]]
- [[../concepts/nonlinear-optics|非线性光学]]
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]
- [[../entities/fluorescein|荧光素 (参比物)]]
