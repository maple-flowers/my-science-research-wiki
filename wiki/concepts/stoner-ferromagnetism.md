---
tags: [concept, 2D-materials, density-functional-theory, ferroelasticity, ferroelectric-tunnel-junction, magnetoelectric-coupling, mxene, ferromagnetism]
title: Stoner铁磁性 / Stoner Ferromagnetism
type: concept
status: mature
domain: [magnetism, 2d-materials, mxene]
mechanism: 巡游电子体系中交换劈裂与态密度在费米面附近的竞争（Stoner 判据 I·N(E_F)>1）决定铁磁稳定性
related_concepts: [stoner-model, density-functional-theory, spin-polarization, ferromagnetism, mxene, strain-engineering, magnetic-anisotropy]
papers: [zahraCriticalAnalysisFerroelectric2025]
updated: 2026-08
---

# Stoner铁磁性 / Stoner Ferromagnetism

Stoner 铁磁性（Stoner Ferromagnetism）是巡游电子体系铁磁性的经典图像：铁磁稳定性由 Stoner 判据 $I\,N(E_F)>1$ 决定，其中 $I$ 为交换（Stoner）参数、$N(E_F)$ 为费米面处态密度。在 MXene 这类功能可调二维平台上，本征无铁磁的体系可通过官能团化、掺杂、应变等策略提高 $N(E_F)$ 与自旋极化，从而诱导 Stoner 型铁磁序（[[../papers/zahraCriticalAnalysisFerroelectric2025]]）。

## 👵 太奶导读

乖孙，这一条讲的是「Stoner 铁磁性」——给"没磁性的材料"点石成金的那道咒语。太奶打个比方：材料里的电子就像一屋子人，要是屋里能塞的人越多（态密度大），而且大家越"合群"（交换作用强），那屋子里的自旋就会齐刷刷朝上，冒出磁性。MXene 这种片片材料本来"人不多"（没磁性），但给它穿上不同的"官能团衣服"（-OH、-O、-F）或者掺点杂质，就能把"人气"（费米面态密度）攒起来，磁性就来了。一句话：**让电子"人多势众"又"同向而行"，Stoner 铁磁就出现了**。

## 🧩 什么是 Stoner 铁磁性？

- **定义**：巡游（非局域）电子体系的铁磁性，磁性来自费米面附近同一能带的多数/少数自旋占据差异，而非局域磁矩排列。
- **Stoner 判据**：当交换能增益 $I\,N(E_F)>1$ 时，自旋劈裂自发出现。因此提升 $N(E_F)$（如平带、缺陷态、官能团杂化）是诱导 Stoner 磁性的关键。
- **与 MXene 的联系**：MXene（如 Ti₃C₂Tₓ）本征中心对称、强共价，无本征铁电/铁磁；但其表面官能团 T（-OH/-O/-F 等）可显著调制电子结构，是实现 Stoner 铁磁的灵活平台。

![图：MXene 结构基元与电子态密度自旋极化](../../raw/figures/zahraCriticalAnalysisFerroelectric2025/fig_3_3DJURTX2.png)
- **关键特征**：MXene 层状结构与费米面处态密度示意，展示官能团化对自旋极化的调制。
- **来源**：[[../papers/zahraCriticalAnalysisFerroelectric2025]] -> [[../figures/crystal-structures|晶体结构与能带]]

## ⚡ 核心机制：交换劈裂 × 态密度工程

1. **交换参数 $I$**：由 3d 过渡金属（如 Ti、V、Mn、Cr）的 d 态决定；官能团与金属 d 态的杂化改变 $I$。
2. **态密度 $N(E_F)$**：MXene 表面终止基团（-O 强、-F 弱）与金属层配比直接决定费米面附近态密度；平带/范霍夫奇点可放大 $N(E_F)$，触发 Stoner 判据。
3. **掺杂与缺陷**：过渡金属替位（如 Gd 掺杂）、空位等引入自旋极化态，进一步提升多数自旋通道占据差，得到非整数磁矩（Stoner 特征，如 Cr₂COOH 体系计算磁矩）。
4. **应变与复合**：拉伸/压缩应变调谐带宽与 $N(E_F)$；与铁电材料（BaTiO₃、PZT）复合则引入界面电荷与自旋重排，实现磁电耦合。

