---
citekey: khazaeiNovelElectronicMagnetic2013
title: "Novel Electronic and Magnetic Properties of Two-Dimensional Transition Metal Carbides and Nitrides"
authors: [Mohammad Khazaei, Masao Arai, Taizo Sasaki, Chan-Yeup Chung, Natarajan S. Venkataramanan, Mehdi Estili, Yoshio Sakka, Yoshiyuki Kawazoe]
year: 2013
journal: "Advanced Functional Materials"
doi: "10.1002/adfm.201202502"
url: "https://doi.org/10.1002/adfm.201202502"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/khazaeiNovelElectronicMagnetic2013]]
projects: [project-2, project-4]
concepts: [2d-materials, density-functional-theory, electron-counting-rule, strain-engineering, surface-functionalization, ferromagnetism, thermoelectricity, boltzmann-transport, max-phase, phonon-stability]
entities: [MXenes, VASP, BoltzTrap, MAX-phases, Ti2CO2, Sc2CF2, Sc2CO2, Cr2C, Cr2N]
methods: [dft, gga-pbe, paw, first-principles, spin-polarized-dft, formation-energy, phonon-dispersion, band-structure, dos, boltzmann-transport, boltztrap]
materials: [MXenes, Ti2C, Sc2C, Zr2C, Hf2C, Cr2C, Cr2N, Ti2CO2, Sc2CF2, Sc2C-OH-2, Sc2CO2, Zr2CO2, Hf2CO2]
figures: [electronic-bands-band-structures, electronic-bands-cdw-transport, electronic-bands-dos-fermi, heterostructures-stacking, vibrational-spectra]
领域基础知识:: >-
  二维材料（2D Materials）是厚度仅为一个或几个原子层的晶体材料，其电子结构受到量子限域效应影响，表现出与三维结构迥异的性质。MXenes是二维材料家族中极具潜力的一类，由过渡金属碳化物、氮化物或碳氮化物构成，通常通过从MAX相陶瓷中选择性刻蚀A元素层而获得。
研究背景:: >-
  石墨烯的发现开启了二维材料研究热潮，但传统机械剥离法难以量产。2011年，实验上通过化学刻蚀法 from MAX相中成功制备出 MXenes，开创了大规模制备二维材料的新路径。实验发现，制备出的 MXene 表面总是被 F、OH 等官能团覆盖，这些官能团对其性质的影响亟需理论阐明。
作者的问题意识:: >-
  在少数 MXene 刚被实验合成之初，作者敏锐地意识到，表面功能化是 MXene 的必然状态，但对其电子与磁学性质的系统性理论理解是空白。他们旨在回答：不同过渡金属与表面官能团组合，将如何调控 MXene 的电子结构？能否从中发现具有半导体、磁性等新奇性质的 MXene 体系？
主要研究对象:: >-
  最薄的 MXene 体系，化学式为 M₂XT₂，其中 M 代表 Sc、 Ti、 V、 Cr、 Zr、 Nb、 Hf、 Ta 等前过渡金属，X 代表 C 或 N，T 代表表面功能化基团 F、OH 或 O。
主要研究方法:: >-
  基于密度泛函理论（DFT）的第一性原理计算，使用 VASP 软件，采用 GGA-PBE 泛函和 PAW 赝势。通过计算不同结构模型的总能、形成能、声子谱来评估稳定性。通过分析态密度（DOS）和能带结构来研究电子性质。基于玻尔兹曼输运理论，使用 BoltzTrap 代码计算热电塞贝克系数。
研究意义:: >-
  本文是 MXene 领域早期且极具影响力的理论工作。它不仅系统预测了多种 MXene 的半导体与磁性，为后续实验合成提供了明确的目标清单，更重要的是揭示了”过渡金属价电子数-功能基团吸电子能力-电子结构转变”之间的核心调控规律，即”电子计数规则”，为 MXene 的性质裁剪与功能设计奠定了坚实的理论基础。
研究结论:: >-
  1. 所有原始 MXene 均为金属，但表面功能化是调控其电子性质的关键。2. Sc₂C(F/OH/O)₂、Ti₂CO₂、Zr₂CO₂ 和 Hf₂CO₂ 被预测为半导体，带隙在 0.24-1.8 eV 之间。3. Cr₂C 和 Cr₂N 基 MXene 的基态是铁磁性。4. 半导体性 MXene 在低温（~100 K）下展现出巨大的塞贝克系数（>1000 μV/K），是潜在的优秀低温热电材料。
