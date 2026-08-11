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
original_note: "[[../../raw/note/Zhang2019a]]"
projects: [project-5]
concepts: [density-functional-theory, machine-learning-potential, molecular-dynamics, embedded-atom-method, pair-distribution-function, common-neighbor-analysis, icosahedral-structure, hcp-structure, fcc-structure, bcc-structure, surface-premelting, size-dependent-melting, dulong-petit-law, five-fold-twinning, geometric-shell-closure, structural-phase-transition, nvt-ensemble]
entities: [Ti, Ti-6Al-4V, LAMMPS, Moldy, GULP]
methods: [md, eam, pair-distribution-function, common-neighbor-analysis, nvt-ensemble, velocity-rescaling, bisection-algorithm, md-step-heating]
materials: [Ti]
figures: [crystal-structures, mathematical-models, thermodynamic-curves]
"领域基础知识": >-
  钛及其合金是重要的生物医用和航空航天材料，具有高比强度、低密度和优异的生物相容性。增材制造（AM，3D打印）技术常用于加工钛部件，该过程涉及对金属粉末的快速熔化和凝固。纳米材料的性质强烈依赖于其尺寸，与宏观块体材料有显著差异。
"研究背景": >-
  当前增材制造主要使用微米级钛粉，其性质接近块体。但对于纳米级钛粉，其在受热时的结构演变和熔化机制尚不清晰。已有研究多集中于由几十个原子组成的极小团簇，对含有数百至数千原子的更大尺寸纳米粒子的研究存在空白。
"作者的问题意识": >-
  当钛颗粒尺寸从微米级缩小到纳米级时，其熔化行为与块体材料有何不同？纳米粒子内部的原子堆积结构如何随温度和粒子尺寸而变化？其微观驱动力是什么？
"主要研究对象": >-
  直径从1.6 nm至5.2 nm（包含135至4079个原子）的孤立纯钛（Ti）纳米粒子。
"主要研究方法": >-
  经典分子动力学（MD）模拟，结合嵌入原子法（EAM）势函数描述原子间相互作用。通过逐步加热和正则系综（NVT）模拟，使用对分布函数（PDF）和原子对分析（PA）技术来表征结构演变。
"研究意义": >-
  理论上，揭示了钛纳米粒子从“团簇-like”多重结构转变到“类块体”熔化的尺寸效应图景，阐明了表面原子在纳米尺度相变中的核心作用。实践上，为基于粉末床熔融的金属增材制造工艺提供了微观机理层面的指导，有助于优化工艺参数，控制制件微观结构。
"研究结论": >-
  1. 钛纳米粒子的熔化行为具有强烈的尺寸依赖性。直径小于2.5 nm的粒子倾向于形成稳定的二十面体（Ih）结构，并经历多重结构转变；较大粒子则呈现类块体熔化，但表面原子会先于内部发生重排。2. 表面原子是所有结构转变的源头，其高移动性驱动了整体的结构演变。3. 对于直径小于3 nm的粒子，经典杜隆-珀蒂定律不再适用。
"对领域的贡献": >-
  构建了钛纳米粒子“尺寸-结构-热稳定性”的定量关系，将极小团簇和块体材料之间的热力学行为联系了起来。揭示了MD模拟中结构转变的原子细节，为理解和预测其他金属纳米粒子的热力学行为提供了研究范式。
"未来研究方向提及": >-
  1. 开发能够同时准确描述HCP和BCC等多相结构的新型钛势函数。2. 将模拟对象从纯金属拓展到更接近实际应用的多组分钛合金体系。3. 研究不同加热/冷却速率对结构转变路径的影响。
"未来研究方向思考": >-
  1. 探索存在表面缺陷（如台阶、空位）或氧化层的纳米粒子的熔化行为。2. 研究多个纳米粒子在接触状态下，受热时的团聚、烧结和熔化耦合过程，以模拟真实的粉末床环境。3. 结合机器学习势函数，实现对大尺寸纳米粒子相变行为的更高精度模拟。4. 发展先进的原位透射电子显微镜（In-situ TEM）实验技术，对模拟结果进行直接验证。
tags:
  - paper
  - type/theory
  - year/2019
  - project/project-5
  - relevance/project-5/weak
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

