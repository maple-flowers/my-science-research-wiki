---
tags: [entity, material, TMD, 2D, ferromagnet, CDW]
title: 二硒化钒 (VSe2) / Vanadium Diselenide
type: entity
status: mature
formula: VSe2
stoichiometry: 1T
class: [TMD, vdW, metal]
properties: [charge-density-wave, 2D-ferromagnetism, pseudogap]
related_entities: [1t-phase, NbSe2, TaS2]
papers: [kawakamiChargedensityWaveAssociated2023, Inosov2008fermi, liPhaseTransitions2D2021, lezoualchStudyChargeDensity, liuSpintronicsTwoDimensionalMaterials2020b, sunSlidingFerroelectricityTwodimensional2025, zhaoOpticalFingerprintsTwodimensional2024]
updated: 2026-08
---

# 二硒化钒 (VSe2) / Vanadium Diselenide

二硒化钒 (VSe2) 是一种备受争议且物理内涵极其丰富的二维材料。在 1T 相下，它展现出极强的电荷密度波 (CDW) 序，且转变温度可被维度效应显著推高。同时，VSe2 的单层形式被认为是实现**本征二维磁性**的有力候选材料，尽管这一结论在实验上仍存在较多竞争性解释。

## 👵 太奶导读

太奶啊，这 VSe2 就像是二维材料里的“摇滚乐手”，特别有个性！它天生就不喜欢平平整整的，一冷下来它的原子就开始“蹦迪”，在表面跳出一层层波浪式的花纹（CDW）。而且啊，它最出名的一点是，大家都说它这么薄薄的一层片片，心里还藏着强烈的“吸铁石能量”（磁性），想成为二维世界的磁铁明星。虽然有些实验还在争论它到底是真磁性还是假磁性，但这种“带磁性的波浪绸缎”听着就够让科学家们兴奋好久了。

## 🏗️ 结构概览

VSe2 的稳定相为八面体配位的 1T 相。在单层极限下，它通过分子束外延 (MBE) 生长，通常展现出比块体更复杂的 CDW 超结构。

![图：单层 1T-VSe2 的 CDW 超晶格与 STM 成像](../../raw/figures/kawakamiChargedensityWaveAssociated2023/fig_2_6CWHPRW4.png)
*   **看图要点**：图中展示了 VSe2 在单层状态下的 STM 实空间图像。可以看到清晰的原子点阵叠加了长程的周期性调制（波纹），这反映了其非公度或公度的 CDW 状态。
*   **来源**：[[../papers/kawakamiChargedensityWaveAssociated2023]] -> [[../figures/crystal-structures-surfaces-defects|表面形貌]]

## 🧩 强电声耦合与 CDW 机制

VSe2 的 CDW 机制与传统的 NbSe2 有所不同，体现了更强的电子-声子耦合特征。

*   **CDW 多样性**：块体 VSe2 的 $T_{CDW} \approx 110\text{ K}$，展现 $4 \times 4 \times 3$ 的超结构；而单层 VSe2 的 $T_{CDW}$ 可远超室温，并出现 $4 \times 4$ 甚至条纹状 (Striped) 的竞争相。
*   **机制探讨**：不同于简单的费米面嵌套，VSe2 的 CDW 往往伴随着显著的能带重整化和**赝能隙 (Pseudogap)** 行为，这暗示了高阶电声耦合和电子关联的共同作用。
*   **磁性争议**：理论预测单层 VSe2 具有较强的本征磁矩，但实验中观测到的磁信号极易受衬底（如石墨烯/SiC）及环境氧化等因素干扰。

## 🔬 物理参数表

| 属性 | 数值 |
| :--- | :--- |
| CDW 转变温度 $T_{CDW}$ | 块体 $\sim 110\text{ K}$ (单层可达 $\sim 450\text{ K}$) |
| 磁性基态 | 理论预言铁磁 (FM)，实验尚存争议 |
| 超结构周期 | $4 \times 4$ 或非公度调制 |

## 📚 相关论文 (Related Papers)

- [[../papers/kawakamiChargedensityWaveAssociated2023]]：研究了 VSe2 中 CDW 与能带结构的关联。
- [[../papers/Inosov2008fermi]]：讨论了 TMD 材料中费米面动力学与电子关联。
- [[../papers/lezoualchStudyChargeDensity]]
- [[../papers/liPhaseTransitions2D2021]]
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波 (CDW)]]
- [[../concepts/pseudogap|赝能隙]]
- [[../entities/1t-phase|1T 相]]
- [[../entities/NbSe2|二硒化铌 (NbSe2)]]
