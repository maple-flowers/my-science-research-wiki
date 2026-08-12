---
tags: [entity, material, ferroelectric, 2D, sliding-ferroelectricity, spintronics]
category: [D01, Z02]
---

# 二碘化汞 / Mercury Diiodide (HgI2)

**HgI2** 是一种展现出稳健滑动铁电性的二维范德华材料。它不仅具有较高的居里温度，更因其显著的自旋-轨道耦合 (SOC) 效应，成为研究**极化可控自旋织构**的理想平台 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 1. 滑动铁电性与室温稳定性
- **极化起源**：双层 HgI2 通过层间滑移实现极化翻转，其饱和极化强度约 **$0.16\text{ \mu C/cm}^2$**。
- **室温铁电性**：由于具有较高的滑动能垒和层间耦合强度，HgI2 在室温下保持稳健的铁电序。
- **双阱势特征**：DFT 计算表明 HgI2 具有典型的双阱能带图，其极化态对应于层间堆叠能量的极小值点。

## 2. Rashba 自旋织构 (Rashba Spin Texture)
- **电控自旋**：HgI2 具有极强的 Rashba 型自旋-轨道耦合。垂直铁电极化的存在打破了空间反演对称性，在能带结构中诱导出显著的自旋劈裂。
- **非易失自旋开关**：通过电场翻转铁电极化，可以同步反转 Rashba 自旋纹理的方向。这一特性是设计**非易失自旋场效应晶体管 (Spin-FET)** 的物理基础 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **饱和极化 ($P$)** | $0.16\text{ \mu C/cm}^2$ | 室温稳定 |
| **自旋耦合** | 强 Rashba SOC | 极化方向可调控 |
| **转变温度 ($T_C$)** | $> 300\text{ K}$ | 室温滑动铁电 |
| **材料类别** | 二维卤化物 | 自旋电子学材料 |

## 4. 本库相关代表性论文
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：详述了 HgI2 的滑动铁电起源、Rashba 自旋织构演化以及在自旋电子器件中的应用前景。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：讨论了高原子序数卤化物在超薄极限下的自旋-极化耦合。

## 5. 关联概念与实体
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/rashba-effect|Rashba 效应 Rashba Effect]]
- [[../entities/WTe2|二碲化钨 WTe2]] (同为 Rashba 铁电金属/半导体)
- [[../projects/project-5-snte-ferroelectric-sim|Project-5]] (自旋轨道耦合模拟参考)
