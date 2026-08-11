---
tags: [concept, 2D, vdW, materials, multiferroicity]
category: [D02, Z01]
---

# 二维范德华材料与低维铁性 / Two-Dimensional Van Der Waals Materials

原子级厚度（单层至数层）的晶体材料，其层内通过强共价键/离子键结合，而层间通过弱范德华（van der Waals, vdW）力堆叠。二维材料的出现打破了传统三维体材料中铁性极化的“临界厚度”（Critical Thickness）限制，为极轻薄、柔性及超低功耗纳米电子学器件奠定了基础。

## 低维铁性物理的突破

二维多铁性材料（2D Multiferroics）在单相中同时具备多种铁性序（铁电 FE、铁磁 FM、铁弹 FA 等），其对称性破缺与耦合机制是当前研究的核心。

![铁性序与对称性破缺](../../raw/figures/RecentAdvancesGrowth2025/fig_1_7IQ7CDIJ.png)
*图 1：铁电性破坏空间反演对称性，铁磁性破坏时间反演对称性，而铁旋性同时破坏两者。摘自 [[../../raw/note/2025_Dahua Ren_Recent advances in g_KEY-HDCR8MGU]]*

1.  **二维铁电性 (2D Ferroelectricity)**：
    - 突破退极化场限制，在单层极限下实现极化。特别是在 [[../entities/HfO2|HfO₂]] 系材料中，极化强度随厚度减小而增加，展现了无临界厚度的特性（[[../../raw/note/FerroelectricityMultiferroicityAtomic2023]]）。
    - **滑动铁电性**：由层间相对位移诱导的电极化，在 TMDs（如 3R-MoS₂）和 h-BN 中被广泛研究。

2.  **本征二维多铁性 (Intrinsic 2D Multiferroics)**：
    - **I 型多铁性**：铁电与磁性起源独立，通常具有较高的转变温度但磁电耦合较弱。
    - **II 型多铁性**：铁电性由特殊的磁结构（如螺旋磁序）诱导，磁电耦合极强，以 **NiI₂** 为代表（[[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]）。
    - **新型耦合机制**：单层 **CuCrSe₂** 通过铁电诱导的 Cr 原子轨道位移增强铁磁耦合，不同于传统的 I/II 型分类。

3.  **三铁性与莫尔工程 (Triferroicity & Moiré Engineering)**：
    - **三铁性 (Triferroic)**：在双层 **GdI₂** 中发现层间滑动可同时翻转铁电、铁磁和能谷极化（谷极化达 155.5 meV），为下一代谷电子学器件提供了可能。
    - **莫尔超晶格**：通过扭角控制实现关联态调控。

![二维多铁性耦合关系](../../raw/figures/RecentAdvancesGrowth2025/fig_2_3222BK6D.png)
*图 2：二维材料中磁电、磁弹、压电及磁谷效应的复杂耦合网络。摘自 [[../../raw/note/2025_Dahua Ren_Recent advances in g_KEY-HDCR8MGU]]*

## 生长与表征技术

### 先进制备方法
- **自上而下**：机械剥离（高结晶度，用于基础物理研究）与液相剥离。
- **自下而上**：
    - **CVD/CVT**：已实现 wafer-scale 单胞厚度 **Cr₂S₃** 的生长（[[../../raw/note/2025_Dahua Ren_Recent advances in g_KEY-HDCR8MGU]]）。
    - **MBE**：在超高真空下精确控制单层 NiI₂ 的原子级生长。
    - **ALD 集成**：通过原子层沉积钝化界面，实现了环境稳定的 NiI₂ 多端电学器件。

### 关键表征手段
- **SHG (二次谐波产生)**：对空间反演对称性破缺极度灵敏，是判定二维铁电性的金标准。
- **PFM (压电力显微镜)**：用于纳米尺度铁电畴的成像与翻转验证。
- **圆偏振拉曼光谱**：直接探测 NiI₂ 中的磁手性（magneto-chiral）基态。
- **太赫兹反射光谱**：探测磁电耦合产生的**电磁子 (Electromagnon)** 模式。

## 代表性二维材料分类

- **范德华绝缘体**：[[../entities/h-BN|h-BN]]（滑动铁电基底）。
- **过渡金属硫/卤化物**：[[../entities/TMDs|TMDs]]、**NiI₂**（II 型多铁极限）、**CuCrP₂S₆**（面内/面外各向异性）。
- **非范德华薄膜**：**Cr₂S₃**（单胞厚度室温多铁）。
- **金属/半导体多铁**：p 掺杂 **SnSe**（室温亚铁磁与铁电共存）、[[../entities/Fe3GeTe2|Fe₃GeTe₂]]。
- **MXenes**：[[../entities/MXenes|Ti₃C₂Tₓ]] 等，具有高导电性和潜在的多铁预测。

## 应用展望

二维多铁性材料为构建高密度、低功耗器件提供了平台：
- **非易失性存储**：基于电场控制磁性的磁电随机存取存储器 (MERAM)，可降低功耗 2-3 个数量级。
- **自旋电子学**：多铁隧道结 (MFTJ) 实现多态逻辑存储（电极化与磁化方向协同控制）。
- **能谷电子学**：利用磁谷耦合实现信息处理。

![二维多铁应用场景](../../raw/figures/RecentAdvancesGrowth2025/fig_15_TMK8S5HG.png)
*图 3：二维多铁性材料在存储、传感器、能量采集及射频器件中的应用蓝图。摘自 [[../../raw/note/2025_Dahua Ren_Recent advances in g_KEY-HDCR8MGU]]*

## 本库相关论文

- [[../../raw/note/2025_Dahua Ren_Recent advances in g_KEY-HDCR8MGU]]：Recent advances in growth, characterization, and application of 2D multiferroics. (2025 重点综述)
- [[../../raw/note/FerroelectricityMultiferroicityAtomic2023]]：Ferroelectricity and multiferroicity down to the atomic thickness. (HfO₂ 与 vdW 极限讨论)
- [[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]：NiI₂ 超快铁电切换研究。
- [[../../raw/note/2022_Song_Evidence for a singl_KEY-DGY8QFB7]]：单层 Cr₂S₃ 中的磁电耦合证据。

## 关联概念与实体

- [[sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[multiferroicity|多铁性 Multiferroicity]]
- [[../entities/In2Se3|硒化铟 In2Se3]]
- [[../entities/HfO2|氧化铪 HfO2]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
- [[../entities/MXenes|MXenes]]
