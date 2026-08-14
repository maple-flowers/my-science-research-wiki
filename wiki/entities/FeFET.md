---
tags: [entity, device, memory, ferroelectric]
title: 铁电场效应晶体管 (FeFET)
type: entity
status: mature
class: [transistor, memory-device]
properties: [non-volatile, ferroelectric-switching, CMOS-compatible]
papers: [chenHafniumBasedFerroelectricPostMoore2026, martinThinfilmFerroelectricMaterials2016, huangTwodimensionalIn2Se3Rising2022]
updated: 2026-08
---

# 铁电场效应晶体管 / Ferroelectric Field-Effect Transistor (FeFET)

铁电场效应晶体管 (FeFET) 是一种将铁电材料集成到常规场效应晶体管 (FET) 栅极堆叠中的三端非易失性存储器件。通过铁电层的极化状态来调制沟道的电导，从而实现信息的存储。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“铁电场效应晶体管”听着玄乎，其实就像咱家那把带“记忆”的电门。常规的电门是按下去就开，撒手或者断电可能就关了。但这个 FeFET 里的“铁电层”就像个听话的小管家，你用电压给它下一道命令（比如让它“极化”向上），它就像在那儿立了个永久的旗子。哪怕你把电压撤了，甚至把电源断了，那个旗子也还在那儿挡着或者引着水流（电流）。
> 
> 这样一来，只要看水流是大还是小，咱就能知道之前下的是啥命令。它最厉害的地方在于，它自己就能存住信息，不需要额外加个小本本（存储单元）记着，而且它跟现在盖大楼（芯片制造）的法子（CMOS工艺）特别合得来，是个能让手机和电脑更省电、记性更好的好宝贝。

## 🏗️ 结构概览

FeFET 的核心结构是将铁电薄膜（如 HZO）作为栅极绝缘层。常见的结构包括金属-铁电-半导体 (MFS) 和金属-铁电-金属-绝缘体-半导体 (MFMIS) 等堆叠方式。

![图：FeFET 器件结构示意图](../../raw/figures/chenHafniumBasedFerroelectricPostMoore2026/fig_4_L3JZI8BN.png)
*   **看图要点**：图中展示了 FeFET 的截面结构，铁电层（Ferroelectric layer）位于栅极电极下方，直接或通过缓冲层覆盖在半导体沟道（Channel）上。通过栅极电压切换铁电层的极化方向，可以无破坏性地读出沟道的电阻状态。
*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 物理机制与性能

### 极化调制机制
FeFET 的工作基于铁电极化对半导体沟道电荷分布的场效应调制。当铁电层向下极化时，它会在半导体表面诱导出相反电荷（如电子），降低阈值电压 ($V_{th}$)，使沟道处于高电导态（"1"）；反之则处于低电导态（"0"）。

### 铪基铁电的优势
传统的铁电材料（如 PZT）难以微缩且与硅工艺兼容性差。铪基铁电体（Hf-FEs）的发现解决了这一问题。它在纳米尺度下仍能保持强铁电性，且可以使用原子层沉积 (ALD) 工艺制备，非常适合后摩尔时代的集成。

### 关键性能参数
*   **开关比**：典型可达 $10^6$ 量级。
*   **存储窗口 (MW)**：通常在 1-2 V 左右。
*   **耐久性**：铪基 FeFET 仍面临唤醒与疲劳效应的挑战，典型寿命在 $10^4$-$10^9$ 次循环。

## 📚 相关论文 (Related Papers)

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：系统综述了铪基 FeFET 的器件物理与集成架构。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：讨论了薄膜铁电材料在电子器件中的应用背景。
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/polarization-switching|极化翻转]]
- [[../entities/HfO2|氧化铪 (HfO2)]]
- [[../entities/FTJ|铁电隧道结 (FTJ)]]
- [[../concepts/neuromorphic-computing|神经形态计算]]

| 属性 | 详情 |
| :--- | :--- |
| 器件类型 | 三端场效应晶体管 |
| 存储原理 | 极化调制阈值电压 |
| 典型材料 | HZO, HfO2, PZT |
| 主要优势 | 非破坏性读出、高速度、CMOS兼容 |
