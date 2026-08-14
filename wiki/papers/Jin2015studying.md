---
citekey: Jin2015studying
title: "Studying the Polarization Switching in Polycrystalline BiFeO3 Films by 2D Piezoresponse Force Microscopy"
authors: [Yaming Jin, Xiaomei Lu, Junting Zhang, Yi Kan, Huifeng Bo, Fengzhen Huang, Tingting Xu, Yingchao Du, Shuyu Xiao, Jinsong Zhu]
year: 2015
journal: "Scientific Reports"
doi: "10.1038/srep12237"
url: "https://doi.org/10.1038/srep12237"
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/Jin2015studying]]
projects: [project-2, project-5]
concepts: [polarization-switching, multiferroicity, magnetoelectric-coupling, ferroelasticity, strain-engineering, density-functional-theory, piezoelectric-response, polycrystalline-ferroelectrics, charge-migration-energy, domain-wall]
entities: [BiFeO3, PFM, first-principles-piezoelectric-tensor]
methods: [pfm, 2d-pfm, first-principles, dft, euler-angle-rotation, numerical-inversion, mod-film-growth, xrd]
materials: [BiFeO3, Pt-Ti-SiO2-Si]
figures: [domain-walls-switching-properties, experimental-setups]
领域基础知识:: >-
  多铁性材料（特别是铁酸铋 BiFeO₃）中的铁电畴结构、极化翻转机制，以及压电力显微镜（PFM）的基本原理。理解铁电体、铁弹体、逆压电效应、菱方钙钛矿结构等概念是阅读本文的基础。
研究背景:: >-
  菱方相 BiFeO₃ 的非 180° 铁电畴翻转会伴随铁弹效应，影响应力和磁序，是磁电耦合器件的关键。然而，现有研究多集中于取向已知的外延薄膜，关于多晶薄膜中本征翻转特性的研究由于难于确定随机取向晶粒的极化矢量而鲜有报道。
作者的问题意识:: >-
  如何在不进行复杂三维样品旋转的情况下，仅通过二维压电力显微镜（2D PFM）的垂直和水平信号，就能精确测定多晶 BiFeO₃ 薄膜中随机取向晶粒的极化翻转角度，并揭示其内在的物理机制与统计规律。
主要研究对象:: >-
  通过金属有机分解法（MOD）在 Pt/Ti/SiO₂/Si 衬底上制备的、厚度约 300 nm、平均晶粒尺寸约 130 nm 的多晶 BiFeO₃ 薄膜。
主要研究方法:: >-
  1. 理论建模：利用第一性原理计算的压电张量，通过欧拉角旋转构建 BFO 晶粒在所有空间取向上的理论压电响应曲面。2. 实验测量：使用二维压电力显微镜（2D PFM），在施加极化电压前后，对同一区域进行扫描，获取垂直（OP）和水平（IPx）方向的压电响应图像。3. 数值求解：开发专用算法，将实验测得的归一化信号与理论曲面进行全局匹配，反推出畴的初始取向与翻转后的取向，从而精确计算翻转角度。
研究意义:: >-
  在方法学上，提供了一种普适性强、可推广至其他随机取向铁电材料的二维 PFM 数据分析方法，无需旋转样品即可确定三维极化信息。在基础科学上，首次定量揭示了多晶 BFO 薄膜中极化翻转角度的统计分布，并建立了"电荷迁移能"与"面内应力能"相互竞争的物理模型，加深了对复杂体系中铁电翻转动力学的理解，为设计可控磁电耦合器件指明了方向。
研究结论:: >-
  1. 成功开发出一种从二维 PFM 数据中解析多晶 BFO 极化翻转角度的方法。2. 在多晶 BFO 薄膜中，71° 极化翻转最为普遍（占翻转面积的 42%），109° 和 180° 翻转各占约 29%。3. 高达 34% 的翻转区域的初始垂向极化方向与极化电场方向平行，这是多晶样品中的一个独特现象。4. 翻转路径的选择主要由电荷迁移（电场能）与面内应力（弹性能）这两个同等重要且相互竞争的因素决定，且对晶粒的几何排布（即晶粒取向）高度敏感。
对领域的贡献:: >-
  1. 开发了一种创新的、可推广的二维 PFM 数据处理方法，能够从随机取向样品中提取三维极化信息，为相关研究提供了强大的分析工具。2. 提供了关于多晶 BFO 薄膜极化翻转行为的第一份详尽的定量统计报告，并揭示了"异常"翻转（初始 Pz 与电场平行）的显著存在。3. 提出了一个清晰、有说服力的"电荷迁移-面内应力"竞争模型，为理解和预测多晶铁电材料中的畴翻转行为提供了重要的理论框架。
未来研究方向提及:: >-
  1. 将该数据处理方法扩展应用于其他具有随机取向的铁电材料体系。2. 利用该方法的实时性优势，研究极化翻转后铁电畴随时间的弛豫过程。3. 基于对翻转机制的理解，探索通过调控应力或电场来控制翻转模式，以实现显著的磁电耦合效应。
未来研究方向思考:: >-
  1. 结合高分辨率 X 射线衍射或透射电子显微镜，直接测量单个翻转畴周围的三维应变场，以验证和细化"面内应力能"模型。2. 将本研究的统计结果与相场模拟相结合，在更大尺度上重现多晶 BFO 在不同极化条件下的畴结构演化，将统计规律与微观动力学过程联系起来。3. 探索在对称电极结构的器件原型中，多晶 BFO 薄膜的极化翻转行为，使研究更贴近实际应用场景。
tags:
  - paper
  - type/experiment
  - year/2015
  - project/project-2
  - project/project-5
  - relevance/project-2/strong
  - relevance/project-5/medium
  - concept/polarization-switching
  - concept/multiferroicity
  - concept/magnetoelectric-coupling
  - concept/ferroelasticity
  - concept/strain-engineering
  - concept/density-functional-theory
  - concept/piezoelectric-response
  - concept/polycrystalline-ferroelectrics
  - concept/charge-migration-energy
  - entity/BiFeO3
  - concept/domain-wall
  - entity/PFM
  - entity/first-principles-piezoelectric-tensor
  - method/pfm
  - method/2d-pfm
  - method/first-principles
  - method/dft
  - method/euler-angle-rotation
  - method/numerical-inversion
  - method/mod-film-growth
  - method/xrd
  - material/BiFeO3
  - material/Pt-Ti-SiO2-Si
  - topic/multiferroics
  - topic/ferroelectricity
  - topic/domain-walls
  - topic/piezoelectricity
---
## 🔗 Wiki 双链
  - 概念 [[../concepts/charge-migration-energy]]、[[../concepts/multiferroicity]]、[[../concepts/piezoelectric-response]]、[[../concepts/polycrystalline-ferroelectrics]]、[[../concepts/domain-wall]]、[[../concepts/magnetoelectric-coupling]]、[[../concepts/ferroelasticity]]、[[../concepts/polarization-switching]]、[[../concepts/strain-engineering]]、[[../concepts/density-functional-theory]]
  - 实体 [[../entities/PFM]]、[[../entities/BiFeO3]]、[[../entities/first-principles-piezoelectric-tensor]]
  - 相关论文 [[../../raw/note/Jin2015studying]]

