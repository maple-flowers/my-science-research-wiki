---
tags: [entity, density-functional-theory, pseudopotential, norm-conserving-pseudopotential, dfpt, phonon-dispersion, electron-phonon-coupling, charge-density-wave, berry-phase, modern-polarization-theory]
title: Quantum-ESPRESSO
type: entity
status: developing
year: 2009
papers: [zhengAnisotropicSuperconductivityTwodimensional2025, chowdhuryReviewTheoreticalComputational, lezoualchStudyChargeDensity, yanagizawaSwitchingChargedensityWave2023, king-smithTheoryPolarizationCrystalline1993, tangGridbasedBaderAnalysis2009]
updated: 2026-08-21
---

# Quantum-ESPRESSO

**Quantum ESPRESSO（QE）** 是一套开源的第一性原理计算软件包，以平面波基组 + 赝势为核心框架，用于电子结构、总能量、结构优化与晶格动力学计算。在本库中它主要作为**声子与电声耦合计算的工具链**出现——这是它与 [[../entities/VASP|VASP]] 的关键分工点。

## 👵 太奶导读

乖孙，QE 是一套算电子结构的免费软件。它跟 VASP 干的活大体重叠，但有一件事它特别拿手：**算声子**。

材料里的原子不是钉死的，它们在振动，这些振动模式叫「声子」。想知道一个结构稳不稳、会不会自己扭曲成新相（比如 [[../concepts/charge-density-wave|电荷密度波]]），就得看声子谱里有没有「虚频」——有的话说明这个结构一推就塌。QE 里的 DFPT（密度泛函扰动理论）模块能直接把声子谱和「电子跟声子耦合得多紧」算出来，所以研究 CDW 和 [[../concepts/electron-phonon-coupling|电声耦合超导]]的人几乎都用它。

记一句话：**要算能带和总能，VASP、QE 都行；要算声子谱和电声耦合，本库里的论文基本都走 QE。**

## 🧩 定位与典型用法 (Role & Usage)

- **基组与赝势**：平面波基组，配合模守恒赝势（norm-conserving）或超软赝势。本库中两篇 QE 论文都明确用了**模守恒赝势**，这与 QE 的 DFPT 实现对赝势类型的要求有关。
- **核心能力（本库涉及）**：
  - 基态电子结构、结构优化、总能量 —— 与 VASP 同类。
  - **DFPT 声子谱与电声耦合矩阵元** —— 本库中 CDW 与超导类工作的主力，是 QE 被选用的主要理由。
  - 各向异性 Migdal-Eliashberg 方程求解（配合 EPW 类后处理）。
  - 电子磁化率 χ₀(q) 计算，用于评估 [[../concepts/fermi-surface-nesting|费米面嵌套]]强度。
  - 基于 [[../concepts/berry-phase|贝里相位]]的极化计算（现代极化理论的标准实现之一）。
- **与 VASP 的关系**：不是替代而是分工。本库的实际使用模式是「结构与磁性用 VASP，声子与电声耦合用 QE」，两者对同一体系的交叉验证也常见。

### 本库中的实际计算参数

| 论文 | 泛函 | 赝势 | 平面波截断 | 用途 | 性质 |
|---|---|---|---|---|---|
| [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025\|zheng2025]] | PBE | 优化模守恒 Vanderbilt | 80 Ry | 电声耦合、超导能隙各向异性 | 计算 |
| [[../papers/chowdhuryReviewTheoreticalComputational\|chowdhury 综述]] | LDA / GGA | 模守恒或超软 | 未统一给出 | CDW 相变模拟（电子温度法、应力法） | 计算（综述汇总） |

⚠️ **边界**：上表仅两条来源，且 chowdhury 是综述性汇总而非单一体系的自洽参数集。这里的数值只能当作「本库见过的用法」，不能当作 QE 计算 CDW/超导的通用推荐参数。

## 📚 相关论文 (Related Papers)

### 以 QE 为主要计算工具

- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]：用 QE（PBE + 优化模守恒赝势 + 80 Ry 截断）完整走通了「电声耦合矩阵元 → 各向异性 Migdal-Eliashberg 方程」这条链路，把 Cu₃(CO)₆ 单层的超导能隙各向异性分布算了出来，是本库中 QE 电声耦合能力最完整的一次使用示范。
- [[../papers/chowdhuryReviewTheoreticalComputational]]：作为综述系统交代了用 QE 计算二维 CDW 的两项关键技巧——用「电子温度」模拟真实温度效应、施加微小压缩应力模拟非公度 CDW——并给出了泛函与赝势的选取基准，是本库理解「QE 怎么用来算 CDW」的方法学参考。
- [[../papers/lezoualchStudyChargeDensity]]：用 QE 的 DFT 模块算基态、DFPT 模块算声子谱与电声耦合矩阵元，并在此基础上自行发展了「从声子软模构建 CDW 超胞畸变」的方法，说明 QE 的声子输出可以直接作为构造畸变相结构的起点。
- [[../papers/yanagizawaSwitchingChargedensityWave2023]]：用 QE 计算单层 1T-TiTe₂ 的能带结构与电子磁化率 χ₀(q)，用来定量判断费米面嵌套强度，是本库中 QE 承担「嵌套判据计算」角色的实例。

### 仅提及 QE 作为方法的承载平台（弱关联）

- [[../papers/king-smithTheoryPolarizationCrystalline1993]]：本文自身不使用 QE，但其提出的贝里相位极化方法后来被 QE、VASP、ABINIT 等主流软件普遍内置，故在此仅作为 QE 极化计算功能的理论来源列出。
- [[../papers/tangGridbasedBaderAnalysis2009]]：本文自身不使用 QE，只在展望中建议把其网格 Bader 分析算法集成进 VASP、QE 等软件作为标准后处理模块；与 QE 的关联属方法生态层面，非实际计算依据。

## 🔗 关联概念与实体 (Related)

- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/pseudopotential|pseudopotential]]
- [[../concepts/norm-conserving-pseudopotential|norm-conserving-pseudopotential]]
- [[../concepts/electron-phonon-coupling|electron-phonon-coupling]]
- [[../concepts/charge-density-wave|charge-density-wave]]
- [[../concepts/fermi-surface-nesting|fermi-surface-nesting]]
- [[../concepts/berry-phase|berry-phase]]
- [[../concepts/modern-polarization-theory|modern-polarization-theory]]
- [[../concepts/polarization-quantum|polarization-quantum]]
- [[../concepts/wannier-function|wannier-function]]
- [[../entities/VASP|VASP]]
- [[../entities/Wannier90|Wannier90]]
