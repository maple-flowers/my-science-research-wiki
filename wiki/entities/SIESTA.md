---
tags: [entity]
---

# SIESTA

基于 **数值原子轨道 (Numerical Atomic Orbitals, NAO)** 基组的第一性原理计算程序包，采用标准范德堡赝势（Norm-conserving pseudopotentials），特别适用于大规模体系和复杂异质结构的电子结构模拟。

## 核心特性与方法论

- **基组优势**：不同于 VASP 或 Quantum ESPRESSO 使用的平面波基组，SIESTA 使用线性组合原子轨道（LCAO）方法。其数值轨道基组具有良好的局部化特性，使得计算量随原子数接近线性增长（Order-N），在处理包含数百至上千原子的超胞时具有显著效率优势。
- **电子温度展宽 (Electronic Smearing)**：支持 Fermi-Dirac 展宽，常用于模拟有限温效应或辅助金属体系的收敛。
- **Berry 相计算**：集成 Berry 相方法，用于计算晶体自发极化强度 $P_s$，是研究铁电性的核心工具。

## 关键研究应用

### 1. 铁电薄膜的临界厚度模拟
在 [[../papers/junqueraCriticalThicknessFerroelectricity2003]] 中，SIESTA 被用于构建完整的“金属电极/铁电薄膜/金属电极”短路电容器超胞（如 SrRuO₃/BaTiO₃/SrRuO₃）。
- **计算策略**：利用其高效处理大超胞的能力，显式包含电极界面，模拟非理想屏蔽效应。
- **物理发现**：通过扫描软模畸变（Soft-mode distortion）下的能量曲线，首次从第一性原理证明了 BaTiO₃ 存在约 6 个晶胞（~24 Å）的临界厚度，低于此值铁电性将被退极化场压制。

### 2. 二维材料电荷密度波 (CDW) 动力学
在 [[../papers/chowdhuryReviewTheoreticalComputational]] 综述涉及的工作中，SIESTA 用于研究 1T-TaS₂ 公度电荷密度波（C-CDW）相的电子结构。
- **电荷转移**：结合 vdW-DF 泛函，计算了不同层间堆叠下的态密度（PDOS）。
- **维数效应**：模拟显示尽管 1T-TaS₂ 是层状材料，其亚飞秒级电荷转移在面内和面外表现出近乎各向同性的特征，挑战了其纯粹“二维”特性的传统认知。

## 相关论文

- [[../papers/junqueraCriticalThicknessFerroelectricity2003]] — 首次证明铁电临界厚度的奠基性工作。
- [[../papers/chowdhuryReviewTheoreticalComputational]] — 二维 CDW 材料计算方法综述。

## 关联实体

- [[VASP]] — 另一种常用的平面波基组 DFT 代码。
- [[TMDs]] — 经常使用 SIESTA 研究其电子结构与相变的材料家族。
