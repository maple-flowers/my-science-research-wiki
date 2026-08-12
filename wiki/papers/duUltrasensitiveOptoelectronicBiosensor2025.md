---
citekey: duUltrasensitiveOptoelectronicBiosensor2025
title: "Ultrasensitive optoelectronic biosensor arrays based on twisted bilayer graphene superlattice"
authors: [Bowen Du, Xilin Tian, Zhi Chen, Yanqi Ge, Chuanghu Chen, Haiyan Gao, et al.]
year: 2025
journal: "National Science Review"
doi: "10.1093/nsr/nwaf357"
url: "https://doi.org/10.1093/nsr/nwaf357"
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/duUltrasensitiveOptoelectronicBiosensor2025]]
projects: [project-5, project-6]
concepts: [moire-superlattice, 2d-materials, density-functional-theory, twistronics, van-hove-singularity, exciton-plasmon-coupling, surface-plasmon-resonance, crispr-cas12a, dna-origami, dielectric-response, photoresponsivity, local-dielectric-environment, trans-cleavage]
entities: [twisted-bilayer-graphene, graphene, gold-nanodisks, gold-nanoparticles, VASP, crispr-cas12a-protein, dna-origami-structure]
methods: [dft, dfpt, fdtd, raman-spectroscopy, sem, tem, afm, sts-stm, pump-probe-spectroscopy, ebl, cvd, page-gel-electrophoresis, photocurrent-mapping, lock-in-amplifier, saed, qpcr-validation]
materials: [twisted-bilayer-graphene, gold, dna-origami, crrna, mirna-21]
figures: [electronic-bands, optical-spectra, experimental-setups, electronic-devices, heterostructures-stacking]
领域基础知识:: >-
  转角电子学（Twistronics）通过调控二维材料层间旋转角产生莫尔超晶格，可定制电子能带结构。扭曲双层石墨烯（tBLG）在大转角（>5°）下，两个狄拉克锥交叉形成态密度鞍点即范霍夫奇点（VHS），在特定能量处显著增强光吸收。表面等离子体共振（SPR）是金属纳米结构中自由电子的集体光振荡；CRISPR-Cas12a是RNA引导的DNA内切酶，识别靶标后激活非特异性单链DNA反式切割活性；DNA折纸术利用碱基互补自组装实现纳米级精确定位。
研究背景:: >-
  传统SPR生物传感器依赖金属-介电界面折射率变化，灵敏度难以达到临床所需的亚飞摩尔级。tBLG虽具有VHS增强光吸收的潜力，但实验上实现微安级光电流通常需要>1000 μW的强光照射，低光条件下光电转换效率不足。纳米结构化可增强二维材料光-物质相互作用，但如何在低光照下同时实现高响应度和生物分子特异性识别仍是未解决的挑战。
作者的问题意识:: >-
  如何利用tBLG转角可调的VHS光电特性，在低光照（60 μW）条件下实现高效光电转换，并将其与CRISPR-Cas12a的特异性分子识别通过DNA折纸术集成，构建一个突破传统光学传感器检测极限、无需外部扩增的超灵敏生物传感平台？
主要研究对象:: >-
  9.4°转角的扭曲双层石墨烯（tBLG），其VHS能量间隔约1.84 eV，与660 nm激光（1.88 eV）和金纳米盘局域表面等离子体共振（LSPR）峰精确对齐。器件由SiO₂/Si基底上的tBLG、周期274 nm、厚 50 nm 的金纳米盘阵列、四面体DNA折纸定位的金纳米颗粒（AuNPs）以及CRISPR-Cas12a系统组成。选择9.4°大转角还可避免小转角（<5°）常见的制备缺陷。
