---
citekey: zhaoRealization2DMultiferroic2024
title: "Realization of 2D multiferroic with strong magnetoelectric coupling by intercalation: a first-principles high-throughput prediction"
title_zh: "嵌入实现强磁电耦合二维多铁性材料：第一性原理高通量预测"
authors: [Ying Zhao, Yanxia Wang, Yue Yang, Jijun Zhao, Xue Jiang]
year: 2024
journal: "npj Computational Materials"
doi: "10.1038/s41524-024-01301-x"
url: "https://doi.org/10.1038/s41524-024-01301-x"
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/zhaoRealization2DMultiferroic2024]]
projects: [project-1, project-2]
concepts: [2D-materials, berry-phase, density-functional-theory, magnetoelectric-coupling, multiferroicity, polarization-switching, spin-orbit-coupling, topological-defects]
entities: [CrTe2, In2Se3, TMDs, VASP, WTe2]
methods: [afm-pfm, berry-phase, dft, monte-carlo, neb]
materials: [CrTe2, In2Se3, TMDs, WTe2]
figures: [crystal-structures, electronic-bands, heterostructures-stacking, mathematical-models]
领域基础知识:: >-
  二维（2D）材料，多铁性（同时存在铁电、铁磁等序），磁电耦合效应（电场控磁，磁场控电），第I类多铁（磁性、铁电来源不同，耦合弱），第II类多铁（铁电源于特殊磁序，耦合强但极化弱），插层（在材料层间插入原子/分子），过渡金属硫族化合物（TMDs），斯格明子（一种拓扑保护的涡旋状自旋结构），Dzyaloshinskii-Moriya相互作用（DMI，非中心对称体系中的反对称交换作用，是形成斯格明子的关键）。
研究背景:: >-
  信息技术发展亟需低功耗、高密度器件。二维多铁材料因其磁电耦合效应，可实现电场写/磁场读，具有巨大潜力。但现有单相二维多铁材料难以同时满足强磁电耦合、高极化强度和高居里温度的要求，存在性能瓶颈。
作者的问题意识:: >-
  如何系统性地设计出磁电耦合强、极化大、转变温度高且稳定的单相二维多铁材料？能否利用插层这一化学手段，在TMD双层中同时引入并调控铁电性和磁性？
主要研究对象:: >-
  960种非中心对称的插层化合物AM₂X₄，其中A为3d/4d过渡金属，M为过渡金属，X为S/Se/Te。最终筛选出的21种二维多铁单层材料，特别是代表材料T-CdCr₂Te₄（type-a），T-CoZr₂S₄（type-b），T-CoTi₂Te₄（type-c）。
主要研究方法:: >-
  高通量第一性原理计算（基于DFT的VASP软件，使用PBE+U泛函），结合蒙特卡洛（MC）模拟。通过结构优化、声子谱、形成能评估稳定性；用Berry phase和偶极修正法计算极化；用CI-NEB方法计算翻转能垒；用MC模拟估算居里温度和模拟自旋织构。
研究意义:: >-
  提出并验证了一种通用的“插层策略”来设计二维多铁材料。一次性预测了21种新型二维多铁材料，极大地扩展了该家族。揭示了金属性与铁电性共存的新机制，并首次在同一体系中实现了通过极化翻转对上下层斯格明子的可逆调控，为设计电场操控拓扑自旋的器件提供了新范式。
研究结论:: >-
  通过插层策略，成功筛选出40种稳定的二维铁电体和21种二维多铁材料。按磁性起源将其分为三类：type-a（磁性在MX₂层，极化翻转可调控斯格明子），type-b（磁性在插层A原子，极化翻转改变磁基态和易磁化轴），type-c（磁性在两者，极化翻转改变自旋极化分布）。其中type-a材料T-CdCr₂Te₄的居里温度和铁电转变温度均接近室温，具有优异的磁电耦合性能。
对领域的贡献:: >-
  贡献了一套系统的材料设计策略和筛选流程。提供了21种高性能二维多铁材料候选物列表，为实验合成指明了方向。深入阐明了三类多铁材料中磁电耦合的微观物理机制，特别是电场控制斯格明子的新机制，为该领域奠定了新的理论基础。
未来研究方向提及:: >-
  需要通过实验合成来验证这些理论预测的材料及其多铁和磁电耦合性能。可通过插层策略进一步探索其他新颖的拓扑物理现象。
