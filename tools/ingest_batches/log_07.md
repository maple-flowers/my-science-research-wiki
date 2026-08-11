# Batch 07 文献阅读日志

## 1. wuSlidingFerroelectricity2D2021a — 二维范德华材料中的滑移铁电性

- **元数据**：Menghao Wu, Ju Li，2021，PNAS（Perspective），DOI 10.1073/pnas.2115703118
- **一句话**：提出层间滑移可在二维范德华材料中产生垂直方向可翻转极化的"滑移铁电性"，并系统给出判据、材料清单与"ripplocation"畴壁图像。
- **现有wiki双链**：
  - [[../../wiki/concepts/sliding-ferroelectricity]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/ferroelasticity]]、[[../../wiki/concepts/moire-superlattice]]、[[../../wiki/concepts/polarization-switching]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/topological-defects]]
  - [[../../wiki/entities/h-BN]]、[[../../wiki/entities/TMDs]]、[[../../wiki/entities/WTe2]]、[[../../wiki/entities/VASP]]
  - [[../../wiki/figures/domain-walls]]、[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/heterostructures-stacking]]
  - [[../../wiki/write/2021]]
  - [[../../raw/note/wuSlidingFerroelectricity2D2021a]]
- **新概念/实体建议**：
  - 滑移铁电判据（sliding-FE criterion）：非中心对称且存在可通过层间平移到达的水平镜面对称态；建议文件名 `sliding-fe-criterion.md`
  - 褶皱位错（ripplocation）：滑移铁电体中结合面内位错与面外褶皱的低能畴壁；建议 `ripplocation.md`
  - 摩尔铁电性（moiré ferroelectricity）：转角双层体系中莫尔周期调制的层间滑移极化；建议 `moire-ferroelectricity.md`
  - 金属铁电性（metallic ferroelectricity）：WTe₂ 等半金属中由滑移产生的可翻转极化；建议 `metallic-ferroelectricity.md`
- **图表**：
  - ![滑移铁电原理与材料分类](../../raw/figures/wuSlidingFerroelectricity2D2021a/fig_1_37UWP3F7.png)
  - ![BN等双层滑移极化曲线](../../raw/figures/wuSlidingFerroelectricity2D2021a/fig_2_UQ8NW6V3.png)
  - ![ripplocation畴壁示意](../../raw/figures/wuSlidingFerroelectricity2D2021a/fig_3_MVR597PP.png)
  - ![WTe2金属铁电与莫尔铁电](../../raw/figures/wuSlidingFerroelectricity2D2021a/fig_5_FQBZIJ7L.png)
  - ![各材料极化值表](../../raw/figures/wuSlidingFerroelectricity2D2021a/tab_1_XD6YJ7L4.png)
- **项目连接**：与 project-5（SnTe 铁电模拟）在二维铁电机理与 Berry 相极化计算上相通；可作为 2D 铁电材料库扩展到其他 vdW 体系。
- **组织与用词**：Perspective 体例，按"物理图像→判据→材料清单→畴壁与莫尔→金属铁电→应用展望"层层推进。可复用术语：滑移铁电 (sliding ferroelectricity)、层间平移 (interlayer translation)、褶皱位错 (ripplocation)、Peierls 势垒 (Peierls barrier)、集体翻转势垒 (collective switching barrier)、铁电非线性反常霍尔效应 (ferroelectric nonlinear anomalous Hall effect)。
- **可写入wiki的要点**：
  - 一般判据：双层非中心对称，且存在可由层间平移到达的水平镜面对称态，则层间滑移可翻转垂直极化。
  - 极化量级（单层相对滑移，pC/m）：h-BN 2.08、ZnO 8.22、AlN 10.29、GaN 9.72、SiC 6.17、MoS₂ 0.97、InSe 0.24；3R 体相以 μC/cm² 计。
  - 畴壁为"ripplocation"，Peierls 势垒仅 meV/unit cell，导致集体翻转势垒极低但孤立层翻转势垒很高（看似矛盾的"低集体势垒+高孤立势垒"）。
  - WTe₂ 是首个金属滑移铁电体，P≈0.16 pC/m，Tc≈350 K；并预言铁电非线性反常霍尔效应。
  - 转角 h-BN 莫尔超晶格中可出现莫尔铁电性，为电场可调的莫尔势阱提供新自由度。

---

## 2. Wu2021 — Ge 二聚体在 c(4×2) 重构 Si(001) 表面的吸附：DFTB 研究

- **元数据**：Lijun Wu 等，2021，Computational Materials Science 187, 110120，DOI 10.1016/j.commatsci.2020.110120
- **一句话**：用 DFTB 系统扫描 774 个 Ge 二聚体在重构 Si(001) 表面的初始构型，得到 22 种稳定结构（8 类吸附模式），并发现带隙变化主要源于 Si 表面扰动而非 Ge 本身。
- **现有wiki双链**：
  - [[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/binding-strength]]、[[../../wiki/concepts/bond-density]]、[[../../wiki/concepts/2D-materials]]
  - [[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/electronic-bands]]
  - [[../../wiki/write/2021]]
  - [[../../raw/note/Wu2021]]
- **新概念/实体建议**：
  - DFTB（密度泛函紧束缚）：大体系表面吸附的半经验量子模拟方法；建议 `dftb.md`
  - c(4×2) 重构 Si(001)：低温下 Si(001) 二聚体行的 buckling 反铁电排列；建议 `si001-c4x2-reconstruction.md`
  - 吸附构型谱系（DVTS/DVBS/MHS/DPBS/DITS/DHS 等）：Ge 二聚体在 Si(001) 上的构型分类；建议 `ge-dimer-adsorption-modes.md`
