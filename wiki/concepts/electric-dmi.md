---
tags: [concept, ferroelectrics, topological-defects, multiferroicity]
title: 电 Dzyaloshinskii-Moriya 相互作用 (Electric DMI)
type: concept
status: mature
domain: [ferroelectrics, topological-defects, multiferroicity, strain-engineering]
mechanism: 铁电体系中由梯度能（Lifshitz 类不变式）、挠曲电与界面效应诱导的类 DMI 项，驱动极化连续旋转形成极性涡旋/斯格明子等手性拓扑结构，是磁性 DMI 的电力学类比
related_concepts: [dzyaloshinskii-moriya-interaction, polar-vortex, polar-skyrmion, flux-closure-domain, meron, solomon-ring, flexoelectricity, topological-defects, chirality, negative-capacitance]
papers: [hanPolarTopologicalMaterials2025, mostovoyMultiferroicsDifferentRoutes2024]
updated: 2026-08
---

# 电 Dzyaloshinskii-Moriya 相互作用 (Electric DMI)

电 Dzyaloshinskii-Moriya 相互作用（Electric DMI）是磁性 DMI 在铁电体系中的直接类比：在反演对称破缺的铁电纳米结构中，梯度能（Lifshitz 类不变式）、挠曲电与界面效应共同诱导出作用于极化（而非自旋）的类 DMI 项，使极化矢量倾向于连续旋转，从而稳定极性涡旋、反涡旋、极性斯格明子、麦纫、所罗门环等手性极性拓扑结构 [[../papers/hanPolarTopologicalMaterials2025]]。

## 👵 太奶导读

太奶啊，磁性材料里有种"拧劲"（DMI），把磁针拧成小漩涡，就是磁斯格明子。咱们材料科学家发现，铁电材料里的"电针"（电极化）也有类似的"拧劲"——叫"电 DMI"。它能把铁电里的小箭头也拧成涡旋、拧成圆环、拧成"阴阳鱼"一样的拓扑花样。这些纳米尺度的"电漩涡"能用来做超高密度存储，还有望实现负电容、超快太赫兹开关这些新奇功能。

## 🧩 核心内容与机制 (Core Content)

- **磁性 DMI 的类比**：磁性 DMI 由自旋轨道耦合在反演破缺体系中产生反对称交换项 $\mathbf{D}\cdot(\mathbf{S}_1\times\mathbf{S}_2)$，稳定手性磁结构；电 DMI 在铁电体系中由梯度能（Lifshitz 不变式）与挠曲电效应产生等效项，稳定手性极性拓扑结构。
- **能量竞争**：体自由能、静电学能（去极化场）、弹性能（应变/挠曲电）与梯度能之间的竞争决定极化基态构型，从均匀单畴过渡到涡旋/斯格明子等拓扑态。
- **拓扑结构谱系**：通量闭合畴（flux-closure）、涡旋（polar vortex）、极性斯格明子（polar skyrmion）、麦纫（meron）、反涡旋、所罗门环（solomon ring）等，各自对应不同的拓扑荷与能量配置 [[../papers/hanPolarTopologicalMaterials2025]]。
- **多场调控**：上述拓扑结构可被电场、机械力、光场和热场有效操控，展现出可编程巨电阻开关、稳态负电容、电控手性光学信号与超快太赫兹动力学等功能。

## 📊 磁性 DMI 与电 DMI 对照

| 特征 | 磁性 DMI | 电 DMI (Electric DMI) |
|------|----------|----------------------|
| 序参量 | 自旋 S | 电极化 P |
| 微观来源 | 自旋轨道耦合 | 梯度能/挠曲电/界面效应 |
| 能量项 | $\mathbf{D}\cdot(\mathbf{S}_1\times\mathbf{S}_2)$ | Lifshitz 类 $P(\partial P)-P^2(\partial P)$ 不变式 |
| 稳定结构 | 斯格明子、螺旋磁序、手性畴壁 | 极性涡旋、极性斯格明子、麦纫、所罗门环 |
| 关键体系 | B20 磁体、重金属/铁磁界面 | (PbTiO3)n/(SrTiO3)n 超晶格、BiFeO3 纳米岛 |
| 器件前景 | 赛道存储、斯格明子逻辑 | 超高密度存储、负电容晶体管、太赫兹器件 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dzyaloshinskii-moriya-interaction|Dzyaloshinskii-Moriya 相互作用]]：电 DMI 的磁性原型。
- [[../concepts/polar-vortex|极性涡旋]]：电 DMI 驱动的典型拓扑结构。
- [[../concepts/polar-skyrmion|极性斯格明子]]：极化版的斯格明子。
- [[../concepts/flux-closure-domain|通量闭合畴]]：涡旋拓扑的边界态。
- [[../concepts/meron|麦纫]]：半整拓扑荷的极性结构。
- [[../concepts/solomon-ring|所罗门环]]：高阶极性拓扑结构。
- [[../concepts/flexoelectricity|挠曲电效应]]：电 DMI 的微观来源之一。
- [[../concepts/topological-defects|拓扑缺陷]]：极性拓扑结构的统称。
- [[../concepts/chirality|手性]]：极性拓扑结构的手性本质。
- [[../concepts/negative-capacitance|负电容]]：极性拓扑结构的功能体现。

## 📚 相关论文 (Related Papers)

- [[../papers/hanPolarTopologicalMaterials2025]]：首次从能量竞争角度系统提出极性拓扑结构设计的普适原理，明确"电 Dzyaloshinskii-Moriya 相互作用"等新机制。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：综述多铁材料磁电耦合的不同微观路径，提供 DMI/逆 DMI 与电学类比的框架。

## 🏷️ 专业名词别名

- `electric-dm-interaction`（concepts）
- `类 DMI 梯度能项`（concepts）
