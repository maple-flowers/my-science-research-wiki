---
tags: [concept, ferroelectricity, 2D, sliding, interlayer, moire]
title: 滑动/堆叠铁电性 / Sliding (Stacking-engineered) Ferroelectricity
type: concept
status: mature
category: [D02, Z01]
domain: ferroelectricity
mechanism: 层间相对滑移打破反演对称，由界面电荷重分布诱导极化
related_concepts: [moire-superlattice, super-paraelectricity, polarization-switching, interfacial-charge-rearrangement, slidetronics, domain-wall-motion]
aliases: ["滑移铁电性", "Sliding Ferroelectricity", "Stacking-engineered ferroelectricity"]
key_quantities:
  origin: "Li & Wu 2017 理论提出；首个实验体系为双层 WTe2 (Fei et al., Nature 2018)"
  barrier: "翻转为弱范德华滑移势垒，较离子位移型低 1–2 个数量级"
  hbn_domain_wall: "h-BN 畴壁宽 10–40 nm，临界场 ~0.026 V/nm（单畴 ~1.41 V/nm）"
papers: [wuSlidingFerroelectricity2D2021a, heUltrafastSwitchingDynamics2024, kaurRecentAdvancesTheoretical2025a, guoAdvancesTwodimensionalFerroelectric2025, tianRoomtemperatureTwodimensionalMultiferroic2026, sunSlidingFerroelectricityTwodimensional2025]
updated: 2026-08
---

# 滑动/堆叠铁电性 / Sliding (Stacking-engineered) Ferroelectricity

**滑动铁电性**（Sliding Ferroelectricity）是范德华（vdW）层状材料中涌现的一种非本征铁电机制：即使单层本身具有反演对称性（非铁电），只要通过特定堆垛（3R 相、转角莫尔超晶格）让层与层发生**相对滑动**而打破空间反演对称，就能由层间界面的电荷重分布诱导出垂直层面的面外极化 $P_z$（或面内极化）。该机制由 Li 和 Wu 于 2017 年首次理论预测，并在双层 WTe2、h-BN、TMDs 等体系实验验证，颠覆了"铁电必须靠离子位移"的传统范式 [[../papers/wuSlidingFerroelectricity2D2021a]] [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]。

## 👵 太奶导读

太奶，您把这类材料想成一摞透明的薄饼。传统"铁电"能记住电方向，靠的是饼里的芝麻（原子）从这头搬到那头——搬一次得扯断化学键，费劲。可"滑动铁电"另辟蹊径：芝麻根本不用动地方，只要把上面那张饼贴着下面那张轻轻一搓、换个叠法，两张饼交接处的电子云就不对称了，凭空攒出一个电的方向来；再往回一搓，方向就反过来。

因为搓动只须克服两张饼之间那点微弱的"粘劲儿"（范德华力），比拽着原子搬家省力一到两个数量级，所以又快又省电、还不容易累。要是把两张饼拧一个小角度，还能叠出像碎花布一样的"莫尔"格子，上面布满一小块一小块朝向不同的电区（铁电畴），可用来做密度极高的存储。更稀罕的是，这招连能导电的金属饼都管用——比如某些磁性薄片，一搓之下磁和电一块儿变，于是"用电指挥磁"做省电存储器就有了着落。一句话：它记住信息不靠原子搬家，而靠"换个叠法"。

## 🧩 核心物理机制

![图：滑动铁电机制示意——(A) BN 双层经层间滑移翻转极化，(B) 转角 BN 中的莫尔铁电畴，(C) 3R 相 MoS2 与 InSe 结构](../../raw/figures/wuSlidingFerroelectricity2D2021a/fig_1_37UWP3F7.png)
*   **看图要点**：(A) 中两层从 AB 滑到 BA，界面电荷转移方向反向、极化翻转；(B) 小转角把堆垛梯度铺成周期性莫尔铁电畴阵列；(C) 3R 相同向堆叠天然破缺反演对称 [[../papers/wuSlidingFerroelectricity2D2021a]]。
*   **来源**：[[../papers/wuSlidingFerroelectricity2D2021a]] -> [[../figures/heterostructures-stacking-sliding|层间滑移]]

