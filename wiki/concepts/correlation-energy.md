---
tags: [concept]
title: '关联能 / Correlation Energy'
type: concept
status: developing
papers: ['perdewGeneralizedGradientApproximation1996a', 'kresseUltrasoftPseudopotentialsProjector1999c', 'vanvleckSurveyTheoryFerromagnetism1945']
updated: 2026-08-18
---

# 关联能 / Correlation Energy

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


关联能（correlation energy）指**电子运动中超出单粒子（平均场）近似的那部分相互作用能量**，是决定多电子体系（尤其强关联与磁性体系）基态性质的关键贡献。在密度泛函理论中，它由交换关联泛函（如 LDA、PBE、GGA、Hubbard U 修正）近似描述，是理解磁性、绝缘体-金属转变与强关联现象的核心概念。

## 👵 太奶导读

电子不是各过各的"单打独斗"，它们之间会"互相躲着走、互相推着走"——这种集体"人情往来"带来的能量修正就叫关联能。算材料时如果完全忽略它，很多绝缘体会被算成金属、磁体被算错磁矩。所以人们发明了 LDA、PBE、加 U 等"补丁"来补偿这笔账，补得准不准，直接决定算出来的材料对不对。

## 🧩 关联能的泛函描述

- **PBE 泛函**：简化 GGA 泛函 PBE 的所有参数均为基本物理常数、无经验参数，其对小分子原子化能的精度（平均绝对误差约 8 kcal/mol）与 PW91 相当、远优于 LSD，是关联能描述的现代标准（[[../papers/perdewGeneralizedGradientApproximation1996a|Perdew 1996]]）。
- **数值实现精度**：投影缀加波（PAW）方法能以接近超软赝势的成本实现与全电子方法相当的精度，为关联能计算提供可靠的基组框架（[[../papers/kresseUltrasoftPseudopotentialsProjector1999c|Kresse 1999]]）。

## 🧩 关联能与磁性理论

- **铁磁性的交换关联起源**：量子力学的交换作用是铁磁性的根本原因，成功解释了外斯分子场的起源；真实材料介于海森堡定域模型与斯托纳巡游模型之间（[[../papers/vanvleckSurveyTheoryFerromagnetism1945|Van Vleck 1945]]）——交换关联能的正确处理是描述这类体系的先决条件。
- **强关联修正**：对 NiO 等莫特绝缘体，需通过加 U（如 U=6.2 eV）修正关联能才能正确再现带隙与结合能（参见 [[../concepts/cohesive-energy|结合能]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]] — From ultrasoft pseudopotentials to the projector augmented-wave method
- [[../papers/perdewGeneralizedGradientApproximation1996a]] — Generalized Gradient Approximation Made Simple
- [[../papers/vanvleckSurveyTheoryFerromagnetism1945]] — A Survey of the Theory of Ferromagnetism

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/density-functional-theory|密度泛函理论]]：关联能近似的理论框架。
- [[../concepts/heisenberg-model|海森堡模型]]：关联交换作用的模型化。
- [[../concepts/ferromagnetism|铁磁性]]：交换关联能驱动的磁性序。
- [[../concepts/antiferromagnetism|反铁磁性]]：关联能修正的典型对象。
- [[../concepts/exchange-interaction|交换相互作用]]：关联能的核心物理来源。
- [[../concepts/magnetism|磁性]]：关联能影响的性质类别。
- [[../concepts/d0-rule|d⁰ 规则]]：铁电-磁性关联的电子组态判据。
- [[../concepts/pseudopotential|赝势]]：关联能计算的数值基础。
