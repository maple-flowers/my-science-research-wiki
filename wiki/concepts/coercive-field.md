---
tags: [concept, ferroelectricity, testing]
title: 矫顽场 / Coercive Field (Ec)
type: concept
status: mature
domain: [ferroelectricity, multiferroics]
mechanism: 迫使铁电体/磁性体的总剩余序参量（极化或磁化）减小为零时所需的外加场强度
related_concepts: [polarization-switching, ferroelectric-hysteresis, domain-wall-motion, flexoelectric-effect, two-step-switching]
key_quantities:
  BiFeO3_Ec: "约 38 kV/mm（70 nm 薄膜）"
  BiFeO3_Vc: "约 2.3 V（70 nm 薄膜）"
  mechanical_switching_force: "3325 nN（完全翻转）"
papers: [Chen2016electrical, martinThinfilmFerroelectricMaterials2016, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, cuiIntercorrelatedInplaneOutofplane2018a, junqueraCriticalThicknessFerroelectricity2003, Kim2008effect, sunSlidingFerroelectricityTwodimensional2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026]
updated: 2026-08
---

# 矫顽场 / Coercive Field ($E_c$)

矫顽场是铁电体在外场反向扫描时，极化强度穿过零点所对应的场强。它不是材料“开始有一点响应”的阈值，而是外场足以推动成核、畴壁运动和极化路径重排，使宏观净极化被抵消的特征尺度，因此常用来衡量极化态的保持性与写入难度。对厚度为 $d$ 的薄膜，理想平行电容器近似下，矫顽电压满足 $V_c \approx E_c d$。

这一概念在薄膜铁电研究中通常不能脱离边界条件单独理解。[[../papers/martinThinfilmFerroelectricMaterials2016|Martin 与 Rappe 的综述]]将翻转行为放在外延应变、界面、缺陷和畴壁共同决定的框架中；[[../papers/Kim2008effect|Kim 等人的 BiFeO₃ 薄膜实验]]则直接显示，衬底施加的外延应变会改变极化状态和铁电滞回响应，因此不同样品的 $E_c$ 必须连同应变状态一起报告。

## 👵 太奶导读

太奶，您可以把铁电材料想成一排排有方向的小箭头。给它一点点反向电场时，箭头只是在原地抖一抖；电场继续加大，先有一小块箭头在缺口或边界处带头掉头，再带动旁边一大片一起换方向。刚好让原来朝上的和已经朝下的箭头数量抵消时，外面测到的总极化就是零；这时所需要的场强，就叫“矫顽场”。它越大，说明这排箭头越难改写，记忆更稳，但写入需要更高电压。

## 🧩 定义与滞回线中的位置

在铁电滞回线（polarization–electric-field loop，极化—电场回线）中，矫顽场是 $P=0$ 与横轴交点对应的电场值。实际报告时应同时说明测量方向、扫描速率、温度、薄膜厚度和电极结构，因为这些条件都会改变成核与畴壁运动的相对贡献。

*   **矫顽场 $E_c$**：描述场强，单位常见为 kV/mm 或 MV/cm。
*   **矫顽电压 $V_c$**：描述器件需要施加的电压，近似为 $E_c d$；薄膜越薄，不能简单认为电压和场强变化同步。
*   **不是单一微观常数**：宏观 $E_c$ 是多个过程叠加后的实验尺度，通常高于理想无缺陷晶体中仅由局域势垒估计的场强。

## ⚡ 翻转阈值由什么决定

极化翻转通常不是整个晶体同时旋转，而是经历“新畴成核 → 原有畴分解 → 反向畴重组”的过程。[[../papers/Chen2016electrical|Chen 等人的 BiFeO₃ 实验]]把这一过程直接分辨出来：外场先在已有畴壁附近产生反向小畴，再经历纳米畴分解，最后重组成微米尺度的稳定反向畴。外场需要先克服局部缺陷、界面电荷和畴壁钉扎，随后才会出现可观的反向畴体积分数。因此，缺陷密度、晶粒/膜厚、界面电极、内建电场和外加场的扫描速率都会改变测得的 $E_c$。

