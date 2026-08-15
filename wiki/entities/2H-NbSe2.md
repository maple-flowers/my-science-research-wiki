---
tags: [entity, material, 2D, TMD, charge-density-wave, superconductor]
title: 二硒化铌 2H 相 (2H-NbSe₂)
type: entity
status: developing
category: [D01]
formula: NbSe2
stoichiometry: 2H
class: [TMD, vdW, metal, superconductor]
properties: [charge-density-wave, superconductivity, electron-phonon-coupling]
related_concepts: [charge-density-wave, superconductivity, electron-phonon-coupling, discommensuration, peierls-instability]
related_entities: [NbSe2, 1T-NbSe2, TiSe2]
papers: [Chen2019superconductivity, gorkovStrongElectronlatticeCoupling2012]
updated: 2026-08
---

# 二硒化铌 2H 相 (2H-NbSe₂)

2H-NbSe₂ 是过渡金属二硫族化物（transition metal dichalcogenide, TMD）家族的代表性层状材料，层内强共价键、层间弱范德华力。其 2H 相中电荷密度波（charge density wave, CDW）与超导电性（superconductivity, SC）共存且相互竞争，是研究电子-晶格耦合与量子有序态相互作用的经典体系。

## 👵 太奶导读

太奶，2H-NbSe₂（二硒化铌，铌和硒组成的层状金属，"2H"是它原子叠放的一种花样）身上同时住着两个"脾气相反的房客"。

第一个是**电荷密度波**（charge density wave，简称 CDW）：本来均匀撒开的电子，到了低温会自己排成**疏密相间的垄沟**，像地里的垄和沟一样一道一道的，同时原子也跟着微微挪位置配合。

第二个是**超导**：温度再降下去，电子会两两结对手拉手，整块材料电阻变成零，通电一点都不发热。

怪就怪在：这两个房客抢同一批电子用。垄沟排得越结实，能拿去结对的电子就越少，超导就越弱；反过来您想办法把垄沟搅乱（比如掺点别的原子进去、或者加高压压一压），超导反倒**冒头变强**了。所以这材料是科学家研究"电子到底更愿意排队还是更愿意结对"的一块标准试验田。

老一套的解释（说垄沟是因为电子在某些方向上正好"合拍"造成的）对不上账——按那个说法排出垄沟以后材料该变成绝缘体，可它偏偏还导电。所以现在更信另一套：是**电子和晶格之间拉得特别紧**（强电子-晶格耦合），局部地方原子和电子抱成团，才排出这些垄沟。

## 🏗️ 结构概览

2H-NbSe₂ 的单层由一层 Nb 夹在两层 Se 之间构成，Nb 处于三棱柱配位。2H 多型的堆垛周期为两层（AA'AA' 序），层间为范德华间隙。它在 T_CDW ≈ 33 K 进入 3×3 非公度电荷密度波相，在 T_c ≈ 7.2 K 进入超导态——两个转变温度相距不远且共处同一费米面，这是它成为 CDW/SC 竞争研究标准体系的结构与能标基础。CDW 相变后材料仍保持金属性，这一点与传统 Peierls 图像的预期直接矛盾。

## 🧩 物理实质：CDW 与超导共存

传统理论将 TMD 中 CDW 归因于费米面嵌套（Fermi surface nesting, FSN）或鞍点奇异性，但无法解释 CDW 相变后仍保持金属性、隧道谱能隙远大于相变温度对应能量尺度等矛盾；强电子-晶格耦合的局域效应提供了更自洽的机制 [[../papers/gorkovStrongElectronlatticeCoupling2012]]。在这一图像下，CDW 不是费米面失稳的全局后果，而是局域晶格形变与电子的强耦合所致，因此只在部分费米面开隙、材料整体仍导电。

## 🔬 实验表征与理论进展

以 1T-TiSe₂ 为代表的 TMD 在电子掺杂或加压抑制公度 CDW 时涌现超导穹顶；基于 McMillan-Ginzburg-Landau 唯象理论，CDW 的拓扑缺陷——错位相子（discommensuration）——在公度到非公度转变中直接诱导或增强超导电性 [[../papers/Chen2019superconductivity]]。这为"抑制 CDW 则超导增强"的普遍观察提供了具体的微观载体：超导不是简单地"捡起 CDW 让出的电子"，而是被 CDW 缺陷网络主动增强。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2019superconductivity]]：研究了 TMD 电荷密度波相中错位相子驱动的超导电性。
- [[../papers/gorkovStrongElectronlatticeCoupling2012]]：提出强电子-晶格耦合是 TMD 中电荷密度波转变的机制。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]：本条目的核心有序态。
- [[../concepts/superconductivity|超导电性]]：与 CDW 竞争的另一有序态。
- [[../concepts/electron-phonon-coupling|电子-声子耦合]]：CDW 形成的现代主流机制。
- [[../concepts/discommensuration|错位相子]]：连接 CDW 与超导增强的拓扑缺陷。
- [[../concepts/peierls-instability|Peierls 失稳]]：被本体系反例挑战的传统图像。
- [[../entities/NbSe2|NbSe₂]]：上位材料条目。
- [[../entities/1T-NbSe2|1T-NbSe₂]]：同一化学式的另一多型，CDW/超导行为不同。
- [[../entities/TiSe2|TiSe₂]]：CDW-超导穹顶的姊妹研究体系。
