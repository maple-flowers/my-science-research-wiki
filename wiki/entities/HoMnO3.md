---
tags: [entity, material, multiferroic]
category: [D02]
---

# 锰酸钬 / Holmium Manganate (HoMnO3)

**HoMnO3** 是一种典型的六方结构稀土锰氧化物 ($h\text{-}RMnO_3$)，属于 **Type-II (磁诱导) 多铁性体系** 或 **几何铁电体**。它是研究磁电锁定 (Phase-Locked) 效应、非本征铁电性以及拓扑畴结构的经典模型材料。

## 1. 几何铁电性与 d⁰ 规则的突破
HoMnO3 的铁电性起源于所谓的“几何机制” (Geometric Ferroelectricity)，这一概念由 [[../papers/hillWhyAreThere2000a]] 首先提出，用以解释为何磁性与铁电性在钙钛矿中难以共存。不同于传统钙钛矿铁电体依赖 B 位离子的 $d^0$ 构型位移，六方结构的 HoMnO3 包含由 $MnO_5$ 三角双锥组成的层状结构。随着温度降至铁电相变温度 ($T_C \approx 870 \text{ K}$)，晶格发生三聚化 (Trimerization) 畸变，导致 $MnO_5$ 多面体发生协调的倾斜与旋转。这种结构不稳定性通过氧原子的中介作用，迫使 $Ho^{3+}$ 离子在 $c$ 轴方向发生位移，从而打破空间反演对称性并产生自发极化 [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]。这种“非本征”特性使得铁电序与晶格畸变模式在相位上紧密锁定。

## 2. 相位锁定的磁电耦合
HoMnO3 的核心物理价值在于其复杂的磁电锁定行为。在低温下 ($T_N \approx 75 \text{ K}$)，$Mn^{3+}$ 子晶格进入反铁磁序，并随温度进一步降低发生多次磁重取向相变。[[../papers/fiebigEvolutionMultiferroics2016]] 指出，利用非线性光学技术 (如二次谐波产生 SHG)，可以观测到铁电畴与反铁磁畴的完全空间重叠。这种耦合并非源于体相的直接作用，而是通过畴壁 (Domain Walls) 处的对称性破缺实现的：在 HoMnO3 中，每一个铁电畴壁在对称性上被限定同时也是磁畴壁，实现了序参量的“相位锁定”。

此外，$Ho^{3+}$ 的 $4f$ 磁矩与 $Mn^{3+}$ 的 $3d$ 磁矩之间存在强烈的交换耦合。实验证明，通过外加磁场可以触发 $Mn$ 子晶格的自旋重取向，进而改变材料的电容或极化状态。这种由磁结构演化驱动的电性响应，是 II 类多铁性材料实现高灵敏磁电换能器的物理基础 [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]。

## 3. 拓扑缺陷与畴壁工程
HoMnO3 展现出独特的六瓣涡旋 (Vortex) 畴结构，这是由晶格三聚化的相位自由度与铁电极化的二值性共同决定的拓扑缺陷。这种涡旋中心是研究拓扑物理与非平衡态动力学的理想场所。当代研究已将重心转向“畴壁工程”，即利用 HoMnO3 畴壁处不同于块体的导电性与磁电响应，构建纳米尺度的功能器件单元 [[../papers/rameshMultiferroicsProgressProspects2007]]。

## 4. 本库相关代表性论文
- [[../papers/hillWhyAreThere2000a]]：定义了打破 $d^0$ 规则的几何结构路径。
- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]：系统阐述了六方锰氧化物的多铁性复兴背景。
- [[../papers/fiebigEvolutionMultiferroics2016]]：综述了该体系中磁电序演化的动力学与对称性本质。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：提供了磁阻挫与非共线磁序驱动耦合的理论框架。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：讨论了多铁性材料在异质结与畴壁层面的应用前景。

## 5. 关联概念与实体
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../concepts/magnetoelectric-coupling|磁电耦合 Magnetoelectric Coupling]]
- [[../entities/domain-wall|畴壁 Domain Wall]]
- [[BiFeO3|铋铁氧体 BiFeO3]] (对比材料：Type-I 多铁)
- [[YMnO3|锰酸钇 YMnO3]] (同类六方多铁材料)
