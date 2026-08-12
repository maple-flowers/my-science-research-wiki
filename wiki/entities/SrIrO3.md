---
tags: [entity, material, half-metal, 2D, strain-engineering, transition-metal-oxide, phase-interlocked]
category: [D01, Z02]
---

# 铱酸锶 / Strontium Iridate (SrIrO3)

**SrIrO3** 是一种具有强自旋轨道耦合 (SOC) 的 5d 过渡金属氧化物。在二维极限下，单层 SrIrO3 展现出显著的应变诱导**相锁定 (Phase-interlocked)** 特性，能够实现从反铁磁 (AFM) 半导体到铁磁 (FM) 半金属的非易失性、超快切换 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。

## 1. 相锁定物理机制 (Phase-interlocked Mechanism)
单层 SrIrO3 的电子态与晶格几何高度耦合，其相锁定特性源于 **IrO₅ 五面体网络** 的协同重排：
- **$Pc$ 相 (基态)**：表现为反铁磁 (AFM) 半导体，其磁序与空间反演对称性破缺锁定。
- **应变诱导相变**：施加约 **3.5%** 的 $a$ 轴压缩应变，可驱动材料向 **$P4bm$ 对称性** 转变。
- **结构-磁-电协同**：在 $P4bm$ 相下，自旋向下通道的带隙闭合，而自旋向上通道的带隙拓宽至 **3.58 eV**，实现 **100% 自旋极化 (半金属性)**。

## 2. 自旋电子学特性 (Spintronic Properties)
- **巨自旋劈裂 (Giant Spin Splitting)**：受 Ir 原子强 SOC 效应及 p-d 轨道强杂化驱动，其能带边缘的自旋劈裂能量超过 **0.2 eV** [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。
- **超快响应**：根据 Arrhenius 动力学估算，该序-序相变响应时间在 **21–232 fs** 量级，跨入飞秒尺度，远快于传统电荷驱动的 CMOS 开关。
- **超低功耗潜力**：单次开关能耗估计在 $10^{-3}$ fJ 量级，为开发非易失性相控自旋逻辑器件提供了材料基础。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **磁转变温度 ($T_N$)** | $135\text{ K}$ | 反铁磁序 (单层) |
| **带隙 ($E_g, Pc$)** | $1.14\text{ eV} / 1.35\text{ eV}$ | 自旋上/下通道 |
| **带隙 ($E_g, P4bm$)** | $0\text{ / }3.58\text{ eV}$ | 半金属态 (Spin-down metallic) |
| **临界应变** | $a$ 轴压缩 $3.5\%$ | 驱动相变阈值 |
| **自旋极化率** | $100\%$ | 铁磁相下 (Half-metal) |

## 4. 本库相关代表性论文
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：npj Comp. Mater. 2025，提出“键密度+结合强度”判据实现非范德华 SrIrO3 单层的理论剥离，并揭示了微应变下的相锁定自旋极化调控机制。

## 5. 关联概念与实体
- [[../concepts/2D-materials|二维材料 2D Materials]]
- [[../concepts/phase-interlocked|相锁定 Phase-interlocked]]
- [[../concepts/strain-engineering|应变工程 Strain Engineering]]
- [[../concepts/half-metal|半金属 Half-metal]]
- [[SrOsO3|钌酸锶 SrOsO3]]
- [[SrMoO3|钼酸锶 SrMoO3]]
- [[BiFeO3|铁酸铋 BiFeO3]]
