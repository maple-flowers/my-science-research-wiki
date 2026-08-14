---
tags: [concept, spintronics, magnetics]
title: 巨磁阻 (Giant Magnetoresistance)
type: concept
status: mature
domain: [condensed-matter-physics, spintronics]
mechanism: 在铁磁/非磁多层膜结构中，电阻随相邻铁磁层磁化方向相对取向改变而发生显著变化的现象
related_concepts: [tunneling-magnetoresistance, spin-valve, magnetic-tunnel-junction, spin-transport]
papers: [liuSpintronicsTwoDimensionalMaterials2020b, xueEmergingNonvolatileMemories2011]
updated: 2026-08
---

# 巨磁阻 / Giant Magnetoresistance (GMR)

巨磁阻 (GMR) 效应发现于由铁磁层 (FM) 和金属非磁导电层 (NM) 交替组成的超晶格或多层膜中。当相邻铁磁层的磁化方向平行时，器件呈现低电阻；当反平行时，由于自旋相关散射增强，呈现高电阻。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“巨磁阻”其实就是微观世界的“顺风车”。想象你在一个长廊里走，走廊两边站满了卫兵（磁铁电极）。如果两边卫兵都挥手朝右（磁场平行），那跟你一样习惯朝右走的电子就像坐上了顺风车，嗖的一下就跑过去了，路就很通畅（低电阻）。
> 
> 但如果左边卫兵朝左挥，右边卫兵朝右挥（反平行），电子无论习惯往哪边走，都会被其中的一排卫兵拦住去路、撞得鼻青脸肿。这样电子走得就特别费劲，路就变得很堵（高电阻）。科学家们就利用这个电阻的大变化，做出了能感应极微弱磁场的装置，咱们以前用的那种机械硬盘，能存那么多东西，全靠这个宝贝。

## 🏗️ 结构概览

GMR 效应最早在 Fe/Cr 多层膜中观察到。在自旋电子学研究中，常见的实现形式是自旋阀 (Spin Valve) 结构。

![图：典型二维材料自旋阀结构与 GMR 测量](../../raw/figures/liuSpintronicsTwoDimensionalMaterials2020b/fig_6_I7PXRSCV.png)
*   **看图要点**：图中展示了基于石墨烯的非局域自旋阀结构。两个铁磁电极（FM）之间通过石墨烯通道相连。通过改变外部磁场，可以控制两个电极的磁化方向，从而观察到明显的非局域电阻阶跃，这体现了自旋相关散射产生的磁阻效应。
*   **来源**：[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 物理机制与意义

### 自旋相关散射
GMR 的核心在于电子在铁磁层中的散射几率与其自旋方向有关。在反平行状态下，两种自旋方向的电子都会经历强散射，导致整体高阻。

### 两流模型 (Two-Current Model)
由莫特 (Mott) 提出，认为总电导是自旋向上和自旋向下两个独立通道的并联。在平行状态下，一个通道阻力极小，显著降低了总电阻。

### 历史地位
GMR 的发现开启了自旋电子学时代，并直接促成了硬盘记录密度的飞跃式提升，两位发现者获得了 2007 年诺贝尔物理学奖。

## 📚 相关论文 (Related Papers)

- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：回顾了 GMR 效应如何从传统薄膜扩展到二维材料（如石墨烯、TMDs）体系。
- [[../papers/xueEmergingNonvolatileMemories2011]]：将磁阻效应列为新兴非易失存储技术的物理基石之一。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/tunneling-magnetoresistance|隧穿磁阻 (TMR)]]
- [[../concepts/spin-valve|自旋阀]]
- [[../concepts/spin-injection|自旋注入]]
- [[../entities/graphene|石墨烯]]
- [[../entities/TMDs|过渡金属硫族化合物]]
