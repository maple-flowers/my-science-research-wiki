---
citekey: Scremin2018nonlinear
title: "Nonlinear absorption of tetrathiafulvalene radical cation (TTF+) based charge transfer (CT) aggregates in PMMA"
authors: [Barbara Federica Scremin]
year: 2018
journal: "Organic Electronics"
doi: "10.1016/j.orgel.2018.06.011"
url: "https://doi.org/10.1016/j.orgel.2018.06.011"
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/Scremin2018nonlinear]]
projects: [project-4, project-1]
concepts: [nonlinear-absorption, saturable-absorption, charge-transfer, z-scan, two-level-system, steady-state-rate-equations, excited-state-lifetime, gaussian-beam, radical-cation, dismutation-equilibrium, mixed-valence, weight-factor-approximation]
entities: [TTF, PMMA, TTFClO4, Origin, titanium-sapphire-laser]
methods: [open-aperture-z-scan, femtosecond-spectroscopy, absorption-spectroscopy, rate-equation-modeling, solvent-casting, gaussian-beam-integration, analytical-fitting]
materials: [TTF+, PMMA, TTFClO4]
figures: []
领域基础知识:: >-
  非线性光学研究材料在强光下吸收系数随光强变化的行为。饱和吸收是指当光强增大到一定程度时，基态粒子被大量抽运到激发态，可吸收光子的粒子数减少，导致吸收系数下降、透过率升高的现象。Z扫描是一种通过让样品沿聚焦高斯光束光轴移动来测量非线性吸收（开孔）和非线性折射（闭孔）的标准单光束技术。四硫富瓦烯（TTF）具有三种稳定氧化态（TTF⁰、TTF⁺、TTF²⁺），其自由基阳离子盐易形成二聚体和高阶聚集体，并在近红外出现强而宽的电荷转移（CT）吸收带。
研究背景:: >-
  TTF及其衍生物因π电子体系和多氧化态在超分子化学、传感器、逻辑门和氧化还原开关中具有应用前景。TTF⁺盐晶体光学密度过高无法进行透射式测量，在极性溶剂中又会发生歧化反应（2TTF⁺ ⇌ TTF⁰ + TTF²⁺）而不稳定，因此其超快非线性光学性质长期未被研究。作者先前发展了将TTFClO₄通过溶剂浇铸嵌入PMMA薄膜的策略，得到30 μm厚、可透光且能在空气中达到歧化平衡的样品，为本研究奠定了基础。
作者的问题意识:: >-
  作者希望首次在飞秒时间尺度上表征TTF⁺ CT聚集体的非线性吸收，并从中提取CT激发态寿命。传统Z扫描拟合公式依赖低饱和强度近似（I ≪ Isat），在飞秒高光强下失效；而已有改进模型（Gu等2006，Adomian分解法）虽避免低饱和近似，却仍默认稳态，且通常只输出非线性吸收系数而不计算寿命。作者进而质疑：当拟合出的寿命与脉冲宽度相当时，稳态假设本身是否还成立？
主要研究对象:: >-
  PMMA基质中由TTFClO₄形成的TTF⁺自由基阳离子电荷转移聚集体（二聚体及高阶聚集体），薄膜厚度30 μm。真空下吸收光谱在~800 nm有强而宽的CT带（二聚体及高阶聚集体特征）；空气暴露数小时后出现~300 nm的TTF⁰带和~1400 nm的TTF⁺-TTF⁰混合价态CT带，但800 nm的TTF⁺ CT带仍部分保留，作者据此将800 nm激发近似为对TTF⁺聚集体的二能级激发。
主要研究方法:: >-
  开孔Z扫描技术：光源为锁模钛宝石再生放大器（Tsunami/Spitfire，Spectra Physics），波长792 nm，脉宽125 fs，重频100 Hz（经测试无热累积），聚焦透镜f=160 mm，远场大面积硅光电二极管采集，位移台分辨率1 μm。建模从稳态二能级速率方程ΔNss=ΔN₀/(1+2τσI/ħω)出发，定义Isat=ħω/(2τσ)，不做低饱和近似直接积分衰减方程；对高斯光束径向分布引入权重因子c_r≈0.5、对高斯脉冲时间分布引入c_t≈0.7，将嵌套指数的超越方程解耦，解析得到归一化透过率公式（文中式15）。用Origin 6拟合实验Z扫描曲线得到Isat，再由σ=1.10×10⁻¹⁸ cm²/dimer反推CT态寿命τ。独立测定的参数还包括Z₀=0.159 cm、αL=1.47。
