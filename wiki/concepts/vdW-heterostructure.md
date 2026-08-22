---
tags: [concept]
title: '范德华异质结 / van der Waals Heterostructure'
type: concept
status: developing
papers: ['dingPredictionIntrinsicTwodimensional2017a', 'hanTunableSlidingFerroelectricity2025', 'songEvidenceSinglelayerVan2022', 'gaoGiantChiralMagnetoelectric2024a', 'liuSpintronicsTwoDimensionalMaterials2020b', 'hallEnvironmentalControlCharge', 'wuElectrostaticGatingIntercalation2022', 'tangMultiferroicityTwodimensionalVan2025']
updated: 2026-08-18
---



# 范德华异质结 / van der Waals Heterostructure

范德华异质结（van der Waals heterostructure, vdW heterostructure）指**由二维层状材料以弱范德华力堆叠而成的异质结构**。与需要严格晶格匹配的外延异质结不同，vdW 异质结的界面无悬挂键，可以自由组合不同材料（甚至不同晶格常数、不同相对转角），从而按需裁剪电子结构、磁性与铁电性。它是二维多铁、滑动铁电、自旋电子学与电荷密度波调控等方向的核心平台。

## 👵 太奶导读

把异质结想成拼积木：传统异质结像两块必须严丝合缝咬在一起的砖（晶格要匹配，不然拼不上）；vdW 异质结更像两张可以随意叠放的纸，轻轻一碰就靠静电一样的力（范德华力）粘在一起，不管纸上的花纹（晶格）对不对得上。科学家把不同功能的"纸"叠起来——一层能发光、一层能带磁、一层滑动一下就能产生电——组合出全新的器件功能，比如用电压去控制磁性，或者做出又薄又省电的存储与传感元件。

## 🧩 堆叠结构与无悬挂键界面

vdW 异质结的核心结构特征是**层间仅由范德华力结合、界面无悬挂键**，因此无需满足外延晶格匹配，可任意堆叠不同材料。二维铁电候选 In₂Se₃ 等 III₂-VI₃ 范德华材料（[[../papers/dingPredictionIntrinsicTwodimensional2017a]]）预测其五层（quintuple layer, QL）单元堆叠具有面外可切换铁电极化；RuX₂（X = Cl, Br, I）家族（[[../papers/hanTunableSlidingFerroelectricity2025]]）则在弱层间耦合下展现出可调的层间堆叠与铁电行为。这类堆叠自由度是 vdW 异质结区别于传统外延结构的关键。

![图：In2Se3 五层 QL 层状结构](<../../raw/figures/dingPredictionIntrinsicTwodimensional2017a/fig_1_NBSIMFLM.png>)

*关键特征：In2Se3 五层（quintuple layer）单元的层状堆叠结构，层间由范德华力结合，支持面外铁电极化。*
*来源：[[../papers/dingPredictionIntrinsicTwodimensional2017a]] -> [[../figures/crystal-structures-bulk|晶体结构与原子构型：体相晶体结构]]*

![图：RuX2 层状晶体结构](<../../raw/figures/hanTunableSlidingFerroelectricity2025/fig_1_N35ETWME.png>)

*关键特征：RuX2（X = Cl, Br, I）的层状晶体结构，层间堆叠方式决定其滑动铁电行为。*
*来源：[[../papers/hanTunableSlidingFerroelectricity2025]] -> [[../figures/crystal-structures-bulk|晶体结构与原子构型：体相晶体结构]]*

## 🧲 二维多铁与滑动铁电

vdW 异质结提供了实现二维多铁与滑动铁电（[[../concepts/sliding-ferroelectricity|滑动铁电]]）的理想平台。song 等（[[../papers/songEvidenceSinglelayerVan2022]]）在单层 vdW 多铁材料中直接观测到极化畴与磁电共存；han 等（[[../papers/hanTunableSlidingFerroelectricity2025]]）通过能量曲线与堆叠路径展示 RuX₂ 层间滑移导致的铁电极化切换；gao 等（[[../papers/gaoGiantChiralMagnetoelectric2024a]]）在 vdW 多铁中观测到巨手性磁电振荡，体现层间堆叠与磁电耦合的深度关联。

![图：单层 vdW 多铁中的极化畴](<../../raw/figures/songEvidenceSinglelayerVan2022/fig_2_CKHGZI78.png>)

*关键特征：单层范德华多铁中观测到的极化畴结构，显示磁电共存的铁电畴图像。*
*来源：[[../papers/songEvidenceSinglelayerVan2022]] -> [[../figures/domain-walls-structures|铁电畴与畴壁：畴结构与畴壁]]*

![图：RuX2 层间滑移的能量曲线与堆叠路径](<../../raw/figures/hanTunableSlidingFerroelectricity2025/fig_2_2XYB57YB.png>)

*关键特征：不同层间堆叠对应的能量曲线与滑动铁电切换路径，展示堆叠自由度的调控能力。*
*来源：[[../papers/hanTunableSlidingFerroelectricity2025]] -> [[../figures/heterostructures-stacking|异质结与堆叠]]*

![图：vdW 多铁中巨手性磁电振荡的衰减曲线](<../../raw/figures/gaoGiantChiralMagnetoelectric2024a/fig_1_8V5GWLM9.png>)

