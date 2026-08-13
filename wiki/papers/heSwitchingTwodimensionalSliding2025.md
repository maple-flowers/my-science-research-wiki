---
citekey: heSwitchingTwodimensionalSliding2025
title: "Switching Two-Dimensional Sliding Ferroelectrics by Mechanical Bending"
title_zh: "机械弯曲切换二维滑动铁电体"
authors: [Ri He, Hua Wang, Fenglin Deng, Yuxiang Gao, Bingwen Zhang, Yubai Shi, Run-Wei Li, Zhicheng Zhong]
year: 2025
journal: "Physical Review Letters"
doi: "10.1103/PhysRevLett.134.076101"
url: "https://doi.org/10.1103/PhysRevLett.134.076101"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/heSwitchingTwodimensionalSliding2025]]
projects: [project-5]
concepts: [2D-materials, berry-phase, ferroelasticity, machine-learning-potential, polarization-switching, sliding-ferroelectricity, strain-engineering, topological-defects]
entities: [In2Se3, TMDs, VASP, WTe2, Wannier90, domain-wall, h-BN]
methods: [berry-phase, dft, mlip, neb]
materials: [In2Se3, TMDs, WTe2, domain-wall, h-BN]
figures: [domain-walls-structures, heterostructures-stacking, mathematical-models-elasticity-strain]
领域基础知识:: >-
  二维范德华（vdW）材料层内为强共价键、层间为弱范德华作用，层间相对平移所产生的"堆垛序"是调控电学、光学、磁学和拓扑性质的关键自由度。当非极性单层以不对称方式堆叠（如 h-BN 的 AB 堆叠）时，层间电荷转移会产生垂直层面的自发极化，极化方向可通过层间微小滑移反转，即"滑动铁电性"，已在双层 WTe2、h-BN、3R-MoS2、MoTe2 中实验观测到。滑动铁电的翻转由软"滑动声子"模触发，相比传统离子位移型铁电体具有更快、更耐疲劳的潜力。二维材料还具有极低的弯曲刚度和高断裂强度，可产生比氧化物异质外延大几个数量级的应变梯度。
研究背景:: >-
  改变 vdW 双层的堆垛顺序可诱导铁磁/反铁磁耦合、外尔拓扑态、谷电子学、拓扑输运和超导等丰富物性，但在不同堆垛序之间切换需要克服层间滑动势垒，实际操控困难。滑动铁电体中 AB 与 BA 两种反向极化堆垛可通过电场或光场切换，但这些手段对非极性或金属体系并不总是适用。与此同时，二维材料优异的柔韧性使其能承受巨大应变梯度，机械弯曲因此被视为一种有潜力的普适调控手段，但弯曲如何具体改变堆垛序、是否能实现铁电翻转此前尚不清楚。
作者的问题意识:: >-
  作者关注的核心问题是：能否不依赖电场或光场，而用一种直接、普适的机械方式来操控二维材料的层间堆垛序。他们注意到 vdW 材料层间滑动势垒低、面内刚度大，弯曲变形会不可避免地驱动层间滑移，因此假设机械弯曲可以成为切换堆垛序及其关联物性的通用途径。论文进一步追问：弯曲后双层是否还保持理想弧形、形成的结构与铁电畴壁是何关系、其极化翻转机制与传统挠曲电效应有何本质区别，以及该机制是否对铁电体和非铁电体均成立。
主要研究对象:: >-
  论文以滑动铁电双层 h-BN 为主模型体系，系统研究其在机械弯曲下的结构、能量景观和电极化变化；并以另一种滑动铁电半导体 3R-MoS2 验证可推广性，以非极性、空间反演对称的双层石墨烯验证机制不依赖于铁电性。为从能量学上定量揭示扭结成因，作者还构建了 h-BN 和 3R-MoS2 的扶手椅型双壁纳米管模型，通过改变直径精确控制曲率和弯曲能。
