---
title: Quantum ESPRESSO
type: entity
tags: [entity, computational-tools, DFT, first-principles]
---

# Quantum ESPRESSO (QE)

**Quantum ESPRESSO** 是一款基于密度泛函理论 (DFT)、平面波基组和赝势（Norm-conserving 与 PAW）的开源第一性原理电子结构计算软件包。它由一套互相协作的组件构成，旨在实现电子结构模拟、材料性能预测以及纳米尺度下的物理机制探索。

## 1. 核心优势与技术特色

- **密度泛函微扰理论 (DFPT)**：QE 的核心组件 `PHonon` 是其区别于 VASP 等软件的关键优势。它允许在布里渊区的任意 $q$ 点直接计算声子频率和本征矢量，是识别 [[../concepts/soft-mode|声子软模]] 和研究 [[../concepts/charge-density-wave|电荷密度波 (CDW)]] 机制的首选工具。
- **电-声相互作用**：配合 [[EPW|EPW]] 代码，QE 可以通过 Wannier 插值精确处理全布里渊区的电声耦合矩阵元，从而预测 [[../concepts/anisotropic-superconductivity|各向异性超导]] 性质。
- **丰富的关联泛函**：支持 LDA、GGA (PBE/PBEsol)、DFT+U、vdW-DF 等，能够处理关联电子体系及范德华力主导的二维材料。
- **高性能并行**：针对大规模集群优化，支持包含数百个原子的复杂超胞计算。

## 2. 在本库研究中的应用

在“相位锁定属性”（Phase-Locked Properties）研究框架下，Quantum ESPRESSO 是连接微观电子拓扑与宏观相变的桥梁：

- **CDW 机制判别 (Project-7)**：
    - 在单层 [[TiTe2|TiTe2]] 研究中，利用 QE 计算费米面及 [[../concepts/electronic-susceptibility|电子磁化率]] $\chi_0(q)$，确立了费米面嵌套的主导驱动力 [[../papers/yanagizawaSwitchingChargedensityWave2023]]。
    - 在 1T-[[VSe2|VSe2]] 和 1T-[[VTe2|VTe2]] 研究中，通过 DFPT 识别虚频软模，系统构建了多种公度与非公度 CDW 超胞模型 [[../papers/lezoualchStudyChargeDensity]]。
- **二维超导预测 (Project-7)**：
    - 在二维金属-有机框架 [[Cu3CO6|Cu3(CO)6]] 中，利用 QE+EPW 流程预测了 $T_c = 16.5$ K 的各向异性超导态，并揭示了嵌套增强电声耦合的本质 [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]。
- **计算方法基准 (Review)**：
    - 综述指出 QE 配合 LDA 交换关联泛函和模守恒赝势，在模拟 TMDs（如 [[TaSe2|TaSe2]]）的拉曼频率时具有极高的精度，优于标准的 PBE-PAW 配置 [[../papers/chowdhuryReviewTheoreticalComputational]]。

## 3. 计算协议参考 (Computational Protocol)

针对二维材料的典型计算参数建议：
- **平面波截断**：波函数截断通常设为 60–80 Ry，电荷密度截断为波函数的 4–8 倍（如 320 Ry）。
- **k-网格采样**：对于单层体系，真空层需大于 10–12 Å；采样密度如 $12\times 12\times 1$ 或更密，视体系金属性而定。
- **赝势选择**：研究电声耦合建议使用模守恒赝势 (Norm-conserving) 以保证矩阵元计算的数值稳定性。

## 4. 相关论文

- [[../papers/yanagizawaSwitchingChargedensityWave2023]] — 单层 TiTe₂ 载流子调控与嵌套机制。
- [[../papers/lezoualchStudyChargeDensity]] — 基于 DFPT 软模的 CDW 建模方法论。
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] — 2D-MOF 中的各向异性超导电性研究。
- [[../papers/chowdhuryReviewTheoreticalComputational]] — 二维 CDW 材料计算方法综述。
- [[../papers/tangGridbasedBaderAnalysis2009]] — 涉及与 [[bader-code|Bader Code]] 的电荷网格后处理集成。

## 5. 关联工具与实体

- [[VASP]] — 另一种基于平面波的主流 DFT 软件。
- [[SIESTA]] — 针对大规模体系的数值原子轨道基组 DFT 代码。
- [[EPW]] — 基于 QE 的电声插值与超导计算模块。
- [[Wannier90]] — 用于构造最大局域化 Wannier 函数，常作为 QE 计算的后处理步骤。
