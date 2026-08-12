---
tags: [concept, magnetoelectric, coupling, multiferroics, 2D-materials, mechanism]
category: [D02]
title: 磁电耦合 / Magnetoelectric Coupling
type: concept
status: mature
domain: multiferroics
mechanism: 电极化 P 与磁化 M 之间的交叉调控——磁场改极化（正磁电效应）、电场改磁化（逆磁电效应）
related_concepts: [type-i-multiferroics, type-ii-multiferroics, multiferroicity, sliding-ferroelectricity, spin-spiral, electromagnon, inverse-dzyaloshinskii-moriya, lone-pair-ferroelectricity]
aliases: ["ME coupling", "磁电效应", "Magnetoelectric Effect", "Magnetoelectric Coupling"]
key_quantities:
  definition: "正效应 ΔP=α·H（磁场诱电极化）；逆效应 ΔM=α·E（电场诱磁化）；α 为磁电系数"
  type_i: "磁、电独立起源，耦合弱（多经应变/界面次级传递），但极化大、Tc 高（BiFeO3）"
  type_ii: "磁序破缺反演对称生极，本征强耦合但极化小、温度低（TbMnO3、NiI2）"
  interface_2d: "层间电荷转移/滑动铁电/应变可在异质结中实现室温电写磁读（双层 CrTe2、CrInTe2/In2Se3）"
papers: [spaldinRenaissanceMagnetoelectricMultiferroics2005, fiebigEvolutionMultiferroics2016, rameshMultiferroicsProgressProspects2007, tianRoomtemperatureTwodimensionalMultiferroic2026, chenStrongSlidingFerroelectricity2024, zhongHighthroughputExfoliationMultiferroic2025, RecentAdvancesGrowth2025]
updated: 2026-08
---

# 磁电耦合 / Magnetoelectric Coupling

**磁电耦合（Magnetoelectric Coupling, ME Coupling）** 指材料中电极化（$P$）与磁化（$M$）之间的交叉调控：磁场改变电极化（正磁电效应 $\Delta P=\alpha H$），电场改变磁化（逆磁电效应 $\Delta M=\alpha E$），$\alpha$ 为磁电系数。它是 [[multiferroicity|多铁性]] 最核心的应用价值所在——用"电压写、磁读取"取代电流写磁，能大幅压低自旋存储的焦耳热 [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]] [[../papers/fiebigEvolutionMultiferroics2016]]。

## 👵 太奶导读

太奶，这两个本事——电和磁——在普通材料里各管各的。可有的特殊材料能让它俩"牵上手"：这边给个磁场，那边就生出电的方向；反过来给个电场，磁的方向也跟着变。这就叫**磁电耦合**。它金贵在哪儿呢？我们平时往硬盘里写东西，得靠电流转圈生磁去拨小磁针，费电、发热；有了磁电耦合，直接加个电压就能"写磁"，又凉快又省电，这就是科学家念叨的"电写磁读"。

它俩能牵上手，得有个前提：这块材料既得破"时间反演"（有磁），又得破"空间反演"（有电），两样对称都打破，磁和电才有合法的"接头暗号"。按照牵手方式不同，分好几家：第一类是一院里两户人家，电、磁各有来历，牵得不太紧（耦合弱），但电的劲儿大、耐温高；第二类是磁直接把电逼出来，磁是因电是果，牵得死紧（耦合强），可惜电劲儿小、怕冷。后来二维薄片兴起，又添了新花样：两层之间电子来回搬家（电荷转移）、或是两层轻轻一搓（滑移），都能在常温下把磁和电拴在一起；还可以拿一片压电材料去"顶"磁片，用形变传话。科学家正想拿它造又凉又密的存储器。

## 🏗️ 结构概览：对称前提

本征磁电耦合要求体系同时破缺时间反演对称（有磁序）与空间反演对称（有电极化）。单一铁性序只破缺其中之一，因此必须由多铁相或特殊异质结把两种对称破缺凑齐，磁电张量 $\alpha$ 才不为零。

