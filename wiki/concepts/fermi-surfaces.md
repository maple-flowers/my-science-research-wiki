---
tags: [concept, electronic-structure]
title: 费米面 / Fermi Surfaces
type: concept
status: developing
related_concepts: [brillouin-zone, charge-density-wave, band-structure, fermi-surface-nesting, ARPES]
papers: [Barnett2006coexistence, Delley2000, Islam2025enhancement, Johannes2008fermi, Kang2012dimer, Laverock2005fermi, Makogon2012wave, bhowalPolarMetalsPrinciples2023b, hallEnvironmentalControlCharge, kaurRecentAdvancesTheoretical2025a, kawakamiChargedensityWaveAssociated2023, lvUnconventionalHystereticTransition2022, majumdarInterplayChargeDensity2020, monkhorstSpecialPointsBrillouinzone1976, nicholsonUniaxialStraininducedPhase2021, wangTunableD0Topological2025b, wongEvidenceMetallic1T, yanagizawaSwitchingChargedensityWave2023, zhengAnisotropicSuperconductivityTwodimensional2025, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08
---

# fermi-surfaces

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


费米面（Fermi surface）是动量空间（布里渊区）中**电子占据态与非占据态的分界面**，即费米能级处的等能面。它的形状、拓扑与嵌套性质决定了金属/半金属的电子输运、磁性、超导与电荷密度波（CDW）等几乎所有电子物性，是凝聚态物理的核心概念。

## 👵 太奶导读

太奶啊，金属里的电子像一池水，费米面就是"水位线"——水面以下电子占满，水面以上空着。这池水的"水面形状"非常关键：水面平平（简单形状）材料普通，水面扭来扭去（复杂形状）就可能出大事——比如两块水面平行对峙（费米面嵌套），电子一激动就搞出电荷密度波；超导、磁性也跟水面在哪儿有关。

## 🧩 核心内容与机制 (Core Content)

- **定义与测量**：费米面是布里渊区中 ε(k)=E_F 的等能面；可通过 ARPES、量子振荡（de Haas-van Alphen）、康普顿散射等实验测量。
- **拓扑与轨道**：费米面拓扑（闭合/开放轨道、口袋、鞍点）决定输运与磁性；Lifshitz 相变由费米面拓扑改变引起。
- **费米面嵌套（nesting）**：费米面不同部分平行时，静态极化率发散，驱动 CDW 与自旋密度波（SDW）不稳定性（本库多篇 TMD/CDW 论文的核心机制）。
- **与超导/磁性**：费米面态密度与嵌套结构影响超导配对与磁性不稳定性（Stoner 判据）。
- **二维体系**：二维材料的费米面形状与角分辨测量（ARPES）对其 CDW、超导研究至关重要。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/brillouin-zone|布里渊区]]：费米面所在的动量空间。
- [[../concepts/charge-density-wave|电荷密度波]]：费米面嵌套驱动的有序态。
- [[../concepts/band-structure|能带结构]]：费米面是能带的等能面。
- [[../concepts/fermi-surface-nesting|费米面嵌套]]：费米面平行的关键机制。
- [[../entities/ARPES|ARPES]]：测量费米面的主要实验手段。

## 📚 相关论文 (Related Papers)

- [[../papers/Barnett2006coexistence]] — Coexistence of Gapless Excitations and Commensurate Charge-Density Wave in the 2H Transition Metal Dichalcogenides
- [[../papers/Delley2000]] — From molecules to solids with the DMol3 approach
- [[../papers/Islam2025enhancement]] — Pressure-induced enhancement of superfluid density in transition metal dichalcogenides with and without charge density wave
- [[../papers/Johannes2008fermi]] — Fermi surface nesting and the origin of charge density waves in metals
- [[../papers/Kang2012dimer]] — Dimer impurity scattering, reconstructed Fermi-surface nesting, and density-wave diagnostics in iron pnictides
- [[../papers/Laverock2005fermi]] — Fermi surface nesting and charge-density wave formation in rare-earth tritellurides
- [[../papers/Makogon2012wave]] — Spin-charge-density wave in a rounded-square Fermi surface for ultracold atoms
- [[../papers/bhowalPolarMetalsPrinciples2023b]] — Polar Metals: Principles and Prospects
- [[../papers/hallEnvironmentalControlCharge]] — Environmental Control of Charge Density Wave Order in Monolayer 2H-TaS₂
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/kawakamiChargedensityWaveAssociated2023]] — Charge-density wave associated with higher-order Fermi-surface nesting in monolayer VS2
- [[../papers/lvUnconventionalHystereticTransition2022]] — Unconventional Hysteretic Transition in a Charge Density Wave
- [[../papers/majumdarInterplayChargeDensity2020]] — Interplay of charge density wave and multiband superconductivity in layered quasi-two-dimensional materials: The case of 2H-NbS₂ and 2H-NbSe₂
- [[../papers/monkhorstSpecialPointsBrillouinzone1976]] — Special points for Brillouin-zone integrations
- [[../papers/nicholsonUniaxialStraininducedPhase2021]] — Uniaxial strain-induced phase transition in the 2D topological semimetal IrTe2
- [[../papers/wangTunableD0Topological2025b]] — Tunable d0 topological magnetic states in multiferroic monolayer In2NO2
- [[../papers/wongEvidenceMetallic1T]] — Metallic 1T Phase, 3d1 Electronic Configuration and Charge Density Wave Order in Molecular Beam Epitaxy Grown Monolayer Vanadium Ditelluride
- [[../papers/yanagizawaSwitchingChargedensityWave2023]] — Switching of charge-density wave by carrier tuning in monolayer TiTe₂
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] — Anisotropic superconductivity in the two-dimensional metal-organic kagome framework Cu 3 ( CO ) 6
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] — High-throughput exfoliation of multiferroic ternary oxide monolayers with high transition temperature and giant spin splitting