主要研究方法:: >-
  理论计算：DFT（PBE泛函，平面波截断500 eV，2×2×1 K网格，DFT-D3范德华校正，15 Å真空层）计算能带；DFPT计算介电常数；FDTD模拟反射光谱和电磁场热点分布。实验制备：CVD生长石墨烯、飞秒激光切割、高精度旋转台转移、电子束光刻（EBL, EBPG 5150）制备Cr/Au电极（10/40 nm）和金纳米盘（5/45 nm）。表征：633 nm拉曼光谱、SEM、AFM、TEM、SAED、STS/STM、飞秒泵浦-探测光谱（单指数拟合τ）、空间分辨光电流映射（锁相放大器CIQTEK Melab，×100物镜，1 kHz调制）。生物验证：PAGE电泳、荧光猝灭实验、肺癌临床血浆样本（10例）与qPCR对比。统计学：OriginPro，n=3，Bonferroni校正。
研究意义:: >-
  首次将转角电子学的莫尔工程光电效应、等离子体纳米天线与CRISPR分子识别融合为统一的光电生物传感范式，实现了从光学信号到电信号的直接转换。亚飞摩尔级灵敏度和免扩增、免标记、实时检测能力为下一代精准诊断和即时检测（POCT）提供了可扩展框架，也为莫尔超晶格在生物医学领域的应用开辟了新方向。
研究结论:: >-
  9.4° tBLG的VHS能量（1.84 eV）与金纳米盘LSPR及660 nm光子能量（1.88 eV）精确对齐，形成激子-等离激元强耦合，在60 μW低光照下实现14.64 mA/W的光响应度，是纯tBLG（2.34 mA/W）的6.27倍，EQE达27.51%，光电流增强约7倍。泵浦-探测显示耦合体系载流子弛豫时间从纯tBLG的1.14 ps缩短至371.11 fs。DFPT揭示9.4° tBLG面内介电常数（εXX/εYY）比13.2°和21.8°高数个数量级，而面外εZZ始终较低。CRISPR-Cas12a反式切割释放AuNPs后吸收峰从684 nm蓝移至663 nm，恢复耦合。对miRNA-21的检测限达44.63 aM（IUPAC 3σ标准，阈值6.45%），动态范围10 aM–100 pM（跨7个数量级），检测时间<1小时，可区分单核苷酸错配，PBS和全血中20天稳定性良好，10例肺癌样本与qPCR结果高度一致。
对领域的贡献:: >-
  概念上首次提出并验证"转角电子学-等离激元-CRISPR生物传感"融合范式，开创莫尔增强光电子学在生物传感中的应用。技术上通过DNA折纸术解决了纳米尺度多组件精确集成和动态介电调控难题，将免扩增核酸检测灵敏度推至44.63 aM，超越传统DNA传感器四个数量级。理论上系统揭示了扭转角、面内介电常数、等离激元耦合与光电流增强之间的定量关系，VHS能量公式E_vhs = E₀|sin(3θ)|（E₀=3.9 eV）为范德华异质结光电器件设计提供了指导。方法上建立了可更换crRNA即可检测不同靶标的通用平台框架。
未来研究方向提及:: >-
  作者明确指出：（1）拓展多路复用检测，同时检测多种疾病标志物；（2）将检测对象从核酸拓展至蛋白质、外泌体等其他生物标志物；（3）推进大规模多中心临床队列研究，开发集成化、便携式读出设备；（4）发展可大规模生产的低成本器件制造工艺（如纳米压印光刻替代EBL）。
未来研究方向思考:: >-
  可系统探索"转角-纳米天线-光源"三维参数空间，寻找其他转角（如13.2°）配合不同波长光源和纳米天线的性能窗口；将tBLG替换为其他二维莫尔体系（如MoS₂/WS₂异质结）可能拓展检测波长范围；建立AuNP位置-局域介电函数-耦合强度-光电流的定量物理模型以替代当前定性解释；设计比率型或signal-off探针降低假阳性；栅压动态扫描介电常数有望在同一器件上实现多靶标可调检测；DFPT介电常数计算流程可迁移至其他二维铁电/介电材料的器件设计；等离子体热点限域（FWHM ~1.5 μm）结合单分子检测技术有望实现数字式生物传感。
