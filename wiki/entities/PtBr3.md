---
tags: [entity, material, altermagnet, 2D, sliding-ferroelectricity, magnetic, phase-locked]
category: [D01, Z02]
---

# 三溴化铂 / Platinum Tribromide (PtBr3)

**PtBr3** 是一种典型的**滑动铁电交变磁体 (Sliding Ferroelectric Altermagnet)**。它通过范德华层间滑动打破空间反演对称性 ($P$) 和时间反演对称性 ($T$) 的乘积对称性 ($PT$)，从而在零净磁矩的状态下诱导出受极化方向锁定的自旋能带劈裂 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 1. 相位锁定物性 (Phase-Locked Properties)

PtBr3 的核心价值在于其电、磁、光三个自由度的深度耦合，展现出清晰的**相位锁定**特征：

### 1.1 极化-自旋劈裂锁定 (Polarization-Locked Altermagnetism)
- **对称性机制**：在 $AA'$、$AB'$ 或 $AC'$ 堆垛中，层间滑移产生的垂直极化 $P_z$ 破坏了系统的 $PT$ 对称性。
- **交变磁性**：系统虽然保持共线反铁磁（AFM）排列且净磁矩为零，但由于 $PT$ 破缺，布里渊区内的能带发生巨大的自发自旋劈裂。
- **锁定效应**：极化方向的翻转（$P \to -P$）会直接导致自旋劈裂能带的符号反转，实现对交变磁性态的非易失电学切换。

### 1.2 极化-磁光响应锁定 (Optical Fingerprints)
- **MOKE 锁定**：磁光克尔效应 (MOKE) 的响应与铁电极化相位严格对应。极化反转会引起克尔角 ($\theta_K$) 和椭偏率的显著变化。
- **晶体霍尔效应 (Crystal Hall Effect)**：由于贝里曲率在动量空间的非对称分布，PtBr3 在零磁场下产生的自发霍尔电压方向受极化相位调制 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 2. 物理参数与特征

| 特性分类 | 物理表现 | 备注 |
| :--- | :--- | :--- |
| **序参量起源** | 层间滑动 (Sliding) | 克服位移铁电的尺寸极限 |
| **磁相序** | 交变磁性 (Altermagnetic) | 零磁矩下的高频自旋响应 |
| **读出信号** | MOKE / 晶体霍尔电压 | 相位锁定，非易失读取 |
| **层间耦合** | $d_z^2 - p_z$ 杂化 | 电子起源的极化机制 |

## 3. 关联论文与路径 (Two-Layer Architecture)

PtBr3 的研究主要建立在对层间相互作用与对称性破缺的深入理解之上：

- [[../papers/kaurRecentAdvancesTheoretical2025a]]：综述了 PtBr3 中 $PT$ 对称性破缺的群论分析，以及 MOKE 信号随极化相位演化的理论预言。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：讨论了二维范德华多铁体系中电荷、自旋与拓扑自由度的高度集成与调控。
- **原始笔记**：详细计算过程参见 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 4. 关联概念与实体
- [[../concepts/altermagnetism|交变磁性 Altermagnetism]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../entities/MnPSe3|MnPSe3]] (另一类典型的滑动诱导交变磁体)
- [[../projects/project-2-mn-multiferroics|Project-2]] (锰基/过渡金属多铁性研究)
