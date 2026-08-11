---
tags: [entity]
---

# Bader Code

**Bader Code** 是由德克萨斯大学奥斯汀分校 **Henkelman Group** 开发的一款高性能开源软件包，旨在通过拓扑分析方法处理第一性原理计算生成的电荷密度网格。它是量子化学中“分子中原子理论”（QTAIM）在周期性体系（尤其是基于平面波基组的 DFT 软件，如 **VASP** 和 **Quantum ESPRESSO**）中的标准实现工具。

### 算法演进与晶格偏差的消除

网格化 Bader 分析的核心挑战在于如何精确地将空间划分为由 **[[../concepts/zero-flux-surface|零通量面]]**（Zero-Flux Surface）界定的原子盆地（Bader 体积）。在早期的算法（即“在网法”，On-grid method）中，**[[../concepts/steepest-ascent-path|最陡上升路径]]** 被限制在三维网格的 26 个离散邻居方向上。正如 **[[../papers/tangGridbasedBaderAnalysis2009|Tang 等人 (2009)]]** 所指出的，这种限制会导致严重的 **[[../concepts/lattice-bias|晶格偏差]]**（Lattice Bias），使得分割面人为地沿网格轴线排列，且这种系统误差无法通过加密网格来消除。

目前的 Bader Code 采用了**近网法**（Near-grid method）作为核心算法。该算法通过引入 **[[../concepts/correction-vector|修正向量]]**（Correction Vector）机制解决了上述问题：在追踪电荷密度梯度的过程中，算法会累积真实离格轨迹与离散格点路径之间的偏差。一旦偏差超过半个网格间距，便触发修正步。这一创新确保了 Bader 电荷和体积计算结果具有旋转不变性，并能随网格密度增加而平滑收敛，使算法在保持 $O(N)$ 线性标度的同时达到了极高的数值精度 [[../papers/tangGridbasedBaderAnalysis2009]]。

### 物理特性与材料学应用

从“相位锁定属性”（Phase-Locked Properties）的角度看，Bader Code 将电子密度场内在的拓扑特征“数字化”。在材料科学研究中，它被广泛用于定量分析原子的氧化态和电荷转移情况。例如，在针对 **[[../entities/MXenes|Mn₂N MXenes]]** 的研究中，研究者利用 Bader 分析验证了 Janus 结构中两侧 Mn 原子由于能级对称性破缺而产生的不同电荷构型，从而区分高自旋与低自旋态 [[../papers/chen3dLevelSymmetry2025]]。

为了获得物理上合理的计算结果，使用 Bader Code 时必须包含**冻芯电荷**（Frozen Core Charges）。在使用 PAW 等赝势方法的 DFT 计算中，仅凭价电子密度会导致原子核位置的电荷密度极大值缺失，甚至产生虚假的 **[[../concepts/non-nuclear-attractor|非核吸引子]]**（Non-nuclear Attractors）。因此，通常需要将全电子密度（如 VASP 中的 AECCAR0 和 AECCAR2）与价电子密度合并后再进行分析。

### 性能与可扩展性

Bader Code 针对大规模并行计算进行了优化，能够处理包含数百个原子、数千万个网格点的复杂超胞体系。其线性标度的特性使其成为现代计算材料学设计（如多铁性材料模拟、催化反应路径分析等）中不可或缺的后处理工具。

## 相关论文

- [[../papers/tangGridbasedBaderAnalysis2009]]
- [[../papers/chen3dLevelSymmetry2025]]
