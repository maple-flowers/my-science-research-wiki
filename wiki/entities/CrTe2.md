---
tags: [entity, material, multiferroic, TMD, 2D, magnetism, ferroelectricity]
category: [D01, Z02]
---

# 二碲化铬 / Chromium Telluride (CrTe₂)

**二碲化铬 (CrTe₂)** 是一种具有高度调控潜力的范德华（vdW）层状过渡金属硫族化合物（TMD）。它是近年来二维凝聚态物理研究的热点，特别是作为首个被实验证实具有**室温、空气稳定性**的本征二维多铁金属材料（[[../../raw/note/tianRoomtemperatureTwodimensionalMultiferroic2026|Tian et al. 2026]]）。其独特的层依赖磁性及由层间电荷转移诱导的铁电性，为实现超低功耗的“电写磁读”自旋电子器件提供了物理基础。

![CrTe2晶体结构](../../raw/figures/tianRoomtemperatureTwodimensionalMultiferroic2026/fig_1_USCG2SF4.png)
*图 1: (a) 1T-CrTe₂ 的晶体结构模型（俯视与侧视）；(b-d) 单层 CrTe₂ 的 STM 及 SP-STM 图像，显示锯齿状反铁磁（z-AFM）序；(f-h) 双层 CrTe₂ 的 STM 及 LEED 图像，显示第一层 AFM 与第二层 FM 的共存。*

## 核心物理特性

### 1. 结构与电子态
- **晶体结构**：CrTe₂ 以三角层状结构（空间群 $P\bar{3}m1$）结晶，单层采用 **1T 相** 构型。Cr 阳离子位于 Te 八面体中心，层内通过共价键连接，层间为弱范德华力。
- **金属性**：不同于传统铁电体必须是绝缘体，CrTe₂ 表现出明显的**面内金属性**（dI/dV 谱在费米能级不为零）。这种“铁电金属”特性的关键在于极化电子与导电电子的空间分离：导电电子分布在 MX₂ 层内，而极化偶极矩局域在界面或特定原子周围（[[../../raw/note/zhaoRealization2DMultiferroic2024|Zhao et al. 2024]]）。

### 2. 层依赖磁性 (Layer-dependent Magnetism)
CrTe₂ 的磁基态对层数极度敏感：
- **单层**：表现为**锯齿状反铁磁（z-AFM）**序，宏观磁矩抵消。
- **双层**：表现为**本征多铁性**。实验观测到其第一层保持 AFM，而第二层转变为**铁磁（FM）**。这种 FM/AFM 交替堆叠结构产生了约 2.44 $\mu_B$/Cr 的净磁矩，且居里温度可达室温（300 K）。

### 3. 层间电荷转移驱动的铁电性
CrTe₂ 的铁电性起源并非传统的层间滑移（Sliding Ferroelectricity），而是源于**层间电荷转移**（Interlayer Charge Transfer）：
- **物理机制**：FM 层与 AFM 层之间存在静电势差（约 0.1 eV）。为了降低体系总能量，电子会自发地从 z-AFM 层转移到 FM 层，以增强铁磁层中的轨道杂化。
- **极化强度**：这种不对称的电荷重新分布打破了空间反演对称性，产生约 **3.0 pC/m** 的面外自发极化（$P_{out}$），强度远高于典型的滑移铁电体（0.1-1.2 pC/m）。

![磁电耦合演示](../../raw/figures/tianRoomtemperatureTwodimensionalMultiferroic2026/fig_3_85N9YJPF.png)
*图 2: 双层 CrTe₂ 的“电写磁读”功能演示。(b) PFM 写入的“盒中盒”铁电畴；(f) 对应区域在 MFM 下读取出的磁畴结构，两者高度吻合。*

## 磁电耦合与器件应用

CrTe₂ 最具突破性的应用潜力在于其强大的**磁电耦合效应**：
1. **电压控制磁序**：通过施加外电场翻转铁电极化方向，可以诱导电荷在两层间重新分配。当电荷填充跨越临界点时，各层的磁基态会在 FM 和 AFM 之间发生非易失性切换。
2. **“电写磁读”功能**：实验已成功演示利用 PFM 针尖在室温大气下写入铁电畴，并利用 MFM 成功读出相应的磁畴构型（图 2）。这为开发超低功耗的非易失性自旋存储器（如电压驱动的 MRAM）铺平了道路。
3. **拓扑磁结构调控**：在高通量预测中，以 CrTe₂ 为基础的插层超晶格（如 $T-CdCr_2Te_4$）被归类为 **Type-a 多铁材料**。在该类体系中，极化翻转可以改变 Dzyaloshinskii-Moriya 相互作用（DMI）的分布，从而实现对**磁斯格明子（Skyrmions）**产生、湮灭及手性的全电学操控（[[../../raw/note/zhaoRealization2DMultiferroic2024|Zhao et al. 2024]]）。

## 关键表征技术
- **SP-STM (自旋极化扫描隧道显微镜)**：在原子尺度鉴定单层 AFM 和双层 FM/AFM 磁序。
- **PFM/MFM 联用**：原位验证铁电-磁畴的关联及其对电场的响应。
- **SQUID**：证实室温下的磁滞回线特征。
- **LEED (低能电子衍射)**：观测单层（0.37 nm）与双层（0.39 nm）间的晶格应变差异。

## 本库相关论文
- [[../../raw/note/tianRoomtemperatureTwodimensionalMultiferroic2026]]：实验首次合成并证实双层 CrTe₂ 的室温多铁性与电写磁读功能。
- [[../../raw/note/zhaoRealization2DMultiferroic2024]]：高通量第一性原理预测，提出插层超晶格策略并分类 CrTe₂ 基多铁材料。
- [[../../raw/note/miaoMagneticFerroelectricMetal2024]]：探讨 2D 磁性金属中的滑动诱导多铁性。

## 关联概念
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/interlayer-charge-transfer|层间电荷转移 Interlayer Charge Transfer]]
- [[../concepts/skyrmion|磁斯格明子 Skyrmion]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
