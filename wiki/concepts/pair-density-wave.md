---
tags: [concept, superconductivity, pairing, density-wave]
title: '配对密度波 / Pair Density Wave (PDW)'
type: concept
status: mature
domain: [condensed-matter-physics, superconductivity, strong-correlation]
mechanism: 库珀对凝聚携带有限动量 Q，超导序参量在实空间周期性调制
related_concepts: [superconductivity, charge-density-wave, spin-density-wave, order-parameter, anisotropic-superconductivity, multiband-superconductivity]
papers: ['majumdarInterplayChargeDensity2020', 'Chen2019superconductivity']
updated: 2026-08
---

# 配对密度波 / Pair Density Wave (PDW)

配对密度波（Pair Density Wave, PDW）指**库珀对的凝聚携带有限动量 $\mathbf{Q}$ 而非零动量**的超导态：其序参量 $\Delta(\mathbf{r}) = \Delta_0 e^{i\mathbf{Q}\cdot\mathbf{r}}$ 在实空间呈周期性调制，库珀对密度随位置振荡。PDW 是均匀 BCS 超导（$\mathbf{Q}=0$）的自然推广，被视为高温超导、条纹相与非常规磁性体系中重要的竞争/母体序。

## 👵 太奶导读

太奶啊，普通超导里的"电子夫妻"（库珀对）都慢悠悠在原地配对，安安静静的。可 PDW 里的电子夫妻们是"跳着舞配对"的——它们带着一股子"横劲儿"（有限动量）到处转，所以配对的密度就像波纹一样，一会儿密一会儿疏。这种"流动着配对"的脾气，会派生出很多奇怪的伴生现象。

## 🏗️ 物理机制

*   **有限动量配对**：当费米面嵌套或磁场/自旋序使电子配对偏好有限动量 $\mathbf{Q}$ 时，序参量获得空间调制 $\Delta(\mathbf{r})\propto e^{i\mathbf{Q}\cdot\mathbf{r}}$；$\mathbf{Q}$ 常与费米面嵌套矢量或磁条纹波矢关联。
*   **与均匀超导/CDW 的关系**：PDW 的 $|\Delta|^2$ 呈周期调制，可在实空间同时产生电荷密度调制（伴生 CDW 分量）与自旋调制，因此 PDW 常"携家带口"出现。
*   **对称性与时间反演**：有限动量配对一般伴随空间反演或时间反演对称性的部分破缺，可能诱发自旋极化电流、环路流等非常规响应。
*   **相位刚度**：PDW 序的相位涨落强烈，可导致"电子液晶"、向列序等中间相。

## 🧩 具体体系与证据

*   **条纹相（Stripes）**：空穴掺杂铜氧化物中自旋/电荷条纹与超导交织，多种实验（STM 涡旋芯调制、Josephson 干涉）支持 PDW 作为条纹相的核心序。
*   **磁场诱导 PDW**：磁场可诱导均匀超导向 PDW 转变，产生半量子涡旋（half-flux-quantum vortex）等拓扑缺陷，是区分 PDW 的探针。
*   **TMD 与层状体系**：2H-NbS₂/NbSe₂ 等体系中[[../concepts/charge-density-wave|CDW]]与多带超导交织 [[../papers/majumdarInterplayChargeDensity2020]]，其微观序是否含 PDW 分量为活跃研究方向；1T-TiSe₂ 中 CDW 与超导转变耦合 [[../papers/Chen2019superconductivity]] 提供了有限动量配对的可能舞台。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/spin-density-wave|自旋密度波]]
- [[../concepts/order-parameter|序参量]]
- [[../concepts/anisotropic-superconductivity|各向异性超导]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../entities/NbSe2|NbSe₂]]、[[../entities/TiSe2|TiSe₂]]

## 📚 相关论文 (Related Papers)

- [[../papers/majumdarInterplayChargeDensity2020]] — CDW 与多带超导在 2H-NbS₂/NbSe₂ 中的交织
- [[../papers/Chen2019superconductivity]] — 1T-TiSe₂ 中 CDW 相与超导涌现
