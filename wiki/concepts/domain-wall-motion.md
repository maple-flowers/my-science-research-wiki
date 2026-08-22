---
tags: [concept, ferroelectricity, spintronics]
title: 畴壁运动 / Domain Wall Motion
type: concept
status: developing
domain: [condensed-matter-physics, ferroelectricity]
mechanism: 外场驱动下铁电/铁磁畴壁迁移，决定极化翻转速度与能耗
related_concepts: [domain-wall, polarization-switching, ferroelectricity, topological-defects]
papers: [Chen2016electrical, chenHafniumBasedFerroelectricPostMoore2026, heUltrafastSwitchingDynamics2024, huangTwodimensionalIn2Se3Rising2022, martinThinfilmFerroelectricMaterials2016, sharmaRoomtemperatureFerroelectricSemimetal2019, sunSlidingFerroelectricityTwodimensional2025, zhangEmergingFrontiersTwodimensional2025]
updated: 2026-08-20
---

# domain-wall-motion

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


畴壁运动（domain wall motion）指铁电/铁磁畴壁在**外场（电场、磁场、应力）驱动下迁移**的过程。畴壁运动决定了极化/磁化翻转的速度与能耗，是铁电存储、铁电器件与神经形态计算中开关动力学与阻变行为的关键物理机制。

## 👵 太奶导读

太奶啊，铁电材料内部被分成一块块"方向一致"的小区域，区域之间隔着一道"墙"（畴壁）。想让整个材料翻转方向，就要让这道墙"搬家"——墙从一头推到另一头，材料的方向就整体换了。墙搬得快不快、省不省电，直接决定存储芯片写得快不快。二维铁电里这道墙尤其轻薄、好推动，成了研究热点。

## 🏗️ 结构概览

畴壁运动是在**驱动场（电场/磁场/应力）**、**缺陷钉扎**与**热涨落**三方竞争下，畴壁在外场方向上的受驱迁移过程。其速度-场关系呈现典型的蠕变 → 去钉扎 → 黏滞流动分段行为，是理解翻转动力学与设计开关器件的核心框架。

## 🧩 核心内容与机制 (Core Content)

- **驱动机制**：电场推动畴壁迁移实现极化翻转；应力、温度梯度亦可驱动；畴壁运动伴随畴成核-长大-合并过程。
- **动力学模型**：畴壁速度-场关系（蠕变 creep、去钉扎 depinning、黏滞流动 viscous flow 区），受缺陷钉扎与热激活影响。
- **二维铁电中的表现**：In₂Se₃、滑动铁电等二维体系中畴壁极薄、翻转极快（本库 he2024 超快开关动力学、fei2018、sun2025）。
- **导电畴壁与功能化**：铁电畴壁可呈导电性（如 MoTe₂ 中极性/相畴壁），畴壁运动可用于阻变存储（忆阻器）与神经形态突触（本库 huangPolarPhase2019、chenHafnium2026）。
- **表征手段**：压电力显微镜（PFM）、二次谐波（SHG）、瞬态电流/电容测量跟踪畴壁运动。

## 📊 参数对照 (Parameters)

| 动力学区 | 驱动场条件 | 速度-场标度 | 主导物理 | 典型应用关联 |
|---|---|---|---|---|
| 蠕变 creep | 弱场（远低于钉扎场） | $v \propto \exp[-(E_c/E)^{\mu}]$ | 热激活 + 随机钉扎 | 低场开关、保留性 |
| 去钉扎 depinning | 场≈临界钉扎场 | 幂律/临界标度 | 缺陷脱钉、临界动力学 | 开关阈值 |
| 黏滞流动 viscous flow | 强场（远高于钉扎场） | $v \propto E$（线性） | 阻尼主导、无钉扎 | 高速翻转、高频器件 |

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2016electrical]] — Electrical and mechanical switching of ferroelectric polarization in the 70 nm BiFeO3 film
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]] — Hafnium-Based Ferroelectric Post-Moore Electronics: Device Physics, Integration Architectures, and Neuromorphic System Implementation
- [[../papers/heUltrafastSwitchingDynamics2024]] — Ultrafast switching dynamics of the ferroelectric order in stacking-engineered ferroelectrics
- [[../papers/huangTwodimensionalIn2Se3Rising2022]] — Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage
- [[../papers/martinThinfilmFerroelectricMaterials2016]] — Thin-film ferroelectric materials and their applications
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] — A room-temperature ferroelectric semimetal
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications
- [[../papers/zhangEmergingFrontiersTwodimensional2025]] — Emerging frontiers in two-dimensional sliding ferroelectrics

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/domain-wall|畴壁]]：运动的主体。
- [[../concepts/polarization-switching|极化翻转]]：畴壁运动是翻转的实现方式。
- [[../concepts/ferroelectricity|铁电性]]：畴壁运动发生的基础。
- [[../concepts/topological-defects|拓扑缺陷]]：畴壁作为拓扑缺陷的行为。
