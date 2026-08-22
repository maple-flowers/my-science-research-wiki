---
tags: [concept, physics, surface-science]
title: 功函数 (Work Function)
type: concept
status: mature
domain: [solid-state-physics, surface-science, microelectronics]
mechanism: 将一个电子从材料内部移到表面外真空能级处所需的最小能量
related_concepts: [schottky-barrier, band-alignment, band-offset, electrostatic-gating]
papers: [chenHafniumBasedFerroelectricPostMoore2026, duUltrasensitiveOptoelectronicBiosensor2025, wangTwodimensionalFerroelectricMetal2025, wangTunableD0Topological2025b, wongEvidenceMetallic1T, wuNonvolatileSwitchableHalfmetallicity2024, yanagizawaSwitchingChargedensityWave2023]
updated: 2026-08
---

# 功函数 / Work Function ($\Phi$)

功函数 ($\Phi$) 是凝聚态物理中的一个基本表面参数。它定义为将一个电子从固体（通常是金属或半导体）的费米能级移除并放置到紧邻其表面外的真空中所需的最小能量（即真空能级 $E_{vac}$ 与费米能级 $E_F$ 之差）。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“功函数”其实就是电子想从家里跑出来的“出路费”。想象每个材料（比如金、银或石墨烯）都是一座大房子，电子就住在里头。
> 
> 有的房子围墙矮（功函数小），电子轻轻松松翻个墙就能跑到外面去；有的房子围墙修得特别高（功函数大），电子得费好大劲、带够了干粮（能量）才能翻出去。当两座房子连在一起时（异质结），墙高墙矮一比，电子就会从好跑的那边往难跑的那边溜。科学家们就是通过挑不一样的房子和修不一样的墙，来决定电流往哪儿走。

## 🏗️ 结构概览

功函数是决定异质结能带对齐 (Band Alignment) 的最关键因素，直接决定了接触是欧姆型还是肖特基型。

![图：不同二维材料与金属接触时的能带与功函数匹配](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_1_BXNBIMFM.png)
*   **看图要点**：图中展示了石墨烯与金电极的接触。金的功函数与石墨烯的费米能级之间的差异，决定了电荷转移的方向以及接触面电位降的分布。
*   **来源**：[[../papers/duUltrasensitiveOptoelectronicBiosensor2025]] -> [[../figures/electronic-devices-sensors|传感器与探测器]]

## 🧩 物理意义与影响因素

### 定义公式
$$\Phi = E_{vac} - E_F$$
其中 $E_{vac}$ 是真空能级，$E_F$ 是费米能级。

### 影响因素
1.  **材料本征性质**：不同原子种类的电负性不同，功函数各异。
2.  **晶面取向**：不同晶面的原子排布密度和表面偶极子不同。
3.  **表面掺杂与修饰**：例如，吸附碱金属原子可以显著降低功函数。
4.  **静电栅控**：对于二维材料，外部栅极电压可以显著移动费米能级，从而动态改变其功函数（有效功函数）。

### 在电子器件中的作用
*   **肖特基势垒**：由金属功函数与半导体电子亲和能之差决定。
*   **光电发射**：光子能量必须大于功函数才能激发出电子。
*   **逻辑器件**：金属栅极功函数的选择直接影响 CMOS 的阈值电压。

## 📚 相关论文 (Related Papers)

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：讨论了铁电极化产生的表面场如何等效改变有效功函数，实现对肖特基二极管的调控。
- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]：涉及金属纳米颗粒与二维材料界面处的电子逸出功平衡。
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]
- [[../papers/wangTunableD0Topological2025b]]
- [[../papers/wongEvidenceMetallic1T]]
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]
- [[../papers/yanagizawaSwitchingChargedensityWave2023]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/schottky-barrier|肖特基势垒]]
- [[../concepts/band-alignment|能带对齐]]
- [[../concepts/electrostatic-gating|静电栅控]]
- [[../entities/gold-nanodisks|金纳米盘]]
- [[../entities/graphene|石墨烯]]