对领域的贡献:: >-
  1. 建立了“结构-功能化-性质”的理论研究范式，为该领域后续计算研究提供了模板。2. 首次提出“电子计数规则”来解释 MXene 金属-半导体转变的机理。3. 预测了 Sc₂C、Ti₂CO₂ 等半导体与 Cr 基磁性 MXene，极大地激发并引导了相关实验探索。
未来研究方向提及:: >-
  1. 系统研究多层 MXene 的电子性质及层间相互作用。2. 全面评估热电性能，特别是计算晶格热导率，以获得热电优值 ZT。3. 探索通过施加应变等外部手段来调控 MXene 的磁性。4. 合成并验证理论预测的半导体与磁性 MXene。
未来研究方向思考:: >-
  1. 超越 GGA-PBE，使用更精确的杂化泛函（如 HSE06）或 GW 方法重新校准带隙，并探索更多潜在的半导体 MXene。2. 研究混合功能化（如 F 和 OH 共存）以及缺陷对 MXene 性质的影响，构建更接近真实实验条件的模型。3. 将计算预测的范围从本征性质扩展到电子/声子输运、光学、催化等应用相关性质，并结合机器学习进行高通量筛选与逆向设计。
tags:
  - paper
  - type/theory
  - year/2013
  - project/project-2
  - project/project-4
  - relevance/project-2/weak
  - relevance/project-4/weak
  - concept/2d-materials
  - concept/density-functional-theory
  - concept/electron-counting-rule
  - concept/strain-engineering
  - concept/surface-functionalization
  - concept/ferromagnetism
  - concept/thermoelectricity
  - concept/boltzmann-transport
  - concept/max-phase
  - concept/phonon-stability
  - entity/MXenes
  - entity/VASP
  - entity/BoltzTrap
  - entity/MAX-phases
  - entity/Ti2CO2
  - entity/Sc2CF2
  - entity/Sc2CO2
  - entity/Cr2C
  - entity/Cr2N
  - method/dft
  - method/gga-pbe
  - method/paw
  - method/first-principles
  - method/spin-polarized-dft
  - method/formation-energy
  - method/phonon-dispersion
  - method/band-structure
  - method/dos
  - method/boltzmann-transport
  - method/boltztrap
  - material/MXenes
  - material/Ti2C
  - material/Sc2C
  - material/Zr2C
  - material/Hf2C
  - material/Cr2C
  - material/Cr2N
  - material/Ti2CO2
  - material/Sc2CF2
  - material/Sc2C-OH-2
  - material/Sc2CO2
  - material/Zr2CO2
  - material/Hf2CO2
  - topic/2d-materials
  - topic/mxenes
  - topic/magnetism
  - topic/thermoelectricity
  - topic/dft
---

## khazaeiNovelElectronicMagnetic2013 — 二维过渡金属碳化物和氮化物的新型电子和磁性

## 📄 元数据
Khazaei, Arai, Sasaki, Chung, Venkataramanan, Estili, Sakka, Kawazoe et al.，2013，Advanced Functional Materials 23(17): 2185–2192，DOI 10.1002/adfm.201202502

## 💡 一句话
本文用第一性原理系统计算了 F/OH/O 表面功能化的 M₂C/M₂N 型 MXene，提出"电子计数规则"解释金属-半导体转变，预测了 Sc/Ti/Zr/Hf 基半导体 MXene、Cr 基铁磁 MXene 以及低温下 >1000 μV/K 的巨塞贝克系数。

