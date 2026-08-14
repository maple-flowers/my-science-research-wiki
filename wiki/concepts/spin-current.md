---
tags: [concept, spintronics]
title: 自旋流 / Spin Current
type: concept
status: mature
domain: [condensed-matter-physics, spintronics]
mechanism: 角动量的定向流动，可独立于电荷流存在
related_concepts: [spin-orbit-coupling, rashba-effect, topological-magnon]
papers: [caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenStrongSlidingFerroelectricity2024, deSousa2008electrical]
updated: 2026-08
---

# 自旋流 / Spin Current

自旋流 (Spin Current) 指的是电子或准粒子（如激磁子）携带的角动量的定向流动。在理想的纯自旋流中，没有净电荷移动。自旋流是自旋电子学的核心载体，利用自旋流代替电流传输和处理信息，可以极大降低器件的焦耳热损耗。

## 👵 太奶导读

好孩子，咱平时用的电就像是河里的水在流（电荷流），水流过去能发电，但也会因为摩擦变热。
这“自旋流”就神了，它就像是河里的水没往前挪，但水面上的漂流瓶（角动量）却在有序地往前传。
你可以把它想象成一群人站在原地传球：人没动（没电流），但球传到了终点（信息传到了）。
因为人不动，就不容易撞来撞去发热。科学家们想用这种“传球”的办法来做芯片，这样你的手机玩一天游戏也不会烫手啦。

## 🏗️ 结构概览：二维逻辑器件中的自旋流注入

在多铁逻辑器件中，自旋流通过铁磁/非磁界面注入并被电调控。

![图：自旋场效应晶体管中的自旋流进动与检测](../../raw/figures/chenStrongSlidingFerroelectricity2024/fig_4_5NCCX3U9.png)
*   **看图要点**：图中 (c) 展示了 Datta-Das 自旋 FET。自旋从铁磁源极注入沟道形成自旋流，在 Rashba 场作用下发生进动，最后由漏极检测其自旋方向。
*   **来源**：[[../papers/chenStrongSlidingFerroelectricity2024]] -> [[../figures/electronic-devices-memory-transistors]]

## 🧩 分类与产生方法

1.  **极化电流 (Polarized Current)**：电荷流与自旋流共存（如巨磁电阻效应中）。
2.  **纯自旋流 (Pure Spin Current)**：只有角动量流动，无电荷移动。
    - **产生方式**：
        - **自旋霍尔效应 (SHE)**：利用强 SOC 使不同自旋电子横向偏转。
        - **激磁子注入**：在绝缘磁体中通过自旋泵浦 (Spin Pumping) 产生。
        - **极化翻转调控**：如滑动铁电中反转 Rashba 场实现自旋流的调制。

## 📚 相关论文 (Related Papers)

- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：利用反常霍尔效应 (AHE) 间接表征器件中的自旋序变化。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：基于滑动铁电设计了电控自旋进动的 FET 器件原型。
- [[../papers/deSousa2008electrical]]：研究了绝缘多铁性材料中激磁子自旋流的电学操控。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-orbit-coupling|自旋-轨道耦合]]（产生与转换的核心）
- [[../concepts/rashba-effect|Rashba 效应]]（调控手段）
- [[../concepts/topological-magnon|拓扑激磁子]]（绝缘体中的载体）
- [[../entities/TMDs|TMDs]]（具有强 SOC 和丰富自旋物理的二维平台）
