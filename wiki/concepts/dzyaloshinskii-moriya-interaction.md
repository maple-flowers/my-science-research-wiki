---
tags: [concept, magnetism, topology]
title: Dzyaloshinskii-Moriya 相互作用 (DMI)
type: concept
status: developing
domain: [magnetism, topology, spintronics, multiferroicity]
mechanism: 自旋轨道耦合与交换作用在反演对称破缺体系中耦合产生的反对称交换作用，哈密顿量 -D·(S₁×S₂)，使相邻自旋倾向于互相垂直，驱动手性磁结构
related_concepts: [spin-orbit-coupling, helical-magnetism, skyrmion, ferromagnetism, inversion-symmetry-breaking, exchange-interaction, chirality, inverse-dzyaloshinskii-moriya, electric-dmi]
papers: [Goswami2011multiferroic, aminiAtomicscaleVisualizationMultiferroicity2024, deSousa2008electrical, hanPolarTopologicalMaterials2025, rameshMultiferroicsProgressProspects2007, tanRevealingEmergentMagnetic2024, tangMultiferroicityTwodimensionalVan2025, wangTunableD0Topological2025b, zhangNonvolatileControlTopological2025, zhaoRealization2DMultiferroic2024]
updated: 2026-08
---

# Dzyaloshinskii-Moriya 相互作用 (DMI)

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


Dzyaloshinskii-Moriya 相互作用（Dzyaloshinskii-Moriya interaction, DMI）是缺乏反演对称的磁性体系中由**自旋轨道耦合（SOC）**与交换作用耦合产生的反对称交换相互作用。其哈密顿量形如 $-\mathbf{D}\cdot(\mathbf{S}_1\times\mathbf{S}_2)$，倾向于使相邻自旋**互相垂直**而非平行/反平行排列，是手性磁结构（螺旋磁序、斯格明子、磁孤子）的核心驱动机制。

## 👵 太奶导读

太奶啊，磁体里的原子磁针本来要么同向要么反向排，规规矩矩。但有一种"坏脾气"的相互作用叫 DMI：它偏要磁针"拧着放"——相邻两根磁针互成直角。这一拧，磁针就拧出了螺旋（helical magnetism），还能拧出像小漩涡一样的"磁斯格明子"。能不能拧出这些花样，取决于材料有没有"左右不对称"（反演对称破缺）和"轨道自旋耦合"。

## 🧩 核心内容与机制 (Core Content)

- **哈密顿量**：$H_{DM} = -\sum_{ij}\mathbf{D}_{ij}\cdot(\mathbf{S}_i\times\mathbf{S}_j)$，其中 $\mathbf{D}_{ij}$ 为 Dzyaloshinskii-Moriya 矢量，其方向由局域晶格对称性决定（Moriya 规则）。
- **起源**：DMI 源于自旋轨道耦合 + 交换作用 + 反演对称破缺（本库 [[../concepts/spin-orbit-coupling|自旋轨道耦合]] 相关）；在界面/表面、体心材料（如 B20 结构）与二维异质结中普遍存在。
- **能量竞争**：DMI 与各向同性交换（$J$）、磁各向异性（$K$）竞争，决定自旋基态构型；$D/J$ 比值控制从铁磁到螺旋磁序再到斯格明子相的转变。
- **手性磁结构**：DMI 稳定手性螺旋磁序（[[../concepts/helical-magnetism|螺旋磁序]]）、斯格明子（[[../concepts/skyrmion|斯格明子]]）与手性畴壁，赋予其拓扑稳定性与低电流驱动特性。
- **二维体系**：磁性二维材料与重金属衬底界面产生的强界面 DMI 是室温斯格明子研究的关键（本库 helimagnon/斯格明子相关论文）。
- **应用前景**：斯格明子可作为信息载体（赛道存储），DMI 大小直接决定其尺寸与稳定性。

## 📊 典型体系与参数

| 体系 | DMI 来源 | D 量级 | 特征磁结构 |
|------|----------|--------|------------|
| B20 体材料（MnSi、FeGe） | 手性晶格本征 DMI | meV 量级 | 螺旋磁序、斯格明子晶格 |
| 重金属/铁磁界面（Pt/Co、Ir/Co） | 界面 Rashba-SOC 诱导 | 界面 DMI 强 | 奈尔型斯格明子、手性畴壁 |
| 二维 vdW 磁体异质结（CrInTe2/In2Se3） | 衬底/邻近铁电调控 | 可电场调控 | 拓扑磁态、斯格明子 [[../papers/zhangNonvolatileControlTopological2025]] |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：DMI 的微观来源。
- [[../concepts/helical-magnetism|螺旋磁序]]：DMI 稳定的手性磁序。
- [[../concepts/skyrmion|斯格明子]]：DMI 驱动的拓扑磁结构。
- [[../concepts/ferromagnetism|铁磁性]]：与 DMI 竞争的基础磁序。
- [[../concepts/inversion-symmetry-breaking|反演对称破缺]]：DMI 存在的必要条件。
- [[../concepts/exchange-interaction|交换相互作用]]：与 DMI 竞争的对称交换。
- [[../concepts/inverse-dzyaloshinskii-moriya|逆 DMI]]：磁结构产生电极化的对偶机制。
- [[../concepts/electric-dmi|电 DMI]]：铁电体系中的类 DMI 类比。

## 📚 相关论文 (Related Papers)

- [[../papers/Goswami2011multiferroic]] — Multiferroic coupling in nanoscale BiFeO3
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] — Atomic-Scale Visualization of Multiferroicity in Monolayer NiI2
- [[../papers/deSousa2008electrical]] — Electrical control of magnon propagation in multiferroic BiFeO3 films
- [[../papers/hanPolarTopologicalMaterials2025]] — Polar topological materials and devices: Prospects and challenges
- [[../papers/rameshMultiferroicsProgressProspects2007]] — Multiferroics: progress and prospects in thin films
- [[../papers/tanRevealingEmergentMagnetic2024]] — Revealing emergent magnetic charge in an antiferromagnet with diamond quantum magnetometry
- [[../papers/tangMultiferroicityTwodimensionalVan2025]] — Towards Multiferroicity in Two-Dimensional Van Der Waals Materials: Challenges and Opportunities
- [[../papers/wangTunableD0Topological2025b]] — Tunable d0 topological magnetic states in multiferroic monolayer In2NO2
- [[../papers/zhangNonvolatileControlTopological2025]] — Nonvolatile control of topological magnetism in two-dimensional CrInTe2/In2Se3 multiferroic heterostructures
- [[../papers/zhaoRealization2DMultiferroic2024]] — Realization of 2D multiferroic with strong magnetoelectric coupling by intercalation: a first-principles high-throughput prediction

## 🏷️ 专业名词别名

- `dm-interaction`（concepts）
- `反对称交换相互作用`（concepts）
