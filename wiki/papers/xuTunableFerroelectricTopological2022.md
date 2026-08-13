---
citekey: xuTunableFerroelectricTopological2022
title: "Tunable ferroelectric topological defects on 2D topological surfaces: strain engineering skyrmion-like polar structures in 2D materials"
authors: [Bo Xu, Zhanpeng Gong, Jingran Liu, Yunfei Hong, Yang Yang, Lou Li, et al.]
year: 2022
journal: "arXiv preprint"
doi: "10.48550/ARXIV.2204.05129"
url: "https://doi.org/10.48550/ARXIV.2204.05129"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/xuTunableFerroelectricTopological2022]]
projects: [project-5]
concepts: [2d-materials, strain-engineering, topological-defects, berry-phase, density-functional-theory, machine-learning-potential, polarization-switching, ferroelasticity, ferroelectric-topological-defects, soft-mode, paraelectric-ferroelectric-transition, polar-vortex, antivortex, flux-closure, polarization-phase-diagram, giant-piezoelectricity, multiscale-simulation, landau-double-well, electron-localization-function]
entities: [VASP, PbTe, domain-wall, deep-potential, PbS, PbSe, LAMMPS, DeepMD-kit, PBE-functional]
methods: [dft, dft-pp, pbe, berry-phase, phonon-spectrum, deepmd, mlip, md, lammps, fem, soft-mode-analysis, elf, piezoelectric-coefficient, indentation-simulation]
materials: [PbS, PbSe, PbTe, 2D-PbX]
figures: []
领域基础知识:: >-
  铁电拓扑缺陷（如斯格明子、涡旋）是下一代高密度非易失性存储器的潜在信息载体，因其具有拓扑保护性且尺寸可至纳米级。二维（2D）材料，特别是二维铁电体，因其原子级厚度和优异柔性，为突破传统钙钛矿氧化物在此领域的应用瓶颈提供了新平台。应变工程是调控二维材料物性的有效手段。第四族单硫族化合物（Group-IV Monochalcogenides）是一类重要的二维铁电材料，其结构与性质对应变敏感。顺电相（Paraelectric Phase）与铁电相（Ferroelectric Phase）是两种不同的极化状态，前者无自发极化，后者具有可被电场翻转的自发极化。第一性原理计算（DFT）、分子动力学模拟（MD）和有限元方法（FEM）是材料科学中多尺度模拟的常用方法。
研究背景:: >-
  已发现的极性拓扑结构（如涡旋、斯格明子）几乎仅限于钙钛矿氧化物超晶格薄膜，其制备复杂且难以实现高度集成。二维（2D）材料的兴起为解决此问题提供了机遇，但其本征的原子级厚度和柔性也带来了新挑战：如何在二维体系中诱导并调控复杂的极性拓扑构图尚属空白。目前已发现多种二维铁电材料，但极少数报道存在极性拓扑结构。PbX（X=S, Se, Te）的基态为高度对称的顺电相，这与传统铁电体不同，暗示其晶格可能对应变有特殊响应。
作者的问题意识:: >-
  能否利用应变工程，在高度柔性且基态为顺电相的二维材料中，通过设计非均匀应变场，诱导出可调控、可逆的类斯格明子铁电拓扑缺陷结构？这一策略是否能打破极性拓扑态仅存在于钙钛矿体系的限制，为未来纳米电子器件开辟新路径？
主要研究对象:: >-
  二维（2D）铅硫族化合物单层材料，即PbX (X=S, Se, Te)，特别是PbTe。研究聚焦于其基态顺电相（PE，空间群Cmcm）在机械应变下向铁电相（FE，空间群Pnma）的转变，以及由此产生的各种极化拓扑结构。
主要研究方法:: >-
  采用多尺度计算模拟框架。首先，利用基于密度泛函理论（DFT）的第一性原理计算，揭示应变诱导顺电-铁电相变的微观机制，并建立极化-应变相图。其次，基于DFT数据训练深度学习势函数（DeepMD），进而进行大规模分子动力学（MD）模拟，再现纳米压痕过程并验证涡旋态的产生。最后，采用有限元方法（FEM），结合DFT计算的相图和力学参数，在宏观器件尺度上设计非均匀应变场，预测并设计多种极性拓扑结构。
