---
tags: [concept]
title: '反铁磁性 / Antiferromagnetism'
type: concept
status: developing
papers: ['vanvleckSurveyTheoryFerromagnetism1945', 'rameshMultiferroicsProgressProspects2007', 'Goswami2011multiferroic', 'Kim2008effect', 'Kang2012dimer', 'petkovStructureIntercalatedCs2002']
updated: 2026-08-18
---



# 反铁磁性 / Antiferromagnetism

反铁磁性（antiferromagnetism）是**相邻自旋通过负交换积分（J<0）反平行排列、使体系宏观净磁化近乎为零**的磁有序态。它由 Louis Néel 于 1936 年提出，可通过将晶格划分为两套交错子晶格（A/B）来描述：每套子晶格内部自旋平行，两套之间反平行。反铁磁体存在特征温度**奈尔温度 T_N**：T>T_N 时磁序消失，磁化率满足居里-外斯定律 χ=C/(T+θ)；T<T_N 时磁化率随降温反而下降。反铁磁序是高温超导、多铁性、自旋电子学等众多前沿领域的共同物理背景。

## 👵 太奶导读

想象一排排相邻的士兵，每个士兵都盯着旁边的人，非要和邻居"脸对脸"站着（自旋反平行）——结果整支队伍虽然每个士兵都很"有原则"，但整体上各种方向完全抵消，对外没有一点磁性。这叫反铁磁。它有个怪脾气：温度太高时（超过奈尔温度）士兵们热得顾不上原则，乱站（顺磁）；温度一降下来，士兵们开始按原则"脸对脸"排好，磁性反而被"锁死"，磁化率还会下降。科学家经常用反铁磁当"背景板"——比如很多高温超导材料、多铁材料，底下都垫着一层反铁磁的磁序。

## 🧩 微观起源：负交换作用与交错子晶格

反铁磁序的微观起源是**负的交换积分**。在交换作用（[[../concepts/exchange-interaction|交换作用]]）框架下，自旋对能量写为 $U_{ij}=-2J_{ij}\mathbf{S}_i\cdot\mathbf{S}_j$：当 J<0 时，相邻自旋反平行排列能量更低，从而形成反铁磁序。Van Vleck 在 1945 年综述（[[../papers/vanvleckSurveyTheoryFerromagnetism1945]]）中系统总结了这一图像：J<0 的晶格（如简单立方、体心立方）可划分为两套交错子晶格 A/B，各自内部自旋平行、两者反平行，并在奈尔温度以下建立长程反铁磁序。该综述将 Néel 的交错分子场理论正式纳入主流固体物理，是反铁磁性理论奠基文献之一。

## 📈 实验特征：奈尔温度与磁化率峰

反铁磁体的磁化率-温度曲线具有鲜明的指纹特征：T>T_N 时 χ 随降温升高（居里-外斯型 χ=C/(T+θ)）；在 T=T_N 处 χ 出现尖锐极大值；T<T_N 时 χ 随降温下降，反映 A/B 子晶格反平行排列趋于稳固、外场更难偏转自旋。T=0 时，平行/垂直外场两种构型按 1:2 权重给出 χ₀/χ_c≈2/3。

![图：反铁磁体磁化率随约化温度的变化——MnO 的奈尔温度峰](<../../raw/figures/vanvleckSurveyTheoryFerromagnetism1945/fig_6_7227PTRL.png>)

*关键特征：理论实线（交错子晶格分子场）与 MnO 实验虚线（Bizette 等）在奈尔温度处出现尖锐磁化率峰值；T<TN 时 χ 随降温下降，T=0 时平行/垂直外场按 1:2 加权给出 χ0/χc≈2/3。*
*来源：[[../papers/vanvleckSurveyTheoryFerromagnetism1945]] -> [[../figures/mathematical-models-magnetoelectric|理论模型与计算方法：磁电耦合与多铁理论]]*

## 🔬 案例一：MnO——检验交错子晶格理论的经典反铁磁体

Van Vleck 在 [[../papers/vanvleckSurveyTheoryFerromagnetism1945]] 中引用 Bizette、Squire 与 Tsai 对 MnO 的磁化率测量，作为交错子晶格分子场理论的直接检验对象。MnO 中 Mn²⁺ 自旋沿交替晶面反平行排列，其 χ(T) 实验曲线与理论在奈尔温度处整体吻合（实验 χ₀/χ_c 介于 0.3–0.85 之间）。MnO 由此成为"反铁磁性作为独立磁有序相"的教科书例证。

## 🔬 案例二：BiFeO₃——室温反铁磁多铁

