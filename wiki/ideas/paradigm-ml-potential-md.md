---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_0b5a5178989d11f19467525400287e28
    ReservedCode1: guwLmf8N/wrEUTkpIHMWSyC8khXos9eeO0JgcqROQiZLb6AN9lPojO8lWTrNRQUU7NleBukSz98bkByoGVpY5OU5kkcNmQ5kwIcBdPUOcukk2KNoVo/wdNtWmE0VcWvU05tVTWje5Pi4bNj6oCMwLzonnD5vsl5AMEnd+BQNeX+y3/2CJXZ9CVDTOMI=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_0b5a5178989d11f19467525400287e28
    ReservedCode2: guwLmf8N/wrEUTkpIHMWSyC8khXos9eeO0JgcqROQiZLb6AN9lPojO8lWTrNRQUU7NleBukSz98bkByoGVpY5OU5kkcNmQ5kwIcBdPUOcukk2KNoVo/wdNtWmE0VcWvU05tVTWje5Pi4bNj6oCMwLzonnD5vsl5AMEnd+BQNeX+y3/2CJXZ9CVDTOMI=
---



# 机器学习势与大规模分子动力学模拟 / Machine-Learning Potentials & Large-Scale MD

> 科研范式 P04：像"请一位学得很快的学徒"——先用 DFT 教它几千个例子，让它学会"看原子就知道能量和力"，然后放手让它去模拟百万原子的大场面。

## 👵 太奶导读

DFT 算得准但太慢，只能算几百个原子；分子动力学想模拟大体系，又缺一把"又快又准"的力。机器学习势就是折中方案：先用 DFT 生成一批"标准答案"训练神经网络，让它学会预测原子间的力，然后就能用它模拟几万、几十万个原子的运动，看铁电怎么翻转、相怎么变化。相当于请了个"速算学徒"，学得快、算得快，还基本准。

## 🧭 范式概述

这个范式的核心逻辑是：**用机器学习势（MLP）替代 DFT 做大规模分子动力学，在保持精度的同时跨越尺度鸿沟**。研究对象是滑移铁电、铁电拓扑结构、铁性相变等动力学过程。总体思路是：先用 DFT 生成覆盖构型空间的训练集，训练并验证 MLP（能量/力误差达标），再用 MLP 跑大规模 MD，分析翻转动力学、相变路径、拓扑缺陷演化等，最后归纳机理。这样设计的原因在于：铁电翻转、相变等过程涉及大尺度、长时间演化，DFT 无法直接覆盖，而 MLP 提供了精度与尺度的平衡。例如 [[../papers/heUltrafastSwitchingDynamics2024]] 用 MLP-MD 揭示超快铁电翻转动力学，[[../papers/xuTunableFerroelectricTopological2022]] 用 MLP-MD 模拟应变调控的拓扑缺陷，[[../papers/yangRipplingFerroicPhase2021]] 用 MLP-MD 研究铁性相变中的涟漪效应。

## 🔁 研究流程

1. **训练集构建**：用 DFT 采样构型空间（含基态、过渡态、高温构型），生成能量/力标签。
2. **MLP 训练与验证**：训练神经网络势，用独立测试集验证能量/力误差与稳定性。
3. **大规模 MD 模拟**：用 MLP 跑数万至百万原子、纳秒级 MD，模拟翻转/相变/缺陷演化。
4. **动力学分析**：提取翻转路径、时间尺度、相变温度、拓扑缺陷运动等。
5. **机理归纳**：将模拟结果与实验/理论对照，给出动力学机理。

## 🛠️ 核心方法与工具

- **机器学习势**：神经网络/高斯过程势，拟合 DFT 能量面（[[../papers/heUltrafastSwitchingDynamics2024]]）。
- **大规模 MD**：NPT/NVT 系综，模拟相变与翻转（[[../papers/yangRipplingFerroicPhase2021]]）。
- **应变/电场调控**：在 MD 中施加外场研究响应（[[../papers/xuTunableFerroelectricTopological2022]]）。
- **DFT 验证**：关键构型用 DFT 复核 MLP 结果（[[../papers/Mińkowski2021cation]]）。

## ✅ 适用条件

- 需要模拟的体系/过程超出 DFT 尺度（>1000 原子或 >ps 时间）。
- 有足够 DFT 数据训练可靠 MLP，且目标性质在训练集覆盖范围内。
- 关注动力学、相变、缺陷等"过程性"问题。

## ⚠️ 局限与风险

- MLP 外推能力有限：训练集未覆盖的构型可能给出错误结果。
- 训练集构建成本高，需精心采样。
- 精度依赖 DFT 标签质量，强关联体系需谨慎。
- 长时模拟的累积误差可能放大。

## 📚 代表论文 (Representative Papers)

- [[../papers/heUltrafastSwitchingDynamics2024]]：MLP-MD 揭示超快铁电翻转动力学。
- [[../papers/xuTunableFerroelectricTopological2022]]：MLP-MD 模拟应变调控铁电拓扑缺陷。
- [[../papers/yangRipplingFerroicPhase2021]]：MLP-MD 研究铁性相变涟漪效应。
- [[../papers/heSwitchingTwodimensionalSliding2025]]：MLP-MD 研究二维滑移铁电切换。

## 🗂️ 覆盖论文全集 (All Covered Papers)

- [[../papers/heSwitchingTwodimensionalSliding2025]]
- [[../papers/heUltrafastSwitchingDynamics2024]]
- [[../papers/Mińkowski2021cation]]
- [[../papers/yangRipplingFerroicPhase2021]]
- [[../papers/xuTunableFerroelectricTopological2022]]

## 🔗 关联概念、实体与主题 (Related Concepts, Entities & Topics)

- [[../concepts/machine-learning-potential|机器学习势]]
- [[../concepts/molecular-dynamics|分子动力学]]
- [[../concepts/sliding-ferroelectricity|滑移铁电]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/topological-insulator|拓扑绝缘体]]
- [[../entities/In2Se3|In₂Se₃]]
- [[../topics/材料模拟计算设计|材料模拟计算设计]]
- [[../topics/多铁性材料|多铁性材料]]

## 📈 生命周期日志

- **2026-08-15**: active — 提炼自 5 篇机器学习势 + 大规模分子动力学类论文。
*（内容由AI生成，仅供参考）*
