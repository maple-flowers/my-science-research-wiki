---
tags: [concept, charge-transfer, electron-paramagnetic-resonance, charge-transfer-compound, radical-cation, dismutation-equilibrium, saturable-absorption]
title: mixed-valence
type: concept
status: developing
year: 2003
papers: [Unknown2003charge, Scremin2018nonlinear]
updated: 2026-08-21
---

# mixed-valence

混合价态（mixed valence）指同一化学物种以两种或多种不同氧化态共存。本库中它以两种截然不同的载体出现：一是**金属离子混合价**（Cu(II)/Cu(I) 共存于同一化合物），二是**分子混合价聚集体**（TTF⁺ 与 TTF⁰ 配对）。两者的检测手段与后果完全不同——前者靠磁学/电化学证据、后果是电导下降；后者靠低能吸收带、后果是新的非线性光学通道。

## 👵 太奶导读

乖孙，混合价态就是"同一种元素在一块材料里有两种不同的带电状态"。

举个能摸得着的例子。有人拿一种叫 BEDT-TTF 的有机分子去和氯化铜、溴化铜反应，想做导电材料。铜本来是 +2 价，反应时会被还原。要是**全部**还原成 +1 价，材料能导电；可要是只还原了一部分，剩下一些 +2 价的铜混在里面，那些残留的 +2 价铜就带着未成对电子，像路障一样用库仑力去撞正在跑的导电电子，材料就变成绝缘体了。溴的给电子能力比氯弱，所以溴化物里剩下的 +2 价铜更多，导电性也就更差——差了整整一个数量级。

怎么知道是"混合"的？看磁性。纯 +2 价铜的理论有效磁矩是 1.73 玻尔磁子，可实测只有 1.22–1.26，说明里头掺了一堆不带磁性的 +1 价铜，把平均值拉下来了。这就是混合价态最干净的证据。

另一种混合价长在分子上：TTF 这个分子的正离子（TTF⁺）和中性态（TTF⁰）凑成一对，这对"混合价聚集体"会在 1400 nm 处冒出一条新的吸收带——单独的 TTF⁺ 或 TTF⁰ 都没这条带，它是"两个价态配对"才有的东西。

## 🧩 核心内容与机制 (Core Content)

### 载体一：金属离子混合价 Cu(II/I)（Unknown2003charge）

体系：(BEDT-TTF)₁.₅CuX₂（X = Cl, Br），BEDT-TTF 与 CuX₂ 在乙腈中直接反应制得。BEDT-TTF 被部分氧化，铜以 Cu(II/I) 混合价存在。

**三条独立证据链锁定混合价：**

| 手段 | 观测 | 推论 |
| --- | --- | --- |
| EPR (77 K, X 波段) | 同时出现 BEDT-TTF⁺ 自由基信号与 Cu(II) 四重超精细分裂；Br 化物的 Cu(II) 信号显著更强 | Cu(II) 确实存在，且 Br 化物中比例更高 |
| SQUID 磁化率 | μ_eff = 1.26 / 1.22 BM，**远小于纯 Cu(II) 理论值 1.73 BM**；居里常数 Br 0.53 > Cl 0.39 | 存在非磁性 Cu(I) 稀释了磁矩——混合价的直接证据 |
| 循环伏安 | 观察到 Cu⁺/Cu 与 Cu²⁺/Cu⁺ 两对氧化还原峰 | 电化学上确证两种价态共存 |

其中 μ_eff < 1.73 BM 这一条最具判别力：EPR 只能证明 Cu(II) 在场，唯有磁矩被"稀释"才说明有不贡献磁矩的 Cu(I) 与之共存。Cu(II) 的 g 值满足 g∥ > g⊥ > 2.0，属典型 d⁹ 构型。

**混合价 → 电导的因果链：**

Br⁻ 的给电子诱导效应弱于 Cl⁻ → Cu(II) 更难被还原 → 残留 Cu(II) 更多 → 局域未成对电子通过库仑相互作用散射导电电子 → 电导下降。

| 化合物 | 居里常数 C | μ_eff (BM) | 电导率 σ (S·cm⁻¹) |
| --- | --- | --- | --- |
| (BEDT-TTF)₁.₅CuCl₂ | 0.39 | 1.26 | 9.4 × 10⁻⁵ |
| (BEDT-TTF)₁.₅CuBr₂ | 0.53 | 1.22 | 8.5 × 10⁻⁶ |

