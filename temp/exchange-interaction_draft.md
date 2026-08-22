---
tags: [concept, magnetism, many-body-physics]
title: 交换作用 / Exchange Interaction
type: concept
status: mature
domain: [magnetism, strongly-correlated-electron-systems, first-principles]
mechanism: 自旋间有效相互作用，源于库仑排斥与泡利原理（直接交换）或中间态虚跃迁（超交换/动力学交换）；符号决定磁有序类型：J>0 铁磁，J<0 反铁磁
related_concepts: [ferromagnetism, antiferromagnetism, heisenberg-model, molecular-field, spin-wave, weak-ferromagnetism, spin-spiral, dzyaloshinskii-moriya-interaction, spin-orbit-coupling, d0-rule]
papers: [vanvleckSurveyTheoryFerromagnetism1945, deSousa2008electrical, heUltrafastSwitchingDynamics2024, shishkinImplementationPerformanceFrequencydependentGWmethod2006, tangMultiferroicityTwodimensionalVan2025, wuElectrostaticGatingIntercalation2022]
updated: 2026-08
---

# 交换作用 / Exchange Interaction

交换作用（exchange interaction）是**自旋之间有效相互作用的统称，其物理根源是库仑排斥与泡利不相容原理的结合**，而非磁偶极相互作用。它以交换积分 J 进入自旋哈密顿量 $U_{ij}=-2J_{ij}\mathbf{S}_i\cdot\mathbf{S}_j$，J 的符号直接决定磁有序的类型：J>0 偏好自旋平行（铁磁），J<0 偏好自旋反平行（反铁磁）。交换作用是铁磁、反铁磁、亚铁磁、自旋螺旋等一切磁有序态的微观起源，也是磁电多铁、高温超导等强关联物理的共同底层。

## 👵 太奶导读

两个电子靠在一起，为什么有的"拧成一股绳"（自旋平行）、有的非要"背对背"（自旋反平行）？这跟磁铁本身的"同性相斥"没关系，而是电子之间有"看不见的规矩"——泡利原理：两个电子不能待在同一个状态里。于是它们要么尽量分开（代价是动能变大，但避开强烈的电荷排斥），要么在中间区域"错开"（自旋反平行，波函数反对称）。这些算计算到最后，就折算成一个叫"交换积分 J"的数字：J 是正的，电子们倾向手拉手（铁磁）；J 是负的，电子们倾向背靠背（反铁磁）。科学家只要算出材料的 J，就能预言它磁性上是什么性格。

## 🧩 直接交换与海森堡模型

Van Vleck 在 1945 年综述（[[../papers/vanvleckSurveyTheoryFerromagnetism1945]]）中系统整理了交换作用理论：自旋对之间的能量由交换积分 J 与自旋标积 $\mathbf{S}_i\cdot\mathbf{S}_j$ 决定，模型可统一写为海森堡交换哈密顿量（[[../concepts/heisenberg-model|海森堡模型]]）。其微观图像是：库仑排斥使两电子避免占据同一空间区域，泡利原理则强制自旋平行电子波函数反对称（空间对称）、自旋反平行电子波函数对称（空间反对称），两种代价的平衡决定 J 的符号与大小。对 J<0 的情况，晶格划分为两套交错子晶格，构成反铁磁序（[[../concepts/antiferromagnetism|反铁磁性]]）——这是 MnO 等经典反铁磁体的理论基础。

除直接交换外，还有超交换（superexchange，经氧等配位离子的中间态虚跃迁）、双交换（double exchange）与动力学交换等更复杂的通道，它们共同构成"交换作用"这一家族。

## 🌀 反对称交换：DM 相互作用

当体系存在自旋轨道耦合（[[../concepts/spin-orbit-coupling|自旋轨道耦合]]）且晶格对称性允许时，交换作用还会出现反对称项——**Dzyaloshinskii–Moriya（DM）相互作用**，能量写为 $\mathbf{D}_{ij}\cdot(\mathbf{S}_i\times\mathbf{S}_j)$。DM 项偏好相邻自旋互相垂直，是许多磁序偏离共线的推手：它使反铁磁体的自旋发生微小倾斜，产生弱铁磁净矩（[[../concepts/weak-ferromagnetism|弱铁磁性]]），也可能稳定自旋螺旋（[[../concepts/spin-spiral|自旋螺旋]]）与非共线磁序。

