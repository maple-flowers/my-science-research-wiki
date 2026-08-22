---
tags: [concept, computing, electronics]
title: 存内计算 (In-Memory Computing)
type: concept
status: developing
domain: [computer-architecture, microelectronics, AI-hardware]
mechanism: 将计算逻辑直接集成到存储单元或存储阵列中，以消除冯·诺依曼架构下的“存储墙”瓶颈
related_concepts: [neuromorphic-computing, non-volatile-memory, memristor, crossbar-array]
papers: [chenHafniumBasedFerroelectricPostMoore2026, xueEmergingNonvolatileMemories2011, huangTwodimensionalIn2Se3Rising2022]
updated: 2026-08
---

# 存内计算 / In-Memory Computing (IMC)

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


存内计算是一种新型的计算范式，其核心思想是“在存储数据的地点直接完成计算”。它打破了传统冯·诺依曼架构中中央处理器 (CPU) 与存储器 (Memory) 分离的格局，通过在存储阵列内利用物理规律（如基尔霍夫电流定律和欧姆定律）执行运算，极大降低了数据搬移带来的能耗和延迟。

## 👵 太奶导读

> [!info]  Grandma 导读
> 好孩子，这“存内计算”其实就是让“仓库”自己会“算账”。现在的电脑像个勤快但脑子不灵光的搬运工，每次算账都得从仓库（内存）把沉重的账本搬到办公室（CPU），算完再搬回去，路上累得满头大汗还浪费时间（这就是存储墙）。
> 
> 咱这新技术呢，是直接在仓库的架子上装上算盘。账本不用动，架子上的机关（忆阻器、铁电器件）自己就能把加减乘除给办了。这样不仅省了搬运的力气（省电），算起账来也快得惊人。这对于现在那些需要算海量数据的活儿（比如人工智能），简直是救命的良方。

## 🏗️ 结构概览

存内计算主要依赖高密度的交叉阵列 (Crossbar Array) 结构实现。

![图：基于忆阻器/铁电阵列的存内计算 VMM 演示](../../raw/figures/chenHafniumBasedFerroelectricPostMoore2026/fig_9_6UW5JTH3.png)
*   **看图要点**：图中展示了利用器件阵列实现向量-矩阵乘法 (VMM) 的原理。输入信号以电压形式施加在字线上，利用电导代表矩阵权重，位线输出的总电流即为乘加运算的结果。
*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 核心优势与实现方式

### 解决“存储墙”问题
在 AI 任务中，数据搬移能耗往往占总能耗的 90% 以上。IMC 通过减少数据在总线上的往返，实现了能效比 (TOPS/W) 的数量级提升。

### 物理计算机制
*   **模拟域计算**：利用 $V_{in} \times G = I_{out}$（欧姆定律）和 $\sum I = I_{total}$（基尔霍夫定律）在模拟域内瞬间完成大规模并行乘加运算。
*   **逻辑存内计算**：利用存储单元状态的逻辑组合（如 MAGIC 或 FELIX 逻辑）实现布尔运算。

### 硬件载体
*   **RRAM/忆阻器**：电导连续可调，密度高。
*   **FeFET/FTJ**：基于铁电极化，读写速度快，CMOS 兼容性好。
*   **SRAM-IMC**：利用现有 SRAM 架构修改，技术最成熟但密度较低。

## 📚 相关论文 (Related Papers)

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：详细介绍了铪基铁电器件在神经网络推理加速和存内逻辑运算中的应用。
- [[../papers/xueEmergingNonvolatileMemories2011]]：从体系结构角度讨论了新兴存储器对存内计算的支撑作用。
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/neuromorphic-computing|神经形态计算]]
- [[../concepts/non-volatile-memory|非易失性存储器]]
- [[../concepts/memristor|忆阻器]]
- [[../concepts/crossbar-array|交叉阵列]]
- [[../entities/FeFET|FeFET]]
