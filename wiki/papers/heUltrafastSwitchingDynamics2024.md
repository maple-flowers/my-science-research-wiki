---
citekey: heUltrafastSwitchingDynamics2024
title: "Ultrafast switching dynamics of the ferroelectric order in stacking-engineered ferroelectrics"
title_zh: "堆垛工程铁电体中铁电有序的超快开关动力学"
authors: [Ri He, Bingwen Zhang, Hua Wang, Lei Li, Ping Tang, Gerrit Bauer, Zhicheng Zhong]
year: 2024
journal: "Acta Materialia"
doi: "10.1016/j.actamat.2023.119416"
url: "https://doi.org/10.1016/j.actamat.2023.119416"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/heUltrafastSwitchingDynamics2024]]
projects: [project-1, project-2, project-3, project-4, project-5, project-6, project-7]
concepts: [2D-materials, berry-phase, density-functional-theory, machine-learning-potential, moire-superlattice, polarization-switching, sliding-ferroelectricity, strain-engineering, super-paraelectricity, topological-defects]
entities: [VASP, deep-potential, domain-wall, h-BN]
methods: [berry-phase, dft, mlip]
materials: [deep-potential, domain-wall, h-BN]
figures: [crystal-structures, domain-walls, heterostructures-stacking, vibrational-spectra]
领域基础知识:: >-
  铁电性、范德华材料、二维材料、极化翻转、畴壁动力学
研究背景:: >-
  实验发现堆叠工程铁电体的临界翻转电场远低于理论预测，且扭转莫尔结构表现出异常电学响应，根源在于对其中畴壁的静态和动态特性缺乏原子尺度的理解。
作者的问题意识:: >-
  揭示堆叠工程铁电体中畴壁的原子结构、物理起源及其在外场下的动态行为，以解释宏观实验现象，并探索其实现超快、低能耗器件应用的潜力。
主要研究对象:: >-
  平行堆叠六方氮化硼（h-BN）双层中的一维铁电畴壁（0°、30°、60°、90°四种类型）和扭转莫尔结构。
主要研究方法:: >-
  基于密度泛函理论（DFT）数据训练的深度势能（Deep Potential, DP）机器学习模型，结合大规模分子动力学模拟，以及一维弹性模型的理论分析。
研究意义:: >-
  首次从原子尺度揭示了范德华堆叠铁电体中畴壁的结构和动力学，澄清了困扰领域的实验矛盾，并提出了超顺电态和缺陷钉扎的新见解，为设计下一代超快、低功耗非易失性存储器提供了理论指导。
研究结论:: >-
  畴壁运动是降低翻转场（降两个数量级）和实现皮秒级超快翻转的关键；畴壁宽度由于低翻转势垒与高面内刚度而极宽（10-40nm）；理想扭转莫尔结构表现为超顺电态，其实验上观察到的铁电性可能源于缺陷对畴壁的钉扎。
对领域的贡献:: >-
  1. 系统地分类并揭示了堆叠铁电体中畴壁的极化纹理（布洛赫/奈尔型）与物理机制。2. 定量解释了畴壁运动如何导致超快、低能耗的极化翻转。3. 从原子尺度阐明了莫尔结构的超顺电本质，并提出了缺陷钉扎模型。
未来研究方向提及:: >-
  1. 发展能精确描述长程静电相互作用的机器学习模型。2. 研究衬底对畴壁结构与莫尔电学响应的影响。3. 系统性研究不同种类和浓度的缺陷对畴壁的钉扎效应。
未来研究方向思考:: >-
  1. 探索该模型在其他范德华铁电材料（如TMDs）中的普适性。2. 基于畴壁运动的超快动力学，设计新型器件结构，如畴壁赛道存储器。3. 研究通过应变、电场等多物理场调控畴壁宽度与动力学行为的可能性。
tags:
  - paper
  - type/theory
  - year/2024
  - project/project-1
  - relevance/project-1/medium
  - project/project-2
  - relevance/project-2/core
  - project/project-3
  - relevance/project-3/medium
  - project/project-4
  - relevance/project-4/medium
  - project/project-5
  - relevance/project-5/strong
  - project/project-6
  - relevance/project-6/medium
  - project/project-7
  - relevance/project-7/weak
  - concept/2D-materials
  - concept/berry-phase
  - concept/density-functional-theory
  - concept/machine-learning-potential
  - concept/moire-superlattice
  - concept/polarization-switching
  - concept/sliding-ferroelectricity
  - concept/strain-engineering
  - concept/super-paraelectricity
  - concept/topological-defects
  - entity/VASP
  - entity/deep-potential
  - entity/domain-wall
  - entity/h-BN
  - method/berry-phase
  - method/dft
  - method/mlip
  - material/deep-potential
  - material/domain-wall
  - material/h-BN
  - topic/2d-materials
  - topic/charge-density-wave
  - topic/domain-walls
  - topic/ferroelectricity
  - topic/humidity-sensing
  - topic/ml-interatomic-potential
  - topic/molecular-crystal
  - topic/multiferroics
  - topic/polarization
  - topic/topological-defects
  - topic/two-photon-fluorescence
