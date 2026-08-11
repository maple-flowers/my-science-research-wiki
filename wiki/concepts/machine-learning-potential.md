---
tags: [concept, mlip, deepmd, dft, simulation, ferroelectrics]
category: [Z01]
---

# 机器学习势与大尺度原子模拟 / Machine Learning Interatomic Potentials (MLIP)

在计算材料学中，通过机器学习（如神经网络、高斯过程、核岭回归等）拟合由第一性原理密度泛函理论（DFT）计算获得的势能量曲面（PES），得到高效且高精度的原子间势函数。这使得在保持量子力学精度的同时，模拟规模跨越到纳秒（ns）和微米（μm）尺度成为可能。

## 核心物理优势

1. **精度与标度的统一**：
   - 具有 DFT 级别的精度（能量误差 ~1 meV/atom，力误差 ~0.05 eV/Å）。
   - 计算复杂度随原子数呈线性标度 $O(N)$，计算速度比 DFT 快 3-5 个数量级，支撑起数万至数百万原子的大体系动力学模拟。
2. **克服“尺寸-精度”困境**：
   - 传统 DFT 难以模拟[[../entities/domain-wall|畴壁（Domain Wall）]]（数纳米至数十纳米宽）、[[moire-superlattice|莫尔超晶格]]（大胞包含成千上万原子）及动态[[polarization-switching|极化翻转]]。
   - MLIP（如 DeePMD-kit）成功捕捉了莫尔铁电畴中的细微结构细节，如 h-BN 中存在的 **Bloch-type (0°)** 和 **Néel-type (90°)** 畴壁（[[../../raw/note/heUltrafastSwitchingDynamics2024|He 2024]]）。
3. **主动学习与生成式采样 (DP-Gen)**：
   - 利用并发学习（Concurrent Learning）自动探索构型空间，仅对不确定性高的构型调用 DFT 标注，确保势函数在极端应变、高电场或相变过程中的稳健性（[[../../raw/note/gaoStrainEngineeringFerroelectric2024|Gao 2024]]）。

## 铁性体系的前沿应用

### 1. 莫尔超晶格与超快畴壁动力学
在二维滑动铁电体（如双层 h-BN）中，MLIP 模拟揭示了莫尔结构中畴壁的固有迁移率极高。
- **超快翻转**：100 nm 尺寸器件的翻转时间仅为 ~15 ps，畴壁速度可达约 6000 m/s，接近声速上限（[[../../raw/note/heUltrafastSwitchingDynamics2024|He 2024]]）。
- **超顺电性 (Super-paraelectricity)**：由于莫尔畴壁具有极低的摩擦力，在极小外场下即可发生可逆移动，表现出无滞后的超顺电响应，除非受到缺陷（如氮空位 $V_N$）的锚定。

### 2. 复合铁电性与多态存储
通过 MLIP 模拟，可以发现单一机制无法解释的复杂物理现象。
- **内禀与滑动协同**：在 1T''-MoSe2 等材料中，内禀畸变产生的偶极矩与层间滑动极化耦合，形成“复合铁电性”。
- **多状态切换**：通过层间滑动与层选择性极化翻转的组合，可实现 6 态或 10 态的稳态存储（[[../../raw/note/tangCombiningIntrinsicSlidinginduced2025|Tang 2025]]）。MLIP 准确描述了不同路径下约 10-30 meV/atom 的微小能垒差异。

### 3. 应变工程与畴结构编程
机械应变不仅能调控相变稳定性，还能直接降低物理势垒。
- **势垒修饰**：应变能将极化翻转势垒显著降低甚至消除，触发自发的铁电-铁弹相变（[[../../raw/note/gaoStrainEngineeringFerroelectric2024|Gao 2024]]）。
- **畴壁编程**：应变方向与畴壁线的夹角决定了畴壁的最终演化路径（如 60° 与 180° 畴壁的转换），为“畴壁电子学”提供了力学控制方案。

## 关联概念与实体

- [[../entities/deep-potential|机器学习势 Deep Potential (DPMD)]]
- [[sliding-ferroelectricity|滑动/堆叠铁电性 Sliding Ferroelectricity]]
- [[moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[../entities/domain-wall|畴壁 Domain Wall]]
- [[polarization-switching|极化翻转 Polarization Switching]]
- [[super-paraelectricity|超顺电性 Super-paraelectricity]]
