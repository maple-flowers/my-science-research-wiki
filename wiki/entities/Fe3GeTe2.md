---
tags: [entity, material, 2D, Fe3GeTe2, sliding-ferroelectricity, multiferroic]
category: [D02, Z01]
---

# 铁锗碲 / Fe3GeTe2 (FGT)

**Fe3GeTe2 (FGT)** 是一种具有强垂直磁异向性（PMA）的金属性二维范德华铁磁材料。其晶体结构由 $\text{Fe}_3\text{Ge}$ 原子层被两个 $\text{Te}$ 原子层包覆构成，单层属于 $P6_3/mmc$ 空间群。它是目前二维自旋电子学领域最受关注的体系之一。

## 1. 核心物理特性
- **本征铁磁性**：单层 FGT 具有稳健的铁磁序，居里温度 $T_C \sim 130\text{--}220\text{ K}$。
- **电学调控**：通过离子液体栅压调控（Ionic Liquid Gating），其 $T_C$ 可有效提升至室温（$300\text{ K}$）以上。
- **拓扑磁性**：在小角度扭转或异质结中，FGT 展现出非平庸的拓扑磁结构（如斯格明子）。

## 2. 滑动诱导的磁性铁电金属 (MFM)
在双层 FGT 中，通过[[../concepts/sliding-ferroelectricity|层间滑动]]可实现罕见的**磁性铁电金属 (Magnetic Ferroelectric Metal)** 态 [[../papers/miaoMagneticFerroelectricMetal2024]]：
- **对称性破缺**：当双层 FGT 从原始堆叠向 $(1/3, 1/3)$ 构型滑动时，打破了水平镜面对称性 $M_z$。
- **层间电荷转移**：对称性破缺驱动了约 **$0.03e$** (每单位晶胞) 的垂直电荷转移，从而产生垂直铁电极化。
- **铁电金属共存**：由于极化起源于层间电荷不对称而非体相离子位移，极化电荷在实空间与层内传导电子分离，使得垂直极化能够在良好的金属性背景下稳定存在，且不被自由电子完全屏蔽。
- **磁电耦合**：极化翻转（翻转势垒约 **$13\text{ meV}$**）可显著调制界面磁矩和自旋极化电导。

## 3. 光学指纹表征
利用光学手段可精确鉴定 FGT 的多铁状态 [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：
- **磁序探测**：磁克尔效应（MOKE）信号的强度反映磁化强度及磁序类型。
- **铁电态探测**：二次谐波产生（SHG）信号对中心对称性破缺极其敏感，可作为滑动铁电相的判据。

## 4. 主要物性参数
| 参数项 | 数值/描述 | 来源 |
| :--- | :--- | :--- |
| **空间群 (单层)** | $P6_3/mmc$ | 基础晶格数据 |
| **空间群 (滑动双层)** | $P3m'1$ (磁空间群) | [[../papers/zhaoOpticalFingerprintsTwodimensional2024]] |
| **滑动相变势垒** | $\sim 13\text{ meV}$ | [[../papers/miaoMagneticFerroelectricMetal2024]] |
| **层间电荷转移** | $\sim 0.03e$ | [[../papers/miaoMagneticFerroelectricMetal2024]] |
| **居里温度 ($T_C$)** | $130\text{--}300+\text{ K}$ | 依赖于栅压调控 |

## 5. 本库相关代表性论文
- [[../papers/miaoMagneticFerroelectricMetal2024]]：Acta Mater. 2024，首次揭示双层 FGT 中的滑动诱导 MFM 相。
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：npj Comp. Mater. 2024，利用对称性分析确定 FGT 多铁态的光学特征。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：综述 FGT 作为滑动铁电异质结在低功耗器件中的应用。

## 6. 关联概念
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
- [[../entities/CrTe2|二碲化铬 CrTe2]] (对比材料：金属性二维多铁)
