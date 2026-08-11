---
citekey: miaoMagneticFerroelectricMetal2024
title: "Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding"
authors: [Xiaoyan Miao, Milorad Milošević, Chunmei Zhang]
year: 2024
journal: "Physica B: Condensed Matter"
doi: "10.1016/j.physb.2024.416427"
url: "https://doi.org/10.1016/j.physb.2024.416427"
paper_type: theory
status: ingested
year_read: 2026
original_note: "[[../../raw/note/miaoMagneticFerroelectricMetal2024]]"
projects: [project-2, project-5]
concepts: [multiferroicity, magnetoelectric-coupling, sliding-ferroelectricity, strain-engineering, 2d-materials, polarization-switching, density-functional-theory, ferroelectric-metal, magnetic-polar-metal, interlayer-charge-transfer, itinerant-ferromagnetism]
entities: [Fe3GeTe2, VASP, WTe2, In2Se3, h-BN, TMDs]
methods: [dft, dft-plus-u, dft-d3, gga-pbe, paw, neb, bader-charge-analysis, band-structure, dos, dipole-correction]
materials: [Fe3GeTe2, WTe2, In2Se3]
figures: [crystal-structures, electronic-bands, mathematical-models]
"领域基础知识": >-
  二维范德华材料、层间堆垛工程、铁电性、铁磁性、金属性、第一性原理计算。
"研究背景": >-
  传统的铁电性和金属性难以共存，而将磁性引入其中形成"磁性极性金属"则更具挑战性。二维范德华材料的层间弱相互作用为通过层间滑移来设计新型量子态提供了可能。
"作者的问题意识": >-
  能否在一种本征的二维铁磁金属中，通过层间滑移这种简单可控的方式，同时实现可翻转的铁电极化和未受屏蔽的金属导电性，从而获得一种极其罕见的磁性铁电金属相？
"主要研究对象": >-
  双层Fe₃GeTe₂ (FGT) 在特定层间滑移操作下的稳定构型（State-1 (1/3, 1/3) 和 State-2 (-1/3, -1/3)）。
"主要研究方法": >-
  基于密度泛函理论 (DFT) 的第一性原理计算，包括结构弛豫、能量计算、Bader电荷分析、NEB方法计算极化翻转势垒、以及电子结构（能带、态密度）分析。
"研究意义": >-
  理论上，拓展了滑移铁电家族到磁性体系，揭示了"磁-电-极"三者共存的物理机制。实践上，为实验制备提供了明确目标，并有望推动基于磁电耦合和自旋电子学的新型低功耗、多功能器件开发。
"研究结论": >-
  在FGT双层中，通过 (1/3, 1/3) 和 (-1/3, -1/3) 的层间滑移操作，可诱导出可切换的垂直极化，同时保持了体系的巡游铁磁性和金属性，成功证明了一种磁性铁电金属相的存在。额外施加中等双轴应变能够反转极化方向。
"对领域的贡献": >-
  提出并验证了在二维极限下，利用层间滑移工程在单一材料中同时实现铁磁性、金属性和可切换铁电性的新范式，为寻找和设计多铁性量子材料开辟了新路径。
"未来研究方向提及": >-
  作者呼吁进行实验验证，并将该层间滑移方法推广到其他二维磁性材料体系中。
"未来研究方向思考": >-
  探索该体系中的磁电耦合效应、研究潜在的拓扑电子态、设计具体的器件模型并评估其性能、以及研究其中的极化畴和磁畴动力学。
tags:
  - paper
  - type/theory
  - year/2024
  - project/project-2
  - project/project-5
  - relevance/project-2/strong
  - relevance/project-5/medium
  - concept/multiferroicity
  - concept/magnetoelectric-coupling
  - concept/sliding-ferroelectricity
  - concept/strain-engineering
  - concept/2d-materials
  - concept/polarization-switching
  - concept/density-functional-theory
  - concept/ferroelectric-metal
  - concept/magnetic-polar-metal
  - concept/interlayer-charge-transfer
  - concept/itinerant-ferromagnetism
  - entity/Fe3GeTe2
  - entity/VASP
  - entity/WTe2
  - entity/In2Se3
  - entity/h-BN
  - entity/TMDs
  - method/dft
  - method/dft-plus-u
  - method/dft-d3
  - method/gga-pbe
  - method/paw
  - method/neb
  - method/bader-charge-analysis
  - method/band-structure
  - method/dos
  - method/dipole-correction
  - material/Fe3GeTe2
  - material/WTe2
  - material/In2Se3
  - topic/multiferroics
  - topic/2d-materials
  - topic/ferroelectricity
  - topic/magnetism
  - topic/sliding-ferroelectricity
  - topic/ferroelectric-metal
  - topic/spintronics
