---
tags: [entity, material, 2d-materials, ferroelectric]
title: 硒化铟 / Indium Selenide (In2Se3)
type: entity
status: developing
formula: In2Se3
stoichiometry: alpha, beta, beta0
class: [III2-VI3, vdW, semiconductor]
properties: [ferroelectricity, sliding-ferroelectricity, piezoelectricity]
related_entities: [Ga2Se3, In2S3, MoS2]
papers: [huangTwodimensionalIn2Se3Rising2022, dingPredictionIntrinsicTwodimensional2017a, FerroelectricityMultiferroicityAtomic2023, RecentAdvancesGrowth2025, aiFerroelectricityCoexistedPorbital2022, chenStrongSlidingFerroelectricity2024, cuiIntercorrelatedInplaneOutofplane2018a, feiFerroelectricSwitchingTwodimensional2018a, fengFerroelectricityMultiferroicityTwodimensional2020, gaoStrainEngineeringFerroelectric2024, guanRecentProgressTwoDimensional2020, guoAdvancesTwodimensionalFerroelectric2025, hanTunableSlidingFerroelectricity2025, heSwitchingTwodimensionalSliding2025, huProgressProspectsLowdimensional2019, kaurRecentAdvancesTheoretical2025a, laiTwodimensionalFerromagnetismDriven2019, liPhaseTransitions2D2021, miaoMagneticFerroelectricMetal2024, neumayerCompetingPolarPhases2025, shenEmergenceMultipleFerroelectric2025, sunSlidingFerroelectricityTwodimensional2025, tangCombiningIntrinsicSlidinginduced2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, wangTunableD0Topological2025b, wuNonvolatileSwitchableHalfmetallicity2024, wuSlidingFerroelectricity2D2021a, xuTwodimensionalFerroelasticityVan2021, yangRipplingFerroicPhase2021, yangStrainEngineeringTwodimensional2021, yuFerroelectricControlMagnetism2026, zahraCriticalAnalysisFerroelectric2025, zhangEmergingFrontiersTwodimensional2025, zhangNonvolatileControlTopological2025, zhaoRealization2DMultiferroic2024]
updated: 2026-08
---

# 硒化铟 / Indium Selenide (In2Se3)

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


硒化铟 ($In_2Se_3$) 是一种极具代表性的二维范德华铁电半导体。它在单层极限（五个原子层厚度）下即可保持稳定的室温铁电性，且具有独特的面内-面外极化锁定（IP-OOP locking）特征。

## 👵 太奶导读

太奶，这个 $In_2Se_3$ 就是材料界的一位“全能选手”。它长得像是一层层薄薄的**威化饼干**。最厉害的地方在于，哪怕您把它撕得只剩下薄薄的一层（单层），它依然能记得自己的极化状态，不会像老式材料那样“人一走茶就凉”（退极化效应）。而且它很“听话”，您在横向给它一个力，它纵向的电信号也会跟着变，这叫“偶极锁定”。这可是咱们做超薄电脑芯片和类脑芯片的心头好！

## 🏗️ 结构概览与多相演变

$In_2Se_3$ 的单层结构由 $Se\text{-}In\text{-}Se\text{-}In\text{-}Se$ 五个原子亚层构成。根据原子的堆垛方式和中心 $Se$ 原子的位置，它主要存在以下几种关键晶相：

1.  **$\alpha$ 相（铁电相）**：这是研究最广泛的相。其特点是两个 $In$ 原子的配位环境完全不同——顶层 $In$ 是**四面体配位**（周围 4 个 $Se$），底层 $In$ 是**八面体配位**（周围 6 个 $Se$）。这种不对称性打破了空间反演对称，产生了一个向下的自发极化（OOP）。
2.  **$\beta$ 相（顺电相）**：在高温下稳定。它的结构是对称的，中心 $Se$ 原子位于两个 $In$ 层的几何中心，整体不显电性。
3.  **$\beta_0$ 相（畸变相）**：这是一种“伪中心对称”状态，中心 $Se$ 原子虽然偏离了中心，但在有限温度下通过快速跳跃在时间平均上表现出对称性。

