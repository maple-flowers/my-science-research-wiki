---
citekey: kresseEfficientIterativeSchemes1996d
title: "Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set"
authors: [G. Kresse, J. Furthmüller]
year: 1996
journal: "Physical Review B"
doi: "10.1103/PhysRevB.54.11169"
url: "https://doi.org/10.1103/PhysRevB.54.11169"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/kresseEfficientIterativeSchemes1996d]]
projects: [project-2, project-4, project-5, project-7]
concepts: [density-functional-theory, rmm-diis, pulay-mixing, kerker-preconditioning, charge-sloshing, conjugate-gradient, subspace-rotation, methfessel-paxton-smearing, harris-foulkes-functional, self-consistent-field, ultrasoft-pseudopotential, plane-wave-basis]
entities: [VASP]
methods: [dft, plane-wave-basis, ultrasoft-pseudopotential, rmm-diis, pulay-mixing, kerker-preconditioning, conjugate-gradient, iterative-diagonalization, methfessel-paxton-smearing, charge-density-mixing]
materials: [diamond, fcc-Fe, fcc-Al]
figures: [mathematical-models-computational]
领域基础知识:: >-
  Kohn-Sham 密度泛函理论 (KS-DFT)、局域密度近似 (LDA)、广义梯度近似 (GGA)、平面波基组、赝势 (Pseudopotentials)、自洽场 (SCF) 方法、迭代对角化、电荷密度混合。
研究背景:: >-
  上世纪 90 年代，第一性原理计算在固体物理与化学中日益重要，但现有算法在处理大型金属系统时面临效率低下和稳定性差（如“电荷晃动”）的瓶颈。直接方法收敛慢，而传统自洽方法存在 O(N³) 的正交化瓶颈。
作者的问题意识:: >-
  如何开发出一套高效、稳定、且具有良好标度属性的迭代算法，以解决在平面波基组下计算金属系统 Kohn-Sham 基态时所面临的矩阵对角化 O(N³) 瓶颈与电荷密度混合收敛困难这两大核心问题。
主要研究对象:: >-
  用于求解 Kohn-Sham 方程的高效迭代算法，具体包括：1. 基于残差最小化的迭代矩阵对角化方案 (RMM-DIIS)；2. 基于 Pulay 混合和 Kerker 预条件的电荷密度混合方案。
主要研究方法:: >-
  理论公式推导与数值实验验证相结合。作者派生并阐述了 RMM-DIIS 和 Pulay 混合算法的理论基础，然后在金刚石、fcc-Fe、fcc-Al 等不同体系上，通过构建不同尺寸的超胞并对比多种算法（CG, CGa）的性能与标度行为，来验证其方案的有效性。
研究意义:: >-
  提出了具有里程碑意义的算法，从根本上解决了 VASP 软件包的核心效率与稳定性问题，使得对包含数百个原子的复杂体系进行高精度、可靠的第一性原理计算成为可能，极大地推动了计算材料科学与凝聚态物理的发展。
研究结论:: >-
  1. RMM-DIIS 算法通过最小化残差向量范数，避免了显式正交化，将计算复杂度降至 O(N²)。2. 结合 Pulay 混合与 Kerker 预条件器的自洽方案，能有效压制金属体系 of 电荷晃动，其收敛速率几乎与系统尺寸无关。3. 该自洽方案在效率、稳定性和标度上均优于当时流行的直接最小化方法。
对领域的贡献:: >-
  1. 提出了 RMM-DIIS 算法，是对迭代对角化技术的重要创新。2. 成功将 Pulay 的 DIIS 方法应用于电荷密度混合，并引入了 Kerker 预条件器与定制度量，解决了电荷晃动难题。3. 构建了 VASP 软件的核心算法框架，定义了现代平面波 DFT 计算的主流范式。
未来研究方向提及:: >-
  1. 探索基于本文自洽方法的 O(N) 线性标度算法。2. 为更复杂的体系（如表面、分子）开发更优的自适应预条件器和度量。3. 尝试将电荷密度预条件思想引入直接最小化方法中，以改进其性能。
