---
title: Wannier90
type: entity
tags: [computational-tools, Wannier-functions, electronic-structure]
---

# Wannier90

**Wannier90** 是一个用于计算最大局域化 Wannier 函数 (MLWFs) 的开源软件包。它作为第一性原理计算（如 [[VASP|VASP]]、Quantum Espresso）的后处理工具，广泛应用于电子结构分析、拓扑性质判定及大规模物性输运模拟。

## 1. 核心物理功能
- **紧束缚模型构建**：通过将 Bloch 波函数变换为局域化的 Wannier 基组，构建高精度的紧束缚 (TB) 哈密顿量。
- **能带插值**：实现极其高效的极细 $k$ 点能带插值，用于精确寻找费米面及布里渊区内的奇点。
- **拓扑特性分析**：计算 Berry 曲率、反常霍尔电导以及手性边缘态。

## 2. 在本库研究中的应用
在自旋电子学与拓扑材料研究中，Wannier90 起到了桥梁作用：
- **自旋纹理分析**：在 [[SrOsO3|SrOsO3]] 等巨自旋劈裂体系中，利用 Wannier 插值技术绘制动量空间中的自旋极化矢量场（自旋纹理） [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。
- **磁交换参数提取**：配合 TB2J 等代码，从 DFT 数据中提取层间/层内交换相互作用强度 ($J$)，进而利用蒙特卡洛模拟估算 $T_C$ 或 $T_N$。
- **大尺度模拟**：为 [[../concepts/moire-superlattice|莫尔超晶格]] 的大体系能带计算提供高效的紧束缚基组。

## 3. 本库相关代表性论文
- [[../papers/pizziWannier90NewFeatures2020]]：介绍了 Wannier90 的最新功能与代码演进。
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：应用 Wannier90 分析二维氧化物单层的自旋劈裂与拓扑物理。
- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：计算背景中的 PAW 与基组转换基础。

## 4. 关联工具与实体
- [[VASP|VASP]] (数据输入源)
- [[../concepts/berry-phase|贝里相位 Berry Phase]]
- [[../concepts/giant-spin-splitting|巨自旋劈裂 Giant Spin Splitting]]
- [[deep-potential|DeePMD-kit]] (用于大尺度原子模拟的替代/补充方案)
