---
tags: [entity, material, ferroelectric, oxide, cmos]
title: 氧化铪 / Hafnium Oxide (HfO2)
type: entity
status: developing
formula: HfO2
class: [oxide, ferroelectric, dielectric]
properties: [ferroelectricity, cmos-compatibility, wake-up-effect, fatigue-effect]
related_entities: [HZO, FTJ, FeFET, BaTiO3]
papers: [FerroelectricityMultiferroicityAtomic2023, chenHafniumBasedFerroelectricPostMoore2026, hanPolarTopologicalMaterials2025, huangTwodimensionalIn2Se3Rising2022, martinThinfilmFerroelectricMaterials2016]
updated: 2026-08-18
---

# 氧化铪 / Hafnium Oxide (HfO2)

氧化铪（HfO₂）本是一种常规高介电常数氧化物，直到 2011 年前后在 Si 掺杂薄膜中意外发现其具有铁电性，才成为铁电领域最受关注的"新贵"。与 BaTiO₃ 等传统钙钛矿铁电体不同，铪基铁电性的来源是亚稳态正交相（Pca2₁），且不存在明显的临界厚度限制，可与 CMOS 工艺直接兼容。这一特性使 HfO₂ 基铁电体（尤其是 Hf₀.₅Zr₀.₅O₂, HZO）成为后摩尔时代非易失性存储与神经形态计算最有力的材料平台之一。

## 👵 太奶导读

乖孙，过去做"会记忆"的铁电材料都要用钙钛矿那种"娇贵"配方，又难做又难装进芯片。氧化铪呢，本来是芯片里很常见的一种"绝缘涂料"（高 k 栅介质），结果科学家意外发现它居然也能变成铁电材料——就像发现家里的墙漆居然能变成磁铁一样神奇。它的好处是跟现有的芯片工艺（CMOS）完全合得来，做得再薄也不怕失效，还没有传统材料"太薄就不灵"的毛病。所以现在造新一代"聪明存储芯片"（FeFET/FTJ/FeRAM）都爱用它。

## 🏗️ 结构概览

HfO₂ 基铁电体系的关键在于"相"：

- **稳定相**：单斜相（常温稳定，非铁电）。
- **铁电相**：正交相 Pca2₁（亚稳），由掺杂、应力或薄膜厚度约束锁定。
- **掺杂策略**：Si、Zr、La、Al、Y、Ce 等掺杂均能稳定正交铁电相；Hf₀.₅Zr₀.₅O₂ (HZO) 是最常用的体系之一。

## 🧩 铁电性来源与器件化

铪基铁电性没有传统钙钛矿的 $d^0$ 约束，其极化源于正交相中氧八面体沿 c 轴的位移，翻转势垒适中、可与微电子工艺兼容。基于此构建的四类核心器件（chenHafniumBasedFerroelectricPostMoore2026）：

1. **FeFET**（铁电场效应晶体管）：用铁电层作为栅介质，极化态调制沟道。
2. **FTJ**（铁电隧道结）：M/FE/M 三明治，极化翻转改变隧穿电阻。
3. **FeRAM**（铁电随机存储器）：铁电电容存储。
4. **Fe-Diode**（铁电二极管）：整流特性随极化变化。

铪基体系还面临三类关键挑战：亚稳正交相的稳定性与唤醒/疲劳效应（wake-up / fatigue）、低于 400°C 的后端（BEOL）热预算兼容、以及三维高密度集成（FerroelectricityMultiferroicityAtomic2023、chenHafniumBasedFerroelectricPostMoore2026）。此外，HfO₂ 基铁电薄膜也被用于极性拓扑结构研究，如极化涡旋等新奇构型（hanPolarTopologicalMaterials2025）。

## 📚 相关论文 (Related Papers)

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：铪基铁电后摩尔电子学最系统的综述，覆盖材料-器件-集成全链条。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：将氧化铪列为原子级厚度铁电/多铁的三大材料体系之一，强调 CMOS 兼容与无临界厚度。
- [[../papers/hanPolarTopologicalMaterials2025]]：讨论 HfO₂ 基铁电薄膜中的极性拓扑结构与器件前景。
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]：以 In₂Se₃ 作对照，讨论铁电数据存储的二维材料路线。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：综述铁电薄膜材料，提供铪基体系与传统钙钛矿的横向对比背景。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/hafnia-ferroelectricity|铪基铁电性]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/polarization-switching|极化翻转]]
- [[../concepts/wake-up-fatigue|唤醒与疲劳效应]]
- [[../concepts/cmos-compatibility|CMOS 兼容性]]
- [[../concepts/neuromorphic-computing|神经形态计算]]
- [[../entities/HZO|HZO（Hf₀.₅Zr₀.₅O₂）]]
- [[../entities/FTJ|铁电隧道结]]
- [[../entities/BaTiO3|BaTiO₃]]
