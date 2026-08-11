---
tags: [entity, domain-wall, ferroic, topological, sliding-ferroelectricity, strain-engineering]
category: [D02, Z01]
---

# 畴壁 / Domain Wall (DW)

畴壁是分隔不同铁性畴（如极化取向不同的铁电畴、磁化取向不同的铁磁畴、或自发应变不同的铁弹畴）的界面拓扑缺陷。在二维材料及纳米复合体系中，畴壁的静态拓扑结构与动态迁移行为不仅决定了材料的宏观铁性响应（如矫顽场、翻转速度），还展现出不同于体相的奇特物理态。

## 核心物理特性与研究进展

### 1. 二维滑动铁电体中的超宽畴壁与超快动力学
在范德华双层体系（如 [[h-BN]]、[[TMDs]]）中，畴壁的性质受层间超低滑移势垒与面内强共价键刚度共同支配：
- **超宽畴壁**：双层 h-BN 的畴壁宽度可达 **10~40 nm**（0° 壁~9.7 nm，90° 壁~40.7 nm），远超传统钙钛矿铁电体（~1 nm）。其中 0° 壁呈现布洛赫型（Bloch-type）极化织构，而 90° 壁则伴随明显的面外屈曲（buckling）并呈现奈尔型（Néel-type）特征（[[../../raw/note/heUltrafastSwitchingDynamics2024|He et al., 2024]]）。
- **极速开关**：畴壁运动介导的极化翻转场（约 **0.026 V/nm**）比单畴均匀翻转场低两个数量级。在 0.18 V/nm 的电场下，畴壁运动速度可达 **~6000 m/s**，实现皮秒级（~15 ps）的超快开关。
- **超顺电态 (Super-paraelectricity)**：在扭转形成的莫尔超晶格中，系统呈现无滞后的超顺电响应。实验观测到的铁电回滞通常源于晶体缺陷（如氮空位 $V_N$）对畴壁的钉扎效应，单个空位的钉扎能约 **50 meV**。

### 2. 应变工程对畴壁类型的精准调控
应变工程是调控二维多铁性材料（如 $\beta'$-In$_2$Se$_3$）畴结构的有力手段，能够克服电场调控易导致漏电的问题：
- **畴壁构型切换**：应变方向与畴壁线的夹角决定了其演化路径。例如，沿垂直于 180° 畴壁方向施加 4% 的拉伸应变可将其转变为 60° 畴壁；而平行于 60° 畴壁的应变可将其转变为 180° 畴壁（[[../../raw/note/gaoStrainEngineeringFerroelectric2024|Gao et al., 2024]]）。
- **势垒降低机制**：应变不仅改变不同极化变体的相对稳定性，还能显著降低相变势垒（在 2% 应变下势垒可降至近零），触发自发的铁电-铁弹相变。

### 3. 几何挫折与拓扑缺陷自组装
在铁电纳米复合体系中，通过调控几何约束可实现拓扑缺陷的复杂排列：
- **自组织涡旋阵列**：在 BTO/BST 纳米材料中，手性诱导的几何挫折会导致涡旋（Vortices）与反涡旋（Antivortices）自组装形成规则阵列。
- **挫折指数**：体系的挫折指数 **$f \approx 3.1-4.0$**，展现出类液体的“浮动”特征及显著的剩余熵（[[../../raw/note/nahasFrustrationSelfOrderingTopological2016|Nahas et al., 2016]]）。

### 4. 导电畴壁与功能界面
畴壁本身可作为纳米级的功能器件实体：
- **金属性界面态**：在 Weyl 半金属 $T_d$-MoTe$_2$ 中，极化畴壁或 $T_d/1T'$ 相畴壁处存在增强的电导，这与高阶拓扑铰链态（Hinge states）或特定的相变诱导态有关（[[../../raw/note/huangPolarPhaseDomain2019|Huang et al., 2019]]）。
- **畴壁纳米电子学**：利用畴壁的导电性与可移动性，可设计非易失性存储器（如 FTJ 阻态连续调控）与新型拓扑逻辑器件（[[../../raw/note/fiebigEvolutionMultiferroics2016|Fiebig et al., 2016]]、[[../../raw/note/sunSlidingFerroelectricityTwodimensional2025|Sun et al., 2025]]）。

## 本库相关论文

- [[../../raw/note/heUltrafastSwitchingDynamics2024|Ultrafast switching dynamics of the ferroelectric order in stacking-engineered ferroelectrics]] (Acta Mater. 2024) —— 揭示滑动铁电中的超宽畴壁与皮秒级动力学。
- [[../../raw/note/gaoStrainEngineeringFerroelectric2024|Strain engineering of ferroelectric polarization and domain in the two-dimensional multiferroic semiconductor]] (APL 2024) —— 论证应变对 $\beta'$-In$_2$Se$_3$ 畴壁类型的调控规律。
- [[../../raw/note/huangPolarPhaseDomain2019|Polar and phase domain walls with conducting interfacial states in WTe2]] —— 发现 Weyl 半金属中畴壁介导的导电界面态。
- [[../../raw/note/nahasFrustrationSelfOrderingTopological2016|Frustration and self-ordering of topological defects in ferroelectrics]] (Nat. Commun. 2016) —— 探讨几何挫折诱导的拓扑缺陷自组织。
- [[../../raw/note/fiebigEvolutionMultiferroics2016|The evolution of multiferroics]] —— 综述多铁材料中畴壁纳米电子学的发展。
- [[../../raw/note/sunSlidingFerroelectricityTwodimensional2025|Sliding ferroelectricity in two-dimensional materials]] —— 讨论滑动铁电在隧道结阻态调控中的应用。

## 关联概念
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/super-paraelectricity|超顺电性 Super-paraelectricity]]
- [[../concepts/strain-engineering|应变工程 Strain Engineering]]
- [[../concepts/topological-defects|拓扑缺陷 Topological Defects]]
- [[deep-potential|机器学习势 Deep Potential]]
- [[h-BN|六方氮化硼 h-BN]]
