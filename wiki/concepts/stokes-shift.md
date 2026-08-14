---
tags: [concept, photophysics, spectroscopy]
title: 斯托克斯位移 / Stokes Shift
type: concept
status: developing
domain: [spectroscopy, photophysics, molecular-physics]
mechanism: 分子的发射光谱（荧光）最大值波长比对应的吸收光谱最大值波长向更长波长方向移动的现象
related_concepts: [solvatochromism, photoluminescence, ict-mechanism, solvent-relaxation]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence]
updated: 2026-08
---

# 斯托克斯位移 / Stokes Shift

斯托克斯位移（Stokes Shift）是指分子发光（荧光或磷光）的最大值波长（或能量）比其对应的吸收光谱最大值波长向更长波长（更低能量）方向移动的现象。

## 👵 太奶导读

太奶啊，这就好比是咱们**“买卖时候的折损”**。您拿 10 块钱（高能量的入射光）去买东西，等您买完倒手卖出去（发射荧光）的时候，因为中间要交税、路费折损（分子内部的振动消耗、周围邻居重排扣除一部分能量），您最后只换回了 8 块钱（更低能量、更长波长的出射光）。中间“折损”（损失掉的能量）越多，吸收和发射波长之间的距离就拉得越开。这个拉开的距离，就是咱们物理上的“斯托克斯位移”。折损得越多，说明这分子跟周围溶剂邻居“互动”得越厉害（极性强、溶剂重排大）。

## 🏗️ 物理起源

斯托克斯位移的大小反映了分子激发态演化过程中的能量耗散：
1.  **振动弛豫 (Vibrational Relaxation)**：电子受激后，迅速损失部分能量，降至第一激发态的最低振动能级（耗时约 $10^{-12}$ 秒）。
2.  **溶剂重排（溶剂弛豫）**：激发态巨大的偶极矩会诱导周围极性溶剂分子发生转动重排。这一重排能极大降低激发态的整体能量。

## 🧩 溶剂化变色中的核心表征

在具有显著 [[../concepts/ict-mechanism|分子内电荷转移 (ICT)]] 的推拉分子中，斯托克斯位移通常会随溶剂极性增加而剧烈增加：
*   **P1 探针**：其吸收峰始终处于 401–419 nm，而发射峰从环己烷中的 445 nm 红移到 DMSO 中的 641 nm。这导致斯托克斯位移从非极性环境中的极小值骤增至极性环境中的超大值 [[../papers/Huang2023two]]。
*   **物理意义**：超大的斯托克斯位移能实现极好的“吸收-发射分离”，在生物成像中可以完全消除自吸收和激发光背景的干扰。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：研究了利用超大斯托克斯位移消除生物背景自发荧光干扰的策略。
- [[../papers/Huang2019solvatochromic]]：使用 Lippert–Mataga 模型对 Stokes 位移随极性参数的偏移进行了线性拟合。
- [[../papers/H2017fluorescence]]：给出了不同质子/非质子溶剂中 P1 探针的精确 Stokes 位移数值表。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/solvatochromism|溶剂化显色]]
- [[../concepts/photoluminescence|光致发光]]
- [[../concepts/ict-mechanism|ICT 机制]]
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]
