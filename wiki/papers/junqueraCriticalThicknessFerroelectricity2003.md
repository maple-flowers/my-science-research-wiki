---
citekey: junqueraCriticalThicknessFerroelectricity2003
title: "Critical thickness for ferroelectricity in perovskite ultrathin films"
authors: [Javier Junquera, Philippe Ghosez]
year: 2003
journal: "Nature"
doi: "10.1038/nature01501"
url: "https://doi.org/10.1038/nature01501"
paper_type: theory
status: ingested
year_read: 2026
original_note: "[[../../raw/note/junqueraCriticalThicknessFerroelectricity2003]]"
projects: [project-5, project-2]
concepts: [density-functional-theory, berry-phase, strain-engineering, polarization-switching, ferroelectric-tunnel-junction, critical-thickness, depolarizing-field, screening-length, soft-mode, spontaneous-polarization, ferroelectricity, short-circuit-boundary]
entities: [SnTe, SIESTA, BaTiO3, SrRuO3, SrTiO3]
methods: [dft, lda, berry-phase, numerical-atomic-orbital, supercell, soft-mode-analysis, electrostatic-model]
materials: [BaTiO3, SrRuO3, SrTiO3]
figures: [crystal-structures, heterostructures-stacking, mathematical-models]
"领域基础知识": >-
  凝聚态物理、材料科学、铁电物理学、第一性原理计算。铁电体为具有自发极化且极化方向可随外加电场反转的材料，钙钛矿氧化物是重要一类。
"研究背景": >-
  随着微电子器件小型化，BaTiO3等钙钛矿铁电薄膜是否存在一个使铁电性消失的临界厚度？前期实验和理论（假设完美屏蔽）结果倾向于不存在，但都忽略了真实电极的非理想屏蔽效应。
"作者的问题意识": >-
  在考虑了真实金属电极的有限屏蔽长度和短路边界条件后，铁电薄膜是否仍能在任意薄尺度下保持其铁电性？
"主要研究对象": >-
  以SrRuO3为电极、BaTiO3为铁电层、外延生长在SrTiO3衬底上的短路铁电电容器。
"主要研究方法": >-
  采用密度泛函理论（DFT）和局域密度近似（LDA）的第一性原理计算，模拟不同厚度的BaTiO3薄膜，并通过分析其能量随软模位移的变化，判断铁电稳定性。
"研究意义": >-
  首次从第一性原理上证明了，在非理想屏蔽的短路电极条件下，铁电性存在一个有限临界厚度，为器件小型化提供了根本性的物理极限。
"研究结论": >-
  BaTiO3薄膜在夹于SrRuO3短路电极之间时，存在约6个晶胞（~24 Å）的临界厚度。低于此厚度，铁电性因电极不完全屏蔽产生的退极化电场而消失。
"对领域的贡献": >-
  解决了关于铁电薄膜临界尺寸的长期争论，将退极化场确立为支配超薄铁电行为的关键因素，为该领域树立了研究真实器件结构的新范式。
"未来研究方向提及": >-
  探索具有更短屏蔽长度的新型电极材料，以减弱退极化场，进一步降低临界厚度。
"未来研究方向思考": >-
  畴结构、界面缺陷、漏电流等现实因素如何协同调控退极化场和临界厚度？在临界厚度以下，这类结构是否可被用作高介电常数材料或出现新的量子效应（如铁电金属）？
tags:
  - paper
  - type/theory
  - year/2003
  - project/project-5
  - project/project-2
  - relevance/project-5/strong
  - relevance/project-2/medium
  - concept/density-functional-theory
  - concept/berry-phase
  - concept/strain-engineering
  - concept/polarization-switching
  - concept/ferroelectric-tunnel-junction
  - concept/critical-thickness
  - concept/depolarizing-field
  - concept/screening-length
  - concept/soft-mode
  - concept/spontaneous-polarization
  - concept/ferroelectricity
  - concept/short-circuit-boundary
  - entity/SnTe
  - entity/SIESTA
  - entity/BaTiO3
  - entity/SrRuO3
  - entity/SrTiO3
  - method/dft
  - method/lda
  - method/berry-phase
  - method/numerical-atomic-orbital
  - method/supercell
  - method/soft-mode-analysis
  - method/electrostatic-model
  - material/BaTiO3
  - material/SrRuO3
  - material/SrTiO3
  - topic/ferroelectricity
  - topic/2d-materials
  - topic/multiferroics
---

## junqueraCriticalThicknessFerroelectricity2003 — 钙钛矿超薄膜铁电性的临界厚度

- **元数据**：Junquera & Ghosez，2003，*Nature* 422, 506–509，DOI 10.1038/nature01501。
- **一句话**：用包含真实 SrRuO₃ 电极的第一性原理超胞计算首次证明，短路 BaTiO₃ 铁电薄膜在约 6 个晶胞（~24 Å）以下因电极不完全屏蔽产生的退极化场而丧失铁电性，确立了铁电器件微缩的静电学极限。

