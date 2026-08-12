---
tags: [concept, multiferroics, magnetism, ferroelectricity, mechanism]
title: 第一类多铁 / Type-I Multiferroics
type: concept
status: mature
category: [D02]
domain: multiferroics
mechanism: 铁电性与磁性来自不同结构/化学单元，两者来源独立、共存于同一相
related_concepts: [type-ii-multiferroics, magnetoelectric-coupling, multiferroicity, lone-pair-ferroelectricity]
aliases: ["I型多铁", "Type-I Multiferroics", "第一类多铁性"]
key_quantities:
  coupling: "磁电耦合通常较弱（磁、电独立起源），但极化往往较大"
  ferroelectric_origins: "孤对电子（BiFeO3）、几何/电荷有序、非共线自旋以外的结构极性"
  examples: "BiFeO3（最典型室温多铁）、部分六方锰氧化物；二维中多以铁磁/铁电异质结实现"
papers: [cheongMultiferroicsMagneticTwist2007a, hillWhyAreThere2000a, FerroelectricityMultiferroicityAtomic2023]
updated: 2026-08
---

# 第一类多铁 / Type-I Multiferroics

**第一类多铁（Type-I Multiferroics）** 指铁电性与磁性在同一材料中共存、但**二者起源相互独立**的多铁体：铁电极化通常来自结构/化学极性（如 Bi³⁺/Pb²⁺ 的孤对电子、几何失稳、电荷有序），而磁性来自另一组磁性离子的自旋有序。由于铁电与磁序并非彼此驱动，**磁电耦合一般较弱**，但优点是极化往往较大、且铁电与磁转变温度可以分别很高（典型如 BiFeO3，室温以上同时铁电与反铁磁）[[../papers/cheongMultiferroicsMagneticTwist2007a]] [[../papers/hillWhyAreThere2000a]]。这与"磁序直接生极、强耦合但小极化"的 [[type-ii-multiferroics|第二类多铁]] 形成对照。

## 👵 太奶导读

太奶，上一条说"第二类多铁"是磁把电给逼出来的，磁电绑得死。这"第一类"正好反过来：它是一个院子里住了两户人家，一户管电、一户管磁，各有各的来历，碰巧住在同一所房子里。

管电的那户，常常是因为某种原子（比如铋）外层留着一对"懒得成键"的电子（叫孤对电子），把屋子撑得不对称了，就有了电的方向；管磁的那户，则是另一群带磁性的金属离子（比如铁）各带小磁针。两户互不使唤，所以想靠磁去扳动电、或用电去扳动磁，劲儿就不大——这就是"耦合弱"。但好处也明显：电方向那户力气大、温度高（能在室温站住），磁那户也耐高温。最有名的是铋铁氧 BiFeO3，常温下两样都有。在二维材料里，纯靠本征做到第一类多铁的很少，更常见的法子是把一片铁磁薄片和一片铁电薄片贴在一起，用界面"牵线搭桥"来补这耦合，那叫人工多铁异质结。

## 🧩 独立起源与典型机制

- **孤对电子驱动**：Bi³⁺、Pb²⁺ 等离子的 6s² 孤对电子导致配位多面体发生偏心位移，产生大极化，磁性由 Fe³⁺、Mn³⁺ 等过渡金属离子另提供。BiFeO3 是范例：室温铁电（$T_C\sim1100$ K）+ 反铁磁（$T_N\sim640$ K）。
- **几何与电荷有序**：某些体系中离子尺寸失配或电荷/轨道有序破缺反演对称而生极，磁性另有来源。
- **非共线自旋以外的结构极性**：与第二类不同，这里的极性不依赖磁序是否破缺反演对称，因此铁电转变可远高于磁转变温度。

由于两个序参量来源不同，第一类多铁的磁电耦合多为次级效应（通过应变、自旋-轨道耦合或界面传递），通常弱于第二类的本征强耦合 [[../papers/hillWhyAreThere2000a]]。

![图：电荷有序与几何失稳诱导铁电极化的几种第一类多铁机制——(a)位点/键中心电荷序共存，(b)↑↑↓↓ 自旋序经交换收缩生极，(c)LuFe2O4 双层电子铁电体，(d)YNiO3 中自旋-电荷序耦合](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_1_D8A9TF3K.png)
*   **看图要点**：这些生极机制（电荷有序、几何/电子铁电性）依赖结构与电荷排布，而非磁序本身破缺反演对称；磁性由另一组离子提供，因此铁电与磁独立共存、耦合较弱 [[../papers/cheongMultiferroicsMagneticTwist2007a]]。
*   **来源**：[[../papers/cheongMultiferroicsMagneticTwist2007a]] -> [[../figures/crystal-structures|晶体结构]]

## 🎯 二维语境：本征稀缺与人工异质结

在二维范德华体系中，单一材料同时具备独立铁电与铁磁序的例子稀少，实践中更常用**异质结工程**逼近第一类多铁功能：把铁磁二维材料（如 Cr2Ge2Te6、CrI3）与铁电二维材料（如 In2Se3）堆叠，借界面磁电耦合实现"电写磁"或"磁读电"。这种人工多铁中磁、电仍来自不同层，思路上延续了第一类"独立起源 + 界面耦合"的范式（详见 [[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]、[[../entities/CrInTe2|CrInTe2]] 条目）[[../papers/FerroelectricityMultiferroicityAtomic2023]]。

## 📊 两类多铁对照

| 维度 | 第一类多铁 | 第二类多铁 |
| :--- | :--- | :--- |
| 极化起源 | 独立的结构/化学极性单元 | 磁序破缺反演对称 |
| 磁电耦合 | 较弱（次级/界面） | 本征、强 |
| 极化大小 | 往往较大 | 一般较小 |
| 转变温度 | 铁电、磁可分别很高 | 受磁序温度限制 |
| 典型体系 | BiFeO3、六方锰氧化物 | TbMnO3、NiI2、CuCrP2S6 |

## 📚 相关论文 (Related Papers)

- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：经典综述，阐明两类多铁的划分与"磁致铁电"物理。
- [[../papers/hillWhyAreThere2000a]]：从化学/对称性角度讨论为何磁性铁电体稀少（第一类多铁的起源约束）。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：原子级厚度多铁综述，讨论二维本征多铁稀缺与异质结策略。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[multiferroicity|多铁性]]、[[type-ii-multiferroics|第二类多铁]]、[[magnetoelectric-coupling|磁电耦合]]、[[lone-pair-ferroelectricity|孤对电子铁电性]]
- [[../entities/BiFeO3|BiFeO3]]（第一类多铁标杆）、[[../entities/In2Se3|In2Se3]]、[[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]（人工多铁异质结组元）
