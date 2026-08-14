---
tags: [concept, plasmonics, spectroscopy]
title: 表面等离子体共振 / Surface Plasmon Resonance (SPR)
type: concept
status: mature
domain: [plasmonics, biosensing, optics]
mechanism: 入射光子与金属表面自由电子气集体振荡发生共振耦合，形成沿界面传播的电磁波（表面等离极化激元）
related_concepts: [exciton-plasmon-coupling, local-dielectric-environment, localized-surface-plasmon-resonance, biosensing]
papers: [duUltrasensitiveOptoelectronicBiosensor2025]
updated: 2026-08
---

# 表面等离子体共振 / Surface Plasmon Resonance (SPR)

表面等离子体共振（Surface Plasmon Resonance, SPR）是一种发生在金属与介质界面的光学现象。当入射光的动量与金属表面自由电子气的集体振荡动量相匹配时，光子能量被转化为金属表面的电子集体振荡能量，形成一种高度局域化的电磁场。

## 👵 太奶导读

太奶啊，这就好比是**“金属表面的一场集体大合唱”**。咱们把光照在金属片（通常是金或银）上，如果这光的频率正好对上了金属里电子们排队的节奏，那些电子就会齐刷刷地跟着光一起跳起舞来（集体振荡）。这种“舞会”紧贴着金属表面，对周围的环境极其敏感。只要金属表面落了一点儿灰尘或者吸附了一个微小的生物分子，电子们的舞步节奏（共振频率）就会立刻乱掉。咱们只要盯着这个节奏的变化，就能发现那些连显微镜都看不清的微小分子。

## 🏗️ 物理分类与特征

1.  **传播型 SPR (Propagating SPR)**：发生在平整金属薄膜表面，电磁波（表面等离极化激元）沿界面传播。
2.  **局域型 SPR (Localized SPR, LSPR)**：发生在金属纳米颗粒（如金纳米盘、纳米颗粒）中。由于尺寸受限，电子振荡被限制在纳米结构内部，产生极强的**电磁场热点 (Hotspots)**。
    *   **tBLG 传感器案例**：利用周期为 274 nm、厚度为 50 nm 的金纳米盘阵列产生的 LSPR，与扭曲双层石墨烯的范霍夫奇点吸收精确耦合，极大地增强了光响应度 [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]。

## 🧩 激子-等离激元耦合 (Exciton–Plasmon Coupling)

这是 SPR 在先进光电器件中的高端玩法。
*   **物理实质**：当材料（如二维材料）的激子（或 VHS 吸收峰）与金属纳米结构的 LSPR 峰在能量上对齐时，两者会发生强相互作用。
*   **效应**：这种耦合不仅能增强光电流（增强约 7 倍），还能缩短载流子的弛豫时间（从 1.14 ps 缩短至 371 fs），显著提高探测效率 [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]。

## 🔬 应用：超灵敏生物传感

由于 SPR 产生的热点对周围**局域介电环境 (Local Dielectric Environment)** 极其敏感，它被广泛用于：
*   **免标记检测**：直接观察分子结合引起的折射率变化。
*   **CRISPR 集成**：利用 CRISPR-Cas12a 酶的切割活性来控制金纳米颗粒与界面的距离，从而动态调制 SPR 信号，实现亚飞摩尔级的核酸检测。

## 📚 相关论文 (Related Papers)

- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]：将 LSPR 与转角石墨烯的 VHS 耦合，构建了超灵敏的光电生物传感器。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/van-hove-singularity|范霍夫奇点 (VHS)]]
- [[../concepts/exciton-plasmon-coupling|激子-等离激元耦合]]
- [[../entities/gold-nanodisks|金纳米盘]]
- [[../entities/twisted-bilayer-graphene|扭曲双层石墨烯]]
