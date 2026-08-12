---
tags: [entity, material, ferroelectric, oxide, fluorite-structure, cmos-compatible]
category: [D02, Z01]
---

# 锆掺杂氧化铪 / Hafnium Zirconium Oxide (HZO)

**HZO** ($Hf_{0.5}Zr_{0.5}O_2$) 是目前最主流的铪基铁电体系。通过在 [[HfO2|HfO2]] 中引入 $Zr$ 掺杂，可以显著拓宽亚稳极性正交相 ($o$-phase, $Pca2_1$) 的结晶工艺窗口，使其成为后摩尔电子学的核心材料 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 1. 掺杂工程与相稳定性
- **Zr 掺杂优势**：$Zr$ 与 $Hf$ 具有相近的离子半径，易于形成全比例固溶体。相比于纯 $HfO_2$，HZO 的结晶温度较低（400–600 °C），且在 $Hf:Zr \approx 1:1$ 附近展现出最强的铁电响应。
- **工艺窗口**：HZO 兼容典型的原子层沉积 (ALD) 工艺，能够在复杂的 3D 结构（如 FinFET 或 3D NAND）中实现高保形性的生长。
- **应变调控**：面内拉伸应变有助于稳定 $o$ 相。Fan 等证明 >3% 的双轴拉伸应变可使 $Pca2_1$ 相比反极性 $Pbca$ 相更稳定 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 2. 物理机制与特性
- **翻转动力学**：多晶 HZO 薄膜的翻转符合**成核限制开关模型 (NLS)**，而非经典的 KAI 模型。实验提取其最小开关时间 $\tau_\infty \approx 236\text{ ns}$，激活场 $E_a \approx 2.4\text{ MV/cm}$。
- **唤醒与疲劳**：
  - **唤醒效应 (Wake-up)**：初始循环中，氧空位 ($V_O^{2+}$) 从畴壁钉扎位点脱嵌，导致剩余极化 $2P_r$ 增大。
  - **疲劳效应 (Fatigue)**：长期循环（$>10^{10}$ 次）后，缺陷电荷重新累积或微裂纹产生，导致性能衰减。
- **无标度铁电性**：由于具有极性声子平带，HZO 理论上不存在铁电临界厚度，在 $1\text{--}3\text{ nm}$ 极薄薄膜中仍能保持稳健的极化 [[../papers/FerroelectricityMultiferroicityAtomic2023]]。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **剩余极化 ($2P_r$)** | $\sim 20\text{--}50\text{ \mu C/cm}^2$ | 取决于工艺与电极 |
| **矫顽场 ($E_c$)** | $\sim 1\text{--}2\text{ MV/cm}$ | 高于传统钙钛矿 |
| **转变温度 ($T_C$)** | $> 400\text{ K}$ | 室温稳定性极佳 |
| **结晶温度** | $400\text{--}600\text{ \textdegree C}$ | 兼容 CMOS 后端 (BEOL) |
| **材料类别** | 萤石结构氧化物固溶体 | CMOS 兼容铁电体 |

## 4. 本库相关代表性论文
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：系统总结了 HZO 在掺杂工程、器件物理及神经形态计算中的应用。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：对比 HZO 与 2D 铁电体在超薄极限下的物理行为。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：讨论了 HZO 界面电荷对二维材料极化的屏蔽效应。

## 5. 关联概念与实体
- [[../entities/HfO2|氧化铪 HfO2]] (母体材料)
- [[../entities/FeFET|FeFET]] (核心应用器件)
- [[../entities/FTJ|FTJ]] (隧道结应用)
- [[../concepts/hafnia-ferroelectricity|氧化铪铁电性 Hafnia Ferroelectricity]]
- [[../projects/project-5-snte-ferroelectric-sim|Project-5]] (铁电模拟与计算方法参考)
