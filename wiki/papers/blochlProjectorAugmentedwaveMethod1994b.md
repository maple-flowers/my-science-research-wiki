---
citekey: blochlProjectorAugmentedwaveMethod1994b
title: "Projector augmented-wave method"
authors: [P. E. Blöchl]
year: 1994
journal: "Physical Review B"
doi: "10.1103/PhysRevB.50.17953"
url: "https://doi.org/10.1103/PhysRevB.50.17953"
paper_type: method
status: ingested
year_read: 2026
original_note:: [[../../raw/note/blochlProjectorAugmentedwaveMethod1994b]]
projects: [project-2, project-7, project-5, project-4]
concepts: [density-functional-theory, paw-method, pseudopotential, lapw, projector-functions, augmentation-region, compensation-charge-density, frozen-core-approximation, additive-augmentation, car-parrinello, norm-conservation, overlap-operator, pulay-force]
entities: [VASP, LAPW, LMTO, Car-Parrinello, MnFO3, Fe2]
methods: [dft, lda, paw, all-electron, pseudopotential, ultrasoft-pseudopotential, car-parrinello-md, plane-wave-basis, radial-grid]
materials: [Mn, Fe, O, F, H, Li, Be, B, N, transition-metals]
figures: [partial-waves, scattering-properties, wave-function-accuracy, energy-conservation-md, plane-wave-convergence, convergence-binding-energy, convergence-bond-length]
领域基础知识:: >-
  第一性原理密度泛函理论（DFT），全电子（AE）方法，赝势（Pseudopotential）方法，线性增强平面波（LAPW）方法，Car-Parrinello分子动力学。
研究背景:: >-
  电子结构计算方法是精确预测材料性质的核心，但主流方法存在鸿沟：全电子方法（如LAPW）精度高但计算复杂，赝势方法效率高但对许多元素（如过渡金属）精度受限或变得“硬”。迫切需要一种能结合二者优势的新方法。
作者的问题意识:: >-
  如何构建一个统一的电子结构计算框架，既能像赝势方法那样利用平滑波函数进行高效计算，又能像LAPW方法那样精确重构出全电子波函数，从而在保持高精度的同时实现高质量的分子动力学模拟？
主要研究对象:: >-
  投影增强波（PAW）方法的理论框架、构建方案、数值表现及其与现有方法（LAPW、赝势）的关系。
主要研究方法:: >-
  构建了一个从平滑赝（PS）波函数到全电子（AE）波函数的线性变换，通过引入全电子分波、赝分波和投影函数来定义此变换。基于此变换，推导了总能量、哈密顿量和力的表达式，并结合Car-Parrinello虚拉格朗日量方法，实现第一性原理分子动力学。通过原子散射、双原子分子等测试进行数值验证。
研究意义:: >-
  首次在理论上统一了增强波方法和赝势方法，证明LAPW是其特例，赝势是其近似。提供了一个兼具全电子精度和赝势效率的全新计算范式，并首次实现了基于全电子波函数的、能量守恒的分子动力学模拟。
研究结论:: >-
  PAW方法成功弥合了全电子方法和赝势方法之间的鸿沟。它能够以中等的计算代价（如30 Ry平面波截断）获得与最先进全电子方法相当的精度，并可以进行高质量的分子动力学模拟。其精度和效率优于传统赝势，尤其在处理“硬”元素时。
对领域的贡献:: >-
  1. 提出了PAW方法这一革命性的理论框架，成为现代高精度DFT计算（如VASP软件）的基石。2. 深刻揭示了不同电子结构计算方法之间的内在联系与统一性。3. 提供了可操作的“配方”来构建分波和投影函数，为方法普及铺平了道路。
未来研究方向提及:: >-
  1. 发展自适应分波，使其能根据实际化学环境进行优化。2. 超越冻结核心近似，实现核心电子态的弛豫。3. 将赝波函数与平面波以外的其他基组结合。
未来研究方向思考:: >-
  1. 探索机器学习方法自动生成更优的PAW势，以平衡精度与效率。2. 发展基于PAW方法的超越DFT的计算方法，如GW、BSE等，用于激发态和光谱计算。3. 将PAW方法拓展到强关联体系，例如与动力学平均场论（DMFT）结合。4. 研究PAW方法在计算核磁共振（NMR）、电子顺磁共振（EPR）等依赖核区波函数精细性质时的系统误差与改进方案。