这一阈值还会随着材料维度和极化分量而变化。[[../papers/cuiIntercorrelatedInplaneOutofplane2018a|Cui 等人的 In₂Se₃ 实验]]显示，超薄材料中的面内、面外极化并非彼此独立，极化翻转可能同时改变不同方向的序参量；[[../papers/junqueraCriticalThicknessFerroelectricity2003|Junquera 与 Ghosez 的第一性原理研究]]则说明，电极屏蔽和退极化场会决定超薄膜能否维持铁电态。两者共同说明，低维体系中的“矫顽场”必须与极化方向、厚度和电静力边界条件一起解释。

![图：BiFeO₃ 薄膜电学翻转中的成核、分解与重组](../../raw/figures/Chen2016electrical/fig_2_8M5UCVB2.png)
*   **关键特征**：从 −1.8 V 到 −2.3 V，反向畴首先在原畴壁附近成核，随后出现纳米尺度分解，最后重组为微米尺度的反向畴；−2.3 V 附近对应该 70 nm 薄膜的矫顽电压，约为 2.3 V。
*   **来源**：[[../papers/Chen2016electrical]] -> [[../figures/domain-walls-switching-properties|极化翻转与铁电性能]]

## 🔬 畴路径与两步翻转

在 BiFeO₃ 这类具有多个等价极化方向的多铁材料中，宏观观察到的 180° 翻转往往不是一步完成。更有利的路径是先发生 71° 或 109° 的铁弹翻转，再完成第二步转向；这条路径同时改变极化方向和晶格畸变，因而与畴壁能、弹性能和磁电耦合相关。矫顽场反映的是这条实际路径被外场驱动起来的难易，而不是孤立离子越过一个固定势垒的简单结果。

对 Chen 等人在 70 nm 外延 BiFeO₃ 薄膜中的实验，$E_c \approx 38\ \text{kV/mm}$，对应 $V_c \approx 2.3\ \text{V}$；电学翻转与机械翻转都遵循相似的三阶段畴演化，支持“材料内禀畴路径决定翻转行为”的判断。[[../papers/tangMultiferroicityTwodimensionalVan2025|Tang 等人的二维范德华多铁综述]]把这类问题推广到低维多铁材料：铁电、铁弹和磁性序参量之间的耦合，会让“翻转难易”同时影响可写入性、磁电响应和器件读出方式。

## 🛠️ 机械场与矫顽场的关系

局部机械力也可以通过应变梯度产生挠曲电场（flexoelectric field），从而推动极化翻转。它不是把“机械力”直接换算成一个普适的电场，而是通过针尖接触造成的非均匀应变改变局部自由能景观，所以机械翻转阈值必须结合针尖半径、接触面积、膜厚和边界条件解释。对于多铁异质结构，[[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025|Cai 等人的实验]]进一步表明，应变驱动的极化变化可以传递到磁性层并产生磁电响应；因此机械或应变调控的阈值不仅决定极化是否翻转，也可能决定磁序能否被可靠写入。

![图：BiFeO₃ 薄膜机械翻转面积随针尖力增加而增长](../../raw/figures/Chen2016electrical/fig_3_V2QYGQGG.png)
*   **关键特征**：针尖力从 700 nN、1050 nN、1400 nN、1750 nN 增至 3325 nN 时，向下极化区域占比约由 8.9%、41.4%、82.2%、95.9% 增至 100%；完全翻转对应约 1.18 GPa 的局部应力。
*   **来源**：[[../papers/Chen2016electrical]] -> [[../figures/domain-walls-switching-properties|极化翻转与铁电性能]]

## 📉 尺度、温度与测量条件

减薄到纳米尺度后，退极化场、界面电荷、应变梯度和电极屏蔽会显著改变翻转能垒与畴结构；温度升高通常降低热激活翻转的有效阈值，而更快的扫描速率可能使表观矫顽场升高。[[../papers/sunSlidingFerroelectricityTwodimensional2025|Sun 等人的综述]]指出，二维滑动铁电还要把层间滑移路径、堆垛状态和层数纳入阈值分析，不能直接套用块体铁电的 $E_c$。[[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026|Tian 等人的室温二维多铁金属实验]]则展示了电压控制极化/磁序的器件路线，说明低维体系的翻转阈值最终还要以“能否稳定写入并读出功能态”来评价。因而不同论文之间比较 $E_c$ 时，不能只比较数值，还要核对厚度、晶向、应变状态、上下电极、频率/扫描速率和测量方法。

