---
tags: [concept, stereochemistry, solid-state-physics]
title: 手性 / Chirality
type: concept
status: mature
domain: [stereochemistry, solid-state-physics, non-linear-optics, topological-magnetism]
mechanism: 系统与其镜像不能通过旋转/平移重合的几何属性，可由非心空间群（结构手性）或非共线磁矩排布（磁手性）产生
related_concepts: [optical-activity, magnetoelectric-coupling, raman-optical-activity, electromagnon, dzyaloshinskii-moriya-interaction, helical-magnetism, skyrmion]
papers: [songEvidenceSinglelayerVan2022, gaoGiantChiralMagnetoelectric2024a, hanPolarTopologicalMaterials2025, nahasFrustrationSelfOrderingTopological2016]
updated: 2026-08
---

# 手性 / Chirality

手性（Chirality）是自然界及凝聚态物理中的一种基本几何属性。当一个系统（分子、晶格、自旋排布）与其镜像不能通过旋转或平移操作完全重合时，该系统就具有手性。在凝聚态与材料科学中，手性既是结构属性（由空间群决定），也是磁序属性（由非共线自旋结构决定），构成手性光电器件、拓扑磁结构与多铁材料的核心几何要素。

## 👵 太奶导读

太奶啊，这就好比咱们的**"左手和右手"**。它们俩看起来长得一模一样，都是大拇指朝外、四指并拢，但您无论怎么转、怎么摆，都不能把左手和右手重合在一起（掌心相对不算重合，必须叠在一起方向一致）。在咱们材料科学里，有的材料里原子排队也像这样分成了"左撇子"和"右撇子"；甚至连里面的磁矩（小磁铁）排成的螺旋圈，也能分成左旋和右旋。这种不对称的结构，会让光在穿过它时产生奇妙的旋转，这就是咱们用来做手性元器件的基础。

## 🏗️ 凝聚态物理中的手性分类

| 类型 | 来源 | 特征 | 实例 |
|------|------|------|------|
| 结构手性 (Structural Chirality) | 不含反演、镜面或滑移对称性的非心空间群（手性空间群，如 $P3_121$、$P3_221$） | 晶格本身手性，决定拓扑晶体光学性质 | Te、Se 手性晶体、$\alpha$-HgS |
| 磁手性 (Magnetic Chirality) | 晶格结构本身非手性，低温非共线自旋结构破缺空间对称性 | 自旋螺旋/摆线具左旋或右旋，与电极化耦合 | NiI2、TbMnO3 |
| 拓扑手性 (Topological Chirality) | 磁拓扑结构（斯格明子、麦纫）内部的自旋涡旋方向 | 赋予拓扑稳定性与电流驱动性 | skyrmion、helical-magnetism |

1.  **结构手性 (Structural Chirality)**：由不含反演、镜面或滑移对称性的非心空间群（手性空间群，如 $P3_121$ 或 $P3_221$）产生，对应拓扑平带与手性光学活性。
2.  **磁手性 (Magnetic Chirality)**：晶格结构本身不具有手性，但其低温下的非共线自旋结构打破了空间对称性，形成手性。
    *   **螺旋磁序 (Spin Helix / Proper-screw)**：在 [[../entities/NiI2|NiI2]] 中，自旋在沿 $c$ 轴传播时发生旋转，形成左旋或右旋的自旋螺旋，产生局域的极性手性畴 [[../papers/songEvidenceSinglelayerVan2022]]。

## 🧩 手性的光学指纹：拉曼光学活性 (ROA)

在多铁材料研究中，手性畴的无损表征是一大难题。圆偏振拉曼光谱中的**拉曼光学活性 (ROA)** 提供了极佳的指纹：
*   在手性磁体 NiI2 中，电磁振子（磁振子与声子耦合的模式）在左旋和右旋圆偏振光激发下表现出截然不同的散射强度 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。
*   ROA 信号的极性（正或负）可以直接判定特定畴的手性对映体类型（左旋或右旋）。

## 🔬 手性磁电振荡

手性自旋序能够通过逆 Dzyaloshinskii–Moriya (IDM) 机制直接诱发铁电极化 $\vec{P}$，从而使得材料成为第二类多铁性体。
*   在飞秒泵浦下，手性畴内的电极化振荡与磁化振荡存在 $\pi/2$ 的固有相位差，产生了巨大的 THz 频段自然光学活性 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。

## 🏷️ 专业名词别名

- `chirality-in-magnetism`（concepts）
- `手性自旋结构`（concepts）

## 📚 相关论文 (Related Papers)

- [[../papers/songEvidenceSinglelayerVan2022]]：提供了在单层极限下稳定存在手性自旋螺旋及磁多铁性的证据。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：深入探讨了手性磁体中的动力学磁电耦合与巨自然光学活性。
- [[../papers/hanPolarTopologicalMaterials2025]]：综述极性拓扑材料（含电手性拓扑结构）的设计原理与器件前景。
- [[../papers/nahasFrustrationSelfOrderingTopological2016]]：阻挫驱动的自组织极性纳米结构与拓扑手性序。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[optical-activity|光学活性]]：手性最直接的宏观光学后果，手性介质对左/右旋圆偏振光响应不等价。
- [[raman-optical-activity|拉曼光学活性 ROA]]：本页所述手性畴无损表征的具体手段，圆偏振拉曼强度差直接读出对映体类型。
- [[electromagnon|电磁振子]]：手性磁体中磁振子与声子/极化耦合的激发，是手性磁电振荡的载体。
- [[dzyaloshinskii-moriya-interaction|Dzyaloshinskii–Moriya 相互作用]]：产生非共线手性自旋结构的微观根源；其逆过程（IDM）把手性自旋序转成铁电极化。
- [[helical-magnetism|螺旋磁性]]：磁手性的典型实现形式，自旋沿传播方向左旋或右旋。
- [[magnetoelectric-coupling|磁电耦合]]：手性自旋序经 IDM 机制诱发极化，使材料成为第二类多铁体。
- [[skyrmion|斯格明子]] 与 [[topological-defects|拓扑缺陷]]：拓扑手性的承载对象，自旋涡旋方向即其手性自由度。
- [[../entities/NiI2|NiI₂]]：本页螺旋磁序与 ROA 手性指纹的主要实验体系。
- [[../entities/TbMnO3|TbMnO₃]]：块体第二类多铁中磁手性与极化耦合的经典参照体系。
