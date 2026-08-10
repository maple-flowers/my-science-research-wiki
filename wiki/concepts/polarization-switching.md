---
tags: [concept, switching, dynamics, ferroelectric, polarization]
category: [D02, Z01]
---

# 极化翻转与动力学 / Polarization Switching Dynamics

铁电及多铁材料在外加电场、机械应变、光照或热激发作用下，铁电极化矢量矢量发生方向改变（如 $180^\circ$ 反转或 $90^\circ$ 转向）的非平衡动力学过程。极化翻转速率、临界场强度及翻转路径是决定铁电存储器（FeRAM/FTJ）和逻辑器件工作速度与功耗的关键因素。

## 主要翻转机制与物理特性

1. **单畴均匀翻转 vs 畴壁核化与生长**：
   - 传统单畴均匀翻转（Stoner-Wohlfarth 型）翻转势垒极高，需要巨大的临界翻转场。
   - 实际晶体中极化翻转通常遵循 **Kolmogorov-Avrami-Ishibashi (KAI)** 模型或 **Nucleation-Limited Switching (NLS)** 模型：先在缺陷或电极界面发生反向畴核化（Nucleation），随后通过[[../entities/domain-wall|畴壁（Domain Wall）]]横向运动扩张完成翻转。
2. **[[sliding-ferroelectricity|滑动铁电体]]中的超快翻转动力学**：
   - 范德华二维材料（如双层 [[../entities/h-BN|h-BN]]、[[../entities/TMDs|3R-MoS₂]]）中，层间相对滑动克服弱 vdW 力即可实现极化反转。
   - [[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]] 研究表明，滑动铁电体的畴壁异常宽（达数十纳米），畴壁运动临界电场比单畴翻转低近两个数量级（0.026 V/nm vs 1.41 V/nm），畴壁移动速度可达 ~6000 m/s，实现了皮秒/纳秒级的超快翻转。
3. **多场驱动的极化翻转**：
   - **机械应变/弯曲驱动**：挠曲电效应（Flexoelectricity）或应变梯度可直接打破对称性驱动极化翻转（[[../../raw/note/2025_He_Switching Two-Dimens_KEY-RXAQ7PX6]]、[[../../raw/note/2021_Yang_Rippling Ferroic Pha_KEY-P2XD9CEM]]）。
   - **电场控制金属/半金属极化**：在二维铁电金属/半金属中，栅极电场通过调控带边电子结构驱动非挥发极化翻转（[[../../raw/note/2018_Fei_Ferroelectric switch_KEY-AMP44BB6]]、[[../../raw/note/2019_Sharma_A room-temperature f_KEY-DTWZPQJW]]）。

## 本库相关论文

- **超快动力学与模拟**：
  - [[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]：Ultrafast switching dynamics of the ferroelectric domain wall — 结合 [[../entities/deep-potential|机器学习势]] 与分子动力学揭示 h-BN 超快畴壁运动。
- **机械与应变驱动翻转**：
  - [[../../raw/note/2025_He_Switching Two-Dimens_KEY-RXAQ7PX6]]：Switching 2D Sliding Ferroelectrics by Mechanical Bending — 机械弯曲诱导层间滑动与极化翻转。
  - [[../../raw/note/2021_Yang_Rippling Ferroic Pha_KEY-P2XD9CEM]]：Rippling Ferroic Phase Transition and Domain Switching — 皱褶相变与畴翻转。
- **二维铁电金属与突触翻转**：
  - [[../../raw/note/2018_Fei_Ferroelectric switch_KEY-AMP44BB6]]：Ferroelectric switching of a two-dimensional metal — 二维金属中的铁电开关。
  - [[../../raw/note/2019_Sharma_A room-temperature f_KEY-DTWZPQJW]]：A room-temperature ferroelectric semimetal — 室温铁电半金属的开关特性。
  - [[../../raw/note/2025_Sun_Sliding ferroelectri_KEY-KZZ35845]] / [[../../raw/note/2025_Sun_Sliding ferroelectri_KEY-UJRJMZE9]]：滑动铁电隧道结（FTJ）与神经形态器件中的脉冲翻转特性。

## 关联概念与实体

- [[sliding-ferroelectricity|滑动/堆叠铁电性 Sliding Ferroelectricity]]
- [[moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[../entities/domain-wall|畴壁 Domain Wall]]
- [[../entities/h-BN|氮化硼 h-BN]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
