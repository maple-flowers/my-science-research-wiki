---
citekey: Johannes2008fermi
title: "Fermi surface nesting and the origin of charge density waves in metals"
title_zh: "费米表面嵌套与金属中电荷密度波的起源"
authors: [M. D. Johannes, I. I. Mazin]
year: 2008
journal: "Physical Review B"
doi: "10.1103/PhysRevB.77.165135"
url: "https://doi.org/10.1103/PhysRevB.77.165135"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/Johannes2008fermi]]
projects: [project-5, project-7]
concepts: [2D-materials, charge-density-wave, density-functional-theory, spin-orbit-coupling, fermi-surface-nesting, hidden-nesting, electron-phonon-coupling, electronic-susceptibility, incommensurate-lattice-transition, peierls-instability]
entities: [TMDs, VASP, WIEN2k, TaSe2, NbSe2]
methods: [arpes, dft, tight-binding]
materials: [TMDs]
figures: [crystal-structures-bulk, electronic-bands-band-structures, electronic-bands-cdw-transport, electronic-bands-dos-fermi]
领域基础知识:: >-
  电荷密度波 (CDW) 是低维金属中电荷密度和晶格结构的周期性调制现象。传统理论认为其源于费米面嵌套 (Fermi Surface Nesting) 导致的纯电子不稳定性，即派尔斯相变 (Peierls Transition)。费米面嵌套是指费米面的不同部分可以通过平移一个特定波矢（即CDW波矢）而重合。
研究背景:: >-
  长期以来，固体物理领域普遍认为费米面嵌套是CDW现象的主要或唯一驱动力。然而，许多实验和计算研究发现，这种纯粹基于电子图像的解释在真实材料中常常失效，表现为费米面嵌套峰与CDW波矢不匹配，或纯粹的电子不稳定性无法稳定存在。
作者的问题意识:: >-
  作者旨在澄清“费米面嵌套导致CDW”这一普遍误解，并系统性地论证在真实材料中，费米面嵌套并非CDW的驱动力。他们试图证明，真正的CDW与由电子-声子耦合驱动的非公度晶格转变 (ILT) 在物理上没有本质区别。
主要研究对象:: >-
  研究的核心是“派尔斯CDW”机制本身，并选取了三种典型的、被认为是嵌套驱动的CDW原型材料作为具体案例：二硒化铌 (NbSe₂)、二硒化钽 (TaSe₂) 和三碲化铈 (CeTe₃)，以及一个理想化的一维钠 (Na) 原子链模型。
主要研究方法:: >-
  1. 理论模型分析：通过数学推导，分析理想和非理想条件下派尔斯一维模型中的实部磁化率 χ′(q) 的行为，论证其脆弱性。2. 第一性原理计算：运用基于密度泛函理论 (DFT) 的WIEN2k和VASP软件包，计算上述真实材料的电子结构、费米面、虚部磁化率 χ′′(q) 和实部磁化率 χ′(q)，并进行对比分析。
研究意义:: >-
  本文颠覆了领域内长期存在的“费米面嵌套驱动CDW”的传统范式，明确指出动量依赖的电子-声子耦合才是核心机制。它为理解和预测CDW材料提供了全新的视角与方法论，避免研究者继续依赖无效的费米面目视检查法，转而关注电子-声子相互作用的计算。
研究结论:: >-
  1. 派尔斯机制中的纯电子不稳定性极其脆弱，易被温度、散射和微小几何偏差破坏。2. 在NbSe₂、TaSe₂和CeTe₃等典型材料中，费米面嵌套的峰值与实际的CDW波矢不一致，不具有预测能力。3. CDW的本质是电子-声子耦合驱动的结构相变，电子和离子子系统协同作用，不可分割。4. 因此，在物理上无法对“CDW”与“非公度晶格转变 (ILT)”做出有意义的区分。
对领域的贡献:: >-
  1. 澄清了“费米面嵌套”和“派尔斯CDW”等核心概念的模糊性，并设定了严格的适用条件。2. 通过理论和计算，有力地解构了旧范式，确立了电子-声子耦合在CDW形成中的核心地位。3. 提供了方法论上的警示，即仅凭费米面拓扑或χ′′(q) 判断CDW是错误的，必须分析χ′(q) 和整个能带的贡献。