主要研究方法:: >-
  作者采用基于机器学习势（DeePMD-kit/DP-GEN 并发学习训练，以 VASP、vdW-DF 泛函的 DFT 数据为参考）的分子动力学模拟，兼顾量子力学精度与大尺度经典模拟速度。模拟流程为：从稳定的 AB 单畴双层出发，沿 x 轴人为施加初始弯曲角 θ 形成圆弧（弯曲区特征长度 12.3 nm，假设层间距和面内晶格不变，故末端滑移量 Δd=θ·D），再固定部分区域做全原子弛豫得到优化角 θ₀。除直接弯曲外还用周期性正弦波纹变形考察稳定性，并在 1100 K 高温下检验扭结的热力学稳健性。极化纹理与畴壁类型通过第一性原理极化计算分析，层间滑动路径的堆垛能景观和临界滑移距离结合 CI-NEB 等方法确定；最后以双壁纳米管解析模型（公式 1–3）定量比较 E_circle 与 E_kink，给出临界直径判据。
研究意义:: >-
  本工作提出了一种区别于电场、光场的机械弯曲调化范式，为动态操控二维材料堆垛序及关联的光学、拓扑、铁电和磁学性质提供了通用手段。在滑动铁电体中，弯曲诱导的扭结本身就是铁电拓扑畴壁，可在无显著离子垂直位移的情况下反转面外极化，这为低功耗、超高密度、抗疲劳的机械写入存储器件和纳米机电（NEMS）开关提供了新思路。该机制原则上适用于从绝缘体到金属、从铁电到非铁电的广泛 vdW 层状材料，并把弯曲这一力学自由度与"滑移电子学"（slidetronics）直接连接起来。
研究结论:: >-
  机械弯曲不会使二维双层形成平滑圆弧，而是产生尖锐、不可逆的 31° 和 57° 扭结（h-BN）；θ₀ 随初始角 θ 呈三个离散平台：θ<12° 恢复平面、12°<θ<62° 形成 31° 单扭结、θ>62° 形成 31°+57° 双扭结，临界角 12° 和 62° 分别对应滑移到达 SP（Δd=0.71 Å）和 AA（Δd=2.84 Å）堆垛。扭结源于弯曲弹性能与层间 vdW 堆垛能的竞争：当弯曲迫使局部进入不稳定的 SP/AA 堆垛时，系统以增加弯曲能为代价弛豫回稳定的 AB/BA 堆垛。31° 扭结（SP 核心）为 Néel 型畴壁，极化在面内平滑旋转；57° 扭结（AA 核心）为 Ising 型畴壁，极化在中心降为零后反向，二者均可反转面外极化。这种由整体层间滑移驱动的"类挠曲电效应"不同于 In2Se3、CuInP2S6 中由应变梯度导致离子垂直位移的传统挠曲电效应；扭结在 3R-MoS2（扭结角约 17.5°、34°）和非极性双层石墨烯中同样存在，并在 1100 K 下稳定，双壁纳米管解析模型给出 h-BN 和 3R-MoS2 的临界直径分别约 2.8 nm 和 9.1 nm。
对领域的贡献:: >-
  论文首次从理论上预测了弯曲二维双层中不可逆扭结的形成，并建立了"弯曲—层间滑移—扭结—畴壁/物性翻转"的完整物理图像。它揭示扭结是弯曲能与层间 vdW 堆垛能竞争的必然结果，并用双壁纳米管解析模型定量给出临界直径判据，深化了对二维材料力学—堆垛序耦合的理解。作者将弯曲诱导的极化翻转明确区别于传统挠曲电效应，提出"类挠曲电效应"概念，并指出扭结在晶体学上可视为部分位错线、在无面内应变下具有极高有效应变梯度。更重要的是，该机制被证明不依赖铁电性、原则上适用于所有二维层状材料，从而把机械弯曲确立为滑移电子学中一种全新的、普适的物性调控手段。
