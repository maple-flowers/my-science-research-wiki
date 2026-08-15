---
tags: [paradigm, high-throughput, data-driven, dft, multiferroic]
title: 高通量筛选与数据驱动材料发现 / High-Throughput Screening & Data-Driven Discovery
type: paradigm
status: active
paradigm_id: P02
domain: [computational-physics, materials-informatics]
core_question: 面对成千上万个候选材料，如何用统一判据批量计算并快速捞出最可能成功的少数几个？
method_pipeline: 数据库构建→批量 DFT→统一判据过滤→精算复核（蒙特卡洛/剥离能）→候选清单
related_concepts: [high-throughput-screening, density-functional-theory, multiferroicity, sliding-ferroelectricity]
related_topics: [Z01-computational-materials-design, D02-multiferroic-materials]
papers: [fengFerroelectricityMultiferroicityTwodimensional2020, zhongHighthroughputExfoliationMultiferroic2025, yanDecipheringStabilityTwodimensional2025, zhaoRealization2DMultiferroic2024]
updated: 2026-08
---

# 高通量筛选与数据驱动材料发现 / High-Throughput Screening & Data-Driven Discovery

> 科研范式 P02：像"大海捞针"一样，把成千上万种候选材料批量算一遍，用统一判据快速捞出最可能成功的几根"针"。

## 👵 太奶导读

想象你要在几千种布料里找一种既防水又透气的，你不会一件件手工试，而是先按"防水"和"透气"两个指标批量测试，快速淘汰大部分，再对剩下的仔细研究。高通量筛选就是这个思路：把大量候选材料放进计算机里批量计算，用统一标准（稳不稳定、有没有铁电/磁性）快速过滤，最后锁定少数最有希望的材料，甚至用机器学习总结出"什么样的结构容易成功"的规律。

## 🧭 范式概述

这个范式的核心逻辑是：**以"批量计算 + 统一判据 + 数据归纳"替代"单点试错"**。研究对象是二维多铁、可剥离层状材料等候选家族。总体思路是：先构建大规模候选结构库，用高通量 DFT 计算稳定性与目标性质，用可量化判据（形成能、剥离能、极化、磁序）逐级过滤，最后用聚类/机器学习从幸存者中提炼设计规则。这样设计的原因在于：候选空间动辄数千，人工逐个研究不现实，只有批量流水线才能覆盖全局。例如 [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] 基于 C2DB 数据库筛选二维多铁，[[../papers/zhongHighthroughputExfoliationMultiferroic2025]] 用剥离判据高通量筛选可剥离多铁单层，[[../papers/yanDecipheringStabilityTwodimensional2025]] 用 DBSCAN 聚类提炼"积木规则"。

## 🔁 研究流程

1. **候选空间构建**：从数据库（如 C2DB）或结构枚举生成大规模候选材料库。
2. **高通量 DFT 计算**：批量做结构优化与稳定性计算，产出统一格式的数据。
3. **判据过滤**：用形成能、剥离能、声子稳定性、极化/磁序等硬判据逐级筛除不合格候选。
4. **机器学习聚类**：对幸存者做聚类/分类，提炼结构—性质关联与设计规则。
5. **目标推荐**：输出最有潜力的材料清单与可解释判据，供实验或深入计算验证。

## 🛠️ 核心方法与工具

- **高通量计算框架**：批量 DFT 流水线（[[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]）。
- **剥离能判据**：评估层状材料可剥离性（[[../papers/zhongHighthroughputExfoliationMultiferroic2025]]）。
- **蒙特卡洛**：估算磁/铁电转变温度（[[../papers/zhaoRealization2DMultiferroic2024]]）。
- **DBSCAN 聚类**：从数据中提炼结构"积木规则"（[[../papers/yanDecipheringStabilityTwodimensional2025]]）。

## ✅ 适用条件

- 存在明确的候选空间（数据库、结构枚举）与可量化的筛选判据。
- 计算量可批量并行，单点成本可控。
- 目标性质可用统一计算协议评估（稳定性、极化、磁序等）。

## ⚠️ 局限与风险

- 判据选择决定结果：判据过松则幸存者过多，过紧则漏掉"意外之喜"。
- 高通量计算精度受泛函限制，强关联体系需谨慎。
- 筛选出的材料仍需实验验证，存在"算得出、做不出"的风险。
- 数据质量依赖输入库的完整性与准确性。

## 📚 代表论文 (Representative Papers)

- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]：基于 C2DB 高通量筛选二维多铁，展示"筛选—DFT—蒙特卡洛"流水线。
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：用剥离判据高通量筛选可剥离多铁单层。
- [[../papers/yanDecipheringStabilityTwodimensional2025]]：高通量 DFT + DBSCAN 提炼材料设计"积木规则"。
- [[../papers/zhaoRealization2DMultiferroic2024]]：高通量 DFT + 蒙特卡洛筛选插层多铁。

## 🗂️ 覆盖论文全集 (All Covered Papers)

- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]
- [[../papers/yanDecipheringStabilityTwodimensional2025]]
- [[../papers/zhaoRealization2DMultiferroic2024]]
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

## 🔗 关联概念、实体与主题 (Related Concepts, Entities & Topics)

- [[../concepts/high-throughput-screening|高通量筛选]]
- [[../concepts/density-functional-theory|密度泛函理论]]
- [[../concepts/multiferroicity|多铁性]]
- [[../concepts/sliding-ferroelectricity|滑移铁电]]
- [[../topics/Z01-computational-materials-design|材料模拟计算设计]]
- [[../topics/D02-multiferroic-materials|多铁性材料]]

## 📈 生命周期日志

- **2026-08-15**: active — 提炼自 4 篇高通量筛选/数据驱动材料发现类论文。
