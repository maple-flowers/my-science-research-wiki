---
tags: [concept, computational-physics, vasp, dft]
title: DFT+U / 密度泛函理论加 U
type: concept
status: mature
domain: [computational-physics, electronic-structure]
mechanism: 通过引入在位库仑排斥项 (Hubbard U) 来修正标准泛函对强关联体系（如过渡金属氧化物）中电子局域化的描述不足。
related_concepts: [density-functional-theory, self-consistent-field-cycle, projector-augmented-wave]
papers: [dudarevElectronenergylossSpectraStructural1998a, zhouFirstprinciplesPredictionRedox2004]
updated: 2026-08
---

# DFT+U / 密度泛函理论加 U (Hubbard-corrected Density Functional Theory)

DFT+U（也常写为 LDA+U 或 GGA+U）是研究强关联体系（尤其是含有 $d$ 或 $f$ 电子的过渡金属氧化物、稀土材料）的必备工具。它修正了标准 DFT 泛函（如 LDA 或 PBE）中普遍存在的“自相互作用误差”，从而能准确描述莫特绝缘体和磁性态。

## 👵 太奶导读

太奶，这 DFT+U 啊，就像是给那些特别“宅”的电子量身定制的规矩。

咱们普通的计算办法（标准 DFT）比较乐观，它总觉得电子喜欢到处乱跑（离域）。但对于铁、镍这类过渡金属里的某些电子来说，它们特别喜欢宅在自己的小窝里（局域化），而且脾气很大：要是两个电子非要挤在一个窝里，它们会因为互相讨厌（在位库仑排斥）而产生巨大的能量损失。

标准办法看不出这种“宅男”电子的痛苦，经常错误地把本来该是绝缘的石头算成了能导电的金属。这 DFT+U 啊，就是专门加了一个叫 $U$ 的补丁，给这些宅在窝里的电子定了个规矩：既然你非要占着这个位子，那就得给你加点额外的能量约束。这样一改，咱们算出来的带隙和磁性一下就跟实验对上号了，真是药到病除！

## 🏗️ 结构概览

DFT+U 的核心是在能量泛函中增加了一项轨道依赖的项。

![图：LSDA+U 修正前后的电荷密度差](../../raw/figures/dudarevElectronenergylossSpectraStructural1998a/fig_2_GBIMQZ9U.png)
*   **看图要点**：图中对比了 NiO 体系中 LSDA 与 LSDA+U 的电荷分布。可以看到加入 U 后，镍离子周围的电荷变得更加收缩、局域，这正是 U 修正物理实质的直观体现。
*   **来源**：[[../papers/dudarevElectronenergylossSpectraStructural1998a]] -> [[../figures/crystal-structures-bulk|体相晶体结构]]

## 🧩 物理机制

### 1. 修正自相互作用误差
标准 DFT 泛函在处理局域电子时，会错误地产生电子与自身发生排斥的假象（Self-interaction error），导致能带过宽、带隙偏小甚至消失。$U$ 参数通过引入一个惩罚项，强制轨道占据数向 0 或 1 两极分化，从而打开关联带隙。

### 2. Dudarev 方法与有效 U
在 VASP 中常用的 Dudarev 方案中，能量修正项形式简洁：
$$ E_{DFT+U} = E_{DFT} + \frac{U_{eff}}{2} \sum_{\sigma} [\text{Tr}(\rho^{\sigma}) - \text{Tr}(\rho^{\sigma}\rho^{\sigma})] $$
其中 $U_{eff} = U - J$，$U$ 是在位库仑排斥，$J$ 是 Hund 交换能。这个形式是旋转不变的，非常适合在平面波基组中实现。

### 3. 光谱与结构的统一
S. L. Dudarev 等人的工作证明，使用合理的 $U$ 值不仅可以修正电子能带结构（如带隙、DOS），还能同时修正体系的几何结构（如晶格常数、体模量）。这说明 $U$ 修正抓住了强关联体系的核心物理本质。

## 📚 相关论文 (Related Papers)

- [[../papers/dudarevElectronenergylossSpectraStructural1998a]]：旋转不变 DFT+U 方法的奠基论文，详细论述了 NiO 的结构与光谱修正。
- [[../papers/zhouFirstprinciplesPredictionRedox2004]]：展示了 DFT+U 在预测电池材料氧化还原电位中的巨大成功。
- [[../papers/krishnamurthiSpinChargeDensity2020]] — Spin/charge density waves at the boundaries of transition metal dichalcogenides
- [[../papers/zhouFirstprinciplesPredictionRedox2004]] — First-principles prediction of redox potentials in transition-metal compounds with LDA+U

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[density-functional-theory|DFT]]：$U$ 修正的基座。
- [[projector-augmented-wave|PAW]]：在 VASP 中，DFT+U 通常作用于 PAW 势的局域分量上。
- MnVO3 / NiO (entities)：典型的强关联氧化物，必须使用 DFT+U 才能准确描述。
- VASP (entity)：LDAU = .TRUE. 及 LDAUU/LDAUJ 参数。

## 🏷️ 专业名词别名

- `dft-plus-u`（concepts）