## 🔗 Wiki 双链
  - 概念 [[../concepts/2d-materials]]
  - 概念 [[../concepts/density-functional-theory]]
  - 概念 [[../concepts/electron-counting-rule]]
  - 概念 [[../concepts/strain-engineering]]
  - 概念 [[../concepts/surface-functionalization|表面功能化]]
  - 概念 [[../concepts/ferromagnetism|铁磁性]]
  - 概念 [[../concepts/thermoelectricity|热电效应]]
  - 概念 [[../concepts/boltzmann-transport|玻尔兹曼输运]]
  - 概念 [[../concepts/phonon-stability|声子稳定性]]
  - 实体 [[../entities/MAX-phase]]
  - 实体 [[../entities/MXenes]]
  - 实体 [[../entities/VASP]]
  - 实体 [[../entities/Sc2CO2|Sc₂CO₂]]
  - 实体 [[../entities/Ti2CO2]]
  - 实体 [[../entities/BoltzTrap]]
  - 实体 [[../entities/Sc2CF2]]
  - 实体 [[../entities/Cr2C]]
  - 实体 [[../entities/Cr2N]]
  - 图表 [[../figures/electronic-bands]]
  - 图表 [[../figures/vibrational-spectra]]
  - 年度 [[../write/2010-2014|2013]]
  - 相关论文 [[../../raw/note/khazaeiNovelElectronicMagnetic2013]]

## 🆕 新概念/实体建议
  - [[../entities/BoltzTrap|BoltzTrap]]：基于玻尔兹曼输运方程计算热电系数的开源代码。
  - [[../entities/Ti2CO2|Ti2CO2]] / [[../entities/Sc2CF2|Sc2CF2]] / [[../entities/Cr2C|Cr2C]] / [[../entities/Cr2N|Cr2N]]：本文具体预测的功能化 MXene 实体，可作为 MXene 子条目或在 MXenes 条目中详述。

