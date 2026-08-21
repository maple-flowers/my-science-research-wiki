---
tags: [concept]
title: '弱铁磁性 / Weak Ferromagnetism'
type: concept
status: developing
papers: ['hillWhyAreThere2000a', 'deSousa2008electrical', 'prosandeevKittelLawInBiFeO3Ultrathin2010', 'mostovoyMultiferroicsDifferentRoutes2024', 'rameshMultiferroicsProgressProspects2007']
updated: 2026-08-18
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_5960e1139a7811f1a98a525400f8a581
    ReservedCode1: btyv0SNHkKKVTPjKZso7CsqTgpujlhRowYUYL3iVUvs1YhJmdJz8GpMsoXfo2V8z1FK5XOglPgD0gPv55YHwdrwUf+fcLHaICpKhz68UeL2gCqsXs2dMcLKHLUhxLXE5roZVN+lPXvkTzuta9i+oLA0PjA0vJB85vCMxCNQ3SBO5ADc7Y6CAkZ5d49E=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_5960e1139a7811f1a98a525400f8a581
    ReservedCode2: btyv0SNHkKKVTPjKZso7CsqTgpujlhRowYUYL3iVUvs1YhJmdJz8GpMsoXfo2V8z1FK5XOglPgD0gPv55YHwdrwUf+fcLHaICpKhz68UeL2gCqsXs2dMcLKHLUhxLXE5roZVN+lPXvkTzuta9i+oLA0PjA0vJB85vCMxCNQ3SBO5ADc7Y6CAkZ5d49E=
---



# 弱铁磁性 / Weak Ferromagnetism

弱铁磁性（weak ferromagnetism, WFM）指**磁结构整体上近似反铁磁或非共线磁序，但由对称性破缺机制使自旋发生微小倾斜，从而出现一个宏观小净磁矩**的现象。其净磁化强度通常比典型铁磁体小 2–3 个数量级，故称"弱"铁磁。弱铁磁是 BiFeO₃ 等磁电多铁材料兼具磁性与铁电性的关键桥梁，也是理解"为什么磁性铁电体如此稀少"这一经典问题的核心概念。

## 👵 太奶导读

把原子自旋想象成排队站岗的士兵：反铁磁是相邻士兵"面对面"互相抵消，整体没有一点磁性；铁磁是所有士兵朝同一个方向，磁性很强。弱铁磁呢，是地面有个看不见的小斜坡（来自 DM 相互作用这种不对称的力），让相邻士兵都朝同一边歪了一点点——整体上大部分还是互相抵消的，但漏出了一点微小的、同向的"歪斜"，也就是一点净磁性。这点磁性虽小，却很金贵：它让同一块材料既"带电"又"带磁"，科学家就能用电压去控制磁性，做省电的存储器件。

## 🧩 弱铁磁的起源：DM 相互作用与自旋倾斜

弱铁磁最常见的微观起源是 **Dzyaloshinskii–Moriya（DM）相互作用**——一种由自旋轨道耦合与磁序对称性共同决定的反对称交换作用。在允许非零 DM 矢量 $\mathbf{D}_{ij}$ 的晶体对称性环境中，能量项 $\mathbf{D}_{ij}\cdot(\mathbf{S}_i\times\mathbf{S}_j)$ 偏好相邻自旋互相垂直，于是原本共线反铁磁序被引入一个小的倾斜角，产生净磁矩。DM 相互作用强度通常远小于各向同性交换，因此净磁矩"弱"。

hill 综述（[[../papers/hillWhyAreThere2000a]]）系统比较了铁磁、反铁磁、弱铁磁（自旋倾斜）与自旋螺旋等磁有序结构，指出弱铁磁在能量与对称性上处于"既想要铁电、又要磁性"的矛盾位置，是磁性铁电体稀少性的出发点。

![图：弱铁磁性示意——在共线反铁磁序上叠加小角度自旋倾斜，产生宏观净磁矩](<../../raw/figures/hillWhyAreThere2000a/fig_1_IBXL696E.png>)

*关键特征：对比铁磁、反铁磁、弱铁磁（自旋倾斜）等磁有序的磁性差异，体现弱铁磁为反铁磁序上的微小倾斜。*
*来源：[[../papers/hillWhyAreThere2000a]] -> [[../figures/electronic-bands-cdw-transport|电子结构与输运：CDW与输运性质]]*

## 🔬 为什么磁性铁电体如此稀少：d⁰ 规则

hill（[[../papers/hillWhyAreThere2000a]]）提出的著名矛盾（即 **d⁰ 规则**，[[../concepts/d0-rule|d⁰规则]]）：铁电性偏爱 **d⁰ 构型**（如 Ti⁴⁺、Nb⁵⁺ 的空 d 轨道有利于 B 位离子位移型极化），而磁性需要**部分占据的 d 轨道**（dⁿ, n≠0）。两者在过渡金属离子上天然互斥，这是"为什么磁性铁电体如此稀少"的核心原因。弱铁磁提供一条绕行路径：不必强铁磁序，只需在反铁磁序上施加微小倾斜，即可在不触碰 d⁰ 矛盾的前提下获得磁性与磁电耦合。

## ⚡ 电控弱铁磁：BiFeO₃ 中的磁振子与磁电耦合