---

## heUltrafastSwitchingDynamics2024 — 堆垛工程铁电体中铁电有序的超快开关动力学

## 📄 元数据
Ri He, Bingwen Zhang, Hua Wang, Lei Li, Ping Tang, Gerrit Bauer, Zhicheng Zhong et al.，2024，Acta Materialia 262, 119416，DOI: 10.1016/j.actamat.2023.119416

## 💡 一句话
基于DFT数据训练深度势能（DP）机器学习势，对h-BN双层中铁电畴壁进行大规模原子模拟，揭示畴壁运动将临界翻转场降低两个数量级、实现皮秒级翻转，并阐明扭转莫尔结构的超顺电本质。

## 🔗 Wiki 双链
本文涉及且 wiki 中已存在的条目，用双链列出（存在才链）：
  - 概念 [[../concepts/sliding-ferroelectricity]]
  - 概念 [[../concepts/polarization-switching]]
  - 概念 [[../concepts/super-paraelectricity]]
  - 概念 [[../concepts/machine-learning-potential]]
  - 概念 [[../concepts/density-functional-theory]]
  - 概念 [[../concepts/2D-materials]]
  - 概念 [[../concepts/moire-superlattice]]
  - 概念 [[../concepts/berry-phase]]
  - 概念 [[../concepts/strain-engineering]]
  - 概念 [[../concepts/topological-defects]]
  - 实体 [[../entities/h-BN]]
  - 实体 [[../entities/deep-potential]]
  - 实体 [[../entities/VASP]]
  - 实体 [[../entities/domain-wall]]
  - 图表 [[../figures/domain-walls]]
  - 图表 [[../figures/vibrational-spectra]]
  - 图表 [[../figures/crystal-structures]]
  - 图表 [[../figures/heterostructures-stacking]]
  - 图表 [[../figures/heterostructures-stacking-sliding|层间滑移铁电：机制、翻转与动力学]]
  - 年度 [[../write/2024]]
  - 相关论文 **heUltrafastSwitchingDynamics2024**

## 🆕 新概念/实体建议
wiki 中没有、但值得新建的概念或材料实体：
  - `stacking-engineered-ferroelectricity`（堆垛工程铁电性）：通过调控范德华双层的层间堆垛方式（AB/BA）产生可翻转极化的铁电机制，是滑移铁电性的子类，但强调"工程"层面的堆垛设计与器件应用。
  - `domain-wall-texture`（畴壁极化纹理）：描述畴壁内极化矢量旋转方式的概念，如布洛赫型（Bloch，极化在畴壁面内旋转）与奈尔型（Néel，极化在垂直畴壁面内旋转），区别于传统伊辛型畴壁。
  - `flexoelectric-effect`（挠曲电效应）：应变梯度诱导电极化的耦合效应，本文中用于解释非0°畴壁的面外屈曲（buckling）起源。
  - `domain-wall-pinning`（畴壁钉扎）：点缺陷（如氮空位）对畴壁运动的捕获与阻碍效应，是解释理想莫尔超顺电态与实验观测铁电回滞之间差异的关键机制。
  - `concurrent-learning`（并发学习/DP-Gen流程）：一种机器学习势训练策略，通过迭代探索构型空间、自动筛选DFT标注样本，本文用23轮迭代生成11,580个训练构型。

