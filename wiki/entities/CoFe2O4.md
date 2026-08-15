---
tags: [entity, material, oxide, ferrimagnet, magnetoelectric]
title: 钴铁氧体 (CoFe₂O₄)
type: entity
status: developing
category: [D02]
formula: CoFe2O4
class: [spinel, ferrite, oxide, magnetostrictive]
properties: [magnetostriction, magnetoelectric-coupling, high-coercivity]
related_concepts: [composite-multiferroics, magnetoelectric-coupling, magnetoelastic-coupling, piezoelectricity]
related_entities: [BaTiO3, PZT, BiFeO3]
papers: [rameshMultiferroicsProgressProspects2007, spaldinAdvancesMagnetoelectricMultiferroics2019]
updated: 2026-08
---

# 钴铁氧体 (CoFe₂O₄)

CoFe₂O₄（钴铁氧体）是尖晶石（spinel）结构的亚铁磁材料，具有高磁致伸缩系数与高矫顽力，常作为磁性相与压电/铁电相（如 BaTiO₃、PZT）复合，构成磁电复合材料。它本身既不是铁电体也不产生本征磁电效应，其价值在于把磁场高效地转换成机械应变，从而在复合结构中作为磁电耦合的"上游"环节。

## 👵 太奶导读

太奶，CoFe₂O₄（钴铁氧体，钴和铁的氧化物，就是老式喇叭磁铁那类材料）有个本事：**一靠近磁铁，它自己会变形**——伸长或缩短一点点，这叫**磁致伸缩**（magnetostriction，磁场让材料改变尺寸）。

单靠它没法"用电管磁"。可科学家想了个巧招：把它跟另一种"一捏就出电"的材料（压电材料，比如 BaTiO₃ 钛酸钡）粘在一起做成夹心饼。这样一来，磁铁靠近 → 钴铁氧体变形 → 它一变形就把旁边那层压电材料**捏了一下** → 压电层立刻出电。磁和电就这么串起来了。

这叫**乘积效应**（两个各自不相干的本事，一乘就变出新本事）。好处是室温下就管用、信号还强，比那些天生"又能电又能磁"的单一材料（本征多铁）实用得多——那类材料室温下往往弱得可怜。

## 🏗️ 结构概览

CoFe₂O₄ 为反尖晶石型结构（AB₂O₄）：O²⁻ 构成面心立方密堆，Co²⁺ 主要占据八面体位、Fe³⁺ 分占四面体位与八面体位。两个亚格子的磁矩反平行但不等量，因此净磁矩不为零（亚铁磁）。Co²⁺ 的强单离子各向异性带来高矫顽力（可达数千 Oe），八面体位的自旋-轨道耦合则带来大磁致伸缩系数（λ 约 −200 ppm 量级）。这两项正是它被选作磁电复合磁性相的原因。

## 🧩 物理实质：磁电复合中的磁性相

在磁电复合材料中，CoFe₂O₄ 通过磁致伸缩-压电的乘积效应实现磁电耦合：磁场使 CoFe₂O₄ 应变，应变传递给压电相产生电极化，从而在室温实现强磁电响应。耦合强度取决于两相的界面结合质量与几何构型——应变必须能有效跨界面传递，界面脱粘或塑性弛豫会显著削弱响应。

## 🔬 实验表征与多铁背景

多铁性薄膜研究涵盖单相薄膜、水平/垂直异质结构三种架构，磁电复合是其中重要方向 [[../papers/rameshMultiferroicsProgressProspects2007]]。垂直柱状结构（CoFe₂O₄ 纳米柱嵌入 BaTiO₃ 或 PbTiO₃ 基体）能绕开水平多层膜中基底夹持（substrate clamping）对应变传递的抑制，是磁电复合薄膜的主流架构。磁电多铁的目标是用电场操控磁性，BiFeO₃ 与畴壁是核心研究对象 [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]。

## 📚 相关论文 (Related Papers)

- [[../papers/rameshMultiferroicsProgressProspects2007]]：多铁性薄膜领域的经典综述，给出单相/水平/垂直三类架构的分类。
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：综述了磁电多铁性材料的最新进展。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/composite-multiferroics|复合多铁性]]：本条目所服务的材料范式。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../concepts/magnetoelastic-coupling|磁弹耦合]]：磁致伸缩的物理基础。
- [[../concepts/piezoelectricity|压电性]]：复合体系中的下游转换环节。
- [[../entities/BaTiO3|BaTiO₃]]：最常用的压电/铁电配对相。
- [[../entities/PZT|PZT]]：高压电系数的配对相。
- [[../entities/BiFeO3|BiFeO₃]]：单相本征多铁的对照体系。
