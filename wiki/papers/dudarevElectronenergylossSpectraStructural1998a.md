---
citekey: dudarevElectronenergylossSpectraStructural1998a
title: "Electron-energy-loss spectra and the structural stability of nickel oxide:  An LSDA+U study"
title_zh: "电子能量损失谱和氧化镍的结构稳定性：  LSDA+U研究"
authors: [S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, A. P. Sutton]
year: 1998
journal: "Physical Review B"
doi: "10.1103/PhysRevB.57.1505"
url: "https://doi.org/10.1103/PhysRevB.57.1505"
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/dudarevElectronenergylossSpectraStructural1998a]]
projects: []
concepts: [density-functional-theory, NiO, hubbard-u, mott-insulator, double-counting-correction, electron-energy-loss-spectroscopy, lsda-plus-u]
entities: []
methods: [dft, dft-plus-u]
materials:
  - NiO
figures: [crystal-structures-bulk, mathematical-models-computational, mathematical-models-formulas, mathematical-models-simulations]
领域基础知识:: >-
  密度泛函理论(DFT)、局域自旋密度近似(LSDA)在处理含d/f电子的强关联体系（如过渡金属氧化物）时，因无法准确描述电子间强库仑排斥(Hubbard U)而失效，导致预测的电子结构与基态性质系统性地偏离实验。
研究背景:: >-
  传统DFT-LSDA方法错误预测氧化镍(NiO)为金属或严重低估其绝缘带隙，并低估晶格常数、高估结合能，根源在于对Ni离子3d电子强关联效应描述不足，亟需能统一描述其激发谱与基态性质的理论方法。
作者的问题意识:: >-
  能否通过一个改进的、考虑3d电子强关联的LSDA+U计算方法，在同一个理论框架下、用同一组参数，同时精确描述NiO的电子激发谱（如EELS）和结构稳定性（如晶格常数、弹性模量），从而建立将光谱模拟与材料基态性质研究相联系的桥梁？
主要研究对象:: >-
  具有反铁磁结构的莫特绝缘体——氧化镍(NiO)晶体，特别是其镍离子的3d电子态。
主要研究方法:: >-
  采用基于全势线性丸盒轨道（FP-LMTO）程序实现的LSDA+U第一性原理计算方法，通过计算氧2p空态密度模拟电子能量损失谱（EELS），并与实验测量值对比；同时计算总能量随晶格常数的变化，推导结构参数。
研究意义:: >-
  首次证明LSDA+U方法能够用一个物性合理的Hubbard U值，统一并精确地描述NiO的电子激发谱和基态结构稳定性，验证了该方法在过渡金属氧化物研究中的有效性，为后续精确研究其表面与缺陷开辟了道路。
研究结论:: >-
  使用LSDA+U方法，取有效Hubbard U=6.2 eV，Hund耦合J=0.95 eV，计算结果在氧K边EELS谱、晶格常数(4.19 Å)、结合能(11.60 eV)和弹性模量上均与实验值显著优于LSDA结果；物理机制是U的引入增强了3d电子局域化，减弱了Ni-O共价键合。
对领域的贡献:: >-
  1. 提供了LSDA+U方法能够统一描述强关联体系光谱和结构性质的关键证据。2. 建立了通过EELS等光谱实验来校准理论计算中关键的Hubbard U参数的方法论。3. 为计算材料学领域提供了研究NiO及其他过渡金属氧化物表面与缺陷的可靠计算方案。
未来研究方向提及:: >-
  文中展望将LSDA+U方法应用于NiO的表面结构、缺陷结构以及对应的扫描隧道显微镜(STM)图像模拟等更复杂的从头算研究中。
未来研究方向思考:: >-
  1. 探索动态U值或结合GW方法，以进一步修正LSDA+U对NiO带隙的低估。2. 系统研究该U值在不同NiO表面、缺陷、以及不同过渡金属氧化物中的可迁移性。3. 研究LSDA+U方法对NiO磁交换耦合常数、声子谱等非基态/非光谱性质的预测能力。
