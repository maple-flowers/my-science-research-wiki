---
tags: [concept, ftj, memory, device, tunneling, mxene, multiferroic]
category: [D02, Z01]
---

# 铁电隧道结与非挥发存储器 / Ferroelectric Tunnel Junctions (FTJ)

由两层电极中间夹一层超薄铁电势垒层（通常 $< 5\text{ nm}$）构成的金属-铁电-金属（M/FE/M）或二维范德华异质结器件。利用铁电极化方向反转改变势垒高度/形状，从而产生巨大的**隧道开关电阻比 (Giant Electroresistance, GER / Tunneling Electroresistance, TER)**，实现非挥发性信息存储。

## 工作原理与物理机制

1. **势垒调制效应 (Tunnel Barrier Modulation)**：
   - **静电势降**：极化电荷在界面处的不完全屏蔽效应产生静电势降。当极化指向势垒较低（或屏蔽长度较短）的电极时，平均势垒高度降低，对应低阻态（LRS）；反之则对应高阻态（HRS）。
   - **巨开关比 (TER)**：在二维极限下，由于界面态的影响减弱，TER比值可达 $10^3\% - 10^6\%$ 以上。

2. **二维[[sliding-ferroelectricity|滑动铁电]] FTJ 的优势**：
   - **突破临界厚度**：传统三维氧化物（如 $BaTiO_3$）受限于退极化场，厚度降至几纳米时铁电性消失。二维滑动铁电（如 [[../entities/h-BN|h-BN]]、[[../entities/TMDs|3R-MoS₂]]）依靠层间滑移产生极化，可在单/双层厚度下保持稳健的极化，极大地减小了隧穿电阻并提高了集成度。
   - **界面优化**：范德华层状材料表面无悬挂键，减少了界面电荷钉扎，提高了器件的可靠性与循环稳定性。

3. **铁电金属与 MXene 基隧道结**：
   - **$\alpha$-MXenes**：如 $Nb_2CF_2$、$Mo_2CO_2$ 等被预测为具有铁电性的金属（Ferroelectric Metals）。这类材料在保持金属性的同时具有极化，可用作 FTJ 的电极或势垒层，提供独特的电荷屏蔽特性。
   - **极化翻转路径**：如图所示，$\alpha$-MXene 的极化反转通过金属原子的位移实现，具有较低的翻转势垒。

   ![Polarization reversal in alpha-MXene](../../raw/figures/zahraCriticalAnalysisFerroelectric2025/fig_5_TZK88HMA.png)
   *图 1: $\alpha$-MXene 中极化从向下到向上的反转过程及计算势垒（[[../../raw/note/zahraCriticalAnalysisFerroelectric2025|Zahra et al., 2025]]）*

## 调控手段与动力学

1. **机械弯曲切换 (Mechanical Bending)**：
   - 最新模拟研究表明，利用**机械弯曲**诱导的层间滑移可实现极化翻转。这种弯曲会产生不可逆的扭结（Kink），包含铁电拓扑畴壁（如 Néel 型或 Ising 型），为“滑动电子学 (Slidetronics)”提供了电场之外的机械调控维度。
   
   ![Mechanical bending induced polarization switching](../../raw/figures/heSwitchingTwodimensionalSliding2025/fig_3_H6HN8MAN.png)
   *图 2: 弯曲诱导的 31° 和 57° 扭结及其对应的畴壁结构（[[../../raw/note/heSwitchingTwodimensionalSliding2025|He et al., 2025]]）*

2. **压电力显微表征 (PFM)**：
   - 实验上常通过 PFM 的相位-偏压迟滞回线和振幅-偏压蝶形曲线来证实超薄层中的铁电切换行为。

   ![PFM characterization of ferroelectric composites](../../raw/figures/zahraCriticalAnalysisFerroelectric2025/fig_17_BSC7ZVIJ.png)
   *图 3: BT/f-Ti3C2Tx 复合材料的 PFM 相位回线与振幅曲线（[[../../raw/note/zahraCriticalAnalysisFerroelectric2025|Zahra et al., 2025]]）*

## 核心应用领域

1. **非挥发性存储器 (NVMT)**：
   - 具备非破坏性读取、超快读写速度（纳秒级）和超低功耗特性（[[../../raw/note/xueEmergingNonvolatileMemories2011|Xue et al., 2011]]）。
2. **神经形态计算 (Neuromorphic Computing)**：
   - 通过外加脉冲精确调控隧道区域内畴壁的渐进式移动，使 FTJ 展现出多态连续可调的电导。这种行为能够模拟生物突触的长期增强（LTP）与长期抑制（LTD）功能。
3. **多功能耦合与 2D 多铁性**：
   - **磁电耦合**：在 2D 多铁异质结（如 $Cr_2Ge_2Te_6 / In_2Se_3$）中，铁电极化可调控磁序，实现铁电控制的隧道磁阻（TMR）。
   - **光电/热电耦合**：结合 MXene 的优异光热性能，可开发出基于铁电-焦耳-光电耦合效应的新型传感器。

![2D Multiferroics Landscape](../../raw/figures/RecentAdvancesGrowth2025/fig_15_TMK8S5HG.png)
*图 4: 二维多铁性材料的耦合效应及应用概览（[[../../raw/note/RecentAdvancesGrowth2025|Recent Advances in Growth, 2025]]）*

## 本库相关论文

- [[../../raw/note/sunSlidingFerroelectricityTwodimensional2025|Sliding ferroelectricity in 2D materials and device applications (Sun et al., 2025)]]：系统总结了滑动铁电机制及其在场效应晶体管和隧道结中的应用。
- [[../../raw/note/heSwitchingTwodimensionalSliding2025|Switching Two-Dimensional Sliding Ferroelectrics by Mechanical Bending (He et al., 2025)]]：提出了通过机械应力/弯曲切换滑动铁电状态的新机制。
- [[../../raw/note/zahraCriticalAnalysisFerroelectric2025|A critical analysis of ferroelectric and ferromagnetic properties in two-dimensional MXene (Zahra et al., 2025)]]：深入分析了 MXene 体系的铁电金属性及多功能应用。
- [[../../raw/note/FerroelectricityMultiferroicityAtomic2023|Ferroelectricity and multiferroicity down to the atomic thickness (Nature Nanotechnology Editorial, 2023)]]：综述了钙钛矿、氧化铪及范德华堆叠在原子级厚度下的进展。
- [[../../raw/note/yuFerroelectricControlMagnetism2026|Ferroelectric Control of Magnetism and Giant Magnetoresistance (Yu et al., 2026)]]：探讨了铁电对隧道磁电性能的调控。

## 关联概念与实体

- [[sliding-ferroelectricity|滑动/堆叠铁电性 Sliding Ferroelectricity]]
- [[polarization-switching|极化翻转动力学 Polarization Switching]]
- [[2D-materials|二维范德华材料 2D Materials]]
- [[../entities/h-BN|氮化硼 h-BN]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
- [[../entities/domain-wall|铁电畴壁 Domain Wall]]
- [[../entities/MXenes|MXenes]]
