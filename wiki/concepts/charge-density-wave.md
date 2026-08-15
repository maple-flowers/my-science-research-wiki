---
tags: [concept, charge-density-wave, 2D-materials]
title: 电荷密度波 / Charge Density Wave (CDW)
type: concept
status: mature
domain: [condensed-matter-physics, charge-density-wave]
mechanism: 费米面嵌套驱动的电子密度和晶格周期性调制
related_concepts: [fermi-surface-nesting, peierls-transition, electron-phonon-coupling]
papers: [cossuStackingChargedensityWaves2024, Inosov2008fermi, kawakamiChargedensityWaveAssociated2023, yanagizawaSwitchingChargedensityWave2023, Barnett2006coexistence, CastroNeto2001charge, Chen2019superconductivity, Islam2025enhancement, Johannes2008fermi, Kang2012dimer, Koley2020charge, Laverock2005fermi, Makogon2012wave, Petkov2020hierarchy, chenFerromagneticNonmagnetic1T2022, chowdhuryReviewTheoreticalComputational, gorkovStrongElectronlatticeCoupling2012, guanRecentProgressTwoDimensional2020, hallEnvironmentalControlCharge, kaurRecentAdvancesTheoretical2025a, kimObservationPhaseTransition1997, krishnamurthiSpinChargeDensity2020, lezoualchStudyChargeDensity, liMonolayerPuckeredPentagonal2022, liPhaseTransitions2D2021, lvUnconventionalHystereticTransition2022, majumdarInterplayChargeDensity2020, mostovoyMultiferroicsDifferentRoutes2024, nakataRobustChargedensityWave2021, nicholsonUniaxialStraininducedPhase2021, petkovStructureIntercalatedCs2002, sunSlidingFerroelectricityTwodimensional2025, tangCombiningIntrinsicSlidinginduced2025, wangFormationMechanismTwin2019, wongEvidenceMetallic1T, wuElectrostaticGatingIntercalation2022, zhengAnisotropicSuperconductivityTwodimensional2025]
updated: 2026-08
---

# 电荷密度波 / Charge Density Wave (CDW)

电荷密度波 (Charge Density Wave, CDW) 是低维固体体系中一种典型的集体量子现象。它表现为电子电荷密度的空间周期性调制，通常伴随着晶格原子位置的周期性畸变 (Periodic Lattice Distortion, PLD)。这种状态通常在低温下发生，其驱动力往往源于费米面嵌套 (Fermi Surface Nesting) 导致的一维或二维不稳定性。

## 👵 太奶导读

好孩子，这“电荷密度波”听着玄乎，其实道理挺像咱们在农村晒场上撒米。
本来你把米匀匀实实地铺开在地上（这就是材料里均匀分布的电子），可要是这地儿有点儿不平，或者米粒之间有点儿奇怪的吸引力，这些米就会自动排成一行行、一垄垄的，有的地方米多，有的地方米少（这就是电荷密度波）。
最神奇的是，这些米粒排好队后，连地上的土也会跟着动，原子也得乖乖移个位来配合。这种现象一般得在特别冷的条件下才能看到，温度一高，米粒就又乱跑了。

## 🏗️ 结构概览

在过渡金属硫族化合物 (TMDs) 中，CDW 通常表现为超晶格结构。例如在 2H-NbSe₂ 中，CDW 呈现为 3×3 的超结构。

![图：2H-NbSe₂ 中的单层 CDW 模式 (HC, CC, HX)](../../raw/figures/cossuStackingChargedensityWaves2024/fig_1_Q8LV7XLD.png)
*   **看图要点**：图中展示了单层中三种最稳定的 CDW 模式：HC (hollow-centered)、CC (chalcogen-centered) 和 HX (hexagonal)。这些模式反映了原子在 CDW 相变发生后，相对于原始格点的位移特征。
*   **来源**：[[../papers/cossuStackingChargedensityWaves2024]] -> [[../figures/heterostructures-stacking|异质结与层间堆积]]

## 🧩 物理机制与费米面嵌套

CDW 的形成传统上由 Peierls 不稳定性解释。在低维体系中，当费米面存在平行片段时，系统响应函数 (Lindhard 函数) 在特定波矢 $q$ 处会发生发散。

![图：2H-NbSe₂ 与 CDW 构型的态密度耗尽（赝能隙）](../../raw/figures/cossuStackingChargedensityWaves2024/fig_3_IFCX25A7.png)
*   **关键特征**：在费米能级 $E_F$ 附近出现了态密度的显著耗尽，形成所谓的“赝能隙”。这表明 CDW 的形成伴随着体系总能量的降低，是电子态重新分布以稳定结构的表现。
*   **来源**：[[../papers/cossuStackingChargedensityWaves2024]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

Inosov 等人的研究指出，虽然费米面嵌套是重要诱因，但嵌套矢量的强度并不直接决定转变温度 $T_{CDW}$，电子-声子耦合 (Electron-Phonon Coupling) 的强弱在其中扮演了更关键的角色。

## 📚 相关论文 (Related Papers)

- [[../papers/cossuStackingChargedensityWaves2024]]：探讨了双层 NbSe₂ 中 CDW 的垂直堆叠效应对电子指纹的影响。
- [[../papers/Inosov2008fermi]]：通过 ARPES 实验验证了 TMDs 中费米面嵌套矢量的非公度性和普适性。
- [[../papers/kawakamiChargedensityWaveAssociated2023]]：研究了 CDW 相关的电子性质及其在不同相中的演化。
- [[../papers/yanagizawaSwitchingChargedensityWave2023]]：演示了 CDW 态的可控切换。
- [[../papers/Barnett2006coexistence]]
- [[../papers/CastroNeto2001charge]]
- [[../papers/Chen2019superconductivity]]
- [[../papers/Islam2025enhancement]]
- [[../papers/Johannes2008fermi]]
- [[../papers/Kang2012dimer]]
- [[../papers/Koley2020charge]]
- [[../papers/Laverock2005fermi]]
- [[../papers/Makogon2012wave]]
- [[../papers/Petkov2020hierarchy]]
- [[../papers/chenFerromagneticNonmagnetic1T2022]]
- [[../papers/chowdhuryReviewTheoreticalComputational]]
- [[../papers/gorkovStrongElectronlatticeCoupling2012]]
- [[../papers/guanRecentProgressTwoDimensional2020]]
- [[../papers/hallEnvironmentalControlCharge]]
- [[../papers/kaurRecentAdvancesTheoretical2025a]]
- [[../papers/kimObservationPhaseTransition1997]]
- [[../papers/krishnamurthiSpinChargeDensity2020]]
- [[../papers/lezoualchStudyChargeDensity]]
- [[../papers/liMonolayerPuckeredPentagonal2022]]
- [[../papers/liPhaseTransitions2D2021]]
- [[../papers/lvUnconventionalHystereticTransition2022]]
- [[../papers/majumdarInterplayChargeDensity2020]]
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]
- [[../papers/nakataRobustChargedensityWave2021]]
- [[../papers/nicholsonUniaxialStraininducedPhase2021]]
- [[../papers/petkovStructureIntercalatedCs2002]]
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]]
- [[../papers/wangFormationMechanismTwin2019]]
- [[../papers/wongEvidenceMetallic1T]]
- [[../papers/wuElectrostaticGatingIntercalation2022]]
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/fermi-surface-nesting|费米面嵌套]]（驱动机制）
- [[../concepts/peierls-instability]]（经典物理图像）
- [[../entities/TMDs|TMDs]]（典型载体材料）
- [[../entities/NbSe2|NbSe₂]]（明星 CDW 材料）
