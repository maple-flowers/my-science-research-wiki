---
tags: [concept, nonlinear-optics, spectroscopy]
title: 二次谐波产生 / Second-Harmonic Generation (SHG)
type: concept
status: mature
domain: [nonlinear-optics, solid-state-physics, materials-characterization]
mechanism: 两个频率为 ω 的光子在非中心对称介质中相互作用，产生一个频率为 2ω 的光子
related_concepts: [inversion-symmetry-breaking, two-photon-absorption, nonlinear-susceptibility, sliding-ferroelectricity]
papers: [zhaoOpticalFingerprintsTwodimensional2024, songEvidenceSinglelayerVan2022, gaoGiantChiralMagnetoelectric2024a, pengStrainEngineering2D2020]
updated: 2026-08
---

# 二次谐波产生 / Second-Harmonic Generation (SHG)

二次谐波产生（Second-Harmonic Generation, SHG）是一种非线性光学过程。在这种过程中，两个频率相同的光子与非线性材料相互作用，并结合成一个新的光子，其能量（频率）是原始光子的两倍，波长则是原始光子的一半。

##  Grandma-style / 奶奶导读

太奶啊，您就把这想象成一个**“变色魔镜”**。您拿两束一样颜色的红光照在上面，这镜子不仅能反射光，还能把这两束红光“捏”在一起，吐出一束绿光来（频率翻倍）。但这个镜子很挑剔，它必须得是**“心长歪了”**的材料（即原子排列不左右对称、没有反演中心）才能显灵。如果这材料里的原子排得太整齐、四平八稳的，这魔镜就失效了。所以咱们科学家就用这招来检查材料的“心”有没有长歪，比如看看它有没有铁电性（极化方向），或者是两层布有没有搓位（滑动铁电）。

## 🏗️ 结构与原理概览

SHG 属于二阶非线性光学效应，其极化强度 $P^{(2)}$ 可表示为：
$$ P^{(2)}(2\omega) = \epsilon_0 \chi^{(2)} E(\omega) E(\omega) $$
其中 $\chi^{(2)}$ 是二阶非线性极化率张量。

![图：二维层间滑移多铁材料的斜入射 SHG 探测原理](../../raw/figures/zhaoOpticalFingerprintsTwodimensional2024/fig_4_H4MUSGVJ.png)
*   **看图要点**：图中展示了 P 偏振光以倾角入射，通过收集不同方位角 $\phi$ 下的 SHG 强度，形成独特的“六瓣花”图案。这种图案的形状和偏转角度直接对应了材料内部的铁电/磁性状态。
*   **来源**：[[../papers/zhaoOpticalFingerprintsTwodimensional2024]] -> [[../figures/optical-spectra|光学光谱]]

## 🧩 对称性敏感性：反演对称破缺的“金标准”

SHG 最核心的用途是探测**空间反演对称性破缺（Inversion Symmetry Breaking）**。
*   **中心对称抵消**：在具有中心对称性的介质中（如大部分普通液体或立方晶格），二阶非线性系数 $\chi^{(2)}$ 在空间反演操作下会变号，从而导致宏观 SHG 信号为零。
*   **极性序探测**：一旦材料产生铁电极化（如 [[../concepts/sliding-ferroelectricity|滑动铁电]]）或磁致反演对称破缺，SHG 信号会急剧增强。在单层 [[../entities/NiI2|NiI2]] 中，科学家正是利用 SHG 在 20 K 以下的突然增强，证实了其二维多铁性的存在 [[../papers/songEvidenceSinglelayerVan2022]]。

## 🔬 SHG 的分类与“光学指纹”

在多铁性材料中，SHG 张量可以进一步分解以区分不同的物理序：
1.  **T-偶分量 (i-type)**：时间反演对称下不变的分量，通常对应晶格的结构极化（铁电序）。
2.  **T-奇分量 (c-type)**：时间反演下变号的分量，源于材料的磁序。
*   **案例分析**：在双层 [[../entities/VSe2|VSe2]] 和 [[../entities/MnBi2Te4|MnBi2Te4]] 中，四种不同的多铁态（极化翻转或磁矩翻转）会改变 $\chi^{(2)}$ 不同分量的相对相位和符号，从而产生截然不同的偏振依赖“光学指纹” [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]。

## 📈 实验技术与波长选择

*   **避开共振**：为了获得纯粹的电偶极（Electric-Dipole, ED）贡献，实验中通常选择低于带隙的激发波长。例如，在 NiI2 实验中，使用 991 nm（~1.25 eV）激发以避开磁偶极（MD）贡献的干扰 [[../papers/songEvidenceSinglelayerVan2022]]。
*   **偏振分辨 (RA-SHG)**：通过旋转样品的方位角或改变入射/探测光的偏振方向，可以绘制出旋转各向异性图案，从而确定晶体的点群对称性。

## 📚 相关论文 (Related Papers)

- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：利用 SHG 识别二维层间滑移多铁材料的四个磁电状态。
- [[../papers/songEvidenceSinglelayerVan2022]]：利用 SHG 作为单层 vdW 多铁性存在的关键实验证据。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：利用时间分辨 SHG (tr-SHG) 探测电磁振子的超快动力学，揭示巨手性磁电耦合。
- [[../papers/pengStrainEngineering2D2020]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/inversion-symmetry-breaking|反演对称破缺]]
- [[../concepts/sliding-ferroelectricity|滑动铁电]]
- [[../concepts/multiferroicity|多铁性]]
- [[../entities/NiI2|二碘化镍 (NiI2)]]
- [[../entities/VSe2|二硒化钒 (VSe2)]]