研究意义:: >-
  首次报道了TTF⁺ CT聚集体在飞秒regime的饱和吸收特性，给出了CT态寿命的定量估计（百飞秒量级）。方法上提供了一个不依赖低饱和强度近似、可直接用于高光强Z扫描数据拟合并提取激发态寿命的解析公式，便于嵌入Origin等常用软件。更重要的是，作者通过将提取的寿命与脉冲宽度对比，揭示了超快Z扫描文献中普遍被忽视的稳态假设适用性问题，具有方法论警示价值。
研究结论:: >-
  PMMA中TTF⁺聚集体在792 nm、125 fs激发下表现为饱和吸收；固定所有实验参数拟合时峰值被高估，将衍射长度Z₀释放为自由参数后拟合显著改善。两种拟合方式所得CT态寿命均在100–200 fs范围，与脉冲宽度（125 fs FWHM）同量级，这使得速率方程的稳态前提（dN/dt=0）并不牢固。文献中通常只从拟合提取非线性吸收系数而不计算寿命，因而掩盖了时间尺度不匹配这一根本问题；纯TTF⁺体系在空气中会演化至TTF⁺、TTF⁰、TTF²⁺共存的平衡态。
对领域的贡献:: >-
  (1) 实验上首次将TTF⁺ CT聚集体的非线性光学研究推进到飞秒时间尺度，并验证了PMMA包埋是研究不稳定高光学密度分子体系的有效策略；(2) 方法上发展了避开低饱和近似、用权重因子解析处理高斯光束时空积分超越方程的Z扫描拟合公式，形式简洁可直接复用；(3) 概念上明确指出当激发态寿命与脉冲宽度可比拟时，所有基于稳态假设的Z扫描拟合（包括本文和Gu等2006的工作）都存在自洽性危机，呼吁发展非稳态模型。
未来研究方向提及:: >-
  作者明确指出文献中尚无不采用稳态假设的吸收系数模型，需要发展基于含时速率方程的非稳态Z扫描理论；应使用泵浦-探测等时间分辨技术直接测量CT态动力学，以独立校验Z扫描反演结果；并可将方法推广到其他TTF衍生物、不同基质环境，以及空气暴露后形成的1400 nm混合价态聚集体的低能CT跃迁。
未来研究方向思考:: >-
  可进一步量化权重因子c_r、c_t对光束横向模式、脉冲波形和样品厚度的敏感性，并把约2%的积分近似误差传播到最终寿命的总不确定度；二能级模型可能忽略激发态吸收、双光子吸收等高阶过程，需用多能级速率方程或密度矩阵方法检验；PMMA中聚集体尺寸、堆积形态和局域环境存在非均匀分布，测得的寿命实为平均值，发展分布式非稳态模型可能更贴近实际；将该实验寿命与TDDFT/多体理论计算的激发态能量、振子强度和辐射/非辐射衰减率对照，可建立TTF CT聚集体的结构-寿命关系，并为TTF分子计算项目提供实验校验锚点。
tags:
  - paper
  - type/experiment
  - year/2018
  - project/project-4
  - project/project-1
  - relevance/project-4/strong
  - relevance/project-1/medium
  - concept/nonlinear-absorption
  - concept/saturable-absorption
  - concept/charge-transfer
  - concept/z-scan
  - concept/two-level-system
  - concept/steady-state-rate-equations
  - concept/excited-state-lifetime
  - concept/gaussian-beam
  - concept/radical-cation
  - concept/dismutation-equilibrium
  - concept/mixed-valence
  - concept/weight-factor-approximation
  - entity/TTF
  - entity/PMMA
  - entity/TTFClO4
  - entity/Origin
  - entity/titanium-sapphire-laser
  - method/open-aperture-z-scan
  - method/femtosecond-spectroscopy
  - method/absorption-spectroscopy
  - method/rate-equation-modeling
  - method/solvent-casting
  - method/gaussian-beam-integration
  - method/analytical-fitting
  - material/TTF+
  - material/PMMA
  - material/TTFClO4
  - topic/nonlinear-optics
  - topic/charge-transfer-salts
  - topic/ttf
  - topic/femtosecond-spectroscopy
  - topic/organic-electronics
  - topic/molecular-crystal
---

## Scremin2018nonlinear — 四硫富瓦烯阳离子自由基（TTF⁺）电荷转移聚集体在PMMA中的非线性吸收

