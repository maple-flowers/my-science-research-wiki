---
tags: [concept, switching, dynamics, ferroelectric, polarization]
category: [D02, Z01]
---

# 极化翻转与动力学 / Polarization Switching Dynamics

铁电及多铁材料在外加电场、机械应变、光照或热激发作用下，其自发极化矢量发生方向改变（如 $180^\circ$ 反转或 $90^\circ$ 转向）的非平衡动力学过程。极化翻转速率、临界场强度及翻转路径是决定铁电存储器（FeRAM/FTJ）和逻辑器件工作速度与功耗的关键物理指标。

## 1. 经典翻转模型与机制

实际晶体中的极化翻转很少通过单畴均匀翻转（Stoner-Wohlfarth 型，势垒极高）完成，通常遵循以下机制：

- **畴壁核化与生长**：极化翻转始于反向畴的核化（通常在缺陷、晶界或电极界面），随后通过[[../entities/domain-wall|畴壁（Domain Wall）]]的横向运动扩张完成。
- **KAI 模型 (Kolmogorov-Avrami-Ishibashi)**：适用于理想单晶，描述畴在均匀成核后的线性扩张过程。
- **NLS 模型 (Nucleation-Limited Switching)**：适用于多晶或存在无序的系统，翻转速率受限于局部成核时间的分布，表现为展宽的翻转时间特性。

## 2. 二维滑动铁电体的超快动力学

范德华（vdW）二维材料（如双层 [[../entities/h-BN|h-BN]]、[[../entities/TMDs|3R-MoS₂]]）通过层间相对滑动克服弱 vdW 势垒实现极化反转，表现出不同于传统铁电体的动力学特征：

- **皮秒级超快翻转**：[[../papers/heUltrafastSwitchingDynamics2024|Ultrafast switching dynamics of the ferroelectric domain wall]] 研究指出，滑动铁电体在电场驱动下可实现皮秒至纳秒级的翻转。其畴壁运动的临界电场（约 0.026 V/nm）比单畴翻转势垒（约 1.41 V/nm）低近两个数量级。
- **异常宽的畴壁与高速度**：由于层间滑动势垒较低，滑动铁电畴壁异常宽（达 10-40 nm）。模拟显示畴壁移动速度可达 ~6000 m/s，接近声速。其畴壁宽度 $w$ 遵循 1D 弹性模型 $w \propto \sqrt{\lambda_{1D}/\Delta}$，其中 $\lambda_{1D}$ 为一维弹性模量，$\Delta$ 为层间堆垛势垒。
- **滑动声子模式**：极化翻转由软化的“滑动声子（Sliding Phonon）”模式触发，这决定了层间滑动的本征频率限。

## 3. 多场驱动的翻转新范式

- **机械弯曲与扭结（Kinks）**：
  在 [[../papers/heSwitchingTwodimensionalSliding2025|Switching Two-Dimensional Sliding Ferroelectrics by Mechanical Bending]] 中，研究者发现机械弯曲会在双层 vdW 材料中诱导不可逆的扭结（Kink）。扭结本质上是**铁电拓扑畴壁**：
    - **3R-hBN 31° 扭结**：对应 Néel 型畴壁，极化在面内平滑旋转实现反转。
    - **57° 扭结**：对应 Ising 型畴壁，极化在畴壁中心消失并反向。
  这种机制不同于传统的**挠曲电效应（Flexoelectricity）**，其核心是弯曲能与层间堆垛能的竞争导致的局部层间滑动。
- **铁电金属与半金属的电场调控**：
  二维铁电半金属（如 WTe₂）的极化翻转具有特殊的非挥发特性。[[../papers/feiFerroelectricSwitchingTwodimensional2018a|Ferroelectric switching of a two-dimensional metal]] 首次证实了在双层 WTe₂ 中，利用栅极电场调控带边电子结构和层间电荷相关性，可实现室温下的稳定翻转，并伴随双稳态电导特征。

## 4. 莫尔超晶格与缺陷效应

- **超顺电性（Super-paraelectricity）**：在无缺陷的[[moire-superlattice|莫尔超晶格]]中，极化畴在极低场下即可发生可逆运动，表现出零滞后的超顺电特征。
- **缺陷钉扎（Defect Pinning）**：氮空位（$V_N$）等点缺陷会作为畴壁的钉扎中心，在超顺电背景中诱导出迟滞回线，使非挥发存储成为可能。

## 本库相关论文

- **动力学模拟与机制**：
  - [[../papers/heUltrafastSwitchingDynamics2024|Ultrafast switching dynamics of the ferroelectric domain wall]]：利用机器学习势揭示 h-BN 超快畴壁运动。
  - [[../papers/heSwitchingTwodimensionalSliding2025|Switching Two-Dimensional Sliding Ferroelectrics by Mechanical Bending]]：机械弯曲诱导的扭结与极化翻转。
- **二维铁电体系探索**：
  - [[../papers/feiFerroelectricSwitchingTwodimensional2018a|Ferroelectric switching of a two-dimensional metal]]：双层 WTe₂ 铁电金属的发现。
  - [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019|A room-temperature ferroelectric semimetal]]：室温铁电半金属开关特性。
  - [[../papers/yangRipplingFerroicPhase2021|Rippling Ferroic Phase Transition and Domain Switching]]：机械皱褶诱导的相变与翻转。
- **器件应用**：
  - [[../papers/sunSlidingFerroelectricityTwodimensional2025|Sliding ferroelectricity in two-dimensional van der Waals materials]]：综述滑动铁电的翻转特性及其在非易失存储中的应用。

## 关联概念与实体

- [[sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[moire-superlattice|莫尔超晶格 Moiré Superlattice]]
- [[../entities/domain-wall|畴壁 Domain Wall]]
- [[../entities/h-BN|氮化硼 h-BN]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
- [[../entities/deep-potential|机器学习势 Deep Potential]]