- **现有wiki双链**：
  - 概念 [[../concepts/density-functional-theory]]、[[../concepts/berry-phase]]、[[../concepts/strain-engineering]]、[[../concepts/polarization-switching]]、[[../concepts/ferroelectric-tunnel-junction]]
  - 实体 [[../entities/SnTe]]
  - 图表 [[../figures/crystal-structures]]、[[../figures/heterostructures-stacking]]、[[../figures/mathematical-models]]
  - 年度 [[../write/2003]]
  - 项目 [[../projects/project-5-snte-ferroelectric-sim]]、[[../projects/project-2-mn-multiferroics]]
  - 相关论文 [[../../raw/note/junqueraCriticalThicknessFerroelectricity2003]]

- **新概念/实体建议**：
  - `concepts/critical-thickness.md` — 铁电薄膜保持铁电性的最小厚度，由退极化场与本征铁电失稳竞争决定。
  - `concepts/depolarizing-field.md` — 铁电体内部由极化束缚电荷未被完全屏蔽而产生的反向静电场，E_d = 2ΔV/l。
  - `concepts/screening-length.md` — 金属电极中感应屏蔽电荷衰减的特征长度，决定界面电势降 ΔV。
  - `concepts/soft-mode.md` — 铁电相变对应的横光学声子软化模式，其冻结产生自发极化。
  - `concepts/spontaneous-polarization.md` — 无外场下晶胞不对称导致的固有极化强度 P_s。
  - `concepts/ferroelectricity.md` — 上位概念，统摄 sliding-ferroelectricity、polarization-switching、FTJ 等现有条目。
  - `concepts/short-circuit-boundary.md` — 电极等势边界条件，自然出现在周期性超胞中，是退极化场研究的标准设置。
  - `entities/BaTiO3.md` — 钙钛矿原型铁电体，四方相软模位移、B 位离子偏心。
  - `entities/SrRuO3.md` — 金属性钙钛矿氧化物电极，与 BaTiO₃/SrTiO₃ 共格外延。
  - `entities/SrTiO3.md` — 钙钛矿衬底/顺电参考材料，量子顺电体。
  - `entities/SIESTA.md` — 数值原子轨道基组的第一性原理代码，本文使用。

- **关键图表**：
  - ![图1 SrRuO3/BaTiO3/SrRuO3 短路铁电电容器结构与计算超胞（SrO/TiO2 界面）](../../raw/figures/junqueraCriticalThicknessFerroelectricity2003/fig_1_BHUIKLVH.png)
  - ![图2 不同 BaTiO3 厚度 m=2–10 下能量随软模畸变 y 的变化：m≤4 顺电稳定，m≥6 出现双阱铁电相；插图为 P_s 随 m 的恢复](../../raw/figures/junqueraCriticalThicknessFerroelectricity2003/fig_2_XASEAFPQ.png)
  - ![图3 沿 [001] 方向的宏观电荷密度差与静电势差：界面偶极子与薄膜内部线性电势降（退极化场 E_d）](../../raw/figures/junqueraCriticalThicknessFerroelectricity2003/fig_3_DQ8AHC66.png)
  - 注：raw/figures 下 manifest.json 对图 1 的自动描述误植为冰芯地图（PDF 提取串文），实际图 1 为本论文的电容器超胞示意，以上图注依据论文正文。

- **项目连接**：
  - **project-5（SnTe 铁电薄膜模拟，strong）**：本文是铁电薄膜有限尺寸效应的奠基性文献，直接对 SnTe 薄膜/二维 SnTe 铁电模拟有参考价值。(1) 机制可类比——SnTe 无论以传统铁电还是滑动铁电形式存在，置于电极间时同样要面对极化束缚电荷的屏蔽问题，电极屏蔽长度不足必然在薄膜内部产生退极化场，本文给出的 E_d = 2ΔV/l 图像可直接迁移到 SnTe 电容器构型。(2) 计算流程可复用——在周期性超胞中显式包含金属电极、施加短路边界条件、沿软模（或相应极性位移模式）扫描能量曲线判断铁电/顺电基态，是判断 SnTe 是否存在临界厚度的标准范式。(3) 静电模型 E = U − P·E_d 可作为 LAMMPS/MLIP 或 DFT 结果的解析校核工具。(4) 数据可参照——BaTiO₃/SrRuO₃ 体系 ~6 uc (~24 Å) 的临界厚度、应变把 P_s 从 24 增至 31 μC cm⁻² 等定量结果，为 SnTe 体系提供对比基准。(5) 对二维/层状 SnTe，电极屏蔽问题甚至更尖锐（界面范德华间隙、有限态密度），本文的方法论是天然起点。
  - **project-2（Mn 多铁，medium）**：多铁薄膜若要实现磁电耦合，铁电分量必须在纳米尺度保持稳定。本文确立的"真实电极下铁电性有临界厚度、退极化场压制极化"的物理图像，对任何钙钛矿多铁薄膜（包括含 Mn 的体系）的厚度设计、电极选择、畴结构考虑都有方法学参考价值；DFT+Berry 相计算极化、超胞加短路电极的做法也可直接借用。但本文材料本身是 BaTiO₃，与 Mn 多铁无直接材料重合，故判为 medium。
  - 其他项目（project-1 双光子、project-3 机械发光 NN、project-4 TTF 分子计算、project-6 湿度传感器、project-7 CDW）无直接项目连接。

