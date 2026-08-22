---
tags: [concept, ferroelectric, metal, polar-metal]
title: 铁电金属 / Ferroelectric Metal
type: concept
status: mature
domain: [ferroelectricity, polar-metals, 2d-materials]
mechanism: "金属导电性与可电场翻转的自发极化共存；极化多由层间滑移或极性声子软模提供，导电电子与极性畸变在实空间/轨道空间解耦，屏蔽不完全"
related_concepts: [polar-metal, metallic-ferroelectricity, hyper-ferroelectric-metal, sliding-ferroelectricity, ferroelectricity]
related_entities: [WTe2, LiOsO3]
papers: [feiFerroelectricSwitchingTwodimensional2018a, bhowalPolarMetalsPrinciples2023b, zhaoRealization2DMultiferroic2024, wangTwodimensionalFerroelectricMetal2025, miaoMagneticFerroelectricMetal2024, sharmaRoomtemperatureFerroelectricSemimetal2019]
updated: 2026-08
---



# 铁电金属 / Ferroelectric Metal

铁电金属（ferroelectric metal）指在**金属态**中同时具有**电场可翻转的自发极化**的材料。传统观念认为金属中自由载流子会屏蔽内建极化，使铁电性与金属性"互斥"；铁电金属通过把极化电荷与传导电子在实空间分离、或利用薄层几何让电场穿透屏蔽层，打破这一禁忌。它区别于极性金属（polar-metal，极化不可翻转）与类铁电金属（如 LiOsO₃），是目前凝聚态物理中"金属+铁电"路线的最前沿形态。

## 👵 太奶导读

太奶，以前人们有个"常识"：金属里电子多得像挤满人的菜市场，谁来电都会被立刻"挤散"，所以金属里存不住"电的记性"（铁电）。但科学家硬是找出了例外：有的材料里，负责导电的电子和负责"记电"的电荷分工在不同的地方住，互不干扰；或者材料薄到只有几层原子，电场能穿透进去。这样一来，**既导电又能记电**的材料就出现了（比如 WTe₂）。它可以把"记"和"传"放在同一个材料里，是做新型存储和芯片的好苗子。

## 🧩 核心内容与机制 (Core Content)

- **概念突破**：铁电金属的成立依赖极化不被完全屏蔽。bhowal 2023 综述指出，铁电金属是"极性金属—类铁电金属—铁电金属"三层概念中最严格的一档：既要有非中心对称结构，又要极化**可通过外场翻转**（[[../papers/bhowalPolarMetalsPrinciples2023b]]）。
- **二维代表 WTe₂**：双层/三层 WTe₂ 在实验上首次实现铁电翻转（fei2018）：垂直极化 P≈1×10⁴ e·cm⁻¹，等效层间转移 ~2×10¹¹ e·cm⁻²；铁电回滞在 1.6 K 至 350 K 以上均存在，且当载流子密度超过 ~2×10¹² cm⁻² 进入金属态后回滞仍然保留（只是变小）——这是"金属铁电"的直接实验证据（[[../papers/feiFerroelectricSwitchingTwodimensional2018a]]）。
- **电荷分离机制**：以插层型 T-PdZr₂Se₄ 为代表的金属铁电体中，传导电子集中在 MX₂ 层、极化电荷局域在插层 A 原子周围，二者实空间分离使传导电子无法完全屏蔽垂直极化（Pout=3.10 pC/m）；16 种非磁金属铁电体 Pout 在 0.43–9.61 pC/m，均大于 WTe₂ 双层的 0.42 pC/m（[[../papers/zhaoRealization2DMultiferroic2024]]）。
- **材料家族**：除 WTe₂ 外，还包括室温铁电半金属（sharma2019）、二维铁电金属 CuCrX₂（X=S, Se，wang2025）、双层 FGT 磁性铁电金属（miao2024）等。
- **应用前景**：铁电金属的极化态可非破坏性读出（电导作为读出信号），适合做非易失存储、自旋电子与电催化平台。

![图：铁电金属 WTe₂ 的滑移翻转路径与差分电荷密度](../../raw/figures/bhowalPolarMetalsPrinciples2023b/fig_7_MZBMKDTD.png)
- **看图要点**：(a) 六方对称下三个等效极化上/下态；(b) 双层 WTe₂ 上层相对下层滑移实现垂直极化翻转；(c) 滑移前后层间差分电荷密度显示化学键合反转。
- **来源**：[[../papers/bhowalPolarMetalsPrinciples2023b]]

## 🔬 物理参数表

| 属性 | 数值 | 方法与来源 |
| :--- | :--- | :--- |
| WTe₂ 双层垂直极化 P | ~1×10⁴ e·cm⁻¹（层间转移 ~2×10¹¹ e·cm⁻²） | 双栅静电测量（[[../papers/feiFerroelectricSwitchingTwodimensional2018a]]） |
| WTe₂ 铁电回滞温区 | 1.6 K ~ 350 K+（~340 K 转非极性相） | 实验（[[../papers/feiFerroelectricSwitchingTwodimensional2018a]]） |
| 金属态阈值载流子密度 n_c | ~2×10¹² cm⁻²（超此仍保留回滞） | 双栅解耦实验（[[../papers/feiFerroelectricSwitchingTwodimensional2018a]]） |
| T-PdZr₂Se₄ 面外极化 Pout | 3.10 pC/m | 偶极修正 DFT（[[../papers/zhaoRealization2DMultiferroic2024]]） |
| 16 种非磁金属铁电体 Pout 范围 | 0.43–9.61 pC/m（均 > WTe₂ 双层 0.42） | 高通量 DFT（[[../papers/zhaoRealization2DMultiferroic2024]]） |

## 🧭 近邻概念辨析

- **与极性金属（polar-metal）**：极性金属仅要求极性结构+金属性，极化**不一定可翻转**（如 LiOsO₃ 是类铁电金属）；铁电金属是其中极化可电场翻转的子类。
- **与超铁电金属（hyper-ferroelectric-metal）**：超铁电金属源自"即使未屏蔽退极化场仍保持极化"的超铁电体掺杂金属化，与 WTe₂ 这类"薄层穿透屏蔽"的铁电金属机制不同。
- **与金属铁电性（metallic-ferroelectricity）**：metallic-ferroelectricity 强调"金属中实现铁电"这一物理现象本身；ferroelectric-metal 则更多指代具备该性质的材料类别，二者常互换使用。

## 📚 相关论文 (Related Papers)

- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]：双层 WTe₂ 铁电翻转的首个实验证实。
- [[../papers/bhowalPolarMetalsPrinciples2023b]]：极性金属/类铁电金属/铁电金属三层概念综述。
- [[../papers/zhaoRealization2DMultiferroic2024]]：插层策略高通量筛选出多种金属铁电体。
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]：二维铁电金属 CuCrX₂ 电催化。
- [[../papers/miaoMagneticFerroelectricMetal2024]]：双层 FGT 磁性铁电金属。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：室温铁电半金属。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/polar-metal|极性金属]]
- [[../concepts/metallic-ferroelectricity|金属铁电性]]
- [[../concepts/hyper-ferroelectric-metal|超铁电金属]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../entities/WTe2|WTe2]]
- [[../entities/LiOsO3|LiOsO3]]
