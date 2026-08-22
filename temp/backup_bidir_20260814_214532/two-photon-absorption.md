---
tags: [concept, photophysics, nonlinear-optics]
title: 双光子吸收 / Two-Photon Absorption (TPA)
type: concept
status: mature
domain: [nonlinear-optics, biophotonics, photophysics]
mechanism: 分子在极短时间内（~10^-15 s）同时吸收两个光子，从基态跃迁到高能激发态
related_concepts: [two-photon-absorption-cross-section, two-photon-fluorescence, second-harmonic-generation, nonlinear-optics]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence, Gittard2013polymerization, Khitrov2000holographic, Kumar2017microstructuring, Nakanishi2009full, Tobeiha2025optical, Unknown2014passive, WRZYSZCZYNSKI2010initiators, Zhang2008synthesis]
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
*   **分子设计**：具有 [[../concepts/donor-pi-acceptor|D-π-A]] 推拉电子结构的分子通常具有较大的 δ 值。在二苯乙烯骨架上引入强吸电子基团（如双氰基）能显著提升该数值。
*   **典型数值**：高性能探针 P1 在非极性溶剂中的峰值 δ 可高达 5560–6670 GM [[../papers/Huang2019solvatochromic]]。

## 🔬 应用场景

*   **双光子显微镜 (TPM)**：生物组织内部的高分辨率三维成像。
*   **双光子光聚合物 (2PP)**：超精密 3D 打印技术。
*   **双光子治疗 (PDT)**：精确定位的肿瘤光动力治疗。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：研究了具有超大双光子吸收截面的二苯乙烯基探针。
- [[../papers/Huang2019solvatochromic]]：系统测量了不同环境下的双光子激发谱和截面。
- [[../papers/H2017fluorescence]]：阐述了双光子吸收在多功能传感中的应用。
- [[../papers/Gittard2013polymerization]]
- [[../papers/Khitrov2000holographic]]
- [[../papers/Kumar2017microstructuring]]
- [[../papers/Nakanishi2009full]]
- [[../papers/Tobeiha2025optical]]
- [[../papers/Unknown2014passive]]
- [[../papers/WRZYSZCZYNSKI2010initiators]]
- [[../papers/Zhang2008synthesis]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/two-photon-absorption-cross-section|双光子吸收截面]]
- [[../concepts/two-photon-fluorescence|双光子荧光]]
- [[../concepts/nonlinear-optics|非线性光学]]
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]
- [[../entities/fluorescein|荧光素 (参比物)]]
