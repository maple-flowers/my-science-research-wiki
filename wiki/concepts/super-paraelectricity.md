---
tags: [concept, super-paraelectric, moire, ferroelectricity, sliding-ferroelectricity]
category: [D02]
---

# 超顺电性 / Super-paraelectricity

## 定义与类比
**超顺电性 (Super-paraelectricity)** 是铁电体系在极小尺寸或高畴壁迁移率下表现出的一种特殊物理状态。其物理图景类比于磁学中的**超顺磁性 (Superparamagnetism)**：
1. **局部有序**：体系内部存在局部自发极化（铁电畴）。
2. **宏观无极化**：在零电场下，由于热涨落或畴壁极易移动且无钉扎，局部极化方向随机化或畴区大小相等，导致宏观净极化为零。
3. **响应特性**：施加外电场时，局部畴迅速对齐达到极化饱和；撤场后极化迅速消失。其 **P-E 回线表现为可逆且无滞后 (Non-hysteretic)** 的特征。

## 二维莫尔结构中的机制
在二维范德华材料及其莫尔超晶格（Moiré Superlattices）中，超顺电性主要源于[[../../raw/note/wuSlidingFerroelectricity2D2021a.md|滑动铁电性 (Sliding Ferroelectricity)]] 的动力学特性。

### 1. 莫尔畴与极化
通过微小扭转（Twist）形成的莫尔结构（如双层 h-BN 或 MoS₂）会产生周期性的 AB 和 BA 堆垛畴区，分别对应向上和向下的面外极化。

### 2. 畴壁动力学 (Domain Wall Dynamics)
超顺电性的存在取决于畴壁（DW）的移动障碍：
- **超顺电态**：在高质量、无缺陷的扭转结构中，畴壁具有极高的迁移率（如“孤子型”或“纹波型”运动），极低的外场即可驱动畴壁移动使某一种极化畴扩张。
- **铁电态转变**：当体系中存在缺陷（如氮空位 $V_N$）或应变梯度时，畴壁会被钉扎（Pinning）。钉扎效应引入了翻转障碍，使 P-E 回线产生滞后，体系从超顺电态转变为宏观铁电态。

## 典型材料与实验发现
### 双层扭转 h-BN
在 [[../../raw/note/heUltrafastSwitchingDynamics2024.md|He et al. (2024)]] 的研究中：
- **极低饱和场**：对于 0.385° 的扭转 h-BN 莫尔结构，仅需 **0.026 V/nm** 的超低偏置场即可实现极化饱和，且过程无滞后，表现出典型的超顺电行为。
- **超快响应**：由于翻转机制涉及的是整体层间滑动而非原子重新成核，其开关速度极快。
- **缺陷诱导转变**：研究通过氧等离子体引入氮空位缺陷，成功将无滞后的超顺电态转变为具有典型铁电滞后回线的状态。

### 其他候选体系
- **3R 相 TMDs**：如 3R-MoS₂，利用其本征非中心对称性结合滑动机制实现极化开关（参见 [[../../raw/note/sunSlidingFerroelectricityTwodimensional2025.md|Sun et al. (2025) 综述]]）。
- **小角度扭转石墨烯**：在特定衬底或异质结条件下诱导的界面铁电性。

## 核心意义
- **低功耗器件**：超顺电性提供了极低电压驱动极化翻转的可能性。
- **物理演化**：它揭示了从局部滑动极化到宏观有序铁电性的演化路径，强调了畴壁钉扎（Domain wall pinning）在宏观铁电性形成中的决定性作用。

## 本库相关
- [[../../raw/note/heUltrafastSwitchingDynamics2024.md]]（h-BN 莫尔超顺电实验证据）
- [[../../raw/note/wuSlidingFerroelectricity2D2021a.md]]（滑动铁电机制探讨）
- [[../../raw/note/sunSlidingFerroelectricityTwodimensional2025.md]]（2D 滑动铁电综述）
- [[../entities/domain-wall]]（畴壁动力学与钉扎）
