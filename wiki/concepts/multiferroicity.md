---
tags: [concept, multiferroics]
category: [D02]
---

# 多铁性 / Multiferroicity

**多铁性**是指在材料的同一相中同时存在两种或两种以上基础“铁性”序（铁电性、铁磁性、铁弹性）的性质。在当代材料科学语境下，该术语通常特指**铁电性（Ferroelectricity）**与**磁有序（Magnetism，包括铁磁、亚铁磁或反铁磁）**的共存及其相互耦合（即磁电效应）。

## 核心挑战：$d^0$ 规则与互斥性
传统钙钛矿（Perovskite）铁电性的来源通常需要 B 位阳离子具有空 d 轨道（$d^0$ 构型，如 $Ti^{4+}$），通过与氧离子的 $p-d$ 杂化稳定偏心畸变。然而，磁有序的产生则需要部分填充的 d 轨道来提供未配对电子自旋。这种对电子态填充要求的直接冲突导致了单相多铁性材料在自然界中极为罕见——这一洞察由 [[../../raw/note/hillWhyAreThere2000a|Nicola Hill (2000)]] 系统阐述。

## 分类与机制

根据铁电性与磁性的来源及耦合强度，多铁性材料通常分为两大类：

### Ⅰ型多铁性 (Type-I Multiferroics)
铁电性与磁性起源于不同的机制，且相对独立。通常具有较高的相变温度（常温可见）但磁电耦合较弱。
- **孤对电子机制**：如 [[../entities/BiFeO3]]，$Bi^{3+}$ 的 $6s^2$ 孤对电子驱动铁电畸变，而 $Fe^{3+}$ 提供反铁磁性。
- **几何铁电性**：源于晶格几何排布导致的结构不稳定，如六方 $RMnO_3$ ($R=Y, Ho-Lu$)。
- **电荷有序**：如 $LuFe_2O_4$，不同价态离子的有序排列打破空间反演对称性。

### Ⅱ型多铁性 (Type-II / Magnetic Multiferroics)
铁电性直接由特定的磁序（通常是非共线磁序）诱导产生。此类材料通常磁电耦合极强，但极化强度较小且相变温度多位于低温区。

#### 1. 逆 DM 相互作用 (Inverse Dzyaloshinskii-Moriya Interaction)
也称为**自旋流模型 (Spin-current model)**。在螺旋磁序中，非共线自旋通过自旋-轨道耦合诱导离子位移，产生的极化 $P$ 遵循：
$$P \propto e_{3} \times Q$$
其中 $e_3$ 为自旋旋转轴，$Q$ 为磁调制波矢。
- **典型材料**：$TbMnO_3$。

![逆DM相互作用机理示意图](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_27_963J6CL5.png)
*图源：[[../../raw/note/cheongMultiferroicsMagneticTwist2007a|Cheong & Mostovoy, Nat. Mater. 2007]]。展示了螺旋磁序如何通过位移氧离子打破空间反演对称性。*

#### 2. 交换伸缩机制 (Exchange Striction)
极化强度 $P$ 正比于自旋标量积的梯度：$P \propto \langle S_i \cdot S_j \rangle$。适用于共线磁序（如 $\uparrow\uparrow\downarrow\downarrow$ 序），通过调节不同自旋对之间的相互作用键长产生极性。
- **典型材料**：$RMn_2O_5$、E-型 $RMnO_3$。

#### 3. 混合不适当铁电性 (Hybrid Improper Ferroelectricity, HIFE)
通过多种非极性结构畸变（如八面体旋转与倾斜）的非线性耦合诱导产生极化。
- **典型材料**：$Ca_3Mn_2O_7$。

## 物理效应与调控

### 极化翻转 (Polarization Flop)
在 II 型多铁性材料中，外磁场可以通过改变磁序方向直接驱动电极化矢量的旋转。例如，在 $TbMnO_3$ 中，磁场可诱导极化从 c 轴翻转至 a 轴。

![TbMnO3 中的极化翻转](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_2_PNAIBBQF.png)
*图源：[[../../raw/note/cheongMultiferroicsMagneticTwist2007a|Cheong & Mostovoy, Nat. Mater. 2007]]。展示了磁场对极化方向的直接操控。*

### 电磁振子 (Electromagnons)
多铁性体系中磁激元（Magnon）与光频支声子（Phonon）的耦合激元。这使得原本只能通过磁场激发的磁子，可以通过电场分量（光）进行探测和操控。

## 前沿研究方向
1. **二维多铁性**：探索范德华材料（如 $NiI_2$、$CuCrP_2S_6$）中的层间滑动铁电性与磁性的耦合。参考 [[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]。
2. **多铁斯格明子 (Multiferroic Skyrmions)**：利用电场操控具有拓扑稳定性的磁子结构，在低功耗存储领域具有巨大潜力。
3. **动态磁电控制**：利用超快激光脉冲实现太赫兹频段的极化开关。

## 本库相关笔记
- [[../../raw/note/hillWhyAreThere2000a|Hill 2000 (d0 规则起源)]]
- [[../../raw/note/cheongMultiferroicsMagneticTwist2007a|Cheong 2007 (磁阻挫与机制综述)]]
- [[../../raw/note/mostovoyMultiferroicsDifferentRoutes2024|Mostovoy 2024 (最新机制与动态效应)]]
- [[magnetoelectric-coupling]]
