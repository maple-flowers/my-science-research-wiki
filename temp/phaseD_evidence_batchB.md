
===== norm-conserving-pseudopotential (papers=6) =====
cites: Li2013bonding, chowdhuryReviewTheoreticalComputational, king-smithTheoryPolarizationCrystalline1993, kresseUltrasoftPseudopotentialsProjector1999c, niuDirectVisualizationLargeScale2021, shishkinImplementationPerformanceFrequencydependentGWmethod2006
--- Li2013bonding ---
title: Bonding Charge Density and Ultimate Strength of Monolayer Transition Metal Dichalcogenides
one: 用第一性原理 DFT 系统计算了六种单层 VI 族 TMD（Mo/W × S/Se/Te）沿扶手椅和锯齿方向的完整应力–应变曲线，揭示极限强度的组分/方向依赖性，并建立"力学性能（E、σ*）随 M→X 电荷转移量 ΔQ 线性增长"的简单定量模型，其电子结构根源是 M-d/X-p 轨道杂化强度。
--- chowdhuryReviewTheoreticalComputational ---
title: Computational Methods for Charge Density Waves in 2D Materials
one: 本综述以 TaS₂ 与 TaSe₂ 为核心，系统总结了用 DFT 等第一性原理方法研究二维 TMDs 中电荷密度波（CDW）时在温度模拟、非公度结构建模、泛函/赝势选择三方面的计算策略，并整理了其在原子/电子结构、拉曼振幅模/相位模、限域与维度效应上的成果。
--- king-smithTheoryPolarizationCrystalline1993 ---
title: Theory of polarization of crystalline solids
one: 本文证明晶体的电极化变化量 ΔP 等于价带波函数贝里相位之差，物理上等价于 Wannier 函数电荷中心的位移，从而奠定了沿用至今的"现代极化理论"及其第一性原理数值算法。
--- kresseUltrasoftPseudopotentialsProjector1999c ---
title: From ultrasoft pseudopotentials to the projector augmented-wave method
one: 严格推导出 Vanderbilt 超软赝势（US-PP）的总能量泛函可由稍作修改的 Blöchl 投影增强波（PAW）泛函对两个原子中心项作一阶线性化得到，从而证明 US-PP 是 PAW 的线性化近似，并给出在现有 US-PP 平面波程序中实现 PAW 的最简路径与系统基准。
--- niuDirectVisualizationLargeScale2021 ---
title: Direct Visualization of Large-Scale Intrinsic Atomic Lattice Structure and Its Collective Anisotropy in Air-Sensitive Monolayer 1T'-WTe2
one: 通过全流程互联惰性气氛保护系统，用原子分辨 HAADF-STEM 直接可视化了空气敏感单层 1T'-WTe2 的大面积完整晶格，发现其本征的、只沿单一晶面方向传播的各向异性褶皱，以及该褶皱对 Te 空位分布的择优调控。
--- shishkinImplementationPerformanceFrequencydependentGWmethod2006 ---
title: Implementation and performance of the frequency-dependent GW method within the PAW framework
one: 在VASP的PAW框架内实现了全频率依赖的G₀W₀计算，利用谱表示与Hilbert/Kramers-Kronig变换将计算成本降至仅约为静态计算的两倍，并以HF水平处理芯-价相互作用，使含d电子材料的准粒子能量计算既快又准。

