---
tags: [entity, material, 2D, semiconductor, sliding-ferroelectricity]
title: 硒化铟 (InSe)
type: entity
status: developing
category: [D01]
formula: InSe
stoichiometry: γ
class: [III-VI, layered-semiconductor, vdW]
properties: [sliding-ferroelectricity, layered-semiconductor]
related_concepts: [sliding-ferroelectricity, interlayer-charge-transfer, interlayer-stacking, broken-inversion-symmetry]
related_entities: [GaSe]
papers: [sunSlidingFerroelectricityTwodimensional2025, wuSlidingFerroelectricity2D2021a, zhangEmergingFrontiersTwodimensional2025]
updated: 2026-08
---

# 硒化铟 (InSe)

InSe（硒化铟）是 III-VI 族层状半导体，层内强共价键、层间弱范德华力。其 γ 相具有非中心对称堆垛构型，层间滑移可导致电荷重分布并产生垂直极化，是滑动铁电性的候选材料体系之一 [[../papers/wuSlidingFerroelectricity2D2021a]]。

## 👵 太奶导读

太奶，InSe（硒化铟，铟和硒组成的层状材料）就像一叠**薄薄的煎饼**：每张饼自己很结实（层内原子手拉手，是牢固的共价键），饼与饼之间却只是虚虚地贴着（这叫范德华力，层与层之间那点微弱的吸力）。

它的 γ 相（一种特定的叠放顺序）有个讲究：上下两张饼不是正正地对齐，而是天生带着点偏。您把上面那张饼往旁边一搓，饼与饼之间的电子就会往一边挪窝（这叫**层间电荷转移**），于是整叠饼上下就有了正负之分——上面带正电、下面带负电，这就是**电极化**。往反方向搓回来，正负还能对调，这就叫**滑动铁电性**。

它比老式铁电材料强在哪儿？老式的靠原子在小格子里上下挪位置来产生电性，做薄了就不灵了（有"最小厚度"的坎儿）；而 InSe 天生就是薄薄几层，靠"搓"就行，正好用来做又薄又省电的记忆芯片。

## 🏗️ 结构概览

InSe 的单层为 Se-In-In-Se 四原子层夹心结构，两个 In 原子居中成键、上下各覆一层 Se。层间为范德华间隙，可机械剥离至单层并人工重新堆叠。γ 相的层间配准方式打破中心反演对称性，是其可能承载面外极化的结构前提；不同多型（β / ε / γ）的对称性差异直接决定是否允许滑动铁电。

## 🧩 物理实质与滑动铁电机制

滑动铁电性源于非中心对称堆垛构型下的层间电荷转移，通过层间滑移而非传统离子位移实现极化翻转，为解决传统铁电体在纳米尺度的临界尺寸效应提供新方案 [[../papers/zhangEmergingFrontiersTwodimensional2025]]。极化大小由层间电荷重分布的幅度决定，通常在每层 ~pC/m 量级，方向沿垂直于层面的方向。

## 🔬 实验表征与器件应用

滑动铁电材料可通过 CVD、机械剥离与人工堆叠、MBE 制备，用 PFM、KPFM、SHG、PUND 电学测量、STEM 表征；器件应用包括铁电隧道结、铁电晶体管与光电器件 [[../papers/sunSlidingFerroelectricityTwodimensional2025]]。

## 📚 相关论文 (Related Papers)

- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：综述了二维材料中的滑动铁电性及其器件应用。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：综述了二维范德华材料中滑动铁电性的相关物理与未来机遇。
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]：综述了二维滑动铁电体的新兴前沿。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]：本条目的核心物性。
- [[../concepts/interlayer-charge-transfer|层间电荷转移]]：极化的微观来源。
- [[../concepts/interlayer-stacking|层间堆垛]]
- [[../concepts/broken-inversion-symmetry|中心反演对称性破缺]]
- [[../concepts/ferroelectric-tunnel-junction|铁电隧道结]]：主要器件出口。
- [[../entities/GaSe|GaSe]]：同为 III-VI 族层状半导体的姊妹体系。
