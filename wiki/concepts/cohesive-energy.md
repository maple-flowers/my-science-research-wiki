---
tags: [concept]
title: '结合能（内聚能） / Cohesive Energy'
type: concept
status: developing
papers: ['dudarevElectronenergylossSpectraStructural1998a', 'kresseInitiomolecularDynamicsLiquid1993', 'naguib25thAnniversaryArticle2013a']
updated: 2026-08-18
---

# 结合能（内聚能） / Cohesive Energy

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


结合能（cohesive energy）指**将晶体分解为自由原子所需的总能量（或分摊到每个原子/原胞的能量）**，是衡量晶体结构稳定性、描述成键强度的核心热力学量。在密度泛函理论（DFT）计算中，结合能常作为验证结构可靠性、比较相稳定性的关键判据，并衍生出剥离能（exfoliation energy）等层状材料专用量。

## 👵 太奶导读

"结合能"就是问：要把一块晶体"拆散"成一个个孤立的原子，得费多大力？拆起来越费劲，说明原子结合得越牢、结构越稳。计算材料学里，它是判断"这个材料存不存在、稳不稳"的第一把尺子；对层状材料，还能专门算出"撕下一层要多大力"——这就是剥离能。

## 🧩 结合能的计算与验证

- **强关联体系**：LSDA+U 计算氧化镍（NiO）时，取有效 Hubbard U=6.2 eV、Hund 耦合 J=0.95 eV，得到的结合能（11.60 eV）、晶格常数（4.19 Å）与弹性模量均显著优于普通 LSDA，物理机制是 U 增强了 3d 电子局域化、减弱了 Ni-O 共价键合（[[../papers/dudarevElectronenergylossSpectraStructural1998a|Dudarev 1998]]）。
- **从头算基准**：精确基态从头算分子动力学（AIMD）在液态 Na 与 Ge 上实现了 meV 级能量守恒与结构、扩散系数等性质的定量再现，为结合能等热力学量的第一性原理评估提供可靠方法（[[../papers/kresseInitiomolecularDynamicsLiquid1993|Kresse 1993]]）。

## 🧩 结合能与层状材料

- **MXenes 的稳定性判据**：MXene（如 Ti₃C₂Tₓ）通过选择性刻蚀 MAX 相获得，DFT 计算在预测与解释其结构、电子与力学性质（含层间结合强弱）方面发挥关键作用（[[../papers/naguib25thAnniversaryArticle2013a|Naguib 2013]]）。
- **与剥离能的联系**：对层状材料，层间结合能决定剥离难易，见 [[../concepts/exfoliation-energy|剥离能]]。

## 📚 相关论文 (Related Papers)

- [[../papers/dudarevElectronenergylossSpectraStructural1998a]] — Electron-energy-loss spectra and the structural stability of nickel oxide: An LSDA+U study
- [[../papers/kresseInitiomolecularDynamicsLiquid1993]] — Ab initio molecular dynamics for liquid metals
- [[../papers/naguib25thAnniversaryArticle2013a]] — 25th Anniversary Article: MXenes: A New Family of Two-Dimensional Materials

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/density-functional-theory|密度泛函理论]]：结合能计算的主流方法。
- [[../concepts/exfoliation-energy|剥离能]]：层状材料的结合能派生量。
- [[../concepts/2d-materials|二维材料]]：结合能评估的应用对象。
- [[../concepts/band-structure|能带结构]]：与结合能互补的电子结构判据。
- [[../concepts/phase-transition|相变]]：结合能比较用于相稳定性分析。
- [[../concepts/magnetism|磁性]]：强关联体系结合能的磁性依赖。
- [[../concepts/pseudopotential|赝势]]：结合能计算的数值基础。
- [[../entities/NiO|NiO]]：LSDA+U 结合能基准体系。
