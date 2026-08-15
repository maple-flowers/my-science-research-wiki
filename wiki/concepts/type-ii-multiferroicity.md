---
tags: [concept, multiferroics, magnetism]
title: 第二类多铁性 / Type-II Multiferroicity
type: concept
status: mature
domain: [condensed-matter-physics, multiferroics]
mechanism: 磁有序（特别是螺旋/摆线磁序）自发打破反演对称性并诱导铁电极化，极化与磁序内禀强耦合
related_concepts: [multiferroicity, magnetoelectric-coupling, spin-helix, improper-electronic-ferroelectricity, dzyaloshinskii-moriya-interaction]
papers: [songEvidenceSinglelayerVan2022, fiebigEvolutionMultiferroics2016, cheongMultiferroicsMagneticTwist2007a, aminiAtomicscaleVisualizationMultiferroicity2024, wuCoexistenceFerroelectricityAntiferroelectricity2024, FerroelectricityMultiferroicityAtomic2023, RecentAdvancesGrowth2025, huProgressProspectsLowdimensional2019]
updated: 2026-08
---

# 第二类多铁性 / Type-II Multiferroicity

第二类多铁性（Type-II Multiferroicity，亦称磁诱导多铁性）是指材料的铁电极化并非起源于结构上的自发畸变，而是由某种特定的磁有序（通常是打破空间反演对称性的非共线磁序，如螺旋磁序或摆线磁序）直接驱动产生的现象。由于极化与磁性序参量具有相同的物理起源，这类材料通常表现出极强的内禀磁电耦合效应。

## Grandma 👵 太奶导读

太奶，这“第二类多铁性”就像是一支**跳出来的舞**。
在“第一类多铁”里，材料原本就是个铁电体（家里有现成的电箭头），只不过刚好它也带点磁性，两者各过各的。
但“第二类多铁”就神奇了，材料原本是不带电（非铁电）的。
可只要里面的磁性小箭头（自旋）开始按某种奇怪的节奏**跳起螺旋舞**（螺旋磁序），这支舞跳得太快、太扭，就把材料里的电荷给扭歪了。电荷一歪，铁电极化就这么“跳”了出来。
因为这电完全是靠磁跳舞带出来的，所以你只要改改磁铁跳舞的姿势，电信号就会跟着发生翻天覆地的变化，这叫强耦合。虽然这种材料一般要在特别冷的地方才跳得动，但它的控制效率是最高的。

## 🧩 微观机制：自旋流与逆 DM 相互作用

第二类多铁性的极化 $P$ 通常由以下几种机制驱动：

1.  **自旋流（Spin Current）模型 / 逆 DM 相互作用**：
    对于相邻的非共线自旋 $\mathbf{S}_i$ 和 $\mathbf{S}_j$，产生的极化正比于自旋积：
    $$\mathbf{P}_{ij} \propto \mathbf{r}_{ij} \times (\mathbf{S}_i \times \mathbf{S}_j)$$
    其中 $\mathbf{r}_{ij}$ 是连接两个磁性位点的矢量。这种机制在摆线磁序（Cycloidal order）中最为常见。
2.  **广义自旋流模型 (gKNB Model)**：
    对于像 NiI₂ 这样的正螺旋（Proper-screw）磁序，极化由更复杂的张量耦合 $M$ 产生：
    $$\mathbf{P}_{ij} = \mathbf{M} \cdot (\mathbf{S}_i \times \mathbf{S}_j)$$
    即使在正螺旋磁序中，只要磁对称性允许，也能产生可观测的铁电极化。

## 🔬 特征与范例

*   **强磁电耦合**：极化强度通常较小（$10^{-5}\text{--}10^{-3}\ \mu\text{C/cm}^2$），但对磁场极其敏感，可用磁场实现极化翻转。
*   **非本征铁电性**：极化转变温度 $T_C$ 始终等于（或低于）磁相变温度 $T_N$。
*   **代表材料**：
    *   **块体**：$TbMnO_3$（原型材料）、$LiCuVO_4$。
    *   **二维**：[[../entities/NiI2|NiI₂]]（首个实验证实的单层第二类多铁体）。

## 🧪 实验表征与最新进展

**三层 NiI₂ 的直接电学证实**：将三层 NiI₂ 封装于石墨烯/hBN"三明治"器件中，利用自主研发的磁-光-电联合测量系统（MOEJSI，低温 10 K、强磁场 ±7 T）原位测量，首次在二维极限下通过 P-E 电滞回线直接证实铁电与反铁电共存；铁电性源于螺旋磁序的 KNB 机制（P ∝ e × q），手性畴交错排列产生反铁电性，磁场可调控铁电畴翻转 [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]。

**原子厚度极限下的多铁**：铁电与多铁性可在单原子层实现，三类体系互补——钙钛矿氧化物（PbTiO₃、BiFeO₃）提供模型系统、氧化铪（Hf₀.₈Zr₀.₂O₂）与 CMOS 兼容、范德华材料凭借堆叠工程成为设计平台 [[../papers/FerroelectricityMultiferroicityAtomic2023]]。

**低维多铁的理论与实验路径**：DFT 第一性原理预测极化大小、翻转势垒与居里温度，MBE、PFM、STEM、SHG 与电输运测量用于证实二维铁电/多铁性 [[../papers/huProgressProspectsLowdimensional2019]]。

**二维多铁生长与表征**：单层 NiI₂、Cr₂S₃、CuCrSe₂ 等可通过 CVD、PVD、MBE、ALD 生长，用 STM、SHG、拉曼、双折射、TEM 等确认多铁序与磁电耦合 [[../papers/RecentAdvancesGrowth2025]]。

## 📚 相关论文 (Related Papers)

- [[../papers/songEvidenceSinglelayerVan2022]]：在单层 NiI₂ 中证实了由螺旋磁序驱动的本征第二类多铁性。
- [[../papers/fiebigEvolutionMultiferroics2016]]：系统总结了多铁性分类及第二类多铁性的物理图像。
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]：在单层 NiI₂ 中原位可视化多铁性。
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：首次系统阐述了磁扭曲诱导铁电性的物理图像。
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]：在二维范德华多铁材料中实现了铁电与反铁电共存。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：综述了铁电性与多铁性在原子厚度极限下的实现。
- [[../papers/RecentAdvancesGrowth2025]]：综述了二维多铁材料的生长、表征与应用。
- [[../papers/huProgressProspectsLowdimensional2019]]：综述了低维多铁性材料的研究进展与展望。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/multiferroicity|多铁性]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../concepts/discommensuration|错位相子]]（磁性变体：自旋孤子）
- [[../entities/NiI2|二碘化镍 (NiI₂)]]

## 🏷️ 专业名词别名

- `type-ii-multiferroic`（concepts）
- `type-ii-multiferroics`（concepts）
