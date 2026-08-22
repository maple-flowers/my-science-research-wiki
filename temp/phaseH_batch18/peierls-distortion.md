---
tags: [concept]
title: 'Peierls 畸变 / Peierls Distortion'
type: concept
status: developing
papers: ['chenFerromagneticNonmagnetic1T2022', 'liFerroelasticityDomainPhysics2016', 'pedramraziManipulatingTopologicalDomain2019', 'xuTwodimensionalFerroelasticityVan2021', 'krishnamurthiSpinChargeDensity2020', 'tahirFerroelectricityNonvolatileMemristor2025']
updated: 2026-08-18
---

# Peierls 畸变 / Peierls Distortion

Peierls 畸变（Peierls distortion）指**一维（或准一维）金属因费米面嵌套而在低温下发生晶格二聚化/周期性畸变、打开能隙而失去金属性**的电子-晶格不稳定性。它由 Rudolf Peierls 于 1955 年提出，是电荷密度波（CDW）在低维体系中的经典微观起源，也是二维过渡金属硫属化物（TMD）1T′ 相、铁弹性变体与拓扑绝缘体形成的关键机制。

## 👵 太奶导读

想象一条单行道的马路，大家都想开快车（金属导电）。但这条路太"挤"了——每隔一段距离，路上的"柱子"（原子）就会两两抱成一团，把路"收紧"，车反而开不快了（变绝缘）。原子越抱团，路越堵，但抱团后体系更"省力"（能量更低）。这条"原子抱团"的路就叫 Peierls 畸变。低温时原子"冷得发抖少了"，更容易抱团，很多低维材料就这么从"金属"变成了"绝缘体"。

## 🧩 微观机制：费米面嵌套与二聚化

准一维金属的费米面近似平行（**嵌套**），使得 2k_F 波矢处的电子-声子耦合被强烈放大：晶格以 2k_F 周期发生**二聚化**畸变，布里渊区边界打开能隙，电子系统失去费米面。这一"电子能降 + 晶格弹性能升"的权衡决定了畸变幅度与相变温度。在二维 TMD 中，1T′ 相即由 Peierls 畸变（M-M 二聚化链）稳定，其能量学可通过 DFT 精确刻画（[[../papers/chenFerromagneticNonmagnetic1T2022|Chen 2022]]，见 [[../concepts/dimerization|二聚化]]）。

## 🔬 铁弹性变体与畴工程

Peierls 畸变不仅是电子相变，还赋予材料**铁弹性**：畸变可在多个等价方向（取向变体）之间切换，形成低能畴壁。

- **1T′ TMD 单层**：第一性原理计算首次预测 1T′ 相 TMD 单层具有三个由 Peierls 畸变产生的取向变体（O1/O2/O3），仅需百分之几弹性应变即可在变体间铁弹切换，切换势垒 <0.2 eV/f.u.，形成低能准一维铁弹畴壁（[[../papers/liFerroelasticityDomainPhysics2016|Li 2016]]）。
- **拓扑畴界操控**：STM 针尖脉冲可在单层 1T′-WSe₂ 中可逆写入/擦除铁弹畴界并诱导 1T′→1H 相变，从而操控量子自旋霍尔绝缘体的拓扑畴界（[[../papers/pedramraziManipulatingTopologicalDomain2019|Pedramrazi 2019]]）。
- **范德华 β'-In₂Se₃**：面内反铁电畸变驱动的二维铁弹性，自发应变约 0.49%，可在外应变 ≤0.5% 下可逆切换畴（[[../papers/xuTwodimensionalFerroelasticityVan2021|Xu 2021]]）。

## 🧲 边界电子态与磁序

Peierls 型晶格极化还可表现为纯电子型不稳定性：TMD 镜像孪晶界的金属性源于 D₃ₕ 晶格极化这一 Z₃ 拓扑不变量在边界处的反转，导致边界态 1/3 分数占据，自发形成无需原子位移的三重周期自旋/电荷密度波（SDW/CDW）（[[../papers/krishnamurthiSpinChargeDensity2020|Krishnamurthi 2020]]，见 [[../concepts/spin-density-wave|自旋密度波]]）。

## 💾 器件应用

Peierls 畸变相关的铁弹/铁电序可直接服务于器件：自支撑 Nb₂CTₓ MXene 薄膜中观测到铁电性（Pr=5.12 μC/cm²），其氧空位与结构畸变构成非易失忆阻器的开关机制（[[../papers/tahirFerroelectricityNonvolatileMemristor2025|Tahir 2025]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/liFerroelasticityDomainPhysics2016]] — Ferroelasticity and domain physics in two-dimensional transition metal dichalcogenide monolayers
- [[../papers/pedramraziManipulatingTopologicalDomain2019]] — Manipulating Topological Domain Boundaries in the Single-Layer Quantum Spin Hall Insulator 1T′–WSe₂
- [[../papers/xuTwodimensionalFerroelasticityVan2021]] — Two-dimensional ferroelasticity in van der Waals β'-In2Se3
- [[../papers/chenFerromagneticNonmagnetic1T2022]] — Ferromagnetic and nonmagnetic 1T′ charge density wave states in transition metal dichalcogenides
- [[../papers/krishnamurthiSpinChargeDensity2020]] — Spin/charge density waves at the boundaries of transition metal dichalcogenides
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]] — Ferroelectricity and Nonvolatile Memristor Applications of Free‐Standing 2D Niobium Carbide

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]：Peierls 畸变是低维 CDW 的经典微观起源。
- [[../concepts/dimerization|二聚化]]：Peierls 畸变的结构表现——原子成对。
- [[../concepts/ferroelasticity|铁弹性]]：Peierls 畸变的多变体切换行为。
- [[../concepts/spin-density-wave|自旋密度波]]：无需原子位移的纯电子型周期序。
- [[../concepts/2d-materials|二维材料]]：Peierls 畸变在 TMD 单层中的核心作用。
- [[../concepts/trimerization|三聚化]]：三分之周期畸变的另一类电子-晶格不稳定性。
- [[../entities/WTe2|WTe₂]]：1T′ 相 Peierls 畸变与拓扑性质的代表体系。
- [[../entities/In2Se3|In₂Se₃]]：范德华铁弹性与畸变耦合的典型材料。