de Sousa 与 Moore（[[../papers/deSousa2008electrical]]）正是利用 BiFeO₃ 中 DM 交换导致的倾斜反铁磁序，构建了电场控制磁振子传播的理论模型：倾斜反铁磁体中的磁静波效应使最低频自旋波色散强烈各向异性——传播方向垂直于奈尔矢量时模式无能隙、群速度高，平行时打开磁静波能隙、群速度为零。结合实验中已证实的电场翻转奈尔矢量，即可用纯电场"开关"长波长磁振子传播，为超低功耗自旋波逻辑器件奠定基础。

![图：BiFeO3 中极化与自旋 DM 耦合的图像](<../../raw/figures/deSousa2008electrical/fig_1_MFP3ILKR.png>)

*关键特征：弱铁磁净矩与铁电极化经 DM 型磁电耦合锁定，电场可翻转奈尔矢量并调制自旋波传播。*
*来源：[[../papers/deSousa2008electrical]] -> [[../figures/electronic-bands-cdw-transport|电子结构与输运：CDW与输运性质]]*

![图：倾斜反铁磁体中磁静波效应导致的自旋波色散](<../../raw/figures/deSousa2008electrical/fig_2_R7A39F2L.png>)

*关键特征：最低频自旋波模式色散的传播各向异性：垂直奈尔矢量方向无能隙、平行方向打开磁静波能隙，实现电场开关磁振子。*
*来源：[[../papers/deSousa2008electrical]] -> [[../figures/electronic-bands-band-structures|电子结构与输运：能带结构与带隙]]*

## 🔄 交换作用的多尺度角色

交换作用在多铁性与堆叠工程铁电中同样关键：tang 综述（[[../papers/tangMultiferroicityTwodimensionalVan2025]]）指出二维范德华多铁中层间堆叠与磁交换耦合相互交织，层间滑移可在改变铁电极化的同时调制磁交换与磁序；wu 等（[[../papers/wuElectrostaticGatingIntercalation2022]]）展示了静电栅压与插层（[[../concepts/intercalation|插层]]）如何通过改变载流子浓度与层间耦合来原位调控交换作用。在激发态计算层面，GW 方法（[[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]]）的核心——Fock 交换项——正是对交换作用在准粒子自能中的多体处理，其在 PAW 框架下的高效实现奠定了 VASP 中高精度带结构计算的基础。而 he 等（[[../papers/heUltrafastSwitchingDynamics2024]]）从动力学角度揭示，堆叠工程铁电体中畴壁运动使极化翻转场降低两个数量级并实现皮秒级超快翻转，其中交换作用与堆叠序的竞争主导了畴壁宽度（10–40 nm）与低翻转势垒。

## 📚 相关论文 (Related Papers)

- [[../papers/vanvleckSurveyTheoryFerromagnetism1945]]：系统建立交换作用理论——J 的符号决定铁磁/反铁磁有序，交错子晶格图像与 MnO 检验。
- [[../papers/deSousa2008electrical]]：DM 反对称交换使反铁磁倾斜产生弱铁磁，电场控制磁振子传播的理论模型。
- [[../papers/heUltrafastSwitchingDynamics2024]]：堆叠工程铁电体中畴壁运动驱动超快、低能耗极化翻转。
- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]]：GW 方法中 Fock 交换项的 PAW 高效实现，交换作用的多体处理。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：二维范德华多铁综述，层间堆叠与磁交换耦合交织。
- [[../papers/wuElectrostaticGatingIntercalation2022]]：静电栅压与插层对二维材料交换耦合与电子态的调控。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferromagnetism|铁磁性]]：J>0 交换作用导致的平行自旋有序。
- [[../concepts/antiferromagnetism|反铁磁性]]：J<0 交换作用导致的交错反平行有序。
- [[../concepts/heisenberg-model|海森堡模型]]：交换作用的量子自旋哈密顿量表述。
- [[../concepts/molecular-field|外斯分子场]]：把交换作用平均化为有效场的近似。
- [[../concepts/spin-wave|自旋波]]：交换作用驱动的自旋集体激发。
- [[../concepts/weak-ferromagnetism|弱铁磁性]]：DM 交换作用使反铁磁自旋倾斜产生的净磁矩。
- [[../concepts/spin-spiral|自旋螺旋]]：DM 交换与非共线磁序，磁电耦合的一种微观机制。
- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：DM 反对称交换与磁各向异性的微观来源。
- [[../concepts/d0-rule|d⁰规则]]：交换作用/磁性对 d 电子占据的要求与铁电性 d⁰ 需求的矛盾。
- [[../concepts/multiferroicity|多铁性]]：交换作用决定的磁序与铁电序共存。
- [[../entities/MnO|MnO]]：交换作用（J<0）理论检验的经典反铁磁体。
- [[../entities/bifeo3|BiFeO₃]]：DM 交换与倾斜反铁磁磁电耦合的代表体系。
