---
tags: [concept, multiferroicity, magnetism]
title: 逆 Dzyaloshinskii-Moriya 相互作用 (Inverse DMI)
type: concept
status: mature
domain: [multiferroicity, magnetism, magnetoelectric-coupling]
mechanism: 螺旋/非共线磁结构通过自旋轨道耦合在相邻离子间产生局域电极化（P ∝ e_ij × (S_i × S_j)），是 type-II 多铁自旋驱动铁电的核心微观机制
related_concepts: [dzyaloshinskii-moriya-interaction, helical-magnetism, magnetoelectric-coupling, exchange-striction, spin-orbit-coupling, chirality]
papers: [RecentAdvancesGrowth2025, fiebigEvolutionMultiferroics2016, cheongMultiferroicsMagneticTwist2007a, wuCoexistenceFerroelectricityAntiferroelectricity2024, gaoGiantChiralMagnetoelectric2024a, mostovoyMultiferroicsDifferentRoutes2024]
updated: 2026-08
---

# 逆 Dzyaloshinskii-Moriya 相互作用 (Inverse DMI)

逆 Dzyaloshinskii-Moriya 相互作用（inverse DMI，又称多铁机制中的自旋-轨道耦合诱导极化）指**螺旋或非共线磁结构通过自旋-轨道耦合在离子间产生电极化**的机制，是"自旋驱动铁电"（type-II 多铁）的核心微观机制之一，将磁性序与铁电极化直接耦合，实现磁电互控。

## 👵 太奶导读

太奶啊，前面说的 DMI 是"自旋轨道耦合让磁针拧起来"；逆 DMI 是反过来：磁针已经拧成螺旋了，这"拧劲"会通过原子之间轨道的作用，硬生生"拽出"一个电极化来——磁序拧巴了，电也跟着歪。于是"磁的排列"直接变成"电的极化"，这就是多铁材料里磁控电/电控磁的底层把戏之一。

## 🧩 核心内容与机制 (Core Content)

- **机制要点**：非共线磁序（螺旋/摆线，[[../concepts/helical-magnetism|螺旋磁序]]）中相邻磁性离子的自旋-轨道耦合产生非对称电荷分布，等效产生局域电极化 $\mathbf{P} \propto \mathbf{e}_{ij} \times (\mathbf{S}_i \times \mathbf{S}_j)$，其中 $\mathbf{e}_{ij}$ 为离子间连接矢量。
- **与 DMI 的对偶**：[[../concepts/dzyaloshinskii-moriya-interaction|DMI]] 是磁结构-轨道耦合产生磁场；逆 DMI 是磁结构产生电场，二者是同一自旋-轨道耦合的对偶效应。
- **多铁材料**：TbMnO₃、CuO、NiI2 等 type-II 多铁中自旋驱动极化即源于此（本库多铁与磁电耦合论文），可实现磁场调控铁电。
- **应用前景**：磁电互控器件、电场调控磁性（本库铁电控磁、磁电耦合异质结论文）。

## 📊 逆 DMI 与交换收缩对比

| 特征 | 逆 DMI (Inverse DMI) | 交换收缩 (Exchange-striction) |
|------|----------------------|-------------------------------|
| 磁结构前提 | 非共线（螺旋/摆线）磁序 | 共线磁序（如 E 型反铁磁） |
| 微观来源 | 自旋轨道耦合 | 各向同性交换 + 晶格畸变 |
| 极化方向 | 由自旋手性方向决定（方向性强） | 由晶格应变对称性决定 |
| 代表材料 | TbMnO3、NiI2、CuO | BiMnO3、Ca3CoMnO6 |
| 磁电互控效率 | 高（直接耦合） | 中等（经晶格传递） |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dzyaloshinskii-moriya-interaction|Dzyaloshinskii-Moriya 相互作用]]：逆 DMI 的对偶机制。
- [[../concepts/helical-magnetism|螺旋磁序]]：逆 DMI 的磁结构前提。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：逆 DMI 的多铁效应。
- [[../concepts/exchange-striction|交换收缩]]：另一类自旋驱动铁电机制。
- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：逆 DMI 的微观来源。
- [[../concepts/chirality|手性]]：逆 DMI 对手性磁序的依赖。

## 📚 相关论文 (Related Papers)

- [[../papers/RecentAdvancesGrowth2025]] — Recent advances in growth, characterization, and application of two-dimensional multiferroic materials
- [[../papers/fiebigEvolutionMultiferroics2016]] — The evolution of multiferroics
- [[../papers/cheongMultiferroicsMagneticTwist2007a]] — Multiferroics: a magnetic twist for ferroelectricity
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]] — Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic
- [[../papers/gaoGiantChiralMagnetoelectric2024a]] — Giant chiral magnetoelectric oscillations in a van der Waals multiferroic
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]] — Multiferroics: different routes to magnetoelectric coupling

## 🏷️ 专业名词别名

- `inverse-dm-interaction`（concepts）
- `自旋驱动铁电机制`（concepts）
