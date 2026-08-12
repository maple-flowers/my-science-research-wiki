---
tags: [concept, multiferroics, magnetism, ferroelectricity, mechanism, stub]
category: [D02]
title: 逆 DM 相互作用 / 自旋流模型 / Inverse DM (Spin-current) Mechanism
type: concept
status: mature
domain: multiferroics
mechanism: 非共线自旋经自旋-轨道耦合诱导电极化 P∝eij×(Si×Sj)，是螺旋/摆线磁序多铁的纯电子生极机制
related_concepts: [dzyaloshinskii-moriya-interaction, type-ii-multiferroics, spin-spiral, magnetoelectric-coupling, electromagnon, exchange-striction, multiferroicity]
aliases: ["逆Dzyaloshinskii-Moriya", "逆DM", "自旋电流模型", "spin-current model", "KNB模型"]
key_quantities:
  formula: "P_ij ∝ e_ij × (S_i × S_j)（Katsura–Nagaosa–Balatsky 自旋流模型）"
  dependence: "依赖自旋-轨道耦合，是纯电子机制（区别于声子/离子位移介导）"
  property: "翻转螺旋手性即翻转 P，本征强磁电耦合；典型 TbMnO3、NiI2"
papers: [gaoGiantChiralMagnetoelectric2024a, cheongMultiferroicsMagneticTwist2007a, fiebigEvolutionMultiferroics2016, mostovoyMultiferroicsDifferentRoutes2024, songEvidenceSinglelayerVan2022]
updated: 2026-08
---

# 逆 DM 相互作用 / 自旋流模型 (Inverse DM / Spin-current Mechanism)

**逆 DM（自旋流/自旋电流）机制** 是非共线磁序中由自旋-轨道耦合（SOC）直接诱导电极化的纯电子机制：对相邻非共线自旋 $\mathbf{S}_i$、$\mathbf{S}_j$，其键上产生的电极化方向为

$$\mathbf{P}_{ij}\propto \mathbf{e}_{ij}\times(\mathbf{S}_i\times\mathbf{S}_j)$$

其中 $\mathbf{e}_{ij}$ 为键方向单位矢量（Katsura–Nagaosa–Balatsky, KNB 模型）。当体系形成螺旋/摆线自旋序时，所有键的微电极大叠加不抵消，给出宏观极化；翻转螺旋手性即翻转 $\mathbf{P}$，故磁电耦合本征且强。它是 [[type-ii-multiferroics|第二类多铁]] 的核心生极机制之一 [[../papers/fiebigEvolutionMultiferroics2016]]。

## 👵 太奶导读

太奶，"逆 DM"这个名字听着唬人，其实说的就是一件事：歪歪扭扭的小磁针（非共线自旋）不用搬动原子，光靠相对论那点"自旋-轨道耦合"，就能凭空挤出一个电方向来，所以又叫"自旋电流模型"。

您想，两个相邻小磁针要是没对齐、叉开一个角度，它俩之间就像有一股悄悄流动的"自旋流"。这股流跟连接两磁针的方向一叉乘，就定出一个电的方向来。螺旋磁序里成千上万对磁针都这样叉着，各自的小电方向累加起来不抵消，就成了宏观的电极化。最妙的是这电方向完全由螺旋"往哪只手转"决定——把左手螺旋换成右手，电方向立马反过来。因此磁场只要拨转螺旋，就能翻电，耦合又直接又强。它跟"逆"字的关系是：普通 DM 相互作用是"结构的不对称导致自旋倾斜"，而这里反其道而行，是"自旋的不对称排布反过来产生电极化"，一正一逆。

## 🏗️ 结构概览：三矢量叉乘几何

电极化由三个方向共同决定：键方向 $\mathbf{e}_{ij}$、以及两个相邻自旋张成的平面法向 $\mathbf{S}_i\times\mathbf{S}_j$。在摆线螺旋中自旋在含传播矢量 $\mathbf{q}$ 的平面内旋转，$\mathbf{S}_i\times\mathbf{S}_j$ 沿螺旋旋转轴，叉乘 $\mathbf{e}_{ij}$ 后给出垂直于 $\mathbf{q}$ 与旋转轴的极化，满足 $\mathbf{P}\propto\mathbf{q}\times\mathbf{e}$。这把"螺旋手性 → 极化方向"写成了明确的几何关系。

