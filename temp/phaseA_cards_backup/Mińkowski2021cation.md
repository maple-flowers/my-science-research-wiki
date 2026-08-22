---
citekey: Mińkowski2021cation
title: "Cation interstitial diffusion in lead telluride and cadmium telluride studied by means of neural network potential based molecular dynamics simulations"
title_zh: "基于神经网络势的分子动力学模拟研究碲化铅和碲化镉中阳离子间质扩散"
authors: [Marcin Mińkowski, Kerstin Hummer, Christoph Dellago]
year: 2021
journal: "Journal of Physics：Condensed Matter"
doi: "10.1088/1361-648X/abb740"
url: "https://doi.org/10.1088/1361-648X/abb740"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/Mińkowski2021cation]]
projects: [project-2, project-4, project-5]
concepts: [density-functional-theory, machine-learning-potential, spin-orbit-coupling, behler-parrinello-nnp, interstitial-diffusion, block-averaging-msd, arrhenius-deviation, interstitial-exchange-mechanism]
entities: [PbTe, SnTe, VASP, CdTe]
methods: [dft, md, mlip, neb]
materials: [PbTe, SnTe]
figures: []
领域基础知识:: >-
  PbTe（碲化铅）和CdTe（碲化镉）是分别属于IV-VI族和II-VI族的半导体材料，它们构成的异质结构广泛应用于中红外光电器件（如量子点激光器）。PbTe为岩盐矿结构，CdTe为闪锌矿结构，二者晶格常数非常接近，但晶格类型不同，且互不相溶。在高温退火下，该体系会发生纳米层向量子点的形态转变，该过程由原子扩散驱动，而点缺陷（尤其是间隙原子）的扩散被认为是关键。
研究背景:: >-
  实验上已能通过控制生长条件制备出高质量的PbTe/CdTe量子点结构，并观察到其形态演化，但现有的理论模型（如Cahn-Hilliard模型、动力学蒙特卡洛）均为粗粒化模型，缺乏对原子尺度微观机制（如原子如何跨界面迁移并导致晶格重构）的精确描述。为填补这一空白，需要从原子层面研究点缺陷的扩散行为，以此作为理解宏观形态演化的基础。
作者的问题意识:: >-
  作者的核心问题是：在PbTe和CdTe体材料中，阳离子间隙原子（Pb和Cd）的微观扩散机制是什么？各自对总扩散的贡献有多大？以及如何通过一种具备高精度和高效率的计算方法，来揭示这些静态计算方法（如NEB）可能遗漏的复杂动力学过程？
主要研究对象:: >-
  本征阳离子间隙原子，即位于PbTe晶格间隙中的一个额外Pb原子，以及位于CdTe晶格间隙中的一个额外Cd原子。研究其在各自体材料构成的4×4×4超胞（共512个晶格原子+1个间隙原子）中的扩散行为。
主要研究方法:: >-
  采用基于**神经网络势**（NNP）的**分子动力学**（MD）模拟。首先，通过**密度泛函理论**（DFT）计算生成大量原子构型的能量和受力数据作为“参考数据”；然后，利用这些数据训练高维神经网络，构建能够精确复现DFT势能面的NNP力场；最后，将训练好的NNP作为力场，在LAMMPS中进行长时间（纳秒级）MD模拟，从模拟轨迹中提取均方位移（MSD）来计算扩散系数，并通过分析原子位移细节来识别微观扩散机制。
研究意义:: >-
  理论层面，本研究首次清晰揭示了PbTe和CdTe中阳离子间隙扩散的“跳跃”与“交换”双机制图像，并定量给出了各自的活化能，修正了之前对单一扩散机制的认知，为理解半导体中的原子扩散提供了新的微观视角。方法学层面，成功验证了NNP-MD方法在复杂半导体缺陷动力学研究中的巨大潜力，为后续研究提供了高效且精确的计算框架，具有推广价值。
研究结论:: >-
  1. PbTe和CdTe中的阳离子间隙扩散均通过“跳跃”（间隙原子在间隙位点间移动）和“交换”（间隙原子与晶格原子互换位置）两种机制发生。2. 在PbTe中，交换机制因活化能更低而占主导；在CdTe中，跳跃机制因活化能更低而占主导。但由于交换机制的单次有效位移更长，它对总扩散的贡献在两种材料中都很重要。3. 总扩散系数的温度依赖性偏离了简单的阿伦尼乌斯关系，这是两种不同活化能机制共同作用的结果。4. 计算得到的活化能与现有实验和理论结果在数量级上可比。
