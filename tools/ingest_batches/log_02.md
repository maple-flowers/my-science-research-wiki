# 批次 02 文献阅读日志

共 13 篇。记录格式：元数据 / 一句话 / 双链 / 新概念建议 / 图表 / 项目连接 / 组织与用词 / 可写入 wiki 的要点。

---

## 1. bhowalPolarMetalsPrinciples2023b — 极性金属：原理与展望

- **元数据**：Sayantika Bhowal, Nicola A. Spaldin et al.，2023，Annual Review of Materials Research 53, 53-79（综述），DOI: 10.1146/annurev-matsci-080921-105501
- **一句话**：系统综述"极性金属"（极性与金属性共存）的设计原理，提出以"极化畸变与导电电子解耦"为核心的范式，并以 LiOsO3、WTe2 为里程碑剖析其微观机制。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/multiferroicity]]、[[../../wiki/concepts/magnetoelectric-coupling]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/berry-phase]]、[[../../wiki/concepts/spin-orbit-coupling]]、[[../../wiki/concepts/sliding-ferroelectricity]]、[[../../wiki/concepts/polarization-switching]]
  - 实体：[[../../wiki/entities/WTe2]]、[[../../wiki/entities/VASP]]、[[../../wiki/entities/BiFeO3]]、[[../../wiki/entities/domain-wall]]
  - 图表：[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/electronic-bands]]
  - 写作年度：[[../../wiki/write/2023]]
  - 关联 raw/note：[[../../raw/note/hillWhyAreThere2000a]]、[[../../raw/note/RecentAdvancesGrowth2025]]、[[../../raw/note/zahraCriticalAnalysisFerroelectric2025]]、[[../../raw/note/neumayerCompetingPolarPhases2025]]、[[../../raw/note/zhaoRealization2DMultiferroic2024]]、[[../../raw/note/tianRoomtemperatureTwodimensionalMultiferroic2026]]
- **新概念/实体建议**：
  - `polar-metal`（极性金属）：属极性点群同时导电，自由载流子不屏蔽极化的材料类。
  - `fe-like-metal`（类铁电金属）：有结构极性转变但极化不可翻转，如 LiOsO3。
  - `geometric-ferroelectricity`（几何铁电性）：由结构倾转/旋转而非二阶Jahn-Teller驱动的铁电，对载流子不敏感。
  - `lone-pair-ferroelectricity`（孤对电子铁电）：Bi³⁺/Pb²⁺ 6s² 孤对驱动的铁电畸变。
  - `hyperferroelectrics`（超铁电体）：即使在静电退极化场下仍稳定的极性相。
  - `nonlinear-hall-effect`（非线性霍尔效应）：可作为极性相变探测工具。
  - 实体建议：`LiOsO3`（首个类铁电金属，2013）、`Ca3Ru2O7`（几何铁电金属）。
- **图表**：
  - ![极性金属分类与解耦机制示意](../../raw/figures/bhowalPolarMetalsPrinciples2023b/fig_1_K5QYFLQM.png)
  - ![LiOsO3 结构与极性相变](../../raw/figures/bhowalPolarMetalsPrinciples2023b/fig_2_MZBMKDTD.png)
  - ![WTe2 面内滑移翻转面外极化](../../raw/figures/bhowalPolarMetalsPrinciples2023b/fig_3_SDUYTBB2.png)
- **项目连接**：无直接项目连接；与 project-5（SnTe 铁电模拟）在"铁电金属/极性半导体"主题上间接相关。
- **组织与用词**：文章以"悖论—解耦机制—案例—展望"四段式组织，先立"自由载流子屏蔽极化"的传统禁区，再把所有设计原理归并到"解耦（decoupling）"这一统一概念下。可复用术语：polar metal（极性金属）、itinerant screening（巡游载流子屏蔽）、geometric/lone-polar/hyper ferroelectricity（几何/孤对/超铁电性）、design principle（设计原理）、noncentrosymmetric conductor（非中心对称导体）、nonlinear Hall effect（非线性霍尔效应）。
- **可写入wiki的要点**：
  1. 极性金属概念由 Anderson & Blount 于 1965 年提出，2013 年 LiOsO3（类铁电金属）和 2018 年 WTe2（铁电金属）才实验确认。
  2. 核心设计原则是"解耦"：使驱动极化的结构畸变与导电电子属于不同的原子/轨道/空间自由度，从而避免屏蔽。
  3. 三条主要解耦路径：(a) 非 d0 机制（几何铁电 Ca3Ru2O7、孤对 PbTi1−xNbxO3）；(b) 空间解耦（WTe2 面内滑移翻转面外极化、面内导电）；(c) 超铁电体（极化对屏蔽场本征鲁棒）。
  4. LiOsO3 在 ~140 K 发生 R-3c → R3c 结构相变，与传统铁电体同构但无滞回，被称为"类铁电金属"。
  5. WTe2 是首个被实验证实的"铁电金属"：层间相对滑移翻转面外极化，同时保持面内金属性，可用于电场调控拓扑（Weyl 节点）。
  6. 极性金属是非线性霍尔效应、Rashba 物理、铁电超导、电控拓扑的统一平台。

---

## 2. vanvleckSurveyTheoryFerromagnetism1945 — 铁磁性理论综述

- **元数据**：J. H. Van Vleck，1945，Reviews of Modern Physics 17(1), 27-47（经典综述），DOI: 10.1103/RevModPhys.17.27
- **一句话**：系统梳理外斯分子场、海森堡交换作用、布洛赫自旋波与斯通纳巡游电子四大理论，奠定现代铁磁性微观理论框架。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/multiferroicity]]（铁磁性为多铁基本序之一）、[[../../wiki/concepts/spin-orbit-coupling]]
  - 写作年度：[[../../wiki/write/1945]]
  - 关联 raw/note：[[../../raw/note/hillWhyAreThere2000a]]