tags:
  - paper
  - type/method
  - year/1994
  - project/project-2
  - project/project-7
  - project/project-5
  - project/project-4
  - relevance/project-2/core
  - relevance/project-7/strong
  - relevance/project-5/medium
  - relevance/project-4/weak
  - concept/density-functional-theory
  - concept/paw-method
  - concept/pseudopotential
  - concept/lapw
  - concept/projector-functions
  - concept/augmentation-region
  - concept/compensation-charge-density
  - concept/frozen-core-approximation
  - concept/additive-augmentation
  - concept/car-parrinello
  - concept/norm-conservation
  - concept/overlap-operator
  - concept/pulay-force
  - entity/VASP
  - entity/LAPW
  - entity/LMTO
  - entity/Car-Parrinello
  - entity/MnFO3
  - entity/Fe2
  - method/dft
  - method/lda
  - method/paw
  - method/all-electron
  - method/pseudopotential
  - method/ultrasoft-pseudopotential
  - method/car-parrinello-md
  - method/plane-wave-basis
  - method/radial-grid
  - material/Mn
  - material/Fe
  - material/transition-metals
  - topic/computational-materials
  - topic/electronic-structure
  - topic/molecular-dynamics
---

## blochlProjectorAugmentedwaveMethod1994b — 投影增强波法（Projector Augmented-Wave Method, PAW）

## 📄 元数据
P. E. Blöchl，1994，Physical Review B 50(24), 17953–17979，DOI: 10.1103/PhysRevB.50.17953
## 💡 一句话
本文提出投影增强波（PAW）方法，通过一个由全电子分波、赝分波和投影函数定义的线性变换，将全电子 LAPW 方法的精度与平面波赝势方法的效率统一起来，并首次实现基于完整波函数的能量守恒第一性原理分子动力学。

## 🔗 Wiki 双链
  - 概念 [[../concepts/density-functional-theory|密度泛函理论（DFT）]]
  - 概念 [[../concepts/paw-method|投影增强波（PAW）]]
  - 概念 [[../concepts/pseudopotential|赝势]]
  - 概念 [[../concepts/projector-functions|投影函数]]
  - 概念 [[../concepts/augmentation-region|增强区域]]
  - 概念 [[../concepts/compensation-charge-density|补偿电荷密度]]
  - 概念 [[../concepts/additive-augmentation|加法缀加]]
  - 概念 [[../concepts/frozen-core-approximation|冻结芯近似]]
  - 概念 [[../concepts/overlap-operator|重叠算符]]
  - 实体 [[../entities/VASP]]
  - 实体 [[../entities/Wannier90]]（PAW 部分波形式天然适合构造 Wannier 轨道）
  - 年度 [[../write/1994]]
  - 相关论文 **blochlProjectorAugmentedwaveMethod1994b**