tags:
  - paper
  - type/experiment
  - year/2025
  - project/project-5
  - project/project-6
  - relevance/project-5/weak
  - relevance/project-6/weak
  - concept/moire-superlattice
  - concept/2d-materials
  - concept/density-functional-theory
  - concept/twistronics
  - concept/van-hove-singularity
  - concept/exciton-plasmon-coupling
  - concept/surface-plasmon-resonance
  - concept/crispr-cas12a
  - concept/dna-origami
  - concept/dielectric-response
  - concept/photoresponsivity
  - entity/twisted-bilayer-graphene
  - entity/graphene
  - entity/gold-nanodisks
  - entity/gold-nanoparticles
  - entity/VASP
  - method/dft
  - method/dfpt
  - method/fdtd
  - method/raman-spectroscopy
  - method/sem
  - method/tem
  - method/afm
  - method/sts-stm
  - method/pump-probe-spectroscopy
  - method/ebl
  - method/cvd
  - method/page-gel-electrophoresis
  - method/photocurrent-mapping
  - method/lock-in-amplifier
  - method/saed
  - material/twisted-bilayer-graphene
  - material/gold
  - material/dna-origami
  - material/mirna-21
  - topic/twistronics
  - topic/biosensing
  - topic/plasmonics
  - topic/2d-materials
  - topic/photocurrent-sensing
  - topic/crispr
  - topic/van-hove-singularity
---

## duUltrasensitiveOptoelectronicBiosensor2025 — 基于扭曲双层石墨烯超晶格的超灵敏光电生物传感器阵列

## 📄 元数据
Bowen Du, Xilin Tian, Zhi Chen, Yanqi Ge, Chuanghu Chen, Haiyan Gao, Zhongyang Liu, Jungchen Tung, Dror Fixler, Songrui Wei, Shi Chen, Han Zhang，2025，National Science Review, 12(10): nwaf357，DOI: 10.1093/nsr/nwaf357
## 💡 一句话
将9.4°扭曲双层石墨烯的范霍夫奇点吸收与金纳米盘等离激元共振精确耦合，并通过DNA折纸-CRISPR-Cas12a系统动态调制局域介电环境，在60 μW低光照下实现了44.63 aM的免扩增核酸检测。
## 🔗 Wiki 双链
  - 概念 [[../concepts/moire-superlattice]]
  - 概念 [[../concepts/2d-materials]]
  - 概念 [[../concepts/density-functional-theory]]
  - 概念 [[../concepts/twistronics|转角电子学]]
  - 概念 [[../concepts/van-hove-singularity|范霍夫奇点]]
  - 概念 [[../concepts/exciton-plasmon-coupling|激子-等离激元耦合]]
  - 概念 [[../concepts/crispr-cas12a|CRISPR-Cas12a]]
  - 概念 [[../concepts/dna-origami|DNA折纸术]]
  - 概念 [[../concepts/dielectric-response|介电响应]]
  - 实体 [[../entities/twisted-bilayer-graphene|扭曲双层石墨烯]]
  - 实体 [[../entities/graphene|石墨烯]]
  - 实体 [[../entities/gold-nanodisks|金纳米盘]]
  - 实体 [[../entities/VASP|VASP]]
  - 图表 [[../figures/electronic-bands]]
  - 图表 [[../figures/optical-spectra]]
  - 图表 [[../figures/experimental-setups]]
  - 图表 [[../figures/electronic-devices]]
  - 图表 [[../figures/heterostructures-stacking]]
  - 图表 [[../figures/heterostructures-stacking-domains-devices|铁弹畴、畴壁、In₂Se₃ 与器件应用 (Domains, Domain Walls, In₂Se₃ & Devices)]]
  - 年度 [[../write/2025]]
  - 相关论文 **duUltrasensitiveOptoelectronicBiosensor2025**