*关键特征：手性磁电振荡信号随时间的衰减曲线，反映 vdW 多铁中磁电耦合的动态响应。*
*来源：[[../papers/gaoGiantChiralMagnetoelectric2024a]] -> [[../figures/crystal-structures-bulk|晶体结构与原子构型：体相晶体结构]]*

## 🔄 自旋电子学与 CDW 调控

vdW 异质结也是自旋电子学（[[../concepts/spin-orbit-coupling|自旋轨道耦合]]）与电荷密度波（[[../concepts/charge-density-wave|电荷密度波]]）调控的平台。liu 综述（[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]）系统覆盖二维材料中的自旋输运与异质结器件，包括石墨烯体系的自旋注入与输运；hall 等（[[../papers/hallEnvironmentalControlCharge]]）在单层 2H-TaS₂ 中展示通过环境（栅压/分子吸附）控制 CDW 序；wu 等（[[../papers/wuElectrostaticGatingIntercalation2022]]）讨论静电栅压（[[../concepts/electrostatic-gating|静电栅压]]）与插层（[[../concepts/intercalation|插层]]）对二维材料电子态的调控。这些手段共同构成 vdW 异质结的"外部旋钮"，可原位调制其磁电与输运性质。

![图：石墨烯体系中的缺陷电荷密度分布](<../../raw/figures/liuSpintronicsTwoDimensionalMaterials2020b/fig_1_VXXN2SRG.png>)

*关键特征：石墨烯中缺陷附近的电荷密度分布，影响自旋注入与输运性质。*
*来源：[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]] -> [[../figures/electronic-bands-cdw-transport|电子结构与输运：CDW与输运性质]]*

![图：二维异质结的制备与自旋输运器件](<../../raw/figures/liuSpintronicsTwoDimensionalMaterials2020b/fig_3_TM5KIMSA.png>)

*关键特征：vdW 异质结的堆叠制备与自旋输运器件结构，展示异质结作为自旋电子学平台的构型。*
*来源：[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]] -> [[../figures/heterostructures-stacking|异质结与堆叠]]*

![图：单层 2H-TaS2 的 STM 形貌](<../../raw/figures/hallEnvironmentalControlCharge/fig_1_8TUKQU42.png>)

*关键特征：单层 2H-TaS2 表面 STM 形貌，用于研究环境对 CDW 序的控制。*
*来源：[[../papers/hallEnvironmentalControlCharge]] -> [[../figures/electronic-bands-dos-fermi|电子结构与输运：态密度与费米面]]*

## 📚 相关论文 (Related Papers)

- [[../papers/dingPredictionIntrinsicTwodimensional2017a]]：预测 In2Se3 等 III2-VI3 范德华材料中的本征二维铁电。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：vdW 多铁中的巨手性磁电振荡。
- [[../papers/hallEnvironmentalControlCharge]]：环境控制单层 2H-TaS2 的 CDW 序。
- [[../papers/hanTunableSlidingFerroelectricity2025]]：二维范德华 RuX2 多铁层中的可调滑动铁电。
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：二维材料中的自旋电子学综述。
- [[../papers/songEvidenceSinglelayerVan2022]]：单层范德华多铁的证据。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：二维范德华材料多铁性的挑战与机遇综述。
- [[../papers/wuElectrostaticGatingIntercalation2022]]：二维材料中的静电栅压与插层调控。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/2d-materials|二维材料]]：vdW 异质结的基本构成单元。
- [[../concepts/moire-superlattice|莫尔超晶格]]：转角堆叠 vdW 异质结中涌现的周期调制。
- [[../concepts/proximity-effect|邻近效应]]：层间相互作用诱导异质结界面的新物性。
- [[../concepts/sliding-ferroelectricity|滑动铁电]]：层间相对滑动产生的铁电极化机制。
- [[../concepts/charge-density-wave|电荷密度波（CDW）]]：vdW 异质结中可被环境调控的电子序。
- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：vdW 异质结自旋电子学与 DM 型磁电耦合的微观来源。
- [[../concepts/intercalation|插层]]：通过插入离子调控 vdW 异质结电子态的手段。
- [[../concepts/electrostatic-gating|静电栅压]]：原位调控 vdW 异质结电子结构与相变的旋钮。
- [[../concepts/ferroelectricity|铁电性]]：vdW 异质结中由堆叠/滑移产生的有序分量。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：vdW 多铁异质结中磁性与铁电的耦合桥梁。
- [[../concepts/spin-spiral|自旋螺旋]]：二维多铁中非共线磁序的可能形式。
- [[../concepts/ferromagnetism|铁磁性]]：vdW 异质结磁性功能的目标物性之一。
- [[../entities/In2Se3|In₂Se₃]]：本征二维铁电的范德华代表材料。
- [[../entities/RuI2|RuI₂]]、[[../entities/RuCl2|RuCl₂]]：RuX₂ 滑动铁电/多铁家族成员。
- [[../entities/graphene|石墨烯]]：自旋电子学 vdW 异质结的基础层。
- [[../entities/2H-TaS2|2H-TaS₂]]、[[../entities/TaS2|TaS₂]]：CDW 调控的 vdW 平台。
- [[../entities/NiI2|NiI₂]]、[[../entities/CrI3|CrI₃]]：二维磁性范德华材料。
- [[../entities/MoS2|MoS₂]]、[[../entities/WSe2|WSe₂]]：过渡金属硫族 vdW 异质结常用层。
- [[../entities/molecular-beam-epitaxy|分子束外延（MBE）]]：vdW 异质结的制备手段之一。
