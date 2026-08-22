---
tags: [concept, computational-materials, methodology]
title: 瓦尼尔函数 / Wannier Function
type: concept
status: mature
domain: [electronic-structure, density-functional-theory, methodology]
mechanism: 对 Bloch 态做周期幺正变换得到的实空间局域基函数，是连接第一性原理精确计算与可解释紧束缚模型的桥梁
related_concepts: [tight-binding, berry-phase, modern-polarization-theory, electron-phonon-coupling, charge-density-wave, fermi-surface-nesting]
papers: [Barnett2006coexistence, king-smithTheoryPolarizationCrystalline1993, zhengAnisotropicSuperconductivityTwodimensional2025]
updated: 2026-08
---

# 瓦尼尔函数 / Wannier Function

瓦尼尔函数（Wannier function）是**由布洛赫（Bloch）态经周期幺正变换得到的实空间局域基函数**，由 Gregory Wannier 于 1937 年引入。形式上，能带 n 的瓦尼尔函数为

$$|\mathbf{R}n\rangle = \frac{\Omega}{(2\pi)^3}\int_\mathrm{BZ} e^{-i\mathbf{k}\cdot\mathbf{R}}|\psi_{n\mathbf{k}}\rangle\,d\mathbf{k}$$

其中 $\Omega$ 为原胞体积，$\mathbf{R}$ 为格矢。其核心价值在于：**把周期性倒空间的第一性原理波函数转化为实空间中指数衰减、可解释的局域轨道**，从而作为"降维（downfolding）"的桥梁——既保留第一性原理的精确数值，又给出可供物理分析的紧束缚图像（跃迁积分、对称性、化学键）。

## 👵 太奶导读

太奶，可以把晶体里的电子想象成一群人绕着大楼（晶格）排队跳舞，布洛赫波是说"每个人都知道整支队伍的步法"，太笼统。瓦尼尔函数呢，就是把舞蹈动作拆成一个一个小节拍，每个节拍只发生在某个固定位置附近，跳完就过去——"咦，这一段明明主要在这栋楼门口附近嘛"。这样拆开以后，就可以说"电子从这栋楼门口跳到旁边门口要花多大力气"（跃迁积分），跟邻居的相互作用也看得清清楚楚。科学家还用这招把复杂的大计算"翻译"成简单的小模型，甚至用它直接算出材料的电极化强度和超导临界温度。

## 🧬 构造与最大局域化

布洛赫态在倒空间有任意相位自由度，直接做傅里叶变换得到的瓦尼尔函数可能很弥散。**Marzari–Vanderbilt 最大局域化（MLWF）**通过一组幺正旋转（跨能带混合）在 k 网格上极小化实空间扩展度（局域化泛函），得到指数局域、形状规整的瓦尼尔轨道。构造流程通常由软件（[[../entities/Wannier90|Wannier90]]、EPW）自动完成：先做 DFT 自洽，再投影到初始猜测轨道（如原子轨道、sp³、d 轨道），再迭代最优化。

## 🧰 三大核心用途

1. **降维到最小紧束缚模型**：从第一性原理提取跃迁积分 $\{t_{ij}\}$、格点能 $\epsilon$，构造可解析处理的紧束缚/晶格模型，用于解释物理机制与预测实验（见下 Barnett 范例）。
2. **现代极化理论的核心变量**：电极化变化量等于瓦尼尔电荷中心的位移，是 Berry 相位极化的实空间等价表述。
3. **电声耦合与超导的插值引擎**：以 Wannier 函数为中介把 DFT/DFPT 的电子-声子矩阵元从粗网格插值到任意精细 k/q 网格，支撑 Migdal–Eliashberg 计算（EPW 方法）。

## 🔬 案例一：Barnett 2006 — 瓦尼尔函数形状如何"制造"物理

[[../papers/Barnett2006coexistence]] 通过第一性原理瓦尼尔函数分析，解开了 2H-TaSe₂ 中"公度 CDW 与无隙金属性共存"的谜题：

- 瓦尼尔函数呈 **d_z² 中心 + d_xy/d_x²-y² 尾部**的特殊形状（由 K/H 点 d 轨道杂化所致）；
- 该形状使**最近邻跃迁 t₁ = 38 meV 因尾部相位相消被抑制**，而**次近邻跃迁 t₂ = 115 meV 因相位相长反而主导**；
- 仅保留次近邻跃迁的三角晶格**拓扑分解为三个互不耦合的三角子晶格**（[[../concepts/sublattice-decoupling|子晶格解耦]]）；
- CDW 畸变只扭曲其中两个子晶格，第三个子晶格能带无隙穿过费米面——CDW 与金属性共存由此得到机制解释。