1.  **层间电荷重分布**：极化来自层间电子轨道重叠与费米能级分裂导致的界面电荷转移。层间滑移改变原子对齐方式（AB↔BA），就改变电荷转移方向，从而翻转极化；母体无须本征极性，导体、半导体、绝缘体皆可。
2.  **超低翻转势垒**：不同于钙钛矿铁电体须断裂/重组强化学键，滑动翻转只克服弱范德华滑移势垒，能量通常低 1–2 个数量级，理论上支持纳秒甚至更快翻转。
3.  **畴壁动力学**：开关由畴壁运动主导。h-BN 双层畴壁宽达 10–40 nm（远宽于传统铁电体），使临界翻转电场较单畴均匀翻转降低约两个数量级（约 0.026 V/nm 对 1.41 V/nm）；高场下畴壁速度可达数千米每秒，对应皮秒级翻转 [[../papers/heUltrafastSwitchingDynamics2024]]。
4.  **莫尔超晶格与超顺电性**：小角度扭转双层的堆垛梯度形成纳米畴阵列；理想莫尔超晶格呈**超顺电**行为（无滞后、撤场即消），实验观测到的回滞多源于缺陷（如氮空位，钉扎能约 50 meV）对畴壁的钉扎。

![图：h-BN 双层中 0°(Bloch 型) 与 90°(Néel 型) 畴壁的原子结构与极化分布](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_5_BK4H4WHC.png)
*   **关键特征**：两种畴壁的极化旋转路径不同，决定其迁移率与临界场；机器学习势模拟揭示莫尔超顺电本质与皮秒级畴壁运动 [[../papers/heUltrafastSwitchingDynamics2024]]。
*   **来源**：[[../papers/heUltrafastSwitchingDynamics2024]] -> [[../figures/domain-walls|畴与畴壁]]

## 🎯 多铁金属、相位锁定与神经形态

- **室温二维多铁金属**：铁电性与金属性本被认为互斥（自由电子屏蔽偶极），但双层 CrTe2、Fe3GeTe2 等打破此范式。以双层 CrTe2 为例，FM 层与 z-AFM 层间的自发层间电荷转移既破缺反演对称诱导面外极化，又通过电子填充调控磁序，实现室温（300 K）空气稳定的"电写磁读"多铁金属 [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]。
- **相位锁定（Phase-Locking）**：低维下电子序（电荷转移、磁序）与晶格拓扑（莫尔条纹、特定堆垛相位）高度耦合，抑制室温热涨落、稳定铁电畴，并使极化翻转对应变高度敏感，便于应变工程微调。
- **多态与神经形态**：精确控制层间滑移量（转角、微位移）可得到连续可调的极化中间态，超越二进制 0/1；据此构筑的人工突触支持长时程增强/抑制（LTP/LTD），翻转功耗可低至皮瓦（pW）量级 [[../papers/sunSlidingFerroelectricityTwodimensional2025]]。

## 📊 代表性材料体系

![图：BN、MoS2、SnS2、WTe2、CrI3 等在不同堆垛构型下的极性相与非极性相](../../raw/figures/wuSlidingFerroelectricity2D2021a/fig_2_UQ8NW6V3.png)
*   **关键特征**：同一母体在不同堆垛下极性有别——同向（R/AB）堆叠多破缺反演对称而具极性，反向（AA′）堆叠常抵消极化；这正是"堆叠工程"开关铁电的结构依据 [[../papers/wuSlidingFerroelectricity2D2021a]]。
*   **来源**：[[../papers/wuSlidingFerroelectricity2D2021a]] -> [[../figures/heterostructures-stacking|层间堆垛总览]]

