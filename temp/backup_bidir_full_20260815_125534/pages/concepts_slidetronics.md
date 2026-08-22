---
name: slidetronics
description: 利用层间滑动调控铁电、自旋、拓扑等物理性质的新兴二维电子学领域
type: concept
papers: [chenStrongSlidingFerroelectricity2024, wuSlidingFerroelectricity2D2021a]
---

# 滑移电子学 / Slidetronics

滑移电子学 (Slidetronics) 是一门新兴的二维材料电子学分支，其核心在于利用范德华层状材料之间的**层间平移滑动 (Interlayer Sliding)** 来调控其宏观物理性质，如铁电极化、自旋纹理、贝里曲率及超导态等。

## Grandma 👵 太奶导读

太奶，这个 **Slidetronics**（滑移电子学）名字洋气，但原理跟咱们以前那种老式的**推拉尺**（或者是带机关的化妆镜）差不多。
这种材料像是一本由极薄的磁性纸叠成的书。
以前的电脑芯片是靠搬动材料里的原子（这就像把书里的每一个字都重新写一遍，费劲得很）。
而滑移电子学是直接把这页纸轻轻地**平着一搓**（滑动）。这一“搓”，整页纸上的信息和电磁脾气全都变了。
科学家发现，这一“搓”的力量极小，但带来的变化特别大，能让芯片变得又快、又省电，还没那么容易发烫！

## 🏗️ 核心驱动：滑动驱动的对称性切换

滑移电子学的物理基础在于不同堆垛序（Stacking Order）之间能量极低且性质截然不同的转变路径。

![图：滑动调控极化与自旋的 TOC 概念图](../../raw/figures/chenStrongSlidingFerroelectricity2024/fig_0_WVFZMG6N.png)
*   **看图要点**：图中展示了通过沿 $b$ 轴的一步滑移，如何实现铁电极化 $\pm P$ 的翻转，以及随之而来的自旋纹理螺旋性的反转。这是滑移电子学中“一石二鸟”调控的典型案例。
*   **来源**：[[../papers/chenStrongSlidingFerroelectricity2024]] -> [[../figures/heterostructures-stacking|层间滑移机制]]

## 🧩 滑移电子学的功能应用

1.  **非易失性存储**：利用[[../concepts/sliding-ferroelectricity|滑动铁电性]]实现低功耗、高密度的 2D-FeFET 存储器。
2.  **贝里曲率记忆**：通过滑动翻转 Berry 曲率偶极子，实现非破坏性的非线性反常霍尔读出（如在 WTe₂ 中）。
3.  **自旋操控**：在强 SOC 的材料（如 HgI₂）中，滑动翻转可直接反转[[../concepts/rashba-effect|Rashba 场]]，用于无磁自旋场效应管。
4.  **莫尔铁电调控**：在扭转体系中，利用局域滑动形成周期性势能阱，捕获激子或诱导关联超导态。

## 📚 相关论文 (Related Papers)

- [[../papers/chenStrongSlidingFerroelectricity2024]]：将滑移电子学应用范围从铁电拓展到了自旋纹理调控。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：滑动铁电与滑移电子学的奠基性综述，提出了该领域的未来框架。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/interlayer-sliding|层间滑动]]
- [[../concepts/rashba-effect|Rashba 效应]]
- [[../concepts/moire-superlattice|莫尔超晶格]]
- [[../entities/WTe2|二碲化钨 (WTe₂)]]
- [[../entities/h-BN|六方氮化硼 (h-BN)]]
