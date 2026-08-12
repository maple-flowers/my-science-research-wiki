---
tags: [concept, multiferroics, magnetism, ferroelectricity, mechanism, 2D-materials]
title: 第二类多铁 / Type-II Multiferroics
type: concept
status: mature
category: [D02]
domain: multiferroics
mechanism: 磁序本身破缺空间反演对称而诱导铁电极化，磁与电本征强耦合
related_concepts: [type-i-multiferroics, magnetoelectric-coupling, spin-spiral, inverse-dzyaloshinskii-moriya, exchange-striction, electromagnon, multiferroicity]
aliases: ["磁感生多铁", "Type-II Multiferroics", "magnetically induced ferroelectricity"]
key_quantities:
  coupling: "磁电耦合强，但极化通常较小（~10⁻²–10² μC/m² 量级）"
  mechanism_models: "自旋电流模型 / 逆 DM 相互作用（螺旋磁序）；交换收缩（共线非公度磁序）"
  examples: "TbMnO3（块体经典）、NiI2（单层本征 2D II 型多铁）、CuCrP2S6"
papers: [FerroelectricityMultiferroicityAtomic2023, huProgressProspectsLowdimensional2019, wuCoexistenceFerroelectricityAntiferroelectricity2024, songEvidenceSinglelayerVan2022]
updated: 2026-08
---

# 第二类多铁 / Type-II Multiferroics

**第二类多铁（Type-II Multiferroics，磁感生多铁）** 指铁电极化并非来自独立的结构畸变，而是**由磁序本身破缺空间反演对称性所诱导**的多铁材料。由于极化完全由自旋排布"驱动"，磁序与电极化之间存在**本征的强磁电耦合**——翻转螺旋手性或磁场改变磁结构即可翻转极化。代价是极化值通常很小。典型机制包括螺旋/摆线自旋序经自旋电流（逆 DM）机制生极，以及共线非公度磁序经交换收缩生极；块体经典如 TbMnO3，二维代表为单层 NiI2 与 CuCrP2S6 [[../papers/FerroelectricityMultiferroicityAtomic2023]]。

## 👵 太奶导读

太奶，"多铁"是说一块材料同时有磁和电两样本事，还能互相使唤。这里头分两派。"第二类"这一派的特点是：电的方向完全是被磁给"逼"出来的，磁是因、电是果。

您把它想成一群跳集体舞的小磁针。要是它们齐刷刷排成直线，左右对称，就生不出电的方向；可要是它们像螺丝纹那样螺旋着、歪歪扭扭地转（这叫螺旋磁序），这螺旋还有"左右手"之分，对称就被打破了，硬逼出一个电的方向来。螺旋换个手转，电的方向立马跟着翻——所以磁和电绑得特别死，这就是"强磁电耦合"。也正因为这电方向是磁"顺带"挤出来的，劲儿一般不大。拿二维的 NiI2（碘化镍）来说，它单层里就是这种有手性的螺旋磁序生的电，科学家用光和电同时看到了它的磁畴和电畴。跟它对照的是"第一类"多铁，那边磁和电各有各的来源、凑在一块，耦合反而弱。

## 🧩 生极机制

![图：第二类多铁的作动原理——非共面 120° Y 型螺旋磁结构打破空间反演对称，产生垂直螺旋平面的电极化 P](../../raw/figures/huProgressProspectsLowdimensional2019/fig_7_ACL4KQI9.png)
*   **看图要点**：非共线、非共面的自旋排布（带手性）使体系失去反演中心，沿特定方向长出电极化 P；极化方向由螺旋手性决定，因此翻磁即翻电，是本征强耦合的几何来源 [[../papers/huProgressProspectsLowdimensional2019]]。
*   **来源**：[[../papers/huProgressProspectsLowdimensional2019]] -> [[../figures/crystal-structures|晶体结构]]

第二类多铁的微观生极模型主要有两类：

- **自旋电流 / 逆 DM 机制**：在螺旋、摆线等非共线自旋序中，相邻自旋叉乘 $\mathbf{e}_{ij}\cdot(\mathbf{S}_i\times\mathbf{S}_j)$ 不为零，经自旋-轨道耦合产生沿 $\mathbf{e}_{ij}\times(\mathbf{S}_i\times\mathbf{S}_j)$ 的局域电极化。螺旋手性反转则极化反转。NiI2 单层的正螺旋自旋序即属此类 [[../papers/songEvidenceSinglelayerVan2022]]。
- **交换收缩（exchange-striction）**：在共线但非公度的磁序中，自旋相关的键长调制破坏反演对称而生极，可不依赖强自旋轨道耦合。

## 🔬 二维范例：NiI2 与铁电/反铁电共存

![图：三层 NiI2 的晶体结构、器件构型与磁性/铁电表征（磁-光-电联合测量）](../../raw/figures/wuCoexistenceFerroelectricityAntiferroelectricity2024/fig_2_MJWI3AEA.png)
*   **关键特征**：以三层 NiI2 为平台，研究团队用铁电测试仪在不同频率下直接测得电滞回线，首次在少层范德华材料中同时、直接地观测到铁电（FE）与反铁电（AFE）共存，并用 DFT 与原子级自旋模拟把宏观电信号追溯到螺旋磁序，证实其 II 型多铁起源 [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]。
*   **来源**：[[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]] -> [[../figures/domain-walls|畴与畴壁]]

二维 II 型多铁的意义在于把强磁电耦合推进到原子级厚度：单层 NiI2 的手性螺旋磁序在 $T_c\approx21$ K 同步产生磁序与极化（见 [[../entities/NiI2|NiI2 条目]]）；CuCrP2S6 则是少数层中磁序破缺反演对称而生极的另一代表。光学上，磁手性基态常伴随**电磁子（electromagnon）**这一动态磁电耦合指纹。

## 📊 两类多铁对照

| 维度 | 第二类多铁 | 第一类多铁 |
| :--- | :--- | :--- |
| 极化起源 | 磁序破缺反演对称 | 独立的结构/化学极性单元 |
| 磁电耦合 | 本征、强 | 通常较弱（磁、电来源独立） |
| 极化大小 | 一般较小 | 往往较大 |
| 典型体系 | TbMnO3、NiI2、CuCrP2S6 | BiFeO3、部分异质结人工多铁 |
| 调控方式 | 磁场翻转磁结构即翻电极化 | 多需应变/异质结界面耦合 |

## 📚 相关论文 (Related Papers)

- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：综述原子级厚度多铁，区分 I/II 型并以 NiI2、CuCrP2S6 为 II 型范例。
- [[../papers/huProgressProspectsLowdimensional2019]]：低维铁电/多铁综述，图 7 给出第二类多铁非共线磁序生极原理。
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]：三层 NiI2 中铁电与反铁电共存的直接电学证据及其螺旋磁序起源。
- [[../papers/songEvidenceSinglelayerVan2022]]：首次以光学手段证实单层 NiI2 的本征 II 型多铁性。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[type-i-multiferroics|第一类多铁]]、[[magnetoelectric-coupling|磁电耦合]]、[[spin-spiral|螺旋自旋序]]、[[inverse-dzyaloshinskii-moriya|逆 DM 相互作用]]、[[exchange-striction|交换收缩]]、[[electromagnon|电磁子]]、[[multiferroicity|多铁性]]
- [[../entities/NiI2|NiI2]]（单层本征 II 型多铁标杆）、[[../entities/CuCrP2S6|CuCrP2S6]]（少层 II 型多铁）
