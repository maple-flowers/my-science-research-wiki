---
tags: [entity, material, ferroelectric, oxide, fluorite-structure, cmos-compatible]
category: [D02, Z01]
---

# 氧化铪 / Hafnium Oxide (HfO2)

**HfO2** 是一种具有萤石结构的二元氧化物。它不仅是现代半导体工业中标准的高-$k$ 栅介质材料，更因其在超薄尺度下展现出的稳健铁电性，成为**后摩尔时代**铁电电子学的核心候选材料。

## 1. 铁电性的本征起源
- **亚稳极性相**：HfO2 的铁电性并非源于其热力学稳定的单斜相（$m$-phase, $P2_1/c$），而是源于**亚稳态的极性正交相 ($o$-phase, $Pca2_1$)** [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。
- **无标度铁电性 (Scale-free Ferroelectricity)**：第一性原理发现其具有极性声子平带，这使得 HfO2 理论上不存在铁电临界厚度，在低至 **$1\text{ nm}$** 时仍能保持极化翻转能力 [[../papers/FerroelectricityMultiferroicityAtomic2023]]。

## 2. 掺杂工程与 HZO
由于纯 HfO2 的铁电相难以稳定，研究者通常采用掺杂手段：
- **HZO ($Hf_{0.5}Zr_{0.5}O_2$)**：Zr 掺杂是最主流的方案，具有较宽的工艺窗口（400–600 °C 结晶），且 $Zr$ 与 $Hf$ 原子半径相近，易于形成固溶体。
- **其他掺杂**：$La$、$Si$、$Al$ 等掺杂已被证实能通过应变或缺陷（如氧空位 $V_O$）调控进一步稳定 $o$ 相，提升剩余极化 $2P_r$ [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 3. 器件应用与 CMOS 兼容性
HfO2 最大的优势在于其与 **CMOS 工艺的天然兼容性**：
- **FeFET (铁电晶体管)**：通过极化调制沟道电导，实现非易失性存储与逻辑运算。
- **FTJ (铁电隧道结)**：利用超薄 HfO2 作为隧穿势垒，实现高速（ps 级）、低功耗存储。
- **神经形态计算**：模拟生物突触的权重调节（LTP/LTD），构建存算一体（In-memory Computing）硬件加速器 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 4. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **剩余极化 ($2P_r$)** | $\sim 20\text{--}55\text{ \mu C/cm}^2$ | 取决于掺杂与厚度 |
| **矫顽场 ($E_c$)** | $\sim 1\text{--}2\text{ MV/cm}$ | 高于传统钙钛矿 |
| **临界厚度** | 无 (低至 $1\text{ nm}$ 稳定) | 优于位移型铁电体 |
| **材料类别** | 萤石结构氧化物 | CMOS 后端兼容 |

## 5. 本库相关代表性论文
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：对比 HfO2 与钙钛矿在原子级厚度下的尺寸效应。
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：系统综述了 HfO2 在器件物理、突触模拟及后摩尔集成方面的完整技术链。
- [[../papers/hanPolarTopologicalMaterials2025]]：讨论了 HfO2 中由电 DMI 稳定极性拓扑结构的可能性。

## 6. 关联概念与实体
- [[../concepts/hafnia-ferroelectricity|氧化铪铁电性 Hafnia Ferroelectricity]]
- [[../concepts/neuromorphic-computing|神经形态计算 Neuromorphic Computing]]
- [[../entities/HZO|HZO]] (主流掺杂体系)
- [[../entities/FeFET|FeFET]] (核心铁电器件)
- [[../entities/BaTiO3|钛酸钡 BaTiO3]] (性能对比标杆)
