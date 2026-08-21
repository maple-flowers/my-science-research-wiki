---
tags: [entity, material, TMD, 2D, CDW, superconductor]
title: 二硒化钛 (TiSe2) / Titanium Diselenide
type: entity
status: mature
formula: TiSe2
stoichiometry: 1T
class: [TMD, vdW, semimetal]
properties: [charge-density-wave, superconductivity, excitonic-insulator]
related_entities: [1t-phase, NbSe2, TaS2]
papers: [Chen2019superconductivity, Koley2020charge, yanagizawaSwitchingChargedensityWave2023]
updated: 2026-08
---

# 二硒化钛 (TiSe2) / Titanium Diselenide

二硒化钛 (TiSe2) 是一种极为特殊的过渡金属硫族化合物。它在低温下（约 200 K）进入 $2 \times 2 \times 2$ 的电荷密度波 (CDW) 态。TiSe₂ 是研究**激子绝缘体 (Excitonic Insulator)** 物理以及 CDW 与超导穹顶竞争关系的明星体系。

## 👵 太奶导读

太奶，这个 **TiSe2** 就像是材料界的一个“不倒翁”。
它在常温下是个半金属，也就是那种电传得不快也不慢的性子。
但它最出名的地方在于，只要你给它“喂”一点电子（电子掺杂），或者使劲压一压（加压），它原本那个死气沉沉的电荷波就会被打乱，然后像变戏法一样，中间会冒出一个圆顶状的**超导区**。
科学家们为了研究它是怎么从“排队走”变成“一起飞（超导）”的，已经盯着它看了几十年了！

## 🏗️ 结构概览：1T 相

TiSe2 采用八面体配位的 1T 相结构。

![图：1T-TiSe2 及其超导穹顶相图](../../raw/figures/Chen2019superconductivity/fig_1_WTGGFJU9.png)
*   **看图要点**：图中展示了随着掺杂量增加，公度 CDW 被抑制，随后超导电性（红色区域）在近公度相附近涌现出的穹顶状特征。
*   **来源**：[[../papers/Chen2019superconductivity]] -> [[../figures/crystal-structures-xrd-phases|相变与相图]]

## 🧩 物理特性：错位相子驱动的超导

*   **激子凝聚**：不同于常规的 Peierls 机制，TiSe2 的 CDW 常被认为是由费米面附近的电子和空穴相互吸引形成的激子凝聚驱动。
*   **超导渗流**：Chen 等人预言，TiSe2 的超导电性并非均匀产生，而是优先在 CDW 的“褶皱”（[[../concepts/discommensuration|错位相子 DC]]）处成核。随着温度降低，超导信号沿着这些褶皱线连成网格，最终形成全域超导。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2019superconductivity]]：提出了 TiSe2 中由错位相子网络介导的超导渗流模型。
- [[../papers/Koley2020charge]]：讨论了 TiSe2 作为强耦合 CDW 体系的代表。
- [[../papers/yanagizawaSwitchingChargedensityWave2023]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/discommensuration|错位相子]]
- [[../concepts/exciton-condensation|激子凝聚]]
- [[../concepts/1t-phase|1T 相]]
