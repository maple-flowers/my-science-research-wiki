---
tags: [entity, material, 2D, MXenes, multiferroicity, ferroelectricity]
category: [D02, Z01]
---

# 过渡金属碳/氮/碳氮化物 / MXenes

**MXenes** 是一种化学式为 $M_{n+1}X_n T_x$ 的二维过渡金属碳/氮化物家族（$M$ 为前过渡金属，$X$ 为 C 或 N，$T_x$ 为表面终止基团，如 -O, -F, -OH, -Cl）。主要通过从 MAX 相晶体中选择性刻蚀 A 层元素制备。

## 1. 物理特性与计算设计
### 1.1 高金属电导率
MXenes 具有类金属性的高电导率和亲水性表面，广泛应用于能量存储、电磁屏蔽及光电器件 [[../papers/naguib25thAnniversaryArticle2013a]]。其费米能级附近的电子态密度主要由 $M$ 原子的 $d$ 轨道贡献。

### 1.2 二维铁电性与多铁性预测
第一性原理计算预测，通过调控表面基团或利用多金属元素序，MXenes 可展现出本征二维铁性 [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：
- **完全补偿亚铁磁性 (Fully Compensated Ferrimagnetism)**：在 $\text{Cr}_2\text{TiC}_2$ 等单层中，预测存在磁矩完全抵消但具有自旋极化能带的物理态。
- **金属性铁电性**：自由立式 MXene 薄膜（如 $\text{Ti}_3\text{C}_2\text{T}_x$）被预测可保留金属导电性同时表现出极化翻转，在非挥发忆阻器及突触计算中展现出潜力。
- **半金属性切换**：在 $\text{Hf}_2\text{C}$ 等体系中，通过调控表面官能团的排布，可实现非易失的可切换半金属性 [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]。

## 2. 磁电耦合与轨道工程
- **3d 能级对称性**：MXenes 的磁性与电子输运特性深受过渡金属 $3d$ 轨道填充与配位环境的影响 [[../papers/chen3dLevelSymmetry2025]]。
- **高通量设计**：利用 DFT 结合主动学习，可高效筛选具有目标磁电响应的 MXene 衍生物。

## 3. 主要物性参数
| 参数项 | 描述 | 备注 |
| :--- | :--- | :--- |
| **电导率** | $\sim 10^4 \text{ S/cm}$ | 金属性特征 |
| **亲水性** | 高 | 适合溶液处理 |
| **稳定性** | 良好 | 依赖于表面 $T_x$ 保护 |
| **功能扩展** | 铁电、铁磁、超导 | 可通过功能化调控 |

## 4. 本库相关代表性论文
- [[../papers/naguib25thAnniversaryArticle2013a]]：Adv. Mater. 2013，MXenes 家族的奠基性综述。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：npj Comp. Mater. 2024，预测 MXene Hf2C 中的非挥发可切换半金属性。
- [[../papers/chen3dLevelSymmetry2025]]：讨论 3d 能级对称性在二维 MXene 磁性调控中的作用。
- [[../papers/khazaeiNovelElectronicMagnetic2013]]：Adv. Funct. Mater. 2013，早期对 MXenes 电子与磁学性质的预测。

## 5. 关联概念与实体
- [[../concepts/2D-materials|二维范德华材料 2D Materials]]
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
