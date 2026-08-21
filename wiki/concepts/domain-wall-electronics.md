---
tags: [concept, ferroelectrics, nanoelectronics, multiferroicity]
title: 畴壁电子学 / Domain-Wall Electronics
type: concept
status: mature
domain: [ferroelectrics, nanoelectronics, spintronics, multiferroicity]
mechanism: 利用畴壁本征的导电性/绝缘性差异构建纳米尺度功能器件（导电纳米导线、逻辑门、存储单元），壁导电性源于带电壁的载流子补偿与壁内序参量梯度
related_concepts: [domain-wall, ferroelectric-domain-wall, polarization-switching, negative-capacitance, ferroelectric-tunnel-junction, multiferroicity, strain-engineering]
papers: [gaoStrainEngineeringFerroelectric2024, neumayerCompetingPolarPhases2025]
updated: 2026-08
---

# 畴壁电子学 / Domain-Wall Electronics

畴壁电子学（domain-wall electronics）指**将铁性材料中的畴壁作为功能单元用于构建电子器件**的研究方向。畴壁具有与体相截然不同的导电性、磁性、机械与拓扑性质，可在不改变材料体性质的前提下提供可重写的纳米尺度功能——如导电纳米导线、逻辑门、存储单元与可编程互连，是后摩尔时代新型器件的候选方案之一。

## 👵 太奶导读

太奶啊，平时我们做电线，得用铜丝银丝。科学家发现，有的材料里"分界线"（畴壁）自己就能导电——就像材料里面天生长了一根"纳米电线"，还能用电场随时画出来、抹掉。这就叫畴壁电子学：不用刻电路，直接在材料里"画"电路，还能越做越小。

## 🧩 核心内容与机制 (Core Content)

- **壁导电性来源**：带电畴壁的束缚电荷被自由载流子补偿形成导电通道；中性壁亦可因壁内极化梯度、能带弯曲或缺陷积累而导电。导电壁可视为可重写的纳米导线。
- **功能器件**：畴壁可用于非易失性存储（壁存在=1）、逻辑门（壁的创建/擦除/移动）、可编程互连与整流器件（壁导电各向异性）。
- **与应变工程结合**：单轴/剪切应变可旋转 β'-In₂Se₃ 的极化方向并触发自发铁弹-铁电相变，应变方向与畴壁走向的夹角在 60°/180° 壁类型间切换，实现"应变编程"畴壁电子学 [[../papers/gaoStrainEngineeringFerroelectric2024]]。
- **竞争极性相调控**：在 CuInP₂S₆ 类材料中，层内铁电、层间铁电与反铁电相能量接近（几十 meV/f.u.），可通过温度、电场与 Cu⁺ 离子迁移实现畴壁构型可逆转换，为按需调控畴壁电子器件提供平台 [[../papers/neumayerCompetingPolarPhases2025]]。

## 📊 畴壁电子学器件速览

| 器件 | 功能 | 畴壁角色 | 关键材料 |
|------|------|----------|----------|
| 导电纳米导线 | 可重写互连 | 导电壁 | BiFeO3、YMnO3 |
| 非易失存储 | 数据存储 | 壁存在/位置 | 铁电薄膜 |
| 逻辑门 | 运算 | 壁创建/擦除 | PbTiO3 异质结 |
| 应变编程器件 | 柔性电子 | 铁弹-铁电壁 | β'-In₂Se₃ |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/domain-wall|畴壁]]：器件的功能单元。
- [[../concepts/ferroelectric-domain-wall|铁电畴壁]]：铁电体系的壁。
- [[../concepts/polarization-switching|极化翻转]]：畴壁的写入机制。
- [[../concepts/ferroelectric-tunnel-junction|铁电隧道结]]：相关铁电器件。
- [[../concepts/multiferroicity|多铁性]]：磁电协同器件平台。
- [[../concepts/strain-engineering|应变工程]]：畴壁构型的调控手段。
- [[../entities/In2Se3|In₂Se₃]]：应变编程畴壁平台。
- [[../entities/CuInP2S6|CuInP₂S₆]]：竞争极性相材料。

## 📚 相关论文 (Related Papers)

- [[../papers/gaoStrainEngineeringFerroelectric2024]]：应变"编程"控制 β'-In₂Se₃ 铁电畴壁类型（60°/180° 切换）的理论框架。
- [[../papers/neumayerCompetingPolarPhases2025]]：能量相近竞争极性相的畴壁构型调控与 Cu⁺ 离子耦合机制。

## 🏷️ 专业名词别名

- `domain-wall-nanoelectronics`（concepts）
- `壁导电器件`（concepts）
