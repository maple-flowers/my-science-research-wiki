---
tags: [concept, multiferroicity, sliding-ferroelectricity, magnetoelectric-coupling, berry-phase, spin-orbit-coupling, supersuperexchange, d-orbital]
title: d轨道跃迁 / d-orbital Hopping
type: concept
status: mature
domain: [multiferroicity, magnetism, 2d-materials]
mechanism: 层间滑移改变 Gd–I–I–Gd 超超交换路径中 d_z² 与 d_xy/d_x²-y² 轨道杂化的竞争，同时决定磁性、铁电性与谷极化
related_concepts: [supersuperexchange, sliding-ferroelectricity, stacking-engineering, ferrovalley, valley-polarization, multiferroicity, magnetic-phase-transition, ferroelasticity]
papers: [xunCoexistingMagnetismFerroelectric2024]
updated: 2026-08
---

# d轨道跃迁 / d-orbital Hopping

d 轨道跃迁（d-orbital Hopping）指磁交换作用的微观载体——磁性离子的 d 轨道之间的跃迁/杂化路径。在双层 GdI₂ 中，层间滑移通过改变 Gd–I–I–Gd 超超交换路径上 **d_z² 轨道**与 **d_xy/d_x²-y² 轨道**的杂化竞争，同时切换磁性（反铁磁↔铁磁）、铁电性与谷极化，从而将"堆垛工程"与"轨道物理"联系起来（[[../papers/xunCoexistingMagnetismFerroelectric2024]]）。

## 👵 太奶导读

乖孙，这一条讲的是「d 轨道跃迁」——磁性是咋来的那点"通道"学问。太奶给您打比方：Gd（钆）原子手里有几条"路"（d_z²、d_xy、d_x²-y² 这些轨道），电子顺着"路"跳到邻居家，就产生了磁性。双层 GdI₂ 里两层布一错位（滑移），电子走的"路"就变了：原先走"直路"（d_z²-d_z²）是反铁磁，错位后改走"弯道"（d_z²-d_xy）就成了铁磁，同时还把铁电和谷极化一起带出来了。一句话：**轨道"走哪条路"决定了磁性、铁电和谷极化，滑一滑就能全切换**。

## 🧩 什么是 d 轨道跃迁？

- **定义**：磁交换（特别是超超交换）由磁性离子 d 轨道之间的跃迁积分（hopping integral）主导。轨道对称性匹配与否，直接决定交换是铁磁还是反铁磁。
- **Goodenough–Kanamori 视角**：两条正交轨道（如 d_z² 与 d_xy）之间的跃迁给出铁磁耦合；同对称性轨道（d_z²-d_z²）的强跃迁给出反铁磁耦合。双层 GdI₂ 正是利用层间滑移在这两种路径间切换。
- **与超超交换的联系**：Gd–I–I–Gd 路径中，磁交换通过两段 I-5p 介导，d-p 杂化的轨道选择性（角动量选择）决定最终交换符号与强度。

![图：双层GdI₂堆垛结构与轨道交换路径示意](../../raw/figures/xunCoexistingMagnetismFerroelectric2024/fig_1_UNCVPF48.png)
- **关键特征**：AA 与 AB/BA 堆垛的结构对照，标出 Gd–I–I–Gd 超超交换路径。
- **来源**：[[../papers/xunCoexistingMagnetismFerroelectric2024]] -> [[../figures/crystal-structures-electronic-bands|晶体结构与能带]]

## ⚡ 核心机制：轨道杂化竞争随滑移切换

1. **AA 堆垛（反铁磁）**：层间 Gd 位对齐，d_z²-d_z² 轨道之间形成强反铁磁超超交换（J₁⊥=0.243 meV，AFM），无净极化、无谷劈裂。
2. **AB/BA 堆垛（铁磁 + 铁电 + 铁谷）**：滑移半晶格后，Gd 位错开，d_z² 与 d_xy/d_x²-y² 正交轨道耦合（J₁⊥=−0.036 meV，FM），反铁磁超超交换被抑制，铁磁胜出；同时滑移本身产生方向相反的垂直极化 P（AB 与 BA 反向），并伴随谷极化（铁谷序）。
3. **三序强耦合**：轨道路径与结构对称性耦合，使磁性、铁电性、谷极化三者随堆垛"共进退"——这是"滑移多铁"（sliding multiferroicity）的核心，也是磁性-铁电-铁谷耦合的通用设计范式。

