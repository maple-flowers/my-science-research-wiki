---
tags: [entity, material, multiferroic, 2D, magnetic, spin-spiral]
category: [D01, Z02]
---

# 碘化镍 / Nickel Iodide (NiI2)

**NiI2** 是一种典型的二维范德华多铁材料。在单层极限下，它被证实为首个具有本征多铁性的纯二维体系，展现出巨大的磁电耦合效应 [[../papers/songEvidenceSinglelayerVan2022]]。

## 1. 单层多铁性机制
NiI2 的多铁性属于 **Type-II (磁感生) 多铁性**，其极化直接由复杂的磁有序驱动：
- **手性螺磁序 (Chiral Spin-spiral Order)**：在单层 NiI2 中，$Ni^{2+}$ 离子形成了蜂窝状晶格。由于竞争的磁交换作用，体系在低温下进入手性螺磁态。
- **对称性破缺**：这种螺磁序打破了空间反演对称性。根据自旋电流模型（Spin-current model），非共线的自旋排布结合 I 原子的强自旋轨道耦合 (SOC)，诱导产生了面内自旋极化。
- **转变温度**：实验测得单层 NiI2 的磁铁电转变温度 **$T_C \approx 21\text{ K}$** [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]。

## 2. 磁电耦合与原子尺度成像
- **巨磁电耦合**：极化方向与螺磁序的手性（旋向）直接挂钩。通过外磁场或电场，可以非易失性地同步翻转极化与磁手性。
- **扫描探针表征**：利用 AFM-PFM 及磁力显微镜技术，研究者已在原子尺度上可视化了单层 NiI2 的多铁畴结构 [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_C$)** | $\sim 21\text{ K}$ | 磁序与极化同步转变 |
| **磁序类型** | 手性螺磁序 | 非共线反铁磁 |
| **自旋轨道耦合** | 强 (来自 I 原子) | 驱动极化的关键 |
| **材料类别** | TMDs 衍生范德华材料 | 本征二维多铁标杆 |

## 4. 本库相关代表性论文
- [[../papers/songEvidenceSinglelayerVan2022]]：Nature 2022，首次实验证实单层 NiI2 的本征二维多铁性。
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]：Nature Nanotechnology 2024，原子尺度可视化 NiI2 多铁性。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：综述二维多铁性在原子级厚度下的极限行为。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：讨论 NiI2 在二维多铁存储器件中的应用潜力。

## 5. 关联概念与实体
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../concepts/magnetoelectric-coupling|磁电耦合 Magnetoelectric Coupling]]
- [[../concepts/2D-materials|二维材料 2D Materials]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
- [[../entities/CrI3|碘化铬 CrI3]] (对比体系：滑动铁电多铁)
- [[../entities/MnBi2Te4|MnBi2Te4]] (磁性拓扑绝缘体)
