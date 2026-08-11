---
tags: [entity]
---

# GeSe (锗化硒)

GeSe 是第四族单硫族化物（Group-IV Monochalcogenides, MX）的典型代表，在二维极限下展现出强耦合的**相锁定特性（Phase-Locked Properties）**。其单层结构具有类黑磷的褶皱（puckered）四方对称性（空间群 *Pnma*），自发打破了反演对称性。

### 强耦合铁弹-铁电性
单层 GeSe 的核心物理特征在于其铁弹性（Ferroelasticity）与铁电性（Ferroelectricity）的强耦合。这种耦合源于离子势能的非谐性，导致原子位移产生的自发极化 $P$ 与晶格畸变产生的自发应变 $\eta$ 在空间取向上完全锁定。

在热力学基态下，GeSe 存在四个能量等效的畴变体（Domain Variants）：$(\eta_x, \pm P_x)$ 和 $(\eta_y, \pm P_y)$。这意味着当通过外场（电场或机械应变）翻转其中一个序参量时，另一个序参量必须协同发生 90° 旋转或 180° 翻转。这种“锁相”机制为多场调控提供了物理基础 [[../papers/yangRipplingFerroicPhase2021]]。

### 波纹效应与相变动力学
作为一种典型的柔性二维材料，GeSe 单层的面外弯曲柔韧性导致其本征存在“波纹”（Ripples）或褶皱位错（Ripplocations）。研究表明，波纹在 GeSe 的相变过程中扮演了双重角色：
1. **稳定短程序**：在高温顺电相中，波纹通过引入局域化应变场，能够稳定局域的短程铁性序，形成长寿命的极性纳米微区（Polar Nano-regions）。这些微区在冷却过程中充当异质形核点，显著提升了铁性相变温度 $T_c$（加热约 310 K，冷却约 260 K） [[../papers/yangRipplingFerroicPhase2021]]。
2. **调控翻转动力学**：本征波纹的存在打破了畴翻转的长程协同性。在理想无约束体系中，畴翻转通常表现为高度协同的雪崩动力学（Avalanche Dynamics），应力降服从幂律分布；而在波纹存在的情况下，畴翻转转变为由局域化应变驱动的独立随机过程，统计特征从幂律分布转向高斯分布 [[../papers/liPhaseTransitions2D2021]]。

### 性能指标与展望
理论预测单层 GeSe 具有巨大的面内自发极化（约 151-506 pC/m）和极高的居里温度，这使其在室温电子器件中具有巨大的应用潜力 [[../papers/huProgressProspectsLowdimensional2019]]。此外，γ-GeSe 等多晶型相被预测具备本征的多铁性（铁电与铁磁共存），为探索超快磁电耦合提供了新平台 [[../papers/tangMultiferroicityTwodimensionalVan2025]]。通过“波纹工程”（Ripple Engineering）主动调控其表面形貌，有望实现对 GeSe 畴结构及物理性能的按需定制。

## Related Papers

- [[../papers/yangRipplingFerroicPhase2021]] — 关于波纹对 GeSe 铁性相变及畴翻转影响的系统 MD 研究。
- [[../papers/huProgressProspectsLowdimensional2019]] — 综述了包括 GeSe 在内的 IV 族单硫族化物的巨极化特性。
- [[../papers/liPhaseTransitions2D2021]] — 探讨了 GeSe 中铁性序与维度、柔性的关系。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]] — 提及 γ-GeSe 的多铁性理论预测。
- [[../papers/guanRecentProgressTwoDimensional2020]] — 梳理了二维铁电机制分类，涵盖了 GeSe 的层内键合机制。
