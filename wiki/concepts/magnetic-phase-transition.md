---
tags: [concept, magnetism, condensed-matter]
title: 磁性相变 / Magnetic Phase Transition
type: concept
status: mature
year: 2024
domain: [magnetism, condensed-matter]
mechanism: 磁性有序态（铁磁/反铁磁/螺旋）在临界温度处与顺磁态之间转变，序参量为自发磁化（或交错磁化/螺旋波矢），由 Landau 自由能描述，临界行为由临界指数刻画
related_concepts: [ferromagnetism, antiferromagnetism, curie-temperature, neel-temperature, phase-transition, order-parameter, landau-theory, helical-magnetism, molecular-field]
papers: [liPhaseTransitions2D2021, chenFerromagneticNonmagnetic1T2022]
updated: 2026-08-20
---

# magnetic-phase-transition

磁性相变（magnetic phase transition）指**磁性材料在温度、磁场、压力或组分等外参量驱动下，从一个磁性有序态（铁磁/反铁磁/螺旋等）转变为另一磁态或顺磁态的过程**。铁磁-顺磁转变在居里温度 $T_C$ 处发生，反铁磁-顺磁转变在奈尔温度 $T_N$ 处发生。连续（二阶）磁性相变由序参量（自发磁化 $M$ 或交错磁化）的连续涌现刻画，可用 Landau 自由能与临界指数理论系统描述；一阶转变则伴随磁结构突变与热滞。

## 👵 太奶导读

太奶啊，磁体烧热了会"退磁"：原本齐刷刷排队的磁针（铁磁），温度一高就乱了套，变成乱哄哄的顺磁。这个从"整齐"到"混乱"的分界线温度叫居里温度。在临界点附近有个神奇现象：磁针排得有多整齐（磁化强度）不是慢慢变，而是以"九次方根"这种奇怪的幂次趋近零——这规律对铁、镍、磁铁矿全都一样，科学家把这叫"普适性"。就好像水在临界点的怪异行为，不同磁体在磁性相变点附近的行为也惊人地一致。

## 🏗️ 结构概览：磁性相变的类型谱系

磁性相变可按序参量与外参量两个维度分类：

- **按有序态分**：
  - 铁磁-顺磁转变（$T_C$）：序参量为自发磁化 $\mathbf{M}$，由交换作用 $J>0$ 驱动（[[../concepts/ferromagnetism|铁磁性]]）。
  - 反铁磁-顺磁转变（$T_N$）：序参量为交错磁化（staggered magnetization），磁化率在 $T_N$ 出现尖峰（[[../concepts/antiferromagnetism|反铁磁性]]）。
  - 螺旋/自旋密度波转变：序参量为螺旋波矢 $\mathbf{q}$，见 [[../concepts/helical-magnetism|螺旋磁序]]。
  - 磁性-超导/CDW 耦合转变：磁性序与电荷序/超导序共存竞争（本库 1T′ 体系磁性-非磁性转变论文）。
- **按相变阶数分**：
  - 二阶（连续）转变：序参量连续涌现，临界涨落显著，由临界指数刻画。
  - 一阶转变：磁序突变，伴随热滞与潜热（如磁场驱动的一阶磁变、马氏体型转变）。
- **按驱动参量分**：温度驱动、磁场驱动（变磁转变、场诱导铁磁）、压力/应变驱动、掺杂与栅压驱动（2D 材料中载流子调控磁序，本库 2D 相变综述）。

## 🧩 核心内容与机制 (Core Content)

