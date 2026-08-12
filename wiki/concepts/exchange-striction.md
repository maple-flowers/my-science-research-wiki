---
tags: [concept, multiferroics, magnetism, ferroelectricity, mechanism, stub]
category: [D02]
title: 交换收缩 / Exchange Striction
type: concept
status: mature
domain: multiferroics
mechanism: 海森堡交换能对键长的依赖使不同自旋组态的键发生非对称伸缩，在共线 ↑↑↓↓ 等非公度磁序中打破反演对称而诱导极化
related_concepts: [type-ii-multiferroics, inverse-dzyaloshinskii-moriya, magnetoelectric-coupling, spin-spiral, multiferroicity]
aliases: ["Exchange Striction", "交换伸缩", "交换致伸缩"]
key_quantities:
  origin: "交换积分 J 依赖键长 d，自旋平行/反平行键平衡长度不同 → 非等距伸缩产生净偶极"
  contrast_DM: "不依赖强自旋-轨道耦合，能量尺度通常大于 DM 机制，可在共线磁序中生极"
  examples: "RMn2O5、Ca3CoMnO6 等共线 ↑↑↓↓ 磁序多铁"
papers: [cheongMultiferroicsMagneticTwist2007a, fiebigEvolutionMultiferroics2016, mostovoyMultiferroicsDifferentRoutes2024]
updated: 2026-08
---

# 交换收缩 / Exchange Striction

**交换收缩（Exchange Striction）** 是一种磁致铁电机制：海森堡交换积分 $J$ 对键长敏感（$J=J(d)$），自旋平行（↑↑）与反平行（↑↓）的键倾向于不同的平衡长度。当磁序为共线但非公度的 ↑↑↓↓ 等图案时，平行键与反平行键交替出现，它们的非对称伸缩使正负离子相对位移、打破空间反演对称，从而诱导出宏观电极化。它与依赖自旋-轨道耦合的 [[inverse-dzyaloshinskii-moriya|逆 DM/自旋电流]] 机制互补，可在**共线磁序**中产生铁电性 [[../papers/cheongMultiferroicsMagneticTwist2007a]]。

## 👵 太奶导读

太奶，前面说螺旋磁序靠"扭着转"挤出电方向。可还有一种情况，小磁针根本不转，全是直来直去地排队（这叫共线磁序），居然也能生出电来——靠的就是"交换收缩"。

道理是这样：两个相邻小磁针同向（头对头）和反向（头顶头）时，它们之间"弹簧"的最舒服长度不一样——同向时弹簧爱长一点，反向时爱短一点。要是磁针排成"同向、同向、反向、反向"（↑↑↓↓）这样的花样，长弹簧和短弹簧就交替出现，把整排原子拽得一会儿近一会儿远。这种不均匀的拉扯破坏了左右对称，正负电荷中心错开，就攒出一个电方向。因为它靠的是"交换作用"这股磁力让晶格收缩错位，所以叫交换收缩。它有个好处：不像螺旋机制那样非得靠强自旋-轨道耦合，劲儿通常还更大，是另一类"磁生电"的路子。

## 🏗️ 结构概览：键长调制生极

设键 $ij$ 上交换能为 $J_{ij}(d_{ij})\mathbf{S}_i\cdot\mathbf{S}_j$。由于 $\mathbf{S}_i\cdot\mathbf{S}_j$ 在平行键与反平行键上符号相反，使能量极小的平衡键长 $d_{ij}$ 也随自旋组态交替变化；这种自旋相关的周期位移叠加后若打破反演对称，即产生净极化 $P$。

![图：电荷/自旋有序诱导铁电的几种机制——其中 ↑↑↓↓ 共线自旋序经交换收缩导致键长二聚化而生极](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_1_D8A9TF3K.png)
*   **看图要点**：图中 ↑↑↓↓ 共线磁序使平行键与反平行键长度不同，形成非对称的键长调制（二聚化），无需螺旋或强自旋轨道耦合即可打破反演对称、产生极化 [[../papers/cheongMultiferroicsMagneticTwist2007a]]。
*   **来源**：[[../papers/cheongMultiferroicsMagneticTwist2007a]] -> [[../figures/crystal-structures|晶体结构]]

## 🧩 与逆 DM 机制的分工

- **交换收缩**：作用于共线（但非公度/有序图案）磁序，靠 Heisenberg 交换对键长的依赖，对自旋-轨道耦合要求低，极化可较大，典型如 $RMn_2O_5$、$Ca_3CoMnO_6$。
- **逆 DM / 自旋电流**：作用于非共线螺旋/摆线磁序，靠 $\mathbf{e}_{ij}\times(\mathbf{S}_i\times\mathbf{S}_j)$ 经 SOC 生极，是 TbMnO3、NiI2 等螺旋多铁的主因。

两者共同构成 [[type-ii-multiferroics|第二类多铁]]"磁序生极"的两大微观路径，并都体现强 [[magnetoelectric-coupling|磁电耦合]] [[../papers/fiebigEvolutionMultiferroics2016]]。

## 📊 两类磁感生铁电机制对照

| 维度 | 交换收缩 | 逆 DM / 自旋电流 |
| :--- | :--- | :--- |
| 磁序类型 | 共线（↑↑↓↓ 等非公度序） | 非共线螺旋/摆线 |
| 对 SOC 依赖 | 弱（主要靠 Heisenberg 交换） | 强（自旋-轨道耦合） |
| 生极方式 | 自旋相关键长调制/二聚化 | $\mathbf{P}\propto\mathbf{e}\times(\mathbf{S}_i\times\mathbf{S}_j)$ |
| 典型体系 | RMn2O5、Ca3CoMnO6 | TbMnO3、NiI2 |

## 📚 相关论文 (Related Papers)

- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：综述电荷/自旋有序铁电，含 ↑↑↓↓ 交换收缩机制。
- [[../papers/fiebigEvolutionMultiferroics2016]]：多铁性十年演变，梳理交换收缩与逆 DM 两类机制。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：多铁铁电性的不同微观路径。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[type-ii-multiferroics|第二类多铁]]、[[inverse-dzyaloshinskii-moriya|逆 DM 相互作用]]、[[magnetoelectric-coupling|磁电耦合]]、[[spin-spiral|自旋螺旋]]、[[multiferroicity|多铁性]]
