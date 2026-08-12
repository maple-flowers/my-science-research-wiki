---
tags: [entity, material, semiconductor, 2D, III-V]
category: [D01, Z02]
---

# 砷化镓 / Gallium Arsenide (GaAs)

**GaAs** 是最著名的 III-V 族半导体之一，具有闪锌矿结构。在从三维块体到二维纳米结构的演化中，GaAs 展现出深刻的“相锁定”物理特性（Phase-Locked Properties）。在本库的知识图谱中，它不仅是验证**现代极化理论** [[../papers/king-smithTheoryPolarizationCrystalline1993]] 和 **PAW 光学计算方法** [[../papers/gajdosLinearOpticalProperties2006]] 的标准基准材料，更是 2025 年提出的“积木组装”稳定性理论中的核心范例 [[../papers/yanDecipheringStabilityTwodimensional2025]]。

## 1. 结构稳定性与积木组装逻辑
二维化 GaAs 的结构预测曾长期依赖直觉，直到 2025 年“积木块（Building Blocks）组装规则”的提出。
- **构建块分解**：通过 DBSCAN 聚类算法，二维 GaAs 的复杂构型可解构为四面体（sp³）、三角形（sp²）和扭曲三角形三种基础单元的灵活组装 [[../papers/yanDecipheringStabilityTwodimensional2025]]。其总能量表现为这些构建块能量的线性叠加，拟合优度 **$R^2 = 0.95$**，证实了“LEGO 式组装”的理性设计范式。
- **能量景观**：四面体构建块对稳定性的能量贡献（$\alpha_{tetra} \approx -0.30$）显著高于三角形单元。由于相同比例的构建块会产生相近的能量值，GaAs 的能量景观呈现出独特的“阶梯状”分布，使得多种准稳态构型（如 Z33, Z13）共存。

## 2. 电子输运与“相锁定”的高迁移率
GaAs 的电子特性与其结构相位高度耦合。在新预测的 **TT 相**（Transition structure）中，GaAs 展现出超越块体的输运性能：
- **空穴迁移率**：理论预测二维 TT-GaAs 的 y 方向空穴迁移率可达 **$1.1 \times 10^5 \text{ cm}^2\text{ V}^{-1}\text{ s}^{-1}$** 数量级 [[../papers/yanDecipheringStabilityTwodimensional2025]]，显著优于传统的 MoS₂ 或黑磷。
- **物理机制**：这种超高迁移率源于“轨道-应变解耦”导致的极低电声耦合。在 TT 相下，价带顶完全由 $p_x$ 轨道占据，对 y 方向的单轴应变极不敏感，导致**形变势常数 ($E_1$)** 骤降。
- **准粒子能带**：利用全频率依赖的 **G₀W₀** 方法计算表明，GaAs 的准粒子能级对 $d$ 电子处理方式极为敏感。通过在 PAW 框架下引入 HF 水平的芯-价相互作用修正，可以获得与全电子方法一致的收敛带隙 [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]]。

## 3. 极化响应与介电性质计算
作为典型的极性半导体，GaAs 是验证计算凝聚态物理核心方法学的里程碑：
- **贝里相位极化**：GaAs 被用于证明晶体电极化变化量 $\Delta P$ 等于价带波函数贝里联络在布里渊区的积分（Zak 相位）[[../papers/king-smithTheoryPolarizationCrystalline1993]]。其压电张量 $\gamma_{14}$ 的计算值（$-0.28 \text{ C/m}^2$）与实验高度吻合，奠定了**现代极化理论**的基础。
- **线性光学响应**：在 PAW 方法中，GaAs 验证了计算频率相关介电函数 $\varepsilon(\omega)$ 时必须采用纵向表达式并引入**偶极矩修正项 ($\mu_{ij}$)**。这一修正项补偿了 PAW 球内赝波函数与全电子波函数的偶极矩差异，使计算精度提升至全电子水平 [[../papers/gajdosLinearOpticalProperties2006]]。

## 4. 主要物性参数
| 参数名称 | 数值 / 构型 | 备注 |
| :--- | :--- | :--- |
| **二维基态** | TT (Transition structure) | 4M+4X 晶胞，矩形对称 [[../papers/yanDecipheringStabilityTwodimensional2025]] |
| **空穴迁移率** | $\sim 10^5 \text{ cm}^2\text{ V}^{-1}\text{ s}^{-1}$ | 二维 TT 相锁定特性 |
| **静态介电常数** | 14.42 (LDA/DFT) | 包含局域场效应 [[../papers/gajdosLinearOpticalProperties2006]] |
| **玻恩有效电荷** | $Z^*_{Ga} \approx 1.98 e$ | 现代极化理论验证值 [[../papers/king-smithTheoryPolarizationCrystalline1993]] |
| **G₀W₀ 带隙** | 1.26 eV (块体) | 实验值 1.52 eV，受多体效应限制 [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]] |

## 5. 本库相关代表性论文
- [[../papers/yanDecipheringStabilityTwodimensional2025]]：二维 III-V 半导体的“积木组装”理论与 TT 相预测。
- [[../papers/king-smithTheoryPolarizationCrystalline1993]]：现代极化理论（Berry phase）的奠基性工作。
- [[../papers/gajdosLinearOpticalProperties2006]]：PAW 框架下精确计算光学性质的方法学标准。
- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]]：VASP 框架下全频率 GW 方法的实现与 GaAs 基准。
