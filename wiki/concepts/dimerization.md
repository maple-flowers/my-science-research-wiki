---
tags: [concept]
title: '二聚化 / Dimerization'
type: concept
status: developing
papers: ['Johannes2008fermi', 'chenFerromagneticNonmagnetic1T2022', 'liFerroelasticityDomainPhysics2016', 'pedramraziManipulatingTopologicalDomain2019', 'nicholsonUniaxialStraininducedPhase2021']
updated: 2026-08-18
---

# 二聚化 / Dimerization

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


二聚化（dimerization）指**晶格中相邻原子两两成对、缩短键长并打开能隙**的结构畸变。它是一维与准低维体系电子-晶格不稳定性的典型表现，构成 Peierls 畸变、电荷密度波（CDW）与 1T′ 相 TMD 微观起源的核心要素，同时也与铁弹性变体、拓扑畴界等物理现象紧密相连。

## 👵 太奶导读

想象一队原本等间距站着的士兵（金属：电子能自由流动）。低温下他们忽然"两两抱团"——相邻两人靠得近、和下一对之间拉得远（二聚化）。抱团让电子"路变窄"（打开能隙），队伍从"能自由跑"变成"被卡住"（从金属变绝缘或半导）。这种"成对"的原子排列，就是材料里各种奇妙相变（电荷密度波、拓扑相）的开端。

## 🧩 二聚化与费米面嵌套：一个重要的修正

经典图像认为二聚化/CDW 由**费米面嵌套（Fermi surface nesting）**驱动。但 Johannes 与 Mazin 通过理论推导与 NbSe₂、TaSe₂、CeTe₃ 及 Na 原子链的第一性原理计算证明，**费米面嵌套不是真实材料中 CDW 的驱动力**——CDW 本质上是由动量依赖的电子-声子耦合驱动的结构相变（[[../papers/Johannes2008fermi|Johannes 2008]]）。这一认识深刻影响了人们对二聚化起源的理解。

## 🔬 1T′ 相中的二聚化机制

在 TMD 的 1T′ 相中，M-M 二聚化链是稳定该相的 Peierls 型畸变（[[../papers/chenFerromagneticNonmagnetic1T2022|Chen 2022]]），并由此产生三个取向变体（O1/O2/O3），仅需百分之几弹性应变即可实现铁弹切换，势垒 <0.2 eV/f.u.（[[../papers/liFerroelasticityDomainPhysics2016|Li 2016]]，见 [[../concepts/ferroelasticity|铁弹性]]）。

## 🧲 二聚化、拓扑与应变调控

- **拓扑畴界操控**：单层 1T′-WSe₂ 中，STM 针尖脉冲可逆写入/擦除铁弹畴界并诱导 1T′→1H 相变，调控量子自旋霍尔绝缘体的拓扑畴界态（[[../papers/pedramraziManipulatingTopologicalDomain2019|Pedramrazi 2019]]）。
- **应变诱导电荷有序**：沿 a 轴施加约 0.1% 单轴拉伸应变即可在宏观尺度上选择性稳定 IrTe₂ 长期争论的 6×1 电荷有序基态，并首次光谱学观测到伴随的 Lifshitz 转变与 II 型体狄拉克态（[[../papers/nicholsonUniaxialStraininducedPhase2021|Nicholson 2021]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Johannes2008fermi]] — Fermi surface nesting and the origin of charge density waves in metals
- [[../papers/chenFerromagneticNonmagnetic1T2022]] — Ferromagnetic and nonmagnetic 1T′ charge density wave states in transition metal dichalcogenides
- [[../papers/liFerroelasticityDomainPhysics2016]] — Ferroelasticity and domain physics in two-dimensional transition metal dichalcogenide monolayers
- [[../papers/pedramraziManipulatingTopologicalDomain2019]] — Manipulating Topological Domain Boundaries in the Single-Layer Quantum Spin Hall Insulator 1T′–WSe₂
- [[../papers/nicholsonUniaxialStraininducedPhase2021]] — Uniaxial strain-induced phase transition in the 2D topological semimetal IrTe2

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/peierls-distortion|Peierls 畸变]]：二聚化是其一维/低维的具体表现形式。
- [[../concepts/charge-density-wave|电荷密度波]]：二聚化驱动的电子-晶格周期序。
- [[../concepts/ferroelasticity|铁弹性]]：二聚化畸变的多取向变体切换。
- [[../concepts/trimerization|三聚化]]：三分之周期畸变的同类不稳定性。
- [[../concepts/2d-materials|二维材料]]：1T′ 相二聚化的载体体系。
- [[../entities/IrTe2|IrTe₂]]：应变稳定电荷有序与二聚化的拓扑半金属。