对器件而言，较大的 $E_c$ 有利于保持性和抗扰动能力，却会增加写入电压、能耗与介质击穿压力；较小的 $E_c$ 易于低功耗写入，但也可能带来保持性下降和读写串扰。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2016electrical]]：在 70 nm BiFeO₃ 薄膜中测得 $E_c \approx 38\ \text{kV/mm}$，并将电学、机械翻转统一到成核—分解—重组的两步铁弹路径。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：综述薄膜厚度、外延应变、界面和畴壁等因素如何共同改变铁电翻转与器件写入行为。
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：展示二维多铁异质结构中铁电性通过应变介导磁电耦合，说明外场驱动极化翻转还可联动磁序响应。
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]：在超薄 In₂Se₃ 中观测面内与面外极化的耦合和可切换性，为二维体系中的极化翻转阈值与尺寸效应提供实验例子。
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]：从第一性原理揭示电极屏蔽和退极化场决定钙钛矿超薄膜的铁电临界厚度，解释了减薄后翻转行为为何会改变。
- [[../papers/Kim2008effect]]：研究外延应变对 BiFeO₃ 薄膜极化、晶格状态和铁电滞回行为的调控，说明应变是改变表观 $E_c$ 的重要边界条件。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：综述二维滑动铁电性的极化翻转机制及器件应用，涵盖层间滑移、势垒和低维写入问题。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：梳理二维范德华多铁材料中的铁电/铁弹序、磁电耦合和调控挑战，为比较不同低维翻转机制提供背景。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：报道室温二维多铁金属中的电压可控磁序，展示极化调控从单纯电写入扩展到电写磁读的器件方向。

## 📋 关键参数表

下表主要汇总 [[../papers/Chen2016electrical|Chen 等人]]在 70 nm 外延 BiFeO₃ 薄膜中的实验参数；这些数值依赖材料、厚度、应变、电极和测量条件，不是矫顽场的普适常数。

| 参数 | 符号 / 数值 | 条件 | 物理含义 |
| :--- | :--- | :--- | :--- |
| 薄膜厚度 | $d \approx 70\ \text{nm}$ | (001) BiFeO₃ 外延薄膜 | 决定电压—场强换算及退极化、界面效应的相对重要性 |
| 矫顽场 | $E_c \approx 38\ \text{kV/mm}$ | 电学翻转 | 极化净值穿过零点时的特征电场 |
| 矫顽电压 | $V_c \approx 2.3\ \text{V}$ | $V_c \approx E_c d$ | 该样品实现电学写入所需的电压尺度 |
| 机械成核力 | $F \approx 700\ \text{nN}$ | 局部应力约 $0.25\ \text{GPa}$ | 首批反向畴出现并占约 8.9% 面积的力学阈值 |
| 完全机械翻转力 | $F \approx 3325\ \text{nN}$ | 局部应力约 $1.18\ \text{GPa}$ | 反向极化区域达到 100% 的针尖载荷 |
| 机械翻转面积 | 8.9% → 41.4% → 82.2% → 95.9% → 100% | 700 → 1050 → 1400 → 1750 → 3325 nN | 反向畴体积分数随机械驱动力增加的演化 |
| 主要翻转路径 | $71^\circ + 109^\circ$ 或 $109^\circ + 71^\circ$ | BiFeO₃ 多畴结构 | 180° 极化翻转通常经两步铁弹中间态完成 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/polarization-switching|极化翻转]]
- [[../concepts/ferroelectric-hysteresis|铁电滞回]]
- [[../concepts/domain-wall-motion|畴壁运动]]
- [[../concepts/flexoelectric-effect|挠曲电效应]]
- [[../concepts/two-step-switching|两步翻转]]
- [[../entities/BiFeO3|铁酸铋 (BiFeO₃)]]