- **新概念/实体建议**：
  - `exchange-interaction`（交换作用）：源于泡利原理与库仑排斥的纯量子效应，是分子场微观起源。
  - `heisenberg-model`（海森堡定域模型）：H = -2ΣJij Si·Sj。
  - `stoner-model`（斯通纳巡游电子模型）：能带自旋劈裂导致铁磁。
  - `molecular-field-theory`（外斯分子场理论）：唯象 H_eff = H + qM。
  - `spin-wave`（自旋波/磁振子）：低温 M(T) ∝ T^(3/2) 定律。
  - `brillouin-function`（布里渊函数）：量子磁化函数，优于经典朗之万。
  - `bethe-peierls-weiss-method`（BPW 集团近似）：非微扰处理短程关联。
  - `antiferromagnetism`（反铁磁性）：J<0 时的交错子晶格序。
- **图表**：
  - ![居里点以上磁化率倒数-温度关系（Fe/Ni）](../../raw/figures/vanvleckSurveyTheoryFerromagnetism1945/fig_1.png)
  - ![饱和磁化强度随约化温度变化，布里渊 vs 朗之万](../../raw/figures/vanvleckSurveyTheoryFerromagnetism1945/fig_3.png)
  - ![MnO 反铁磁磁化率峰值（理论 vs Bizette 实验）](../../raw/figures/vanvleckSurveyTheoryFerromagnetism1945/fig_6.png)
- **项目连接**：无直接项目连接；为 project-2（Mn 多铁）涉及的磁性基础理论提供历史框架。
- **组织与用词**：先立"分子场之谜"，再依次引入定域模型与巡游模型，最后批判比较并推广至反铁磁。可复用术语：molecular field（分子场）、exchange integral（交换积分）、localized vs itinerant（定域/巡游）、saturation magnetization（饱和磁化强度）、Curie/Neel temperature（居里/奈尔温度）、Brillouin function（布里渊函数）、Stoner criterion（斯通纳判据）。
- **可写入wiki的要点**：
  1. 经典磁偶极相互作用仅能产生 ~1 K 量级的分子场，无法解释 10^3 K 的居里温度；交换作用（量子效应）才是微观起源。
  2. 海森堡模型 H = -2J Σ Si·Sj，J>0 铁磁、J<0 反铁磁；其第一性平均场近似给出 Tc = 2zJS(S+1)/3k。
  3. 布洛赫自旋波预测低温 M(T) = M0[1 - A(kT/J)^(3/2)]，即 T^(3/2) 定律，与实验吻合。
  4. 贝特-佩尔斯-外斯方法通过精确对角化中心原子+最近邻集团，能区分配位数相同但拓扑不同的晶格（如简单立方有铁磁、平面六角没有），优于级数展开。
  5. 斯通纳巡游模型引入参数 kθ'/ε0（交换/费米能之比），自然解释非整数玻尔磁子（如 Ni 的 0.6 μB），并预言电子比热的线性过剩项。
  6. Van Vleck 指出"理论越精修，1/χ-T 线性反而越差"的悖论，预示后来重正化群对临界普适性的解答。

---

## 3. RecentAdvancesGrowth2025 — 二维多铁性材料的生长、表征及应用研究进展

- **元数据**：Dahua Ren et al.，2025，Frontiers of Physics 20(4), 44302（专题综述），DOI: 10.15302/frontphys.2025.044302
- **一句话**：系统综述二维多铁材料（尤其 II 型 FM-FE/FM-FA）的 CVD/PVD/MBE/ALD 生长、SHG/STM/拉曼/太赫兹表征与存储器/自旋电子学应用全景。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/multiferroicity]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/magnetoelectric-coupling]]、[[../../wiki/concepts/ferroelasticity]]、[[../../wiki/concepts/spin-orbit-coupling]]、[[../../wiki/concepts/sliding-ferroelectricity]]、[[../../wiki/concepts/polarization-switching]]、[[../../wiki/concepts/strain-engineering]]
  - 实体：[[../../wiki/entities/h-BN]]、[[../../wiki/entities/TMDs]]、[[../../wiki/entities/CrTe2]]、[[../../wiki/entities/VASP]]、[[../../wiki/entities/domain-wall]]
  - 图表：[[../../wiki/figures/experimental-setups]]、[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/heterostructures-stacking]]、[[../../wiki/figures/optical-spectra]]、[[../../wiki/figures/electronic-devices]]
  - 写作年度：[[../../wiki/write/2025]]
  - 关联 raw/note：[[../../raw/note/bhowalPolarMetalsPrinciples2023b]]、[[../../raw/note/zhaoRealization2DMultiferroic2024]]、[[../../raw/note/zahraCriticalAnalysisFerroelectric2025]]、[[../../raw/note/neumayerCompetingPolarPhases2025]]、[[../../raw/note/hillWhyAreThere2000a]]、[[../../raw/note/tianRoomtemperatureTwodimensionalMultiferroic2026]]
- **新概念/实体建议**：
  - `type-II-multiferroic`（II 型多铁）：铁电由特殊磁序（螺旋）产生，耦合强但极化小、温度低。
  - `electromagnon`（电磁振子）：同时带电极矩的自旋波激发，是动态磁电耦合指纹。
  - `triferroics`（三铁性）：铁电+铁磁+铁谷共存。
  - `ferrovalley`（铁谷性）：二维六角晶格中 K/K' 谷极化可外场翻转。
  - 实体建议：`NiI2`（单层 II 型多铁原型）、`Cr2S3`（晶圆级单层多铁）、`CuCrSe2`（室温铁电/120 K 铁磁）、`SnSe`（p 型掺杂室温多铁）。
- **图表**：
  - ![铁磁/铁电/多铁的时间与空间反演对称性](../../raw/figures/RecentAdvancesGrowth2025/fig_1_7IQ7CDIJ.png)
  - ![CVD/PVD/MBE/ALD 四种气相沉积法对比](../../raw/figures/RecentAdvancesGrowth2025/fig_4_QAJUJ232.png)
  - ![NiI2 螺旋磁序经 e×q 机制产生极化](../../raw/figures/RecentAdvancesGrowth2025/fig_9.png)
  - ![二维多铁应用全景：M-P-ε 耦合与器件](../../raw/figures/RecentAdvancesGrowth2025/fig_15_TMK8S5HG.png)