- **图表**：
  - ![Ge二聚体吸附模式分类](../../raw/figures/Wu2021/fig_1_W6FHVP2A.png)
  - ![8类稳定构型结构](../../raw/figures/Wu2021/fig_3_CMVVBG5C.png)
  - ![Mulliken电荷与带隙变化](../../raw/figures/Wu2021/fig_7_AFM89M3Y.png)
  - ![稳定构型能量与带隙表](../../raw/figures/Wu2021/tab_1_B4DKJGTV.png)
- **项目连接**：无直接项目连接；属于表面吸附/半导体异质结基础模拟，方法学上与 project-5（SnTe 铁电模拟）的 DFT 工作流可互为参照。
- **组织与用词**：标准计算材料学论文，"方法→构型扫描→分类→电子结构→结论"。可复用术语：紧束缚近似 (tight-binding)、Mulliken 布居 (Mulliken population)、二聚体空位 (dimer vacancy)、背键 (back-bond)、带隙工程 (band-gap engineering)、重构表面 (reconstructed surface)。
- **可写入wiki的要点**：
  - 扫描参数：高度 h=1.0–5.2 Å，取向角 θ=0–170°，共 774 个初始构型，收敛至 22 种稳定结构，归为 8 类模式（DVTS、DVBS、MHS、DPBS、DITS、MHS+MBS、DPTS、DHS）。
  - 体系带隙可在 0.082–0.536 eV 范围内调控（跨度 0.454 eV），提供可调纳米电子平台。
  - Mulliken 电荷分析表明带隙变化主要由 Si 表面受扰动引起，而非 Ge 二聚体自身的电子态——这是反直觉但重要的机理结论。
  - DFTB 在大构型空间扫描中兼顾精度与效率，可作为高通量表面吸附筛选的方法模板。

---

## 3. cheongMultiferroicsMagneticTwist2007a — 多铁性材料：磁性扭曲

- **元数据**：Sang-Wook Cheong, Maxim Mostovoy，2007，Nature Materials 6, 13–20，DOI 10.1038/nmat1804
- **一句话**：经典综述，系统阐述"磁性失配驱动铁电极化"的非本征多铁性物理，建立螺旋序 P∝e₃×Q 与交换收缩 ↑↑↓↓ 两大机理范式。
- **现有wiki双链**：
  - [[../../wiki/concepts/multiferroicity]]、[[../../wiki/concepts/magnetoelectric-coupling]]、[[../../wiki/concepts/topological-defects]]、[[../../wiki/concepts/spin-orbit-coupling]]、[[../../wiki/concepts/2D-materials]]
  - [[../../wiki/entities/BiFeO3]]、[[../../wiki/entities/HoMnO3]]
  - [[../../wiki/figures/domain-walls]]、[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/mathematical-models]]
  - [[../../wiki/write/2007]]
  - [[../../raw/note/cheongMultiferroicsMagneticTwist2007a]]
- **新概念/实体建议**：
  - 本征/非本征铁电（proper/improper ferroelectricity）：极化由自旋序诱导而非软模驱动；建议 `proper-improper-fe.md`
  - Dzyaloshinskii–Moriya 相互作用与螺旋序极化 P∝e₃×Q；建议 `dm-spiral-polarization.md`
  - 交换收缩（exchange striction）：共线 ↑↑↓↓ 序中等价键不等长导致极化；建议 `exchange-striction.md`
  - 电磁振子（electromagnon）：磁序与电极化耦合的集体激发；建议 `electromagnon.md`
  - 环向矩（toroidal moment）：破坏空间反演与时间反演的三阶张量序参量；建议 `toroidal-moment.md`
- **图表**：
  - ![多铁性材料分类与机理总览](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_1_D8A9TF3K.png)
  - ![螺旋序与P∝e3×Q几何关系](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_2_PNAIBBQF.png)
  - ![RMn2O5交换收缩与TbMnO3极化翻转](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/fig_6_7B4LX9VV.png)
  - ![多铁性材料性质汇总表](../../raw/figures/cheongMultiferroicsMagneticTwist2007a/tab_1_X3QYE982.png)
- **项目连接**：project-2（Mn 多铁性）核心参考文献；直接为 Mn 基多铁性（RMnO₃、RMn₂O₅）的磁电耦合机理提供理论框架。
- **组织与用词**：综述按"本征 vs 非本征→螺旋序→共线序→磁电耦合→畴与拓扑→展望"组织。可复用术语：磁性失配 (magnetic frustration)、螺旋自旋序 (spiral spin order)、极化翻转 (polarization flop)、锥磁序 (conical magnet)、居里–外斯温度 (Curie–Weiss temperature)、磁电耦合 (magnetoelectric coupling)。
- **可写入wiki的要点**：
  - 非本征多铁中极化由磁序诱导，量级约 10⁻² μC/cm²，比本征铁电小 2–3 个数量级。
  - 螺旋序 + DM 相互作用给出 P ∝ e₃×Q（e₃ 为自旋旋转轴，Q 为螺旋波矢）；典型体系 TbMnO₃、DyMnO₃。
  - 共线 ↑↑↓↓ 序通过交换收缩产生极化（RMn₂O₅）；TbMn₂O₅ 可由脉冲磁场实现 180° 极化翻转。
  - 强磁电响应：TbMnO₃ 在 ~5 T 磁场下极化 flop；DyMnO₃ 介电常数变化达 500%。
  - 磁失配判据：Curie–Weiss 温度远大于 Néel 温度（如 YMn₂O₅ T_CW≈250 K vs T_N≈45 K），是强失配的标志。

---

## 4. liFerroelasticityDomainPhysics2016 — 单层 1T′ TMD 中的铁弹性与畴物理

