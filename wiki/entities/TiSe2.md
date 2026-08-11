---
citekey: TiSe2
title: 1T-二硒化钛 (1T-TiSe2)
tags:
  - entity
  - material/TMDs
  - concept/charge-density-wave
  - concept/superconductivity
---

# 1T-二硒化钛 (1T-TiSe2)

1T-TiSe₂ 是过渡金属二硫族化物（TMDs）中的典型体系，因其在低温下表现出的 $2 \times 2 (\times 2)$ 公度电荷密度波（C-CDW）与超导电性（SC）的复杂竞争与共存关系，成为研究量子相变、激子凝聚及非均匀超导态的原型材料。

## 电子结构与相变基础
- **能带结构**：TiSe₂ 是一种补偿型半金属或窄带隙半导体。费米面由布里渊区中心 $\Gamma$ 点的空穴口袋（Se $4p$ 轨道）和边缘 $M$ 点的电子口袋（Ti $3d$ 轨道）组成。
- **电荷密度波 (CDW)**：在 $T_{CDW} \approx 60\text{ K}$ 时，材料进入 $2 \times 2$ 公度相。与典型的费米面嵌套机制不同，TiSe₂ 的 CDW 被广泛认为由**激子凝聚（Excitonic Condensation）**驱动，即电子与空穴通过库仑相互作用形成束缚对并发生玻色凝聚 [[../papers/yanagizawaSwitchingChargedensityWave2023]]。
- **超导电性 (SC)**：通过电子掺杂（如 Cu 插层、离子门控）或施加压力抑制 C-CDW 后，系统会涌现出一个超导穹顶（Superconducting Dome），最高 $T_c \approx 4\text{ K}$ [[../papers/wuElectrostaticGatingIntercalation2022]]。

## 锁相性质与畴壁物理 (Phase-Locked Properties)
TiSe₂ 的超导起源与其 CDW 相的“锁相”特征密切相关，特别是在公度（C）向非公度（IC）转变的临界区域。

### 错位相子 (Discommensuration, DC) 网络
在近公度（NC）相中，系统并非均匀分布，而是由**公度畴**和将其分隔的**畴壁网络**（即错位相子，DC）组成。
- **Kagome 网络**：理论模型预测，DC 在实空间形成二维 Kagome 超晶格。在 DC 处，CDW 的相位发生 $\pi$ 跳变，且振幅显著下降 [[../papers/Chen2019superconductivity]]。
- **超导成核与渗流**：超导序参量 $\Phi(r)$ 优先在 DC 处成核。随温度降低，系统经历 **0D 点状成核 → 1D 网络渗流 → 2D 全域超导** 的渗流过程。这一非均匀超导态具有配对密度波（PDW）特征。

### Little-Parks 磁阻振荡
在 TiSe₂ 薄膜中观测到的 Little-Parks 振荡可由 DC 网络解释：超导电流被局域在 1D 的 DC 通道中，构成微观超导线网格，磁通量子化导致临界温度随磁场周期性波动 [[../papers/Chen2019superconductivity]]。

## 调控机理
- **强耦合图像**：TiSe₂ 被视为强耦合体系（$2\Delta/k_B T_c \approx 7$）。其 CDW 态可视为“预成型激子液体”在 $T_{CDW}$ 处的相干恢复转变 [[../papers/Koley2020charge]]。
- **无序工程**：非磁性无序（如 S 掺杂）能破坏 CDW 的长程相干性，根据安德森定理，s 波超导对非磁性无序具有鲁棒性，从而释放被 CDW 压制的超导态 [[../papers/Koley2020charge]]。

## 关键实验指纹
- **ARPES**：观测到 $M$ 点处的能带折叠（Band Folding），这是 $2 \times 2$ 超结构的直接证据 [[../papers/yanagizawaSwitchingChargedensityWave2023]]。
- **STM**：在超导穹顶附近的 NC 相中直接观察到数十纳米间距的位错线，并探测到 DC 处局部态密度的增强。

## Related Papers
- [[../papers/Chen2019superconductivity]] — 提出位错驱动超导理论与渗流模型。
- [[../papers/Koley2020charge]] — 讨论强耦合激子凝聚与无序诱导的超导重入。
- [[../papers/yanagizawaSwitchingChargedensityWave2023]] — 通过载流子调谐对比 TiSe₂ 与 TiTe₂ 的 CDW 机制。
- [[../papers/wuElectrostaticGatingIntercalation2022]] — 综述门控与插层对 TiSe₂ 量子相的极端调控。
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] — 引用 TiSe₂ 作为嵌套与电声耦合竞争序的参考。
