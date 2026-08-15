---
tags: [entity, material, multiferroic, magnetism, 2D]
title: 二碘化镍 (NiI2) / Nickel Iodide
type: entity
status: mature
formula: NiI2
stoichiometry: R-3m (bulk)
class: [vdW, multiferroic, magnetic-semiconductor]
properties: [type-ii-multiferroicity, spin-helix, electromagnon, improper-electronic-ferroelectricity]
related_entities: [MnPSe3, CrI3, BiFeO3]
updated: 2026-08
papers: [songEvidenceSinglelayerVan2022, fiebigEvolutionMultiferroics2016, FerroelectricityMultiferroicityAtomic2023, aminiAtomicscaleVisualizationMultiferroicity2024, tangMultiferroicityTwodimensionalVan2025, wuCoexistenceFerroelectricityAntiferroelectricity2024, RecentAdvancesGrowth2025]
---

# 二碘化镍 (NiI2) / Nickel Iodide
二碘化镍 (NiI₂) 是一种范德华层状磁性半导体，是目前已知唯一在单层极限下仍保持本征**第二类多铁性 (Type-II Multiferroicity)** 的材料。其多铁性起源于非对称的螺旋磁序（Proper-screw）对晶格对称性的打破，是研究二维磁电耦合物理的里程碑体系。
## Grandma 👵 太奶导读
太奶，这个 **NiI2** 可是材料界最近的大红人。
它长得像是一叠由碘原子和镍原子夹成的“紫金威化饼”。
以前大家都觉得，材料要是薄到只有一层原子那么厚，它的磁性和电性就很难保持稳定，早晚得散架。
但科学家们发现，哪怕把 NiI₂ 撕得只剩一张纸那么薄（单层），它里面的磁性小箭头依然能排成非常整齐的“螺旋长龙”，而且这条龙一摆尾巴，就能给材料带出电信号来。这就像是一个能在微型世界里同时玩转磁铁和电池的小天才！
## 🏗️ 结构概览：二维三角晶格
NiI₂ 晶体结构属于菱面体系（$R\bar{3}m$）。Ni²⁺ 离子构成二维三角晶格。
![图：块体 NiI₂ 的多铁相转变（双折射与偏振旋转证据）](../../raw/figures/songEvidenceSinglelayerVan2022/fig_2_CKHGZI78.png)
*   **看图要点**：图中展示了 NiI₂ 随温度降低发生的两次相变。$T_{N,1} \approx 75\text{ K}$ 进入反铁磁相；$T_{N,2} \approx 59.5\text{ K}$（块体）进入螺旋磁/多铁相。单层极限下，这一转变温度约为 $21\text{ K}$。
*   **来源**：[[../papers/songEvidenceSinglelayerVan2022]] -> [[../figures/crystal-structures-xrd-phases|相变与相图]]
## 🧩 物理特性
*   **正螺旋磁序 (Proper-screw)**：Ni²⁺ 的自旋在 $a-b$ 面内呈周期性螺旋排列，其传播矢量 $Q$ 打破了原晶格的反演对称性。
*   **磁致极化**：根据[[../concepts/type-ii-multiferroicity|第二类多铁性]]机制，磁序直接诱导沿 $a$ 轴方向的自发极化。
*   **电磁振子**：在 $T < T_C$ 时，拉曼光谱中会出现 31 cm⁻¹ 和 37 cm⁻¹ 的特征峰，具有巨大的圆二色性（ROA），是磁电强耦合的动力学标志。
## 📊 核心参数
| 参数 | 数值 | 来源/备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_C$)** | 块体 ~60 K / 单层 ~21 K | 层数越薄，转变温度越低 |
| **磁序类型** | 正螺旋磁序 (Proper-screw) | $Q = (0.138, 0, 1.457)$ |
| **极化方向** | 沿 $a$ 轴 (in-plane) | 由磁手性唯一决定 |
| **光学带隙** | ~1.3 eV | 磁性半导体 |
## 📚 相关论文 (Related Papers)
- [[../papers/songEvidenceSinglelayerVan2022]]：Nature 封面论文，实验证实单层 NiI₂ 为本征多铁体。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]
- [[../papers/fiebigEvolutionMultiferroics2016]]
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]
- [[../papers/RecentAdvancesGrowth2025]]
## 🔗 关联概念与实体 (Related Concepts & Entities)
- [[../concepts/type-ii-multiferroicity|第二类多铁性]]
- [[../concepts/electromagnon|电磁振子]]
- [[../concepts/spin-helix|螺旋磁序]]
- [[../entities/CrI3|三碘化铬 (CrI₃)]]（同族层状磁性材料）