- **元数据**：Wenbin Li, Ju Li，2016，Nature Communications 7, 10843，DOI 10.1038/ncomms10843
- **一句话**：第一性原理预言单层 1T′ TMD（MoTe₂、WTe₂ 等）具有铁弹性，三个取向变体可由百分之几的应变切换，势垒 <0.2 eV/f.u.，可实现二维形状记忆。
- **现有wiki双链**：
  - [[../../wiki/concepts/ferroelasticity]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/strain-engineering]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/topological-defects]]
  - [[../../wiki/entities/TMDs]]、[[../../wiki/entities/WTe2]]、[[../../wiki/entities/VASP]]
  - [[../../wiki/figures/domain-walls]]、[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/mathematical-models]]
  - [[../../wiki/write/2016]]
  - [[../../raw/note/liFerroelasticityDomainPhysics2016]]
- **新概念/实体建议**：
  - Peierls 畸变（Peierls distortion）：1T′ 相一维金属态失稳形成二聚化带隙；建议 `peierls-distortion.md`
  - 取向变体（orientation variant）：Peierls 畸变方向不同形成的 O1/O2/O3 等价畴；建议 `orientation-variant.md`
  - 二维形状记忆效应（2D shape memory）：铁弹应变可热/力回复；建议 `2d-shape-memory.md`
  - 格林–拉格朗日应变张量（Green–Lagrange strain）；建议 `green-lagrange-strain.md`
- **图表**：
  - ![1T′TMD三种取向变体与Peierls畸变](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_1_YTRF2PW6.png)
  - ![应变-能量相图与共切线](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_3_A8FT3APU.png)
  - ![NEB翻转势垒与畴壁能](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_5_XYSVC9LT.png)
  - ![铁弹翻转示意图](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_7_BRNW8WQ3.png)
- **项目连接**：与 project-5（SnTe 铁电模拟）共享铁弹/铁电畴与应变工程主题；方法上 VASP+NEB 可复用。
- **组织与用词**："结构识别→变体对称性→应变相变曲线→NEB 翻转→畴壁→形状记忆"。可复用术语：铁弹翻转 (ferroelastic switching)、共切线构造 (common tangent construction)、NEB（nudged elastic band）、畴壁能 (domain-wall energy)、相变应变 (transformation strain)、二聚化 (dimerization)。
- **可写入wiki的要点**：
  - 1T′ TMD 单层由 Peierls 畸变产生三种取向变体 O1/O2/O3，相互夹角 60°/120°。
  - 铁弹翻转仅需 1–4% 应变，NEB 势垒 <0.2 eV/f.u.（对应约 0.2 ns 时间尺度），远低于 1T′→2H 的 0.8 eV。
  - 变换应变张量 e₂₁ = [0.034, −0.019; −0.019, −0.030]（Green–Lagrange），共切线出现在 1–4% 应变区间。
  - 畴壁形成能约 50 meV/Å，畴壁可运动并具有各向异性。
  - 提出二维形状记忆合金概念：铁弹畴的热/力可逆重排。

---

## 5. Huang2023two — 双光子三重荧光二氰基二苯乙烯探针

- **元数据**：Chi-Bao Huang，2023，Journal of Cytology & Histology Research 2(1), 1，DOI 10.47363/JCHR/2023(2)108
- **一句话**：设计两种二甲氨基/二苯氨基给体的二氰基二苯乙烯探针，首次观测到 LE–TICT–激基复合物三重荧光，并在环己烷中实现 5560/6670 GM 的双光子吸收截面。
- **现有wiki双链**：
  - [[../../wiki/concepts/giant-spin-splitting]]（仅作共轭电子结构旁证，关联弱）
  - [[../../wiki/figures/optical-spectra]]
  - [[../../wiki/write/2023]]
  - [[../../raw/note/Huang2023two]]
- **新概念/实体建议**：
  - TICT（twisted intramolecular charge transfer，扭转分子内电荷转移）；建议 `tict-state.md`
  - 双光子吸收截面（two-photon absorption cross section, GM）；建议 `two-photon-cross-section.md`
  - 溶致变色（solvatochromism）与三重荧光（triple fluorescence: LE/TICT/exciplex）；建议 `triple-fluorescence.md`
  - 二氰基二苯乙烯（dicyanostilbene）D–π–A 荧光团骨架；建议 `dicyanostilbene-dyes.md`
- **图表**：无关键图（笔记未抽取图片）
- **项目连接**：project-1（双光子）直接相关——提供 TPA 截面量级、溶剂依赖规律及生物窗口（790 nm 激发）的分子设计参考。
- **组织与用词**："合成→光物理表征→溶剂效应→双光子→生物成像"。可复用术语：扭转分子内电荷转移 (TICT)、局域激发态 (LE state)、激基复合物 (exciplex)、双光子吸收 (TPA)、量子产率 (quantum yield)、Wittig–Horner 反应。
- **可写入wiki的要点**：
  - 探针 1a（二甲氨基给体）发射从环己烷 445 nm 红移到 DMSO 641 nm，位移 196 nm，是强溶致变色。
  - δ_TPA 最大值：1a 为 5560 GM，1b 为 6670 GM（环己烷）；在 DMF 中骤降至约 130 GM，说明 TICT 抑制双光子响应。
  - 激发波长 790 nm，处于生物透明窗口，适用于双光子生物成像。
  - 首次报道双光子三重荧光：LE 带、TICT 带和激基复合物 E 带（约 542 nm）。
  - 荧光量子产率 Φ 在二氧六环中高达 0.812，在 DMSO 中仅 0.013，反映非辐射 TICT 衰减。

---