- **项目连接**：无直接项目连接；为 project-2（Mn 多铁）提供二维多铁材料全景与方法论参考。
- **组织与用词**："制备—表征—应用—展望"四段式综述，把 I 型/II 型分类作为贯穿主线。可复用术语：type-I/II multiferroics（I/II 型多铁）、electromagnon（电磁振子）、SHG（二次谐波）、MERAM/MFTJ（磁电 RAM/多铁隧道结）、triferroic（三铁）、van der Waals epitaxy（范德华外延）。
- **可写入wiki的要点**：
  1. 单层 NiI2 是首个实验证实的单层 II 型多铁：螺旋磁序 q 与自旋轨道耦合通过 P ∝ e×q 产生极化，转变温度约 21 K（TN2 = 59.5 K 处出现电磁振子）。
  2. 单层 Cr2S3 在蓝宝石上实现 1 英寸晶圆级、单晶胞（1.8 nm）生长，室温铁电、~200 K 铁磁。
  3. 单层 CuCrSe2 表现室温铁电 + 120 K 铁磁；p 型掺杂 SnSe 经 PVD 合成，Tc(铁磁) 337 K 且铁电共存。
  4. 表征矩阵：SHG/PFM/双折射探铁电，SQUID/中子/拉曼磁振子探磁序，太赫兹+拉曼探电磁振子（动态磁电耦合）。
  5. I 型多铁铁电与磁来源不同、耦合弱但极化大温度高；II 型由磁序生电、耦合强但极化小温度低。
  6. 应用瓶颈：室温强耦合材料稀缺、空气不稳定、驱动电压需降至 100 mV 以下；未来方向含三铁性、非层状 vdW 外延、超快动力学。

---

## 4. zahraCriticalAnalysisFerroelectric2025 — 二维 MXene 铁电和铁磁性质的临界分析

- **元数据**：Saman Zahra, Bo Dai, Xianhua Wei, Fei Zhou, Syed Irfan et al.，2026（在线 2025），Critical Reviews in Solid State and Materials Sciences 51(2), 200-226（综述），DOI: 10.1080/10408436.2025.2511122
- **一句话**：首篇系统批判性综述 MXene（Mn+1XnTx）中铁电、铁磁与多铁性的工作，归纳掺杂/官能团/应变/复合四类调控策略及器件应用。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/multiferroicity]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/magnetoelectric-coupling]]、[[../../wiki/concepts/polarization-switching]]、[[../../wiki/concepts/strain-engineering]]、[[../../wiki/concepts/density-functional-theory]]
  - 实体：[[../../wiki/entities/MXenes]]、[[../../wiki/entities/BiFeO3]]、[[../../wiki/entities/VASP]]
  - 图表：[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/electronic-devices]]
  - 写作年度：[[../../wiki/write/2025]]
  - 关联 raw/note：[[../../raw/note/RecentAdvancesGrowth2025]]、[[../../raw/note/bhowalPolarMetalsPrinciples2023b]]、[[../../raw/note/hillWhyAreThere2000a]]
- **新概念/实体建议**：
  - `surface-termination`（表面终端官能团 -O/-OH/-F）：调控 MXene 对称性与磁性的主要自由度。
  - `max-phase`（MAX 相）：MXene 的三元碳化物/氮化物前驱体。
  - `magnetic-proximity-effect`（磁近邻效应）：MXene 与铁磁复合时诱导磁性的机制。
  - 实体建议：`Ti3C2Tx`（MXene 代表体系）、`BaTiO3`、`PZT`（复合对象）。
- **图表**：
  - ![MXene 结构与刻蚀合成流程](../../raw/figures/zahraCriticalAnalysisFerroelectric2025/fig_1_WJ78IQDN.png)
  - ![掺杂/官能团诱导铁电与铁磁的策略汇总](../../raw/figures/zahraCriticalAnalysisFerroelectric2025/fig_10_8U7ZULVR.png)
- **项目连接**：无直接项目连接。
- **组织与用词**：按"结构—合成—铁电—铁磁—多铁—应用"递进，并采用"批判性分析"姿态指出现有 DFT 预测与实验验证间的差距。可复用术语：MXene（Mxene）、surface termination（表面终端）、etching（刻蚀）、intercalation（插层）、ferroelectric memristor（铁电忆阻器）、spin polarization（自旋极化）。
- **可写入wiki的要点**：
  1. MXene 通式 Mn+1XnTx，由 MAX 相选择性刻蚀 A 原子层得到，本征中心对称、无铁电/铁磁。
  2. 诱导铁电途径：表面不对称官能团化（-O/-OH/-F 分布失衡）、掺杂破坏反演对称、与 BaTiO3/PZT/BiFeO3 形成异质结。
  3. 诱导铁磁途径：边缘/空位缺陷、磁性过渡金属掺杂、双过渡金属有序 MXene（如 Cr2TiC2）、磁近邻效应。
  4. 刻蚀工艺（HF、熔盐、无氟）显著影响表面化学进而决定磁/电性质，是实验可重复性的关键。
  5. MXene 基铁电忆阻器、纳米发电机、自旋电子器件已有原型，但室温稳定、规模化与磁电耦合微观机制仍是瓶颈。
  6. 该综述首次把"多铁性"作为 MXene 的独立章节评述，指出高通量 DFT 预测远多于实验验证的现状。

---

## 5. pengStrainEngineering2D2020 — 二维半导体和石墨烯的应变工程：从应变场到能带调谐和光子应用

- **元数据**：Zhiwei Peng, Xiaolin Chen, Yulong Fan, David J. Srolovitz, Dangyuan Lei，2020，Light: Science & Applications 9, 190（综述），DOI: 10.1038/s41377-020-00421-5
- **一句话**：建立宏观弹性理论—微观 k·p 哈密顿量—光学响应三层框架，系统综述应变对 TMDC/石墨烯能带、激子、拉曼、SHG 的调控及光子器件应用。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/strain-engineering]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/deformation-potential]]、[[../../wiki/concepts/giant-spin-splitting]]
  - 实体：[[../../wiki/entities/TMDs]]、[[../../wiki/entities/h-BN]]
  - 图表：[[../../wiki/figures/optical-spectra]]、[[../../wiki/figures/electronic-bands]]、[[../../wiki/figures/mathematical-models]]
  - 写作年度：[[../../wiki/write/2020]]
  - 关联 raw/note：（笔记中未列关联文献）