未来研究方向提及:: >-
  作者明确提出若干后续方向：一是实验验证，建议用楔形针尖对悬空双层带做纳米压痕并同步电学测量，以卸载后扭结的持续存在作为层间滑移和铁电翻转的直接证据，并结合 SEM、PFM 或 STEM 原位观测；二是把弯曲诱导层间滑移推广为更广泛的"滑动挠曲响应"家族，包括滑动挠曲磁（sliding flexomagnetic）、滑动挠曲光伏（sliding flexophotovoltaic）和滑动挠曲谷电子（sliding flexovalleytronic）等效应；三是探索基于该机制的力学开关、力学传感器和超高密度存储器等器件应用；四是研究弯曲加载—卸载过程中的动力学行为，如扭结成核与传播、畴壁移动速度和钉扎效应等。
未来研究方向思考:: >-
  论文基于洁净、无缺陷的悬空双层做准静态"先弯曲后弛豫"模拟，实际体系中的衬底、吸附物、空位和晶界可能钉扎层间滑移、改变扭结形态，动态加载速率与弯曲几何（三点弯、四点弯等）也可能引入路径依赖，这些都需进一步研究。由于扭结被描述为不可逆，其形成是否伴随能量耗散、能否通过反向弯曲或电场实现可逆擦写，对可擦写存储至关重要。真实材料中传统挠曲电与本文"滑动挠曲电"可能共存，如何设计实验定量解耦两种贡献是关键挑战。此外，扭结/畴壁本身高度局域，其电子学性质（如是否形成一维导电或磁性通道）、在多层与异质结中的协同滑移模式，以及将曲率场与各类滑动挠曲响应以张量形式统一起来的唯象理论，都是值得深入的方向。
tags:
  - paper
  - type/theory
  - year/2025
  - project/project-5
  - relevance/project-5/medium
  - concept/2D-materials
  - concept/berry-phase
  - concept/ferroelasticity
  - concept/machine-learning-potential
  - concept/polarization-switching
  - concept/sliding-ferroelectricity
  - concept/strain-engineering
  - concept/topological-defects
  - entity/In2Se3
  - entity/TMDs
  - entity/VASP
  - entity/WTe2
  - entity/Wannier90
  - entity/domain-wall
  - entity/h-BN
  - method/berry-phase
  - method/dft
  - method/mlip
  - method/neb
  - material/In2Se3
  - material/TMDs
  - material/WTe2
  - material/domain-wall
  - material/h-BN
  - topic/2d-materials
  - topic/domain-walls
  - topic/ferroelectricity
  - topic/ml-interatomic-potential
  - topic/polarization
  - topic/topological-defects
---

## heSwitchingTwodimensionalSliding2025 — 机械弯曲切换二维滑动铁电体

## 📄 元数据
Ri He, Hua Wang, Fenglin Deng, Yuxiang Gao, Bingwen Zhang, Yubai Shi, Run-Wei Li, Zhicheng Zhong et al.，2025，Physical Review Letters 134, 076101，DOI 10.1103/PhysRevLett.134.076101
## 💡 一句话
用机器学习势模拟发现，机械弯曲会在二维双层（h-BN、3R-MoS₂、双层石墨烯）中诱导不可逆"扭结"，扭结即铁电拓扑畴壁，可反转滑动铁电极化，其机制是弯曲能与层间堆垛能的竞争，区别于传统挠曲电效应。
## 🔗 Wiki 双链
  - 概念 [[../concepts/sliding-ferroelectricity]]
  - 概念 [[../concepts/polarization-switching]]
  - 概念 [[../concepts/2D-materials]]
  - 概念 [[../concepts/machine-learning-potential]]
  - 概念 [[../concepts/strain-engineering]]
  - 概念 [[../concepts/ferroelasticity]]
  - 概念 [[../concepts/topological-defects]]
  - 概念 [[../concepts/berry-phase]]（文中提及Berry curvature memory/stacking transition相关引用）
  - 概念 [[../concepts/flexoelectric-effect|挠曲电效应]]（本文"类挠曲电效应"的经典对照）
  - 概念 [[../concepts/bending-induced-kink|弯曲诱导扭结]]（本文核心新结构概念）
  - 概念 [[../concepts/slidetronics|滑移电子学 slidetronics]]
  - 概念 [[../concepts/sliding-phonon-mode|滑动声子模]]（滑动铁电翻转的软模基础）
  - 概念 [[../entities/bilayer-graphene|双层石墨烯]]（非极性对照体系）
  - 概念 [[../entities/MoS2|二硫化钼 MoS₂]]（3R-MoS₂滑动铁电体系）
  - 实体 [[../entities/h-BN]]
  - 实体 [[../entities/TMDs]]（3R-MoS₂）
  - 实体 [[../entities/domain-wall]]
  - 实体 [[../entities/In2Se3]]（文中作为传统挠曲电对照）
  - 实体 [[../entities/WTe2]]（背景中提及滑动铁电实验体系）
  - 实体 [[../entities/VASP]]、[[../entities/Wannier90]]（极化计算方法背景）
  - 实体 [[../entities/bilayer-graphene|双层石墨烯]]（非极性二维体系，验证机制不依赖铁电性）
  - 图表 [[../figures/domain-walls]]
  - 图表 [[../figures/heterostructures-stacking]]
  - 图表 [[../figures/heterostructures-stacking-sliding|层间滑移铁电：机制、翻转与动力学]]
  - 图表 [[../figures/mathematical-models]]（能量竞争模型公式1-3）
  - 年度 [[../write/2025]]
  - 相关论文 **heSwitchingTwodimensionalSliding2025**
