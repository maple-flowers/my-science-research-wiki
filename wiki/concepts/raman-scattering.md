---
tags: [concept, spectroscopy, vibrational-spectra]
title: 拉曼散射 / Raman Scattering
type: concept
status: mature
domain: [spectroscopy, solid-state-physics, molecular-physics]
mechanism: 光子与物质分子/晶格发生非弹性碰撞，光子能量发生转移（产生 Stokes 或 anti-Stokes 位移）
related_concepts: [vibrational-spectra, electromagnon, raman-optical-activity, phonon]
papers: [songEvidenceSinglelayerVan2022, gaoGiantChiralMagnetoelectric2024a]
updated: 2026-08
---

# 拉曼散射 / Raman Scattering

拉曼散射（Raman Scattering）是一种非弹性散射过程。当单色光（通常是激光）照射物质时，光子与物质分子或晶格振动（声子）发生相互作用，导致散射光的频率发生改变。这种频率的改变（拉曼位移）反映了物质内部的振动能级信息。

## 👵 太奶导读

太奶啊，您就把这想象成**“听声辨物”**。咱们拿一个小木棒（激光光子）去敲一下不同的东西（分子或晶格）。大多数时候，小木棒弹回来还是原来的调门（这叫瑞利散射）。但有时候，小木棒敲上去会把一部分力传给东西让它晃动起来（声子振动），弹回来的调门就变低了（这就是拉曼散射的斯托克斯位移）。不同的东西“嗓门”不一样，咱们听听这个调门变了多少，就能知道这东西是铁还是木头，或者是它的原子是怎么排队的。

## 🏗️ 原理概览

拉曼散射涉及光子与物质间的能量交换：
1.  **瑞利散射 (Rayleigh Scattering)**：弹性散射，散射光频率等于入射光频率 ($\nu_s = \nu_0$)。
2.  **斯托克斯散射 (Stokes Scattering)**：光子失去能量，散射光频率降低 ($\nu_s = \nu_0 - \nu_v$)，对应物质吸收一个声子能级。
3.  **反斯托克斯散射 (Anti-Stokes Scattering)**：光子获得能量，散射光频率升高 ($\nu_s = \nu_0 + \nu_v$)，对应物质原处于激发态并释放一个声子给光子。

![图：块体 NiI2 的变温偏振拉曼光谱](../../raw/figures/songEvidenceSinglelayerVan2022/fig_4_8NRPR6W3.png)
*   **看图要点**：图中展示了随温度降低，拉曼谱图中出现了新的峰位（磁振子和电磁振子峰）。这些峰的出现标志着材料进入了新的物理相（多铁相）。
*   **来源**：[[../papers/songEvidenceSinglelayerVan2022]] -> [[../figures/vibrational-spectra|振动光谱]]

## 🧩 磁性与多铁性中的拉曼指纹

在凝聚态物理研究中，拉曼散射不仅能探测声子（晶格振动），还能探测：
*   **磁振子 (Magnon)**：磁性材料中自旋排列的集体激发。在 [[../entities/NiI2|NiI2]] 中，75 K 以下会出现特征磁振子峰 [[../papers/songEvidenceSinglelayerVan2022]]。
*   **电磁振子 (Electromagnon)**：在 [[../concepts/multiferroicity|多铁性]] 材料中，磁序与极化序耦合产生的特殊集体激发。这种模式通常具有极强的拉曼光学活性 (ROA)，是判定动态磁电耦合的重要证据。
*   **对称性破缺**：偏振拉曼光谱（XX/XY 配置）可以探测晶格旋转对称性的破缺。例如，$E_g$ 声子峰的分裂通常意味着单斜畸变的发生。

## 🔬 拉曼光学活性 (ROA)

拉曼光学活性（Raman Optical Activity）是指手性物质对左旋和右旋圆偏振光（$\sigma^+$ 和 $\sigma^-$）产生的拉曼散射强度存在差异。
*   在手性磁体 [[../entities/NiI2|NiI2]] 中，电磁振子峰展现出巨大的 ROA 信号，且该信号在对映纯手性畴之间符号相反，成为探测二维磁手性的利器 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。

## 📚 相关论文 (Related Papers)

- [[../papers/songEvidenceSinglelayerVan2022]]：在单层 NiI2 中利用拉曼光谱探测电磁振子和对称性破缺。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：利用圆偏振拉曼光谱展示 NiI2 中的巨手性磁电耦合。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/vibrational-spectra|振动光谱]]
- [[../concepts/electromagnon|电磁振子]]
- [[../concepts/raman-optical-activity|拉曼光学活性 (ROA)]]
- [[../entities/NiI2|二碘化镍 (NiI2)]]
- [[../concepts/multiferroicity|多铁性]]
