---
tags: [concept, ferroelectrics, ferroelasticity, magnetism]
title: 畴壁分类 / Domain-Wall Classification
type: concept
status: mature
domain: [ferroelectrics, ferroelasticity, magnetism, topological-defects]
mechanism: 按畴壁取向相对序参量的角度、壁内序参量旋转方式（Ising/Néel/Bloch）、壁的带电性与拓扑手性对畴壁进行分类
related_concepts: [domain-wall, ferroelectric-domain-wall, polarization-switching, topological-defects, ferroelasticity, chirality, domain-wall-texture]
papers: [xuTwodimensionalFerroelasticityVan2021]
updated: 2026-08
---

# 畴壁分类 / Domain-Wall Classification

畴壁分类（domain-wall classification）指**按几何取向、序参量旋转方式、带电性与拓扑性质对畴壁进行系统分类**的方法。畴壁是不同铁性（铁电、铁弹、铁磁）畴之间的过渡区域，其类型直接决定壁的输运、机械与拓扑功能。典型分类维度包括：壁取向相对极化的角度（180°/90°/60°/71° 等）、壁内序参量旋转平面（Ising/Néel/Bloch 型）、壁的电荷状态（带电/中性）与手性（左旋/右旋）。

## 👵 太奶导读

太奶啊，铁电或磁体里不同"小区域"（畴）之间的分界线叫畴壁。这些分界线不是一种——有的"陡"（像 180° 墙，极化方向直接掉头），有的"缓"；有的壁里极化是像扇子一样转着弯过去的，还有的壁本身带电。分法不同，用处也不同：有的壁导电、有的壁绝缘，就能做成"纳米导线"。科学家把这些分界线分门别类，才能选对材料做器件。

## 🧩 核心内容与机制 (Core Content)

- **按壁取向分类**：壁的晶面取向相对相邻畴序参量方向的角度决定其类型——铁电 180° 壁（极化反向）、90°/71°/109° 壁（极化旋转）、铁弹畴壁（自发应变变体边界）。如 β'-In₂Se₃ 中三种取向铁弹畴变体形成约 0.49% 自发应变的畴壁构型 [[../papers/xuTwodimensionalFerroelasticityVan2021]]。
- **按序参量旋转方式分类**：磁性畴壁分为 Bloch 壁（自旋在壁平面内旋转）、Néel 壁（自旋在壁法线平面内旋转）、Ising 壁（壁内自旋指向壁法线）；铁电壁类似地存在 Ising 型（极化沿壁法线）与 Néel 型（极化在壁内旋转）的连续谱。
- **按带电性分类**：铁电畴壁按极化不连续条件分为带电壁（束缚电荷 σ = P·n 不连续）与中性壁；带电壁通过载流子补偿形成导电通道，是"畴壁电子学"的核心要素。
- **拓扑分类**：部分畴壁具有手性旋转（左/右旋）与拓扑荷，可与极性涡旋、麦纫等拓扑结构衔接（本库 [[../concepts/topological-defects|拓扑缺陷]]）。
- **二维铁弹畴**：机械剥离与 CVD 生长的 β'-In₂Se₃ 薄片中，2H/3R 堆垛与反铁电畸变共同决定畴壁类型与倾斜取向 [[../papers/xuTwodimensionalFerroelasticityVan2021]]。

## 📊 畴壁分类速览

| 分类维度 | 类型 | 特征 | 典型体系 |
|----------|------|------|----------|
| 取向角 | 180°/90°/71°/109° 壁 | 序参量翻转/旋转 | BaTiO3、PbTiO3 |
| 旋转方式 | Bloch / Néel / Ising | 自旋/极化旋转平面 | 磁性薄膜、铁电纳米点 |
| 带电性 | 带电壁 / 中性壁 | 束缚电荷补偿 | BiFeO3、YMnO3 |
| 拓扑性 | 手性壁 / 拓扑壁 | 手性旋转、拓扑荷 | 极性涡旋、麦纫体系 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/domain-wall|畴壁]]：分类的对象。
- [[../concepts/ferroelectric-domain-wall|铁电畴壁]]：铁电体系的壁。
- [[../concepts/domain-wall-texture|畴壁织构]]：壁内序参量分布。
- [[../concepts/polarization-switching|极化翻转]]：畴壁产生的过程。
- [[../concepts/topological-defects|拓扑缺陷]]：畴壁的拓扑延伸。
- [[../concepts/ferroelasticity|铁弹性]]：铁弹畴壁的来源。
- [[../concepts/chirality|手性]]：壁手性分类。
- [[../entities/In2Se3|In₂Se₃]]：典型二维铁弹材料。

## 📚 相关论文 (Related Papers)

- [[../papers/xuTwodimensionalFerroelasticityVan2021]]：二维铁弹性的首个明确实验证据，给出 β'-In₂Se₃ 三种取向铁弹畴变体的畴壁分类与表征。

## 🏷️ 专业名词别名

- `domain-wall-types`（concepts）
- `畴壁构型分类`（concepts）