![图：铁性序与空间/时间反演对称的关系——多铁相同时落在两类对称破缺的交集，是磁电耦合的对称前提](../../raw/figures/RecentAdvancesGrowth2025/fig_1_7IQ7CDIJ.png)
*   **看图要点**：铁电破空间反演、铁磁破时间反演；二者交集（多铁）才允许 P 与 M 线性耦合，这正是磁电效应的对称学起源 [[../papers/RecentAdvancesGrowth2025]]。
*   **来源**：[[../papers/RecentAdvancesGrowth2025]] -> [[../figures/crystal-structures|晶体结构与对称性]]

## 🧩 本征单相耦合：第一类 vs 第二类

- **[[type-i-multiferroics|第一类多铁]]**：铁电与磁来自不同子系统（如 BiFeO3 中 Bi³⁺ 的 6s² 孤对电子驱动铁电、Fe 3d 驱动磁性），二者无直接对称关联，故磁电耦合较弱；但极化大、转变温度高 [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]。
- **[[type-ii-multiferroics|第二类多铁]]**：铁电极化直接由磁结构（螺旋/摆线自旋序经 [[inverse-dzyaloshinskii-moriya|逆 DM]]/自旋电流机制）破缺反演对称而诱导，极化是磁序的派生量，故本征耦合极强；但极化小、磁转变温度往往很低（如 TbMnO3、NiI2）[[../papers/fiebigEvolutionMultiferroics2016]]。

![图：非共线/非共面自旋排布打破反演对称、沿 eij×(Si×Sj) 方向诱导电极化的第二类多铁几何](../../raw/figures/huProgressProspectsLowdimensional2019/fig_7_ACL4KQI9.png)
*   **关键特征**：自旋手性决定极化方向，翻磁即翻电——这是第二类多铁"本征强耦合"的几何来源 [[../papers/huProgressProspectsLowdimensional2019]]。
*   **来源**：[[../papers/huProgressProspectsLowdimensional2019]] -> [[../figures/crystal-structures|晶体结构]]

## 🔌 层间电荷转移：二维多铁金属

在范德华双层中，铁磁层与反铁磁层因静电势差发生自发层间电荷转移，非对称电荷分布既破缺反演对称诱导面外极化，又通过电子填充调控磁序。这是不依赖强自旋轨道耦合的新机制，且在导电体系中实现了极化（多铁金属）。

![图：双层 CrTe2 的"电写磁读"——PFM 写入的电畴与 MFM 在同区域读出的磁畴一一对应](../../raw/figures/tianRoomtemperatureTwodimensionalMultiferroic2026/fig_3_85N9YJPF.png)
*   **关键特征**：室温大气环境下，电场写入的电极化图样被磁成像原样读出，直接证明层间电荷转移把 P 与 M 锁在一起，实现非易失磁电互控 [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]。
*   **来源**：[[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]] -> [[../figures/electronic-devices|电子器件与表征]]

## 🪣 层间滑移与莫尔铁电调控磁性

层间相对滑移（或转角莫尔超晶格）改变堆叠对称性、诱导面外偶极，进而调控邻近磁性层的各向异性、DMI 与拓扑磁结构。这一机制翻转势垒超低，适合低功耗调控（见 [[sliding-ferroelectricity|滑动铁电性]]）。

![图：层间横向滑移打破中心对称、诱导面外偶极子（红色箭头）的滑动铁电机制示意](../../raw/figures/chenStrongSlidingFerroelectricity2024/fig_1_I9JJ25R3.png)
*   **关键特征**：以 HgI2/HgBr2 等为代表，滑移改变层间对齐即产生可翻转偶极；把磁性层与滑移铁电层堆叠，即可用滑移极化"旋钮"调控磁性 [[../papers/chenStrongSlidingFerroelectricity2024]]。
*   **来源**：[[../papers/chenStrongSlidingFerroelectricity2024]] -> [[../figures/heterostructures-stacking-sliding|层间滑移]]

