---
tags: [concept, methodology, quantum-simulation, electronics]
category: [M01, Z01]
---

# DFTB+ / 密度泛函紧束缚方法 (Density Functional Tight Binding)

**DFTB+** 是一款基于自洽电荷密度泛函紧束缚 (Self-Consistent Charge Density Functional Tight Binding, SCC-DFTB) 算法的计算软件包。作为一种半经验量子力学方法，DFTB 通过 Slater-Koster 参数化表色，在保持接近密度泛函理论 (DFT) 精度的同时，实现了数量级的计算加速，使其成为研究包含数百至数千原子的大尺度纳米体系（如掺杂纳米管、复杂表面吸附景观）的理想工具 [[../papers/Wei2021]]。

## 晶体结构与几何收缩效应 (Geometric Mechanisms)

在原子尺度模拟中，DFTB+ 能够精确捕捉由化学掺杂或表面重构诱导的几何畸变。
1. **氮环内缩 (N-ring Contraction)**：在类竹节状氮掺杂碳纳米管 (Bamboo-like N-CNTs) 的模拟中，研究发现氮原子环相对于碳原子环表现出明显的向内收缩特征。这种收缩不仅改变了键角（如 C-N-N 与 C-C-N 的对立演化），还导致 C/N 环直径差随手性指数 $n$ 呈现显著的**奇偶振荡 (Odd-Even Oscillation)** 现象 [[../papers/Wei2021]]。
2. **表面吸附景观 (Adsorption Landscape)**：利用 DFTB+ 的高效性，研究者能够对 Ge 二聚体在 Si(001) c(4×2) 重构表面上的吸附行为进行高通量扫描（如 774 个初始构型）。识别出的 8 种稳定吸附模式（如垂直顶位 DVTS、平行桥位 DPBS 等）揭示了吸附高度 $h$ 与倾角 $\theta$ 对能量景观的复杂影响 [[../papers/Wu2021]]。

## 电子能带与属性调控 (Electronic Bands)

DFTB+ 结合 **Mülliken 布居分析 (Mülliken Population Analysis)**，可深入分析体系的电荷转移与能隙演化：
- **能隙振荡与金属性转变**：在 N-CNTs 体系中，能隙随管径增大而减小，且在特定手性下发生金属性转变。这种电子结构的变化由氮掺杂诱导的 $sp^2/sp^3$ 杂化共存及曲率效应共同驱动 [[../papers/Wei2021]]。
- **扰动主导的能隙调控**：在 Ge/Si 异质界面研究中，DFTB+ 计算表明体系能隙的剧烈波动主要源于吸附原子对 Si 衬底二聚体键合状态的局域扰动，而非来自吸附物本身的直接电子贡献 [[../papers/Wu2021]]。

## 相锁定属性与波纹耦合 (Phase-Locked Properties)

在二维铁性材料模拟中，DFTB 级别的方法常被用于构建大尺度模型，以研究面外波纹 (Ripples) 与面内序参量的**相锁定 (Phase-Locked)** 关系。
- **波纹工程 (Ripple Engineering)**：局域曲率通过挠曲电效应与原子级铁性序参量强耦合，稳定的波纹能够形成长寿命的**极性纳米微区 (PNR)**。这些微区在冷却过程中作为异质形核点，显著提升了宏观相变温度 $T_c$ [[../papers/yangRipplingFerroicPhase2021]]。
- **动力学模式转变**：波纹引入的局域应力场会打破畴翻转的长程协同性，使**雪崩动力学 (Avalanche Dynamics)** 从幂律分布的级联行为退化为受波纹位置驱动的局域随机过程（高斯分布） [[../papers/yangRipplingFerroicPhase2021]]。

## 关联概念与实体

- [[../concepts/density-functional-theory|密度泛函理论 DFT]]
- [[../concepts/odd-even-oscillation|奇偶振荡 Odd-Even Oscillation]]
- [[../concepts/atomistic-order-parameter|原子级铁性序参量]]
- [[../concepts/ripples|波纹 Ripples]]
- [[../entities/carbon-nanotubes|碳纳米管 CNTs]]
- [[../entities/GeSe|锗化硒 GeSe]]