研究意义:: >-
  理论层面，该研究首次证明了极性拓扑结构并非钙钛矿氧化物所独有，可在二维范德华材料中实现，拓展了极性拓扑物理的认知边界。同时，它建立了“应变场设计-相变控制-拓扑图案编写”的新范式，揭示了力-电-拓扑耦合的新机制。实践层面，为开发基于二维材料的超薄、柔性、高密度、可擦写的拓扑电子学器件（如存储器、传感器）提供了坚实的理论依据与清晰的设计路线图。
研究结论:: >-
  二维PbX材料的基态是顺电相。施加超过临界值的单轴或剪切应变可诱导其发生可逆的顺电-铁电相变，该过程由声子软模驱动，并伴随巨压电效应。通过建立极化-应变相图，可实现对极化态的精确控制。分子动力学模拟证实，机械压痕产生的非均匀应变场能在薄膜中形成涡旋极性拓扑结构。有限元模拟进一步表明，通过设计基底孔洞形状和薄膜取向，可产生反涡旋、通量闭合等多种可调谐的拓扑极性图案。应变工程是实现二维材料中可设计、可逆极性拓扑态的有效策略。
对领域的贡献:: >-
  1. 开辟了“二维材料中的应变驱动拓扑极性态”这一新研究方向。2. 提供了一套完整的多尺度计算方法论，从第一性原理到机器学习再到有限元，为研究力-电耦合下的复杂结构演化提供了范例。3. 发现并系统解释了二维PbX中应变诱导的顺电-铁电相变现象及其物理机制。4. 绘制了首个应变-极化相图，为后续实验和理论研究提供了“设计蓝图”。5. 预测了多种可通过简单力学设计实现的拓扑结构，展示了该技术的巨大应用潜力。
未来研究方向提及:: >-
  1. 将此应变工程策略扩展到其他本征具有铁电性的二维材料。2. 设计更复杂的基底图案（如多边形、扇形孔洞），以产生更多样化的拓扑结构，如斯格明子晶格。3. 探索这些人工拓扑结构在外电场、光场等激励下的动态响应和新奇物性。4. 在实验上，需要发展先进的纳米应变操控和皮米级极化表征技术来验证 these 理论预测。
未来研究方向思考:: >-
  1. **动力学过程研究**：采用相场模拟等方法，深入研究在非均匀应变场加载过程中，相变、畴壁运动与拓扑结构形成的动力学路径，这对于精确控制最终结构至关重要。2. **室温稳定性与热效应**：系统研究温度对这些拓扑态的热稳定性和形成过程的影响，评估其在实际工作温度下的可行性。3. **电学/光学读出方案设计**：探索如何将不同的拓扑态（涡旋、反涡旋等）映射为可识别的电学信号（如隧穿电阻、非线性霍尔效应）或光学信号（如二次谐波产生），这是实现存储功能的核心。4. **缺陷工程与钉扎效应**：研究二维材料中不可避免的空位、晶界等缺陷对拓扑态的成核、移动和钉扎作用，为通过缺陷工程稳定和调控拓扑态提供思路。5. **与现有硅基技术兼容性**：探索在硅基衬底上或与二维半导体（如MoS2）异质集成的条件下，实现应变加载与拓扑态调控的可能性，为该技术未来融入CMOS工艺打下基础。
tags:
  - paper
  - type/theory
  - year/2022
  - project/project-5
  - relevance/project-5/strong
  - concept/2d-materials
  - concept/strain-engineering
  - concept/topological-defects
  - concept/berry-phase
  - concept/density-functional-theory
  - concept/machine-learning-potential
  - concept/polarization-switching
  - concept/ferroelasticity
  - concept/ferroelectric-topological-defects
  - concept/soft-mode
  - concept/paraelectric-ferroelectric-transition
  - concept/polar-vortex
  - concept/antivortex
  - concept/flux-closure
  - concept/polarization-phase-diagram
  - concept/giant-piezoelectricity
  - concept/multiscale-simulation
  - concept/landau-double-well
  - concept/electron-localization-function
  - entity/VASP
  - entity/PbTe
  - entity/domain-wall
  - entity/deep-potential
  - entity/PbS
  - entity/PbSe
  - entity/LAMMPS
  - entity/DeepMD-kit
  - entity/PBE-functional
  - method/dft
  - method/dft-pp
  - method/pbe
  - method/berry-phase
  - method/phonon-spectrum
  - method/deepmd
  - method/mlip
  - method/md
  - method/lammps
  - method/fem
  - method/soft-mode-analysis
  - method/elf
  - method/piezoelectric-coefficient
  - method/indentation-simulation
  - material/PbS
  - material/PbSe
  - material/PbTe
  - material/2D-PbX
  - topic/ferroelectricity
  - topic/topological-defects
  - topic/2d-materials
  - topic/domain-walls
  - topic/strain-engineering
  - topic/multiferroics
  - topic/ml-interatomic-potential