## 📊 关键图表
  - ![图1 双层h-BN在不同初始弯曲角θ下弛豫后的原子结构：θ<12°恢复平面，12°<θ<62°形成31°单扭结，θ>62°形成31°+57°双扭结](../../raw/figures/heSwitchingTwodimensionalSliding2025/fig_1_HAQT3EAV.png) → [[../figures/heterostructures-stacking|异质结与堆叠]]
  - **图示描述**：图1以侧视原子结构展示双层 h-BN 从平面 AB 堆叠出发，沿 x 轴人为施加初始弯曲角 θ 后再做全原子弛豫得到的最终构型；(a) 为理想圆弧示意，(b)–(d) 分别对应小、中、大三种 θ 下弛豫后的平面、单扭结和双扭结形态。
  - **关键特征**：弯曲区特征长度 12.3 nm，层间滑移量满足几何关系 Δd = θ·D（D 为层间距 3.25 Å）；θ < 12° 时回弹为平面（θ₀ = 0°），12° < θ < 62° 时形成角度固定的 31° 单扭结，θ > 62° 时出现 31° + 57° 紧邻双扭结；扭结卸载后不回弹，属于不可逆塑性重构，区别于常规二维薄片的弹性弯曲。
  - **结论/意义**：该图给出"弯曲不形成平滑圆弧而形成离散扭结"这一核心现象的直接原子证据，奠定全文能量竞争解释的结构基础。
  - ![图2 (a)层间滑动路径上的堆垛能景观（AB/BA为极小值，SP/AA为极大值）；(b)弛豫后角度θ₀随初始θ的阶梯状关系，临界角12°和62°](../../raw/figures/heSwitchingTwodimensionalSliding2025/fig_2_ZQQMMCBF.png) → [[../figures/heterostructures-stacking|异质结与堆叠]]
  - **图示描述**：图2把结构现象与能量景观对应起来：(a) 横轴为弯曲驱动的层间滑移路径、纵轴为堆垛能，绘出 AB/BA 极小值与 SP/AA 极大值构成的双势阱；(b) 横轴为初始弯曲角 θ、纵轴为弛豫后角度 θ₀，显示三段离散平台。
  - **关键特征**：AB、BA 为全局能量极小（稳定极化堆垛），SP（鞍点）和 AA 为能量极大（不稳定堆垛）；到达 SP 对应 Δd = 0.71 Å、θ = 12°，到达 AA 对应 Δd = 2.84 Å、θ = 62°；θ₀–θ 曲线在 12° 和 62° 处发生跳变，把弯曲响应切成 0°、31°、31°+57° 三个离散态。
  - **结论/意义**：该图从能量学上解释了扭结角度为何固定、临界角为何是 12° 和 62°，把几何滑移量与堆垛能垒直接定量对应起来。
  - ![图3 弯曲h-BN中的极化纹理：(a)31°扭结为Néel型畴壁（SP堆垛核心，极化面内旋转），(b)57°扭结为Ising型畴壁（AA堆垛核心，极化过零反向），(c)AB→SP→BA→AA→AB循环切换示意](../../raw/figures/heSwitchingTwodimensionalSliding2025/fig_3_H6HN8MAN.png) → [[../figures/domain-walls-structures|畴结构与畴壁]]
  - **图示描述**：图3在扭结原子结构上叠加极化矢量箭头，(a)(b) 分别给出 31° 和 57° 扭结的侧视/顶视图及极化分布，(c) 为 AB→SP→BA→AA→AB 循环堆垛切换的概念示意。
  - **关键特征**：31° 扭结以 SP 堆垛为核心，构成 Néel 型畴壁——极化大小基本不变、方向在面内平滑旋转 180°，畴壁中心极化完全位于面内；57° 扭结以 AA 堆垛为核心，构成 Ising 型畴壁——极化在中心降为零后再反向长出；两类畴壁均可把面外极化从向上翻为向下，且几乎不伴随离子垂直位移。
  - **结论/意义**：该图证明弯曲诱导扭结在晶体学上即铁电拓扑畴壁，把"机械弯曲—层间滑移—极化翻转"串成完整机制，并明确区别于由应变梯度驱动离子位移的传统挠曲电效应。
  - ![图4 h-BN和3R-MoS₂双壁纳米管形成能随直径变化及解析模型ΔE=E_circle−E_kink，预测临界直径（h-BN约2.8 nm，3R-MoS₂约9.1 nm）](../../raw/figures/heSwitchingTwodimensionalSliding2025/fig_4_J9YU9FTH.png) → [[../figures/mathematical-models-elasticity-strain|应变、弹性与力学模型]]
  - **图示描述**：图4以扶手椅型双壁纳米管为可控模型，(a)(b) 分别绘出 h-BN 和 3R-MoS₂ 纳米管在弛豫前（理想圆形）与弛豫后（出现扭结）的形成能随直径变化，(c) 给出解析模型中 ΔE = E_circle − E_kink 随直径的变化。
  - **关键特征**：当直径超过临界值后，扭结纳米管形成能低于圆形纳米管，扭结在热力学上更稳定；解析模型预测 h-BN 临界直径约 2.8 nm、3R-MoS₂ 约 9.1 nm，与深度势能模拟的 ~1.8 nm 和 ~9.4 nm 高度一致；3R-MoS₂ 扭结角约 17.5° 和 34°，约为 h-BN 的一半，原因是其层间距更大（6.14 Å vs 3.25 Å），而 θ ∝ Δd/D。
  - **结论/意义**：该图把扭结成因定量归结为弯曲弹性能与层间 vdW 堆垛能的竞争，并证明机制可推广到其他 vdW 双层，为临界尺寸设计提供了解析判据。
  - 公式（eq_1–eq_3，图片见 raw/figures/heSwitchingTwodimensionalSliding2025/）：
  - **图示描述**：三个公式构成双壁纳米管能量竞争的解析模型；E = E_vdW + E_bending 为总形成能，E_circle 为沿圆周积分局域堆垛能密度再加弯曲项的理想圆形管能量，E_kink 为扭结管能量（含过渡堆垛贡献、扭结曲率项和稳定堆垛基底项）。
  - **关键特征**：E_circle 中 2πr∫u[ψ(θ)]dθ 项随直径线性积累 vdW 失配能，而 2πD_m/r 弯曲项随直径增大而衰减；E_kink 中扭结曲率 K 由过渡态与稳态堆垛能差决定；比较 ΔE = E_circle − E_kink 的正负即可判断扭结是否热力学有利，模型参数均取自 DFT 计算。
  - **结论/意义**：这组公式为图4的临界直径提供了解析来源，说明大直径下 vdW 堆垛能压倒弯曲能、扭结必然出现，是全文机制的数学概括。
