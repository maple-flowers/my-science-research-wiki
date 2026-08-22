---
tags: [entity, material, TMD, 2D, metal, CDW, superconductor]
title: 二硒化钽 (TaSe2) / Tantalum Diselenide
type: entity
status: mature
formula: TaSe2
stoichiometry: 2H
class: [TMD, vdW, metal]
properties: [charge-density-wave, superconductivity, marginal-fermi-liquid]
related_entities: [TaS2, NbSe2, 2h-phase]
papers: [CastroNeto2001charge, Inosov2008fermi, Johannes2008fermi, Koley2020charge, Petkov2020hierarchy, chowdhuryReviewTheoreticalComputational]
updated: 2026-08
---

# 二硒化钽 (TaSe2) / Tantalum Diselenide

二硒化钽 (TaSe2) 是一种极具代表性的二维过渡金属硫族化合物 (TMD)，以其在低温下复杂的**电荷密度波 (CDW)** 序及其与**超导电性**的共存而闻名。它是理解费米面嵌套、电子-声子耦合以及反常金属行为（如边缘费米液体）的核心物理原型材料。

##  Grandma 👵 太奶导读

太奶啊，您就把这 TaSe2 想象成一叠层层叠叠的“导电锡箔纸”。这纸在常温下就是普通的金属，通电很快。但神奇的是，一旦天冷到了极点（低于零下一百五十度），这纸表面就会自发地生出一种“排队波”。电子不再乱跑，而是像阅兵方阵一样，排成一格一格的方块阵型（这就是**电荷密度波**）。

别的材料一旦长了这种波，往往就不导电了，可 TaSe2 却非常调皮，它不但保持着非常好的导电性（金属性），甚至在冷到极致的时候，还能变成一点阻力都没有的**超导体**。而且这材料里电子的脾气很古怪，它们互相撞击的频率和温度是成比例的，这在物理上叫“反常金属”，是全世界科学家都想破解的谜团。

## 🏗️ 结构概览

TaSe2 最稳定的形式是 2H 相。钽 (Ta) 原子位于硒 (Se) 原子构成的三棱柱中心，层间通过弱范德华力堆垛。

![图：TaSe2/NbSe2 家族的 T_cdw 与 T_c 随结构参数 a/c 的演化](../../raw/figures/CastroNeto2001charge/fig_1_VHUZ3FLK.png)
*   **看图要点**：图中展示了 TaSe2 在 TMD 家族中的地位。随着晶格比例 $a/c$ 的变化，CDW 转变温度与超导转变温度呈现明显的反相关关系。TaSe2 处于 CDW 极强而超导极弱（$T_c \approx 0.1\text{ K}$）的临界区域。
*   **来源**：[[../papers/CastroNeto2001charge]] -> [[../figures/crystal-structures-bulk|晶体结构]]

## 🧩 电荷密度波与狄拉克费米子

TaSe2 的 CDW 状态非常独特，它并不是简单的绝缘相，而是一个保持优良金属性的态。

*   **f 波序参量**：Castro Neto 等人提出 TaSe2 的 CDW 具有六重节点的 **f 波对称性**。这意味着在动量空间中，某些特定的点（狄拉克点）上能隙为零。
*   **狄拉克电子 (Dirac Electrons)**：在 CDW 相中，低能激发由无质量的各向异性狄拉克费米子主导。这解释了为何材料进入 CDW 相后电阻率反而下降。
*   **边缘费米液体 (Marginal Fermi Liquid)**：在 CDW 相中，电子通过压电耦合与声子相互作用，导致其散射率与频率呈线性关系，而非传统费米液体的平方关系。

## 🔬 费米面嵌套与电子-声子耦合

关于 TaSe2 CDW 的起源曾有长期争论，目前倾向于电子-声子耦合驱动。

![图：TaSe2 的电子自能虚部随能量变化（ARPES 证据）](../../raw/figures/CastroNeto2001charge/fig_3_Y8PXIM8Z.png)
*   **关键特征**：图中展示了利用角分辨光电子能谱 (ARPES) 测得的电子散射率（自能虚部）。在低能区明显的线性行为是边缘费米液体的直接证据，证实了 CDW 相中狄拉克电子的存在。
*   **来源**：[[../papers/CastroNeto2001charge]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

Inosov 等人的研究显示，TaSe2 确实存在一个非公度的费米面嵌套矢量（位于 $\sim 0.60\ \Gamma\text{M}$），但 CDW 的最终稳定性和转变温度更多取决于动量依赖的电子-声子耦合强度。

## 📚 相关论文 (Related Papers)

- [[../papers/CastroNeto2001charge]]：提出了 TaSe2 中 f 波 CDW 和狄拉克电子的统一理论。
- [[../papers/Inosov2008fermi]]：通过 ARPES 精确测定了 TaSe2 的非公度嵌套矢量。
- [[../papers/Johannes2008fermi]]：解构了费米面嵌套范式，强调了电子-声子耦合的核心地位。
- [[../papers/Koley2020charge]]
- [[../papers/Petkov2020hierarchy]]
- [[../papers/chowdhuryReviewTheoreticalComputational]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波 (CDW)]]
- [[../concepts/dirac-electrons|狄拉克电子]]
- [[../concepts/marginal-fermi-liquid|边缘费米液体]]
- [[../concepts/fermi-surface-nesting|费米面嵌套]]
- [[../entities/NbSe2|二硒化铌 (NbSe2)]]（同族强超导对照）
