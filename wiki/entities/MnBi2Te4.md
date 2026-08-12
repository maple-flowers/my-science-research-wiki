---
tags: [entity, material, topological-insulator, multiferroic, magnetic, vdW]
category: [D01, Z02]
---

# 硫碲化锰铋 / Manganese Bismuth Telluride (MnBi2Te4, MBT)

**MnBi2Te4 (MBT)** 是一种典型的本征磁性拓扑绝缘体，属于范德华层状材料。它在二维极限下展现出丰富的磁电耦合效应和量子化输运特性，是研究**量子反常霍尔效应 (QAHE)** 和**轴子绝缘体 (Axion Insulator)** 的标杆体系 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 1. 结构与磁序
- **晶体结构**：MBT 具有层状范德华结构，每一层是一个由七个原子层构成的七重层 (Septuple Layer, SL, $Te\text{-}Bi\text{-}Te\text{-}Mn\text{-}Te\text{-}Bi\text{-}Te$)。
- **层间磁序**：
  - **A型反铁磁 (A-type AFM)**：层内呈现强铁磁耦合，层间呈现反铁磁耦合。
  - **奇偶层效应**：在少层极限下，奇数层表现出净磁矩（铁磁性），而偶数层则表现出磁矩抵消（反铁磁性）。
- **滑动切换磁序**：在双层 MBT 中，通过层间的滑移（滑动铁电机制）可以打破空间反演对称性，从而实现磁序与拓扑态的电场切换 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 2. 拓扑物性与磁电耦合
- **量子反常霍尔效应 (QAHE)**：在单层或奇数层 MBT 薄膜中，磁性打破了时间反演对称性，使得材料在无外磁场下即可展现出量子化的霍尔电导 ($\sigma_{xy} = \pm e^2/h$)。
- **轴子绝缘体态**：在偶数层（AFM 序）中，如果满足一定的对称性限制，可诱导出具有非零轴子场（$\theta = \pi$）的拓扑态，展现出反常的磁电响应。
- **铁电 QAH 绝缘体**：四层 MBT 在滑动打破空间反演对称后，可演化为铁电 QAHE 态。此时，极化翻转能够直接逆转 AFM 自旋分布、Berry 曲率以及手性边缘态的手性 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_N$)** | $\sim 25\text{ K}$ | 块体反铁磁 Neel 温度 |
| **磁结构** | $A$-type AFM | 层间反平行排列 |
| **能隙 ($E_g$)** | $\sim 0.1\text{--}0.2\text{ eV}$ | 拓扑体能隙 |
| **霍尔电导 ($\sigma_{xy}$)** | $\pm e^2/h$ | 量子化边缘态 (少层) |
| **材料类别** | 磁性拓扑绝缘体 (vdW) | [[../entities/TMDs|TMDs]] 相关家族 |

## 4. 本库相关代表性论文
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：详述了 MBT 在滑动铁电机制驱动下的磁、电、拓扑耦合效应及其作为铁电 QAH 绝缘体的潜力。
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：利用光学手段探测 MBT 薄膜中的磁序演化与电子能带特征。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：讨论了原子级厚度下的磁性稳定性与铁电性共存。

## 5. 关联概念与实体
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/quantum-anomalous-hall-effect|量子反常霍尔效应 QAHE]]
- [[../entities/Bi2Te3|碲化铋 Bi2Te3]] (母体拓扑绝缘体)
- [[../projects/project-2-mn-multiferroics|Project-2]] (Mn 基磁性与多铁研究)
- [[../projects/project-7-cdw-charge-density-wave|Project-7]] (层间耦合与电荷密度波)