反铁磁序在多铁材料中扮演核心角色。单相 BiFeO₃（BFO）是典型的室温反铁磁-铁电多铁：Fe³⁺ 自旋构成 G 型反铁磁序，并叠加一个周期约 62 nm 的自旋螺旋（[[../concepts/spin-spiral|自旋螺旋]]）调制，宏观净磁化被抑制。ramesh 与 Spaldin 综述（[[../papers/rameshMultiferroicsProgressProspects2007]]）指出，在薄膜中通过外延应变可**抑制螺旋自旋结构**，释放弱铁磁净矩，从而获得强磁电耦合（[[../concepts/magnetoelectric-coupling|磁电耦合]]）——这是多铁薄膜器件设计的关键路径。

Goswami 等（[[../papers/Goswami2011multiferroic]]）进一步在约 22 nm 的 BiFeO₃ 纳米颗粒中直接观测到公度反铁磁序：室温中子衍射给出磁传播矢量 (0,0,0)（公度磁晶格）、Fe³⁺ 有序磁矩约 3.22 μB，奈尔温度由块体约 653 K 降至约 635 K；粒径小于螺旋周期（约 62 nm）使自旋螺旋被抑制，释放的净磁化经 DM 相互作用（[[../concepts/spin-orbit-coupling|自旋轨道耦合]]来源）增强氧八面体非铁电旋转，进而通过极性-旋转耦合调控铁电极化——铁电极化在 T_N 处跃升约 30%，5 T 磁场下被抑制约 7%，证实纳米尺度下反铁磁序与铁电序的强耦合。

![图：BiFeO3 纳米颗粒中子衍射（0 T 与 5 T）与磁结构精修](<../../raw/figures/Goswami2011multiferroic/fig_3_9WFFLRUD.png>)

*关键特征：公度磁晶格（k=(0,0,0)），Fe3+ 有序磁矩约 3.22 μB；对比 0 T/5 T 精修，Bi 的 z 坐标变化使净离子位移减小约 0.06 Å，对应极化被抑制约 7%。*
*来源：[[../papers/Goswami2011multiferroic]] -> [[../figures/experimental-setups|实验装置与表征方法]]*

![图：BiFeO3 纳米颗粒跨奈尔温度的晶格参数与极化演化](<../../raw/figures/Goswami2011multiferroic/fig_4_X25BTCRC.png>)

*关键特征：T_N 处晶格体积收缩约 0.4%（磁弹耦合），离子位移与点电荷模型极化的台阶式跃升（约 30%），展示反铁磁序"从无到有"对铁电极化的强调控。*
*来源：[[../papers/Goswami2011multiferroic]] -> [[../figures/crystal-structures-xrd-phases|晶体结构与原子构型：XRD与相]]*

## 📚 相关论文 (Related Papers)

- [[../papers/vanvleckSurveyTheoryFerromagnetism1945]]：铁磁性理论综述，系统建立 J<0 时交错子晶格反铁磁理论与 MnO 磁化率检验。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：多铁薄膜综述，指出 BiFeO3 为室温反铁磁多铁，薄膜应变可抑制螺旋自旋结构。
- [[../papers/Goswami2011multiferroic]]：约 22 nm BiFeO3 纳米颗粒中反铁磁序与铁电序强耦合的直接实验证据。
- [[../papers/Kim2008effect]]：外延应变/尺寸对 BiFeO3 铁电与磁序影响的第一性原理研究。
- [[../papers/Kang2012dimer]]：铁基超导体系中与反铁磁背景相关的费米面嵌套与密度波研究。
- [[../papers/petkovStructureIntercalatedCs2002]]：低维孔道限域金属离子结构研究，与低维磁序背景相关。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferromagnetism|铁磁性]]：J>0 的平行自旋有序，反铁磁的对照物。
- [[../concepts/exchange-interaction|交换作用]]：反铁磁序的微观起源（J<0）。
- [[../concepts/heisenberg-model|海森堡模型]]：描述反铁磁自旋交换的量子模型。
- [[../concepts/molecular-field|外斯分子场]]：交错子晶格分子场理论的基础。
- [[../concepts/spin-wave|自旋波]]：反铁磁自旋激发（反铁磁磁振子）。
- [[../concepts/weak-ferromagnetism|弱铁磁性]]：反铁磁序上的微小自旋倾斜产生的净磁矩。
- [[../concepts/spin-spiral|自旋螺旋]]：BiFeO3 等反铁磁体上的非共线调制，抑制净磁化。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：反铁磁序在多铁材料中与铁电序的耦合。
- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：DM 相互作用与反铁磁磁电耦合的微观来源。
- [[../concepts/magnetoelastic-coupling|磁弹耦合]]：反铁磁序对晶格与极化的应变耦合。
- [[../concepts/multiferroicity|多铁性]]：反铁磁序与铁电序共存产生磁电响应。
- [[../entities/MnO|MnO]]：经典反铁磁体，交错子晶格理论的原型检验对象。
- [[../entities/BiFeO3|BiFeO₃]]：室温反铁磁-铁电多铁的典型代表。
- [[../entities/Cr2O3|Cr₂O₃]]：另一种经典反铁磁体。
