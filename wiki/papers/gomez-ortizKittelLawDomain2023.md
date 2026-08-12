---
citekey: gomez-ortizKittelLawDomain2023
title: "Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices"
authors: [Fernando Gómez-Ortiz, Hugo Aramberri, Juan M. López, Pablo García-Fernández, Jorge Íñiguez, Javier Junquera]
year: 2023
journal: "Physical Review B"
doi: "10.1103/PhysRevB.107.174102"
url: "https://doi.org/10.1103/PhysRevB.107.174102"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/gomez-ortizKittelLawDomain2023]]
projects: [project-2, project-5]
concepts: [kittel-law, polar-vortices, vortex-antivortex-pair, depolarization-field, domain-walls, topological-defects, strain-engineering, multiferroicity, ferroelasticity, polarization-switching, second-principles, superlattice, anharmonic-effects, polarization-waves, topological-charge, kosterlitz-thouless, poincare-hopf-theorem]
entities: [PbTiO3, SrTiO3, BiFeO3, SCALE-UP, PHONOPY, domain-wall]
methods: [second-principles, dft, monte-carlo-annealing, langevin-md, force-constant-bands, phonon-spectra, born-effective-charges, effective-hamiltonian]
materials: [PbTiO3, SrTiO3, PbTiO3-SrTiO3-superlattice]
figures: [domain-walls, crystal-structures, mathematical-models]
领域基础知识:: >-
  铁电材料中存在自发极化区域"畴"，不同畴的边界为"畴壁"。畴的形成是为了降低退极化场和静电能量。经典的Kittel定律描述了铁磁畴中畴宽与材料厚度的平方根关系，并后来被推广至铁电材料。
研究背景:: >-
  Kittel定律已在简单铁电薄膜中得到验证，但在具有复杂畴壁结构的新型铁电/介电超晶格中是否成立尚不明确。PbTiO₃/SrTiO₃超晶格因其内部能形成独特的极化涡旋畴壁，成为检验该定律普适性和探索新畴结构形成机制的理想体系。
作者的问题意识:: >-
  核心问题是验证Kittel定律在(PbTiO₃)ₙ/(SrTiO₃)ₙ超晶格的极化涡旋相中是否依然有效。其次，探索当体系处于不符合Kittel定律的亚稳态时，其畴结构将如何通过微观动力学过程演化至基态。
主要研究对象:: >-
  (PbTiO₃)ₙ/(SrTiO₃)ₙ铁电/介电超晶格，其中层厚n取值为8至16个单胞，重点研究其内部由顺时针/逆时针涡旋序列构成的畴壁结构及畴的宽度。
主要研究方法:: >-
  采用第二性原理模拟，具体使用SCALE-UP软件包。通过蒙特卡洛模拟退火寻找系统能量最低的稳定构型，并利用朗之万分子动力学在有限温度下追踪畴结构的动态演化。同时，结合力常数谱分析（PHONOPY）预测最优畴周期。
研究意义:: >-
  本研究将经典Kittel定律的适用范围从简单的铁电畴成功拓展到具有复杂极化涡旋织构的超晶格体系，证实了该定律的普适性。同时，它首次揭示了一种全新的畴形成动力学路径，为理解和调控低维铁性材料中的纳米畴结构提供了关键的理论依据。
研究结论:: >-
  1. Kittel定律在(PbTiO₃)ₙ/(SrTiO₃)ₙ超晶格的极化涡旋相中成立，最优畴宽与PbTiO₃层厚的平方根成正比。2. 当体系处于畴密度偏低的亚稳态时，它可以通过在界面处成核涡旋-反涡旋对，并经历涡旋延伸、反涡旋合并以及最终的涡旋-反涡旋对复合与湮灭这一系列过程，来生成新畴，从而弛豫到符合Kittel定律的基态。
对领域的贡献:: >-
  理论贡献在于推广了经典物理定律，并揭示了在多畴竞争和复杂拓扑结构下的能量-结构关系。技术贡献在于展示了第二性原理模拟在连接微观相互作用与介观畴结构演化方面的强大能力。其发现的涡旋-反涡旋复合机制为畴工程提供了新的物理思想。
未来研究方向提及:: >-
  作者提及可探索不同PbTiO₃/SrTiO₃层厚比下的情形；系统研究温度和应变对畴结构稳定性及相变路径的影响；以及探究高畴密度亚稳态（畴宽度小于最优值）的弛豫机制。
