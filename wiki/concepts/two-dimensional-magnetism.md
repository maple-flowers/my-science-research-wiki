---
tags: [concept, magnetism, 2d-materials, two-dimensional-magnetism, van-der-waals]
title: 二维磁性 / Two-Dimensional Magnetism
type: concept
status: mature
year: 2020
domain: [condensed-matter-physics, magnetism, 2d-materials]
mechanism: 单层/少层范德华晶体中稳定的磁有序；二维极限下 Mermin-Wagner 定理禁阻各向同性长程磁序，需磁各向异性（易轴/易面）支撑
related_concepts: [ferromagnetism, magnetic-anisotropy, curie-temperature, van-der-waals-heterostructure, magnetoelectric-coupling, altermagnetism, spintronics, 2d-materials]
papers: [liuSpintronicsTwoDimensionalMaterials2020b]
updated: 2026-08-19
---

# 二维磁性 / Two-Dimensional Magnetism

二维磁性（two-dimensional magnetism）指在单层或几层范德华晶体中实现的磁有序。它把磁性推进到原子厚度极限，可通过电场、应变、邻近效应与层间堆叠精细调控，是磁存储、自旋电子学与磁-光探测的理想平台。

## 👵 太奶导读

乖孙，二维磁性就是"把磁铁压成一张纸"。以前大家都以为磁铁薄到只剩一层原子时，会因热晃动而"站不住"（长程磁序会乱掉），结果 CrI₃、Cr₂Ge₂Te₆ 这些"饼状"材料在单层时依然能保持磁性——秘诀是它们天生带"方向偏好"（磁各向异性）把磁矩"钉住"。把这种"纸片磁铁"叠进异质结，就能用电压、应变来开关磁性。一句话：**"单层原子的磁铁也能稳定吸东西，还更好调"**。

## 🏗️ 结构概览

二维磁体通常由层间弱范德华耦合、层内强共价的原子薄层构成；磁序可通过磁各向异性、层数、邻近效应与外部场多维度调控。

## 🧩 核心内容与机制 (Core Content)

### 1. 二维磁序的稳定性

Mermin-Wagner 定理指出各向同性二维体系不存在有限温长程磁序；但磁晶各向异性（易轴/易面）打开能隙、抑制低能自旋波激发，使 CrI₃（易轴）、Cr₂Ge₂Te₆（易面）等单层可稳定磁化。磁各向异性能（MAE）是二维磁性的"定海神针"。

### 2. 代表性材料与探测

- CrI₃：层间反铁磁耦合的范德华磁体，磁光 Kerr 效应与磁圆二色（MCD）可单层探测；
- Cr₂Ge₂Te₆：层内铁磁、易面各向异性；
- Fe₃GeTe₂：金属性二维磁体，可电/离子调控居里温度。
临界厚度与磁转变行为由层数依赖的交换/各向异性竞争决定（[[../papers/gongAbsenceCriticalThickness2023|Gong 2023]]）。

### 3. 调控手段

- 电场/离子液体门控：调制载流子浓度改变 T_C；
- 应变：调制交换作用与各向异性；
- 邻近效应：与强自旋-轨道耦合材料（TMD、拓扑材料）堆叠引入 SOC；
- 铁电极化：通过磁电耦合非易失控制磁序（与多铁异质结结合）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 居里温度 T_C | 磁序稳定上限 | 多数低于室温，需设计提升 |
| 磁各向异性 | 磁序稳定来源 | 易轴（CrI₃）/ 易面（Cr₂Ge₂Te₆） |
| 层间耦合 | 层堆叠行为 | 铁磁/反铁磁可调 |
| 调控方式 | 外部自由度 | 电场、应变、邻近、铁电极化 |
| 应用 | 器件功能 | 自旋存储、磁光探测、异质结 |

## 🔀 近邻概念辨析

- **二维磁体 vs 三维磁体薄膜**：二维磁体原子级厚度、无悬挂键、可无损堆叠成异质结，层间耦合可控；三维薄膜受衬底与界面缺陷影响更大。
- **二维磁性 vs 交变磁性**：二维磁性强调维度带来的磁序稳定性与可调性；交变磁性强调"零净磁化 + 自旋劈裂"的对称性新相，二者可在二维平台结合。

## 📚 相关论文 (Related Papers)

- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：二维材料自旋电子学综述，覆盖二维磁体与自旋器件。

### ⚠️ 已撤回的引文

以下条目原列于本节，经核对其 `raw/note` 原始笔记后确认无据，于 2026-08-21 撤回：

- `gongAbsenceCriticalThickness2023`：原文笔记中无二维磁性相关表述。
- `xiangTwodimensionalRoomTemperature2020`：同上。

## 🔗 关联概念与实体 (Related)

- [[../concepts/ferromagnetism|铁磁性]]
- [[../concepts/magnetic-anisotropy|磁各向异性]]
- [[../concepts/curie-temperature|居里温度]]
- [[../concepts/van-der-waals-heterostructure|范德华异质结]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../concepts/altermagnetism|交变磁性]]
- [[../entities/CrI3|CrI3]]
- [[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]
- [[../entities/Fe3GeTe2|Fe3GeTe2]]
