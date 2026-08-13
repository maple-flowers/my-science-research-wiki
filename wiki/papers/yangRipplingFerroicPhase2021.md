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
concepts: [2d-materials, ferroelasticity, multiferroicity, strain-engineering, density-functional-theory, machine-learning-potential, polarization-switching, moire-superlattice, ripples, ripple-engineering, polar-nano-regions, avalanche-dynamics, flexoelectric-effect, atomistic-order-parameter, za-phonon-mode, ferroic-order, heterogeneous-nucleation, power-law-statistics]
entities: [VASP, LAMMPS, SnTe, In2Se3, WTe2, GeSe, CrI3, Cr2Ge2Te6, domain-wall]
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
  - entity/domain-wall
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

## yangRipplingFerroicPhase2021 — 二维材料中的波纹铁电相变与畴开关

## 📄 元数据
Yang Yang, Hongxiang Zong, Jun Sun, Xiangdong Ding et al.，2021，Advanced Materials 33(49), 2103469，DOI: 10.1002/adma.202103469
## 💡 一句话
通过自研机器学习势的大规模分子动力学模拟，首次揭示二维单层 GeSe 中本征波纹既能稳定高温相短程铁性序、提高冷却相变温度，又能将应力诱导畴翻转从协同雪崩式（幂律分布）转变为波纹驱动的局域随机过程（高斯分布）。
## 🔗 Wiki 双链
  - 概念 [[../concepts/2D-materials]]、[[../concepts/ferroelasticity]]、[[../concepts/multiferroicity]]、[[../concepts/strain-engineering]]、[[../concepts/density-functional-theory]]、[[../concepts/machine-learning-potential]]、[[../concepts/polarization-switching]]、[[../concepts/moire-superlattice]]、[[../concepts/ripples|波纹]]、[[../concepts/ripple-engineering|波纹工程]]、[[../concepts/polar-nano-regions|极性纳米微区]]、[[../concepts/avalanche-dynamics|雪崩动力学]]、[[../concepts/flexoelectric-effect|挠曲电效应]]、[[../concepts/atomistic-order-parameter|原子级铁性序参量]]、[[../concepts/za-phonon-mode|ZA 声子模]]、[[../concepts/ferroic-order|铁性序]]
  - 实体 [[../entities/VASP]]、[[../entities/SnTe]]、[[../entities/In2Se3]]、[[../entities/WTe2]]、[[../entities/domain-wall]]、[[../entities/GeSe]]、[[../entities/LAMMPS]]、[[../entities/CrI3]]、[[../entities/Cr2Ge2Te6]]
  - 图表 [[../figures/crystal-structures]]、[[../figures/domain-walls]]、[[../figures/mathematical-models]]、[[../figures/heterostructures-stacking-sliding|层间滑移铁电：机制、翻转与动力学]]
  - 年度 [[../write/2021]]
  - 项目 [[../projects/project-5-snte-ferroelectric-sim]]、[[../projects/project-2-mn-multiferroics]]
  - 相关论文 [[../../raw/note/yangRipplingFerroicPhase2021]]
