---
tags: [concept, ferroelectricity, 2d-materials]
title: 滑动铁电性 / Sliding Ferroelectricity
type: concept
status: mature
domain: [ferroelectricity, 2d-materials]
mechanism: 通过范德华层间位移打破反演对称性并产生垂直于层面的电极化
related_concepts: [dipole-locking, moire-superlattice, interlayer-polarization-coupling, stacking-engineered-ferroelectricity, depolarization-field]
papers: [huangTwodimensionalIn2Se3Rising2022, wuSlidingFerroelectricity2D2021a, feiFerroelectricSwitchingTwodimensional2018a, FerroelectricityMultiferroicityAtomic2023, RecentAdvancesGrowth2025, bhowalPolarMetalsPrinciples2023b, chenStrongSlidingFerroelectricity2024, guanRecentProgressTwoDimensional2020, guoAdvancesTwodimensionalFerroelectric2025, hanTunableSlidingFerroelectricity2025, heSwitchingTwodimensionalSliding2025, heUltrafastSwitchingDynamics2024, huProgressProspectsLowdimensional2019, huangPolarPhaseDomain2019, kaurRecentAdvancesTheoretical2025a, kimObservationPhaseTransition1997, liPhaseTransitions2D2021, martinThinfilmFerroelectricMaterials2016, miaoMagneticFerroelectricMetal2024, neumayerCompetingPolarPhases2025, shenEmergenceMultipleFerroelectric2025, sunSlidingFerroelectricityTwodimensional2025, tangCombiningIntrinsicSlidinginduced2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, xunCoexistingMagnetismFerroelectric2024, zhangEmergingFrontiersTwodimensional2025, zhaoOpticalFingerprintsTwodimensional2024]
updated: 2026-08
---

# 滑动铁电性 / Sliding Ferroelectricity

滑动铁电性（Sliding Ferroelectricity）是一种存在于范德华层状材料中的新型铁电机制。它的核心特征是：**通过层与层之间的侧向位移（Sliding）来打破空间反演对称性，从而在垂直于层面的方向上感生出自发极化（Out-of-plane Polarization）**。它与传统铁电的根本区别在于，极化不是来源于单胞内原子的位移，而是来源于层间相对位置（堆垛构型）的变化。

## 👵 太奶导读

太奶啊，您就把这材料想象成两层平铺好的**花格子布**。原本这两层布叠得严丝合缝，正反看都一模一样，没啥特别的。但如果您用手轻轻这么**一搓**（层间滑动），让上面那层布错开一丁点儿位移，这两层布叠出来的花纹就不再对称了。在咱们物理上，这一"错位"，电荷分布就不平衡了，就像是一排排整齐的小箭头齐刷刷地指向了上方或下方，这就产生了"铁电性"。这可比在布料里搬动一颗颗线头（原子位移）要省力得多，所以这种材料做成的存储器速度特别快、特别省电。

## 🧩 什么是滑动铁电性？

在传统的铁电体（如 $BaTiO_3$）中，铁电性起源于原子在单胞内部的微小位移。而在二维范德华材料中，由于层间作用力非常弱（范德华力），层与层之间可以发生相对滑动。

- **物理起源**：当两层原本中心对称的单层材料（如双层 $h\text{-BN}$）以特定的方式堆叠（如 $AB$ 堆叠）时，其重叠部分的电荷分布会因为不对称而发生垂直方向的偏移。
- **对称性破缺**：如果我们将上层相对于下层滑动一个特定的矢量（例如从 $AB$ 滑动到 $BA$），体系的垂直极化方向就会发生 $180^\circ$ 的翻转。
- **纯电子起源**：滑动铁电的极化源于不对称堆叠导致的层间电荷转移与轨道畸变，是一种纯电子效应，而非离子位移效应（[[../papers/kaurRecentAdvancesTheoretical2025a]]）。
- **与传统铁电的区别**：传统铁电是"内生位移"，滑动铁电是"层间错位"。这使得铁电性在单层或双层的物理极限下依然能稳定存在，极大地挑战了传统的"临界厚度"理论。

## ⚡ 核心机制：横向滑动驱动垂直极化

滑动铁电性最神奇的地方在于**面内位移与面外电信号的耦合**。