## 📊 关键图表
  - ![图1 传感器结构、激子-等离激元耦合原理与CRISPR检测流程](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_1_BXNBIMFM.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - ![图2 不同转角tBLG拉曼光谱、金纳米盘SEM/AFM形貌、光电流-电压/功率曲线、实时开关与空间光电流成像](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_2_TCFKNXU2.png) → [[../figures/heterostructures-stacking-domains-devices|铁弹畴、畴壁、In₂Se₃ 与器件应用]]
  - ![图3 吸收光谱蓝移、泵浦-探测载流子动力学、DFPT介电常数各向异性、DFT能带与STS验证VHS](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_3_GLKWBZ8Y.png) -> [[../figures/optical-spectra|光学与吸收光谱]]
  - ![图4 转角依赖的光响应度-光子能量关系、偏压调制、调制深度与FDTD热点模拟](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_4_9UN4Q757.png) → [[../figures/heterostructures-stacking-domains-devices|铁弹畴、畴壁、In₂Se₃ 与器件应用]]
  - ![图5 DNA折纸组装、PAGE验证、TEM三角形结构、AFM高度分布、浓度依赖光电流与检测限标准曲线](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_5_3KFW8A5V.png) → [[../figures/heterostructures-stacking-domains-devices|铁弹畴、畴壁、In₂Se₃ 与器件应用]]
  - ![图6 空间光电流成像与肺癌临床样本qPCR对比验证](../../raw/figures/duUltrasensitiveOptoelectronicBiosensor2025/fig_6_5U9MCGPA.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
## 🔬 项目连接
  - **project-5（SnTe铁电模拟）— weak**：本文使用DFPT计算tBLG的面内/面外介电常数张量（εXX/εYY/εZZ），计算流程（PBE泛函、500 eV截断、DFPT从OUTCAR读取介电张量）与铁电材料介电/声子计算在方法层面有共通之处。但其物理体系（石墨烯莫尔超晶格 vs SnTe铁电）和研究目标（光电传感 vs 铁电极化）差异很大，仅DFPT方法可参考。
  - **project-6（湿度传感器）— weak**：本文是二维材料基光电传感器，展示了利用2D材料介电环境变化进行信号转导的器件架构，以及金纳米结构增强信号的思路。湿度传感同样依赖材料表面介电/电导环境变化，但本文的靶标（核酸）、机制（CRISPR酶切+等离激元耦合）和读出方式（光电流）与湿度传感截然不同，仅"2D材料+介电环境调制+电学读出"的器件概念有形式上的可借鉴性。
  - project-1（双光子）、project-2（Mn多铁）、project-3（机械发光NN）、project-4（TTF分子计算）、project-7（CDW）：无直接项目连接。
## 🔗 项目双链
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]
- 项目 [[../projects/project-6-humidity-sensor|项目六：小花闻的电压湿度传感器]]

## 📝 组织与用词
文章采用"器件设计构建 → 物理机制验证 → 光电性能表征 → 生物传感验证 → 临床转化"的经典递进结构。先建立tBLG/金纳米盘的物理增强层，再叠加DNA折纸-CRISPR生物识别层，层层验证。值得复用的术语：
  - [[../concepts/twistronics|twistronics / 转角电子学]]
  - [[../concepts/van-hove-singularity|van Hove singularity]] (VHS) / 范霍夫奇点
  - moiré superlattice / 莫尔超晶格 [[../concepts/moire-superlattice|莫尔超晶格]]
  - [[../concepts/exciton-plasmon-coupling|exciton–plasmon coupling / 激子-等离激元耦合]]
  - localized surface plasmon resonance (LSPR) / 局域表面等离激元共振
  - trans-cleavage / 反式切割
  - [[../concepts/dna-origami|DNA origami / DNA折纸术]]
  - photoresponsivity / 光响应度
  - modulation depth (ΔM) / 调制深度
  - external quantum efficiency (EQE) / 外量子效率
  - [[../concepts/localized-surface-plasmon-resonance|localized-surface-plasmon-resonance]]
## ✏️ 可写入 Wiki 的要点
  1. 9.4° tBLG的VHS能量间隔2E_VHS ≈ 1.84 eV，与660 nm光子能量（1.88 eV）和[[../entities/gold-nanodisks|金纳米盘]]LSPR峰精确对齐，实现激子-等离激元[[../concepts/strong-coupling|强耦合]]。VHS能量与转角的经验关系为E_vhs = E₀|sin(3θ)|，E₀ = 3.9 eV。
  2. 金纳米盘/tBLG异质结在60 μW低光照下光响应度达14.64 mA/W，是纯tBLG（2.34 mA/W）的6.27倍，EQE 27.51%，光电流密度为纯tBLG的7倍。金纳米盘参数：周期274 nm，厚度 50 nm （Cr/Au 5/45 nm），异质结面积7 μm × 7 μm。
  3. 飞秒泵浦-探测揭示：纯tBLG载流子弛豫时间τ = 1.14 ± 0.10 ps（VHS态局域化载流子），金纳米盘/tBLG缩短至371.11 ± 61.98 fs（快约3倍），同时光响应度反升6.27倍，证明耦合极化激元加速了能量转移而非简单猝灭。Au-SLG仅缩短35.5%（555.62 fs vs SLG 861.44 fs）但光响应度有限，排除了纯等离激元贡献的主导地位。
  4. DFPT计算表明9.4° tBLG面内介电常数εXX/εYY比13.2° 与 21.8° tBLG高数个数量级，面外εZZ在所有转角下均低。这种强[[../concepts/migdal-eliashberg-theory|各向异性]]意味着电场仅通过面内极化有效调制，9.4°的高ε增强了界面电荷屏蔽和电场局域，放大等离激元热点。
  5. STS测量在约1.84 eV处观测到LDOS峰，与DFT计算的VHS能量和660 nm光子能量（1.88 eV）三重吻合，是VHS存在的直接实验证据。拉曼G带在9.4°最强，I_G/I_2D比SLG高约28.11倍。
  6. 9.4°器件在0.2 V偏压下即达到近100%调制深度（ΔM = (Cp−C)/(Cp+C)），阈值电压显著低于其他转角，与其高面内介电常数一致。空间光电流成像呈高斯分布，FWHM约1.5 μm，与等离激元限域尺度吻合。
  7. CRISPR-Cas12a检测机制：无靶标时DNA折纸锚定的AuNP（探针高度18–21 nm）破坏[[../concepts/exciton-plasmon-coupling|激子-等离激元耦合]]，吸收峰红移至684 nm，光电流低（关态）；靶标miRNA-21激活Cas12a反式切割ssDNA连接子，AuNP释放，吸收峰蓝移至663 nm，耦合恢复，光电流升高（开态）。残留DNA链导致峰位比原始660 nm略有红移（663 nm）。
  8. 生物传感性能：LOD = 44.63 aM（IUPAC 3σ标准，阈值6.45%），动态范围10 aM–100 pM跨7个数量级，检测时间<1小时，可区分单核苷酸错配，在PBS和全血中20天保持高响应保真度。信号变化率公式ΔI = (I₂−I₁)/I₀ × 100%（I₀基线、I₁ AuNP固定后、I₂反式切割后）。
  9. 临床验证：10例肺癌患者血浆样本中miRNA-21 与 miRNA-155检测结果与qPCR高度一致，且本传感器信号变化率显著高于qPCR的Ct值区分度，展示了更高的信号对比度。
  10. DFT计算参数：GGA-PBE泛函，平面波截断500 eV，2×2×1 Monkhorst-Pack K网格，15 Å z轴真空层，力收敛0.01 eV/Å，能量收敛10⁻⁵ eV（弛豫）/10⁻⁷ eV（SCF），DFT-D3范德华校正，介电常数由DFPT计算从OUTCAR读取。器件制备采用CVD[[../entitys/graphene|石墨烯]]、800 nm飞秒激光切割、EBL（EBPG 5150）图案化。