- **新概念/实体建议**：
  - `exciton-funnel-effect`（激子漏斗效应）：非均匀应变梯度把激子漂移到窄带隙区域。
  - `flexible-substrate-strain`（柔性衬底应变）：PDMS/PET 弯曲/拉伸施加单/双轴应变。
  - `local-strain`（局部应变）：纳米柱、褶皱、气泡、AFM 针尖产生非均匀应变。
  - `deformation-potential-theory`（形变势理论）：描述带边随应变移动的耦合常数。
  - `pseudomagnetic-field`（赝磁场）：石墨烯非均匀应变产生的有效磁场。
- **图表**：
  - ![TMDC/石墨烯应变调控光学性质总览](../../raw/figures/pengStrainEngineering2D2020/fig_1_XEEBDMHH.png)
- **项目连接**：无直接项目连接；strain-engineering 概念条目可直接吸收本篇内容。
- **组织与用词**：先理论（宏观弹性张量+微观有效哈密顿量），再实验（均匀/非均匀应变技术），最后光学响应与器件，是"机制—技术—应用"的综述范本。可复用术语：uniaxial/biaxial strain（单/双轴应变）、deformation potential（形变势）、exciton funnel（激子漏斗）、pseudomagnetic field（赝磁场）、bandgap transition（直接-间接带隙转变）、wrinkle/bubble/nanopillar（褶皱/气泡/纳米柱）。
- **可写入wiki的要点**：
  1. 单层 TMDC 在双轴拉伸下带隙红移，~1-2% 应变即可引发直接-间接带隙转变；单层 MoS2 带隙形变势约 -45 meV/%（双轴）至 -80 meV/%（单轴）量级。
  2. 石墨烯单轴应变导致拉曼 G 峰分裂为 G+/G-，2D 峰位移可作为应变量子；非均匀应变产生高达数十 T 的赝磁场。
  3. 局部应变（纳米柱、气泡、AFM 压痕）形成"激子漏斗"，把激子漂移到窄带隙高应变区，可实现单光子发射器。
  4. 应变可调控 TMDC 的 SHG 强度并诱导 2H-1T' 相变，改变谷极化与自旋劈裂。
  5. 应变施加技术分三类：柔性衬底弯曲/拉伸（均匀）、压电衬底（可逆）、微纳结构基底（局部非均匀）。
  6. 应用方向：应变传感器、宽谱太阳能漏斗、单光子源、可调谐光电器件；开放问题包括动态/超快应变与二维异质结中的应变传递。

---

## 6. tanRevealingEmergentMagnetic2024 — 用金刚石量子磁强计揭示反铁磁体中的涌现磁荷

- **元数据**：Anthony K. C. Tan, Hariom Jani, Michael Högen, Claudio Castelnovo, Paolo G. Radaelli, Mete Atatüre et al.，2024，Nature Materials 23(2), 205-211，DOI: 10.1038/s41563-023-01737-4
- **一句话**：利用金刚石量子磁强计（DQM）在 α-Fe2O3 薄膜中成像反铁磁拓扑织构，实验建立反梅隆/梅隆/畴壁与涌现磁单极子/四极子/偶极子的对偶关系。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/topological-defects]]、[[../../wiki/concepts/spin-orbit-coupling]]、[[../../wiki/concepts/altermagnetism]]
  - 实体：[[../../wiki/entities/domain-wall]]
  - 图表：[[../../wiki/figures/experimental-setups]]、[[../../wiki/figures/mathematical-models]]
  - 写作年度：[[../../wiki/write/2024]]
  - 关联 raw/note：（笔记中未列关联文献）
- **新概念/实体建议**：
  - `emergent-magnetic-charge`（涌现磁荷）：拓扑自旋织构产生的有效磁单极场。
  - `meron-antimeron`（梅隆/反梅隆）：拓扑荷 ±1/2 的面内涡旋织构。
  - `diamond-quantum-magnetometry`（金刚石量子磁强计，DQM/NV 色心）：高灵敏度矢量磁场成像。
  - `canted-antiferromagnet`（斜方反铁磁体）：如 α-Fe2O3，弱 FM 分量来自 DMI 倾斜。
  - `dzyaloshinskii-moriya-interaction`（DMI，Dzyaloshinskii-Moriya 相互作用）：驱动非共线织构。
  - 实体建议：`alpha-Fe2O3`（赤铁矿，斜方反铁磁原型）。
- **图表**：
  - ![α-Fe2O3 中 a-Bloch 梅隆/反梅隆/畴壁的 NV 磁成像](../../raw/figures/tanRevealingEmergentMagnetic2024/fig_2_F3UEVWZT.png)
  - ![涌现磁荷随积分半径的线性增长（单极子特征）](../../raw/figures/tanRevealingEmergentMagnetic2024/fig_4_TQTWANCS.png)
- **项目连接**：无直接项目连接；与 project-7（CDW）共享"量子材料中拓扑织构的桌面量子传感"方法论。
- **组织与用词**：标准实验论文结构——背景悖论（反铁磁织构难探测）→ 新方法（DQM 矢量成像）→ 三类织构测量 → 对偶映射 → 展望。可复用术语：emergent magnetic charge（涌现磁荷）、meron/antimeron（梅隆/反梅隆）、vorticity/chirality（涡度/手性）、canted antiferromagnet（斜方反铁磁体）、NV center（NV 色心）、topological spin texture（拓扑自旋织构）。
- **可写入wiki的要点**：
  1. α-Fe2O3 薄膜中 DMI 诱导反相畴壁（ADW）、顺时针/逆时针 a-Bloch 梅隆、反梅隆、双梅隆等多种拓扑织构。
  2. a-Bloch 梅隆对应涌现磁单极子：其杂散场积分得到的总"磁荷"随积分半径线性增长；反梅隆总磁荷为零，对应磁四极子；畴壁对应磁偶极子。
  3. 磁荷极性由织构涡度（vorticity）手性决定，首次在实验上建立反铁磁涡度与磁荷的对偶。
  4. 该磁荷非量子化，并因织构间相互作用而改变，区别于自旋冰中的单极子。
  5. 方法上确立了 DQM（金刚石 NV 色心磁强计）作为量子材料桌面式矢量磁场成像工具的地位。
  6. 斜方反铁磁体被提出为二维"单极子物理"新平台，区别于传统自旋冰体系。

