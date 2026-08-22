---
tags: [concept]
title: '结合强度 / Binding Strength'
type: concept
status: developing
papers: ['Li2013bonding', 'Wu2021', 'yanDecipheringStabilityTwodimensional2025', 'zhongHighthroughputExfoliationMultiferroic2025']
updated: 2026-08-18
---

# 结合强度 / Binding Strength

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


结合强度（binding strength）指**原子间化学键或层间的束缚强度**，在计算材料学中常以键能、结合能密度或剥离所需能量来量化。它是材料力学性能（弹性模量、极限强度）、结构稳定性与二维材料可剥离性的决定因素。高通量筛选常以"键密度 + 面内/面外结合强度"作为判据，从大量候选晶体中预选可稳定剥离的二维材料。

## 👵 太奶导读

"结合强度"就是原子之间"抱得多紧"。抱得紧，材料就硬、耐拉（强度高）；原子和层之间抱得松，就能像撕胶带一样剥成单层（二维材料）。科学家做高通量筛选时，先算这个"抱得紧不紧"，把上万种候选材料快速筛到几十种再细算，省时又准。

## 🧩 力学性能与电荷转移

单层 TMD 的极限强度由 M→X 电荷转移量 ΔQ 决定：**力学性能（杨氏模量 E、极限强度 σ\*）随 ΔQ 线性增长**，其电子结构根源是 M-d/X-p 轨道杂化强度。扶手椅与锯齿方向的应力-应变曲线揭示了强度对各向异性的依赖（[[../papers/Li2013bonding|Li 2013]]）。

## 🧩 结构与吸附稳定性

- **表面吸附**：Si(001) c(4×2) 重构表面上 Ge 二聚体有 8 种稳定吸附模式，键能与吸附构型由电荷转移与表面二聚体扰动决定（[[../papers/Wu2021|Wu 2021]]）。
- **二维 III-V 半导体**：所有稳定二维 III-V 半导体皆由四面体（sp³）、三角形（sp²）、扭曲三角形三种"积木"经 V 族原子作"柔性胶水"按电子计数规则组装；体系总能是积木能量的线性叠加（[[../papers/yanDecipheringStabilityTwodimensional2025|Yan 2025]]）。

## 🔬 高通量剥离判据

"键密度 + 面内/面外结合强度"通用判据从 831 种 ABO₃ 钙钛矿中筛出 35 种可剥离稳定单层（[[../papers/zhongHighthroughputExfoliationMultiferroic2025|Zhong 2025]]）。结合强度与 [[../concepts/cohesive-energy|内聚能]]、[[../concepts/exfoliation-energy|剥离能]] 共同构成描述二维材料可制备性的能量学三角。

## 📚 相关论文 (Related Papers)

- [[../papers/Li2013bonding]] — Bonding Charge Density and Ultimate Strength of Monolayer Transition Metal Dichalcogenides
- [[../papers/Wu2021]] — Atomic arrangements, bond energies, and charge distribution on Si(0 0 1) surfaces with the adsorption of a Ge dimer by DFTB calculations
- [[../papers/yanDecipheringStabilityTwodimensional2025]] — Deciphering the stability of two-dimensional III-V semiconductors: Building blocks and their versatile assembly
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] — High-throughput exfoliation of multiferroic ternary oxide monolayers

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/bond-density|键密度]]：结合强度的空间密度度量。
- [[../concepts/cohesive-energy|内聚能]]：结合强度的能量学度量。
- [[../concepts/exfoliation-energy|剥离能]]：层间结合强度的度量。
- [[../concepts/2d-materials|二维材料]]：结合强度决定其可剥离性。
- [[../concepts/electron-counting-rule|电子计数规则]]：二维 III-V 稳定性与键合的组织原则。
