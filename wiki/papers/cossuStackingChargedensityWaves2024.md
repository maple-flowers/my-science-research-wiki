---
citekey: cossuStackingChargedensityWaves2024
title: "Stacking of charge-density waves in                     <mml:math xmlns:mml='http://www.w3.org/1998/Math/MathML'>                       <mml:mn>2</mml:mn>                       <mml:mi mathvariant='normal'>H</mml:mi>                       <mml:mtext>−</mml:mtext>                       <mml:msub>                         <mml:mi>NbSe</mml:mi>                         <mml:mn>2</mml:mn>                       </mml:msub>                     </mml:math>                     bilayers"
title_zh: "电荷密度波的叠加http://www.w3.org/1998/Math/MathML“><mml:mn>2<mml:mn>2<mml:mn>"
authors: [F. Cossu, D. Nafday, K. Palotás, M. Biderang, H.-S. Kim, A. Akbari, I. Di Marco]
year: 2024
journal: "Physical Review Research"
doi: "10.1103/PhysRevResearch.6.043111"
url: "https://doi.org/10.1103/PhysRevResearch.6.043111"
paper_type: experiment
status: ingested
year_read: 2026
original_note: "[[../../raw/note/cossuStackingChargedensityWaves2024]]"
projects: [project-5, project-7]
concepts: [2D-materials, charge-density-wave, density-functional-theory, moire-superlattice, strain-engineering]
entities: [TMDs, VASP, Wannier90]
methods: [dft, mlip, raman, stm-mbe, tem, xanes, xrd]
materials: [TMDs]
figures: [crystal-structures, electronic-bands, heterostructures-stacking, vibrational-spectra]
"领域基础知识": >-
  电荷密度波 (Charge Density Wave, CDW) 是低维金属体系中，电子密度和晶格原子位置发生周期性调制的集体量子现象。过渡金属硫族化合物 (Transition Metal Dichalcogenides, TMDs) 是典型的层状范德华材料，其弱层间耦合使得研究维度效应对CDW的影响成为可能，并且CDW常与超导、磁性等其他量子序共存或竞争。
"研究背景": >-
  过去对2H-NbSe₂中CDW的研究，实验观测多基于表面，理论解释则主要依赖单层模型，系统性地忽略了层间堆叠效应。然而，近期在1T-TaS₂等1T型TMDs中发现，层间CDW的特定堆叠方式足以驱动金属-绝缘体转变，这引发了关于层间堆叠在金属性TMDs中是否同样扮演重要角色的普遍性问题。
"作者的问题意识": >-
  作者的核心问题在于，金属性TMD 2H-NbSe₂中是否存在由层间耦合驱动的CDW垂直堆叠序？这种堆叠序会产生哪些新的物理现象？其存在的“指纹”能否被当前的实验技术（如扫描隧道显微镜）所分辨和检测？
"主要研究对象": >-
  2H-NbSe₂双层结构，作为保持块体中心对称性且能体现层间耦合的最简模型系统。研究聚焦于其电荷密度波 (CDW) 的垂直堆叠构型。
"主要研究方法": >-
  采用基于密度泛函理论 (DFT) 的第一性原理计算，使用VASP软件包。为准确描述层间范德华 (vdW) 相互作用，系统对比了多种vdW修正泛函 (GGA+D2, TS, DF, MBD@FI)。通过构建3×3超胞并控制离子初始位置，系统性地生成了不同的CDW堆叠构型（“混合物”和“位移”），并结合态密度、模拟STM图像和几何结构因子等手段进行分析。
"研究意义": >-
  本研究将TMDs中CDW的研究范式从“单层主导”拓展到“考虑层间堆叠”，揭示了一个普遍被忽略的物理自由度。它连接了表面敏感的STM实验与理论模型之间的鸿沟，为重新解释过往实验数据及设计未来实验提供了关键的理论指导，对理解多维强关联电子体系具有重要价值。
"研究结论": >-
  2H-NbSe₂双层中的层间堆叠会产生多种能量相近的CDW构型，导致自发对称性破缺。基态是HC-HC混合物中的S3位移构型，而HC-CC混合构型是其重要的低能激发态。这些不同的堆叠构型在模拟STM图像和倒空间的几何结构因子上展现出独特且可分辨的指纹，预测其能被现代高分辨率实验技术检测到。
"对领域的贡献": >-
  首次系统性地绘制了2H-NbSe₂双层中CDW堆叠的能量景观，并提出了具体的、可实验验证的微观指纹特征。证明了层间耦合在金属性TMDs中的非平庸作用，将堆叠工程的概念从1T型材料推广到了更广泛的2H型材料，启发了对层状量子材料中隐藏自由度的探索。
