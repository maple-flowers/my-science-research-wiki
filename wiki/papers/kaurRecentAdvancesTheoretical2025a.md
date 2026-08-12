---
citekey: kaurRecentAdvancesTheoretical2025a
title: "Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials"
authors: [Arneet Kaur, Abir De Sarkar]
year: 2025
journal: "Journal of Physics: Condensed Matter"
doi: "10.1088/1361-648X/addf05"
url: "https://doi.org/10.1088/1361-648X/addf05"
paper_type: review
status: ingested
year_read: 2026
original_note:: [[../../raw/note/kaurRecentAdvancesTheoretical2025a]]
projects: [project-5, project-2, project-7, project-4, project-1]
concepts: [sliding-ferroelectricity, multiferroicity, magnetoelectric-coupling, berry-phase, spin-orbit-coupling, 2d-materials, density-functional-theory, polarization-switching, moire-superlattice, strain-engineering, ferroelasticity, machine-learning-potential, topological-defects, altermagnetism, dynamical-multiferroicity, rashba-effect, spin-hall-effect, quantum-anomalous-hall-effect, born-effective-charge, first-order-phase-transition, peierls-dimerization, charge-transfer, orbital-distortion, across-layer-sliding-ferroelectricity]
entities: [h-BN, TMDs, WTe2, VASP, Wannier90, Fe3GeTe2, CrTe2, SnTe, MnBi2Te4, CrI3, Cr2Ge2Te6, MnSe, VS2, ZrI2, ReS2, MoSi2N4, HgI2, CuInP2S6, BaTiO3, SnS, NbI4, graphene, benzene, MnPSe3, MoTe2, MoS2, PtBr3, VI2, GaN, GeC, InN]
methods: [dft, berry-phase, neb, dfpt, md, mlip, aimd, soc, wannier, gw, tight-binding, group-theory, landau-ginzburg, ising-model, kubo-formula, deam-framework, td-dft, gga-pbe, hubbard-u, phonons]
materials: [h-BN, WTe2, MoS2, MoTe2, WS2, MoSi2N4, HgI2, GeS2-CuInP2S6, graphene, BaTiO3, SnS, NbI4, VS2, VSe2, ZrI2, MnBi2Te4, CrI3, Cr2Ge2Te6, Fe3GeTe2, MnSe, VI2, CrI3-MnSe2, SnS2-MnPSe3, PtBr3, ReS2, MoGe2N4, GaN, GeC, InN, AlN, SiC, BP, BSb, benzene]
figures: [crystal-structures, energy-barriers, polarization-landscapes, electronic-bands, spin-textures, berry-curvature, charge-density-difference, phase-diagrams, domain-walls, moire-patterns, heterostructures-stacking, device-schematics, band-alignments, differential-charge-density, tables]
领域基础知识:: >-
  - **量子受限 Stark 效应 (QCSE)**：在半导体异质结构中，外加电场会导致电子和空穴的波函数向相反方向偏移，从而降低激子复合概率并引起能级红移。
  - **单光子源 (SPS)**：能够按需每次发射一个且仅一个光子的器件，是量子计算和量子通信的核心组件。
  - **六方氮化硼 (hBN)**：一种宽禁带二维范德华材料，其内部的深能级缺陷可作为室温下的高效单光子源。
  - **光子晶体腔 (PCC)**：通过微纳加工在半导体材料上制造周期性孔洞结构，利用带隙效应将光子限制在极小空间内，增强光与物质的相互作用（Purcell 效应）。
  - **极化激元 (Polaritons)**：光子与材料中的偶极激发（如激子）强耦合形成的准粒子，具有光的低质量和物质的非线性特性。

研究背景:: >-
  - **量子技术的需求**：高性能单光子源是构建量子网络的基石。理想的 SPS 需具备高亮度、高纯度、不可区分性，且最好能在室温下工作。
  - **二维材料的崛起**：hBN 因其巨大的带隙（约 6 eV）和能够承载高亮度单光子发射器的特性，成为近年来量子光学研究的热点。
  - **当前挑战**：hBN 中 SPE 的物理起源（缺陷类型）仍存在争议；环境噪声引起的谱扩散和 QCSE 导致的能级不稳定限制了其在实际量子系统中的应用；如何实现高效的电控集成也是待解难题。

