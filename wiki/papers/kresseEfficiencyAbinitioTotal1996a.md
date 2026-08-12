---
citekey: kresseEfficiencyAbinitioTotal1996a
title: "Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set"
title_zh: "用平面波基组计算金属和半导体从头算总能量的效率"
authors: [G. Kresse, J. Furthmüller]
year: 1996
journal: "Computational Materials Science"
doi: "10.1016/0927-0256(96"
url: "https://doi.org/10.1016/0927-0256(96"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/kresseEfficiencyAbinitioTotal1996a]]
projects: [project-2, project-4, project-5]
concepts: [density-functional-theory]
entities: [VASP]
methods: [dft]
materials: []
figures: [mathematical-models]
领域基础知识:: >-
  本领域为计算材料科学中的第一性原理总能计算，基于密度泛函理论（DFT）的Kohn-Sham方程，采用平面波基组与赝势（pseudopotential）或超软赝势（ultrasoft pseudopotential, US-PP）来展开电子波函数，通过自洽求解电子基态能量与电荷密度。
研究背景:: >-
  20世纪90年代，Car-Parrinello（CP）联合动力学方法推动了第一性原理分子动力学，但其时间步长受限于电子自由度，且对金属体系因电子占据数在费米面处的突变，导致k点积分收敛极慢，计算效率低下。
作者的问题意识:: >-
  如何构建一套高效、稳健且通用的算法框架，以显著提升平面波赝势方法在金属和半导体体系中的电子基态计算效率，并克服CP方法对金属处理困难和绝热限制的固有缺陷。
主要研究对象:: >-
  基态电子结构计算的核心算法，包括：处理金属部分占据的Methfessel-Paxton展宽法与线性四面体法；迭代矩阵对角化技术（Davidson、共轭梯度、残差最小化RMM-DIIS）；电荷密度自洽混合技术（Pulay混合、Broyden混合及其预条件处理）；以及直接最小化Kohn-Sham泛函的优化方法。
主要研究方法:: >-
  通过理论推导阐述各种算法的数学原理，并将其实现于一个统一的程序包VAMP中。然后，选取液态锗（金属）、钯(111)表面（强电荷震荡金属）和金刚石(100)表面（半导体）三个典型体系，对上述不同算法组合进行非自洽和自洽的基准测试，从能量收敛速度、力的收敛精度、单步耗时等维度进行定量比较。
研究意义:: >-
  通过系统整合与创新，构建了后来VASP软件的核心算法框架，使得对包含过渡金属、液态金属等复杂体系的高效、精确第一性原理模拟成为可能，极大地推动了计算材料科学的发展。
研究结论:: >-
  1. 基于自洽场循环（SC）的方法在效率上普遍优于直接最小化KS泛函的方法。2. 在SC方法中，RMM-DIIS迭代对角化算法因避免了显式正交化，对大于30个原子的体系具有最优的计算标度。3. Methfessel-Paxton展宽法是处理金属部分占据问题的最优方案，其能量和力自洽一致，且无需精细调节参数。4. 结合了预条件矩阵和优化度量的Pulay混合方法，能有效抑制电荷密度震荡，是自洽混合的最稳定选择。
对领域的贡献:: >-
  奠定了现代第一性原理计算软件VASP的方法学基础，将RMM-DIIS对角化、MP展宽、Pulay混合等最先进算法创造性地整合为一个高效、稳健的通用框架，并论证了其对金属、半导体、表面等复杂体系的普适性，开启了大规模、高精度第一性原理分子动力学模拟的新阶段。
未来研究方向提及:: >-
  文中提及的未来方向包括：进一步优化直接能量最小化方法的在线搜索精度；将算法推广至PAW（投影缀加平面波）和LAPW（线性缀加平面波）等全势方法；利用RMM-DIIS的天然并行性支持更大规模计算；以及将高效算法与精确力计算结合，用于声子谱等晶格动力学性质的计算。
