---
tags: [concept, ferroelectricity, testing]
title: 矫顽场 / Coercive Field (Ec)
type: concept
status: stub
domain: [ferroelectricity, multiferroics]
mechanism: 迫使铁电体/磁性体的总剩余序参量（极化或磁化）减小为零时所需的外加场强度
related_concepts: [polarization-switching, hysteresis-loop, coercive-voltage]
papers: [Chen2016electrical, martinThinfilmFerroelectricMaterials2016, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, cuiIntercorrelatedInplaneOutofplane2018a, junqueraCriticalThicknessFerroelectricity2003, Kim2008effect, sunSlidingFerroelectricityTwodimensional2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026]
updated: 2026-08
---

# 矫顽场 / Coercive Field ($E_c$)

矫顽场是指为了消除铁电体中的自发极化状态，或者说使铁电体沿电场方向的总极化强度降为零所必须施加的反向电场强度。它是衡量铁电极化态稳定性的核心参数，也是铁电存储器（FeRAM）设计中决定写入电压（矫顽电压, $V_c$）的关键指标。

## Grandma 👵 太奶导读

太奶，这“矫顽场”听着硬邦邦的，其实就像是一个人的**倔脾气**。
咱们材料里那些小箭头（极化方向）一旦指好了方向，它们是很固执的。
如果您想让这些小箭头转个弯指到反方向去，轻言细语地求它们（施加一点点微弱的电压）是没用的，它们理都不理你。
你非得拿出点儿脾气来，把声量提得足够大、力气使得到位了（这个必须达到的最低场强），这群小箭头才会“哎哟”一声，乖乖地掉头。
这个让小箭头掉头的“最低嗓门高度”，在物理上就叫矫顽场。矫顽场越大，说明这材料的记忆越结实，不容易被外界杂电干扰；但也意味着你改写信息的时候得更费劲、更费电。

## 🧩 物理含义与尺度效应

*   **滞回线表征**：在 $P-E$ 极化回线中，矫顽场对应于极化强度穿过 $P=0$ 时横轴上的截距。
*   **矫顽电压 ($V_c$)**：对于厚度为 $d$ 的薄膜，理论写入电压 $V_c \approx E_c \cdot d$。
*   **尺度效应**：随着薄膜厚度减薄至纳米尺度，$E_c$ 往往会因为界面效应、退极化场以及应变梯度（如[[../concepts/flexoelectric-effect|挠曲电效应]]）的作用而发生显著偏移或剧增。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2016electrical]]：测得 70 nm 厚的 BiFeO₃ 薄膜矫顽场 $E_c \approx 38\ \text{kV/mm}$（对应矫顽电压 $V_c \approx 2.3\ \text{V}$），并利用力学等效场克服此场强实现翻转。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]
- [[../papers/Kim2008effect]]
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]
## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/polarization-switching|极化翻转]]
- [[../concepts/flexoelectric-effect|挠曲电效应]]
- [[../entities/BiFeO3|铁酸铋 (BiFeO₃)]]