未来研究方向思考:: >-
  1. 探索这些材料在器件集成中的性能，如设计原型器件并评估读写速度。2. 研究缺陷（空位、掺杂）对这些材料，尤其是斯格明子稳定性的影响，进行性能优化。3. 构建范德华异质结，利用界面效应调控磁电耦合。4. 研究除电场外的其他外场（如应力、光）对多铁性能的调控。
tags:
  - paper
  - type/experiment
  - year/2024
  - project/project-1
  - relevance/project-1/medium
  - project/project-2
  - relevance/project-2/medium
  - concept/2D-materials
  - concept/berry-phase
  - concept/density-functional-theory
  - concept/magnetoelectric-coupling
  - concept/multiferroicity
  - concept/polarization-switching
  - concept/spin-orbit-coupling
  - concept/topological-defects
  - entity/CrTe2
  - entity/In2Se3
  - entity/TMDs
  - entity/VASP
  - entity/WTe2
  - method/afm-pfm
  - method/berry-phase
  - method/dft
  - method/monte-carlo
  - method/neb
  - material/CrTe2
  - material/In2Se3
  - material/TMDs
  - material/WTe2
  - topic/2d-materials
  - topic/ferroelectricity
  - topic/multiferroics
  - topic/polarization
  - topic/topological-defects
---

## zhaoRealization2DMultiferroic2024 — 通过插层实现具有强磁电耦合的二维多铁性材料：第一性原理高通量预测

## 📄 元数据
Ying Zhao, Yanxia Wang, Yue Yang, Jijun Zhao, Xue Jiang（大连理工大学/华南师范大学），2024，npj Computational Materials 10:122，DOI: 10.1038/s41524-024-01301-x
## 💡 一句话
提出将过渡金属离子 A 非中心对称地插入 TMD 双层四方空位构建 AM₂X₄ 的"超晶格插层"通用策略，从 960 种候选物中高通量筛选出 21 种强磁电耦合二维多铁体，并按磁性起源分为 a/b/c 三类，其中 T-CdCr₂Te₄ 可通过极化翻转可逆调控反斯格明子的产生、湮灭与手性反转。
## 🔗 Wiki 双链
  - 概念 [[../concepts/multiferroicity]]、[[../concepts/magnetoelectric-coupling]]、[[../concepts/2D-materials]]、[[../concepts/density-functional-theory]]、[[../concepts/berry-phase]]、[[../concepts/spin-orbit-coupling]]、[[../concepts/topological-defects]]、[[../concepts/polarization-switching]]
  - 实体 [[../entities/TMDs]]、[[../entities/VASP]]、[[../entities/In2Se3]]、[[../entities/WTe2]]、[[../entities/CrTe2]]
  - 图表 [[../figures/crystal-structures]]、[[../figures/electronic-bands]]、[[../figures/mathematical-models]]、[[../figures/heterostructures-stacking]]、[[../figures/experimental-setups|实验测试与测量装置]]、[[../figures/heterostructures-stacking-multiferroic|多铁与磁电异质结]]
  - 年度 [[../write/2024]]
  - 主题 [[多铁性材料]]、[[材料模拟计算设计]]
  - 相关论文 [[../../raw/note/zhaoRealization2DMultiferroic2024]]
## 🆕 新概念/实体建议
  - `intercalation`（插层）：外来原子/分子嵌入范德华层间间隙形成杂化化合物的化学过程，是本文设计策略的核心。
  - `magnetic-skyrmion`（磁斯格明子）：拓扑保护的涡旋状纳米自旋织构，可作赛道存储器信息比特；本文在 T-CdCr₂Te₄ 中实现电控反斯格明子。
  - `dzyaloshinskii-moriya-interaction`（DMI，Dzyaloshinskii-Moriya 相互作用）：破缺反演对称体系中的反对称交换作用，是斯格明子形成的关键驱动力。
  - `metallic-ferroelectricity`（金属铁电性）：金属中自由电子未能完全屏蔽局域极化电荷而保留铁电极化的现象，本文以极化电子/传导电子空间分离机制解释。
  - `AM2X4-intercalation-family`（AM₂X₄ 插层化合物家族）：由 A 离子插入 MX₂ 双层构成的非范德华二维材料家族，可承载多铁、拓扑等多种序参量。
  - `high-throughput-screening`（高通量筛选）：基于第一性原理批量计算并按稳定性/能垒/物性漏斗式筛选候选材料的方法论。
  - 实体 `T-CdCr2Te4`：本文旗舰型 a 类多铁体，近室温（T_C=260 K）、电场可克斯格明子手性。
