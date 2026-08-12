---
tags: [entity, material, 2D, non-vdW, oxide]
category: [D01, Z02]
---

# 锌酸钠 / Sodium Zincate (NaZnO3)

**NaZnO3** 是一种钙钛矿氧化物材料。在 2025 年的高通量剥离研究中，它被识别为最具剥离潜力的非范德华三元氧化物单层之一 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]。

## 1. 极低剥离能 (Ultra-low Exfoliation Energy)
在 Zhong 等人筛选的 831 种 $ABO_3$ 化合物中，NaZnO3 展现出极其优异的剥离特性：
- **剥离能 ($E_{exf}$)**：预测值为 **$0.049\text{ eV/\text{\AA}}^2$**。
- **对比**：这一数值为筛选名单中的最低值，已接近典型范德华材料的量级（如石墨烯 $0.013$、MoS₂ $0.019\text{ eV/\text{\AA}}^2$）。
- **判据验证**：其同时满足低键密度 ($\rho \le 0.3$) 与面外结合强度小于面内的判据 ($\xi_\perp < \xi_\parallel$)。

## 2. 结构与稳定性
- **稳定性**：通过第一性原理分子动力学（AIMD）和声子谱分析，NaZnO3 单层在二维极限下表现出良好的动力学和热力学稳定性，能够在 300 K 下保持结构完整。
- **制备潜力**：极低的剥离能意味着 NaZnO3 单层在实验上极易通过机械剥离或液相剥离方法从其块体中获得。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **剥离能 ($E_{exf}$)** | $0.049\text{ eV/\text{\AA}}^2$ | 全库最低值之一 |
| **键密度 ($\rho$)** | $\le 0.3\text{ bonds/\text{\AA}}^2$ | 易剥离判据 |
| **维度** | 2D (Monolayer) | 原子级薄层 |
| **材料类别** | $ABO_3$ 氧化物 | 非范德华前驱体 |

## 4. 本库相关代表性论文
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：npj Comp. Mater. 2025，二维非范德华多铁单层的高通量剥离与相调控研究。

## 5. 关联概念与实体
- [[../concepts/non-vdw-exfoliation|非范德华剥离 Non-vdw Exfoliation]]
- [[../concepts/binding-strength|结合强度 Binding Strength]]
- [[MnVO3|偏钒酸锰 MnVO3]]
- [[ZnO|氧化锌 ZnO]]