![图：官能团化 MXene 的自旋极化态密度与磁矩](../../raw/figures/zahraCriticalAnalysisFerroelectric2025/fig_10_8U7ZULVR.png)
- **关键特征**：典型官能团化 MXene（如 Cr₂COOH 类）的自旋分辨态密度与磁矩，佐证 Stoner 巡游磁性。
- **来源**：[[../papers/zahraCriticalAnalysisFerroelectric2025]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

![图：掺杂诱导铁磁的磁滞回线](../../raw/figures/zahraCriticalAnalysisFerroelectric2025/fig_11_YQE9M99K.png)
- **关键特征**：掺杂体系（如 Gd 掺杂）的 M–H 回线，显示铁磁序被成功诱导。
- **来源**：[[../papers/zahraCriticalAnalysisFerroelectric2025]] -> [[../figures/crystal-structures-xrd-phases|结构与相]]

## 🧲 MXene 铁磁-铁电共存（多铁策略）

- **对称性破缺**：Janus 结构、梯度官能团化打破中心对称，可诱导铁电性；与 Stoner 铁磁结合形成多铁 MXene。
- **铁电-铁磁复合**：MXene/铁电体（BaTiO₃、BiFeO₃、PZT）异质结或三明治结构，通过界面应变与电荷转移实现磁电耦合与铁电极化开关磁性。
- **器件优势**：铁电忆阻、电池、自旋电子器件中展现低功耗、非易失优势；室温稳定与规模化仍是关键挑战。

![图：MXene-铁电复合器件的界面磁电响应](../../raw/figures/zahraCriticalAnalysisFerroelectric2025/fig_8_75AQ6FBG.png)
- **关键特征**：MXene/铁电异质结中电场驱动的极化-磁性响应（蝴蝶曲线类特征）。
- **来源**：[[../papers/zahraCriticalAnalysisFerroelectric2025]] -> [[../figures/crystal-structures-xrd-phases|结构与相]]

## 🔬 物理参数表

| 属性 | 数值/特征 | 说明 |
| :--- | :--- | :--- |
| Stoner 判据 | $I\,N(E_F)>1$ | 巡游铁磁阈值条件 |
| 磁矩 | 非整数（Stoner 特征） | 如 Cr₂COOH 类官能团化体系 |
| 官能团调制 | -O 强 / -F 弱 | 决定 $N(E_F)$ 与磁性强度 |
| 掺杂 | 3d/4f 替位（如 Gd） | 诱导铁磁回线 |
| 多铁路线 | Janus / 梯度官能团 + 铁电复合 | 对称性破缺 + 界面耦合 |

> 注：上表汇总自 [[../papers/zahraCriticalAnalysisFerroelectric2025]] 的综述内容，具体数值以原文为准。

## 🧭 近邻概念辨析

- **与 [[../concepts/stoner-model|Stoner 模型]]**：本条目是 Stoner 模型在二维 MXene 材料上的具体应用——以"态密度工程"为设计杠杆。
- **与局域磁矩铁磁**：Stoner 铁磁巡游、磁矩非整数；局域磁矩（如 Heisenberg）则磁矩整数、适合局域交换描述。
- **与 [[../concepts/magnetoelectric-coupling|磁电耦合]]**：MXene 通过铁电复合获得磁电耦合，而 Stoner 机制本身不产生磁电；二者结合才形成多铁 MXene。
- **与 [[../concepts/janus-mxene|Janus MXene]]**：Janus 结构是诱导铁电/磁电的对称性破缺手段，为 Stoner 磁性的"兄弟机制"。

## 📚 相关论文 (Related Papers)

- [[../papers/zahraCriticalAnalysisFerroelectric2025]]：本页唯一引文，其对本条目的具体贡献在于给出 Stoner 判据的一个**可工程化实现路径**——指出 MXene 的磁性主要来自过渡金属 M 的 d 轨道电子，通过掺杂（Gd、Nb 等）、官能团化、应变、缺陷等手段调控费米能级附近的电子态密度，使自旋向上与向下的电子数失衡，即可在本征无磁的 Ti₃C₂ 等体系中诱导出铁磁序。⚠️ 该文本身未使用 Stoner 判据或 Stoner 模型的表述（笔记中「Stoner」仅 1 次命中），「提高 $N(E_F)$ 以满足 $I\,N(E_F)>1$」这一层解读是本页所加，非原文语言。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/ferroelasticity|ferroelasticity]]
- [[../concepts/ferroelectric-tunnel-junction|ferroelectric-tunnel-junction]]
- [[../concepts/magnetoelectric-coupling|magnetoelectric-coupling]]
- [[../concepts/multiferroicity|multiferroicity]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/strain-engineering|strain-engineering]]
- [[../concepts/topological-defects|topological-defects]]
- [[../concepts/janus-mxene|janus-mxene]]
- [[../concepts/i-mxene|i-mxene]]
- [[../concepts/surface-terminations-tx|surface-terminations-tx]]
- [[../concepts/v2c-mxene|v2c-mxene]]
- [[../concepts/ti3c2tx|ti3c2tx]]
- [[../concepts/ferroelectric-metal|ferroelectric-metal]]
- [[../concepts/stoner-model|stoner-model]]
- [[../entities/BiFeO3|BiFeO3]]