对领域的贡献:: >-
  1. 提出了一个解释PbTe/CdTe体系中原子扩散的全新微观物理模型，即“交换”机制，这为理解该体系在界面处的形态演化（可能需要晶格重建）提供了关键的原子级线索。2. 建立了一套完整的NNP-MD模拟流程，该流程能处理大规模、长时间的缺陷动力学问题，为半导体缺陷工程领域提供了强有力的研究工具。
未来研究方向提及:: >-
  1. 将研究对象从单一材料扩展到**跨界面体系**，即研究Pb原子在CdTe中，以及Cd原子在PbTe中的扩散行为。2. 探索由“原子交换”机制引发的局部晶格结构（如从岩盐矿到闪锌矿）的动力学重建过程，以直接连接微观扩散与宏观形态转变。3. 开发能描述PbTe/CdTe界面的NNP，以直接模拟界面处的原子迁移。
未来研究方向思考:: >-
  1. **缺陷的耦合效应**：未来可研究间隙扩散与空位扩散之间的耦合。例如，一个交换机制产生的“新”间隙原子，是否更倾向于与随之产生的空位发生复合？2. **电荷态动力学**：发展能够描述电子结构和电荷态变化的机器学习势函数（如基于深度学习的电荷均衡方法），以更精确地模拟半导体中载流子对缺陷扩散的影响。3. **多尺度模拟的对接**：将本研究的MD模拟结果（如扩散系数、反应路径）作为输入参数，输入到更高尺度的动力学蒙特卡洛或相场模型中，从而实现从原子尺度到宏观器件的直接模拟，真正预测和优化实验工艺。
tags:
  - paper
  - type/theory
  - year/2021
  - project/project-2
  - relevance/project-2/medium
  - project/project-4
  - relevance/project-4/medium
  - project/project-5
  - relevance/project-5/medium
  - concept/density-functional-theory
  - concept/machine-learning-potential
  - concept/spin-orbit-coupling
  - entity/PbTe
  - entity/SnTe
  - entity/VASP
  - method/dft
  - method/md
  - method/mlip
  - method/neb
  - material/PbTe
  - material/SnTe
  - topic/ml-interatomic-potential
---

## Mińkowski2021cation — 基于神经网络势的分子动力学模拟研究碲化铅和碲化镉中阳离子间隙扩散

## 📄 元数据
Marcin Mińkowski, Kerstin Hummer, Christoph Dellago et al.，2021，*Journal of Physics: Condensed Matter* 33, 015901，DOI: 10.1088/1361-648X/abb740

## 💡 一句话
用 Behler–Parrinello 神经网络势（NNP）驱动长时 MD，首次揭示 PbTe（岩盐矿）和 CdTe（闪锌矿）中阳离子间隙原子均通过"直接跳跃"和"与晶格原子交换"两种机制扩散，二者活化能不同导致总扩散系数偏离 Arrhenius 行为；PbTe 中交换主导，CdTe 中跳跃主导。

## 🔗 Wiki 双链
  - 概念 [[../concepts/density-functional-theory]]
  - 概念 [[../concepts/machine-learning-potential]]
  - 概念 [[../concepts/spin-orbit-coupling]]
  - 概念 [[../concepts/interstitial-diffusion|间隙扩散]]
  - 概念 [[../concepts/interstitial-exchange-mechanism|间隙-晶格交换机制]]
  - 概念 [[../concepts/arrhenius-deviation|非阿伦尼乌斯行为]]
  - 概念 [[../concepts/behler-parrinello-nnp|Behler–Parrinello 神经网络势]]
  - 概念 [[../concepts/block-averaging-msd|MSD 块平均误差估计]]
  - 实体 [[../entities/CdTe|CdTe（碲化镉）]]
  - 实体 [[../entities/PbTe]]
  - 实体 [[../entities/SnTe]]
  - 实体 [[../entities/VASP]]
  - 图表 [[../figures/mathematical-models]]
  - 图表 [[../figures/crystal-structures]]
  - 年度 [[../write/2020-2024|2021]]
  - 项目 [[../projects/project-5-snte-ferroelectric-sim]]
  - 项目 [[../projects/project-2-mn-multiferroics]]
  - 项目 [[../projects/project-4-ttf-molecular-calc]]
  - 相关论文 [[../../raw/note/Mińkowski2021cation]]

