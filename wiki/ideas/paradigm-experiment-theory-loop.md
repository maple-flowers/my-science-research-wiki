---
tags: [paradigm, experiment, theory, characterization]
title: 实验-理论闭环 / Experiment-Theory Closed Loop
type: paradigm
status: active
paradigm_id: P06
domain: [condensed-matter-physics, characterization, first-principles]
core_question: 如何让实验证据与理论计算互相校验、逐轮收敛，直到某个物理机制被唯一确定？
method_pipeline: 实验观测（STM/PFM/ARPES）→理论候选机制→计算可观测量→与实验对标→修正模型或补充实验
related_concepts: [ferroelectricity, multiferroicity, charge-density-wave, sliding-ferroelectricity, ferroelasticity]
related_entities: [In2Se3, NiI2]
related_topics: [D02-multiferroic-materials, Z01-computational-materials-design]
papers: [aminiAtomicscaleVisualizationMultiferroicity2024, nakataRobustChargedensityWave2021, xuTwodimensionalFerroelasticityVan2021, songEvidenceSinglelayerVan2022]
updated: 2026-08
entities: [ARPES, PFM, STM]
---

# 实验-理论闭环 / Experiment-Theory Closed Loop

> 科研范式 P06：像"侦探破案"——实验给出线索（图像、谱线、曲线），理论给出解释（能带、能量、机制），两者互相印证，直到案情（机理）水落石出。

## 👵 太奶导读

很多新材料现象，光做实验看不懂"为什么"，光算理论又不知道"是不是真的"。实验-理论闭环就是把两者绑在一起：先用显微镜、光谱、电学测量等手段"看到"现象，再用 DFT 或理论模型解释现象背后的机制，最后回到实验验证理论预言。就像侦探先收集物证，再推理作案手法，最后用推理反推验证物证。这样得出的结论才扎实可信。

## 🧭 范式概述

这个范式的核心逻辑是：**以"实验表征 + 理论计算"双轮驱动，对同一物理现象形成自洽解释**。研究对象覆盖二维铁电/多铁/铁弹、电荷密度波、磁性、拓扑畴等。总体思路是：先制备高质量样品，用多种表征手段（STM、PFM、TEM、XRD、光谱、输运）获取实验证据，再用 DFT/理论建模计算对应性质，将两者对照，若一致则确认机理，若不一致则修正模型或补充实验。这样设计的原因在于：单一手段易误判，实验与理论互相约束才能得到可靠结论。例如 [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] 用原子级成像 + DFT 揭示多铁性，[[../papers/nakataRobustChargedensityWave2021]] 用 STM + DFT 研究单层 1T-TaSe₂ 的 CDW，[[../papers/xuTwodimensionalFerroelasticityVan2021]] 用原位表征 + 第一性原理研究 β'-In₂Se₃ 铁弹性。

## 🔁 研究流程

1. **样品制备**：生长/剥离/合成高质量样品（单层、异质结、薄膜）。
2. **多手段表征**：STM/STEM、PFM、TEM、XRD、拉曼/光谱、输运、磁测量等获取实验证据。
3. **理论建模**：用 DFT/唯象模型计算对应结构、电子、磁性、极化性质。
4. **对照解释**：将实验与理论结果逐项对照，确认或修正机理。
5. **机理确认**：形成自洽解释，必要时设计新实验验证理论预言。

## 🛠️ 核心方法与工具

- **STM/STEM 原子级成像**：直接观察原子结构与电子态（[[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]、[[../papers/nakataRobustChargedensityWave2021]]）。
- **PFM**：纳米尺度极化/畴成像（[[../papers/huangPolarPhaseDomain2019]]）。
- **原位 XRD/变温测量**：追踪相变（[[../papers/xuTwodimensionalFerroelasticityVan2021]]）。
- **DFT 计算**：能带、声子、极化、磁性解释（[[../papers/songEvidenceSinglelayerVan2022]]）。
- **输运/磁电测量**：宏观响应验证（[[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]）。

## ✅ 适用条件

- 现象复杂、单一手段无法定论，需要多证据交叉验证。
- 实验样品可制备，且理论可计算对应性质。
- 关注"是什么 + 为什么"的机理问题。

## ⚠️ 局限与风险

- 实验与理论对照存在尺度/条件差异，需谨慎匹配。
- 样品质量、缺陷、衬底效应可能干扰结论。
- 理论模型简化可能遗漏真实机制。
- 闭环周期长、成本高。

## 📚 代表论文 (Representative Papers)

- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]：原子级成像 + DFT 揭示多铁性机制。
- [[../papers/nakataRobustChargedensityWave2021]]：STM + DFT 研究单层 1T-TaSe₂ CDW。
- [[../papers/xuTwodimensionalFerroelasticityVan2021]]：原位表征 + 第一性原理研究二维铁弹性。
- [[../papers/songEvidenceSinglelayerVan2022]]：实验证据 + DFT 确认单层范德华铁电。

## 🗂️ 覆盖论文全集 (All Covered Papers)

- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]
- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]
- [[../papers/gongAbsenceCriticalThickness2023]]
- [[../papers/hallEnvironmentalControlCharge]]
- [[../papers/huangPolarPhaseDomain2019]]
- [[../papers/Jin2015studying]]
- [[../papers/kawakamiChargedensityWaveAssociated2023]]
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]
- [[../papers/lvUnconventionalHystereticTransition2022]]
- [[../papers/majumdarInterplayChargeDensity2020]]
- [[../papers/naguib25thAnniversaryArticle2013a]]
- [[../papers/nakataRobustChargedensityWave2021]]
- [[../papers/nicholsonUniaxialStraininducedPhase2021]]
- [[../papers/niuDirectVisualizationLargeScale2021]]
- [[../papers/pedramraziManipulatingTopologicalDomain2019]]
- [[../papers/Petkov2020hierarchy]]
- [[../papers/petkovStructureIntercalatedCs2002]]
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]
- [[../papers/shuTwoDimensionalBlackArsenic2020]]
- [[../papers/songEvidenceSinglelayerVan2022]]
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]
- [[../papers/wangFormationMechanismTwin2019]]
- [[../papers/wernetSpectroscopicCharacterizationMicroscopic2005]]
- [[../papers/wongEvidenceMetallic1T]]
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]
- [[../papers/yanagizawaSwitchingChargedensityWave2023]]
- [[../papers/xuTwodimensionalFerroelasticityVan2021]]

## 🔗 关联概念、实体与主题 (Related Concepts, Entities & Topics)

- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/multiferroicity|多铁性]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/sliding-ferroelectricity|滑移铁电]]
- [[../concepts/ferroelasticity|铁弹性]]
- [[../entities/ARPES|角分辨光电子能谱]]
- [[../entities/STM|扫描隧道显微镜]]
- [[../entities/PFM|压电力显微镜]]
- [[../entities/In2Se3|In₂Se₃]]
- [[../entities/NiI2|NiI₂]]
- [[../topics/D02-multiferroic-materials|多铁性材料]]
- [[../topics/Z01-computational-materials-design|材料模拟计算设计]]

## 📈 生命周期日志

- **2026-08-15**: active — 提炼自 30 篇实验-理论闭环类论文（含原子级成像+DFT、原位表征+第一性原理等）。
