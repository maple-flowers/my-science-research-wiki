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
concepts: [kittel-law, polar-vortices, vortex-antivortex-pair, depolarization-field, domain-walls, topological-defects, strain-engineering, multiferroicity, ferroelasticity, polarization-switching, second-principles, superlattice, anharmonic-effects, polarization-waves, topological-charge, kosterlitz-thouless, poincare-hopf-theorem, domain-wall]
entities: [PbTiO3, SrTiO3, BiFeO3, SCALE-UP, PHONOPY]
methods: [second-principles, dft, monte-carlo-annealing, langevin-md, force-constant-bands, phonon-spectra, born-effective-charges, effective-hamiltonian]
materials: [PbTiO3, SrTiO3, PbTiO3-SrTiO3-superlattice]
figures: [crystal-structures-bulk, domain-walls-structures]
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
  - concept/domain-wall
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
## 🔗 Wiki 双链
  - 概念 [[../concepts/multiferroicity]]、[[../concepts/second-principles]]、[[../concepts/superlattice]]、[[../concepts/domain-walls]]、[[../concepts/depolarization-field]]、[[../concepts/topological-defects]]、[[../concepts/polarization-waves]]、[[../concepts/strain-engineering]]、[[../concepts/domain-wall]]、[[../concepts/vortex-antivortex-pair]]、[[../concepts/kittel-law]]、[[../concepts/poincare-hopf-theorem]]、[[../concepts/polar-vortices]]、[[../concepts/topological-charge]]、[[../concepts/ferroelasticity]]、[[../concepts/kosterlitz-thouless]]、[[../concepts/anharmonic-effects]]、[[../concepts/polarization-switching]]
  - 实体 [[../entities/BiFeO3]]、[[../entities/SCALE-UP]]、[[../entities/SrTiO3]]、[[../entities/PbTiO3]]、[[../entities/PHONOPY]]
  - 相关论文 [[../../raw/note/gomez-ortizKittelLawDomain2023]]

