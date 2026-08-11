---
tags: [concept, moire, superlattice, twist, 2D]
category: [D02, Z01]
---

# 莫尔超晶格 / Moiré Superlattice

在范德华（vdW）异质结或同质结中，将两层二维晶体以极小扭转角（Twist Angle $\theta$）堆叠，或由于两层晶格常数失配（Lattice Mismatch），在纳米到微米尺度上形成的周期性干涉图案。莫尔超晶格打破了原始晶体的平移对称性，产生了长周期（数纳米到数十纳米）的超晶格势场。

## 物理效应与涌现现象

1. **莫尔铁电性与[[super-paraelectricity|超顺电性]]**：
   - 扭曲双层（如 [[../entities/h-BN|h-BN]]、[[../entities/TMDs|3R-MoS₂]]）在莫尔超晶格中形成周期性排列的 AB 与 BA 堆叠区域。每个区域具有相反的垂直铁电极化。
   - 零场下 AB 与 BA 畴面积相同，宏观极化抵消；微小电场（如 0.026 V/nm）即可驱动畴壁大幅移动使极化饱和，表现出无极化滞后的超顺电行为（[[../papers/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]）。
2. **莫尔多铁性与磁性扭转**：
   - 在二维磁性材料或范德华异质结中，莫尔超晶格周期性调制层间交换耦合强度乃至符号（如铁磁/反铁磁交替），产生非共线磁序、磁斯天明（Skyrmions）及扭转诱导的多铁性（[[../papers/2007_Cheong_Multiferroics：a mag_KEY-CWD5QBWM]]）。
3. **关联电子态与能带工程**：
   - 莫尔势场折叠布里渊区形成平带（Flat Bands），显著增强电子-电子库仑相互作用，产生莫特绝缘体、超导及关联拓扑态（[[../papers/2025_Sun_Sliding ferroelectri_KEY-KZZ35845]]）。

## 本库相关论文

- **莫尔铁电与超快动力学**：
  - [[../papers/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]：DFT + [[../entities/deep-potential|机器学习势]] 研究小角度扭曲 h-BN 莫尔超晶格的大尺度畴结构及超顺电回线。
  - [[../papers/2021_Wu_Sliding ferroelectri_KEY-B52WT4T8]]：莫尔超晶格中的[[sliding-ferroelectricity|滑动铁电]]及其物理效应。
- **莫尔多铁与磁性调控**：
  - [[../papers/2007_Cheong_Multiferroics：a mag_KEY-CWD5QBWM]]：Multiferroics: A Magnetic Twist for Ferroelectricity — 揭示扭角与莫尔工程对多铁性的独特调控。
  - [[../papers/2024_Gao_Strain engineering o_KEY-MW64GHEG]]：应变与莫尔势场协同调控二维极化与畴结构。
- **莫尔器件与生物传感**：
  - [[../papers/2025_Du_Ultrasensitive optoe_KEY-XAK7F6XW]]：基于扭曲双层莫尔超晶格的超灵敏光电生物传感器阵列。
  - [[../papers/2025_Sun_Sliding ferroelectri_KEY-KZZ35845]] / [[../papers/2025_Sun_Sliding ferroelectri_KEY-UJRJMZE9]]：莫尔超晶格在二维滑动铁电隧道结与脑启发突触器件中的应用。

## 关联概念与实体

- [[sliding-ferroelectricity|滑动/堆叠铁电性 Sliding Ferroelectricity]]
- [[super-paraelectricity|超顺电性 Super-paraelectricity]]
- [[topological-defects|拓扑缺陷与磁斯天明 Topological Defects]]
- [[../entities/domain-wall|畴壁 Domain Wall]]
- [[../entities/h-BN|氮化硼 h-BN]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
