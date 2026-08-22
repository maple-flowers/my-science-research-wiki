---
tags: [entity, material, sliding-ferroelectricity, spin-orbit-coupling, polarization-switching, 2d-materials, spintronics]
title: 碘化汞 (HgI2) / Mercury Iodide
type: entity
status: mature
formula: HgI2
stoichiometry: 4H
class: [layered-halide, vdW, polar]
properties: [sliding-ferroelectricity, rashba-spin-texture, room-temperature-stability]
related_concepts: [sliding-ferroelectricity, spin-orbit-coupling, polarization-switching, rashba-effect, interfacial-charge-rearrangement]
related_entities: [WTe2, ReS2, GaSe]
papers: [chenStrongSlidingFerroelectricity2024, kaurRecentAdvancesTheoretical2025a, zhangEmergingFrontiersTwodimensional2025, sunSlidingFerroelectricityTwodimensional2025, tangMultiferroicityTwodimensionalVan2025]
updated: 2026-08
---

# 碘化汞 (HgI2) / Mercury Iodide

HgI₂（碘化汞）是一种层状卤化物材料，被理论预测并证实为**室温稳定的强滑动铁电体**。其显著特点是极化强度远高于此前已实现的滑动铁电体（如 WTe₂、MoS₂ 等），且极化源于**层间界面电荷重排**而非阳离子位移。更重要的是，HgI₂ 双层表现出极化方向依赖的 Rashba 自旋纹理，可通过电控自旋进动与检测实现自旋场效应晶体管功能，将"滑移电子学"与"自旋电子学"结合。

## 👵 太奶导读

太奶，HgI₂（碘化汞，一种由汞和碘组成的层状材料）就像一叠**会自己带电的扑克牌**。它最有意思的地方是：电性不是靠搬动牌里面的原子产生的，而是靠上下两张牌之间"错位"时的**电荷挪窝**产生的——上面带正电、下面带负电，这就是极化。往反方向一搓，正负就对调，这就是"滑动铁电"。

它比别人强在哪儿？过去发现的滑动铁电材料（像 WTe₂、MoS₂）产生的电性都很弱，只有一点点；而 HgI₂ 一搓能搓出**很强**的电性，室温下也稳稳当当的。更神奇的是，它还能让电子"自转"的方向受电性控制（这叫 Rashba 自旋纹理），像是给电子装了个可以电动调节的方向盘，可以用来做又省电又能算又能记的自旋芯片。

## 🏗️ 结构概览

HgI₂ 为层状结构，层内原子强键合、层间为范德华相互作用。晶体存在极性（FE，铁电）与非极性（PE，顺电）两种堆垛多型，双层/多层在极性堆垛下呈现稳定的滑动铁电序（[[../papers/kaurRecentAdvancesTheoretical2025a]]）。

![图：HgI2 双层能量双阱与 Rashba 自旋织构](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_12_5DRMFEUA.png)
- **看图要点**：(a) 极性 ±P 与非极性 PE 块体 HgX₂ 晶体结构；(b)(c) 块体与双层的能量双阱及极化曲线；(d) 三至六层 HgI₂ 的面平均屏蔽电荷；(e)(f) 总层间极化与平均层间极化随层数变化；(g) FE-HgI₂ 双层 +P 态在 kx–ky 面 VBM/CBM 的自旋织构。
- **来源**：[[../papers/kaurRecentAdvancesTheoretical2025a]] -> [[../figures/crystal-structures-bulk|体相晶体结构]]

## 🧩 极化机制：层间电荷重排

与"离子位移"主导的传统铁电不同，HgI₂ 的滑动铁电极化起源于**层间界面电荷重排**：

- 不对称堆叠导致层间界面处电荷重新分布，形成垂直层面的净偶极矩。
- 极化强度由 FE 相与 PE 相面平均屏蔽电荷密度之差积分求得（$P=m/d$），而非依赖阳离子位移（[[../papers/chenStrongSlidingFerroelectricity2024]]）。
- 极化强度随层数增加趋于饱和，实验厚纳米片可达约 0.16 μC/cm²，说明极化可检测、可规模化。