## 📄 元数据
Barbara Federica Scremin，2018，*Organic Electronics* 61, 329–333，DOI [10.1016/j.orgel.2018.06.011](https://doi.org/10.1016/j.orgel.2018.06.011)
## 💡 一句话
用开孔飞秒Z扫描结合一个不做低饱和近似的解析拟合公式，首次测得PMMA中TTF⁺ CT聚集体的激发态寿命为百飞秒量级，并据此揭示稳态速率方程模型在超快脉冲下的自洽性危机。
## 🔗 Wiki 双链
  - 图表 [[../figures/optical-spectra]]、[[../figures/mathematical-models]]
  - 概念 [[../concepts/nonlinear-absorption|非线性吸收]]、[[../concepts/saturable-absorption|饱和吸收]]、[[../concepts/charge-transfer|电荷转移（CT）]]、[[../concepts/z-scan|Z扫描]]、[[../concepts/two-level-system|二能级系统]]、[[../concepts/steady-state-rate-equations|稳态速率方程]]、[[../concepts/excited-state-lifetime|激发态寿命]]、[[../concepts/weight-factor-approximation|权重因子近似]]、[[../concepts/mixed-valence|混合价态]]
  - 实体 [[../entities/TTF|TTF（四硫富瓦烯）]]、[[../entities/PMMA|PMMA（有机玻璃）]]、[[../entities/TTFClO4|TTFClO₄（高氯酸四硫富瓦烯盐）]]
  - 年度 [[../write/2018]]
  - 项目 [[../projects/project-4-ttf-molecular-calc]]、[[../projects/project-1-two-photon]]
  - 相关论文 [[../../raw/note/Scremin2018nonlinear]]
## 📊 关键图表
> 说明：`raw/figures/Scremin2018nonlinear/` 下仅有 manifest.json，没有实际图片文件，以下按笔记文字描述逐图给出说明，不伪造图片路径。

**图1：TTFClO₄/PMMA薄膜的吸收光谱**
  - **图示描述**：TTFClO₄通过溶剂浇铸嵌入PMMA薄膜后的稳态吸收光谱，分为左右两部分——左图为真空条件下室温（蓝）与15 K低温（红）两条曲线，右图为室温下薄膜在空气中暴露数小时达到平衡后的光谱；横轴为波长（覆盖紫外到近红外约300–1400 nm），纵轴为吸光度。
  - **关键特征**：约800 nm处存在一个强而宽的电荷转移（CT）吸收带，归属于TTF⁺二聚体及高阶聚集体，是后续792 nm飞秒共振激发的直接依据；空气暴露后新增约300 nm的TTF⁰带和约1400 nm的TTF⁺–TTF⁰混合价态低能CT带，反映O₂结合TTF²⁺形成S-氧化物并移动歧化平衡（2TTF⁺ ⇌ TTF⁰ + TTF²⁺）；与溶液中歧化完全、CT带消失不同，PMMA中反应达到平衡态，800 nm的TTF⁺ CT带仍部分保留，从而支撑二能级近似。
  - **结论/意义**：该图既验证了PMMA包埋策略稳定TTF⁺聚集体的有效性，也为800 nm激发近似为对TTF⁺聚集体的二能级跃迁提供了光谱依据。

**图2：开孔Z扫描实验曲线与理论拟合**
  - **图示描述**：归一化透过率 T_N 随样品位置 Z（相对于焦点）变化的开孔Z扫描曲线，散点为实验数据，实线为文中式(15)的拟合；左图为固定表1中全部实验参数的拟合，右图为将衍射长度 Z₀（瑞利长度）释放为自由参数后的拟合；横坐标为 Z（cm），纵坐标为归一化透过率，曲线在焦点（Z≈0）处出现典型饱和吸收峰。
  - **关键特征**：焦点处光强最高、吸收被饱和，透过率形成对称的"峰"，直接表明材料表现为饱和吸收；固定参数拟合在峰值处明显高估实验值；释放Z₀为自由参数后拟合显著改善，说明实际光束衍射特性与理想高斯光束理论值存在偏差；拟合参数 P1=1/I_sat、P2=Z_c、P3=Z₀、P4=αL，由P1可反推饱和强度 I_sat，再由 I_sat=ħω/(2τσ) 与 σ=1.10×10⁻¹⁸ cm²/dimer 计算CT态寿命 τ。
  - **结论/意义**：该图展示了不依赖低饱和近似的解析拟合公式在高光强飞秒Z扫描数据上的适用性，并通过Z₀自由拟合策略提高了参数提取的可靠性。

**图3：两种拟合方式下估算的CT态寿命**
  - **图示描述**：以柱状或带状图展示由图2两种拟合（固定参数与释放Z₀）分别反推出的TTF⁺聚集体CT激发态寿命，蓝色条带标注激发脉冲的半高全宽 Δτ_FWHM = 125 fs 作为时间尺度参照；纵轴为寿命（fs）。
  - **关键特征**：两种拟合方式所得CT态寿命均落在100–200 fs范围内，与125 fs脉冲宽度处于同一量级，甚至可能短于脉宽；这意味着在脉冲作用期间体系无法建立 dN/dt=0 的稳态，式(1)(2)所依赖的稳态前提并不牢固。
  - **结论/意义**：该图是全文方法论批判的核心——它用自身拟合结果揭示了稳态Z扫描模型在飞秒超快 regime 下的自洽性危机，提示文献中只提取非线性吸收系数而不反推寿命的做法掩盖了时间尺度失配问题。

**表1：数据拟合所用的实验测定参数**
  - **图示描述**：以表格列出独立测量得到、用于Z扫描绝对拟合的各项参数，包括激光波长 λ、脉冲半高全宽 Δτ_FWHM、瑞利长度 Z₀、样品厚度 L、吸收截面 σ 和线性吸收-厚度积 αL。
  - **关键特征**：λ = 792 nm（对应TTF⁺ CT带）；Δτ_FWHM = 125 fs = 125×10⁻¹⁵ s；Z₀ = 0.159 cm；L = 30 μm，满足 L ≪ Z₀ 的薄样品近似；σ = 1.10×10⁻¹⁸ cm²/dimer；αL = 1.47（无量纲）。
  - **结论/意义**：该表为"绝对测量"提供了完整输入，使寿命可由拟合饱和强度直接反推，而不只是得到无量纲的非线性系数。

## 🔬 项目连接
  - **project-4（TTF分子计算）— strong**：本文直接研究TTF⁺自由基阳离子及其二聚体/高阶聚集体，正是项目四的核心分子体系。可复用的实验锚点包括：TTF⁺聚集体CT跃迁能量（~800 nm ≈ 1.55 eV）、吸收截面（1.10×10⁻¹⁸ cm²/dimer）、CT态寿命（~100–200 fs），以及歧化反应2TTF⁺ ⇌ TTF⁰ + TTF²⁺在PMMA中达到平衡、在溶液中完全转化的对比。这些数据可用于校验DeepMD/MACE势函数训练中对不同电荷态TTF分子几何与层间作用的描述，也提示在构建训练集时需覆盖TTF⁰/TTF⁺/TTF²⁺多种电荷态及混合价堆积。
  - **project-1（双光固化/双光发光）— medium**：本文以800 nm飞秒激光研究非线性吸收，所使用的开孔Z扫描方法、饱和吸收公式推导、稳态vs非稳态的讨论，对双光子吸收材料的非线性光学表征具有直接方法学参考价值；尤其警示在飞秒高光强下低饱和近似失效、稳态寿命反演需与脉宽对比，这对双光子激发态动力学分析同样适用。材料体系本身（TTF⁺/PMMA）与项目一的光固化树脂不同，故为方法/物理类比而非核心文献。
  - project-2、project-3、project-5、project-6、project-7：无直接项目连接。
## 🔗 项目双链
- 项目 [[../projects/project-4-ttf-molecular-calc|项目四：lsl老师的ttf分子计算]]
- 项目 [[../projects/project-1-two-photon|项目一：双光固化和双光发光]]

## 📝 组织与用词
论文按"引言（材料难点与PMMA策略）→ 实验/建模/结果（Z扫描装置 + 二能级稳态模型推导 + 权重因子处理超越方程 + Origin拟合）→ 讨论（寿命与脉宽同量级，质疑稳态假设）→ 结论（重申方法贡献与文献普遍盲区）"组织。建模部分的论证链条是：从式(1)稳态粒子数差→式(2)未作低饱和近似的衰减方程→式(5)(10)代入高斯光束时空分布后出现超越方程式(7)(12)→用c_r、c_t解耦→式(15)可拟合的归一化透过率。值得复用的术语：
  - [[../concepts/saturable-absorption|**saturable absorption / 饱和吸收**：焦点处透过率升高形成Z扫描峰]]
  - [[../concepts/charge-transfer|**charge-transfer]] (CT) aggregate / 电荷转移聚集体**：TTF⁺二聚体及高阶聚集体
  - **open-aperture Z-scan / 开孔Z扫描**：对非线性吸收敏感、对折射不敏感
  - **steady-state assumption / 稳态假设**：dN/dt=0，要求τ ≪ 脉宽
  - **low-saturation regime / 低饱和区**：I ≪ Isat，传统级数展开近似成立的条件
  - **saturation intensity / 饱和强度**：Isat = ħω/(2τσ)
  - **transcendental form / 超越形式**：嵌套指数exp[−c·exp(−x²)]无法初等积分
  - **dismutation equilibrium / 歧化平衡**：2TTF⁺ ⇌ TTF⁰ + TTF²⁺
  - [[../concepts/mixed-valence|**mixed-valence aggregate / 混合价态聚集体**：TTF⁺-TTF⁰，对应~1400 nm低能CT带]]
  - [[../concepts/rayleigh-range|**Rayleigh range]] (diffraction length) / 瑞利长度（衍射长度）**：Z₀ = kw₀²/2，薄样品近似要求L ≪ Z₀
  - [[../concepts/z-scan|z-scan]]
## ✏️ 可写入 Wiki 的要点
  1. TTF⁺盐在极性溶剂（如DMSO）中形成CT二聚体但不稳定，晶体光学密度过高无法透射测量；将TTFClO₄以溶剂浇铸法嵌入PMMA制成30 μm薄膜，既解决透光性又将歧化反应冻结在平衡态，CT带得以保留。
  2. TTFClO₄/PMMA薄膜在真空下的吸收光谱：~800 nm为TTF⁺二聚体及高阶聚集体的强宽CT带；空气暴露后新增~300 nm的TTF⁰带和~1400 nm的TTF⁺-TTF⁰[[../concepts/mixed-valence|混合价态]]CT带，机制是O₂结合TTF²⁺形成S-氧化物从而移动歧化平衡。
  3. 开孔[[../concepts/z-scan|Z扫描]]实验参数：λ=792 nm，Δτ_FWHM=125 fs，重频100 Hz（无热累积），f=160 mm聚焦透镜，Z₀=0.159 cm，L=30 μm（满足L ≪ Z₀薄样品近似），σ=1.10×10⁻¹⁸ cm²/dimer，αL=1.47。
  4. [[../concepts/saturable-absorption|饱和吸收]]模型核心公式：稳态粒子数差ΔNss=ΔN₀/(1+2τσI/ħω)，饱和强度Isat=ħω/(2τσ)，未做I ≪ Isat近似时衰减方程为dI/dz=−αI/(1+I/Isat)。
  5. 数学处理创新：将高斯光束径向分布I_in(r)=I_in(0)exp(−2r²/w²)和高斯时间轮廓Pin(t)=Pin(0)exp(−4ln2·t²/Δτ²)代入后，积分中出现嵌套指数的超越方程；用峰值强度乘权重因子c_r≈0.5（空间）、c_t≈0.7（时间）将内层指数提出积分号，得到式(15)形式的解析归一化透过率，积分近似误差约2%。
  6. 拟合策略对比：用全部实验测定参数固定拟合时高估Z扫描峰值；将衍射长度Z₀释放为自由参数后拟合显著改善。两种拟合均给出CT态寿命在100–200 fs范围。
  7. 核心物理结论与自洽性悖论：提取的CT态寿命（百fs量级）与激发脉冲宽度（125 fs FWHM）同量级，意味着体系在脉冲作用期间无法达到稳态（dN/dt不可忽略），因此推导式(1)(2)所用的稳态假设本身不稳固。
  8. 文献批评：Gu等2006年用Adomian分解法虽避免了低饱和近似，但仍使用稳态吸收系数模型；更普遍的是文献只从Z扫描拟合中提取[[../concepts/nonlinear-absorption|非线性吸收]]系数而不反推寿命，从而掩盖了时间尺度失配问题，使稳态假设的适用范围长期未被讨论。
  9. 作者指出截至2018年文献中尚无不含稳态假设的吸收系数模型，明确呼吁发展含时速率方程的非稳态Z扫描理论，并用泵浦-探测等时间分辨技术独立测量寿命以校验Z扫描反演。
  10. 对TTF分子计算项目的启示：计算激发态（TDDFT/多体方法）时需重现~1.55 eV的CT跃迁和~100 fs量级的非辐射衰减；构建MLIP训练集时应同时包含TTF⁰、TTF⁺、TTF²⁺电荷态及其混合堆积，以描述歧化平衡和混合价聚集体。
