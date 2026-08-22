---
tags: [concept]
title: '穿透深度 / Penetration Depth'
type: concept
status: developing
papers: ['majumdarInterplayChargeDensity2020', '2019optical', 'Terasaki2011ultrasonic']
updated: 2026-08-18
---

# 穿透深度 / Penetration Depth

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


穿透深度（penetration depth, λ）指**外加场（电磁场、光、超声波）或量子序参量向材料内部衰减/延伸的特征长度**。在超导物理中特指伦敦穿透深度——磁场在超导体内部指数衰减的尺度，与超流密度、能隙结构直接相关；在光学与超声学中则指波在介质中的穿透距离，是传感与无损检测的关键参数。

## 👵 太奶导读

任何东西"探进"材料里都会慢慢变弱——光会衰减、磁场会被屏蔽、超声波会消耗。变弱到 1/e 那么深的距离就叫穿透深度。超导体里它有个特别含义：磁场几乎进不去，只在表面薄薄一层溜达，这一层的厚度就是伦敦穿透深度。量它就能反推超导有多"强壮"。

## 🧩 穿透深度与超导电性

- **CDW 与多带超导的竞争**：对高质量 2H-NbSe₂ 与 2H-NbS₂ 单晶的研究表明，CDW 与超导（SC）是竞争关系——压力可抑制 CDW 并显著增强 SC；两者均具有双 s 波超导能隙且大能隙呈强耦合特征，CDW 不影响该基本能隙结构；NbS₂ 的上临界场由泡利顺磁效应主导，而 NbSe₂ 表现出多带效应，两者均偏离 Uemura 关系（[[../papers/majumdarInterplayChargeDensity2020|Majumdar 2020]]）。穿透深度的温度依赖正是确定超流密度与能隙对称性的标准手段。

## 🧩 穿透深度与传感应用

- **光学穿透与湿度传感**：基于 TiO₂-SiO₂ 包层的聚合物光纤湿度传感器利用光纤中光场在包层/环境界面的穿透与倏逝波耦合，实现对湿度的实时测量，体现了光学穿透深度对介质环境（水分子吸附）的敏感性（[[../papers/2019optical|Optical Fiber Sensor 2019]]）。
- **超声穿透与机械发光**：超声波是有效的机械发光（ML）刺激源，其诱导的 ML 发光具有可重复性与快速响应性，发光强度与超声功率正相关；超声可穿透组织激发体内 ML 光源（如 Eu 掺杂 SrAl₂O₄），穿透能力是超声-ML 体内应用的关键前提（[[../papers/Terasaki2011ultrasonic|Terasaki 2011]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/2019optical]] — Optical Fiber Polymer Sensor System with TiO₂-SiO₂ Cladding for Measuring Humidity
- [[../papers/Terasaki2011ultrasonic]] — Ultrasonic Wave Induced Mechanoluminescence
- [[../papers/majumdarInterplayChargeDensity2020]] — Interplay of charge density wave and multiband superconductivity in layered quasi-two-dimensional materials

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]：伦敦穿透深度的母体序。
- [[../concepts/charge-density-wave|电荷密度波]]：与超导竞争的对手序。
- [[../concepts/mechanoluminescence|机械发光]]：超声穿透激发的发光现象。
- [[../entities/NbSe2|NbSe₂]]：多带超导-穿透深度研究体系。
- [[../entities/NbS2|NbS₂]]：泡利顺磁主导的端元材料。
- [[../entities/SrAl2O4|SrAl₂O₄]]：超声机械发光材料。
