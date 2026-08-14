---
tags: [concept, photophysics, thermochromism]
title: 热致变色 / Thermochromism
type: concept
status: developing
domain: [photophysics, physical-chemistry, materials-science]
mechanism: 物质的吸收或发射光谱（颜色）随温度改变而发生可逆变化的现象
related_concepts: [solvatochromism, viscosity-sensing, solvent-relaxation]
papers: [Huang2019solvatochromic, H2017fluorescence]
updated: 2026-08
---

# 热致变色 / Thermochromism

热致变色（Thermochromism）是指某些物质的吸收或发射光谱（即其呈现的颜色）随着温度的变化而发生可逆改变的现象。这一效应可以是由于晶格畸变、配位几何变化、化学平衡移动，或在有机探针中由于介质粘度与溶剂弛豫速度的变化而引起的。

## 👵 太奶导读

太奶啊，这就好比一朵**“温度敏感花”**。这花儿很神奇，天冷的时候（低温）它是一个颜色，天热起来（高温）它又变成另一个颜色。只要温度变回来，它的颜色也能跟着变回来。在咱们这些荧光分子里，是因为天热了以后，周围黏糊糊的甘油液体变得不那么黏了（粘度下降），分子可以更轻松地在里面“拧麻花”（扭转构型），而且周围的溶剂邻居们跑得更快，把分子抱得更紧。这一热一松，能量变了，发出来的光也就跟着变了色。

## 🏗️ 机制分类

热致变色可按材料类型和微观机理分为：
1.  **无机晶体畸变**：由于温度改变导致点阵参数、配位多面体产生微小变化，从而改变能带结构。
2.  **分子热变色（溶剂松弛控制）**：在环境敏感的有机染料中，温度直接控制介质（如甘油）的粘度。升温使粘度急剧下降，促使：
    *   **溶剂弛豫更充分**：激发态达到更低的溶剂化平衡态，导致发光红移 [[../papers/Huang2019solvatochromic]]。
    *   **构型转变加速**：提供扭转能垒，促使局域激发态（LE）向扭转分子内电荷转移态（[[../concepts/tict-mechanism|TICT]]）转变。

## 🧩 实验表征：温度依赖光谱

在有机多铁性或多通道环境探针的研究中，温度依赖荧光光谱是必不可少的手段。
*   **P1 探针**：在甘油中 25–80 °C 变温时，长波发射带 A 带（TICT）显著红移，短波 B 带（LE）相对强度逐渐下降 [[../papers/H2017fluorescence]]。
*   这种非单调的发光变化，可用于纳米尺度的非接触式光学温度传感器。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2019solvatochromic]]：详细讨论了甘油介质中 P1 探针的热致溶剂化变色（Thermo-Solvatochromism）机制。
- [[../papers/H2017fluorescence]]：给出了单光子与双光子变温荧光强度演化的定量比对。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/solvatochromism|溶剂化显色]]
- [[../concepts/tict-mechanism|TICT 机制]]
- [[../concepts/locally-excited-state|局域激发态 (LE)]]
- [[../entities/glycerol|甘油 (高粘度变温介质)]]
