---
tags: [entity, material, TMD, 2D, Mott-insulator, CDW]
title: 二硫化钽 (TaS2) / Tantalum Disulfide
type: entity
status: mature
formula: TaS2
stoichiometry: 1T
class: [TMD, vdW, Mott-insulator]
properties: [charge-density-wave, Mott-transition, superconductivity]
related_entities: [1t-phase, NbSe2, VSe2]
papers: [nakataRobustChargedensityWave2021, CastroNeto2001charge, Koley2020charge, hallEnvironmentalControlCharge, chowdhuryReviewTheoreticalComputational]
updated: 2026-08
---

# 二硫化钽 (TaS2) / Tantalum Disulfide

二硫化钽 (TaS2) 尤其是其 $1\text{T}$ 相（1T-TaS2），是凝聚态物理中研究**莫特绝缘体 (Mott Insulator)** 与**电荷密度波 (CDW)** 强耦合行为的经典模本材料。它在低温下自发发生晶格畸变，将自由移动的金属电子锁死在局部超结构中，是“带宽控制型莫特相变”的典型代表。

## 👵 太奶导读

太奶啊，这 1T-TaS2 就像是一个设计巧妙的“电子蜂巢”。本来呢，这个材料是一条宽敞的马路，里面的电子（小蜜蜂）可以自由自在地流淌，这时候它是个导电的金属。可是温度一降下来，材料里的原子就会像列队一样，每 13 个原子抱成一个团，挤成一朵朵精致的“大卫之星”超大蜂巢。每个蜂巢中心只留出一个空位，因为电子之间互相嫌弃（强库仑排斥），一旦每个位置被占了一个，其他电子就再也进不去了，整条马路瞬间被堵死，金属就变成了完全不导电的莫特绝缘体。这就是物理上奇妙的“大卫之星锁定”。

## 🏗️ 结构概览

1T-TaS2 属于八面体配位的 1T 相（空间群 $P\bar{3}m1$）。在低温下，由于强烈的电声耦合，它会自发畸变形成 $\sqrt{13} \times \sqrt{13}$ 的“大卫之星 (Star-of-David)”超晶格。

![图：1T-TaS2 畸变形成的大卫之星超结构](../../raw/figures/nakataRobustChargedensityWave2021/fig_1_6T5AGUJF.png)
*   **看图要点**：图中展示了大卫之星超晶格的形成：每 13 个 Ta 原子（蓝色）向星团中心发生自发收缩。12 个过渡金属原子的最外层电子两两配对成键，而中心第 13 个原子上剩下一个半满的单电子，正是这个局域化的单电子在强关联作用下诱导了莫特能隙。
*   **来源**：[[../papers/nakataRobustChargedensityWave2021]] -> [[../figures/crystal-structures-bulk|晶体结构]]

## 🧩 CDW 驱动的莫特相变

1T-TaS2 具有复杂的变温相图，展现了多种 CDW 阶段：

1.  **无公度 CDW (ICCDW)**：高温下展现。
2.  **近公度 CDW (NCCDW)**：中温阶段。
3.  **完全公度 CDW (CCDW)**：在 $T < 180\text{ K}$ 时发生。此时大卫之星超结构完全锁定，电子动能带宽 $W$ 显著收缩。当有效库仑排斥能 $U$ 与带宽 $W$ 的比值 $U/W$ 超过临界值时，材料彻底转变为莫特绝缘体。
4.  **维度调控**：将 1T-TaS2 减薄至单层或通过外界蒸镀/静电掺杂，可以极大地重整其下哈伯德带（LHB），并有可能实现超导、极性金属甚至自旋液体态的可逆调控。

## 🔬 物理参数表

| 属性 | 数值 |
| :--- | :--- |
| CDW 周期结构 | $\sqrt{13} \times \sqrt{13}\ \text{R}13.9^\circ$ (13原子超胞) |
| Mott 转变温度 $T_{Mott}$ | 块体 $\sim 180\text{ K}$ (单层可提升至室温以上) |
| 莫特能隙 (Mott gap) | $\sim 0.1\text{--}0.2\text{ eV}$ |

## 📚 相关论文 (Related Papers)

- [[../papers/nakataRobustChargedensityWave2021]]：详细讨论了单层 1T-TMD 体系中电子关联和晶格畸变对莫特相稳定性的调控。
- [[../papers/CastroNeto2001charge]]：经典的 TMD CDW 物理综述。
- [[../papers/Koley2020charge]]
- [[../papers/hallEnvironmentalControlCharge]]
- [[../papers/chowdhuryReviewTheoreticalComputational]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波 (CDW)]]
- [[../concepts/mott-insulator|莫特绝缘体]]
- [[../concepts/star-of-david|大卫之星团簇]]
- [[../entities/1t-phase|1T 相]]
- [[../entities/NbSe2|二硒化铌 (NbSe2)]]
