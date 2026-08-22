---
tags: [concept, magnetoelectric-coupling, symmetry-analysis, multiferroicity]
title: 磁电多极子 / Magnetoelectric Multipoles
type: concept
status: mature
domain: [magnetoelectric-coupling, symmetry-analysis, multiferroicity]
mechanism: 将磁电张量 α_ij 展开为磁单极、磁偶极（环电流矩/环面矩）与磁四极等对称化多极子，用于在微观（原子/键）层面解析磁电耦合的来源与空间对称性
related_concepts: [magnetoelectric-coupling, multiferroicity, spin-orbit-coupling, magnetic-phase-transition, dzyaloshinskii-moriya-interaction]
papers: [spaldinAdvancesMagnetoelectricMultiferroics2019]
updated: 2026-08
---

# 磁电多极子 / Magnetoelectric Multipoles

磁电多极子（magnetoelectric multipoles）指**将磁电耦合张量按对称化多极展开得到的磁单极、磁偶极（含环电流矩）与磁四极等结构单元**。该框架由 Spaldin 等引入，用于在原子与键尺度解析"哪些局域磁/电荷构型贡献磁电响应"以及它们如何受空间对称性约束，是多铁与磁电材料对称性分析与第一性原理诊断的标准工具。

## 👵 太奶导读

太奶啊，磁电材料里"磁"和"电"会互相影响，但这种影响从哪儿来、长什么样？科学家把它拆成几块"积木"来分析：像圆点一样的磁单极、像小圆圈电流一样的磁偶极（环电流矩）、像十字花一样的磁四极。这些"积木"的摆放方式（对称性）决定了材料里磁电耦合强不强、能不能用。这就像分析一个复杂的舞蹈动作——先拆成一个个基本舞步。

## 🧩 核心内容与机制 (Core Content)

- **磁电张量与多极展开**：线性磁电响应 $P_i = \alpha_{ij} H_j$ 中的张量 $\alpha$ 可按对称性分解，其非零分量与体系磁空间群相关。多极展开将微观电荷/磁矩分布组织为磁单极（monopole）、磁偶极（dipole，含环电流矩 toroidal moment）与磁四极（quadrupole）。
- **磁单极**：与电荷密度的磁对称相关项，贡献各向同性磁电响应，常出现在自旋轨道耦合强或磁性离子配位特殊的体系。
- **磁偶极（环电流矩）**：由环状自旋流/轨道流产生，是许多磁电与多铁材料响应的核心贡献者，与手性自旋结构（[[../concepts/helical-magnetism|螺旋磁序]]）相关。
- **磁四极**：描述磁矩的角分布，与轨道序、磁性离子的晶体场分布相关。
- **对称性分析与计算**：多极子框架与群论结合，可在第一性原理中定量分解磁电耦合，指导新材料设计；BiFeO₃ 等室温多铁中的磁电响应可据此诊断 [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]。

## 📊 磁电多极子一览

| 多极子阶 | 名称 | 微观构型 | 典型贡献 |
|----------|------|----------|----------|
| 0 | 磁单极 | 各向同性磁荷分布 | 各向同性磁电项 |
| 1 | 磁偶极 / 环电流矩 | 环状自旋/轨道流 | 手性磁电响应 |
| 2 | 磁四极 | 角分布四极图案 | 轨道序磁电项 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/magnetoelectric-coupling|磁电耦合]]：磁电多极子描述的宏观量。
- [[../concepts/multiferroicity|多铁性]]：磁电多极子的宿主体系。
- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：磁电多极子的微观来源。
- [[../concepts/helical-magnetism|螺旋磁序]]：环电流矩产生的磁序背景。
- [[../concepts/magnetic-phase-transition|磁相变]]：磁电多极子随磁序变化。
- [[../entities/BiFeO3|BiFeO₃]]：磁电响应诊断的模型材料。

## 📚 相关论文 (Related Papers)

- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：多铁家族树综述，系统阐述磁电多极子分析框架及其在对称性诊断中的应用。

## 🏷️ 专业名词别名

- `magnetoelectric-multipolar`（concepts）
- `环电流矩展开`（concepts）
