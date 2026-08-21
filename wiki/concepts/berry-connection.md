---
tags: [concept, berry-phase, quantum-geometry, modern-polarization-theory, wannier-function, born-effective-charge]
title: 贝里联络 / Berry Connection
type: concept
status: mature
year: 1984
domain: [condensed-matter-physics, topological-physics, quantum-geometry]
mechanism: 参数空间中量子态相位梯度的规范场，贝里相位与曲率的定义基础
related_concepts: [berry-phase, berry-curvature, quantum-geometric-tensor, modern-polarization-theory, wannier-function, born-effective-charge]
papers: [king-smithTheoryPolarizationCrystalline1993]
updated: 2026-08
---

# 贝里联络 / Berry Connection

贝里联络 (Berry connection, 记作 $\mathcal{A}_n(k) = i\langle u_{n,k}|\nabla_k u_{n,k}\rangle$) 是定义在参数空间（如动量空间）上的**规范场**，描述第 $n$ 条能带 Bloch 波函数随参数（波矢 $k$）变化时积累的相位梯度。它是贝里相位、贝里曲率、陈数等一系列量子几何与拓扑概念的微分学基础，也是现代极化理论的核心构建块。

## 👵 太奶导读

乖孙，你要是想知道材料里的电子"走位"有多玄妙，得先认识这个"贝里联络"。
想象你爬山，手里拿一个指南针。你沿着一条路走一圈回到原点，指南针可能已经不是原来的方向了——多转出来的那个角度，就是"贝里相位"。而"贝里联络"就是描述你每走一小步时指南针会偏多少的那个"偏转说明书"。它本身随你怎么标注方向（规范）而变，但把一圈的偏转加起来得到的角度却是固定的，能告诉我们电子的量子态在能带里"转了多大一个圈"。

## 🏗️ 结构概览

贝里联络是量子几何的语言起点：由它可积分得到贝里相位（闭合路径环绕数），由其旋度得到贝里曲率（规范不变的物理量），再由贝里曲率的积分得到陈数等拓扑不变量。它在规范变换下不不变（类似电磁矢势 $\mathbf{A}$），因此单独数值依赖规范选择，但由它构造的闭合路径积分（贝里相位）与曲率均规范不变。

## 🧩 核心内容与机制 (Core Content)

- **定义**：对含参哈密顿量 $H(\lambda)$ 的本征态 $|n(\lambda)\rangle$，贝里联络定义为
  $$\mathcal{A}_n(\lambda) = i\langle n(\lambda)|\nabla_\lambda n(\lambda)\rangle$$
  在动量空间中即 $\mathcal{A}_n(k) = i\langle u_{n,k}|\nabla_k u_{n,k}\rangle$（$u_{n,k}$ 为周期部分）。
- **规范依赖**：在相位变换 $|u_{n,k}\rangle \to e^{i\chi(k)}|u_{n,k}\rangle$ 下，联络按 $\mathcal{A}_n(k) \to \mathcal{A}_n(k) - \nabla_k\chi(k)$ 变换——与电磁矢势完全类比。
- **与贝里相位的关系**：闭合路径 $C$ 上的贝里相位 $\gamma_n = \oint_C \mathcal{A}_n(k)\cdot dk$，是规范不变的（模 $2\pi$）。
- **现代极化理论**：晶体电子极化 $\mathbf{P}$ 的量子表达以贝里联络为核（Berry phase 表示），King-Smith 与 Vanderbilt 于 1993 年建立了晶格极化与贝里相位（联络沿路径积分）的严格等价，使铁电极化成为可计算量（[[../papers/king-smithTheoryPolarizationCrystalline1993|King-Smith & Vanderbilt 1993]]）。

## 📋 关键参数表

| 参数 | 含义 | 规范性质 |
|---|---|---|
| 贝里联络 $\mathcal{A}_n(k)$ | 量子态相位梯度 | 规范依赖 |
| 贝里相位 $\gamma_n$ | 闭合路径积分 | 规范不变（模 2π） |
| 贝里曲率 $\Omega_n(k)$ | 联络的旋度 | 规范不变 |
| 极化 $\mathbf{P}$ | 现代极化理论核心量 | 模量子 $eR/\Omega$ 不确定 |

## 🔀 近邻概念辨析

- **贝里联络 vs 贝里曲率**：联络是"矢势"，依赖规范；曲率是"磁场"，规范不变。物理可观测量由后者（或其积分）承载。
- **贝里联络 vs 电磁矢势**：结构完全类比（规范场），但贝里联络作用在量子态空间而非实空间。
- **贝里联络 vs 现代极化理论**：现代极化理论用贝里联络（相位）计算极化差，是联络最重要的实际应用。

## 📚 相关论文 (Related Papers)

- [[../papers/king-smithTheoryPolarizationCrystalline1993]] — 建立了晶格极化与贝里相位（联络路径积分）的等价性，奠定现代极化理论。

## 🔗 关联概念与实体 (Related)

- [[../concepts/berry-phase|贝里相位]]：联络的闭合路径积分。
- [[../concepts/berry-curvature|贝里曲率]]：联络的旋度，规范不变的量子几何量。
- [[../concepts/modern-polarization-theory|现代极化理论]]：以联络计算铁电极化。
- [[../concepts/wannier-function|Wannier 函数]]：与联络互补的实空间基组。
- [[../concepts/born-effective-charge|Born 有效电荷]]：极化的响应量，依赖联络框架。
- [[../entities/GaAs|GaAs]]：极化计算经典测试体系。
- [[../entities/Wannier90|Wannier90]]：基于联络/相位提取极化的主流软件。
*（内容由AI生成，仅供参考）*