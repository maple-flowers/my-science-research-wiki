---
tags: [entity, material, 2D, SnTe, IV-VI, TCI]
category: [D02, Z01]
---

# 碲化锡 / Tin Telluride (SnTe)

**SnTe** 是一种经典的 IV-VI 族半导体，也是著名的**拓扑晶体绝缘体 (Topological Crystalline Insulator, TCI)**。在原子级厚度极限下，SnTe 展现出稳健的二维面内铁电性，打破了传统铁电体的尺寸效应极限。

## 1. 核心物理特性
### 1.1 二维铁电性 (2D Ferroelectricity)
- **稳健性**：单胞厚度（1-UC）的 SnTe 膜在室温下即可展现出稳定的面内铁电性。
- **反常尺度效应**：其铁电转变温度 $T_C$ 随厚度减小而升高（1-UC 膜 $T_C \approx 270\text{ K}$，4-UC 膜 $T_C \approx 70\text{ K}$），这与传统钙钛矿铁电体（厚度减小则 $T_C$ 降低）截然不同 [[../papers/changDiscoveryRobustInplane2016]]。
- **极化强度**：单层自发极化强度约 **$1.5 \times 10^{-10}\text{ C/m}$**。

### 1.2 拓扑特性与耦合
作为拓扑晶体绝缘体，SnTe 的表面态受晶体镜面对称性保护。
- **铁电-拓扑耦合**：铁电极化产生的结构畸变可以调控能带拓扑，实现电场驱动的拓扑相变。
- **超导与多场耦合**：掺杂后的 SnTe 可表现出超导性，是研究铁电、拓扑与超导共存的理想平台。

## 2. 模拟与方法学
在项目 [[../projects/project-5-snte-ferroelectric-sim]] 中，SnTe 是机器学习势 (MLIP) 研究的重点对象：
- **势函数开发**：利用 [[deep-potential|DeePMD-kit]] 训练针对 SnTe 铁电相变的势函数，以模拟大尺度下的畴壁运动与相变动力学。
- **极化计算**：采用 [[../concepts/berry-phase|Berry Phase]] 方法精确提取不同畸变程度下的自发极化矢量。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_C$, 1-UC)** | $\sim 270\text{ K}$ | 随厚度减小而升高 |
| **自发极化 ($P_{in}$)** | $\sim 1.5 \times 10^{-10}\text{ C/m}$ | 面内极化 |
| **材料类别** | IV-VI 族半导体 | 拓扑晶体绝缘体 |
| **对称性** | Pnma (铁电相) | 褶皱结构 |

## 4. 本库相关代表性论文
- [[../papers/changDiscoveryRobustInplane2016]]：Science 2016，实验首次证实原子级厚度 SnTe 的面内铁电性。
- [[../papers/gaoStrainEngineeringFerroelectric2024]]：APL 2024，在应变调控研究中作为代表性面内铁电材料引用。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：讨论滑动铁电与传统面内铁电（如 SnTe）的关联。

## 5. 关联概念与实体
- [[../concepts/2D-materials|二维范德华材料 2D Materials]]
- [[../concepts/polarization-switching|极化翻转动力学 Polarization Switching Dynamics]]
- [[../entities/PbTe|碲化铅 PbTe]] (对比材料：应变诱导铁电)
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
