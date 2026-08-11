---
tags: [entity, device, ferroelectric, transistor, cmos-compatible]
category: [D02, Z01]
---

# 铁电场效应晶体管 / Ferroelectric Field-Effect Transistor (FeFET)

**FeFET** 是一种利用铁电层作为栅极介质的三端非易失性存储器件。通过铁电极化的翻转来调制半导体沟道的电导，实现逻辑态的存储与读取。在 [[HfO2|HfO2]] 基铁电发现后，FeFET 因其卓越的 CMOS 兼容性成为后摩尔时代存算一体的核心候选者 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 1. 结构与工作原理
- **器件结构**：典型的结构包括金属-铁电-半导体 (MFS) 或金属-铁电-绝缘体-半导体 (MFIS)。其中，绝缘体层（如 $SiO_2$ 或 $Al_2O_3$）常用于抑制漏电流和界面态。
- **阈值电压调制**：铁电层的面外极化指向沟道（$P_{down}$）或远离沟道（$P_{up}$）会分别在半导体表面感生异号电荷，从而显著改变晶体管的阈值电压 ($V_{th}$)。
- **存储窗口 (MW)**：$V_{th}$ 的移动量定义了存储窗口，计算公式通常为 $MW \approx 2E_c \cdot d_{fe}$（$E_c$ 为矫顽场，$d_{fe}$ 为铁电层厚度）。

## 2. 关键性能与优势
- **三端解耦**：与两端存储器（如 RRAM 或 FTJ）不同，FeFET 的写入路径（栅极）与读取路径（源漏沟道）解耦，允许在不破坏极化态的情况下进行高增益读取。
- **高开关比**：基于 HZO 的 FeFET 开关比可达 $10^6$ 以上，存储窗口可超过 $2\text{ V}$ [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。
- **多态存储与突触模拟**：通过控制极化畴的演化，FeFET 可以实现连续的电导调节，模拟生物突触的**长程增强/抑制 (LTP/LTD)** 行为，适用于神经形态计算 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 3. 核心挑战
- **耐久性 (Endurance)**：由于界面电荷注入和电介质击穿，FeFET 的循环寿命（通常 $10^4\text{--}10^6$ 次）目前低于 FeRAM。
- **保持性 (Retention)**：去极化场和漏电流可能导致小尺寸器件中的电荷流失。
- **器件变异性**：多晶铁电薄膜中畴的随机分布导致器件间的性能偏差。

## 4. 主要物性指标
| 参数名称 | 典型数值 | 备注 |
| :--- | :--- | :--- |
| **开关比 ($I_{on}/I_{off}$)** | $10^3\text{--}10^6$ | 取决于沟道材料 (Si/2D) |
| **存储窗口 (MW)** | $0.5\text{--}2.5\text{ V}$ | 取决于 $E_c$ 和厚度 |
| **读出速度** | $< 10\text{ ns}$ | 极快非易失读出 |
| **主要材料** | [[HZO|HZO]], [[MoS2|MoS2]], [[IGZO|IGZO]] | 多材料集成平台 |

## 5. 本库相关代表性论文
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：详细综述了 FeFET 在后摩尔电子学与神经形态系统中的架构与实现。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：讨论了 2D 材料（如 $WTe_2$, $MoS_2$）作为 FeFET 沟道材料的潜力。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：早期关于铁电氧化物薄膜在晶体管集成中的讨论。

## 6. 关联概念与实体
- [[../entities/HZO|HZO]] (主流栅介质材料)
- [[../entities/FTJ|FTJ]] (两端铁电隧道结)
- [[../concepts/neuromorphic-computing|神经形态计算 Neuromorphic Computing]]
- [[../concepts/in-memory-computing|存内计算 In-memory Computing]]
- [[../projects/project-5-snte-ferroelectric-sim|Project-5]] (器件物理模拟参考)