## 6. Unknown2003charge — (BEDT-TTF)₁.₅CuX₂ (X=Cl, Br) 的电荷转移与混合价态

- **元数据**：Young-Inn Kim，2003，Bulletin of the Korean Chemical Society 24(9), 1389–1392，DOI 10.5012/bkcs.2003.24.9.1389
- **一句话**：合成并表征 (BEDT-TTF)₁.₅CuX₂，证明 Cu 为 II/I 混合价，Br 化合物残留更多 Cu(II) 且电导率低一个数量级，库仑散射主导输运。
- **现有wiki双链**：
  - [[../../wiki/concepts/charge-density-wave]]、[[../../wiki/concepts/bond-density]]、[[../../wiki/concepts/electron-counting-rule]]
  - [[../../wiki/figures/vibrational-spectra]]、[[../../wiki/figures/optical-spectra]]、[[../../wiki/figures/crystal-structures]]
  - [[../../wiki/write/2003]]
  - [[../../raw/note/Unknown2003charge]]
- **新概念/实体建议**：
  - BEDT-TTF（ET，双乙撑二硫四硫富瓦烯）有机给体分子；建议 `bedt-ttf.md`
  - 混合价 Cu(II/I) 与 EPR 四线超精细结构；建议 `mixed-valence-cu.md`
  - 库仑散射（Coulomb scattering by local moments）；建议 `coulomb-scattering.md`
  - 电荷转移盐（charge-transfer salt）；建议 `charge-transfer-salt.md`
- **图表**：
  - ![EPR谱与Cu(II)四线超精细](../../raw/figures/Unknown2003charge/fig_1_PVI4APFY.png)
  - ![IR中A1g振动激活指示BEDT-TTF电离](../../raw/figures/Unknown2003charge/fig_2_UB562FUX.png)
  - ![磁化率与磁矩数据表](../../raw/figures/Unknown2003charge/tab_1_AJ7CFCDI.png)
- **项目连接**：project-4（TTF 分子计算）直接相关——为 TTF 基电荷转移盐的混合价、电导率与振动光谱判据提供实验参照。
- **组织与用词**："合成→组成分析→EPR/SQUID/CV 价态→IR/UV-Vis-NIR 电离度→电导率→机理"。可复用术语：混合价 (mixed valence)、有效磁矩 (effective magnetic moment)、居里常数 (Curie constant)、A1g 振动激活、部分电离 (partial ionization)、库仑散射。
- **可写入wiki的要点**：
  - EPR 显示 g∥>g⊥>2.0 及四线超精细，证实 Cu(II) 存在；SQUID 有效磁矩 1.26/1.22 BM < 1.73 BM，说明大部分 Cu 被还原为 Cu(I)。
  - Br 化合物居里常数 0.53 大于 Cl 的 0.39，即 Br⁻ 给电子能力弱于 Cl⁻，残留更多 Cu(II)。
  - 电导率：Cl 盐 9.4×10⁻⁵ S/cm，Br 盐 8.5×10⁻⁶ S/cm；Cu(II) 局域磁矩对载流子的库仑散射是主要散射源。
  - BEDT-TTF 部分电离由 IR 中 ~1400/1330 cm⁻¹ A1g 模激活及 UV-Vis-NIR ~970 nm 带证实。
  - 要使 CuX₂ 完全还原，BEDT-TTF:CuX₂ 摩尔比需超过 2:1。

---

## 7. wangScreeningEnabledChemiresistiveMoisture2025 — 屏蔽效应赋能的 M₂(TTFTB) MOF 化学电阻型湿敏传感

- **元数据**：Yingchao Wang 等（Lei Sun 组，西湖大学），2025，JACS 147(52), 48158–48165，DOI 10.1021/jacs.5c16110
- **一句话**：单晶 M₂(TTFTB) 导电 MOF 中，水分子通过屏蔽 TTF•⁺ 空穴–阴离子库仑陷阱使电导提升 >10³ 倍，Zn 类似物因 Zn²⁺ 库仑势强而仅 ~10²。
- **现有wiki双链**：
  - [[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/binding-strength]]、[[../../wiki/concepts/deformation-potential]]（载流子散射旁通）
  - [[../../wiki/figures/electronic-devices]]、[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/vibrational-spectra]]
  - [[../../wiki/write/2025]]
  - [[../../raw/note/wangScreeningEnabledChemiresistiveMoisture2025]]
- **新概念/实体建议**：
  - 导电 MOF（conductive MOF, M₂(TTFTB)）：π 堆叠 TTF 柱提供一维导电通道；建议 `conductive-mof.md`
  - 库仑陷阱屏蔽（Coulomb-trap screening by water）；建议 `coulomb-trap-screening.md`
  - 化学电阻型传感（chemiresistive sensing）；建议 `chemiresistive-sensing.md`
  - TTF•⁺ 自由基阳离子柱（TTF radical-cation column）；建议 `ttf-radical-column.md`
- **图表**：
  - ![M2(TTFTB)结构与TTF柱](../../raw/figures/wangScreeningEnabledChemiresistiveMoisture2025/fig_1_MXBQAIX7.png)
  - ![湿度响应开关曲线与on/off比](../../raw/figures/wangScreeningEnabledChemiresistiveMoisture2025/fig_2_NPPDW9RW.png)
  - ![EIS Nyquist图与活化能](../../raw/figures/wangScreeningEnabledChemiresistiveMoisture2025/fig_4_RPGH3YNP.png)
  - ![四种金属MOF对比与机理解释](../../raw/figures/wangScreeningEnabledChemiresistiveMoisture2025/fig_6_CWIG2WCN.png)