## 📊 关键图表
  - ![T-/H-AM2X4 晶体结构与铁电翻转机制](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_1_S88Q2EF3.png) → [[../figures/heterostructures-stacking-multiferroic|多铁与磁电异质结]]
    - **图示描述**：对比展示基于 1T 相 MX₂ 双层的 T-AM₂X₄ 与基于 2H 相的 H-AM₂X₄ 两种晶体结构，标出插层原子 A 的两个等效位置 FE1/FE2 及 A 在两位置间翻转的位移路径（蓝色箭头）。
    - **关键特征**：A 原子（紫色）与一侧 1 个 X、另一侧 3 个 X 形成不对称四面体配位，从而破缺中心反演对称并产生自发极化；A 在 FE1↔FE2 间 180° 翻转即对应上下层配位环境互换与极化反向，是整篇论文"插层诱导铁电"策略的结构起源。
    - **结论/意义**：该图给出全部 960 种候选物共用的结构母型，把铁电翻转简化为单原子在四面体空位间的位移，为后续低翻转势垒设计提供几何基础。
  - ![960→21 高通量筛选漏斗流程图](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_2_7QNUMABJ.png) → [[../figures/experimental-setups|实验测试与测量装置]]
    - **图示描述**：以漏斗式流程图呈现从 960 种非中心对称 AM₂X₄ 候选物到最终 21 种多铁体的四步高通量筛选，每一步标出通过的材料数目与判据。
    - **关键特征**：第一步结构优化确认自发极化；第二步声子谱无虚频（104 种）+ 形成能为负（100 种）保证动力学/热力学稳定；第三步以铁电翻转势垒 < 200 meV/f.u. 并排除已报道体系，筛出 40 种稳定铁电体；第四步按磁基态再筛得 21 种多铁体（10 FM、9 AFM、2 FiM），并按磁性起源分成 type-a/b/c 三类。
    - **结论/意义**：这张图是全文论证骨架，把"插层策略"落到可复制的筛选流水线，并直接给出 21 种候选物的分类结果。
  - ![T-PdZr2Se4 与 T-CoTi2Te4 电子结构及极化/传导电子空间分离](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_3_VSIZIKC2.png) -> [[../figures/electronic-bands|电子能带与电子态]]
    - **图示描述**：左右两栏分别对应金属铁电体 T-PdZr₂Se₄（非磁）与 T-CoTi₂Te₄（自旋极化），每栏含 (a,d) 能带、(b,e) PDOS、(c,f) 沿 z 方向的传导电子密度 ρ_c(z) 与极化电子密度 ρ_P(z) 曲线。
    - **关键特征**：能带显示费米能级穿过能带、无带隙，证实两种材料均为金属；PDOS 表明 T-PdZr₂Se₄ 的导电电子主要来自 ZrSe₂ 层；ρ_c 主要分布在顶/底 MX₂ 层，而 ρ_P=ρ_FE−ρ_PE 局域在插层原子周围并呈振荡——两类电荷实空间分离使自由电子无法完全屏蔽面外极化，T-PdZr₂Se₄ 的 P_out 达 3.10 pC/m。
    - **结论/意义**：该图从电子结构层面解释了"金属性与铁电性共存"这一反直觉现象，是论文提出金属铁电新机制的核心证据。
  - **图4（raw/figures 中未附图片）**：T-CdCr₂Te₄ 中极化翻转调控反斯格明子的蒙特卡洛自旋织构快照
    - **图示描述**：上下两排分别对应 FE1 与 FE2 极化态，(a,h) 给出顶/底 CrTe₂ 层 DMI 矢量排列，(b–g)、(i–n) 为不同垂直磁场（约 0–3.5 T）下的 MC 自旋织构快照。
    - **关键特征**：FE1 态顶层 Cr 在 B ≈ 2.4–3.17 T 区间出现反斯格明子（直径约 3.8–8.9 nm，随场增大而缩小），底层保持 FM；FE2 态顶/底层行为互换，且两态斯格明子手性相反；FE1 态顶层 D 值约为底层 3 倍，FE2 态反转，D/|J| 在 9.03%–20.80% 间随极化切换。
    - **结论/意义**：这是 type-a 磁电耦合的旗舰结果，证明单靠电场翻转极化即可可逆地产生、湮灭并反转拓扑磁织构的手性。
  - **图5（raw/figures 中未附图片）**：T-CdCr₂Te₄ FE1 态顶层 Cr 的温度-磁场自旋织构相图
    - **图示描述**：横轴为垂直磁场（约 0–3.5 T），纵轴为温度（0–60 K），用色块/边界标出条纹畴、反斯格明子晶格、FM 与无序相等区域。
    - **关键特征**：T = 0 K 时反斯格明子相锁定在约 2.4–3.17 T 的窄磁场窗口；随温度升高窗口变窄、临界场降低；T > 40 K 后不再形成斯格明子，条纹畴直接转入 FM；T > 60 K 进入热无序相，斯格明子晶格相的临界温度约 40 K。
    - **结论/意义**：给出实验上观测电控斯格明子的温度/磁场操作窗口，也指出当前体系斯格明子相仍受低温限制。
  - ![T-CoZr2S4 极化翻转路径上磁基态 FM-AFM-FM 与 MAE 变化](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_6_D3YLN99Y.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
    - **图示描述**：横轴为 CI-NEB 得到的铁电翻转路径（FE1 → PE → FE2），多条彩色曲线表示不同 AFM 构型相对 FM 态的能量差 ΔE，黑色曲线表示磁各向异性能 MAE 沿路径的变化。
    - **关键特征**：FE1、FE2 两端 ΔE_AFM−FM > 0，磁基态为 FM；接近 PE 相处 ΔE 变负，磁基态转为 AFM，整体经历 FM→AFM→FM 可逆转变；PE 相处 MAE 骤变为约 −13.34 meV/Co，易磁化轴由面外翻为面内；代表材料 T-CoZr₂S₄ 的 T_C ≈ 70 K，FE 在 300 K 仍稳定。
    - **结论/意义**：该图刻画了 type-b 磁电耦合机制——极化路径不仅切换电极化，还同时切换磁基态与易轴方向，为电场调控磁序提供新途径。
  - ![T-CoTi2Te4 FE1/FE2 态能带与 PDOS 自旋极化反转](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_7_DKCIN6VB.png) -> [[../figures/electronic-bands|电子能带与电子态]]
    - **图示描述**：(a,b) 为 T-CoTi₂Te₄ 在 FE1 与 FE2 态下的电子能带，(c,d) 为对应自旋分辨的 PDOS，对比费米能级附近上、下自旋通道的占据。
    - **关键特征**：两种极化态均为金属；FE1 态费米能级附近传导电子以自旋向下为主，FE2 态翻转为自旋向上为主；Ti_top/Ti_bot 磁矩由 0.62/0.82 μ_B 互换为 0.82/0.62 μ_B，净磁矩约 0.21 μB/f.u.；易磁化轴由 x 方向翻为 z 方向。
    - **结论/意义**：该图是 type-c 磁电耦合的直接证据——极化翻转重排了自旋极化电子的实空间分布，可用于电控自旋滤波或自旋逻辑器件。
  - ![表1：19 种非磁铁电体带隙、极化与翻转势垒](../../raw/figures/zhaoRealization2DMultiferroic2024/tab_1_P98XXL3P.png) -> [[../figures/mathematical-models|数学模型与物理公式]]
    - **图示描述**：表格汇总从 40 种稳定铁电体中分出的 19 种非磁（半导体/金属）铁电体，列出 GGA+U 带隙、磁基态、面外极化 P_out 与铁电翻转势垒 E_B。
    - **关键特征**：4 种半导体铁电体同时具有面内 P_in（Berry phase，最高约 306.45 pC/m）和面外 P_out（偶极修正，最高约 15.22 pC/m），量级与 In₂Se₃ 相当；其余金属铁电体 P_out 分布在约 0.43–9.61 pC/m，普遍大于实验测得的 WTe₂ 双层（0.42 pC/m）；势垒整体控制在 200 meV/f.u. 阈值以下。
    - **结论/意义**：表 1 量化了"插层策略"在非磁体系中的铁电性能，为后续多铁筛选提供基准池。
  - ![表2：21 种多铁体磁基态、T_C/T_N、MAE、极化与势垒](../../raw/figures/zhaoRealization2DMultiferroic2024/tab_2_BHS6QQPS.png) -> [[../figures/mathematical-models|数学模型与物理公式]]
    - **图示描述**：表格列出全部 21 种多铁 AM₂X₄ 的磁基态（FM/AFM/FiM）、居里/奈尔温度 T_C/T_N、磁各向异性能 MAE、面外极化 P_out 与翻转势垒 E_B，并按 type-a/b/c 分组。
    - **关键特征**：type-a 旗舰 T-CdCr₂Te₄ 的 T_C ≈ 260 K、FE 转变温度 >300 K、P_out ≈ 2.77 pC/m、E_B ≈ 66 meV/f.u.；type-b 代表 T-CoZr₂S₄ 的 T_C ≈ 70 K 但 FE 在室温稳定；type-c 代表 T-CoTi₂Te₄ 净磁矩约 0.21 μB/f.u.、E_B ≈ 79 meV/f.u.；同属 type-a 的 T-AgMn₂Se₄ T_C 高达约 525 K。
    - **结论/意义**：表 2 是论文交付给实验方的候选材料清单，把三类磁电耦合机制与具体组分、关键性能参数一一对应。
  - ![表3：T-CdCr2Te4 顶层/底层 Cr 的 J 与 DMI 参数](../../raw/figures/zhaoRealization2DMultiferroic2024/tab_3_2VLQ8VY7.png) -> [[../figures/heterostructures-stacking-multiferroic|多铁与磁电异质结]]
    - **图示描述**：表格给出 T-CdCr₂Te₄ 在 FE1 与 FE2 态下，顶层与底层 CrTe₂ 亚层的近邻海森堡交换 J_ij 与 Dzyaloshinskii-Moriya 矢量 D_ij 等自旋哈密顿量参数。
    - **关键特征**：FE1 态顶层 |D| 约为底层的 3 倍，FE2 态两层的 D 强度与方向整体互换；J 始终为铁磁性符号但随极化方向略有变化；由此算出的 D/|J| 比落在约 9.03%–20.80%，恰好进入可承载斯格明子的区间；这些参数是 MC 模拟复现反斯格明子及其手性反转的直接输入。
    - **结论/意义**：表 3 把"电场控斯格明子"的现象学观察落实到可量化的微观磁耦合参数上，是 type-a 机制的定量支撑。
  - 注：原文图4（极化翻转调控斯格明子自旋织构快照）与图5（温度-磁场相图）在 raw/figures 目录中未附图片，已按 raw/note 中的图表解析以文字形式补全。
## 🔬 项目连接
project-2 Mn多铁（本文 a 类含多种 Mn 基多铁体如 T-CuMn₂Se₄、T-AgMn₂S₄/Se₄、T-CdMn₂Se₄，T-AgMn₂Se₄ 的 T_C 高达 525 K，与 Mn 多铁主题直接相关）；其余 project-1/3/4/5/6/7 无直接连接。
## 🔗 项目双链
- 项目 [[../projects/project-1-two-photon|项目一：双光固化和双光发光]]
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]

