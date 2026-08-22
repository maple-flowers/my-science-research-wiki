---
tags: [entity, material, multiferroic, perovskite]
title: 铁酸铋 / Bismuth Ferrite (BiFeO3, BFO)
type: entity
status: developing
formula: BiFeO3
class: [perovksite, multiferroic, insulator]
properties: [multiferroicity, ferroelectricity, antiferromagnetism, magnetoelectric-coupling]
key_quantities:
  Tc: "~1100 K"
  Tn: "~640 K"
  polarization: "~90 uC/cm2 (thin film)"
related_entities: [HoMnO3, PZT, BaTiO3]
papers: [spaldinRenaissanceMagnetoelectricMultiferroics2005, rameshMultiferroicsProgressProspects2007, prosandeevKittelLawInBiFeO3Ultrathin2010, Chen2016electrical, FerroelectricityMultiferroicityAtomic2023, Goswami2011multiferroic, Jin2015studying, Kim2008effect, Perugu2024morphology, RecentAdvancesGrowth2025, aiFerroelectricityCoexistedPorbital2022, aminiAtomicscaleVisualizationMultiferroicity2024, bhowalPolarMetalsPrinciples2023b, cheongMultiferroicsMagneticTwist2007a, deSousa2008electrical, fiebigEvolutionMultiferroics2016, gomez-ortizKittelLawDomain2023, guanRecentProgressTwoDimensional2020, guoAdvancesTwodimensionalFerroelectric2025, hanPolarTopologicalMaterials2025, hillWhyAreThere2000a, huProgressProspectsLowdimensional2019, huangTwodimensionalIn2Se3Rising2022, laiTwodimensionalFerromagnetismDriven2019, martinThinfilmFerroelectricMaterials2016, mostovoyMultiferroicsDifferentRoutes2024, sharmaRoomtemperatureFerroelectricSemimetal2019, spaldinAdvancesMagnetoelectricMultiferroics2019, sunSlidingFerroelectricityTwodimensional2025, tahirFerroelectricityNonvolatileMemristor2025, tangMultiferroicityTwodimensionalVan2025, tianRoomtemperatureTwodimensionalMultiferroic2026, wuCoexistenceFerroelectricityAntiferroelectricity2024, wuSlidingFerroelectricity2D2021a, yuFerroelectricControlMagnetism2026, zahraCriticalAnalysisFerroelectric2025, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08
---

# 铁酸铋 / Bismuth Ferrite (BiFeO3, BFO)

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


铁酸铋 (Bismuth Ferrite, BiFeO₃) 是一种典型的钙钛矿结构氧化物，是目前已知的极少数在室温下同时具有铁电性和磁性（G型反铁磁）的单相多铁性材料。它具有极高的居里温度 (Curie temperature, $T_C \approx 1100$ K) 和奈尔温度 (Néel temperature, $T_N \approx 640$ K)，是设计多功能存储器件和磁传感器最核心的候选材料之一。

## 👵 太奶导读

孙子，这“铁酸铋”可是多铁材料里的“头号明星”。
别看它名字里带个“酸”字，它其实是一种像陶瓷一样的石头。它的身体里住着两种“箭头”：一种是铁磁性的磁箭头，一种是铁电性的电箭头。
平时这些材料要么电太弱，要么磁不稳，还得在冰天雪地里才能显灵。但这铁酸铋天生骨头硬（热稳定性高），在大夏天（室温）也能保持它的这些本事。更神的是，你只要给它加点电压，它身体里的磁箭头也会跟着转个方向，这就是科学家们常说的“一箭双雕”，以后做成手机芯片，能存更多的照片还不费电。

## 🏗️ 结构概览：71° 纳米条带畴

在 (001) 衬底上外延生长的 BFO 超薄膜中，由于外延应变和静电边界条件，常会形成高度规则的条带畴。

![图：BFO 薄膜中 71° 条带畴的局域极化与 AFD 矢量分布](../../raw/figures/prosandeevKittelLawInBiFeO3Ultrathin2010/fig_1_GV39IF8G.png)
*   **看图要点**：图中 (a) 显示了 BFO 超薄膜中的 71° 铁电条带畴。极化矢量 $u_i$ 沿 [uuv] 方向交替排布。由于开路边界条件，在表面 4 层内，电偶极子和氧八面体倾斜矢量 $\xi_i$ 发生卷曲，形成了磁通闭合 (flux-closure) 涡旋结构，以消除退极化场。
*   **来源**：[[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]] -> [[../figures/domain-walls-structures|畴结构与畴壁]]

## 🧩 机制与物性：孤对电子与基特尔定律

BFO 的铁电性源于 Bi³⁺ 离子的 $6s^2$ 孤对电子 (Lone Pair) 的立体化学活性，而磁性源于 Fe³⁺ 离子。

Prosandeev 等人的理论研究证实，BFO 超薄膜在厚度大于 2 nm 时，其畴宽遵循经典的基特尔定律 (Kittel Law, $w \propto \sqrt{h}$)。

![图：BFO 超薄膜总能与畴周期 w 的拟合曲线及 AFD 贡献](../../raw/figures/prosandeevKittelLawInBiFeO3Ultrathin2010/fig_2_478MJ9U5.png)
*   **关键特征**：与传统铁电体不同，BFO 中的畴壁能（$C/w$ 项）主要由氧八面体倾斜 (AFD) 的短程相互作用决定，而非简单的电偶极排斥。这揭示了晶格自由度在多铁界面物理中的主导作用。
*   **来源**：[[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]] -> [[../figures/domain-walls-structures|畴结构与畴壁]]

## 📊 核心性质参数表 (Core Properties)

| 性质 | 数值/描述 | 来源/备注 |
| :--- | :--- | :--- |
| **晶体结构** | 菱方 (R3c) / 钙钛矿 | 体相基态 |
| **居里温度 ($T_C$)** | ~1100 K | 极高热稳定性 |
| **奈尔温度 ($T_N$)** | ~640 K | G-型反铁磁 |
| **自发极化 ($P_s$)** | ~90-100 $\mu$C/cm² | 薄膜测量值，远超早期体相 |
| **磁电耦合方式** | 间接耦合 | 通过反向 Fe-O-Fe 超交换 |
| **光学带隙** | ~2.67 eV | 可见光响应，半导体/绝缘体边界 |

## 📚 相关论文 (Related Papers)

- [[../papers/spaldinRenaissanceMagnetoelectricMultiferroics2005]]：确立了 BFO 作为绕开 $d^0$-$d^n$ 禁忌的明星机制代表。
- [[../papers/rameshMultiferroicsProgressProspects2007]]：展示了 BFO 薄膜在电控磁、垂直纳米结构中的巨大应用前景。
- [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]：利用第一性原理哈密顿量揭示了 BFO 超薄膜畴结构的非传统起源。
- [[../papers/Chen2016electrical]]：从实验研究角度梳理了「Electrical and mechanical switching of ferroelectric polarization in the 70 nm BiFeO3 film」。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：从综述角度梳理了「Ferroelectricity and multiferroicity down to the atomic thickness」。
- [[../papers/Goswami2011multiferroic]]：从实验研究角度梳理了「Multiferroic coupling in nanoscale BiFeO3」。
- [[../papers/Jin2015studying]]：从实验研究角度梳理了「Studying the Polarization Switching in Polycrystalline BiFeO3 Films by 2D Piezoresponse Force Microscopy」。
- [[../papers/Kim2008effect]]：从实验研究角度梳理了「Effect of epitaxial strain on ferroelectric polarization in multiferroic BiFeO3 films」。
- [[../papers/Perugu2024morphology]]：从实验研究角度梳理了「Synthesis, Structural, Morphology and Magnetic Properties: Effect of La on Multiferroic Nature of BiFeO3 Nanoparticles」。
- [[../papers/RecentAdvancesGrowth2025]]：从综述角度梳理了「二维多铁性材料的生长、表征及应用研究进展」。
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]：从理论分析角度梳理了「二维金属氮氧化物中的铁电性与p轨道铁磁性和金属丰度共存」。
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]：从实验研究角度梳理了「Atomic-Scale Visualization of Multiferroicity in Monolayer NiI2」。
- [[../papers/bhowalPolarMetalsPrinciples2023b]]：从综述角度梳理了「极性金属：原理与展望」。
- [[../papers/cheongMultiferroicsMagneticTwist2007a]]：从理论分析角度梳理了「多铁性：铁电的磁扭曲」。
- [[../papers/deSousa2008electrical]]：从理论分析角度梳理了「Electrical control of magnon propagation in multiferroic BiFeO3 films」。
- [[../papers/fiebigEvolutionMultiferroics2016]]：从综述角度梳理了「多铁性的演化」。
- [[../papers/gomez-ortizKittelLawDomain2023]]：从理论分析角度梳理了「Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices」。
- [[../papers/guanRecentProgressTwoDimensional2020]]：从综述角度梳理了「Recent Progress in Two‐Dimensional Ferroelectric Materials」。
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]：从综述角度梳理了「二维铁电材料的研究进展」。
- [[../papers/hanPolarTopologicalMaterials2025]]：从综述角度梳理了「Polar topological materials and devices: Prospects and challenges」。
- [[../papers/hillWhyAreThere2000a]]：从理论分析角度梳理了「为什么磁性铁电体这么少？」。
- [[../papers/huProgressProspectsLowdimensional2019]]：从综述角度梳理了「低维多铁性材料的研究进展与展望」。
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]：从综述角度梳理了「Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage」。
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]：从实验研究角度梳理了「范德华 CuCrP₂S₆ 中的二维铁磁性和驱动铁电性」。
- [[../papers/martinThinfilmFerroelectricMaterials2016]]：从综述角度梳理了「铁电薄膜材料及其应用」。
- [[../papers/mostovoyMultiferroicsDifferentRoutes2024]]：从综述角度梳理了「多铁性：磁电耦合的不同途径」。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：从实验研究角度梳理了「一种室温铁电半金属」。
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：从综述角度梳理了「磁电多铁性材料研究进展」。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：从综述角度梳理了「Sliding ferroelectricity in two-dimensional materials and device applications」。
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]]：从实验研究角度梳理了「自由基二维碳化铌的铁电性和非易失性忆阻应用：自由基MXene在电子器件中的新前沿」。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：从综述角度梳理了「二维范德华材料的多铁性：挑战与机遇」。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：从实验研究角度梳理了「具有电压可控磁序的室温二维多铁金属」。
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]：从实验研究角度梳理了「Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic」。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：从综述角度梳理了「二维范德华材料中的滑动铁电性：相关物理和未来机遇」。
- [[../papers/yuFerroelectricControlMagnetism2026]]
- [[../papers/zahraCriticalAnalysisFerroelectric2025]]
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/multiferroicity|多铁性]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../entities/HoMnO3|HoMnO₃]]
