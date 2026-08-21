---
tags: [entity, material, 2d-material, tmd, cdw, mott-insulator]
title: 二硫化钽 / Tantalum Disulfide (1T-TaS2)
type: entity
status: developing
formula: 1T-TaS2
class: [transition-metal-dichalcogenide, cdw-material, mott-insulator]
properties: [charge-density-wave, mott-insulator, phase-transition, superconductivity, star-of-david]
related_entities: [2H-TaSe2, 1T-TaSe2, NbSe2, TMDs]
papers: [Chen2019superconductivity, cossuStackingChargedensityWaves2024, kimObservationPhaseTransition1997, nakataRobustChargedensityWave2021]
updated: 2026-08-18
---

# 二硫化钽 / Tantalum Disulfide (1T-TaS2)

1T-TaS₂ 是过渡金属二硫族化物（TMDs）中研究电荷密度波（CDW）与莫特绝缘体转变的经典模型材料。其标志性特征是低温下形成由 13 个 Ta 原子构成的"大卫之星"（Star-of-David）CDW 超结构（√13×√13），并伴随非磁性的莫特绝缘相。该体系兼具 CDW、莫特物理与（加压/掺杂下的）超导穹顶，是研究电子关联、电子-声子耦合与低维有序竞争的核心平台。

## 👵 太奶导读

乖孙，1T-TaS₂ 就像一块"电子们排队打太极"的薄片。它里面的电子不喜欢随意乱跑，到了一定温度就会自动排成一组一组的"星星"图案（这就是"电荷密度波"），排好队之后电子被"卡"住，材料从导体变成绝缘体（莫特绝缘）。更有趣的是，它排队的"队形"还能被外界调来调去——用一根极细的针尖一戳、或者加压力、掺电子，队形就会变，甚至能变出超导（零电阻）来。科学家拿它当"电子排队"的实验场，研究材料里电子的各种怪脾气。

## 🏗️ 结构概览

- **晶体结构**：1T 相为八面体配位（Ta 原子被 6 个 S 原子八面体包围），层状范德华结构。
- **低温相**：降温后形成 √13×√13 R13.9° 的"大卫之星"CDW 超结构，每个星团由 13 个 Ta 原子构成（中心 1 个、外围 12 个向内收缩）。
- **多相转变**：随温度经历近公度（NCCDW）→ 公度（CCDW）CDW 转变，公度相伴随莫特绝缘态；加压或掺杂可抑制 CDW 并诱导超导。

## 🧩 CDW、莫特绝缘与超导的竞争

- **莫特绝缘起源**：nakataRobustChargedensityWave2021 对单层 1T-TaSe₂（同族 1T 体系）的 ARPES 研究表明，CDW 晶格畸变重整并压窄电子能带，使有效库仑能与带宽之比 U/W 增大，从而把体系推入莫特-哈伯德能隙；单层 1T-TaSe₂ 的 CDW-莫特转变温度可达约 530 K（远超块体的 <200 K），是强耦合（2Δ/k_BT ≈ 12）的二维 CDW-莫特相。
- **CDW 堆叠与电子关联**：cossuStackingChargedensityWaves2024 在 2H-NbSe₂ 双层中展示层间 CDW 的堆叠构型本身即可产生多种能量相近的构型并自发破缺对称性，预示 CDW 堆叠是 TMDs 中被普遍忽略的物理自由度（对 1T 体系同样适用）。
- **针尖诱导相变**：kimObservationPhaseTransition1997 首次在室温下用 STM 针尖电压脉冲将 1T-TaS₂ 表层由 T 相（NCCDW）转化为 2H 相，相变由表面 S 原子层沿 [112̄0] 方向集体滑移 (√3/3)a₀ 实现，将 STM 操控从单原子提升到原子层集体运动级别。
- **超导涌现机制**：Chen2019superconductivity 构建 McMillan-Ginzburg-Landau 唯象理论，指出在 CDW 由公度到非公度转变的中间态（近公度相）中，"错位相子"（discommensuration）网络驱动超导成核，解释实验相图并预言非均匀超导态。

## 📚 相关论文 (Related Papers)

- [[../papers/nakataRobustChargedensityWave2021]]：实验揭示单层 1T-TMD 中 CDW-莫特转变温度远超室温，阐明电子-晶格耦合对带宽的压制是决定 U/W 的主导因素。
- [[../papers/kimObservationPhaseTransition1997]]：STM 针尖诱导 1T-TaS₂ 表面 T→H 相变，开创原子层集体运动的操控范式。
- [[../papers/cossuStackingChargedensityWaves2024]]：以 2H-NbSe₂ 双层为例论证层间 CDW 堆叠自由度与自发对称性破缺，连接 STM 实验与理论模型。
- [[../papers/Chen2019superconductivity]]：提出错位相子驱动的 CDW 涨落作为超导配对机制的统一唯象框架。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/mott-insulator|莫特绝缘体]]
- [[../concepts/electron-correlation|电子关联]]
- [[../concepts/superconductivity|超导电性]]
- [[../entities/TMDs|过渡金属二硫族化物（TMDs）]]
- [[../entities/2H-TaSe2|2H-TaSe₂（同族 CDW 参照）]]
