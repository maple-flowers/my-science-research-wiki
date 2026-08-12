---
tags: [entity, material, antiferromagnetic, 2D, strain-engineering, oxide]
category: [D01, Z02]
---

# 钼酸锶 / Strontium Molybdate (SrMoO3)

**SrMoO3** 是一种钙钛矿氧化物材料。在二维极限下，单层 SrMoO3 被预测为一种具有高 Néel 温度（$T_N \approx 315\text{ K}$）的二维反铁磁材料，其电子态可以通过应变诱导的相变在半导体和自旋极化金属之间切换 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。

## 1. 高温反铁磁性 (High-Temperature Antiferromagnetism)
在筛选出的 35 种稳定 $ABO_3$ 单层中，SrMoO3 展现出最高的磁转变温度：
- **磁基态**：表现为 Néel 型反铁磁（AFM）序。
- **转变温度**：预测的 Néel 温度 **$T_N = 315\text{ K}$**，超过了室温，这使其在常温自旋电子器件应用中极具潜力。
- **物理起源**：源于强的层内超交换相互作用（Super-exchange），磁性原子（Mo）通过氧桥介导磁耦合。

## 2. 相锁定切换 (Phase-interlocked Switching)
单层 SrMoO3 的电子结构与晶格对称性高度锁定 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：
- **相变路径**：$P4mm \text{ (AFM)} \leftrightarrow Pc \text{ (AFM)}$。
- **电子态演化**：
    - **$P4mm$ 相**：表现为窄带隙半导体特性（带隙 $E_g \approx 0.19\text{ eV}$）。
    - **$Pc$ 相**：转变为自旋极化金属态，自旋向下的通道穿过费米面，而自旋向上的通道保持带隙（$0.304\text{ eV}$）。
- **应变调控**：通过非对称应变（$a$ 轴拉伸 $0.7\%$，$b$ 轴压缩 $2.7\%$）可驱动该相变，实现导电性的“开关”控制。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **Néel 温度 ($T_N$)** | $315\text{ K}$ | 高于室温 |
| **磁矩 (Mo)** | $1.386\text{ \mu_B}$ | 局域磁矩 |
| **带隙 ($E_g$)** | $0.19\text{ eV}$ | $P4mm$ 相半导体 |
| **自旋极化率** | $100\%$ | $Pc$ 金属相下 |
| **开关能耗** | $\sim 4.9 \times 10^{-3}\text{ fJ}$ | 超低功耗器件 |

## 4. 本库相关代表性论文
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：npj Comp. Mater. 2025，二维非范德华多铁单层的高通量剥离与相调控研究。

## 5. 关联概念与实体
- [[../concepts/superexchange|超交换 Superexchange]]
- [[../concepts/phase-interlocked|相锁定 Phase-interlocked]]
- [[SrOsO3|钌酸锶 SrOsO3]]
- [[SrIrO3|铱酸锶 SrIrO3]]