---

## 7. zhaoRealization2DMultiferroic2024 — 插层实现强磁电耦合二维多铁：第一性原理高通量预测

- **元数据**：Ying Zhao, Yanxia Wang, Yue Yang, Jijun Zhao, Xue Jiang，2024，npj Computational Materials 10, 122，DOI: 10.1038/s41524-024-01301-x
- **一句话**：提出"插层"通用策略，从 960 种 AM2X4 中高通量筛选出 40 种铁电体与 21 种二维多铁单层，并按磁性起源分三类，首次实现极化翻转可逆调控斯格明子。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/multiferroicity]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/magnetoelectric-coupling]]、[[../../wiki/concepts/berry-phase]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/spin-orbit-coupling]]、[[../../wiki/concepts/lego-assembly]]、[[../../wiki/concepts/topological-defects]]
  - 实体：[[../../wiki/entities/TMDs]]、[[../../wiki/entities/VASP]]、[[../../wiki/entities/Wannier90]]
  - 图表：[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/electronic-bands]]、[[../../wiki/figures/mathematical-models]]
  - 写作年度：[[../../wiki/write/2024]]
  - 关联 raw/note：[[../../raw/note/RecentAdvancesGrowth2025]]、[[../../raw/note/bhowalPolarMetalsPrinciples2023b]]、[[../../raw/note/hillWhyAreThere2000a]]、[[../../raw/note/neumayerCompetingPolarPhases2025]]、[[../../raw/note/tianRoomtemperatureTwodimensionalMultiferroic2026]]
- **新概念/实体建议**：
  - `intercalation-strategy`（插层策略）：在 TMD 双层间隙插入 A 原子打破反演对称引入铁电。
  - `type-a-b-c-intercalated-multiferroic`（三类插层多铁）：a 磁性在 MX2 层、b 磁性在插层 A、c 两者皆有。
  - `electric-field-control-skyrmion`（电场控制斯格明子）：极化翻转切换 DMI 符号从而产生/擦除斯格明子。
  - 实体建议：`CdCr2Te4`（type-a 代表，Tc 近室温）、`CoZr2S4`（type-b）、`CoTi2Te4`（type-c）。
- **图表**：
  - ![插层 AM2X4 结构与三类多铁分类](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_1_S88Q2EF3.png)
  - ![高通量筛选流程与稳定性判定](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_2_7QNUMABJ.png)
  - ![T-CdCr2Te4 极化翻转调控斯格明子](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_3_VSIZIKC2.png)
- **项目连接**：无直接项目连接；为 project-2（Mn 多铁）提供高通量设计范式参考。
- **组织与用词**：标准高通量计算论文——提出策略→结构筛选→稳定性判定→铁电/磁学分类→代表体系深描→新机制（电控斯格明子）。可复用术语：intercalation（插层）、high-throughput screening（高通量筛选）、Berry phase（Berry 相极化）、CI-NEB（翻转能垒）、Monte Carlo（蒙特卡洛）、skyrmion（斯格明子）、type-a/b/c multiferroic（三类多铁）。
- **可写入wiki的要点**：
  1. 对 960 种非中心对称 AM2X4（A 为 3d/4d 过渡金属，X = S/Se/Te）高通量筛选，得 40 种稳定二维铁电体、21 种多铁单层。
  2. 三类多铁：type-a 磁性在 MX2 层（极化翻转调控斯格明子）、type-b 磁性在插层 A 原子（翻转改变磁基态与易轴）、type-c 两者皆有磁矩（翻转改变自旋极化分布）。
  3. 代表体系 T-CdCr2Te4 的铁电转变温度与居里温度均接近室温，磁电耦合性能优异。
  4. 方法学：VASP + PBE+U 结构优化，Berry phase+偶极修正算极化，CI-NEB 算翻转能垒，MC 模拟估 Tc 与斯格明子。
  5. type-a 体系首次理论演示极化翻转可逆改变 DMI 符号，从而产生/擦除上下层斯格明子——电场控制拓扑自旋的新范式。
  6. 揭示金属性与铁电性可在插层体系共存，扩展了二维多铁材料家族。

---

## 8. kresseUltrasoftPseudopotentialsProjector1999c — 从超软赝势到投影增强波方法

- **元数据**：G. Kresse, D. Joubert，1999，Physical Review B 59(3), 1758-1775，DOI: 10.1103/PhysRevB.59.1758
- **一句话**：从形式上证明超软赝势（US-PP）是 PAW 方法在原子参考态的一阶线性化近似，并提出在现有 US-PP 代码中简洁实现 PAW 的重构总能量泛函。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/density-functional-theory]]
  - 实体：[[../../wiki/entities/VASP]]、[[../../wiki/entities/Wannier90]]
  - 图表：[[../../wiki/figures/mathematical-models]]
  - 写作年度：[[../../wiki/write/1999]]
  - 关联 raw/note：[[../../raw/note/kresseEfficiencyAbinitioTotal1996a]]、[[../../raw/note/RecentAdvancesGrowth2025]]、[[../../raw/note/zhaoRealization2DMultiferroic2024]]
- **新概念/实体建议**：
  - `projector-augmented-wave`（PAW，投影增强波方法）：统一赝势与全电子方法的变换框架。
  - `ultrasoft-pseudopotential`（US-PP，超软赝势）：Vanderbilt 提出，放松模守恒约束并引入增强电荷。
  - `augmentation-charge`（增强电荷）：恢复芯区电荷密度的补偿项。
  - `all-electron-method`（全电子方法，如 FLAPW）：精度基准。
  - `frozen-core-approximation`（冻结芯近似）。
