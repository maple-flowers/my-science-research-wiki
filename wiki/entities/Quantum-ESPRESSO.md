---
tags: [entity, berry-phase, berry-connection, modern-polarization-theory, wannier-function, born-effective-charge, charge-density-wave, 2d-materials, density-functional-theory, electron-phonon-coupling, fermi-surface-nesting]
title: Quantum-ESPRESSO
type: entity
status: developing
year: 1993
papers: [king-smithTheoryPolarizationCrystalline1993, lezoualchStudyChargeDensity, tangGridbasedBaderAnalysis2009, yanagizawaSwitchingChargedensityWave2023, zhengAnisotropicSuperconductivityTwodimensional2025, chowdhuryReviewTheoreticalComputational]
updated: 2026-08-18
---

# Quantum-ESPRESSO

本文档围绕 **Quantum-ESPRESSO** 汇集 6 篇论文的证据，覆盖其结构、物性与机制等多方面信息。

## 👵 太奶导读

乖孙，这一条讲的是「Quantum-ESPRESSO」，由多篇论文的证据共同支撑。
一句话记住它的发现：: 建立了绝对极化差值与“相位弛豫图”的等效性。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：晶体极化的实验有广泛应用在铁电、压电中，但原子论框架下直接计算“极化变化量”长期未解，J*没有以协变方式定义“绝对极化”，导致形式化理论与现代多体第一性原理计算脱节。本文旨在提供可实现的理论框架。
- **核心问题**：主要在于为理论与计算摇篮间的鸿沟架桥——如何从原子论层面严格推导一个在实际DFT基计算机语境下能用局部价波函数**数值计算**并限定“任意相位”干扰下的的极化变化?
- **主要结论**：: 建立了绝对极化差值与“相位弛豫图”的等效性；“规范自由度”的剩余被化为`归一化模`（量子）；实际数值优于。并与线性响应理论计算结果偏差<5，进而明确说明电子响应对综合死电物理的特征独立。；单层1T-TiTe₂中的2×2 CDW在电子和空穴载流子精确补偿（有效零掺杂）的极窄范围内出现。该CDW的驱动力是费米面嵌套，即布里渊区Γ点处的内空穴口袋与M点处的椭球型电子口袋，通过2×2 CDW矢量实现部分嵌套。通过控制外延温度或沉积钾原子来改变载流子浓度，可以方便地实现CDW的开与关。；Cu3(CO)6单层是一种由电-声子耦合驱动的BCS超导体，其特征为单能隙、各向异性超导，临界温度Tc达16.5 K。其超导电性主要由费米面附近的Cu dxy,x2-y2和O s+px,y电子态与低能区（<40 meV）的Cu、O原子振动模式之间的强耦合所致，电-声子耦合强度λ=0.72。费米面嵌套效应是增强该耦合的重要因素。；1) 通过“电子温度”和“应力工程”方法，DFT可以有效模拟CDW相变。2) 首次通过计算清晰识别并解释了TaSe₂中振幅模和相位模的原子振动图像。3) 揭示了TaS₂和TaSe₂在CDW行为上的显著差异（如非公度性、相变模式）。4) 阐明了维度降低通过改变费米面拓扑、削弱层间耦合等方式，显著调控CDW的稳定性、结构以及与其他量子相（如超导）的竞争，并提出了一个基于离子电荷转移、电子-声子耦合和波函数空间扩展的统一相图框架。
- **领域贡献**：为后续边界IP（现代极化理论）到达原始发初端点；提供了α标准处理方法；发表了现代实现对“自发极化极值算法”的评价基石（如现代铁电材料构型研究），同时引入相位几何的概念影响到拓扑物理。；提供了一种通过载流子调谐来钉扎原子层厚度TMD材料中CDW机制的有效方法。为费米面嵌套驱动的CDW理论提供了清晰、系统的实验范例，并建立了一个可通过掺杂、栅压等手段高度调控其电子基态的二维材料平台。；1. 在实验已合成的2D-MOF中预测了具有可观Tc的超导电性，填补了该体系的研究空白。2. 通过求解各向异性Migdal-Eliashberg方程，精确描绘了超导能隙的各向异性分布，为理解2D-MOFs中的超导机制提供了更精细的理论模型。3. 将超导驱动力明确归因于特定原子（Cu、O）的低能振动模式，并揭示了费米面嵌套的深层作用，为后续的材料设计与性能调控指明了方向。；本文的主要贡献在于：(1) 系统总结了二维CDW材料计算的挑战与解决方案，具有极高的教学价值；(2) 通过对比研究，为DFT计算参数的选择提供了基准；(3) 将光谱学特征与原子级微观动力学直接联系，深化了对CDW集体激发的理解；(4) 提出了一个普适的维度依赖CDW相图概念模型，为后续研究指明了方向。
- **研究意义**：实现对**宏观极化**由量子力学波函数直接积分并进行一定粟子；为铁电/压电材料的第一性原理计算设计了一种不依赖于激发态的超衬底从而具有普适性；是穴坐现代“Polarization geometry”的基础。

## 📚 相关论文 (Related Papers)

- [[../papers/king-smithTheoryPolarizationCrystalline1993]]：为后续边界IP（现代极化理论）到达原始发初端点；提供了α标准处理方法；发表了现代实现对“自发极化极值算法”的评价基石（如现代铁电材料构型研究），同时引入相位几何的概念影响到拓扑物理。
- [[../papers/lezoualchStudyChargeDensity]]：为本文档提供核心证据。
- [[../papers/tangGridbasedBaderAnalysis2009]]：为本文档提供核心证据。
- [[../papers/yanagizawaSwitchingChargedensityWave2023]]：提供了一种通过载流子调谐来钉扎原子层厚度TMD材料中CDW机制的有效方法。
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]：1. 在实验已合成的2D-MOF中预测了具有可观Tc的超导电性，填补了该体系的研究空白。
- [[../papers/chowdhuryReviewTheoreticalComputational]]：本文的主要贡献在于：(1) 系统总结了二维CDW材料计算的挑战与解决方案，具有极高的教学价值；(2) 通过对比研究，为DFT计算参数的选择提供了基准；(3) 将光谱学特征与原子级微观动力学直接联系，深化了对CDW集体激发的理解；(4) 提出了一个普适的维度依赖CDW相图概念模型，为后续研究指明了方向。

## 🔗 关联概念与实体 (Related)

- [[../concepts/berry-phase|berry-phase]]
- [[../concepts/berry-connection|berry-connection]]
- [[../concepts/modern-polarization-theory|modern-polarization-theory]]
- [[../concepts/wannier-function|wannier-function]]
- [[../concepts/born-effective-charge|born-effective-charge]]
- [[../concepts/polarization-quantum|polarization-quantum]]
- [[../concepts/piezoelectricity|piezoelectricity]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/ferroelectricity|ferroelectricity]]
- [[../entities/GaAs|GaAs]]
- [[../entities/VASP|VASP]]
- [[../entities/Wannier90|Wannier90]]
- [[../concepts/charge-density-wave|charge-density-wave]]
- [[../concepts/2d-materials|2d-materials]]
- [[../concepts/electron-phonon-coupling|electron-phonon-coupling]]
