---
tags: [concept, multiferroics, magnetism, ferroelectricity, 2D-materials]
category: [D02]
---

# 多铁性 / Multiferroicity

**多铁性** 是指在材料的同一相中同时存在两种或两种以上基础“铁性”序（铁电性、铁磁性、铁弹性、铁旋性）的物理性质。在当前凝聚态物理研究中，该术语通常特指 **铁电性（Ferroelectricity）** 与 **磁有序（Magnetism）** 的共存及其相互耦合（即磁电效应）。

## 1. 核心挑战：$d^0$ 规则与互斥性
传统钙钛矿（Perovskite, $ABO_3$）铁电性的产生通常依赖于 B 位阳离子的 $d^0$ 电子构型（如 $Ti^{4+}$、$Zr^{4+}$），通过与氧离子的 $p-d$ 杂化驱动偏心位移。然而，磁有序的产生则需要部分填充的 $d$ 轨道以提供未配对自旋。这种对电子态填充要求的直接冲突导致了单相多铁材料在自然界中极为罕见——这一物理瓶颈被称为 **$d^0$ 规则**（[[../papers/hillWhyAreThere2000a|Hill 2000]]）。

## 2. 分类与机制

根据铁电性与磁性的来源及耦合强度，多铁性材料通常分为两大类：

### Ⅰ型多铁性 (Type-I Multiferroics)
铁电性与磁性起源于不同的物理机制，且基本独立。通常具有较高的相变温度（甚至高于室温）但磁电耦合较弱。
- **孤对电子机制**：如 **[[../entities/BiFeO3|BiFeO3]]**。$Bi^{3+}$ 的 $6s^2$ 孤对电子驱动铁电畸变，而 $Fe^{3+}$ 提供反铁磁性（[[../papers/hillWhyAreThere2000a|Hill 2000]]）。
- **几何铁电性**：源于非中心对称配位几何本身的结构不稳定，如六方 **$RMnO_3$** 中 $Y^{3+}$ 稳定了 5 配位的三角双锥结构（[[../papers/cheongMultiferroicsMagneticTwist2007a|Cheong 2007]]）。
- **电荷有序**：由不同价态离子的有序排列打破空间反演对称性（如 $LuFe_2O_4$）。

### Ⅱ型多铁性 (Type-II / Magnetic Multiferroics)
铁电性直接由特定的非共线磁序（通常是磁阻挫驱动的螺旋或锥形磁序）诱导产生。此类材料具有极强的磁电耦合，但极化强度通常较小且相变温度多位于低温区（[[../papers/cheongMultiferroicsMagneticTwist2007a|Cheong 2007]]）。
- **逆 DM 相互作用 / 自旋流模型**：螺旋磁序中相邻自旋通过自旋-轨道耦合诱导离子位移，产生的极化遵循 $P \propto e_{3} \times Q$。
- **交换伸缩机制 (Exchange Striction)**：极化由自旋对之间的海森堡交换作用引起，适用于共线 $\uparrow\uparrow\downarrow\downarrow$ 序（如 $RMn_2O_5$）。

## 3. 二维多铁性的兴起 (2020+)

随着原子层厚度范德华（vdW）材料的研究深入，多铁性在二维极限下的稳定性得到了证实：

### 3.1 本征二维 II 型多铁性：NiI₂
2022 年实验证实，单层 **[[../entities/NiI2|NiI2]]** 在 21 K 以下形成正螺旋（proper-screw）磁序，通过自旋流机制诱导出面内电极化。这是首个在单层极限下证实的本征 II 型多铁材料（[[../papers/songEvidenceSinglelayerVan2022|Song 2022]]）。

### 3.2 插层设计策略 (Intercalation Strategy)
通过将过渡金属 A 原子（如 Mn, Cr, Co）非中心对称地插入 TMD 双层中，可以构建稳定的 **$AM_2X_4$** 二维多铁体。例如 **$T-CdCr_2Te_4$**，其 $T_C \approx 260$ K，并可通过极化翻转实现对反斯格明子（Anti-skyrmions）手性的可逆调控（[[../papers/zhaoRealization2DMultiferroic2024|Zhao 2024]]）。

### 3.3 非范德华氧化物单层
基于**键密度**与**结合强度**判据，从非层状 $ABO_3$ 氧化物中剥离出的单层（如 **[[../entities/SrOsO3|SrOsO3]]**）表现出独特的“相锁定”磁电耦合，支持常温下的自旋极化电流开关（[[../papers/zhongHighthroughputExfoliationMultiferroic2025|Zhong 2025]]）。

## 4. 关键图表

![多铁性分类：本征与非本征](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/tab_1_X3QYE982.png)
*表 1：铁电体分类：本征（$d^0$、孤对电子）与非本征（几何、电子、磁性铁电体）。摘自 [[../papers/cheongMultiferroicsMagneticTwist2007a]]*

![TbMnO3 中的极化翻转](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_2_PNAIBBQF.png)
*图 1：在 II 型多铁性材料（如 $TbMnO_3$）中，外磁场可诱导极化矢量发生 90° 翻转。摘自 [[../papers/cheongMultiferroicsMagneticTwist2007a]]*

## 5. 相关概念
- [[magnetoelectric-coupling|磁电耦合 Magnetoelectric Coupling]]
- [[2D-materials|二维范德华材料与低维铁性]]
- [[../entities/BiFeO3|BiFeO3]]
- [[../entities/NiI2|NiI2]]
- [[phase-interlocked|相锁定 Phase Interlocked]]
- [[ferroelasticity|铁弹性 Ferroelasticity]]
