---
tags: [concept, multiferroics, magnetism, spin-orbit-coupling, mechanism]
category: [D02]
title: Dzyaloshinskii–Moriya 相互作用 / DM 相互作用 (DMI)
type: concept
status: mature
domain: magnetism
mechanism: 破缺空间反演时由自旋-轨道耦合产生的反对称交换 D·(S_i×S_j)，使自旋倾向倾斜/非共线，导致弱铁磁、螺旋磁序与斯格明子
related_concepts: [inverse-dzyaloshinskii-moriya, spin-spiral, weak-ferromagnetism, skyrmion, electromagnon, multiferroicity, magnetoelectric-coupling, spin-texture, exchange-striction]
aliases: ["Dzyaloshinskii-Moriya interaction", "DMI", "DM相互作用", "DM 相互作用", "Dzyaloshinsky-Moriya"]
key_quantities:
  hamiltonian: "H_DM = Σ D_ij·(S_i×S_j)，方向由 Moriya 规则决定，大小 ∝ SOC×Δg/g"
  effect: "在反铁磁背景上叠加小的倾斜角 canting ∼ D/J，产生弱铁磁净磁矩；稳定螺旋/摆线与斯格明子"
  examples: "α-Fe2O3（弱铁磁）、BiFeO3（长周期摆线）、CrI3/界面 DMI 斯格明子"
papers: [deSousa2008electrical, wangTunableD0Topological2025b, zhangNonvolatileControlTopological2025, Goswami2011multiferroic, rameshMultiferroicsProgressProspects2007, zhaoRealization2DMultiferroic2024, tanRevealingEmergentMagnetic2024, tangMultiferroicityTwodimensionalVan2025]
updated: 2026-08
---

# Dzyaloshinskii–Moriya 相互作用 / DM 相互作用 (DMI)

**Dzyaloshinskii–Moriya 相互作用（DMI）** 是破缺空间反演对称性的体系中，由自旋-轨道耦合（SOC）产生的一种**反对称交换作用**，形式为

$$H_{DM}=\sum_{\langle ij\rangle}\mathbf{D}_{ij}\cdot(\mathbf{S}_i\times\mathbf{S}_j)$$

其中 $\mathbf{D}_{ij}$ 为 DM 矢量，方向由晶体对称性（Moriya 五条规则）决定，大小正比于自旋-轨道耦合强度与轨道混合 $D\sim(\Delta g/g)\,J$。与偏好自旋平行/反平行的海森堡交换 $J\,\mathbf{S}_i\cdot\mathbf{S}_j$ 不同，DMI 偏好相邻自旋**互相倾斜一个角度**（叉乘最大），从而在反铁磁体中造成自旋涡转、弱铁磁性，并稳定螺旋磁序、磁斯格明子等拓扑磁结构 [[../papers/deSousa2008electrical]]。

## 👵 太奶导读

太奶，磁铁里相邻小磁针之间那股"非要头对头或尾对尾对齐"的劲儿叫交换作用。可要是原子摆得左右不对称（破了反演对称），再加上相对论那点"自旋-轨道耦合"，就会冒出另一股偏心的劲儿：它不要磁针完全对齐，偏要让它俩**斜着叉开一点点**。这股斜劲儿就是 **DM 相互作用**。

这一斜不要紧，本来反铁磁是两两对消、外头不显磁性的，现在每对都朝同一个方向歪一点，就攒出一个微弱的净磁矩来，叫"弱铁磁"。要是这斜劲儿在晶格上一排排传开，磁针就会边走边转，拧成一根"螺旋/摆线"——像 BiFeO₃ 里周期几百埃的自旋摆线。更妙的是，斜劲儿和别的力一较劲，能把磁针拧成一个个小漩涡，那就是斯格明子，可以用电场或电流搬动，是做超低功耗存储器的好苗子。DM 还有一个"逆"版本（见 [[inverse-dzyaloshinskii-moriya|逆 DM/自旋流模型]]）：那里是自旋先斜着排，反过来挤出电方向；而本页说的"正 DM"是结构先不对称、再把自旋掰斜。一正一逆，正好是多铁里"电"和"磁"牵手的两座桥。

## 🏗️ 结构概览：D 矢量与自旋倾斜

DM 矢量 $\mathbf{D}_{ij}$ 的方向由键的局域对称性决定（Moriya 规则：如镜面垂直键则 D 在镜面内，二次轴沿键则 D 垂直该轴等）。当一个反铁磁键上同时存在 $J>0$（喜反平行）和有限 $D$ 时，能量极小让两自旋偏离严格反平行一个倾角 $\theta\sim D/J$，方向垂直于 $\mathbf{D}$。这个微小、同向累积的倾斜就是弱铁磁矩的来源。DMI 与 $J$ 的比值 $|D/J|$ 决定了非共线磁结构的周期与拓扑相的稳定性——拉伸应变可在保持 $J$ 的同时显著放大 $D$，从而"拧出"斯格明子 [[../papers/wangTunableD0Topological2025b]]。

![图：双轴应变下单层磁体的海森堡交换 J 与 DM 相互作用 d_k（右轴）随应变的变化，内插 |d_k/J| 在拉伸侧快速上升](../../raw/figures/wangTunableD0Topological2025b/fig_4_R8KDU8IB.png)
*   **看图要点**：拉伸应变使 DMI（d_k）显著增大而交换 J 减小，$|D/J|$ 比值大幅提升；正是这一比值控制自旋倾角与螺旋/斯格明子周期，说明 DMI 可由应变等外场定量调控 [[../papers/wangTunableD0Topological2025b]]。
*   **来源**：[[../papers/wangTunableD0Topological2025b]] -> [[../figures/heterostructures-stacking-spintronics-strain|自旋与应变调控]]