![图：单层 In2Se3 的 alpha/beta/beta0 相晶体结构对比](../../raw/figures/huangTwodimensionalIn2Se3Rising2022/fig_3_U5LQBVVS.png)
*   **看图要点**：图中 (B)-(D) 展示了 $\alpha$ 相的不对称“头重脚轻”结构；(E) 是完全对称的 $\beta$ 相；(F) 则是中心原子偏心的 $\beta_0$ 相。
*   **来源**：[[../papers/huangTwodimensionalIn2Se3Rising2022]] -> [[../figures/crystal-structures-bulk|体相晶体结构]]

## 🧩 墨西哥帽势能面与“再成键”机制

不同于传统铁电体（如 $BaTiO_3$）中仅 10 pm 左右的微小离子位移，$In_2Se_3$ 的铁电翻转涉及约 **100 pm** 的剧烈原子横移，并伴随化学键的断裂与重构。

*   **墨西哥帽势能面 (Mexican-Hat PES)**：在 $\beta$ 相中，中间层 $Se$ 原子的势能面像一顶墨西哥草帽——中心是能量最高点（不稳），而环绕中心有一圈 12 个等价的能量极小值谷。Se 原子必须“跌入”其中一个谷，从而打破对称性。
*   **偶极锁定 (Dipole Locking)**：$In_2Se_3$ 的面内（IP）极化和面外（OOP）极化是死死锁在一起的。翻转了其中一个，另一个必然跟着翻转。这种互锁机制使得它能极好地抵抗退极化场，即使在单层厚度下也能保持铁电性。

![图：beta 相中间层 Se 原子的墨西哥帽势能面与 12 个能量谷](../../raw/figures/huangTwodimensionalIn2Se3Rising2022/fig_4_4ZJWB5XE.png)
*   **关键特征**：中间的红色区域是能量高地，Se 原子更倾向于落在蓝色的能量低谷中。
*   **来源**：[[../papers/huangTwodimensionalIn2Se3Rising2022]]

## ⚡ 铁电翻转的超快动力学

理论模拟（如 $750 K$ 的分子动力学）显示，$\alpha \to \beta$ 的相变可以在 **1.5 ps**（皮秒）量级完成。这主要由一种**剪切声子模式 (Shear Phonon Mode)** 驱动，表现为上两层原子与下三层原子之间的反向滑动。

## 📊 核心物性参数表 (Core Properties)

| 性质 | 数值/描述 | 来源/备注 |
| :--- | :--- | :--- |
| **晶体常数** | $a=b \approx 4.11$ Å | $R3m$ 空间群 ($\alpha$) |
| **居里温度 ($T_C$)** | $\sim 700$ K | 高于室温，适合稳定器件 |
| **带隙 ($E_g$)** | $\sim 1.39$ eV | 铁电半导体特性 |
| **极化强度 ($P_s$)** | $\sim 0.1-0.5$ pC/m | 二维本征偶极矩 |
| **翻转势垒** | $\sim 0.066$ eV/u.c. | 三步协同路径 (NEB 计算) |
| **开关时间** | $\sim 1.5$ ps (本征) | 实验器件受限于 RC 常数与熵垒 |

## 📚 相关论文 (Related Papers)

