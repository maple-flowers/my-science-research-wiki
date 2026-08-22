---
tags: [concept, computing, AI]
title: 突触权重 (Synaptic Weight)
type: concept
status: mature
domain: [neural-networks, neuromorphic-engineering, neuroscience]
mechanism: 在神经网络中，代表两个神经元之间连接强度的定量参数
related_concepts: [synaptic-plasticity, neuromorphic-computing, memristor, in-memory-computing]
papers: [chenHafniumBasedFerroelectricPostMoore2026]
updated: 2026-08
---

# 突触权重 / Synaptic Weight

突触权重是神经网络架构中的核心参数，它决定了前级神经元的信号（输入）对后级神经元状态的影响程度。在生物大脑中，权重对应于突触传递神经递质的效率；在硬件神经网络中，权重通常由电子器件（如忆阻器、铁电晶体管）的电导值来物理表达。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“突触权重”就是咱脑子里那根连接线的“粗细”。想象你有两个脑细胞在说话，中间连着一根管子。
> 
> 如果这根管子特别粗（权重高），前一个细胞一嚷嚷，后一个细胞马上就能听得清清楚楚，反应很大。如果这根管子特别细（权重低），前一个细胞喊破嗓子，后一个细胞可能也只是动动耳朵。咱们学习的过程，其实就是不断把重要的管子变粗、不重要的管子变细的过程。在现在的电脑芯片里，科学家们用电压来把这些“电子管子”调粗调细，这就是在帮机器学东西呢。

## 🏗️ 结构概览

在硬件集成中，突触权重通常以阵列形式排列，对应矩阵中的每一个元素。

![图：基于铁电电导调节的突触权重映射](../../raw/figures/chenHafniumBasedFerroelectricPostMoore2026/fig_8_49WAIQHG.png)
*   **看图要点**：图中展示了器件电导随脉冲数量的变化曲线。这种“电导-脉冲”响应的连续性和线性度，直接决定了突触权重调节的精度，是实现高准确率神经网络硬件的关键。
*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 物理实现与数学意义

### 物理映射
在存内计算阵列中，电导 $G$ 物理上等同于权重 $W$。根据欧姆定律，输出电流 $I = V \cdot G$，在数学上对应乘法运算 $y = x \cdot w$。

### 关键要求
1.  **多态性 (Multi-level States)**：权重需要具备足够多的离散或连续能级（通常要求 $\ge 32$ 级，即 5-bit 精度）。
2.  **对称性与线性度**：在权重增加（增强）和减少（抑制）的过程中，步长应尽量一致且呈线性，以便于算法训练收敛。
3.  **非易失性**：权重一旦设定，在断电后应能长期保持。

### 调节机制
*   **铁电材料**：通过改变铁电畴的反转比例来微调电导。
*   **阻变材料**：通过控制导电细丝的截面积或长度。

## 📚 相关论文 (Related Papers)

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：详细测试了铪基铁电器件作为突触权重单元的线性度和稳定性。

### ⚠️ 已撤回的引文

以下条目原列于本节，经核对其 `raw/note` 原始笔记后确认无据，于 2026-08-21 撤回：

- `xueEmergingNonvolatileMemories2011`：原文笔记中无 synapse/突触相关内容。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/synaptic-plasticity|突触可塑性]]
- [[../concepts/neuromorphic-computing|神经形态计算]]
- [[../concepts/memristor|忆阻器]]
- [[../concepts/in-memory-computing|存内计算]]
- [[../entities/FeFET|FeFET]]
