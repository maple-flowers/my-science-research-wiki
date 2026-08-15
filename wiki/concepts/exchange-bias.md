---
tags: [concept, magnetism]
title: 交换偏置 / Exchange Bias
type: concept
status: mature
domain: [condensed-matter-physics, magnetism]
mechanism: 铁磁/反铁磁界面处的交换相互作用导致磁滞回线发生水平漂移
related_concepts: [magnetoelectric-coupling, multiferroicity, neel-temperature, Curie-temperature]
updated: 2026-08
papers: [rameshMultiferroicsProgressProspects2007, fiebigEvolutionMultiferroics2016, mostovoyMultiferroicsDifferentRoutes2024, tangMultiferroicityTwodimensionalVan2025, spaldinAdvancesMagnetoelectricMultiferroics2019]
---

# 交换偏置 / Exchange Bias
交换偏置 (Exchange Bias) 是一种界面磁现象，通常发生在铁磁 (FM) 层与反铁磁 (AFM) 层接触的界面处。表现为铁磁层的磁滞回线沿磁场轴发生水平偏移，并伴随矫顽力的增加。它是现代读写磁头中磁锚定的核心技术。
## 👵 太奶导读
乖孙，这“交换偏置”就像是给一群不听话的小人儿找了个“严厉的班主任”。
铁磁层的小人儿平时虽然听话，但一旦外界诱惑（磁场）太强，他们就容易跟着跑。
这时候我们在旁边贴上一层反铁磁材料（班主任）。反铁磁的小人儿特别死板，他们定住了就不动。因为两层紧挨着，铁磁的小人儿就被班主任“拽住”了。
结果就是，你想把这群小人儿往左边带，得费比往右边带更大的劲。这种“不平衡”就是交换偏置，它能让数据存得稳稳当当，不怕磁场乱搅和。
## 🏗️ 结构概览：多铁异质结中的界面交换偏置
在多铁异质结中，交换偏置常被用于实现电场对磁性的锁定。
![图：BiFeO3/CoFeB 界面处的交换偏置示意](../../raw/figures/prosandeevKittelLawInBiFeO3Ultrathin2010/eq_1_QC77D3EP.png)
*   **看图要点**：BiFeO₃ 作为反铁磁层，其表面自旋与铁磁层自旋通过交换作用耦合。改变铁电极化可联动改变界面反铁磁序，从而移动铁磁层的磁滞回线。
*   **来源**：[[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]] -> [[../figures/mathematical-models-magnetoelectric]]
*(注：引用 Ramesh 2007 综述中关于 BFO 交换偏置的经典物理描述)*
## 🧩 物理模型与参数
交换偏置场 $H_{eb}$ 定义为磁滞回线中心相对于原点的偏移量。
$$ H_{eb} = \frac{J_{int}}{M_{FM} t_{FM}} $$
其中：
- $J_{int}$：界面交换耦合强度。
- $M_{FM}, t_{FM}$：铁磁层的饱和磁化强度和厚度。
关键条件：必须经过磁场冷却 (Field Cooling) 过程，跨越反铁磁层的尼尔温度，使界面自旋排列锁定。
## 📚 相关论文 (Related Papers)
- [[../papers/rameshMultiferroicsProgressProspects2007]]：详细讨论了在 BiFeO₃ 薄膜异质结中利用交换偏置实现电控磁的蓝图。
- [[../papers/fiebigEvolutionMultiferroics2016]]：阐述了多铁性材料中交换偏置的动力学特性。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：分析了新型范德华多铁界面处的交换偏置效应。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]
## 🔗 关联概念与实体 (Related Concepts & Entities)
- [[../concepts/magnetoelectric-coupling|磁电耦合]]（应用目标）
- [[../concepts/neel-temperature|尼尔温度]]（锁定温度）
- [[../entities/BiFeO3|BiFeO₃]]（最常用的反铁磁/多铁锁定层）
- [[../entities/Fe3GeTe2|Fe₃GaTe₂]]（常作为被锁定的铁磁层）