未来研究方向思考:: >-
  可进一步研究自适应、无参数的预条件函数，以应对强关联或低维材料；探索RMM-DIIS方法在能带反交叉等复杂情况下的全局收敛性问题；结合机器学习技术，开发更智能的电荷密度混合策略，以预测历史信息并加速收敛；在异构计算（GPU）架构下，重新评估内存占用与计算效率之间的权衡，优化算法设计。
tags:
  - paper
  - type/theory
  - year/1996
  - project/project-2
  - relevance/project-2/strong
  - project/project-4
  - relevance/project-4/medium
  - project/project-5
  - relevance/project-5/medium
  - concept/density-functional-theory
  - entity/VASP
  - method/dft
  - topic/ferroelectricity
  - topic/molecular-crystal
  - topic/multiferroics
---

## kresseEfficiencyAbinitioTotal1996a — 用平面波基组计算金属和半导体从头算总能量的效率

## 📄 元数据
G. Kresse, J. Furthmüller et al.，1996，Computational Materials Science 6, 15-50，DOI 10.1016/0927-0256(96)00008-0
## 💡 一句话
系统提出并基准验证了以 RMM-DIIS 迭代对角化 + Pulay/Kerker 电荷密度混合 + Methfessel-Paxton 展宽为核心的自洽循环算法框架，奠定了 VASP（前身 VAMP）高效率求解金属与半导体 Kohn-Sham 基态的方法学基石。
## 🔗 Wiki 双链
本文涉及且 wiki 中已存在的条目，用双链列出（存在才链）：
  - 概念 [[../concepts/density-functional-theory]]
  - 实体 [[../entities/VASP]]
  - 图表 [[../figures/mathematical-models]]
  - 年度 [[../write/1996]]
  - 主题 [[材料模拟计算设计]]
  - 相关论文 [[../../raw/note/kresseEfficiencyAbinitioTotal1996a]]
## 🆕 新概念/实体建议
wiki 中没有、但值得新建的概念或材料实体，每个给 kebab-case 建议文件名 + 一句说明
  - `self-consistent-field-cycle`：自洽场（SC）循环，迭代求解 KS 方程并混合电荷密度直至输入/输出密度一致的标准电子基态求解框架，本文论证其优于直接最小化 KS 泛函。
  - `rmm-diis`：残差最小化-迭代子空间直接反演（Residual Minimization Method - Direct Inversion in the Iterative Subspace），本文核心算法创新，通过最小化残差向量范数而非 Rayleigh 商避免显式正交化，使大体系对角化趋近 N² 标度并天然并行。
  - `methfessel-paxton-smearing`：Methfessel-Paxton 展宽法，用 Hermite 多项式展开阶跃占据函数，N≥1 时自由能与零温能量偏差为 O(σ^(N+2))，熵项可直接作为误差估计，并保证能量与力的自洽一致，是金属体系的优选展宽方案。
  - `charge-density-mixing`：电荷密度混合（Pulay/Broyden/Kerker），自洽循环中根据历史残差生成下一输入密度的拟牛顿类加速技术，Kerker 预条件矩阵 G₁=A·q²/(q²+q₀²) 专门抑制低波数电荷震荡（charge sloshing）。
  - `iterative-diagonalization`：Kohn-Sham 哈密顿量迭代对角化（Davidson / 共轭梯度 / RMM-DIIS 三大家族），对比其收敛步数、单步耗时与 N³ 正交化开销。
  - `ultrasoft-pseudopotential`：超软 Vanderbilt 赝势，将过渡金属和第一周期元素所需截断能降低 2-4 倍，引入增广电荷 Qij 与重叠算符 S，需广义本征值方程 H|φ⟩=εS|φ⟩。
  - `plane-wave-basis`：平面波基组，利用 FFT 在实/倒空间快速施加哈密顿量（局域势实空间对角、动能倒空间对角、非局域投影可分离），是迭代算法效率的基础。