- **图表**：无关键图（笔记附件以公式 eq_*.png 为主）。
- **项目连接**：间接支撑 project-5（SnTe 铁电模拟）所依赖的 VASP/PAW 方法学。
- **组织与用词**：方法学论文——先回顾 US-PP 与 PAW，再解析推导线性化关系，最后小分子/块体/磁性体系基准测试。可复用术语：projector augmented wave（投影增强波）、ultrasoft pseudopotential（超软赝势）、norm-conserving（模守恒）、augmentation charge（增强电荷）、all-electron accuracy（全电子精度）、transformation operator（变换算符）。
- **可写入wiki的要点**：
  1. US-PP 是 PAW 在原子参考态对局域能量项做一阶线性化得到的近似，这解释了 US-PP 为何通常精确但在强磁性/大电负性差体系失效。
  2. PAW 通过在原子球内重建全电子波函数，以接近 US-PP 的计算成本获得 FLAPW 全电子精度。
  3. US-PP 在强磁性体系的误差源于伪化增强电荷无法精确描述自旋极化电荷密度分布。
  4. 论文提出重构的、数值更稳定的 PAW 总能量泛函与算符，使 PAW 可在现有 US-PP 平面波代码中相对简洁地实现。
  5. 基准测试覆盖小分子、块体与磁性体系，定位了 US-PP 误差来源并给出方法选择指南。
  6. 该工作直接奠定了 VASP 中 PAW 作为事实标准的地位。

---

## 9. kresseEfficiencyAbinitioTotal1996a — 平面波基组下金属与半导体从头算总能的效率

- **元数据**：G. Kresse, J. Furthmüller，1996，Computational Materials Science 6, 15-50，DOI: 10.1016/0927-0256(96)00008-0
- **一句话**：系统整合 RMM-DIIS 迭代对角化、Methfessel-Paxton 展宽、Pulay/Broyden 电荷混合等算法，构建后来 VASP 的高效稳健第一性原理总能计算框架。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/density-functional-theory]]
  - 实体：[[../../wiki/entities/VASP]]
  - 图表：[[../../wiki/figures/mathematical-models]]
  - 写作年度：[[../../wiki/write/1996]]
  - 关联 raw/note：[[../../raw/note/kresseUltrasoftPseudopotentialsProjector1999c]]
- **新概念/实体建议**：
  - `rmm-diis`（Residual Minimization-Direct Inversion in Iterative Subspace，残差最小化迭代对角化）：对 >30 原子体系标度最优。
  - `methfessel-paxton-smearing`（MP 展宽）：处理金属部分占据，能量与力自洽一致。
  - `pulay-mixing`（Pulay 电荷混合）：基于历史残差的自洽混合。
  - `davidson-algorithm`（Davidson 对角化）、`broyden-mixing`（Broyden 混合）、`linear-tetrahedron-method`（线性四面体法）。
  - `car-parrinello-md`（CP 分子动力学）：被对比的旧范式。
- **图表**：无关键图（笔记附件仅 manifest.json，无图片导出）。
- **项目连接**：间接支撑 project-5（SnTe 铁电模拟）所用 VASP 算法。
- **组织与用词**：算法论文——依次讨论占据数处理、对角化、电荷混合、直接最小化，再用液态 Ge/Pd(111)/金刚石(100) 三体系基准。可复用术语：self-consistent field cycle（SCF 循环）、partial occupation（部分占据）、smearing（展宽）、charge mixing（电荷混合）、preconditioning（预条件）、iterative diagonalization（迭代对角化）。
- **可写入wiki的要点**：
  1. 自洽场（SC）循环方法在效率上普遍优于直接最小化 Kohn-Sham 能量泛函的方法，尤其对金属体系。
  2. RMM-DIIS 因避免显式正交化，对大于 30 原子的体系具有最优的计算标度，是 VASP 默认对角化器。
  3. Methfessel-Paxton 展宽是处理金属部分占据的最优方案：能量与力自洽一致，且 σ 选择不敏感；对比之下四面体法在力计算上需更密 k 点。
  4. 结合预条件矩阵与优化度量的 Pulay 混合最稳定，可有效抑制电荷密度振荡；Broyden 混合在某些情形更快但需调参。
  5. 基准体系：液态锗（金属）、Pd(111) 表面（强电荷振荡金属）、金刚石(100) 表面（半导体）。
  6. 该工作奠定了 VASP 的算法骨架，使过渡金属、液态金属等复杂体系的大规模第一性原理 MD 成为可能。

---

## 10. hillWhyAreThere2000a — 为什么磁性铁电体这么少？

- **元数据**：Nicola A. Hill，2000，The Journal of Physical Chemistry B 104(29), 6694-6709，DOI: 10.1021/jp000114x
- **一句话**：提出制约钙钛矿中铁磁与铁电共存的"d0 规则"，并指出 BiMnO3（孤对）与 YMnO3（六方结构）两条破规路径，奠定现代多铁材料理性设计基础。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/multiferroicity]]、[[../../wiki/concepts/magnetoelectric-coupling]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/electron-counting-rule]]
  - 实体：[[../../wiki/entities/BiFeO3]]、[[../../wiki/entities/HoMnO3]]、[[../../wiki/entities/SrMnO3]]
  - 图表：[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/electronic-bands]]
  - 写作年度：[[../../wiki/write/2000]]
  - 关联 raw/note：[[../../raw/note/bhowalPolarMetalsPrinciples2023b]]、[[../../raw/note/RecentAdvancesGrowth2025]]、[[../../raw/note/zhaoRealization2DMultiferroic2024]]、[[../../raw/note/neumayerCompetingPolarPhases2025]]
- **新概念/实体建议**：
  - `d0-rule`（d0 规则）：钙钛矿中铁电需 B 位 d0，磁性需未满 d 壳，二者互斥。
  - `lone-pair-driven-ferroelectricity`（孤对驱动铁电）：Bi3+ 6s2 与 O 2p 共价杂化。
  - `geometric-ferroelectricity-hexagonal`（六方几何铁电）：小 A 位阳离子稳定非中心对称六方结构。
  - 实体建议：`BiMnO3`（铁磁+可能铁电）、`YMnO3`（六方反铁磁铁电）、`LaMnO3`（对照非铁电）。
- **图表**：
  - ![钙钛矿中铁电与磁性的电子结构对比](../../raw/figures/hillWhyAreThere2000a/fig_1_IBXL696E.png)
  - ![BiMnO3 vs LaMnO3：Bi 孤对的作用](../../raw/figures/hillWhyAreThere2000a/fig_10_YF7NY83P.png)
  - ![六方 YMnO3 结构与铁电畸变](../../raw/figures/hillWhyAreThere2000a/fig_13_N92KZA4L.png)
