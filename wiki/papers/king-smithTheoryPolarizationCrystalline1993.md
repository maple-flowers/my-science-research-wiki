---
citekey: king-smithTheoryPolarizationCrystalline1993
title: "Theory of polarization of crystalline solids"
authors: [King-Smith R. D., Vanderbilt David]
year: 1993
journal: "Physical Review B"
doi: "10.1103/PhysRevB.47.1651"
url: "https://doi.org/10.1103/PhysRevB.47.1651"
paper_type: theory
status: ingested
year_read: 2026
original_note: "[[../../raw/note/king-smithTheoryPolarizationCrystalline1993]]"
projects: [project-5, project-2]
concepts: [berry-phase, berry-connection, modern-polarization-theory, wannier-function, born-effective-charge, polarization-quantum, piezoelectricity, polarization-switching, density-functional-theory, ferroelectricity]
entities: [GaAs, VASP, Wannier90, Quantum-ESPRESSO]
methods: [dft, berry-phase, lda, pseudopotential, monkhorst-pack, dfpt-linear-response]
materials: [GaAs]
figures: [mathematical-models]
"领域基础知识": >-
  需要掌握晶体平移对称性与布洛赫定理、Kohn–Sham 密度泛函理论（DFT）、平面波赝势方法，以及布里渊区积分等基本能带论工具；同时要熟悉贝里相位（Berry phase）/几何相位这一量子力学概念，以及瓦尼尔函数（Wannier function）作为布洛赫波在实空间的局域表示。理解压电效应、铁电效应、热电效应等宏观极化响应现象有助于把握论文动机。
"研究背景": >-
  1993 年以前，晶体电极化 P 无法从第一性原理严格定义：在无限周期体系中位置算符病态，P=(1/V)∫ρr dr 的结果依赖于晶胞边界的任意选取；超胞法破坏周期性且引入表面效应，线性响应（DFPT）虽严谨但实现复杂。实验上压电、热释电、铁电极化翻转等均可测量极化的"变化量"ΔP，但缺乏一个只依赖体相波函数、便于在常规 DFT 代码中实现的理论公式。
"作者的问题意识": >-
  作者要回答：能否绕开"绝对极化"无法定义的困境，直接给出一个在物理上可观测、在数值上可计算、只依赖初末态价带波函数的极化"有限变化量"ΔP 的普适表达式？并进一步给出一个能在常规迭代对角化 DFT 框架下稳健实现、且不受波函数随机相位影响的数值方案。
"主要研究对象": >-
  理论对象是在保持平移对称性、宏观电场 E=0 条件下，Kohn–Sham 哈密顿量沿参数 λ∈[0,1] 发生绝热变化的绝缘晶体。数值验证选用闪锌矿结构的砷化镓（GaAs）：这是典型的压电 III–V 族半导体，压电张量只有一个独立分量 γ₁₄，且有成熟的线性响应计算与实验值可作比对，便于干净地检验新方法。
"主要研究方法": >-
  理论推导：从绝热电流的 Kubo 公式（式 1，Resta 启发式给出）出发，借用 Thouless 等在量子霍尔效应中的技巧把价带–导带求和改写为仅含价带晶胞周期函数 u_{kn} 对 k、λ 导数的布里渊区积分（式 4）；在周期性规范 u_{k+G,n}=u_{k,n} 下分部积分得到核心式 (8)：ΔP=P(1)−P(0)，其中 P(λ)=(ife/8π³)Σ_n∫dk ⟨u_{kn}|∂_k|u_{kn}⟩，即价带贝里联络在 BZ 的积分（Zak 相位）。借助 Wannier 函数证明 ΔP=(fe/Ω)Σ_n R_n，即 Wannier 电荷中心位移之和。数值实现采用沿短倒格矢 G∥ 的 k 点串（J 个点）上的对数行列式 φ=Im ln Π_j det⟨u_{k_j}|u_{k_{j+1}}⟩（式 15），该量对每个 k 点的任意波函数相位规范不变。GaAs 计算使用模守恒非局域赝势、LDA（Wigner 形式）、20 Ry 平面波截断、(4,4,4) Monkhorst–Pack 网格自洽，ΔP 积分用 16 个 k⊥ 点 × 10 点 k∥ 串；理论晶格常数 a=5.576 Å；Ga 沿 (001) 位移 0.01a 求 Z*；施加 1% xy 剪切应变求 γ'₁₄。
