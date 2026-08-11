---
tags: [entity, material, semiconductor, 2D, high-mobility, III-V]
category: [D01, Z02]
---

# 锑化镓 / Gallium Antimonide (GaSb)

**GaSb** 是一种高性能 III-V 族半导体。在 2025 年的理论研究中，二维化的 GaSb 被预测具有超越石墨烯的超高空穴迁移率，成为下一代超高速电子器件的潜力材料 [[../papers/yanDecipheringStabilityTwodimensional2025]]。

## 1. 结构稳定性与“积木”组装
二维 GaSb 的稳定性遵循 **“乐高式”组装 (LEGO-like assembly)** 规则：
- **基态结构**：其最稳结构被确定为 **双层蜂窝结构 (DLHC)**，而非块体的闪锌矿相。
- **构建单元**：由四面体 (sp³) 和三角形 (sp²) 构建块组成。由于 Sb 的电负性较低，四面体单元在能量稳定性中占主导地位。
- **电子计数规则 (ECR)**：结构通过电荷转移满足 ECR，消除了表面悬挂键。

*图 1: 二维 III-V 材料结构从平面六角形到 DLHC、NB 等复杂结构的演化路线。图表来源：[[../papers/yanDecipheringStabilityTwodimensional2025]]*

## 2. 纪录级的载流子迁移率
二维 GaSb 在电子输运方面展现出惊人的理论性能：
- **空穴迁移率**：理论预测值高达 **$3.4 \times 10^8\text{ cm}^2\text{ V}^{-1}\text{ s}^{-1}$**（y 方向）。
- **对比分析**：这一数值比石墨烯（$2 \times 10^5$）高出三个数量级，目前位居二维半导体理论预测值的首位。
- **物理机制——轨道应变解耦**：
    - 极高迁移率源于极低的**形变势常数 ($E_1 \approx 0.0037\text{ eV}$)**。
    - 微观上，其价带顶 (VBM) 完全由 $p_x$ 轨道占据，对 $y$ 方向的单轴应变极不敏感。这种“轨道-应变解耦”机制导致了极弱的电声耦合作用 [[../papers/yanDecipheringStabilityTwodimensional2025]]。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **空穴迁移率** | $\sim 10^8\text{ cm}^2\text{ V}^{-1}\text{ s}^{-1}$ | 目前理论预测的最高纪录 |
| **最稳构型** | DLHC | 双层蜂窝结构 |
| **形变势 ($E_{1y}$)** | $0.0037\text{ eV}$ | 极弱声子散射的起源 |
| **对称性** | 低对称性 (P2/m) | 典型非层状材料二维化特征 |

## 4. 本库相关代表性论文
- [[../papers/yanDecipheringStabilityTwodimensional2025]]：Science Advances 2025，破译二维 III-V 半导体的稳定性：构建块及其多功能组装。