未来研究方向提及:: >-
  1. 发展精确计算动量依赖的电子-声子耦合强度的方法。2. 深入探索CeTe₃中发现的“隐藏嵌套”机制，即费米速度匹配在更广泛材料体系中的作用。3. 理解Na原子链中“之”字形畸变的具体物理起源。4. 重新审视其他被归类为“嵌套驱动”的CDW材料。
未来研究方向思考:: >-
  1. 开发一个能够同时量化费米面拓扑与带间跃迁贡献的综合性谱函数或描述符，以统一评估电子结构对CDW的不稳定性。2. 探索利用超快光谱或非弹性X射线散射等实验技术，直接测量实部磁化率χ′(q)或动量分辨的电子-声子耦合。3. 在电荷密度波体系中，深入研究电子-声子耦合与超导电性等其他量子序的竞争与共存关系。
tags:
  - paper
  - type/experiment
  - year/2008
  - project/project-5
  - relevance/project-5/medium
  - project/project-7
  - relevance/project-7/core
  - concept/2D-materials
  - concept/charge-density-wave
  - concept/density-functional-theory
  - concept/spin-orbit-coupling
  - entity/TMDs
  - entity/VASP
  - method/arpes
  - method/dft
  - method/tight-binding
  - material/TMDs
  - topic/2d-materials
  - topic/charge-density-wave
  - topic/ferroelectricity
  - topic/phase-transition
  - topic/polarization
---

