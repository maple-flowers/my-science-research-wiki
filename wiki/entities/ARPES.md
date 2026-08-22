---
tags: [entity]
title: 'arpes'
type: entity
status: developing
papers: ['yanagizawaSwitchingChargedensityWave2023', 'CastroNeto2001charge', 'nakataRobustChargedensityWave2021']
updated: 2026-08-18
---

# arpes

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


ARPES（角分辨光电子能谱，Angle-Resolved Photoemission Spectroscopy）是**通过测量光子激发的光电子的能量与角度分布，直接探测材料电子能带结构 E(k)** 的核心实验技术。它是解析拓扑材料、高温超导、二维材料与强关联体系电子结构的"黄金标准"，在凝聚态物理中地位卓著。

## 👵 太奶导读

太奶啊，ARPES 就是用光照材料、把电子"轰"出来，然后仔细看"轰出来的电子朝哪飞、带多少能量"——从这些信息就能反推出材料内部电子"住在哪个能量、往哪个方向跑"的完整地图（能带结构）。想看材料是不是拓扑绝缘体、超导能隙长啥样、二维材料的能带怎么弯，全靠 ARPES 这把"显微镜"。

## 🧩 核心内容与机制 (Core Content)

- **原理**：光电效应 + 能量/动量守恒，由 (E, θ) 映射电子色散 E(k)；需超高真空与同步辐射/激光光源（本库 ARPES 实验论文）。
- **能带成像**：直接可视化能带（band-structure）、费米面（fermi-surfaces）、自旋分辨（spin-ARPES）与自旋极化。
- **应用**：拓扑绝缘体表面态（topological-insulator）、Weyl 半金属、高温超导配对、二维材料（WSe2、h-BN 异质结）能带（本库拓扑与超导 ARPES 论文）。
- **相关技术**：时间分辨 ARPES（trARPES）看超快动力学；与理论（DFT/Wannier）对照。
- **局限**：需导电样品、表面敏感（需解理），超导能隙测量要求高能量分辨率。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/band-structure|能带结构]]：ARPES 直接测量的对象。
- [[../concepts/fermi-surfaces|费米面]]：ARPES 成像的电子结构。
- [[../concepts/topological-insulator|拓扑绝缘体]]：ARPES 确认的拓扑态。
- [[../entities/WSe2|WSe₂]]：ARPES 研究的二维材料。

## 📚 相关论文 (Related Papers)

- [[../papers/yanagizawaSwitchingChargedensityWave2023]] — Switching of charge-density wave by carrier tuning in monolayer TiTe₂

- [[../papers/CastroNeto2001charge]] — Charge Density Wave, Superconductivity, and Anomalous Metallic Behavior in 2D Transition Metal Dichalcogenides
- [[../papers/nakataRobustChargedensityWave2021]] — Robust charge-density wave strengthened by electron correlations in monolayer 1T-TaSe2 and 1T-NbSe2

## 🏷️ 专业名词别名

- `arpes`（concepts）
- `arpes`（entities）
- `ARPES`（entities）