- **元数据**：Lin Zhang，2019，Advanced Engineering Materials，21(4): 1800531，DOI 10.1002/adem.201800531
- **一句话**：用Zhou EAM势的经典MD模拟系统刻画了直径1.6–5.2 nm（135–4079原子）孤立Ti纳米粒子在逐级加热中的熔化行为，识别出<2.5 nm粒子的Ih几何壳层闭合与多重结构转变、2.5–4 nm粒子的"表面预熔—整体崩溃"机制，并以ΔEav/ΔT→1.5kB判定杜隆-珀蒂定律在约3 nm以下失效。

- **现有wiki双链**：
  - 概念 [[../concepts/density-functional-theory]]（文中引用Agarwal等用该EAM势与DFT状态方程对比验证）
  - 概念 [[../concepts/machine-learning-potential]]（仅在"未来方向"中提及MLIP可提升大尺寸粒子相变精度）
  - 图表 [[../figures/crystal-structures]]（HCP/FCC/Ih/BCC原子堆积与五重孪晶快照）
  - 图表 [[../figures/mathematical-models]]（EAM总势能、电子密度、对势、嵌入能分段公式 Eq.1–7；PDF公式 Eq.9）
  - 年度 [[../write/2019]]
  - 相关论文 [[../../raw/note/Zhang2019a]]

- **新概念/实体建议**：
  - `concepts/molecular-dynamics.md` — 经典MD：积分牛顿方程追踪原子轨迹，本文用1.6 fs步长、NVT、逐级加热
  - `concepts/embedded-atom-method.md` — EAM势：Etot=ΣFi(ρe)+½Σφij(rij)，本文用Zhou等参数化的Ti EAM（re=0.2933872 nm，截断0.656 nm）
  - `concepts/pair-distribution-function.md` — g(R) PDF：g(R)=(1/N²)⟨ΣΣδ(R−|R*ij|)⟩，用峰锐/宽化判别晶态/液态
  - `concepts/common-neighbor-analysis.md` — 对分析/共同邻居分析（PA/CNA）：1421/1422对对应FCC/HCP密堆积，1441/1661对对应BCC
  - `concepts/icosahedral-structure.md` — 二十面体（Ih）：五重对称非晶体学密堆积，小团簇因表面能最低而优先
  - `concepts/surface-premelting.md` — 表面预熔：低配位表面原子先于芯部运动/重排，无序壳层在高温下迅速贯穿整个粒子
  - `concepts/size-dependent-melting.md` — 纳米粒子熔点尺寸效应：<4 nm Tm振荡式上升，>4 nm缓慢收敛到块体值
  - `concepts/dulong-petit-law.md` — 杜隆-珀蒂定律及失效边界：原子热容3kB（势能贡献1.5kB），N<800–900（<约3 nm）时偏离
  - `concepts/five-fold-twinning.md` — 五重孪晶：Ti257在1300 K形成，界面为HCP堆积
  - `concepts/geometric-shell-closure.md` — 几何壳层闭合：Ih团簇的"幻数"稳定性来源
  - `entities/Ti.md` — 钛：α相HCP，块体实验熔点1941 K，EAM预测无缺陷块体熔点2218 K
  - `entities/LAMMPS.md` — MD代码（文中与GULP并列为可处理非周期体系的主流代码）
  - `entities/Moldy.md` — 本文MD代码修改自旧版Moldy（PBC下用大盒子隔离粒子）
  - `figures/thermodynamic-curves.md` — 新图表类型：能量-温度曲线、PDF、Tm-d关系、ΔEav/ΔT-N关系等热分析图

