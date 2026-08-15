---
tags: [entity, material, TMD, 2D, semiconductor]
title: 二硫化钼 (MoS2) / Molybdenum Disulfide
type: entity
status: mature
formula: MoS2
stoichiometry: 2H
class: [TMD, vdW, semiconductor]
properties: [direct-bandgap, valley-polarization, photoluminescence]
related_entities: [WS2, MoTe2, 2h-phase, 1t-phase]
updated: 2026-08
papers: [liPhaseTransitions2D2021, RecentAdvancesGrowth2025, FerroelectricityMultiferroicityAtomic2023, Li2013bonding, Owji20212d, chenHafniumBasedFerroelectricPostMoore2026, guanRecentProgressTwoDimensional2020, kaurRecentAdvancesTheoretical2025a, liuSpintronicsTwoDimensionalMaterials2020b, sunSlidingFerroelectricityTwodimensional2025, yangStrainEngineeringTwodimensional2021, wuElectrostaticGatingIntercalation2022]
---

# 二硫化钼 (MoS2) / Molybdenum Disulfide
二硫化钼 (MoS2) 是二维半导体领域的明星材料。它在块体状态下是间接带隙半导体，但当减薄至单层时，由于量子限制效应转变为直接带隙半导体，展现出极强的光致发光 (PL) 效应和独特的能谷电子学性质。
## 奶奶导读
太奶啊，这 MoS2 就是二维材料里的“变形金刚”和“发光纸片”。它本来像是一叠厚厚的黑色复写纸，虽然能导电但不太亮眼。可如果您把它撕到只剩一层薄薄的原子层，它就会突然“变身”，变得非常爱发光（光致发光）。而且它还有两个像“山谷”一样的电子能量坑，我们可以用特定的光让电子只进其中的一个坑（能谷极化），就像给电子发了不同的通行证。
## 🏗️ 结构概览
MoS2 的稳态结构为 2H 相，Mo 原子位于六角排列的 S 原子中心，呈三棱柱配位。
![图：MoS2 的多晶型结构 (2H vs 1T)](../../raw/figures/liPhaseTransitions2D2021/fig_5_RCAID2CF.png)
*   **看图要点**：图中对比了 MoS2 的 2H 相（三棱柱配位，半导体）和 1T 相（八面体配位，金属）。2H 相是自然界最稳定的形态。
*   **来源**：[[../papers/liPhaseTransitions2D2021]] -> [[../figures/crystal-structures-bulk|晶体结构]]
## 🧩 直接带隙与光电性能
MoS2 的最显著特征是随厚度减薄发生的带隙转变。
*   **带隙转变**：从块体的 $\sim 1.2\text{ eV}$（间接）转变为单层的 $\sim 1.8\text{ eV}$（直接）。
*   **能谷电子学**：在单层 MoS2 中，由于空间反演对称性破缺和强自旋-轨道耦合，$K$ 和 $K'$ 能谷的电子具有不同的角动量特性，可通过圆偏振光选择性激发。
*   **相变工程**：通过锂离子插层或电场调控，MoS2 可以从 2H 相转变为金属性的 1T 或 1T' 相，用于开发高性能忆阻器或催化电极。
## 🔬 物理参数表
| 属性 | 数值 (单层) |
| :--- | :--- |
| 带隙 (Bandgap) | $\sim 1.8\text{ eV}$ (直接) |
| 载流子迁移率 | $200\text{--}500\text{ cm}^2\text{V}^{-1}\text{s}^{-1}$ |
| 激子结合能 | $\sim 0.5\text{ eV}$ |
## 🔬 实验表征与调控

**静电门控与插层调控**：通过静电门控（electrostatic gating）与离子插层（intercalation）可在 MoS₂ 等二维材料中连续调控载流子浓度、诱导相变并改变电子结构，是超越传统掺杂的灵活调控手段 [[../papers/wuElectrostaticGatingIntercalation2022]]。

## 📚 相关论文 (Related Papers)
- [[../papers/liPhaseTransitions2D2021]]：详细讨论了 MoS2 的相变与调控机制。
- [[../papers/RecentAdvancesGrowth2025]]：综述了 TMD 晶圆级生长的最新进展。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：综述了原子级厚度下的铁电与多铁性。
- [[../papers/Li2013bonding]]：研究了单层 TMD 的成键电荷密度与极限强度。
- [[../papers/Owji20212d]]：将二维材料涂覆于刻蚀光纤上制成湿度传感器。
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：综述了基于铪的铁电后摩尔电子学器件与神经形态系统。
- [[../papers/guanRecentProgressTwoDimensional2020]]：综述了二维铁电材料的最新进展。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：综述了层状与范德华二维材料中滑动铁电性的理论研究进展。
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：综述了二维材料中的自旋电子学。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：综述了二维材料中的滑动铁电性及其器件应用。
- [[../papers/yangStrainEngineeringTwodimensional2021]]：综述了二维材料的应变工程方法、性质与应用。
- [[../papers/wuElectrostaticGatingIntercalation2022]]：综述了二维材料中的静电门控与插层调控。

## 🔗 关联概念与实体 (Related Concepts & Entities)
- [[../concepts/valley-polarization|能谷极化]]
- [[../concepts/photoluminescence|光致发光]]
- [[../entities/WS2|二硫化钨 (WS2)]]
- [[../entities/2h-phase|2H 相]]
- [[../entities/1t-phase|1T 相]]

## 🏷️ 专业名词别名

- `molybdenum-disulfide`（entities）
