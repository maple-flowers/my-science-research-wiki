---
tags: [entity]
---

# DeepMD-kit

DeepMD-kit 是一种基于机器学习的原子间势函数训练框架，它实现了 **深度势能（Deep Potential, DP）** 方法，是连接第一性原理计算精度与大规模分子动力学（MD）效率的核心桥梁。在“Phase-Locked Properties”这一科研主题下，DeepMD-kit 提供了量化分析力-电耦合动力学及拓扑结构演化的关键工具，使得研究者能够跨越量子力学与连续介质力学的尺度鸿沟。

## 核心机制与物理约束

DeepMD-kit 的核心在于其能够通过神经网络拟合势能面（PES），同时保持物理定律的完备性。它采用 **描述符（Descriptor）** 对原子局域环境进行特征提取，这些描述符天然满足平移、旋转及原子位置置换不变性（Symmetry-preserving）。在训练过程中，DeepMD-kit 不仅拟合总能量，还利用自动微分技术同时拟合受力和维里应力（Virial），从而确保了动力学模拟中压力和应变演化的物理一致性。

在针对二维铅硫族化合物（PbX, X=S, Se, Te）的研究中 [[../papers/xuTunableFerroelectricTopological2022]]，DeepMD-kit 被用于构建精确捕捉顺电-铁电相变的势函数。其损失函数通过加权组合能量偏离量（$\Delta \epsilon$）、受力偏离量（$\Delta F$）以及维里偏离量（$\Delta \xi$），实现了对多体相互作用能景观的精确刻画。这种高精度的力场描述对于捕捉相变临界点附近的非线性响应至关重要。

## 多尺度范式下的“相位锁定”

在多尺度模拟（Multiscale Simulation）流水线中，DeepMD-kit 扮演着不可替代的“相位转换”角色：
1. **微观标定**：基于 VASP 等第一性原理软件生成的电子结构数据，通过 Berry 相计算提取极化信息，标定原子层级的非线性极化响应和声子软模动力学。
2. **介观演化**：通过集成到 LAMMPS 软件，在数万个原子的体系（如 28 nm × 28 nm 的薄膜）中模拟非均匀应变场下的结构演化。
3. **拓扑锁定**：研究证明，DeepMD-kit 能成功模拟纳米压痕产生的非均匀应变梯度如何驱动极化矢量的连续旋转，从而在介观尺度上“锁定”了如 **极性涡旋（Polar Vortex）** 和 **反涡旋（Antivortex）** 等非平庸拓扑缺陷 [[../papers/xuTunableFerroelectricTopological2022]]。

## 对 Phase-Locked 研究的意义

对于致力于应变工程与拓扑铁电物理的研究者，DeepMD-kit 提供了一种验证“应变-相变-拓扑”关联的定量手段。它证明了在高度对称的顺电基态材料中，可以通过精确的力学载荷诱导并稳定特定的极性相位。这种从微观电子轨道重构到宏观拓扑构型的协同映射，正是相位锁定性质在计算模拟维度的核心体现。此外，该框架的普适性也使其在研究 SiGe 异质界面吸附 [[../papers/Wu2021]] 及多铁性材料的复杂序参量耦合拟合中展现出巨大潜力 [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]。

## Related Papers

- [[../papers/xuTunableFerroelectricTopological2022]] — 核心引文：利用 DeepMD 势函数验证了二维 PbTe 中应变诱导的类斯格明子极性结构。
- [[../papers/Wu2021]] — 讨论了将机器学习势（MLIP）引入半经验量子化学框架以提升高通量扫描效率的前景。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]] — 综述中提及在处理电荷转移及复杂轨道序耦合时，需对机器学习势函数的描述能力提出更高要求。