作者的问题意识:: >-
  - **核心痛点**：尽管 hBN 单光子源表现出极高的亮度，但如何**主动、精确地调控**其发射波长和动力学过程，以适应量子干扰和片上集成的需求？
  - **现状分析**：现有的调控手段（压力、磁场、应变）各有局限，而电场调控（QCSE）因其响应快、易于集成而备受关注，但相关理论模型和实验验证尚需系统总结。
  - **研究空白**：hBN SPE 与光子结构（如纳米腔）的集成如何进一步提升提取效率？极化激元在增强发射方面扮演了什么角色？

主要研究对象:: >-
  - **hBN 单光子发射器 (SPEs)**：包括点缺陷（如 $N_B V_N$ 等候选模型）引发的零声子线 (ZPL) 发射。
  - **调控机制**：重点关注量子受限 Stark 效应 (QCSE) 对能级的移动作用。
  - **集成结构**：hBN 与硅基光子晶体腔、银/金等金属纳米结构的耦合系统。
  - **混合激元系统**：声子极化激元 (PhPs) 与激子的相互作用。

主要研究方法:: >-
  - **文献综述与对比分析**：系统回顾了近年来关于 hBN 中 SPE 的物理特性研究。
  - **理论建模分析**：分析了 QCSE 的数学模型及其对不同缺陷对称性的影响。
  - **工程策略归纳**：总结了通过纳米光子学结构调控自发辐射率（Purcell 效果）和光搜集效率的方法。

研究意义:: >-
  - **理论价值**：阐明了 hBN 中 Stark 位移的物理机制，为辨别缺陷类型提供了光谱学依据。
  - **技术指导**：为开发可调谐、高性能的室温二维量子光源提供了明确的路线图，特别是在电控调控和腔增强集成方面。
  - **应用前景**：助力基于二维材料的集成光子电路 (PICs) 和分布式量子计算网络的发展。

研究结论:: >-
  - **Stark 效应的强大调控力**：证明了外加电场可以实现超过 10 meV 的 ZPL 位移，是实现多源频率匹配的关键。
  - **缺陷特性的异质性**：hBN 中的不同缺陷对电场的响应显著不同，这暗示了发射源起源的多样性。
  - **集成优势明显**：与微腔耦合不仅能提高单光子源的亮度（Purcell 指数可达数十倍），还能改善其发射方向性。
  - **未来趋势**：未来的高性能 SPS 将依赖于“电控+腔增强”的混合平台。

对领域的贡献:: >-
  - **知识整合**：在二维材料量子光源领域，率先将“电控调控 (Stark)”与“光子结构集成”两大前沿话题进行了深度整合讨论。
  - **模型梳理**：提供了关于 hBN SPE 在外部扰动下演化规律的清晰综述。

未来研究方向提及:: >-
  - **确定性集成**：实现 hBN 缺陷在空间位置和发射能量上的确定性生长与放置。
  - **深紫外光源**：探索 hBN 在更短波长（深紫外）范围内的受激发射潜力。
  - **全电控量子电路**：将 hBN SPS 与二维门控结构完美整合，实现全电学驱动的量子位操作。

未来研究方向思考:: >-
  - **缺陷工程的精准化**：目前依赖于随机产生的缺陷，未来需结合离子注入或电子束辐照后的退火工艺，实现“按需定制”的缺陷阵列。
  - **极化激元强耦合**：是否能利用 hBN 极化激元与 SPE 的强耦合，实现室温下的超流态或极化激元激光？
  - **稳定性瓶颈**：电控过程中引入的电荷捕获导致的 ZPL 闪烁（Blinking）仍需通过表面钝化或界面工程解决。
