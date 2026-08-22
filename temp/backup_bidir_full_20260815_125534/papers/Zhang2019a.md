---
citekey: Zhang2019a
title: "Studying Stability of Atom Packing for Ti Nanoparticles on Heating by Molecular Dynamics Simulations"
authors: [Lin Zhang]
year: 2019
journal: "Advanced Engineering Materials"
doi: "10.1002/adem.201800531"
url: "https://doi.org/10.1002/adem.201800531"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/Zhang2019a]]
projects: []
concepts: [density-functional-theory, machine-learning-potential, molecular-dynamics, embedded-atom-method, pair-distribution-function, common-neighbor-analysis, icosahedral-structure, hcp-structure, fcc-structure, bcc-structure, surface-premelting, size-dependent-melting, dulong-petit-law, five-fold-twinning, geometric-shell-closure, structural-phase-transition, nvt-ensemble, icosahedral-packing]
entities: [Ti, Ti-6Al-4V, LAMMPS, Moldy, GULP]
methods: [md, eam, pair-distribution-function, common-neighbor-analysis, nvt-ensemble, velocity-rescaling, bisection-algorithm, md-step-heating]
materials: [Ti]
figures: [crystal-structures-surfaces-defects, heterostructures-stacking, mathematical-models-computational, mathematical-models-formulas, mathematical-models-simulations]
领域基础知识:: >-
  钛及其合金是重要的生物医用和航空航天材料，具有高比强度、低密度和优异的生物相容性。增材制造（AM，3D打印）技术常用于加工钛部件，该过程涉及对金属粉末的快速熔化和凝固。纳米材料的性质强烈依赖于其尺寸，与宏观块体材料有显著差异。
研究背景:: >-
  当前增材制造主要使用微米级钛粉，其性质接近块体。但对于纳米级钛粉，其在受热时的结构演变和熔化机制尚不清晰。已有研究多集中于由几十个原子组成的极小团簇，对含有数百至数千原子的更大尺寸纳米粒子的研究存在空白。
作者的问题意识:: >-
  当钛颗粒尺寸从微米级缩小到纳米级时，其熔化行为与块体材料有何不同？纳米粒子内部的原子堆积结构如何随温度和粒子尺寸而变化？其微观驱动力是什么？
主要研究对象:: >-
  直径从1.6 nm至5.2 nm（包含135至4079个原子）的孤立纯钛（Ti）纳米粒子。
主要研究方法:: >-
  经典分子动力学（MD）模拟，结合嵌入原子法（EAM）势函数描述原子间相互作用。通过逐步加热和正则系综（NVT）模拟，使用对分布函数（PDF）和原子对分析（PA）技术来表征结构演变。
研究意义:: >-
  理论上，揭示了钛纳米粒子从“团簇-like”多重结构转变到“类块体”熔化的尺寸效应图景，阐明了表面原子在纳米尺度相变中的核心作用。实践上，为基于粉末床熔融的金属增材制造工艺提供了微观机理层面的指导，有助于优化工艺参数，控制制件微观结构。
研究结论:: >-
  1. 钛纳米粒子的熔化行为具有强烈的尺寸依赖性。直径小于2.5 nm的粒子倾向于形成稳定的二十面体（Ih）结构，并经历多重结构转变；较大粒子则呈现类块体熔化，但表面原子会先于内部发生重排。2. 表面原子是所有结构转变的源头，其高移动性驱动了整体的结构演变。3. 对于直径小于3 nm的粒子，经典杜隆-珀蒂定律不再适用。
对领域的贡献:: >-
  构建了钛纳米粒子“尺寸-结构-热稳定性”的定量关系，将极小团簇和块体材料之间的热力学行为联系了起来。揭示了MD模拟中结构转变的原子细节，为理解和预测其他金属纳米粒子的热力学行为提供了研究范式。
未来研究方向提及:: >-
  1. 开发能够同时准确描述HCP和BCC等多相结构的新型钛势函数。2. 将模拟对象从纯金属拓展到更接近实际应用的多组分钛合金体系。3. 研究不同加热/冷却速率对结构转变路径的影响。
未来研究方向思考:: >-
  1. 探索存在表面缺陷（如台阶、空位）或氧化层的纳米粒子的熔化行为。2. 研究多个纳米粒子在接触状态下，受热时的团聚、烧结和熔化耦合过程，以模拟真实的粉末床环境。3. 结合机器学习势函数，实现对大尺寸纳米粒子相变行为的更高精度模拟。4. 发展先进的原位透射电子显微镜（In-situ TEM）实验技术，对模拟结果进行直接验证。
