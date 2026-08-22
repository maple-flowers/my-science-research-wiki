---
tags: [entity, material, perovskite, metallic-oxide, electrode]
title: 钌酸锶 / Strontium Ruthenate (SrRuO3)
type: entity
status: developing
formula: SrRuO3
class: [perovskite, metallic-oxide, electrode]
properties: [metallic-conductivity, ferromagnetism, epitaxial-electrode]
related_entities: [BaTiO3, BiFeO3, SrTiO3, SrMnO3]
papers: [Kim2008effect, hanPolarTopologicalMaterials2025, junqueraCriticalThicknessFerroelectricity2003]
updated: 2026-08-18
---

# 钌酸锶 / Strontium Ruthenate (SrRuO3)

钌酸锶（SrRuO₃）是钙钛矿结构氧化物中少见的"金属性 + 铁磁性"材料，Ru⁴⁺ 的 4d 电子使其具有良好的导电性。正因如此，SrRuO₃ 在铁电与多铁氧化物研究中最核心的角色是**外延底电极**（epitaxial bottom electrode）：它与 BaTiO₃、BiFeO₃ 等铁电层晶格匹配良好，可在全氧化物异质结构中提供高质量的导电电极。同时，SrRuO₃ 电极的"有限屏蔽长度"直接决定超薄铁电薄膜是否能够保持铁电性，是理解铁电器件微缩极限的关键一环。

## 👵 太奶导读

乖孙，SrRuO₃ 就像钙钛矿家族里的"导电地板"。别的钙钛矿氧化物大多不导电，但它是少数既导电又带磁的"全能选手"。做铁电存储芯片时，下面得先铺一层导电的"地板"（电极），这层地板的导电能力好不好，直接决定了上面那层几纳米厚的铁电膜还灵不灵——地板"罩不住"（屏蔽不好），铁电就失效了。科学家用它证明了：铁电膜做太薄（约 24 埃以下）真的会断电性，从此大家知道了做微型铁电器件的"物理底线"。

## 🏗️ 结构概览

- **晶体结构**：正交畸变钙钛矿，与 SrTiO₃ 衬底晶格失配小，可高质量外延。
- **电子态**：Ru⁴⁺ 4d 电子离域，呈金属导电；同时具有巡游铁磁性（居里温度约 160 K）。
- **功能定位**：作为导电底电极，支撑 BaTiO₃、BiFeO₃、PZT 等铁电/压电薄膜与超晶格的生长。

## 🧩 电极屏蔽与铁电临界厚度

SrRuO₃ 在多铁研究中的科学价值主要来自其"电极"身份（junqueraCriticalThicknessFerroelectricity2003、Kim2008effect）：

- **临界厚度判定**：Junquera & Rabe 2003 通过第一性原理计算证明，夹在 SrRuO₃ 短路电极之间的 BaTiO₃ 薄膜存在约 6 个晶胞（~24 Å）的临界厚度——低于此厚度，电极有限屏蔽产生的退极化场将使铁电性消失。这一结果确立了铁电器件微缩的静电学极限，也使 SrRuO₃ 成为"理想 vs 真实电极"研究的标准对象。
- **薄膜器件基石**：在 BiFeO₃ 外延薄膜研究（Kim2008effect）中，SrRuO₃ 作为底电极用于应变-厚度梯度实验中，支撑对铁电极化随应变演化的系统测量；同时作为导电氧化物，它也是极性拓扑结构器件与铁电异质结（如 FTJ）中电极-铁电界面的常用选择（hanPolarTopologicalMaterials2025）。
- **界面工程**：SrRuO₃ 与铁电层的界面屏蔽质量、界面终止层性质直接影响铁电、磁电耦合与开关行为，是全氧化物电子学的关键材料单元。

## 📚 相关论文 (Related Papers)

- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]：以 SrRuO₃ 电极 + BaTiO₃ 超胞计算确立铁电薄膜临界厚度（~6 晶胞），核心电极屏蔽理论。
- [[../papers/Kim2008effect]]：在 BiFeO₃ 外延薄膜实验中以 SrRuO₃ 为底电极，研究应变-厚度对铁电极化的影响。
- [[../papers/hanPolarTopologicalMaterials2025]]：在铁电氧化物异质结与极性拓扑器件中讨论电极与界面作用。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/critical-thickness-ferroelectric|铁电临界厚度]]
- [[../concepts/depolarization-field|退极化场]]
- [[../concepts/incomplete-screening|电极不完全屏蔽]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../entities/BaTiO3|BaTiO₃（铁电层对照）]]
- [[../entities/BiFeO3|BiFeO₃（多铁铁电层对照）]]
- [[../entities/SrTiO3|SrTiO₃（衬底）]]
- [[../entities/SrMnO3|SrMnO₃（同族磁性钙钛矿）]]
