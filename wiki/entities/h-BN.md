---
tags: [entity, material, 2D, h-BN, sliding-ferroelectricity, moire]
category: [D02, Z01]
---

# 六方氮化硼 / Hexagonal Boron Nitride (h-BN)

**六方氮化硼 (h-BN)** 是一种由硼 (B) 和氮 (N) 原子交替排列构成的二维范德华绝缘体（带隙 $\sim 5.9\text{ eV}$）。由于其原子级平整表面、无悬挂键及极高的力学/电学稳定性，h-BN 被誉为“二维材料界的白石墨烯”。

## 1. 滑动铁电性 (Sliding Ferroelectricity)
单层 h-BN 具有反演中心，不具备铁电性。但在双层堆叠体系中，h-BN 是**滑动铁电性**的原型材料 [[../papers/heUltrafastSwitchingDynamics2024]]：
- **物理机制**：平行堆叠的双层 h-BN 在 AB 与 BA 构型下打破了垂直反演对称性，导致层间发生自发电荷转移。
- **自发极化**：垂直电极化强度 $P_z \approx 0.68\text{ pC/m}$。
- **极化翻转**：通过层间沿面内滑动极小距离（$\sim 1.44\text{ \text{\AA}}$）即可实现极化翻转。这种翻转路径具有极低的能量势垒，不涉及穿层原子位移。

## 2. 莫尔超晶格与超顺电性
当双层 h-BN 发生微小角度扭转时，会形成**莫尔超晶格 (Moiré Superlattice)**：
- **畴结构**：莫尔周期内自动划分出三角形的 AB 和 BA 铁电畴。
- **超顺电态 (Super-paraelectricity)**：理想扭转双层 h-BN 的 $P\text{--}E$ 曲线无回滞，表现为超顺电行为 [[../papers/heUltrafastSwitchingDynamics2024]]。
- **缺陷钉扎**：实验中观察到的铁电回滞通常归因于点缺陷（如氮空位 $V_N$）对畴壁的钉扎效应（钉扎能 $\sim 50\text{ meV}$）。

## 3. 畴壁动力学
h-BN 具有极宽的铁电畴壁和极快的动力学响应：
- **超宽畴壁**：其畴壁宽度 $w$ 达到 **$10\text{--}40\text{ nm}$**，由高面内刚度与低翻转势垒共同决定。
- **皮秒开关**：畴壁运动将翻转电场降低了两个数量级（$\sim 0.026\text{ V/nm}$），在电场驱动下畴壁速度可达 **$6000\text{ m/s}$**，实现皮秒级超快逻辑切换。

## 4. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **带隙 ($E_g$)** | $\sim 5.9\text{ eV}$ | 宽禁带绝缘体 |
| **自发极化 ($P_z$)** | $0.68\text{ pC/m}$ | 双层滑动极化 |
| **畴壁宽度 ($w$)** | $9.7\text{--}40.7\text{ nm}$ | 范德华超宽畴壁 |
| **滑移距离** | $\sim 1.44\text{ \text{\AA}}$ | 极化翻转位移 |
| **介电常数 ($\varepsilon$)** | $\sim 3\text{--}4$ | 低介电衬底 |

## 5. 本库相关代表性论文
- [[../papers/heUltrafastSwitchingDynamics2024]]：Acta Mater. 2024，系统研究 h-BN 双层滑动铁电畴壁与莫尔超快动力学。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：综述 h-BN 在滑动铁电隧道结（FTJ）与神经形态器件中的应用。
- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]：利用 h-BN 莫尔超晶格构建超灵敏光电传感器阵列。
- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：计算模拟的基础 PAW 方法。

## 6. 关联概念与实体
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[../concepts/super-paraelectricity|超顺电性 Super-paraelectricity]]
- [[domain-wall|畴壁 Domain Wall]]
- [[deep-potential|机器学习势 Deep Potential]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