## 📊 关键图表
  - **图1：单层 GeSe 的晶体结构、四畴变体与温度诱导铁性相变**
  - ![图1 单层GeSe晶体结构、四畴变体、势能-温度相变曲线、晶格常数演化及原子级铁性序空间分布与角度关联函数](../../raw/figures/yangRipplingFerroicPhase2021/fig_1_9ERHR5CE.png) → [[../figures/crystal-structures-bulk|体相晶体结构]]
  - **图示描述**：图1a-b 给出单层 GeSe 褶皱蜂窝晶格及四个能量等效畴变体（以原子级铁性序参量 Rp 方向着色，色环定义矢量取向）；图1c-d 为加热-冷却循环中势能（eV/原子）和 x/y 晶格常数（Å）随温度的演化；图1e-h 是 200→400→246→200 K 各阶段 Rp 的空间分布图；图1i 为不同温度下空间关联角 θij(r)（度）随距离 r（nm）的曲线。
  - **关键特征**：势能曲线在加热约 310 K、冷却约 260 K 处出现不连续跳变，对应一级铁性相变并带弱滞后；高温相 x/y 晶格常数趋同、自发应变消失；400 K 时长程序消失但局部仍存在团簇状"偶极子"，即极性纳米微区；θij(r) 在低温相 r>6 nm 仍 <45°，在高温相 r<2 nm 保持 75°–90°（低于完全随机的 90°），定量证实短程铁性序存在；冷却至 200 K 形成由两个 90° 畴壁分隔的条纹状多畴。
  - **结论/意义**：建立了单层 GeSe 铁弹-铁电强耦合体系的相变基线，并首次在二维高温相中识别出区别于体材料顺电相的短程有序极性纳米微区。

  - **图2：波纹对温度诱导铁性相变的调控**
  - ![图2 波纹对铁性相变的影响：序参量-温度、弛豫时间、平均曲率及相关性、波纹振幅热涨落、波峰波谷处铁性序长寿命](../../raw/figures/yangRipplingFerroicPhase2021/fig_2_594HMLNH.png) → [[../figures/crystal-structures-surfaces-defects|表面、缺陷与形貌]]
  - **图示描述**：图2a 对比 constrained（无波纹）与 unconstrained（有波纹）模型平均铁性序幅度 |Rp| 随温度的变化；图2b 为两模型铁性序弛豫时间 τ（ps）-温度曲线；图2c 给出空间平均曲率 κ（Å⁻¹）及其与 |Rp| 的相关性随温度变化；图2d 为波纹均方振幅 <h²>（Å²）-温度关系；图2e-h 为 280 K 下经 0.2 ps 与 2.0 ps 时间平均的表面形貌及对应局域铁性序分布。
  - **关键特征**：波纹将冷却相变温度从约 245 K 提升至约 275 K，并增大铁性序幅度；2Tc 处波纹使弛豫速率降低约 23.3%（τ 显著延长）；平均铁性序增量 ΔR 与平均曲率 κ 呈强线性相关，高温下相关性二次增长；<h²> 随温度线性增长，符合 Gao-Huang 热力学模型（GeSe 低温相弯曲刚度 δ=1.35 eV，样品初始面积 27237.5 Å²）；波峰/波谷处局域铁性序寿命最长，高温下经 100τ 仍有残留；大尺度长寿命波纹与 ZA 声子模一致。
  - **结论/意义**：证明波纹通过曲率耦合稳定高温短程铁性序，并在冷却时充当异质形核点，从而提高相变温度，为"波纹工程"调控 Tc 提供依据。

  - **图3：双轴应变对波纹的主动调控**
  - ![图3 双轴应变调控波纹：曲率-应变曲线及压缩应变诱导高温条纹状铁电畴](../../raw/figures/yangRipplingFerroicPhase2021/fig_3_V7PAZ76Z.png) → [[../figures/domain-walls-structures|畴结构与畴壁]]
  - **图示描述**：图3a 为 350 K 下平均曲率 κ（Å⁻¹）随双轴应变（%，正拉伸/负压缩）的变化曲线；图3b-c 与图3d-e 分别对比无应变和施加 −0.2% 双轴压缩应变时的表面形貌与局域铁性序分布。
  - **关键特征**：拉伸应变抑制波纹（κ 减小），压缩应变增强波纹（κ 增大）；350 K 无应变样品整体无序，而 −0.2% 压缩下波纹显著增强并诱导出清晰条纹状铁电畴；这表明通过应变/衬底工程可在高于 Tc 的温度下主动写入并稳定铁性畴。
  - **结论/意义**：在模拟层面验证了"波纹工程"的可操作性，即通过外场调控波纹曲率来控制二维铁性畴图案。

  - **图4：波纹对应力诱导畴翻转动力学的重塑**
  - ![图4 波纹对应力诱导畴翻转的影响：应力-应变曲线、微观畴演化、应力降PDF从幂律到高斯的转变](../../raw/figures/yangRipplingFerroicPhase2021/fig_4_6PXSF5EA.png) → [[../figures/domain-walls-structures|畴结构与畴壁]]
  - **图示描述**：图4a 为 50 K 沿 x 拉伸时 NPT 平坦模型（蓝）与 NVT 波纹模型（红）的应力（GPa）-应变（%）曲线；图4b-q 依次给出两种模型在不同应变下的微观畴结构演化；图4r 为首次屈服后应力降幅度 A 的概率密度 P(A) 对比。
  - **关键特征**：无波纹曲线在 ε≈4%、9–11%、16% 出现三次突发应力降，对应初级孪晶 (ηx,−Px)、次级孪晶 (ηx,Px) 的形核与竞争生长，并出现初级畴"吞噬"次级畴的自催化级联；有波纹曲线在 ε>4% 后明显平滑，波纹通过改变曲率协调畸变，次级孪晶形核应变由 9.7% 推迟到 12.9%；无波纹 P(A) 服从截断幂律 P(A)~A^(−δ)（δ=1.3），为协同雪崩动力学标志，有波纹 P(A) 变为高斯分布，反映独立随机的局域翻转；补充材料 Fig. S12 证明 NPT/NVT 系综本身不改变该统计。
  - **结论/意义**：从宏观力学响应、微观畴演化到统计物理三个层面，证明波纹把畴翻转从长程协同雪崩转变为局域随机过程。

  - **公式 1：机器学习势总能量表达式**
  - ![公式 机器学习势总能量表达式 Etot=ΣEi=ΣΣαm K(Vi,Vt)](../../raw/figures/yangRipplingFerroicPhase2021/eq_1_VAIRPZZ9.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：基于 Botu-Ramprasad 框架、核岭回归（KRR）构建的 ML 势总能量公式，系统总能量 Etot 为各原子能量 Ei 之和，每个 Ei 由权重系数 αm 与原子环境特征 Vi 和参考数据集 Vt 之间的核函数 K(Vi,Vt) 线性叠加得到。
  - **关键特征**：以 11893 个 DFT 构型（VASP, PBE-GGA, 300 eV cutoff, 3×3×1 k 网格）训练，使用 121 个特征（指数衰减余弦键函数 + 高斯平滑径向分布）；ML 势重现晶格常数、弹性常数、声子谱、相变温度与相变势垒；超胞 40a×40b（a=3.986 Å, b=4.246 Å），LAMMPS 模拟，使万原子、纳秒级波纹-铁性耦合动力学成为可能。
  - **结论/意义**：这是连接 DFT 精度与大尺度 MD 的方法学核心，支撑全文全部定量结论。

  - **公式 2：波纹热涨落 Gao-Huang 模型**
  - ![公式 波纹热涨落 Gao-Huang 模型 <h²>≈16 kB T S0/(π² δ)](../../raw/figures/yangRipplingFerroicPhase2021/eq_4_QASXJXYU.png) -> [[../figures/mathematical-models-elasticity-strain|应变、弹性与力学模型]]
  - **图示描述**：Gao-Huang 热力学模型给出二维膜波纹均方振幅 <h²>≈16 k_B T S0/(π² δ)，其中 k_B 为玻尔兹曼常数、T 为温度、S0 为样品初始面积、δ 为弯曲刚度。
  - **关键特征**：<h²> 与温度 T 成正比、与弯曲刚度 δ 和初始面积 S0 成反比；单层 GeSe 低温相 δ=1.35 eV，样品 S0=27237.5 Å²；MD 测得的波纹振幅热涨落与该解析模型线性吻合，验证了模拟中波纹为热力学平衡涨落而非数值伪影。
  - **结论/意义**：为把波纹作为可定量预测的热力学自由度、并进一步通过应变/衬底工程设计波纹提供了解析基础。

## 🔬 项目连接
  - **project-5（SnTe 铁电模拟）— strong**：本文直接讨论 SnTe 等第四族单硫族化物中铁电相变温度的厚度依赖性，并明确提出波纹变形是理解该现象的关键；所用的 ML 势 + 大尺度 MD + 原子级铁性序参量 + 空间/时间关联函数分析流程，可直接迁移到 SnTe 单层/少层的铁电相变与畴翻转模拟；NPT/NVT 对照隔离波纹效应的方法学设计、Gao-Huang 热涨落模型验证、应力降统计判别雪崩 vs 随机动力学等，均可复用。
  - **project-2（Mn 多铁）— weak**：本文聚焦铁弹-铁电强耦合二维 GeSe，虽非 Mn 基体系，但所阐述的"波纹/应变梯度稳定短程铁性序""耦合序参量定义""应力降统计区分集体与局域翻转"等物理图像，对理解多铁材料中应变-极化-磁耦合的动力学具有形式类比价值；ML 势构建流程也可作为 Mn 多铁大尺度模拟的方法参考。
  - project-1（双光子）、project-3（机械发光 NN）、project-4（TTF 分子计算）、project-6（湿度传感器）、project-7（CDW）：无直接项目连接。
## 🔗 项目双链
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]

