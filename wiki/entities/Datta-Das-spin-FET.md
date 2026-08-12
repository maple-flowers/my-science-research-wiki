---
title: Datta-Das 自旋场效应晶体管 / Datta-Das Spin FET
type: entity
tags: [device, spintronics, spin-FET, Rashba-effect]
category: [D02]
---

# Datta-Das 自旋场效应晶体管 / Datta-Das Spin FET

**Datta-Das 自旋 FET** 是 1990 年 Datta 和 Das 提出的标志性自旋电子器件概念，利用 Rashba 自旋-轨道耦合效应通过栅压控制自旋进动，实现非易失逻辑开关。在本库中，基于铁电材料的 Datta-Das 自旋 FET 设计将铁电极化与自旋操控结合，拓展了滑移电子学的功能边界。

## 器件原理

- **自旋注入**：铁磁电极注入自旋极化电子进入半导体沟道。
- **Rashba 进动**：沟道中 Rashba 场使自旋进动，进动角 θ = αmL/ℏv_F，其中 αm 为 Rashba 系数，L 为沟道长度。
- **栅压控制**：栅压翻转铁电极化 → Rashba 场方向反转 → 进动角符号翻转 → 漏极自旋平行（ON）或反平行（OFF）于漏极磁化。
- **基于 FE-HgI₂ 双层**：沟道长度 143 nm 时进动角 θ = ±π/2，可实现完整开关 [[../papers/chenStrongSlidingFerroelectricity2024]]。

## Related Papers

- [[../papers/chenStrongSlidingFerroelectricity2024]]：基于 FE-HgI₂ 双层的 Datta-Das 自旋 FET 设计

## 关联概念与实体

- [[../concepts/rashba-effect|Rashba 效应]]
- [[../concepts/spin-texture|自旋纹理]]
- [[../concepts/spin-transport|自旋输运]]
- [[../entities/HgI2|碘化汞 HgI₂]]