"研究意义": >-
  这篇论文奠定了"现代极化理论"（Modern Theory of Polarization）：它把宏观极化变化严格地建立在价带波函数的几何相位（贝里相位）之上，使第一性原理计算自发极化、玻恩有效电荷、压电张量、热释电系数以及铁电极化翻转成为常规操作，是此后 VASP、Quantum ESPRESSO、ABINIT 等所有主流 DFT 代码中 LCALCPOL/berry 类算法的源头。它也首次在体相热力学量层面揭示了几何/拓扑相位的可观测后果，为后来的拓扑绝缘体电极化描述提供了思想雏形。
"研究结论": >-
  （1）晶体在绝热变化下的极化变化量 ΔP 严格等于初末态价带波函数贝里相位之差，等价于所有占据态 Wannier 函数电荷中心位移的矢量和 ΔP=(fe/Ω)Σ_n R_n。（2）当哈密顿量沿闭合绝热路径回到自身时，ΔP 被量子化为 (fe/Ω)R 的整数倍（R 为格矢），这是一维 Zak 相位/量子化极化的体现，并与量子霍尔效应量子化电导形成深刻类比。（3）对 GaAs 的计算给出 a=5.576 Å、Z*_Ga=1.984（线性响应 1.994，实验 2.16）、(a/e)γ'₁₄=−1.352（线性响应 −1.405）、总压电常数 γ₁₄=−0.28（线性响应 −0.35，实验 −0.32 C/m²），与已有理论和实验合理吻合；γ₁₄ 是电子项与离子项强相消后的小量，新方法能稳定捕捉这一精细抵消。（4）使用非局域赝势时式 (1) 动量算符需修正，但晶胞周期哈密顿量有精确补偿修正，从式 (4) 起的结论不变。
"对领域的贡献": >-
  相对于此前依赖超胞表面建模或复杂线性响应理论的状况，本文首次给出了一个无需导带、无需超胞、仅需价带波函数在初末态两次自洽计算加后处理即可得到 ΔP 的普适公式与规范不变数值算法（式 15 的离散 k 串对数行列式），并赋予其"Wannier 电荷中心位移"的清晰物理图像。它把极化从"静态电荷分布"观转变为"绝热流 + 几何相位"观，确立了极化是定义在模 eR/Ω 上的多值物理量这一现代认识，与 Resta、Vanderbilt 后续工作共同构成现代极化与轨道磁化理论的基石，并直接催生了铁电材料自发极化的第一性原理预测产业。
"未来研究方向提及": >-
  作者在结尾明确指出：把式 (8b) 中的 P(λ) 直接当作"绝对极化"是诱人的，虽然它只在模 efR/Ω 意义下良定义；"这种等同在何种条件下有用"将是后续通讯（future communication）的主题。论文还把适用范围限定在 E=0、绝热路径上全程保持绝缘、且势变化保持平移对称的情形，金属/能隙闭合路径、有限电场、非周期扰动留待后续。
"未来研究方向思考": >-
  （1）对 project-5（SnTe 铁电模拟）：Berry 相极化是计算 SnTe 薄膜/块体自发极化、极化翻转路径 ΔP、以及 Born 有效电荷随应变/层厚演化的标准工具，可与 LAMMPS/DeepMD 势函数得到的结构耦合，把 DFT 端的极化数据作为势函数拟合或验证目标；应注意"极化量子 eR/Ω"在小原胞中可能与真实 ΔP 同量级，需沿绝热中间态细分 λ 以去量子。（2）对 project-2（Mn 多铁）：在 Mn 基极化结构中用 Berry 相计算电子极化贡献、磁电耦合中极化随磁序变化的响应，并结合 DFT+U 考察局域 d 电子对 Z* 与 γ 的修正。（3）方法学上可延伸到：能隙闭合路径（极化相变）如何处理、有限电场下的现代极化理论、轨道磁化的 Berry 相公式、以及用 Wannier 电荷中心追踪拓扑绝缘体/高阶拓扑绝缘体的边界极化。（4）把 Berry 相极化作为高通量筛选二维铁电/滑动铁电/多铁材料的标准描述符，与本库 sliding-ferroelectricity、polarization-switching 等条目打通。
tags:
  - paper
  - type/theory
  - year/1993
  - project/project-5
  - project/project-2
  - relevance/project-5/core
  - relevance/project-2/strong
  - concept/berry-phase
  - concept/berry-connection
  - concept/modern-polarization-theory
  - concept/wannier-function
  - concept/born-effective-charge
  - concept/polarization-quantum
  - concept/piezoelectricity
  - concept/polarization-switching
  - concept/density-functional-theory
  - concept/ferroelectricity
  - entity/GaAs
  - entity/VASP
  - entity/Wannier90
  - entity/Quantum-ESPRESSO
  - method/dft
  - method/berry-phase
  - method/lda
  - method/pseudopotential
  - method/monkhorst-pack
  - method/dfpt-linear-response
  - material/GaAs
  - topic/ferroelectricity
  - topic/piezoelectricity
  - topic/berry-phase
  - topic/dft-methodology
  - topic/multiferroics
