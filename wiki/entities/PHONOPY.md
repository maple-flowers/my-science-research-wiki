---
title: PHONOPY / 声子计算软件
type: entity
tags: [software, phonon, lattice-dynamics, DFT]
category: [Z01]
---

# PHONOPY / 声子计算软件

**PHONOPY** 是一个开源声子计算软件包，通过与 VASP、Quantum ESPRESSO 等 DFT 代码接口，使用超胞方法计算声子色散、声子态密度和热力学性质，是计算材料学中验证结构动力学稳定性的标准工具。

## 核心功能

- **声子色散**：通过有限位移法或密度泛函微扰理论（DFPT）计算完整布里渊区声子色散。
- **动力学稳定性验证**：检查声子谱中是否存在虚频（imaginary modes），判断结构是否动力学稳定。
- **热力学性质**：从声子谱推导自由能、熵、比热等温度依赖性质。

## 本库中的应用

- 用于验证铁电畴壁结构的动力学稳定性 [[../papers/gomez-ortizKittelLawDomain2023]]。
- 用于验证极性相结构的声子谱 [[../papers/huangPolarPhaseDomain2019]]。

## Related Papers

- [[../papers/gomez-ortizKittelLawDomain2023]]：畴壁 Kittel 律验证中的声子计算
- [[../papers/huangPolarPhaseDomain2019]]：极性畴相的声子稳定性验证

## 关联概念与实体

- [[../concepts/soft-mode-theory|软模理论]]
- [[../concepts/soft-phonon-mode|软声子模式]]
- [[../entities/VASP|VASP]]