这是 **"DFT + Wannier downfold 到最小模型"范式的经典范例**：第一性原理给精确数值，瓦尼尔函数给可解释的实空间跃迁，最小模型给解析图像与可验证预测。

## 🔬 案例二：King-Smith & Vanderbilt 1993 — 瓦尼尔中心 = 极化

[[../papers/king-smithTheoryPolarizationCrystalline1993]] 证明电极化变化量

$$\Delta P = \frac{fe}{\Omega}\sum_n \mathbf{R}_n$$

即极化变化**等于所有占据态瓦尼尔电荷中心位移之和**，与 Berry 相位（[[../concepts/berry-phase|贝里相位]]）积分在数学上完全等价（式 10）。这一"电子云刚性位移"的图像是抽象几何相位理论的直观入口，并引出规范不变数值算法（式 15）——沿 k 点串计算 $\varphi = \operatorname{Im}\ln\prod_j \det\langle u_{k_j}|u_{k_{j+1}}\rangle$，该算法对每个 k 点本征矢的任意相位不敏感，是 VASP LCALCPOL、Quantum ESPRESSO、ABINIT 等所有现代 Berry 相极化代码的原型。

## 🔬 案例三：zheng 2025 — Wannier 插值驱动超导预测

[[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] 对二维 kagome 金属-有机框架 Cu₃(CO)₆ 预测 Tc = 16.5 K 的各向异性超导性：

- DFPT 声子在 4×4×1 q 网格计算；
- **EPW 在 8×8×1 粗网格构造最大局域化瓦尼尔函数，插值到 40×40×1 细网格**；
- 由此得到动量分辨电声耦合 λ_nk（0.62–1.31）与超导能隙 Δ_nk（5 K 下 2.08–3.90 meV），经各向异性 Migdal–Eliashberg 方程求 Tc。

## 📋 关键参数表

| 参数 | 数值 | 对象与条件 | 证据类型 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| 最近邻跃迁 t₁ | 38 meV（相位相消抑制） | 2H-TaSe₂ d_z² 带 | 计算（Wannier downfold） | [[../papers/Barnett2006coexistence]] |
| 次近邻跃迁 t₂ | 115 meV（相位相长主导） | 2H-TaSe₂ d_z² 带 | 计算 | [[../papers/Barnett2006coexistence]] |
| 层间跃迁 t⊥,1 / t⊥,2 | 29 / 23 meV | 2H-TaSe₂ | 计算 | [[../papers/Barnett2006coexistence]] |
| ΔP = (fe/Ω)ΣR_n | — | 极化=瓦尼尔中心位移（一般关系） | 理论推导 | [[../papers/king-smithTheoryPolarizationCrystalline1993]] |
| EPW 插值网格 | 8×8×1 → 40×40×1 | Cu₃(CO)₆ 电声/超导计算 | 计算 | [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] |

## 📚 相关论文 (Related Papers)

- [[../papers/Barnett2006coexistence]]：瓦尼尔函数形状 → 次近邻主导 → 三子晶格解耦，解释 CDW 与金属性共存。
- [[../papers/king-smithTheoryPolarizationCrystalline1993]]：现代极化理论——极化等于瓦尼尔电荷中心位移，奠定 Berry 相极化算法。
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]：Wannier 插值（EPW）支撑各向异性超导 Tc 的第一性原理预测。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/tight-binding|紧束缚模型]]：Wannier downfold 的直接产物。
- [[../concepts/berry-phase|贝里相位]]：极化、拓扑性质的几何相位框架，与瓦尼尔中心互为等价表述。
- [[../concepts/modern-polarization-theory|现代极化理论]]：以瓦尼尔电荷中心为核心变量的极化理论。
- [[../concepts/electron-phonon-coupling|电子-声子耦合]]：经 Wannier 插值实现任意 k/q 精度的定量计算。
- [[../concepts/charge-density-wave|电荷密度波（CDW）]]：Wannier 分析用于理解 CDW 的微观机制。
- [[../concepts/sublattice-decoupling|子晶格解耦]]：由瓦尼尔跃迁层级结构涌现的物理。
- [[../entities/Wannier90|Wannier90]]：最大局域化瓦尼尔函数构造的标准软件。
- [[../entities/VASP|VASP]]：本库第一性原理计算主软件，与 Wannier90/EPW 联用。
- [[../entities/NbSe2|NbSe₂]]、[[../entities/2H-TaSe2|2H-TaSe₂]]：瓦尼尔分析的主要对象体系。
