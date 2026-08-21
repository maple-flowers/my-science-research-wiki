---
tags: [concept, multiferroicity, magnetoelectric-coupling]
title: 动力学磁电效应 / Kinetic Magnetoelectric Effect
type: concept
status: mature
domain: [multiferroicity, magnetoelectric-coupling, magnetism]
mechanism: 非共线/螺旋磁序通过自旋轨道耦合在相邻磁性离子间产生动力学电极化（P ∝ e_ij × (S_i × S_j)），即 Katsura-Nagaosa-Balatsky 机制，属于逆 DMI 的动力学来源
related_concepts: [inverse-dzyaloshinskii-moriya, magnetoelectric-coupling, multiferroicity, helical-magnetism, spin-spiral, electromagnon, dzyaloshinskii-moriya-interaction]
papers: [gaoGiantChiralMagnetoelectric2024a, mostovoyMultiferroicsDifferentRoutes2024, fiebigEvolutionMultiferroics2016, cheongMultiferroicsMagneticTwist2007a]
updated: 2026-08
---

# 动力学磁电效应 / Kinetic Magnetoelectric Effect

动力学磁电效应（kinetic magnetoelectric effect）指**非共线磁序（螺旋、摆线等）通过自旋轨道耦合在相邻磁性离子之间产生局域电极化**的机制，由 Katsura、Nagaosa 与 Balatsky 于 2005 年系统阐明。它是"自旋驱动铁电"（type-II 多铁）与逆 Dzyaloshinskii-Moriya 相互作用的微观物理基础，实现磁序对电极化的直接（动力学）耦合。

## 👵 太奶导读

太奶啊，有些磁体里的"小磁针"不是朝同一个方向排，而是拧成螺旋形（像搓麻绳）。这种"拧着排"的磁针，在电子轨道的作用下会硬生生"拽出"电来——磁针拧巴了，材料就带上了电极化。这就是"动力学磁电效应"：磁的排列方式（非共线磁序）直接决定了电的极性。磁控电、电控磁的把戏，根子上就有它一份。

## 🧩 核心内容与机制 (Core Content)

- **微观表达式**：局域电极化 $\mathbf{P} \propto \mathbf{e}_{ij} \times (\mathbf{S}_i \times \mathbf{S}_j)$，其中 $\mathbf{e}_{ij}$ 为相邻磁性离子间连接矢量，$\mathbf{S}_i$、$\mathbf{S}_j$ 为自旋。非共线排列（$\mathbf{S}_i \times \mathbf{S}_j \neq 0$）是产生极化的必要条件。
- **与逆 DMI 的关系**：动力学磁电效应与 [[../concepts/inverse-dzyaloshinskii-moriya|逆 DMI]] 描述同一物理——均源于自旋轨道耦合；前者强调电子运动学贡献（含 Anderson 移位项），后者强调离子位移贡献。
- **多铁材料**：TbMnO₃、NiI2、CuO 等螺旋磁序材料的电极化主要源于此机制 [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]；螺旋方向（手性）决定极化方向。
- **动力学光学活性**：非共线自旋序还能产生巨自然光学活性（圆二色/旋光），如 vdW 多铁 NiI2 中手性畴的 THz 磁电振荡 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。
- **与交换收缩的区别**：交换收缩依赖共线磁序与晶格畸变（对称机制）；动力学磁电效应依赖非共线自旋-轨道耦合（反对称机制），极化方向选择性更强。

## 📊 自旋驱动铁电机制对比

| 机制 | 磁序类型 | 微观来源 | 极化表达式 | 代表材料 |
|------|----------|----------|------------|----------|
| 动力学磁电效应（逆 DMI） | 非共线螺旋/摆线 | 自旋轨道耦合 | $\mathbf{P}\propto\mathbf{e}_{ij}\times(\mathbf{S}_i\times\mathbf{S}_j)$ | TbMnO3、NiI2、CuO |
| 交换收缩 | 共线（E 型） | 交换+晶格畸变 | $\mathbf{P}\propto\mathbf{r}_{ij}(\mathbf{S}_i\cdot\mathbf{S}_j)$ | BiMnO3、Ca3CoMnO6 |
| 孤对电子机制 | 无需磁序 | 孤对电子位移 | 结构固有 | BiFeO3 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/inverse-dzyaloshinskii-moriya|逆 DMI]]：动力学磁电效应的等价表述。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：动力学磁电效应的宏观表现。
- [[../concepts/multiferroicity|多铁性]]：动力学磁电效应的宿主体系。
- [[../concepts/helical-magnetism|螺旋磁序]]：动力学磁电效应的磁序前提。
- [[../concepts/spin-spiral|自旋摆线]]：典型非共线磁序。
- [[../concepts/electromagnon|电磁振子]]：磁电耦合的动力学激发。
- [[../entities/TbMnO3|TbMnO₃]]：螺旋磁序多铁原型。
- [[../entities/NiI2|NiI₂]]：vdW 螺旋磁序多铁。

## 📚 相关论文 (Related Papers)

- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：手性磁体中的巨自然光学活性与动力学磁电振荡。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：多铁磁电耦合的不同微观路径（含动力学机制）。
- [[../papers/fiebigEvolutionMultiferroics2016]]：多铁性发展综述，涵盖自旋驱动铁电机制。
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：磁扭转产生铁电性的早期经典综述。

## 🏷️ 专业名词别名

- `knb-mechanism`（concepts）
- `Katsura-Nagaosa-Balatsky 机制`（concepts）
- `自旋流磁电机制`（concepts）