---

## xuTunableFerroelectricTopological2022 — 二维拓扑表面上可调铁电拓扑缺陷：二维材料中应变工程类 skyrmion 极性结构

## 📄 元数据
Bo Xu, Zhanpeng Gong, Jingran Liu, Yunfei Hong, Yang Yang, Lou Li, Yilun Liu, Junkai Deng, Jefferson Zhe Liu，2022，arXiv preprint，DOI [10.48550/ARXIV.2204.05129](https://doi.org/10.48550/ARXIV.2204.05129)。
## 💡 一句话
通过 DFT→DeepMD 分子动力学→有限元的多尺度模拟，首次在二维铅硫族化合物 PbX（X=S, Se, Te）中用应变工程从顺电基态"无中生有"地诱导出可逆的铁电相变，并按需设计出涡旋、反涡旋、通量闭合等类斯格明子极性拓扑图案。

## 🔗 Wiki 双链
  - 概念 [[../concepts/2D-materials]]、[[../concepts/strain-engineering]]、[[../concepts/topological-defects]]、[[../concepts/density-functional-theory]]、[[../concepts/berry-phase]]、[[../concepts/machine-learning-potential]]、[[../concepts/polarization-switching]]、[[../concepts/ferroelasticity]]、[[../concepts/ferroelectric-topological-defects|铁电拓扑缺陷]]、[[../concepts/soft-mode|软模]]、[[../concepts/paraelectric-ferroelectric-transition|顺电-铁电相变]]、[[../concepts/polar-vortex|极性涡旋]]、[[../concepts/antivortex|反涡旋]]、[[../concepts/flux-closure-domain|通量闭合畴]]、[[../concepts/polarization-phase-diagram|极化-应变相图]]、[[../concepts/giant-piezoelectricity|巨压电效应]]、[[../concepts/multiscale-simulation|多尺度模拟]]
  - 实体 [[../entities/PbTe]]、[[../entities/VASP]]、[[../entities/deep-potential]]、[[../entities/domain-wall]]、[[../entities/DeepMD-kit|DeepMD-kit]]、[[../entities/LAMMPS|LAMMPS]]
  - 图表 [[../figures/crystal-structures]]、[[../figures/vibrational-spectra]]、[[../figures/mathematical-models]]、[[../figures/domain-walls]]
  - 年度 [[../write/2022]]
  - 项目 [[../projects/project-5-snte-ferroelectric-sim]]
  - 相关论文 [[../../raw/note/xuTunableFerroelectricTopological2022]]

## 🆕 新概念/实体建议
  - `entities/PbS.md`、`entities/PbSe.md` — 二维铅硫族化合物，与 PbTe 同构，基态 Cmcm 顺电相。
  - `figures/polarization-phase-diagram.md` — 二维应变空间中的极化方向/大小相图，是本文核心图件类型。
  - `figures/multiscale-simulation-workflow.md` — DFT+MLIP+FEM 三级火箭式工作流示意图。

## 📊 关键图表
> 笔记未附图片（`raw/figures/xuTunableFerroelectricTopological2022/` 下只有 manifest.json，无图文件），以下依据 raw/note 的图表深度解析以文字描述补全。

  - **图1：顺电与铁电相的原子结构、电子局域函数（ELF）及相变能量变化**
  - **图示描述**：(a-c) 对比二维 PbX 的三种晶相——顺电相 PE（Cmcm，Pb 与 X 共面）、铁电相 FE[100] 与 FE[110]（后两者呈黑磷式褶皱 puckered 结构，极化分别沿 x 轴和对角线方向）；(d-f) 给出三相的 ELF 图以显示价键与孤对电子分布；(g-h) 为 PbTe 单层在单轴拉伸 (g) 与面内剪切 (h) 下的总能量-应变曲线，蓝线为 FE 相、黑线为被强制维持的 PE 相。
  - **关键特征**：ELF 显示每个 Te 周围价 Te–Pb 键数在 PE/FE[100]/FE[110] 相中分别为 5/3/4，证明相变伴随显著化学键重构；能量曲线在 PbTe 临界应变（拉伸 3.5%、剪切 3.6%）处由 PE 最低翻转为 FE 最低，且过渡平滑，提示为连续（位移型）相变；该图是整篇论文"应变替代温度驱动铁电相变"论点的热力学起点。

  - **图2：相变驱动力——能量-序参量 Landau 双势阱与 Γ 点软模声子谱**
  - **图示描述**：(a) 在不同拉伸应变下绘制体系总能量随序参量（Pb–Te 原子在 x-y 平面投影相对位移）的变化曲线；(b) 比较 4% 拉伸下 PE 相（红）与 FE 相（黑）沿布里渊区高对称路径的声子色散谱，纵轴为声子频率 (THz)；(c) 为 (b) 中 Γ 点软模对应的原子振动本征矢示意。
  - **关键特征**：应变 <3.5% 时能量曲线为单势阱（零位移处稳定），>3.5% 时变为 Landau 双势阱，两极小值对应 ±[100] 等效极化态，是铁电双稳态的热力学标志；4% 拉伸下 PE 相声子谱在 Γ 点出现虚频（频率平方为负），FE 相所有模恢复正频；软模本征矢为 Pb 与 X 原子沿 x 方向反向振动，直接破坏反演对称性并产生 [100] 极化，从晶格动力学角度确认软模驱动机制。

  - **图3：极化强度与压电系数的应变响应（巨压电峰）**
  - **图示描述**：(a, c) 分别给出 PbS、PbSe、PbTe 三种单层在单轴拉伸 (a) 与面内剪切 (c) 下极化值随应变的变化；(b, d) 为对应压电系数 e₁₁ (b) 与 e₁₆/e₂₆ (d) 随应变的变化。横轴为应变 (%)，纵轴极化/压电系数单位均为 10⁻¹⁰ C/m（二维体系单位长度电荷）。
  - **关键特征**：三种材料的极化在各自临界应变处由零突变为非零，随后随应变平滑增长，表现为典型压电响应；相变点附近压电系数出现尖锐"爆发式"峰值，PbTe 拉伸 e₁₁ 峰值约 139.2×10⁻¹⁰ C/m、PbSe 拉伸 e₁₁ 峰值约 144.3×10⁻¹⁰ C/m，远高于远离相变点的稳态值；该巨压电效应源自相变临界点的结构失稳，对应力-电能量收集与高灵敏纳米传感器件有意义。

  - **图4：(ε_x, ε_y, γ_xy) 极化相图——应变工程的"设计蓝图"**
  - **图示描述**：(a) 为 PbTe 在双轴应变 ε_x、ε_y（范围 −7% 至 7%）与剪切应变 γ_xy（0% 至 8%）共同作用下的完整极化相图，灰色为极化近零的 PE 相，彩色为 FE 相并用颜色/箭头编码极化大小与方向；(b) 为固定 γ_xy = 0%、2%、4%、6% 时 (ε_x, ε_y) 平面内的二维极化矢量切片。
  - **关键特征**：γ_xy = 0 时极化沿较大应变方向——ε_x > ε_y 沿 [100]，ε_x < ε_y 沿 [010]，ε_x = ε_y 沿 [110]；引入剪切后极化方向偏离晶轴并随 γ_xy 连续旋转；该相图把任意局部应变状态映射为确定的极化矢量，是后续 MD 压痕和 FEM 器件设计中"按应变场书写极化图案"的查找表，也是全文连接微观机制与宏观拓扑结构的核心桥梁。

  - **图5：DeepMD–LAMMPS 纳米压痕 MD 模拟与涡旋极性拓扑态**
  - **图示描述**：(a) 为 MD 模型示意：半径 3.5 nm 球形压头下压 60×60 单胞（约 28×28 nm）的 PbTe 单层薄膜；(b) 为压痕深度 3.6 nm 时薄膜中心区每个单胞的净极化矢量分布；(c-e) 分别给出同一区域 a 轴拉伸、b 轴拉伸、剪切三种局部应变分量的分布图（颜色编码应变大小，单位 %）。
  - **关键特征**：压深 3.6 nm 时中心区出现四象限极化图案，各象限极化分别近似指向 ±x、±y，由 90° 畴壁分隔，构成中心发散的极性涡旋 (vortex)，是首次在二维材料中实现的极性拓扑态；(c-e) 应变分布同样被对角线分割，与 (b) 极化图案高度相关，直接证明非均匀应变场按图4相图"装配"出拓扑极化；该模拟在 10 K 下基于 DFT 数据训练的 DeepMD 势完成，验证了机器学习势+LAMMPS 处理相变附近大尺度非均匀应变的可行性。

  - **图6：FEM 器件模型——孔洞形状与晶体取向调谐反涡旋/通量闭合畴**
  - **图示描述**：(a-c) 为三种器件几何：硬质衬底开孔、单层 PbTe 膜边界固定并受均匀气压 P 向下鼓泡——模型 I 圆孔（直径 200 nm）；模型 II 方孔（边长 200 nm），膜晶格沿孔边对齐；模型 III 同方孔但晶格旋转 45°；(d-f) 为对应 FEM 应变场经图4相图映射得到的极化拓扑图案（背景色表示极化大小，箭头表示方向）。
  - **关键特征**：模型 I 在约 14 MPa 下得到立方状反涡旋 (cubic anti-vortex)；模型 II 在约 8 MPa 下得到圆形反涡旋 (round anti-vortex)；模型 III 在约 4.5 MPa 下得到通量闭合畴 (flux-closure)；FEM 将 PbTe 视为各向异性弹性膜，按局部应变是否越过临界值切换 PE/FE 相弹性常数 (C₁₁, C₂₂, C₁₂ 等)；三种几何仅靠孔洞形状与晶体取向差异就"挑选"出三种拓扑类别，证明通过简单图形化衬底+均匀气压即可在微米器件尺度按需编写可逆极性拓扑图案。

## 🔬 项目连接
  - **project-5（lammps 势函数 SnTe 铁电模拟）— strong**：本文是与 project-5 最直接对口的方法学/机理参考文献之一。(1) 材料同属 IV–VI 族岩盐结构衍生的二维单硫族化物，PbX 与 SnTe 电子结构、晶格对称性（Cmcm 顺电相对应 Pnma 铁电相）、软模相变图像高度相似；(2) 计算流水线正是 project-5 计划采用的 DFT（VASP/PBE）→ DeepMD 训练 → LAMMPS 大尺度 MD → 连续介质（FEM/相场）的多尺度范式，DeepMD 损失函数、训练数据采样、相变附近势函数精度等细节可直接借鉴；(3) 本文给出的极化-应变相图构建方法、Berry 相电极化计算、压电系数提取、压痕/鼓泡非均匀应变加载方案，可直接迁移到 SnTe 的铁电动力学与拓扑极化结构研究；(4) 文中 60×60 单胞、压痕 3.6 nm、10 K MD 等具体模拟参数可作为 project-5 量纲和尺度规划的参照。建议在 project-5 大纲中把本文列为"多尺度模拟流程"和"应变诱导拓扑极化"两节的核心引文。
  - project-2（Mn 多铁）：无直接连接。本文只涉及纯铁电/力学自由度，不含磁性、磁电耦合或 Mn 基氧化物。
  - project-1/3/4/6/7：无直接连接（非双光子、非机械发光 NN、非 TTF 分子、非湿度传感、非 CDW）。

## 🔗 项目双链
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]

