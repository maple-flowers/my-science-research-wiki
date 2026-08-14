---
tags: [concept, spintronics, magnetics]
title: 隧穿磁阻 (Tunneling Magnetoresistance)
type: concept
status: mature
domain: [condensed-matter-physics, spintronics]
mechanism: 电子穿过夹在两个铁磁层之间的超薄绝缘势垒时，隧穿几率取决于两铁磁层磁化方向的相对取向
related_concepts: [magnetic-tunnel-junction, giant-magnetoresistance, spin-injection, stt-ram]
papers: [liuSpintronicsTwoDimensionalMaterials2020b, xueEmergingNonvolatileMemories2011]
updated: 2026-08
---

# 隧穿磁阻 / Tunneling Magnetoresistance (TMR)

隧穿磁阻 (TMR) 效应发生在由两个铁磁层 (FM) 和中间超薄绝缘层（隧道势垒）构成的磁隧道结 (MTJ) 中。当两铁磁层的磁化方向平行时，电子隧穿几率高，表现为低阻态；当磁化方向反平行时，隧穿几率低，表现为高阻态。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“隧穿磁阻”其实就是微观世界的“对暗号”。想象两块磁铁中间夹了一层特别薄的绝缘纸。虽然纸是不导电的，但在微观世界里，电子像是有“穿墙术”（隧穿）一样能钻过去。
> 
> 不过电子是有脾气的（自旋方向）。如果两块磁铁的磁场方向是一致的（平行），就像是暗号对上了，电子穿墙就容易，水流（电流）就大；如果两块磁铁磁场方向相反（反平行），暗号没对上，电子穿墙就费劲，水流就小。通过看水流大小，咱们就能知道这两块磁铁是怎么摆的，这就成了记录“0”和“1”的绝妙办法。

## 🏗️ 结构概览

TMR 效应的核心载体是磁隧道结 (MTJ)，其性能主要由 TMR 比值衡量。

![图：磁隧道结 (MTJ) 结构与 TMR 效应原理](../../raw/figures/liuSpintronicsTwoDimensionalMaterials2020b/fig_9_WV5SSCXM.png)
*   **看图要点**：图中展示了典型的 MTJ 结构：FM1/Insulator/FM2。两层铁磁层（如 CoFeB）中间夹着纳米级的绝缘层（如 MgO 或 hBN）。右侧曲线显示了电阻随外部磁场改变（导致磁化方向切换）而发生的阶跃变化。
*   **来源**：[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 物理原理与关键参数

### 朱利尔模型 (Jullière Model)
TMR 的大小可以用 Jullière 模型定量描述：
$$TMR = \frac{R_{ap} - R_p}{R_p} = \frac{2P_1 P_2}{1 - P_1 P_2}$$
其中 $P_1$ 和 $P_2$ 分别是两个铁磁电极在费米能级处的自旋极化率。极化率越高，TMR 效应越显著。

### 二维材料中的 TMR
在二维材料体系中，使用原子级平整的 hBN 作为隧道势垒，可以有效减少界面散射。基于二维磁体（如 $CrI_3$, $Fe_3GeTe_2$）的全二维 MTJ 已展现出极高的 TMR 比值。

### 应用
TMR 效应是硬盘读取磁头和自旋转移矩磁随机存储器 (STT-MRAM) 的核心物理原理。

## 📚 相关论文 (Related Papers)

- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：系统综述了二维材料异质结中的 TMR 效应与 MTJ 器件。
- [[../papers/xueEmergingNonvolatileMemories2011]]：讨论了基于 TMR 的 STT-RAM 在存储系统中的应用。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/magnetic-tunnel-junction|磁隧道结 (MTJ)]]
- [[../concepts/giant-magnetoresistance|巨磁阻 (GMR)]]
- [[../concepts/spin-injection|自旋注入]]
- [[../entities/h-BN|h-BN]]
- [[../concepts/stt-ram|STT-RAM]]
