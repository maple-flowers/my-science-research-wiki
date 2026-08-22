---
tags: [concept]
title: 'CDW-莫特相 / CDW-Mott Phase'
type: concept
status: mature
domain: [condensed-matter-physics, strongly-correlated-systems]
mechanism: 电荷密度波与莫特局域化协同形成的绝缘相
related_concepts: [charge-density-wave, mott-insulator, electron-correlation, 2d-materials, metal-insulator-transition, spin-charge-density-wave]
papers: [nakataRobustChargedensityWave2021]
updated: 2026-08
---

# CDW-莫特相 / CDW-Mott Phase

CDW-莫特相（CDW-Mott phase）指**电荷密度波（CDW）序与莫特型电子关联协同共存、共同决定体系电子结构的有序相**。其核心物理是：低维性与强电子关联相结合，使体系同时呈现晶格驱动的电荷调制（CDW）与库仑定域化的能隙（Mott），二者互锁，产生既不同于纯 CDW、也不同于纯 Mott 绝缘体的独特量子态。

## 👵 太奶导读

乖孙，这一条讲的是「CDW 和莫特绝缘」是怎么手拉手合作的。
单独看：CDW 是材料里的电子像"排成波浪队形"一样周期性扎堆；莫特绝缘是电子因为"互相嫌弃"（库仑排斥）而各自守在自己格位上不许乱跑，材料就变得不导电了。这个 CDW-莫特相呢，就是这两种"不导电的理由"凑在一起、互相帮衬的状态——既排了队形，又守了格位，双重理由把电子牢牢锁住，形成一种特别顽固的绝缘/量子有序态。

## 🏗️ 结构概览

CDW-莫特相位于"晶格序"与"关联序"两个物理世界的交汇点。纯 CDW 由电子-声子耦合/费米面嵌套驱动；纯 Mott 绝缘由库仑排斥驱动。当两者强度可比时，体系进入 CDW-Mott 协同态：CDW 的波矢调制为 Mott 定域提供周期势，Mott 的强关联又增强 CDW 的稳定性，二者自洽强化。该相常见于 1T-TaS₂ 等层状过渡金属硫族化物（TMD），是理解其金属-绝缘体转变与多体物理的关键。

## 🧩 核心内容与机制 (Core Content)

- **协同机制**：CDW 提供周期性晶格畸变与电荷调制，降低体系的动能；Mott 关联在调制后的格位上进一步将电子定域，二者协同打开比单一机制更宽的能隙。
- **典型体系**：1T-TaS₂ 在低温呈现的"公度 CDW + 莫特绝缘"态是 CDW-Mott 相的教科书范例；其电荷有序与关联能隙共存决定了丰富的相图（[[../papers/nakataRobustChargedensityWave2021|Nakata 2021]]）。
- **与超导/磁性竞争**：CDW-Mott 相常与超导、磁性、金属相竞争，压力、掺杂、电场可驱动其间的相变。
- **低维增强**：二维体系的电子-声子耦合与关联效应均被增强，使 CDW-Mott 协同更容易出现（[[../papers/nakataRobustChargedensityWave2021|Nakata 2021]]）。

## 📋 关键参数表

| 参数 | 含义 | 特征 |
|---|---|---|
| 关联强度 U | Mott 定域程度 | 强关联判据 |
| CDW 波矢 q | 电荷调制周期 | 公度/近公度 |
| 能隙 Δ | 激发间隙 | CDW+Mott 协同 |
| 相变温度 | 有序/失序 | 压力/掺杂可调 |
| 维度 | 低维增强 | 2D 更显著 |

## 🔀 近邻概念辨析

- **CDW-Mott 相 vs 纯 CDW**：纯 CDW 可理解为晶格/嵌套驱动的电荷调制；CDW-Mott 相额外叠加库仑定域化，能隙与绝缘性显著增强，两者不能仅用单粒子图像描述。
- **CDW-Mott 相 vs 纯 Mott 绝缘体**：Mott 绝缘强调格点定域、无电荷调制周期图案；CDW-Mott 相在定域基础上还有 CDW 的周期性电荷/晶格调制。
- **CDW-Mott 相 vs 电荷有序**：电荷有序泛指任何格点电荷周期排列；CDW-Mott 相特指 CDW 与 Mott 关联协同的强关联态。

## 📚 相关论文 (Related Papers)

- [[../papers/nakataRobustChargedensityWave2021]] — Robust charge density wave state in (…)，为 CDW-Mott 协同提供了关键证据。

## 🔗 关联概念与实体 (Related)

- [[../concepts/charge-density-wave|电荷密度波]]：CDW 序的基础。
- [[../concepts/mott-insulator|莫特绝缘体]]：关联定域化基础。
- [[../concepts/electron-correlation|电子关联]]：Mott 定域的根源。
- [[../concepts/2d-materials|二维材料]]：CDW-Mott 协同的载体。
- [[../concepts/spin-charge-density-wave|自旋-电荷密度波]]：电荷与自旋调制共存图像。
- [[../entities/TaSe2|TaSe₂]]：CDW 研究典型体系。
