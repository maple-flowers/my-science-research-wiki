---
tags: [entity, device, ferroelectric, tunnel-junction, memory]
title: 铁电隧道结 / Ferroelectric Tunnel Junction (FTJ)
type: entity
status: developing
class: [ferroelectric-device, tunnel-junction]
properties: [ferroelectricity, quantum-tunneling, resistance-switching, synaptic-plasticity]
related_entities: [HfO2, BaTiO3, In2Se3, MoS2]
papers: [FerroelectricityMultiferroicityAtomic2023, chenHafniumBasedFerroelectricPostMoore2026, huProgressProspectsLowdimensional2019, kaurRecentAdvancesTheoretical2025a, zahraCriticalAnalysisFerroelectric2025]
updated: 2026-08-18
---

# 铁电隧道结 / Ferroelectric Tunnel Junction (FTJ)

铁电隧道结 (Ferroelectric Tunnel Junction, FTJ) 是一种两端器件，其核心结构为金属-超薄铁电层-金属 (M/FE/M) 三明治。当铁电层厚度降到几纳米时，电子可以直接隧穿通过该层；而铁电层的极化方向可以通过外电场翻转，从而显著改变隧穿势垒高度与宽度，产生巨大的隧穿电阻变化（TER 效应）。这一"极化可翻转 + 隧穿电阻可调"的特性，使 FTJ 成为非易失性存储与神经形态突触器件的核心候选结构之一。

## 👵 太奶导读

乖孙，FTJ 就像一扇带"记忆开关"的极薄门。门板只有几个原子厚，电子能直接"穿墙"（隧穿）过去。这扇门有个特殊本领：你按一下电压开关，门里的"电箭头"（极化）就会换个方向，门的"厚度"（势垒）也跟着变，于是电子穿过的难易程度（电阻）就完全不同了。而且这个状态断电也不会丢——就像门记住了你上次怎么关的。科学家想用它做又能存数据、又能算东西的"聪明硬盘"（存算一体），一个器件顶过去好几个。

## 🏗️ 结构概览

FTJ 的典型结构为金属/铁电体/金属三明治，关键要素有三层：

1. **铁电隧穿层**：厚度通常为 2–5 nm，需保持铁电性并允许量子隧穿；传统钙钛矿（如 BaTiO₃）与铪基铁电（如 HfO₂）均可承担此角色。
2. **电极**：上下金属电极决定边界条件（屏蔽质量），电极的有限屏蔽长度直接影响铁电层能否在极薄尺度保持极化。
3. **界面**：电极/铁电界面处的肖特基势垒高度随极化翻转而改变，是 TER 的重要来源。

## 🧩 工作原理：极化翻转与隧穿电阻

FTJ 的电阻开关来自极化状态对电子隧穿的两重调制：

- **势垒高度调制**：极化翻转改变金属/铁电界面附近的静电势与肖特基势垒高度，从而改变隧穿电流。
- **势垒宽度与透射率调制**：铁电层内极化电荷的屏蔽差异会改变隧穿势垒的有效形状，叠加量子隧穿透射率差异，最终形成高阻态/低阻态（ON/OFF）的电阻差异。

由于这一机理依赖"铁电性在原子级厚度下仍存在"，FTJ 与原子级厚度铁电材料的进展紧密耦合：钙钛矿氧化物、氧化铪基薄膜与范德瓦尔斯堆叠铁电体都在此背景下被系统性评估（FerroelectricityMultiferroicityAtomic2023）。在铪基体系中，FTJ 与 FeFET、FeRAM、Fe-Diode 并列为四类核心器件结构，其优势在于 CMOS 兼容与可微缩性，并被用于模拟突触可塑性，支撑神经形态计算（chenHafniumBasedFerroelectricPostMoore2026）。

## 📚 相关论文 (Related Papers)

- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：将 FTJ 置于"原子级厚度铁电/多铁"框架下，作为低功耗微型化器件核心结构之一评述。
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：系统梳理铪基铁电四类器件（含 FTJ）的材料工程、器件物理与神经形态集成。
- [[../papers/huProgressProspectsLowdimensional2019]]：在低维多铁综述中将隧穿结列为下一代高密度低功耗器件应用方向。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：从二维滑移铁电理论角度，为 FTJ 的原子级铁电层提供新材料候选与机制参考。
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]：对二维 MXene 铁电/铁磁性质的批判性分析，涉及二维 FTJ 候选材料的可靠性评估。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectric-tunnel-junction|铁电隧道结概念]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/quantum-tunneling|量子隧穿]]
- [[../concepts/neuromorphic-computing|神经形态计算]]
- [[../concepts/in-memory-computing|存内计算]]
- [[../concepts/schottky-barrier|肖特基势垒]]
- [[../entities/HfO2|HfO₂（氧化铪）]]
- [[../entities/BaTiO3|BaTiO₃]]
- [[../entities/In2Se3|In₂Se₃]]
