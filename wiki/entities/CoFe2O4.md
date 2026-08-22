---
tags: [entity, material, oxide, ferrimagnet, magnetoelectric]
title: 钴铁氧体 (CoFe₂O₄)
type: entity
status: mature
category: [D02]
formula: CoFe2O4
class: [spinel, ferrite, oxide, magnetostrictive]
properties: [magnetostriction, magnetoelectric-coupling, high-coercivity]
related_concepts: [composite-multiferroics, magnetoelectric-coupling, magnetoelastic-coupling, piezoelectricity]
related_entities: [BaTiO3, PZT, BiFeO3]
key_quantities:
  magnetostriction: "约 −200 ppm 量级（方向、形貌和成分相关）"
  nanopillar_coercive_field: "约 3 kOe（BiFeO3–CoFe2O4 垂直纳米结构实例）"
  switching_voltage: "16 V（叠加约 700 Oe 偏置场的纳米柱翻转实例）"
papers: [rameshMultiferroicsProgressProspects2007, spaldinAdvancesMagnetoelectricMultiferroics2019]
updated: 2026-08
---

# 钴铁氧体 (CoFe₂O₄)

CoFe₂O₄（钴铁氧体，CFO）是具有反尖晶石结构的亚铁磁氧化物，以较高磁各向异性、矫顽力和磁致伸缩著称。它本身通常不是铁电体；在磁电复合材料中，它承担“磁场 → 形变”的转换，再由相邻压电/铁电相把形变转换成电极化或电压。因此，CFO 的主要价值不是单相中同时具有铁电和磁序，而是作为应变介导磁电耦合链条中的磁致伸缩相。

## 👵 太奶导读

太奶，您可以把 CoFe₂O₄ 想成一种“见到磁场就会微微变形的硬磁陶瓷”。它单独不会因为受压就像压电材料那样产生可翻转极化，也不能凭自己完成强电控磁。可把它和 BaTiO₃、PZT 或 BiFeO₃ 这类会“受力生电、加电变形”的材料紧密结合后，就得到两步转换：磁场让 CFO 伸缩，CFO 再推拉铁电层产生电信号；反过来，电场让铁电层变形，这个应变改变 CFO 的磁各向异性和磁化方向。

这叫乘积效应：磁致伸缩与压电效应各做一半。真正决定效果的，不只是两种材料各自参数有多大，还包括界面是否牢固、形变方向是否匹配、衬底是否把薄膜夹死，以及磁化翻转是否需要额外偏置场。

## 🏗️ 结构概览

CoFe₂O₄ 属于尖晶石 AB₂O₄ 结构。O²⁻ 构成近似面心立方密堆，阳离子分布在四面体 A 位和八面体 B 位；理想反尖晶石分布可近似写为 $(\mathrm{Fe}^{3+})_A[\mathrm{Co}^{2+}\mathrm{Fe}^{3+}]_B\mathrm O_4$。A、B 两个磁性子晶格通过氧介导的超交换反平行排列，但两边磁矩不完全抵消，因此产生净亚铁磁矩。

Co²⁺ 在八面体晶场中的轨道与自旋—轨道耦合带来较强磁晶各向异性；磁化转动又与晶格应变耦合，形成显著磁致伸缩。实际阳离子反位、氧空位、晶粒尺寸、外延应变和温度都会改变各向异性、磁矩与矫顽场，所以“反尖晶石”是理解起点，不代表所有样品具有同一参数。

## 🧲 从磁致伸缩到复合磁电耦合

磁致伸缩是磁畴取向或磁化方向变化引起的晶格尺寸变化。CFO 常见磁致伸缩为负值量级，表示在特定测量方向上材料随磁化趋于收缩；符号和大小依赖晶向、织构、磁场方向及制备状态。反向过程称逆磁致伸缩或 Villari 效应：外加应力改变磁各向异性能量，进而改变易轴、磁化状态或翻转场。

在 CFO/压电体复合结构中，正向磁电转换可写成：

$$H \rightarrow \text{CFO 磁致伸缩} \rightarrow \text{界面应变} \rightarrow \text{压电极化/电压}.$$

逆向电控磁则是：

$$E \rightarrow \text{铁电/压电应变} \rightarrow \text{CFO 磁弹各向异性变化} \rightarrow M\text{ 重定向或翻转}.$$

因此，测得复合体磁电响应并不意味着 CFO 自身出现了铁电序；它是两个相通过机械边界条件形成的器件级耦合。

## 🧱 为什么垂直纳米柱结构重要

水平多层膜中的铁电层和磁性层都贴在刚性衬底上，面内形变容易被衬底夹持，从而削弱应变传递。垂直异质结构把 CFO 尖晶石纳米柱嵌入钙钛矿铁电基体，使柱壁提供大面积三维界面，并让部分形变沿柱方向释放。[[../papers/rameshMultiferroicsProgressProspects2007|Ramesh 与 Spaldin]]据此把薄膜多铁结构分为单相、水平异质结和垂直异质结三类，并将 CFO 纳米柱视为垂直磁性相的典型实现。

[[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019|Spaldin 等人的后续综述]]进一步把 BaTiO₃–CoFe₂O₄ 垂直排列纳米复合体作为复合多铁策略的代表：尖晶石柱与钙钛矿基体通过共格/半共格界面耦合，以几何设计缓解夹持并增强可用界面面积。

