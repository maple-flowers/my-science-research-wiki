---
tags: [entity, material, 2D, ferroelectric, vdW]
category: [D02, Z01]
---

# 硫磷酸铜铟 / Copper Indium Thiophosphate (CuInP2S6, CIPS)

**CuInP2S6 (CIPS)** 是一种典型的二维范德华铁电材料。它因其在原子级厚度下仍能保持稳健的面外铁电性而备受关注，是研究二维极限下**位移型铁电性**的代表体系。

## 1. 二维面外铁电性
- **稳健极化**：CIPS 的单层及薄层在室温下表现出显著的面外自发极化。
- **物理起源**：其铁电性源于 $Cu$ 和 $In$ 阳离子在双角锥/八面体间隙中的协同位移。
- **临界厚度**：实验证实，CIPS 在低至 **$2\text{ nm}$**（约 3 个单位层）厚度时仍能通过 PFM 观测到清晰的铁电翻转迟滞回线 [[../papers/FerroelectricityMultiferroicityAtomic2023]]。

## 2. 负纵向压电效应 (Negative Longitudinal Piezoelectricity)
CIPS 展现出反常的**负 $d_{33}$** 压电响应，即在垂直电场下，材料会沿极化方向收缩而非膨胀。这种效应与其范德华层间耦合及 $Cu$ 离子的亚点阵移动机制密切相关。

## 3. 多场调控与异质结
- **应变调控**：通过面内应变可以显著调节 CIPS 的极化强度和转变温度 [[../papers/gaoStrainEngineeringFerroelectric2024]]。
- **莫尔超晶格**：将 CIPS 与其他二维材料（如 GeS2）构成转角异质结，可产生复杂的位移-滑动耦合铁电态，实现超高密度（$\sim 0.7\text{ TB/cm}^2$）的极化存储阵列 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 4. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_C$)** | $\sim 315\text{ K}$ | 块体室温铁电 |
| **自发极化 ($P_{out}$)** | $\sim 2\text{--}5\text{ \mu C/cm}^2$ | 典型面外极化 |
| **压电系数 ($d_{33}$)** | 负值 | 反常压电响应 |
| **材料类别** | 金属磷硫化物 (MPS3) 家族 | 范德华铁电体 |

## 5. 本库相关代表性论文
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：综述原子级厚度 CIPS 的铁电与多铁特性。
- [[../papers/gaoStrainEngineeringFerroelectric2024]]：讨论应变对 CIPS 极化翻转动力学的影响。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：理论预测 CIPS/GeS2 莫尔系统中的高密度存储潜力。

## 6. 关联概念与实体
- [[../concepts/2D-materials|二维材料 2D Materials]]
- [[../concepts/polarization-switching|极化翻转 Polarization Switching]]
- [[../concepts/moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[../entities/SnS|硫化锡 SnS]] (对比体系：面内铁电)
- [[../entities/In2Se3|硒化铟 In2Se3]] (对比体系：面内/面外耦合)