## 📊 关键图表
笔记未附图片。
## 🔬 项目连接
  - project-5 SnTe 铁电模拟：SnTe 等拓扑/铁电材料的第一性原理计算通常以 VASP 为引擎，本文所述 RMM-DIIS、MP 展宽、Pulay 混合是日常 SCF 收敛与高精度力计算的算法基础，可作为"计算方法"章节引用。
  - project-2 Mn 多铁：过渡金属 Mn 体系费米面附近 d 带结构复杂，本文 Table 1 给出过渡金属（V、Rh）推荐 σ≈0.3 eV 的 MP 展宽参数，对磁性/多铁金属或窄隙体系的 k 点收敛与声子计算具有直接参考价值。
  - project-4 TTF 分子计算：若使用平面波 DFT 软件做分子晶体/分子体系，本文的 US-PP、RMM-DIIS 与力修正方案可指导高精度结构弛豫。
## 🔗 项目双链
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]
- 项目 [[../projects/project-4-ttf-molecular-calc|项目四：lsl老师的ttf分子计算]]
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]

## 📝 组织与用词
文章采用"问题—理论模块—算法对决—结论"的层进式结构。第 1 节指出 CP 方法电子-离子同步更新导致时间步长受电子自由度限制的瓶颈，明确比较直接最小化 (i) 与自洽循环 (ii) 两条路线；第 2 节建立部分占据下的 KS 自由能泛函 F=E−σS，系统比较线性四面体法 LT/LT-C、高斯/Fermi-Dirac 展宽、Methfessel-Paxton 法；第 3 节以残差向量 |R⟩=(H−εS)|φ⟩ 与 Teter 预条件函数为统一语言，对比块 Davidson (DAV2)、序贯共轭梯度 (CG) 与 RMM-DIIS 三种对角化策略；第 4 节用 Johnson 改进 Broyden 框架统一 Pulay 混合与 Broyden 第二方法，引入 Kerker 预条件与优化度量 f_q=(q₁²+q²)/q²；第 5 节给出直接最小化的梯度（含子空间变化项与幺正旋转项）；第 6 节在液态 Ge（64 原子）、Pd(111)+H 表面、金刚石 C(100) 表面三个基准上做非自洽/自洽收敛与单步耗时对比；第 7 节给出结论。论证最有力之处在于把数学推导、操作数计数（T_H≈N²ln N、T_GS≈N³、T_ort≈2N³）与实际计时（Table 3，IBM RS/6000 Model 590）三者对应起来。值得在 wiki 叙述中复用的关键词/术语：
  - Self-consistency cycle (SC) / 自洽循环
  - RMM-DIIS (residual minimization – direct inversion in iterative subspace) / 残差最小化-迭代子空间直接反演
  - Methfessel-Paxton smearing / MP 展宽
  - Partial occupancies / 部分占据数
  - Charge density mixing & Kerker preconditioning / 电荷密度混合与 Kerker 预条件
  - Pulay mixing / Pulay 混合（DIIS）
  - Preconditioned residual vector / 预条件残差向量
  - Ultrasoft pseudopotential (US-PP) / 超软赝势
