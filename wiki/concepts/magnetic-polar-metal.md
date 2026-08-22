---
tags: [concept, multiferroic, metal, magnetism]
title: 磁性极性金属 / Magnetic Polar Metal
type: concept
status: mature
domain: [multiferroics, polar-metals, 2d-magnetism]
mechanism: "在同一金属相中同时破缺空间反演（极性畸变）与时间反演（磁有序），三种序参量（导电性、极化、磁化）共存并通过自旋-轨道耦合互相调控"
related_concepts: [multiferroicity, magnetoelectric-coupling, polar-metal, ferroelectric-metal, sliding-ferroelectricity]
related_entities: [Fe3GeTe2, WTe2]
papers: [miaoMagneticFerroelectricMetal2024, wuNonvolatileSwitchableHalfmetallicity2024, tianRoomtemperatureTwodimensionalMultiferroic2026]
updated: 2026-08
---



# 磁性极性金属 / Magnetic Polar Metal

磁性极性金属（magnetic polar metal）指在**金属（导电）材料中同时实现磁性（磁有序）与极性（非中心对称、含垂直极化）**的材料。它是"磁性 + 铁电 + 金属"三重属性的交集：金属性提供电导读出，极性提供可开关的垂直极化，磁性提供磁序与自旋自由度。此类材料是二维多铁（multiferroic）家族中导电性能最优的一支，有望实现"电控磁/磁控电"的高密度低功耗器件。

## 👵 太奶导读

太奶，这种材料就像一块**又导电、又能记电、还带磁**的"三合一"宝贝。一般的材料，要么导电不能记电，要么能记电但不导电，还要么有磁性但不听电指挥。磁性极性金属把这三种本事凑到一起：导电方便读数据，记电方便存数据，磁性方便"用磁写字、用电读"或者反过来。做个既能存储又能传感的芯片，它最合适不过。

## 🧩 核心内容与机制 (Core Content)

- **典型体系：双层 FGT（Fe₃GeTe₂）**：miao2024 提出双层 FGT 作为磁性铁电金属。铁磁性（居里温度 ~150–220 K 量级）与垂直极化共存；极化源于**层间滑移**改变堆垛，极化大小 ~8.3×10⁻⁴ e·Å/单胞，势垒 ~13 meV/单胞（[[../papers/miaoMagneticFerroelectricMetal2024]]）。
- **滑移诱导极化**：双层 FGT 的 State-1/State-2 对应滑移矢量 (1/3,1/3) 与 (-1/3,-1/3)，产生相反的垂直极化 ±P；Bader 电荷分析显示层间转移 ~0.03 e，极化方向与电荷转移方向一致（[[../papers/miaoMagneticFerroelectricMetal2024]]）。
- **磁电耦合与应变调控**：磁矩大小影响极化稳定性；-1% 应变可使极化反转并伴随磁各向异性调制，实现应变可控的磁电耦合（[[../papers/miaoMagneticFerroelectricMetal2024]]）。
- **扩展家族**：T-CdCr₂Te₄（磁性铁电半导体）、双层 FGT/多铁异质结等；与半金属性（half-metallicity）结合可实现自旋分辨极化开关（[[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]）。
- **应用**：金属电导使极化态可非破坏读取，结合磁性可实现多态存储、自旋电子逻辑与磁电传感器。

![图：双层 FGT 磁性铁电金属的滑移极化和磁结构](../../raw/figures/miaoMagneticFerroelectricMetal2024/fig_1_SVDXYJ6N.png)
- **看图要点**：双层 FGT 结构、铁磁层间耦合与滑移引起的极化示意；对比不同堆垛的极化与磁序。
- **来源**：[[../papers/miaoMagneticFerroelectricMetal2024]]

![图：极化-应变-磁性耦合相图与翻转路径](../../raw/figures/miaoMagneticFerroelectricMetal2024/fig_2_HRQRQ5VP.png)
- **看图要点**：应变依赖的极化能量面与磁化强度；-1% 应变下极化反转与磁各向异性变化。
- **来源**：[[../papers/miaoMagneticFerroelectricMetal2024]]

## 🔬 物理参数表

| 属性 | 数值 | 方法与来源 |
| :--- | :--- | :--- |
| 双层 FGT 垂直极化 P | ~8.3×10⁻⁴ e·Å/单胞 | DFT（[[../papers/miaoMagneticFerroelectricMetal2024]]） |
| 双层 FGT 翻转势垒 | ~13 meV/单胞 | NEB/DFT（[[../papers/miaoMagneticFerroelectricMetal2024]]） |
| 层间 Bader 电荷转移 | ~0.03 e | Bader 分析（[[../papers/miaoMagneticFerroelectricMetal2024]]） |
| 滑移矢量（两态） | (1/3,1/3) ↔ (-1/3,-1/3) | 结构模型（[[../papers/miaoMagneticFerroelectricMetal2024]]） |
| -1% 应变效应 | 极化反转 + 磁各向异性调制 | DFT（[[../papers/miaoMagneticFerroelectricMetal2024]]） |

## 🧭 近邻概念辨析

- **与极性金属（polar-metal）**：磁性极性金属 = 极性金属 + 磁有序；极性金属不要求磁性。
- **与铁电金属（ferroelectric-metal）**：铁电金属要求极化可翻转但通常非磁；磁性极性金属额外要求磁序，是"多铁"与"铁电金属"的交集。
- **与多铁性（multiferroicity）**：多铁性泛指两种及以上铁性共存（铁电/铁磁/铁弹）；磁性极性金属是多铁性的"导电+磁电耦合"分支，强调金属基体。

## 📚 相关论文 (Related Papers)

- [[../papers/miaoMagneticFerroelectricMetal2024]]：双层 FGT 磁性铁电金属理论预言。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：可切换半金属磁性。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：二维室温多铁候选。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/multiferroicity|多铁性]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../concepts/polar-metal|极性金属]]
- [[../concepts/ferroelectric-metal|铁电金属]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../entities/Fe3GeTe2|Fe3GeTe2]]
- [[../entities/WTe2|WTe2]]
