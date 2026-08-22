---
citekey: yangRipplingFerroicPhase2021
title: "Rippling Ferroic Phase Transition and Domain Switching In 2D Materials"
authors: [Yang Yang, Hongxiang Zong, Jun Sun, Xiangdong Ding]
year: 2021
journal: "Advanced Materials"
doi: "10.1002/adma.202103469"
url: "https://doi.org/10.1002/adma.202103469"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/yangRipplingFerroicPhase2021]]
projects: [project-5, project-2]
concepts: [2d-materials, ferroelasticity, multiferroicity, strain-engineering, density-functional-theory, machine-learning-potential, polarization-switching, moire-superlattice, ripples, ripple-engineering, polar-nano-regions, avalanche-dynamics, flexoelectric-effect, atomistic-order-parameter, za-phonon-mode, ferroic-order, heterogeneous-nucleation, power-law-statistics, domain-wall]
entities: [VASP, LAMMPS, SnTe, In2Se3, WTe2, GeSe, CrI3, Cr2Ge2Te6]
methods: [md, mlip, dft, kernel-ridge-regression, npt-nvt-ensembles, stress-strain, order-parameter-analysis, autocorrelation-function, first-principles-md]
materials: [GeSe, SnTe, In2Se3, CrI3, Cr2Ge2Te6]
figures: [crystal-structures-bulk, crystal-structures-surfaces-defects, domain-walls-structures, mathematical-models-computational, mathematical-models-elasticity-strain]
领域基础知识:: >-
  二维材料的面外弯曲柔韧性导致本征结构缺陷“波纹”的产生。波纹通过引入局域化应变场，影响材料的电子、力学和摩擦等物理性质。同时，二维铁性材料（如铁电、铁弹体）因其自发极化/应变及外场可调性，在新型功能器件中具有巨大潜力。然而，波纹对二维铁性的影响是领域内长期存在的认知空白。
研究背景:: >-
  过去十年，二维材料研究主要集中在莫尔超晶格工程和利用面外柔韧性引入的局域化应变上。波纹作为二维材料中普遍存在的本征缺陷，已被发现具有量子化、层依赖等特性，并影响电子结构和摩擦行为。然而，这种无处不在的波纹如何影响二维材料中另一种关键物性——铁性（铁电、铁弹），其作用机制和影响效果完全未知。
作者的问题意识:: >-
  作者旨在揭示二维材料中本征缺陷“波纹”对铁性相变和畴翻转动力学的影响。核心问题是：自发形成的波纹是否会，以及如何影响二维铁性材料的相变温度和畴翻转行为？其微观机制是什么？
主要研究对象:: >-
  单层GeSe（锗化硒），一种典型的、具有强耦合铁弹性和铁电性的二维（第四族单硫族化物）材料。
主要研究方法:: >-
  基于自研机器学习原子间势函数的大规模分子动力学模拟。通过对比“约束模型”（禁止面外运动，无波纹）和“无约束模型”（允许面外运动，有波纹）的模拟结果，孤立并揭示波纹在温度诱导相变和应力诱导畴翻转过程中的作用。使用原子级铁性序参量、空间/时间关联函数、曲率等微观量进行分析。
研究意义:: >-
  研究首次将“波纹”从一种被动的结构缺陷，提升为一种可主动调控二维材料铁性功能的“新自由度”。填补了二维材料物理领域关于波纹对铁性影响的理论空白，并为通过“波纹工程”设计柔性二维电子器件提供了理论指导。
研究结论:: >-
  波纹在二维铁性中扮演双重角色：1）在温度诱导相变中，波纹能稳定高温相的短程铁性序，形成极性纳米微区，这些微区可作为异质形核点，从而显著提高铁性相变温度；2）在应力诱导畴翻转中，波纹将畴翻转从长程协同的雪崩式集体行为，转变为由波纹局域化应力驱动的独立随机过程，表现为应力降统计从幂律分布变为高斯分布。
