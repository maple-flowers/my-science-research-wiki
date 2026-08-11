# 畴与畴壁结构 (Domains & Domain Walls)

> 收录铁电畴、铁磁畴、畴壁结构、畴壁宽度、极化/自旋翻转动力学畴图相关的关键图表。本页面重点关注二维范德华材料中涌现的极宽畴壁（10-40 nm）及其超快动力学。

[[科研Wiki/wiki/figures/_index|← 返回总索引]]

---

## 🔬 实验成像与可视化 (Experimental Visualization)

### 1. 原子级 STM 可视化 (NiI₂)
在单层 NiI₂ 中，通过扫描隧道显微镜（STM）直接观测到了由自旋螺旋诱导的电极化调制条纹。

![图：单层 NiI₂ 的 STM 表征，显示导带中的电极化条纹与多铁畴](../../raw/figures/aminiAtomicscaleVisualizationMultiferroicity2024/fig_2_U9H48DE6.png)
*   **来源**：[[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]
*   **关键特征**：条纹周期（~1.8 nm）恰为磁螺旋周期的一半，证实了第 II 类多铁性的磁电同源特征。

### 2. PFM/MFM 电写磁读 (CrTe₂)
在室温二维多铁金属 CrTe₂ 中，演示了利用 PFM 写入电畴并由 MFM 读取对应磁畴的过程。

![图：双层 CrTe₂ 中的电写磁读，±7V 写入的盒中盒电畴与磁畴完全对应](../../raw/figures/tianRoomtemperatureTwodimensionalMultiferroic2026/fig_3_85N9YJPF.png)
*   **来源**：[[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]
*   **关键特征**：非易失性磁电耦合，证实了层间电荷转移（ICT）机制驱动的室温多铁性。

![图：磁场依赖的 PFM/MFM，显示外磁场对已写入多铁畴的擦除过程](../../raw/figures/tianRoomtemperatureTwodimensionalMultiferroic2026/fig_4_QKXBGTR6.png)
*   **来源**：[[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]

### 3. 室温铁电金属畴 (WTe₂)
首次在块体半金属 WTe₂ 中探测到室温稳定的铁电畴。

![图：PFM 观测到的 WTe₂ 反平行铁电畴（20–50 nm），相位差约 180°](../../raw/figures/sharmaRoomtemperatureFerroelectricSemimetal2019/fig_2_UK4SYAPY.png)
*   **来源**：[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]
*   **关键特征**：畴壁处 PFM 振幅极小（暗线），揭示了金属屏蔽环境下铁电性的幸存。

---

## 💻 动力学模拟与纹理分析 (Dynamics & Textures)

### 1. 畴壁类型与极化纹理 (h-BN)
基于深度势能（DP）机器学习势的大规模模拟，揭示了滑移铁电体中存在不同对称性的畴壁。

![图：h-BN 双层中的四种畴壁：0° 布洛赫型（平面）与 90° 奈尔型（面外屈曲）](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_5_BK4H4WHC.png)
*   **来源**：[[../papers/heUltrafastSwitchingDynamics2024]]
*   **关键数据**：畴壁宽度极宽（9.7 - 40.7 nm），由极低翻转能垒与高面内刚度共同决定。

### 2. 超快翻转动力学
模拟证实在外电场（或剪切力）驱动下，畴壁运动是实现极化快速翻转的核心机制。

![图：300 K 下 h-BN 畴壁运动快照，两畴壁以 ~6000 m/s 速度在 9 ps 内湮灭](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_6_IH4EUPKK.png)
*   **来源**：[[../papers/heUltrafastSwitchingDynamics2024]]
*   **物理结论**：畴壁运动将临界翻转场降低了两个数量级，预示着皮秒级低功耗存储。

### 3. 莫尔畴壁与 LPRI 模型
在莫尔超晶格中，畴壁宽度受局部极化登记指数（LPRI）控制。

![图：h-BN 莫尔畴壁结构，显示 AB/BA 畴区的扩张与畴壁极化纹理](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_1_AU76XCXF.png)
*   **来源**：[[../papers/kaurRecentAdvancesTheoretical2025a]]

---

## 🛠️ 操控与钉扎机制 (Control & Pinning)

### 1. STM 针尖局域操控
利用 STM 针尖施加电压脉冲，可以实现对原子级多铁畴壁的精确移动。

![图：STM 针尖电压脉冲操控 NiI₂ 多铁畴壁移动，证明了强磁电耦合](../../raw/figures/aminiAtomicscaleVisualizationMultiferroicity2024/fig_4_EDSCRMUC.png)
*   **来源**：[[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]

### 2. 缺陷钉扎效应
解释了为何理论预测为"超顺电"的理想莫尔结构在实验中表现出铁电回滞。

![图：氮空位对 h-BN 畴壁的钉扎能垒（~50 meV），是产生剩余极化的关键](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_8_RY66EXIM.png)
*   **来源**：[[../papers/heUltrafastSwitchingDynamics2024]]

### 3. 特殊物理性质：畴壁金属性
在某些滑动多铁体系中，带电畴壁由于电荷积累可诱导绝缘-金属转变。

![图：ZrI₂ 头对头带电畴壁的电子结构，显示束缚电荷积累诱导的能带弯曲与金属性](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_18_TT3NFJTQ.png)
*   **来源**：[[../papers/kaurRecentAdvancesTheoretical2025a]]

---

## 📐 物理公式与模型 (Formulas & Models)

### 1. 畴壁宽度分析 (One-Dimensional Elastic Model)
用于预测范德华层状铁电体中畴壁宽度的解析公式：

$$ w = \frac{u_0}{2} \sqrt{\frac{\lambda_{1D}}{\Delta}} $$

*   **变量说明**：$u_0$ 为滑移矢量，$\lambda_{1D}$ 为面内拉梅系数（刚度），$\Delta$ 为单位长度翻转能垒。
*   **来源**：[[../papers/heUltrafastSwitchingDynamics2024]]

### 2. 第 II 类多铁极化模型 (Phenomenological Model)
描述自旋螺旋诱导极化的微观公式：

$$ \mathbf{P} = \Lambda \frac{\mathbf{M} \times (\nabla \times \mathbf{M})}{M^2} $$

*   **变量说明**：$\Lambda$ 与自旋-轨道耦合（SOC）强度成正比。该模型预测极化周期为磁螺旋周期的一半。
*   **来源**：[[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]

### 3. VASP 核心算法公式 (Subspace Iteration)
在模拟复杂电子结构（如含 $d$ 电子的多铁体）时，VASP 使用的高效迭代方案公式。

$$ |\bar{f}_k\rangle = \sum_m B_{mk}|f_m\rangle $$

*   **物理意义**：子空间旋转（Subspace Rotation）用于获取精确的本征态近似。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/multiferroicity|多铁性]]、[[../concepts/type-ii-multiferroicity|第 II 类多铁性]]、[[../concepts/magnetoelectric-coupling|磁电耦合]]、[[../concepts/sliding-ferroelectricity|滑移铁电性]]、[[../concepts/moire-superlattice|莫尔超晶格]]、[[../concepts/ferroelectric-domain|铁电畴]]、[[../concepts/domain-wall-motion|畴壁运动]]、[[../concepts/spin-orbit-coupling|自旋–轨道耦合]]、[[../concepts/machine-learning-potential|机器学习势]]、[[../concepts/super-paraelectricity|超顺电性]]

**相关材料/实体**：[[../entities/NiI2|NiI₂]]、[[../entities/CrTe2|CrTe₂]]、[[../entities/WTe2|WTe₂]]、[[../entities/h-BN|h-BN]]、[[../entities/ZrI2|ZrI₂]]、[[../entities/VASP|VASP]]、[[../entities/domain-wall|畴壁]]
