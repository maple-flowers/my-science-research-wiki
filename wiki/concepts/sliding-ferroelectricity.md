---
tags: [concept, ferroelectricity, 2D, sliding, interlayer, Moire]
category: [D02, Z01]
---

# 滑动/堆叠铁电性 / Sliding (Stacking-engineered) Ferroelectricity

**滑动铁电性**（Sliding Ferroelectricity）是范德华（vdW）层状材料中涌现的一种非本征铁电机制。即使单层材料具有反演对称性（非铁电），通过特定的层间堆垛工程（如 3R 相、扭转角形成的莫尔超晶格），利用**层间相对滑动**打破空间反演对称性，可诱导产生垂直于层平面的面外极化（$P_z$）或面内极化。

该机制于 2017 年由 Li 和 Wu 首次通过第一性原理计算预测，并在 h-BN、TMDs 等体系中得到实验验证。它颠覆了传统铁电性依赖离子位移的范式，为原子级厚度下的稳定铁电序及高速、低功耗器件应用提供了新平台。

![滑动铁电机制](raw/figures/wuSlidingFerroelectricity2D2021a/fig_1_37UWP3F7.png)
*图 1: 滑动铁电机制示意图。(A) BN 双层通过层间滑移实现极化翻转；(B) 扭转 BN 双层中的莫尔铁电畴；(C) 3R 相 MoS₂ 和 InSe 的结构。*

## 核心物理机制

1. **层间电荷转移**：
   极化起源于层间电子轨道的重叠与费米能级的分裂，导致界面电荷重新分布。层间滑移改变了原子的对齐方式（如从 AB 到 BA 堆垛），从而改变了电荷转移的方向，实现极化翻转。
2. **超低翻转势垒**：
   不同于传统钙钛矿铁电体（位移型）需要克服强化学键的断裂与重组，滑动铁电体仅需克服弱范德华力的滑移势垒，其翻转能量通常低 1-2 个数量级。
3. **畴壁（Domain Wall）动力学**：
   滑动铁电体的开关过程由畴壁运动主导。研究表明，h-BN 双层中的畴壁宽度可达 10–40 nm（远宽于传统铁电体）。畴壁运动使临界翻转电场比单畴均匀翻转降低约两个数量级（如 0.026 V/nm vs 1.41 V/nm）。在高电场下，畴壁速度可达数千米每秒，实现皮秒级超快翻转（[[../../raw/note/heUltrafastSwitchingDynamics2024]]）。
4. **莫尔超晶格与超顺电性**：
   在小角度扭转双层中，周期性的堆垛梯度形成纳米畴阵列。理想的莫尔超晶格呈现**超顺电行为**（Super-paraelectricity），即极化响应无滞后且撤去电场后消失。实验观察到的回滞通常源于缺陷（如氮空位，钉扎能约 50 meV）对畴壁的钉扎效应。

![畴壁结构](raw/figures/heUltrafastSwitchingDynamics2024/fig_5_BK4H4WHC.png)
*图 2: h-BN 双层中 0° (Bloch-type) 和 90° (Néel-type) 畴壁的原子结构与极化分布。*

## 代表性材料体系

| 材料类别 | 代表体系 | 关键特征 |
| :--- | :--- | :--- |
| **绝缘体** | [[h-BN]] | 最典型的滑动铁电体，AB/BA 滑动诱导极化，室温稳定，抗疲劳。 |
| **半导体** | [[TMDs]] (MoS₂, WSe₂) | 3R 相天然具备滑动铁电性；2H 相通过扭转产生莫尔铁电。 |
| **半金属** | [[WTe2]], [[Graphene]] | 扭转双层石墨烯（>3层）或石墨烯/h-BN 异质结中可观测到滑动铁电响应。 |
| **III-VI 族** | [[In2Se3]], [[GaSe]] | 本征极化与滑动诱导极化联动，实现多态切换。 |
| **磁性材料** | [[Fe3GeTe2]] | 滑动诱导磁性铁电金属相（Multiferroic Metal）。 |

![不同堆垛相](raw/figures/wuSlidingFerroelectricity2D2021a/fig_2_UQ8NW6V3.png)
*图 3: 不同堆垛构型下的极性相与非极性相（BN, MoS₂, SnS₂, WTe₂, CrI₃）。*

## 关键表征技术

- **PFM (压电力显微镜)**：通过观测 180° 相位翻转和蝴蝶曲线证实极化翻转。
- **SHG (二次谐波产生)**：对空间反演对称性破缺极度敏感，用于鉴定非中心对称结构。
- **4D-STEM (四维扫描透射电镜)**：在皮米（pm）尺度直接观察层间位移和莫尔条纹重构（[[../../raw/note/sunSlidingFerroelectricityTwodimensional2025]]）。

## 器件应用潜力

滑动铁电性因其**原子级厚度**、**高居里温度**和**本征抗疲劳性**，在下一代电子学中展现出巨大优势：

1. **铁电场效应晶体管 (FeFET)**：基于 3R-MoS₂ 的器件可实现 >10⁴ 次循环的稳定读写，翻转时间在纳秒级。
2. **铁电隧道结 (FTJ)**：利用原子级薄层作为隧穿势垒，实现高达 10³ 的开关比（ON/OFF ratio）。
3. **类脑突触器件**：模拟生物突触的长时程增强/抑制（LTP/LTD），功耗可低至 20 pW。
4. **多铁存储**：在 2D 磁性材料中通过滑移耦合磁序与电序，实现磁电互控存储。

![器件应用](raw/figures/RecentAdvancesGrowth2025/fig_15_TMK8S5HG.png)
*图 4: 二维滑动铁电在 FET、FTJ、突触器件及多铁存储中的应用前景。*

## 本库相关论文

- **物理机制与模拟**：
  - [[../../raw/note/heUltrafastSwitchingDynamics2024]]：使用机器学习势揭示 h-BN 超快畴壁动力学与莫尔超顺电本质。
  - [[../../raw/note/heSwitchingTwodimensionalSliding2025]]：机械应变对滑动铁电翻转的调控。
  - [[../../raw/note/kaurRecentAdvancesTheoretical2025a]]：二维滑动铁电理论计算进展综述。
- **材料体系探索**：
  - [[../../raw/note/miaoMagneticFerroelectricMetal2024]]：双层 Fe₃GeTe₂ 中的滑动诱导磁性铁电金属。
  - [[../../raw/note/tangCombiningIntrinsicSlidinginduced2025]]：结合本征与滑动极化实现多态存储。
  - [[../../raw/note/wuSlidingFerroelectricity2D2021a]]：滑动铁电物理与器件早期综述。
- **器件应用**：
  - [[../../raw/note/sunSlidingFerroelectricityTwodimensional2025]]：2D 滑动铁电在存储、计算及人工突触中的最新应用综述。
  - [[../../raw/note/zhangEmergingFrontiersTwodimensional2025]]：二维铁电前沿展望。

## 关联概念

- [[moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[super-paraelectricity|超顺电性 Super-paraelectricity]]
- [[polarization-switching|极化翻转 Polarization Switching]]
- [[../entities/domain-wall|畴壁 Domain Wall]]
- [[../entities/h-BN|氮化硼 h-BN]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
