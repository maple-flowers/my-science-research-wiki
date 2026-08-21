---
tags: [concept, superconductivity, disorder, percolation]
title: '超导渗流 / Superconducting Percolation'
type: concept
status: mature
domain: [condensed-matter-physics, superconductivity, disorder]
mechanism: 无序体系中超导区域随掺杂/无序度增加而连通，宏观超导在逾渗阈值处涌现
related_concepts: [superconductivity, charge-density-wave, order-parameter, quantum-critical-point]
papers: ['Chen2019superconductivity', 'Koley2020charge']
updated: 2026-08
---

# 超导渗流 / Superconducting Percolation

超导渗流（superconducting percolation）指在**无序或相分离体系**中，超导区域（微米/纳米尺度岛）随掺杂、压力或温度变化而逐步连通，当超导占比超过逾渗阈值 $p_c$ 时，宏观电阻突然降为零、体系呈现整体超导的现象。它与"均匀 BCS 超导"不同：超导性先在局域"液滴"中出现，再经约瑟夫森耦合在空间上"连通成网"。

## 👵 太奶导读

太奶啊，这就像一块田里先长出几棵"超导苗"（零电阻的小岛），苗太少时电流还得从没超导的地方绕，还是有电阻。等苗多到连成片、把整块田都连起来了，电流就能全程"零摩擦"地跑，这就是"渗流"——像水渗过沙子一样，只有连成通路才有好戏。

## 🏗️ 物理机制

*   **逾渗阈值**：二维体系逾渗阈值约为 $p_c \approx 0.5$（键逾渗约 0.347/座逾渗约 0.593 依模型而异），超过阈值后超导岛形成贯穿整个体系的连通集团。
*   **约瑟夫森网络**：孤立超导岛之间通过弱连接（隧穿/近邻效应）耦合，整体超导由约瑟夫森结网络的凝聚决定；临界电流与连接强度、相位相干相关。
*   **临界指数**：在阈值附近，超导刚度/临界电流以幂律 $I_c \propto (p-p_c)^\nu$ 趋于零，体现渗流普适类。
*   **脆性超导**：由渗流产生的超导常表现为"脆性"（brittle）——临界电流远低于均匀超导、对微弱扰动敏感，区别于本征超导。

## 🧩 具体体系实例

*   **TMD 合金中的无序释放超导**：在 TaSe₂₋ₓSₓ 等体系中，非磁性团簇无序破坏长程 CDW 相干，释放被压制的 s 波超导；超导随组分出现"重入-增强"行为，与超导区域渗流连通图景一致 [[../papers/Koley2020charge]]。
*   **1T-TiSe₂ 的 CDW/SC 转变**：公度-近公度-非公度 CDW 相变与超导涌现耦合，超导在 CDW 被抑制的区域（渗流通道）形成 [[../papers/Chen2019superconductivity]]。
*   **颗粒超导薄膜**：金属-绝缘体转变附近的颗粒膜，超导渗流与[[../concepts/order-parameter|序参量]]相位刚度共同决定宏观响应。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/charge-density-wave|电荷密度波]]：超导的竞争者/宿主。
- [[../concepts/order-parameter|序参量]]：超导序的空间分布。
- [[../concepts/quantum-critical-point|量子临界点]]：无序体系中的量子相变框架。
- [[../entities/TiSe2|TiSe₂]]、[[../entities/TaSe2|TaSe₂]]：渗流型超导研究体系。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2019superconductivity]] — 1T-TiSe₂ 中 CDW 相与超导涌现行为
- [[../papers/Koley2020charge]] — 无序释放 TMD 中被压制的超导
