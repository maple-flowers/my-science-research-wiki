---
tags: [entity, material, multiferroic, magnetic, perovskite]
category: [D01, Z02]
---

# 锰酸铋 / Bismuth Manganite (BiMnO3, BMO)

**BiMnO3 (BMO)** 是一种极具科学研究价值的磁电多铁材料。它是首批被理论和实验证明能够通过“孤对电子”机制打破 $d^0$ 规则限制，在钙钛矿结构中实现铁磁性与铁电性共存的代表性体系。与大多数反铁磁多铁材料（如 [[../entities/BiFeO3|BiFeO3]]）不同，BMO 在低温下展现出稳健的铁磁序，这使其成为开发新型磁存储和自旋电子学器件（如多铁隧道结）的理想候选材料。

## 1. 磁电共存机制：打破 $d^0$ 规则
在传统的位移型铁电体（如 [[BaTiO3|BaTiO3]]）中，铁电畸变要求 B 位阳离子具有空 $d$ 轨道（$d^0$ 构型）以形成强共价杂化。然而，磁性要求 $d$ 轨道部分填充，这导致了铁电与磁性的化学“互斥性”。

BMO 成功破局的关键在于**A 位驱动机制**：
- **孤对电子立体化学活性**：$Bi^{3+}$ 离子具有 $6s^2$ 活性孤对电子。第一性原理计算表明，Bi $6p$ 轨道与 O $2p$ 轨道发生强烈的共价杂化，驱动 $Bi$ 离子偏离中心位置，从而在 A 位子晶格诱导铁电极化 [[../papers/hillWhyAreThere2000a]]。
- **电子铁电性猜想**：Nicola Hill 在其里程碑论文中曾预言，由于 Bi $6p$ 与 Mn $3d$ 的轨道杂化，BMO 中可能存在一种不依赖离子位移的“电子铁电性”机制，极化可由电子结构的不稳定性驱动 [[../papers/hillWhyAreThere2000a]]。

## 2. 磁性：罕见的钙钛矿铁磁体
与同族的 [[../entities/LaMnO3|LaMnO3]]（典型的 A 型反铁磁 Mott 绝缘体）截然不同，BMO 表现出铁磁序（$T_C \sim 105\text{ K}$）。这种磁序的转变源于 Bi-O 键的共价性增强：
- **削弱超交换**：Bi $6s/6p$ 与氧轨道的杂化改变了 $Mn$-$O$-$Mn$ 的键角和电子云分布，显著削弱了通常占据主导地位的反铁磁超交换作用，从而使铁磁耦合在基态中占据优势 [[../papers/hillWhyAreThere2000a]]。
- **弱铁磁性与磁电耦合**：实验观察到 BMO 的磁化强度与电场具有相关性，揭示了体系中自旋、轨道与晶格自由度的深度耦合。

## 3. 薄膜生长与异质结应用
由于 BMO 块体在常压下处于热力学亚稳态（通常需要高压合成），外延薄膜工程成为研究和应用的关键：
- **应变稳定化**：通过选取合适的衬底（如 SrTiO3），可以利用外延应变稳定钙钛矿相 BMO。Ramesh 等指出，高质量薄膜的制备对于抑制漏电流、观测本征铁电性至关重要 [[../papers/rameshMultiferroicsProgressProspects2007]]。
- **多铁隧道结 (MFTJ)**：BMO 由于兼具铁电与铁磁性，被认为是制造超薄隧道势垒的绝佳材料。在 MFTJ 中，通过电场翻转 BMO 的极化方向可调制势垒高度，同时其磁性可充当自旋过滤器，实现电、磁双控的四态电阻开关 [[../papers/rameshMultiferroicsProgressProspects2007]]。

## 4. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_C$, 铁磁)** | $\sim 105\text{ K}$ | 块体与薄膜存在差异 |
| **铁电极化 ($P$)** | 理论预测 $\sim 10\text{ \mu C/cm}^2$ | 实验受漏电流限制 |
| **晶体结构** | 单斜相 (C2) | 畸变的钙钛矿结构 |
| **磁矩** | $\sim 3.6\text{ \mu B/Mn}$ | 接近 $Mn^{3+}$ 理论值 |
| **材料地位** | 铁磁铁电原型 | [[../projects/project-2-mn-multiferroics|Project-2]] 核心材料 |

## 5. 本库相关代表性论文
- [[../papers/hillWhyAreThere2000a]]：定义了 $d^0$ 规则及其破局路径，首次从电子结构层面论证了 BMO 的多铁性。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：系统综述了 BMO 在薄膜架构中的应用前景，尤其是作为自旋过滤器的潜力。

## 6. 关联概念与实体
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../concepts/magnetoelectric-coupling|磁电耦合 Magnetoelectric Coupling]]
- [[../entities/BiFeO3|铁酸铋 BiFeO3]] (反铁磁多铁标杆)
- [[../entities/LaMnO3|锰酸镧 LaMnO3]] (非铁电对照组)
- [[../entities/YMnO3|锰酸钇 YMnO3]] (几何铁电机制对照)