## ⚡ Rashba 自旋纹理与自旋电子应用

FE-HgI₂ 双层具有**极化方向依赖的 Rashba 自旋纹理**：

- 自旋劈裂的方向与符号随极化方向（+P/−P）反转，实现电控自旋进动与检测。
- 可据此设计 Datta-Das 型自旋场效应晶体管（自旋 FET，通道长度约 143 nm），实现电控自旋输运。

## 🔬 物理参数表

| 属性 | 数值 | 方法与来源 |
| :--- | :--- | :--- |
| 双层自发极化 $P$ | 0.11 μC/cm² | 屏蔽电荷积分法（[[../papers/chenStrongSlidingFerroelectricity2024]]） |
| 体相自发极化 $P$ | 1.16 μC/cm² | Berry 相位计算（[[../papers/chenStrongSlidingFerroelectricity2024]]） |
| 厚纳米片饱和极化 | ~0.16 μC/cm² | 实验厚纳米片（[[../papers/chenStrongSlidingFerroelectricity2024]]） |
| 双层翻转势垒 | 24.65 meV/f.u. | DFT+NEB（[[../papers/chenStrongSlidingFerroelectricity2024]]） |
| 自旋 FET 通道长度 | 143 nm | Datta-Das 设计（[[../papers/chenStrongSlidingFerroelectricity2024]]） |

> 注：上表为 DFT 计算与实验报道数值，适用对象与条件已在数值中标注，详细来源见 📚 相关论文 节。

## 🧭 近邻体系辨析

- **与 WTe₂ 的区别**：WTe₂ 是半金属（铁电金属），极化来源于低载流子浓度下的不完全屏蔽，翻转能垒约 0.29 eV/f.u.；HgI₂ 是层状卤化物绝缘体，极化来源于层间电荷重排，能垒更低（24.65 meV/f.u.）且带 Rashba 自旋纹理。
- **与 ReS₂ 的区别**：ReS₂ 多层滑动铁电极化在 pC/m 量级（0.07–0.68 pC/m），且为铁弹-铁电耦合体系；HgI₂ 极化在 μC/cm² 量级（约 0.11–0.16 μC/cm²），强度高出数个量级。
- **与 GaSe 的区别**：GaSe 为 III-VI 族层状半导体，滑动铁电极化约 6.19 pC/m；HgI₂ 作为卤化物体系极化更强，且兼具自旋电子学功能。

## 📚 相关论文 (Related Papers)

- [[../papers/chenStrongSlidingFerroelectricity2024]]：发现了 HgI₂ 这一强滑动铁电体系，将已知滑动铁电体的极化强度提升至新水平；揭示了层间电荷重排对极化的主导作用；展示了通过层间滑动同时控制铁电与自旋性质的可能性。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：从理论综述角度梳理了「Recent advances in theoretical investigations of sliding ferroelectricity」，其中图 12 系统给出 HgI₂ 双层的双阱、极化计算与 Rashba 自旋织构。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：从综述角度梳理了「Sliding ferroelectricity in two-dimensional materials and device applications」，将 HgI₂ 列入理论预测的强极化滑动铁电材料谱系。
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]：从综述角度梳理了「二维滑动铁电体的新兴前沿」。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：从综述角度梳理了「二维范德华多铁材料的设计策略」。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/rashba-effect|Rashba 效应]]
- [[../concepts/interfacial-charge-rearrangement|界面电荷重排]]
- [[../concepts/polarization-switching|极化翻转]]
- [[../concepts/spin-texture|自旋纹理]]
- [[../entities/WTe2|WTe2]]
- [[../entities/ReS2|ReS2]]
- [[../entities/GaSe|GaSe]]
