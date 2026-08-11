---
tags: [entity]
---

# 1T-TaS₂ (二硫化钽)

1T-TaS₂ 是过渡金属硫族化合物 (TMDs) 家族中物理内涵最为丰富的体系之一，被视为研究强关联电子态、电荷密度波 (CDW) 与莫特 (Mott) 绝缘相竞争的原型材料。其核心物理特性源于对称性破缺诱导的晶格重构以及由此锁定的层间相互作用。

## 核心机制：大卫之星与莫特物理

1T-TaS₂ 的基态特性由 $\sqrt{13} \times \sqrt{13}$ R13.9° 的电荷密度波超结构定义。在每一层内，13 个 Ta 原子发生向心位移，形成所谓的**“大卫之星” (Star-of-David)** 团簇。这种周期性晶格畸变 (PLD) 导致能带的剧烈重整：13 个原子提供的 13 个 $5d$ 电子中，12 个被填入由畸变形成的深能级带，剩下的 1 个电子占据费米能级附近的一条极窄能带。

由于这条能带的带宽 $W$ 被极度压窄，即使在中等的在位库仑排斥 $U$ 作用下，体系也会跨越 Mott 准则 ($U/W > 1$)，打开莫特-哈伯德能隙，转变为**莫特绝缘体**。[[../papers/nakataRobustChargedensityWave2021]] 通过对比 Ta 和 Nb 体系证明，决定该莫特相稳定性的主导因素并非单纯的电子关联强度，而是 CDW 晶格畸变对带宽 $W$ 的有效压制。

## 相位锁定与层间堆叠

1T-TaS₂ 的金属性对维度和层间耦合高度敏感。在块体材料中，层间 CDW 的相位锁定方式（堆叠序）决定了体系的输运性质。[[../papers/cossuStackingChargedensityWaves2024]] 指出，1T 型 TMDs 中层间 CDW 的特定堆叠排列足以驱动金属-绝缘体转变，这揭示了层间耦合作为一个非平庸的物理自由度，通过改变化学键合的“相位相干性”来锁定电子态。

## 相变路径与拓扑缺陷

该体系表现出复杂的相变序列：
1. **公度 CDW (C-CDW)**：低温下的完全绝缘态，大卫之星呈长程有序排列。
2. **近公度 CDW (NCCDW)**：室温附近的典型相，由公度畴和**非公度畴壁 (Discommensurations, DCs)** 组成的网络构成。[[../papers/kimObservationPhaseTransition1997]] 利用 STM 证实了该相的超结构，并展示了通过针尖诱导电压脉冲实现从 1T 到 2H 相的原子级共格滑移相变。
3. **超导性 (SC)**：当通过压力或掺杂抑制 C-CDW 序时，超导穹顶往往会在 C-IC 转变的临界区涌现。[[../papers/Chen2019superconductivity]] 提出了一个唯象框架，认为近公度相中 DC 网络的涨落是驱动超导成核的关键，预言超导电性首先在畴壁处成核并经历渗流转变。

## 技术应用价值

由于 1T-TaS₂ 的 CDW-莫特转变具有超快响应速度和显著的电阻变化，它在高性能电子开关、类脑计算以及室温莫特器件中具有巨大的应用潜力。通过调控层数（减薄至单层可增强有效 $U/W$）或施加外部扰动（如光激发、载流子注入），可以实现对该体系“锁定”属性的动态解耦与重构。

## Related Papers

- [[../papers/cossuStackingChargedensityWaves2024]] (层间堆叠与 CDW 耦合)
- [[../papers/kimObservationPhaseTransition1997]] (STM 针尖诱导相变与 NCCDW 观测)
- [[../papers/nakataRobustChargedensityWave2021]] (单层极限下的鲁棒莫特相)
- [[../papers/Chen2019superconductivity]] (非公度畴壁驱动的超导电性)
- [[../papers/nakataRobustChargedensityWave2021]] (电子关联与带宽控制)
