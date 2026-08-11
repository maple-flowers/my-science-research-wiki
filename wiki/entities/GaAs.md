---
tags: [entity, material, semiconductor, 2D, III-V]
category: [D01, Z02]
---

# 砷化镓 / Gallium Arsenide (GaAs)

**GaAs** 是最著名的 III-V 族半导体之一，广泛应用于高频器件和光电子领域。在 2025 年的研究中，二维 GaAs 被选为验证“积木”组装理论和能量回归模型的典型案例 [[../../raw/note/yanDecipheringStabilityTwodimensional2025|Yan et al. 2025]]。

## 1. 结构预测与能量分解

二维 GaAs 的结构多样性可以通过基础构建块的线性叠加来描述：
- **回归分析模型**：GaAs 的总能量表现为四面体（Tetrahedron）、三角形（Triangle）和扭曲三角形构建块的线性组合，模型拟合优度 $R^2$ 达到 **0.95**。
- **稳定性贡献**：计算表明，四面体构建块对稳定性的贡献是三角形的 **2-3 倍**。
- **能量阶梯**：由于相同比例的构建块会产生相近的能量值，GaAs 的能量景观呈现出明显的“阶梯状”分布 [[../../raw/note/yanDecipheringStabilityTwodimensional2025|Yan et al. 2025]]。

## 2. 电子输运特性

在二维过渡结构（TT）下，GaAs 展现出优异的载流子迁移率：
- **空穴迁移率**：预测值达到 **$10^5 \text{ cm}^2 \text{ V}^{-1} \text{ s}^{-1}$** 数量级，远超其块体对应物。
- **物理机制**：虽然二维化导致有效质量增加，但由于**形变势常数 (Deformation potential constant)** 的大幅降低，声子散射被显著削弱，从而提升了迁移率。

## 3. 主要物性参数

| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **最稳构型** | TT (Transition structure) | 结合四面体与三角形 |
| **空穴迁移率** | $\sim 10^5 \text{ cm}^2 \text{ V}^{-1} \text{ s}^{-1}$ | 相比块体显著提升 |
| **能量回归 R²** | 0.95 | 证实了 LEGO 组装概念 |
| **材料类别** | III-V 族半导体 | 二维限域效应显著 |

## 4. 本库相关代表性论文
- [[../../raw/note/yanDecipheringStabilityTwodimensional2025|Yan et al. 2025]]：破译二维 III-V 半导体的稳定性：构建块及其多功能组装。