===== peierls-distortion (papers=6) =====
cites: chenFerromagneticNonmagnetic1T2022, krishnamurthiSpinChargeDensity2020, liFerroelasticityDomainPhysics2016, pedramraziManipulatingTopologicalDomain2019, tahirFerroelectricityNonvolatileMemristor2025, xuTwodimensionalFerroelasticityVan2021
--- chenFerromagneticNonmagnetic1T2022 ---
title: Ferromagnetic and nonmagnetic 1T′ charge density wave states in transition metal dichalcogenides: Physical mechanisms and charge doping induced reversible transition
one: 通过DFT计算揭示TMDs中1T′铁磁CDW态的两种形成机制（直接交换→超交换转变 vs M-M二聚化），并预测CrS₂中电荷掺杂可诱导NM/FM CDW可逆相变，产生高达12.17%的驱动应变与磁性突变。
--- krishnamurthiSpinChargeDensity2020 ---
title: Spin/charge density waves at the boundaries of transition metal dichalcogenides
one: 通过 DFT+U 计算证明 TMDC 镜像孪晶界（MTB）的金属性源于 D₃ₕ 晶格极化这一 Z₃ 拓扑不变量在边界处的反转，导致边界态 1/3 分数占据，并自发形成无需原子位移的纯电子型三重周期自旋密度波/电荷密度波（SDW/CDW），打开约 0.1 eV 能隙，预言携带 ±1/3 e 分数电荷的孤子激发。
--- liFerroelasticityDomainPhysics2016 ---
title: Ferroelasticity and domain physics in two-dimensional transition metal dichalcogenide monolayers
one: 通过第一性原理计算首次预测 1T′ 相 TMD 单层具有三个由 Peierls 畸变产生的取向变体（O1/O2/O3），仅需百分之几弹性应变即可在变体间实现铁弹性切换，切换势垒 <0.2 eV/f.u.，并形成低能准一维铁弹畴壁，从而提出"二维铁弹性/二维形状记忆材料"概念。
--- pedramraziManipulatingTopologicalDomain2019 ---
title: Manipulating Topological Domain Boundaries in the Single-Layer Quantum Spin Hall Insulator 1T′–WSe₂
one: 用 STM 针尖脉冲在单层 1T′-WSe2 中可逆写入/擦除铁弹畴界（120°/60°/0°）并诱导 1T′→1H 相变，结合 STS 与 DFT/NEGF 首次系统表征了 QSHI 中拓扑"未保护"的 1T′/1T′ 畴界面态，建立了其与拓扑保护 1T′/1H 边缘态的谱学鉴别标准。
--- tahirFerroelectricityNonvolatileMemristor2025 ---
title: Ferroelectricity and Nonvolatile Memristor Applications of Free‐Standing 2D Niobium Carbide: A New Frontier of Free‐Standing MXene in Electronic Devices
one: 首次在自支撑二维 Nb₂CTₓ MXene 薄膜上观测到铁电性（1000 Hz 下剩余极化 Pr = 5.12 μC/cm²，为当时自支撑 MXene 最高值），并以其本征氧空位作为开关层构筑了 Ti₃C₂Tₓ/Nb₂CTₓ/Ti₃C₂Tₓ 与 rGO/Nb₂CTₓ/rGO 两种非易失性双极阻变忆阻器。
--- xuTwodimensionalFerroelasticityVan2021 ---
title: Two-dimensional ferroelasticity in van der Waals β'-In2Se3
one: 首次在少层范德华 β'-In2Se3 中实验证实由面内反铁电畸变驱动的二维铁弹性，定量给出 ~0.49% 的自发应变并实现 ≤0.5% 外应变下的可逆畴切换。

