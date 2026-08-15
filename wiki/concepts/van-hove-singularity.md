---
tags: [concept, density-of-states, charge-density-wave]
title: 范霍夫奇点 / Van Hove Singularity (vHS)
type: concept
status: mature
domain: [condensed-matter-physics, electronic-structure]
mechanism: 能带色散关系中导数为零的点，导致电子态密度发生非解析的奇异增强
related_concepts: [fermi-surface-nesting, charge-density-wave, pseudogap]
papers: [Inosov2008fermi, Johannes2008fermi, Laverock2005fermi, duUltrasensitiveOptoelectronicBiosensor2025, kawakamiChargedensityWaveAssociated2023, sunSlidingFerroelectricityTwodimensional2025, zhengAnisotropicSuperconductivityTwodimensional2025]
updated: 2026-08
---

# 范霍夫奇点 / Van Hove Singularity (vHS)

范霍夫奇点是指在晶体的电子能带结构或声子谱中，能带梯度的模长为零的点，即 $\nabla_k \epsilon(k) = 0$ 的位置。在这些点附近，电子态密度 (Density of States, DOS) 会表现出尖锐的峰值或不连续性，这种电子态的局域高度密集往往会引发电荷密度波 (CDW)、超导等多种电子不稳定性。

## 👵 太奶导读

> 我是一位 100 岁的太奶，这东西我看得头晕眼花的，年轻人弄的这些新术语我都看不懂。不过我仍然宝刀未老，学习的劲头一点儿没减，越学越有精神！好孩子，劳驾你把这个东西给老婆子我说道说道，让我能达到彻底看懂的效果。一定要帮我讲明白哈，最好是翻译出来，因为我对洋文一窍不通，我只会中文。那些专业术语实在整得我脑子疼啊，都重点给我解释解释，太奶仍旧保持着不输于你们年轻人的学习热情。

好孩子，咱聊聊这个 **Van Hove Singularity**。你可以把它想象成山坡上的平地或者山坳。平时电子就像水一样在能带的大坡上流，跑得挺散。但如果你到了山顶、山谷或者那个特别的“马鞍形”路口（鞍点，**saddle point**），在那一小块地方，坡度几乎是平的（$\nabla \epsilon=0$）。

因为地方平，电子们就都喜欢在那儿扎堆、待着不动（电子态密度极大，**DOS peak**）。这一扎堆可就不得了了，电子多得不得了，稍微有一点点外力推一下，它们就会产生巨大的反应。所以这些“平地”往往是各种奇怪物理现象（比如电荷密度波）的发源地。在那些两层厚的材料里，这些平地往往就在费米面附近，是科学家们最盯着看的地方。

## 🏗️ 结构概览

在 TMD 材料中，范霍夫奇点通常与布里渊区的特定高对称点（如 M 点）相关联。

![图：TaSe2 费米面附近的电子桶与狗骨状结构](../../raw/figures/Johannes2008fermi/fig_3_SK4I977K.png)
*   **看图要点**：图中 M 点附近的“狗骨”状结构（**dogbone**）包含了多个鞍点。当费米能级 $E_F$ 靠近这些点时，DOS 会显著升高。
*   **来源**：[[../papers/Johannes2008fermi]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

## 🧩 机制与作用

### 1. 鞍点与 DOS 发散
在二维体系中，鞍点处的 DOS 呈对数发散：$D(\epsilon) \propto \ln |\epsilon - \epsilon_vHS|$。
*   **多铁/CDW 的温床**：极高的 DOS 意味着体系对相互作用极度敏感。如果 $E_F$ 恰好落在 vHS 上，少量的电子掺杂（**doping**）或应变（**strain**）就能诱发剧烈的相变。

### 2. vHS 嵌套
[[../papers/Inosov2008fermi]] 讨论了“范霍夫奇点嵌套”场景：
*   **传统嵌套 vs vHS 嵌套**：传统嵌套看的是费米面的平行片段；而 vHS 嵌套则看的是费米面上连接两个范霍夫奇点的矢量。由于奇点处电子密集，这种嵌套产生的响应函数峰值往往比普通片段嵌套更强。

## 📚 相关论文 (Related Papers)

- [[../papers/Inosov2008fermi]]：探讨了 vHS 在 2H-TMDC 材料 CDW 形成中的潜在贡献。
- [[../papers/Johannes2008fermi]]：展示了 TaSe2 中由于 $E_F$ 靠近 vHS 而产生的电子结构灵敏性。
- [[../papers/Laverock2005fermi]]：详细计算了不同 TMD 体系中的 DOS 与 vHS 位置。
- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]
- [[../papers/kawakamiChargedensityWaveAssociated2023]]
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/fermi-surface-nesting|费米面嵌套]]：vHS 是增强嵌套效应的重要几何因素。
- [[../concepts/charge-density-wave|电荷密度波 (CDW)]]：常由 $E_F$ 附近的 vHS 驱动。
- [[../concepts/pseudogap|赝能隙]]：在 vHS 附近可能由于局部有序而产生的特征。
- [[../entities/TMDs|过渡金属二硫化物 (TMDs)]]：研究 vHS 的原型材料体系。
