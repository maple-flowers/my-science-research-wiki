---
tags: [entity, material, semiconductor, 2D, III-V, high-mobility]
category: [D01, Z02]
---

# 砷化硼 / Boron Arsenide (BAs)

**BAs** 是一种具有极高热导率（Bulk 态达 $1300\text{ W/(m}\cdot\text{K)}$）和卓越迁移率的新兴 III-V 族半导体。在二维极限下，其结构稳定性和输运性能展现出超越传统层状材料的潜力。

## 1. 二维稳定性与“积木”组装理论
二维 BAs 的稳定性不再遵循石墨烯的高对称性直觉，而是遵循**电子计数规则 (ECR)** 和**积木块 (Building Block) 组装**法则：
- **TT (Transition structure) 基态**：通过高通量计算与机器学习发现，二维 BAs 的最稳构型为 TT 相（矩形对称，每个晶胞 4B+4As）。
- **混合杂化机制**：该结构由表面 $sp^2$ 杂化的三角形单元和内部 $sp^3$ 杂化的四面体单元组装而成。$As$ 原子的引入作为“柔性胶水”提供了关键的能量稳定性 [[../papers/yanDecipheringStabilityTwodimensional2025]]。
- **热稳定性**：300 K 下的 AIMD 模拟证实 TT-BAs 在动力学上是稳定的。

## 2. 卓越的载流子迁移率
TT-BAs 在二维化后展现出惊人的空穴和电子迁移率：
- **量级提升**：其空穴和电子迁移率均可达到 **$10^5\text{ cm}^2\text{ V}^{-1}\text{ s}^{-1}$**，部分方向甚至超过石墨烯 [[../papers/yanDecipheringStabilityTwodimensional2025]]。
- **物理机理（轨道-应变解耦）**：迁移率的飙升并非源于有效质量的减小，而是源于**形变势常数 ($E_1$)** 的显著降低。例如在类似体系 TT-GaSb 中，VBM 完全由 $p_x$ 轨道占据，对 $y$ 方向单轴应变极不敏感，导致极弱的电声耦合（$\mu \propto 1/E_1^2$）。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **最稳构型 (2D)** | TT 相 | 四面体-三角形混合相 |
| **载流子迁移率** | $\sim 10^5\text{ cm}^2\text{ V}^{-1}\text{ s}^{-1}$ | 远超块体对应物 |
| **热导率 (Bulk)** | $\sim 1300\text{ W/(m}\cdot\text{K)}$ | 仅次于金刚石 |
| **材料类别** | III-V 族半导体 | 非层状块体二维化典型 |

## 4. 本库相关代表性论文
- [[../papers/yanDecipheringStabilityTwodimensional2025]]：利用高通量计算与机器学习揭示二维 BAs 的稳定性规律与超高迁移率机制。

## 5. 关联概念与实体
- [[../concepts/2D-materials|二维材料 2D Materials]]
- [[../concepts/carrier-mobility|载流子迁移率 Carrier Mobility]]
- [[../concepts/lego-assembly|积木组装 LEGO-like Assembly]]
- [[../entities/GaAs|砷化家 GaAs]] (同族半导体对比)
- [[../entities/h-BN|氮化硼 h-BN]] (同族宽禁带对比)