## 🧩 物理后果：弱铁磁与螺旋摆线

- **弱铁磁性（canted antiferromagnet）**：在原本反铁磁的体系（如 α-Fe₂O₃、菱铁矿类）中，DMI 使相邻磁矩同向微倾，产生垂直于反铁磁轴的小净磁矩。
- **螺旋/摆线磁序**：当 DMI 在晶格中连贯传播时，它与交换竞争选择有限波矢 $\mathbf{q}\propto D/J$，形成长周期螺旋（BiFeO₃ 中周期约 62 nm 的摆线），并平均掉宏观极化或净磁矩 [[../papers/Goswami2011multiferroic]]。
- **与磁电耦合的关系**：在多铁体中，DMI 决定的自旋进动同时调制极化（见 [[electromagnon|电磁振子]]），是电场控磁、磁场控电的微观桥梁之一 [[../papers/rameshMultiferroicsProgressProspects2007]]。

![图：倾斜多铁（如 BiFeO3 薄膜）中自旋波与极化波的同相/反相耦合——DMI 撑开两模频率隙](../../raw/figures/deSousa2008electrical/fig_1_MFP3ILKR.png)
*   **关键特征**：DMI 偏好的自旋倾斜使磁化与极化的涨落绑在一起进动，形成同相（低频）与反相（高频）两支杂化模，频率隙由 DM 相互作用设定，直观呈现 DMI 在多铁动力学中的作用 [[../papers/deSousa2008electrical]]。
*   **来源**：[[../papers/deSousa2008electrical]] -> [[../figures/vibrational-spectra|振动与磁激发谱]]

## 🌀 拓扑磁结构：斯格明子

在二维铁磁体或铁磁/非磁界面，破缺反演对称产生的**界面 DMI** 把自旋拧成纳米尺度的涡旋——磁斯格明子（Néel 型）与双半子（bimeron）。DMI 提供拓扑保护与手性选择，而交换与各向异性决定其尺寸；外磁场、电流或与铁电层耦合的电场可驱动其成核、移动与擦除，是赛道存储与逻辑器件的物理基础 [[../papers/zhangNonvolatileControlTopological2025]]。

![图：Néel 型斯格明子与双半子在磁场下运动的时间序列快照（0 ns 起）](../../raw/figures/zhangNonvolatileControlTopological2025/fig_6_ZU3NDFU8.png)
*   **关键特征**：DMI 稳定的拓扑自旋纹理在磁场/电流下整体平动而不弥散，其手性由 D 矢量方向固定；与铁电衬底耦合即可用电场非易失地调控这些拓扑磁结构 [[../papers/zhangNonvolatileControlTopological2025]]。
*   **来源**：[[../papers/zhangNonvolatileControlTopological2025]] -> [[../figures/crystal-structures|晶体结构]]

## 📊 DMI 相关作用与现象对照

| 概念 | 表达式/特征 | 角色 |
| :--- | :--- | :--- |
| （正）DM 相互作用 | $\mathbf{D}\cdot(\mathbf{S}_i\times\mathbf{S}_j)$，破反演 + SOC | 掰斜自旋：弱铁磁、螺旋、斯格明子 |
| [[inverse-dzyaloshinskii-moriya\|逆 DM/自旋流]] | $\mathbf{P}\propto\mathbf{e}\times(\mathbf{S}_i\times\mathbf{S}_j)$ | 非共线自旋反过来产生电极化 |
| [[exchange-striction\|交换收缩]] | $J(d)$ 键长依赖，共线 ↑↑↓↓ | 不靠 SOC 的磁感生铁电 |
| [[spin-spiral\|自旋螺旋]] | 波矢 $q\propto D/J$ | DMI 与交换竞争的长波产物 |
| [[skyrmion\|斯格明子]] | 拓扑保护的自旋涡旋 | DMI 稳定的非共线拓扑纹理 |

## 📚 相关论文 (Related Papers)

- [[../papers/deSousa2008electrical]]：倾斜多铁中自旋波-极化波耦合与 DM 频率隙。
- [[../papers/wangTunableD0Topological2025b]]：应变调控 DMI/J 比值与拓扑磁态。
- [[../papers/zhangNonvolatileControlTopological2025]]：CrInTe₃/In₂Se₃ 中非易失电场控制斯格明子/双半子。
- [[../papers/Goswami2011multiferroic]]：BiFeO₃ 纳米晶中自旋螺旋抑制与磁电耦合。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：多铁进展与 DM 在磁电耦合中的角色。
- [[../papers/zhaoRealization2DMultiferroic2024]]、[[../papers/tanRevealingEmergentMagnetic2024]]、[[../papers/tangMultiferroicityTwodimensionalVan2025]]：二维多铁与拓扑磁结构。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[inverse-dzyaloshinskii-moriya|逆 DM/自旋流模型]]、[[spin-spiral|自旋螺旋]]、[[exchange-striction|交换收缩]]、[[weak-ferromagnetism|弱铁磁性]]、[[skyrmion|斯格明子]]、[[spin-texture|自旋织构]]、[[electromagnon|电磁振子]]、[[magnetoelectric-coupling|磁电耦合]]、[[multiferroicity|多铁性]]
- [[../entities/BiFeO3|BiFeO3]]（DM 稳定的长周期摆线多铁）