- **项目连接**：与 project-2（Mn 多铁）直接相关——BiMnO3/YMnO3 是 Mn 基多铁原型。
- **组织与用词**：以"问题—电子结构解释—反例—设计原则"组织，是典型的"基于第一性原理对比研究"范式。可复用术语：d0 rule（d0 规则）、lone pair（孤对电子）、perovskite（钙钛矿）、second-order Jahn-Teller（二阶 Jahn-Teller）、covalent hybridization（共价杂化）、geometric ferroelectricity（几何铁电性）。
- **可写入wiki的要点**：
  1. d0 规则：钙钛矿中铁电位移通常由 B 位 d0 构型的二阶 Jahn-Teller 失稳驱动，而磁性要求未满 d 轨道，二者在同一 B 位化学上互斥。
  2. 破规路径一（化学驱动）：BiMnO3 中 Bi3+ 6s2 孤对与 O 2p 强共价杂化提供铁电驱动力，把铁电职责从 B 位转移到 A 位，Mn3+ 同时承担磁性。
  3. 破规路径二（结构驱动）：YMnO3 中 Y3+ 半径小，稳定本身非中心对称的六方结构，铁电来自几何倾转而非 d0 机制。
  4. 方法上采用 LSDA 第一性原理对比 BiMnO3/LaMnO3、YMnO3/LaMnO3，通过声子不稳定性与态密度分离关键变量。
  5. 该工作把多铁研究从盲目试错引向基于电子结构与化学键的理性设计。
  6. 后续被反向激发的方向包括自旋驱动铁电（II 型多铁）、几何铁电、孤对铁电金属等。

---

## 11. Xie2024isostructural — 有机持久机械发光的同构掺杂

- **元数据**：Zongliang Xie, Yufeng Xue, Xianhe Zhang, Junru Chen, Zesen Lin, Bin Liu，2024，Nature Communications 15，DOI: 10.1038/s41467-024-47962-6
- **一句话**：提出"同构掺杂+结构修饰"通用策略，在压电咔唑主体中引入同构客体，首次实现最长 384.1 ms、量子产率 11.9% 的多色有机持久力致发光（pML）。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/2D-materials]]（无直接概念对应；机械发光暂无 wiki 概念条目）
  - 写作年度：[[../../wiki/write/2024]]
  - 关联 raw/note：（笔记中未列关联文献）
- **新概念/实体建议**：
  - `persistent-mechanoluminescence`（持久力致发光，pML）：机械刺激后持续发光的现象。
  - `isostructural-doping`（同构掺杂）：主体与客体结构相似、晶格匹配的掺杂策略。
  - `charge-transfer-exciplex`（电荷转移激基复合物）：主客体间电荷转移激发态，促进系间窜越与磷光。
  - `piezoelectric-host`（压电主体）：受力时产生局域电场激发客体发光。
  - `intersystem-crossing`（系间窜越，ISC）、`phosphorescence`（磷光）。
- **图表**：笔记附件仅 manifest.json，无图片导出。
- **项目连接**：与 project-3（机械发光 NN）直接相关——同为有机力致发光体系，提供"主体-客体同构掺杂"设计原理与光物理机制，可作为 NN 数据集的正样本与机制标签来源。
- **组织与用词**：策略—合成—表征—机理—器件五步走，先指出"有机 ML 寿命短、有机长余辉需光激发"的两难，再用同构掺杂破题。可复用术语：persistent mechanoluminescence（持久力致发光）、isostructural doping（同构掺杂）、piezoelectric host（压电主体）、charge-transfer exciplex（电荷转移激基复合物）、intersystem crossing（系间窜越）、afterglow（余辉）。
- **可写入wiki的要点**：
  1. 传统有机 ML 寿命仅纳秒级；有机长余辉虽可达毫秒-秒但需光激发，二者此前无法兼得。
  2. 策略：在压电主体（咔唑衍生物）上引入 Br 与 -CN 官能团，再与结构相似的同构客体掺杂。官能团增强偶极矩与自旋轨道耦合，促进 ISC，抑制非辐射衰减。
  3. 主客体间形成电荷转移激基复合物，大幅提升三重态布居与磷光比例。
  4. 代表体系 BCPC&BCPB 实现橙色/黄色/绿色多色 pML，最长寿命 384.1 ms，磷光量子产率最高 11.9%。
  5. 该策略在 4 个额外同构体系中复现，证明普适性。
  6. 展示了光学存储、压力显示、应力监测等应用原型。

---

## 12. chowdhuryReviewTheoreticalComputational — 二维电荷密度波材料的理论与计算方法综述

- **元数据**：Sugata Chowdhury, Heather M. Hill, Albert F. Rigosi, Patrick M. Vora, Angela R. Hight Walker, Francesca Tavazza，日期/期刊字段在笔记中缺失（综述，聚焦 TaS2/TaSe2），DOI 未记录
- **一句话**：系统综述二维 CDW（尤其 TaS2、TaSe2）的 DFT 计算方法、原子结构、拉曼振幅/相位模与维度效应，提出维度依赖 CDW 相图的统一概念模型。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/charge-density-wave]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/strain-engineering]]、[[../../wiki/concepts/electron-counting-rule]]
  - 实体：[[../../wiki/entities/TMDs]]、[[../../wiki/entities/VASP]]
  - 图表：[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/vibrational-spectra]]、[[../../wiki/figures/electronic-bands]]、[[../../wiki/figures/mathematical-models]]
  - 写作年度：[[../../wiki/write/Unknown]]
  - 关联 raw/note：（笔记中未列关联文献）
- **新概念/实体建议**：
  - `amplitude-mode`（振幅模）与`phase-mode`（相位模）：CDW 集体激发，对应幅度涨落与滑移。
  - `fermi-surface-nesting`（费米面嵌套）：CDW 传统驱动机制之一。
  - `electron-phonon-coupling-cdw`（电声耦合驱动 CDW）：在 TaS2/TaSe2 中日益被强调。
  - `dimensionality-effect`（维度效应）：从块体到单层 CDW 波矢、转变温度、与超导竞争的变化。
  - `electronic-temperature-scheme`（电子温度方案）：DFT 中模拟 CDW 相变的展宽技巧。
  - 实体建议：`TaS2`、`TaSe2`（1T/2H 相 CDW 原型）。