对领域的贡献:: >-
  1）揭示了一种二维材料中普遍存在的物理机制，即波纹通过稳定短程有序和局域化长程相互作用来调控铁性相变与畴翻转；2）提出了“波纹工程”的概念，为主动设计二维材料的铁性提供了新的策略；3）为理解一系列实验中观察到的层数依赖的相变行为提供了新的理论框架。
未来研究方向提及:: >-
  作者指出，该理论可应用于解释其他二维材料（如SnTe， In2Se3， SnS）中波纹与铁性畴共存的实验现象，并有望通过基底工程、应变工程等实验手段，实现“波纹工程”的精确调控，从而按需控制二维材料的畴结构。
未来研究方向思考:: >-
  1）将该模拟方法推广至其他二维铁性、磁性及多铁材料体系，研究波纹效应的普适性；2）探索波纹与莫尔超晶格等其他微结构在调控物性上的协同或竞争关系；3）模拟真实器件结构（如与基底、电极接触）下波纹的行为，并基于此设计功能器件原型；4）研究利用超快激光、电场等外场动态、可逆地调控波纹，以实现超高速、超高密度的信息写入与存储。
tags:
  - paper
  - type/theory
  - year/2021
  - project/project-5
  - project/project-2
  - relevance/project-5/strong
  - relevance/project-2/weak
  - concept/2d-materials
  - concept/ferroelasticity
  - concept/multiferroicity
  - concept/strain-engineering
  - concept/density-functional-theory
  - concept/machine-learning-potential
  - concept/polarization-switching
  - concept/moire-superlattice
  - concept/ripples
  - concept/ripple-engineering
  - concept/polar-nano-regions
  - concept/avalanche-dynamics
  - concept/flexoelectric-effect
  - concept/atomistic-order-parameter
  - concept/za-phonon-mode
  - concept/ferroic-order
  - concept/heterogeneous-nucleation
  - concept/power-law-statistics
  - entity/VASP
  - entity/LAMMPS
  - entity/SnTe
  - entity/In2Se3
  - entity/WTe2
  - entity/GeSe
  - entity/CrI3
  - entity/Cr2Ge2Te6
  - concept/domain-wall
  - method/md
  - method/mlip
  - method/dft
  - method/kernel-ridge-regression
  - method/npt-nvt-ensembles
  - method/stress-strain
  - method/order-parameter-analysis
  - method/autocorrelation-function
  - method/first-principles-md
  - material/GeSe
  - material/SnTe
  - material/In2Se3
  - material/CrI3
  - material/Cr2Ge2Te6
  - topic/ferroelectricity
  - topic/2d-materials
  - topic/domain-walls
  - topic/multiferroics
  - topic/phase-transitions
  - topic/machine-learning-potential
---
## 🔗 Wiki 双链
  - 概念 [[../concepts/ferroic-order]]、[[../concepts/ripple-engineering]]、[[../concepts/multiferroicity]]、[[../concepts/flexoelectric-effect]]、[[../concepts/power-law-statistics]]、[[../concepts/avalanche-dynamics]]、[[../concepts/heterogeneous-nucleation]]、[[../concepts/atomistic-order-parameter]]、[[../concepts/ripples]]、[[../concepts/strain-engineering]]、[[../concepts/2d-materials]]、[[../concepts/density-functional-theory]]、[[../concepts/polar-nano-regions]]、[[../concepts/machine-learning-potential]]、[[../concepts/moire-superlattice]]、[[../concepts/polarization-switching]]、[[../concepts/ferroelasticity]]、[[../concepts/za-phonon-mode]]、[[../concepts/domain-wall]]
  - 实体 [[../entities/Cr2Ge2Te6]]、[[../entities/CrI3]]、[[../entities/WTe2]]、[[../entities/VASP]]、[[../entities/LAMMPS]]、[[../entities/In2Se3]]、[[../entities/GeSe]]、[[../entities/SnTe]]
  - 相关论文 [[../../raw/note/yangRipplingFerroicPhase2021]]

