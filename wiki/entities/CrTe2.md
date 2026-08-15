---
tags: [entity, material, 2D, magnetism]
title: 二碲化铬 (CrTe₂)
type: entity
status: mature
category: [D01]
formula: CrTe2
stoichiometry: 1T Phase / Bulk
class: [vdW, magnet, metal]
properties: [room-temperature-ferromagnetism, metallic-conduction, thickness-dependent-magnetism]
related_entities: [CrI3, Fe3GeTe2, VSe2, TMDs]
papers: [caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenFerromagneticNonmagnetic1T2022, guoAdvancesTwodimensionalFerroelectric2025, kaurRecentAdvancesTheoretical2025a, liMonolayerPuckeredPentagonal2022, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, wuNonvolatileSwitchableHalfmetallicity2024, yuFerroelectricControlMagnetism2026, zhangNonvolatileControlTopological2025, zhaoRealization2DMultiferroic2024]
updated: 2026-08
---

# 二碲化铬 (CrTe₂)

CrTe₂ 是一种备受关注的二维金属性铁磁材料，特别是在其 1T 相结构下。与许多需要在极低温下工作的二维磁体不同，少层甚至单层 CrTe₂ 表现出接近甚至超过室温的居里温度 ($T_C$)。结合其优异的导电性，它是开发高性能自旋电子器件（如磁隧道结、自旋轨道转矩器件）的关键候选材料。

## 👵 太奶导读

好孩子，这“二碲化铬”就是二维磁铁里的“全能劳模”。
一般的二维小磁铁都特别“怕热”，一到常温就没磁性了。但这 CrTe₂ 特别皮实，在咱们平时生活的温度下也能磁力十足。
因为它本身就能导电，就像是一根自带磁性的金属丝。科学家们非常看好它，觉得以后可以用它来做那种既能当导线传信号、又能当磁铁存信号的超级微型零件，省空间还省电。

## 🏗️ 结构概览：1T-CrTe2 的晶体结构与金属性

![图：1T-CrTe2 的层状结构与费米面金属性](../../raw/figures/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025/fig_1_A3L3NFIH.png)
*   **看图要点**：Cr 原子被 Te 原子构成的八面体包围，形成典型的 1T 相层状结构。图中展示了其费米能级处具有显著的电子态密度，证实了其金属性。
*   **来源**：[[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]] -> [[../figures/electronic-devices-memory-transistors]]
*(注：借用 Cai 2025 中关于二维金属磁体背景的描述)*

## 🧩 核心物性参数

| 性质 | 数值 | 备注 |
| :--- | :--- | :--- |
| **居里温度 ($T_C$)** | ~300 - 320 K | 随层数减薄可能略有下降但维持高位 |
| **磁各向异性** | 易面 (Easy-plane) | 倾向于在面内磁化 |
| **导电性** | 金属 | 低电阻率，适合高速自旋注入 |
| **稳定性** | 环境敏感 | 在空气中易氧化，需在惰性气体下保护 |

## 🔬 实验表征/特征与范例

**室温二维多铁金属（双层 CrTe₂）**：通过 MBE 在石墨烯/SiC 衬底上生长的双层 CrTe₂ 呈现独特的层状磁序——第一层反铁磁（AFM）、第二层铁磁（FM），构成室温稳定的二维多铁金属。实验将压电力显微镜（PFM）与磁力显微镜（MFM）联用，实现"电写磁读"，即通过电压非易失地控制磁序翻转 [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]。

**插层诱导强磁电耦合（Cr₄S₄FBr₂）**：由双层 CrSBr 通过氟离子（F⁻）桥联"融合"设计的单层 Cr₄S₄FBr₂（CSFB）是 A 型完全补偿亚铁磁金属，插层诱导的对称性破缺将铁电性与磁性强关联，实现室温电场对磁矩的完全控制，并预测巨磁阻与多铁隧道结（MFTJ）应用 [[../papers/yuFerroelectricControlMagnetism2026]]。

**高通量插层多铁（AM₂X₄）**：对 960 种非中心对称插层化合物 AM₂X₄ 进行第一性原理高通量筛选，鉴定出 21 种二维多铁单层（如 T-CdCr₂Te₄、T-CoZr₂S₄、T-CoTi₂Te₄），兼具强磁电耦合、高极化与较高转变温度 [[../papers/zhaoRealization2DMultiferroic2024]]。

**1T' 相 CDW 与磁性共存**：1T' 相 TMD 中 CDW 态大多非磁（NM），少数铁磁（FM）；CrS₂ 中电荷掺杂可诱导巨大的应变输出相变，为纳米致动器与自旋电子器件提供平台 [[../papers/chenFerromagneticNonmagnetic1T2022]]。

**滑动铁电与二维铁电背景**：滑动铁电性（层间滑移产生极化）是二维铁电的新范式，理论综述覆盖 hBN、TMDs、CrTe₂ 等体系 [[../papers/kaurRecentAdvancesTheoretical2025a]]；二维铁电材料分为自发极化（离子位移）与滑移铁电（层间电荷重分布）两类 [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]。

**多铁异质结与多铁性背景**：CrTe₂ 作为室温二维磁体，常被用于构建多铁异质结实现电控磁性，如 Hf₂MnC₂O₂/Sc₂CO₂ [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]、CrInTe₂/In₂Se₃ [[../papers/zhangNonvolatileControlTopological2025]]；二维范德华多铁性的挑战与机遇综述 [[../papers/tangMultiferroicityTwodimensionalVan2025]]；Fe₃GaTe₂ 应变调控磁各向异性 [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]；五边形 VTe₂ 多铁半导体 [[../papers/liMonolayerPuckeredPentagonal2022]]。

## 📚 相关论文 (Related Papers)

- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：引用 CrTe₂ 作为高性能室温二维磁体的代表。
- [[../papers/chenFerromagneticNonmagnetic1T2022]]：研究了 1T' 相 TMD 中的 CDW 与磁性共存机制，涉及 CrTe₂ 类体系对比。
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]：综述了新型二维铁磁体在多铁异质结中的集成。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：综述了层状与范德华二维材料中滑动铁电性的理论研究进展。
- [[../papers/liMonolayerPuckeredPentagonal2022]]：预测了单层褶皱五边形 VTe₂ 作为具有多铁性耦合的二维铁磁半导体。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：综述了二维范德华材料实现多铁性的挑战与机遇。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：报道了具有电压可控磁序的室温二维多铁金属。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：在 MXene Hf₂MnC₂O₂/Sc₂CO₂ 多铁异质结中实现了非易失可开关的半金属性与磁性。
- [[../papers/yuFerroelectricControlMagnetism2026]]：通过插层诱导对称性破缺实现铁电调控磁性及巨磁阻。
- [[../papers/zhangNonvolatileControlTopological2025]]：在 CrInTe₂/In₂Se₃ 多铁异质结中实现了对拓扑磁性的非易失调控。
- [[../papers/zhaoRealization2DMultiferroic2024]]：通过插层实现强磁电耦合二维多铁的第一性原理高通量预测。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/curie-temperature|居里温度]]（室温稳定性）
- [[../concepts/charge-density-wave|CDW]]（1T' 相中可能存在的关联序）
- [[../entities/Fe3GeTe2|Fe₃GaTe₂]]（垂直易轴竞争材料）
- [[../entities/VSe2|VSe₂]]（同为 1T 相的二维磁体）
