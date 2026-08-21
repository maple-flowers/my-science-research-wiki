---
tags: [concept]
title: 'moire-superlattice'
type: concept
status: developing
papers: ['FerroelectricityMultiferroicityAtomic2023', 'aminiAtomicscaleVisualizationMultiferroicity2024', 'chowdhuryReviewTheoreticalComputational', 'cossuStackingChargedensityWaves2024', 'duUltrasensitiveOptoelectronicBiosensor2025', 'guanRecentProgressTwoDimensional2020', 'guoAdvancesTwodimensionalFerroelectric2025', 'hallEnvironmentalControlCharge', 'hanTunableSlidingFerroelectricity2025', 'heUltrafastSwitchingDynamics2024', 'huProgressProspectsLowdimensional2019', 'kaurRecentAdvancesTheoretical2025a', 'liPhaseTransitions2D2021', 'pengStrainEngineering2D2020', 'shenEmergenceMultipleFerroelectric2025', 'sunSlidingFerroelectricityTwodimensional2025', 'wuElectrostaticGatingIntercalation2022', 'wuSlidingFerroelectricity2D2021a', 'yangRipplingFerroicPhase2021', 'yangStrainEngineeringTwodimensional2021', 'zhangEmergingFrontiersTwodimensional2025']
updated: 2026-08-18
---

# moire-superlattice

莫尔超晶格（moire superlattice）指**两层晶格常数或转角略有差异的二维材料堆叠时，因晶格失配/旋转产生的大周期干涉图案**。莫尔势可重构电子能带，形成平带、层间激子、关联态（超导、Mott 绝缘体、铁电）与拓扑态，是"转角电子学"（twistronics）的物理基础，也是本库二维材料研究的核心主题之一。

## 👵 太奶导读

太奶啊，把两层同样花纹的纱窗叠在一起，稍微错开一点角度，就会看到一圈圈大大的"水波纹"图案——这就是莫尔条纹。把两层原子纸叠出莫尔图案后，原子层的周期性被"放大"，电子看到的是一种全新的大格子，能带被压扁成"平带"。平带里的电子"挤挤挨挨、相互作用强"，于是变出超导、绝缘、铁电、磁性等一大堆神奇性质。

## 🧩 核心内容与机制 (Core Content)

- **莫尔周期**：由晶格失配 δ 与转角 θ 决定：λ ≈ a/(√(δ²+θ²))；小转角产生大周期莫尔势（本库 h-BN、TMD、石墨莫尔体系论文）。
- **平带与关联态**：特定转角（魔角）处平带（flat-band）出现，电子关联增强，产生超导、Mott 绝缘、铁磁等（本库魔角石墨、莫尔 TMD 相关论文）。
- **莫尔铁电**：滑动/层间堆垛变化产生铁电极化（sliding-ferroelectricity），本库 h-BN/TMD 莫尔铁电与铁电光伏为核心案例。
- **层间激子与莫尔激子**：莫尔势捕获激子，形成莫尔激子阵列（本库 WSe₂/WS₂ 莫尔激子论文）。
- **拓扑态**：莫尔系统可实现拓扑平带与分数化量子态（本库拓扑莫尔态相关）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superlattice|超晶格]]：莫尔超晶格是超晶格特例。
- [[../concepts/flat-band|平带]]：莫尔能带的关键特征。
- [[../concepts/interlayer-coupling|层间耦合]]：莫尔物理的微观纽带。
- [[../concepts/sliding-ferroelectricity|滑动铁电]]：莫尔体系铁电性。
- [[../concepts/2d-materials|二维材料]]：莫尔超晶格的平台。

## 📚 相关论文 (Related Papers)

- [[../papers/FerroelectricityMultiferroicityAtomic2023]] — Ferroelectricity and multiferroicity down to the atomic thickness
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] — Atomic-Scale Visualization of Multiferroicity in Monolayer NiI2
- [[../papers/chowdhuryReviewTheoreticalComputational]] — Computational Methods for Charge Density Waves in 2D Materials
- [[../papers/cossuStackingChargedensityWaves2024]] — Stacking of charge-density waves in 2H-NbSe₂ bilayers
- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]] — Ultrasensitive optoelectronic biosensor arrays based on twisted bilayer graphene superlattice
- [[../papers/guanRecentProgressTwoDimensional2020]] — Recent Progress in Two‐Dimensional Ferroelectric Materials
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]] — Advances in two-dimensional ferroelectric materials
- [[../papers/hallEnvironmentalControlCharge]] — Environmental Control of Charge Density Wave Order in Monolayer 2H-TaS₂
- [[../papers/hanTunableSlidingFerroelectricity2025]] — Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers
- [[../papers/heUltrafastSwitchingDynamics2024]] — Ultrafast switching dynamics of the ferroelectric order in stacking-engineered ferroelectrics
- [[../papers/huProgressProspectsLowdimensional2019]] — Progress and prospects in low‐dimensional multiferroic materials
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials
- [[../papers/pengStrainEngineering2D2020]] — Strain engineering of 2D semiconductors and graphene: from strain fields to band-structure tuning and photonic applications
- [[../papers/shenEmergenceMultipleFerroelectric2025]] — Emergence of multiple ferroelectric states in multilayer black phosphorus
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications
- [[../papers/wuElectrostaticGatingIntercalation2022]] — Electrostatic gating and intercalation in 2D materials
- [[../papers/wuSlidingFerroelectricity2D2021a]] — Sliding ferroelectricity in 2D van der Waals materials: Related physics and future opportunities
- [[../papers/yangRipplingFerroicPhase2021]] — Rippling Ferroic Phase Transition and Domain Switching In 2D Materials
- [[../papers/yangStrainEngineeringTwodimensional2021]] — Strain engineering of <scp>two‐dimensional</scp> materials: Methods, properties, and applications
- [[../papers/zhangEmergingFrontiersTwodimensional2025]] — Emerging frontiers in two-dimensional sliding ferroelectrics