1. **侧向滑动 (Lateral Shift)**：在外电场或机械力的驱动下，层间发生微小的剪切运动（通常为亚埃级横向位移）。
2. **偶极子翻转 (Dipole Switching)**：这种横向位移改变了层间原子的重叠模式，迫使电荷在垂直方向上重新分布，从而实现了极化的翻转。
3. **互锁特征 (Locking)**：在某些材料（如 $\alpha\text{-}In_2Se_3$）中，这种滑动与面内的自发极化是"锁死"的，即翻转面外极化的过程本质上就是驱动层间发生剪切滑移的过程。

![图：In2Se3 极化反转的三步协同滑动路径](../../raw/figures/huangTwodimensionalIn2Se3Rising2022/fig_8_EC7NT7IT.png)
- **关键特征**：图中的三步路径清晰地展示了层间滑动（Sliding）是如何作为中间过程，将一种极化状态转换为另一种的。其翻转势垒（0.066 eV）远低于直接跳跃路径。
- **来源**：[[../papers/huangTwodimensionalIn2Se3Rising2022]] -> [[../figures/crystal-structures-bulk|晶体结构]]

## 🗺️ 三类实现路径

滑动铁电性可以通过三种主要途径实现（[[../papers/sunSlidingFerroelectricityTwodimensional2025]]）：

| 路径 | 原理 | 典型体系 |
| :--- | :--- | :--- |
| 3R 菱方堆叠 | 利用非中心对称的 3R 堆垛构型 | 3R-MoS₂、γ-InSe、GaSe、ReS₂ |
| 层间扭转 | 两层以特定扭转角堆叠 | 扭转双层石墨烯、扭转 TMDs |
| 莫尔超晶格 | 周期扭转/晶格失配形成莫尔势 | 莫尔铁电畴阵列 |

## 🔬 典型材料与参数

- **双层 $h\text{-BN}$**：原本是非铁电的，但在特定的堆叠（如 Bernal 堆叠）下展现出强烈的滑动铁电性，极化可由表面电荷观测验证。
- **$\alpha\text{-}In_2Se_3$**：目前研究最成熟的二维滑动铁电体，其翻转势垒约 0.066 eV，滑动路径远低于直接翻转路径。
- **HgI₂**：强滑动铁电体，双层极化可达 0.11 μC/cm²（屏蔽电荷积分法），翻转势垒 24.65 meV/f.u.。
- **ReS₂ 多层**：极化随层数由 2 增至 7 从 0.07 pC/m 升至 0.68 pC/m，势垒由 17 meV 升至 100 meV。
- **WTe₂ 双层/三层**：层间堆叠失配产生面外极化，翻转能垒约 0.29 eV/f.u.。

## 🔬 物理参数表

| 属性 | 典型数值 | 体系与来源 |
| :--- | :--- | :--- |
| 翻转势垒 | 0.066 eV | α-In₂Se₃ 三步滑动路径（[[../papers/huangTwodimensionalIn2Se3Rising2022]]） |
| 双层极化 | 0.11 μC/cm² | HgI₂ 屏蔽电荷积分法（[[../papers/chenStrongSlidingFerroelectricity2024]]） |
| 翻转势垒 | 24.65 meV/f.u. | HgI₂（[[../papers/chenStrongSlidingFerroelectricity2024]]） |
| 双层极化 | 0.07 pC/m；势垒 17.1 meV | 1T′-ReS₂（[[../papers/kaurRecentAdvancesTheoretical2025a]]） |
| 多层极化（2→7 层） | 0.07 → 0.68 pC/m；17 → 100 meV | ReS₂（[[../papers/kaurRecentAdvancesTheoretical2025a]]） |
| 单层参照极化 | 6.19 pC/m | GaSe（[[../papers/sunSlidingFerroelectricityTwodimensional2025]]） |

> 注：上表为 DFT/实验典型数值，适用对象与条件已在数值中标注，详细来源见 📚 相关论文 节。

## 🧭 近邻概念辨析

- **与传统位移铁电的区别**：传统铁电（如 $BaTiO_3$、$HfO_2$）极化来源于单胞内阳离子相对阴离子的位移，受临界厚度限制；滑动铁电来源于层间相对位移，在单层/双层极限仍可稳定。
- **与偶极锁定 (dipole-locking) 的区别**：偶极锁定指面内与面外极化自由度的互锁（如 α-In₂Se₃），是滑动铁电的一种特殊表现；滑动铁电本身不要求面内偶极存在（如 h-BN 双层无面内偶极）。
- **与莫尔铁电的区别**：莫尔超晶格铁电是扭转/失配周期势下的滑动铁电空间调制，可视为滑动铁电在周期结构中的推广。
- **与层间极化耦合的区别**：滑动铁电关注"单次层间位移如何产生/翻转极化"这一机制；层间极化耦合关注多层体系中相邻层极化的相互作用（逐层翻转、多态），是滑动铁电在多层极限下的集体行为。