tags:
  - paper
  - type/experiment
  - year/1998
  - concept/density-functional-theory
  - method/dft
  - method/dft-plus-u
  - method/stm-mbe
  - method/tem
  - topic/ferromagnetism
  - topic/multiferroics
---

## dudarevElectronenergylossSpectraStructural1998a — 电子能量损失谱和氧化镍的结构稳定性：LSDA+U研究
## 📄 元数据
S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, A. P. Sutton et al.，1998，Physical Review B 57(3), 1505-1509，DOI: 10.1103/PhysRevB.57.1505
## 💡 一句话
用同一个有效 Hubbard U（6.2 eV）在 LSDA+U 框架下同时准确描述了 NiO 的氧 K 边 EELS 激发谱和基态结构稳定性参数（晶格常数、结合能、弹性模量），证明该方法能统一处理强关联过渡金属氧化物的光谱与结构性质。
## 🔗 Wiki 双链
本文涉及且 wiki 中已存在的条目，用双链列出（存在才链）：
  - 概念 [[../concepts/density-functional-theory]]、[[../concepts/lsda-plus-u|LSDA+U]]、[[../concepts/hubbard-u|Hubbard U]]、[[../concepts/mott-insulator|莫特绝缘体]]、[[../concepts/double-counting-correction|双计数修正]]、[[../concepts/electron-energy-loss-spectroscopy|电子能量损失谱（EELS）]]、[[../concepts/NiO|氧化镍（NiO）]]
  - 年度 [[../write/1945-1999|1998]]
  - 相关论文 [[../../raw/note/dudarevElectronenergylossSpectraStructural1998a]]