===== relative-humidity (papers=6) =====
cites: 2019optical, Doroodmand2017conjugated, Ismail2015humidity, Tobeiha2025optical, XiaokangZhang2013calibrating, Yarai2005optical
--- 2019optical ---
one: 将聚合物光纤（POF, Autonics FD-620-10）中段包层剥离并浸渍涂覆 TiO2-SiO2 纳米复合亲水层，利用倏逝场强度调制实现相对湿度测量，确定最佳剥离长度 2 cm（R²=0.982，灵敏度 0.0376 V/%），并集成到基于 Arduino Uno 的测量系统中（平均误差 2.78%）。
--- Doroodmand2017conjugated ---
title: Electro-synthesized Conjugated Salen Polymer-Glassy Carbon as Hydrochromic Reflective Filter for Humidity Detection: Introduction of Humidity Optical Sensor
one: 首次用循环伏安法在玻碳电极上电合成"无金属"共轭 Salen 聚合物薄膜，将其同时作为亲水感湿层和白光反射滤光片，通过相机读取反射光蓝色分量强度，实现 5–80% RH 范围内线性、快速（~9.5 s）、高选择性的光学湿度检测。
--- Ismail2015humidity ---
title: Humidity Sensor - A Review of Nanostructured Zinc Oxide (ZnO) - Based Humidity Sensor
one: 本文是一篇面向初学者的短篇综述，系统梳理了纳米结构 ZnO 作为湿度敏感材料的核心机理（水分子"施主效应"调制耗尽层电阻）、四种典型纳米形貌（团簇/棒/片/线）、Sn/Al 掺杂的利弊权衡以及四种金属电极构型（叉指/迷宫/城堡/圆形），并指出迷宫式电极在电容式湿度传感器中灵敏度最高。
--- Tobeiha2025optical ---
title: Optical humidity sensor based on G/GO nanosheets
one: 用声化学剥离法制备石墨烯/氧化石墨烯（G/GO）纳米片，系统比较370/450/808 nm激光对其湿度传感性能的调控，发现450 nm蓝光因光子能量足以克服GO带隙与激子结合能，使传感器在灵敏度、线性度、响应/恢复速度（1.0 s/1.3 s）上全面最优。
--- XiaokangZhang2013calibrating ---
title: Calibrating an optical fiber humidity sensor and applying it in real-time monitoring of relative humidity in fresh concrete
one: 制备了一种琼脂糖涂覆的双层包层单模光纤（DCSMF）湿度传感器，首次系统研究其在 25–34 °C、30–100% RH 范围内的温-湿耦合响应，提出基于查找表/校准矩阵的工程化校准方法，并成功埋入新拌混凝土实现 33 小时内部相对湿度与温度的实时原位监测。
--- Yarai2005optical ---
title: Optical fiber sensor for humidity monitoring based on thermal lens detection technique
one: 首次将热透镜（TL）泵浦-探测光谱技术引入光纤湿度传感，用两根端面间距 <50 μm 的球透镜光纤构成微腔传感头，在泵浦功率 <100 mW 下实现了无需对光纤包层做任何化学处理的湿度测量，并证明传感器本质上测量的是绝对湿度。

===== remanent-polarization (papers=6) =====
cites: Kim2008effect, RecentAdvancesGrowth2025, caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, heUltrafastSwitchingDynamics2024, tahirFerroelectricityNonvolatileMemristor2025, zhangEmergingFrontiersTwodimensional2025
--- Kim2008effect ---
title: Effect of epitaxial strain on ferroelectric polarization in multiferroic BiFeO3 films
one: 通过厚度梯度（40–960 nm）系统证明 BiFeO₃ 薄膜从高应变四方相（c/a≈1.04）弛豫到近菱形相（c/a≈1.01）时，沿伪立方 [111] 的本征铁电极化仅变化 1.6%，所测 Pr 的微弱变化主要源于极化矢量随 c/a 比的几何旋转，揭示孤对电子驱动铁电性对外延应变的本征不敏感性。
--- RecentAdvancesGrowth2025 ---
title: Recent advances in growth, characterization, and application of two-dimensional multiferroic materials
one: 系统综述二维多铁材料（重点为 II 型铁磁-铁电/铁磁-铁弹体系）的分类、CVD/PVD/MBE/ALD 生长方法、STM/SHG/拉曼/太赫兹等表征工具箱及六大器件应用，并以 NiI₂、Cr₂S₃、CuCrSe₂、p 型 SnSe 为里程碑案例。
--- caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025 ---
title: Ferroelectricity-driven strain-mediated magnetoelectric coupling in two-dimensional multiferroic heterostructure
one: 在 Fe3GaTe2/P(VDF-TrFE) 双栅二维多铁异质结中，利用底栅铁电聚合物的逆压电效应诱导应变，室温下非易失、全电学可逆地调控 Fe3GaTe2 的磁各向异性常数 K1，并演示了 0.5 aJ/5 ns 的可重构自旋逻辑门、半加器及二分类神经网络。
--- heUltrafastSwitchingDynamics2024 ---
title: Ultrafast switching dynamics of the ferroelectric order in stacking-engineered ferroelectrics
one: 基于DFT数据训练深度势能（DP）机器学习势，对h-BN双层中铁电畴壁进行大规模原子模拟，揭示畴壁运动将临界翻转场降低两个数量级、实现皮秒级翻转，并阐明扭转莫尔结构的超顺电本质。
--- tahirFerroelectricityNonvolatileMemristor2025 ---
title: Ferroelectricity and Nonvolatile Memristor Applications of Free‐Standing 2D Niobium Carbide: A New Frontier of Free‐Standing MXene in Electronic Devices
one: 首次在自支撑二维 Nb₂CTₓ MXene 薄膜上观测到铁电性（1000 Hz 下剩余极化 Pr = 5.12 μC/cm²，为当时自支撑 MXene 最高值），并以其本征氧空位作为开关层构筑了 Ti₃C₂Tₓ/Nb₂CTₓ/Ti₃C₂Tₓ 与 rGO/Nb₂CTₓ/rGO 两种非易失性双极阻变忆阻器。
--- zhangEmergingFrontiersTwodimensional2025 ---
title: Emerging frontiers in two-dimensional sliding ferroelectrics
one: 系统梳理二维范德华材料中"滑动铁电性"的材料体系、五种打破反演对称性的工程策略、层间滑移翻转的微观机制（层间电荷转移、逐层翻转、拓扑畴壁扭结）以及柔性存储/FTJ/超快光电/神经形态器件应用，并指出理论-实验鸿沟、动力学黑箱、性能跷跷板与规模化制备四大挑战。

