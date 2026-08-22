---
tags: [concept, superconductivity, 2D-materials, uemura-relation]
title: 超流密度 / Superfluid Density
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 超流密度正比于超导凝聚中的配对载流子有效密度，通过穿透深度 λ 由 London 方程导出，ns ∝ 1/λ²
related_concepts: [superconductivity, penetration-depth, multiband-superconductivity, two-gap-superconductivity, uemura-relation, charge-density-wave]
papers: [Islam2025enhancement, majumdarInterplayChargeDensity2020]
updated: 2026-08
---

# 超流密度 / Superfluid Density

超流密度（Superfluid Density）$n_s$ 是刻画超导凝聚体刚度的核心量，定义为单位体积内参与无耗散超流输运的有效载流子数。它与穿透深度 $\lambda$ 直接关联：由 London 方程 $n_s = m^*/(\mu_0 e^2 \lambda^2)$，即 $n_s \propto 1/\lambda^2$。超流密度的温度依赖与数值大小是区分常规/非常规配对、判定超导凝聚机制（BCS 弱耦合、强耦合、BCS-BEC 渡越）的重要观测量。

## 👵 太奶导读

太奶啊，超导就是电子结成“整齐的队列”无阻地流。超流密度就是这支队列有多“密实”——密实了，磁场钻不进去（被挤出表面），温度也没那么容易把队列打散。咱们不直接数电子，而是量磁场能钻多深（穿透深度），深度越浅说明队列越密实、超流密度越大。

## 🏗️ 物理特征与定量描述

*   **London 关系**：$n_s = \dfrac{m^*}{\mu_0 e^2 \lambda^2}$，穿透深度 $\lambda$ 是实验上获取 $n_s$ 的主要窗口。
*   **温度依赖**：在 BCS 弱耦合下低温近似 $n_s(T)/n_s(0) \approx 1 - \sqrt{2\pi\Delta/k_BT}\, e^{-\Delta/k_BT}$（指数饱和）；存在节点（如 $d$ 波）或低能激发时则呈幂律。
*   **Uemura 关系**：在欠掺杂铜氧化物等非常规超导体中，$T_c \propto n_s/m^*$（Uemura 标度），反映超导由凝聚刚度主导，而非由配对能标主导。
*   **多能隙贡献**：多带/[[../concepts/two-gap-superconductivity|双能隙]]体系中 $n_s(T)$ 是各带贡献的加权叠加，低温段由大能隙带主导。

## 🧩 压力/应变调控下的超流密度

对层状硫族化物超导体的研究展示超流密度如何响应序竞争：

*   2 GPa 压力下，4H-NbSe₂ 的超流密度增强 **75%**，高于 2H-NbSe₂ 的 **32%**；两者 CDW 均被抑制约 20% [[../papers/Islam2025enhancement]]。
*   解释：压力抑制[[../concepts/charge-density-wave|CDW]]、恢复费米面态密度，凝聚刚度增强；4H 的多带结构使其对 CDW 抑制更敏感，$n_s$ 增幅更大。
*   这体现了超流密度作为“序竞争”敏感探针的价值——它同时编码了配对强度（$\Delta$）与配对载流子数（$n_s$）两类信息。

## 🔬 实验判据速览

| 观测量 | 与超流密度的关系 | 用途 |
| --- | --- | --- |
| 穿透深度 λ | ns ∝ 1/λ² | 主探针（微波谐振、μSR、磁光） |
| 上临界场 Hc2 | 正比于 ns 相关量 | 交叉验证 |
| 比热 | 反映能隙结构 | 配合解析多能隙 |

## 📚 相关论文 (Related Papers)

- [[../papers/Islam2025enhancement]]：压力下 4H/2H-NbSe₂ 超流密度增强，量化 CDW 竞争对凝聚刚度的调控。
- [[../papers/majumdarInterplayChargeDensity2020]]：2H-NbSe₂/2H-NbS₂ 中 CDW 与超导竞争，提供超流密度响应的背景图像。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/penetration-depth|穿透深度]]
- [[../concepts/uemura-relation|Uemura 关系]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../concepts/two-gap-superconductivity|双能隙超导]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../entities/NbSe2|二硒化铌 (NbSe2)]]