## 📝 组织与用词
文章采用"问题提出—现象观察—机制揭示—应用拓展"的论证结构。先在无波纹条件下确立单层 GeSe 的温度诱导铁性相变基线（一级相变、高温极性纳米微区、短程有序），再通过 constrained vs unconstrained 模型对照定量分离波纹效应（提高 Tc、延长弛豫时间、作异质形核点），最后转向应力诱导畴翻转，用应力-应变曲线和应力降概率密度分布（截断幂律 δ=1.3 vs 高斯）完成从"协同雪崩"到"局域随机"的动力学模式判定。论证以对照模拟和统计物理量为核心证据。值得复用的术语：ripples（波纹）、ripplocation（波纹位错）、atomistic ferroic order parameter（原子级铁性序参量）、polar nano-regions（极性纳米微区）、heterogeneous nucleation（异质形核）、avalanche dynamics（雪崩动力学）、cut-off power-law distribution（截断幂律分布）、ripple engineering（波纹工程）、flexural/ZA mode（弯曲/ZA 声学模）、ferroelastic-ferroelectric coupling（铁弹-铁电耦合）。
## ✏️ 可写入 Wiki 的要点
  1. 单层 GeSe 属第四族单硫族化物 MX（M=Ge/Sn，X=S/Se/Te），热力学稳定相具有[[../concepts/strong-coupling|强耦合]]自发极化 P 与[[../concepts/spontaneous-strain|自发应变]] η，存在四个能量等效畴变体 (ηx,±Px)、(ηy,±Py)，由 90° 畴壁分隔。
  2. [[../concepts/atomistic-order-parameter|原子级[[../concepts/ferroic-order|铁性序]]参量]]定义为相邻 Ge-Se 相对位移矢量 R=R_Se−R_Ge 在局域切平面上的投影 Rp=(Δx,Δy)，单一参量同时刻画铁弹与铁电状态，可作空间/[[../concepts/time-correlation|时间关联]]分析。
  3. 加热-冷却 MD 循环（0.77 K/ps）测得 GeSe 单层相变温度：加热约 310 K、冷却约 260 K，呈弱速率依赖的滞后；高温相 x/y 晶格常数趋同，自发应变消失。
  4. 高温相（400 K）并非传统体材料顺电相的完全无序：空间关联角 θij(r) 在 r<2 nm 范围内保持 75°–90°（低于完全随机的 90°），证实存在短程铁性序，即[[../concepts/polar-nano-regions|极性纳米微区]]。
  5. 允许面外运动（有波纹）相比约束面内运动（无波纹），冷却相变温度从约 245 K 提升至约 275 K，且铁性序幅度增大；平均铁性序增量 ΔR 与空间平均曲率 κ 呈线性强相关。
  6. 波纹使铁性序弛豫时间 τ 显著延长（在 2Tc 处降低弛豫速率约 23.3%），波峰/波谷处局域铁性序寿命最长，甚至在高温下经 100τ 后仍残留；这些长寿命微区在冷却时充当异质形核点。
  7. 波纹热涨落满足 Gao-Huang 热力学模型 <h²>≈16 kB T S0/(π² δ)，GeSe 低温相弯曲刚度 δ=1.35 eV，样品初始面积 27237.5 Å²；大尺度波纹的长寿命与声子 ZA 模一致。
  8. 350 K 下施加 −0.2% 双轴压缩应变可增强波纹并诱导出清晰条纹状[[../concepts/ferroelectric-domain|铁电畴]]，而拉伸应变抑制波纹，证明"[[../concepts/ripple-engineering|波纹工程]]"可通过应变/基底工程实现。
  9. 50 K 沿 x 拉伸时，无波纹 NPT 模型应力-应变曲线出现多次突发应力降（ε=4%、9–11%、16%），对应初级/次级孪晶畴的自催化级联形核生长；有波纹 NVT 模型曲线平滑，次级孪晶形核应变从 9.7% 推迟到 12.9%。
  10. 应力降幅度 PDF 是动力学判据：无波纹时服从截断幂律分布 P(A)~A^(−δ)（δ=1.3），标志高度协同[[../concepts/avalanche-dynamics|雪崩动力学]]；有波纹时服从高斯分布，标志波纹局域应力驱动的独立随机翻转；NVT/[[../concepts/npt-ensemble|NPT 系综]]本身不影响该统计（图 S12）。
  11. 方法学：基于 Botu-Ramprasad 框架、核岭回归（KRR）训练的 ML 势，用 11893 个 DFT 参考构型（VASP, PBE-GGA, 300 eV cutoff, 3×3×1 k 网格），121 个特征（指数衰减余弦键函数 + 高斯平滑径向分布），可准确重现晶格常数、弹性常数、声子谱、相变温度和相变势垒；超胞 40a×40b（a=3.986 Å, b=4.246 Å），LAMMPS 模拟，应变率 5×10⁸ s⁻¹，GeSe 有效厚度 9.41 Å。
