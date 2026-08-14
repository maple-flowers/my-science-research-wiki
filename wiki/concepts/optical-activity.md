---
tags: [concept, photophysics, non-linear-optics]
title: 旋光性与光学活性 / Optical Activity
type: concept
status: mature
domain: [photophysics, stereochemistry, solid-state-physics]
mechanism: 手性物质使穿过它的线偏振光的偏振面发生旋转的现象
related_concepts: [chirality, raman-optical-activity, electromagnon, magnetoelectric-coupling]
papers: [songEvidenceSinglelayerVan2022, gaoGiantChiralMagnetoelectric2024a]
updated: 2026-08
---

# 旋光性与光学活性 / Optical Activity

旋光性与光学活性（Optical Activity）是指某种物质能够旋转穿过它的线偏振光的偏振面的性质。这种现象通常发生在具有 [[../concepts/chirality|手性]] 结构的物质中，反映了物质对左旋和右旋圆偏振光具有不同的折射率或吸收率。

## 👵 太奶导读

太奶啊，这就好比一束光是一根**“笔直的尺子”**（线偏振光），它在空中是直着往前走的。但当这把尺子穿过这些具有“光学活性”的材料时，材料里的特殊结构（手性）就像是有无数只小手轻轻拨了一下。等这尺子从材料另一头出来时，它就不再是原来的朝向，而是顺时针或者逆时针**“歪了一下”**。咱们看它歪了多少度（旋转角），就能知道这材料里面手性结构有多强。

## 🏗️ 物理分类

1.  **自然光学活性 (Natural Optical Activity, NOA)**：
    *   由物质本征的手性结构（如糖分子、螺旋磁序）引起。
    *   **范德华多铁案例**：在手性磁体 [[../entities/NiI2|NiI2]] 中，由于电磁振子的存在，在 THz 频段观测到了巨大的自然光学活性。其旋光率 $\eta$ 约为 $1000^\circ/\text{mm}$，比普通螺旋磁体高出两个数量级 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。
2.  **磁致旋光（法拉第效应）**：由外加磁场引起，而非物质本征手性。

## 🧩 谱学表征：拉曼光学活性 (ROA)

在多铁性二维材料的表征中，光学活性通常体现在圆偏振光的响应差上：
*   **圆偏振拉曼**：左旋（$\sigma^+$）与右旋（$\sigma^-$）圆偏振光的拉曼散射强度不同。
*   在 NiI2 的多铁相中，电磁振子峰展现出强烈的 ROA 信号。该信号的极性能够区分不同磁手性的畴（Domain I 与 Domain II 符号相反）[[../papers/songEvidenceSinglelayerVan2022]]。

## 🔬 动态磁电耦合的体现

光学活性在本质上是**空间非局域磁电耦合**的一种体现。
*   其强度通常由动态磁电耦合张量 $\alpha(\omega)$ 的虚部决定。
*   在 NiI2 单畴中，通过时间分辨实验提取的 $\alpha$ 系数约为 $11 \times 10^3 \text{ ps m}^{-1}$，确证了巨手性磁电耦合的存在 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。

## 📚 相关论文 (Related Papers)

- [[../papers/songEvidenceSinglelayerVan2022]]：在单层 NiI2 中观测到了与磁手性相关的光学响应和拉曼活性。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：详细研究了范德华多铁体中的太赫兹波段巨自然光学活性。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/chirality|手性]]
- [[../concepts/raman-optical-activity|拉曼光学活性 (ROA)]]
- [[../concepts/electromagnon|电磁振子]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../entities/NiI2|二碘化镍 (NiI2)]]