## 🆕 新概念/实体建议
（暂无）

## 📊 关键图表
笔记未附图片（raw/figures 下仅有 manifest.json，未抽取图 1–8 图像文件；正文含图 1 轨迹投影、图 2 MSD、图 3 块平均收敛、图 4 总 D 的 Arrhenius 图、图 5–6 跳跃/交换机制示意、图 7 分机制速率 Arrhenius 图、图 8 双机制拟合，以及表 1–4 数值）。以下按论文原图号逐图给出中文描述。

图1：700 K 下 PbTe 中 Pb 间隙与 CdTe 中 Cd 间隙的二维轨迹投影
  - **图示描述**：nnp-1 势函数在 700 K 下单个阳离子间隙原子约 2 ns MD 轨迹在 xy 平面的投影，上下两子图分别为 PbTe 与 CdTe；绿圈为起点、红圈为终点。
  - **关键特征**：轨迹呈离散跳跃式而非连续布朗运动，PbTe 中轨迹覆盖范围明显大于 CdTe，直观显示 Pb 间隙扩散更快；为后续区分"跳跃"与"交换"两种机制提供视觉证据。

图2：PbTe 与 CdTe 中单间隙原子的均方位移（MSD）随时间变化
  - **图示描述**：nnp-1 在 700–1200 K 多个温度下 MSD（Å²）对时间（ps）的双对数/线性曲线，虚线为 2–14 ps 区间线性拟合。
  - **关键特征**：短时（< 2 ps）为弹道区、长时（> 14 ps）统计误差增大，2–14 ps 为爱因斯坦扩散线性区，由斜率除以 6 得 D；温度越高斜率越大、扩散越快，是提取扩散系数的核心图。

图3：700 K 下 MSD 的块平均法收敛性检验
  - **图示描述**：nnp-1 在 700 K 下 PbTe（红）与 CdTe（蓝）的 M_Bσ²_B（Å⁴）随块大小 M_B 变化曲线。
  - **关键特征**：两曲线均在 M_B ≈ 3500 处达到平台，PbTe 平台 s ≈ 8.0×10⁴ Å⁴、CdTe ≈ 1.2×10⁴ Å⁴；对应扩散系数误差 ΔD 分别为 7.46×10⁻⁷ 与 9.13×10⁻⁷ cm²/s，证明 10 ps 滞后下采样已充分收敛、误差估计可靠。

图4：三个独立 NNP 得到的总扩散系数 Arrhenius 图
  - **图示描述**：PbTe 与 CdTe 中 nnp-1/2/3 给出的 D（cm²/s，对数轴）对 1000/T（K⁻¹）散点（带误差棒）及单一 Arrhenius 项拟合直线。
  - **关键特征**：三个独立训练的 NNP 趋势和数量级高度一致，验证方法鲁棒性；数据点略偏离直线，暗示多机制并存；PbTe 表观 Ea = 250–338 meV、CdTe = 368–391 meV（表 2）；PbTe 在低温区 D 更大、CdTe 在高温区反超，源于 Ea 与 D0 的竞争。

图5：PbTe 中 Pb 间隙的跳跃与交换机制示意
  - **图示描述**：岩盐矿 PbTe 晶格中，跳跃沿 [100] 在等价间隙位间移动、步长 a/2；交换时间隙 Pb 踢出最近邻晶格 Pb，被踢出者沿 [110] 或 [111] 成为新间隙，有效位移 a√2/2 或 a√3/2；箭头表示原子运动，透明色为末态。
  - **关键特征**：PbTe 间隙位等价、跳跃几何简单；一次交换等效 2–3 次跳跃的位移，故即使交换频次不是极高，其对总 D 贡献也很大；该图是 PbTe 中交换主导结论的图像基础。