## 📊 关键图表
  - **图1：MAX 相到 MXene 的结构演变及 A/B 型空心位**
  - ![图1 MAX相到MXene的结构演变及A/B型空心位](../../raw/figures/khazaeiNovelElectronicMagnetic2013/fig_0_A944QDPD.png) -> [[../figures/heterostructures-stacking|异质结与堆叠]]
  - **图示描述**：(a) 层状 M₂AX 块体 MAX 相的典型结构，M（过渡金属）、A（主族元素）、X（C/N）原子层交替堆垛；(b) 移除 A 层后所得二维 M₂X（MXene）的俯视图与侧视图，呈现 M–X–M 三层原子板。
  - **关键特征**：M–X 键为强共价/离子键，M–A 键为较弱的金属键，这是化学刻蚀能选择性去除 A 层的结构基础；俯视图虚线标出 A 型空心位（正下方无 X 原子）和 B 型空心位（正下方有 X 原子），二者是后续 F/OH/O 官能团可能的吸附位点。
  - **结论/意义**：该图奠定全文结构模型的几何语言，所有功能化构型与电子性质差异均围绕 A/B 两类空心位展开。

  - **图4：Ti₂CO₂ 声子色散谱**
  - ![图4 Ti2CO2声子色散谱（无虚频，动力学稳定）](../../raw/figures/khazaeiNovelElectronicMagnetic2013/fig_2_7VHUK5LE.png) -> [[../figures/vibrational-spectra|振动光谱]]
  - **图示描述**：完全氧终止的 Ti₂CO₂ 沿第一布里渊区高对称路径的声子色散曲线，横轴为波矢，纵轴为声子频率（THz）。
  - **关键特征**：图中所有声学支与光学支频率均为正值，没有虚频出现；虚频意味着结构在微小扰动下会自发弛豫到更低能量构型。
  - **结论/意义**：从动力学角度证明 Ti₂CO₂ 等完全功能化 MXene 机械稳定、可实验存在，为后续电子结构与热电性质预测提供了稳定性前提。

  - **图6：Ti₂C、Ti₂CF₂、Ti₂CO₂ 的态密度演变**
  - ![图6 Ti2C、Ti2CF2、Ti2CO2的态密度演变](../../raw/figures/khazaeiNovelElectronicMagnetic2013/fig_6_L6YM244Q.png) -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]
  - **图示描述**：(a–c) 原始 Ti₂C 的总态密度及 Ti、C 原子轨道投影态密度；(d) Ti₂CF₂、(e) Ti₂CO₂ 的态密度，费米能级统一置零。
  - **关键特征**：原始 Ti₂C 费米能级穿过 Ti-d 带，是金属；C-p 带位于 −3 至 −5 eV，与 Ti-d 带之间存在约 1.0 eV 的天然间隙。F 官能化时每个 F 接受 1 个电子，费米能级下移但仍落在 Ti-d 带内，Ti₂CF₂ 保持金属性，并在约 −7 eV 出现 F-p/Ti-d 杂化带。O 官能化时每个 O 接受 2 个电子，Ti(+4) 的价电子恰好满足 C(−4) 与两个 O(−2) 的需求，费米能级被推入 d–p 间隙中心，Ti₂CO₂ 变为带隙 0.24 eV 的间接带隙半导体。
  - **结论/意义**：以 Ti 系为例直观演示了"电子计数规则"——官能团吸电子数与金属价电子数是否匹配决定金属–半导体转变，是全文核心机理图。

  - **图7：Sc₂C 及其 F/O 功能化体系的态密度**
  - ![图7 Sc2C及其F/O功能化体系的态密度](../../raw/figures/khazaeiNovelElectronicMagnetic2013/fig_7_2JKX7NVX.png) -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]
  - **图示描述**：(a–c) 原始 Sc₂C 的总态密度及 Sc、C 投影态密度；(d) Sc₂CF₂、(e) 假设取模型 2 构型时 Sc₂CO₂ 的态密度，费米能级置零。
  - **关键特征**：原始 Sc₂C 费米能级位于 Sc-d 带内，为金属，C-p 带与 Sc-d 带间约有 0.5 eV 间隙。Sc 最高氧化态为 +3，每个 F/OH 仅需 1 个电子，因此 F 或 OH 官能化后费米能级即落入间隙，Sc₂CF₂（带隙 1.03 eV）和 Sc₂C(OH)₂（带隙 0.45 eV，直接带隙）为半导体。若 Sc₂CO₂ 采用模型 2（O 均在 A 位），O 共需 4 个电子而 Sc 只能提供 3 个，费米能级仍落在 d 带内呈金属性；这与总能计算矛盾，提示真实稳定构型另有其图。
  - **结论/意义**：通过对比 Ti(+4) 与 Sc(+3) 的价电子差异，阐明为何 Sc 系在 F/OH 下即可半导体化，并为图 8 的模型 3 重构埋下伏笔。

  - **图8：Sc₂CO₂ 模型 3 的分波态密度**
  - ![图8 Sc2CO2模型3的分波态密度（O_B-C杂化导致绝缘体）](../../raw/figures/khazaeiNovelElectronicMagnetic2013/fig_2013_9WCGT42E.png) -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]
  - **图示描述**：Sc₂CO₂ 最稳定构型（模型 3：一个 O 在 A 型空心位 O_A，另一个 O 移至 B 型空心位 O_B）的总态密度，以及 Sc_A/Sc_B、C、O_A/O_B 的分波投影态密度。
  - **关键特征**：O-p 能带因局域构型不同而分裂为 O_B p 带（−6.5 至 −5 eV）和 O_A p 带（−4.5 至 −3 eV），均与 Sc-d 轨道杂化；Sc_A–O_A、Sc_B–O_B 距离分别为 2.085 Å 和 2.101 Å。关键在于 O_B pz 与下方 C pz 轨道直接杂化，O_B–C 距离仅 1.65 Å（短于 O_B–Sc_B），在 1.0–1.5 eV 处形成 C pz–O_B pz 反键态，该未占据反键态的分裂打开了约 1.8 eV 的带隙。
  - **结论/意义**：解释了当金属无法提供足够电子时，O 原子通过迁移到 B 位与 C 直接成键来"自救"获电子，使 Sc₂CO₂ 成为绝缘体；这是电子计数规则在电子供求失衡时驱动结构重构的典型案例。

  - **图9：Ti₂CO₂ 和 Sc₂C(OH)₂ 的塞贝克系数随化学势变化**
  - ![图9 Ti2CO2和Sc2C(OH)2的塞贝克系数随化学势变化](../../raw/figures/khazaeiNovelElectronicMagnetic2013/fig_850_F5TPYD5G.png) -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]
  - **图示描述**：基于 BoltzTrap 计算的单层 Ti₂CO₂（a）和 Sc₂C(OH)₂（b）塞贝克系数 S 随电子化学势 μ 的变化曲线，不同曲线对应不同温度；Ti₂CO₂ 价带/导带边位于 −0.12 和 +0.12 eV，Sc₂C(OH)₂ 位于 −0.225 和 +0.225 eV。
  - **关键特征**：在约 100 K 低温下，Ti₂CO₂ 塞贝克系数峰值约 1140 μV/K；带隙更大的 Sc₂C(OH)₂（0.45 eV）在相同温度下峰值更高。巨大 S 值源于带边附近态密度的剧烈反差（导带底 DOS 极高、价带顶 DOS 极低）。作为对比，SrTiO₃ 在 90 K 的巨塞贝克系数约为 850 μV/K，商用 Bi₂Te₃ 仅约 ±200 μV/K。
  - **结论/意义**：预测半导体性 MXene 是潜在的高性能低温热电材料；作者同时指出完整 ZT 评估还需电导率 σ 与晶格/电子热导率 κl、κe。

  - **表3：Cr₂C/Cr₂N 功能化体系的磁矩与铁磁–非磁能量差**
  - ![表3 Cr2C/Cr2N功能化体系的磁矩与铁磁-非磁能量差](../../raw/figures/khazaeiNovelElectronicMagnetic2013/tab_2_H34HFH2L.png) -> [[../figures/electronic-bands-cdw-transport|CDW与输运性质]]
  - **图示描述**：自旋极化 GGA/PBE 计算得到的 Cr₂C、Cr₂N 经 F、OH、O 官能化后的磁基态、每个 Cr 原子的磁矩（μB/Cr）以及铁磁态相对非磁态的能量差 ΔE（eV/Cr）。
  - **关键特征**：Cr₂CF₂ 磁矩 2.71 μB/Cr、ΔE = −0.12 eV/Cr；Cr₂C(OH)₂ 磁矩 2.24 μB/Cr、ΔE = −0.08 eV/Cr；Cr₂CO₂ 磁矩为 0、非磁。Cr₂NF₂ 磁矩 3.23 μB/Cr、ΔE = −0.35 eV/Cr；Cr₂N(OH)₂ 磁矩 3.01 μB/Cr、ΔE = −0.26 eV/Cr；Cr₂NO₂ 磁矩 2.50 μB/Cr、ΔE = −0.49 eV/Cr。磁性均来源于 Cr 的 d 轨道，ΔE 数值较大，预示铁磁序可能维持到近室温。
  - **结论/意义**：首次理论预测了 Cr 基 MXene 的铁磁性，将 MXene 的性质空间从半导体拓展到磁性二维材料，并提出应变可进一步调控磁性（类比 VS₂、VSe₂）。