## 📊 关键图表
列出本文关键图
  - **图1**：
  - ![图1 上：氧K边EELS实验谱与LSDA/LSDA+U计算的O 2p空态DOS对比；下：总能量随晶格常数变化曲线](../../raw/figures/dudarevElectronenergylossSpectraStructural1998a/fig_1_D42XHL87.png) -> [[../figures/mathematical-models-simulations|模拟与数值结果]]
  - **图示描述**：上半部分为归一化的氧 K 边实验 EELS 谱（实线，能量轴已平移 528.3 eV 以对齐 O 1s 芯能级）与 LSDA、LSDA+U（Ū=6.2 eV 和 8.0 eV）计算的 O 2p 空态密度（虚线，经高斯展宽模拟 0.4–0.5 eV 仪器/寿命分辨率）的对比；下半部分为 LSDA 与 LSDA+U 每 NiO 单元总能量随晶格常数的变化曲线。
  - **关键特征**：(1) LSDA 两主峰间距比实验大 ~2 eV，且低能 O 2p–Ni 3d 杂化峰权重过高；(2) Ū=6.2 eV 时两峰间距与低能峰强度均显著贴近实验，Ū=8.0 eV 也优于 LSDA 但峰距偏差稍大；(3) 能量极小值从 LSDA 的 4.08 Å 右移至 LSDA+U（Ū=6.2 eV）的 4.19 Å，接近实验值 4.17 Å（Ū=8.0 eV 给出 4.22 Å）；(4) 对应的 LSDA+U 带隙为 3.0 eV（Ū=8.0 eV 为 3.2 eV），高于 LSDA 的 0.6 eV 但仍低于实验 4.2 eV。
  - **结论/意义**：同一 Ū=6.2 eV 同时再现光谱的峰位/峰强和结构的平衡晶格常数，是 LSDA+U 方法统一描述 NiO 激发谱与基态结构的核心证据。
  - **图2**：
  - ![图2 上：NiO岩盐结构；下：(100)面 LSDA+U 与 LSDA 电荷密度差，显示间隙区电荷密度减少、共价键减弱](../../raw/figures/dudarevElectronenergylossSpectraStructural1998a/fig_2_GBIMQZ9U.png) -> [[../figures/crystal-structures-bulk|体相晶体结构]]
  - **图示描述**：上图为 NiO 岩盐（NaCl 型）晶体结构示意（白球为氧、灰球为镍）；下图为在 (100) 晶面上 LSDA+U（Ū=6.2 eV）相对于 LSDA 的电荷密度差 Δρ = ρ(LSDA+U) − ρ(LSDA) 的空间分布。
  - **关键特征**：(1) Ni–O 之间的间隙区域 Δρ 为负，即 LSDA+U 下该区域成键电荷减少；(2) 电子云收缩至 Ni 离子周围，反映 3d 电子因在位库仑排斥而更局域；(3) 该图像与图1 中低能 O 2p–Ni 3d 杂化峰被压低、向高能移动完全自洽，而对应 O 2p–Ni 4s/4p 的高能峰几乎不受影响，体现 U 的轨道选择性。
  - **结论/意义**：从实空间电荷分布上阐明了 U 使平衡晶格常数增大的微观机制——减弱 Ni–O 共价键合、键网"松弛"。
  - **公式(1)**：
  - ![公式(1) 含轨道简并的模型哈密顿量，含Ū和J̄两项](../../raw/figures/dudarevElectronenergylossSpectraStructural1998a/eq_1_Q5JBCHIW.png) -> [[../figures/mathematical-models-formulas|光学、输运与其他解析公式]]
  - **图示描述**：考虑 3d 壳层五重轨道简并的 Hubbard 模型哈密顿量，求和遍及轨道投影 m, m′（d 电子取 −2…2）与自旋 σ；第一项系数为 Ū/2（相反自旋、含 m=m′ 自身相互作用），第二项系数为 (Ū−J̄)/2（同自旋、m≠m′）。
  - **关键特征**：(1) Ū 为球平均屏蔽库仑矩阵元（有效在位排斥），J̄ 为球平均 Hund 交换；(2) 对单轨道 Hubbard 模型退化为 (U/2)Σ_σ n̂_σ n̂_{−σ}；(3) 固定 J̄=0.95 eV，本文主要变化 Ū。
  - **结论/意义**：是后续推导整数/非整数占据能量差、构造 LSDA+U 泛函的出发点。
  - **公式(4)**：
  - ![公式(4) LSDA+U总能量泛函（对角占据数形式）](../../raw/figures/dudarevElectronenergylossSpectraStructural1998a/eq_4_UT7YQAUM.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：E_LSDA+U = E_LSDA + (Ū−J̄)/2 · Σ_σ (n_m,σ − n²_m,σ)，其中 n_m,σ 为第 m 个 d 轨道的占据数；该式由非整数占据的 UHF 能量表达式减去整数占据下的密度泛函表达式得到。
  - **关键特征**：(1) 修正项在整数占据（n=0 或 1）时为零，保证不破坏原子参考态；(2) 在半占据 n=1/2 时惩罚最大，强制轨道占据两极分化，从而打开关联带隙；(3) 形式上是 Anisimov 轨道依赖 LSDA+U 的简化版本。
  - **结论/意义**：定义了 LSDA+U 的能量修正，是计算 O 2p DOS 与总能量曲线的实际泛函。
  - **公式(5)**：
  - 公式(5) 旋转不变的LSDA+U泛函 E_LSDA+(Ū-J̄)/2 Σ_σ[Trρ^σ-Tr(ρ^σρ^σ)]（笔记未附该公式图片）
  - **图示描述**：将公式(4)中对角占据数推广为 d 电子密度矩阵 ρ^σ，得到旋转不变形式 E_LSDA+U = E_LSDA + (Ū−J̄)/2 · Σ_σ [Tr(ρ^σ) − Tr(ρ^σ ρ^σ)]。
  - **关键特征**：(1) 对 d 轨道空间的任意幺正变换（如实 d 轨道基与球谐基之间）保持不变；(2) 桥接 Anisimov 等的轨道依赖形式与 Liechtenstein 等的旋转不变泛函；(3) 整数占据极限下第二项消失，使该泛函可一致计算固体内聚能。
  - **结论/意义**：克服了早期 LSDA+U 对轨道基组选择的依赖，是实际可在任意程序中实现的协变形式。
  - **公式(6)**：
  - ![公式(6) 单电子势矩阵元 V_jl^σ = δE_LSDA/δρ_jl^σ + (Ū-J̄)(δ_jl/2 - ρ_jl^σ)](../../raw/figures/dudarevElectronenergylossSpectraStructural1998a/eq_6_KX36V9IK.png) -> [[../figures/mathematical-models-formulas|光学、输运与其他解析公式]]
  - **图示描述**：对公式(5)关于密度矩阵元 ρ_{jl}^σ 求变分导数得到的单电子势矩阵：V_{jl}^σ = δE_LSDA/δρ_{jl}^σ + (Ū−J̄)(δ_{jl}/2 − ρ_{jl}^σ)。
  - **关键特征**：(1) 第二项 (Ū−J̄) 作用于已占据轨道（ρ→1）时为负、未占据轨道（ρ→0）时为正，从而把占据态下移、空态上移、打开带隙；(2) 非对角元使势本身也是密度矩阵的函数，需自洽求解；(3) 是 FP-LMTO 自洽循环中实际进入 Kohn–Sham 方程的势。
  - **结论/意义**：把能量泛函转化为可数值求解的单电子势，是 LSDA+U 自洽计算的执行方程。
  - **公式(7)**：
  - ![公式(7) 用Kohn-Sham本征值表示的总能量，含双计数修正项](../../raw/figures/dudarevElectronenergylossSpectraStructural1998a/eq_7_YP9VVUC6.png) -> [[../figures/mathematical-models-formulas|光学、输运与其他解析公式]]
  - **图示描述**：用 Kohn–Sham 本征值 {ε_i} 重写总能量：E_LSDA+U = E_LSDA[{ε_i}] + (Ū−J̄)/2 · Σ_{l,j,σ} ρ_{lj}^σ ρ_{jl}^σ，其中末项为双计数修正。
  - **关键特征**：(1) 末项减去被 E_LSDA[{ε_i}] 重复计入的在位平均库仑能；(2) 与整数占据消去性质配合，使原子与固体参考态一致；(3) 是输出表1中结合能、弹性模量等结构量的总能量表达式。
  - **结论/意义**：给出实际计算总能量（及晶格常数、内聚能、体弹/剪切模量）所使用的表达式。

## 🔬 项目连接
无直接项目连接。本文是 LSDA+U 方法学奠基性 work，所验证的 DFT+U 方案是计算过渡金属氧化物（含 project-2 Mn 多铁体系）电子结构的通用工具，但本文研究对象为 NiO，与七个项目均无直接数据或材料连接。
## 🔗 项目双链

## 📝 组织与用词
文章按"问题提出（LSDA 对过渡金属氧化物失效）→ 方法构建（推导旋转不变 LSDA+U 泛函与单电子势）→ 双重验证（EELS 谱对比 + 总能量/结构参数计算）→ 机制解释（电荷密度差揭示共价键减弱）→ 结论"组织，论证链条清晰，光谱与结构两条证据线在同一 U 值下汇合。值得复用的术语：
  - **LSDA+U / DFT+U**（局域自旋密度近似加 U）
  - **Hubbard U / on-site Coulomb repulsion**（[[../concepts/hubbard-u|Hubbard U]] / 在位库仑排斥）
  - **EELS ([[../concepts/electron-energy-loss-spectroscopy|Electron Energy-Loss Spectroscopy]])**（电子能量损失谱）
  - [[../concepts/mott-insulator|**Mott insulator**]]（莫特绝缘体）
  - **rotational invariance**（旋转不变性）
  - [[../concepts/double-counting-correction|**double counting correction**]]（双计数修正）
  - **covalent bonding / hybridization**（共价键合 / 杂化）
  - **cohesive energy**（内聚能/结合能）
  - [[../concepts/cohesive-energy|cohesive-energy]]
## ✏️ 可写入 Wiki 的要点
  1. **LSDA 对 NiO 的系统性失效**：LSDA 预测晶格常数 4.08 Å（实验 4.17 Å）、带隙仅 0.6 eV（实验 4.2 eV）、[[../concepts/cohesive-energy|内聚能]] 13.74 eV（实验 8.26 eV）；即使计入反铁磁序得到绝缘态，带隙仍比实验小一个数量级。Hartree-Fock 则走向另一极端（带隙 14.2 eV、晶格常数 4.26 Å、内聚能 6.2 eV）。
  2. **LSDA+U 统一参数（Ū=6.2 eV, J̄=0.95 eV）的结果**：晶格常数 4.19 Å、带隙 3.0 eV、内聚能 11.60 eV、体弹模量 B=182 GPa、剪切模量 C'=161 GPa、C44=86 GPa，均介于 LSDA 与 HF 之间，整体最接近实验值（4.17 Å、4.2 eV、8.26 eV）。
  3. **U 值的确定**：约束 LSDA 给出 Ū=8.0 eV（未计 d 电子自屏蔽，偏高）；通过匹配 EELS 两主峰间距选定 Ū=6.2 eV，与经验值 6.7 eV 接近；同一 U 值同时预测出合理的结构参数。
  4. **旋转不变 LSDA+U 泛函**：E_LSDA+U = E_LSDA + (Ū−J̄)/2 · Σ_σ [Tr(ρ^σ) − Tr(ρ^σρ^σ)]，该式桥接了 Anisimov 等的轨道依赖形式与 Liechtenstein 等的旋转不变泛函；单电子势为 V_jl^σ = δE_LSDA/δρ_jl^σ + (Ū−J̄)(δ_jl/2 − ρ_jl^σ)。
  5. **整数占据极限的消去性质**：在整数占据数极限下，非整数占据的 UHF 表达式与整数占据的密度泛函表达式精确抵消，使式(5)右侧修正项为零，因此该泛函可正确计算固体的内聚能（避免原子参考态与固体间的不一致）。
  6. **EELS 验证的物理细节**：氧 K 边对应 O 1s→空 2p 偶极跃迁，近边结构直接反映氧位 p 对称空态 DOS；将计算的 O 2p DOS 与高斯函数卷积以模拟[[../concepts/excited-state-lifetime|激发态寿命]]和仪器展宽（能量分辨率 0.4–0.5 eV，冷场发射枪 + Gatan GIF 678）。LSDA 两主峰间距比实验大约 2 eV 且低能峰（O 2p–Ni 3d 杂化峰）权重过高；LSDA+U 将该峰推向高能并压低其强度。
  7. **U 修正结构的微观机制**：[[../concepts/charge-density|电荷密度]]差 Δρ=ρ(LSDA+U)−ρ(LSDA) 显示 Ni–O 间隙区电荷密度减少，表明在位库仑排斥使 Ni 3d 电子更局域、减弱 Ni–O 共价键合，从而使晶格膨胀、平衡晶格常数增大；EELS 低能峰减弱与该图像自洽。U 对 O 2p–Ni 4s/4p 杂化的高能峰几乎无影响，体现轨道选择性。
  8. **失效根源与方法定位**：d 电子有效在位库仑作用强度与价带宽度相当，导致电子转移引起大幅能量涨落、载流子局域化与带隙形成；LSDA+U 本质是 LSDA（平均场、偏离域）与 UHF（精确交换、偏局域）的折衷，适用于轨道有序明显的[[../concepts/mott-insulator|莫特绝缘体]]，但仍为基态理论，带隙（3.0 eV）低于实验（4.2 eV），未含动态关联与激子效应。
  9. **计算实现细节**：全势 LMTO（FP-LMTO）程序，Moruzzi-Janak-Williams 交换关联势，三个能量面板、[[../concepts/brillouin-zone|布里渊区]] 343 个 k 点；NiO 取反铁磁基态（磁面平行于 (111) 面）。
  10. **方法学意义**：首次表明光谱特征（EELS 峰间距/峰强）可作为校准 Hubbard U 的独立实验探针，且校准所得 U 可迁移用于预测同一材料的基态结构性质，为过渡金属氧化物表面、缺陷及 STM 图像的从头算研究提供了可靠方案。