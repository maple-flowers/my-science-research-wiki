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
concepts: [2d-materials, strain-engineering, topological-defects, berry-phase, density-functional-theory, machine-learning-potential, polarization-switching, ferroelasticity, ferroelectric-topological-defects, soft-mode, paraelectric-ferroelectric-transition, polar-vortex, antivortex, flux-closure, polarization-phase-diagram, giant-piezoelectricity, multiscale-simulation, landau-double-well, electron-localization-function, domain-wall]
entities: [VASP, PbTe, deep-potential, PbS, PbSe, LAMMPS, DeepMD-kit, PBE-functional]
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
  - concept/domain-wall
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
## 🔗 Wiki 双链
  - 概念 [[../concepts/ferroelectric-topological-defects]]、[[../concepts/multiscale-simulation]]、[[../concepts/polarization-phase-diagram]]、[[../concepts/flux-closure]]、[[../concepts/antivortex]]、[[../concepts/electron-localization-function]]、[[../concepts/topological-defects]]、[[../concepts/strain-engineering]]、[[../concepts/2d-materials]]、[[../concepts/density-functional-theory]]、[[../concepts/polar-vortex]]、[[../concepts/berry-phase]]、[[../concepts/soft-mode]]、[[../concepts/landau-double-well]]、[[../concepts/paraelectric-ferroelectric-transition]]、[[../concepts/machine-learning-potential]]、[[../concepts/giant-piezoelectricity]]、[[../concepts/ferroelasticity]]、[[../concepts/polarization-switching]]、[[../concepts/domain-wall]]
  - 实体 [[../entities/deep-potential]]、[[../entities/PbTe]]、[[../entities/PBE-functional]]、[[../entities/PbS]]、[[../entities/LAMMPS]]、[[../entities/PbSe]]、[[../entities/VASP]]、[[../entities/DeepMD-kit]]
  - 相关论文 [[../../raw/note/xuTunableFerroelectricTopological2022]]

