---
tags: [concept, ftj, memory, device, tunneling]
category: [D02, Z01]
---

# 铁电隧道结与非挥发存储器 / Ferroelectric Tunnel Junctions (FTJ)

由两层电极中间夹一层超薄铁电势垒层（通常 $< 5\text{ nm}$）构成的金属-铁电-金属（M/FE/M）或二维范德华异质结器件。利用铁电极化方向反转改变势垒高度/形状，从而产生巨大的**隧道开关电阻比 (Giant Electroresistance, GER)**，实现非挥发性信息存储。

## 工作原理与物理机制

1. **势垒调制效应 (Tunnel Barrier Modulation)**：
   - 极化电荷在界面处的不完全屏蔽效应产生静电势降。当极化指向势垒较低的电极时，平均势垒高度降低（低阻态 LRS）；反之则升高（高阻态 HRS）。
2. **二维[[sliding-ferroelectricity|滑动铁电]] FTJ 的优势**：
   - **突破临界厚度**：传统三维氧化物 FTJ 受限于退极化场，厚度降至几纳米时铁电性消失。二维滑动铁电（如 [[../entities/h-BN|h-BN]]、[[../entities/TMDs|3R-MoS₂]]）依靠层间滑移产生极化，可在单/双层厚度下保持极化，极大地减小了隧穿电阻。
   - **界面优化**：范德华层状材料表面无悬挂键，减少了界面态引起的电荷钉扎，提高了器件的可靠性与开关比。
3. **新型开关手段**：
   - 除了电场驱动外，最新研究表明利用**机械弯曲**诱导的层间滑移（扭结形成）可实现极化翻转，为“滑动电子学 (Slidetronics)”提供了新的调控维度（[[../../raw/note/heSwitchingTwodimensionalSliding2025|He et al., 2025]]）。

## 核心应用领域

1. **非挥发性存储器 (NVMT)**：
   - 具备非破坏性读取、超快读写速度（纳秒级）和超低功耗特性（[[../../raw/note/xueEmergingNonvolatileMemories2011|Xue et al., 2011]]）。
2. **神经形态计算 (Neuromorphic Computing)**：
   - 通过外加脉冲精确调控隧道区域内畴壁的渐进式移动，使 FTJ 展现出多态连续可调的电导。这种行为能够模拟生物突触的长期增强（LTP）与长期抑制（LTD）功能，是类脑硬件的核心组件。
3. **多功能耦合器件**：
   - 结合多铁性材料，可实现铁电控制隧道磁阻（TMR）或巨磁阻（GMR）效应，用于自旋电子学存储（[[../../raw/note/yuFerroelectricControlMagnetism2026|Yu et al., 2026]]）。

## 本库相关论文

- [[../../raw/note/sunSlidingFerroelectricityTwodimensional2025|Sliding ferroelectricity in 2D materials and device applications (Sun et al., 2025)]]：系统总结了滑动铁电机制及其在场效应晶体管和隧道结中的应用。
- [[../../raw/note/heSwitchingTwodimensionalSliding2025|Switching Two-Dimensional Sliding Ferroelectrics by Mechanical Bending (He et al., 2025)]]：提出了通过机械应力/弯曲切换滑动铁电状态的新机制。
- [[../../raw/note/tahirFerroelectricityNonvolatileMemristor2025|Ferroelectricity and Nonvolatile Memristor Applications (Tahir et al., 2025)]]：探讨了基于自由立式薄膜的铁电忆阻器应用。
- [[../../raw/note/yuFerroelectricControlMagnetism2026|Ferroelectric Control of Magnetism and Giant Magnetoresistance (Yu et al., 2026)]]：铁电对隧道磁电性能的调控。
- [[../../raw/note/guoAdvancesTwodimensionalFerroelectric2025|Advances in Two-Dimensional Ferroelectric Materials (Guo et al., 2025)]]：二维铁电材料的最新进展综述。

## 关联概念与实体

- [[sliding-ferroelectricity|滑动/堆叠铁电性 Sliding Ferroelectricity]]
- [[polarization-switching|极化翻转动力学 Polarization Switching]]
- [[2D-materials|二维范德华材料 2D Materials]]
- [[../entities/h-BN|氮化硼 h-BN]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
- [[../entities/domain-wall|铁电畴壁 Domain Wall]]
