---
tags: [entity, material, 2D, sliding-ferroelectricity, moire, graphene]
category: [D01, Z02]
---

# 多层石墨烯 / Multilayer Graphene (Graphene-tetralayer+)

多层石墨烯（特别是四层及以上）通过一种被称为**跨层滑动铁电性 (Across-Layer Sliding Ferroelectricity, ALSF)** 的机制，在纯单质体系中实现了铁电极化序。这一发现打破了“单质材料难以产生本征极化”的传统认知 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 1. 跨层滑动铁电性 (ALSF)
- **物理机制**：虽然单层和双层石墨烯任何形式的滑动都不会打破反演对称性，但从四层开始，特定的堆垛序（如 $ABAC$、$CABA$、$CBAB$）通过次近邻（非相邻层）的不对称耦合打破了空间反演对称性。
- **自发极化**：
  - **面外极化 ($P_{out}$)**：约为 **$0.21\text{ pC/m}$**。
  - **面内极化 ($P_{in}$)**：约为 **$57.49\text{ pC/m}$**，面内极化强度远高于面外分量。
- **超低翻转能垒**：滑动铁电态之间的翻转能垒极低（$< 5\text{ meV}$），允许利用极微弱的外电场进行极化操控。

## 2. 滑动莫尔铁电性 (Sliding Moiré Ferroelectricity)
- **转角石墨烯**：在具有小转角的四层石墨烯体系中，会出现周期性的铁电畴结构。
- **畴壁平移**：实验和模拟表明，通过施加面外电场，可以实现莫尔铁电畴壁的水平平移，从而切换局域的堆垛序和极化方向。这种“滑动莫尔铁电性”为构建超高密度存储（理论上限达 $10^4\text{ Tbit/in}^2$）提供了新思路 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **面外极化 ($P_{out}$)** | $\sim 0.2\text{ pC/m}$ | 四层 ABAC 堆垛 |
| **面内极化 ($P_{in}$)** | $\sim 57\text{ pC/m}$ | 显著的面内分量 |
| **翻转能垒** | $< 5\text{ meV}$ | 极易翻转 |
| **材料类别** | 单质范德华材料 | 跨层滑动铁电 |

## 4. 本库相关代表性论文
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：详述了四层及多层石墨烯中的 ALSF 机制、极性堆垛序以及滑动莫尔铁电性。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：讨论了石墨烯异质结中界面电荷对铁电极化的调制。

## 5. 关联概念与实体
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[../entities/graphene|石墨烯 Graphene]] (母体材料)
- [[../entities/h-BN|h-BN]] (构建异质结参考)
- [[../projects/project-5-snte-ferroelectric-sim|Project-5]] (多层体系计算方法参考)