- [[../papers/huangTwodimensionalIn2Se3Rising2022]]：系统回顾了 In2Se3 从微观机制到 FeFET、人工突触等器件的应用。
- [[../papers/dingPredictionIntrinsicTwodimensional2017a]]：首次预测单层铁电性的开创性工作。
- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]：实验验证了 In2Se3 的层间滑动翻转。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：从综述角度梳理了「Ferroelectricity and multiferroicity down to the atomic thickness」。
- [[../papers/RecentAdvancesGrowth2025]]：从综述角度梳理了「二维多铁性材料的生长、表征及应用研究进展」。
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]：从理论分析角度梳理了「二维金属氮氧化物中的铁电性与p轨道铁磁性和金属丰度共存」。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：从理论分析角度梳理了「Strong Sliding Ferroelectricity and Interlayer Sliding Controllable Spintronic Effect in Two-Dimensional HgI₂ Layers」。
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]：从实验研究角度梳理了「Intercorrelated In-Plane and Out-of-Plane Ferroelectricity in Ultrathin Two-Dimensional Layered Semiconductor In2Se3」。
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]：从理论分析角度梳理了「二维 Sc₂P₂Se₆ 与 ScCrP₂Se₆ 单层的铁电性与多铁性」。
- [[../papers/gaoStrainEngineeringFerroelectric2024]]：从理论分析角度梳理了「Strain engineering of ferroelectric polarization and domain in the two-dimensional multiferroic semiconductor」。
- [[../papers/guanRecentProgressTwoDimensional2020]]：从综述角度梳理了「Recent Progress in Two‐Dimensional Ferroelectric Materials」。
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]：从综述角度梳理了「二维铁电材料的研究进展」。
- [[../papers/hanTunableSlidingFerroelectricity2025]]：从理论分析角度梳理了「Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers」。
- [[../papers/heSwitchingTwodimensionalSliding2025]]：从理论分析角度梳理了「机械弯曲切换二维滑动铁电体」。
- [[../papers/huProgressProspectsLowdimensional2019]]：从综述角度梳理了「低维多铁性材料的研究进展与展望」。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：从综述角度梳理了「Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials」。
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]：从实验研究角度梳理了「范德华 CuCrP₂S₆ 中的二维铁磁性和驱动铁电性」。
- [[../papers/liPhaseTransitions2D2021]]：从综述角度梳理了「Phase transitions in 2D materials」。
- [[../papers/miaoMagneticFerroelectricMetal2024]]：从理论分析角度梳理了「Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding」。
- [[../papers/neumayerCompetingPolarPhases2025]]：从综述角度梳理了「二维铁电过渡金属硫代和硒酸盐中的竞争极性相」。
- [[../papers/shenEmergenceMultipleFerroelectric2025]]：从实验研究角度梳理了「多层黑磷中多铁电态的出现」。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：从综述角度梳理了「Sliding ferroelectricity in two-dimensional materials and device applications」。
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]]：从理论分析角度梳理了「Combining intrinsic and sliding-induced polarizations for multistates in two-dimensional ferroelectrics」。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：从综述角度梳理了「二维范德华材料的多铁性：挑战与机遇」。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：从实验研究角度梳理了「具有电压可控磁序的室温二维多铁金属」。
- [[../papers/wangTunableD0Topological2025b]]：从理论分析角度梳理了「Tunable d0 topological magnetic states in multiferroic monolayer In2NO2」。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：从实验研究角度梳理了「MXene Hf₂MnC₂O₂/Sc₂CO₂ 多铁异质结中的非易失可开关半金属性与磁性」。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：从综述角度梳理了「二维范德华材料中的滑动铁电性：相关物理和未来机遇」。
- [[../papers/xuTwodimensionalFerroelasticityVan2021]]：从实验研究角度梳理了「Two-dimensional ferroelasticity in van der Waals β'-In2Se3」。
- [[../papers/yangRipplingFerroicPhase2021]]：从理论分析角度梳理了「Rippling Ferroic Phase Transition and Domain Switching In 2D Materials」。
- [[../papers/yangStrainEngineeringTwodimensional2021]]：从综述角度梳理了「二维材料的应变工程：方法、性质和应用」。
- [[../papers/yuFerroelectricControlMagnetism2026]]：从实验研究角度梳理了「强磁电耦合二维多铁性材料中嵌入诱导对称破缺对磁性和巨磁电阻的铁电控制」。
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]：从综述角度梳理了「二维MXene铁电和铁磁性质的临界分析」。
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]
- [[../papers/zhangNonvolatileControlTopological2025]]
- [[../papers/zhaoRealization2DMultiferroic2024]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dipole-locking|偶极锁定]]
- [[../concepts/re-bonding-mechanism|再成键机制]]
- [[../concepts/shear-phonon-mode|剪切声子模式]]
- [[../entities/FeFET|铁电场效应晶体管]]
