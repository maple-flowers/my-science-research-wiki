---
tags: [concept, ferroelectric, 2D]
title: '偶极锁定 / Dipole Locking'
type: concept
status: developing
domain: [ferroelectricity, 2d-materials]
mechanism: "同一体系内不同取向（面内/面外）或不同晶位的极化分量通过共价再成键相互约束，一个分量翻转必然牵动另一分量协同翻转"
related_concepts: [ferroelectricity, sliding-ferroelectricity, 2d-materials, ferroelectric-domain, charge-transfer, depolarization-field]
related_entities: [In2Se3, WTe2, CuInP2S6]
papers: ['huangTwodimensionalIn2Se3Rising2022', 'guanRecentProgressTwoDimensional2020', 'guoAdvancesTwodimensionalFerroelectric2025']
updated: 2026-08
---

# 偶极锁定 / Dipole Locking

偶极锁定（dipole locking）指**铁电体中不同方向（如面内与面外）或不同晶位的极化偶极分量相互锁定的现象**：一个分量翻转必然牵动另一个分量协同翻转。偶极锁定是理解 α-In₂Se₃ 等"面内-面外互锁铁电"、抗退极化场能力与多态存储的关键机制。

## 👵 太奶导读

有些铁电体里的偶极"绑在一起"：面内方向的偶极和面外方向的偶极像榫卯一样咬死，你动我也得跟着动——这叫偶极锁定。好处是：想翻"上下"就必然带动"左右"一起翻，状态更稳、更难被杂散场破坏，还能靠这个"连锁反应"实现多态存储。α-In₂Se₃ 就是这种"全身绑一起"的典型代表。

## 🧩 偶极锁定与面内-面外互锁铁电

- **α-In₂Se₃ 的互锁极化**：二维 In₂Se₃ 的铁电性源于独特的"再成键"机制与面内-面外极化互锁（偶极锁定），能有效抵抗退极化场；顺电 β 相具有"墨西哥帽"势能面，导致结构多样性。基于该材料的 FeFET、FeS-FET 等器件在存储与神经形态计算方面展现巨大潜力（[[../papers/huangTwodimensionalIn2Se3Rising2022|Huang 2022]]）。

## 🧩 偶极锁定与二维铁电机制

- **机制分类**：二维铁电性的内在机制可归纳为"层内键合作用"（包括结构畸变、偶极锁定、电子极化）与"层间平移作用"两大类，偶极锁定是层内键合路线的核心要素（[[../papers/guanRecentProgressTwoDimensional2020|Guan 2020]]）。
- **与滑动铁电互补**：滑动铁电通过层间滑移诱导电荷重分布产生面外极化，具有超低翻转能垒与高可调性，与依赖偶极锁定的本征铁电体互为补充（[[../papers/guoAdvancesTwodimensionalFerroelectric2025|Guo 2025]]）。

## 🧭 近邻概念辨析

| 对比对象 | 关键区别 |
| :--- | :--- |
| [[../concepts/sliding-ferroelectricity\|滑动铁电]] | 滑动铁电的极化来自**层间**相对平移（层间平移作用）；偶极锁定属**层内键合作用**，靠同一层内共价再成键把不同取向偶极绑定。Guan 2020 正是把二维铁电机制二分为这两大类（[[../papers/guanRecentProgressTwoDimensional2020\|Guan 2020]]） |
| 位移型铁电 | In₂Se₃ 被归为「相变型铁电体」而非传统位移型：翻转伴随再成键与结构相变，不是单一离子在固定骨架中偏移（[[../papers/huangTwodimensionalIn2Se3Rising2022\|Huang 2022]]） |
| [[../concepts/depolarization-field\|退极化场]] | 退极化场是**削弱**薄层极化的静电效应；偶极锁定是**抵抗**退极化场的结构机制，二者是矛与盾的关系 |
| 普通多轴铁电体 | 多轴铁电只是存在多个等价极化方向，各方向可独立选取；偶极锁定要求各分量**强制联动**，不能独立翻转 |

> ⚠️ 证据边界：本库现有 3 篇均为**综述**，「面内-面外互锁」在其中以定性机制描述给出，未提供锁定强度（如耦合系数、分量间夹角）的定量值；α-In₂Se₃ 的翻转势垒等数值出自其他页引用的同批文献，条件口径不一，故本页不设参数表。补入 In₂Se₃ 原始计算/实验论文后可升级 status。

## 📚 相关论文 (Related Papers)

- [[../papers/huangTwodimensionalIn2Se3Rising2022]] — Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage：提出「相变型铁电体」概念，指明 In₂Se₃ 的稳健铁电性源于再成键机制与面内-面外极化互锁，并用「墨西哥帽」势能面统一解释顺电 β 相的结构多样性——本页机制的主要来源。
- [[../papers/guanRecentProgressTwoDimensional2020]] — Recent Progress in Two-Dimensional Ferroelectric Materials：把二维铁电起源归纳为「层内键合作用」与「层间平移作用」两大类，偶极锁定被明确列为前者的核心要素，是本页在机制谱系中的定位依据；同时强调 PFM 假信号风险、需 SHG/TEM 交叉验证。
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]] — Advances in two-dimensional ferroelectric materials：区分「自发极化」与「滑移铁电」两大范式，说明依赖偶极锁定的本征铁电体与超低势垒的滑动铁电互为补充，为本页的辨析表提供对照口径。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：偶极锁定的母体序。
- [[../concepts/sliding-ferroelectricity|滑动铁电]]：与偶极锁定互补的另一条二维铁电路线，区别见上方辨析表。
- [[../concepts/depolarization-field|退极化场]]：偶极锁定所抵抗的对象。
- [[../concepts/2d-materials|二维材料]]：偶极锁定现象的主要载体。
- [[../concepts/ferroelectric-domain|铁电畴]]：偶极锁定在空间上的表现形式。
- [[../concepts/charge-transfer|电荷转移]]：再成键与偶极锁定的微观来源。
- [[../entities/In2Se3|In₂Se₃]]：面内-面外互锁铁电的原型体系。
- [[../entities/WTe2|WTe₂]]：以层间滑移为机制的对照 TMD 体系。
- [[../entities/CuInP2S6|CuInP₂S₆]]：层内键合型二维铁电体。
