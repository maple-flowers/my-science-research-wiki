---
tags: [concept, topological-physics, symmetry]
title: 时间反演对称性 / Time-Reversal Symmetry
type: concept
status: developing
domain: [condensed-matter-physics, topological-physics]
mechanism: 体系哈密顿量在时间倒转算符变换下的不变性
related_concepts: [topological-insulator, Z2-invariant, quantum-spin-hall-effect, weyl-semimetal, broken-inversion-symmetry]
papers: [pedramraziManipulatingTopologicalDomain2019, sharmaRoomtemperatureFerroelectricSemimetal2019, wangTunableD0Topological2025b, zhaoOpticalFingerprintsTwodimensional2024, RecentAdvancesGrowth2025]
updated: 2026-08
---

# 时间反演对称性 / Time-Reversal Symmetry

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


时间反演对称性 (Time-Reversal Symmetry, $\mathcal{T}$) 是指体系的物理规律（或哈密顿量）在时间方向倒转（即 $t \rightarrow -t$）的操作下保持不变的性质。在量子力学中，时间反演操作是一个反线性算符，它会将动量和自旋的方向反转。它是保护拓扑绝缘体和量子自旋霍尔效应中非耗散边缘态的基础。

## 👵 太奶导读

好孩子，这“时间反演对称性”说白了就是“电影倒着放，一切都还对得上”。
想象你拍了一段台球碰撞的视频（不考虑摩擦），然后把视频倒着放。你看着视频里台球倒着滚、撞在一起，也会觉得这符合物理规律，这就叫时间反演对称。
在微观世界里，电子自己不仅在跑，还在自转（自旋）。如果你把时间倒过来，电子不仅跑的方向反了，转的方向也反了（动量和自旋都反向）。
对于没有磁性的材料，这种倒转是非常完美的，所有的电子都能找到和自己正好反着来的伙伴（克拉默对），这就保护了拓扑绝缘体里的那些“高速公路”不发生堵车（背散射）。但如果你放块磁铁（引入铁磁性），这个对称性就被打破了。

## 🏗️ 结构概览

时间反演对称性要求能带在动量空间中满足 $\epsilon_n(k) = \epsilon_n(-k)$（无自旋-轨道耦合时）或特殊的克拉默简并。

![图：时间反演对称性保护下的 Kramers 简并能带](../../raw/figures/pedramraziManipulatingTopologicalDomain2019/fig_4_EMKKQ7YH.png)
*   **看图要点**：展示了具有时间反演对称性的 1T'-WSe₂ 在时间反演对称点处的能带简并（狄拉克交叉点）。
*   **来源**：[[../papers/pedramraziManipulatingTopologicalDomain2019]] -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]

## 🧩 克拉默定理与对称性破缺

*   **克拉默定理 (Kramers' Theorem)**：对于具有半整数自旋且满足时间反演对称性的系统，哈密顿量的每一个本征态都至少是双重简并的（即克拉默对，Kramers pair）。
*   **背散射抑制**：由于 $\mathcal{T}$ 的存在，量子自旋霍尔边缘态中自旋向上的向前运动电子无法被非磁性杂质散射成自旋向下的向后运动电子，因为这违反了时间反演下的概率守恒。
*   **对称性破缺**：引入磁性（如铁磁、反铁磁）会打破 $\mathcal{T}$，从而可能将拓扑绝缘体转变为外尔半金属或量子反常霍尔绝缘体。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 时间反演操作 T | 反转时间 | T²=-1（自旋 1/2） |
| 克拉默简并 | 无磁场下自旋简并 | SOC 下仍保持 |
| 破缺方式 | 外磁场/磁序 | 产生劈裂 |
| 拓扑作用 | Z2 保护 | 拓扑绝缘体根基 |
| 表征 | 磁化/自旋极化 | 判定 TRS 状态 |

## 🔀 近邻概念辨析

- **时间反演 vs 空间反演**：时间反演反转动量与自旋；空间反演反转位置。二者独立，破缺后果不同（磁性 vs 极化）。
- **时间反演 vs 磁性**：磁序/外磁场破缺时间反演，但不一定破缺空间反演；铁电反之。
- **TRS 保护 vs 拓扑**：Z2 拓扑需 TRS 存在；破坏 TRS（磁性掺杂）可将 TI 转为量子反常霍尔态。

## 📚 相关论文 (Related Papers)

- [[../papers/pedramraziManipulatingTopologicalDomain2019]]：1T'-WSe₂ 的拓扑边缘态受时间反演对称性保护。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：WTe₂ 保持时间反演对称但破缺空间反演。
- [[../papers/wangTunableD0Topological2025b]]：d0 铁磁性材料 In₂NO₂ 破缺了时间反演对称性。
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]
- [[../papers/RecentAdvancesGrowth2025]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/Z2-invariant|Z2 不变量]]（受时间反演对称性保护的拓扑指数）
- [[../concepts/quantum-spin-hall-effect|量子自旋霍尔效应]]（需要 $\mathcal{T}$ 保护）
- [[../concepts/broken-inversion-symmetry|破缺的空间反演对称性]]（常与 $\mathcal{T}$ 配合产生外尔半金属）
- [[../entities/WSe2|WSe₂]]（非磁性，满足 $\mathcal{T}$）
