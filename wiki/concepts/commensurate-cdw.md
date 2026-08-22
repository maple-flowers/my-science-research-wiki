---
tags: [concept]
title: '公度电荷密度波 / Commensurate CDW'
type: concept
status: mature
domain: [condensed-matter-physics, charge-density-wave]
mechanism: 调制波矢与晶格倒格矢成有理数比值的电荷密度波
related_concepts: [charge-density-wave, incommensurate-cdw, commensurate-incommensurate-cdw, structural-phase-transition, charge-order]
papers: [Barnett2006coexistence, Inosov2008fermi]
updated: 2026-08
---

# 公度电荷密度波 / Commensurate CDW

公度电荷密度波（commensurate CDW）指**调制波矢 q 与晶格倒格矢成有理数比值（q = p/m · G）的电荷密度波**。此时电荷调制与晶格周期严格"锁定"，形成整数个调制周期恰好覆盖整数个晶格周期的超结构。公度 CDW 通常在降温过程中从不公度（或近公度）相转变而来，伴随晶格畸变、能隙打开与对称性降低，是 CDW 材料相图中的关键有序相。

## 👵 太奶导读

太奶啊，"公度"说白了就是"整齐对上号"。
电荷密度波是电子在材料里排成"波浪"。如果这个波浪的间距和原子的间距是"整倍数"的关系（比如每隔 3 个原子一个浪头），波浪就正好跟晶格"咬合"上了，这就叫公度。公度的波浪特别稳定，很难被推走，常出现在材料降温之后，往往还会把导电性搞没（打开能隙）。反过来对不齐整倍数、波浪跟晶格"拧着"的，就叫不公度。

## 🏗️ 结构概览

CDW 按调制波矢与晶格的匹配程度分为公度、近公度与不公度三类。公度 CDW 是最强的锁相态：q 与倒格矢的比值固定，电荷调制与晶格形成互锁超结构。其形成常伴随 Peierls 型晶格畸变与费米面能隙打开，并可通过超晶格反射（X 射线/电子衍射）直接观测。温度、压力、掺杂可驱动公度↔不公度相变，此类相变是 CDW 材料研究的核心议题。

## 🧩 核心内容与机制 (Core Content)

- **定义与锁定**：公度 CDW 的波矢 q 与倒格矢 G 满足 q = (p/m)G（p、m 整数），电荷调制与晶格严格互锁，体系能量最低。
- **与不公度相的转变**：降温或压力驱动下，体系从不公度（q 与 G 无理比）或近公度相进入公度相，伴随晶格畸变增强与能隙演化（[[../papers/Inosov2008fermi|Inosov 2008]]）。
- **超导共存**：公度 CDW 常与超导性共存/竞争，二者的微观关系（配对对称性、能隙结构）是凝聚态物理核心问题（[[../papers/Barnett2006coexistence|Barnett 2006]]）。
- **实验表征**：衍射超晶格峰、ARPES 能隙观测、STM 实空间调制。

## 📋 关键参数表

| 参数 | 含义 | 特征 |
|---|---|---|
| 波矢 q | 调制周期 | 与 G 成有理比 |
| 锁定比例 | q/G | p/m 有理数 |
| 转变温度 | 公度-不公度转变 | 降温/加压驱动 |
| 超晶格峰 | 衍射表征 | 公度超结构 |
| 能隙 Δ | 费米面打开 | 公度相显著 |

## 🔀 近邻概念辨析

- **公度 CDW vs 不公度 CDW**：公度 CDW 波矢与晶格有理比、严格锁相；不公度 CDW 波矢无理比、调制与晶格不匹配。公度相通常能量更低、更稳定。
- **公度 CDW vs 电荷有序**：电荷有序强调格点占据的实空间图案（常天然公度）；CDW 强调波矢调制的动量空间图像，公度 CDW 是两者交汇的情形。
- **公度 CDW vs Peierls 畸变**：Peierls 畸变特指一维金属因嵌套失稳形成的二聚化（q=π/a，公度特例）；公度 CDW 泛指任意有理比调制。

## 📚 相关论文 (Related Papers)

- [[../papers/Barnett2006coexistence]] — 公度 CDW 与超导共存的微观机制。
- [[../papers/Inosov2008fermi]] — 公度/不公度 CDW 转变与费米面结构演化。

## 🔗 关联概念与实体 (Related)

- [[../concepts/charge-density-wave|电荷密度波]]：CDW 的总概念。
- [[../concepts/incommensurate-cdw|不公度 CDW]]：调制波矢无理比的对应相。
- [[../concepts/commensurate-incommensurate-cdw|公度-不公度 CDW]]：两类相转变的合集概念。
- [[../concepts/structural-phase-transition|结构相变]]：公度转变伴随晶格畸变。
- [[../concepts/charge-order|电荷有序]]：实空间电荷图案。
- [[../entities/TaSe2|TaSe₂]]：公度/近公度 CDW 典型材料。
- [[../entities/NbSe2|NbSe₂]]：CDW 与超导共存体系。