## 📊 关键图表
  - 图1：Mn 原子的全电子分波（实线）、赝分波（虚线/点划线）与投影函数（s/p/d 通道），3s、3p 作为价态处理。
  ![Mn 的分波与投影函数](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/fig_1_MBXMFE5N.png) -> [[../figures/electronic-bands|电子能带与电子态]]
  - 图2：Mn 原子散射性质（对数导数 D_l(ε) 随能量），单分波（虚线）价区偏差大，两分波（实线）在占据态以上约 1.5 Ry 内精确。
  ![Mn 原子散射性质](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/fig_2_TFC3U9WB.png) -> [[../figures/electronic-bands|电子能带与电子态]]
  - 图3：Mn 原子波函数精度比较。价带能量 −8.16 eV 时 PAW 重构 AE 波函数与精确解误差 <1%；高能 +13.61 eV 时 s 波约 15% 偏差，为分波截断的典型特征。
  ![Mn 原子波函数精度](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/fig_3_VUN7LY3T.png) -> [[../figures/mathematical-models|数学模型与物理公式]]
  - 图4：Fe₂ 第一性原理分子动力学能量演化。守恒能量（实线）在 0.5 ps 内漂移 <0.8 meV，无单调漂移，振动周期对应 441 cm⁻¹，证明全波函数能量守恒 MD 的可行性。
  ![Fe2 分子动力学能量守恒](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/fig_4_7SIKWYXK.png) -> [[../figures/heterostructures-stacking-mechanics-misc|力学性质、剥离能与杂项]]
  - 图5：第一行元素及 Fe 原子总能量的平面波收敛性，30–40 Ry 达到 0.1 eV 精度。
  ![原子总能量平面波收敛性](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/fig_5_F273ESRL.png) -> [[../figures/electronic-bands|电子能带与电子态]]
  - 图6：双原子分子结合能的平面波收敛性，30 Ry 时误差 <0.1 eV，比绝对总能量收敛更快。
  ![结合能平面波收敛性](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/fig_6_SXMJN2H7.png) -> [[../figures/electronic-bands|电子能带与电子态]]
  - 图7：双原子分子键长的平面波收敛性，30 Ry 时键长精确到 0.02 a₀（<1%）。
  ![键长平面波收敛性](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/fig_7_4YR3MYMF.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - 表I：构造 PS 分波所用参数（截断参数 A=6，各原子的 ṽ_ps(0)、匹配半径等）。
  ![表I PS分波构造参数](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/tab_6_8N64J9RS.png) -> [[../figures/electronic-bands|电子能带与电子态]]
  - 表II：30 Ry 截断下 H₂、Li₂、Be₂、B₂、N₂、O₂、F₂、Fe₂ 等二聚体的结合能、键长、振动频率与其他全电子 LDA 计算的对比（键长偏差 <1%，频率偏差约 4%，结合能偏差 0.1–0.2 eV）。
  ![表II 二聚体性质对比](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/tab_30_9X7NQLGJ.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]

## 🔬 项目连接
  - **project-2 Mn多铁（core）**：项目子课题明确使用 VASP 做多孔 MoS₂、多层黑磷、高通量 DFT 计算，且核心材料含 Mn（BiFeO₃、HoMnO₃、Mn 基多铁）。PAW 正是 VASP 的默认电子结构表示，本文是理解 VASP 中 PAW 势、截断能选择、半芯态处理（3s/3p）、Mn/Fe 等过渡金属 d 电子为何需要两分波的原始文献，直接决定计算精度与收敛性判断，属核心方法文献。
  - **project-7 CDW（strong）**：项目对 CrS₂、VTe₂、MnX₂ 等 TMD 做 DFT 计算（1T/1T′ 结构、DOS、电荷掺杂、磁耦合），这些过渡金属二硫属化物的 DFT 几乎都依赖 PAW 势处理 Cr/V/Mn 的 d 电子与 S/Te 的价电子。本文关于过渡金属用四阶多项式匹配 PS 势、每角动量两分波处理窄 d 态、30 Ry 收敛标准等内容可直接指导其 INCAR/POTCAR 选择与收敛性测试。
  - **project-5 SnTe铁电模拟（medium）**：项目主体用 LAMMPS/DeepMD 做势函数与铁电动力学，但其训练标签与参考能量/力通常来自 DFT（VASP/QE，均用 PAW）。理解 PAW 对 Sn（半芯态 4d）、Te 重元素的处理、自旋-轨道耦合扩展（本文已展望）对评估 DFT 参考数据质量、Berry 相极化计算的精度有方法参考价值；体项目本身不直接做 PAW 级开发，故定为 medium。
  - **project-4 TTF分子计算（weak）**：项目以 UFF/LAMMPS/MACE/DeepMD 分子模拟为主，涉及 TTF 有机分子（C/S/H），不直接做平面波 DFT。但若用 DFT 生成训练数据或做单点能参考，PAW 对第一行元素（C/N/O/F/S）的处理结论（一分波即可、30 Ry 收敛）有间接参考意义，故定为 weak。
  - **project-1 双光子 / project-3 机械发光NN / project-6 湿度传感器**：无直接项目连接（光学/ML/器件实验为主，不涉及平面波 DFT 电子结构方法）。

## 🔗 项目双链
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]
- 项目 [[../projects/project-7-cdw-charge-density-wave|项目七：CDW电荷密度波]]
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]
- 项目 [[../projects/project-4-ttf-molecular-calc|项目四：lsl老师的ttf分子计算]]

