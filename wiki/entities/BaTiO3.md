---
tags: [entity, material, ferroelectric, perovskite]
category: [D02, Z01]
---

# 钛酸钡 / Barium Titanate (BaTiO3, BTO)

**BaTiO3 (BTO)** 是最经典的位移型铁电体原型，也是首个发现的氧化物铁电材料。它在铁电物理研究中具有基石地位，是理解 $d^0$ 规则、临界厚度效应以及极性拓扑结构的标杆体系。

## 1. 铁电机制与 $d^0$ 规则
- **位移型铁电性**：BTO 的铁电性源于立方相向四方相转变时，中心 $Ti^{4+}$ 离子相对于氧八面体中心发生偏心位移。
- **$d^0$ 规则原型**：$Ti^{4+}$ 的 $3d^0$ 构型使得 $Ti$ $3d$ 轨道与 $O$ $2p$ 轨道能发生强烈的共价杂化，从而驱动自发极化。这是典型的“$d^0$ 铁电性”，与磁性（需 $d$ 电子填充）在本质上存在化学矛盾 [[../papers/hillWhyAreThere2000a]]。

## 2. 尺寸效应与临界厚度
- **去极化场限制**：在超薄膜极限下，BTO 的极化受界面去极化场（Depolarization Field）的强烈压制。
- **理论临界厚度**：第一性原理超胞计算（SRO/BTO/SRO 构型）证明，由于电极屏蔽不完全，BTO 在厚度低于 **~2.4 nm**（约 6 个晶胞）时将丧失铁电性，转为顺电态 [[../papers/junqueraCriticalThicknessFerroelectricity2003]]。

## 3. 极性拓扑结构 (Polar Topology)
- **早期预测**：2003 年，Bellaiche 等人利用有效哈密顿量方法，首次在 BTO 纳米点中预言了极化矢量绕核连续旋转形成的**极性涡旋 (Polar Vortex)**。
- **实验观测**：在 BTO 薄膜及异质结中，研究者已观测到通量闭合畴（Flux-closure domains）等拓扑序织构 [[../papers/hanPolarTopologicalMaterials2025]]。

## 4. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_C$)** | $\sim 393\text{ K}$ | 立方-四方相变 |
| **自发极化 ($P_s$)** | $26\text{ \mu C/cm}^2$ | Bulk 值 |
| **临界厚度** | $\sim 2.4\text{ nm}$ | SRO 电极屏蔽极限 |
| **材料类别** | $ABO_3$ 钙钛矿 | 位移型铁电标杆 |

## 5. 本库相关代表性论文
- [[../papers/hillWhyAreThere2000a]]：定义 $d^0$ 规则，将 BTO 作为磁电排斥性的参考原型。
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]：Nature 2003 奠基性工作，确立超薄 BTO 的临界厚度极限。
- [[../papers/hanPolarTopologicalMaterials2025]]：综述 BTO 及其衍生物中的极性拓扑结构与器件应用。

## 6. 关联概念与实体
- [[../concepts/ferroelectricity|铁电性 Ferroelectricity]]
- [[../concepts/depolarizing-field|去极化场 Depolarizing Field]]
- [[../concepts/critical-thickness|临界厚度 Critical Thickness]]
- [[../entities/SrTiO3|钛酸锶 SrTiO3]] (常用衬底/参考)
- [[../entities/PbTiO3|钛酸铅 PbTiO3]] (强极化对比)
- [[../entities/BiFeO3|铁酸铋 BiFeO3]] (室温多铁扩展)