## 🔬 项目连接
  - **project-2（Mn多铁）— weak**：本文用自旋极化 GGA/PBE 预测 Cr 基 MXene 的铁磁基态，并明确提出应变可诱导/调控二维磁性（类比 VS₂、VSe₂）。这套"磁性二维体系的 DFT 稳定性 + 磁矩 + FM/非磁能量差"计算流程，对 Mn 基多铁体系中磁序判定与应变调控有方法学参考价值；材料体系本身不重叠。
  - **project-4（TTF分子计算）— weak**：本文以离子价态/电子供求关系解释结构稳定性与金属-半导体转变（电子计数规则），并以电荷转移 + 轨道杂化分析成键；这种"价电子计数 + DFT 验证"的思路可类比迁移到 TTF 类电荷转移分子晶体的计算分析。
  - **project-5（SnTe铁电模拟）— weak**：同属二维/层状材料的 DFT 电子结构计算，表面终止（F/OH/O）显著改变带隙与能带对齐的物理图像，对 SnTe 表面/界面工程与能带调控有物理类比意义；但本文不涉及铁电或拓扑。
  - project-1（双光子）、project-3（机械发光NN）、project-6（湿度传感器）、project-7（CDW）：无直接项目连接。（MXene 虽可用于湿度传感，但本文未涉及传感机制。）

## 🔗 项目双链
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]
- 项目 [[../projects/project-4-ttf-molecular-calc|项目四：lsl老师的ttf分子计算]]