- **项目连接**：project-6（湿度传感器）核心文献；project-4（TTF 分子计算）在 TTF•⁺ 电子结构层面相关。
- **组织与用词**："材料→器件响应→排除竞争机理→金属对照→设计原则"。可复用术语：化学电阻 (chemiresistor)、库仑陷阱 (Coulomb trap)、π 堆叠 (π-stacking)、Nyquist 图、活化能 (activation energy)、有效核电荷 (Z_eff/r)、直流极化 (DC polarization)。
- **可写入wiki的要点**：
  - M₂(TTFTB)（M=Mn、Co、Zn、Cd；TTFTB=四苯甲酸 TTF）沿 c 轴形成 π 堆叠 TTF 柱，是导电各向异性来源。
  - 湿度使电导升高：Mn/Co/Cd 的 on/off >10³，Zn 仅 ~10²，因为 Zn²⁺ 的 Z_eff/r 高、对空穴束缚更强，水屏蔽不足以完全解除陷阱。
  - 系统排除 O₂ 掺杂（EPR 不变）、本征迁移率变化（PXRD 显示干态 c 轴收缩但电导反降）和质子传导（线性 I–V、半圆 Nyquist、致密 Pt 电极、10 V 下 2000 s DC 极化衰减 <8%）。
  - 设计原则：选择载流子–反离子相互作用弱的金属节点，可最大化湿度响应。
  - 为化学电阻型湿度传感提供了"陷阱屏蔽"这一区别于质子传导的新机理范式。

---

## 8. tianRoomtemperatureTwodimensionalMultiferroic2026 — 室温二维多铁性金属：双层 CrTe₂

- **元数据**：Dacheng Tian 等（Kehui Wu、Suhuai Wei、Lan Chen 等合作），2026，Nature Materials 25(6), 956–963，DOI 10.1038/s41563-026-02537-2
- **一句话**：MBE 生长的双层 CrTe₂/石墨烯/SiC 在室温下同时具有铁磁性（2.44 μB/Cr）和可翻转面外铁电性（PFM 矫顽 1–2 V），通过层间电荷转移实现"电写磁读"。
- **现有wiki双链**：
  - [[../../wiki/concepts/multiferroicity]]、[[../../wiki/concepts/magnetoelectric-coupling]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/spin-orbit-coupling]]、[[../../wiki/concepts/polarization-switching]]
  - [[../../wiki/entities/CrTe2]]、[[../../wiki/entities/VASP]]
  - [[../../wiki/figures/electronic-devices]]、[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/heterostructures-stacking]]
  - [[../../wiki/write/2026]]
  - [[../../raw/note/tianRoomtemperatureTwodimensionalMultiferroic2026]]
- **新概念/实体建议**：
  - 二维多铁性金属（2D multiferroic metal）：铁磁序与可翻转极化在金属中共存；建议 `2d-multiferroic-metal.md`
  - 层间电荷转移铁电机理（interlayer charge-transfer ferroelectricity）：非 SOC 机制，由 FM 层部分填充 Cr-e_g 轨道驱动；建议 `interlayer-ct-ferroelectricity.md`
  - 电写磁读（electric-write magnetic-read）；建议 `electric-write-magnetic-read.md`
  - z 型反铁磁单层（z-type AFM monolayer）；建议 `z-type-afm.md`
- **图表**：
  - ![双层CrTe2结构与MBE生长](../../raw/figures/tianRoomtemperatureTwodimensionalMultiferroic2026/fig_1_USCG2SF4.png)
  - ![STM/SP-STM磁结构与铁电PFM](../../raw/figures/tianRoomtemperatureTwodimensionalMultiferroic2026/fig_2_WFPFNDUZ.png)
  - ![电写磁读盒中图与磁场响应](../../raw/figures/tianRoomtemperatureTwodimensionalMultiferroic2026/fig_3_85N9YJPF.png)
  - ![DFT+U层间电荷转移机理](../../raw/figures/tianRoomtemperatureTwodimensionalMultiferroic2026/fig_4_QKXBGTR6.png)
- **项目连接**：project-2（Mn 多铁性）高度相关——CrTe₂ 虽非 Mn 基，但提供了室温二维多铁与电写磁读的新机理（电荷转移而非 SOC），可作为 Mn 基多铁设计的对照范式。
- **组织与用词**："生长→磁结构→铁电表征→电写磁读→机理→稳定性"。可复用术语：分子束外延 (MBE)、自旋极化 STM (SP-STM)、压电力显微镜 (PFM)、磁力显微镜 (MFM)、层间电荷转移 (interlayer charge transfer)、e_g 轨道 (e_g orbital)、空气稳定性 (air stability)。
- **可写入wiki的要点**：
  - 单层 CrTe₂ 为 z 型 AFM（晶格 0.37 nm，zigzag SP-STM 条纹 a=0.74、b=0.64 nm）；第二层为 FM（0.39 nm，六角）。
  - 室温铁磁：2.44 μB/Cr（20 K）；面外铁电极化 P≈3.0 pC/m，PFM 矫顽电压 1–2 V。
  - ±6–8 V 写盒中图，MFM 镜像反转，实现电写磁读；磁场至 1300 Oe 使两者信号均减弱。
  - 新机理：层间电荷转移约 0.019–0.020 C/m²，由 FM 层部分填充 Cr-e_g 轨道引起，静电势差约 0.1 eV；不是自旋–轨道耦合机制。
  - 空气稳定性：数周后信号约保留 30%（2 周）。

---

## 9. gongAbsenceCriticalThickness2023 — (PTO)n/(STO)n 超晶格中极斯格明子不存在临界厚度

