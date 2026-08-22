---
tags: [entity, material, multiferroic, charge-ordering, ferrite]
title: 铁酸镥 / Lutetium Ferrite (LuFe2O4)
type: entity
status: developing
formula: LuFe2O4
class: [ferrite, multiferroic, charge-ordered]
properties: [multiferroicity, ferroelectricity, charge-ordering, magnetism]
related_entities: [ferrite, BiFeO3, TbMnO3]
papers: [cheongMultiferroicsMagneticTwist2007a, fiebigEvolutionMultiferroics2016, rameshMultiferroicsProgressProspects2007]
updated: 2026-08-18
---

# 铁酸镥 / Lutetium Ferrite (LuFe2O4)

铁酸镥（LuFe₂O₄）是"电子铁电"（Electronic Ferroelectricity）机制的代表材料：其铁电性不来源于离子位移，而是来源于 Fe²⁺/Fe³⁺ 混合价态在三角双层晶格上的电荷有序排列。当电荷有序打破空间反演对称性时，材料便自发产生宏观电极化。在 fiebigEvolutionMultiferroics2016 的多铁分类中，LuFe₂O₄ 与 Fe₃O₄ 一起被列为电荷有序机制（I 类）的典型代表。

## 👵 太奶导读

乖孙，LuFe₂O₄ 给科学家的启发是："电"不一定是靠原子搬家搬出来的，靠电子自己排队也能排出来。这个材料里有两种不同"岁数"的铁离子（Fe²⁺ 和 Fe³⁺），它们喜欢在晶格里排成有规律的队形，队形一乱排（破缺对称），材料整体就带上了电。更妙的是它同时还有磁性——既是"电队形"又是"磁队形"。虽然它的电和磁都还很弱、还不够实用，但它告诉我们一条全新的、绕开老规矩（d⁰ 与 dⁿ 互斥）做多铁材料的思路。

## 🏗️ 结构概览

- **晶体结构**：R-3m 菱方结构，由 Fe₂O₄²⁻ 三角双层与 Lu³⁺ 层沿 c 轴交替堆叠构成。
- **电荷状态**：Fe²⁺ 与 Fe³⁺ 以 1:1 混合价态共存，其有序排布决定极性。
- **磁电共存**：Fe 亚晶格同时提供磁序，形成"电荷有序 + 磁性"的多铁状态。

## 🧩 电子铁电机制

LuFe₂O₄ 的核心机制是电荷有序驱动的铁电性（cheongMultiferroicsMagneticTwist2007a、fiebigEvolutionMultiferroics2016）：

- **电荷有序破缺反演对称**：Fe²⁺/Fe³⁺ 在三角双层内的有序排列（如 2:1 或 3:1 堆叠模式）使电荷密度分布失去反演中心，产生电极化，与磁序的交换伸缩机制、离子位移机制在微观来源上完全不同。
- **与 Fe₃O₄ 的对照**：磁铁矿（Fe₃O₄）同样存在 Verwey 电荷有序，二者共同构成"电荷有序铁电"这一机制家族。
- **价值与局限**：电荷有序机制绕开了传统 $d^0$ 铁电的化学禁忌，但极化较弱、有序温度偏低，目前更多作为机制范本而非实用器件材料。

在薄膜异质结视角下，这类多铁材料与 BiFeO₃、o-TbMnO₃ 共同构成单相多铁的机制谱系（rameshMultiferroicsProgressProspects2007），为设计新多铁体系提供对照。

## 📚 相关论文 (Related Papers)

- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：将 LuFe₂O₄ 列为电子铁电体对照体系，与磁致铁电区分。
- [[../papers/fiebigEvolutionMultiferroics2016]]：明确将 LuFe₂O₄ 归入电荷有序（I 类）多铁机制。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：在薄膜多铁框架下提供多铁机制与薄膜化的对照背景。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/multiferroicity|多铁性]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/charge-ordered-ferroelectricity|电荷有序铁电]]
- [[../entities/ferrite|铁氧体（电荷有序铁电对照）]]
- [[../entities/BiFeO3|BiFeO₃（孤对电子 I 型多铁）]]
- [[../entities/TbMnO3|TbMnO₃（自旋驱动 II 型多铁）]]
