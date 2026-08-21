---
tags: [concept, superconductivity, 2D-materials, charge-density-wave]
title: 超导穹顶 / Superconducting Dome
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 临界温度 Tc 随掺杂/压力等控制参量呈先升后降的非单调穹顶状，两侧受竞争序与量子临界涨落抑制
related_concepts: [superconductivity, charge-density-wave, multiband-superconductivity, superfluid-density]
papers: [Chen2019superconductivity]
updated: 2026-08
---

# 超导穹顶 / Superconducting Dome

超导穹顶（Superconducting Dome）指超导临界温度 $T_c$ 随某一控制参量（掺杂浓度、载流子密度、压力、层数等）变化呈现**先升后降的穹顶状**非单调行为的普遍现象。它在铜氧化物高温超导（掺杂穹顶）、重费米子、有机超导以及 1T-TiSe₂ 等二维材料中反复出现，通常被解读为超导与某种竞争序（反铁磁、[[../concepts/charge-density-wave|CDW]] 等）及量子临界点共存/博弈的指纹。

## 👵 太奶导读

太奶啊，这就好比熬汤，火候（掺杂/压力）太小汤不鲜，火太大又糊了，中间有个“刚刚好”的甜点。超导也一样：调控参量太小时序太弱，太大时又被别的“坏分子”（竞争序）拆台，只有在中间的某个窗口，超导最兴旺——画成图就是一个“小山包”（穹顶）。

## 🏗️ 物理特征与定量描述

*   **穹顶形态**：$T_c(x)$ 随控制参量 $x$ 先增后减，峰值 $T_c^{\max}$ 出现在最佳掺杂/压力处。
*   **量子临界点**：穹顶峰值常靠近被抑制的竞争序的量子临界点，量子临界涨落被认为可能提供非常规配对媒介。
*   **两侧机制**：欠掺杂侧受静态序（反铁磁/CDW）抑制；过掺杂侧配对涨落与序参量刚度下降。
*   **与超流密度的关系**：Uemura 标度下穹顶两侧 $T_c$ 与凝聚刚度 $n_s/m^*$ 的关联不同，欠掺杂侧偏离 BCS 关系。

## 🧩 1T-TiSe₂ 中的超导穹顶

二维过渡金属二硫族化物 1T-TiSe₂ 是一个典型二维实例：

*   其 CDW 在公度（C）、近公度（NC）与非公度（IC）相之间转变，超导在 CDW 被抑制的窗口内涌现，$T_c$ 随调控呈穹顶状 [[../papers/Chen2019superconductivity]]。
*   近公度相由“错位相子”构成的二维网络承载，超导与之共存并受其调控，体现 CDW-超导竞争下穹顶的微观来源。

| 参量 | 行为 | 解读 |
| --- | --- | --- |
| 欠掺杂/弱压力 | Tc 低 | 竞争序（CDW/反铁磁）压制 |
| 最佳点 | Tc 峰值 | 量子临界涨落增强配对 |
| 过掺杂/强压力 | Tc 下降 | 序参量刚度下降 |

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2019superconductivity]]：1T-TiSe₂ 中 CDW 相变与超导涌现，提供二维超导穹顶的实例。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../concepts/superfluid-density|超流密度]]
- [[../entities/TiSe2|二硒化钛 (TiSe2)]]
