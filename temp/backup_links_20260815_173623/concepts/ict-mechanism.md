---
tags: [concept, photophysics, excited-state]
title: 分子内电荷转移机制 / ICT Mechanism
type: concept
status: mature
domain: [photophysics, physical-organic-chemistry, spectroscopy]
mechanism: 分子从基态跃迁至激发态时，电子密度从给体（Donor）部分向受体（Acceptor）部分发生显著转移
related_concepts: [solvatochromism, tict-mechanism, donor-pi-acceptor, stokes-shift]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence]
updated: 2026-08
---

# 分子内电荷转移机制 / ICT Mechanism

分子内电荷转移（Intramolecular Charge Transfer, ICT）是有机发光分子中最基础的激发态机制之一。它发生在具有强给体（Donor）和强受体（Acceptor）通过共轭链相连的分子（即 [[../concepts/donor-pi-acceptor|D-π-A]] 分子）中。

## 👵 太奶导读

太奶啊，这就好比一个**“分家产”**的过程。这分子在平时（基态）的时候，给体（就像是阔气的地主老财）和受体（就像是想发财的掌柜）虽然也连在一块儿，但电荷这“家产”还算散得均匀。可一旦这分子吸收了能量（激发态），这一大笔电荷“家产”就像是被一股脑儿地从地主老财（给体）那边赶到了掌柜（受体）手里。这一“分家”，分子的极性（两头电性差）就猛地变大了。如果这时候周围环境特别极化，就会把这种“家产分散”的状态给稳固住，让发出来的光变了颜色。

## 🏗️ 物理实质与光谱指纹

在激发态发生 ICT 时，分子的**偶极矩 ($\mu$)** 通常会发生剧增。这导致了以下光谱特征：
*   **吸收谱不敏感**：基态受溶剂影响较小，吸收峰位置基本恒定。
*   **发射谱高度敏感**：由于激发态偶极矩巨大，极性溶剂分子的重排（[[../concepts/solvent-relaxation|溶剂弛豫]]）能极大地稳定激发态能量。这导致发射峰随溶剂极性增大而显著红移，即典型的**正向溶剂化显色效应**。
*   **Stilbene 案例**：基于二氰基二苯乙烯的探针 1a 利用了双氰基受体的强吸电子能力，实现了从 445 nm 到 641 nm 的巨大 ICT 红移 [[../papers/Huang2023two]]。

## 🧩 构效关系

实现高效 ICT 的分子设计准则：
1.  **强推拉结构**：给体（如二甲氨基）与受体（如氰基、硝基、醛基）之间的能级匹配。
2.  **共轭连通性**：π 共轭桥（如乙烯基、苯环）必须保证电子云的顺畅流动。
3.  **协同效应**：在 1a 分子中，邻位和间位两个氰基的协同作用，既增强了受体强度，又扩大了电荷分布，从而获得了超大的双光子吸收截面 [[../papers/H2017fluorescence]]。

## 🔬 与 TICT 的关系

ICT 是分子内电荷转移的广义称呼。如果这种转移伴随着分子内化学键的旋转扭转（从共平面变为正交），则进一步演化为 [[../concepts/tict-mechanism|扭曲分子内电荷转移 (TICT)]] 态，通常会导致荧光的猝灭。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：分析了二氰基取代如何通过 ICT 机制产生超大双光子截面。
- [[../papers/Huang2019solvatochromic]]：探讨了 ICT 态的溶剂弛豫对热致变色的贡献。
- [[../papers/H2017fluorescence]]：阐述了激发态绝热 ICT 过程中的电荷稳定机制。
- [[../papers/H2017fluorescence]] — Dicyanostilbene-based Two-photon Thermo-solvatochromic Fluorescence Probes with Two-photon Triple Fluorescence
- [[../papers/Huang2019solvatochromic]] — Stilbene-Based Two-Photon Thermo-Solvatochromic Fluorescence Probes with Large Two-Photon Absorption Cross Sections and Two-Photon Triple Fluorescence: Detection of Solvent Polarities, Viscosities, and Temperature
- [[../papers/WRZYSZCZYNSKI2010initiators]] — Two-photon initiators of polymerization
- [[../papers/Zhang2008synthesis]] — Synthesis and nonlinear optical properties of two three-branched two-photon polymerization initiators

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/solvatochromism|溶剂化显色]]
- [[../concepts/tict-mechanism|TICT 机制]]
- [[../concepts/stokes-shift|斯托克斯位移]]
- [[../concepts/donor-pi-acceptor|D-π-A 结构]]
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]

## 🏷️ 专业名词别名

- `intramolecular-charge-transfer`（concepts）
