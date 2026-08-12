---
tags: [concept, multiferroics, magnetism, ferroelectricity, 2D-materials, hub]
category: [D02]
title: 多铁性 / Multiferroicity
type: concept
status: mature
domain: multiferroics
mechanism: 同一相中两种及以上铁性序（通常铁电与磁有序）共存并可发生磁电耦合
related_concepts: [magnetoelectric-coupling, type-i-multiferroics, type-ii-multiferroics, lone-pair-ferroelectricity, exchange-striction, inverse-dzyaloshinskii-moriya, electromagnon, spin-spiral, ferroelasticity, phase-interlocked]
aliases: ["Multiferroic", "多铁材料", "多铁体"]
key_quantities:
  d0_rule: "传统钙钛矿铁电需 B 位 d0 构型，而磁性需部分填充 d 轨道，二者冲突使单相多铁稀缺（Hill 2000）"
  type_i: "磁、电独立起源，耦合弱但 Tc 高/极化大（BiFeO3）"
  type_ii: "磁序破缺反演生极，耦合强但极化小/温度低（TbMnO3、NiI2，Tc~21 K）"
  intercalated: "T-CdCr2Te4 Tc~260 K，极化翻转可调反斯格明子手性"
papers: [hillWhyAreThere2000a, cheongMultiferroicsMagneticTwist2007a, spaldinRenaissanceMagnetoelectricMultiferroics2005, songEvidenceSinglelayerVan2022, zhaoRealization2DMultiferroic2024, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08
---

# 多铁性 / Multiferroicity

**多铁性**指材料在同一相中同时存在两种或以上基础"铁性"序（铁电性、铁磁性/反铁磁性、铁弹性、铁旋性）。当前语境下通常特指**铁电性与磁有序的共存及其相互耦合（磁电效应）**，目标是以电场调控磁性、以磁场调控电极化，实现低功耗"电写磁读"器件 [[../papers/cheongMultiferroicsMagneticTwist2007a]]。本页是多铁主题的总览枢纽页，细分机制见 [[type-i-multiferroics|第一类]] 与 [[type-ii-multiferroics|第二类多铁]]、[[magnetoelectric-coupling|磁电耦合]]。

## 👵 太奶导读

太奶，材料里有好几种"认方向、还能被掰来掰去记住"的脾气：电偶极认一个方向叫铁电，小磁针认一个方向叫铁磁。要是一块材料同时有这两样本事，就叫"多铁"。金贵的地方在于它俩能互相使唤——加个电压就能拨动磁的方向，既省电又不发热，将来做存储器最理想。

可这两样本事天生犯冲：按老经验，要产生铁电，金属原子最外层的 d 轨道得是空的（叫 d0）；要有磁性，d 轨道里又非得有没配对的电子不可。一个要空、一个要有，凑不到一块儿，所以自然界里单相多铁特别稀罕，这就是有名的"d0 规则"。科学家绕开它的办法分成两派。第一派是"一院两户"：电和磁各有各的来历（比如铋的孤对电子管电、铁管磁），凑在一块，耐温高、电劲儿大，可惜它俩互相使唤不太动。第二派是"磁逼出电"：一群小磁针螺旋着转，转着转着把对称打破、硬挤出一个电方向来，磁电绑得死紧，可惜电劲儿小、还怕冷。后来二维薄片兴起，又有插层、氧化物单层剥离等新招，把多铁做到了原子级厚度。

## 🏗️ 结构概览：d0 规则与铁电分类

传统钙钛矿铁电依赖 B 位阳离子的 $d^0$ 构型（如 Ti⁴⁺、Zr⁴⁺）通过 $p$–$d$ 杂化偏心位移，而磁性需要部分填充的 d 轨道提供未配对自旋——这一化学冲突即 **$d^0$ 规则**，是单相多铁稀缺的根源 [[../papers/hillWhyAreThere2000a]]。绕开它的途径包括孤对电子铁电、几何/电荷有序铁电，以及直接由磁序生极（II 型）。

![表：铁电体分类——本征（d0、孤对电子）与非本征（几何、电子、磁性铁电体）](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/tab_1_X3QYE982.png)
*   **看图要点**：表格把铁电按起源分门别类；磁性铁电（II 型多铁）单列一类，说明它不必走 d0 偏心位移的老路，从而避开了 d0 与磁性的冲突 [[../papers/cheongMultiferroicsMagneticTwist2007a]]。
*   **来源**：[[../papers/cheongMultiferroicsMagneticTwist2007a]] -> [[../figures/crystal-structures|晶体结构]]

## 🧩 第一类多铁：独立起源

第一类多铁的铁电与磁来自不同子系统，故耦合较弱但相变温度可高于室温、极化较大：
- **孤对电子机制**：[[../entities/BiFeO3|BiFeO3]] 中 Bi³⁺ 的 6s² 孤对电子驱动铁电畸变，Fe³⁺ 提供反铁磁（$T_C\sim1100$ K，$T_N\sim640$ K）[[../papers/hillWhyAreThere2000a]]。
- **几何铁电性**：六方 $RMnO_3$ 中非中心对称配位几何本身失稳。
- **电荷有序**：不同价态离子有序排列打破反演对称（如 $LuFe_2O_4$）。

![图：电荷/几何失稳诱导铁电的几种第一类机制——位点/键中心电荷序共存、↑↑↓↓ 交换收缩、双层电子铁电等](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_1_D8A9TF3K.png)
*   **关键特征**：这些生极机制依赖结构与电荷排布，磁由另一组离子另供，故铁电与磁独立共存、磁电耦合为次级效应 [[../papers/cheongMultiferroicsMagneticTwist2007a]]。
*   **来源**：[[../papers/cheongMultiferroicsMagneticTwist2007a]] -> [[../figures/crystal-structures|晶体结构]]

## 🌀 第二类多铁：磁序生极

第二类多铁中铁电由非共线磁序（螺旋/锥形）直接诱导，极化是磁序派生量，故磁电耦合极强但极化小、温度低。机制包括逆 DM/自旋电流（$P\propto e_3\times Q$）与共线 ↑↑↓↓ 序的 [[exchange-striction|交换收缩]] [[../papers/cheongMultiferroicsMagneticTwist2007a]]。

![图：TbMnO3 中磁场诱导的极化翻转——H‖b 约 5 T 时 Pc 转为 Pa（90° flop）](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_2_PNAIBBQF.png)
*   **关键特征**：磁场改变自旋旋转轴即让极化方向 90° 翻转，直接证明磁序是极化的来源（而非仅是共存），这是 II 型多铁强磁电耦合的标志指纹 [[../papers/cheongMultiferroicsMagneticTwist2007a]]。
*   **来源**：[[../papers/cheongMultiferroicsMagneticTwist2007a]] -> [[../figures/domain-walls|畴与畴壁]]

## 🔬 二维多铁的兴起（2020+）

- **本征单层 II 型**：2022 年实验证实单层 [[../entities/NiI2|NiI2]] 在约 21 K 以下形成正螺旋磁序，经自旋流机制诱导面内极化，是首个单层本征 II 型多铁 [[../papers/songEvidenceSinglelayerVan2022]]。
- **插层设计**：把过渡金属非中心对称插入 TMD 双层构建 $AM_2X_4$ 多铁体；$T$-$CdCr_2Te_4$ 的 $T_C\approx260$ K，极化翻转可调控反斯格明子手性 [[../papers/zhaoRealization2DMultiferroic2024]]。
- **非范德华氧化物单层**：从 $ABO_3$ 剥离出的 [[../entities/SrOsO3|SrOsO3]] 等表现出 [[phase-interlocked|相锁定]] 磁电耦合，支持常温自旋极化电流开关 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。

![图：单层 NiI2 的晶体/螺旋磁结构（9a×√3a 超胞）与自旋-轨道耦合诱导的面内极化模型](../../raw/figures/aminiAtomicscaleVisualizationMultiferroicity2024/fig_1_8XET8BR2.png)
*   **关键特征**：STM 在导带能量处看到周期约 17.8 Å 的条纹（恰为磁螺旋周期之半的电极化周期），从原子尺度可视化了单层 II 型多铁序 [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]。
*   **来源**：[[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] -> [[../figures/crystal-structures|晶体结构]]

## 📊 两类多铁对照

| 维度 | 第一类 (Type-I) | 第二类 (Type-II) |
| :--- | :--- | :--- |
| 极化起源 | 独立结构/化学极性（孤对、几何、电荷序） | 磁序破缺反演对称 |
| 磁电耦合 | 较弱（次级/界面） | 本征、强 |
| 极化大小 | 较大 | 较小 |
| 转变温度 | 铁电、磁可分别很高 | 受磁序温度限制（常低温） |
| 典型体系 | BiFeO3、六方 RMnO3 | TbMnO3、NiI2、CuCrP2S6 |

## 📚 相关论文 (Related Papers)

- [[../papers/hillWhyAreThere2000a]]：阐明 d0 规则与磁性铁电体稀缺的化学根源。
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：经典综述，确立两类多铁划分与磁致铁电物理。
- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]：多铁复兴综述。
- [[../papers/songEvidenceSinglelayerVan2022]]：单层 NiI2 本征 II 型多铁的光学证据。
- [[../papers/zhaoRealization2DMultiferroic2024]]：插层 $AM_2X_4$ 多铁与反斯格明子手性电调控。
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：高通量剥离 ABO3 单层与相锁定多铁。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[magnetoelectric-coupling|磁电耦合]]、[[type-i-multiferroics|第一类多铁]]、[[type-ii-multiferroics|第二类多铁]]、[[spin-spiral|自旋螺旋]]、[[electromagnon|电磁振子]]、[[exchange-striction|交换收缩]]、[[inverse-dzyaloshinskii-moriya|逆 DM 相互作用]]、[[lone-pair-ferroelectricity|孤对电子铁电性]]、[[ferroelasticity|铁弹性]]、[[phase-interlocked|相锁定]]
- [[../entities/BiFeO3|BiFeO3]]、[[../entities/NiI2|NiI2]]、[[../entities/SrOsO3|SrOsO3]]、[[../entities/TMDs|TMDs]]