图6：CdTe 中 Cd 间隙的跳跃与交换机制示意
  - **图示描述**：闪锌矿 CdTe 中存在 Ta（Te 四面体配位）与 Tc（Cd 四面体配位）两个不等价间隙位；跳跃沿 [110] 在 Ta↔Tc 之间、单步长 √(2/3) a；交换主要发生在两个 Tc 位之间，一次交换等效两次跳跃。
  - **关键特征**：间隙原子大部分时间占据 Ta 位、短暂经过 Tc 位（对应 Cd²⁺ 电荷态）；CdTe 路径比 PbTe 复杂，跳跃为更频繁机制，但交换单步位移更大，使两机制对总 D 贡献相当。

图7：PbTe 与 CdTe 中跳跃速率与交换速率的 Arrhenius 图
  - **图示描述**：左右两子图分别为 PbTe、CdTe，纵轴为事件速率 k（s⁻¹，对数），横轴为 1000/T；散点为按"LAMMPS 原子 ID 是否改变 + 连续 10 MD 步保持"判据从轨迹统计的 hop/exchange 事件速率，线为 Arrhenius 拟合。
  - **关键特征**：PbTe 中交换速率全程高于跳跃速率（低温约高一个数量级），CdTe 相反；随温度升高两者比值趋近 1，700 K 时差约一个数量级、1200 K 时同量级；拟合得 PbTe E_ex = 224–309 meV < E_hops = 461–564 meV，CdTe E_hops = 218–256 meV < E_ex = 399–447 meV（表 3），直接定量区分两机制贡献。

图8：双机制模型对总扩散系数的拟合
  - **图示描述**：用 D = D0^hops exp(−βE_hops) + D0^ex exp(−βE_ex)（公式 16）对图 4 同一组 D 数据重新拟合的 Arrhenius 曲线。
  - **关键特征**：双指数曲线比图 4 单一 Arrhenius 直线更贴合数据、尤其在低温区改善明显；闭环证明总 D 的弯曲来自两条不同活化能通道的并行贡献，是论文论证的"画龙点睛"图；拟合参数（表 4）与表 3 独立拟合结果一致。

表1：NNP 能量与力 RMSE（训练集/测试集）
  - **图示描述**：六个 NNP（PbTe/CdTe 各三个独立随机种子）的能量 RMSE（meV/atom）与力 RMSE（meV/Å）。
  - **关键特征**：PbTe 能量 RMSE ≈ 0.47–0.57 meV/atom、力 ≈ 69–73 meV/Å；CdTe 能量 ≈ 0.25–0.54 meV/atom、力 ≈ 55–72 meV/Å；训练/测试误差同量级表明无过拟合，CdTe 误差普遍小于 PbTe。

表2：总扩散的表观活化能与指前因子
  - **关键特征**：PbTe Ea = 250–338 meV、D0 ≈ 1.2–2.9×10⁻³ cm²/s；CdTe Ea = 368–391 meV、D0 ≈ 4.4–5.6×10⁻³ cm²/s；三个 NNP 给出的 Ea 散布 ≤ 100 meV，作者以此作为 NNP 方法活化能的不确定度估计。

表3：分机制活化能 E_hops 与 E_ex
  - **关键特征**：PbTe 中 E_ex（224–309 meV）远低于 E_hops（461–564 meV），故交换主导；CdTe 中 E_hops（218–256 meV）低于 E_ex（399–447 meV），故跳跃更频繁；每个 NNP 的表观 Ea（表 2）均落在表 3 两值之间，自洽支持双机制图像。

表4：双机制模型（公式 16）的指前因子
  - **关键特征**：给出 D0^hops 与 D0^ex，用于图 8 的双项拟合；相比表 2 单 Arrhenius 项，用表 3/4 参数能更好复现总 D 的温度弯曲。


