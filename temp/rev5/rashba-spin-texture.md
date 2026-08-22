---
tags: [concept, spintronics, spin-orbit-coupling, sliding-ferroelectricity, 2d-materials]
title: Rashba 自旋纹理 / Rashba Spin Texture
type: concept
status: mature
year: 2025
domain: [spintronics, quantum-materials]
mechanism: 结构反演对称性破缺体系中 SOC 使自旋沿等能面切向锁定于动量，形成顺/逆时针螺旋纹理，且可被铁电极化翻转
related_concepts: [rashba-effect, spin-texture, spin-orbit-coupling, sliding-ferroelectricity, edelstein-effect, spin-hall-effect, spin-transport, polarization-switching]
papers: [chenStrongSlidingFerroelectricity2024, wuSlidingFerroelectricity2D2021a, kaurRecentAdvancesTheoretical2025a, liuSpintronicsTwoDimensionalMaterials2020b]
updated: 2026-08-19
---

# Rashba 自旋纹理 / Rashba Spin Texture

## 👵 太奶导读

乖孙，这一条讲的是「Rashba 自旋纹理」——是前面两条（Rashba 效应 + 自旋纹理）合体的**具体图像**：在反演破缺的二维体系里，电子自旋沿着费米面附近的等能圈"切向绕圈"，内外两圈转的方向正好相反（顺/逆时针）。最有用的地方是：如果这个体系是滑动铁电的，您**一翻电压，所有小磁针的绕向就整体掉头**——这就是用电压画自旋风向图的技术。一句话：**"Rashba 效应在动量空间画出的、可被电压翻转的螺旋自旋地图"**。

## 🏗️ 结构概览

Rashba 自旋纹理是反演破缺体系费米面等能圈上的切向螺旋自旋分布。

![图：HgI₂ 双层滑动铁电中的 Rashba 自旋纹理](../../raw/figures/chenStrongSlidingFerroelectricity2024/fig_4_5NCCX3U9.png)
*   **看图要点**：自旋沿等能圈切向环绕、内外分支螺旋性相反；极化翻转时螺旋性反转。
*   **来源**：[[../papers/chenStrongSlidingFerroelectricity2024]]

## 🧩 核心机制：螺旋纹理的几何与电控

### 1. 为什么是"切向螺旋"

- Rashba 哈密顿量 $H_R=\alpha_R(\boldsymbol{\sigma}\times\mathbf{k})\cdot\hat{\mathbf{z}}$ 的能量本征态要求自旋 $\langle \mathbf{s}\rangle$ 垂直于 $\mathbf{k}$ 且在面内。
- 于是等能面（费米圈）上，自旋沿**切向**排列，形成环形纹理；内、外两支能带（$\pm\alpha_R k$）螺旋性相反。
- 纹理的手性由 $\alpha_R$ 符号决定。

### 2. 滑动铁电如何翻转纹理

- 双层 HgI₂ 等滑动铁电体：极化 $+P\leftrightarrow -P$ 使垂直内电场反向 → $\alpha_R\to-\alpha_R$ → 纹理手性反转。
- 该过程**无磁、非易失、低能耗**，是"电压写自旋"的核心物理。

### 3. 器件意义

- 为 Datta–Das **spin-FET** 提供沟道材料：源端注入自旋后，沟道 Rashba 纹理决定进动，门电压翻转纹理可开关自旋电流。
- 逆过程（电流→自旋积累的 [[../concepts/edelstein-effect|Edelstein 效应]]）用于自旋读出，构成 MESO 逻辑的自旋-电荷转换环节。

## 📊 物理参数表

| 参数 | 含义 |
| --- | --- |
| $\alpha_R$ | Rashba 系数，决定纹理手性与劈裂强度 |
| 螺旋性 | 切向绕向（内外分支相反，极化翻转反转） |
| 等能圈 | 纹理所在动量路径（费米圈） |
| $+P/-P$ | 极化态，对应顺/逆时针纹理 |

## 🧭 近邻概念辨析

- **与 [[../concepts/rashba-effect|Rashba 效应]]**：效应强调**物理机制**（SIA+SOC 劈裂），纹理强调**动量空间几何呈现**，二者是同一物理的两种表述。
- **与 [[../concepts/spin-texture|自旋纹理]]**：Rashba 纹理是自旋纹理的**一种典型形态**（切向螺旋），自旋纹理还包含 Dresselhaus 型、面外型等。
- **与 [[../concepts/sliding-ferroelectricity|滑动铁电]]**：滑动铁电是**电控翻转手段**，Rashba 纹理是被调控的对象。

## 📚 相关论文

- [[../papers/chenStrongSlidingFerroelectricity2024]]：DFT+SOC 展示 HgI₂ 双层 $+P$/$-P$ 态 Rashba 纹理手性反转。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：将滑动铁电中自旋-动量锁定纹理列为重大机遇。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：综述滑动铁电体系 Rashba 纹理及其自旋电子效应。
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：评述 Rashba 纹理相关的自旋注入与读出机制。

## 🔗 关联概念与实体

- [[../concepts/rashba-effect|rashba-effect]]
- [[../concepts/spin-texture|spin-texture]]
- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/sliding-ferroelectricity|sliding-ferroelectricity]]
- [[../concepts/edelstein-effect|edelstein-effect]]
- [[../concepts/spin-hall-effect|spin-hall-effect]]
- [[../concepts/spin-transport|spin-transport]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../entities/HgI2|HgI2]]
- [[../entities/WTe2|WTe2]]
