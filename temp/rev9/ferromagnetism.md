---
tags: [concept, magnetism, spintronics, 2d-materials, exchange-interaction]
title: 铁磁性 / Ferromagnetism
type: concept
status: mature
year: 2020
domain: [condensed-matter-physics, magnetism, spintronics]
mechanism: 量子交换相互作用使原子磁矩自发平行排列，无外场时形成宏观自发磁化，并具有磁滞回线与居里温度
related_concepts: [antiferromagnetism, ferrimagnetism, altermagnetism, exchange-interaction, curie-temperature, magnetic-anisotropy, hysteresis, coercive-field, domain-wall, two-dimensional-magnetism, spintronics]
papers: [vanvleckSurveyTheoryFerromagnetism1945, xiangTwodimensionalRoomTemperature2020, wangTwodimensionalFerroelectricMetal2025, laiTwodimensionalFerromagnetismDriven2019]
updated: 2026-08-19
---

# 铁磁性 / Ferromagnetism

铁磁性（ferromagnetism）指材料中**原子磁矩在无外场时自发平行排列**并形成宏观磁化的磁性序，由量子力学交换相互作用驱动，是磁存储、自旋电子学与磁性功能材料的物理基础。其宏观表现为自发磁化、磁滞回线与明确的居里温度（Curie temperature）。

## 👵 太奶导读

太奶啊，铁磁材料就是咱们常说的"吸铁石"家族：里面的无数小磁针（原子磁矩）天生爱"齐刷刷朝一个方向"排，所以哪怕没有外界磁场，材料本身也是磁化的。加热超过某个温度（居里温度）它们就"乱了阵脚"变回普通磁体；外加磁场能把它"重新排齐"，拿走磁场它还能记住方向——这就是磁滞，存储数据的原理就靠它。

## 🏗️ 结构概览

铁磁性是磁性相图的核心相之一，与反铁磁、亚铁磁、交变磁性并列；其成立依赖交换作用强度、维度与温度三者的竞争。

- **维度极限**：二维体系因热涨落（Mermin-Wagner 定理）长程磁序受限，需磁各向异性或磁耦合支撑，构成"二维磁性"专题（[[../concepts/two-dimensional-magnetism|二维磁性]]）。
- **材料谱系**：金属（Fe/Co/Ni）、氧化物（如 CrO₂ 半金属）、二维范德华磁体（CrI₃、Cr₂Ge₂Te₆、Fe₃GeTe₂）等。

## 🧩 核心内容与机制 (Core Content)

### 1. 微观起源：交换相互作用

泡利不相容原理与库仑排斥竞争，使自旋平行排布能量更低，形成分子场/交换场；定域模型（海森堡）与巡游模型（斯托纳）分别描述绝缘磁体与金属磁体（[[../papers/vanvleckSurveyTheoryFerromagnetism1945|Van Vleck 1945]]）。

### 2. 宏观磁性参数

- 自发磁化 M_s、磁滞回线（hysteresis）、矫顽力（coercive field）、剩磁；
- 居里温度 T_C：铁磁-顺磁转变点，是材料实用性的关键指标（二维磁体追求室温 T_C，见 [[../papers/xiangTwodimensionalRoomTemperature2020|Xiang 2020]]）。

### 3. 磁畴与各向异性

为降低静磁能形成磁畴，畴壁运动决定磁化反转动力学；磁晶各向异性（magnetic anisotropy）决定易磁化轴与矫顽力。

### 4. 二维与调控

Cr₂Ge₂Te₆、CrI₃ 等二维铁磁体将磁性推向原子极限，配合铁电极化、应变可实现非易失电控（[[../papers/wangTwodimensionalFerroelectricMetal2025|Wang 2025]]、[[../papers/laiTwodimensionalFerromagnetismDriven2019|Lai 2019]]）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 居里温度 T_C | 铁磁-顺磁转变 | Fe 1043 K；2D 磁体多低于室温 |
| 自发磁化 M_s | 无场磁化强度 | 材料相关 |
| 矫顽力 | 反转磁化所需场 | 软磁小 / 硬磁大 |
| 交换作用 | 磁序能量尺度 | 定域 vs 巡游模型 |
| 应用 | 器件功能 | 磁存储、自旋电子学 |

## 🔀 近邻概念辨析

- **铁磁 vs 反铁磁 vs 亚铁磁**：铁磁有净磁化；反铁磁磁矩两两反排、净磁化为零；亚铁磁反排但大小不等、仍有净磁化。
- **铁磁 vs 交变磁性**：交变磁性净磁化为零（类反铁磁）但能带有显著自旋劈裂（类铁磁），是"隐藏"的铁磁序（[[../concepts/altermagnetism|交变磁性]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/vanvleckSurveyTheoryFerromagnetism1945]]：铁磁性理论（交换作用/磁序）的经典综述。
- [[../papers/xiangTwodimensionalRoomTemperature2020]]：二维室温铁磁材料的设计与展望。
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]：二维铁电金属中的磁性序。
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]：二维铁磁性及其调控机制。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/exchange-interaction|交换相互作用]]
- [[../concepts/curie-temperature|居里温度]]
- [[../concepts/magnetic-anisotropy|磁各向异性]]
- [[../concepts/hysteresis|磁滞回线]]
- [[../concepts/domain-wall|畴壁]]
- [[../concepts/antiferromagnetism|反铁磁性]]
- [[../concepts/altermagnetism|交变磁性]]
- [[../concepts/two-dimensional-magnetism|二维磁性]]
- [[../entities/CrI3|CrI3]]
- [[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]
- [[../entities/Fe3GeTe2|Fe3GeTe2]]
