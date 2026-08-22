---
tags: [concept, ferroelectrics, multiferroicity, nanoelectronics]
title: 畴壁工程 / Domain Wall Engineering
type: concept
status: developing
domain: [ferroelectrics, ferroelasticity, magnetism, multiferroicity, nanoelectronics]
mechanism: 通过电场、应变或针尖力学对畴壁进行设计、操控与功能化，利用壁异于体相的导电/极性/磁性与拓扑性质构建纳米功能元件
related_concepts: [domain-wall, domain-wall-energy, ferroelasticity, multiferroicity, magnetoelectric-coupling, ferroelectricity, sliding-ferroelectricity, strain-engineering]
papers: [fiebigEvolutionMultiferroics2016, liFerroelasticityDomainPhysics2016, xuTwodimensionalFerroelasticityVan2021, heUltrafastSwitchingDynamics2024]
updated: 2026-08
---

# 畴壁工程 / Domain Wall Engineering

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


畴壁工程（domain wall engineering）指**对铁电/铁弹/磁性材料中相邻畴之间的过渡界面（畴壁）进行设计、操控与功能化**的技术。畴壁具有与体相迥异的导电性、极性、磁性与拓扑性质，被视为"纳米功能元件"——如导电畴壁、磁电畴壁与拓扑畴界，可通过电场、应变或针尖力学操控，是多铁与低维材料器件化的核心手段。

## 👵 太奶导读

太奶啊，铁电/铁磁材料内部分成一块块"方向一致的小区域"（畴），区域之间的"分界线"就是畴壁。这条分界线别看只有几个原子厚，却常常"身怀绝技"：能导电（本身材料是绝缘体）、能开关、还特别薄。畴壁工程就是想办法"玩转"这些分界线——用电压或压力把它们推来推去、写进去擦掉，做成比传统器件小得多的"畴壁器件"。

## 🧩 畴壁的物理与新功能

畴壁拥有体相不具备的对称性，可承载新物理：导电畴壁（domain-wall nanoelectronics）、磁电畴壁（磁化与极化同时改变）、以及涡旋/斯格明子等拓扑缺陷。多铁性领域将畴壁视为超越存储的功能元件来源 [[../papers/fiebigEvolutionMultiferroics2016]]（见 [[../concepts/multiferroicity|多铁性]]）。

## 🔬 低维畴壁的操控

- **铁弹畴壁**：1T′ 相 TMD 单层的 Peierls 畸变产生三个取向变体，仅需百分之几应变即可切换，形成低能准一维铁弹畴壁 [[../papers/liFerroelasticityDomainPhysics2016]]；少层 β'-In₂Se₃ 中实现 ≤0.5% 外应变下的可逆畴切换 [[../papers/xuTwodimensionalFerroelasticityVan2021]]。
- **超快畴壁运动**：堆叠工程铁电（h-BN 双层）中，深度势能机器学习势模拟表明畴壁运动可将临界翻转场降低两个数量级、实现皮秒级翻转 [[../papers/heUltrafastSwitchingDynamics2024]]。

## 📊 畴壁工程手段与功能

| 手段 | 操控对象 | 功能产物 | 典型材料 |
|------|----------|----------|----------|
| 电场 | 导电畴壁创建/擦除 | 可重写互连、存储 | BiFeO3、YMnO3 |
| 应变 | 铁弹畴壁切换 | 应变可编程器件 | β'-In₂Se₃、1T′-TMD |
| 针尖力学 | 局域壁移动 | 扫描探针器件 | 铁电薄膜 |
| 堆叠工程 | 层间滑移势垒 | 超快开关 | h-BN、滑动铁电 |

## 📚 相关论文 (Related Papers)

- [[../papers/liFerroelasticityDomainPhysics2016]] — Ferroelasticity and domain physics in two-dimensional transition metal dichalcogenide monolayers
- [[../papers/xuTwodimensionalFerroelasticityVan2021]] — Two-dimensional ferroelasticity in van der Waals β'-In2Se3
- [[../papers/heUltrafastSwitchingDynamics2024]] — Ultrafast switching dynamics of the ferroelectric order in stacking-engineered ferroelectrics
- [[../papers/fiebigEvolutionMultiferroics2016]] — The evolution of multiferroics

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/domain-wall-energy|畴壁能]]：畴壁形成与稳定性的能量学。
- [[../concepts/ferroelasticity|铁弹性]]：铁弹畴壁的应变操控。
- [[../concepts/multiferroicity|多铁性]]：磁电畴壁的功能化背景。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：畴壁处的磁电新物理。
- [[../concepts/ferroelectricity|铁电性]]：导电畴壁的载体。
- [[../concepts/sliding-ferroelectricity|滑动铁电]]：堆叠工程畴壁平台。
- [[../concepts/strain-engineering|应变工程]]：铁弹畴壁的驱动场。
- [[../entities/In2Se3|In₂Se₃]]：二维铁弹畴壁材料。
- [[../entities/BiFeO3|BiFeO₃]]：导电畴壁代表材料。

## 🏷️ 专业名词别名

- `domain-wall-technology`（concepts）
- `畴壁器件工程`（concepts）
