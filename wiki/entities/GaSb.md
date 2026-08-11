---
tags: [entity, material, semiconductor, 2D, high-mobility, III-V]
category: [D01, Z02]
---

# 锑化镓 / Gallium Antimonide (GaSb)

**GaSb** 是一种传统的高性能 III-V 族半导体。在 2025 年的一项研究中，二维化的 GaSb 被预测具有超越石墨烯的超高空穴迁移率，成为下一代超高速电子器件的明星候选材料 [[../../raw/note/yanDecipheringStabilityTwodimensional2025|Yan et al. 2025]]。

## 1. 结构稳定性与“积木”组装

根据 Yan 等人的理论，二维 GaSb 的稳定性遵循 **“乐高式”组装 (LEGO-like assembly)** 规则：
- **最稳结构**：二维 GaSb 的基态被确定为 **双层蜂窝结构 (DLHC)**。
- **构建单元**：由四面体 (Tetrahedron) 和三角形 (Triangle) 构建块组成。四面体单元提供了主要的能量稳定性。
- **电子计数规则 (ECR)**：该结构通过电荷转移满足 ECR，消除了表面悬挂键导致的不稳定性。

![III-V材料结构演化图](../../raw/figures/yanDecipheringStabilityTwodimensional2025/fig_1_N9B2S7D4.png)
*图 1: 二维 III-V 材料从平面六角形到 DLHC、NB 等复杂结构的演化过程。摘自 [[../../raw/note/yanDecipheringStabilityTwodimensional2025|Yan et al. 2025]]*

## 2. 纪录级的载流子迁移率

二维 GaSb 在电子输运方面展现出惊人的性能：
- **空穴迁移率**：预测值高达 **$\sim 10^8 \text{ cm}^2 \text{ V}^{-1} \text{ s}^{-1}$**。
- **对比**：该数值比石墨烯（$2 \times 10^5$）高出三个数量级，比块体 GaSb 高出五个数量级。
- **物理机制**：极高的迁移率源于其极低的 **形变势常数 ($E_1 \approx 0.0037\text{ eV}$)**。这意味着价带顶 (VBM) 对晶格应变极不敏感，显著削弱了电声耦合作用（Electron-phonon coupling）。

## 3. 主要物性参数

| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **空穴迁移率** | $\sim 10^8 \text{ cm}^2 \text{ V}^{-1} \text{ s}^{-1}$ | 目前理论预测的纪录值 |
| **最稳构型** | DLHC | 双层蜂窝结构 |
| **形变势 ($E_{1y}$)** | $0.0037\text{ eV}$ | 极弱的声子散射 |
| **对称性** | 低对称性 (P2/m) | 稳定性与对称性折衷 |

## 4. 本库相关代表性论文
- [[../../raw/note/yanDecipheringStabilityTwodimensional2025|Yan et al. 2025]]：破译二维 III-V 半导体的稳定性：构建块及其多功能组装。
