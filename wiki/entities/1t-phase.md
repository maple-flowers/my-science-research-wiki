---
tags: [entity, phase, material-structure, TMD]
title: 1T 相 / 1T-phase
type: entity
status: mature
formula: "MX2"
stoichiometry: 1T
class: [structure-phase, TMD]
properties: [octahedral-coordination, metallicity, CDW, Mott-insulator]
related_entities: [2h-phase, 1t-phase, TaS2, VSe2, MoS2, MoTe2]
papers: [liPhaseTransitions2D2021, nakataRobustChargedensityWave2021, CastroNeto2001charge]
updated: 2026-08
---

# 1T 相 / 1T-phase

1T 相是过渡金属硫族化合物 (TMD) 的一种重要晶体结构构型。在 1T 相中，过渡金属原子 (M) 处于由六个硫族原子 (X) 构成的**八面体 (Octahedral)** 配位环境中。相比于稳态的 2H 相，1T 相通常表现出金属性，但由于其费米面的电子不稳定性，常伴随强烈的电荷密度波 (CDW) 和莫特绝缘体行为。

## 奶奶导读

太奶啊，这 1T 相就是 TMD 材料里的“好动派”。原本这些原子层像是有序的三棱柱积木搭起来的（2H 相），但一旦变成 1T 相，原子就像是钻进了一个个八面体的“魔方”里。这个魔方里的电子非常活跃，像水一样能流来流去，所以它通常是导电的。但它也有个毛病，就是“心思不稳定”，冷一点原子的位置就会悄悄挪动，搞出一堆花样百出的波纹（CDW）或者把路给堵死（莫特转变）。

## 🏗️ 结构概览

1T 相的单层具有中心对称性，属于 $D_{3d}$ 点群。原子堆叠顺序为 $AbC$ 型（大写字母代表硫族原子，小写字母代表过渡金属原子）。

![图：1T 相的八面体配位示意图](../../raw/figures/liPhaseTransitions2D2021/fig_5_RCAID2CF.png)
*   **看图要点**：图中展示了 1T 相的侧视图。中间层的金属原子被上下两层硫族原子包围，形成完美的八面体。在 1T' 或 Td 相中，这个八面体会发生扭曲。
*   **来源**：[[../papers/liPhaseTransitions2D2021]] -> [[../figures/crystal-structures-bulk|晶体结构]]

## 🧩 物理特性与 Peierls 不稳定性

1T 相的 TMD 展现出与结构密切相关的丰富物性：

*   **金属性与不稳定性**：理想的 1T 相通常具有交叉费米面的金属性。然而，这种金属性在单维或低维极限下往往是不稳定的，极易发生 **Peierls 畸变**。
*   **大卫之星畸变**：在 1T-TaS2 或 1T-TaSe2 中，1T 相会进一步演化为 $\sqrt{13} \times \sqrt{13}$ 的超晶格（大卫之星），从而诱发莫特绝缘态。
*   **相变工程**：通过化学插层（如锂化）或电荷注入，可以驱动 MoS2 等材料从 2H 相转变为亚稳态的 1T 相，利用其优异的导电性提高催化性能。

## 🔬 结构对比表

| 特征 | 1T 相 | 2H 相 |
| :--- | :--- | :--- |
| 配位多面体 | 八面体 (Octahedral) | 三棱柱 (Trigonal Prismatic) |
| 原子堆垛 | $AbC$ | $AbA$ |
| 典型电子态 | 金属 / Mott 绝缘体 | 半导体 |
| 对称性 | 中心对称 ($D_{3d}$) | 非中心对称 ($D_{3h}$) |

## 📚 相关论文 (Related Papers)

- [[../papers/liPhaseTransitions2D2021]]：系统分析了 1T 相及其衍生物相的相变与物理诱因。
- [[../papers/nakataRobustChargedensityWave2021]]：研究了 1T 相 TMD 中电子关联对 CDW 的增强作用。
- [[../papers/CastroNeto2001charge]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/peierls-instability|Peierls 不稳定性]]
- [[../concepts/charge-density-wave|电荷密度波 (CDW)]]
- [[../entities/2h-phase|2H 相]]
- [[../entities/TaS2|二硫化钽 (TaS2)]]
- [[../entities/VSe2|二硒化钒 (VSe2)]]
