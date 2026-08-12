---
tags: [concept, ferroics, phase-transition, domain-wall, 2D-materials, straintronics]
category: [D02]
---

# 铁弹性 / Ferroelasticity

**铁弹性** 是指材料在无外加应力的情况下存在多种能量等价且稳定的取向变体（Orientation Variants），并且可以通过施加机械应力在这些变体之间实现可逆切换的物理现象。在二维（2D）体系中，铁弹性为**应变电子学（Straintronics）**提供了理想平台，即利用晶格畸变调控材料的电子、磁性与拓扑物性。

## 1. 微观物理机制

### 1.1 Peierls 畸变与 1T'-TMDs
在第 VI 族过渡金属硫族化合物（TMDs）中，高对称性的 1T 相在能量上往往不稳定，倾向于发生 **Peierls 畸变**。这种畸变导致金属原子二聚化（Dimerization），形成长方形晶格的 **1T' 相**（如 $WTe_2$ 和 $MoTe_2$）。由于畸变可以沿三角晶格的三个等价方向发生，从而产生三种取向变体（O1, O2, O3）（[[../papers/liFerroelasticityDomainPhysics2016|Li & Li 2016]]）。

### 1.2 自发应变与 β'-In₂Se₃
在范德华材料 **$\beta'-In_2Se_3$** 中，铁弹性起源于与**反铁电位移**强耦合的自发应变（约 0.49%）。不同于 1T'-TMDs 的二聚化机制，$\beta'-In_2Se_3$ 的铁弹性表现为宏观的纳米条纹超结构（Nanostriped Superstructure），其畴界移动由极小的单轴拉伸应力（$\le 0.5\%$）驱动（[[../papers/xuTwodimensionalFerroelasticityVan2021|Xu 2021]]）。

## 2. 能量学与动力学

### 2.1 翻转能垒 (Switching Barrier)
不同变体之间的切换需要克服一定的能量势垒。在 $1T'-WTe_2$ 单层中，NEB 计算显示变体转换能垒 **$< 0.2\text{ eV/f.u.}$**，这保证了材料在室温下具有良好的机械可塑性与翻转活性（[[../papers/liFerroelasticityDomainPhysics2016|Li & Li 2016]]）。

### 2.2 屈服应变 (Yield Strain)
二维铁性材料通常表现出极高的机械强度。例如，$\beta'-In_2Se_3$ 在保持铁弹翻转特性的同时，其屈服应变可达 **$\approx 5.5\%$**，远高于传统三维陶瓷材料。

## 3. 畴物理 (Domain Physics)
铁弹畴是具有不同取向变体的区域，由**畴壁（Domain Walls, DWs）**分隔。在 2D 体系中，畴壁具有独特的对称性与功能化潜力：
- **W-walls**：受对称性严格限制的边界。
- **S-walls**：应变依赖的边界，其取向随局部应变场动态调整以最小化弹性能。
- **功能性**：畴壁处可能由于对称性进一步破缺而承载独特的电子态或拓扑相，成为二维纳米线器件的天然构建模块（[[../papers/liFerroelasticityDomainPhysics2016|Li & Li 2016]]）。

## 4. 应变调控与多铁性耦合
通过铁弹性与磁性的耦合，可以设计高性能的二维多铁材料。
- **插层调控**：在 TMDs 双层中插入过渡金属原子形成的 **$AM_2X_4$** 体系中，铁弹/铁电翻转可以直接改变材料的磁基态（如 FM $\leftrightarrow$ AFM）或磁易轴方向，实现强磁电耦合（[[../papers/zhaoRealization2DMultiferroic2024|Zhao 2024]]）。

## 5. 关键图表

![1T'相的Peierls畸变与变体](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_2_KHBH8L57.png)
*图 1：1T'-MX₂ 单层中源自三角晶格的三个取向变体。摘自 [[../papers/liFerroelasticityDomainPhysics2016]]*

![In2Se3中的条纹畴结构](../../raw/figures/xuTwodimensionalFerroelasticityVan2021/fig_1_3385VJAN.png)
*图 2：β’-In2Se3 中的纳米条纹超结构与卫星衍射斑点。摘自 [[../papers/xuTwodimensionalFerroelasticityVan2021]]*

## 6. 相关概念
- [[straintronics|应变电子学 Straintronics]]
- [[2D-materials|二维范德华材料与低维铁性]]
- [[multiferroicity|多铁性 Multiferroicity]]
- [[../entities/WTe2|二碲化钨 WTe2]]
- [[../entities/In2Se3|硒化铟 In2Se3]]