- **元数据**：Feng-Hui Gong 等（Xiu-Liang Ma 组），2023，Nature Communications 14, 3376，DOI 10.1038/s41467-023-39169-y
- **一句话**：(PTO)n/(STO)n 超晶格中 Kittel 定律 d∝√h 在 h<~4 nm 失效，极斯格明子在 2 个单胞（~0.8 nm）PTO 中仍存在，突破铁电临界厚度。
- **现有wiki双链**：
  - [[../../wiki/concepts/topological-defects]]、[[../../wiki/concepts/polarization-switching]]、[[../../wiki/concepts/super-paraelectricity]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/ferroelasticity]]
  - [[../../wiki/figures/domain-walls]]、[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/mathematical-models]]
  - [[../../wiki/write/2023]]
  - [[../../raw/note/gongAbsenceCriticalThickness2023]]
- **新概念/实体建议**：
  - 极斯格明子（polar skyrmion）：铁电材料中的拓扑极性织构；建议 `polar-skyrmion.md`
  - Kittel 定律（Kittel's law d∝√h）及其在超薄限域下的失效；建议 `kittels-law.md`
  - 双曲 d–h 关系（hyperbolic d-h relation, d = ah + b/h + c）；建议 `hyperbolic-domain-scaling.md`
  - 退极化场（depolarization field）与绝缘边界条件；建议 `depolarization-field.md`
  - 拓扑数 N_Q（topological charge/number）；建议 `topological-number-nq.md`
- **图表**：
  - ![PTO/STO超晶格与极斯格明子HAADF-STEM](../../raw/figures/gongAbsenceCriticalThickness2023/fig_1_SYSSN7EC.png)
  - ![周期d-厚度h双曲标度](../../raw/figures/gongAbsenceCriticalThickness2023/fig_2_7DNARR37.png)
  - ![2-u.c.PTO中斯格明子与拓扑数映射](../../raw/figures/gongAbsenceCriticalThickness2023/fig_4_4ADC7YNR.png)
- **项目连接**：与 project-5（SnTe 铁电模拟）共享极性拓扑、退极化场与相场模拟主题；与 project-2（Mn 多铁性）在拓扑织构层面间接相关。
- **组织与用词**："PLD 生长→STEM 极化映射→d–h 标度→极薄极限→相场/DFT 机理→电极效应"。可复用术语：脉冲激光沉积 (PLD)、HAADF-STEM、单胞 (unit cell, u.c.)、相场模拟 (phase-field simulation)、LSMO 电极、可见–近红外吸收。
- **可写入wiki的要点**：
  - n 从 37 降至 2 u.c.；Kittel 的 √h 标度在 h<~4 nm 破坏，d 平台于 ~5–6 nm 或略升。
  - 实验双曲拟合 d = 0.68h + 2.17/h + 3.24；相场两组拟合 d = 0.72h + 3.73/h + 4.48 和 d = 1.32h + 4.10/h + 2.48。
  - 极斯格明子在 2-u.c. PTO（~0.8 nm）仍存在，拓扑数 N_Q=−1 贯穿，低于常规铁电临界厚度（~3 u.c.）。
  - 退极化场需要绝缘边界；LSMO 导电电极抑制斯格明子，证实边界条件的关键作用。
  - 矫顽电压低至 1.2 V，可见光吸收增强，提示光电器件潜力。

---

## 10. fornerQuantumTemperatureEffects1993 — Davydov 孤子动力学中的量子与温度效应 III：链间耦合

- **元数据**：Wolfgang Förner，1993，Journal of Physics: Condensed Matter 5(7), 823–840，DOI 10.1088/0953-8984/5/7/009
- **一句话**：数值模拟证明 Scott "单链等效三链"猜想在 |D₂⟩ 态普适但在 |D₁⟩ 态 A 模式下失效，并指出氢键力常数 W>30–40 N/m 是 Davydov 孤子在 300 K 存在的阈值。
- **现有wiki双链**：
  - [[../../wiki/figures/mathematical-models]]
  - [[../../wiki/write/1993]]
  - [[../../raw/note/fornerQuantumTemperatureEffects1993]]
- **新概念/实体建议**：
  - Davydov 孤子（Davydov soliton）：酰胺-I 振动与氢键声子耦合的自陷态；建议 `davydov-soliton.md`
  - 拟设态 |D₁⟩/|D₂⟩（ansatz states，量子/经典晶格）；建议 `d1-d2-ansatz.md`
  - 链间耦合（interchain coupling, L≈1.54 meV）与 Scott 三倍参数猜想；建议 `interchain-coupling.md`
  - 酰胺-I 振动（amide-I vibration, C=O 伸缩）；建议 `amide-i-vibration.md`
- **图表**：
  - ![α-螺旋三氢键链示意与参数空间(X,W)相图](../../raw/figures/fornerQuantumTemperatureEffects1993/fig_1_ZWUNGVGZ.png)
  - ![单链概率与晶格位移时间演化](../../raw/figures/fornerQuantumTemperatureEffects1993/fig_3_ATRT67MT.png)
  - ![T=0三链与单链对比验证Scott猜想](../../raw/figures/fornerQuantumTemperatureEffects1993/fig_6_T99ZL7CA.png)
  - ![300K三链局域/E/A模式激发孤子生存](../../raw/figures/fornerQuantumTemperatureEffects1993/fig_8_IKE7SU6I.png)