- **序参量**：铁磁序用自发磁化 $\mathbf{M}$（矢量），反铁磁用交错磁化（子晶格磁化差），螺旋用序波矢 $\mathbf{q}$；序参量的出现标志着对称性破缺。
- **Landau 理论**：自由能按序参量展开 $F=F_0+a(T-T_c)\phi^2+b\phi^4+\cdots$，$a>0$ 时系数变号驱动相变；$b<0$ 或含三次项时为一阶转变（[[../concepts/landau-theory|朗道理论]]）。
- **平均场与临界指数**：分子场近似（[[../concepts/molecular-field|外斯分子场]]）预言 $\beta=1/2$、$\gamma=1$、$\nu=1/2$，但真实体系（如 3D 海森堡普适类 $\beta\approx0.37$）因临界涨落偏离平均场。
- **临界温度**：$T_C$（[[../concepts/curie-temperature|居里温度]]）、$T_N$（[[../concepts/neel-temperature|奈尔温度]]）由交换作用强度决定，$k_B T_C \sim z J S^2$。
- **相变与磁电耦合**：多铁材料中磁性相变与铁电相变可耦合（如 BiFeO₃ 在 $T_N$ 附近磁结构变化），2D 材料中相变温度与堆垛/层数/载流子密切相关（本库 2D 相变综述论文）。
- **2D 磁性的特殊问题**：Mermin-Wagner 定理禁止各向同性 2D 系统在有限温度出现长程序，2D 磁性相变依赖磁各向异性或层间耦合（本库 2D 相变综述论文）。

## 📊 物理参数表

| 相变类型 | 序参量 | 临界温度 | 标志实验特征 |
|---|---|---|---|
| 铁磁-顺磁 | 自发磁化 $\mathbf{M}$ | 居里温度 $T_C$ | $\chi$ 在 $T_C$ 发散（Curie-Weiss），比热 $\lambda$ 形峰 |
| 反铁磁-顺磁 | 交错磁化 | 奈尔温度 $T_N$ | $\chi$ 在 $T_N$ 出现尖峰（各向异性） |
| 螺旋-顺磁 | 螺旋波矢 $\mathbf{q}$ | $T_N$（螺旋序温度） | 中子衍射卫星峰，热导/比热异常 |
| 磁性-电荷序 | 磁序+CDW 序 | 共存/竞争区间 | 电阻-磁化关联，场诱导跃变（本库 1T′ 体系） |
| 临界指数（平均场） | $\beta=1/2$, $\gamma=1$, $\nu=1/2$ | — | 偏离真实体系（3D 海森堡 $\beta\approx0.37$） |

## 🧭 近邻概念辨析

- **磁性相变 vs 相变（[[../concepts/phase-transition|phase-transition]]）**：磁性相变是相变的磁有序子类，序参量具有矢量/序波矢性质；相变是更一般的概念，涵盖结构、电荷、拓扑等所有相变。
- **磁性相变 vs 序参量（[[../concepts/order-parameter|order-parameter]]）**：序参量是描述相变的核心概念工具；磁性相变以自发磁化等磁序量为序参量。
- **磁性相变 vs 朗道理论（[[../concepts/landau-theory|landau-theory]]）**：朗道理论是描述相变的唯象框架，磁性相变是其最经典应用场景之一。
- **铁磁相变 vs 反铁磁相变**：铁磁相变序参量为净磁化（在 $T_C$ 以下自发出现），反铁磁相变序参量为交错磁化（净磁化恒为零，$T_N$ 处磁化率反常）。
- **磁性相变 vs 超导/铁电相变**：三者同为对称性破缺相变但序参量不同（磁化/配对波函数/电极化），多铁与磁性超导体系出现序间耦合。

## 📚 相关论文 (Related Papers)

- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials（2D 材料中磁性等相变与维数效应综述）
- [[../papers/chenFerromagneticNonmagnetic1T2022]] — Ferromagnetic and nonmagnetic 1T′ charge density wave states in transition metal dichalcogenides: Physical mechanisms and charge doping induced reversible transition（磁性-非磁性转变的微观机制）

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferromagnetism|铁磁性]]：铁磁-顺磁相变的有序态。
- [[../concepts/antiferromagnetism|反铁磁性]]：反铁磁-顺磁相变的有序态。
- [[../concepts/curie-temperature|居里温度]]：铁磁相变临界温度。
- [[../concepts/neel-temperature|奈尔温度]]：反铁磁相变临界温度。
- [[../concepts/phase-transition|相变]]：磁性相变的所属大类。
- [[../concepts/order-parameter|序参量]]：描述相变的核心概念。
- [[../concepts/landau-theory|朗道理论]]：磁性相变的唯象描述框架。
- [[../concepts/helical-magnetism|螺旋磁序]]：以波矢为序参量的磁性相变。
- [[../concepts/molecular-field|外斯分子场]]：磁性相变的平均场近似。
