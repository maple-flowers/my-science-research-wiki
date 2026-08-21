---
tags: [concept, spin-orbit-coupling, 2d-materials, magnetoelectric-coupling, spintronics]
title: 邻近效应 / Proximity Effect
type: concept
status: mature
year: 2020
domain: [condensed-matter-physics, spintronics, 2d-materials]
mechanism: 异质结界面处一种有序性（磁性/超导/自旋轨道）通过波函数重叠与交换耦合诱导到邻近材料中
related_concepts: [magnetoelectric-coupling, spin-orbit-coupling, rashba-effect, edelstein-effect, two-dimensional-magnetism, van-der-waals-heterostructure, spin-valve, spin-injection]
papers: [liuSpintronicsTwoDimensionalMaterials2020b, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]
updated: 2026-08-19
---

# 邻近效应 / Proximity Effect

邻近效应（proximity effect）指在**两种材料紧密接触的界面**处，一种材料的有序性（磁性、超导性、自旋-轨道耦合等）通过量子力学波函数重叠、交换相互作用或界面电荷转移**诱导、赋予到另一种材料**中的现象。在二维自旋电子学中，邻近效应是"用异质结给本身无磁/弱自旋轨道材料赋能"的关键手段。

## 👵 太奶导读

太奶啊，有些材料天生"胆小"——没有磁性、也不爱理睬自旋。可只要把它们紧紧贴在一种"有本事"的材料旁边（像磁铁、强自旋-轨道材料），贴在脸上的那一层就会"沾光"：隔壁的本事会渗过来，让这层胆小材料也带上磁性或学会摆弄自旋。这种"近朱者赤"的界面效应，就叫邻近效应。

## 🏗️ 结构概览

邻近效应按"被诱导的有序性"分型：磁邻近效应（诱导磁性）、自旋轨道邻近效应（诱导 SOC/Rashba 场）、超导邻近效应（诱导超导配对）。二维范德华异质结因其原子级平整界面成为邻近效应的理想平台。

## 🧩 核心内容与机制 (Core Content)

### 1. 磁邻近效应

磁性衬底/层（如 EuO、CrI₃、Fe₃GeTe₂）通过界面交换耦合在邻近层（石墨烯、TMD）中诱导出交换劈裂与磁性序，使本征非磁的二维材料获得自旋依赖的能带结构，是实现自旋注入与自旋滤波的前提（[[../papers/liuSpintronicsTwoDimensionalMaterials2020b|Liu 2020]]）。

### 2. 自旋轨道邻近效应

强 SOC 材料（WSe₂、Pt、拓扑绝缘体）通过邻近效应在石墨烯等弱 SOC 层中诱导出增强的自旋-轨道耦合与 Rashba 场，为电学自旋操控（自旋轨道矩、自旋-电荷转换）提供平台（[[../papers/liuSpintronicsTwoDimensionalMaterials2020b|Liu 2020]]）。

### 3. 与磁电调控的结合

邻近效应可与铁电调控协同：铁电衬底通过应变/场效应对邻近磁性层实现非易失磁各向异性调控，如 Fe₃GaTe₂/P(VDF-TrFE) 体系中的应变介导磁电耦合（[[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025|Cai 2025]]）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 诱导序类型 | 被诱导的有序性 | 磁 / SOC / 超导 |
| 界面质量 | 邻近效应强度 | 原子级平整界面最优 |
| 作用距离 | 效应衰减尺度 | 界面附近几纳米 |
| 平台材料 | 被赋能层 | 石墨烯、TMD、拓扑材料 |
| 源材料 | 提供有序性 | 磁性层、强 SOC 层 |

## 🔀 近邻概念辨析

- **邻近效应 vs 掺杂**：邻近效应是界面量子耦合、无原子替换，可逆、可门控；掺杂改变本征材料属性且引入无序。
- **邻近效应 vs 磁电耦合**：磁电耦合是电场↔磁化的本征交叉耦合；邻近效应是界面诱导机制，可为磁电耦合提供介质。
- **邻近效应 vs 自旋注入**：自旋注入强调电荷载体携带自旋越过界面；邻近效应强调界面诱导出静态有序性。

## 📚 相关论文 (Related Papers)

- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：二维自旋电子学综述，系统论述邻近效应在自旋注入与操控中的作用。
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：铁电极化驱动应变介导磁电耦合的邻近调控实例。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../concepts/spin-orbit-coupling|自旋-轨道耦合]]
- [[../concepts/rashba-effect|Rashba 效应]]
- [[../concepts/edelstein-effect|埃德尔斯坦效应]]
- [[../concepts/two-dimensional-magnetism|二维磁性]]
- [[../concepts/van-der-waals-heterostructure|范德华异质结]]
- [[../concepts/spin-injection|自旋注入]]
- [[../concepts/spin-valve|自旋阀]]
