---
tags: [entity, material, 2D, semiconductor, sliding-ferroelectricity]
title: 硒化镓 (GaSe)
type: entity
status: developing
category: [D01]
formula: GaSe
class: [III-VI, layered-semiconductor, vdW]
properties: [sliding-ferroelectricity, layered-semiconductor]
related_concepts: [sliding-ferroelectricity, interlayer-stacking, interlayer-translation, broken-inversion-symmetry]
related_entities: [InSe]
papers: [sunSlidingFerroelectricityTwodimensional2025, wuSlidingFerroelectricity2D2021a]
updated: 2026-08
---

# 硒化镓 (GaSe)

GaSe（硒化镓）是 III-VI 族层状半导体，单层由共价键合的 Se-Ga-Ga-Se 四原子层构成，层间以弱范德华力（van der Waals force，靠分子间微弱吸引堆在一起的力）堆叠。在非中心对称的堆垛构型下，层间相对滑移可打破中心对称性并产生面外电极化，因此 GaSe 是滑动铁电性（sliding ferroelectricity）的候选材料体系。

## 👵 太奶导读

太奶，您想象一叠**刚出锅的春饼**：每张饼本身结实（层内是牢固的共价键，原子之间手拉手拉得死紧），可饼跟饼之间只是轻轻贴着，一推就能错开（这叫范德华力，就是层与层之间那点微弱的吸力）。

GaSe（硒化镓，一种镓和硒组成的层状半导体）就是这种"春饼"。它妙的地方在于：本来上下两张饼的花纹是对称的，谁也不偏；可您把上面那张往旁边一搓，花纹就错位了，整叠饼上下两面立刻有了"高低之分"——上面带正电、下面带负电，这就叫**电极化**（材料内部正负电荷分开、有了方向性）。往回搓一下，正负还能对调。

这种靠"搓一下"而不是靠原子上下挪位置来产生和翻转电性的现象，就叫**滑动铁电性**。它金贵在哪儿？传统铁电材料做得太薄就失效了（有个"临界厚度"的坎儿），而滑动铁电天生就是薄薄几层，正好能做成最省电的记忆芯片。

## 🏗️ 结构概览

GaSe 的单层为 Se-Ga-Ga-Se 四原子层夹心结构：两个 Ga 原子在中间形成 Ga-Ga 共价键，上下各覆一层 Se。层内为强共价键，层间为弱范德华相互作用，因此易于机械剥离并可人工堆叠成任意扭转角/堆垛序的多层结构。不同堆垛多型（ε / β / γ 相）对应不同的层间配准方式，其中非中心对称多型是滑动铁电的必要前提。

## 🧩 物理实质：滑动铁电性

在非中心对称堆叠的层状材料中，层间相对滑移可打破中心对称性并产生面外电极化，且极化方向可通过滑移方向翻转，构成滑动铁电性（sliding ferroelectricity）的微观机制 [[../papers/wuSlidingFerroelectricity2D2021a]]。与传统位移型铁电体依赖离子在单胞内的相对位移不同，滑动铁电的极化来源是层间电荷重分布，因此不受传统铁电体临界尺寸效应的限制。

## 🔬 实验表征与器件应用

滑动铁电性已在多种二维范德华材料中被证实，其极化翻转与层间滑移耦合，可用于非易失存储、神经形态计算等器件应用 [[../papers/sunSlidingFerroelectricityTwodimensional2025]]。常用表征手段包括压电力显微镜 (PFM)、二次谐波产生 (SHG) 与 PUND 电学测量。

## 📚 相关论文 (Related Papers)

- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：综述了二维材料中的滑动铁电性及其器件应用。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：综述了二维范德华材料中滑动铁电性的相关物理与未来机遇。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]：本条目的核心物性。
- [[../concepts/interlayer-stacking|层间堆垛]]
- [[../concepts/interlayer-translation|层间平移]]
- [[../concepts/broken-inversion-symmetry|中心反演对称性破缺]]：产生极化的对称性前提。
- [[../entities/InSe|InSe]]：同为 III-VI 族层状半导体的姊妹体系。
