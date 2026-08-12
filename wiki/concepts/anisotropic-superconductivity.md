---
title: 各向异性超导
type: concept
tags: [concept, superconductivity, many-body-physics]
---

# 各向异性超导 (Anisotropic Superconductivity)

各向异性超导是指超导能隙 $\Delta_{n\mathbf{k}}$ 在费米面上随动量 $\mathbf{k}$ 变化而表现出不均匀分布的超导态。与传统 BCS 理论中的各向同性能隙（能隙大小在费米面上为常数）不同，各向异性超导体系虽然通常仍属于单能隙（Single-gap）范畴（即能隙在费米面上是连续分布的，而非像多带超导体那样存在离散的能隙分支），但其配对强度受到电子轨道、带特征及声子模式各向异性的强烈调制。

## 1. 物理机制与微观驱动

各向异性超导的形成通常与材料的低维特性、复杂的费米面拓扑以及特定波矢下的强电-声耦合（EPC）密切相关。

- **电子-声子相互作用 (EPC)**：在电-声耦合驱动的超导体中，总耦合强度 $\lambda$ 是动量分辨耦合 $\lambda_{n\mathbf{k}}$ 的平均值。如果电子态在费米面不同区域与特定声子模式的散射概率差异巨大，则会产生显著的各向异性。
- **费米面嵌套 (Fermi Surface Nesting)**：嵌套效应通过增强特定波矢 $\mathbf{q}$ 处的电子磁化率 $\chi(\mathbf{q})$，能够显著提升该波矢附近的电声耦合强度。在 [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] 研究的二维 kagome 框架 $\text{Cu}_3(\text{CO})_6$ 中，费米面嵌套被确认为增强电声耦合并诱导各向异性超导的关键微观机制。

## 2. 相位锁定属性 (Phase-Locked Properties)

在“相位锁定”的研究框架下，各向异性超导体现了晶体结构、电子局域化程度与配对对称性之间的紧密关联：

- **晶格对称性与轨道杂化**：以二维金属-有机框架 (2D-MOFs) 为例，$\text{Cu}_3(\text{CO})_6$ 的 kagome 几何结构导致了独特的电子能带结构，包括狄拉克锥、平带 (Flat band) 和范霍夫奇点 (VHS)。这种 $\pi-d$ 共轭效应锁定了费米面附近的电子态特征，使得 $\text{Cu}$ $d_{xy,x^2-y^2}$ 和 $\text{O}$ $s+p_{x,y}$ 轨道对超导配对的贡献远大于其他轨道。
- **能隙分布分布**：通过求解各向异性 Migdal-Eliashberg 方程，可以精确描绘能隙在费米面上的拓扑分布。在 $\text{Cu}_3(\text{CO}_6)$ 中，费米面包含 $\pi_1$、$\pi_2$ 和 $\delta$ 三片。由于轨道分辨耦合强度的不同，$\delta$ 带表现出最强的配对强度，导致能隙在 2.08 meV 到 3.90 meV 之间连续波动，临界温度 $T_c$ 达到 16.5 K [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]。

## 3. 实验表征与判定

各向异性超导可以通过以下手段进行识别：
- **各向异性 Migdal-Eliashberg 计算**：利用 [[../entities/Wannier90|Wannier 函数插值]] 和 [[../entities/EPW|EPW]] 代码，从第一性原理角度预测动量分辨的能隙值。
- **隧道谱 (Tunneling Spectroscopy)**：观测超导态准粒子态密度 (DOS) 中的相干峰加宽或多峰结构。
- **比热测量**：各向异性能隙会导致比热在极低温度下的行为偏离标准 BCS 的指数下降规律。

## 4. 相关文献

- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] — 预测二维 Cu₃(CO)₆ 中的各向异性单能隙超导，并揭示其电声耦合由费米面嵌套驱动。
- [[../papers/lezoualchStudyChargeDensity]] — 讨论了 TMDs 中电荷密度波与超导的竞争，这种竞争往往发生在具有强烈各向异性特征的体系中。

## 5. 关联概念与实体

- 概念：[[../concepts/electron-phonon-coupling|电子-声子耦合]]、[[../concepts/fermi-surface-nesting|费米面嵌套]]、[[../concepts/kagome-lattice|笼目晶格]]
- 实体：[[../entities/Cu3CO6|Cu₃(CO)₆]]、[[../entities/EPW|EPW]]、[[../entities/Quantum-ESPRESSO|Quantum ESPRESSO]]
