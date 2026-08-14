---
tags: [concept, charge-density-wave, topological-defect]
title: 错位相子 / Discommensuration (DC)
type: concept
status: developing
domain: [condensed-matter-physics, charge-density-wave]
mechanism: 近公度电荷密度波中相位发生局域 2πν 跳变的孤子状畴壁
related_concepts: [charge-density-wave, soliton, topological-defect, pair-density-wave]
papers: [Chen2019superconductivity, nakataRobustChargedensityWave2021]
updated: 2026-08
---

# 错位相子 / Discommensuration (DC)

错位相子 (Discommensuration, DC) 是指在近公度电荷密度波 (Near-Commensurate CDW, NC-CDW) 体系中，相位发生局域突变的拓扑缺陷或畴壁。它是连接公度区域 (Commensurate domains) 的边界。在 DC 处，CDW 的相位会跳变一个特定值（通常为 $2\pi\nu$，$\nu$ 为公度分数），同时伴随着序参量振幅的局部下降。

## Grandma 👵 太奶导读

太奶，这“错位相子”听着别扭，其实道理特简单，就像您以前在家里**缝被面儿**。
本来您想把被面和里子对得齐齐整整的（这就是公度态，**commensurate**）。
但要是这被面儿比里子长出那么一丁点儿（这就是非公度趋势），您缝着缝着，就得在中间**打个褶儿**，把多出来的布给“消化”掉。
这一道褶子，在物理上就叫一个“错位相子”。
科学家们发现，这些褶子在材料里可不安分，它们会连成一张大网。最神奇的是，很多新奇的本领（比如超导）就是专门从这些褶子里钻出来的！

## 🏗️ 结构概览：二维 Kagome DC 网络

在二维 TMD 材料（如 1T-TiSe₂）中，错位相子会自发组织成周期性的超晶格网络。

![图：近公度相中的 Kagome 状错位相子 (DC) 网络示意](../../raw/figures/Chen2019superconductivity/fig_2_WA3G7MTL.png)
*   **看图要点**：图中黄色虚线标出了错位相子的位置。这些线构成了二阶超晶格（Kagome 晶格）。在这些线上，CDW 的相位发生 $\pi$ 跳变，而超导序参量（颜色深浅）则优先在这些褶皱处增强。
*   **来源**：[[../papers/Chen2019superconductivity]] -> [[../figures/electronic-bands-cdw-transport|CDW与输运]]

## 🧩 物理特性与功能

1.  **超导成核中心**：由于 DC 处 CDW 振幅受到抑制，且梯度能较大，它往往成为超导电性优先萌发的温床。Chen 等人预言超导会沿着 DC 网络经历从 0D 点到 1D 线再到 2D 面的渗流。
2.  **孤子行为**：在一维极限下，DC 的物理描述等价于 sine-Gordon 方程的孤子（**Soliton**）解。
3.  **Little–Parks 振荡**：由 DC 围成的封闭网格可以定义超导环，在磁场下产生由于磁通量子化导致的阻值周期振荡。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2019superconductivity]]：提出了错位相子驱动超导成核的 McMillan-GL 理论模型。
- [[../papers/nakataRobustChargedensityWave2021]]：通过 STM 观测到了 TMD 体系中由 DC 畴壁分割的铁电/CDW 畴结构。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波 (CDW)]]
- [[../concepts/pair-density-wave|配对密度波 (PDW)]]
- [[../concepts/domain-wall|畴壁]]
- [[../entities/TiSe2|二硒化钛 (TiSe₂)]]
