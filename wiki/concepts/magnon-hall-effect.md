---
tags: [concept, magnetism, transport]
title: 激磁子霍尔效应 / Magnon Hall Effect
type: concept
status: mature
domain: [condensed-matter-physics, transport]
mechanism: 由于贝里曲率的作用，激磁子（自旋波）在温度梯度下发生的横向偏转
related_concepts: [topological-magnon, spin-current, spin-orbit-coupling]
papers: [deSousa2008electrical, tanRevealingEmergentMagnetic2024, bhowalPolarMetalsPrinciples2023b]
updated: 2026-08
---

# 激磁子霍尔效应 / Magnon Hall Effect

激磁子霍尔效应 (Magnon Hall Effect) 指的是在磁性材料中，激磁子（自旋波）流在纵向温度梯度（热流）驱动下，发生横向偏移的现象。它是电子反常霍尔效应在绝缘磁体中的类比，其微观起源通常归功于激磁子能带的非平庸拓扑性质（贝里曲率）。

## 👵 太奶导读

乖孙，这“激磁子霍尔效应”就像是在磁铁内部吹起了一阵“歪风”。
本来你给磁铁一头加热，激磁子（就是磁性波浪）应该直勾勾地往冷的那头跑。
但因为材料里有一种叫“贝里曲率”的隐形推手，这些波浪跑着跑着就集体拐弯了，往侧面斜着冲过去。
这就像你在斜坡上滚球，结果球不往山下滚，反而横着跑。科学家们能通过测量这个“拐弯”的程度，算出材料里那些看不见的拓扑秘密，还能用来做那种不需要导线就能传热、传信息的精密器件。

## 🏗️ 结构概览：热流驱动下的自旋波偏转

![图：激磁子霍尔效应中的横向偏转示意](../../raw/figures/tanRevealingEmergentMagnetic2024/fig_1_A3L3NFIH.png)
*   **看图要点**：示意图展示了在温度梯度 $\nabla T$ 作用下，自旋波包由于受内部有效场作用而偏离直线路径。
*   **来源**：[[../papers/tanRevealingEmergentMagnetic2024]] -> [[../figures/experimental-setups]]
*(注：引用 Tan 2024 背景中关于拓扑输运的描述)*

## 🧩 物理机制

1.  **贝里曲率驱动**：激磁子波函数在动量空间的 Berry 曲率充当了“有效磁场”，产生洛伦兹力般的侧向推动力。
2.  **对称性要求**：通常需要破缺反演对称性或存在特定的 SOC 机制（如 DMI）。
3.  **观测手段**：通过测量热磁横向电势或利用布里渊区散射 (BLS) 光学成像。

## 📚 相关论文 (Related Papers)

- [[../papers/deSousa2008electrical]]：探讨了如何通过电场改变 BiFeO₃ 的磁结构从而调制激磁子传输特性。
- [[../papers/tanRevealingEmergentMagnetic2024]]：利用纳米级磁场探测手段研究手性体系中的拓扑输运。
- [[../papers/bhowalPolarMetalsPrinciples2023b]]：综述了极性材料中关联输运现象的对称性基础。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/topological-magnon|拓泊激磁子]]（机制载体）
- [[../concepts/spin-current|自旋流]]（宏观表现）
- [[../entities/CrI3|CrI₃]]（具有显著激磁子能带拓扑的二维材料）
- [[../entities/BiFeO3|BiFeO₃]]（磁电调控激磁子的样板体系）
