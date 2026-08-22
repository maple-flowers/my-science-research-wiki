---
tags: [entity, material, sliding-ferroelectricity, ferroelasticity, multiferroicity, 2d-materials]
title: 二硫化铼 (ReS2) / Rhenium Disulfide
type: entity
status: mature
formula: ReS2
stoichiometry: 1T'
class: [TMD, layered, vdW]
properties: [sliding-ferroelectricity, ferroelasticity, room-temperature-multiferroicity]
related_concepts: [sliding-ferroelectricity, ferroelasticity, polarization-switching, interlayer-polarization-coupling]
related_entities: [WTe2, SnS]
papers: [kaurRecentAdvancesTheoretical2025a, sunSlidingFerroelectricityTwodimensional2025, tangMultiferroicityTwodimensionalVan2025, guanRecentProgressTwoDimensional2020]
updated: 2026-08
---

# 二硫化铼 (ReS2) / Rhenium Disulfide

ReS₂（二硫化铼）是一种过渡金属硫族化合物（TMD），以**扭曲 1T（1T′）结构**稳定存在。其独特的 Re 原子菱形链构型使其成为典型的二维铁弹体，并可通过多层堆垛的层间滑移实现滑动铁电性。ReS₂ 多层体系的滑动铁电极化随层数增加而增强，且实验上单层 ReS₂ 还表现出室温铁电-铁磁共存，是研究"弹中诱电"多铁策略与多层极化耦合的重要材料平台。

## 👵 太奶导读

太奶，ReS₂（二硫化铼，铼和硫组成的层状材料）就像一叠**斜着铺的瓦片**。别的层状材料原子都是整整齐齐排成棋盘格，而 ReS₂ 里面的铼原子是**歪歪扭扭排成一条条小斜链**的，就像棋盘里被踩歪了一行。正因为这种歪斜的排布，它有上下两个方向都行得通的"歪法"，这就是"铁弹性"（材料可以像弹簧一样在两种歪斜方向之间切换）。

更有意思的是，把两层 ReS₂ 叠起来、互相一搓（层间滑动），也会产生上面正电、下面负电的"滑动铁电"。而且**叠的层数越多，电性越强**——从两层到七层，极化涨了将近十倍。它还特别争气，单层在室温下就能同时带电又带磁，是少见的"一材两用"。

## 🏗️ 结构概览

ReS₂ 采用**扭曲 1T（1T′）结构**：Re 原子偏离八面体配位位置，形成沿晶格方向延伸的二聚化菱形链（Re 链），空间群为三斜的 $P\bar{1}$。从理想 T 相（$P\bar{3}m1$）到 T′ 相（$P\bar{1}$）的结构相变产生**两个等效取向的铁弹畴**，这是其铁弹性的结构基础（[[../papers/tangMultiferroicityTwodimensionalVan2025]]）。