| 材料类别 | 代表体系 | 关键特征 |
| :--- | :--- | :--- |
| **绝缘体** | [[../entities/h-BN\|h-BN]] | 最典型体系，AB/BA 滑动诱导极化，室温稳定、抗疲劳 |
| **半导体** | [[../entities/TMDs\|TMDs]]（MoS2、WSe2） | 3R 相天然滑动铁电；2H 相经转角产生莫尔铁电；3R-MoS2 支持多态存储 |
| **半金属** | [[../entities/WTe2\|WTe2]]、[[../entities/Graphene\|石墨烯]] | 双层 WTe2 为首个实验证实的滑移铁电（铁电金属）；石墨烯/BN 中亦见响应 |
| **III–VI 族** | [[../entities/In2Se3\|In2Se3]]、GaSe | 本征极化与滑动极化联动，实现多态切换 |
| **磁性材料** | [[../entities/CrTe2\|CrTe2]]、[[../entities/Fe3GeTe2\|Fe3GeTe2]] | 滑动/电荷转移诱导室温多铁金属 |

## 🔬 表征与器件

- **表征**：PFM（180° 相位翻转与蝴蝶曲线证实极化翻转）、SHG（对反演对称破缺极敏感）、4D-STEM（在皮米尺度直接观察层间位移与莫尔重构）[[../papers/sunSlidingFerroelectricityTwodimensional2025]]。
- **器件**：FeFET（3R-MoS2 器件 >10⁴ 次稳定读写、纳秒翻转）、铁电隧道结 FTJ（原子级势垒、开关比可达 10³）、类脑突触（LTP/LTD，功耗可低至 ~20 pW）、多铁存储器（磁电互控）。

![图：二维滑动铁电在 FET、FTJ、突触器件及多铁存储中的应用前景](../../raw/figures/RecentAdvancesGrowth2025/fig_15_TMK8S5HG.png)
*   **来源**：[[../papers/RecentAdvancesGrowth2025]] -> [[../figures/electronic-devices|电子与突触器件]]

## 📚 相关论文 (Related Papers)

- **机制与模拟**：[[../papers/wuSlidingFerroelectricity2D2021a]]（物理与器件早期综述）、[[../papers/heUltrafastSwitchingDynamics2024]]（机器学习势揭示 h-BN 超快畴壁动力学与超顺电本质）、[[../papers/heSwitchingTwodimensionalSliding2025]]（应变调控翻转）、[[../papers/kaurRecentAdvancesTheoretical2025a]]（理论计算综述）。
- **多铁金属**：[[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]（双层 CrTe2 室温多铁金属）、[[../papers/miaoMagneticFerroelectricMetal2024]]（双层 Fe3GeTe2 磁性铁电金属）。
- **材料与器件**：[[../papers/guoAdvancesTwodimensionalFerroelectric2025]]（确立滑移铁电范式）、[[../papers/tangCombiningIntrinsicSlidinginduced2025]]（本征+滑动极化多态存储）、[[../papers/sunSlidingFerroelectricityTwodimensional2025]]（存储/计算/突触应用综述）、[[../papers/zhangEmergingFrontiersTwodimensional2025]]（前沿展望）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[moire-superlattice|莫尔超晶格]]、[[super-paraelectricity|超顺电性]]、[[polarization-switching|极化翻转]]、[[interfacial-charge-rearrangement|层间电荷重排]]、[[slidetronics|滑移电子学]]、[[domain-wall-motion|畴壁运动]]
- [[../entities/h-BN|h-BN]]、[[../entities/TMDs|TMDs]]、[[../entities/WTe2|WTe2]]、[[../entities/In2Se3|In2Se3]]、[[../entities/CrTe2|CrTe2]]、[[../entities/Fe3GeTe2|Fe3GeTe2]]、[[../entities/domain-wall|畴壁]]