## Johannes2008fermi — 费米面嵌套与金属中电荷密度波的起源
## 📄 元数据
M. D. Johannes, I. I. Mazin，2008，Physical Review B 77, 165135，DOI [10.1103/PhysRevB.77.165135](https://doi.org/10.1103/PhysRevB.77.165135)
## 💡 一句话
通过理论推导与 NbSe₂、TaSe₂、CeTe₃ 及 Na 原子链的第一性原理计算，系统证明费米面嵌套（FS nesting）不是真实材料中 CDW 的驱动力，CDW 本质上是由动量依赖的电子-声子耦合驱动的结构相变。
## 🔗 Wiki 双链
  - 概念 [[../concepts/charge-density-wave]]
  - 概念 [[../concepts/density-functional-theory]]
  - 概念 [[../concepts/spin-orbit-coupling]]
  - 概念 [[../concepts/2d-materials]]
  - 概念 [[../concepts/fermi-surface-nesting|费米面嵌套]]
  - 概念 [[../concepts/peierls-instability|派尔斯不稳定性]]
  - 概念 [[../concepts/electron-phonon-coupling|电子-声子耦合]]
  - 概念 [[../concepts/electronic-susceptibility|电子极化率]]
  - 概念 [[../concepts/hidden-nesting|隐藏嵌套]]
  - 概念 [[../concepts/incommensurate-lattice-transition|非公度晶格转变]]
  - 概念 [[../entities/TaSe2|TaSe₂]]
  - 实体 [[../entities/TMDs]]
  - 实体 [[../entities/VASP]]
  - 实体 [[../entities/WIEN2k]]
  - 实体 [[../entities/NbSe2|NbSe₂]]
  - 实体 [[../entities/TaSe2|TaSe₂]]
  - 图表 [[../figures/electronic-bands]]
  - 图表 [[../figures/crystal-structures]]
  - 年度 [[../write/2005-2009|2008]]
  - 项目 [[../projects/project-7-cdw-charge-density-wave]]
  - 主题 [[../topics/材料模拟计算设计]]
  - 相关论文 [[../../raw/note/Johannes2008fermi]]
  - 实体 [[../entities/CeTe3]]

## 🆕 新概念/实体建议
  - 实体 `CeTe3.md` — 三碲化铈，RTe₃ 家族准一维 Te-p 费米面，是“隐藏嵌套”的范例；计算用 LDA+U（U=4.5 eV）去除 f 带。
## 📊 关键图表
  - ![图1 理想 1D Peierls 模型中 χ′(q) 在 q=2k_F 的对数发散被温度、散射 γ、几何偏差 δk 急剧削弱为弱峰](../../raw/figures/Johannes2008fermi/fig_1_SNEVCPH4.png) -> [[../figures/electronic-bands-band-structures|能带结构与带隙]]
    - **图示描述**：对比理想半满一维自由电子气与引入温度、Drude 弛豫率 γ、几何不完全嵌套 δk 三种非理想条件后实部极化率 χ′(q) 随波矢 q 的变化曲线；横轴以 k_F 为单位，纵轴为 χ′(q)（任意单位）。
    - **关键特征**：理想情形下 χ′(q) 在 q=±2k_F 处呈对数发散；引入 γ~0.1–0.2 eV 后峰高仅为 χ′(0) 的 2–2.5 倍；T=10 K 时增强约 4 倍；5% 几何偏差（δk/k_F=0.05）时增强仅约 3 倍；第三维方向 δk 量级色散同样破坏嵌套。
    - **结论/意义**：从理论上证明派尔斯纯电子不稳定性极其脆弱，真实材料中几乎不可能以理想形式存在。
  - ![图2 CDW 打开能隙 2V 后的能量增益 δE_k：主导项来自费米能级以下所有占据态而非费米面附近](../../raw/figures/Johannes2008fermi/fig_2_LRPET7NK.png) -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]
    - **图示描述**：上图为 Q=2k_F 非公度转变前后的单电子能带示意（虚线为原带、实线为打开 2V 能隙后的新带），下图为按嵌套波矢连接的电子态对的能量差 ΔE_k 与单态能量下移 δE_k 随 q/k_F 的分布，阴影区为总能量增益。
    - **关键特征**：一阶微扰给出 δE_G/V²≈(1/16μ)[1+2ln(8μ/V)]；第一项（非发散）来自费米面附近 ΔE_k<V 的态；第二项（随带宽对数发散）来自费米能级以下直至带底的所有占据态，是主导项。
    - **结论/意义**：颠覆"CDW 仅为消除费米面态密度"的传统认识，强调全部占据态及带间跃迁对不稳定性的贡献。
  - ![图3 TaSe₂ 费米面：E_F 下移 40 meV 后拓扑显著改变，但 χ′/χ′′ 几乎不变](../../raw/figures/Johannes2008fermi/fig_3_SK4I977K.png) -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]
    - **图示描述**：TaSe₂ 在 q_x–q_y 平面内的 DFT 费米面，(a) 为未平移费米能级，(b) 为将 E_F 下移 0.04 eV 以匹配 ARPES 观测；计算中包含自旋-轨道耦合（重 Ta 元素）。
    - **关键特征**：仅 40 meV 的费米能级移动就使片状费米面拓扑显著改变，与 ARPES 近乎吻合；但同一移动对 χ′(q) 和 χ′′(q) 无可观察影响；q_CDW=(1/3,0,0) 处"连弱嵌套都没有"。
    - **结论/意义**：直接证明费米面几何形状对决定 CDW 极化率结构不重要，目视费米面寻找嵌套无预测能力。
  - ![图4 TaSe₂ 的 χ′′(q)（嵌套峰位于错误波矢）与 χ′(q)（弱峰位于正确 q_CDW）对比](../../raw/figures/Johannes2008fermi/fig_4_DDJ3N7RI.png) -> [[../figures/electronic-bands-cdw-transport|CDW与输运性质]]
    - **图示描述**：TaSe₂ 在 q_x–q_y 平面上的二维彩色图，左为虚部极化率 χ′′(q)（即嵌套函数），右为实部极化率 χ′(q)；亮度代表强度。
    - **关键特征**：χ′′ 的最强嵌套峰位于远离 q_CDW=(1/3,0,0) 的波矢（与 NbSe₂ 类似，约在 (1/3,1/3,0)）；χ′ 在 q_CDW 处出现弱峰，但该峰来自有限能量电子跃迁而非费米面几何；χ′′ 与 χ′ 的峰位置解耦。
    - **结论/意义**：χ′′ 反映拓扑、χ′ 才决定稳定性，二者解耦是"嵌套不驱动 CDW"的直接证据。
  - ![图5 CeTe₃ 层状结构与纯 Te 层中 p_x/p_y 紧束缚模型及准一维费米面](../../raw/figures/Johannes2008fermi/fig_5_A4X8CSIK.png) -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]
    - **图示描述**：(a) CeTe₃ 层状晶体结构，纯 Te 层（大球）与 Ce–Te 层交替堆叠；(b) 纯 Te 层中 Te p_x、p_y 轨道的最近邻紧束缚示意，t_σ≈5t_π；(c) 该模型给出的交叉影线准一维费米面，并叠加旋转 45° 的折叠后小布里渊区。
    - **关键特征**：E_F 附近态以 Te p 轨道为主；最近邻 Te 位因层堆叠对称性破缺而不等价，导致晶胞变大、BZ 旋转；折叠后准一维带状结构仍清晰可见，为后续嵌套分析提供基础。
    - **结论/意义**：从结构与最小 TB 模型出发解释 CeTe₃ 准一维费米面的来源，是图6、图7 嵌套/隐藏嵌套讨论的铺垫。
  - ![图6 CeTe₃ 完整 DFT 费米面；沿 (110) 的 q_nest 完美嵌套但与 CDW 无关，q_CDW 处嵌套差却出现 χ′ 峰](../../raw/figures/Johannes2008fermi/fig_6_32RCJVCM.png) -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]
    - **图示描述**：(a) 完整 DFT 计算的 CeTe₃ 费米面（细线）与准一维 TB 模型结果（粗虚线）叠加；(b)(c) 为卡通图，分别演示沿 (110) 方向 q_nest 的近似完美嵌套、以及沿 q_CDW=(1,0,0) 方向的差嵌套。
    - **关键特征**：q_nest 处两准一维费米片几乎完全重合，产生 χ′′ 最强峰；q_CDW 处在 E_F 上嵌套差，但被连接两态的费米速度等大反向（v_k=−v_{k+q}），使 E_F 上下宽能量范围内 ε_k+vδk 与 ε_{k+q}−vδk 能量简并，即"隐藏嵌套"。
    - **结论/意义**：用隐藏嵌套机制解释为何正确的 CDW 波矢处 χ′ 出现峰而 χ′′ 不敏感。
  - ![图7 CeTe₃ 的 χ′′(q) 最强峰在 q_nest 而 χ′(q) 最强峰在 q_CDW，二者解耦](../../raw/figures/Johannes2008fermi/fig_7_RUGZDKQS.png) -> [[../figures/electronic-bands-cdw-transport|CDW与输运性质]]
    - **图示描述**：CeTe₃ 在 q_x–q_y 平面上的 χ′′(q)（上图）与 χ′(q)（下图）彩色图；箭头分别标出 q_nest（来自图6b 的完美几何嵌套）与 q_CDW 的位置。
    - **关键特征**：χ′′ 最强峰位于 q_nest，而同一位置在 χ′ 中完全消失；q_CDW 处 χ′′ 几乎无特征，χ′ 却出现清晰峰；χ′ 峰高的主要贡献来自远离 E_F 的有限能量跃迁，而非费米面嵌套。
    - **结论/意义**：以最直观方式把"费米面嵌套"与"CDW 电子不稳定性"彻底解耦，是全文核心论点的关键图证。
  - ![图8 Na 原子链弛豫后形成之字形构型（间距 3.43 Å，角度 152°），加倍晶胞但不打开 E_F 能隙](../../raw/figures/Johannes2008fermi/fig_8_RIPIJUU5.png) -> [[../figures/crystal-structures-bulk|体相晶体结构]]
    - **图示描述**：初始为等间距（3.34 Å）一维 Na 原子链，非链方向间距 38 Å；允许二维自由度弛豫后形成的之字形（zigzag）稳定构型，标出原子间距 3.43 Å 与弯折角 152°。
    - **关键特征**：钳制离子时纯电子 CDW 不稳定；仅允许沿一维方向弛豫时即使预置二聚化也回弹；放开二维自由度才出现之字形畸变，晶胞加倍；但 BZ 边界 k=±π/a 处矩阵元因垂直方向积分而归零，E_F 处无能隙；强制二聚化虽打开能隙却能量上不稳定。
    - **结论/意义**：在最接近理想派尔斯的体系中也排除了 Peierls 机制，表明派尔斯不稳定性比理论预期更弱，CDW 与结构相变无本质区别。
