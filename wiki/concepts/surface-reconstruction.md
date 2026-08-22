---
tags: [concept]
title: '表面重构 / Surface Reconstruction'
type: concept
status: developing
papers: ['Wu2018', 'Wu2021', 'guanRecentProgressTwoDimensional2020', 'liPhaseTransitions2D2021', 'zhongHighthroughputExfoliationMultiferroic2025']
updated: 2026-08-18
---

# 表面重构 / Surface Reconstruction

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


表面重构（surface reconstruction）指**晶体表面原子在失去体相配位后，通过重新排列（如二聚化、弛豫、吸附诱导有序）降低表面自由能**的现象。重构改变表面的原子排布与电荷分布，是理解表面电子结构、吸附行为与二维材料界面性质的基础。半导体表面的重构（如 Si(001) 的 p(2×2)/c(4×2)）是经典研究对象。

## 👵 太奶导读

晶体内部每个原子周围"朋友"很多、很安稳；表面原子却"缺朋友"，悬空的化学键让它们很不舒服。于是表面原子会"自己想办法"：相邻两个原子靠拢成对（二聚化）、或者轻微错位（弛豫），换来整体能量更低——这就是重构。就像一群人站在悬崖边，靠近边缘的人会下意识互相靠近抱团，排列变得和中间不一样。

## 🧩 表面重构的经典案例：Si(001)

Si(001) 表面的悬挂键驱动原子二聚化，形成 p(2×2) 与 c(4×2) 重构。DFTB 计算表明：

- **单 Ge 原子吸附**：Ge 优先吸附于二聚体翘起原子的外侧顶位或二聚体桥位，且总是失去电荷，最终构型与电荷转移模式强烈依赖初始吸附高度和位置（[[../papers/Wu2018|Wu 2018]]）。
- **Ge 二聚体吸附**：对 774 个初始构型系统扫描，识别出 8 种稳定吸附模式；体系能隙变化主要由吸附对 Si 表面二聚体的扰动决定，而非 Ge 原子本身（[[../papers/Wu2021|Wu 2021]]）。

## 🔬 二维材料中的重构与相变

- **二维铁电表征**：表面/界面重构影响二维铁电材料的探测与稳定性，实验证实的二维铁电体集中在 CuInP₂S₆、α-In₂Se₃、SnTe、WTe₂、d1T-MoTe₂、BA₂PbCl₄ 等少数体系（[[../papers/guanRecentProgressTwoDimensional2020|Guan 2020]]）。
- **相变工程**：短程化学键、长程静电/弹性相互作用与空间可及性三维框架统一了二维材料中的多晶型、铁性与扩散相变（[[../papers/liPhaseTransitions2D2021|Li 2021]]）。
- **单层剥离与稳定性**：键密度+结合强度判据从 831 种 ABO₃ 钙钛矿筛出 35 种可剥离稳定单层（[[../papers/zhongHighthroughputExfoliationMultiferroic2025|Zhong 2025]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Wu2018]] — Study of atomic arrangements and charge distribution on Si(0 0 1) surfaces with the adsorption of one Ge atom by DFTB calculations
- [[../papers/Wu2021]] — Atomic arrangements, bond energies, and charge distribution on Si(0 0 1) surfaces with the adsorption of a Ge dimer by DFTB calculations
- [[../papers/guanRecentProgressTwoDimensional2020]] — Recent Progress in Two‐Dimensional Ferroelectric Materials
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] — High-throughput exfoliation of multiferroic ternary oxide monolayers

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dimerization|二聚化]]：Si(001) 表面重构的核心畸变模式。
- [[../concepts/2d-materials|二维材料]]：表面重构影响其稳定性与性质。
- [[../concepts/density-functional-theory|密度泛函理论]]：DFTB 研究表面重构的理论工具。
- [[../concepts/phase-transition|相变]]：重构驱动的表面与体相结构转变。
- [[../concepts/ferroelectricity|铁电性]]：二维铁电体稳定性与表面重构相关。