de Sousa 与 Moore（[[../papers/deSousa2008electrical]]）研究多铁 BiFeO₃ 薄膜中通过电场控制磁振子（magnon）传播的机制：弱铁磁净矩与铁电极化经 DM 型磁电耦合锁定，外加电场翻转极化即可调制自旋波的色散与传播。

![图：BiFeO3 薄膜中极化与自旋 DM 耦合的图像](<../../raw/figures/deSousa2008electrical/fig_1_MFP3ILKR.png>)

*关键特征：显示弱铁磁净矩与铁电极化之间的 DM 型磁电耦合，电场可翻转极化并调制磁序。*
*来源：[[../papers/deSousa2008electrical]] -> [[../figures/electronic-bands-cdw-transport|电子结构与输运：CDW与输运性质]]*

![图：BiFeO3 磁振子色散曲线](<../../raw/figures/deSousa2008electrical/fig_2_R7A39F2L.png>)

*关键特征：磁振子（自旋波）色散随极化方向变化，体现电控弱铁磁的传播特性。*
*来源：[[../papers/deSousa2008electrical]] -> [[../figures/electronic-bands-band-structures|电子结构与输运：能带结构与带隙]]*

## 📏 Kittel 定律与 BiFeO₃ 超薄膜极限

prosandeev 等（[[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]）通过第一性原理研究 BiFeO₃ 超薄膜中的 **Kittel 定律**（[[../concepts/kittel-law|Kittel定律]]）：弱铁磁单畴/畴壁的尺寸与能量随薄膜厚度的幂律关系在超薄极限下发生显著变化，磁化矢量分布与能量-尺寸拟合曲线揭示了弱铁磁序随尺寸演化的规律，为薄膜器件设计提供尺寸依赖的磁序图像。

![图：BiFeO3 超薄膜磁化矢量分布](<../../raw/figures/prosandeevKittelLawInBiFeO3Ultrathin2010/fig_1_GV39IF8G.png>)

*关键特征：超薄膜中弱铁磁磁化矢量的空间分布，随薄膜厚度变化。*
*来源：[[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]] -> [[../figures/domain-walls-structures|铁电畴与畴壁：畴结构与畴壁]]*

![图：BiFeO3 超薄膜能量-尺寸拟合（Kittel 定律）](<../../raw/figures/prosandeevKittelLawInBiFeO3Ultrathin2010/fig_2_478MJ9U5.png>)

*关键特征：磁畴/单畴能量随体系尺寸的幂律拟合，验证 Kittel 定律在超薄极限的行为。*
*来源：[[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]] -> [[../figures/domain-walls-structures|铁电畴与畴壁：畴结构与畴壁]]*

## 🧲 通往磁电耦合的多条路线

mostovoy（[[../papers/mostovoyMultiferroicsDifferentRoutes2024]]）综述指出，弱铁磁是通往磁电耦合（[[../concepts/magnetoelectric-coupling|磁电耦合]]）的多条路线之一。除 DM 自旋倾斜外，还包括自旋螺旋（[[../concepts/spin-spiral|自旋螺旋]]）、交换收缩（[[../concepts/exchange-striction|交换收缩]]）、proper-screw（[[../concepts/proper-screw|proper-screw]]）等机制，各自对应不同的磁空间群与多铁类型。ramesh 的薄膜综述（[[../papers/rameshMultiferroicsProgressProspects2007]]）则从实验与器件角度总结了 BiFeO₃ 等弱铁磁多铁薄膜的进展与应用前景。

## 📚 相关论文 (Related Papers)

- [[../papers/deSousa2008electrical]]：BiFeO₃ 薄膜中电场控制磁振子传播——弱铁磁与极化的 DM 型磁电耦合。
- [[../papers/hillWhyAreThere2000a]]：提出"为什么磁性铁电体如此稀少"，给出 d⁰ 规则与弱铁磁的对称性分析。
- [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]：BiFeO₃ 超薄膜中的 Kittel 定律与尺寸依赖的弱铁磁序。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：多铁薄膜（含 BiFeO₃ 弱铁磁）的进展与器件前景综述。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：通向磁电耦合的多条路线综述，含弱铁磁机制定位。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferromagnetism|铁磁性]]：弱铁磁的强磁对应物，宏观净磁矩远大于弱铁磁。
- [[../concepts/antiferromagnetism|反铁磁性]]：弱铁磁所叠加的基础磁序。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：弱铁磁在多铁材料中产生磁电响应的桥梁。
- [[../concepts/d0-rule|d⁰规则]]：解释磁性铁电体稀少性的核心矛盾。
- [[../concepts/kittel-law|Kittel定律]]：磁畴尺寸与能量随体系尺寸的标度律。
- [[../concepts/exchange-striction|交换收缩]]：另一条通往磁电耦合的机制。
- [[../concepts/spin-spiral|自旋螺旋]]：非共线磁序导致磁电耦合的机制。
- [[../concepts/proper-screw|proper-screw]]：自旋摆线型磁序的多铁机制。
- [[../concepts/ferroelectricity|铁电性]]：弱铁磁多铁材料中的有序分量。
- [[../entities/BiFeO3|BiFeO₃]]：弱铁磁-铁电多铁的典型代表体系。
*（内容由AI生成，仅供参考）*