tags:
  - paper
  - type/theory
  - year/2019
  - concept/molecular-dynamics
  - concept/embedded-atom-method
  - concept/pair-distribution-function
  - concept/common-neighbor-analysis
  - concept/icosahedral-structure
  - concept/hcp-structure
  - concept/fcc-structure
  - concept/bcc-structure
  - concept/surface-premelting
  - concept/size-dependent-melting
  - concept/dulong-petit-law
  - concept/five-fold-twinning
  - concept/geometric-shell-closure
  - concept/structural-phase-transition
  - concept/nvt-ensemble
  - entity/Ti
  - entity/Ti-6Al-4V
  - entity/LAMMPS
  - entity/Moldy
  - entity/GULP
  - method/md
  - method/eam
  - method/pair-distribution-function
  - method/common-neighbor-analysis
  - method/nvt-ensemble
  - method/velocity-rescaling
  - method/bisection-algorithm
  - method/md-step-heating
  - material/Ti
  - topic/nanoparticles
  - topic/molecular-dynamics
  - topic/phase-transition
  - topic/metallic-materials
  - topic/additive-manufacturing
  - topic/melting
---

## Zhang2019a — 用分子动力学方法研究Ti纳米粒子在加热过程中原子堆积的稳定性

## 📄 元数据
Lin Zhang，2019，Advanced Engineering Materials，21(4): 1800531，DOI 10.1002/adem.201800531
## 💡 一句话
用Zhou EAM势的经典MD模拟系统刻画了直径1.6–5.2 nm（135–4079原子）孤立Ti纳米粒子在逐级加热中的熔化行为，识别出<2.5 nm粒子的Ih几何壳层闭合与多重结构转变、2.5–4 nm粒子的"表面预熔—整体崩溃"机制，并以ΔEav/ΔT→1.5kB判定杜隆-珀蒂定律在约3 nm以下失效。

## 🔗 Wiki 双链
  - 概念 [[../concepts/density-functional-theory]]（文中引用Agarwal等用该EAM势与DFT状态方程对比验证）
  - 概念 [[../concepts/machine-learning-potential]]（仅在"未来方向"中提及MLIP可提升大尺寸粒子相变精度）
  - 概念 [[../concepts/molecular-dynamics|分子动力学（MD）]]（1.6 fs步长、NVT、逐级加热，积分牛顿方程追踪原子轨迹）
  - 概念 [[../concepts/embedded-atom-method|嵌入原子法（EAM）]]（Zhou等参数化的Ti EAM势，re=0.293 nm，截断0.656 nm）
  - 概念 [[../concepts/pair-distribution-function|对分布函数（PDF）]]（g(R)，用峰锐/宽化判别晶态/液态）
  - 概念 [[../concepts/common-neighbor-analysis|共同邻居分析（CNA/PA）]]（1421/1422/1441/1661键对指纹识别FCC/HCP/BCC）
  - 概念 [[../concepts/icosahedral-packing|二十面体结构（Ih）]]（<2.5 nm小粒子低温弛豫形成的五重对称密堆积）
  - 概念 [[../concepts/surface-premelting|表面预熔]]（低配位表面原子先于芯部重排，无序壳层贯穿粒子）
  - 概念 [[../concepts/size-dependent-melting|尺寸依赖熔化]]（<4 nm Tm振荡式上升，>4 nm收敛至块体值）
  - 概念 [[../concepts/dulong-petit-law|杜隆-珀蒂定律]]（N<800–900时ΔEav/ΔT偏离1.5kB势能贡献）
  - 概念 [[../concepts/five-fold-twinning|五重孪晶]]（Ti257在1300 K形成，界面为HCP堆积）
  - 概念 [[../concepts/geometric-shell-closure|几何壳层闭合]]（Ih团簇"幻数"稳定性来源）
  - 实体 [[../entities/Ti|钛（Ti）]]（α相HCP，实验块体熔点1941 K）
  - 实体 [[../entities/LAMMPS|LAMMPS]]（文中列为可处理非周期体系的主流MD代码）
  - 实体 [[../entities/Moldy|Moldy]]（本文MD代码修改自旧版Moldy，用大盒子PBC隔离粒子）
  - 图表 [[../figures/crystal-structures]]（HCP/FCC/Ih/BCC原子堆积与五重孪晶快照）
  - 图表 [[../figures/mathematical-models]]（EAM总势能、电子密度、对势、嵌入能分段公式 Eq.1–7；PDF公式 Eq.9）
  - 年度 [[../write/2015-2019|2019]]
  - 概念 [[../concepts/fcc-structure]]、[[../concepts/nvt-ensemble]]、[[../concepts/hcp-structure]]、[[../concepts/structural-phase-transition]]、[[../concepts/icosahedral-structure]]、[[../concepts/bcc-structure]]
  - 实体 [[../entities/GULP]]、[[../entities/Ti-6Al-4V]]
  - 相关论文 [[../../raw/note/Zhang2019a]]

