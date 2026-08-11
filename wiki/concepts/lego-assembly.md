---
name: lego-assembly
description: 二维 III-V 半导体的结构演化规律，由四面体、三角形和扭曲三角形构建块灵活组装而成。
metadata:
  type: concept
---

# 乐高式组装 / LEGO-like Assembly

**乐高式组装** 是由 Yan 等人提出的一种描述二维非层状 III-V 族半导体结构稳定性的理论模型。该模型认为，这些材料的复杂二维结构可以解构为少数几种基础“积木块”的有序排列 [[../papers/yanDecipheringStabilityTwodimensional2025|Yan et al. 2025]]。

## 1. 基础构建块 (Building Blocks)

通过机器学习 (DBSCAN 聚类) 识别出三种核心单元：
- **四面体 (Tetrahedron)**：对应 $sp^3$ 杂化，键角 $\sim 109.5^\circ$。
- **三角形 (Triangle)**：对应 $sp^2$ 杂化，键角 $\sim 120^\circ$。
- **扭曲三角形 (Distorted Triangle)**：介于两者之间的过渡形态。

## 2. 能量加和规则

该理论的核心贡献在于量化了稳定性的来源。回归分析表明，二维 III-V 结构的能量表现为其构建块能量的线性叠加：
$$E_{total} = \sum (n_i \cdot E_{block, i})$$

- **稳定性贡献**：四面体单元对能量稳定性的贡献通常是三角形单元的 **2-3 倍**。
- **能量阶梯**：具有相同比例构建块的不同异构体往往具有相近的能量，在能量分布图上呈现明显的“阶梯状”。

## 3. 应用：TT 结构

基于该理论预测的 **TT (Transition structure)** 构型：
- **构成**：结合了四面体与三角形构建块。
- **性能**：在多种 III-V 材料中被证明比以往预测的平面六角形更稳，且在 [[../../entities/GaSb|GaSb]] 中实现了纪录级的迁移率。

## 4. 相关实体
- [[../../entities/GaAs|GaAs]]
- [[../../entities/GaSb|GaSb]]
- [[../../entities/BAs|BAs]]
- [[../../entities/InSb|InSb]]

## 5. 相关概念
- [[electron-counting-rule|电子计数规则 (ECR)]]
- [[deformation-potential|形变势 (与迁移率提升相关)]]