---

## king-smithTheoryPolarizationCrystalline1993 — 晶体固体的极化理论（现代极化理论奠基论文）

- **元数据**：R. D. King-Smith、David Vanderbilt（Rutgers 大学），1993 年，*Physical Review B* **47**(3), 1651–1654，DOI [10.1103/PhysRevB.47.1651](https://doi.org/10.1103/PhysRevB.47.1651)。
- **一句话**：本文证明晶体的电极化变化量 ΔP 等于价带波函数贝里相位之差，物理上等价于 Wannier 函数电荷中心的位移，从而奠定了沿用至今的"现代极化理论"及其第一性原理数值算法。

- **现有 wiki 双链**：
  - 概念 [[../concepts/berry-phase]]
  - 概念 [[../concepts/polarization-switching]]
  - 概念 [[../concepts/density-functional-theory]]
  - 实体 [[../entities/GaAs]]
  - 实体 [[../entities/VASP]]
  - 实体 [[../entities/Wannier90]]
  - 图表 [[../figures/mathematical-models]]
  - 年度 [[../write/1993]]
  - 项目 [[../projects/project-5-snte-ferroelectric-sim]]
  - 项目 [[../projects/project-2-mn-multiferroics]]
  - 相关论文 [[../../raw/note/king-smithTheoryPolarizationCrystalline1993]]

- **新概念/实体建议**：
  - `modern-polarization-theory.md`（概念）：现代极化理论，把宏观极化变化建立在价带 Berry 相位/Wannier 中心位移之上的理论框架，应作为 berry-phase 条目下的主干子条目，并串联 polarization-switching、born-effective-charge。
  - `wannier-function.md`（概念）：布洛赫波在实空间的局域傅里叶变换表示，Wannier 电荷中心位移是极化变化的直观物理图像；与已有实体 Wannier90 互链。
  - `berry-connection.md`（概念）：A_n(k)=i⟨u_{kn}|∇_k|u_{kn}⟩，贝里联络，其在 BZ 的积分即 Berry/Zak 相位，是 P(λ) 的被积函数。
  - `born-effective-charge.md`（概念）：Z*_{α,β}= (Ω/e) ∂P_α/∂u_β，原子位移引起的极化响应张量，是铁电/压电材料的关键微观量，可由 Berry 相方法直接计算。
  - `polarization-quantum.md`（概念）：极化量子 eR/Ω，反映极化作为多值（lattice-valued）物理量的模不确定性，是解读 Berry 相计算结果分支选择的依据。
  - `piezoelectricity.md`（概念）：压电效应，应变诱导极化（γ₁₄ 等），本文用 GaAs 作为方法验证对象；可与后续热电、铁电条目并列。
  - `Quantum-ESPRESSO.md`（实体）：主流开源 DFT 代码，内置 Berry 相极化（epsi/pieze）模块，与 VASP 的 LCALCPOL、ABINIT 的 berry  optdriver 并列，是现代极化理论的直接实现载体。

- **关键图表**：笔记未附图片（raw/figures 目录仅含 manifest.json）。论文正文唯一数据表为 Table I（GaAs 理论与实验压电响应对比）：

  | 量 | 本工作 | 线性响应 | 实验 |
  |---|---|---|---|
  | a (Å) | 5.576 | 5.496 | 5.642 |
  | Z*_Ga (e) | 1.984 | 1.994 | 2.16 |
  | (a/e)γ'₁₄ | −1.352 | −1.405 | — |
  | γ₁₄ | −0.28 | −0.35 | −0.32 |

- **项目连接**：
  - **project-5（lammps 势函数 SnTe 铁电模拟）— core**：本文是 SnTe 铁电极化 Berry 相计算的方法学源头。SnTe 作为岩盐结构铁电体，其自发极化、极化翻转路径上的 ΔP、Born 有效电荷以及应变/层厚对极化的调控，都必须用本文建立的 Berry 相公式在 DFT 端算出，再作为 LAMMPS/DeepMD 势函数的拟合或验证目标；需要沿 λ 路径细分以避开 eR/Ω 量子分支选择问题，这一注意事项直接来自本文。
  - **project-2（Mn 极化结构铁电材料）— strong**：项目涉及多层黑磷应力极化、MoS₂ 应变能带、Mn 基多铁等 DFT 计算，自发极化与极化翻转的定量计算均以 Berry 相方法为标准工具；在含 Mn 的关联体系中需结合 DFT+U，但极化的几何相位定义与数值算法仍遵循本文式 (8)、(15)。本文也是理解磁电耦合中极化分量随磁序变化的理论基础。
  - 其他项目（project-1 双光子、project-3 机械发光 NN、project-4 TTF 分子计算、project-6 湿度传感器、project-7 CDW）无直接项目连接；project-4 若涉及分子晶体极化可作弱方法学参考，但目前不打标签。

- **组织与用词**：论文走"问题—公式—物理图像—数值方案—实例验证—展望"的简洁 PRB 快报路线：先指出 ΔP 由绝热电流定义、给出 Kubo 型公式 (1)；借 Thouless 量子霍尔技巧消去导带得式 (4)；在周期性规范下得到核心 Berry 相公式 (8)；用 Wannier 函数赋予电荷中心位移的图像并证明量子化式 (13)；给出离散 k 串对数行列式的规范不变算法式 (15)；最后以 GaAs 的 Z* 与 γ₁₄ 作数值验证。值得在 wiki 叙述中复用的关键词：
  - "现代极化理论"（modern theory of polarization）
  - "贝里相位 / 贝里联络"（Berry phase / Berry connection）
  - "Wannier 函数电荷中心"（Wannier function center of charge）
  - "极化量子 / 极化的晶格值性质"（polarization quantum / lattice-valued P）
  - "玻恩有效电荷"（Born effective charge, Z*）
  - "压电张量"（piezoelectric tensor, γ₁₄）
  - "周期性规范"（periodic gauge）
  - "绝热电流 / Kubo 公式"（adiabatic current / Kubo formula）

- **可写入 wiki 的要点**：
  1. 核心公式：ΔP = P(1) − P(0)，P(λ) = (ife/8π³) Σ_n ∫_BZ dk ⟨u_{kn}^λ | ∂/∂k | u_{kn}^λ⟩（式 8b），即价带 Berry 联络在布里渊区的积分（Zak 相位）。
  2. 物理图像：ΔP = (fe/Ω) Σ_n R_n，极化变化等于所有占据态 Wannier 函数电荷中心位移之和（式 10）；这是把抽象几何相位转化为"电子云刚性位移"直观图像的关键等式。
  3. 量子化：当 V^KS(λ=1) = V^KS(λ=0) 时，ΔP = (fe/Ω) Σ_n R_n 必为 (fe/Ω)R 的整数倍（式 13），R 为格矢；这是一维 Zak 相位量子化的三维推广，与量子霍尔电导量子化同源。
  4. 适用前提：绝热路径上系统必须始终为绝缘体（有能隙），宏观电场 E=0，且势变化保持平移对称；金属或能隙闭合路径会使式 (2) 积分发散，理论失效。
  5. 规范不变数值算法（式 15）：沿 G∥ 方向取 k 点串 k_j = k⊥ + jG∥/J，计算 φ = Im ln Π_j det⟨u_{k_j}|u_{k_{j+1}}⟩，行列式与乘积结构使结果对每个 k 点本征矢的任意相位完全不敏感；这是所有现代 Berry 相极化代码（VASP LCALCPOL、QE、ABINIT）的算法原型。
  6. 极化是多值量：P 只在模 efR/Ω 意义下良定义；实际计算中若 |ΔP| ≪ |(fe/Ω)R₁|（R₁ 为最短非零格矢）可通过观察消去量子不确定性，否则应把 λ 路径细分为若干子区间。
  7. GaAs 验证：a = 5.576 Å（LDA/Wigner、20 Ry、(4,4,4) MP 网格）；Z*_Ga = 1.984（线性响应 1.994、实验 2.16，理论较实验小约 8%）；总 γ₁₄ = −0.28 C/m²（线性响应 −0.35、实验 −0.32）；γ₁₄ 是 clamped-ion 项 (a/e)γ'₁₄ = −1.352 与内应变项强相消后的小残差。
  8. 非局域赝势：式 (1) 中动量算符需修正，但晶胞周期哈密顿量有精确补偿，从式 (4) 起所有结论保持不变——这一条对实际用非局域/模守恒赝势做 Berry 相计算很重要。
  9. 方法优势：只需价带波函数、无需导带、无需超胞、无需线性响应（DFPT）的复杂二阶导数推导，可直接复用标准自洽总能量计算的基础设施，特别适合基于迭代对角化的现代电子结构代码。
  10. 历史地位与后续：本文与 Resta 1993–1994 的工作共同奠定"现代极化理论"，直接催生铁电体自发极化、压电/热释电张量、铁电翻转路径、拓扑绝缘体电极化等第一性原理计算方向；论文结尾把 P(λ) 视为"绝对极化"（模 eR/Ω）是否有用留作 future work，这一问题在随后 Vanderbilt、Resta 的系列论文中得到系统回答。
