---
tags: [concept, spintronics, 2D-materials, spin-orbit-coupling, topological-physics, magnetoelectric-coupling]
title: 自旋输运 / Spin Transport
type: concept
status: mature
year: 2020
domain: [condensed-matter-physics, spintronics, 2D-materials]
mechanism: 自旋角动量（而非电荷）在材料中的注入、传输、操控与探测；二维材料以原子级厚度、长自旋弛豫与可调对称性提供理想平台
related_concepts: [spintronics, spin-orbit-coupling, spin-texture, spin-current, spin-transfer-torque, spin-orbit-torque, valleytronics, magnetoelectric-coupling, domain-wall, topological-insulator]
papers: [liuSpintronicsTwoDimensionalMaterials2020b, pedramraziManipulatingTopologicalDomain2019, spaldinAdvancesMagnetoelectricMultiferroics2019]
updated: 2026-08-19
---

# 自旋输运 / Spin Transport

自旋输运 (Spin Transport) 指自旋角动量（而非电荷）在材料中的注入、传输、操控与探测过程，是自旋电子学 (spintronics) 的核心。二维材料凭借原子级厚度、可调对称性与异质结构筑能力，为自旋输运提供了理想平台；自旋输运与拓扑态、磁电耦合、多铁性紧密交织。

## 👵 太奶导读

传统电子学传"电荷"，自旋电子学传"自旋"——把电子当作一个个带方向的"小磁针"来传信息。自旋传得快、不发热、掉电不忘，是下一代低功耗计算的大热门。二维材料薄如原子层，自旋在里面不容易乱（弛豫长），还能用电场、磁场、异质结多种手段操控，是做自旋输运器件的"黄金赛道"。

## 🏗️ 结构概览

自旋输运的完整链条：注入 → 传输 → 操控 → 探测。

![图：二维材料中的自旋电子学与自旋输运器件示意](../../raw/figures/liuSpintronicsTwoDimensionalMaterials2020b/fig_1_VXXN2SRG.png)
*   **看图要点**：展示了基于二维材料的自旋注入、传输与探测器件构型。
*   **来源**：[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]

## 🧩 核心机制

### 1. 自旋注入与传输

通过 hBN 隧道势垒电学注入已实现近 100% 的自旋极化率；hBN 封装与悬浮技术大幅提升石墨烯的自旋弛豫时间与扩散长度。二维材料中自旋-轨道耦合可调（从石墨烯的弱到 TMD 的强），提供了自旋寿命与操控的平衡空间。

### 2. 异质结邻近效应与操控

在异质结中通过邻近效应引入自旋-轨道耦合或磁性，实现电控自旋方向；自旋-轨道力矩 (SOT)、自旋转移力矩 (STT) 是操控磁化的主要电学手段。

### 3. 拓扑与畴壁中的一维自旋通道

在单层量子自旋霍尔绝缘体 1T′-WSe₂ 中，STM 针尖脉冲可逆创建 1T′/1T′ 畴界，其上存在拓扑不受保护的一维电子态，具能量色散与空间衰减特征，构成纳米尺度的自旋/电荷通道。

### 4. 磁电耦合与多铁调控

多铁材料通过磁电耦合实现电控磁性，进而调控自旋输运；BiFeO₃ 畴壁展现导电、忆阻等独立于母体的功能，为原子级自旋电子学提供器件基础。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 自旋极化率 | 注入效率 | 近 100%（hBN 势垒） |
| 弛豫时间/长度 | 自旋保持 | hBN 封装石墨烯大幅提升 |
| 自旋-轨道耦合 | 操控媒介 | 材料可调（弱-强） |
| 操控方式 | 电学手段 | STT / SOT / 邻近效应 |
| 通道形态 | 输运载体 | 2D 平面 / 一维畴界 |

## 🔀 近邻概念辨析

- **自旋输运 vs 电荷输运**：前者传输自旋角动量，可伴随很小电荷流（纯自旋流）；后者传输电荷。二者通过自旋-电荷转换（自旋霍尔效应等）相互联系。
- **自旋输运 vs 磁电耦合**：磁电耦合是电/磁序参量的互控（宏观对称性机制）；自旋输运是自旋的微观输运过程，磁电耦合可成为调控自旋输运的手段。

## 📚 相关论文 (Related Papers)

- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：综述二维材料中的自旋电子学与自旋输运进展。
- [[../papers/pedramraziManipulatingTopologicalDomain2019]]：拓扑畴界中的一维电子态与自旋通道实验。
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：多铁性与磁电耦合对自旋输运的调控框架。

## 🔗 关联概念与实体 (Related)

- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/spin-texture|spin-texture]]
- [[../concepts/spin-current|spin-current]]
- [[../concepts/spin-transfer-torque|spin-transfer-torque]]
- [[../concepts/spin-hall-effect|spin-hall-effect]]
- [[../concepts/magnetoelectric-coupling|magnetoelectric-coupling]]
- [[../concepts/domain-wall|domain-wall]]
- [[../concepts/topological-insulator|topological-insulator]]
- [[../entities/TMDs|TMDs]]
- [[../entities/BiFeO3|BiFeO3]]