## 📝 组织与用词
  - 论证按"问题提出 → DFT 微观机制（相变+软模+相图）→ DeepMD-MD 介观验证（压痕涡旋）→ FEM 宏观器件设计（孔洞形状调拓扑）→ 结论"递进，是一篇标准的多尺度模拟理论文章，逻辑链条即"应变场设计 → 相变控制 → 拓扑图案编写"。
  - 值得在 wiki 中复用的术语：
    - ferroelectric topological defect / 铁电拓扑缺陷 [[../concepts/ferroelectric-topological-defects|铁电拓扑缺陷]]
    - skyrmion-like polar structure / 类斯格明子极性结构
    - paraelectric (PE)–ferroelectric (FE) transition / 顺电-铁电相变 [[../concepts/paraelectric-ferroelectric-transition|顺电-铁电相变]]
    - soft mode [[../concepts/soft-mode|soft mode]] / 软模（横向光学模软化）
    - Landau double-well potential / Landau 双势阱
    - strain engineering / 应变工程 [[../concepts/strain-engineering|应变工程]]
    - polarization phase diagram / 极化-应变相图 [[../concepts/polarization-phase-diagram|极化-应变相图]]
    - antivortex & flux-closure / 反涡旋与通量闭合畴

## ✏️ 可写入 Wiki 的要点
  1. 二维 PbX（X=S, Se, Te）基态为高对称顺电相（空间群 Cmcm，Pb 与 X 共面），与 GeS/GeSe/SnS/SnSe 等本征 Pnma 铁电体不同；施加单轴拉伸 >3.5%（PbTe）或面内剪切 >3.6% 即可诱导 Cmcm→Pnma 的可逆位移型铁电相变，产生面内自发极化。
  2. 相变临界应变随材料不同：PbS 为 1.6% 拉伸 / 2.1% 剪切，PbSe 为 2.2% / 2.4%，PbTe 为 3.5% / 3.6%（见表1）；晶格常数 a 分别为 4.237、4.400、4.638 Å。
  3. 相变由 Γ 点横向光学软模驱动：4% 拉伸下 PE 相声子谱在 Γ 点出现虚频，FE 相所有声子模恢复为正频；软模本征矢为 Pb 与 X 原子沿 x 方向反向振动，直接破坏中心[[../concepts/inversion-symmetry|反演对称性]]。
  4. 能量-[[../concepts/order-parameter|序参量]]曲线在临界应变以上由单势阱变为 Landau [[../concepts/double-well|双势阱]]，两个极小值对应 ±[100] 极化态，是铁电双稳态的热力学标志；应变在二维 PbX 中扮演了传统铁电体（如 BaTiO₃）中温度的角色。
  5. ELF 显示相变伴随显著化学键重构：PE 相中每个 Te 周围有 5 个价键，FE[100] 相中为 3 个，FE[110] 相中为 4 个；FE 相呈现黑磷式褶皱（puckered）结构。
  6. 临界应变附近出现巨压电系数"爆发"：PbTe 拉伸 e₁₁ 峰值约 139.2×10⁻¹⁰ C/m，PbSe 拉伸 e₁₁ 峰值约 144.3×10⁻¹⁰ C/m，远超远离相变点的稳态值，对应力-电能量收集与高灵敏传感有意义。
  7. 作者构建了 (ε_x, ε_y, γ_xy) 全空间极化相图：γ_xy=0 时极化沿较大应变方向（ε_x>ε_y 沿 [100]，ε_x=ε_y 沿 [110]），引入剪切后极化方向连续旋转；这张相图是后续用应变场"绘制"任意图案的[[../concepts/lookup-table-calibration|查找表]]。
  8. 用 DeepMD-kit 训练深度学习势（损失函数 L = p_ε Δε² + p_f/(3N) Σ|ΔF_i|² + p_ξ/9 ‖Δξ‖²，同时拟合能量、力、virial），在 LAMMPS 中对 60×60 单胞（~28×28 nm）PbTe 薄膜做 10 K、半径 3.5 nm 球形压头压痕，压深 3.6 nm 时中心区出现由 90° 畴壁分隔的四象限涡旋极性图案，首次在[[../concepts/2D-materials|二维材料]]中实现极性拓扑态。
  9. FEM 把 PbTe 视为[[../concepts/migdal-eliashberg-theory|各向异性]]弹性膜，按局部应变是否越过相变临界值切换 PE/FE 相弹性常数 (C₁₁, C₂₂, C₁₂ 等)，在带孔硬质衬底上施加均匀气压使薄膜鼓泡：圆孔（200 nm，14 MPa）→ 立方[[../concepts/antivortex|反涡旋]]；方孔晶格对齐孔边（200 nm，8 MPa）→ 圆形反涡旋；方孔晶格旋转 45°（4.5 MPa）→ [[../concepts/flux-closure-domain|通量闭合畴]]。证明孔洞形状+晶体取向即可挑选拓扑类别。
  10. 局限：全程 0 K/10 K 模拟，未讨论室温热稳定性；FEM 在相界处用均质化阶跃切换参数，忽略梯度能和畴壁动力学；缺乏实验验证（需要 AFM 压痕+PFM/4D-STEM DPC 联用）；未给出拓扑态的电学/光学读取方案；DeepMD 势在训练集外（如相变附近、非均匀应变）的泛化误差未量化。这些正是 project-5 等后续工作可补足的方向。
