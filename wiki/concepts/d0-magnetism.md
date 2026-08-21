---
tags: [concept, 2d-materials, multiferroicity, magnetoelectric-coupling, strain-engineering, density-functional-theory, magnetic-2d, skyrmion, dmi]
title: d0磁性 / d0 Magnetism
type: concept
status: mature
domain: [magnetism, 2d-materials, spintronics]
mechanism: p 轨道电子（d0 构型）在小磁矩、巡游性下驱动铁磁性与强 DMI，形成高稳定拓扑自旋织构
related_concepts: [stoner-model, skyrmion, bimeron, dzyaloshinskii-moriya-interaction, half-metallicity, multiferroicity, magnetoelectric-coupling, strain-engineering, ferroelectricity]
papers: [wangTunableD0Topological2025b]
updated: 2026-08
---

# d0磁性 / d0 Magnetism

d0 磁性（d0 Magnetism）指磁矩不由传统 d/f 轨道电子、而由 **p 轨道电子（或空 d 壳层的配体）** 承载的一类磁性。因为磁性离子本身呈 d0（无 d 电子）构型，磁矩必须来自与配体 p 轨道的杂化或非磁元素上的自旋极化。本条目以单层 In₂NO₂ 为范例，阐述 d0 磁性如何与铁电、半金属、DMI 结合，驱动高稳定性的斯格明子与双半子等拓扑自旋织构，并实现电场/应变多维度调控（[[../papers/wangTunableD0Topological2025b]]）。

## 👵 太奶导读

乖孙，这一条讲的是「d0 磁性」——一种不是靠铁、钴、镍这些金属的 d 电子，而是靠氮、氧这类轻元素的 p 电子来产生磁性的新花样。平时我们以为"没 d 电子的材料就没磁性"，这一条偏要打破这个常识：单层 In₂NO₂ 这种材料，磁性全来自 N 原子的 p 电子，磁矩小、又很"溜"（巡游），结果反而让里面的斯格明子（那种像小旋风一样的自旋结构）在很高的温度下都稳稳当当。更妙的是，这材料天生就带铁电，翻一翻它的极化方向，斯格明子的"旋向"就跟着反过来；拉一拉它（加应变），小旋风的密度和存活范围还能变大。一句话：**不用重金属，p 电子也能撑起磁性、还能被电场和应变随便摆弄**。

## 🧩 什么是 d0 磁性？

- **定义**：磁矩来源不含 d/f 电子，而是由配体 p 轨道（如 O-2p、N-2p）的巡游自旋极化或缺陷/掺杂诱导的自旋极化承载。In₂NO₂ 中 In 为 [Kr]4d¹⁰5s⁰5p⁰（d0），N 为 1s²2s²2p⁵，仅一个未配对 p 电子贡献磁性。
- **与常规 d 磁性的区别**：d 磁性局域、磁矩大（3–5 μB）、DMI 弱；d0 磁性巡游、磁矩小（总磁矩 1 μB/f.u.，N 上 M_N=0.584 μB 为非整数，体现 Stoner 巡游铁磁特征），DMI 反而可被重配体（In）的 SOC 放大。
- **定量特征**：单层 In₂NO₂ 为 P3m1（No.156）三角晶格，O–In–N–In–O 五原子层，a=3.41 Å；声子谱无虚频、AIMD 证稳定；能带呈半金属性（一自旋通道穿费米面、另一通道有带隙），SOC 影响很小（[[../papers/wangTunableD0Topological2025b]]）。

