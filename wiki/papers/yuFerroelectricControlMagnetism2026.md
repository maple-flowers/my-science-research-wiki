---
citekey: yuFerroelectricControlMagnetism2026
title: "Ferroelectric Control of Magnetism and Giant Magnetoresistance Via Intercalation-Induced Symmetry Breaking in Two-Dimensional Multiferroics with Strong Magnetoelectric Coupling"
title_zh: "强磁电耦合二维多铁性材料中嵌入诱导对称破缺对磁性和巨磁电阻的铁电控制"
authors: [Cuiju Yu, Liangliang Hong, Zhao Chen, Zhao Liu, Shizhe Jiao, Xiaofeng Liu, Wei Hu]
year: 2026
journal: "The Journal of Physical Chemistry Letters"
doi: "10.1021/acs.jpclett.6c00390"
url: "https://doi.org/10.1021/acs.jpclett.6c00390"
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/yuFerroelectricControlMagnetism2026]]
projects: []
concepts: [2D-materials, altermagnetism, berry-phase, density-functional-theory, giant-spin-splitting, magnetoelectric-coupling, multiferroicity, polarization-switching, spin-orbit-coupling, strain-engineering, domain-wall]
entities: [BiFeO3, CrTe2, Fe3GeTe2, HoMnO3, In2Se3, MXenes, TMDs, VASP, WTe2, Wannier90, h-BN]
methods: [afm-pfm, berry-phase, dft, md, mlip, monte-carlo, neb, stm-mbe]
materials: [BiFeO3, CrTe2, Fe3GeTe2, HoMnO3, In2Se3, MXenes, TMDs, WTe2, h-BN]
figures: [crystal-structures-bulk, domain-walls-switching-properties, electronic-bands-band-structures, electronic-bands-cdw-transport, electronic-bands-dos-fermi]
领域基础知识:: >-
  二维多铁材料（2D Multiferroics）与磁电耦合（Magnetoelectric Coupling）是自旋电子学（Spintronics）的前沿领域。核心目标是在单一材料中耦合铁电性（Ferroelectricity, FE，可被电场翻转的自发电极化）和磁性（Magnetism，自发的磁有序），以实现电场控制磁矩，开发低功耗器件。传统多铁体的主要瓶颈在于磁性和铁电性起源独立，耦合微弱，限制了其应用。
研究背景:: >-
  已发现的二维多铁材料主要分为三类：I型（磁性与铁电性起源独立，耦合弱），II型（磁性驱动铁电性，但极化弱），III型（铁电性驱动磁性，稀少且难以设计）。因此，寻找一种能实现强磁电耦合的通用设计策略和室温二维多铁材料体系是该领域的关键挑战。
作者的问题意识:: >-
  作者旨在解决二维多铁材料中磁电耦合弱的根本性难题。他们提出并验证了一个核心问题：能否通过一种通用的材料设计策略（如插层），在范德华反铁磁体中人为引入并强关联铁电性和磁性，从而实现室温下电场对磁矩的完全控制，并展示其在器件中的应用潜力？
主要研究对象:: >-
  单层Cr₄S₄FBr₂ (CSFB)，一种由双层CrSBr通过“融合”和氟离子（F⁻）桥联设计而成的二维A型完全补偿亚铁磁金属（A-type fully compensated ferrimagnetic metal）。此外，还研究了其衍生物Cr₄S₄X₃和Mn₄N₄X₃系列以验证策略的通用性。
主要研究方法:: >-
  基于第一性原理的多尺度理论计算。主要包括：密度泛函理论（DFT，如PBE+U, HSE06）计算电子结构与磁性；CI-NEB方法计算铁电翻转势垒与路径；构建有效哈密顿量模型，结合蒙特卡洛和分子动力学（MD）模拟估算Néel温度（TN）和铁电居里温度（TC）；非平衡格林函数（NEGF）方法模拟多铁隧道结（MFTJ）的量子输运特性。
研究意义:: >-
  1. 提出了一种全新的“插层诱导对称性破缺”范式，为设计III型多铁体和实现强磁电耦合提供了清晰的理论框架。2. 成功预测了单层Cr₄S₄FBr₂这一兼具室温磁电耦合、高转变温度、巨磁阻效应的具体材料体系，为实验探索提供了明确目标。3. 演示了电场驱动的、非易失性巨磁阻效应，为开发超低功耗自旋电子学器件指明了新方向。