## 🔬 项目连接
  - **project-7（CDW）—— 核心参考**：这是该项目必须引用的机理文献。它直接给出判别 CDW 是否由嵌套驱动的四条严格标准（χ′′ 在 q_CDW 有峰、该峰传递到 χ′、χ′ 发散、所有声子支软化）；明确 χ′(q) 而非 χ′′(q) 才是判据；提供 NbSe₂/TaSe₂/CeTe₃ 三个原型体系的计算范式（WIEN2k/VASP，~15000–30000 k 点，2 mRy 展宽，LDA+U 处理 Ce f 电子，U=4.5 eV）；并给出 Peierls 模型脆弱性的定量公式（γ~0.1–0.2 eV 时增强仅 2–2.5 倍；5% δk 时增强约 3 倍；带间跃迁即可产生 2–3 倍的 χ′ 增强）。可直接用于项目中“为什么不能只看费米面/χ′′”的方法论论证与电声耦合驱动图像。
  - **project-4（TTF 分子计算）**：无直接项目连接。本文聚焦无机层状金属的 CDW，与 TTF 分子体系的电子结构计算问题不同；但其“计算 χ′(q) 而非目视费米面”的第一性原理响应函数方法论对任何电荷有序问题具有一般参考意义。
  - **project-5（SnTe 铁电模拟）**：弱方法学参考。本文展示 LDA/LDA+U、自旋-轨道耦合（重元素 Ta）、以及“钳制离子 vs 允许弛豫”的超胞对比计算，可类比用于铁电畸变稳定性测试；但物理对象（CDW vs 铁电位移）不同。
  - **project-1 / project-2 / project-3 / project-6**：无直接项目连接。
