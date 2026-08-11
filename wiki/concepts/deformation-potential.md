---
name: deformation-potential
description: 描述载流子与声子相互作用强弱的物理量，衡量能带边缘对晶格形变的敏感程度。
metadata:
  type: concept
---

# 形变势 / Deformation Potential ($E_1$)

**形变势** 是半导体物理中衡量电子-声子耦合强度的关键物理量。它直接决定了材料的载流子迁移率，尤其是在声学声子散射占主导的二维材料中 [[../../raw/note/yanDecipheringStabilityTwodimensional2025|Yan et al. 2025]]。

## 1. 定义与公式

形变势常数定义为能带边缘（CBM 或 VBM）能量随晶格应变的线性变化率：
$$E_1 = \frac{\Delta E}{\Delta \epsilon}$$

在二维材料迁移率公式中，迁移率 $\mu$ 与形变势的平方成反比：
$$\mu \propto \frac{1}{E_1^2}$$

## 2. 二维化效应

在 Yan 等人的研究中，二维 III-V 半导体展现出远超块体的迁移率，其核心机制在于**形变势的大幅降低**：
- **纪录值**：在 [[../../entities/GaSb|GaSb]] 的 TT 结构中，空穴形变势降低至约 **0.0037 eV**。
- **物理机制**：二维化改变了波函数的对称性，使得特定方向的应变对能带边缘的影响极小，从而抑制了声子散射。

## 3. 相关实体
- [[../../entities/GaSb|GaSb (极低形变势案例)]]
- [[../../entities/BAs|BAs]]

## 4. 相关概念
- [[lego-assembly|乐高式组装]]
- [[strain-engineering|应变工程]]
