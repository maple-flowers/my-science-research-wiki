---
tags: [concept]
title: 'brillouin-zone'
type: concept
status: developing
papers: ['Kang2012dimer', 'Laverock2005fermi', 'chowdhuryReviewTheoreticalComputational', 'dudarevElectronenergylossSpectraStructural1998a', 'king-smithTheoryPolarizationCrystalline1993', 'liMonolayerPuckeredPentagonal2022', 'shenEmergenceMultipleFerroelectric2025', 'yuFerroelectricControlMagnetism2026', 'zhengAnisotropicSuperconductivityTwodimensional2025']
updated: 2026-08-18
---

# brillouin-zone

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


布里渊区（Brillouin zone, BZ）是倒空间中周期晶格的**魏格纳-塞茨原胞（Wigner-Seitz cell）**，是描述晶体电子能带、费米面与各种集体激发在动量空间分布的基本框架。周期势下的布洛赫波函数以波矢 **k** 标记，全部不等价 **k** 点都集中在第一布里渊区（1st BZ）内，因此能带结构、态密度、费米面嵌套等计算都在 BZ 中进行。

## 👵 太奶导读

太奶啊，晶体的原子排得整整齐齐，电子在里面"排队唱歌"，每个电子都有一个"节拍号"（波矢 k）。布里渊区就像是所有不同节拍号电子的一张"地图"——所有可能的不同节拍都在这张地图里。科学家算能带、看费米面、研究电子怎么不老实（比如形成电荷密度波），都要在这张地图上做文章。

## 🧩 核心内容与机制 (Core Content)

- **倒空间与 BZ**：倒格矢由正格矢定义，第一布里渊区为倒空间 Wigner-Seitz 原胞；BZ 形状反映晶格对称性（如六角格子的六边形 BZ）。
- **高对称点与路径**：BZ 中的高对称点（Γ、X、M、K 等）与连线构成能带计算的路径，能带色散即沿这些路径展开。
- **费米面与嵌套**：费米面是 BZ 中占据态与非占据态的边界；费米面嵌套（不同费米面片平行部分）是电荷密度波（CDW）等电子有序态的重要驱动机制（本库多篇 CDW 论文以此为出发点）。
- **k 点采样**：BZ 积分（态密度、总能量）通过 Monkhorst-Pack 等 k 网格离散求和实现，密度与收敛性决定计算精度。
- **与极化/拓扑的关系**：Berry 相位（本库 king-smith1993 极化理论）通过 BZ 上的波函数几何相位定义电极化；BZ 拓扑性质（陈数）刻画拓扑绝缘体/半金属。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/band-structure|能带结构]]：能带即定义在 BZ 上的色散关系。
- [[../concepts/fermi-surfaces|费米面]]：费米面嵌套是 CDW 的关键机制。
- [[../concepts/charge-density-wave|电荷密度波]]：其不稳定性与 BZ 费米面嵌套相关。
- [[../concepts/density-of-states|态密度]]：BZ 积分的直接产物。
- [[../entities/ARPES|ARPES]]：实验上直接测量 BZ 中的能带与费米面。
- [[../concepts/berry-phase|Berry 相位]]：通过 BZ 几何定义电极化与拓扑不变量。

## 📚 相关论文 (Related Papers)

- [[../papers/Kang2012dimer]] — Dimer impurity scattering, reconstructed Fermi-surface nesting, and density-wave diagnostics in iron pnictides
- [[../papers/Laverock2005fermi]] — Fermi surface nesting and charge-density wave formation in rare-earth tritellurides
- [[../papers/chowdhuryReviewTheoreticalComputational]] — Computational Methods for Charge Density Waves in 2D Materials
- [[../papers/dudarevElectronenergylossSpectraStructural1998a]] — Electron-energy-loss spectra and the structural stability of nickel oxide:  An LSDA+U study
- [[../papers/king-smithTheoryPolarizationCrystalline1993]] — Theory of polarization of crystalline solids
- [[../papers/liMonolayerPuckeredPentagonal2022]] — Monolayer puckered pentagonal VTe2: An emergent two-dimensional ferromagnetic semiconductor with multiferroic coupling
- [[../papers/shenEmergenceMultipleFerroelectric2025]] — Emergence of multiple ferroelectric states in multilayer black phosphorus
- [[../papers/yuFerroelectricControlMagnetism2026]] — Ferroelectric Control of Magnetism and Giant Magnetoresistance Via Intercalation-Induced Symmetry Breaking in Two-Dimensional Multiferroics with Strong Magnetoelectric Coupling
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] — Anisotropic superconductivity in the two-dimensional metal-organic kagome framework Cu 3 ( CO ) 6
