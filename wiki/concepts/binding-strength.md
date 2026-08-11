---
name: binding-strength
description: 比较晶面内与晶面间的结合强度，用于预判非范德华材料的剥离各向异性。
metadata:
  type: concept
---

# 结合强度 / Binding Strength ($\xi$)

**结合强度** 是判断非范德华材料是否可剥离的第二个关键物理指标，与 [[bond-density|键密度]] 共同构成了高通量筛选二维氧化物单层的理论判据 [[../papers/zhongHighthroughputExfoliationMultiferroic2025|Zhong 2025]]。

## 1. 物理含义

结合强度判据通过量化不同空间方向上的原子轨道重叠与化学键合程度，来评估三维块体材料的剥离各向异性。在非范德华（non-vdW）体系中，由于缺乏天然的范德华间隙，剥离必须发生在化学键相对薄弱的晶面上。

- **面外结合强度 ($\xi_\perp$)**：衡量垂直于目标剥离晶面方向的原子轨道波函数重叠程度（轨道模长求和）。
- **面内结合强度 ($\xi_\parallel$)**：衡量平行于晶面方向的原子轨道波函数重叠程度。

## 2. 剥离判据条件

根据 [[../papers/zhongHighthroughputExfoliationMultiferroic2025|Zhong 2025]] 提出的普适性规则，一个晶面若具有剥离潜力，必须满足：
$$\xi_\perp < \xi_\parallel$$
且同时满足低键密度条件 ($\rho \le 0.3$ bonds/Å²)。这表明层间相互作用力显著弱于层内共价/离子键合，使得材料在受到机械力或化学剥离时，倾向于沿该晶面解理，而保持单层结构的完整性。

## 3. 微观机制与调控

在二维氧化物（如 SrOsO₃、BiFeO₃）中，结合强度与金属-氧（M–O）轨道杂化密切相关：
- **杂化主导**：例如在 SrOsO₃ 中，Os 5d 与 O 2p 轨道的强杂化直接决定了结合强度。
- **应变调控**：通过应变工程（Strain Engineering）可以显著改变结合强度的各向异性。在 SrOsO₃ 模拟中，面外积分晶体轨道哈密顿布居（−ICOHP）在应变驱动下从 0.53 eV 增至 0.91 eV，反映了面外结合强度的剧烈演化，并驱动了序-序相变。

## 4. 相关概念
- [[bond-density|键密度 Bond Density]]
- [[../entities/SrOsO3|SrOsO3]]
- [[strain-engineering|应变工程 Strain Engineering]]
- [[phase-interlocked|相锁定 Phase Interlocked]]
