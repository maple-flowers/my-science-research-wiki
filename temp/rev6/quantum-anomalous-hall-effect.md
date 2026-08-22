---
tags: [concept, topological-physics, quantum-hall, spintronics]
title: 量子反常霍尔效应 / Quantum Anomalous Hall Effect (QAHE)
type: concept
status: mature
year: 2025
domain: [condensed-matter-physics, topological-physics, spintronics]
mechanism: 磁有序 + 强自旋-轨道耦合在零外磁场下打开拓扑非平庸能隙，产生量子化的反常霍尔电导 e²/h
related_concepts: [anomalous-hall-effect, chern-number, berry-curvature, topological-insulator, quantum-spin-hall-effect, sliding-ferroelectricity, multiferroicity, magnetoelectric-coupling, spin-orbit-coupling, altermagnetism, 2d-materials, topological-charge]
papers: [kaurRecentAdvancesTheoretical2025a, wangTunableD0Topological2025b, hanPolarTopologicalMaterials2025]
updated: 2026-08-19
---

# 量子反常霍尔效应 / Quantum Anomalous Hall Effect (QAHE)

量子反常霍尔效应 (QAHE) 是指在没有外磁场的情况下，磁性拓扑绝缘体中仅由内禀磁有序与自旋-轨道耦合（SOC）即可实现陈数 $C=1$ 的拓扑非平庸态，其霍尔电导被精确量子化为 $\sigma_{xy} = C e^2/h$。它是反常霍尔效应的量子化版本，也是无耗散边缘态输运的标志。

## 👵 太奶导读

乖孙，这一条讲的是「量子反常霍尔效应」。普通霍尔效应要用个大磁铁把电子往旁边推；而"反常"霍尔效应，材料自己身上的磁性就能当那个"磁铁"；再往上加一个"量子"二字，意思是霍尔电导被钉死在一个精确的数值上——像用卡尺量出来的一样，一份就是 $e^2/h$，不多不少。在滑动铁电这类二维材料里，科学家甚至打算用**电压**（而不是磁场）来把这种拓扑量子态"开关"——一翻极化，量子反常霍尔就出现或消失。一句话：**"不用磁铁、霍尔电阻还能量子化，而且能用电压来开关"**。

## 🏗️ 结构概览

量子反常霍尔效应要求体系同时具备磁性、强自旋-轨道耦合和拓扑非平庸的能带结构；在滑动铁电体系中，层间极化可对这一拓扑量子态进行非易失电控。

## 🧩 核心机制：磁性 + SOC 如何产生量子化霍尔电导

### 1. 从反常霍尔到量子反常霍尔

- **反常霍尔效应 (AHE)**：磁化强度提供内禀横向力（贝里曲率），霍尔电导随磁化强度演化，但数值连续、可带耗散。
- **QAHE**：当体系处于拓扑绝缘体基态且磁性打开交换能隙时，贝里曲率在布里渊区的积分取整数值 $C$，霍尔电导被量子化为 $C e^2/h$，边缘态成为无耗散的手性导电通道。

### 2. 滑动铁电中的电控 QAHE

- 层间滑移产生面外极化 $P$，打破空间反演对称性，可调控磁性层与拓扑层的电子结构。
- 理论计算表明，在特定范德华异质结/多层膜中，翻转极化可在 QAHE 态与普通绝缘态（或平庸金属态）之间切换，实现"电压驱动的量子相变"。
- 该路径绕开了传统 QAHE 依赖磁性掺杂均匀性、低温等苛刻条件，为室温可开关拓扑量子器件提供候选。

## 📋 关键参数表

| 参数 | 含义 | 典型值/要求 |
|---|---|---|
| 陈数 $C$ | 布里渊区贝里曲率积分 | $\pm 1$（量子化） |
| 霍尔电导 $\sigma_{xy}$ | 横向电导 | $C e^2/h$ |
| 交换能隙 | 磁性打开拓扑能隙 | 需大于热涨落（mK–K 量级） |
| SOC 强度 | 自旋-轨道耦合 | 需强到翻转能带拓扑 |
| 极化翻转 | 电控开关手段 | 滑动铁电层间滑移 |

## 🔀 近邻概念辨析

- **QAHE vs 量子自旋霍尔效应 (QSHE)**：QSHE 靠时间反演对称保护、自旋分辨边缘态、陈数为零；QAHE 靠磁性破缺时间反演对称，产生手性单通道边缘态、陈数非零。
- **QAHE vs 反常霍尔效应**：前者是量子化、零耗散的拓扑效应；后者是连续、可耗散的半经典效应。

## 📚 相关论文 (Related Papers)

- [[../papers/kaurRecentAdvancesTheoretical2025a]]：综述滑动铁电与磁性、拓扑耦合，提出电控量子反常霍尔效应的理论路线。
- [[../papers/wangTunableD0Topological2025b]]：d0 磁性多铁单层中可调拓扑磁态与陈数变化的机制研究。
- [[../papers/hanPolarTopologicalMaterials2025]]：极性拓扑材料综述，覆盖拓扑态与极化序耦合的器件前景。

## 🔗 关联概念与实体 (Related)

- [[../concepts/anomalous-hall-effect|anomalous-hall-effect]]
- [[../concepts/chern-number|chern-number]]
- [[../concepts/berry-curvature|berry-curvature]]
- [[../concepts/topological-insulator|topological-insulator]]
- [[../concepts/quantum-spin-hall-effect|quantum-spin-hall-effect]]
- [[../concepts/sliding-ferroelectricity|sliding-ferroelectricity]]
- [[../concepts/multiferroicity|multiferroicity]]
- [[../concepts/magnetoelectric-coupling|magnetoelectric-coupling]]
- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/altermagnetism|altermagnetism]]
- [[../entities/h-BN|h-BN]]
- [[../entities/MnBi2Te4|MnBi2Te4]]