- **关键图表**（raw/figures/Zhang2019a/ 实际存在文件）：
  - ![EAM总势能公式 Eq.1](../../raw/figures/Zhang2019a/eq_1_JKSLE4FW.png)
  - ![广义元素对势 Eq.3](../../raw/figures/Zhang2019a/eq_3_IY4F7YGW.png)
  - ![电子密度函数 Eq.4](../../raw/figures/Zhang2019a/eq_4_LZSYGSBF.png)
  - ![嵌入能分段公式 Eq.5–7](../../raw/figures/Zhang2019a/eq_5_AKZ9ZC4I.png)
  - ![嵌入能分段公式 Eq.6](../../raw/figures/Zhang2019a/eq_6_3NZCI3TL.png)
  - ![嵌入能分段公式 Eq.7](../../raw/figures/Zhang2019a/eq_7_WN3PU9VD.png)
  - ![对分布函数公式 Eq.9](../../raw/figures/Zhang2019a/eq_9_KF8MDN7A.png)
  - ![图1 Ti135/Ti257/Ti895弛豫过程每原子能量随时间步变化](../../raw/figures/Zhang2019a/fig_1_8GSJRYRQ.png)
  - ![图2 1421/1422/1441/1661原子对示意图](../../raw/figures/Zhang2019a/fig_2_34UVRTQI.png)
  - ![图3 小尺寸粒子平均能量-温度曲线](../../raw/figures/Zhang2019a/fig_3_VVXJNDWX.png)
  - ![图4 Ti135/Ti257/Ti895不同温度PDF与原子堆积快照](../../raw/figures/Zhang2019a/fig_4_SK6TQB88.png)
  - ![图5 熔化温度随粒子直径变化（<4 nm振荡，>4 nm收敛）](../../raw/figures/Zhang2019a/fig_5_UJHJUH45.png)
  - ![图6 大尺寸粒子（Ti1099–Ti3455）能量-温度曲线](../../raw/figures/Zhang2019a/fig_6_T7VXXEFK.png)
  - ![图7 六粒子1421/1422原子对数量随温度变化](../../raw/figures/Zhang2019a/fig_7_TQ8EAVTC.png)
  - ![图8 ΔEav/ΔT斜率随原子数N变化（杜隆-珀蒂1.5kB边界）](../../raw/figures/Zhang2019a/fig_8_2H6SNMFM.png)
  - ![图9 Ti1099/Ti2361/Ti3347不同温度原子堆积（表面预熔可视化）](../../raw/figures/Zhang2019a/fig_9_JRFEECJM.png)
  - ![表1 EAM势参数](../../raw/figures/Zhang2019a/tab_1_GBW2JGJ2.png)

- **项目连接**：
  - **project-5 SnTe铁电模拟 — weak**：本文物理对象是金属Ti纳米粒子熔化，与SnTe铁电无直接材料/机理重合；但作为经典MD加热模拟的方法学范本，其计算流程可类比复用：(1) NVT逐级加热协议（50 K起、50 K步长、每温2×10⁶步、速度标定控温、1.6 fs步长、以上一温终态为下一温初态）；(2) 结构诊断三件套——平均势能Eav、对分布函数g(R)、对分析1421/1422/1441/1661——用于区分HCP/FCC/BCC/液态，对应铁电模拟中可用类似的局部有序参数/键对分析追踪结构相变；(3) "二分法"在25 K窗口内定位转变温度（Ti895熔点1260 K即由1250–1300 K区间二分得到）可直接用于铁电居里/相变温度的精确定位；(4) ΔEav/ΔT斜率与杜隆-珀蒂1.5kB对比划定经典热力学适用尺寸（N<800–900偏离），为SnTe纳米粒子有限尺寸效应提供类比判据；(5) "表面预熔→无序壳层→整体崩溃"的图像可类比有限尺寸铁电体中表面退极化场驱动的表面先行失稳。物理差异大，故仅weak。
  - project-1 双光子 / project-2 Mn多铁 / project-3 机械发光NN / project-4 TTF分子计算 / project-6 湿度传感器 / project-7 CDW：无直接项目连接（金属EAM MD熔化主题与分子晶体、多铁、CDW、荧光、湿度传感机制无可复用的物理或数据交集；project-4虽涉及计算但TTF为分子晶体，不用EAM金属势，方法不可直接迁移）。

- **组织与用词**：
  论文采用标准"引言—实验/方法—结果与讨论—结论"IMRaD结构。论证链条为"应用驱动（AM钛粉）→尺度问题（微米→纳米）→方法（EAM MD）→三层结果（小粒子多形转变 / 中粒子表面预熔 / 大粒子类块体）→量化（Tm-d、ΔEav/ΔT-N）→坦诚局限（EAM不能给HCP→BCC）"。方法部分给全EAM势函数形式（Eq.1–7）、电子密度（Eq.2、4）、PDF（Eq.9）和参数表1，可复用性强。结果讨论用"能量+PDF+PA+快照"四重证据交叉印证，避免单一指标判熔化的模糊性。
  值得在wiki叙述中复用的关键词/术语：
  - atom packing / 原子堆积
  - geometric shell closure / 几何壳层闭合
  - multi-structures' transitions / 多结构转变
  - surface premelting / 表面预熔
  - pair analysis (PA) / 对分析（即共同邻居分析CNA）
  - pair distribution function g(R) / 对分布函数
  - icosahedron (Ih) / 二十面体
  - five-fold twins / 五重孪晶
  - bisection algorithm / 二分法（熔点定位）
  - Dulong–Petit limit / 杜隆-珀蒂极限（1.5kB势能斜率）