## 🔬 项目连接
  - **project-1 双光子**：无直接项目连接。
  - **project-2 Mn 多铁（缺陷/掺杂调控）**：有方法参考价值。本文展示的"DFT 参考数据 → 迭代训练 NNP（以外推警告和多网络分歧主动加样）→ LAMMPS 长时 MD → MSD/块平均提取扩散系数 → 按原子 ID 追踪区分跳跃与交换事件 → 分机制 Arrhenius 拟合"完整流程，可直接迁移到 Mn 基多铁材料中掺杂/间隙离子迁移、缺陷动力学的模拟；其"交换机制导致协同输运"的物理图像也可类比缺陷在钙钛矿晶格中的迁移。对讨论缺陷如何介导铁电/磁序耦合有参考意义。
  - **project-3 机械发光 NN**：无直接项目连接。
  - **project-4 TTF 分子计算**：有方法参考价值。Behler–Parrinello NNP 的构造细节（Rc=6 Å 截断、G2/G3/G9 对称函数、双隐层各 25 节点、Kalman 滤波优化、β=5 权衡量/力、0.08% 力子采样、50 epoch、三独立随机种子评估模型不确定性、外推警告驱动的主动学习）是把 ML 势用于分子/凝聚态体系的标准范本，对 TTF 等分子晶体若需长时动力学（如堆积重排、离子跳跃）可复用该训练协议。注意 TTF 含分子内自由度，对称函数参数需重新调参。
  - **project-5 SnTe 铁电模拟**：参考价值最强。SnTe 与 PbTe 同为 IV–VI 族岩盐矿结构、晶格常数相近（a≈6.46 Å），且 SnTe 是铁电/拓扑材料。本文在 PbTe 中得到的 Pb 间隙跳跃（沿 [100]，步长 a/2）与交换（沿 [110]/[111]，有效步长 a√2/2 或 a√3/2）双机制、交换活化能（224–309 meV）低于跳跃活化能（461–564 meV）因而交换主导、总表观活化能 250–338 meV 等结论，可直接作为 Sn 间隙在 SnTe 中扩散的对照基线和方法模板；NNP-MD 能发现静态 NEB 预设路径之外的新机制这一优势，对研究 SnTe 中缺陷介导的铁电畴翻转/极化退化尤其有启发。
  - **project-6 湿度传感器**：无直接项目连接。
  - **project-7 CDW**：无直接项目连接。

## 🔗 项目双链
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]
- 项目 [[../projects/project-4-ttf-molecular-calc|项目四：lsl老师的ttf分子计算]]
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]

## 📝 组织与用词
论文按"应用背景（PbTe/CdTe 量子点形态演化）→ 体系晶体学（岩盐矿 vs 闪锌矿、间隙位等价性）→ 方法三部曲（VASP/PBEsol 生成参考数据、n2p2 训练 NNP、LAMMPS MD）→ 结果（NNP 误差、MSD 与块平均、总 D 的 Arrhenius 拟合、轨迹可视化识别两种机制、分机制速率拟合、双机制模型重拟合）→ 与实验/NEB 对比 → 结论与跨界面展望"线性展开。论证的关键转折是：总 Arrhenius 图略微弯曲 → 轨迹分析发现跳跃/交换两机制 → 分别统计速率并拟合活化能 → 用两项之和重拟合总 D 成功复现弯曲，形成闭环。方法严谨性体现在：三个独立随机种子训练 NNP 交叉验证、迭代式主动学习消除外推、块平均量化统计误差、用"原子 ID 是否改变 + 连续 10 步"判据区分交换与涨落。值得复用的术语：
  - neural network potential (NNP) — 神经网络势
  - [[../concepts/interstitial-exchange-mechanism|interstitial exchange mechanism — 间隙-晶格交换机制]]
  - direct hop — 直接跳跃
  - [[../concepts/arrhenius-deviation|Arrhenius deviation / non-Arrhenius behaviour — 非阿伦尼乌斯行为]]
  - symmetry functions (G2/G3/G9) — 对称函数
  - extrapolation warning — 外推警告（主动学习判据）
  - [[../concepts/block-averaging-msd|block averaging — 块平均]]（误差估计）
  - tetrahedral interstitial sites Ta/Tc — 四面体间隙位（阴离子/阳离子配位）