---

## miaoMagneticFerroelectricMetal2024 — 层间滑动作用下双层Fe3GeTe2中的磁性铁电金属

- **元数据**：Xiaoyan Miao, Milorad Milošević, Chunmei Zhang，2024，Physica B: Condensed Matter 694, 416427，DOI [10.1016/j.physb.2024.416427](https://doi.org/10.1016/j.physb.2024.416427)
- **一句话**：基于第一性原理计算预测双层 Fe₃GeTe₂ 通过 (±1/3, ±1/3) 层间滑移可同时拥有可翻转的垂直铁电极化、巡游铁磁性和金属导电性，构成罕见的磁性铁电金属相，且中等双轴压缩应变即可反转极化方向。
- **现有wiki双链**：
  - 概念 [[../concepts/multiferroicity]]、[[../concepts/magnetoelectric-coupling]]、[[../concepts/sliding-ferroelectricity]]、[[../concepts/strain-engineering]]、[[../concepts/2d-materials]]、[[../concepts/polarization-switching]]、[[../concepts/density-functional-theory]]
  - 实体 [[../entities/Fe3GeTe2]]、[[../entities/VASP]]、[[../entities/WTe2]]、[[../entities/In2Se3]]、[[../entities/h-BN]]、[[../entities/TMDs]]
  - 图表 [[../figures/crystal-structures]]、[[../figures/electronic-bands]]、[[../figures/mathematical-models]]
  - 年度 [[../write/2024]]
  - 项目 [[../projects/project-2-mn-multiferroics]]、[[../projects/project-5-snte-ferroelectric-sim]]
  - 相关论文 [[../../raw/note/miaoMagneticFerroelectricMetal2024]]
- **新概念/实体建议**：
  - `ferroelectric-metal`（铁电金属/极性金属）：Anderson–Blount 1965 年提出的概念，指金属中可切换极性畸变与导电性共存；本文是其二维磁性版本。
  - `magnetic-polar-metal`（磁性极性金属）：同时具备磁序、极性结构畸变和金属导电性的稀有物相，区别于仅极性+金属的 polar metal。
  - `interlayer-charge-transfer`（层间电荷转移）：滑移铁电性的微观机制，未补偿的垂直层间电荷得失形成面外偶极矩，可作为 sliding-ferroelectricity 的子概念。
  - `itinerant-ferromagnetism`（巡游铁磁性）：FGT 中由 Fe 3d 传导电子承载的铁磁性，区别于局域磁矩铁磁，可作为 magnetism 类概念补充。
- **关键图表**：
  - ![图1 IM/State-1/State-2原子结构、极化等高线与NEB翻转势垒](../../raw/figures/miaoMagneticFerroelectricMetal2024/fig_1_SVDXYJ6N.png)
  - ![图2 FGT单层与State-1/State-2双层的自旋极化能带](../../raw/figures/miaoMagneticFerroelectricMetal2024/fig_2_HRQRQ5VP.png)
  - ![图3 Fe-d轨道投影态密度与自旋分辨轨道投影能带](../../raw/figures/miaoMagneticFerroelectricMetal2024/fig_3_JXUJYRXV.png)
  - ![图4 双轴压缩应变对State-1/State-2极化的调控](../../raw/figures/miaoMagneticFerroelectricMetal2024/fig_4_WEH6C4WM.png)
  - ![表1 不同滑移操作下双层FGT的相对能量](../../raw/figures/miaoMagneticFerroelectricMetal2024/tab_1_T9BJAJ33.png)
- **项目连接**：
  - **project-2（Mn多铁）— strong**：本文核心问题正是磁性与铁电极化在金属体系中的共存，直接提供"磁性铁电金属"这一多铁性新范式；其"垂直极化—面内导电解耦""层间电荷转移生极化""滑移不破坏 FM 基态"等机制，以及 FM/AFM 能量对比、U\* 处理 Fe 3d 的流程，对 Mn 基多铁（尤其是金属/半金属多铁）的磁电共存机理分析有直接参考价值。
  - **project-5（SnTe铁电模拟）— medium**：方法学可直接复用——经典电动力学 ∫ρz dz 计算面外极化、CI-NEB 算翻转势垒、双轴应变调控极化方向、DFT-D3 描述层间相互作用、Bader 电荷分析追踪极化起源，均是 SnTe 铁电模拟中常用的计算组合；其"电子极化与离子极化竞争导致应变下极化反转"的分析框架也可迁移到 SnTe 应变工程讨论。材料本身（FGT vs SnTe）和维度不同，故定为 medium。
  - 其他项目（project-1/3/4/6/7）：无直接连接。
- **组织与用词**：文章按"提出悖论（铁电vs金属vs磁三者互斥）→选材（二维vdW巡游铁磁金属FGT）→方法（DFT-D3+U\*+NEB）→能量筛选最稳滑移态→逐项验证铁电/磁/金属三性→应变调控"的递进链组织；先用表1能量比较锁定 State-1/2，再用 Bader 电荷解释极化起源、FM/AFM 能量对比确认磁基态、能带/DOS 确认金属性，最后加应变旋钮，逻辑闭环完整。值得复用的术语：铁电金属（ferroelectric metal）、磁性极性金属（magnetic polar metal）、滑移铁电性（sliding ferroelectricity）、未补偿层间电荷转移（uncompensated interlayer charge transfer）、面内-面外解耦（in-plane/out-of-plane decoupling）、巡游铁磁性（itinerant ferromagnetism）、极化翻转势垒（polarization switching barrier）、双轴应变调控（biaxial strain engineering）。
- **可写入wiki的要点**：
  - 双层 FGT 通过相对滑移 (1/3,1/3) 和 (−1/3,−1/3) 得到两个能量简并的最稳态 State-1/State-2，分别具 P↑/P↓ 垂直极化，大小均为 ±8.3×10⁻⁴ eÅ/unit cell；其他滑移构型能量高 19.6–21.4 meV。
  - CI-NEB 计算的 P↑↔P↓ 翻转势垒约 13 meV/unit cell，低于 In₂Se₃（~60 meV/unit cell）而高于 WTe₂（~0.6 meV/unit cell），因只需克服弱层间 vdW 相互作用，室温下可翻转。
  - 极化微观起源：Bader 电荷分析显示 State-1 中顶层与底层电荷得失约 0.03 e，未补偿的垂直层间电荷转移形成面外偶极矩；State-2 电荷转移方向相反，极化随之翻转。
  - 磁基态：层内为 FM，层间 FM 构型比 AFM 能量更低；滑移不改变 FGT 的铁磁基态。双层相比块体层数减少使 Pauli 势降低，反而增强 FM 型层间交换耦合。Fe 3d 轨道通过线性响应法获取 U\* 值进行在位库仑修正。
  - 金属性：费米能级附近态密度和能带主要由 Fe 3d 轨道贡献；面内传导电子在垂直方向受限，与面外极化空间解耦（类比 WTe₂ 双层），故自由电子不屏蔽垂直偶极矩，使金属性与铁电性共存。
  - 应变调控：约 −1% 双轴压缩应变即使 State-1/State-2 极化方向反转；机制是应变让层内 FeII 与 Ge 原子偏离 z 方向镜面位置、产生反向离子极化，当离子极化贡献超过电子极化贡献时总极化反转。ε=−1%,−2%,−3%,−4% 时 State-1 极化约 −1.3,−1.8,−3.6×10⁻⁴ 和 −3.1×10⁻³ eÅ/unit cell，绝对值随应变增大。
  - 计算参数：VASP + PAW + GGA-PBE + DFT-D3，平面波截断 500 eV，Γ 中心 8×8×1 k 网格，真空层 ≥30 Å，力收敛 0.001 eV/Å、能量收敛 10⁻⁶ eV；极化由经典电动力学 ∫ρz dz 在整个超胞积分得到并加偶极校正。
  - 结构背景：FGT 单层为 P6₃/mmc 六方中心对称结构，五层原子次序 Te–Fe–(FeII,Ge)–Fe–Te，Fe 占两个不等价 Wyckoff 位（FeI, FeII）；块体 AB 堆叠具反演对称，AA 堆叠双层有 Mz 镜像但直接叠出的 IM 态不稳定，会自发滑移到 State-1/2。
