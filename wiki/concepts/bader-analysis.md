---
tags: [concept]
---

# 基于电荷密度拓扑性质的原子电荷分配方案：Bader分析

Bader 分析（Bader Analysis）是一种基于分子或晶体实空间电荷密度 $\rho(r)$ 拓扑性质将空间划分为原子体积（Bader Volume）的方案。其理论核心是量子化学中的**分子原子论（AIM）**，定义原子盆地（Atomic Basin）之间的边界为**电荷密度零通量面（Zero-flux Surface）**，即在该面上任意一点，电荷密度的梯度 $\nabla\rho$ 与面法向 $n$ 垂直（$\nabla\rho \cdot n = 0$）。相比于依赖特定基组或波函数定义的 Mulliken 布居分析，Bader 分析直接基于物理可观测的电荷密度网格，因此在 DFT 后处理中表现出极高的稳健性。

### 算法演进与晶格偏差

在处理离散网格数据（如平面波 DFT 的输出）时，早期的高效算法（在网法，On-grid method）存在固有的**晶格偏差（Lattice Bias）**，即分割路径被限制在有限的 26 个离散方向，导致原子面人为地与网格对齐，产生棱角感且无法通过单纯加密网格消除。Henkelman 组提出的**近网法（Near-grid method）**通过引入"修正向量"机制解决了这一问题，使电荷分配路径能精准追踪真实的离格梯度轨迹，实现了 Bader 电荷/体积随网格加密的单调收敛以及旋转不变性 [[../papers/tangGridbasedBaderAnalysis2009]]。

### 相位锁定性质（Phase-Locked Properties）中的应用

在"相锁性质"（Phase-Locked Properties）的研究框架下，Bader 分析是跨越结构、电子、自旋与极化维度的核心量化桥梁：

- **晶体结构与力学耦合**：在二维过渡金属硫族化物（TMDs）中，材料的杨氏模量和极限强度被证明与从金属（M）到硫族（X）原子的电荷转移量 $\Delta Q$ 呈强线性相关。其底层物理是金属 $d$ 轨道与硫族 $p$ 轨道的杂化强度决定了键合密度，Bader 电荷因此成为了预测力学强度的关键电子描述符 [[../papers/Li2013bonding]]。
- **电子态调控与能级对称性**：在 Mn₂N MXenes 体系中，两侧金属层的 $3d$ 能级对称性决定了电荷在金属层间的重分布。Bader 分析揭示了电荷转移如何导致轨道填充状态在半金属（Half-metal）与半导体（Semiconductor）之间切换，直接量化了由表面钝化或应变诱导的电子相变过程 [[../papers/chen3dLevelSymmetry2025]]。
- **磁序与电荷密度波（CDW）**：在研究 1T′ TMDs 的铁磁 CDW 态时，Bader 电荷分析常用于判定磁性原子在畸变后的氧化态变化，并能捕捉非磁性阴离子上出现的反平行感生磁矩，从而辅助确认由直接交换向超交换机制的转变 [[../papers/chenFerromagneticNonmagnetic1T2022]]。
- **极化与滑移铁电性**：在双层 Fe₃GeTe₂ 等范德华磁性金属中，通过层间滑移诱导的可翻转垂直极化，其本质是未补偿的层间电荷转移（Interlayer charge transfer）。Bader 分析通过量化层间得失电子数，为"磁性极性金属"这一罕见物相提供了微观证据 [[../papers/miaoMagneticFerroelectricMetal2024]]。

### 实施建议

进行 Bader 分析时，建议包含**冻芯电荷（Frozen core charge）**以提高离子电荷的绝对准确度，并需对网格密度进行收敛性测试。

领域:: [[../concepts/density-functional-theory]]
常用软件:: [[../entities/VASP]], [[../entities/bader-code]]
核心描述符:: `charge_transfer` (ΔQ)
