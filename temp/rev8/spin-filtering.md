---
tags: [concept, spintronics, 2D-materials, spin-filtering, spin-orbit-coupling]
title: 自旋过滤 / Spin Filtering
type: concept
status: mature
year: 2020
domain: [condensed-matter-physics, spintronics, device-physics]
mechanism: 利用磁性与/或自旋-轨道耦合使两种自旋通道的隧穿/传输几率不对称，从而产生高自旋极化电流
related_concepts: [spin-injection, spin-polarization, spin-valve, magnetic-tunnel-junction, spin-orbit-coupling, spin-hall-effect, 2d-materials, ferromagnetism]
papers: [liuSpintronicsTwoDimensionalMaterials2020b]
updated: 2026-08-19
---

# 自旋过滤 / Spin Filtering

自旋过滤 (Spin Filtering) 指器件或材料对不同自旋方向的电子施加不对称的传输几率，从而输出高自旋极化电流的过程。它是自旋注入与自旋探测的基础环节：理想的"自旋过滤器"应只让一种自旋通过，如磁隧道结中的自旋依赖隧穿、磁性半导体势垒、以及强自旋-轨道耦合材料中的自旋选择性传输。

## 👵 太奶导读

乖孙，自旋过滤就像"给电子装了个安检门"：电子带着两种"方向"（自旋朝上/朝下）跑来，过滤门只放行其中一种，出来的就是"清一色"的自旋电流。这好比牛奶的"脱脂"——把一种成分单独挑出来。有了这个"纯自旋流"，后面的器件（磁存储、自旋逻辑）才有原料可用。一句话：**"给电子装安检门，只放一种自旋过去"**。

## 🏗️ 结构概览

自旋过滤可发生在势垒层（自旋依赖隧穿）或体材料/界面（自旋选择性散射）。

![图：自旋相关的隧穿与过滤机制示意](../../raw/figures/liuSpintronicsTwoDimensionalMaterials2020b/fig_5_JCRJICFM.png)
*   **看图要点**：展示了自旋依赖的态密度/隧穿过程与自旋极化输出。
*   **来源**：[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]

## 🧩 核心机制

### 1. 自旋依赖隧穿

铁磁电极中两种自旋的态密度在费米面处不等。隧穿电流正比于势垒两侧态密度乘积，平行/反平行配置下两种自旋通道占比不同，产生自旋极化电流。

### 2. 磁性势垒过滤

用磁性绝缘体（如 EuS、EuO）作势垒：势垒高度本身自旋相关，一种自旋被"抬高"阻挡、另一种通过，可实现接近 100% 的单自旋选择，构成"自旋过滤器"。

### 3. 强 SOC 材料的自旋选择性

在自旋-轨道耦合劈裂的能带（如 Rashba/自旋-谷锁定）中，特定动量通道只承载单一自旋，可依此实现动量-自旋选择性的过滤与探测（与自旋霍尔效应互补）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 自旋极化率 | 输出自旋纯度 | 磁性势垒近 100% |
| 过滤媒介 | 实现载体 | 铁磁电极、磁性势垒、SOC 能带 |
| 能量范围 | 工作窗口 | 费米面附近 |
| 器件形态 | 实现方式 | 隧穿 / 散射 / 选择性通道 |
| 应用 | 器件功能 | 自旋注入源、磁传感 |

## 🔀 近邻概念辨析

- **自旋过滤 vs 自旋注入**：注入指把非平衡自旋"送入"材料；过滤指在传输/隧穿过程中"筛出"单一自旋。过滤是获得高极化注入的一种手段。
- **自旋过滤 vs 自旋霍尔效应**：自旋霍尔效应靠 SOC 把电荷流横向转换为纯自旋流（电荷-自旋转换）；自旋过滤靠磁性/势垒不对称直接筛选自旋通道。

## 📚 相关论文 (Related Papers)

- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：综述基于 2D 材料与磁性势垒的自旋过滤/注入机制。

## 🔗 关联概念与实体 (Related)

- [[../concepts/spin-injection|spin-injection]]
- [[../concepts/spin-filtering|spin-filtering]]
- [[../concepts/spin-valve|spin-valve]]
- [[../concepts/magnetic-tunnel-junction|magnetic-tunnel-junction]]
- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/spin-hall-effect|spin-hall-effect]]
- [[../concepts/spin-transport|spin-transport]]
- [[../entities/EuS|EuS]]
- [[../entities/h-BN|h-BN]]
- [[../entities/TMDs|TMDs]]
