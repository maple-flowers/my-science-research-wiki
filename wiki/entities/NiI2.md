---
tags: [entity, material, multiferroic, 2D, magnetic, vdW, spin-spiral]
title: 碘化镍 / Nickel Iodide (NiI2)
type: entity
status: mature
category: [D01, Z02]
formula: NiI2
aliases: ["二碘化镍", "NiI₂", "nickel diiodide"]
class: [transition-metal-dihalide, vdW, magnetic]
properties: [type-ii-multiferroics, chiral-spin-spiral, magnetoelectric-coupling, electromagnon]
related_entities: [CrI3, Cr2Ge2Te6, TMDs]
key_quantities:
  Tc_monolayer: "~21 K"
  Tc_bulk: "~59.5 K (T_N,2)"
  Q_vector: "(0.138, 0, 1.457) r.l.u. (proper-screw helix)"
  layer_dependence: "1L 21 K → 2L 30 K → 3L 39 K → 4L 41 K"
papers: [songEvidenceSinglelayerVan2022, aminiAtomicscaleVisualizationMultiferroicity2024, FerroelectricityMultiferroicityAtomic2023, tangMultiferroicityTwodimensionalVan2025]
updated: 2026-08
---

# 碘化镍 / Nickel Iodide (NiI2)

NiI2 是过渡金属二卤化物（transition metal dihalide）家族的范德华磁性材料，是**首个在单原子层极限下实验证实的本征二维多铁体**。其多铁性属于 **II 型（磁感生）多铁**：一种具有确定手性的**正螺旋自旋序（proper-screw spin helix）**打破空间反演对称性，直接诱导面内电极化，从而实现巨大的本征磁电耦合 [[../papers/songEvidenceSinglelayerVan2022]]。

## 👵 太奶导读

太奶，您先记着："多铁"就是一块材料同时有两样本事——一是自带磁性（像小磁针），二是电极化有方向（像一排朝同一个方向的小箭头能记住事儿）。"多铁"最金贵的地方是这两样本事能互相使唤：磁一动，电也跟着动。

普通材料里这两样本事各管各的、凑不到一块儿。NiI2 这"碘化镍"的妙处在于：它里头的小磁针不是齐刷刷排成直线，而是像螺丝纹那样一圈圈螺旋着排，而且这个螺旋是有"左右手"方向的（这就叫正螺旋自旋序）。正是这歪歪扭扭的螺旋把材料的对称给打破了，硬逼出了电的方向；螺旋换个手，电的方向也跟着翻。所以只要让它磁的部分转个向，电的记忆就跟着改写——这就是磁电控。

还有一层：这材料越薄越娇贵。厚厚的时候能耐到约零下二百多度（59 K），剥到只有一层原子时，只能在更冷的约零下二百五十二度（21 K）才维持得住这螺旋。科学家拿光来照它、看颜色和偏振的变化，就把这层薄纱里的磁和电看了个明白。它的用处，是将来做又薄又省电、磁电能互相管着的存储器件打地基。

## 🏗️ 结构概览

NiI2 是层状范德华晶体：镍（Ni）原子夹在两层碘（I）原子之间，构成"三明治"式的单层，层与层之间靠微弱的范德华力贴在一起，因此能像撕胶带那样一层层剥下来。单层里 Ni 原子排成蜂窝晶格，碘原子又大又重（自旋轨道耦合强），是磁性能"挤"出电极化的关键。

![图：NiI2 晶格结构与光学表征——(a)晶体侧视图/俯视图，(b)拉曼光路，(c–d)双层与体相的 SHG/双折射信号](../../raw/figures/songEvidenceSinglelayerVan2022/fig_2_CKHGZI78.png)
*   **看图要点**：(a) 左为单层 NiI2 晶体结构（紫色 Ni、粉紫 I 原子，可见层状三明治堆叠），右为蜂窝状 Ni 平面；下方 (c)(d) 是二次谐波（SHG）和双折射信号随温度的变化，用光学手段间接读出对称性破缺与极性序 [[../papers/songEvidenceSinglelayerVan2022]]。
*   **来源**：[[../papers/songEvidenceSinglelayerVan2022]] -> [[../figures/crystal-structures|晶体结构]]

## 🧩 正螺旋自旋序与磁感生极化