## 🆕 新概念/实体建议
  - `figures/thermodynamic-curves.md` — 新图表类型：能量-温度曲线、PDF、Tm-d关系、ΔEav/ΔT-N关系等热分析图

## 📊 关键图表
  - ![EAM总势能公式 Eq.1](../../raw/figures/Zhang2019a/eq_1_JKSLE4FW.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：EAM势的总能量表达式，将N原子体系的总势能拆为嵌入能与对势能两部分。
  - **关键特征**：$E_{\text{tot}}=\sum_i F_i(\rho_e)+\tfrac12\sum_{i\ne j}\phi_{ij}(r_{ij})$；嵌入能$F_i$依赖背景电子密度$\rho_e$，对势$\phi_{ij}$依赖原子间距$r_{ij}$；该项是后续所有能量/结构分析的势函数基础。
  - ![广义元素对势 Eq.3](../../raw/figures/Zhang2019a/eq_3_IY4F7YGW.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：Zhou EAM势中两体对势$\phi_{ij}(r_{ij})$的解析形式，由指数衰减项乘以截断多项式构成。
  - **关键特征**：分子分母分别含$(r_{ij}/r_e-\kappa)^{20}$与$(r_{ij}/r_e-\lambda)^{20}$，在$r_e=0.2933872$ nm附近给出平衡间距；20次幂提供在0.656 nm处的陡峭光滑截断；参数$A,B,\alpha,\beta,\kappa,\lambda$由表1给出。
  - ![电子密度函数 Eq.4](../../raw/figures/Zhang2019a/eq_4_LZSYGSBF.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：原子$j$在原子$i$位置产生的电子密度贡献$f(r)$，形式与对势吸引项相同。
  - **关键特征**：$f(r)=f_e\exp[-\beta(r/r_e-1)]/[1+(r/r_e-\lambda)^{20}]$；$f_e=1.863200$，与对势共用$\beta,\lambda$保证自洽；所有邻居贡献求和即得$\rho_e=\sum_j f_j(r_{ij})$，用于驱动嵌入能。
  - ![嵌入能分段公式 Eq.5–7](../../raw/figures/Zhang2019a/eq_5_AKZ9ZC4I.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：嵌入能$F(\rho)$的三段拼接总览，按电子密度$\rho$相对于$\rho_n=0.85\rho_e$、$\rho_0=1.15\rho_e$的位置分段。
  - **关键特征**：低密度段用三次多项式$F_{n0..3}$、中密度段用三次多项式$F_{0..3}$、高密度段用Rose型$F_e[1-\ln(\rho/\rho_s)^\eta]$；三段在连接点处函数值与斜率均连续；$\rho_e=\rho_s=25.565138$。
  - ![嵌入能分段公式 Eq.6](../../raw/figures/Zhang2019a/eq_6_3NZCI3TL.png) -> [[../figures/mathematical-models-formulas|光学、输运与其他解析公式]]
  - **图示描述**：中密度段（$\rho_n\le\rho<\rho_0$）的三次多项式嵌入能表达式。
  - **关键特征**：$F(\rho)=\sum_{i=0}^{3}F_i(\rho/\rho_e-1)^i$；系数$F_0=3.22$ eV、$F_1=0$、$F_2=0.608587$ eV、$F_3=0.750710$ eV；与Eq.5、Eq.7在端点匹配值与一阶导数，保证能量曲面光滑。
  - ![嵌入能分段公式 Eq.7](../../raw/figures/Zhang2019a/eq_7_WN3PU9VD.png) -> [[../figures/mathematical-models-formulas|光学、输运与其他解析公式]]
  - **图示描述**：高密度段（$\rho\ge\rho_0$）嵌入能的Rose普适状态方程形式。
  - **关键特征**：$F(\rho)=F_e[1-\ln(\rho/\rho_s)^\eta]$；$F_e=3.219176$ eV、$\eta=0.558572$；描述过压缩状态下嵌入能随电子密度对数缓慢上升的行为。
  - ![对分布函数公式 Eq.9](../../raw/figures/Zhang2019a/eq_9_KF8MDN7A.png) -> [[../figures/mathematical-models-simulations|模拟与数值结果]]
  - **图示描述**：对分布函数$g(R)$的统计定义，用于在模拟轨迹中识别晶态/液态短程序。
  - **关键特征**：$g(R)\propto\langle\sum_{i\ne j}\delta(R-|R^*_{ij}|)\rangle$，对全部原子对距离作直方图并在整条轨迹上平均；尖锐多重峰对应HCP/FCC/Ih晶态，宽化单峰对应液态；是图4判熔化的核心定量指标。
  - ![图1 Ti135/Ti257/Ti895弛豫过程每原子能量随时间步变化](../../raw/figures/Zhang2019a/fig_1_8GSJRYRQ.png) -> [[../figures/mathematical-models-simulations|模拟与数值结果]]
  - **图示描述**：三条曲线分别给出Ti135、Ti257、Ti895在50 K初始弛豫阶段每原子总势能（eV/atom）随模拟时间步的变化。
  - **关键特征**：所有粒子从人为切割的高能HCP构型起步，能量快速跌落并进入振荡平衡；Ti135、Ti257出现阶梯式再次下降，标志从HCP向更低能量的Ih等结构发生相变；Ti895仅平滑下降后平稳，保持初始HCP；直接证明小粒子表面原子比例高、低温即自发重构。
  - ![图2 1421/1422/1441/1661原子对示意图](../../raw/figures/Zhang2019a/fig_2_34UVRTQI.png) -> [[../figures/crystal-structures-surfaces-defects|表面、缺陷与形貌]]
  - **图示描述**：球棍示意Honeycutt–Andersen对分析（PA）所用的四类特征键对：1421、1422、1441、1661。
  - **关键特征**：白圆为成键原子对，黑圆为其共有近邻，黑线表示在截断距离0.656 nm内；1421与1422对应FCC/HCP密堆积（1422偏HCP，1421在FCC中亦多），1441+1661对应BCC；该图是图7定量追踪HCP→FCC转变和BCC缺失的方法学钥匙。
  - ![图3 小尺寸粒子平均能量-温度曲线](../../raw/figures/Zhang2019a/fig_3_VVXJNDWX.png) -> [[../figures/mathematical-models-simulations|模拟与数值结果]]
  - **图示描述**：Ti135、Ti257、Ti895在300–1400 K逐级加热中的每原子平均势能$E_{\text{av}}$（eV/atom）对温度（K）曲线。
  - **关键特征**：Ti135在750 K附近出现平台/下降，300 K因表面比例最高而整体能量最高；Ti257在600 K以下不稳定、700–1200 K出现长平台，1200 K后再变；Ti895在1300 K以下近线性上升、1300 K斜率突变进入熔化（二分法定位熔点1260 K）；三条曲线对比直观呈现尺寸依赖的多形转变与类块体熔化。
  - ![图4 Ti135/Ti257/Ti895不同温度PDF与原子堆积快照](../../raw/figures/Zhang2019a/fig_4_SK6TQB88.png) -> [[../figures/heterostructures-stacking|异质结与堆叠]]
  - **图示描述**：三栏(a/b/c)分别对应Ti135、Ti257、Ti895，左侧为300–1400 K若干温度的对分布函数$g(R)$（R以nm为单位），右侧为统计窗内能量最低构型的原子堆积快照。
  - **关键特征**：Ti135在300 K即呈Ih特征PDF并保持至1200 K，1400 K峰消失转为液态；Ti257在800 K出现峰位右移与远峰突变，对应HCP→Ih→FCC，1300 K形成五重孪晶（界面为HCP），1400 K分裂为两块；Ti895主峰在1300 K前保持HCP，仅峰高降低，1300 K后突变为液态；PDF与快照互为印证，是全文最综合的结构演变证据。
  - **结论/意义**：支撑"小粒子多重结构转变、大粒子保持HCP至熔化"的核心论断，并把Ti895熔点锁定在1260 K。
  - ![图5 熔化温度随粒子直径变化（<4 nm振荡，>4 nm收敛）](../../raw/figures/Zhang2019a/fig_5_UJHJUH45.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：27个Ti纳米粒子的熔化温度$T_m$（K）对粒子直径$d$（nm，1.6–5.2 nm）散点/折线图。
  - **关键特征**：$d<4$ nm段$T_m$随$d$振荡式快速升高，逐尺寸波动源于表面原子比例与几何壳层闭合差异；$d>4$ nm后斜率明显变缓，$T_m$向EAM块体预测值2218 K收敛；4 nm是"分子型"向"块体型"熔化过渡的特征尺寸；EAM块体熔点较实验1941 K高约277 K（14%）。
  - ![图6 大尺寸粒子（Ti1099–Ti3455）能量-温度曲线](../../raw/figures/Zhang2019a/fig_6_T7VXXEFK.png) -> [[../figures/mathematical-models-simulations|模拟与数值结果]]
  - **图示描述**：Ti1099、Ti1639、Ti2361、Ti2493、Ti3347、Ti3455六个直径3.36–5.03 nm粒子的$E_{\text{av}}$–$T$曲线（eV/atom vs K）。
  - **关键特征**：熔化前能量随温度近线性增加，误差棒小，结构稳定；熔点处能量阶跃上升，且直径越大熔点越高、熔化前势能越低；Ti1099误差棒略大，暗示其熔化前有少量HCP→FCC局部转变（与图7一致）；整体呈现"表面预熔—整体崩溃"的类块体熔化模式。
  - ![图7 六粒子1421/1422原子对数量随温度变化](../../raw/figures/Zhang2019a/fig_7_TQ8EAVTC.png) -> [[../figures/crystal-structures-surfaces-defects|表面、缺陷与形貌]]
  - **图示描述**：与图6对应的六个大粒子中，1421与1422特征键对数量（或占比）随300–1450 K温度的变化。
  - **关键特征**：低温下两者之和维持高位，代表HCP/FCC密堆积比例；在各自熔点处1421+1422数量急剧下降，标志有序结构崩塌；Ti1099在熔化前1421升、1422降，定量显示HCP→FCC局部转变，其他更大粒子无此现象；全程几乎不出现1441/1661，暴露该EAM势不能再现块体Ti的HCP→BCC高温相变。
  - ![图8 ΔEav/ΔT斜率随原子数N变化（杜隆-珀蒂1.5kB边界）](../../raw/figures/Zhang2019a/fig_8_2H6SNMFM.png) -> [[../figures/mathematical-models-simulations|模拟与数值结果]]
  - **图示描述**：高温区势能-温度斜率$\Delta E_{\text{av}}/\Delta T$对粒子原子数$N$的散点图，并以1.5$k_B$水平线作杜隆-珀蒂参照。
  - **关键特征**：$N<800$（约$d<3$ nm）的粒子斜率远低于1.5$k_B$，Ti135、Ti257甚至为负，因加热中朝更低势能的Ih等结构转变；$N\ge 895$后斜率稳定在约1.5$k_B$，与块体晶体势能贡献一致；Ti135取1050–1200 K、Ti257取850–1200 K、其他取300–1200 K拟合；该图把经典热力学的纳米尺度适用边界定在~3 nm。
  - ![图9 Ti1099/Ti2361/Ti3347不同温度原子堆积（表面预熔可视化）](../../raw/figures/Zhang2019a/fig_9_JRFEECJM.png) -> [[../figures/crystal-structures-surfaces-defects|表面、缺陷与形貌]]
  - **图示描述**：Ti1099、Ti2361、Ti3347在300、1000、1250、1450 K四个温度下的原子构型快照。
  - **关键特征**：300 K三粒子均呈完整HCP有序；1000 K表面原子开始无序重排，核心仍为HCP，形成"液态壳层"；1250 K临近熔点时无序区贯穿粒子；1450 K整体完全无序呈液态；粒子越小表面无序越早侵入核心，直观可视化了"表面预熔→无序壳层扩展→整体熔化"机制。
  - ![表1 EAM势参数](../../raw/figures/Zhang2019a/tab_1_GBW2JGJ2.png) -> [[../figures/mathematical-models-computational|计算方法与泛函]]
  - **图示描述**：Zhou等Ti EAM势的全部数值参数表，分两行列势函数与嵌入能系数。
  - **关键特征**：$r_e=0.2933872$ nm、$f_e=1.863200$、$\rho_e=\rho_s=25.565138$；$A=8.775431$、$B=4.680230$、$A(\text{eV})=0.373601$、$B(\text{eV})=0.570968$、$\kappa=0.5$、$\lambda=1.0$；嵌入能系数$F_{n0..3}$、$F_{0..3}$、$F_e=3.219176$ eV、$\eta=0.558572$；截断半径0.656 nm，复现的无缺陷块体Ti熔点为2218 K。

## 🔬 项目连接
  - **project-5 SnTe铁电模拟 — weak**：本文物理对象是金属Ti纳米粒子熔化，与SnTe铁电无直接材料/机理重合；但作为经典MD加热模拟的方法学范本，其计算流程可类比复用：(1) NVT逐级加热协议（50 K起、50 K步长、每温2×10⁶步、速度标定控温、1.6 fs步长、以上一温终态为下一温初态）；(2) 结构诊断三件套——平均势能Eav、对分布函数g(R)、对分析1421/1422/1441/1661——用于区分HCP/FCC/BCC/液态，对应铁电模拟中可用类似的局部有序参数/键对分析追踪结构相变；(3) "二分法"在25 K窗口内定位转变温度（Ti895熔点1260 K即由1250–1300 K区间二分得到）可直接用于铁电居里/相变温度的精确定位；(4) ΔEav/ΔT斜率与杜隆-珀蒂1.5kB对比划定经典热力学适用尺寸（N<800–900偏离），为SnTe纳米粒子有限尺寸效应提供类比判据；(5) "表面预熔→无序壳层→整体崩溃"的图像可类比有限尺寸铁电体中表面退极化场驱动的表面先行失稳。物理差异大，故仅weak。
  - project-1 双光子 / project-2 Mn多铁 / project-3 机械发光NN / project-4 TTF分子计算 / project-6 湿度传感器 / project-7 CDW：无直接项目连接（金属EAM MD熔化主题与分子晶体、多铁、CDW、荧光、湿度传感机制无可复用的物理或数据交集；project-4虽涉及计算但TTF为分子晶体，不用EAM金属势，方法不可直接迁移）。

## 🔗 项目双链

## 📝 组织与用词
  论文采用标准"引言—实验/方法—结果与讨论—结论"IMRaD结构。论证链条为"应用驱动（AM钛粉）→尺度问题（微米→纳米）→方法（EAM MD）→三层结果（小粒子多形转变 / 中粒子表面预熔 / 大粒子类块体）→量化（Tm-d、ΔEav/ΔT-N）→坦诚局限（EAM不能给HCP→BCC）"。方法部分给全EAM势函数形式（Eq.1–7）、电子密度（Eq.2、4）、PDF（Eq.9）和参数表1，可复用性强。结果讨论用"能量+PDF+PA+快照"四重证据交叉印证，避免单一指标判熔化的模糊性。
  值得在wiki叙述中复用的关键词/术语：
  - atom packing / 原子堆积
  - geometric shell closure / 几何壳层闭合 [[../concepts/geometric-shell-closure|几何壳层闭合]]
  - multi-structures' transitions / 多结构转变
  - surface premelting / 表面预熔 [[../concepts/surface-premelting|表面预熔]]
  - pair analysis (PA) / 对分析 [[../concepts/pair-analysis|对分析]]（即共同邻居分析CNA）
  - pair distribution function g(R) / 对分布函数 [[../concepts/pair-distribution-function|对分布函数]]
  - icosahedron (Ih) / 二十面体
  - five-fold twins / 五重孪晶 [[../concepts/five-fold-twinning|五重孪晶]]
  - bisection algorithm / 二分法（熔点定位）
  - Dulong–Petit limit / 杜隆-珀蒂极限（1.5kB势能斜率）

## ✏️ 可写入 Wiki 的要点
  1. **[[../concepts/embedded-atom-method|EAM势]]函数形式**：Etot=Σ_i Fi(ρe)+½Σ_{i≠j}φij(rij)；电子密度ρe=Σ_j fj(rij)；对势φij为A·exp[−α(rij/re−1)]/(1+(rij/re−κ)²⁰)−B·exp[−β(rij/re−1)]/(1+(rij/re−λ)²⁰)；嵌入能F(ρ)在ρ<ρn（0.85ρe）、ρn≤ρ<ρ0（1.15ρe）、ρ≥ρ0三段分别用三次多项式与Fe[1−ln(ρ/ρs)^η]拼接，保证值和斜率连续。
  2. **Ti EAM参数（Zhou等）**：re=0.2933872 nm，fe=1.863200，ρe=ρs=25.565138，A=8.775431，B=4.680230，A(eV)=0.373601，B(eV)=0.570968，κ=0.5，λ=1.0；截断0.656 nm；预测无缺陷块体Ti熔点2218 K，比实验值1941 K高277 K（14%偏差），作者认为仍可用于固-液堆积变化研究。
  3. **模拟协议**：从块体HCP Ti沿[101̄0]、[12̄10]、[0001]建20.745×20.745×24.894 nm³晶胞，切出1.6–5.2 nm球形碎片共27组（135至4079原子）；50 K起以50 K步长升至1400 K，NVT系综，速度标定每步控温，1.6 fs时间步，每温2×10⁶步；小粒子（Ti135/257/895）取末70 000步、大粒子取末300 000步统计能量；结构分析取统计窗内能量最低那一步的轨迹以消除粒子旋转影响。
  4. **三尺寸区熔化图像**：(a) <2.5 nm（Ti135、Ti257）：低温即从初始HCP弛豫到Ih，加热中经历HCP→Ih→FCC多结构转变，Ti257在1300 K形成[[../concepts/five-fold-twinning|五重孪晶]]（界面HCP）；(b) 2.5–4 nm（如Ti895，熔点1260 K）：芯部保持HCP，表面在450–1250 K宽温区重排，1300 K无序迅速贯穿；(c) >4 nm（Ti1099等6粒，直径3.36–5.03 nm）：类块体[[../concepts/surface-premelting|表面预熔]]，Tm随直径缓慢升高并收敛。
  5. **Tm-d关系（图5）**：d<4 nm时Tm随d振荡式快速上升（表面原子比例高且排布逐尺寸不同），d>4 nm斜率变缓趋近块体值；4 nm是"分子型"向"块体型"熔化过渡的特征尺寸。
  6. **[[../concepts/common-neighbor-analysis|对分析]]指纹**：1421对（两对共有4邻居的键合邻居平行排列）与1422对（两对键合邻居有交点）之和代表HCP/FCC密堆积比例；其中1422为HCP特征、1421在FCC中亦大量存在；1441+1661为BCC特征。Ti1099熔化前1422降、1421升，证明发生HCP→FCC局部转变；所有粒子全程几乎无1441/1661，说明该EAM势不能再现块体Ti的HCP→BCC高温相变。
  7. **杜隆-珀蒂失效边界（图8）**：高温晶体每原子热容3kB，势能贡献1.5kB。N<800（约<3 nm）粒子ΔEav/ΔT远小于1.5甚至为负（因加热中向更低势能的Ih等结构转变）；N≥895后斜率稳定在≈1.5，小偏差来自表面结构差。Ti135取1050–1200 K、Ti257取850–1200 K、其余取300–1200 K计算斜率。
  8. **熔点二分法**：以Ti895为例，在1250–1300 K间：1280 K无序→缩至1250–1280；1265 K熔→再测1258 K仍有序→区间1258–1265；反复二分至1260 K。该流程可直接迁移到其他[[../concepts/molecular-dynamics|经典MD]]相变温度定位。
  9. **孤立粒子实现**：代码基于旧版Moldy（PBC预定），用足够大的中心晶胞（20.7×20.7×24.9 nm³）使中心粒子与26个镜像像胞原子间距超过0.656 nm截断，从而无需改代码即模拟孤立粒子；文中指出GULP、LAMMPS等支持原生非周期模拟。
  10. **作者自陈局限与未来方向**：单一EAM势无法同时描述低温静态构型与高温热力学（HCP→BCC缺失）；需MEAM/多体势、多组分（Ti-6Al-4V）、非平衡极速加热/冷却（AM实际>10⁶ K/s）、多粒子团聚烧结耦合、MLIP提升精度，并呼唤原位TEM对1.6–5.2 nm这一"TEM太大、XRD太小"表征盲区的实验验证。