未来研究方向思考:: >-
  1. 如何在本文的自洽框架下，实现对非共线磁性和自旋-轨道耦合等复杂体系的高效、稳定求解。2. 将机器学习方法引入，以学习并构建适应于特定体系的最优电荷密度混合预条件器，替代人工调参。3. 进一步发展适应于大规模并行计算（如 GPU 异构集群）的 RMM-DIIS 和电荷密度混合算法的通信和计算模型，以突破万核级并行效率瓶颈。4. 探索 RMM-DIIS 方法在超越 DFT 的更高阶理论（如 GW 近似、Bethe-Salpeter 方程）中的应用潜力。
tags:
  - paper
  - type/method
  - year/1996
  - project/project-2
  - project/project-4
  - project/project-5
  - project/project-7
  - relevance/project-2/strong
  - relevance/project-4/strong
  - relevance/project-5/strong
  - relevance/project-7/strong
  - concept/density-functional-theory
  - concept/rmm-diis
  - concept/pulay-mixing
  - concept/kerker-preconditioning
  - concept/charge-sloshing
  - concept/conjugate-gradient
  - concept/subspace-rotation
  - concept/methfessel-paxton-smearing
  - concept/harris-foulkes-functional
  - concept/self-consistent-field
  - concept/ultrasoft-pseudopotential
  - concept/plane-wave-basis
  - entity/VASP
  - method/dft
  - method/plane-wave-basis
  - method/ultrasoft-pseudopotential
  - method/rmm-diis
  - method/pulay-mixing
  - method/kerker-preconditioning
  - method/conjugate-gradient
  - method/iterative-diagonalization
  - method/methfessel-paxton-smearing
  - method/charge-density-mixing
  - material/diamond
  - material/fcc-Fe
  - material/fcc-Al
  - topic/computational-methods
  - topic/dft
  - topic/electronic-structure
---

## kresseEfficientIterativeSchemes1996d — 基于平面波基集的从头算总能量计算的高效迭代格式

## 📄 元数据
G. Kresse、J. Furthmüller，1996，Physical Review B 54(16), 11169–11186，DOI 10.1103/PhysRevB.54.11169。
## 💡 一句话
本文提出 RMM-DIIS 迭代对角化与基于 Kerker 预条件的 Pulay 电荷密度混合两大算法，将平面波赝势 DFT 的标度从 O(N³) 降至 O(N²)、使金属体系自洽迭代次数几乎不随系统尺寸增长，奠定了 VASP 的核心算法框架。
## 🔗 Wiki 双链
  - 概念 [[../concepts/density-functional-theory]]、[[../concepts/rmm-diis]]、[[../concepts/pulay-mixing]]、[[../concepts/kerker-preconditioning]]、[[../concepts/charge-sloshing]]、[[../concepts/subspace-rotation]]、[[../concepts/methfessel-paxton-smearing]]、[[../concepts/ultrasoft-pseudopotential]]、[[../concepts/plane-wave-basis]]
  - 实体 [[../entities/VASP]]
  - 图表 [[../figures/mathematical-models|数学模型与物理公式]]、[[../figures/crystal-structures|晶体结构与原子排布]]、[[../figures/electronic-bands|电子能带与电子态]]、[[../figures/electronic-devices|电子与突触器件]]、[[../figures/optical-spectra|光学与吸收光谱]]、[[../concepts/domain-wall]]
  - 年度 [[../write/1945-1999|1996]]
  - 项目 [[../projects/project-2-mn-multiferroics]]、[[../projects/project-4-ttf-molecular-calc]]、[[../projects/project-5-snte-ferroelectric-sim]]、[[../projects/project-7-cdw-charge-density-wave]]
  - 概念 [[../concepts/conjugate-gradient]]、[[../concepts/self-consistent-field-cycle]]、[[../concepts/harris-foulkes-functional]]
  - 相关论文 [[../../raw/note/kresseEfficientIterativeSchemes1996d]]
