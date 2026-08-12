---
tags: [entity, device, ferroelectric, diode, cmos-compatible]
category: [D02, Z01]
---

# 铁电二极管 / Ferroelectric Diode (Fe-Diode)

**铁电二极管**（Fe-Diode）是一种利用铁电极化翻转来调制结区势垒高度，进而改变电流-电压（I-V）特性的两端电子器件。在铪基铁电（[[HfO2|HfO2]]）体系中，Fe-Diode 因其极高的读写速度和对 3D 交叉阵列的天然支持，被视为高效、高密度存储的重要方向 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 1. 物理机制
- **肖特基势垒调制**：在铁电层与金属电极形成的肖特基结中，极化方向决定了界面处空间电荷层的分布，从而显著改变肖特基势垒的高度和宽度。
- **整流比切换**：极化翻转可诱导器件从低阻态（LRS）切换至高阻态（HRS），实现非易失性的逻辑存储。
- **自选择特性**：由于二极管的本征整流特性，Fe-Diode 可以在 3D 交叉阵列中自动抑制“潜行电流”（Sneak-path current），无需额外增加选通器。

## 2. 性能优势
- **极快开关**：实验已证实 HfO2 基 Fe-Diode 的开关速度可快至 **$800\text{ ps}$**，远超传统的 RRAM。
- **3D 集成潜力**：其工艺流程与 BEOL 兼容，且已演示多达 16 层的 3D 堆叠，面积效率极高（$\sim 0.06\text{ F}^2/\text{state}$）。
- **耐久性与功耗**：写入过程基于位移电流，功耗低且耐久性较好 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 3. 主要物性指标
| 参数名称 | 典型数值 | 备注 |
| :--- | :--- | :--- |
| **开关速度** | $\sim 800\text{ ps}$ | 超快写入响应 |
| **存储窗口 ($I_{on}/I_{off}$)** | $10^2\text{--}10^4$ | 取决于界面工程 |
| **3D 堆叠层数** | $> 16\text{ layers}$ | 极高面积密度 |
| **主要材料** | [[HZO|HZO]], [[TiN|TiN]] | CMOS 兼容材料体系 |

## 4. 本库相关代表性论文
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：系统综述了 HfO2 基铁电二极管的物理机制、阵列集成及在存内计算中的优势。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：讨论了滑动铁电隧道结作为新型两端器件的潜力。

## 5. 关联概念与实体
- [[../entities/HZO|HZO]] (主流功能层材料)
- [[../entities/FTJ|FTJ]] (铁电隧道结，另一类两端器件)
- [[../entities/FeFET|FeFET]] (三端器件)
- [[../concepts/in-memory-computing|存内计算 In-memory Computing]]
- [[../projects/project-5-snte-ferroelectric-sim|Project-5]] (结区势垒模拟参考)