## 📊 关键图表
  - ![图1 h-BN双层铁电性：极化矢量随层间滑移的演化、能量势垒与电荷密度差](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_1_TZK5GGQL.png) → [[../figures/heterostructures-stacking-sliding|层间滑移铁电：机制、翻转与动力学]]
  - ![图2 DP模型与DFT的能量/原子力基准测试（能量误差0.60 meV/atom）](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_2_WP5XMYXN.png) -> [[../figures/mathematical-models|数学模型与物理公式]]
  - ![图3 DP与DFT声子色散对比，验证AB堆垛动力学稳定性](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_3_FPIDI2M5.png) → [[../figures/heterostructures-stacking-sliding|层间滑移铁电：机制、翻转与动力学]]
  - ![图4 50-700 K热稳定性：层间距与极化随温度变化](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_4_DAWZJSBV.png) → [[../figures/heterostructures-stacking-sliding|层间滑移铁电：机制、翻转与动力学]]
  - ![图5 四种畴壁的原子结构与极化分布：0°布洛赫型、90°奈尔型，宽度9.7-40.7 nm](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_5_BK4H4WHC.png) → [[../figures/domain-walls|畴与畴壁结构]]
  - ![图6 300 K下畴壁运动动力学快照：9 ps内两畴壁湮灭实现翻转](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_6_IH4EUPKK.png) → [[../figures/heterostructures-stacking-sliding|层间滑移铁电：机制、翻转与动力学]]
  - ![图7 0.385°扭转莫尔结构的P-E曲线：无回滞，超顺电态](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_7_UDICC663.png) → [[../figures/heterostructures-stacking-sliding|层间滑移铁电：机制、翻转与动力学]]
  - ![图8 氮空位对畴壁的钉扎能垒（约50 meV）](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_8_RY66EXIM.png) → [[../figures/domain-walls|畴与畴壁结构]]

## 🔬 项目连接
  - **project-1 双光子**：无直接项目连接。本文研究范德华双层铁电畴壁动力学，与双光子吸收/非线性光学无机制或方法交集。
  - **project-2 Mn多铁**：弱参考价值。论文引言提及畴壁影响多铁现象（引用[15,16]），但核心材料为h-BN而非Mn基多铁体；畴壁分类（布洛赫/奈尔型）与一维弹性模型的物理图像可作为多铁材料畴壁研究的类比参考，但不涉及Mn体系的具体机制。
  - **project-3 机械发光NN**：无直接项目连接。本文无机械发光或神经网络用于发光性质预测的内容。
  - **project-4 TTF分子计算**：中等方法参考价值。本文的DP-Gen并发学习流程（DFT标注→DPMD探索→模型偏差筛选→迭代训练）和DeePMD-kit大规模MD模拟方案，为TTF等分子晶体的大尺度原子模拟提供了可复用的机器学习势构建范式；h-BN与TTF材料体系虽不同，但"DFT精度+大规模动力学"的计算流程具有方法学迁移价值。
  - **project-5 SnTe铁电模拟**：强参考价值。本文与SnTe铁电模拟高度相关：(1) 均使用Berry相位法计算自发极化；(2) DP机器学习势实现大尺度铁电畴壁动力学模拟的方案可直接借鉴；(3) 畴壁运动降低临界翻转场两个数量级的机制、朗道-金兹堡-德文希尔（LGD）自由能唯象分析、一维弹性模型w∝√(λ/Δ)对畴壁宽度的预测，均可为SnTe的畴壁与翻转动力学研究提供理论框架；(4) 缺陷钉扎（氮空位~50 meV）的研究思路可类比SnTe中的缺陷工程。
  - **project-6 湿度传感器**：无直接项目连接。
  - **project-7 CDW**：弱参考价值。畴壁作为拓扑缺陷的类孤子（soliton-like）运动、临界驱动力与速度的定量关系，与CDW中相移孤子的动力学在物理图像上有可类比之处；但本文研究的是铁电极化畴壁而非电荷密度波畴壁，机制不同，仅提供拓扑缺陷动力学的方法论参考。

## 🔗 项目双链
- 项目 [[../projects/project-1-two-photon|项目一：双光固化和双光发光]]
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]
- 项目 [[../projects/project-3-mechanoluminescence-nn|项目三：应力发光神经网络]]
- 项目 [[../projects/project-4-ttf-molecular-calc|项目四：lsl老师的ttf分子计算]]
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]
- 项目 [[../projects/project-6-humidity-sensor|项目六：小花闻的电压湿度传感器]]
- 项目 [[../projects/project-7-cdw-charge-density-wave|项目七：CDW电荷密度波]]

## 📝 组织与用词
文章遵循"提出问题→构建方法→静态结构→动态行为→特殊结构（莫尔）→总结"的计算物理研究范式。先以领域两大谜题（实验翻转场偏低、莫尔回线变窄）为引子，将答案锁定在畴壁；再展示DP模型的构建与精度验证；随后从静态（四种畴壁的原子结构、宽度、一维弹性模型）到动态（畴壁运动、临界场、速度、翻转时间）层层推进；最后将尺度拓展至莫尔超晶格，提出超顺电态与缺陷钉扎机制。论证以模拟数据为核心，辅以解析模型（一维弹性模型、LGD唯象分析）进行定量解释。值得复用的关键词/术语：
  - 堆垛工程铁电性（stacking-engineered ferroelectricity）
  - 滑移铁电性 [[../concepts/sliding-ferroelectricity|滑移铁电性]]（sliding ferroelectricity）
  - 畴壁纹理（domain-wall texture）：布洛赫型/奈尔型（Bloch-type/Néel-type）
  - 超顺电态（super-paraelectric state）
  - 深度势能（deep potential, DP）/ 并发学习（concurrent learning, DP-Gen）
  - 一维弹性模型（one-dimensional elastic model）：w = u₀/2·√(λ₁ᴰ/Δ)
  - 畴壁钉扎/去钉扎（domain-wall pinning/depinning）
  - 类孤子运动（soliton-like motion）