![图：非共面 120° Y 型螺旋磁结构打破空间反演对称，沿 e×(Si×Sj) 方向产生电极化 P](../../raw/figures/huProgressProspectsLowdimensional2019/fig_7_ACL4KQI9.png)
*   **看图要点**：自旋两两叉开、叉乘不为零且方向一致，沿 $\mathbf{e}_{ij}\times(\mathbf{S}_i\times\mathbf{S}_j)$ 方向长出净极化；手性反转则叉乘反向、P 翻转，这是逆 DM/自旋流生极的几何来源 [[../papers/huProgressProspectsLowdimensional2019]]。
*   **来源**：[[../papers/huProgressProspectsLowdimensional2019]] -> [[../figures/crystal-structures|晶体结构]]

## 🧩 与（正）DM 及交换收缩的区别

- **正 DM 相互作用**（[[dzyaloshinskii-moriya-interaction|DM]]）：破缺反演的结构中 $\mathbf{D}\cdot(\mathbf{S}_i\times\mathbf{S}_j)$ 偏好非共线自旋，造成自旋倾斜/弱铁磁并稳定斯格明子——是"结构不对称→自旋倾斜"。
- **逆 DM（本页）**：非共线自旋排布经 SOC 反过来产生电极化——是"自旋不对称→生极"。
- **[[exchange-striction|交换收缩]]**：靠 Heisenberg 交换对键长的依赖、在共线 ↑↑↓↓ 序中靠离子位移生极，对 SOC 依赖弱；逆 DM 则是不依赖离子位移的纯电子机制。

![图：NiI2 的左右手性自旋螺旋与面内诱导极化 P——螺旋手性直接决定 P 方向](../../raw/figures/gaoGiantChiralMagnetoelectric2024a/fig_1_8V5GWLM9.png)
*   **关键特征**：图中 q=(0.138a*,0,1.457c*) 的螺旋经逆 DM 关系诱导沿 y（C2 轴）的面内极化，左/右手螺旋给出相反 P，对应实验观测到的手性电磁振子与磁电响应 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。
*   **来源**：[[../papers/gaoGiantChiralMagnetoelectric2024a]] -> [[../figures/optical-spectra|光学光谱]]

## 📊 磁致生极机制对照

| 维度 | 逆 DM / 自旋流 | 交换收缩 |
| :--- | :--- | :--- |
| 磁序 | 非共线螺旋/摆线 | 共线 ↑↑↓↓ 等非公度序 |
| 微观来源 | SOC，纯电子极化 | Heisenberg 交换对键长依赖，离子位移 |
| 极化方向 | $\mathbf{P}\propto\mathbf{e}\times(\mathbf{S}_i\times\mathbf{S}_j)$ | 由键长调制方向决定 |
| 典型体系 | TbMnO3、NiI2 | RMn2O5、Ca3CoMnO6 |

## 📚 相关论文 (Related Papers)

- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：NiI2 手性螺旋的逆 DM 极化与电磁振子。
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：磁致铁电物理与逆 DM/交换收缩机制综述。
- [[../papers/fiebigEvolutionMultiferroics2016]]：多铁性演变与磁电耦合。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：多铁铁电性的不同微观路径。
- [[../papers/songEvidenceSinglelayerVan2022]]：单层 NiI2 本征 II 型多铁的光学证据。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[dzyaloshinskii-moriya-interaction|Dzyaloshinskii–Moriya 相互作用]]、[[type-ii-multiferroics|第二类多铁]]、[[spin-spiral|自旋螺旋]]、[[magnetoelectric-coupling|磁电耦合]]、[[electromagnon|电磁振子]]、[[exchange-striction|交换收缩]]、[[multiferroicity|多铁性]]
- [[../entities/NiI2|NiI2]]