## 📝 组织与用词
论文按"策略提出 → 四步高通量筛选 → 铁电行为（半导体/金属分开讨论）→ 三类磁电耦合机制逐一剖析 → 结论"递进展开。论证以筛选漏斗（960→104/100→40→21）为骨架，再用三个代表材料（T-CdCr₂Te₄、T-CoZr₂S₄、T-CoTi₂Te₄）分别承载 a/b/c 三类机制，结构清晰、数据-机制对应。值得复用的术语：
  - [[../concepts/intercalation|插层 intercalation]]
  - 磁电耦合 magnetoelectric (ME) coupling
  - 磁斯格明子 / 反斯格明子 magnetic skyrmion / anti-skyrmion
  - Dzyaloshinskii-Moriya 相互作用 DMI
  - [[../concepts/high-throughput-screening|高通量第一性原理筛选 high-throughput first-principles screening]]
  - [[../concepts/switching-barrier|铁电翻转势垒 FE switching barrier]]
  - 极化电子与传导电子空间分离 spatial separation of polarization and conduction electrons
  - 拓扑磁织构 topological magnetic texture
  - [[../concepts/dzyaloshinskii-moriya-interaction|dzyaloshinskii-moriya-interaction]]
  - [[../concepts/topological-spin-texture|topological-spin-texture]]
