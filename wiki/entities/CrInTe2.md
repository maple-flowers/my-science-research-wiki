---
tags: [entity, material, magnetic, 2D, vdW, multiferroic, topological, ferromagnetic-metal]
title: 碲铟化铬 / Chromium Indium Telluride (CrInTe2)
type: entity
status: mature
category: [D01, D02, Z02]
formula: CrInTe2
aliases: ["CrInTe₂", "chromium indium telluride"]
class: [vdW, ferromagnetic-metal, topological-magnet]
properties: [ferromagnetism, dzyaloshinskii-moriya-interaction, topological-spin-textures, magnetoelectric-coupling, artificial-multiferroic]
related_entities: [In2Se3, Cr2Ge2Te6, CrI3]
key_quantities:
  stacking: "Te2–Cr–Te1–In 层序，与 In2Se3 晶格失配 ~0.7%"
  J: "P↑ 11.69 meV → P↓ 9.85 meV"
  DMI_dpar: "P↑ 1.87 meV → P↓ 1.98 meV（增强 ~6%）"
  MAE_K: "P↑ 2.44 meV/Cr → P↓ 1.96 meV/Cr（抑制 ~20%）"
  stability: "P↓ 态斯格明子晶格在 200 K 仍稳定，4.4 T 下密度 >628 μm⁻²"
  note: "无量纲判据 κ=(π²/4)(2JK/3d||²)，5<|κ|<10 稳定孤立斯格明子/双半子"
papers: [zhangNonvolatileControlTopological2025]
updated: 2026-08
---

# 碲铟化铬 / Chromium Indium Telluride (CrInTe2)

CrInTe2 是一种理论提出的二维范德华铁磁金属，单层具有 **Te2–Cr–Te1–In** 的四原子层堆垛。它本身不是铁电体，但与铁电半导体 α-In2Se3 构成异质结后，翻转 In2Se3 的面外极化即可非易失地调控界面的 Dzyaloshinskii–Moriya 相互作用（DMI）与磁各向异性能（MAE），从而在铁磁态与斯格明子晶格之间开关，实现"电写磁拓扑"。它是二维多铁异质结调控拓扑磁性的代表体系 [[../papers/zhangNonvolatileControlTopological2025]]。

## 👵 太奶导读

太奶，这 CrInTe2 您就想成一张上面满是小磁针的金属薄片。小磁针若按部就班全朝一个方向站，就是普通的"铁磁"；可要是围圈圈排成一个个小漩涡，那漩涡就叫"斯格明子"——它是个有拓扑"身份证号"的小疙瘩，搬来搬去不易散，将来能当极小的存储单位。难就难在：怎么让这些小漩涡想开就开、想关就关，还得省电、断了电也不丢。

科学家的招儿是"贴搭档"：把这张磁片跟一片会记电方向的硒化铟（In2Se3）背对背贴好。硒化铟一朝上一朝下，贴脸处的电子云和原子轨道就变了样，于是磁片里让磁针扭圈的那股劲（叫 DMI）变大了约百分之六，而把磁针摁直的那股劲（叫各向异性能）变小了约百分之二十。一增一减，漩涡就冒出来了；电方向一翻回去，漩涡又抹平成齐刷刷的铁磁。算出来这些漩涡能耐到约零下七十度（200 K），密度还挺高。更妙的是还能催生出叫"双半子"的另一种小疙瘩，它被电流推着走时不怎么跑偏，适合做赛道存储。这整套就是用电来指挥磁的拓扑花样，是典型的人工多铁。

## 🏗️ 结构概览

CrInTe2 单层为 Te2–Cr–Te1–In 四原子层堆垛，Cr 提供局域磁矩；α-In2Se3 为 Se–In–Se–In–Se 五层铁电半导体，具有两种可翻转的面外极化态 P↑/P↓。两者晶格失配仅约 0.7%，堆叠后界面破缺空间反演对称，是产生界面 DMI 的结构前提。

![图：CrInTe2/In2Se3 异质结晶体结构——(a)单层 CrInTe2 俯/侧视图，(b)单层 In2Se3 及 P↑/P↓ 极化态，(c)异质结不同堆叠构型](../../raw/figures/zhangNonvolatileControlTopological2025/fig_1_JDGLCTDB.png)
*   **看图要点**：(a) 中可见 Cr 层夹在 Te/In 之间的四层结构；(b) 箭头标出 In2Se3 两种面外极化方向；(c) 给出 AB1/AC1/AD1 等多种堆叠，P↓-AC1 为能量最低构型，界面处 Te1 与 Se 的相对位置决定轨道杂化强度 [[../papers/zhangNonvolatileControlTopological2025]]。
*   **来源**：[[../papers/zhangNonvolatileControlTopological2025]] -> [[../figures/heterostructures-stacking-multiferroic|多铁异质结]]

## ⚡ 铁电极化调控磁相互作用

翻转 In2Se3 极化（P↑→P↓）改变界面电荷转移与轨道杂化，从而协同调控三个磁学参数：交换作用 $J$ 由 11.69 降至 9.85 meV，DMI 系数 $d_\parallel$ 由 1.87 升至 1.98 meV（增约 6%），MAE 的 $K$ 由 2.44 降至 1.96 meV/Cr（降约 20%）。这种"DMI 增强 + MAE 受抑"的组合正是斯格明子成核所需的能量条件。

