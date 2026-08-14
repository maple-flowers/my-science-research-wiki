---
tags: [concept, topological-physics, symmetry]
title: 破缺的空间反演对称性 / Broken Inversion Symmetry
type: concept
status: developing
domain: [condensed-matter-physics, topological-physics, ferroelectricity]
mechanism: 体系结构在坐标反演操作（x,y,z -> -x,-y,-z）下的不对称性
related_concepts: [ferroelectricity, multiferroicity, weyl-semimetal, spin-orbit-coupling, berry-curvature, non-centrosymmetric]
papers: [sharmaRoomtemperatureFerroelectricSemimetal2019, hanPolarTopologicalMaterials2025, wangTunableD0Topological2025b, xuTunableFerroelectricTopological2022]
updated: 2026-08
---

# 破缺的空间反演对称性 / Broken Inversion Symmetry

破缺的空间反演对称性 (Broken Inversion Symmetry, $\mathcal{P}$) 是指体系的物理结构或性质在空间坐标反演操作（即 $\vec{r} \rightarrow -\vec{r}$）下不再保持不变。在晶体学中，这意味着体系不具有反演中心（非中心对称，non-centrosymmetric）。这一性质是实现铁电性、压电性、二次谐波产生 (SHG) 以及外尔半金属态的先决条件。

## 👵 太奶导读

好孩子，这“破缺的空间反演对称性”说白了就是“左手抓不住右手，正面照不出反面”。
想象你照镜子，如果你这个人的长相是完全上下左右前后都对称的，那镜子里的你和外面的你就没区别（这叫反演对称）。但如果你的左眼长了个痣（破缺了对称性），那镜子里的痣就在右边，你就跟镜子里的自己不一样了。
在材料里，如果正负电荷分布得不对称，它就会产生“自发极化”，也就是成了铁电体。
在能带里，这种不对称会导致原本合在一起的能带产生“劈裂”（比如拉什巴劈裂），还会让能带交叉形成“外尔点”。所以说，想要材料有各种神奇的功能，比如发电（压电）或者是变成拓扑半金属，你就得想办法把它的这个“反演对称性”给打破了。

## 🏗️ 结构概览

非中心对称结构（如 WTe₂ 的 Td 相）是实现极性态和拓扑态的基础。

![图：Td-WTe₂ 的非中心对称晶体结构](../../raw/figures/sharmaRoomtemperatureFerroelectricSemimetal2019/fig_1_NDNYXQ2A.png)
*   **看图要点**：图中展示了原子在晶胞中的非对称排布，导致系统具有极性轴（c 轴）。
*   **来源**：[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] -> [[../figures/crystal-structures-bulk|体相晶体结构]]

## 🧩 物理意义与涌现效应

*   **铁电性 (Ferroelectricity)**：必须破缺空间反演对称性。
*   **压电性 (Piezoelectricity)**：在机械应力下产生电压，需要非中心对称结构。
*   **外尔半金属 (Weyl Semimetal)**：在保持时间反演对称性时，必须破缺空间反演对称性才能产生外尔点。
*   **非线性光学**：如二次谐波产生 (SHG) 只在非中心对称介质中发生。

## 📚 相关论文 (Related Papers)

- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：WTe₂ 由于破缺空间反演对称而展现出铁电性。
- [[../papers/xuTunableFerroelectricTopological2022]]：通过应变打破单层 PbX 的空间反演对称性，诱导顺电-铁电相变。
- [[../papers/hanPolarTopologicalMaterials2025]]：综述了极性材料中的反演对称破缺。
- [[../papers/wangTunableD0Topological2025b]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/non-centrosymmetric|非中心对称]]（对应的晶体学术语）
- [[../concepts/weyl-semimetal|外尔半金属]]（依赖此对称性破缺产生）
- [[../concepts/ferroelectricity|铁电性]]（此对称性破缺的最直接表现）
- [[../entities/WTe2|WTe₂]]（典型的非中心对称材料）
- [[../entities/PbTe|PbTe]]（可通过应变打破对称性的候选者）