## ✏️ 可写入 Wiki 的要点
5-10 条 bullet，是可直接用于第二步充实 wiki 条目的具体事实、机制、数据、公式、结论
  - **SC 方法 vs 直接最小化**：在液态 Ge、Pd(111)、C(100) 三类基准上，基于"迭代对角化 + 电荷混合"的自洽循环比直接最小化 KS 泛函的共轭梯度法（CGa/SDa）快约 3-5 倍，且对金属体系鲁棒性更强；根本原因是混合方案可保留全部历史步信息，而直接 CG 受限于线最小化精度。
  - **RMM-DIIS 核心机制**：最小化目标为残差范数 ⟨R|R⟩ 而非 Rayleigh 商 ⟨φ|H|φ⟩/⟨φ|S|φ⟩；因残差范数在每个本征态处都是无约束最小值 0，故无需将搜索方向显式正交化到其它能带，避免了 T_ort≈2 N_b² N_PW≈2N³ 的操作与内存带宽瓶颈，使算法接近 N²ln N 标度；同时各能带优化彼此解耦，天然适合并行。
  - **RMM-DIIS 实现细节**：每步沿 K|R⟩ 方向以步长 λ（取首步 Rayleigh 商线最小化结果，限制在 0.1–1）做试探，再在 {|φ_i⟩, |R_i⟩} 子空间中通过求解厄米本征问题 Σⱼ⟨R_i|R_j⟩α_j=λα_i 做 DIIS 组合；初始化采用随机波函数 + 三次扫描（每次含一次[[../concepts/subspace-rotation|子空间旋转]]与两次最陡下降），随后再切换到 RMM，以避免"能带遗漏"。
  - **Methfessel-Paxton 展宽**：以 Hermite 多项式展开阶跃函数，f_N=f_0+Σ A_m H_{2m-1}e^{-x²}，熵项 S_N=Σ A_m H_{2m-1}e^{-x²}，N=0 即高斯展宽；N≥1 时 F(σ)=E_{σ=0}+O(σ^{N+2})，σ 可取到使熵项 <1 meV/atom（Table 1：Al 1.0、Li 0.4、Te 0.8、Cu 0.4、V 0.3、Rh 0.3 eV），且力（自由能导数）与零温能量一致，无需外推。
  - **LT/LT-C 与展宽法的力对比（Table 2）**：Rh K 点声子频率在 9×9×3 [[../concepts/monkhorst-pack-grid|Monkhorst-Pack 网格]]下，MP（N=2, σ=0.4 eV）能量法与力法给出 4.29/4.28 THz（横波）与 7.95/7.96 THz（纵波），高度一致；LT-C 若天真地固定占据数算力则偏差约 5%（横波 4.30→4.10 THz），LT 因 k 点不足误差可达 10%——证明 MP 法是力/声子计算的最可靠选择。
  - **Kerker 预条件混合**：初始混合矩阵取 G₁=A·q²/(q²+q₀²)（A=0.8，q₀=1.5 Å⁻¹ 为通用默认值，磁性体系或表面可用 A=0.1），在小 q 处近似 A·q²/q₀² 以抑制长程电荷 sloshing，大 q 处退化为线性混合；在残差内积中再引入度量 f_q=(q₁²+q²)/q²（最短波向量加权为最长波向量的 20 倍），Pulay 混合稳定性显著优于 Broyden 第二方法，但离子弛豫等少自由度情形 Broyden 更稳。
  - **Teter 预条件函数**：采用 K(q)=(27+18x+12x²+8x³)/(27+18x+12x²+8x³+16x⁴)·x·2/εkin(R)，其中 x=(ħ²q²/2m_e)/εkin(R)（本文改用 ½εkin(R) 改善收敛），高 q 处趋于 -2m_e/(ħ²q²)（动能预条件的精确逆），低 q 处有限，避免了 q_cut 经验参数。
  - **操作数标度**：单次哈密顿量作用 T_H≈N_b N_PW ln N_PW≈N²ln N（FFT 与实空间非局域投影主导）；Gram-Schmidt 正交化 T_GS≈N_b²N_PW≈N³；显式能带间正交化 T_ort≈2N_b²N_PW≈2N³ 且破坏缓存局部性，在标量机上比 T_GS 慢 3–10 倍。这是 RMM-DIIS 在 >20–30 原子体系胜出的定量依据。
  - **力的快速收敛修正**：在自洽循环中用 F_N=-∫(V_H[ρ_mix]+V_XC[ρ_mix])∂ρ_in/∂R_N（混合密度局域项）加上修正 dF/dR_N≈∫(V_H[ρ_in]+V_XC[ρ_in])(ρ_out−ρ_in)，可把力的精度提高近两个数量级（Fig. 4，Pd(111)+H 表面），从而允许更早终止 SCF；未修正的输出密度力可差 100 倍。
  - **软件与适用范围**：算法实现于 VAMP（Vienna ab-initio molecular-dynamics package，即 VASP 前身），支持超软赝势与可分离因式化非局域势，已成功用于液态/非晶半导体（Ge）、液态简单金属与过渡金属（Na、V、Cu）、金属-非金属转变（l-Hg）、清洁/氢化 C(100) 与 Al(111) 表面吸附、Rh 表面与体声子（金刚石、石墨）等；作者指出算法可直接推广至 PAW 与 LAPW 等全势基组，并因 RMM-DIIS 的局域性适合大规模并行。