## 📝 组织与用词
  文章按"背景 → 计算细节 → 四种表面吸附构型模型 → 稳定性筛选（总能/形成能/化学势/声子谱）→ 电子结构（DOS/能带）→ 磁性 → 热电 → 结论"的经典计算材料范式展开。核心论证是把复杂的 DFT 结果归结为一个直观的"电子计数"图像：过渡金属 M 的价电子数与 X（C/N）+ T（F/OH/O）的吸电子需求是否匹配，决定费米能级落入 M-d 带还是落入 d-p 间隙。
  值得复用的术语：
  - MXenes [[../entities/MXenes|MXenes]] / MXene（过渡金属碳/氮化物二维材料）
  - MAX phases / MAX 相 [[../entities/MAX-phase]]
  - [[../concepts/surface-functionalization|surface functionalization / termination]]（表面功能化/终止）
  - [[../concepts/electron-counting-rule|electron counting rule]]（电子计数规则）
  - hollow sites A / B（A/B 型空心位）
  - [[../concepts/formation-energy|formation energy]]（形成能）
  - Seebeck coefficient（塞贝克系数）
  - figure of merit ZT（热电优值）

  - [[../entities/MAX-phase]]
## ✏️ 可写入 Wiki 的要点
  1. 原始（未功能化）M₂X MXene 全部为金属，费米能级落在过渡金属 d 带；C/N 的 p 带位于 d 带下方，二者间存在约 0.5–1.0 eV 的天然间隙。
  2. 功能基团作为电子受体从 M 抽走电子：F/OH 各接受 1 个电子，O 接受 2 个电子；当 M 的价电子恰好满足 X 和 T 的需求时，费米能级落入 d-p 间隙，体系变为半导体——即"[[../concepts/electron-counting-rule|电子计数规则]]"。
  3. 预测的半导体 MXene 及 PBE 带隙：Sc₂CF₂ 1.03 eV、Sc₂C(OH)₂ 0.45 eV（直接带隙）、Sc₂CO₂ 1.8 eV、Ti₂CO₂ 0.24 eV、Zr₂CO₂ 0.88 eV、Hf₂CO₂ 1.0 eV；除 Sc₂C(OH)₂ 外均为间接带隙。
  4. Ti(+4)、Zr(+4)、Hf(+4) 能同时满足 C(-4) 和两个 O(-2)，故 O 功能化后为半导体；Sc(+3) 只需 F/OH(-1) 即可饱和，故 Sc₂CF₂、Sc₂C(OH)₂ 为半导体。
  5. Sc₂CO₂ 因 Sc 无法提供两个 O 所需的 4 个电子，稳定构型为模型 3：一个 O 移至 B 型空心位直接与下方 C 成键（O_B–C 距离 1.65 Å），O_B pz 与 C pz 杂化，反键态位于 1.0–1.5 eV，使体系成为绝缘体。
  6. 表面吸附构型选择规律：若 M 能提供足够电子，模型 2（基团在 A 型空心位）最稳定；电子不足时模型 3 或 4（基团在 B 型空心位，可与 X 杂化获电子）更稳定；顶位吸附（模型 1）通常最不稳定。
  7. [[../concepts/formation-energy|形成能]]公式 Hf = Etot(M₂XYₙ) − Etot(M₂X) − (n/2)Etot(Y₂) − nΔμ；所有体系形成能均为约 −7 至 −12 eV 的大负值，证明完全功能化热力学高度有利；Ti₂C 在 −4.0–0.0 eV 氧[[../concepts/chemical-potential|化学势]]范围内完全氧覆盖（Ti₂CO₂）最稳定。
  8. Ti₂CO₂ 声子谱全正（无虚频），证明完全功能化 MXene 动力学/机械稳定；多层 MXene 层间距约 3.0 Å，主要靠范德华作用结合，费米能级附近电子结构与单层差异不大。
  9. Cr₂CF₂、Cr₂C(OH)₂、Cr₂NF₂、Cr₂N(OH)₂、Cr₂NO₂ 基态为[[../concepts/ferromagnetism|铁磁性]]，磁矩 2.24–3.23 μB/Cr，FM 与非磁态能量差 −0.08 至 −0.49 eV/Cr，预示磁性可能维持到近室温；磁性源于 Cr 的 d 轨道。
  10. 基于 BoltzTrap 的热电计算：Ti₂CO₂ 在 ~100 K 塞贝克系数峰值约 1140 μV/K，可与 SrTiO₃ 的巨塞贝克系数（~850 μV/K @90 K）相比；带隙更大的 Sc₂C(OH)₂ 峰值更高，源于带边附近[[../concepts/density-of-states|态密度]]的剧烈反差。作者指出完整 ZT 评估还需电导率 σ 与晶格/电子热导率 κl、κe。