研究结论:: >-
  单层Cr₄S₄FBr₂是一种高Néel温度（469 K）和铁电居里温度（334 K）的A型完全补偿亚铁磁金属。其垂直铁电极化（1.1 pC/m）源于F原子位移，翻转势垒低（0.11 eV）。该材料展现出强磁电耦合，翻转铁电极化可完全反转自旋极化、自旋纹理和Chern数（从-2到+2）。基于该材料的多铁隧道结可实现由纯电场驱动的、高达4.8 × 10³%的巨磁阻。
对领域的贡献:: >-
  1. **理论贡献**：为设计强磁电耦合多铁材料提供了“插层破缺对称性”的新范式，并揭示了A型亚铁磁中实现铁电-自旋-拓扑锁定的微观机制。2. **材料贡献**：预测了Cr₄S₄FBr₂及其衍生物等一系列高性能室温二维多铁材料，丰富了多铁材料库。3. **器件贡献**：展示了电场控制巨磁阻的新概念器件，证明了其在非易失性、低功耗信息存储和处理中的巨大潜力。
未来研究方向提及:: >-
  1. 实验合成与验证：通过文中提出的卤素离子交换插层或堆垛工程等方法，实际制备单层CSFB及器件，并验证其多铁性与磁电耦合性能。2. 拓展材料家族：将插层策略系统性地应用于与CrSBr同构的、更广泛的二维磁体家族（如MnNX等），探索其多铁潜力。
未来研究方向思考:: >-
  1. **缺陷与界面工程**：研究缺陷对CSFB中铁电畴翻转动力学和矫顽场的影响，以及在实际金属电极/CSFB界面的磁电耦合效应。2. **多场调控与拓扑物理**：探索应变、光场、静电掺杂等手段对CSFB磁电耦合和拓扑Chern数的调控，或通过掺杂打开全局带隙，实现量子反常霍尔效应或拓扑超导。3. **自旋动力学**：研究电场是否可激发或调控CSFB中的自旋波（磁振子），探索基于磁振子的逻辑器件。4. **机制深化**：澄清其“完全补偿亚铁磁体”与“交变磁体”之间的概念关联，并深入分析在金属性背景下，自由电子对铁电偶极子场的屏蔽效应及其对器件性能的影响。
tags:
  - paper
  - type/experiment
  - year/2026
  - concept/2D-materials
  - concept/altermagnetism
  - concept/berry-phase
  - concept/density-functional-theory
  - concept/giant-spin-splitting
  - concept/magnetoelectric-coupling
  - concept/multiferroicity
  - concept/polarization-switching
  - concept/spin-orbit-coupling
  - concept/strain-engineering
  - entity/BiFeO3
  - entity/CrTe2
  - entity/Fe3GeTe2
  - entity/HoMnO3
  - entity/In2Se3
  - entity/MXenes
  - entity/TMDs
  - entity/VASP
  - entity/WTe2
  - entity/Wannier90
  - concept/domain-wall
  - entity/h-BN
  - method/afm-pfm
  - method/berry-phase
  - method/dft
  - method/md
  - method/mlip
  - method/monte-carlo
  - method/neb
  - method/stm-mbe
  - material/BiFeO3
  - material/CrTe2
  - material/Fe3GeTe2
  - material/HoMnO3
  - material/In2Se3
  - material/MXenes
  - material/TMDs
  - material/WTe2
  - material/h-BN
  - topic/2d-materials
  - topic/charge-density-wave
  - topic/ferroelectricity
  - topic/ferromagnetism
  - topic/mof
  - topic/multiferroics
  - topic/mxene
  - topic/phase-transition
  - topic/polarization
---
## 🔗 Wiki 双链
  - 概念 [[../concepts/multiferroicity]]、[[../concepts/berry-phase]]、[[../concepts/domain-wall]]、[[../concepts/magnetoelectric-coupling]]、[[../concepts/giant-spin-splitting]]、[[../concepts/spin-orbit-coupling]]、[[../concepts/2d-materials]]、[[../concepts/altermagnetism]]、[[../concepts/polarization-switching]]、[[../concepts/strain-engineering]]、[[../concepts/density-functional-theory]]
  - 实体 [[../entities/TMDs]]、[[../entities/MXenes]]、[[../entities/WTe2]]、[[../entities/CrTe2]]、[[../entities/Wannier90]]、[[../entities/h-BN]]、[[../entities/Fe3GeTe2]]、[[../entities/BiFeO3]]、[[../entities/In2Se3]]、[[../entities/VASP]]、[[../entities/HoMnO3]]
  - 相关论文 [[../../raw/note/yuFerroelectricControlMagnetism2026]]