Ni²⁺ 离子构成蜂窝晶格，由于竞争磁交换作用，低温下进入手性螺磁态。该正螺旋自旋序具有传播矢量 $\mathbf{Q}=(0.138,0,1.457)$ r.l.u.，给定的旋向（handedness）打破了空间反演与三重旋转对称；依据自旋电流（spin-current）模型，非共线自旋排布叠加 I 原子的强自旋轨道耦合（SOC），诱导出沿特定晶轴的面内极化 [[../papers/songEvidenceSinglelayerVan2022]]。极化方向由螺旋手性直接决定，外场可同步非易失地翻转极化与磁手性。

![图：NiI2 的正螺旋自旋纹理（a–c）与蒙特卡罗模拟的极化、比热随温度演化（d）](../../raw/figures/songEvidenceSinglelayerVan2022/fig_1_GZQKY2GB.png)
*   **关键特征**：(a–c) 示意给定手性的 proper-screw 螺旋自旋纹理（黑箭头为自旋面内分量、色图为面外分量），该非共线序打破反演对称产生面内极化；(d) 蒙特卡罗模拟给出电极化分量（实心方块）与比热（星号）随温度同步出现拐点，对应磁/极性共转变，模拟 $T_c\approx27$ K，与实验单层 21 K 相符 [[../papers/songEvidenceSinglelayerVan2022]]。
*   **来源**：[[../papers/songEvidenceSinglelayerVan2022]] -> [[../figures/heterostructures-stacking-spintronics-strain|自旋电子学与应变工程]]

## 🔬 单层多铁性的光学证据

由于单层 NiI2 难以用电学方法直接测量极化，Song 等人以多种互补光学手段探测极性与磁手性基态：

- **圆二色拉曼光谱**：发现具有显著拉曼旋光性（Raman optical activity, ROA）的**电磁子（electromagnon）**模式，是动态磁电耦合与磁手性基态的直接指纹。
- **二次谐波产生（SHG）与双折射**：检测到同时破缺三重旋转与反演对称的高度各向异性电子态，支持极性序。
- **偏振旋转角 θ(T)**：双折射信号随温度下降的拐点定义转变温度。

![图：NiI2 多铁序的层数依赖与原子尺度多铁畴成像](../../raw/figures/aminiAtomicscaleVisualizationMultiferroicity2024/fig_1_8XET8BR2.png)
*   **关键特征**：左/中部显示偏振旋转角（归一化）随层数与温度的演化，转变温度随层数单调升高；右部为 AFM-PFM 与磁力显微镜在原子尺度上对单层 NiI2 多铁畴结构的成像，将光学推断的极性态落实到真实空间畴形貌 [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]。
*   **来源**：[[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] -> [[../figures/domain-walls|畴与畴壁]]

## 🎯 层数依赖的转变温度

一个关键发现是多铁转变温度随层数减少而单调降低：单层 21 K → 双层 30 K → 三层 39 K → 四层 41 K → 块体 59.5 K（$T_{N,2}$）。这表明**层间交换耦合对稳定多铁序至关重要**；单层中磁各向异性打开有限温度能隙，使长程序在 2D 极限下得以存在（规避 Mermin–Wagner 限制）[[../papers/songEvidenceSinglelayerVan2022]]。

## 📊 主要物性参数

| 参数 | 数值 | 备注 |
| :--- | :--- | :--- |
| 单层 $T_c$ | ~21 K | 磁序与极化同步转变 |
| 块体 $T_{N,2}$ | ~59.5 K | 螺旋磁基态 |
| 传播矢量 $\mathbf{Q}$ | (0.138, 0, 1.457) r.l.u. | 正螺旋 |
| 磁序类型 | 手性 proper-screw 螺旋 | 非共线反铁磁 |
| SOC | 强（来自 I 配体） | 驱动极化的关键 |
| 材料家族 | 过渡金属二卤化物 | 本征 2D II 型多铁标杆 |

## 📚 相关论文 (Related Papers)

- [[../papers/songEvidenceSinglelayerVan2022]]：Nature 2022，首次以圆二色拉曼/SHG/双折射证实单层 NiI2 的本征 II 型多铁性。
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]：Nature Nanotechnology 2024，原子尺度成像 NiI2 多铁畴。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：综述原子级厚度多铁性，NiI2 为 II 型范例。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：二维范德华多铁综述，讨论 NiI2 在电写磁读存储中的潜力。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/type-ii-multiferroics|II 型多铁]]、[[../concepts/magnetoelectric-coupling|磁电耦合]]、[[../concepts/electromagnon|电磁子]]、[[../concepts/spin-spiral|螺旋自旋序]]、[[../concepts/inverse-dzyaloshinskii-moriya|逆 DM 相互作用]]
- [[../entities/CrI3|CrI3]]（二维铁磁对照）、[[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]（二维磁性参考）