tags:
  - paper
  - type/review
  - year/2025
  - project/project-5
  - project/project-2
  - project/project-7
  - project/project-4
  - project/project-1
  - relevance/project-5/strong
  - relevance/project-2/strong
  - relevance/project-7/medium
  - relevance/project-4/weak
  - relevance/project-1/weak
  - concept/sliding-ferroelectricity
  - concept/multiferroicity
  - concept/magnetoelectric-coupling
  - concept/berry-phase
  - concept/spin-orbit-coupling
  - concept/2d-materials
  - concept/density-functional-theory
  - concept/polarization-switching
  - concept/moire-superlattice
  - concept/strain-engineering
  - concept/ferroelasticity
  - concept/machine-learning-potential
  - concept/altermagnetism
  - concept/dynamical-multiferroicity
  - concept/rashba-effect
  - concept/spin-hall-effect
  - concept/quantum-anomalous-hall-effect
  - concept/born-effective-charge
  - concept/first-order-phase-transition
  - concept/peierls-dimerization
  - concept/charge-transfer
  - concept/orbital-distortion
  - concept/across-layer-sliding-ferroelectricity
  - entity/h-BN
  - entity/TMDs
  - entity/WTe2
  - entity/VASP
  - entity/Wannier90
  - entity/Fe3GeTe2
  - entity/SnTe
  - entity/MnBi2Te4
  - entity/CrI3
  - entity/Cr2Ge2Te6
  - entity/MnSe
  - entity/VS2
  - entity/ZrI2
  - entity/ReS2
  - entity/MoSi2N4
  - entity/HgI2
  - entity/CuInP2S6
  - entity/BaTiO3
  - entity/SnS
  - entity/NbI4
  - entity/graphene
  - entity/MnPSe3
  - entity/MoTe2
  - entity/MoS2
  - entity/PtBr3
  - entity/VI2
  - method/dft
  - method/berry-phase
  - method/neb
  - method/dfpt
  - method/md
  - method/mlip
  - method/aimd
  - method/soc
  - method/wannier
  - method/tight-binding
  - method/group-theory
  - method/landau-ginzburg
  - method/ising-model
  - method/kubo-formula
  - method/td-dft
  - method/gga-pbe
  - method/hubbard-u
  - method/phonons
  - material/h-BN
  - material/WTe2
  - material/MoS2
  - material/MoTe2
  - material/WS2
  - material/MoSi2N4
  - material/HgI2
  - material/GeS2-CuInP2S6
  - material/graphene
  - material/BaTiO3
  - material/SnS
  - material/NbI4
  - material/VS2
  - material/ZrI2
  - material/MnBi2Te4
  - material/CrI3
  - material/Cr2Ge2Te6
  - material/Fe3GeTe2
  - material/MnSe
  - material/VI2
  - material/SnS2-MnPSe3
  - material/PtBr3
  - material/ReS2
  - material/benzene
  - topic/ferroelectricity
  - topic/2d-materials
  - topic/multiferroics
  - topic/sliding-ferroelectricity
  - topic/spintronics
  - topic/topological-insulators
  - topic/moire-superlattice
  - topic/charge-density-wave
  - topic/domain-walls
  - topic/magnetoelectric-coupling
  - topic/first-principles
  - topic/nonvolatile-memory
---

## kaurRecentAdvancesTheoretical2025a — 层状和范德华二维材料中滑动铁电性的理论研究进展