- **图表**：
  - ![二维 CDW 计算方法与原子结构总览](../../raw/figures/chowdhuryReviewTheoreticalComputational/fig_1_6U85MKFS.png)
  - ![TaS2/TaSe2 拉曼振幅模与相位模](../../raw/figures/chowdhuryReviewTheoreticalComputational/fig_3_F6W5S8YU.png)
  - ![维度依赖的 CDW 相图概念模型](../../raw/figures/chowdhuryReviewTheoreticalComputational/fig_7_NZSMJSXX.png)
- **项目连接**：与 project-7（CDW）直接相关——该综述是 project-7 的方法论与维度效应核心参考。
- **组织与用词**：教学型综述——先方法（DFT 参数、k 点、展宽、应力），再结构与声子，最后维度效应与统一相图。可复用术语：charge density wave（CDW，电荷密度波）、amplitude/phase mode（振幅/相位模）、Fermi surface nesting（费米面嵌套）、electron-phonon coupling（电声耦合）、commensurate/incommensurate（公度/非公度）、dimensionality（维度）。
- **可写入wiki的要点**：
  1. DFT 模拟 CDW 相变的两类技巧：电子温度（展宽）法与应力工程法，可分别稳定/抑制 CDW 相。
  2. 首次通过计算清晰识别 TaSe2 中振幅模与相位模的原子振动图像，并与拉曼光谱对应。
  3. TaS2 与 TaSe2 在 CDW 行为上差异显著：非公度性、相变模式、与超导竞争关系各不相同。
  4. 维度降低通过改变费米面拓扑、削弱层间耦合、增强波函数空间扩展，显著调控 CDW 稳定性与结构。
  5. 提出基于离子电荷转移、电子-声子耦合、波函数空间扩展三要素的统一维度依赖 CDW 相图框架。
  6. 计算参数（泛函、k 点网格、展宽、范德华修正）对 CDW 波矢与转变温度影响巨大，论文给出基准建议。

---

## 13. neumayerCompetingPolarPhases2025 — 二维铁电过渡金属硫/硒磷酸盐中的竞争极性相

- **元数据**：Sabine Neumayer, Huimin Qiao, Nina Balke，2025，Applied Physics Letters（Perspective/观点），DOI: 10.1063/5.0253879
- **一句话**：提出二维过渡金属硫/硒磷酸盐（TMTPs，如 CIPS、CIPSe）中"能量相近的竞争极性相"统一框架，揭示 Cu+ 离子迁移与铁电序耦合的新范式。
- **现有wiki双链**：
  - 概念：[[../../wiki/concepts/polarization-switching]]、[[../../wiki/concepts/2D-materials]]、[[../../wiki/concepts/ferroelasticity]]、[[../../wiki/concepts/multiferroicity]]、[[../../wiki/concepts/magnetoelectric-coupling]]、[[../../wiki/concepts/density-functional-theory]]、[[../../wiki/concepts/strain-engineering]]
  - 实体：[[../../wiki/entities/domain-wall]]、[[../../wiki/entities/VASP]]
  - 图表：[[../../wiki/figures/crystal-structures]]、[[../../wiki/figures/electronic-devices]]、[[../../wiki/figures/experimental-setups]]
  - 写作年度：[[../../wiki/write/2025]]
  - 关联 raw/note：[[../../raw/note/RecentAdvancesGrowth2025]]、[[../../raw/note/bhowalPolarMetalsPrinciples2023b]]、[[../../raw/note/zhaoRealization2DMultiferroic2024]]、[[../../raw/note/hillWhyAreThere2000a]]
- **新概念/实体建议**：
  - `tmtp`（过渡金属硫/硒磷酸盐，transition metal thio/selenophosphates）：二维铁电材料家族。
  - `competing-polar-phases`（竞争极性相）：能量差仅几十 meV/f.u. 的多种铁电/反铁电相共存。
  - `intralayer-vs-interlayer-ferroelectricity`（层内 vs 层间铁电）：Cu 位移方向不同的两类极性相。
  - `ionic-polarization-coupling`（离子-极化耦合）：Cu+ 离子迁移驱动极化翻转，区别于传统偶极翻转。
  - 实体建议：`CuInP2S6`（CIPS）、`CuInP2Se6`（CIPSe）。
- **图表**：
  - ![TMTPs 中多种竞争极性相示意](../../raw/figures/neumayerCompetingPolarPhases2025/fig_1_4FMFYJBN.png)
  - ![CIPS/CIPSe 层内/层间铁电与反铁电相](../../raw/figures/neumayerCompetingPolarPhases2025/fig_2_V7R5BUVE.png)
  - ![电场/温度驱动的相转换与 Cu+ 迁移](../../raw/figures/neumayerCompetingPolarPhases2025/fig_3_IGPCQM6L.png)
- **项目连接**：无直接项目连接；与 project-5（SnTe 铁电模拟）在"二维铁电翻转机制"主题上方法学相关。
- **组织与用词**：观点（Perspective）文章——先立"能量相近多相共存"概念，再用 CIPS/CIPSe 为证据，最后展望器件与表征。可复用术语：competing polar phases（竞争极性相）、intralayer/interlayer FE（层内/层间铁电）、antiferroelectric phase（反铁电相）、ionic migration（离子迁移）、ionic-polarization coupling（离子-极化耦合）、van der Waals ferroelectric（范德华铁电体）。
- **可写入wiki的要点**：
  1. 在 CuInP2S6（CIPS）与 CuInP2Se6（CIPSe）中，层内铁电相、层间铁电相、反铁电相能量差仅几十 meV/f.u.，可共存并相互竞争。
  2. 这些相可通过温度、电场、Cu+ 离子迁移等外部刺激可逆转换；层间铁电相与反铁电相多以局部微区存在。
  3. 微区相稳定性受局部应变、界面效应、Cu+ 无序化强烈影响。
  4. Cu+ 离子电导与铁电序耦合，打破了"极化仅由偶极子集体翻转"的传统范式。
  5. 该家族为超越二进制的高密度存储、自适应传感器、可调电容器、神经形态器件提供材料平台。
  6. 未来方向包括低剂量 STEM/冷冻电镜原子级验证、宏观尺度相控制、缺陷（Cu 空位/间隙）调控、CIPS/IPS 铁电/顺电异质结。
