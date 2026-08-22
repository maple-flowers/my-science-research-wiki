---
tags: [entity, multiferroicity, type-ii-multiferroic, ferroelectricity, magnetoelectric-coupling, 2d-materials, electrocatalysis, chemical-vapor-transport]
title: CuCrSe2
type: entity
status: developing
year: 2024
papers: [RecentAdvancesGrowth2025, tangMultiferroicityTwodimensionalVan2025, xiangTwodimensionalRoomTemperature2020, wangTwodimensionalFerroelectricMetal2025]
updated: 2026-08-21
---

# CuCrSe2

**CuCrSe₂** 是本库中少数**已在实验上做到单层、且单层即具多铁性**的二维材料之一。它的价值在于：铁电性与磁性由不同的原子承担（Cu 位移给极化，Cr 给磁性），却又通过 Cu 的位移改变相邻 CrSe₂ 层的电子结构而彼此耦合。

## 👵 太奶导读

乖孙，多铁材料难做，难在一个老矛盾：**铁电要 d 轨道空着，铁磁要 d 轨道半满**——同一个原子没法两头都占。

CuCrSe₂ 的办法是**分工**：让 Cu 原子管铁电，Cr 原子管磁性。

Cu 原子在这个结构里被硒原子包成一个四面体，但上下两边的硒不对称——一边挨着 1 个 Se，另一边挨着 3 个 Se。这就让 Cu 离子上下位置偏了一点，整层因此有了垂直方向的电极化。而 Cr³⁺ 的 d 轨道是半满的，天生带磁性。

妙处在于两者并非各管各的：Cu 一偏，紧邻的 CrSe₂ 层的电子结构就跟着变，磁性也跟着变。所以拿电场推动 Cu 位移，就能间接调磁——这就是磁电耦合。

要记住的一句话：**CuCrSe₂ 是「铁电靠 Cu、磁性靠 Cr、耦合靠 Cu 位移牵动 CrSe₂ 层」的第二类多铁范例，且已经在实验上做到了单层。**

## 🧩 结构与机制 (Structure & Mechanism)

- **Cu 配位的不对称性是极化之源**：Cu⁺ 为 d¹⁰ 满壳层，按晶体场理论倾向 sp³ 四面体配位。在 CuCrX₂（X = S, Se）中每个 Cu 与一侧相邻层的 1 个 X 原子、另一侧的 3 个 X 原子配位，Cu 离子到上下两层的垂直距离因此不等，直接产生垂直电极化。
- **磁性来源与耦合路径**：Cr³⁺ 提供磁序；Cu⁺ 的不对称位移在产生极化的同时改变相邻 CrSe₂ 层的电子结构，从而诱发／调制磁性。电场驱动 Cu⁺ 重排即可间接调控磁序——这是本体系[[../concepts/magnetoelectric-coupling|磁电耦合]]的机制。
- **多铁类型**：单原子层即表现出**第二类（type-II）多铁序**，与 NiI₂ 同属实验已实现的少数体系。
- **制备**：化学气相输运（CVT）法，以多晶粉末为源，配合化学剥离得到单层。CVT 也是 NiI₂、Cr₂S₃ 等二维多铁材料的主流制备手段。
- **表征**：二次谐波产生（SHG）是判定这类体系铁电与磁序的主要手段——它只在非中心对称介质中出现。

### 转变温度与性能

| 量 | 数值 | 来源 | 性质 |
|---|---|---|---|
| 铁电 T_C | 室温以上 | Sun et al. 2024 单层实验（经 [[../papers/RecentAdvancesGrowth2025\|综述]]转述） | 实验 |
| 铁磁 T_C | 120 K | 同上 | 实验 |
| 铁磁 T_C（预测） | 室温以上 | Zhong et al. 预测，经 [[../papers/xiangTwodimensionalRoomTemperature2020\|xiang2020]]评述 | 计算预测 |
| ORR 过电位（双层 P⁺） | 1.06 V | [[../papers/wangTwodimensionalFerroelectricMetal2025\|wang2025]] | 计算预测 |

⚠️ **一处需注意的理论—实验落差**：理论预测 CuCrX₂ 的铁磁与铁电 T_C **均高于室温**（机制归为载流子密度提升与极化驱动的轨道能移），但单层实验测得的铁磁 T_C 只有 **120 K**。本库现有材料不足以判断落差来自样品质量、层数差异还是预测本身偏乐观，此处仅记录矛盾，不作裁决。

## ⚗️ 一个反例：为什么它不是好催化剂

CuCrSe₂ 在 ORR/OER 催化上**表现明显不如同族的 CuCrS₂**，原因符合萨巴蒂尔原理：Se 电负性弱于 S、原子半径更大，导致表面对 O₂ 的吸附**过强**，使第一步 `O₂ → *OOH` 成为决速步并抬高能垒，过电位普遍超过 1.0 V；相较之下三层 CuCrS₂ 的 P⁺ 表面 ORR 过电位仅 0.28 V。这条反例的意义在于说明**铁电极化调控表面催化的前提是吸附强度本身落在合适区间**——极化能优化的是「恰到好处」附近的性能，救不回吸附过强的体系。

## 📚 相关论文 (Related Papers)

- [[../papers/RecentAdvancesGrowth2025]]：给出本页唯一的单层实验数据来源——CVT 法结合化学剥离制备的单层 CuCrSe₂ 呈室温铁电 + 120 K 铁磁，并将其与 NiI₂ 并列为「单原子层即具第二类多铁序」的里程碑案例，同时交代了 CVT 制备与 SHG 表征这两项方法学基础。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：把 CuCrSe₂ 归入「在磁体中引入铁电」这一设计策略，并明确指出其机制是 Cu 与 Cr 的垂直位移使铁电与铁磁序共存、且 Cu⁺ 位移改变相邻 CrSe₂ 层电子结构，为本页的耦合路径提供了机制层面的表述。
- [[../papers/xiangTwodimensionalRoomTemperature2020]]：作为评述文章转述了 Zhong 等人对 CuCrX₂（X = S, Se）的预测——铁磁与铁电 T_C 均高于室温，铁磁由载流子密度提升与极化驱动的轨道能移稳定——是本页「理论预测值」一栏的唯一来源，也是上文理论—实验落差的一端。
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]：本文主角是 CuCrS₂，CuCrSe₂ 在其中扮演对照组：因 Se 电负性较弱导致 O₂ 吸附过强、过电位普遍高于 1.0 V。它为本页提供的是一条**负面结论**——说明 CuCrSe₂ 的电催化潜力有限，不宜与其多铁性能混为一谈。

## 🔗 关联概念与实体 (Related)

- [[../concepts/multiferroicity|multiferroicity]]
- [[../concepts/magnetoelectric-coupling|magnetoelectric-coupling]]
- [[../concepts/ferroelectricity|ferroelectricity]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/ferroic-order|ferroic-order]]
- [[../concepts/d0-rule|d0-rule]]
- [[../concepts/2d-materials|2d-materials]]
- [[../concepts/intercalation-engineering|intercalation-engineering]]
- [[../entities/NiI2|NiI2]]
- [[../entities/BiFeO3|BiFeO3]]
- [[../entities/In2Se3|In2Se3]]
