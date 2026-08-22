---
tags: [concept, superconductivity, 2D-materials, charge-density-wave, fermiology]
title: 多带超导 / Multiband Superconductivity
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 超导配对同时在费米面的多个能带通道上建立，各通道能隙不同，整体响应为多能隙加权叠加
related_concepts: [superconductivity, two-gap-superconductivity, charge-density-wave, fermi-surface-nesting, superfluid-density]
papers: [majumdarInterplayChargeDensity2020]
updated: 2026-08
---

# 多带超导 / Multiband Superconductivity

多带超导（Multiband Superconductivity）指超导序参量同时展布于费米面的多个能带（多个费米面片）之上，各带拥有独立（或部分独立）的超导能隙。它常见于层状过渡金属硫族化物、铁基超导体与 MgB₂ 等具有多重费米面片（空穴/电子口袋）的材料，是理解非常规超导微观机制的核心概念之一。

## 👵 太奶导读

太奶啊，一般的超导像“一条河上架一座桥”，只走一条道。多带超导呢，像“好几条平行河各架一座桥”，每条河的水流（能带）都有自己的桥（能隙），载客能力不一样。测超导的总响应时，几条河的贡献叠在一起，看起来就像一个“叠影”的能隙。这就是多带超导的朴素图像。

## 🏗️ 物理特征与定量描述

*   **多能隙结构**：不同能带上的能隙 $\Delta_1, \Delta_2, \dots$ 大小不一，低温比热、穿透深度与隧道谱出现多台阶/双峰结构。
*   **带间耦合**：带间散射（杂质或配对）把各带能隙耦合成整体，影响 $T_c$ 与能隙比 $2\Delta/k_BT_c$ 偏离 BCS 弱耦合值。
*   **带间配对符号**：各带配对序参数可能同号（$s_{++}$，如 MgB₂ 声子机制）或反号（$s_\pm$，如铁基超导体自旋涨落机制），后者的探测常借助杂质敏感性或相敏实验。

## 🧩 层状硫族化物中的多带超导与 CDW

以 2H-NbSe₂、2H-NbS₂ 为代表的过渡金属二硫族化物同时拥有 CDW 与超导两种序。高质量单晶研究揭示了：

*   **CDW 与超导的竞争**：[[../concepts/charge-density-wave|电荷密度波]]会重构费米面、耗散[[../concepts/fermi-surface-nesting|嵌套]]口袋，抑制超导配对。
*   **压力调控**：施加压力可抑制 CDW、恢复被局域化的费米面，从而**显著增强超导**——2H-NbSe₂ 中 CDW 与 SC 呈竞争关系，压力下 CDW 被抑制、超导增强 [[../papers/majumdarInterplayChargeDensity2020]]。
*   **多带贡献**：多能隙响应叠加后，[[../concepts/superfluid-density|超流密度]]与穿透深度的温度依赖偏离单带 London 行为，可通过低温幂律/指数行为区分。

## 🔬 实验判据

| 判据 | 多带/多能隙表现 |
| --- | --- |
| 比热 | 低温指数/多台阶，能隙比偏离 BCS |
| 穿透深度 | 低温由大能隙主导，呈指数饱和 |
| 隧道谱 | 多峰结构 |
| 上临界场 | 温度依赖偏离单带 Werthamer-Helfand-Hohenberg 曲线 |

## 📚 相关论文 (Related Papers)

- [[../papers/majumdarInterplayChargeDensity2020]]：2H-NbSe₂/2H-NbS₂ 单晶中 CDW 与超导的竞争及压力增强超导，体现多带费米面重构对超导的关键作用。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/two-gap-superconductivity|双能隙超导]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/fermi-surface-nesting|费米面嵌套]]
- [[../concepts/superfluid-density|超流密度]]
- [[../entities/NbSe2|二硒化铌 (NbSe2)]]
- [[../entities/NbS2|二硫化铌 (NbS2)]]