## 📄 元数据
Arneet Kaur, Abir De Sarkar，2025，*Journal of Physics: Condensed Matter* 37, 253001，DOI [10.1088/1361-648X/addf05](https://doi.org/10.1088/1361-648X/addf05)
## 💡 一句话
系统综述二维/层状范德华材料中"滑动铁电性"的第一性原理理论框架——从电荷转移/轨道畸变起源、DFT+Berry-phase+NEB 计算流程、应变/电场/激光/层数调控，到与磁性、拓扑、交变磁性、铁弹性的耦合及连续介质热力学一级相变图像。
## 🔗 Wiki 双链
  - 概念 [[../concepts/sliding-ferroelectricity]]、[[../concepts/multiferroicity]]、[[../concepts/magnetoelectric-coupling]]、[[../concepts/berry-phase]]、[[../concepts/spin-orbit-coupling]]、[[../concepts/2D-materials]]、[[../concepts/density-functional-theory]]、[[../concepts/polarization-switching]]、[[../concepts/moire-superlattice]]、[[../concepts/strain-engineering]]、[[../concepts/ferroelasticity]]、[[../concepts/machine-learning-potential]]、[[../concepts/topological-defects]]、[[../concepts/charge-density-wave]]、[[../concepts/across-layer-sliding-ferroelectricity|跨层滑动铁电性]]、[[../concepts/altermagnetism|交变磁性]]、[[../concepts/born-effective-charge|Born 有效电荷]]、[[../concepts/charge-transfer|电荷转移]]、[[../concepts/dynamical-multiferroicity|动态多铁性]]、[[../concepts/first-order-ferroelectric-transition|一级铁电相变]]、[[../concepts/layer-polarized-spin-hall-effect|层极化自旋霍尔效应]]、[[../concepts/polarization-registry-index|极化登记指数]]、[[../concepts/quantum-anomalous-hall-effect|量子反常霍尔效应]]、[[../concepts/rashba-effect|Rashba 效应]]、[[../concepts/rashba-spin-texture|Rashba 自旋织构]]、[[../concepts/spin-hall-effect|自旋霍尔效应]]
  - 实体 [[../entities/h-BN]]、[[../entities/TMDs]]、[[../entities/WTe2]]、[[../entities/VASP]]、[[../entities/Wannier90]]、[[../entities/Fe3GeTe2]]、[[../entities/CrTe2]]、[[../entities/SnTe]]、[[../entities/In2Se3]]、[[../entities/MXenes]]、[[../entities/deep-potential]]、[[../entities/domain-wall]]、[[../entities/BaTiO3|BaTiO3]]、[[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]、[[../entities/CrI3|CrI3]]、[[../entities/CuInP2S6|CuInP2S6]]、[[../entities/HgI2|HgI2]]、[[../entities/MnBi2Te4|MnBi2Te4]]、[[../entities/MnSe|MnSe]]、[[../entities/MoSi2N4|MoSi2N4]]、[[../entities/MoTe2|MoTe2]]、[[../entities/NbI4|NbI4]]、[[../entities/PtBr3|PtBr3]]、[[../entities/ReS2|ReS2]]、[[../entities/SnS|SnS]]、[[../entities/VS2|VS2]]、[[../entities/ZrI2|ZrI2]]、[[../entities/graphene|石墨烯]]、[[../entities/graphene-tetralayer|四层石墨烯]]
  - 图表 [[../figures/crystal-structures]]、[[../figures/electronic-bands]]、[[../figures/heterostructures-stacking]]、[[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]、[[../figures/domain-walls]]、[[../figures/electronic-devices]]
  - 年度 [[../write/2025]]
  - 项目 [[../projects/project-5-snte-ferroelectric-sim]]、[[../projects/project-2-mn-multiferroics]]、[[../projects/project-7-cdw-charge-density-wave]]、[[../projects/project-4-ttf-molecular-calc]]、[[../projects/project-1-two-photon]]
  - 相关论文 [[../../raw/note/kaurRecentAdvancesTheoretical2025a]]
## 📊 关键图表
  - 图1 h-BN 双层滑动铁电原理、GPRI/LPRI 与 DFT 势降对比、莫尔畴壁 ![h-BN sliding FE and GPRI](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_1_AU76XCXF.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图2 层间距/应变对 h-BN 极化、负泊松比与负压电性的影响 ![interlayer spacing and strain](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_2_WXXKXBRL.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图3 N-pz 轨道畸变、电场调化极化与 NEB 能垒、三态翻转 ![orbital distortion and E-field](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_3_4WK7RC3W.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图4 DREAM/Allegro MLIP 预测 Tc≈1500 K、倾斜电场降低矫顽场、恒定 24° 倾角 ![MLIP Tc and inclined E](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_4_KNAMQJ9W.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图5 THz 激光 3–4 ps 超快翻转、动态多铁性感生磁场 12 nT ![laser-induced switching](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_5_6I78ZK76.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图6 Td-WTe2 双层 0.6 meV 能垒、双阱势、自旋织构反转、自旋 FET 设计 ![WTe2 bilayer](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_6_K9RVARA2.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图7 III–V/IV 族二元双层 (BP, GaN, GeC)：极化与电负性比/有效距离关系、GeC 为唯一全局极性基态 ![binary bilayers](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_7_5ZKSFJXQ.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图8 Janus TMD (SeMoS/TeMoS)：内建电场比压缩层间距更能提升极化而不显著升能垒；MoS2/WS2 异质双层 ![Janus TMDs](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_8_PHYF2JFI.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图9 层极化自旋霍尔效应 (LP-SHE)、Berry 曲率、MoTe2/MoS2 应变调控 ![LP-SHE](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_9_AVZKMT9S.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图10 1T′-ReS2 多层：A/A′ 双稳态、电荷转移、极化/能垒随层数上升 ![ReS2 multilayers](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_10_739TUGAA.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图11 MoSi2N4/MoGe2N4 双层：层分辨 VBM/CBM、莫尔 II 型量子点阵列 ![MoSi2N4](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_11_BNEYWJCN.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图12 HgI2 双层：双阱、屏蔽电荷积分求极化、Rashba 自旋织构、室温稳定 ![HgI2](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_12_5DRMFEUA.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图13 GeS2/CuInP2S6：位移铁电+滑动铁电四/六态耦合、莫尔极化织构、0.7 TB/cm² 存储密度 ![GeS2-CIPS](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_13_Q2ZT9TYR.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图14 跨层滑动铁电：h-BN/石墨烯/h-BN；苯分子层/石墨烯/h-BN 达 10⁴ Tbit/in² ![across-layer SF](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_14_EU6ERPYG.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图15 四层/多层石墨烯极性堆垛 (ABAC, CABA, CBAB)、滑动莫尔铁电性、平带 ![graphene multilayers](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_15_7HMHTA47.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图16 1-uc BaTiO3/SnS：二维/三维杂化稳定超薄铁电，Néel 点、Bloch 涡旋、联合扭转-滑动 ![BTO-SnS](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_16_MI7YCSTX.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图17 3R-VS2 多铁：四种 P-M 构型、Berry 曲率随电场、AFM↔FM、线性/二阶磁电系数、四态控制 ![VS2 multiferroic](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_17_GCQLXFUN.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图18 ZrI2：T0/1T′/Td 相、声子虚频、双阱、六逻辑态多铁、头对头畴壁金属性与 0.24 eV 势差 ![ZrI2](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_18_TT3NFJTQ.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图19 2H-MnBi2Te4 双层：滑动切换磁序与拓扑（陈数），层间 Te-pz 耦合 ![MnBi2Te4 bilayer](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_19_PFJF35FL.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图20 四层 MnBi2Te4：破 P 对称的铁电 QAH 绝缘体，σxy=±e²/h，陈数随层间距变化 ![FE-QAH FLMBT](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_20_MSGL9MAG.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图21 CrI3、Cr2Ge2Te6、Fe3GeTe2 双层反平行/平行堆垛的滑动铁电与"压电多铁效应" ![magnetic bilayers](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_21_7MRZGUTM.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图22 MnSe 双层：2.7 pC/m 极化、电控塞曼劈裂、8 mμB/胞净磁矩、应变与空穴掺杂协同 ![MnSe multiferroic](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_22_3BZPZSMY.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图23 VI2：自旋螺旋序诱导的非位移铁电、滑动-螺旋手性锁定、SOC 依赖 ![VI2 spin spiral](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_23_IQTNM2V2.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图24 CrI3/MnSe2 异质双层：紧束缚+DFT 揭示磁序可反转层间电子极化，非易失磁电耦合 ![CrI3-MnSe2](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_24_TLD45LIJ.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图25 SnS2/MnPSe3/SnS2：滑动打破 PT 对称诱导交变磁性，两条翻转路径与能垒 ![SnS2-MnPSe3](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_25_Y6TELKJU.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图26 SnS2/MnPSe3/SnS2：Mn 周围电荷耗尽、交变磁体能带劈裂 ![altermagnetic bands](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_26_WRL54Q7E.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图27 PtBr3：AA′/AB′/AC′ 堆垛、晶体霍尔效应、MOKE 克尔角与椭偏率随 ±P 反转 ![PtBr3 altermagnet](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_27_UMBP4VUW.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图28 全部滑动铁电双层的"极化–能垒"性能地图（理想区：右下，高极化低能垒），绿色为多铁材料 ![polarization-barrier map](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_28_5ICIG7NK.png) -> [[../figures/heterostructures-stacking-moire|莫尔超晶格、扭转角与层间堆积]]
  - 图29 连续介质模型：P(T) 一级相变、临界场、电卡熵变 Δs(E) ![first-order transition](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_29_PC3552FQ.png)
  - 表1 各材料带隙、面外/面内极化 (pC/m)、翻转能垒 (meV) 汇总 ![Table 1](../../raw/figures/kaurRecentAdvancesTheoretical2025a/tab_1_3QKTNISV.png)
  - 表2 各滑动铁电材料居里温度 (K) 汇总 ![Table 2](../../raw/figures/kaurRecentAdvancesTheoretical2025a/tab_2_CNML9EBW.png)
  - 公式图像（笔记中按原文顺序抽取的关键公式）：![eq4](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_4_HGFDZPHI.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq5](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_5_T7EMI4TE.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq6](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_6_YYHPFE8I.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq7](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_7_DG7HVECU.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq10](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_10_EG6HZVKT.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq13](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_13_LFPVEJ4K.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq14](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_14_I93RIQPS.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq16](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_16_ED73SZUL.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq17](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_17_ENVBAXF3.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq18](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_18_ARIS5SRN.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq19](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_19_QEYAP45U.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq20](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_20_URI5MQNZ.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq21](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_21_8CWLAPNS.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq23](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_23_QRKNBC4D.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq25](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_25_FNM46Z9F.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq26](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_26_DTISGU7I.png) -> [[../figures/mathematical-models|数学模型与物理公式]] ![eq27](../../raw/figures/kaurRecentAdvancesTheoretical2025a/eq_27_7T5QSPXL.png) -> [[../figures/mathematical-models|数学模型与物理公式]]
## 🔬 项目连接
  - **project-5 SnTe 铁电模拟 —— strong**。本文是滑动铁电 DFT 方法论的"全集"：现代极化理论/Berry 相（King-Smith & Vanderbilt）计算 P、Wannier 电荷中心、NEB/CI-NEB 计算翻转路径与能垒、差分电荷密度与平面平均屏蔽电荷积分求 P、PBE/PBE+U/SOC、DFPT 声子、AIMD 室温稳定性、电偶极矩随层间距/应变/电场的扫描流程——均可直接迁移到 SnTe（以及本项目中任何铁电体）的 DFT 模拟。文中还给出了关键"陷阱"：(i) 应使用"孤立势垒 Δ"而非集体翻转势垒与 Tc 关联（Tc≈2Δ/3kB）；(ii) 二维材料高面内刚度使低能垒下极化仍稳健；(iii) 倾斜电场可降低矫顽场；(iv) Janus/内建电场比压缩层间距更能提升极化而不抬能垒；(v) 表1/表2/图28 的极化-能垒地图可作为 SnTe 计算结果的横向参照系。SnTe 在文中虽未直接出现（讨论了 SnS 与 1-uc BTO/SnS），但同属 IV–VI 铁电半导体方法论范畴。
  - **project-2 Mn 多铁 —— strong**。综述第 3 节几乎是"Mn 基二维多铁手册"：MnBi2Te4（滑动切换磁序与 QAH/轴子拓扑）、MnSe（AFM 滑动铁电、电控塞曼劈裂、磁电系数 αS≈−9.8×10⁻¹⁴ G·cm²/V）、SnS2/MnPSe3/SnS2（PT 破缺诱导交变磁性）、CrI3/MnSe2 异质结（磁序反转电子极化）。磁电耦合的微观机制（层间 dz²–pz 杂化、Berry 曲率随电场、μ0ΔM=βE²+αE）对 Mn 基多铁项目的物理图像与计算设计有直接参考价值；altermagnetism、dynamical multiferroicity 等新概念也可作为 wiki 多铁条目扩充。
  - **project-7 CDW —— medium**。WTe2 是 CDW 与铁电共存的明星体系，本文 §2.2 详述 Td-WTe2 双层的 0.6 meV 滑动能垒、Pmn21 对称性、PRI 模型、层间 Te-pz 耦合、自旋纹理；§3.3 中 MnBi2Te4 也涉及 Te-pz 层间耦合驱动的拓扑相变。NbI4 的 Peierls 二聚化与滑动极化（§2.12）则是 CDW/二聚化与铁电耦合的直接案例。CDW 本身不是综述主线，但上述体系的结构失稳、声子虚频（如 ZrI2 T0 相 Γ2⁻/Γ4⁺ 模）、层间耦合分析方法可迁移。
  - **project-4 TTF 分子计算 —— weak**。文中提出"用分子层（苯）替代原子层实现 10⁴ Tbit/in² 超高密度滑动存储"（§2.9，苯/石墨烯/h-BN），以及分子独立存储比特的图像，与分子晶体计算有形式类比；DFT+vdW+NEB 的层间滑移流程也适用于 TTF 类分子晶体。但 TTF 本身未出现，连接强度为弱。
  - **project-1 双光子 —— weak**。§2.1.4 讨论 THz 激光（1.08 THz，高斯包络电场脉冲）共振激发 E(4)/E(5) 红外软模、3–4 ps 内实现层间滑动翻转，并通过 TD-DFT 给出电子激发→电声能量转移→层间滑动三步机制，且动态多铁性感生磁场。这对光-铁电耦合、光控磁有参考价值，但与双光子荧光/吸收无直接关系。
  - **project-3 机械发光 NN**：无直接项目连接。
  - **project-6 湿度传感器**：无直接项目连接。
## 🔗 项目双链
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]
- 项目 [[../projects/project-7-cdw-charge-density-wave|项目七：CDW电荷密度波]]
- 项目 [[../projects/project-4-ttf-molecular-calc|项目四：lsl老师的ttf分子计算]]
- 项目 [[../projects/project-1-two-photon|项目一：双光固化和双光发光]]

## 📝 组织与用词
文章按"原型 h-BN → 单质/二元/TMD/Janus/多层/异质结/分子层 → 多铁与拓扑耦合 → 群论与热力学一般理论 → 隧道结应用 → 总结"递进；每材料小节统一给出对称性破缺、极化值、NEB 能垒、应变/电场/层数响应、新奇物性，是非常规范的理论综述范式。值得在 wiki 中复用的术语：
  - sliding ferroelectricity [[../concepts/sliding-ferroelectricity|sliding ferroelectricity]] / 滑动铁电性
  - out-of-plane (interlayer) polarization / 面外（层间）极化
  - across-layer sliding ferroelectricity (ALSF) / 跨层滑动铁电性 [[../concepts/across-layer-sliding-ferroelectricity|跨层滑动铁电性]]
  - Global/Local Polarization Registry Index (GPRI/LPRI) / 全局/局部极化登记指数
  - orbital distortion (N-pz) / 轨道畸变
  - dynamical multiferroicity (P×∂tP) / 动态多铁性 [[../concepts/dynamical-multiferroicity|动态多铁性]]
  - altermagnetic phase / 交变磁性相
  - layer-polarized spin Hall effect (LP-SHE) / 层极化自旋霍尔效应 [[../concepts/layer-polarized-spin-hall-effect|层极化自旋霍尔效应]]
  - inclined/tilted electric field / 倾斜电场
  - isolated barrier Δ vs. collective switching barrier / 孤立势垒与集体翻转势垒
## ✏️ 可写入 Wiki 的要点
  1. 滑动[[../concepts/ferroelectricity|铁电性]]是电子效应：Jiang 等在 h-BN 中证实滑动不产生面外离子位移，极化来自[[../concepts/interlayer-charge-transfer|层间[[../concepts/charge-transfer|电荷转移]]]]；Liu 等进一步指出 N-pz MLWF 瓣在双层中不对称（N1 比 N2 畸变更强），N-pz–B-pz 排斥与 N-pz–B³⁺ 吸引共同导致电荷中心偏移。
  2. 定量参考值：h-BN 双层 P=2.08 pC/m（Wannier 法 2.14，实验 2.25 pC/m @4.2 K），NEB 能垒 9 meV（BA→AP→AB 路径仅 2.6 meV）；层间电压 U=qd/εS 约 0.23 V (BN)、0.17 V (C/BN)。
  3. GPRI=(S_BN−S_NB)/(S_BN^max−S_NB^max)，以二维高斯原子投影重叠定义，σ_BN=σ_NB=0.22b (b=a/√3, a=2.51 Å) 时与 DFT 势降最佳吻合；可推广到 WTe2、MoS2（引入指数 f(h)=e^{−α(h−h0)} 修正不等价层间距）与转角莫尔体系（LPRI 给出 ~10 nm 畴壁宽度，与 KPFM 实验一致）。
  4. 应变/压力规律：P 与层间距成反比；面内双轴应变经弛豫反而增大层间距（负面外泊松比），h-BN AB 构型同时具有负纵向压电 d33；压力与应变使 P 和能垒同时升高。Janus TMD 中内建电场（而非压缩层间距）可在不显著抬能垒下将 TeMoS 极化较 MoS2 提升 65%——P 越大，电场下 AB/AC 能量差越大，越易电控翻转。
  5. MLIP 精度：DREAM/Allegro 框架同时预测能量、力与 [[../concepts/born-effective-charge|Born 有效电荷]]张量，结构能量差 MAE=0.053 meV/atom；用复[[../concepts/order-parameter|序参量]] ψ=e^{iG·t} 的 MD（900 原子，1–2000 K，50 ps/点）给出 h-BN Tc≈1500 K（此前高估为 1.58×10⁴ K），并证实倾斜 24° 电场 (E∥=0.2 V/Å) 将 E⊥,c 从 ~2 V/Å 显著降低。
  6. 激光超快翻转：h-BN 的 E(4)/E(5) 简并光学模在 1.08 THz，沿 y 偏振的高斯脉冲在 5 K 下 3–4 ps 内克服势垒完成翻转；P 矢量做摆线型旋转并按 M=(S/2me)(e²/ħ)(Z̄*/Z̄*_yy Z̄*_zz) P×∂tP 感生 Mx≈2.7×10⁻⁸ μB、B≈12 nT（[[../concepts/dynamical-multiferroicity|动态[[../concepts/multiferroicity|多铁性]]]]）。TD-DFT 给出"电子 pz 激发→电声能量转移→层间滑动→弛豫反向极化"三步机制。
  7. WTe2 原型：Pmn21 正交结构，NEB 势垒 0.6 meV，P_max=0.37 pC/m（实验 0.23）；AFE 态比 FE 高 0.39 eV/f.u.，Tc≈350 K；Tc 应与"孤立势垒 Δ"关联 (Tc≈2Δ/3kB) 而非集体[[../concepts/switching-barrier|翻转势垒]]。[[../concepts/polarization-switching|极化翻转]]时 Rashba [[../concepts/spin-texture|自旋纹理]]反转，可设计自旋 FET（n≥3 层 WTe2 做电极解决阻抗失配）。
  8. 跨层滑动铁电 (ALSF)：单质双层任何滑动都不破反演，但[[../entities/graphene-tetralayer|四层[[../entitys/graphene|石墨烯]]]]的 ABAC/CABA/CBAB 等堆垛通过次近邻不对称耦合产生 0.21 pC/m 面外 + 57.49 pC/m 面内极化，能垒 <5 meV；h-BN/插层石墨烯/h-BN 为 0.48 pC/m、3 meV。1+3 转角四层石墨烯的极性畴可被电场平移底层切换——"滑动莫尔铁电性"。苯分子层/石墨烯/h-BN 预测 10⁴ Tbit/in²。
  9. 多铁耦合定量：3R-VS2 中 δd=0.6 Å 时线性磁电 αS≈−9.8×10⁻¹⁴ G·cm²/V (−1.48×10⁻⁷ s/m)，δd=0.8 Å 时出现二阶 βS≈−4.5×10⁻²² G·cm³/V²；AFM↔FM 转变伴随半导体-金属转变。MnSe 双层 P=2.7 pC/m、层间电势差 0.23 V、电控净磁矩 8 mμB/胞，磁电效应随层数线性增长（三层 16、四层 24 mμB）；空穴掺杂 1.39×10¹⁵ cm⁻² 时磁矩极大 0.3 μB。
  10. 拓扑与[[../concepts/altermagnetism|交变磁性]]：2H-MnBi2Te4 双层 AB′↔AC′ 翻转能垒 30 meV，可在 AFM/FM 与平庸/陈绝缘体态间切换；四层 P1-FLMBT 为铁电 QAH 绝缘体，σxy=±e²/h，P 翻转逆转 AFM 自旋分布、Berry 曲率与手性边缘态。SnS2/MnPSe3/SnS2 与 PtBr3 中滑动破坏 PT 对称后出现交变磁相，伴随晶体[[../concepts/hall-effect|霍尔效应]]与 MOKE，可用于非易失读取。ZrI2 头对头带电畴壁因束缚电荷使价/导带抵达[[../concepts/fermi-surfaces|费米面]]（0.24 eV 势差）而金属化，[[../concepts/formation-energy|形成能]] E_DW=2P_el E_g/e≈1 mJ/m²。
  11. 一般理论判据：双层要有面外极化必须打破反演、z 镜面、二次旋转轴等对称性；两个中心对称单层也可堆出极性双层。连续介质机电（横场 Ising 类）模型给出一级 FE–PE 相变（P(T) 在 Tc 不连续、临界场随温度变化、伴随电卡熵变 Δs(E)）；尽管翻转势垒极低，[[../concepts/2D-materials|二维材料]]的高面内刚度使弹性能代价抑制热涨落，从而保护长程铁电序（与 Mermin–Wagner 约束相容）。
  12. 应用：滑动[[../entitys/FTJ|铁电隧道结]]预测巨大 TER；压电纳米发电机（WTe2 沿 x/y 拖动产生振荡电信号）；滑移可调制载流子迁移率（ZrI2 金属畴壁）；MoSi2N4 [[../concepts/moire-superlattice|莫尔[[../concepts/superlattice|超晶格]]]]中垂直极化（非层间杂化）产生 II 型量子点阵列用于激子捕获；GeS2/CIPS 莫尔阵列 5° 转角下 0.7 TB/cm² 存储密度。