两者**均为绝缘体**，Cl 化物仅比 Br 化物高约一个数量级。作者的设计结论是：欲获高电导，BEDT-TTF 与 CuX₂ 的比例应大于 2:1，以确保 Cu(II) 被完全还原为 Cu(I)。

即在这一体系中，**混合价是要被消除的缺陷，而非要被利用的功能**——这与许多以混合价为导电根源的体系（如混合价钙钛矿）恰好相反。

### 载体二：分子混合价聚集体 TTF⁺–TTF⁰（Scremin2018nonlinear）

体系：PMMA 基质中的 TTF⁺ 聚集体（源自 TTFClO₄）薄膜。真空下与空气暴露数小时后的吸收光谱对比给出：

- ~300 nm 新带 → TTF⁰ 生成；
- ~1400 nm 新带 → **TTF⁺–TTF⁰ 混合价聚集体**，代表一种能量更低的电荷转移跃迁。

机制：氧气结合 TTF²⁺ 并形成 S-氧化物，从而移动了 TTF⁺ 的[[../concepts/dismutation-equilibrium|歧化平衡]]，导致 TTF⁺–TTF⁰ 生成。与溶液中的对照很关键：溶液里歧化反应**完全**走向 TTF⁰ + TTF²⁺，TTF⁺ 二聚体/聚集体的 CT 带彻底消失；而在 PMMA 中反应只达到一个**平衡态**，CT 带仍存在。也就是说，是聚合物基质的束缚使混合价物种得以稳定观测。

该 1400 nm 带被作者列为待研究的对象（"研究其在更低能量光子下的超快响应"），本文的非线性光学测量主要在 ~800 nm 激发 TTF⁺ 聚集体的 CT 带上进行。

## ⚠️ 使用本页时的边界

- **两种载体不可混谈**。Cu(II/I) 是金属离子价态共存，判据是磁矩稀释；TTF⁺–TTF⁰ 是分子氧化态配对，判据是低能 CT 吸收带。二者的实验手段无交集。
- Scremin2018 对 1400 nm 带的归属用的是**推测性措辞**（"may be due to the formation of mixed valence aggregates"），并非确证。本页不把它当作已定论的赋值。
- Unknown2003charge **未给出晶体结构解析**，因此"Cu(II) 与 Cu(I) 在晶格中如何分布"这一问题在原文中悬置；本页的库仑散射图像是基于磁学+电导关联的推断，不是结构证据。
- 电导率为**粉末压片**测量值，非单晶各向异性测量，不宜与单晶数据直接比较。
- 两篇论文均标注为 `Unknown` / 作者信息不全的条目，引用时须回溯原始出处。

## 📚 相关论文 (Related Papers)

- [[../papers/Unknown2003charge]]：在 (BEDT-TTF)₁.₅CuX₂ 中以 EPR、SQUID（μ_eff 1.22–1.26 BM 远低于纯 Cu(II) 的 1.73 BM）和循环伏安三条证据确证 Cu(II/I) 混合价，并建立"卤素诱导效应弱 → Cu(II) 残留多 → 库仑散射增强 → 电导下降一个数量级"的构效关系，从而把混合价定性为需被消除的导电障碍。
- [[../papers/Scremin2018nonlinear]]：在 PMMA 基质的 TTF⁺ 薄膜中观察到空气暴露后出现约 1400 nm 的新吸收带，将其归为 TTF⁺–TTF⁰ 分子混合价聚集体的低能电荷转移跃迁，并指出聚合物基质使歧化反应停在平衡态而非完全转化，从而让混合价物种得以稳定观测。

## 🔗 关联概念与实体 (Related)

- [[../concepts/charge-transfer|charge-transfer]]
- [[../concepts/charge-transfer-compound|charge-transfer-compound]]
- [[../concepts/electron-paramagnetic-resonance|electron-paramagnetic-resonance]]
- [[../concepts/dismutation-equilibrium|dismutation-equilibrium]]
- [[../concepts/radical-cation|radical-cation]]
- [[../concepts/saturable-absorption|saturable-absorption]]
- [[../entities/TTF|TTF]]
- [[../entities/TTFClO4|TTFClO4]]
- [[../entities/PMMA|PMMA]]
