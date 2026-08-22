---
tags: [concept, spintronics, 2D-materials, spin-injection, magnetoelectric-coupling]
title: 自旋注入 / Spin Injection
type: concept
status: mature
year: 2020
domain: [condensed-matter-physics, spintronics, device-physics]
mechanism: 通过隧道势垒、光学激发、自旋泵浦或自旋-轨道转换等方式，把自旋极化载流子从源材料送入非磁性/半导体通道
related_concepts: [spin-transport, spin-valve, spin-relaxation, spin-filtering, magnetic-tunnel-junction, spin-orbit-coupling, spin-hall-effect, proximity-effect, spintronics, 2d-materials]
papers: [liuSpintronicsTwoDimensionalMaterials2020b, yuFerroelectricControlMagnetism2026]
updated: 2026-08-19
---

# 自旋注入 / Spin Injection

自旋注入 (Spin Injection) 指把非平衡自旋极化载流子从自旋源（铁磁电极、磁性半导体、光学激发等）送入目标通道（金属、半导体或二维材料）的过程。它是自旋电子学器件的"入口"，注入效率（自旋极化率）直接决定后续传输与探测的信号强度。二维材料体系中，hBN/MgO 隧道势垒结合界面工程已实现近 100% 的自旋注入极化率。

## 👵 太奶导读

乖孙，自旋注入就是"给电子先排好队"再送进材料里。好比往会场里放人：你要让大家都朝一个方向走（自旋一致）才叫"注入成功"。直接放进去常常乱（接触阻抗失配），所以要架一座"小桥"（隧道势垒）慢慢放。二维材料领域最拿手的就是用 hBN 这座"桥"让电子排得整整齐齐进场。一句话：**"架座小桥，让电子排着整齐队形进场"**。

## 🏗️ 结构概览

自旋注入方案多样：电学注入（隧道势垒）、光学注入（圆偏振光）、自旋泵浦与自旋霍尔转换。

![图：二维材料中的自旋注入方案示意](../../raw/figures/liuSpintronicsTwoDimensionalMaterials2020b/fig_4_767YPDYC.png)
*   **看图要点**：展示了电学/光学自旋注入的器件构型与注入效率。
*   **来源**：[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]

## 🧩 核心机制

### 1. 电学注入与阻抗失配问题

直接从铁磁金属向高阻半导体注入时，阻抗失配使注入极化率极低（低于 0.1%）。解决方案是插入高阻隧道势垒（MgO、h-BN、Al₂O₃），使注入由隧穿主导，极化率提升至接近 100%。

### 2. 光学注入

用圆偏振光激发半导体（如 TMD），通过自旋-谷锁定选择性地产生特定自旋的载流子（光选通），实现高极化率自旋注入与谷极化。

### 3. 自旋泵浦与自旋霍尔转换

- **自旋泵浦**：铁磁层进动把自旋"泵"入相邻层，无需电接触；
- **自旋霍尔效应**：重金属中电荷流经 SOC 转换为横向纯自旋流，再注入邻近层。

### 4. 铁电调控注入

利用铁电极化调控界面能带或磁矩方向（磁电耦合），可实现"电写"式自旋注入状态切换（[[../papers/yuFerroelectricControlMagnetism2026|Yu 2026]]）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 注入极化率 | 注入效率 | hBN 势垒近 100% |
| 注入方式 | 手段 | 电学 / 光学 / 泵浦 / SHE |
| 势垒层 | 阻抗匹配 | MgO、h-BN、Al₂O₃ |
| 界面工程 | 极化提升 | 隧道势垒 + 钝化 |
| 调控途径 | 额外自由度 | 铁电/磁电耦合 |

## 🔀 近邻概念辨析

- **自旋注入 vs 自旋过滤**：注入关注"把极化自旋送进通道"的整体过程；过滤关注"从混合自旋中筛出单一自旋"的机制。高极化注入常依赖势垒过滤。
- **电学注入 vs 光学注入**：电学注入用铁磁源+势垒，可集成、可电控；光学注入用圆偏振光，极化高但需光激发。

## 📚 相关论文 (Related Papers)

- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：综述 2D 材料自旋注入的隧道势垒、光学注入与泵浦方法。
- [[../papers/yuFerroelectricControlMagnetism2026]]：铁电调控磁性/自旋注入状态切换的新机制。

## 🔗 关联概念与实体 (Related)

- [[../concepts/spin-transport|spin-transport]]
- [[../concepts/spin-valve|spin-valve]]
- [[../concepts/spin-filtering|spin-filtering]]
- [[../concepts/spin-relaxation|spin-relaxation]]
- [[../concepts/spin-hall-effect|spin-hall-effect]]
- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/magnetoelectric-coupling|magnetoelectric-coupling]]
- [[../entities/h-BN|h-BN]]
- [[../entities/MgO|MgO]]
- [[../entities/graphene|graphene]]