## ✏️ 可写入 Wiki 的要点
  1. 插层设计原理：将 3d/4d 过渡金属 A 插入 2H 或 [[../concepts/1t-phase|1T 相]] MX₂ 双层的类四方空位，A 与一层 1 个 X、另一层 3 个 X 配位，形成不对称四面体配位而破缺反演对称；A 在两位置间 180° 翻转即实现极化反转，构成 H-/T-AM₂X₄ 两种结构。
  2. 筛选漏斗：960 种组合 → 结构优化确认自发极化 → 声子谱无虚频（104 种）且[[../concepts/formation-energy|形成能]]为负（100 种）→ 铁电[[../concepts/switching-barrier|翻转势垒]] < 200 meV/f.u.（约合室温 k_BT/原子）并排除已报道体系 → 40 种稳定铁电体 → 磁基态筛选得 21 种多铁体（10 FM、9 AFM、2 FiM）。
  3. 金属铁电共存机制：以 T-PdZr₂Se₄ 为例，传导电子 ρ_c(z) 主要分布于顶/底 ZrSe₂ 层，极化电子 ρ_P(z)=ρ_FE−ρ_PE 主要局域在插层 Pd 原子周围并呈振荡；两类电荷实空间分离使传导电子无法完全屏蔽垂直极化，Pout=3.10 pC/m。16 种非磁金属铁电体 Pout 在 0.43–9.61 pC/m，均大于实验测得的 WTe₂ 双层（0.42 pC/m）。
  4. 半导体铁电体（T-CdSc₂Se₄、T-CdRh₂S₄、T-CoSc₂S₄、T-CoY₂S₄）同时具有面内 Pin（Berry phase，最高 306.45 pC/m）和面外 Pout（偶极修正，最高 15.22 pC/m），与 In₂Se₃ 相当，并存在面内-面外铁电关联（dipole locking），可用于多向场效应晶体管。
  5. 分类依据：a 类（12 种）磁性来自 MX₂ 层 M 原子（A=Pd/Cu/Ag/Zn/Cd 满 d 壳层非磁）；b 类（7 种，CoSc₂S₄、CoY₂S₄、CoZr₂S₄、CoZr₂Se₄、CrMo₂Se₄、MnMo₂S₄、MnMo₂Se₄）磁性来自插层 A 原子；c 类（2 种，CoTi₂Se₄、CoTi₂Te₄）磁性来自 A 与 M 两者。
  6. a 类旗舰 T-CdCr₂Te₄：FM 基态，T_C=260 K（MC），FE 转变温度 >300 K（AIMD：250 K 时 Cd 位移 0.376 Å，300 K 降至 0.020 Å），Pout=2.77 pC/m，E_B=66 meV/f.u.，MAE=−0.34 meV/Cr（面内易轴）；T-AgMn₂Se₄ 的 T_C 更高达 525 K。
  7. a 类电控[[../concepts/skyrmion|斯格明子]]：FE1 态顶层 CrTe₂ 的 D 值约为底层 3 倍，FE2 态反转；D/|J| 比在 9.03%–20.80% 间随极化切换。MC 模拟显示 FE1 态顶层在 B=2.4–3.17 T 出现反斯格明子（直径 3.8–8.9 nm，随场增大而缩小），底层保持 FM；FE2 态顶层/底层行为互换，且两态斯格明子手性相反。斯格明子晶格相临界温度约 40 K（T>40 K 时条纹畴直接转 FM，T>60 K 为无序相）。
  8. b 类 T-CoZr₂S₄：J1>0 主导 FM，MAE=0.61 meV/Co（面外易轴），T_C≈70 K，FE 在 300 K 稳定；[[../concepts/polarization-switching|极化翻转]]路径上磁基态经历 FM→AFM→FM，PE 相处 MAE 骤变为 −13.34 meV/Co（易轴翻为面内），T-CoY₂S₄ 与 H-MnMo₂Se₄ 表现类似耦合。
  9. c 类 T-CoTi₂Te₄：FiM 基态，净磁矩 0.21 μB/f.u.（T-CoTi₂Se₄ 为 0.24 μB/f.u.）；FE1 态费米能级传导电子以自旋向下为主、FE2 态转为自旋向上为主；Titop/Tibot 磁矩由 0.62/0.82 μB 互换为 0.82/0.62 μB；易磁化轴由 x 方向翻为 z 方向，实现对自旋极化输运的电场调控。
  10. 方法学：VASP + PAW + PBE(GGA)+U，平面波截断 500 eV，k 点间距 2π×0.02 Å⁻¹，真空层 >15 Å；Phonopy 有限位移法算声子；形成能 E_f=(E_AM2X4−E_A−2E_M−4E_X)/7；CI-NEB 算翻转势垒；Berry phase 算 Pin、偶极修正算 Pout；MC（80×80 晶格，Spirit 软件，Metropolis 算法，最小 6×10⁵ 步）估算 T_C/T_N 并模拟自旋织构；AIMD（NVT，4×4×1 超胞，≥10 ps，1 fs 步长）估算 FE 转变温度。含 DMI 的自旋哈密顿量为 H=ΣJ_ij S_i·S_j − A_z Σ(S_i^z)² + Σ D_ij·(S_i×S_j)。