"未来研究方向提及": >-
  研究层间扭转角度和外部压力对CDW堆叠的调控；计算不同堆叠构型的声子谱以理解拉曼光谱和温度效应；将双层模型推广到块体和异质结；探索不同堆叠构型对磁性、超导等共存序的影响。
"未来研究方向思考": >-
  可进一步探索CDW堆叠畴壁的动力学和拓扑性质，研究其在电流或光激发下的运动。探究不同堆叠构型中，由对称性破缺导致的非平庸能带拓扑性质（如拓扑费米面）。结合机器学习势函数进行大规模分子动力学模拟，研究有限温度下CDW堆叠的相变和涨落。 🚀 [笔记回链](zotero://select/library/items/B3JHKN7M) * * * `GPT 自定 ②` `deepseek-v4-pro` _由批量 AI 解读自动生成于 2026/8/11 06:50:43 （重新解读）_ 🏷️ #🤖️/AI文献解读 🏷️ #🤖️/AI文献阅读
tags:
  - paper
  - type/experiment
  - year/2024
  - project/project-5
  - relevance/project-5/weak
  - project/project-7
  - relevance/project-7/core
  - concept/2D-materials
  - concept/charge-density-wave
  - concept/density-functional-theory
  - concept/moire-superlattice
  - concept/strain-engineering
  - entity/TMDs
  - entity/VASP
  - entity/Wannier90
  - method/dft
  - method/mlip
  - method/raman
  - method/stm-mbe
  - method/tem
  - method/xanes
  - method/xrd
  - material/TMDs
  - topic/2d-materials
  - topic/charge-density-wave
  - topic/ferroelectricity
  - topic/superconductivity
---

## cossuStackingChargedensityWaves2024 — 2H-NbSe₂ 双层中电荷密度波的堆叠

- **元数据**：F. Cossu, D. Nafday, K. Palotás, M. Biderang, H.-S. Kim, A. Akbari, I. Di Marco et al.，2024，Physical Review Research 6, 043111，DOI [10.1103/PhysRevResearch.6.043111](https://doi.org/10.1103/PhysRevResearch.6.043111)

- **一句话**：通过 DFT 第一性原理计算首次系统绘制 2H-NbSe₂ 双层中电荷密度波（CDW）的垂直堆叠能量景观，证明不可忽略的层间耦合导致自发对称性破缺，基态为 HC-HC_(S3)，混合堆叠 HC-CC_(S4) 等近简并激发态在模拟 STM 图像与几何结构因子中具有可分辨的"指纹"。

- **现有wiki双链**：
  - 概念 [[../concepts/charge-density-wave]]
  - 概念 [[../concepts/density-functional-theory]]
  - 概念 [[../concepts/2D-materials]]
  - 概念 [[../concepts/moire-superlattice]]（文中展望扭转双层 NbSe₂）
  - 概念 [[../concepts/strain-engineering]]（作者团队前作 strain-induced stripe phase in NbSe₂）
  - 实体 [[../entities/TMDs]]
  - 实体 [[../entities/VASP]]
  - 实体 [[../entities/Wannier90]]（无直接关联，不链）
  - 图表 [[../figures/crystal-structures]]
  - 图表 [[../figures/electronic-bands]]
  - 图表 [[../figures/heterostructures-stacking]]
  - 图表 [[../figures/vibrational-spectra]]（展望声子/拉曼）
  - 年度 [[../write/2024]]
  - 项目 [[../projects/project-7-cdw-charge-density-wave]]
  - 相关论文 [[../../raw/note/cossuStackingChargedensityWaves2024]]

- **新概念/实体建议**：
  - `entities/NbSe2.md` — 二硒化铌，典型金属性 2H 型 TMD，CDW 与超导共存的模型体系；本文研究其双层 CDW 堆叠。
  - `entities/1T-TaS2.md` — 二硫化钽 1T 相，层间 CDW（大卫之星）堆叠驱动金属-绝缘体转变，是本文立论的参照体系。
  - `concepts/interlayer-stacking.md` — 层间堆叠（stacking order），双层/多层范德华材料中各层 CDW 或晶格的相对平移与旋转，可改变整体对称性与物性。
  - `concepts/cdw-blends-displacements.md` — CDW"混合物与位移"分类法：blend 指上下层 CDW 类型组合（HC-HC、HC-CC 等），displacement（S1/S2/…）指给定 blend 下由对称性允许的非等价层间平移。
  - `concepts/geometric-structure-factor.md` — 几何结构因子 f(h,k,l)，从原子坐标或部分电荷密度的傅里叶变换得到，用于连接 XRD/TEM/FT-STM 实验与理论对称性分析。
  - `concepts/pseudogap.md` — 赝能隙，费米能级处态密度被抑制但未完全打开能隙；本文显示 CDW 构型越稳定，E_F 处态密度耗尽越显著。
  - `concepts/vdw-correction.md` — 范德华修正（D2/TS/DF/MBD@FI 等），层状材料 DFT 中层间距与层间耦合强度对修正方案高度敏感。
  - `concepts/peierls-instability.md` — Peierls 不稳定性，一维电子-声子耦合导致的 CDW 机制；本文将"E_F 态耗尽 → 能量增益"的 Peierls 逻辑推广到 2H-NbSe₂ 这一由动量依赖电声耦合主导的二维体系。

- **关键图表**：
  - ![图1：单层/双层结构及 HC/CC/HX 三种单层 CDW 与 HC-HC、HC-CC 双层 blend 的位移构型](../../raw/figures/cossuStackingChargedensityWaves2024/fig_1_Q8LV7XLD.png)
  - ![图2：七种关键 CDW 堆叠构型的轴测视图](../../raw/figures/cossuStackingChargedensityWaves2024/fig_2_T57PVLQW.png)
  - ![图3：对称态与三种最稳定 CDW 构型的总态密度（E_F 附近赝能隙）](../../raw/figures/cossuStackingChargedensityWaves2024/fig_3_IFCX25A7.png)
  - ![图4：GGA+DF 下各 CDW 构型的 Se-Se 键长斑块模式](../../raw/figures/cossuStackingChargedensityWaves2024/fig_4_Q3DQNIFN.png)
  - ![图5：正常相、单层 HC 与双层三种 CDW 的恒流模式模拟 STM 图像（-0.2 V）](../../raw/figures/cossuStackingChargedensityWaves2024/fig_5_GXNU2V27.png)
  - ![图6：(h,k,0) 平面几何结构因子——左列结构数据、右列费米能级附近部分电荷密度](../../raw/figures/cossuStackingChargedensityWaves2024/fig_6_Q5Z2ZLRD.png)
  - ![图7：纯 GGA（无 vdW 修正）下的补充 STM 模拟](../../raw/figures/cossuStackingChargedensityWaves2024/fig_7_DY75UYF5.png)
  - ![图8：基态 HC-HC_(S3) 在不同偏压下的 STM 图像](../../raw/figures/cossuStackingChargedensityWaves2024/fig_8_U6BTPHHS.png)
  - ![图9：结构因子原始数据点（附录 B）](../../raw/figures/cossuStackingChargedensityWaves2024/fig_9_TJ7WPXTW.png)
  - ![表II：双层与单层 CDW 相对能量（GGA 与 GGA+DF，meV/f.u.）](../../raw/figures/cossuStackingChargedensityWaves2024/tab_2_X3L9MSGS.png)

- **项目连接**：project-7 CDW（电荷密度波）。本文直接对应 CDW 层间堆叠与维度效应，是 project-7 的核心理论参考；对 project-5 SnTe 铁电模拟中涉及的层间耦合/堆叠方法学有间接借鉴意义。

- **组织与用词**：
  文章按"引言（1T 型金属-绝缘体转变启发 → 金属性 2H 型是否同样存在堆叠效应）→ 方法（DFT/PBE+多种 vdW 修正、3×3 超胞、Tersoff-Hamann STM 模拟）→ 结果（正常相结构、CDW 能量景观、电子结构、Se 图案与 STM、电荷密度与结构因子）→ 讨论与结论（推广至薄膜/块体、展望磁性/压力/扭转/拉曼）"的经典链条展开。论证策略是：先用多种 vdW 方案标定基准结构（表 I），再系统枚举 blend × displacement 构型得到能量层级（表 II），然后分别从实空间（STM 图 5）和倒空间（结构因子图 6）给出可实验检测的指纹，最后将结论从 1T 推广到金属性 2H 型 TMDs。

  可复用术语（中英对照）：
  1. 电荷密度波（Charge-Density Wave, CDW）
  2. 周期性晶格畸变（Periodic Lattice Distortion, PLD）
  3. 混合物 / 位移（blend / displacement）
  4. 空心中心三角 / 硫族中心三角 / 六方结构（HC / CC / HX）
  5. 层间耦合（interlayer coupling）
  6. 范德华修正（van der Waals correction；D2、TS、DF、MBD@FI）
  7. 几何结构因子（geometric structure factor）
  8. 赝能隙 / 费米能级态耗尽（pseudogap / depletion of states at E_F）
  9. 恒流模式 STM 表观高度与起伏（constant-current STM apparent height / corrugation）
  10. 电子-声子耦合（electron-phonon coupling）

- **可写入wiki的要点**：
  1. 2H-NbSe₂ 双层是保持块体中心反演对称性的最小单元，两层单层彼此旋转 π；正常相空间群 P3m1，CDW 态下降为 C2/m（HC-HC 全部位移）、P3m1（HC-CC，除 S2 外）、C1（HC-CC_(S2)）、P1（CC-CC_(S2)）或 Cm（CC-CC 其他位移）。
  2. 三种最稳定的单层 CDW 模式为 HC（hollow-centered triangular）、CC（chalcogen-centered triangular）、HX（hexagonal）；其在 1H-NbSe₂ 单层中的相对能量（GGA+DF）为 HC=0、CC=1.43、HX=2.06 meV/f.u.。
  3. 双层基态为 HC-HC_(S3)（GGA 与 GGA+DF 一致），第一激发态 HC-HC_(S1)（0.06 / 0.21 meV/f.u.），第二激发态为混合堆叠 HC-CC_(S4)（0.18 / 0.39 meV/f.u.）；前三激发态能量窗口仅 0.18（GGA）/0.39（GGA+DF）meV/f.u.，小于单层 HC–CC 差，预示多种堆叠可在缺陷或热激发下共存。
  4. vdW 修正显著改变层间距：GGA 给出 d_Nb-Nb=6.926 Å、d_Se-Se=3.560 Å；GGA+TS 给出 6.053 / 2.732 Å（TS 过度束缚，混合 blend 无法收敛到正确对称性）；GGA+DF 给出 6.527 / 3.141 Å（主文采用，与块体实验值 c/2≈6.27 Å 同量级）；GGA+MBD@FI 给出 6.178 / 2.844 Å。
  5. 计算参数：VASP + PAW + PBE，平面波截断 500 eV；原胞 k 网格 45×45×1、3×3 超胞 20×20×1；结构弛豫力收敛至 10⁻³ eV/Å，电子步能量容差 10⁻⁷–10⁻⁹ eV；面内晶格常数固定为 3.45 Å，z 方向真空层 20 Å。
  6. 电子结构证据：不同堆叠整体 DOS 相似，但 HC-CC_(S4) 在 −1.8 eV 出现尖锐峰，投影 DOS 指认为层间 Se 原子的 p_z 轨道杂化，是层间耦合的直接电子指纹；CDW 能量增益与费米能级处态密度耗尽程度呈正相关，将一维 Peierls 逻辑推广到由动量依赖电声耦合驱动的二维 NbSe₂。
  7. STM 模拟（Tersoff-Hamann，−0.2 V 偏压、电流等高线最大值 5.8 Å）：无 CDW 对称双层 corrugation 13 pm，CDW 双层 29–39 pm，单层 HC 51 pm；绿斑位置构成指纹——HC-HC_(S3) 位于三叶状凸起之一、HC-HC_(S1) 位于凹陷之一、HC-CC_(S4) 位于所有尖端；绿斑表观高度差分别为 2、4–5、6 pm，现代 STM 垂直分辨率（<10 pm）足以分辨。
  8. 几何结构因子：结构数据（模拟 XRD）中 CDW 峰被强布拉格峰掩盖，但差异图（c/e）形状可区分；费米能级附近部分电荷密度（模拟 FT-STM）中 CDW 峰位于中心点到一级布拉格峰距离的 1/3 处，呈六重星状，HC-HC_(S3) 与 HC-CC_(S4) 的差异图案（d/f）显著不同，为 XRD、TEM、EELS 实验提供补充判据。
  9. Se-Se 键长斑块规律：每一 blend 中能量最低构型（HC-HC_(S3)、HC-CC_(S4)）对应上下两层 Se-Se"斑块"不重叠；作者推测层间 p_z 轨道相干性最大化是稳定机制，是对 Lin et al.（Nano Lett. 2022）轴向键合维度效应机制的推广。
  10. 热稳定性估计：与 1T-TaS₂ 块体两堆叠态能量差 0.08 meV/f.u. 对应约 60 K 锁定温度相比，2H-NbSe₂ 双层 0.18–0.39 meV/f.u. 的激发能预示在实验 CDW 临界温度（~33 K）以下堆叠应稳定；原子位移仅 ~0.2 Å 且非完全同相，振动熵修正估计 <0.04 meV/f.u.，不足以翻转表 II 能量层级；作者明确指出精确结论需声子谱计算，但不在本文范围。