## 📚 相关论文 (Related Papers)

- [[../papers/wuSlidingFerroelectricity2D2021a]]：系统阐述了滑动铁电性的通用物理图像与未来机遇。
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]：讨论了滑动机制在 In2Se3 器件中的应用，给出三步协同滑动翻转路径。
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]：实验上观测到了双层 WTe₂ 中的滑动翻转。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：系统综述滑动铁电的原理、材料谱系、表征与器件应用。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：从理论综述角度系统整合了滑动铁电的电子起源、材料库与调控机制，提出"极化-能垒"性能地图。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：从理论分析角度梳理了「Strong Sliding Ferroelectricity and Interlayer Sliding Controllable Spintronic Effect in Two-Dimensional HgI₂ Layers」。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：从综述角度梳理了「Ferroelectricity and multiferroicity down to the atomic thickness」。
- [[../papers/RecentAdvancesGrowth2025]]：从综述角度梳理了二维铁电材料的最新进展与生长方法。
- [[../papers/bhowalPolarMetalsPrinciples2023b]]：从综述角度梳理了「极性金属：原理与展望」。
- [[../papers/guanRecentProgressTwoDimensional2020]]：从综述角度梳理了「Recent Progress in Two‐Dimensional Ferroelectric Materials」。
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]：从综述角度梳理了「二维铁电材料的研究进展」。
- [[../papers/hanTunableSlidingFerroelectricity2025]]：从理论分析角度梳理了「Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers」。
- [[../papers/heSwitchingTwodimensionalSliding2025]]：从实验研究角度梳理了「机械弯曲切换二维滑动铁电体」。
- [[../papers/heUltrafastSwitchingDynamics2024]]：从实验研究角度梳理了滑动铁电体的超快翻转动力学。
- [[../papers/huProgressProspectsLowdimensional2019]]：从综述角度梳理了「低维多铁性材料的研究进展与展望」。
- [[../papers/huangPolarPhaseDomain2019]]：从实验研究角度梳理了「Polar and phase domain walls with conducting interfacial states in a Weyl semimetal MoTe2」。
- [[../papers/kimObservationPhaseTransition1997]]：从实验研究角度梳理了 h-BN 相关的堆垛与相变观测背景。
- [[../papers/liPhaseTransitions2D2021]]：从综述角度梳理了「二维材料中包括滑动铁电在内的多自由度相变」。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：从综述角度梳理了「Thin-Film Ferroelectric Materials and Their Applications」。
- [[../papers/miaoMagneticFerroelectricMetal2024]]：从理论分析角度梳理了「Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding」。
- [[../papers/neumayerCompetingPolarPhases2025]]：从综述角度梳理了「二维铁电过渡金属硫代和硒酸盐中的竞争极性相」。
- [[../papers/shenEmergenceMultipleFerroelectric2025]]：从实验研究角度梳理了「多层黑磷中多铁电态的出现」。
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]]：从理论分析角度梳理了「Combining intrinsic and sliding-induced ferroelectricity」的多态铁电概念。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：从综述角度梳理了二维范德华多铁材料的设计策略。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：从实验研究角度梳理了室温二维多铁的进展。
- [[../papers/xunCoexistingMagnetismFerroelectric2024]]：从实验研究角度梳理了「Coexisting magnetism and ferroelectricity」相关体系。
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]：从综述角度梳理了「二维滑动铁电体的新兴前沿」。
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：从实验研究角度梳理了二维铁电体的光学指纹表征。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dipole-locking|偶极锁定]]
- [[../concepts/moire-superlattice|莫尔超晶格]]
- [[../concepts/interlayer-polarization-coupling|层间极化耦合]]
- [[../concepts/stacking-engineered-ferroelectricity|堆垛工程铁电]]
- [[../concepts/depolarization-field|退极化场]]
- [[../entities/In2Se3|In2Se3]]
- [[../entities/HgI2|HgI2]]
- [[../entities/ReS2|ReS2]]
- [[../entities/WTe2|WTe2]]