## 🌡️ 应变介导与相锁定

- **应变介导（复合材料路线）**：铁电相在电场下压电形变，经界面把应变传给铁磁相、经磁弹耦合改磁；室温磁电系数可比单相高 2–3 个数量级，是薄膜存储的主流路线 [[../papers/rameshMultiferroicsProgressProspects2007]]。二维版本如 CrInTe2/In2Se3、Cr2Ge2Te6/In2Se3 异质结，借极化翻转调应变与轨道杂化，进而调控 DMI/MAE 与斯格明子（见 [[../entities/CrInTe2|CrInTe2]]、[[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]）。
- **相锁定（2025 新范式）**：在二维非范德华氧化物单层（如 SrOsO3、SrIrO3）中，应变以极低能垒（约 9.1 meV/atom）驱动有序-有序相变（$P4mm\leftrightarrow P4bm$），直接改变轨道杂化，实现半导体↔半金属（近 100% 自旋极化）与 AFM/FM 的可逆切换 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。

![图：应变诱导相变与轨道相互作用演化——以扭转角 θ 与 pCOHP 强度为旋钮控制磁性与极化](../../raw/figures/zhongHighthroughputExfoliationMultiferroic2025/fig_4_ABKMCTN8.png)
*   **关键特征**：晶格相变把结构、电子态与磁序"锁"在一起，一个应变旋钮同时切换电导与磁序，是强耦合新范式 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。
*   **来源**：[[../papers/zhongHighthroughputExfoliationMultiferroic2025]] -> [[../figures/heterostructures-stacking-multiferroic|多铁异质结]]

## 📊 耦合机制对照

| 机制 | 耦合强度 | 温度/极化 | 典型体系 | 调控方式 |
| :--- | :--- | :--- | :--- | :--- |
| 第一类单相 | 弱（独立起源） | 高 Tc、大 P | BiFeO3 | 多需应变/界面 |
| 第二类单相 | 本征、强 | 低温、小 P | TbMnO3、NiI2 | 磁场翻磁即翻电 |
| 层间电荷转移 | 强（2D 金属） | 室温、面外 P | 双层 CrTe2 | 电场写磁、非易失 |
| 滑移/莫尔铁电 | 中-强、超低势垒 | 取决于体系 | HgI2、磁性/铁电堆叠 | 层间滑移/转角 |
| 应变介导 | 室温、系数大 | 复合材料路线 | PZT/CoFe2O4、CrInTe2/In2Se3 | 电场→应变→磁 |
| 相锁定 | 强（序参量绑定） | 取决于材料 | SrOsO3、SrIrO3 | 应变驱动相变 |

## 📚 相关论文 (Related Papers)

- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]：多铁复兴与 d0 约束，奠定第一/二类划分。
- [[../papers/fiebigEvolutionMultiferroics2016]]：多铁性十年演变与磁电耦合物理。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：薄膜/异质结多铁与应变介导耦合进展。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：双层 CrTe2 室温二维多铁金属与电写磁读。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：HgI2/HgBr2 强滑移铁电及其磁电调控潜力。
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：二维氧化物单层中应变相锁定的强磁电耦合。
- [[../papers/RecentAdvancesGrowth2025]]：二维多铁/铁电材料与器件应用路线图。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[multiferroicity|多铁性]]、[[type-i-multiferroics|第一类多铁]]、[[type-ii-multiferroics|第二类多铁]]、[[sliding-ferroelectricity|滑动铁电性]]、[[spin-spiral|螺旋自旋序]]、[[electromagnon|电磁子]]、[[inverse-dzyaloshinskii-moriya|逆 DM 相互作用]]、[[lone-pair-ferroelectricity|孤对电子铁电性]]
- [[../entities/BiFeO3|BiFeO3]]、[[../entities/CrTe2|CrTe2]]、[[../entities/In2Se3|In2Se3]]、[[../entities/CrInTe2|CrInTe2]]、[[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]、[[../entities/HgI2|HgI2]]
