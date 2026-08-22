---
tags: [entity, rare-earth-doping, sliding-ferroelectricity, two-photon-excitation, lateral-integration, interlayer-charge-transfer, polarization-switching]
title: GaN
type: entity
status: developing
year: 2002
papers: [wuSlidingFerroelectricity2D2021a, kaurRecentAdvancesTheoretical2025a, Khitrov2002internal]
updated: 2026-08-21
---

# GaN

氮化镓（GaN）在本库中以两个互不相干的身份出现，必须分开看：一是**稀土掺杂发光母体**，作为宽禁带半导体承载稀土离子的 f–f 跃迁，用于电致发光器件；二是**石墨型少层 GaN**，作为蜂窝格子二元化合物，在双层错堆叠下表现出滑移铁电性。两者的文献、时间跨度（2002 vs 2021–2025）和物理机制都无重叠，本页不把它们合并叙述。

## 👵 太奶导读

乖孙，氮化镓这东西在这个库里被当成两种完全不同的材料在用。

一种用法是把它当"灯罩"：它带隙宽、透光，往里掺不同的稀土离子（铕发红、铽发绿），离子被电流激发后各发各的颜色。以前的做法是把不同掺杂层上下叠起来，可上下层要用不同电压才亮，电路很麻烦；2002 年有人改成把不同掺杂区**并排铺在同一个平面上**，同一个电压就能各自发光，电路一下就简单了。

另一种用法完全是近几年的事：把 GaN 剥成两层石墨那样的蜂窝薄片，上下两层稍微错开一点堆叠，层与层之间就会挪一点电子过去，整个薄片自己就带上了上下方向的电偶极——这就是滑移铁电性。它的计算极化是 9.72 pC/m，比同样机制的氮化硼双层（2.08 pC/m）高将近五倍。注意这是**理论计算值**，不是量出来的。

## 🧩 核心内容与机制 (Core Content)

### 身份一：石墨型少层 GaN —— 滑移铁电候选材料

wu2021a 把滑移铁电性的适用范围从 h-BN 推广到"大多数蜂窝格子二元化合物"，并明确点出石墨型少层 GaN **已被实验合成**，因此不是纯假想体系。其机制与 h-BN 同源：AB 错堆叠破坏中心对称，层间发生微小电荷转移，产生垂直方向自发极化；极化方向可由层间滑移翻转。

计算的 AB 堆叠双层垂直极化（同一套计算，可横向比较）：

| 体系 | 极化 (pC/m) |
| --- | --- |
| BN | 2.08 |
| ZnO | 8.22 |
| AlN | 10.29 |
| **GaN** | **9.72** |
| [[../entities/SiC\|SiC]] | 6.17 |
| MoS₂ | 0.97 |
| InSe | 0.24 |

GaN 位于该表的高极化一端，仅次于 AlN。kaur2025a 复述并归纳了同一结论："AlN、ZnO、SiC 和 GaN 双层体系显示出高达五倍的自发垂直极化"（相对 h-BN），并把 GaN 与 [[black-phosphorus\|black-phosphorus]]、GeC 并列为 AC 堆叠构型的代表体系。kaur2025a 同时指出，在这组 III–V / IV 族化合物中，**GeC 的 AC 堆叠是全局能量最低态，实验可行性更高**——也就是说 GaN 虽然极化大，但在"哪个更容易做出来"这一维度上并非首选。

### 身份二：稀土掺杂 GaN —— 横向颜色集成的发光母体

Khitrov2002internal 记述的工作：在 GaN 母体中分区掺入不同稀土离子，实现红、绿电致发光单元的**横向集成**。关键动机是电路简化——传统垂直集成把不同掺杂层上下堆叠，各层需施加不同偏压才能分别发光；横向集成把不同掺杂区并排做在同一平面，各区在相同驱动条件下独立发光。原文报告实现了红、绿 ELD 的横向集成并在相同偏压下获得代表性颜色。

发光机制：不同稀土离子具有各自特征的 f–f 跃迁能级，在 GaN 母体中受载流子激发后发出特定波长的光。GaN 在此仅充当宽禁带主体，本身不是发光中心。

## ⚠️ 使用本页时的边界

- **两个身份不可混用**。滑移铁电性讨论的是石墨型（蜂窝、二维）GaN；稀土掺杂器件用的是常规三维 GaN 外延层。把 9.72 pC/m 挪到发光器件语境里是错的。
- **9.72 pC/m 是 DFT 计算值**，wu2021a 的表 1 通篇为"Computed vertical polarizations"。本库中未见石墨型 GaN 铁电性的实验测量。
- **Khitrov2002internal 不是一篇研究论文**，而是 2002 年 4 月《MRS Bulletin》"RESEARCH/RESEARCHERS"栏目的一组研究快讯（内含 Si/SiGe 超晶格纳米线、纳米纤维悬浮、双光子缺陷成像、GaN 横向集成四则彼此独立的短讯）。引用它时只能引 GaN 那一则，且它本身是二手报道，原始工作为 Lee 和 Steckl 所做——本库无该原始论文。
- 原文并未给出横向集成器件的发光效率、亮度或稀土离子浓度，故本页不列参数表。

## 📚 相关论文 (Related Papers)

- [[../papers/wuSlidingFerroelectricity2D2021a]]：给出 AB 堆叠双层的统一计算极化表，将石墨型少层 GaN（9.72 pC/m）列为已合成且极化远高于 h-BN 的滑移铁电候选体系。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：归纳 AlN/ZnO/SiC/GaN 一族双层的垂直极化可达 h-BN 的五倍，同时指出同族中 GeC 的 AC 堆叠为全局能量最低态、实验可行性更高，为 GaN 的候选地位划出边界。
- [[../papers/Khitrov2002internal]]：作为 2002 年研究快讯记述了稀土掺杂 GaN 的红、绿电致发光单元横向集成方案，其价值在于以同平面分区替代垂直堆叠，使各发光区可在相同偏压下驱动。

## 🔗 关联概念与实体 (Related)

- [[../concepts/sliding-ferroelectricity|sliding-ferroelectricity]]
- [[../concepts/interlayer-stacking|interlayer-stacking]]
- [[../concepts/interlayer-charge-transfer|interlayer-charge-transfer]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/rare-earth-doping|rare-earth-doping]]
- [[../concepts/lateral-integration|lateral-integration]]
- [[../entities/SiC|SiC]]
- [[../entities/black-phosphorus|black-phosphorus]]