- **项目连接**：无直接项目连接；属生物物理/非线性动力学，与本组材料主题较远，但方法论上"链间耦合+量子/温度效应"对低维体系有启发。
- **组织与用词**："背景争议→模型→单链 300K→三链 0K 验证→三链 300K→结论"。可复用术语：安萨茨 (ansatz)、激子–声子耦合 (exciton–phonon coupling)、氢键弹性力常数 (H-bond spring constant)、热平均哈密顿量 (thermal-averaged Hamiltonian)、移动孤子/钉扎孤子 (mobile/pinned soliton)。
- **可写入wiki的要点**：
  - |D₂⟩ 态（经典晶格近似）下，Scott 猜想（单链质量与 W 乘 3 等效三链）对 A、E、局域激发均成立。
  - |D₁⟩ 态（量子晶格修正）下，对称 A 模式运动方程自动退化为单链方程，无需参数重整化，猜想不适用。
  - 300 K 下，传统 W=13–19 N/m 时激发被钉扎；W≥30–40 N/m 时多种初始模式下出现稳定移动孤子（如 W=40、X=62 pN 局域激发；W=50、A 模式可耐端反射）。
  - 链间偶极–偶极耦合 L=1.54 meV；蛋白质中共价骨架束缚使有效 W 应远大于甲酰胺晶体测量值 13 N/m。
  - 温度通过将 Nk_BT 按玻色–爱因斯坦统计分配给简正模引入，属平均场近似。

---

## 11. sattarFunctionalizedDoubleTransition2025 — 功能化双过渡金属 Mo₂Ti₂C₃T_x 铁电 MXene 与激光还原石墨烯柔性忆阻器

- **元数据**：Kubra Sattar 等（Houbing Huang、Syed Rizwan），2025，Carbon 237, 120149，DOI 10.1016/j.carbon.2025.120149
- **一句话**：400°C 真空热处理在自支撑双过渡金属 MXene Mo₂Ti₂C₃T_x 中原位生成金红石 TiO₂ 而诱导铁电性，结合激光还原石墨烯电极构建全柔性双极性忆阻器。
- **现有wiki双链**：
  - [[../../wiki/concepts/polarization-switching]]、[[../../wiki/concepts/2D-materials]]
  - [[../../wiki/entities/MXenes]]
  - [[../../wiki/figures/electronic-devices]]、[[../../wiki/figures/vibrational-spectra]]、[[../../wiki/figures/crystal-structures]]
  - [[../../wiki/write/2025]]
  - [[../../raw/note/sattarFunctionalizedDoubleTransition2025]]
- **新概念/实体建议**：
  - 双过渡金属 MXene（double transition metal MXene, Mo₂Ti₂C₃T_x）；建议 `double-transition-mxene.md`
  - 热致铁电性（heat-induced ferroelectricity via in-situ TiO₂）；建议 `heat-induced-fe-mxene.md`
  - 激光还原石墨烯（laser-scribed/laser-reduced graphene, LSG）；建议 `laser-reduced-graphene.md`
  - 铁电内场辅助氧空位导电细丝（ferroelectric internal-field assisted Vo filament）；建议 `fe-assisted-vo-filament.md`
- **图表**：无关键图（笔记未抽取图片；原文含 XRD/Raman/FTIR/PFM/P-E/I-V/导电细丝模型等）
- **项目连接**：无直接项目连接；与 project-5（SnTe 铁电）在铁电存储器层面间接相关，且为铁电+忆阻交叉器件提供材料体系。
- **组织与用词**："MXene 制备→热处理诱导氧化→铁电表征→器件构筑→阻变性能→导电机理"。可复用术语：MAX 相、酸刻蚀、TMAOH 插层、金红石 TiO₂、P–E 电滞回线、蝴蝶形 C–V、双极性阻变 (bipolar resistive switching)、空间电荷限制电流 (SCLC)。
- **可写入wiki的要点**：
  - (002) 峰由 MAX 相 7.6° 移至刻蚀 6.8°、剥离后 ~5°（c-lp=32 Å）；热处理后新增 12°/30°/35° 峰对应金红石 TiO₂ 与 MoO₃。
  - FTIR/Raman 互证：Ti-O（618、1425 cm⁻¹）、Mo-O/Mo=O（867、1164、816、986 cm⁻¹）。
  - PFM 显示不规则铁电畴（形貌高度差 ~240 nm），P-E 呈现饱和电滞回线，C-V 蝴蝶形；原始 MXene 无铁电性。
  - LSG/HT-Mo₂Ti₂C₃T_x/LSG 器件：SET ~+1.8 V，RESET ~−1.7 V，开关比 ~10²，耐久 10³ 次，保持 5×10³ s。
  - 机理：铁电内场辅助氧空位导电细丝；LRS 斜率≈1（欧姆），HRS 斜率≈2（Child 平方律/SCLC）。

---

## 12. duUltrasensitiveOptoelectronicBiosensor2025 — 基于扭曲双层石墨烯超晶格的超灵敏光电生物传感器阵列

- **元数据**：Bowen Du 等（Han Zhang、Dror Fixler 等），2025，National Science Review 12(10), nwaf357，DOI 10.1093/nsr/nwaf357
- **一句话**：将 9.4° 扭曲双层石墨烯的范霍夫奇点吸收与 Au 纳米盘等离激元共振对齐，结合 DNA 折纸与 CRISPR-Cas12a，实现 44.63 aM 核酸免扩增检测。
- **现有wiki双链**：
  - [[../../wiki/concepts/moire-superlattice]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/binding-strength]]
  - [[../../wiki/figures/electronic-devices]]、[[../../wiki/figures/optical-spectra]]、[[../../wiki/figures/experimental-setups]]
  - [[../../wiki/write/2025]]
  - [[../../raw/note/duUltrasensitiveOptoelectronicBiosensor2025]]
