---
tags: [concept]
title: 'molecular-dynamics'
type: concept
status: developing
papers: ['Wei2021', 'Zhang2019a', 'Zhang2019b', 'Zhang2019c', 'guoAdvancesTwodimensionalFerroelectric2025', 'kresseInitiomolecularDynamicsLiquid1993', 'lezoualchStudyChargeDensity']
updated: 2026-08-18
---

# molecular-dynamics

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


分子动力学（molecular dynamics, MD）是**通过数值积分牛顿运动方程模拟原子/分子随时间的运动轨迹**的计算方法，用于研究相变、扩散、力学、热输运、液体与无定形结构、生物分子等。依据势能来源分为经典 MD（经验势）、机器学习势 MD 与从头算 MD（AIMD）。

## 👵 太奶导读

太奶啊，分子动力学就是在电脑里"放一部原子动画片"：给每个原子定好受力规则（势函数），然后让电脑一步一帧地推演所有原子"下一步往哪跑"，跑几十万步就看出了材料怎么运动、怎么变形的全过程。想看材料在高温下怎么相变、原子怎么扩散、导热怎么进行，就让原子们"跑起来"。

## 🧩 核心内容与机制 (Core Content)

- **基本原理**：求解 F=ma 的牛顿方程（Velocity-Verlet 等积分器），统计系综（NVE/NVT/NPT）控制温度压力，本库 MLP 驱动的 MD 论文即属此流。
- **势能类型**：经验势（快、粗）、机器学习势（MLP，近 DFT 精度、本库主力）、从头算 MD（AIMD，精确但慢，本库 Car-Parrinello 相关）。
- **典型应用**：结构相变（structural-phase-transition）、原子扩散与迁移（配合 NEB）、热导率（Green-Kubo）、力学性能、界面与电化学（本库液态金属、无定形、相变材料 MD 论文）。
- **分析手段**：径向分布函数、均方位移（扩散系数）、速度自相关（态密度/热导）、结构因子。
- **与实验对照**：MD 预测可与 XRD、中子散射、DSC 等实验结果对照。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/machine-learning-potential|机器学习势]]：高精度 MD 的势函数。
- [[../concepts/density-functional-theory|密度泛函理论]]：从头算 MD 的基础。
- [[../concepts/structural-phase-transition|结构相变]]：MD 研究的重要对象。
- [[../concepts/nudged-elastic-band|NEB 方法]]：与 MD 互补的路径方法。

## 📚 相关论文 (Related Papers)

- [[../papers/Wei2021]] — Atomic simulations of bamboo-like N-doped CNTs with spaced nitrogen and carbon atoms by DFTB algorithm
- [[../papers/Zhang2019a]] — Studying Stability of Atom Packing for Ti Nanoparticles on Heating by Molecular Dynamics Simulations
- [[../papers/Zhang2019b]] — Packing Changes in Melting, Freezing, and Coalescence of Titanium Nanoparticles from Atomic Simulations
- [[../papers/Zhang2019c]] — Atomic simulations of packing patterns and thermal behavior in Ti clusters
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]] — Advances in two-dimensional ferroelectric materials
- [[../papers/kresseInitiomolecularDynamicsLiquid1993]] — <i>Ab initio</i> molecular dynamics for liquid metals
- [[../papers/lezoualchStudyChargeDensity]] — Study of charge density waves in transition metal dichalcogenides