![图：复合多铁架构中的尖晶石纳米柱—钙钛矿基体](../../raw/figures/spaldinAdvancesMagnetoelectricMultiferroics2019/fig_2_S95EDSFB.png)
*   **关键特征**：图 b 直接画出尖晶石纳米柱垂直嵌入钙钛矿基体、下方连接电极和衬底的结构；它强调三维柱壁界面，而不是把两相简单水平叠放。图 a、c 是其他复合路线，用于对照不同结构工程方法。
*   **来源**：[[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]] -> [[../figures/heterostructures-stacking|异质结与堆叠]]。

## ⚡ 电场驱动磁化：证据与限制

在 BiFeO₃–CoFe₂O₄ 自组装垂直纳米结构中，[[../papers/rameshMultiferroicsProgressProspects2007|Ramesh 与 Spaldin 的综述]]汇总了一项电控磁实验：样品先在 2 T 磁场中预磁化，再对局部区域施加 16 V 直流电压，并叠加约 700 Oe 偏置磁场，MFM 观察到受电区域内 CFO 纳米柱磁化反转；该实例中纳米柱矫顽场约 3 kOe。解释是铁电基体的电致应变跨界面传递，改变 CFO 柱的磁各向异性。

这里有两个重要边界。第一，实验使用了偏置磁场，因此不能表述为“零磁场下只靠电压确定性翻转”；偏置场用于打破时间反演相关的正反方向简并。第二，16 V、700 Oe 和 3 kOe 都属于该特定纳米结构与测量流程，不是块体 CFO 的普适常数。

## 🔬 设计与表征判据

- **结构与成分**：XRD、电子显微镜和谱学确认尖晶石相、阳离子占位、纳米柱尺寸与界面连续性。
- **磁性**：磁滞回线给出矫顽场和各向异性；不同方向测量可区分形状各向异性与外延应变贡献。
- **磁致伸缩/磁弹响应**：应报告晶向、磁场方向、最大场和是否饱和，不能只给单一 $\lambda$。
- **电控磁证据**：应同时对照电场、偏置磁场和热效应，并用 MFM、MOKE 或磁输运确认变化来自磁态而非表面电荷伪影。
- **界面传递**：裂纹、孔隙、位错和塑性松弛都会损失应变；界面越多不一定耦合越强。

## 📚 相关论文 (Related Papers)

- [[../papers/rameshMultiferroicsProgressProspects2007]]：建立单相—水平—垂直三类薄膜多铁架构，并汇总 BiFeO₃–CoFe₂O₄ 纳米柱中 16 V 与偏置磁场共同驱动磁化翻转的实例。
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：将 BaTiO₃–CoFe₂O₄ 垂直纳米复合结构置于现代复合多铁设计框架中，强调三维界面、应变耦合和纳米柱尺度控制。

## 📋 关键参数表

以下参数分为材料量级和具体异质结构实例；不同制备、晶向和几何条件之间不能直接互换。

| 参数 | 数值 / 范围 | 条件 | 物理意义 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| 磁致伸缩系数 | 约 $-200$ ppm 量级 | CFO 常见报道量级；依赖晶向、形貌与成分 | 决定磁场产生机械应变的能力；负号表示特定方向上的收缩 | [[../papers/rameshMultiferroicsProgressProspects2007]] 所述材料背景；页面原有资料 |
| 预磁化场 | 2 T | BiFeO₃–CoFe₂O₄ 垂直纳米结构 | 先统一纳米柱磁化方向 | [[../papers/rameshMultiferroicsProgressProspects2007]] |
| 局部写入电压 | 16 V 直流 | 上述纳米结构的中心方形区域 | 通过铁电基体应变调制 CFO 磁各向异性 | [[../papers/rameshMultiferroicsProgressProspects2007]] |
| 偏置磁场 | 约 700 Oe | 与 16 V 同时施加 | 打破正反磁化简并，辅助确定性翻转 | [[../papers/rameshMultiferroicsProgressProspects2007]] |
| 纳米柱矫顽场 | 约 3 kOe | 上述 CFO 纳米柱实例 | 表征该结构抵抗磁化反转的场尺度 | [[../papers/rameshMultiferroicsProgressProspects2007]] |
| 普适磁电系数 | 未确认 | 取决于压电相、体积分数、频率、几何和界面 | CFO 单相参数不能直接给出复合体磁电系数 | 仓库现有资料不足 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/composite-multiferroics|复合多铁性]]：用不同材料相的乘积效应获得磁电响应。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：电与磁响应之间的交叉控制。
- [[../concepts/magnetoelastic-coupling|磁弹耦合]]：磁化、应力和晶格形变相互转换的物理基础。
- [[../concepts/piezoelectricity|压电性]]：复合结构中“应变 ↔ 电信号”的另一半转换。
- [[../entities/BaTiO3|BaTiO₃]]：常用铁电/压电钙钛矿基体。
- [[../entities/PZT|PZT]]：具有较强压电响应的配对相。
- [[../entities/BiFeO3|BiFeO₃]]：既可作本征多铁参照，也可作 CFO 纳米柱的铁电基体。
