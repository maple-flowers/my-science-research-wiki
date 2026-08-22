---
tags: [concept]
title: 'soft-mode'
type: concept
status: developing
papers: ['kawakamiChargedensityWaveAssociated2023', 'gomez-ortizKittelLawDomain2023', 'hillWhyAreThere2000a', 'junqueraCriticalThicknessFerroelectricity2003', 'Makogon2012wave', 'lezoualchStudyChargeDensity', 'xuTunableFerroelectricTopological2022', 'chenHafniumBasedFerroelectricPostMoore2026', 'chenStrongSlidingFerroelectricity2024']
updated: 2026-08-18
---

# soft-mode

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


软模（soft mode）指**相变温度附近频率趋近于零的晶格振动（声子）模式**，其"软化"标志晶格对畸变的不稳定性，是位移型相变（铁电、铁弹、结构相变）的微观机制：声子频率 ω² 随温度趋近相变点线性降至零，对应 Ginzburg-Landau 序参量的恢复力消失。

## 👵 太奶导读

太奶啊，原子在晶格里像连着小弹簧一样振动，每种振动方式有自己的"音高"（频率）。有些材料要相变时，某种振动的"音高"会越来越低、越来越"懒"（软化），到相变温度就彻底"趴下"（频率归零）——原子顺势"歪"向新位置，材料就变出铁电、铁弹等新性质。这"变懒"的振动就是软模，是相变的"预警信号"。

## 🧩 核心内容与机制 (Core Content)

- **位移型相变**：软模机制描述铁电（如 BaTiO₃、SrTiO₃）、铁弹与结构相变（structural-phase-transition）中原子集体位移的来源（本库铁电与结构相变论文）。
- **频率与温度**：ω² ∝ (T - T_C)（居里-外斯型），相变点 ω→0；由声子谱计算（本库 phonon 计算、DFPT 论文）。
- **与 CDW 的关系**：CDW 相变伴随 Kohn 异常与声子软化（kohn-anomaly），电子-声子耦合驱动软模（本库 CDW 论文）。
- **序参量关联**：软模坐标即序参量（order-parameter）的动力学变量，Ginzburg-Landau 理论（ginzburg-landau）中恢复力系数 a 变号。
- **实验探测**：非弹性中子/ X 射线散射、拉曼与太赫兹光谱观测软模（本库 Ti-sapphire 等光谱实验相关）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/structural-phase-transition|结构相变]]：软模驱动的相变。
- [[../concepts/kohn-anomaly|Kohn 异常]]：与软模相关的声子反常。
- [[../concepts/ferroelectricity|铁电性]]：位移型铁电的软模机制。
- [[../concepts/order-parameter|序参量]]：软模坐标与序参量。

## 📚 相关论文 (Related Papers)

- [[../papers/kawakamiChargedensityWaveAssociated2023]] — Charge-density wave associated with higher-order Fermi-surface nesting in monolayer VS2
- [[../papers/gomez-ortizKittelLawDomain2023]] — Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices
- [[../papers/hillWhyAreThere2000a]] — Why Are There so Few Magnetic Ferroelectrics?
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]] — Critical thickness for ferroelectricity in perovskite ultrathin films
- [[../papers/Makogon2012wave]] — Spin-charge-density wave in a rounded-square Fermi surface for ultracold atoms
- [[../papers/lezoualchStudyChargeDensity]] — Study of charge density waves in transition metal dichalcogenides
- [[../papers/xuTunableFerroelectricTopological2022]] — Tunable ferroelectric topological defects on 2D topological surfaces: strain engineering skyrmion-like polar structures in 2D materials
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]] — Hafnium-Based Ferroelectric Post-Moore Electronics: Device Physics, Integration Architectures, and Neuromorphic System Implementation
- [[../papers/chenStrongSlidingFerroelectricity2024]] — Strong Sliding Ferroelectricity and Interlayer Sliding Controllable Spintronic Effect in Two-Dimensional HgI₂ Layers

## 🏷️ 专业名词别名

- `soft-mode-phonon`（concepts）
- `soft-phonon-mode`（concepts）