![图：ReS2 多层滑动铁电 A/A' 双稳态](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_10_739TUGAA.png)
- **看图要点**：(a) ReSe₂ 单层；(b) ReS₂ 双层铁电双稳态 A、A′ 与非极性中间态 B；(c) 以滑动距离 $(l_a,l_b)$ 为坐标的能量等高线；(d) A↔A′ 的 NEB 能垒；(e) 差分电荷密度；(f)(g) 三层/四层翻转示意；(h) 极化与能垒随层数的变化。
- **来源**：[[../papers/kaurRecentAdvancesTheoretical2025a]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

## 🧩 滑动铁电机制

ReS₂ 多层体系的滑动铁电源于**层间相对滑动**驱动的电荷转移：

- 双层存在 A/A′ 两个极性双稳态与非极性中间态 B，通过层间滑移路径实现极化翻转。
- Berry 相计算给出双层极化约 0.07 pC/m、翻转势垒约 17.1 meV；顶→底层电荷转移仅 0.0003 e 即可产生面外极化，说明其极化机制高度敏感于层间堆垛细节。
- 三层/四层的翻转通过特定层间滑移（约 (1 Å, 3.6 Å)）实现，极化随层数累积：层数由 2 增至 7，极化升至 0.07–0.68 pC/m，能垒由 17 meV 升至 100 meV（[[../papers/kaurRecentAdvancesTheoretical2025a]]）。

## 🧭 多铁与实验表征

- **室温多铁性**：实验报道单层 ReS₂ 在室温同时具备铁电与铁磁序，极化约 0.85 μC/cm²（[[../papers/tangMultiferroicityTwodimensionalVan2025]]）。
- **铁弹-铁电耦合**：作为"弹中诱电"策略的代表，ReS₂/ReSe₂ 通过 T→T′ 相变产生铁弹畴，堆垛/相变可进一步诱导铁电序。
- **滑动铁电实验谱系**：ReS₂ 亦被列入实验报道的二维滑动铁电材料谱系（[[../papers/sunSlidingFerroelectricityTwodimensional2025]]）。

## 🔬 物理参数表

| 属性 | 数值 | 方法与来源 |
| :--- | :--- | :--- |
| 双层滑动铁电极化 | 0.07 pC/m | Berry 相位（[[../papers/kaurRecentAdvancesTheoretical2025a]]） |
| 双层翻转势垒 | 17.1 meV | DFT+NEB（[[../papers/kaurRecentAdvancesTheoretical2025a]]） |
| 多层极化（2→7 层） | 0.07 → 0.68 pC/m | Berry 相位（[[../papers/kaurRecentAdvancesTheoretical2025a]]） |
| 多层翻转势垒（2→7 层） | 17 → 100 meV | DFT+NEB（[[../papers/kaurRecentAdvancesTheoretical2025a]]） |
| 翻转电荷转移 | 0.0003 e | 差分电荷密度（[[../papers/kaurRecentAdvancesTheoretical2025a]]） |
| 单层室温极化 | 0.85 μC/cm² | 实验（[[../papers/tangMultiferroicityTwodimensionalVan2025]]） |

> 注：上表为 DFT 计算与实验报道数值，适用对象与条件已在数值中标注，详细来源见 📚 相关论文 节。

## 🧭 近邻体系辨析

- **与 ReSe₂ 的区别**：ReSe₂ 与 ReS₂ 同构（同为 1T′ 结构、铁弹体），但 ReS₂ 被更系统地研究了滑动铁电极化随层数的演化；两者可作为铁弹-铁电耦合的姊妹体系对照。
- **与 WTe₂ 的区别**：WTe₂ 是半金属（Td 相），滑动铁电极化来源于低载流子下的不完全屏蔽；ReS₂ 是半导体，极化来源于层间电荷转移，且具有铁弹序与室温多铁性。
- **与 SnS/SnSe 的区别**：SnS/SnSe 为 IV-VI 族磷烯同构褶皱结构，面内铁电与铁弹互锁（90° 翻转）；ReS₂ 为三斜 T′ 结构，铁弹畴来自 T→T′ 相变，滑动铁电为面外极化。

## 📚 相关论文 (Related Papers)

- [[../papers/kaurRecentAdvancesTheoretical2025a]]：从理论综述角度梳理了「Recent advances in theoretical investigations of sliding ferroelectricity」，其图 10 系统给出 1T′-ReS₂ 多层的双稳态、电荷转移与极化/能垒随层数演化。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：从综述角度梳理了「Sliding ferroelectricity in two-dimensional materials and device applications」，将 ReS₂ 列入实验报道的滑动铁电材料谱系。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：从综述角度梳理了「二维范德华多铁材料的设计策略」，以 ReS₂/ReSe₂ 为例阐述"弹中诱电"策略并给出单层室温 FE+FM 的定量数据。
- [[../papers/guanRecentProgressTwoDimensional2020]]：从综述角度梳理了「Recent Progress in Two‐Dimensional Ferroelectric Materials」。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/ferroelasticity|铁弹性]]
- [[../concepts/interlayer-polarization-coupling|层间极化耦合]]
- [[../concepts/polarization-switching|极化翻转]]
- ReSe₂（姊妹铁弹体系，未建页）
- [[../entities/WTe2|WTe2]]
- [[../entities/SnS|SnS]]
