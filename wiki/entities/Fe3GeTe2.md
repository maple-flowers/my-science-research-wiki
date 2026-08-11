---
tags: [entity, material, 2D, Fe3GeTe2]
category: [D02, Z01]
---

# 铁锗碲 / Fe3GeTe2 (FGT)

## 概述
**Fe₃GeTe₂ (FGT)** 是一种具有强垂直磁异向性（PMA）的金属性二维范德华铁磁材料。其晶体结构由 $\text{Fe}_3\text{Ge}$ 原子层被两个 $\text{Te}$ 原子层包覆构成，单层属于 $P6_3/mmc$ 空间群（具有水平镜面对称性 $M_z$ 但无空间反演对称性 $P$）。

FGT 是目前二维磁性材料研究的核心体系，主要因其高居里温度（$T_c$）和可调控性而备受关注。
- **居里温度**：单层本征 $T_c \sim 130\text{--}220\text{ K}$。
- **调控手段**：通过离子液体栅压调控（Ionic Liquid Gating），其 $T_c$ 可提升至室温以上（RT），是构建二维室温自旋电子器件的关键候选材料。

## 磁性铁电金属 (MFM) 相
在 [[../../raw/note/miaoMagneticFerroelectricMetal2024|miaoMagneticFerroelectricMetal2024]] 的研究中，双层 FGT 被证实可以通过[[../concepts/sliding-ferroelectricity|层间滑动]]诱导出罕见的**磁性铁电金属（Magnetic Ferroelectric Metal）**态。

1.  **物理机制**：双层 FGT 通过从原始堆叠向特定坐标滑动（如从 $(0, 0)$ 滑向 $(1/3, 1/3)$），打破了水平镜面对称性 $M_z$。这种对称性破缺导致两层之间发生约 $0.03e$ 的垂直电荷转移，从而诱导出垂直铁电极化。
2.  **极化与金属性共存**：尽管 FGT 具有良好的金属性，但由于其极化来源于层间电荷不对称而非体相离子的位移，自由电子的屏蔽效应无法完全抵消这种跨层的电位差，使得垂直极化与金属性得以非互斥地共存。
3.  **多铁耦合**：该相同时具备铁磁序（FM）和滑动铁电序（FE），极化的翻转可以调制自旋极化电导和界面磁矩，形成典型的多铁性响应。

## 关键物理参数与性质

| 参数项 | 数值/描述 | 来源 |
| :--- | :--- | :--- |
| **空间群 (单层)** | $P6_3/mmc$ | 基础晶格数据 |
| **空间群 (滑动双层)** | $P3m'1$ (磁空间群) | [[../../raw/note/zhaoOpticalFingerprintsTwodimensional2024|Zhao et al. 2024]] |
| **层间滑动势垒** | $\sim 13\text{ meV}$ (NEB计算) | [[../../raw/note/miaoMagneticFerroelectricMetal2024|Miao et al. 2024]] |
| **稳定滑动状态** | State-1 $(1/3, 1/3)$, State-2 $(-1/3, -1/3)$ | [[../../raw/note/miaoMagneticFerroelectricMetal2024|Miao et al. 2024]] |
| **垂直电荷转移** | $\sim 0.03e$ (每单位晶胞) | [[../../raw/note/miaoMagneticFerroelectricMetal2024|Miao et al. 2024]] |
| **光学指纹** | Kerr 信号区分磁序，SHG 信号区分铁电/多铁态 | [[../../raw/note/zhaoOpticalFingerprintsTwodimensional2024|Zhao et al. 2024]] |

## 应用前景
- **非挥发性存储器**：利用滑动铁电极化控制自旋极化电流，实现超高密度、低功耗的 FeFET 或磁电随机存储器。
- **自旋电子学器件**：通过极化反转调控交换偏置（Exchange Bias）和界面磁各向异性。
- **莫尔超晶格**：在小角度扭转的 FGT 莫尔体系中探索拓扑磁性与铁电性的非平庸耦合。

## 本库关联文献

- [[../../raw/note/miaoMagneticFerroelectricMetal2024|Magnetic ferroelectric metal in bilayer Fe₃GeTe₂ under interlayer sliding]] (2024)：首次揭示双层 FGT 中的滑动诱导 MFM 相及开关势垒。
- [[../../raw/note/zhaoOpticalFingerprintsTwodimensional2024|Optical fingerprints of two-dimensional interlayer-sliding multiferroic materials]] (2024)：利用对称性分析确定 FGT 在不同多铁态下的 SHG 和 Kerr 光学特征。
- [[../../raw/note/sunSlidingFerroelectricityTwodimensional2025|Sliding ferroelectricity in two-dimensional van der Waals materials]] (2025)：综述 FGT 作为金属性铁磁体在滑动铁电异质结中的器件应用。
- [[../../raw/note/wuCoexistenceFerroelectricityAntiferroelectricity2024|Coexistence of Ferroelectricity and Antiferroelectricity in 2D Systems]] (2024)：讨论 2D 多铁性的实验鉴定方法。

## 关联概念与实体
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../concepts/2D-materials|二维范德华材料 2D Materials]]
- [[TMDs|过渡金属硫化物 TMDs]] (对比材料)