- **新概念/实体建议**：
  - 转角电子学（twistronics）与扭曲双层石墨烯（tBLG）；建议 `twistronics.md`
  - 范霍夫奇点（van Hove singularity, VHS）；建议 `van-hove-singularity.md`
  - 激子–等离激元耦合（exciton–plasmon coupling）；建议 `exciton-plasmon-coupling.md`
  - DNA 折纸（DNA origami）与 CRISPR-Cas12a 反式切割；建议 `dna-origami-crispr-cas12a.md`
  - 阿摩尔检测（attomolar detection, aM）；建议 `attomolar-sensing.md`
- **图表**：
  - ![传感器结构与CRISPR开关原理](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_1_BXNBIMFM.png)
  - ![tBLG/Au纳米盘光电流增强6.27倍](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_2_TCFKNXU2.png)
  - ![吸收/泵浦探测/DFPT介电常数/STS的VHS证据](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_3_GLKWBZ8Y.png)
  - ![miRNA检测定量曲线(44.63 aM)与临床验证](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_5_3KFW8A5V.png)
- **项目连接**：无直接项目连接；project-6（湿度传感器）在"二维材料化学/光电传感"方法论层面有借鉴，但生物传感主题不直接重叠。
- **组织与用词**："材料物理增强→生物识别集成→性能表征→临床验证"。可复用术语：莫尔超晶格 (moiré superlattice)、局域表面等离激元共振 (LSPR)、光响应度 (photoresponsivity)、外量子效率 (EQE)、泵浦–探测 (pump–probe)、FDTD 模拟、反式切割 (trans-cleavage)。
- **可写入wiki的要点**：
  - 9.4° tBLG 的 VHS 能量间隔 ~1.84 eV，与 660 nm（1.88 eV）激光和 Au 纳米盘 LSPR 精确对齐。
  - Au 纳米盘/tBLG 光响应度 14.64 mA/W，是纯 tBLG（2.34 mA/W）的 6.27 倍；EQE 27.51%；60 μW 低光强下信号衰减 <5%。
  - 泵浦–探测显示耦合态弛豫 371 fs，远快于纯 tBLG 的 1.14 ps；DFPT 给出 9.4° tBLG 极高面内介电常数与各向异性。
  - CRISPR-Cas12a 反式切割释放 AuNP，恢复激子–等离激元耦合，光电流升高；LOD=44.63 aM，动态范围 10 aM–100 pM（跨 7 个数量级），1 小时完成、免扩增。
  - 10 例肺癌血浆样本检测与 qPCR 高度一致；PBS/全血中 20 天保持高保真度。

---

## 13. king-smithTheoryPolarizationCrystalline1993 — 晶体固体的极化理论

- **元数据**：R. D. King-Smith, David Vanderbilt，1993，Physical Review B 47(3), 1651–1654，DOI 10.1103/PhysRevB.47.1651
- **一句话**：建立现代极化理论，证明晶体绝热变化下的极化改变量 ΔP 等于价带波函数 Berry 相位之差，亦等于占据态 Wannier 函数电荷中心位移之和。
- **现有wiki双链**：
  - [[../../wiki/concepts/berry-phase]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/polarization-switching]]、[[../../wiki/concepts/multiferroicity]]
  - [[../../wiki/entities/Wannier90]]、[[../../wiki/entities/GaAs]]、[[../../wiki/entities/VASP]]
  - [[../../wiki/figures/mathematical-models]]
  - [[../../wiki/write/1993]]
  - [[../../raw/note/king-smithTheoryPolarizationCrystalline1993]]
- **新概念/实体建议**：
  - 现代极化理论（modern theory of polarization）；建议 `modern-polarization-theory.md`
  - Berry 相位/Zak 相位与极化量子化；建议 `berry-phase-polarization.md`
  - Wannier 电荷中心（Wannier charge center）；建议 `wannier-charge-center.md`
  - 玻恩有效电荷（Born effective charge, Z*）；建议 `born-effective-charge.md`
  - 规范不变离散化方案（gauge-invariant discretization, 相邻 k 点内积行列式）；建议 `gauge-invariant-bdiscretization.md`
- **图表**：无关键图（原文以公式推导为主，含 GaAs 压电响应 Table I）
- **项目连接**：project-5（SnTe 铁电模拟）理论基石——SnTe 极化值由 Berry 相方法计算；project-2（Mn 多铁性）中铁电极化定量同样依赖该理论。
- **组织与用词**：简短论文（4 页），"问题→绝热电流→波函数导数→Berry 相位→Wannier 图像→数值方案→GaAs 验证"。可复用术语：绝热演化 (adiabatic evolution)、Kohn–Sham 哈密顿量、周期性规范 (periodic gauge)、极化量子化 (polarization quantization)、压电张量 (piezoelectric tensor)。
- **可写入wiki的要点**：
  - 核心公式：P(λ) = (ifq_e/8π³) Σ_n ∫ dk ⟨u_{kn}^(λ)|∂/∂k|u_{kn}^(λ)⟩；ΔP = P(1)−P(0) 即 Berry 相位差。
  - 物理图像：ΔP = (fq_e/Ω) Σ_n R_n，等于所有占据态 Wannier 函数电荷中心位移矢量和。
  - 绝热循环后哈密顿量回到自身时，ΔP 以 (fq_e/Ω)R 为单位量子化，与量子霍尔效应量子化电导深刻类比。
  - 数值方案：沿 k 方向离散化，计算 Π_j det⟨u_{k_j}|u_{k_{j+1}}⟩ 的虚部对数，规范不变，解决波函数随机相位问题。
  - GaAs 验证：Z*_Ga=1.984（线性响应 1.994，实验 2.16），γ₁₄=−0.28（线性响应 −0.35，实验 −0.32），精确捕捉电子项与离子项的强抵消。
  - 适用前提：绝热过程中体系始终为绝缘体；若能隙闭合（穿越金属态），理论失效。