![图：In₂NO₂ 晶体结构、能带、差分电荷密度与态密度](../../raw/figures/wangTunableD0Topological2025b/fig_1_7FXHGJ8M.png)
- **关键特征**：(a) O–In–N–In–O 五层结构及 ±P 两本征铁电极化态；(b) w/o 与 w/ SOC 自旋分辨能带，一通道金属、一通道带隙（半金属）；(c) 差分电荷密度显示 In 失电子、N/O 得电子；(d) E_f 附近态密度几乎全由 N-2p 贡献，是 d0 磁性的直接证据。
- **来源**：[[../papers/wangTunableD0Topological2025b]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

## ⚡ 核心机制：p 轨道磁性 × 重配体 SOC × 铁电破缺

1. **磁性来源（p 轨道 + Stoner 巡游）**：N-2p 单电子自旋极化给出总磁矩 1 μB/f.u.，M_N=0.584 μB 的非整数值表明磁矩离域、宜用 Stoner 模型描述；U 值对能带几乎无影响（取 U=0），进一步佐证巡游本质（[[../concepts/stoner-model|Stoner 模型]]）。
2. **强 DMI 的来源（重配体 SOC，而非磁性元素）**：虽然 N、O 轻、SOC 弱，但较重的 In 贡献了主要原子分辨 SOC 能量差 ΔE_SOC，是体系强 DMI 的物理来源——打破"只有重磁性元素才有大 DMI"的直觉。
3. **铁电破缺（本征 ±P 态）**：In₂NO₂ 本征具有面外铁电极化 ±P。磁参数（J、DMI）与极化符号直接关联：面内 DMI d_k 在 +P/−P 态分别为 +0.9367/−0.9367 meV，符号相反 → 斯格明子手性相反，可被面外电场可逆翻转。
4. **交换与各向异性**：J=32.2194 meV（铁磁）、各向异性交换 k≈0、K_MCA=18 μeV、K_MSA=3.8 μeV、单离子各向异性 K=14.2 μeV（面外易轴）；蒙特卡洛估计 T_C≈105 K。面外 DMI d_⊥ 因 C3 对称可忽略。

![图：原子分辨 SOC、自旋织构与 ±P 态斯格明子手性](../../raw/figures/wangTunableD0Topological2025b/fig_2_QZWY2VAA.png)
- **关键特征**：(a) In 的 ΔE_SOC 最大，是强 DMI 的来源；(b) 0 T 为宽磁畴、1 T 收缩为离散斯格明子；(c) +P/−P 态 d_k 符号相反，斯格明子手性相反。
- **来源**：[[../papers/wangTunableD0Topological2025b]] -> [[../figures/electronic-bands-cdw-transport|CDW与输运性质]]

## 🌀 拓扑自旋织构：斯格明子与双半子

- **垂直磁场 B_z**：1–5 T 形成 d0 斯格明子，2 T 时拓扑荷 Q 达峰值 8；5 T 时直径约 9.6 nm；5.5 T 进入平庸铁磁态。Q 在 0–150 K 稳定，**甚至超过 T_C≈105 K**，归因于 p 轨道磁性小磁矩与离域化带来的超 T_C 稳定性。
- **面内磁场 B_x**：1.5–3 T 形成双半子，0–120 K 稳定，130 K 进入无序相。
- **电场控制手性**：翻转铁电极化 → DMI 反号 → 斯格明子手性反转。

![图：斯格明子与双半子的磁场与温度演化](../../raw/figures/wangTunableD0Topological2025b/fig_3_UYVUXL8I.png)
- **关键特征**：(a) B_z 从 0 到 5.5 T 的织构快照；(b) B_z=2 T 时 Q 在 0–150 K 内小幅波动；(c,d) 面内磁场下双半子 0–120 K 稳定。
- **来源**：[[../papers/wangTunableD0Topological2025b]] -> [[../figures/electronic-bands-cdw-transport|CDW与输运性质]]

## 🧲 应变与异质结调控

- **应变工程**：拉伸应变使 d_k 单调增加、J 略减，|d_k/J| 显著增大，SIA 保持为正并增强；5% 拉伸下斯格明子可在 B_z=4–11 T 极宽窗口内纯相存在、密度增大；压缩应变影响很小。器件可选用约 3% 应变（MoS₂ 器件典型 ≤2.5%、WS₂ 已达 4%）。
- **In₂NO₂/MoSe₂ 异质结**：晶格失配仅 2.4%；±P 态因功函数失配不同导致界面电荷转移量不同，J、d_k 等参数显著差异（+P 态 J 明显下降、d_k 反号）。−P 态 B_z<5.9 T 为斯格明子相，+P 态仅在 5.9–7.0 T 出现斯格明子相（5.9 T 时直径 7.96 nm）。**在约 5.9 T 固定磁场下，电场翻转极化即可在铁磁"0"态与斯格明子"1"态间非易失切换**，演示磁电拓扑存储二进制编码。

![图：应变依赖的磁参数与应变-磁场拓扑相图](../../raw/figures/wangTunableD0Topological2025b/fig_4_R8KDU8IB.png)
- **关键特征**：拉伸应变下 |d_k/J| 显著上升；−4%–5% 内 SIA 为正、面外易轴，由 K_MCA 主导；5% 拉伸时斯格明子稳定窗口扩展到 4–11 T。
- **来源**：[[../papers/wangTunableD0Topological2025b]] -> [[../figures/crystal-structures-xrd-phases|XRD与相变]]

![图：In₂NO₂/MoSe₂ 异质结及 ±P 态 Q–B_z 曲线](../../raw/figures/wangTunableD0Topological2025b/fig_5_GYG5QB2H.png)
- **关键特征**：(a) ±P 堆叠模型；(b) 两态界面差分电荷密度；(c,d) −P/+P 态 Q 随 B_z 变化，绿色区 Q=0（"0"态）、粉色区 Q>0（"1"态），展示电场开关"0/1"。
- **来源**：[[../papers/wangTunableD0Topological2025b]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

## 🔬 物理参数表

| 属性 | 数值 | 说明 |
| :--- | :--- | :--- |
| 晶格常数 a | 3.41 Å | P3m1 三角晶格，O–In–N–In–O 五层 |
| 总磁矩 | 1 μB/f.u. | N 上 M_N=0.584 μB（Stoner 巡游） |
| 交换 J | 32.2194 meV | 铁磁耦合 |
| 面内 DMI d_k | ±0.9367 meV | +P/−P 符号相反 |
| 单离子各向异性 K | 14.2 μeV | 面外易轴（K_MCA=18 μeV、K_MSA=3.8 μeV） |
| 居里温度 T_C | ≈105 K（MC） | 织构超 T_C 稳定 |
| 斯格明子 | B_z=1–5 T，Q 峰值 8@2T，直径 9.6 nm@5T | 0–150 K 稳定 |
| 双半子 | B_x=1.5–3 T | 0–120 K 稳定 |
| 异质结失配 | 2.4% | In₂NO₂/MoSe₂ |
| 切换磁场窗口 | ≈5.9 T | 电场翻转极化实现"0/1"非易失切换 |

> 注：上表为 DFT 典型数值，来源见 [[../papers/wangTunableD0Topological2025b]] 的表格与正文。

## 🧭 近邻概念辨析

- **与 d 轨道磁性（如传统过渡金属磁体）的区别**：d0 磁性磁矩小、巡游，赋予拓扑织构更高的温度/磁场稳定性；d 磁性局域强磁矩、尺寸大、能耗高。
- **与 [[../concepts/stoner-model|Stoner 模型]]**：d0 磁性的非整数磁矩是 Stoner 巡游铁磁的标志，U=0 仍保持磁性进一步佐证巡游本质。
- **与 [[../concepts/dzyaloshinskii-moriya-interaction|DMI]]**：d0 体系的大 DMI 可由非磁性重配体（In）的 SOC 提供，且被本征铁电破缺"锁存"符号，为电控拓扑磁结构提供了新自由度。
- **与 [[../concepts/skyrmion|斯格明子]]/[[../concepts/bimeron|双半子]]**：d0 磁性是该类拓扑织构在高磁场/高温下的稳定载体。

## 📚 相关论文 (Related Papers)

- [[../papers/wangTunableD0Topological2025b]]：提出单层 In₂NO₂ 为 d0 拓扑磁体，系统给出磁性起源（N-p 轨道 + In-SOC）、斯格明子/双半子相图及应变/电场调控方案。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/2d-materials|2d-materials]]
- [[../concepts/multiferroicity|multiferroicity]]
- [[../concepts/magnetoelectric-coupling|magnetoelectric-coupling]]
- [[../concepts/strain-engineering|strain-engineering]]
- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/berry-phase|berry-phase]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/topological-defects|topological-defects]]
- [[../concepts/skyrmion|skyrmion]]
- [[../concepts/bimeron|bimeron]]
- [[../concepts/dzyaloshinskii-moriya-interaction|dzyaloshinskii-moriya-interaction]]
- [[../concepts/heisenberg-model|heisenberg-model]]
- [[../concepts/micromagnetic-simulation|micromagnetic-simulation]]
- [[../concepts/topological-spin-texture|topological-spin-texture]]
- [[../concepts/stoner-model|stoner-model]]
- [[../concepts/half-metallicity|half-metallicity]]