![图：原子与轨道分辨的磁性相互作用——(a)各原子对 MAE 贡献，(b,c)/(e,f)Te 原子 p 轨道分辨 MAE，(d)原子层分辨的 DMI 相关 SOC 能量](../../raw/figures/zhangNonvolatileControlTopological2025/fig_2_Q7TYSSIJ.png)
*   **关键特征**：Te 原子是 MAE 的主要贡献者，Te2 主导 DMI；极化翻转为 P↓ 时 Te1 对 DMI 的贡献由负转正，直接增大总 DMI——能量单位为 meV，从电子轨道层面解释了"电方向如何扭动磁漩涡" [[../papers/zhangNonvolatileControlTopological2025]]。
*   **来源**：[[../papers/zhangNonvolatileControlTopological2025]] -> [[../figures/heterostructures-stacking-spintronics-strain|自旋电子学与应变工程]]

## 🌀 拓扑自旋织构及其相图

在低场（约 50 mT）下，P↑ 态为均匀铁磁态，翻到 P↓ 态则自发形成斯格明子晶格（SkX），实现非易失的电控"写入/擦除"。P↓ 态斯格明子在 200 K 仍稳定，密度在 4.4 T、200 K 下高于 628 μm⁻²；调节 $K$ 与 $d_\parallel$ 还能在斯格明子与双半子（bimeron）之间相变。

![图：拓扑磁结构的静态相图——(a)P↑/P↓ 在不同场下的自旋织构，(b)拓扑电荷 Q 随磁场，(c)温度-磁场相图及自旋快照，(d)斯格明子半径随磁场变化](../../raw/figures/zhangNonvolatileControlTopological2025/fig_3_Z9FGHBYU.png)
*   **关键特征**：(a) 直观呈现极化翻转导致的铁磁↔斯格明子晶格切换；(c) 中磁场单位为 T、温度单位为 K，斯格明子晶格在 200 K 仍存活；(d) 中半径 Rx 单位为 nm，随磁场增大而收缩，给出尺寸调控手段 [[../papers/zhangNonvolatileControlTopological2025]]。
*   **来源**：[[../papers/zhangNonvolatileControlTopological2025]] -> [[../figures/heterostructures-stacking-spintronics-strain|自旋电子学与应变工程]]

![图：基于 DMI(d||) 与 MAE(K) 的全局拓扑相图（a）及无量纲判据 κ 的一维相图（b）](../../raw/figures/zhangNonvolatileControlTopological2025/fig_5_SCSIXLYM.png)
*   **关键特征**：作者提出无量纲稳定性判据 $\kappa=\frac{\pi^2}{4}\frac{2JK}{3d_\parallel^2}$，当 $5<|\kappa|<10$ 时体系稳定承载孤立斯格明子或双半子，为实验筛选材料与调界面提供了明确路标 [[../papers/zhangNonvolatileControlTopological2025]]。
*   **来源**：[[../papers/zhangNonvolatileControlTopological2025]] -> [[../figures/mathematical-models|数学模型与物理公式]]

## 💾 电流驱动与赛道存储

微磁学模拟比较了斯格明子与双半子在自旋转移力矩下的运动：相同驱动下双半子的霍尔角约 2.44°，远小于斯格明子的 11.68°（减小约 80%），横向漂移被显著抑制，降低了赛道存储中因撞边而湮灭的概率，轨迹控制更精准；斯格明子较大的横向运动则可用于逻辑器件的定向分流。

![图：斯格明子(a)与双半子(b)在 0/3/6 ns 的电流驱动快照，及纵向(c)/横向(d)速度随自旋转移力矩 u 的变化](../../raw/figures/zhangNonvolatileControlTopological2025/fig_6_ZU3NDFU8.png)
*   **关键特征**：速度单位为 m/s、u 单位为 μeV；两类拓扑准粒子的纵向速度相近，但双半子横向速度被各向异性耗散张量压低，对应更小的拓扑霍尔角，这是其应用优势的来源 [[../papers/zhangNonvolatileControlTopological2025]]。
*   **来源**：[[../papers/zhangNonvolatileControlTopological2025]] -> [[../figures/electronic-devices|电子与突触器件]]

## 📊 主要物性参数

| 参数 | P↑ 态 | P↓ 态 | 备注 |
| :--- | :--- | :--- | :--- |
| 交换作用 $J$ | 11.69 meV | 9.85 meV | 极化翻转减小 |
| DMI $d_\parallel$ | 1.87 meV | 1.98 meV | 增强 ~6% |
| MAE $K$ | 2.44 meV/Cr | 1.96 meV/Cr | 抑制 ~20% |
| 拓扑态 | 铁磁（FM） | 斯格明子晶格 | 50 mT 即可切换 |
| 斯格明子稳定性 | — | ≤ 200 K | 4.4 T 下密度 >628 μm⁻² |
| 霍尔角（斯格明子/双半子） | 11.68° | 2.44° | 双半子低 ~80% |
| 晶格失配 | CrInTe2/In2Se3 ~0.7% | | 界面 DMI 来源 |

## 📚 相关论文 (Related Papers)

- [[../papers/zhangNonvolatileControlTopological2025]]：Materials Today Chemistry 2025，第一性原理 + 微磁学模拟提出 CrInTe2/In2Se3 异质结的非易失电控拓扑磁性，给出 κ 判据与斯格明子/双半子动力学。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/magnetoelectric-coupling|磁电耦合]]、[[../concepts/dzyaloshinskii-moriya-interaction|Dzyaloshinskii–Moriya 相互作用]]、[[../concepts/skyrmion|斯格明子]]、[[../concepts/bimeron|双半子]]、[[../concepts/magnetic-anisotropy-energy|磁各向异性能]]、[[../concepts/exchange-interaction|交换相互作用]]、[[../concepts/spin-texture|自旋织构]]、[[../concepts/spin-orbit-coupling|自旋轨道耦合]]、[[../concepts/multiferroicity|多铁性]]
- [[../entities/In2Se3|In2Se3]]（铁电调控层）、[[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]、[[../entities/CrI3|CrI3]]（二维磁体对照）
