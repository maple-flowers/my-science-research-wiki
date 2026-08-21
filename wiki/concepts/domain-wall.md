---
tags: [concept, ferroelectricity, magnetism, domain-wall, multiferroicity, nanoelectronics]
title: 畴壁 / Domain Wall
type: concept
status: mature
year: 2021
domain: [condensed-matter-physics, ferroics, nanoelectronics]
mechanism: 不同有序畴（极化/磁化/应变）之间的界面过渡区，序参量连续变化，常承载与体相迥异的导电性、磁性、拓扑性
related_concepts: [domain-wall-motion, ferroelectricity, ferroelasticity, topological-defects, polar-vortex, polarization-switching, ferromagnetism, skyrmion, kittel-law]
papers: [prosandeevKittelLawInBiFeO3Ultrathin2010, heUltrafastSwitchingDynamics2024, sunSlidingFerroelectricityTwodimensional2025, martinThinfilmFerroelectricMaterials2016, yuFerroelectricControlMagnetism2026]
updated: 2026-08-19
---

# 畴壁 / Domain Wall

畴壁（domain wall）是铁电/铁磁/铁弹材料中不同**有序畴之间过渡的界面区域**，宽度从纳米到亚纳米尺度。畴壁处序参量（极化/磁化/应变）连续过渡，常展现出与体相迥异的物理性质（导电性、磁性、拓扑性），已成为"畴壁电子学（domain wall nanoelectronics）"的核心研究对象。

## 👵 太奶导读

太奶啊，铁电/磁性材料里面电子"排的队伍方向"不是处处一样的，分成一块一块的小区域，叫畴。两块方向不同的区域之间的"分界线"，就是畴壁——像两个房间之间的"隔断墙"。这堵墙虽然只有几个原子厚，却有神奇的本事：有的墙能导电、有的墙能搅动磁性、有的墙还能被搬来搬去。科学家把这堵墙当"活开关"来用，是新一代电子器件的好材料。

## 🏗️ 结构概览

畴壁按序参量与取向分型：铁电 180°/非 180°（71°/109°）畴壁、铁磁布洛赫/奈尔壁、铁弹畴壁；二维体系还出现极性畴壁与拓扑畴壁（极化涡旋、斯格明子）。

## 🧩 核心内容与机制 (Core Content)

### 1. 畴壁类型与能量学

- **180° 畴壁**：序参量方向反转，极化不连续最大；
- **非 180° 畴壁**（71°/109°）：极化方向旋转，常见于 BiFeO₃、PbTiO₃ 等；
- **铁磁畴壁**：布洛赫壁（面内旋转）/奈尔壁（面外旋转），取决于各向异性与维数；
- 畴壁宽度由交换/梯度能与各向异性能竞争决定，畴构型服从 Kittel 定律（[[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010|Prosandeev 2010]]）。

### 2. 畴壁导电

铁电畴壁可通过极化不连续性产生局域电荷积累而导电，实现"墙即是导线"；二维极性畴壁（如 MoTe₂）在原子极限下仍保持可移动导电通道（[[../papers/martinThinfilmFerroelectricMaterials2016|Martin 2016]]）。

### 3. 拓扑与磁性畴壁

畴壁可承载拓扑磁结构——斯格明子、磁荷、极化涡旋；二维多铁异质结中极化翻转还能在畴壁层面切换磁性织构（[[../papers/yuFerroelectricControlMagnetism2026|Yu 2026]]）。

### 4. 畴壁动力学与开关

畴壁在外场（电场/电流/应力）下迁移，决定铁电开关、阻变存储与超快写入速度；二维滑移铁电中面内/面外极化的协同翻转为低能耗开关提供新路径（[[../papers/heUltrafastSwitchingDynamics2024|He 2024]]、[[../papers/sunSlidingFerroelectricityTwodimensional2025|Sun 2025]]）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 畴壁宽度 | 过渡区尺度 | 纳米至亚纳米 |
| 畴壁类型 | 取向分类 | 180° / 71° / 109° / 布洛赫 / 奈尔 |
| 导电性 | 功能属性 | 绝缘/导电可调（畴壁导电） |
| 迁移率 | 动力学参数 | 决定开关速度 |
| 标度律 | 尺寸依赖 | Kittel 定律 |

## 🔀 近邻概念辨析

- **畴壁 vs 畴**：畴是均匀有序区；畴壁是相邻畴的过渡界面，物理性质往往"突变"且功能化。
- **畴壁 vs 拓扑缺陷**：畴壁本身是拓扑缺陷（一维）；但可承载更高维拓扑结构（斯格明子、涡旋）——后者是"缺陷中的缺陷"。
- **铁电畴壁 vs 磁性畴壁**：铁电畴壁靠极化不连续电荷导电；磁性畴壁靠自旋旋转承载磁化反转，二者物理机制不同但动力学类似。

## 📚 相关论文 (Related Papers)

- [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]：超薄 BiFeO₃ 中 Kittel 定律与畴尺度标度。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：铁电薄膜畴壁导电与器件化综述。
- [[../papers/heUltrafastSwitchingDynamics2024]]：畴壁超快开关动力学。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：二维滑移铁电的畴壁与极化翻转。
- [[../papers/yuFerroelectricControlMagnetism2026]]：铁电畴壁调控磁性织构。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/domain-wall-motion|畴壁运动]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/ferroelasticity|铁弹性]]
- [[../concepts/topological-defects|拓扑缺陷]]
- [[../concepts/polar-vortex|极性涡旋]]
- [[../concepts/polarization-switching|极化翻转]]
- [[../concepts/skyrmion|斯格明子]]
- [[../concepts/kittel-law|Kittel 定律]]
- [[../concepts/ferromagnetism|铁磁性]]
