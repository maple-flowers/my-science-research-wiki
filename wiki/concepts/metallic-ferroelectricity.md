---
tags: [concept, ferroelectric, metal]
title: 金属铁电性 / Metallic Ferroelectricity
type: concept
status: mature
domain: [ferroelectricity, polar-metals, 2d-materials]
mechanism: "自由载流子存在时仍能保留可翻转极化：极性自由度与导电通道在实空间或轨道上分离，使载流子屏蔽不足以消灭极化双稳态"
related_concepts: [ferroelectric-metal, polar-metal, hyper-ferroelectric-metal, sliding-ferroelectricity, ferroelectricity]
related_entities: [WTe2]
papers: [zhaoRealization2DMultiferroic2024, feiFerroelectricSwitchingTwodimensional2018a, wuSlidingFerroelectricity2D2021a, bhowalPolarMetalsPrinciples2023b, wangTwodimensionalFerroelectricMetal2025]
updated: 2026-08
---



# 金属铁电性 / Metallic Ferroelectricity

金属铁电性（metallic ferroelectricity）指**在金属（导电）材料中实现铁电有序**这一物理现象。传统观念认为金属中的自由载流子会完全屏蔽内建极化场，使铁电态无法存在；金属铁电性通过让"屏蔽不彻底"的机制（电荷实空间分离、薄层穿透屏蔽、低载流子密度）打破这一限制。它是"极性金属—铁电金属"概念中最具功能性的环节：不仅导电，而且极化可被电场开关。

## 👵 太奶导读

太奶，金属里电子多得能"淹没"任何电场，所以过去大家都说金属不可能有铁电（记住电方向的"记性"）。金属铁电性就是科学家证明"这事儿能行"的本领：有的材料把"负责导电的电子"和"负责记电的电荷"分成两个地方住（比如一层管子导电、夹层小圆球记电），电子再多也淹不到记电的地方。这样既导电又能记电，做存储、做传感器都更省事。

## 🧩 核心内容与机制 (Core Content)

- **核心悖论与出路**：金属中载流子屏蔽退极化场 → 铁电被抹平。出路有三：①极化电荷与传导电子实空间分离；②二维薄层中电场穿透屏蔽层；③低载流子密度体系（掺杂铁电体）保持极性（[[../papers/bhowalPolarMetalsPrinciples2023b]]）。
- **二维插层设计（zhao2024）**：在 MX₂ 层间插入 A 原子（A=Cu, Ag, Au, Pb, Bi, Sb 等），形成 AM₂X₄ 结构。传导电子主要分布在 MX₂ 层，极化电荷局域于插层 A 原子周围，二者空间分离使传导电子无法完全屏蔽垂直极化；系统筛选出 16 种非磁金属铁电体，Pout 在 0.43–9.61 pC/m，全部大于 WTe₂ 双层的 0.42 pC/m（[[../papers/zhaoRealization2DMultiferroic2024]]）。
- **T-PdZr₂Se₄ 案例**：三角相插层化合物，Pout=3.10 pC/m，兼具金属性（费米面在 Zr-Se 轨道）与铁电极化；可同时承载铁电-铁弹-多铁耦合。
- **实验里程碑**：双层 WTe₂ 首次实验实现"金属铁电翻转"——载流子密度跨过 ~2×10¹² cm⁻² 进入金属态后铁电回滞仍保留（fei2018）。
- **应用价值**：金属铁电体的极化态可通过电导非破坏性读出，规避了绝缘铁电的"读破"难题，是神经形态器件、非易失存储与铁电拓扑的重要载体。

![图：插层型金属铁电体 T-PdZr₂Se₄ 的结构与极化机理](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_2_7QNUMABJ.png)
- **看图要点**：插层 A 原子（红/粉）与 MX₂ 层（绿/蓝）的空间排布；极化由插层原子位移主导，传导电子分布在 MX₂ 层。
- **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

## 🔬 物理参数表

| 属性 | 数值 | 方法与来源 |
| :--- | :--- | :--- |
| 16 种非磁金属铁电体 Pout 范围 | 0.43–9.61 pC/m | 高通量 DFT（[[../papers/zhaoRealization2DMultiferroic2024]]） |
| T-PdZr₂Se₄ 面外极化 Pout | 3.10 pC/m | 偶极修正 DFT（[[../papers/zhaoRealization2DMultiferroic2024]]） |
| WTe₂ 双层 Pout（对比基准） | 0.42 pC/m | DFT/实验（[[../papers/zhaoRealization2DMultiferroic2024]]） |
| WTe₂ 金属态回滞保持阈值 n_c | ~2×10¹² cm⁻² | 双栅实验（[[../papers/feiFerroelectricSwitchingTwodimensional2018a]]） |
| 二维铁电金属 CuCrX₂ 载流子 | 金属/半金属（铜/铬 d 带） | DFT（[[../papers/wangTwodimensionalFerroelectricMetal2025]]） |

## 🧭 近邻概念辨析

- **与铁电金属（ferroelectric-metal）**：二者几乎同义——metallic ferroelectricity 强调"现象/机制"，ferroelectric metal 强调"材料类别"；本库中 ferroelectric-metal 指代实现金属铁电的具体材料与工程，metallic-ferroelectricity 聚焦机制与可行性论证。
- **与极性金属（polar-metal）**：极性金属只要求极性+金属，极化不一定可翻转；金属铁电性则**必然要求极化可翻转**。
- **与超铁电金属（hyper-ferroelectric-metal）**：超铁电金属走"超铁电体掺杂"路线，靠小 Born 有效电荷/弱 LO-TO 分裂抵抗屏蔽；金属铁电性不预设这一机制，涵盖更广（滑动、插层等）。

## 📚 相关论文 (Related Papers)

- [[../papers/zhaoRealization2DMultiferroic2024]]：插层策略实现二维金属铁电多铁，提出 16 种候选。
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]：双层 WTe₂ 金属铁电翻转实验。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：滑动铁电综述，讨论金属铁电与非线性霍尔。
- [[../papers/bhowalPolarMetalsPrinciples2023b]]：极性金属理论综述，覆盖屏蔽悖论机制。
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]：二维铁电金属 CuCrX₂ 电催化应用。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectric-metal|铁电金属]]
- [[../concepts/polar-metal|极性金属]]
- [[../concepts/hyper-ferroelectric-metal|超铁电金属]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../entities/WTe2|WTe2]]
