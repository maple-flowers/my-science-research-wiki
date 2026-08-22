---
tags: [concept, spintronics, spin-transfer-torque, magnetoelectric-coupling, 2d-materials]
title: 自旋转移矩 / Spin-Transfer Torque
type: concept
status: mature
year: 2025
domain: [condensed-matter-physics, spintronics, device-physics]
mechanism: 自旋极化的电流流过铁磁体时把角动量转移给局域磁矩，从而翻转磁化；与自旋轨道矩（SOT）并列为电流驱动磁化翻转的两大机制
related_concepts: [magnetic-tunnel-junction, spin-injection, spin-polarization, spin-orbit-torque, spin-hall-effect, magnetization-switching, skyrmion, magnetoelectric-coupling, 2d-materials]
papers: [zhangNonvolatileControlTopological2025]
updated: 2026-08-19
---

# 自旋转移矩 / Spin-Transfer Torque

自旋转移矩（Spin-Transfer Torque, STT）指自旋极化的电流在流过铁磁层时，通过 s-d 交换作用把自旋角动量转移给局域磁矩，从而对磁化施加力矩并实现电流驱动翻转的机制。它是 STT-MRAM 等下一代非易失存储器的核心写入原理，也是磁涡旋、斯格明子等拓扑磁结构电流操控的基础。

## 👵 太奶导读

乖孙，自旋转移矩就是"让电流本身去翻动小磁铁"。电流里的电子是带"自旋方向"的（像小陀螺），当它们冲进一块磁铁时，会把自己的"转劲"交给磁铁的磁矩——推着磁矩转向。这样一来，不用外加磁场，只靠电流就能"写"磁存储器的 0 和 1，又快又不掉电。一句话：**"让电流当扳手，拧动磁铁的方向"**。

## 🏗️ 结构概览

STT 的典型器件是磁隧道结（MTJ）：固定层 / 势垒 / 自由层。电流垂直流过时，被固定层极化后携带自旋角动量，在自由层处施矩翻转其磁化（平行 ↔ 反平行）。

## 🧩 核心内容与机制 (Core Content)

### 1. 力矩来源：自旋角动量转移

电子流经铁磁层时，其自旋被逐步对齐到局域磁化方向（自旋滤波），损失的角动量以力矩形式作用在磁矩上（Slonczewski/Berger 力矩）。平行/反平行方向决定力矩符号，从而可双向翻转。

### 2. 阈值电流与临界条件

STT 翻转需超过临界电流密度 $J_c$，与阻尼系数、各向异性场和热稳定性相关。降低 $J_c$ 是器件低功耗化的关键。

### 3. 从 STT 到拓扑磁结构操控

电流驱动 STT 可移动磁畴壁、斯格明子与双半子等拓扑磁织构。二维多铁异质结中，铁电极化翻转可协同增强界面 DMI 并抑制磁各向异性能（MAE），实现"铁磁态 ↔ 斯格明子晶格"的非易失电控切换（仅需 50 mT 辅助磁场），并可用无量纲判据 κ（孤立斯格明子/双半子稳定区间 5 < |κ| < 10）设计拓扑态（[[../papers/zhangNonvolatileControlTopological2025|Zhang 2025]]）。

### 4. 与磁电耦合的协同

多铁界面中电荷转移同时调控 DMI 与 MAE，为 STT 器件增加"电场写入、电流操控"的双重自由度，朝向全电控自旋电子学器件发展。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 临界电流密度 J_c | 翻转阈值 | 越低越省功耗 |
| 力矩类型 | 机制分类 | Slonczewski / Berger |
| 器件形态 | 应用载体 | MTJ、畴壁/斯格明子器件 |
| 辅助手段 | 降阈值 | 铁电/磁电协同、辅助磁场 |
| 应用 | 器件功能 | STT-MRAM、拓扑磁结构操控 |

## 🔀 近邻概念辨析

- **STT vs 自旋轨道矩（SOT）**：STT 靠电流被磁化层极化后转移角动量；SOT 靠重金属/界面自旋霍尔效应或 Rashba 效应产生的自旋流驱动。SOT 无需写入电流穿过势垒，通常更快但需面内电流布局。
- **STT vs 磁场写入**：磁场写入需外置线圈、能耗高；STT 直接电流写入，可缩小器件、低功耗、高集成度。

## 📚 相关论文 (Related Papers)

- [[../papers/zhangNonvolatileControlTopological2025]]：二维多铁异质结中非易失电控斯格明子与电流驱动动力学（STT 场景）。

## 🔗 关联概念与实体 (Related)

- [[../concepts/magnetic-tunnel-junction|磁隧道结]]
- [[../concepts/spin-injection|自旋注入]]
- [[../concepts/spin-hall-effect|自旋霍尔效应]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../concepts/skyrmion|斯格明子]]
- [[../entities/Fe3GeTe2|Fe3GeTe2]]