## 🔗 项目双链
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]
- 项目 [[../projects/project-7-cdw-charge-density-wave|项目七：CDW电荷密度波]]

## 📝 组织与用词
文章采用“先破后立”的总-分-总结构：（1）引言区分两种 CDW 定义并为“派尔斯 CDW”立下四条可证伪标准；（2）第一部分用 1D 模型解析推导证明 χ′(2k_F) 对数发散对温度、散射、几何偏差、带间效应的脆弱性，并证明能隙打开后的能量增益主要来自远离 E_F 的占据态；（3）第二部分用 DFT 逐一解剖 NbSe₂/TaSe₂（χ′′ 峰与 q_CDW 错位）、CeTe₃（近乎完美嵌套但峰在错误波矢，q_CDW 处为“隐藏嵌套”）、Na 链（理想 1D 也不发生派尔斯二聚化，而是之字形畸变且无能隙）；（4）总结 CDW=ILT，必须计算 χ′(q) 并结合电声耦合。值得复用的术语：费米面嵌套（Fermi surface nesting）、派尔斯不稳定性（Peierls instability）、电子极化率实部/虚部（real/imaginary part of electronic susceptibility χ′/χ′′）、电子-声子耦合（electron-phonon coupling, q-dependent）、隐藏嵌套（hidden nesting）、非公度晶格转变（incommensurate lattice transition, ILT）、电荷密度波（charge density wave, CDW）、钳制离子计算（clamped-ion calculation）。
## ✏️ 可写入 Wiki 的要点
  1. 派尔斯 CDW 的四条严格判据：(a) χ′₀′(q)（即低频 χ′′/ω）在 q_CDW 有峰；(b) 该峰传递到 χ′₀(q)；(c) χ′₀ 的峰在全极化率中发散，使电子子系统在离子钳制时仍不稳定；(d) 所有声子支（对称性禁戒除外）都在 q_CDW 软化。作者指出没有任何真实材料满足全部四条。
  2. χ′(q)（实部）与 χ′′(q)（虚部）的物理分工：χ′′(q,ω→0)=Σ_k δ(ε_k−ε_F)δ(ε_{k+q}−ε_F) 只反映[[../concepts/fermi-surfaces|费米面]]拓扑、可由中子散射测量；χ′(q)=Σ_k [f(ε_k)−f(ε_{k+q})]/(ε_k−ε_{k+q}) 才决定电子稳定性，且包含所有占据态与有限能量跃迁贡献，但实验上难以测绘。仅凭 χ′′ 判断 CDW 趋势是常见错误。
  3. Peierls 发散极其脆弱：引入 Drude 弛豫率 γ 后，χ′(±2k_F)/χ′(0)≈¼ln(1+64μ²/γ²)；γ~0.1–0.2 eV 时增强仅 2–2.5 倍；T=10 K 时约 4 倍；几何不完全嵌套 δk 时 χ′(2k_F)/χ′(0)≈½[1+ln(4k_F/δk)]，5% 偏差（δk/k_F=0.05）增强仅约 3 倍。第三维方向 δk 量级色散同样破坏嵌套，输运[[../concepts/migdal-eliashberg-theory|各向异性]]小于一个数量级的材料在“嵌套意义上”是三维的。
  4. DFT 总能量表达式 δE_tot=−½δV_ext χ δV_ext=−½δV_ext χ₀(1−v_iχ₀)⁻¹δV_ext 表明：即使无相互作用的 χ₀ 发散，全极化率 χ=χ₀/ε 也受 −1/v_i 限制而不发散；考虑局域场后给出 Pick–Cohen–Martin 声子频率公式。相互作用半满系统对无穷小扰动稳定，只有电声耦合超过临界值的有限畸变才能稳定。
  5. CDW 能量增益的来源被定量改写：δE_G/V²≈(1/16μ)[1+2ln(8μ/V)]。第一项（非发散）来自费米能级附近 ∆E_k<V 的态；第二项（随带宽对数发散）来自费米能级以下直至带底的所有占据态，是主导项。因此“优化所有占据态能量”比“在最大费米面面积上打开能隙”更重要，带间跃迁不可忽略。
  6. 绝缘二带[[../concepts/tight-binding|紧束缚模型]]（带间距 ε）的带间极化率 χ′_inter(q)=(1/a)/√(ε²−4sin²(qa/2))，在 BZ 边界 q=π/a 处相对 q=0 增强 ε/√(ε²−4) 倍；ε=2.25（能隙为带宽 1/8）时增强 2.2 倍，与典型“嵌套增强”同量级，说明没有费米面也能产生类 CDW 的 χ′ 结构。
  7. NbSe₂：χ′′ 的嵌套峰在 q=(1/3,1/3,0)，而实验 q_CDW=(1/3,0,0)；χ′ 在 q_CDW 仅有弱峰，必须与同波矢电声耦合协同。超胞计算中离子钳制时即使人工预置电荷调制也会弛豫回高对称态；允许离子移动后正确波矢的不稳定性才出现。
  8. TaSe₂：[[../concepts/spin-orbit-coupling|自旋-轨道耦合]]（重 Ta）显著改变 Γ–K 附近色散和费米面拓扑；E_F 下移 0.04 eV 可使计算费米面与 ARPES 近乎一致，但该移动对 χ′、χ′′ 无可观察影响，直接证明费米面形状对决定 CDW 磁化率结构不重要；q_CDW 处“连弱嵌套都没有”，χ′ 峰来自有限能量电子跃迁。
  9. CeTe₃：纯 Te 层的 p_x/p_y 最近邻紧束缚模型（t_σ≈5t_π）给出交叉影线准一维费米面，折叠入旋转 45° 的小 BZ；沿 (110) 的 q_nest 近乎完美嵌套并产生最强 χ′′ 峰，但与 CDW 无关；q_CDW=(1,0,0) 处 χ′′ 弱而 χ′ 强，原因是被连接两态的费米速度等大反向（v_k=−v_{k+q}），使 E_F 上下宽能量范围内 ε_k+vδk 与 ε_{k+q}−vδk 能量简并——即“[[../concepts/hidden-nesting|隐藏嵌套]]”（Whangbo et al., Science 1991）。计算用 LDA+U（U=4.5 eV，fully localized limit）移除 Ce f 带，~30000 k 点。
  10. Na 原子链（非链方向间距 38 Å，链内 Na–Na 3.34 Å）：钳制离子时纯电子 CDW 不稳定；允许沿 1D 弛豫也不[[../concepts/dimerization|二聚化]]（即使预置二聚化也回弹）；只有放开二维自由度才形成之字形畸变（间距 3.43 Å，角度 152°），晶胞加倍但 E_F 处无能隙——因为畸变是二维的而波函数是一维的，垂直方向积分使 BZ 边界矩阵元归零，紧束缚计算同样给出 k=±π/a 态简并。强制二聚化虽打开能隙导致能量上不稳定，故 Peierls 机制可被排除。