- **可写入wiki的要点**：
  1. **EAM势函数形式**：Etot=Σ_i Fi(ρe)+½Σ_{i≠j}φij(rij)；电子密度ρe=Σ_j fj(rij)；对势φij为A·exp[−α(rij/re−1)]/(1+(rij/re−κ)²⁰)−B·exp[−β(rij/re−1)]/(1+(rij/re−λ)²⁰)；嵌入能F(ρ)在ρ<ρn（0.85ρe）、ρn≤ρ<ρ0（1.15ρe）、ρ≥ρ0三段分别用三次多项式与Fe[1−ln(ρ/ρs)^η]拼接，保证值和斜率连续。
  2. **Ti EAM参数（Zhou等）**：re=0.2933872 nm，fe=1.863200，ρe=ρs=25.565138，A=8.775431，B=4.680230，A(eV)=0.373601，B(eV)=0.570968，κ=0.5，λ=1.0；截断0.656 nm；预测无缺陷块体Ti熔点2218 K，比实验值1941 K高277 K（14%偏差），作者认为仍可用于固-液堆积变化研究。
  3. **模拟协议**：从块体HCP Ti沿[101̄0]、[12̄10]、[0001]建20.745×20.745×24.894 nm³晶胞，切出1.6–5.2 nm球形碎片共27组（135至4079原子）；50 K起以50 K步长升至1400 K，NVT系综，速度标定每步控温，1.6 fs时间步，每温2×10⁶步；小粒子（Ti135/257/895）取末70 000步、大粒子取末300 000步统计能量；结构分析取统计窗内能量最低那一步的轨迹以消除粒子旋转影响。
  4. **三尺寸区熔化图像**：(a) <2.5 nm（Ti135、Ti257）：低温即从初始HCP弛豫到Ih，加热中经历HCP→Ih→FCC多结构转变，Ti257在1300 K形成五重孪晶（界面HCP）；(b) 2.5–4 nm（如Ti895，熔点1260 K）：芯部保持HCP，表面在450–1250 K宽温区重排，1300 K无序迅速贯穿；(c) >4 nm（Ti1099等6粒，直径3.36–5.03 nm）：类块体表面预熔，Tm随直径缓慢升高并收敛。
  5. **Tm-d关系（图5）**：d<4 nm时Tm随d振荡式快速上升（表面原子比例高且排布逐尺寸不同），d>4 nm斜率变缓趋近块体值；4 nm是"分子型"向"块体型"熔化过渡的特征尺寸。
  6. **对分析指纹**：1421对（两对共有4邻居的键合邻居平行排列）与1422对（两对键合邻居有交点）之和代表HCP/FCC密堆积比例；其中1422为HCP特征、1421在FCC中亦大量存在；1441+1661为BCC特征。Ti1099熔化前1422降、1421升，证明发生HCP→FCC局部转变；所有粒子全程几乎无1441/1661，说明该EAM势不能再现块体Ti的HCP→BCC高温相变。
  7. **杜隆-珀蒂失效边界（图8）**：高温晶体每原子热容3kB，势能贡献1.5kB。N<800（约<3 nm）粒子ΔEav/ΔT远小于1.5甚至为负（因加热中向更低势能的Ih等结构转变）；N≥895后斜率稳定在≈1.5，小偏差来自表面结构差。Ti135取1050–1200 K、Ti257取850–1200 K、其余取300–1200 K计算斜率。
  8. **熔点二分法**：以Ti895为例，在1250–1300 K间：1280 K无序→缩至1250–1280；1265 K熔→再测1258 K仍有序→区间1258–1265；反复二分至1260 K。该流程可直接迁移到其他经典MD相变温度定位。
  9. **孤立粒子实现**：代码基于旧版Moldy（PBC预定），用足够大的中心晶胞（20.7×20.7×24.9 nm³）使中心粒子与26个镜像像胞原子间距超过0.656 nm截断，从而无需改代码即模拟孤立粒子；文中指出GULP、LAMMPS等支持原生非周期模拟。
  10. **作者自陈局限与未来方向**：单一EAM势无法同时描述低温静态构型与高温热力学（HCP→BCC缺失）；需MEAM/多体势、多组分（Ti-6Al-4V）、非平衡极速加热/冷却（AM实际>10⁶ K/s）、多粒子团聚烧结耦合、MLIP提升精度，并呼唤原位TEM对1.6–5.2 nm这一"TEM太大、XRD太小"表征盲区的实验验证。
