---
tags: [concept, ferroelectrics, polarization-switching]
title: 畴壁成核 / Domain-Wall Nucleation
type: concept
status: mature
domain: [ferroelectrics, polarization-switching, device-physics]
mechanism: 极化翻转的起始过程——新畴在电极/缺陷/表面处成核，临界核越过自由能垒后由畴壁传播扩张；成核率与传播速度共同决定开关动力学
related_concepts: [domain-wall-motion, domain-wall-pinning, polarization-switching, coercive-field, ferroelectric-domain, domain-wall, depletion-layer]
papers: [Chen2016electrical]
updated: 2026-08
---

# 畴壁成核 / Domain-Wall Nucleation

畴壁成核（domain-wall nucleation）指**铁电极化翻转过程中新畴的诞生过程**：在外电场驱动下，局部区域（电极界面、缺陷、表面台阶）克服自由能垒形成临界尺寸的反向畴核，随后通过畴壁传播（domain-wall motion）扩张至整个畴。成核与传播两大机制共同决定铁电器件的开关时间、矫顽场与疲劳特性。

## 👵 太奶导读

太奶啊，铁电材料里的"小箭头"（极化）要掉头，得先在一个小地方"冒出"一个反向的小区域——就像水烧开了，得先起几个小气泡。这个小气泡"冒出来"的过程就是成核；气泡太小会自己缩回去，够大了才能长大。材料里的缺陷、电极边角就是最容易"冒泡"的地方。搞懂在哪冒泡、多快冒泡，才能让存储器写得又快又稳。

## 🧩 核心内容与机制 (Core Content)

- **成核位点**：成核优先发生在电场增强处——电极/铁电界面、表面台阶、晶界与缺陷附近（局部退极化场与缺陷能降低成核势垒）。
- **临界核与势垒**：成核需跨越由体自由能（−2P·E·V）与畴壁能（表面项）竞争决定的自由能垒；临界核尺寸由体项与表面项平衡给出，与电场强度成反比。
- **与畴壁传播竞争**：极化开关动力学由成核率与畴壁传播速度共同控制（Kolmogorov-Avrami 型模型）；薄膜中开关常受成核主导，单畴/微米级畴可由传播主导。
- **器件影响**：成核与传播的不均匀性影响铁电存储器的写电压、开关速度与疲劳；多步开关（two-step switching）与中间态也与成核/传播的竞争有关 [[../papers/Chen2016electrical]]。

## 📊 成核与传播对比

| 特征 | 畴壁成核 | 畴壁传播 |
|------|----------|----------|
| 物理过程 | 新畴诞生 | 既有畴壁扩张 |
| 关键位点 | 电极/缺陷/表面 | 壁内钉扎中心 |
| 能量障碍 | 临界核自由能垒 | 钉扎势 |
| 对开关影响 | 决定起始时间 | 决定扩张速率 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/domain-wall-motion|畴壁运动]]：成核后的扩张过程。
- [[../concepts/domain-wall-pinning|畴壁钉扎]]：传播的主要障碍。
- [[../concepts/polarization-switching|极化翻转]]：成核所属的完整过程。
- [[../concepts/coercive-field|矫顽场]]：成核/传播所需电场。
- [[../concepts/ferroelectric-domain|铁电畴]]：成核的对象。
- [[../concepts/domain-wall|畴壁]]：成核/传播的界面。
- [[../entities/BiFeO3|BiFeO₃]]：典型铁电/多铁材料。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2016electrical]]：铁电极化开关中畴演化对宏观电性能的关键作用，涉及成核与传播机制。

## 🏷️ 专业名词别名

- `domain-nucleation`（concepts）
- `极化畴成核`（concepts）