===== two-photon-excitation (papers=6) =====
cites: H2017fluorescence, Huang2019solvatochromic, Huang2023two, Khitrov2002internal, Nakanishi2009full, WRZYSZCZYNSKI2010initiators
--- H2017fluorescence ---
title: Dicyanostilbene-based Two-photon Thermo-solvatochromic Fluorescence Probes with Two-photon Triple Fluorescence
one: 作者通过在二苯乙烯骨架上引入邻/间位双氰基受体和二甲氨基给体，构建了 D-π-A 型分子 P1，实现了 445→641 nm 的超宽溶剂化变色、最高 5560 GM 的双光子吸收截面，并首次在双光子激发下观察到由 LE / TICT / Exciplex 三态构成的三重荧光，可同时传感极性、粘度和温度。
--- Huang2019solvatochromic ---
title: Stilbene-Based Two-Photon Thermo-Solvatochromic Fluorescence Probes with Large Two-Photon Absorption Cross Sections and Two-Photon Triple Fluorescence: Detection of Solvent Polarities, Viscosities, and Temperature
one: 在二苯乙烯单芳环上同时引入邻/间位双氰基与二甲氨基，构建出 D-π-A 型探针 P1，其发射峰随溶剂极性从 445 nm 红移至 641 nm（≈196 nm），双光子吸收截面最高达 6670 GM，并首次在双光子激发下观察到 LE/TICT/Exciplex 三重荧光，可同时响应极性、粘度和温度。
--- Huang2023two ---
title: Two Dicyanostilbene-Based Two-Photon Fluorescence Environmentally Sensitive Probes with Large Two-Photon Absorption Cross Sections and Two-Photon Triple Fluorescence
one: 在二苯乙烯骨架的单个苯环上引入 2,5-二氰基受体搭配强给体二甲氨基，得到溶剂化显色位移达 196 nm、双光子吸收截面高达 5560 GM 的探针 1a，并首次在双光子激发下观察到由 LE / TICT / 分子间激基复合物构成的三重荧光。
--- Khitrov2002internal ---
title: Internal Defects Observed by Two-Photon-Induced Photoluminescence
one: 报道了利用飞秒钛宝石激光双光子激发在多晶 ZnSe 内部 200 μm 深度实现三维缺陷光致发光成像（同期栏目还介绍了 Si/SiGe 超晶格纳米线、单根碳纳米管悬浮、稀土掺杂 GaN 横向颜色集成三项进展）。
--- Nakanishi2009full ---
title: Full Quantum Analysis of Two-Photon Absorption Using Two-Photon Wave Function: Comparison of Two-Photon Absorption with One-Photon Absorption
one: 建立基于双光子波函数的全量子多模理论，解析给出任意光子对态的单/双光子吸收概率，并证明矩形时间窗波函数在 Δ·τ = π(2n+1) 时可完全抑制单光子吸收而保持双光子吸收，即"纠缠诱导双光子透明"。
--- WRZYSZCZYNSKI2010initiators ---
title: Two-photon initiators of polymerization
one: 本文系统综述双光子聚合引发剂的物理机制（顺序/同时双光子吸收）、分子设计准则（D-π-D / D-π-A-π-D / A-π-D-π-A）、代表性化合物类别（二苯乙烯衍生物、噻嗪染料、三苯胺、香豆素/酮香豆素二元体系等）及其在三维微纳加工中的应用优势。