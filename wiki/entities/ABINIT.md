---
title: ABINIT / 第一性原理计算软件
type: entity
tags: [software, DFT, plane-wave, pseudopotential]
category: [Z01]
---

# ABINIT / 第一性原理计算软件

**ABINIT** 是一个开源的平面波赝势 DFT 计算软件包，支持 norm-conserving 赝势、PAW 方法、含时密度泛函理论（TDDFT）和多体微扰理论（GW、BSE），广泛用于材料电子结构、声子谱和光学性质的计算。

## 核心功能

- **电子结构计算**：基于平面波基组和赝势方法计算能带、态密度和电荷密度。
- **声子计算**：通过 DFPT 计算声子色散和电子-声子耦合。
- **光学性质**：计算介电函数、吸收光谱等线性光学性质。

## 本库中的应用

- 用于 TMD 材料的化学键和电子结构分析 [[../papers/Li2013bonding]]。

## Related Papers

- [[../papers/Li2013bonding]]：TMD 化学键分析中的 ABINIT 计算

## 关联概念与实体

- [[../concepts/density-functional-theory|密度泛函理论]]
- [[../entities/VASP|VASP]]
- [[../entities/Quantum-ESPRESSO|Quantum ESPRESSO]]
