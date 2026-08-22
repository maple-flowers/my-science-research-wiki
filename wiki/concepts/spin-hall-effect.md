---
tags: [concept]
title: '自旋霍尔效应 / Spin Hall Effect'
type: concept
status: developing
papers: ['liuSpintronicsTwoDimensionalMaterials2020b', 'kaurRecentAdvancesTheoretical2025a', 'xuTwodimensionalFerroelasticityVan2021']
updated: 2026-08-18
---

# 自旋霍尔效应 / Spin Hall Effect

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


自旋霍尔效应（spin Hall effect, SHE）指**自旋-轨道耦合使纵向电荷流在垂直于电流方向的横向产生纯自旋流（无需外加磁场、无净电荷积累）的现象**。自旋霍尔效应是自旋电子学的核心输运机制之一，用于自旋注入、自旋轨道矩操控与自旋流探测；在二维材料与铁弹/铁电体系中，SHE 与自旋轨道耦合强度、晶格对称性密切相关。

## 👵 太奶导读

普通霍尔效应是磁场把电荷往侧面推，产生横向电压。自旋霍尔效应更绝：不用磁场，靠材料自身"左右手不对称"的原子势（自旋-轨道耦合），就能让自旋朝上和朝下的电子分道扬镳，向两侧各走各路——净电荷没有流动，但"纯自旋流"诞生了。这为不靠磁场造自旋、操控自旋提供了新开关。

## 🏗️ 结构概览

自旋霍尔效应属于自旋-电荷转换家族，与逆自旋霍尔效应（ISHE，探测自旋流的互逆过程）、埃德尔斯坦效应并列为无磁场自旋操控路径。其强度由自旋-轨道耦合与体系对称性决定，分为内禀（能带 Berry 曲率）与外禀（杂质散射）贡献。

## 🧩 核心内容与机制 (Core Content)

### 二维自旋电子学视角

- **二维材料的自旋注入与操控**：2D 材料是自旋电子学的理想平台——通过 hBN 隧道势垒电学注入已实现近 100% 的自旋极化率；通过 hBN 封装和悬浮技术，石墨烯的自旋弛豫时间和扩散长度极大提升；异质结邻近效应是实现自旋操控的有效途径。然而实现室温二维铁磁性、解决自旋操控与传输的矛盾、走向大规模集成仍是核心挑战（[[../papers/liuSpintronicsTwoDimensionalMaterials2020b|Liu 2020]]）。
- **理论进展**：滑动铁电/层状二维材料的理论研究表明，层间滑移可同时调控极性与自旋轨道相关输运，为自旋霍尔效应等自旋输运现象提供新自由度（[[../papers/kaurRecentAdvancesTheoretical2025a|Kaur 2025]]）。

### 铁弹性调制视角

- **铁弹畴与自旋-轨道相关输运**：β'-In₂Se₃ 具有源于反铁电畸变的约 0.49% 二维自发应变，形成三种取向畴变体，可在 ≤0.5% 外部应变下通过畴壁传播和畴成核机制实现畴的可逆切换——铁弹畴的重排会改变局域晶格对称性，从而调制与自旋-轨道耦合相关的输运（如自旋霍尔效应）（[[../papers/xuTwodimensionalFerroelasticityVan2021|Xu 2021]]）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 自旋霍尔角 | 电荷流→自旋流转换效率 | 依赖 SOC 与散射 |
| 贡献机制 | 内禀/外禀 | Berry 曲率 vs 杂质散射 |
| 横向自旋流 | 无净电荷流 | 自旋-电荷分离 |
| 体系要求 | 强 SOC | 重元素、界面、铁弹畴调制 |
| 逆过程 | ISHE | 自旋流→电荷流探测 |

## 🔀 近邻概念辨析

- **SHE vs 普通霍尔效应**：SHE 无需外磁场、横向产生纯自旋流无电荷积累；普通霍尔效应需磁场产生横向电压。
- **SHE vs 埃德尔斯坦效应**：SHE 可在中心对称体相出现；埃德尔斯坦效应依赖反演破缺（界面/极性）。
- **SHE vs 量子自旋霍尔效应**：SHE 是体相输运现象；QSHE 是拓扑态，边缘态无耗散且受拓扑保护。

## 📚 相关论文 (Related Papers)

- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]] — Spintronics in Two-Dimensional Materials
- [[../papers/xuTwodimensionalFerroelasticityVan2021]] — Two-dimensional ferroelasticity in van der Waals β'-In₂Se₃

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-transport|自旋输运]]：自旋霍尔效应的上游/下游过程。
- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：自旋霍尔效应的物理根源。
- [[../concepts/topological-insulator|拓扑绝缘体]]：与 SHE 相关的自旋极化边缘态。
- [[../concepts/ferroelasticity|铁弹性]]：晶格对称性对 SHE 的调制。
- [[../concepts/spin-texture|自旋织构]]：动量空间的自旋排列。
- [[../entities/WSe2|WSe₂]]：自旋电子学二维体系。
- [[../entities/In2Se3|In₂Se₃]]：铁弹畴调制输运的二维材料。