## 📝 组织与用词
  文章按"形式理论（II）→实用近似（III）→力/哈密顿量/重叠矩阵（IV）→Car-Parrinello 分子动力学（V）→分波与投影函数构造（VI）→截断误差分析与扩展（VII）→数值测试（VIII）→与现有方法比较（IX）"的总-分-总结构组织。先给最一般线性变换，再逐层落到可实现方案，最后用误差分析反向证明设计选择的合理性，并把 LAPW 与赝势分别证明为其特例/近似，完成两大流派的理论统一。
  值得复用的关键术语：
  - 投影增强波（Projector Augmented-Wave, PAW）
  - 全电子分波 / 赝分波（AE / PS partial waves）
  - 投影函数 [[../concepts/projector-functions|投影函数]]（projector functions）
  - 线性变换（linear transformation T = 1 + Σ_R T_R）
  - 增强区域 [[../concepts/augmentation-region|增强区域]]（augmentation region / muffin-tin sphere / core region）
  - 补偿电荷密度 [[../concepts/compensation-charge-density|补偿电荷密度]]（compensation charge density n̂）
  - 加法缀加 [[../concepts/additive-augmentation|加法缀加]]（additive augmentation）
  - 冻结芯近似 [[../concepts/frozen-core-approximation|冻结芯近似]]（frozen-core approximation）
  - 重叠算符 [[../concepts/overlap-operator|重叠算符]]（overlap operator Õ，放松范数守恒的结果）
  - Pulay 力（Pulay forces，位置依赖基组拖拽电子产生的力）

## ✏️ 可写入 Wiki 的要点
  - PAW 核心变换：|Ψ⟩ = |Ψ̃⟩ + Σ_i (|φ_i⟩ − |φ̃_i⟩) ⟨p̃_i|Ψ̃⟩，三要素为 AE 分波 |φ_i⟩、PS 分波 |φ̃_i⟩（[[../concepts/augmentation-region|增强区域]]外与 AE 分波相同）、[[../concepts/projector-functions|投影函数]] ⟨p̃_i|（满足 ⟨p̃_i|φ̃_j⟩=δ_ij）。
  - 任意算符 A 的 PS 表示为 Ã = T†AT，形式与广义可分离赝势完全一致；PS 算符含直接作用项与两类局域投影修正项，后者在径向网格上用球谐函数与 Clebsch-Gordan 系数求值。
  - 总能量分解为 E = Ẽ + E¹ − Ẽ¹：Ẽ 在规则网格/傅里叶空间计算平滑部分，E¹、Ẽ¹ 在径向网格上做单中心 AE 与 PS 修正，相减去除双计数。
  - [[../concepts/compensation-charge-density|[[../concepts/compensation-charge|补偿电荷]]密度]] n̂ = Σ_R n̂_R = Σ_R,L g_RL(r) Q_RL（广义高斯函数）使单中心电荷差的多极矩为零，把静电作用转移到平面波部分，并允许[[../concepts/charge-density|电荷密度]]平面波截断仅取波函数截断的两倍（相比 USPP 的四倍显著省算）。
  - 实用近似仅两个：平面波截断 E_pw（典型 30 Ry）与每位点每角动量分波数（典型 1–2 个，l_max=1 或 2）；第一行元素一分波即可，过渡金属窄 d 态和半芯态需两分波。
  - 放松范数守恒导致非平凡[[../concepts/overlap-operator|重叠算符]] Õ = 1 + Σ_ij |p̃_i⟩(⟨φ_i|φ_j⟩−⟨φ̃_i|φ̃_j⟩)⟨p̃_j|，波函数需在 Õ 下正交化；这是 PAW/USPP 区别于范数守恒赝势的根本点。
  - 力分三部分：F_R = F_R⁽¹⁾+F_R⁽²⁾+F_R⁽³⁾，分别对应平滑部分刚性位移、单中心密度形状变化（Pulay 力）、波函数正交性变化；力与总能量 must 一致才能保证 MD 能量守恒。
  - [[../concepts/additive-augmentation|加法缀加]]原理下，AE 与 PS 分波以完全相同方式截断，未显式包含的高阶分波由平面波尾部表示，基组完备性不依赖分波数；误差分析证明芯与核的强变化势不对截断误差贡献（电荷密度可迁移性误差与能量可迁移性误差有效抵消）。
  - 数值验证：MnFO₃（Mn +7 氧化态）冻芯与显式含半芯 3s/3p 结果几乎一致（d_MnF≈3.19–3.21 a₀，d_MnO≈2.97–2.98 a₀），与全电子计算吻合，优于赝势（高估约 2.5%）；Fe₂ 全电子 Car-Parrinello MD 能量漂移 <0.8 meV/0.5 ps，核[[../concepts/mass-renormalization|质量重整化]]约 8%。
  - 方法统一：LAPW 是 PAW 的特例（用球面值与导数匹配代替投影函数内积）；范数守恒赝势可通过对单中心密度偏离原子值做一阶泰勒展开从 PAW 导出；Vanderbilt 超软赝势与 PAW 形式相似但 PAW 是全电子方法（保留完整波函数、含芯态、无"赝化"步骤），且因单中心项在径向网格处理而效率更高。
