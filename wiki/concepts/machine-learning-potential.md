---
tags: [concept, mlip, deepmd, dft, simulation]
category: [Z01]
---

# 机器学习势与大尺度原子模拟 / Machine Learning Interatomic Potentials (MLIP)

在计算材料学中，通过机器学习（如神经网络、高斯过程、核岭回归等）拟合由第一性原理密度泛函理论（DFT）计算获得的势能量曲面（PES），得到高效且高精度的原子间势函数。

## 物理意义与核心优势

1. **兼顾精度与效率**：
   - 具有 DFT 级别的量子化学精度（能量误差 ~1 meV/atom，力误差 ~0.05 eV/Å）。
   - 计算复杂度随原子数呈线性标度 $O(N)$，计算速度比 DFT 快 3-5 个数量级，可实现数万至数百万原子、纳秒级（ns）时空尺度的分子动力学（MD）模拟。
2. **克服大尺度铁性缺陷模拟瓶颈**：
   - 传统 DFT 难以直接模拟[[../entities/domain-wall|畴壁（Domain Wall）]]（数纳米至数十纳米宽）、[[moire-superlattice|莫尔超晶格]]（大胞包含成千上万原子）及动态[[polarization-switching|极化翻转]]。
   - 机器学习势（如 DeePMD-kit）使得大尺度莫尔铁电畴、畴壁高迁移率及温度驱动相变的全原子动力学模拟成为可能（[[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]）。
3. **主动学习与生成式采样 (DP-Gen)**：
   - 利用并发学习（Concurrent Learning）/主动学习自动探索构型空间，仅对不确定性较高的构型调用 DFT 标注，极大减少算力浪费。

## 本库相关论文与应用

- [[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]：He 2024 (Nature Communications) — 结合 DFT 与 DeePMD-kit (DP-Gen) 拟合 h-BN 范德华双层势函数，系统研究了包含数万原子的莫尔超晶格中[[sliding-ferroelectricity|滑动铁电]]畴壁的超快动力学（~6000 m/s）与[[super-paraelectricity|超顺电]]相变。
- [[../../raw/note/2024_Gao_Strain engineering o_KEY-MW64GHEG]]：通过应变工程与机器学习势模拟调控二维材料极化与畴结构。

## 关联概念与实体

- [[../entities/deep-potential|机器学习势 Deep Potential (DPMD)]]
- [[sliding-ferroelectricity|滑动/堆叠铁电性 Sliding Ferroelectricity]]
- [[moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[../entities/domain-wall|畴壁 Domain Wall]]