## 📊 关键图表
  - 图1：fcc-Fe（4 晶胞）自洽循环中不同方案下原子受力的收敛性，opt（式25 修正）较 out 快约 100 倍，证明 Pulay 型力修正对离子弛豫/MD 的关键作用。
  ![Fig.1 力的收敛性对比（fcc-Fe）](../../raw/figures/kresseEfficientIterativeSchemes1996d/fig_1_CDNY7B53.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：横轴为自洽迭代步数，纵轴为原子受力（单位 eV/Å），对比 fcc-Fe 4 晶胞在自洽循环中采用 out（未经修正的输出密度）、mix（混合密度）、opt（混合密度叠加式(25) Pulay 力修正）三种方案时力的收敛曲线。
  - **关键特征**：out 曲线数十步后仍剧烈振荡，误差约为 opt 的 100 倍；mix 曲线收敛性大幅改善但初期仍有波动；opt 曲线最平滑，约 10 步即达高精度，且随步数单调下降。
  - **结论/意义**：证明原子力对电荷密度的微小误差极其敏感，式(25) 修正计入了离子位移时输入密度自身的变化，是获得可靠结构弛豫与分子动力学力的关键。
  - 图2：RMM-DIIS 在不同尺寸立方金刚石超胞（1×–8×）中的非自洽总自由能收敛，各曲线几乎重合，证明对角化迭代次数与系统尺寸无关。
  ![Fig.2 RMM-DIIS 对金刚石的非自洽能量收敛](../../raw/figures/kresseEfficientIterativeSchemes1996d/fig_2_K2M97DMS.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：固定势场下仅迭代波函数，横轴为 RMM-DIIS 迭代步数，纵轴为总自由能（单位 eV），四条曲线分别对应 1（8 原子）、2、4、8 个立方金刚石晶胞。
  - **关键特征**：四条收敛曲线几乎完全重合；尽管随超胞增大最高占据态与最低空态之间隙缩小，RMM-DIIS 仍稳定收敛到正确本征态；初始波函数由随机初始化加 3 次 CG 子空间旋转生成。
  - **结论/意义**：直接证明 RMM-DIIS 对角化所需迭代次数与体系尺寸无关，是本文 O(N²) 标度论断的核心证据之一。
  - 图3：RMM-DIIS（实）与 CGa（虚）对不同尺寸 fcc-Fe 超胞的非自洽能量收敛，逐带 RMM-DIIS 比全自由度 CGa 振荡更小、步数更少。
  ![Fig.3 RMM-DIIS 与 CGa 对 fcc-Fe 的非自洽收敛](../../raw/figures/kresseEfficientIterativeSchemes1996d/fig_3_GBM9JB34.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：固定势场下对比 RMM-DIIS（实线）与直接最小化 KS 泛函的 CGa（虚线），横轴为迭代步数，纵轴为 fcc-Fe 超胞的总自由能（单位 eV），覆盖 1×–8× 不同超胞尺寸。
  - **关键特征**：两种方法均表现出与尺寸无关的收敛性；RMM-DIIS 能量下降更快、曲线更平滑，所需步数更少；CGa 振荡略大但也能在固定势场下收敛。
  - **结论/意义**：说明即使在非自洽阶段，分而治之的"逐带对角化"策略也比整体优化的直接法更高效，为后续自洽对比奠定基线。
  - 图4：自洽计算中 RMM-DIIS 与 CGa 对金刚石的总能量（上）和力（下）收敛，RMM-DIIS 约 10–12 步、力达三位小数精度，比 CGa 快 2–3 倍。
  ![Fig.4 金刚石自洽能量与力收敛](../../raw/figures/kresseEfficientIterativeSchemes1996d/fig_4_45NBH4FX.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：开启自洽循环后金刚石体系的收敛曲线，上图纵轴为总能量（单位 eV）、下图纵轴为原子力（单位 eV/Å），横轴均为自洽迭代步数，RMM-DIIS 为实线、CGa 为虚线。
  - **关键特征**：能量上 RMM-DIIS 约 12 步即达极高精度，CGa 需约 30 步；力上 RMM-DIIS 曲线平滑快速下降，10 步后小数点后三位以上正确，CGa 需至少加倍迭代步数才能达到同等精度。
  - **结论/意义**：这是"自洽循环 + 专门混合"策略完胜直接最小化的直接证据——自洽循环把耦合问题解耦，由 Pulay/Kerker 混合高效处理密度更新，而 CGa 在密度变化引起的复杂势能面上共轭梯度搜索效率骤降。
  - 图5：fcc-Fe 自洽能量（上）与力（下）收敛，Kerker+Pulay 混合使迭代次数从最小到最大晶胞仅增约一倍，而 CGa 对大晶胞几乎不收敛。
  ![Fig.5 fcc-Fe 自洽能量与力收敛](../../raw/figures/kresseEfficientIterativeSchemes1996d/fig_5_MDMEZAFI.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：过渡金属 fcc-Fe 的自洽收敛，上图为总能量、下图为原子力随迭代步数的变化，对比 RMM-DIIS（实线）与 CGa（虚线），并覆盖 1-cell 到 8-cell 不同超胞尺寸。
  - **关键特征**：RMM-DIIS 能量约 20 步内收敛，从最小到最大超胞迭代次数仅增加约一倍；CGa 收敛非常缓慢，且随体系尺寸增大显著恶化，大晶胞下几乎不收敛；Fe 的开壳层 d 电子使电荷晃动比金刚石更严重。
  - **结论/意义**：证明 RMM-DIIS 结合 Pulay 混合与 Kerker 预条件能有效压制金属体系的长波电荷振荡，而直接法因缺乏对密度更新的预条件在金属中失效。
  - 图6：近自由电子金属 fcc-Al 的自洽能量收敛，RMM-DIIS 仅需约 8 步且与尺寸无关，CGa 随尺寸增大性能急剧下降。
  ![Fig.6 fcc-Al 自洽能量收敛](../../raw/figures/kresseEfficientIterativeSchemes1996d/fig_6_D9VHA5DL.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：近自由电子金属 fcc-Al 的自洽总自由能（单位 eV）随迭代步数的收敛曲线，对比 RMM-DIIS 与 CGa，并覆盖从小到大多个超胞尺寸。
  - **关键特征**：RMM-DIIS 仅需约 8 步即收敛，且与体系尺寸无关；CGa 收敛性随尺寸增大而显著变差；Al 的介电屏蔽行为与 Kerker 模型高度吻合，使预条件混合近乎最优。
  - **结论/意义**：再次强调针对金属长波介电响应设计 Kerker 预条件的重要性，是 RMM-DIIS+Pulay 方案在简单金属上接近最优收敛的直接体现。
  - 表 I（C 体系）：IBM RS/6000 Model 590 上单步耗时（秒）：8 原子 RMM=1.0/CG=1.0/CGa=1.2；216 原子 RMM=410/CG=800，RMM 对大体系快约一倍。
  ![Table I 碳体系单步耗时](../../raw/figures/kresseEfficientIterativeSchemes1996d/tab_6000_PUVVJLFL.png)
  - **图示描述**：在 IBM RS/6000 Model 590 工作站上，RMM-DIIS、CG、CGa 三种方法对不同尺寸碳（金刚石）超胞的单次自洽迭代耗时（单位秒）。
  - **关键特征**：小体系（8 原子）三者耗时相近，分别约为 1.0、1.0、1.2 秒；最大 216 原子体系 RMM-DIIS 约 410 秒、CG 约 800 秒，RMM-DIIS 快近一倍；单步优势来自减少显式正交化与分块 Choleski Gram-Schmidt。
  - **结论/意义**：结合图 4–6 的迭代次数差异，表明衡量算法效率的黄金标准是"单步时间 × 迭代次数"的总耗时，RMM-DIIS 在两方面同时占优。
## 🔬 项目连接
  - **project-2 Mn 多铁（strong）**：项目中的 MnVO3、SrMnO3、LaCuO3 等钙钛矿多铁计算全部依赖 VASP 平面波 DFT。本文是 VASP 电子最小化与电荷混合的算法源头：理解 RMM-DIIS 为何对过渡金属（开壳层、d 带、近简并）稳定、为何必须包含空带、以及 Kerker 混合如何压制磁性金属体系 of 电荷晃动，直接指导 INCAR 中 ALGO、IMIX/AMIX/BMIX、SIGMA/ISMEAR 的选择与收敛排错。
  - **project-4 TTF 分子计算（strong）**：TTF 分子晶体的 DFT 总能/结构优化同样跑 en VASP 上。本文的力修正公式（式 25）使自洽早期即可获得高精度原子力，对分子晶体的离子弛豫、声子与弱相互作用结构优化尤为重要；Methfessel-Paxton 展宽与 k 点收敛讨论也适用于分子晶体（绝缘体/窄带隙）参数设置。
  - **project-5 SnTe 铁电模拟（strong）**：SnTe 铁电模拟涉及大超胞、Berry 相极化、应变与拓扑缺陷，全部用 VASP。本文证明自洽迭代次数对多达 200+ 原子、1000 电子体系几乎不随尺寸增长（O(N²) 单步标度），这正是大超胞铁电/缺陷计算可行的算法基础；Kerker 混合对金属化或窄带隙 SnTe 表面/缺陷体系的收敛至关重要。
  - **project-7 CDW（strong）**：CDW 体系通常是金属或窄带隙、需要大超胞与密集 k 点，电荷晃动问题突出。本文直接给出金属体系自洽收敛的机理（介电矩阵 1/q² 发散）与解决方案（Kerker 预条件 + 定制度量 + Pulay/Broyden 二次收敛），是 CDW 大超胞结构优化和声子/电声计算能够收敛的方法学保障；空带与展宽的讨论也适用于费米面附近的 CDW 计算。
  - **project-1 双光子**：以实验双光子荧光为主，不涉及平面波 DFT 电子步，无直接项目连接。
  - **project-3 机械发光 NN**：以神经网络/实验为主，无直接项目连接。
  - **project-6 湿度传感器**：以器件/实验为主，无直接项目连接。
## 🔗 项目双链
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]
- 项目 [[../projects/project-4-ttf-molecular-calc|项目四：lsl老师的ttf分子计算]]
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]
- 项目 [[../projects/project-7-cdw-charge-density-wave|项目七：CDW电荷密度波]]

## 📝 组织与用词
全文按"问题分解 → 两大引擎 → 数值验证"组织：第二节建立含部分占据的 KS 自由能泛函与自洽循环、并推导力修正；第三节推导 RMM-DIIS 对角化（对比顺序 CG、子空间旋转、计算量与迭代次数标度）；第四节推导 Pulay 混合与 Kerker 预条件/度量；第五节在绝缘体（金刚石）、开壳层过渡金属（fcc-Fe）、简单金属（fcc-Al）上系统测试非自洽与自洽收敛、单步耗时与尺寸标度；第六节结论。论证的核心手法是把一个病态耦合问题（KS 基态）拆成两个可分别预条件的子问题（对角化 + 电荷混合），再用收敛曲线和计时表证明"总耗时=单步时间×迭代次数"才是公平判据。值得在 wiki 中复用的术语：
  - RMM-DIIS（残差最小化-迭代子空间直接求逆，residual minimization method–direct inversion in the iterative subspace）
  - charge sloshing（电荷晃动）
  - Kerker preconditioner（Kerker 预条件器）
  - Pulay mixing / DIIS（Pulay 混合/直接迭代子空间求逆）
  - subspace rotation（子空间旋转，Rayleigh-Ritz）
  - partial occupancies / smearing（部分占据数/展宽，Methfessel-Paxton）
  - self-consistency cycle vs. direct minimization（自洽循环 vs. 直接最小化，CGa）
  - Harris-Foulkes functional（Harris-Foulkes 泛函，HF 鞍点而非极小）
## ✏️ 可写入 Wiki 的要点
  1. RMM-DIIS 不最小化 Rayleigh 商 ⟨φ|H|φ⟩/⟨φ|S|φ⟩，而最小化残差范数 ||(H−ε_app S)|φ⟩||；残差范数在每个本征态处都是正定的局部极小值，因此原则上无需显式正交化即可收敛到离初值最近的本征态，把 O(N³) 正交化降至最低。
  2. RMM-DIIS 每步沿预条件残差 K|R⟩ 做 Jacobi 试探步 |φ₁⟩=|φ₀⟩+λK|R₀⟩（λ 限 0.1–1，通常 0.3–1），再用 DIIS 在试探向量张成的子空间中最小化残差范数（式 35–39，等价于一个小维度广义本征问题）；试探步廉价故总以试探步收尾。
  3. 必须保留[[../concepts/subspace-rotation|子空间旋转]]（Rayleigh-Ritz，式 32–34）和 Gram-Schmidt 重新正交化：相邻本征值 ε 与 ε+δε 之间的残差范数势垒仅为 δε 量级，无旋转时 RMM-DIIS 会越过浅丘收敛到错误能带；旋转还使首步残差等于精确正交梯度、保证初始最速下降稳定。
  4. 金属必须包含费米能级以上空带（文中 fcc-Fe 用 1.5 Nions 个空带）：只算占据带时最高占据带与最低空带间隙随系统尺寸缩小，γ_min∝1/N，收敛随 √N 变慢；空带把"问题区域"上移到对总能/力不重要的未占据态，使所有占据带迭代次数与尺寸无关。
  5. Pulay 混合把输入密度写成历史值的线性组合 ρ_in^opt=Σa_i ρ_in^i，在 Σa_i=1（电子数守恒）下最小化残差范数；作者证明这等价于准牛顿法，其逆雅可比（即介电矩阵逆）满足 G_m|ΔR_i⟩=−|Δρ_i⟩（式 57–60），具有二次收敛性——这是对 Annett 认为 Broyden 类方法不改善标度的直接反驳。
  6. Kerker 预条件 G_q=A·q²/(q²+q₀²)（式 61）针对金属中介电矩阵 J≈1−χU、U(q)∝1/q² 的长波发散：小 q 时 G→0、几乎不混合以阻尼电荷晃动，大 q 时 G→A 退化为高效线性混合；默认 A=0.8、体材料 q₀≈1.0–1.5 Å⁻¹（fcc-Fe 最优 q₀≈4.0 Å⁻¹），磁性体系/表面可用 A=0.2。
  7. 定制度量 f_q=(q²+q₁²)/q²（式 64）给小波矢残差更高权重（最短波矢权重约为最长波矢的 20 倍），强制算法优先收敛长波（最危险的电荷晃动）分量；引入度量比调 G₁ 更重要，且二者独立改善收敛。
  8. 力的式(25)修正 ∫d³r {∂[V_H(r_atom)+V_xc(r_atom)]/∂R_N}[ρ_out−ρ_in] 用原子电荷叠加近似输入密度随离子位置的变化，把自洽早期力的精度提高近两个数量级（图1），使自洽循环可提前停止、大幅加速离子弛豫与 MD。
  9. 部分占据采用 Methfessel-Paxton 展宽：自由能 F=E−Σ_n σ S_N[(ε_n−μ)/σ]，高阶（N=1,2）熵项极小、F(σ)=E_{σ=0}+O(σ^{2N+1})，并用 E_{σ=0}≈[(N+1)F(σ)+E(σ)]/(N+2)（式15）解析外推到零温；熵项本身就是 F 与 E_{σ=0} 之差的误差估计（σ 可调到该误差<1 meV）。
  10. 标度结论：在最多 1000 电子（约 200 简单原子或 100 过渡金属原子）体系上单步计算近 O(N²)（Hamiltonian 作用 N_b N_plw ln N_plw、实空间非局域投影线性于 N），Gram-Schmidt 用 Choleski 分块实现（附录，式 A1–A3）比顺序正交化快 2–4 倍；k 点数随超胞线性减少时总标度可接近 O(N)；256 MB 工作站即可处理上述规模。
