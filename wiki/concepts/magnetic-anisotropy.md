---
tags: [concept, magnetism]
title: 磁各向异性 / Magnetic Anisotropy
type: concept
status: mature
domain: [condensed-matter-physics, magnetism]
mechanism: 磁性能随晶格方向不同而表现出的差异，源于晶体场和自旋-轨道耦合
related_concepts: [spin-orbit-coupling, magnetoelectric-coupling, easy-axis, easy-plane]
papers: [caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenStrongSlidingFerroelectricity2024, prosandeevKittelLawInBiFeO3Ultrathin2010, hanTunableSlidingFerroelectricity2025, songEvidenceSinglelayerVan2022, wangTunableD0Topological2025b, fengFerroelectricityMultiferroicityTwodimensional2020, liMonolayerPuckeredPentagonal2022, liPhaseTransitions2D2021, liuSpintronicsTwoDimensionalMaterials2020b, rameshMultiferroicsProgressProspects2007, spaldinAdvancesMagnetoelectricMultiferroics2019, tangMultiferroicityTwodimensionalVan2025, wuElectrostaticGatingIntercalation2022, wuNonvolatileSwitchableHalfmetallicity2024, zhangNonvolatileControlTopological2025, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08
---

# 磁各向异性 / Magnetic Anisotropy

磁各向异性 (Magnetic Anisotropy) 指的是材料的磁学性质（如磁化能、矫顽力等）在空间不同方向上表现出差异的特性。这意味着自旋倾向于指向某些特定方向（易磁化轴）而非其他方向（难磁化轴）。它是实现非易失性磁存储的物理前提。

## 👵 太奶导读

好孩子，这“各向异性”就像是给磁铁里的小箭头找了个“舒适区”。
通常情况下，小箭头往哪儿指都行。但因为材料的原子排布是有讲究的，有些方向就像是宽敞的大道（易轴），小箭头呆在那儿最省力；有些方向就像是窄小的胡同（难轴），非要往那儿指就得费老鼻子劲了。
要是没有这种偏心眼，咱们硬盘里的数据就像沙子一样随风倒，根本存不住。科学家们现在想方设法用应变或者电场去改这个“舒适区”，好让小箭头能听话地翻转。

## 🏗️ 结构概览：应变调控磁各向异性

在二维 Fe₃GaTe₂ 中，磁各向异性能 (MAE) 随面内应变发生显著变化。

![图：Fe3GaTe2 的磁各向异性能随应变翻转示意](../../raw/figures/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025/fig_2_BQHGIU8F.png)
*   **看图要点**：图中 (f) 展示了 DFT 计算得到的 MAE。在零应变下，面外方向 (mz) 能量最低；随着拉伸应变增加，面内方向 (mx) 变为能量最低，实现了易轴的 90° 翻转。
*   **来源**：[[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]] -> [[../figures/vibrational-spectra]]

## 🧩 能量项与来源

总磁能通常表示为：
$$ E_a = K_u \sin^2 \theta $$
其中 $K_u$ 为磁各向异性常数。

主要来源包括：
1.  **磁晶各向异性 (Magnetocrystalline Anisotropy)**：核心来源，由自旋-轨道耦合 (SOC) 将自旋方向与晶体轴绑定。
2.  **形状各向异性 (Shape Anisotropy)**：由磁静电能决定，倾向于使磁矩沿长轴排列。
3.  **磁弹各向异性 (Magnetoelastic Anisotropy)**：由应变改变轨道占据和能级分裂引起。

## 🔬 实验表征/特征与范例

**应变翻转易轴（Fe₃GaTe₂）**：在 Fe₃GaTe₂/P(VDF-TrFE) 双栅极范德华异质结中，通过底栅逆压电效应引入应变，实现应变介导的磁电耦合。DFT 计算显示零应变时面外 (mz) 能量最低，随拉伸应变增加面内 (mx) 变为能量最低，实现易轴 90° 翻转，可在室温下实现非易失、全电学、超低功耗的磁性调控 [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]。

**单层范德华多铁（NiI₂）**：单层 NiI₂ 中通过二次谐波产生（SHG）、圆偏振拉曼等非侵入光学手段，证实了螺旋磁序诱导的本征第二类多铁性，磁手性序与极性序在单层极限下共存，将多铁物理拓展至二维 [[../papers/songEvidenceSinglelayerVan2022]]。

**d0 拓扑磁态（In₂NO₂）**：单层 In₂NO₂ 是 p 轨道诱导的 d0 铁磁半金属，兼具本征铁电性，可承载斯格明子、双半子等拓扑自旋结构；d0 磁性因小磁矩与巡游性，赋予拓扑自旋结构更高的温度与磁场稳定性，并可通过应变与铁电场多维度调控 [[../papers/wangTunableD0Topological2025b]]。

**五边形 VTe₂**：单层褶皱五边形 VTe₂ 是二维铁磁半导体，兼具铁弹性，形成铁弹-铁磁耦合的多铁性，其磁各向异性能（MAE）决定易磁化轴取向 [[../papers/liMonolayerPuckeredPentagonal2022]]。

**滑动铁电（RuX₂、HgI₂）**：RuX₂ (X=Cl, Br, I) 双层/三层通过层间滑移产生可调极化，与铁磁序共存形成二维多铁 [[../papers/hanTunableSlidingFerroelectricity2025]]；HgI₂ 双层滑动铁电极化最高约 0.16 μC/cm²，达到实验可检测水平，且 Rashba 自旋纹理可随极化翻转调控，为自旋场效应晶体管提供新思路 [[../papers/chenStrongSlidingFerroelectricity2024]]。

**多铁异质结电控磁性**：Hf₂MnC₂O₂/Sc₂CO₂ 多铁异质结中，通过铁电极化翻转实现非易失、可开关的半金属性与磁性 [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]；CrInTe₂/In₂Se₃ 异质结中，铁电局域场协同调控界面 DMI 与 MAE，实现非易失电控斯格明子，并提出无量纲稳定性判据 κ [[../papers/zhangNonvolatileControlTopological2025]]。

**基特尔定律（BiFeO₃）**：BFO 超薄膜中条带状 71° 铁电畴遵循基特尔定律（畴宽 ∝ √厚度），但其微观机制由氧八面体倾斜与磁电耦合主导，颠覆了传统铁电/铁磁薄膜的认知 [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]。

**Sc₂P₂Se₆ / ScCrP₂Se₆**：Sc₂P₂Se₆ 为纯铁电体（P 原子翘曲），ScCrP₂Se₆ 通过 Cr 替换实现铁电与铁磁共存，突破 d⁰ 规则，展现磁电耦合 [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]。

**高通量 ABO₃ 单层**：从 831 种 ABO₃ 三元氧化物中高通量筛选出 35 种可剥离单层（如 SrOsO₃、SrIrO₃、BiFeO₃），兼具高磁转变温度与巨自旋分裂，为多铁氧化物单层提供候选库 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。

**二维自旋电子学与相变背景**：二维材料（石墨烯、TMDs、Fe₃GeTe₂、CrI₃ 等）为自旋注入、传输与操控提供平台，磁各向异性是决定自旋取向与稳定性的关键参数 [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]；二维相变（铁电、铁弹、CDW 等）与应变调控为各向异性工程提供手段 [[../papers/liPhaseTransitions2D2021]]。

**多铁性综述背景**：多铁性薄膜（BiFeO₃ 等）与磁电耦合的经典综述 [[../papers/rameshMultiferroicsProgressProspects2007]]、[[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]；二维范德华多铁性的挑战与机遇 [[../papers/tangMultiferroicityTwodimensionalVan2025]]；静电门控与插层作为磁性调控手段 [[../papers/wuElectrostaticGatingIntercalation2022]]。

## 📚 相关论文 (Related Papers)

- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：定量研究了应变对 Fe₃GaTe₂ 磁各向异性的调控。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：分析了 SOC 对滑动铁电中各向异性的贡献。
- [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]：探讨了薄膜中畴壁能与各向异性的标度关系。
- [[../papers/hanTunableSlidingFerroelectricity2025]]：研究了 RuX₂ (X=Cl, Br, I) 滑动铁电层中可调的铁电性及其与磁性的耦合。
- [[../papers/songEvidenceSinglelayerVan2022]]：在单层 NiI₂ 中证实了范德华多铁性。
- [[../papers/wangTunableD0Topological2025b]]：预测了 In₂NO₂ 单层中可调的 d0 拓扑磁态。
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]：预测了 Sc₂P₂Se₆ 与 ScCrP₂Se₆ 单层的铁电性与多铁性。
- [[../papers/liMonolayerPuckeredPentagonal2022]]：预测了单层褶皱五边形 VTe₂ 作为具有多铁性耦合的二维铁磁半导体。
- [[../papers/liPhaseTransitions2D2021]]：综述了二维材料中的相变及其调控机制。
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：综述了二维材料中的自旋电子学。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：多铁性薄膜领域的经典综述。
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：综述了磁电多铁性材料的最新进展。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：综述了二维范德华材料实现多铁性的挑战与机遇。
- [[../papers/wuElectrostaticGatingIntercalation2022]]：综述了二维材料中的静电门控与插层调控。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：在 MXene Hf₂MnC₂O₂/Sc₂CO₂ 多铁异质结中实现了非易失可开关的半金属性与磁性。
- [[../papers/zhangNonvolatileControlTopological2025]]：在 CrInTe₂/In₂Se₃ 多铁异质结中实现了对拓扑磁性的非易失调控。
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：高通量筛选出具有高转变温度和巨自旋分裂的多铁三元氧化物单层。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-orbit-coupling|自旋-轨道耦合]]（微观推手）
- [[../concepts/easy-axis|易轴]]（能量最低方向）
- [[../entities/Fe3GeTe2|Fe₃GaTe₂]]（具有强垂直各向异性的二维材料）
- [[../entities/CrI3|CrI₃]]（首个二维铁磁体，具强各向异性）

## 🏷️ 专业名词别名

- `magnetic-anisotropy-energy`（concepts）
