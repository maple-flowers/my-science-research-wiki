---
name: electron-counting-rule
description: 判断半导体表面或二维结构稳定性的经验规则，要求成键轨道填满且反键轨道全空。
metadata:
  type: concept
---

# 电子计数规则 / Electron Counting Rule (ECR)

**电子计数规则** 是半导体物理与化学中判断表面重构及纳米结构稳定性的重要经验准则。在 2025 年关于二维 III-V 半导体的研究中，该规则被用来解释[[lego-assembly|“积木块”]]组装的化学本质 [[../papers/yanDecipheringStabilityTwodimensional2025|Yan et al. 2025]]。

## 1. 核心内容

一个稳定的半导体二维结构应满足：
- **电荷转移**：电子从电正性原子（如 III 族元素 M）转移到电负性原子（如 V 族元素 X）。
- **轨道填充**：所有成键态（Bonding states）被电子填满，而所有反键态（Anti-bonding states）以及阳离子的悬挂键轨道保持全空。

## 2. 在 III-V 族中的体现

- **三角形积木块**：III 族原子通过 $sp^2$ 杂化成键，其垂直平面的 $p$ 轨道为空，而 V 族原子的对应轨道被孤对电子占满，整体满足 ECR。
- **多功能组装**：通过调整四面体与三角形的比例，体系可以有效消除表面悬挂键带来的能量代价，实现更高的稳定性。

## 3. 相关概念
- [[lego-assembly|乐高式组装]]
- [[../entities/GaAs|GaAs]]
- [[../entities/GaSb|GaSb]]
