---
tags: [concept]
title: '赝势 / Pseudopotential'
type: concept
status: developing
papers: ['blochlProjectorAugmentedwaveMethod1994b', 'Delley2000', 'kresseInitiomolecularDynamicsLiquid1993', 'perdewGeneralizedGradientApproximation1996a', 'tangGridbasedBaderAnalysis2009']
updated: 2026-08-18
---

# 赝势 / Pseudopotential

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


赝势（pseudopotential）是**用有效势替代原子实（core）与价电子之间的真实库仑势，使波函数在芯区平滑化**的方法，它保留价电子在成键区的正确行为而省去芯态振荡，从而显著降低平面波基组规模。与投影缀加波（PAW）、全电子方法并列，是 DFT 平面波计算（VASP、Quantum ESPRESSO 等）的三大电子结构方法之一。

## 👵 太奶导读

原子里的电子分两层：内层（芯电子）跟原子核"抱得很紧"，几乎不参与化学键；外层（价电子）才真正决定材料的性质。但精确计算时，芯电子那种"贴着核剧烈抖动"的波函数要花大量计算资源才能描述。赝势的妙招是：假装把内层"糊掉"，用一个"假势"代替，让外层电子的行为完全不变，但计算量骤减——就像处理一栋楼只关心外墙装饰、不细算每块砖，省时又不失精度。

## 🧩 方法与家族

赝势家族包括范数守恒赝势（NCPP，见 [[../concepts/norm-conserving-pseudopotential|norm-conserving pseudopotential]]）、超软赝势（USPP）与**投影缀加波（PAW）**。PAW 通过全电子分波、赝分波与投影函数定义的线性变换，统一了全电子 LAPW 的精度与平面波赝势的效率，并首次实现基于完整波函数的能量守恒第一性原理分子动力学（[[../papers/blochlProjectorAugmentedwaveMethod1994b|Blöchl 1994]]）。

## 🔬 赝势支撑的关键计算工具

- **DMol3**：短尾数值原子轨道 + 半局域赝势，从气相分子扩展到固体，精度瓶颈在泛函而非数值方法（[[../papers/Delley2000|Delley 2000]]）。
- **VASP 核心算法**：精确基态 AIMD 方案在每个 MD 步用共轭梯度法精确求电子基态，克服 Car-Parrinello 方法在金属中的非绝热失稳（[[../papers/kresseInitiomolecularDynamicsLiquid1993|Kresse 1993]]）。
- **PBE 泛函**：从七个物理极限条件推导的无经验参数 GGA 泛函，是赝势平面波计算的标准配套（[[../papers/perdewGeneralizedGradientApproximation1996a|Perdew 1996]]）。
- **Bader 分析**：近网法通过累积修正向量追踪真实的离网格电荷密度梯度轨迹，消除晶格偏差，使 Bader 电荷/体积随网格加密单调收敛（[[../papers/tangGridbasedBaderAnalysis2009|Tang 2009]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/blochlProjectorAugmentedwaveMethod1994b]] — Projector augmented-wave method
- [[../papers/Delley2000]] — From molecules to solids with the DMol3 approach
- [[../papers/kresseInitiomolecularDynamicsLiquid1993]] — Ab initio molecular dynamics for liquid metals
- [[../papers/perdewGeneralizedGradientApproximation1996a]] — Generalized Gradient Approximation Made Simple
- [[../papers/tangGridbasedBaderAnalysis2009]] — A grid-based Bader analysis algorithm without lattice bias

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/norm-conserving-pseudopotential|范数守恒赝势]]：赝势家族的重要成员。
- [[../concepts/density-functional-theory|密度泛函理论]]：赝势方法的应用框架。
- [[../concepts/plane-wave-basis|平面波基组]]：赝势方法配合的基组形式。
- 投影缀加波（PAW）：统一精度与效率的现代方法。
- [[../entities/ABINIT|ABINIT]]：赝势平面波 DFT 代码之一。
- [[../entities/Wannier90|Wannier90]]：基于平面波结果的局域化工具。
