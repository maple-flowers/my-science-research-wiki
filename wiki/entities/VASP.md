---
title: VASP
type: entity
tags: [computational-tools, DFT, first-principles]
---

# Vienna Ab initio Simulation Package (VASP)

**VASP** 是目前学术界和工业界应用最广泛的基于密度泛函理论 (DFT) 的第一性原理计算软件包之一。它采用平面波基组和投影增强波 (PAW) 方法，能够高效地模拟多粒子体系的电子结构、力学性质、磁学性质及动力学过程。

## 1. 核心功能与特色
- **高效能计算**：通过优化的算法实现大规模并行计算，适用于金属、半导体及绝缘体体系。
- **丰富的官能团支持**：支持 LDA、GGA (PBE/RPBE)、混合泛函 (HSE06) 以及 SOC（自旋轨道耦合）效应。
- **物性分析**：支持计算剥离能、能带结构、态密度 (DOS)、电荷密度、声子谱及 AIMD（第一性原理分子动力学）。

## 2. 在本库研究中的应用
在二维材料与多铁性研究中，VASP 是核心的模拟平台：
- **高通量筛选**：用于计算 831 种 $ABO_3$ 氧化物的剥离能与稳定性判据 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。
- **多铁性验证**：提取 [[BiFeO3|BiFeO3]]、[[CrTe2|CrTe2]] 等体系的极化强度与磁性基态数据。
- **机器学习势开发**：作为底层数据源，为 [[deep-potential|DeePMD-kit]] 提供高精度的 DFT 训练数据 [[../papers/gaoStrainEngineeringFerroelectric2024]]。

## 3. 计算协议参考 (Computational Protocol)
典型的二维材料计算流程包括：
- **收敛标准**：能量收敛阈值通常设为 $10^{-7}\text{ eV}$，力收敛标准为 $0.001\text{ eV/\text{\AA}}$。
- **修正项**：对于范德华力主导的体系，通常加入 DFT-D3 等色散修正；对于极性表面，需开启偶极修正。

## 4. 本库相关代表性论文
- [[../papers/kresseEfficiencyAbInitio1996]]：VASP 的奠基性论文，详细阐述了计算效率与方法学。
- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：PAW 方法的原始论文，是 VASP 计算的基础。
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：应用 VASP 进行高通量二维氧化物筛选的范例。

## 5. 关联工具与实体
- [[../concepts/density-functional-theory|密度泛函理论 DFT]]
- [[Wannier90|Wannier90]] (紧束缚拟合与自旋纹理分析)
- [[deep-potential|DeePMD-kit]] (机器学习势训练)
- [[SIESTA|SIESTA]] (基于局域基组的替代方案)