## ✏️ 可写入 Wiki 的要点
  1. h-BN双层AB/BA堆垛产生面外极化Pz=1.46×10⁻¹² C/m（[[../concepts/berry-phase|Berry相位]]法，optB86b-vdW泛函），极化源于[[../concepts/interlayer-charge-transfer|层间[[../concepts/charge-transfer|电荷转移]]]]而非离子位移；鞍点（SP）构型为纯面内极化1.38×10⁻¹² C/m，极化模长在翻转路径上基本保持不变。
  2. DP模型通过DP-Gen[[../concepts/concurrent-learning|并发学习]]流程训练23轮，生成11,580个构型；能量误差0.60 meV/atom，面内力误差0.051 eV/Å，面外力误差0.017 eV/Å；截断半径Rc=6 Å，嵌入网络(25,50,100)，拟合网络(240,240,240)，训练180万步。
  3. 四种一维畴壁按DW与滑移矢量夹角φ分类：0°（布洛赫型，平面，最稳定）、30°、60°、90°（奈尔型，面外屈曲最显著）；畴壁宽度随φ单调增加：9.7、17.6、32.1、40.7 nm，比钙钛矿铁电体（~0.7 nm）大一个数量级。
  4. 一维弹性模型给出畴壁宽度w = u₀/2·√(λ₁ᴰ/Δ)，其中λ₁ᴰ为面内拉梅力系数，Δ为单位长度[[../concepts/switching-barrier|翻转势垒]]；范德华材料超低Δ与极高面内刚度λ₁ᴰ共同导致超宽畴壁；λ₁ᴰ可通过应变/电场调控，是铁电[[../concepts/domain-wall-engineering|畴壁工程]]的新自由度（类比磁学中[[../concepts/exchange-interaction|交换作用]]）。
  5. 单畴直接翻转临界场：100 K时Fs=3.8×10⁻³ eV/Å（Ev≈1.41 V/nm），300 K时3.5×10⁻³ eV/Å（~1.32 V/nm），对热涨落不敏感；而通过0°[[../concepts/domain-wall-motion|畴壁运动]]翻转的临界Fs仅7×10⁻⁵ eV/Å（Ev=0.026 V/nm），降低约两个数量级；90°畴壁临界Fs=3×10⁻⁴ eV/Å（Ev=0.11 V/nm）。
  6. 300 K下施加Fs=5×10⁻⁴ eV/Å（Ev=0.18 V/nm）时，两个0°畴壁以~6000 m/s速度相向运动，9 ps内湮灭；100 nm直径器件翻转时间约15 ps，预示超快低功耗非易失存储。
  7. 垂直电场Ev与横向剪切力Fs的关系为Fs=Ev·Z*₁₃，Berry相位计算给出Z*₁₃^top=0.027、Z*₁₃^bottom=−0.027，比BaTiO₃小两个数量级；LGD唯象分析表明梯度能系数Gij增大→畴壁更宽→速度更快→临界场更低（临界场与畴壁宽度成反比）。
  8. 0.385°扭转[[../concepts/moire-superlattice|莫尔[[../concepts/superlattice|超晶格]]]]（355,012原子）弛豫后，AB/BA畴扩张为三角形、高能AA畴收缩为点；垂直电场下BA畴由三角形变为类六边形，Pz在Ev=0.026 V/nm即快速饱和至1.32×10⁻¹² C/m，撤场后恢复，P-E曲线无回滞——本征态为超顺电体而非铁电体。
  9. 氮空位（VN）对畴壁形成约50 meV的捕获势阱，少量缺陷即可钉扎畴壁，阻止AB/BA畴尺寸在零场下平衡，从而产生[[../concepts/remanent-polarization|剩余极化]]与类铁电回滞——这为莫尔结构实验中观测到的铁电响应提供了缺陷钉扎机制解释。
  10. 热稳定性：50-700 K范围内单畴结构保持完整，700 K时极化仅从1.46降至1.14×10⁻¹² C/m（因层间距热膨胀增大），证实极高[[../concepts/curie-temperature|居里温度]]；面内化学键刚度使极化几乎不受热涨落影响。
