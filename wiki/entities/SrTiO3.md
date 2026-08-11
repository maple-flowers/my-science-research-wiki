---
tags: [entity, material, paraelectric, substrate, perovskite]
category: [D02, Z01]
---

# 钛酸锶 / Strontium Titanate (SrTiO3, STO)

**SrTiO3 (STO)** 是一种具有钙钛矿结构的典型**量子顺电体 (Quantum Paraelectric)**。作为氧化物电子学中的“金标准”衬底和功能层，它不仅在物理特性上表现出丰富的相变行为（如低温下的量子涨落抑制铁电相变），更是构建极性拓扑织构、实现超薄膜铁电性以及探索界面二维电子气 (2DEG) 的核心平台。

## 1. 物理特性：量子顺电性与高介电响应
- **量子波动与铁电抑制**：在本体态下，STO 随着温度降低，介电常数遵循居里-外斯定律上升。然而，在接近绝对零度时，晶格的量子涨落抑制了软模（Soft Mode）的冻结，使其终身保持顺电相而不发生铁电相变。
- **巨介电常数**：在低温（< 10 K）下，其相对介电常数可飙升至 $10^4$ 量级，且对微小的电场、应变或化学掺杂极其敏感。

## 2. 异质结中的核心作用：去极化场与极性拓扑
在 **[[../entities/PbTiO3|PbTiO3 (PTO)]] / STO** 或 **[[../entities/BaTiO3|BaTiO3 (BTO)]] / STO** 异质体系中，STO 承担着关键的物理角色：
- **引入去极化场 (Depolarization Field)**：由于 STO 是顺电绝缘体，在铁电/顺电超晶格中，由于界面束缚电荷未被完全屏蔽，会在铁电层中引入巨大的去极化场 [[../papers/junqueraCriticalThicknessFerroelectricity2003]]。
- **驱动极化连续旋转**：这种静电能的竞争促使极化矢量从面外方向旋转，从而在超晶格中稳定出**[[../concepts/polar-vortex|极性涡旋 (Polar Vortex)]]**、**[[../concepts/polar-skyrmion|极性斯格明子 (Polar Skyrmion)]]** 等拓扑织构 [[../papers/hanPolarTopologicalMaterials2025]]。
- **违反 Kittel 定律**：在极薄极限下，STO 夹层的存在使得斯格明子的周期-厚度关系偏离经典的 $d \propto \sqrt{h}$ 规律，转而遵循双曲标度律 [[../papers/gongAbsenceCriticalThickness2023]]。

## 3. 应变工程与维度调控
- **应变诱导铁电性**：通过外延应变（如生长在晶格常数较小的衬底上），可以打破 STO 的中心对称性，诱导出室温铁电性 [[../papers/martinThinfilmFerroelectricMaterials2016]]。这在 **[[../entities/SrMnO3|SrMnO3]]** 等相似钙钛矿体系中也被广泛研究 [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]。
- **自支撑 (Freestanding) 膜与拓扑态**：在自支撑的 STO 膜中，利用褶皱或弯曲产生的**应变梯度**（[[../concepts/flexoelectricity|挠曲电效应]]），可以稳定产生极性半子 (Meron) 和迷宫畴，实现非极性材料向极性拓扑态的转化 [[../papers/hanPolarTopologicalMaterials2025]]。

## 4. 电子学与自旋轨道耦合
- **相锁定 (Phase-locked) 调控**：在新型二维氧化物单层设计中，STO 及其衍生物被预测可作为研究**巨自旋劈裂**和**半金属态**的候选平台，通过微小应变即可实现电子-自旋特性的协同调控 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。

## 5. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_C$)** | 0 K | 本征态不发生铁电相变；应变下可升至室温 |
| **晶格常数 ($a$)** | $3.905\text{ \AA}$ | 氧化物外延的“金标准”参考值 |
| **带隙 ($E_g$)** | $\sim 3.2\text{ eV}$ | 宽禁带绝缘体 |
| **结构对称性** | 立方钙钛矿 ($Pm\bar{3}m$) | 105 K 以下发生反铁畸变相变 ($I4/mcm$) |

## 6. 本库相关代表性论文
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]：确立了 STO 界面去极化场导致铁电临界厚度的静电学图像。
- [[../papers/gongAbsenceCriticalThickness2023]]：揭示了 PTO/STO 超晶格中极性斯格明子违反 Kittel 定律的机制。
- [[../papers/hanPolarTopologicalMaterials2025]]：系统综述了基于 STO 异质结的极性拓扑设计原理及多场操控。
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：探讨了钙钛矿氧化物（含 STO 衍生物）在二维极限下的相锁定物性调控。
- [[../papers/Chen2016electrical]]：展示了以 STO 为衬底生长的 BiFeO3 薄膜的电-机械极化开关。

## 7. 关联概念与实体
- **概念**：[[../concepts/depolarizing-field|去极化场]]、[[../concepts/polar-skyrmion|极性斯格明子]]、[[../concepts/flexoelectricity|挠曲电效应]]、[[../concepts/strain-engineering|应变工程]]
- **实体**：[[../entities/PbTiO3|钛酸铅 (PTO)]]、[[../entities/BaTiO3|钛酸钡 (BTO)]]、[[../entities/BiFeO3|铁酸铋 (BFO)]]、[[../entities/SrRuO3|钌酸锶 (SRO)]]