- **组织与用词**：
  - 文章采用"问题—矛盾—模型—结果—机制—影响"的简洁 Nature 论证链。先指出前人在 E=0 假设下预测无临界尺寸，再用包含真实电极的超胞计算给出反例，然后用宏观平均电荷密度与静电势把退极化场可视化，最后用 E = U − P·E_d 解析模型定量复现第一性原理结果，证明静电学主导、界面化学次要。并通过漏电流时间尺度（~0.1 s）与极化翻转时间尺度（~10⁻⁹ s）的对比排除了有限电导率对临界厚度结论的干扰。
  - 值得复用的术语：
    - critical thickness — 临界厚度
    - depolarizing field — 退极化场（去极化场）
    - screening length — 屏蔽长度
    - soft-mode distortion — 软模畸变
    - short-circuit boundary condition — 短路边界条件
    - interface dipole — 界面偶极子
    - spontaneous polarization — 自发极化
    - ferroelectric instability — 铁电不稳定性

- **可写入wiki的要点**：
  1. **临界厚度数值**：BaTiO₃ 夹于两个短路 SrRuO₃ 电极之间、外延于 SrTiO₃ 衬底（约 2% 压应变）时，临界厚度约为 m=6 个晶胞，对应 ~24–26 Å；m≤4 顺电相稳定，m≥6 铁电相稳定，m=6 附近为临界点。
  2. **物理机制**：极化 P 在界面产生束缚电荷 σ_pol = P·n̂，金属电极电子因有限屏蔽长度无法完全中和，在两界面形成同号偶极子；为维持短路（电极等势），薄膜内部必然出现反向退极化场 E_d = 2ΔV/l，厚度 l 越小 E_d 越强，最终压制铁电不稳定性。
  3. **静电模型**：E = U − P·E_d，其中 U 为零场内能（用体相软模双阱势近似），P = (1/Ω)Σ Z*_i y_i + χ_∞ E_d；横向有效电荷 Z* 用 Berry 相方法计算，电子极化率 χ_∞ 由超胞技术获得。该模型仅用体相参数即完整复现第一性原理能量曲线，说明静电学主导超薄行为，界面化学键合贡献次要。
  4. **方法学创新**：首次在第一性原理计算中显式构建完整的"金属电极/铁电薄膜/金属电极/衬底"超胞，通式 [SrO-(RuO₂-SrO)_n/TiO₂-(BaO-TiO₂)_m]，n=5、m=2–10，周期性边界条件自然施加短路条件；面内晶格常数固定为 SrTiO₃ 体相值以隐式包含外延应变。
  5. **应变效应量化**：衬底施加的 ~2% 压应变抑制 BaTiO₃ 面内铁电不稳定性，同时通过垂直方向泊松弛豫将计算的自发极化从 24 μC cm⁻² 放大到 31 μC cm⁻²。
  6. **超临界厚度后的残余压制**：即使 m>6，退极化场仍使 P_s 低于体相值，并随 m 增大缓慢趋近体相值（图 2 插图）；这意味着器件在临界厚度以上仍受静电场影响，关联到矫顽场、开关电压、疲劳等性能。
  7. **漏电流时间尺度论证**：典型铁电电容 J < 10⁻⁵ A cm⁻²、σ_pol < 10⁻⁶ C cm⁻² 下，漏电流屏蔽所需时间约 0.1 s，远长于极化翻转时间 ~10⁻⁹ s，故漏电流不能阻止亚临界厚度薄膜弛豫回顺电态；但长时间尺度上仍可能影响矫顽场与疲劳。
  8. **与前人工作的边界**：Ghosez & Rabe (2000)、Meyer & Vanderbilt (2001) 等在零内场（完美屏蔽）条件下预测无临界尺寸；本工作通过引入真实金属-钙钛矿界面（有限屏蔽长度、界面化学、衬底应变）推翻了该结论。Rao et al. (1997) 虽研究过金属/BaTiO₃ 界面，但未讨论铁电不稳定性。
  9. **计算细节**：SIESTA 代码、数值原子轨道基组、LDA；SrO/TiO₂ 界面终端（实验上因 Ru 挥发性所致）；先以中心 TiO₂ 层镜面对称约束弛豫得到顺电参考态（原子最大受力 < 40 meV Å⁻¹），再沿体相四方软模位移模式 y 扫描能量；对 m=2 超胞还做了无约束全原子弛豫验证，原子自发回到顺电位置。
  10. **后续启示**：寻找更短屏蔽长度的电极材料（金属、导电氧化物乃至二维导体）、界面工程（插层、终端调控）、多畴与畴壁屏蔽、缺陷/氧空位的电荷补偿，是降低临界厚度与调控超薄铁电性能的主要方向；临界厚度以下结构可能作为高介电常数材料或出现铁电金属等新量子态。
