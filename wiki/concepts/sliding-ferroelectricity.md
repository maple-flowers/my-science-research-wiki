---
tags: [concept, ferroelectricity, 2D, sliding, interlayer]
category: [D02, Z01]
---

# 滑动/堆叠铁电性 / Sliding (Stacking-engineered) Ferroelectricity

在范德华（vdW）双层及多层二维材料中，即使单层材料具有反演对称性（非铁电），通过特定堆叠角度或非中心对称堆叠（如 3R 相、AB/BA 堆叠），**层间相对滑动**可诱导垂直于层平面的面外极化（$P_z$）或面内极化（$P_xy$）。极化反转机制并非来自传统的原子内部位移或离子置换，而是由层间电子电荷重新分布与层间相对滑动协同决定。

## 核心物理特征与机制

1. **超低翻转势垒**：
   - 相比传统钙钛矿（需要切断/重组强化学键），滑动铁电体仅需克服弱范德华层间相互作用，翻转势垒通常低 1-2 个数量级。
2. **畴壁运动主导快开关**：
   - 滑动铁电体中畴壁宽度可达数十纳米（如 h-BN 中 9.7–40.7 nm），临界翻转电场远低于单畴均匀翻转（如 0.026 V/nm vs 1.41 V/nm）。畴壁高迁移率主导了皮秒/纳秒级的快开关动力学（[[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]）。
3. **莫尔超晶格与扭转调控**：
   - 在小角度扭曲双层（Moire superlattice）中，面内滑动梯度自动形成周期性纳米铁电畴阵列，呈现无滞后的[[super-paraelectricity|超顺电行为]]。
4. **多场耦合与多态集成**：
   - 滑动铁电性可与金属性、磁性（如 [[Fe3GeTe2]]）及谷电子学耦合，构建自旋/铁电多态存储与超低功耗铁电隧道结（FTJ）（[[../../raw/note/2024_Miao_Magnetic ferroelectr_KEY-R2TZ62V5]]、[[../../raw/note/2025_Sun_Sliding ferroelectri_KEY-KZZ35845]]）。

## 代表性材料体系

- **氮化硼双层 ([[h-BN]])**：AB↔BA 滑动诱导面外极化，莫尔扭曲导致超顺电。
- **过渡金属硫族化合物 ([[TMDs]])**：3R-MoS₂、WSe₂、WTe₂ 薄层，层间滑动驱动极化与金属性相变。
- **III-VI 族化合物 ([[In2Se3]])**：层间滑动与层内极化联动。
- **2D 磁性材料 ([[Fe3GeTe2]])**：滑动诱导磁性铁电金属相。

## 本库相关论文

- **理论与机制**：
  - [[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]：DFT + [[../entities/deep-potential|机器学习势]] 揭示 h-BN 双层超快畴壁开关与莫尔超顺电。
  - [[../../raw/note/2024_Chen_Strong Sliding Ferro_KEY-3Q4MAH3N]]：强滑动铁电性与层间滑动调控自旋裂分。
  - [[../../raw/note/2025_Kaur_Recent advances in t_KEY-QGM7RIPI]]：二维滑动铁电理论计算进展综述。
  - [[../../raw/note/2025_He_Switching Two-Dimens_KEY-RXAQ7PX6]]：机械应变与弯曲调控二维滑动铁电翻转。
- **多维耦合与器件**：
  - [[../../raw/note/2024_Miao_Magnetic ferroelectr_KEY-R2TZ62V5]]：双层 Fe₃GeTe₂ 中层间滑动诱导磁性铁电金属。
  - [[../../raw/note/2025_Tang_Combining intrinsic_KEY-M645VPJN]]：本征与滑动诱导极化结合实现多态铁电。
  - [[../../raw/note/2024_Zhao_Optical fingerprints_KEY-BK4MKECB]]：二维层间滑动多铁性的光学指纹。
  - [[../../raw/note/2025_Han_Tunable sliding ferr_KEY-KRMPDUJI]]：二维 RuX₂ 中可调控滑动铁电。
- **综述与器件应用**：
  - [[../../raw/note/2025_Zhang_Emerging frontiers i_KEY-2W6V8X6T]]：二维滑动铁电前沿与展望。
  - [[../../raw/note/2021_Wu_Sliding ferroelectri_KEY-B52WT4T8]]：2D vdW 材料中的滑动铁电性物理与器件。
  - [[../../raw/note/2025_Sun_Sliding ferroelectri_KEY-KZZ35845]] / [[../../raw/note/2025_Sun_Sliding ferroelectri_KEY-UJRJMZE9]]：二维滑动铁电材料及其在 FTJ、FET 与突触器件中的应用。

## 关联概念与实体

- [[moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[super-paraelectricity|超顺电性 Super-paraelectricity]]
- [[polarization-switching|极化翻转 dynamics Polarization Switching]]
- [[../entities/domain-wall|畴壁 Domain Wall]]
- [[../entities/h-BN|氮化硼 h-BN]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
- [[../entities/Fe3GeTe2|铁锗碲 Fe3GeTe2]]