未来研究方向思考:: >-
  可进一步研究缺陷（如氧空位）或掺杂对涡旋-反涡旋成核和移动的钉扎作用，以探索实现畴结构定点操控的可能性。此外，可尝试将这种二维涡旋畴壁的动力学研究扩展到三维体系，考虑涡旋线沿另一方向的弯切和缠绕等复杂行为。
tags:
  - paper
  - type/theory
  - year/2023
  - project/project-2
  - project/project-5
  - relevance/project-2/medium
  - relevance/project-5/strong
  - concept/kittel-law
  - concept/polar-vortices
  - concept/vortex-antivortex-pair
  - concept/depolarization-field
  - concept/domain-walls
  - concept/topological-defects
  - concept/strain-engineering
  - concept/multiferroicity
  - concept/ferroelasticity
  - concept/polarization-switching
  - concept/second-principles
  - concept/superlattice
  - concept/anharmonic-effects
  - concept/polarization-waves
  - concept/topological-charge
  - concept/kosterlitz-thouless
  - concept/poincare-hopf-theorem
  - entity/PbTiO3
  - entity/SrTiO3
  - entity/BiFeO3
  - entity/SCALE-UP
  - entity/PHONOPY
  - entity/domain-wall
  - method/second-principles
  - method/dft
  - method/monte-carlo-annealing
  - method/langevin-md
  - method/force-constant-bands
  - method/phonon-spectra
  - method/born-effective-charges
  - method/effective-hamiltonian
  - material/PbTiO3
  - material/SrTiO3
  - material/PbTiO3-SrTiO3-superlattice
  - topic/ferroelectricity
  - topic/domain-walls
  - topic/topological-defects
  - topic/multiferroics
  - topic/superlattices
  - topic/perovskites
---

## gomez-ortizKittelLawDomain2023 — PbTiO₃/SrTiO₃ 超晶格中的 Kittel 定律与畴形成机制

