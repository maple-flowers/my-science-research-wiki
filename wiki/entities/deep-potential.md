---
tags: [entity, method, mlip, deepmd, dft, simulation]
category: [Z01, D02]
---

# 机器学习势 / Deep Potential (DPMD/DP-Gen)

**机器学习势 (Machine Learning Interatomic Potential, MLIP)** 是一种利用深度神经网络拟合第一性原理密度泛函理论（DFT）势能量曲面（PES）的原子间势函数方法。其核心目标是在保持 DFT 级精度的前提下，实现大规模、长时标的原子动力学模拟。代表性开源工具包为 **DeePMD-kit** 与 **DP-Gen**。

## 1. 核心物理与算法架构

### 1.1 描述符与对称性 (Smooth Descriptor)
DeePMD 通过深度神经网络将局部原子环境（原子坐标）映射为标量能量。为了满足物理约束，其采用了**光滑描述符 (Smooth Descriptor)**，通过局部坐标系与径向分布函数确保了能量对体系的**平移不变性**、**旋转不变性**与**置换不变性**（同种原子交换位置能量不变）。这种端到端的映射避免了人为选取描述符的主观性。

### 1.2 DP-Gen 主动学习工作流
通过 **主动学习 (Active Learning)** 的闭环迭代极大提升了训练数据效率：
1. **探索 (Exploration)**：利用当前的 DP 模型进行大规模分子动力学（MD）采样。
2. **筛选 (Labeling)**：利用多个并行训练模型之间的预测偏差（Model Deviation, $\sigma_f$）评估不确定性。
3. **训练 (Training)**：仅对偏差较大的“关键构型”进行 DFT 标注并加入训练集，不断通过迭代（如 [[../papers/heUltrafastSwitchingDynamics2024]] 中的 23 轮迭代）演化出鲁棒的势函数。

## 2. 相位锁定性质与堆垛工程 (Phase-Locked Properties)

在二维滑动铁电与多铁材料研究中，Deep Potential 方法成功揭示了“相位锁定”现象——即宏观物理性质（如电极化、拓扑序）与微观原子堆垛相位（Stacking Phase）的深度耦合。

### 2.1 超快畴壁动力学
传统 DFT 模拟受限于数百个原子，无法捕捉宏观翻转过程。[[../papers/heUltrafastSwitchingDynamics2024]] 利用 DP 模型对包含数十万原子的 [[../entities/h-BN|h-BN]] 双层进行了皮秒尺度的模拟。
- **孤子运动**：发现滑动铁电翻转遵循畴壁运动机制，畴壁在电场驱动下表现出类孤子（Soliton-like）运动，速度高达 $6000\text{ m/s}$。
- **尺度效应**：计算揭示其畴壁宽度（$10\text{-}40\text{ nm}$）远超传统氧化物铁电体，这归因于范德华材料极低的面外翻转势垒与极高的面内化学键刚度。

### 2.2 弯曲诱导的拓扑扭结 (Mechanical Kinks)
在应变工程研究中，[[../papers/heSwitchingTwodimensionalSliding2025]] 证明机械弯曲会在双层体系中诱导不可逆的**扭结 (Kinks)**。
- **能量竞争**：扭结的形成是弯曲弹性能与层间范德华堆垛能（vdW Stacking Energy）竞争的结果。
- **极化翻转**：扭结中心锚定了 SP（鞍点）或 AA（高对称不稳态）堆垛，分别对应 Néel 型与 Ising 型拓扑畴壁。这实现了一种无需电场的“类挠曲电”翻转模式。

## 3. 计算优势与科研价值

Deep Potential 彻底解决了量子力学模拟中的“不可能三角”：
- **高精度**：能量误差可控制在 $1\text{ meV/atom}$ 以下，力误差优于 $0.05\text{ eV/\AA}$。
- **大规模**：可轻松模拟 $10^5 \sim 10^7$ 原子体系，使得[[../concepts/moire-superlattice|莫尔超晶格]]的真实物理状态表征成为可能。
- **长时标**：支持纳秒（ns）级别的模拟，能够揭示相变过程中的缺陷钉扎机制（如氮空位 $V_N$ 对畴壁的锚定效应）。

## 4. 本库相关项目与论文
- **项目连接**：[[../projects/project-5-snte-ferroelectric-sim]]（利用 MLIP 探索 SnTe 铁电相变与畴壁动力学）；[[../projects/project-4-ttf-molecular-simulation]]（利用并发学习流程构建复杂分子晶体势函数）。
- **代表性论文**：
    - [[../papers/heUltrafastSwitchingDynamics2024]]：揭示堆垛工程铁电体中铁电有序的超快开关动力学。
    - [[../papers/heSwitchingTwodimensionalSliding2025]]：机械弯曲切换二维滑动铁电体的力学诱导机制。
    - [[../papers/Zhang2019a]]：DeePMD-kit 核心算法描述。

## 5. 关联概念与实体
- [[../concepts/machine-learning-potential|机器学习势 Concept Page]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../entities/domain-wall|畴壁 Domain Wall]]
- [[../entities/h-BN|六方氮化硼 h-BN]]
- [[../entities/VASP|VASP 计算软件]]
- [[../entities/deep-potential|Deep Potential (此条目)]]