![图：堆垛依赖的磁性相变与轨道杂化机制](../../raw/figures/xunCoexistingMagnetismFerroelectric2024/fig_2_AGA9PAPG.png)
- **关键特征**：不同堆垛的交换能、磁构型对比，显示 AA→AB 由 AFM 转 FM。
- **来源**：[[../papers/xunCoexistingMagnetismFerroelectric2024]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

## 🔄 铁电-铁谷共现与可逆翻转

- **铁电极化**：AB/BA 堆垛产生面外极化，AB 与 BA 方向相反，可通过层间滑移/电场可逆翻转。
- **谷极化**：滑移打破谷简并，价带顶谷劈裂显著（ΔV 约 22.86 meV 量级），可通过堆垛方向翻转谷极化符号。
- **铁磁切换**：FM 态的磁化与铁电极化、谷极化方向锁存，实现"滑移三态"电控切换。

![图：铁电、谷极化与磁性的滑移可逆切换](../../raw/figures/xunCoexistingMagnetismFerroelectric2024/fig_3_XJ7U4H33.png)
- **关键特征**：AB↔BA 滑移路径上极化与谷劈裂的翻转图像。
- **来源**：[[../papers/xunCoexistingMagnetismFerroelectric2024]] -> [[../figures/crystal-structures-xrd-phases|结构与相]]

![图：堆垛依赖能量与交换竞争定量结果](../../raw/figures/xunCoexistingMagnetismFerroelectric2024/fig_4_5PV9HUPZ.png)
- **关键特征**：各堆垛相对能量、J₁⊥ 数值与磁基态对比，定量支撑"d 轨道杂化竞争"结论。
- **来源**：[[../papers/xunCoexistingMagnetismFerroelectric2024]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

![图：滑移多铁器件化与谷电子应用示意](../../raw/figures/xunCoexistingMagnetismFerroelectric2024/fig_5_GWY2W8FP.png)
- **关键特征**：展示滑移驱动的多铁态在自旋/谷电子器件中的开关应用。
- **来源**：[[../papers/xunCoexistingMagnetismFerroelectric2024]] -> [[../figures/crystal-structures-electronic-bands|晶体结构与能带]]

## 🔬 物理参数表

| 属性 | 数值（AA / AB-BA） | 说明 |
| :--- | :--- | :--- |
| 层间交换 J₁⊥ | 0.243 meV（AFM）/ −0.036 meV（FM） | 轨道杂化竞争切换 |
| 磁基态 | 反铁磁 / 铁磁 | 滑移驱动相变 |
| 垂直极化 | 0 / P（AB 与 BA 反向） | 滑移铁电 |
| 谷劈裂 | 0 / ΔV≈22.86 meV | 铁谷序 |
| 交换路径 | Gd–I–I–Gd 超超交换 | d_z² vs d_xy/d_x²-y² 竞争 |

> 注：上表为 DFT 典型数值，来源见 [[../papers/xunCoexistingMagnetismFerroelectric2024]] 及其参数表。

## 🧭 近邻概念辨析

- **与 [[../concepts/supersuperexchange|超超交换]]**：d 轨道跃迁是超超交换的微观通道；本条目侧重"轨道对称性竞争"如何被堆垛工程操纵。
- **与 [[../concepts/sliding-ferroelectricity|滑动铁电]]**：滑动铁电描述几何滑移产生极化；d 轨道跃迁给出为何滑移同时翻转磁性（轨道交换路径改变）。
- **与 [[../concepts/ferrovalley|铁谷序]]/[[../concepts/valley-polarization|谷极化]]**：谷极化随滑移方向翻转，与铁电极化、磁化耦合，构成三序一体。
- **与 [[../concepts/stacking-engineering|堆垛工程]]**：堆垛是手段，d 轨道跃迁竞争是机制，二者构成"结构-机制"闭环。

## 📚 相关论文 (Related Papers)

- [[../papers/xunCoexistingMagnetismFerroelectric2024]]：提出层间滑移在双层 GdI₂ 中同时实现并耦合磁性、铁电性与谷极化的通用机制，并从 d 轨道杂化竞争角度给出微观解释。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/multiferroicity|multiferroicity]]
- [[../concepts/sliding-ferroelectricity|sliding-ferroelectricity]]
- [[../concepts/magnetoelectric-coupling|magnetoelectric-coupling]]
- [[../concepts/berry-phase|berry-phase]]
- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/ferroelasticity|ferroelasticity]]
- [[../concepts/ferrovalley|ferrovalley]]
- [[../concepts/valley-polarization|valley-polarization]]
- [[../concepts/supersuperexchange|supersuperexchange]]
- [[../concepts/stacking-engineering|stacking-engineering]]
- [[../concepts/magnetic-phase-transition|magnetic-phase-transition]]
- [[../entities/VASP|VASP]]
- [[../entities/TMDs|TMDs]]
- [[../entities/h-BN|h-BN]]
- [[../entities/GdI2|GdI2]]
