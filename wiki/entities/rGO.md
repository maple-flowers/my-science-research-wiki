---
tags: [entity]
---

# 还原氧化石墨烯 / rGO (Reduced Graphene Oxide)

还原氧化石墨烯（rGO）是氧化石墨烯（GO）经热、化学或激光处理去除部分含氧官能团后的产物。在 [[../concepts/2D-materials|二维铁电电子学]] 体系中，rGO 常作为柔性、高导电性的二维电极，用于构建全二维三明治结构的 [[resistive-switching-memory|忆阻器]]。

## 核心特性与 Phase-Locked 演化

### 1. 从绝缘到导电的演化过程
- **前驱体 GO**：具有丰富的含氧官能团（-OH, -O-, -COOH），表现为绝缘性，c 轴晶格常数较大（XRD 峰约在 11°）。
- **还原过程 (rGO/LSG)**：通过激光光热还原（Laser-Scribed/Reduced Graphene, LSG）或化学还原，含氧官能团大量脱除，sp² 杂化区域重新恢复，导电性急剧提升。在 XRD 上表现为 11° 峰消失，在 ~25° 出现宽化的石墨烯衍射峰 [[../papers/tahirFerroelectricityNonvolatileMemristor2025]]。

### 2. 作为二维电极的优势
- **界面稳定性**：与传统的金属电极（如 Ag, Cu）相比，rGO 电极能有效避免金属离子向活性层（如 [[MXenes]]）扩散，从而降低漏电流并提升循环耐久性。
- **机械柔韧性**：rGO 薄膜具有优异的柔性，可与自支撑的 MXene 薄膜结合构筑全柔性器件，满足可穿戴电子设备需求 [[../papers/sattarFunctionalizedDoubleTransition2025]]。

## 实验表征与判定依据

- **XPS 表征**：C 1s 谱图中 C–C/C=C 峰占比显著提升，而 C–O、C=O 等氧化峰强度大幅下降。
- **Raman 光谱**：呈现典型的 D 峰（~1350 cm⁻¹）与 G 峰（~1580 cm⁻¹），其强度比 $I_D/I_G$ 的变化反映了还原后缺陷分布与晶域尺寸的调整。

## 在忆阻器中的功能定位

在全二维忆阻器件（如 LSG/HT-Mo₂Ti₂C₃Tₓ/LSG）中：
1. **电极角色**：提供载流子注入，并作为导电细丝生长的物理边界。
2. **机理耦合**：配合铁电 MXene 的 [[../concepts/polarization-switching|极化翻转]]，rGO 电极界面的电荷俘获/去俘获过程参与调控阻变行为，影响 SET/RESET 电压的一致性 [[../papers/zahraCriticalAnalysisFerroelectric2025]]。

## 相关论文

- [[../papers/sattarFunctionalizedDoubleTransition2025]] — 探讨了激光还原石墨烯（LSG）作为电极在双过渡金属 MXene 忆阻器中的应用。
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]] — 对比了 Ti₃C₂Tₓ 与 rGO 两种二维电极对 Nb₂CTₓ 忆阻器导电机理的影响。
- [[../papers/zahraCriticalAnalysisFerroelectric2025]] — 综述了 rGO 在增强 MXene 基复合材料电学性能中的作用。

## 关联导航
- **上游概念**：[[../concepts/2D-materials]]
- **活性层协作**：[[MXenes]]、[[Mo2Ti2C3Tx]]、[[Nb2CTx]]
- **器件原型**：[[../figures/electronic-devices]]
