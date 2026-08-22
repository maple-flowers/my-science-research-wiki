---
tags: [concept, superconductivity, 2D-materials, charge-density-wave, strain-engineering]
title: 双能隙超导 / Two-Gap Superconductivity
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 超导序参量由两个（类）能隙刻画，通常对应两群费米面或两种配对通道，宏观响应呈两能隙叠加
related_concepts: [superconductivity, multiband-superconductivity, charge-density-wave, superfluid-density, bec-bcs-crossover]
papers: [Islam2025enhancement]
updated: 2026-08
---

# 双能隙超导 / Two-Gap Superconductivity

双能隙超导（Two-Gap Superconductivity）是[[../concepts/multiband-superconductivity|多带超导]]中最常见的情形：超导态由两个能隙 $\Delta_1$、$\Delta_2$ 共同刻画，二者通常对应两群不同费米面片（如层状材料中的不同价带）或两种配对强度。它在 MgB₂、NbSe₂、铁基超导等体系中被广泛观测。

## 👵 太奶导读

太奶啊，还是“多座桥”的老故事，只不过这次明确只有**两座桥**：一座结实（大能隙）、一座软（小能隙）。低温时主要是结实那座在承重（扛着超导序），温度升高软桥先垮。测总响应时两条曲线叠在一起，会出现两个特征温度尺度——这就是“双能隙”的指纹。

## 🏗️ 物理特征与定量描述

*   **两个能隙**：$\Delta_1 \neq \Delta_2$，各自与 $T_c$ 的比值 $2\Delta/k_BT_c$ 可分别偏离或接近 BCS 值。
*   **两温度尺度**：热力学量（比热、超流密度、穿透深度）在低温与中温出现两个不同幂律/指数区间。
*   **带间泄漏**：温度升高时大能隙带上的准粒子通过散射耦合进小能隙带，使小能隙被“拖高”，表现为非简单的两带独立。

## 🧩 硫族化物中的双能隙与压力/应变调控

对层状硫族化物超导体单晶（如含 CDW 的 4H-NbSe₂ 与不含 CDW 的 2H-NbS₂）的研究表明：

*   在 2 GPa 压力下，4H-NbSe₂ 的[[../concepts/superfluid-density|超流密度]]增强 **75%**，显著高于 2H-NbSe₂ 的 **32%**，而两者的 CDW 都被抑制约 20% [[../papers/Islam2025enhancement]]。
*   该差异源于双能隙/多带结构：CDW 对费米面的重构作用在不同能带上不同，压力恢复的态密度对 4H 结构增益更大，从而超流密度增幅更强。
*   这一现象把“双能隙超导”与[[../concepts/charge-density-wave|CDW]]竞争、以及[[../concepts/bec-bcs-crossover|BCS-BEC 渡越]]的能标联系起来。

## 🔬 与多带超导的区分

| 对比项 | 双能隙超导 | 多带超导（广义） |
| --- | --- | --- |
| 能隙数量 | 两个（主通道） | 两个及以上 |
| 典型来源 | 两群费米面/两配对通道 | 多费米面片叠加 |
| 观测特征 | 双台阶/双温度尺度 | 多台阶/连续谱 |

## 📚 相关论文 (Related Papers)

- [[../papers/Islam2025enhancement]]：4H-NbSe₂ 与 2H-NbS₂ 在压力下超流密度增强的对比，揭示双能隙与 CDW 竞争对超导的调控。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../concepts/superfluid-density|超流密度]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/bec-bcs-crossover|BCS-BEC 渡越]]
- [[../entities/NbSe2|二硒化铌 (NbSe2)]]
- [[../entities/NbS2|二硫化铌 (NbS2)]]
