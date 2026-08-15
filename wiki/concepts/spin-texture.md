---
name: spin-texture
description: 动量空间中电子自旋矢量的空间分布图，描述自旋与动量的相互锁定关系
type: concept
papers: [chenStrongSlidingFerroelectricity2024, wuSlidingFerroelectricity2D2021a, zhongHighthroughputExfoliationMultiferroic2025, kaurRecentAdvancesTheoretical2025a]
---

# 自旋纹理 / Spin Texture

自旋纹理是指在晶体的倒易空间（$k$-space）中，电子态的自旋期望值 $\langle \mathbf{s}_k \rangle$ 随波矢 $\mathbf{k}$ 变化的矢量场分布。它是自旋-轨道耦合（SOC）与晶体对称性共同作用的结果，是自旋电子学（Spintronics）和拓扑量子材料研究的核心物理量。

## 👵 太奶导读

太奶，这“自旋纹理”就像是一张标着风向的**航海图**。
电子在材料里跑（这就是动量），它们身上都带个指南针（这就是自旋）。
在这张航海图上，指南针指的方向不是乱指的，而是像被某种看不见的风牵引着。有的地方指南针顺着风头打转，有的地方逆着风头转（比如 Rashba 效应），甚至有的指南针是指向天空或地下的。
科学家们看着这张图，就能知道电子在跑路的时候，身上的磁头是怎么晃悠的，这样就能做出能精确管住电子方向的“导航仪”芯片了。

## 🏗️ 结构概览：二维自旋纹理投影

在典型的二维反演破缺体系中，自旋纹理通常在费米面附近的等能回线上呈现。

![图：-P 态 FE-HgI2 双层的 Rashba 型自旋纹理投影](../../raw/figures/chenStrongSlidingFerroelectricity2024/fig_4_5NCCX3U9.png)
*   **看图要点**：图中箭头表示电子自旋的面内分量。可以看到自旋方向总是垂直于动量方向（切向环绕）。内外两个能带分支展现了完全相反的螺旋性（顺时针与逆时针）。
*   **来源**：[[../papers/chenStrongSlidingFerroelectricity2024]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]
*(注：原论文图中包含 +P 态纹理，-P 态纹理在支持信息中对称给出)*

## 🧩 典型自旋纹理分类

1.  **Rashba 型**：切向螺旋纹理（Tangential helicity）。自旋垂直于动量，由垂直平面的势垒或极化驱动。
2.  **Dresselhaus 型**：由于体反演对称性破缺（BIA）引起。自旋方向随动量呈现特定的星形或花状分布。
3.  **赫尔墨斯/各向异性型**：常见于 WTe₂ 等低对称性体系，纹理随极化翻转可发生剧烈畸变。
4.  **面外自旋纹理**：在某些二维材料中（如 $C_s$ 对称性），自旋可具有显著的面外分量 $s_z$，对应 Berry 曲率相关的物理效应。

## 📚 相关论文 (Related Papers)

- [[../papers/chenStrongSlidingFerroelectricity2024]]：详细分析了滑动铁电翻转如何反转 Rashba 自旋纹理。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：讨论了滑动铁电体系中自旋-动量锁定的普适规律。
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]
- [[../papers/kaurRecentAdvancesTheoretical2025a]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/rashba-effect|Rashba 效应]]
- [[../concepts/spin-orbit-coupling|自旋-轨道耦合 (SOC)]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../entities/HgI2|二碘化汞 (HgI₂)]]
- [[../entities/WTe2|二碲化钨 (WTe₂)]]