## 📄 元数据
Fernando Gómez-Ortiz, Hugo Aramberri, Juan M. López, Pablo García-Fernández, Jorge Íñiguez, Javier Junquera et al.，2023 年，Physical Review B 107, 174102，DOI [10.1103/PhysRevB.107.174102](https://doi.org/10.1103/PhysRevB.107.174102)
## 💡 一句话
用第二性原理模拟首次在具有反向旋转极化涡旋畴壁的 (PbTiO₃)ₙ/(SrTiO₃)ₙ 超晶格中验证 Kittel 定律 ω²∝d，并揭示亚稳态通过界面涡旋-反涡旋对成核、拉长、合并与湮灭（缺陷复合）动态形成新畴的微观机制。
## 🔗 Wiki 双链
  - 概念 [[../concepts/multiferroicity]]、[[../concepts/topological-defects]]、[[../concepts/strain-engineering]]、[[../concepts/ferroelasticity]]、[[../concepts/polarization-switching]]、[[../concepts/kittel-law|Kittel定律]]、[[../concepts/polar-vortex|极性涡旋]]、[[../concepts/vortex-antivortex-pair|涡旋-反涡旋对]]、[[../concepts/depolarization-field|退极化场]]、[[../concepts/second-principles|第二性原理]]、[[../concepts/superlattice|超晶格]]、[[../concepts/anharmonic-effects|非谐效应]]、[[../concepts/polarization-waves|极化波]]、[[../concepts/topological-charge|拓扑荷]]、[[../entities/PHONOPY|PHONOPY]]
  - 实体 [[../entities/BiFeO3]]、[[../entities/domain-wall]]、[[../entities/PbTiO3|PbTiO₃]]、[[../entities/SrTiO3|SrTiO₃]]
  - 图表 [[../figures/domain-walls]]、[[../figures/crystal-structures]]、[[../figures/mathematical-models]]
  - 年度 [[../write/2023]]
  - 相关论文 **gomez-ortizKittelLawDomain2023**
## 🆕 新概念/实体建议
  - 实体 `PbTiO3-SrTiO3-superlattice.md`：钙钛矿铁电/顺电端元构成的超晶格复合相。
  - 实体 `SCALE-UP.md`：第二性原理有效哈密顿量模拟所用的软件包。
## 📊 关键图表
  - 图1：双畴结构从 Ising 初态弛豫为顺时针/逆时针极化涡旋畴壁（畴壁厚约 1 u.c.，出现 y 向极化分量）
    ![图1 双畴结构弛豫为涡旋畴壁](../../raw/figures/gomez-ortizKittelLawDomain2023/fig_1_I73SSRGV.png) -> [[../figures/domain-walls|畴与畴壁结构]]
  - 图2：不同 n 下单胞能量随横向尺寸 L 的曲线及 ω²–n 线性拟合（Kittel 定律验证，红点能量最小化、蓝方块力常数法）
    ![图2 Kittel定律验证](../../raw/figures/gomez-ortizKittelLawDomain2023/fig_2_AAWRLAWB.png) -> [[../figures/domain-walls|畴与畴壁结构]]
  - 图3：Γ–X 力常数带与最强不稳定声子模 q_min≈0.123，冻结后得规则涡旋阵列
    ![图3 力常数谱分析](../../raw/figures/gomez-ortizKittelLawDomain2023/fig_3_KHD8X69N.png) -> [[../figures/mathematical-models|数学模型与物理公式]]
  - 图4：2 畴与 4 畴构型能量交叉，临界横向尺寸 Lc 随 n 增大
    ![图4 畴密度相竞争](../../raw/figures/gomez-ortizKittelLawDomain2023/fig_4_LEVTBY7M.png) -> [[../figures/domain-walls|畴与畴壁结构]]
  - 图5：n=12 时 L=24/36/48 u.c. 下极化地图，含亚稳态界面新生涡旋-反涡旋对及升温后 4 畴态
    ![图5 不同L下极化构型](../../raw/figures/gomez-ortizKittelLawDomain2023/fig_5_JV3KYDD2.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - 图6：n=14, L=28, T=90 K, −0.5% 压应变下，0–600 fs 内涡旋拉长→反涡旋合并为涡度−2→湮灭形成新畴的 MD 快照
    ![图6 涡旋-反涡旋复合动力学](../../raw/figures/gomez-ortizKittelLawDomain2023/fig_6_RKRLCYXC.png) -> [[../figures/heterostructures-stacking-mechanics-misc|力学性质、剥离能与杂项]]
## 🔬 项目连接
  - **project-2（Mn 多铁）— medium**：本文虽以 PbTiO₃/SrTiO₃ 为对象，但系统给出了铁电/多铁薄膜中畴壁能–静电能–梯度能竞争、Kittel 标度、非 Ising 拓扑畴壁（涡旋）的通用物理图像，并直接引用 BiFeO₃ 超薄膜中 Kittel 定律的前作（Ref. [12]）与极化波现象对照。对理解 Mn 基多铁中畴结构、畴壁能及应变调控有物理类比与文献脉络价值。
  - **project-5（SnTe 铁电模拟）— strong**：方法论高度可复用：(i) 第二性原理/DFT 参数化有效势 + 蒙特卡洛模拟退火（60 K→0.003 K，约 20000 次扫描）找全局最低畴构型；(ii) 朗之万分子动力学（T=90 K）追踪畴形成/翻转动力学；(iii) 力常数带（PHONOPY 直接超胞法，含非解析项）从软模波矢 q_min 反推最优畴周期 ω=1/(2q)−1；(iv) 外延应变约束（固定面内 a=b=3.901 Å）与压应变（−0.5%）对畴稳定性/相变势垒的影响；(v) 用 Born 有效电荷张量×位移/体积线性近似求局域极化。这些流程可直接迁移到 SnTe 铁电薄膜/超晶格的畴结构、厚度标度与应变工程计算。
  - project-1（双光子）、project-3（机械发光 NN）、project-4（TTF 分子计算）、project-6（湿度传感器）、project-7（CDW）：无直接项目连接。（project-7 的周期性调制与拓扑缺陷有形式类比，但材料/物理差距较大，不单列。）
## 🔗 项目双链
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]

## 📝 组织与用词
文章采用"提出问题→验证经典定律→揭示新机制→结论"的标准 PRB 结构。方法论部分先交代 SCALE-UP 第二性原理势的拟合来源（DFT+LDA，−11.2 GPa 静水压修正立方晶格常数低估）、外延约束与超胞尺寸（退火用 L×1×2n，MD 用 L×10×2n），再把结果分为 A. Kittel 定律验证（能量最小化与力常数谱两条独立证据，系统差异归因非谐效应）和 B. 畴形成（2 畴/4 畴能量竞争定 Lc，再用 MD 拍涡旋-反涡旋复合全过程）。值得复用的关键词：
  - Kittel law / Landau-Kittel law — Kittel 定律（朗道-基特尔定律），ω²/δ=Ad
  - polar vortex (clockwise/counterclockwise) — 极性涡旋（顺时针/逆时针）
  - vortex-antivortex recombination — 涡旋-反涡旋复合
  - depolarization field [[../concepts/depolarization-field|depolarization field]] / electrostatic energy — 退极化场 / 静电能
  - domain wall energy vs gradient energy — 畴壁能与梯度能
  - force-constant band / soft mode — 力常数带 / 软模 [[../concepts/soft-mode|软模]]
  - anharmonic effect / offset (vortex core shift) — 非谐效应 / 涡旋中心偏移
  - polarization wave — 极化波
  - second-principles simulation (SCALE-UP) — 第二性原理模拟
  - Poincaré-Hopf theorem / vorticity — 庞加莱-霍普夫定理 / 涡度
## ✏️ 可写入 Wiki 的要点
  1. [[../concepts/kittels-law|Kittel 定律]]在 (PbTiO₃)ₙ/(SrTiO₃)ₙ（n=8–16 u.c.）的[[../concepts/polar-vortex|极性涡旋]]相中成立：[[../concepts/domain-wall-energy|畴壁能]]与静电能平衡给出最优畴周期 ω，其平方与 PbTiO₃ 层厚 d 线性相关，ω²/δ=Ad（δ≈1 u.c. 为畴壁厚度）。
  2. 该体系基态不是 180° Ising 条带畴，而是由垂直于堆叠方向、顺时针/逆时针反向旋转的涡旋序列充当畴壁，涡旋核处出现沿 y 方向的轴向极化分量。
  3. 两种独立方法验证 Kittel 定律：(i) 全能量最小化（蒙特卡洛退火，ω=L/2−1）；(ii) 简谐力常数带分析（PHONOPY，q_min≈0.123，ω=1/(2q)−1）。谐波法系统性预测更窄的畴，因为它无法捕捉非谐弛豫（涡旋中心偏移+面内极化倾斜），而该倾斜减少垂直表面极化分量与退极化电荷，允许畴更宽。
  4. 对固定 n，2 畴与 4 畴构型存在临界横向尺寸 Lc：L<Lc 时 2 畴稳定（畴壁能惩罚主导），L>Lc 时 4 畴稳定（静电能惩罚主导）；Lc 随 n 增大。
  5. 低畴密度[[../concepts/metastability|亚稳态]]（畴宽过大，L>Lc）在 T<50 K 长寿命存在；升温至 ≥90 K 或施加 ≥−0.5% 压应变可越过势垒，自发形成新畴。高畴密度亚稳态（L<Lc，[[../concepts/polarization-waves|极化波]]态）即使升温也无法弛豫到低密度态——这种不对称性源于静电能与梯度能势垒形态不同。
  6. 畴形成的微观动力学四步：界面处[[../concepts/vortex-antivortex-pair|涡旋-[[../concepts/antivortex|反涡旋]]对]]成核→涡旋沿界面拉长并将反涡旋推向 PbTiO₃ 层中心→两个反涡旋合并为涡度−2 的高能双反涡旋（能量随涡度平方增加，符合 Kosterlitz-Thouless XY 模型）→约 50 fs 内与两个涡旋湮灭，形成向下极化新畴与新的拉长顺/逆时针涡旋对，最终展宽至 Kittel 最优尺寸。整个过程发生在数百飞秒内（n=14, L=28, T=90 K, −0.5% 应变）。
  7. 总涡度守恒：周期性边界条件下由庞加莱-霍普夫定理要求净涡度为零，故涡旋（+1）必与反涡旋（−1）成对出现/湮灭；反涡旋主要出现在极化幅度较小的 SrTiO₃ 层中（头对头/尾对尾静电能代价低），与第一性原理结果一致。
  8. 层厚 n 增大有两个效应：PbTiO₃ 层极化趋近体相值、SrTiO₃ 层极化减小（从静电"耦合"态过渡到"解耦"态），两者共同使单胞能量降低；同时能量曲线的极小值变浅且向更大 L 移动。
  9. 计算细节可复用：[[../concepts/second-principles|第二性原理]]模拟势由 DFT(LDA) 拟合，施 −11.2 GPa 静水压修正立方晶格常数低估；外延约束 a=b=3.901 Å 模拟 SrTiO₃ 衬底；局域极化用 [[../concepts/born-effective-charge|Born 有效电荷]]张量×原子位移/单元胞体积的线性近似；力常数带含 Gonze-Lee 非解析项以分裂纵/横极性带。
  10. 历史脉络：Landau-Lifshitz(1935)→Kittel(1946,1949) 铁磁畴→Mitsui-Furuichi(1953) 罗谢尔盐推广到铁电→Stephanovich 等铁电/顺电[[../concepts/superlattice|超晶格]]→Roitburd 外延铁弹薄膜→Lai/Bellaiche 等 PZT 与 Prosandeev/Bellaiche 等 BiFeO₃ 超薄膜第一性原理验证（薄至 3 u.c.）→本文推广到极性涡旋相，并补上动力学机制。