## ✏️ 可写入 Wiki 的要点
  1. **方法流程**：VASP（PBEsol 泛函，Γ 点，4×4×4 超胞 512/513 原子）生成能量/力参考数据 → n2p2 训练 Behler–Parrinello NNP（Rc=6 Å，G2/G3/G9 对称函数，两隐层各 25 节点，Kalman 滤波，β=5，50 epoch）→ LAMMPS 跑 700–1200 K NPT MD（2 fs 步长，≤800 K 跑 8 ns，850 K 跑 6 ns，≥900 K 跑 4 ns）。
  2. **主动学习策略**：训练集迭代扩充——把 MD 中触发外推警告最多的构型、以及两个独立 NNP 预测分歧最大的构型挑出做 DFT 标注后重训，直至相关温度区间无外推警告；过渡态附近构型靠可视化手动补入。最终 PbTe 用 4898 个构型、CdTe 用 2866 个构型（90% 训练 / 10% 测试）。
  3. **NNP 精度**：能量 RMSE 约 0.47–0.57 meV/atom（PbTe）、0.25–0.54 meV/atom（CdTe）；力 RMSE 约 69–73 meV/Å（PbTe）、55–72 meV/Å（CdTe）；三网络给出的活化能相差 ≤100 meV，作者以此作为 NNP 方法计算活化能的不确定度估计。
  4. **两种扩散机制的几何**：PbTe（岩盐矿，间隙位等价）中跳跃沿 [100]、步长 a/2；交换时间隙 Pb 踢出一个晶格 Pb，新间隙落于 [110] 或 [111] 方向，有效位移 a√2/2 或 a√3/2（一次交换等效 2–3 次跳跃）。CdTe（闪锌矿）有 Ta、Tc 两个不等价间隙位，跳跃沿 [110] 在 Ta↔Tc 之间（单步 √(2/3) a），交换主要发生在两个 Tc 位之间，一次交换等效两次跳跃。
  5. **分机制活化能（表 3）**：PbTe 中 E_ex=224–309 meV < E_hops=461–564 meV，故交换主导；CdTe 中 E_hops=218–256 meV < E_ex=399–447 meV，故跳跃更频繁。由于交换单步位移更大，即使在 CdTe 中两种机制对总 D 的贡献也相当。
  6. **总活化能与非 Arrhenius 行为**：PbTe 表观 Ea=250–338 meV、D0≈1.2–2.9×10⁻³ cm²/s；CdTe 表观 Ea=368–391 meV、D0≈4.4–5.6×10⁻³ cm²/s。总 D 用 D = D0^hops exp(−βE_hops) + D0^ex exp(−βE_ex) 双项拟合比单一 Arrhenius 项更贴合数据，证明弯曲来自两机制并行。
  7. **间隙原子追踪方法**：将"邻居数最多的原子"定义为间隙原子；为排除高温热涨落造成的误判，只有当新间隙原子身份连续保持 10 个 MD 步（20 fs）才计为一次交换事件。跳跃/交换的区分依据是事件前后 LAMMPS 原子 ID 是否改变。
  8. **扩散系数提取**：MSD 取 2–14 ps 线性区，由 D=MSD斜率/(2d)（d=3）得到；统计误差用块平均法在 10 ps 滞后上估计，当 M_B σ²_B 对块大小 M_B 达到平台 s 时，σ²(⟨MSD⟩)=s/M，ΔD=σ(⟨MSD⟩)/(6t)。
  9. **与实验/NEB 对比**：PbTe 中 Pb 扩散实验活化能 249 meV（放射性同位素）与计算 250–338 meV 吻合，但实验 D0≈3.1×10⁻⁶ cm²/s 比计算小约三个数量级——作者认为放射性示踪对交换机制不敏感；CdTe 在 800 K 实验 D≈1.75×10⁻⁶ cm²/s，比计算小约一个数量级；NEB 给出 CdTe 间隙势垒 330 meV，与计算 368–391 meV 接近，但 NEB 因端点固定无法发现交换机制。
  10. **局限与展望**：DFT 未加自旋轨道耦合（对含 Pb/Te 重元素体系是潜在系统误差）；NNP 隐式拟合电荷态、无法描述 Cd 间隙 Cd⁰/Cd⁺/Cd²⁺ 的动态电荷转变（模拟主要对应 Cd²⁺）；只算了单种阳离子自间隙、未含界面、未计空位-间隙耦合。下一步应把 NNP 训练扩展到 PbTe/CdTe 界面和异类阳离子（Pb in CdTe、Cd in PbTe），验证"交换导致局部岩盐矿↔闪锌矿重构从而驱动量子点形态演化"的假说。
