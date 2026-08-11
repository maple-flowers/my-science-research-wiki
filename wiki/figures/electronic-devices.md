# 电子与突触器件 (Electronic & Synaptic Devices)

> 收录多铁/铁电器件应用分类、滑移铁电器件综述脉络，以及支撑器件模拟的电子结构迭代算法核心公式。重点关注非易失存储、自旋电子、传感器及神经形态突触器件的应用场景与性能指标。

[[科研Wiki/wiki/figures/_index|← 返回总索引]]

---

## 🔌 器件应用与分类 (Device Applications & Categories)

### 1. 二维多铁材料的器件应用矩阵
该表归纳了二维多铁材料在不同电子系统中的应用类别、所依托的物理效应及关键器件/指标，覆盖从非易失存储到微波相移器的七大方向。

| 应用类别 | 依托效应 | 关键指标/器件 |
|---|---|---|
| 非易失存储 | 铁电极化+自旋的磁电耦合 | 四态隧道效应、磁性切换 |
| 自旋电子 | 磁电耦合 | 自旋场效应晶体管、多铁隧道结 |
| 传感器 | 磁电效应 | 磁场感知探测器 |
| 制动器 | 压电/磁致伸缩 | 低功耗柔性致动 |
| 能量收集 | 磁电耦合 | 复合电压压电/磁致伸缩材料 |
| 微波/RF | 磁电效应 | 可调滤波器、天线、FMR 调谐 |
| 相移器 | 电磁耦合 | 微波相控阵雷达、通讯 |

*   **来源**：[[../papers/RecentAdvancesGrowth2025]]
*   **关键特征**：铁电极化与自旋自由度的磁电耦合是实现四态存储与低功耗自旋电子器件的共同物理基础。
*   **另见**：同表亦以 HTML 形式收录于 [[experimental-setups#🔧 器件制备流程与架构 (Device Fabrication & Architectures)|实验测试与测量装置]] 与 [[vibrational-spectra#🧲 二维多铁材料体系综述 (2D Multiferroic Systems Overview)|振动能谱与声子谱]]。

### 2. 滑移铁电器件综述脉络
该表列出了二维滑移铁电综述各章节的主题与核心内容，其中第五章系统梳理了铁电场效应晶体管（FeFET）、铁电突触器件、铁电隧道结（FTJ）等器件应用。

| 章节 | 主题 | 核心功能 |
|---|---|---|
| 第 1 章 | 引言 | 概述铁电材料历史、传统材料的尺寸瓶颈、滑移铁电的发现背景与综述定位 |
| 第 2 章 | 滑移铁电基本原理 | 阐述滑移铁电的物理机制、极化产生模式、结构构筑途径与理论模型 |
| 第 3 章 | 制备与表征方法 | CVD/PVD/机械剥离与堆叠工艺；矢量 PFM、电学表征、SHG、TEM |
| 第 4 章 | 二维滑移铁电材料体系 | 石墨烯、h-BN、TMDs、MXene、异质结、InSe 等材料 |
| 第 5 章 | 滑移铁电器件应用 | FeFET、铁电突触器件、FTJ、逻辑存储器件、光伏随机存储器 |
| 第 6 章 | 总结与展望 | 大规模制备、性能调控、多功能器件、热稳定性、产业化五大方向 |

*   **来源**：[[../papers/sunSlidingFerroelectricityTwodimensional2025]]
*   **关键特征**：滑移铁电的原子级厚度与层间切换机制使其成为后摩尔时代低功耗神经形态器件的候选体系。

---

## 📐 电子结构迭代算法 (Electronic-Structure Iterative Algorithms)

### 1. 电荷密度混合残差矢量 (Residual Vector for Charge Mixing)
在自洽循环中，残差矢量定义为输出电荷密度与输入电荷密度之差，是 Broyden/Pulay 混合方案更新电荷密度的核心量。

$$ R[\rho_{\text{in}}] = \rho_{\text{out}} - \rho_{\text{in}} $$

*   **变量说明**：$\rho_{\text{out}}$ 由当前波函数按方程 (3) 计算得到；$R[\rho_{\text{in}}]$ 结合前序混合步信息用于构造下一循环的 $\rho_{\text{in}}$。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 2. 子空间旋转变换 (Subspace Rotation)
在迭代对角化中，将试探波函数在子空间内线性组合，以获得精确最低本征值与本征矢的最佳近似。

$$ |\bar{f}_k\rangle = \sum_m B_{mk} |f_m\rangle $$

*   **变量说明**：$|f_m\rangle$ 为当前试探波函数，$B_{mk}$ 为子空间旋转矩阵系数，$|\bar{f}_k\rangle$ 为旋转后近似本征态。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 3. 显式正交化的计算标度 (Cost of Explicit Orthogonalization)
序贯共轭梯度算法中，每个能带更新时新梯度必须与所有其他能带正交化，其操作量随能带数呈三次方标度，是大规模计算的主要内存带宽瓶颈。

$$ T_{\text{ort}} = 2 N_b^2 N_{\text{plw}} \approx 2 N^3 $$

*   **变量说明**：$N_b$ 为能带数，$N_{\text{plw}}$ 为平面波数；Gram-Schmidt 正交化因数据局部性更好，耗时通常比显式正交化低 4–8 倍。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/multiferroicity|多铁性]]、[[../concepts/magnetoelectric-coupling|磁电耦合]]、[[../concepts/sliding-ferroelectricity|滑移铁电]]、[[../concepts/ferroelectric-tunnel-junction|铁电隧道结 (FTJ)]]、[[../concepts/multiferroic-tunnel-junction|多铁隧道结]]、[[../concepts/piezoelectricity|压电效应]]、[[../concepts/neuromorphic-computing|神经形态计算]]、[[../concepts/synaptic-plasticity|突触可塑性]]、[[../concepts/density-functional-theory|密度泛函理论 (DFT)]]

**相关材料/实体**：[[../entities/VASP|VASP]]、[[../entities/h-BN|六方氮化硼 (h-BN)]]、[[../entities/TMDs|过渡金属二硫化物 (TMDs)]]、[[../entities/MXenes|MXenes]]、[[../entities/graphene|石墨烯]]
