---
tags: [entity, material, multiferroic, perovskite, type-ii]
title: 锰酸铽 / Terbium Manganite (TbMnO3)
type: entity
status: developing
formula: TbMnO3
class: [perovskite, multiferroic, insulator]
properties: [multiferroicity, ferroelectricity, spiral-magnetism, magnetoelectric-coupling]
key_quantities:
  Tn: "~41 K"
  polarization: "~0.08 uC/cm2"
related_entities: [BiFeO3, RMnO3-orthorhombic, RMn2O5]
papers: [cheongMultiferroicsMagneticTwist2007a, fiebigEvolutionMultiferroics2016, rameshMultiferroicsProgressProspects2007, spaldinRenaissanceMagnetoelectricMultiferroics2005]
updated: 2026-08-18
---

# 锰酸铽 / Terbium Manganite (TbMnO3)

正交锰酸铽（TbMnO₃）是 II 型多铁（Type-II Multiferroic）最经典的模型材料之一。其铁电性并非源于传统离子位移，而是由非共线螺旋磁序在约 41 K 以下"诱导"产生：磁性首先破缺空间反演对称性，进而驱动晶格弛豫形成电极化。2003 年实验发现其电极化可被外磁场剧烈调控（90° 极化翻转、约 500% 巨磁介电效应），拉开了"磁序诱导铁电"这一新范式的序幕。

## 👵 太奶导读

乖孙，TbMnO₃ 是个"用磁场指挥电"的典型例子。一般铁电材料靠离子的规则排列来产生电，但 TbMnO₃ 不一样——它靠的是磁性"拧成麻花"（螺旋磁序）来挤出一点电。它的电很弱，但有个独门绝技：你给它加个磁场，它产生的电方向会整体转个弯（90° 翻转）。这就像用一块磁铁在远处一挥手，就能让一条电线里的电流方向改变。科学家们正是从它身上学到了"用磁来管电"的本事，想用来做特别省电的存储器。

## 🏗️ 结构概览

- **晶体结构**：正交钙钛矿（Pbnm），Mn³⁺ 处于氧八面体中心，A 位为 Tb³⁺。
- **磁结构演化**：随降温经历顺磁 → 正弦共线反铁磁（~41 K）→ 螺旋磁序（~28 K）两个转变。
- **铁电出现**：螺旋磁序打破空间反演对称性，约 28 K 以下出现自发极化。

## 🧩 磁致铁电机制

TbMnO₃ 的电极化来自磁阻挫体系中的"磁序诱导非本征铁电"（cheongMultiferroicsMagneticTwist2007a）：

- **逆 Dzyaloshinskii–Moriya（自旋流）机制**：非共线螺旋磁序中，相邻自旋之间的 DM 相互作用等效于一个"自旋流"，使氧离子发生位移，从而产生垂直于自旋旋转轴和波矢方向的极化，遵循方向定则 $\mathbf{P} \parallel \mathbf{e}_3 \times \mathbf{Q}$（$\mathbf{e}_3$ 为自旋旋转轴，$\mathbf{Q}$ 为螺旋波矢）。
- **磁场调控**：外加磁场可使螺旋序重新取向，导致电极化 90° 翻转或 180° 可逆翻转；约 5 T 磁场下即可实现极化方向翻转。
- **弱极化**：磁致极化约 $10^{-2}$ μC/cm² 量级，比传统铁电体小 2–3 个数量级，但磁场可调性前所未有。

在 fiebigEvolutionMultiferroics2016 的 I/II 类多铁分类中，o-TbMnO₃ 是自旋驱动（II 类）机制的代表，而自旋驱动正是实现强磁电耦合的关键路径；在薄膜与异质结架构下，TbMnO₃ 等 II 类材料也用于研究电场调控磁性（rameshMultiferroicsProgressProspects2007）。

## 📚 相关论文 (Related Papers)

- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：系统阐述"磁阻挫 → 螺旋磁序 → 磁致铁电"范式，TbMnO₃ 为最核心案例，给出逆 DM 与交换伸缩机制及 $\mathbf{P} \parallel \mathbf{e}_3 \times \mathbf{Q}$ 定则。
- [[../papers/fiebigEvolutionMultiferroics2016]]：将 TbMnO₃ 列为 II 类（自旋驱动）多铁机制的代表材料。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：从薄膜多铁角度讨论磁致铁电材料的薄膜化与异质结构路线。
- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]：提供多铁性复兴与"磁电互斥"理论背景，TbMnO₃ 是绕开禁忌的案例之一。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/type-ii-multiferroicity|II 型多铁性]]
- [[../concepts/multiferroicity|多铁性]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../entities/BiFeO3|BiFeO₃（I 型室温多铁参照）]]
- [[../entities/RMn2O5|RMn₂O₅（交换伸缩机制多铁）]]
