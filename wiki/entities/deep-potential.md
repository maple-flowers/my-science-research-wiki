---
tags: [entity, method, mlip, deepmd, dft, simulation]
category: [Z01, D02]
---

# 机器学习势 / Deep Potential (DPMD/DP-Gen)

基于深度神经网络（Deep Neural Network）拟合第一性原理密度泛函理论（DFT）势能量曲面（PES）的原子间势函数方法（代表性开源工具包为 DeePMD-kit 与 DP-Gen）。

## 核心物理与算法架构

1. **平移/旋转/置换不变性描述符**：
   - DeePMD 使用局部原子环境的光滑描述符（Smooth Descriptor），自然满足量子力学势能面的平移、旋转及同种原子置换不变性。
2. **DP-Gen 主动学习/采样工作流**：
   - 包含“采样（Exploration）- 标注（Labeling）- 训练（Training）”闭环。在分子动力学轨迹中利用多个神经网络势预测结果的偏差（Model Deviation）定量评估不确定性，仅对偏差较大的构型自动调用 VASP/QE 进行 DFT 能量/力计算，极大提升数据效率与势函数泛化能力。
3. **在低维铁性与大尺度物理中的突破**：
   - [[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]] 论文中，单纯 DFT 仅能计算包含数百原子的小胞，无法处理宽达数几十纳米的畴壁及成千上万原子的莫尔超晶格。通过 DP-Gen 训练获得 h-BN 范德华双层深度势能，成功实现了对包含数万原子的莫尔超晶格及[[domain-wall|畴壁]]超快运动（~6000 m/s）的近 DFT 精度大尺度分子动力学模拟。

## 本库相关论文与概念

- [[../../raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]：Ultrafast switching dynamics of the ferroelectric domain wall in stacking-engineered h-BN bilayer — 示范了 DFT + DeePMD-kit 在二维[[../concepts/sliding-ferroelectricity|滑动铁电]]超快动力学研究中的应用。
- [[../concepts/machine-learning-potential|机器学习势与大尺度原子模拟 Concept Page]]
- [[../concepts/sliding-ferroelectricity|滑动/堆叠铁电性 Sliding Ferroelectricity]]
- [[../concepts/moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[domain-wall|畴壁 Domain Wall]]
