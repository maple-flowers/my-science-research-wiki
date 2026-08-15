---
citekey: TSUJI2019phosphorescence
title: "Phosphorescence light decay curve from mechanoluminescence material subjected to hydrostatic load"
authors: [Tomoaki TSUJI, Tomohisa Kojima]
year: 2019
journal: "The Proceedings of the Materials and Mechanics Conference (JSME)"
doi: "10.1299/jsmemm.2019.OS0512"
url: "https://doi.org/10.1299/jsmemm.2019.OS0512"
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/TSUJI2019phosphorescence]]
projects: [project-3]
concepts: [mechanoluminescence, phosphorescence, exponential-decay, trap-depletion, reabsorption, hydrostatic-pressure, time-resolved-spectroscopy, carrier-detrapping]
entities: [PMT, oscilloscope, pulsed-led, photodiode]
methods: [time-resolved-phosphorescence, exponential-fitting, hydrostatic-loading, pulsed-led-excitation, pmt-detection]
materials: [mechanoluminescent-powder, elastomeric-composite]
figures: []
领域基础知识:: >-
  机械发光（mechanoluminescence, ML）是材料在机械刺激（压缩、拉伸、摩擦、静水压力等）下发光的现象，其微观机制通常与陷阱载流子在应力作用下脱陷并在发光中心复合有关。磷光（phosphorescence）是激发停止后发光仍持续的现象，其衰减曲线反映了陷阱载流子的释放动力学，常以单指数或多指数函数 I(t)=I0 exp(-t/τ)+B 拟合，τ 为磷光寿命。对 ML 材料施加静水载荷（hydrostatic load）可在不引入剪切/断裂发光干扰的情况下，研究应力如何调制陷阱释放与磷光衰减；重吸收（reabsorption）则是发射光子在样品内部被自身吸收从而改变表观衰减曲线的效应。
研究背景:: >-
  多数 ML 材料的发光特性依赖于预辐照充能，且在机械加载过程中陷阱载流子的消耗会导致发光强度随加载时间衰减，这种时间依赖性是定量 ML 应力传感必须标定的因素。本文针对一种受静水载荷的 ML 材料，测量其磷光发光强度随时间的衰减曲线，并尝试用包含吸收/重吸收因子 γ 的指数模型来描述，以区分正常衰减与受吸收调制的衰减行为，为理解 ML 材料在持续载荷下的光输出演化提供实验依据。
作者的问题意识:: >-
  作者关注的核心问题是：在静水载荷条件下，ML 材料的磷光发光强度随时间如何衰减？标准的单指数衰减模型是否足以描述实测曲线？如果发光在样品内部存在吸收（或重吸收），应如何在衰减模型中引入修正因子 γ 以及 α、β 两个分支参数，使模型能同时复现"测量曲线""指数曲线"和"吸收曲线"三种行为？
主要研究对象:: >-
  一种处于静水载荷下的机械发光（ML）材料（笔记中以含弹性体/液体的体系描述，具体化学成分在可读文本中未明确给出，可能为粉末分散于弹性基体中的 ML 复合体系）。研究对象是其在脉冲光激发后磷光发光强度随时间的衰减曲线，以及静水载荷对该曲线的调制。
主要研究方法:: >-
  采用时间分辨磷光测量装置：脉冲高功率 LED（脉宽约 20 µs，重复频率 10 Hz，由示波器触发的自制电流脉冲器驱动）激发样品，样品发射的磷光由光电倍增管（PMT）检测，信号经数字存储示波器记录；激发光强度由接放大器的光电二极管监测。在 LED 关闭后记录 PMT 信号随时间的变化，用单指数衰减模型 I(t)=I0 exp(-t/τ)+B 进行拟合，并引入吸收/重吸收因子 γ（含 α、β 参数）修正模型，将实测曲线、纯指数曲线与吸收模型曲线三者对比。
研究意义:: >-
  工作为持续静水下载荷 ML 材料的磷光动力学提供了直接的时间分辨测量与建模框架，明确指出吸收/重吸收因子 γ 对表观衰减曲线的不可忽略的影响。这对 ML 应力/应变传感器的定量标定、陷阱参数（寿命 τ、脱陷速率）的可靠提取，以及区分"力学驱动的陷阱消耗"与"光学重吸收"两种导致表观衰减的机制具有参考价值。
研究结论:: >-
  在静水载荷下，ML 材料的磷光发光强度随时间呈衰减趋势，实测曲线与指数模型总体吻合但存在偏差；引入吸收因子 γ（含 α、β 两个过程参数）的"吸收模型"能更好地复现实测的光强-时间曲线，表明发射光在样品内部的吸收/重吸收对表观磷光衰减有显著贡献。图中在 0–120 s 时间窗内同时给出 measured、exponential、absorption 三条曲线及 α、β 标识，支持了"正常衰减+吸收修正"的双过程图像。
对领域的贡献:: >-
  一是提供了静水载荷下 ML 材料磷光衰减的时间分辨实验数据（PMT+脉冲 LED+示波器装置，20 µs/10 Hz 激发方案）；二是提出以吸收/重吸收因子 γ 及 α、β 参数修正标准单指数衰减的建模思路，将"正常衰减曲线"与"吸收模型曲线"分离比较；三是提醒 ML 领域在由衰减曲线提取陷阱寿命/脱陷速率时必须扣除自吸收效应，为后续 ML 动力学建模与应力传感器标定提供了可借鉴的方法论片段。
未来研究方向提及:: >-
  笔记可读部分为会议短文，未明确列出系统的未来方向。从其逻辑可延伸的方向包括：在不同静水压力水平下系统测量 τ、γ、α、β 的压力依赖关系；将吸收模型与陷阱深度、载流子脱陷速率的物理模型结合；用热释光等独立手段标定陷阱参数并与光学拟合交叉验证；拓展到不同 ML 材料体系与弹性基体以检验模型普适性。
未来研究方向思考:: >-
  可进一步发展的方向：（1）建立 γ 与静水压力、样品厚度/颗粒浓度之间的定量关系，区分压力调制的带隙吸收与几何重吸收；（2）用双指数或拉伸指数模型替代单指数，以反映连续陷阱深度分布；（3）结合辐射传输/蒙特卡罗模拟自吸收过程，给出 γ 的微观表达式而非唯象参数；（4）将该衰减标定嵌入 ML 应力传感器的信号反演流程，实现对长时间加载下信号漂移的补偿；（5）对 project-3 的神经网络 ML 模型而言，这类带吸收修正的衰减曲线可作为训练标签或物理约束特征。
tags:
  - paper
  - type/experiment
  - year/2019
  - project/project-3
  - relevance/project-3/strong
  - concept/mechanoluminescence
  - concept/phosphorescence
  - concept/exponential-decay
  - concept/trap-depletion
  - concept/reabsorption
  - concept/hydrostatic-pressure
  - concept/time-resolved-spectroscopy
  - concept/carrier-detrapping
  - entity/pmt
  - entity/oscilloscope
  - entity/pulsed-led
  - entity/photodiode
  - method/time-resolved-phosphorescence
  - method/exponential-fitting
  - method/hydrostatic-loading
  - method/pulsed-led-excitation
  - method/pmt-detection
  - material/mechanoluminescent-powder
  - material/elastomeric-composite
  - topic/mechanoluminescence
  - topic/phosphorescence-decay
  - topic/trap-physics
  - topic/optical-sensing
---

## TSUJI2019phosphorescence — 静水载荷下机械发光材料的磷光衰减曲线

## 📄 元数据
Tomoaki TSUJI、Tomohisa Kojima，2019，The Proceedings of the Materials and Mechanics Conference (JSME)，论文编号 OS0512，DOI: 10.1299/jsmemm.2019.OS0512
## 💡 一句话
用 PMT+脉冲 LED 的时间分辨装置测量静水载荷下 ML 材料的磷光衰减曲线，并以含吸收因子 γ（α、β）的指数模型修正标准单指数衰减，揭示自吸收对表观衰减的显著影响。

## 🔗 Wiki 双链
  - 概念 [[../concepts/mechanoluminescence|机械发光]]、[[../concepts/trap-depletion|陷阱消耗]]、[[../concepts/reabsorption|重吸收]]
  - 图表 [[../figures/optical-spectra]]
  - 图表 [[../figures/mathematical-models]]
  - 图表 [[../figures/experimental-setups]]
  - 年度 [[../write/2015-2019|2019]]
  - 项目 [[../projects/project-3-mechanoluminescence-nn]]
  - 概念 [[../concepts/carrier-detrapping]]、[[../concepts/hydrostatic-pressure]]、[[../concepts/time-resolved-spectroscopy]]、[[../concepts/phosphorescence]]、[[../concepts/exponential-decay]]
  - 实体 [[../entities/PMT]]、[[../entities/pulsed-led]]、[[../entities/photodiode]]、[[../entities/oscilloscope]]
  - 相关论文 [[../../raw/note/TSUJI2019phosphorescence]]

## 🆕 新概念/实体建议
  - [[../concepts/mechanoluminescence|mechanoluminescence]]（机械发光）：wiki/concepts 下尚缺，是 project-3 的核心概念，建议新建并涵盖弹性发光、摩擦发光、断裂发光等子类。
  - [[../concepts/phosphorescence-decay|phosphorescence-decay]]（磷光衰减）：建议新建概念条目，收录单/多指数衰减、寿命 τ、陷阱释放动力学等。
  - [[../concepts/trap-depletion|trap-depletion]]（陷阱消耗/陷阱载流子耗尽）：ML 与长余辉材料在持续载荷/激发下信号衰减的共同机制，建议与 carrier-detrapping 协同建条目。
  - [[../concepts/reabsorption|reabsorption]]（重吸收/自吸收）：发光在样品内部被自身再吸收从而改变表观光谱与衰减的效应，建议建概念条目。
  - [[../entities/hydrostatic-pressure-cell|hydrostatic-pressure-cell]]（静水压加载装置）：可作为实体条目记录典型的静水载荷实验配置。
  - [[../entities/elastomeric-composite|elastomeric-composite]]（弹性体复合发光材料）：ML 粉末分散于弹性基体的典型器件形态，建议建材料实体条目。

## 📊 关键图表
  > raw/figures/TSUJI2019phosphorescence/ 下未抽取到图片文件（manifest.json 中 figures、formulas 均为空数组），以下依据 raw/note 中可读的英文转写段落以文字形式记录，不伪造图片路径。

  - **图1：磷光衰减曲线（measured / exponential / absorption 对比）**
  - **图示描述**：横轴为时间 t（0–120 s），纵轴为光强 I（约 0–4500 a.u.），同一坐标系内绘制三条曲线——measured（PMT 实测散点）、exponential（单指数拟合 I(t)=I0·exp(-t/τ)+B）、absorption（引入吸收/重吸收因子 γ 的修正模型），并以 α、β 标识吸收模型中的两个区段参数。
  - **关键特征**：①LED 关断后磷光强度随时间整体单调下降，符合单指数衰减的总体趋势；②纯指数曲线与实测之间存在系统性偏差，吸收模型曲线在 α、β 区段更贴近 measured，说明发射光子在样品内部被重吸收，对表观衰减有可观测贡献；③该图在 0–120 s 时间窗内同时呈现"正常衰减"与"吸收修正衰减"两种行为，是论文区分两种机制的核心证据。
  - **结论/意义**：支持作者关于"从衰减曲线提取磷光寿命 τ 或脱陷速率时必须扣除自吸收效应"的论断，否则会把光学重吸收误判为陷阱动力学。

  - **图2：磷光时间分辨测量装置示意图**
  - **图示描述**：展示样品在静水（含弹性体材料的液体）环境中的激发与探测光路：脉冲高功率 LED 激发样品，样品发射的磷光由光电倍增管（PMT）收集并送入数字存储示波器；LED 由示波器触发的自制电流脉冲器驱动，激发光强由接放大器的光电二极管旁路监测。
  - **关键特征**：①激发脉宽约 20 µs、重复频率 10 Hz，保证两次激发之间陷阱态有充足的衰减观测窗口；②PMT+数字存储示波器记录 LED 关断后 PMT 信号随时间的变化，得到 I(t) 衰减曲线；③光电二极管支路用于监测每次脉冲的激发光强，以归一化激发涨落；④样品处于静水载荷构型中，避免摩擦/断裂发光干扰，单独考察压力对磷光动力学的影响。
  - **结论/意义**：该装置为论文提供了可重复的时间分辨磷光测量协议（20 µs/10 Hz 脉冲 LED + PMT + 示波器），是图1三条曲线的数据来源，也是 project-3 复用 ML 衰减测量方法时可直接借鉴的配置基线。

## 🔬 项目连接
  - **project-3 机械发光NN — strong（强连接）**：本文直接研究机械发光（ML）材料在静水载荷下的磷光衰减动力学，正是 project-3 的目标材料体系与物理过程。其参考价值在于：（1）提供了 ML 材料时间分辨磷光测量的标准装置与参数（20 µs 脉冲 LED、10 Hz、PMT+示波器+光电二极管监测）；（2）给出了带吸收修正 γ(α,β) 的指数衰减建模范式，可作为神经网络训练 ML 衰减/应力响应时的物理特征或约束；（3）提醒在 ML 信号中区分"陷阱消耗导致的真衰减"与"自吸收导致的表观衰减"，对 NN 特征工程有直接指导意义。
  - project-1 双光子、project-2 Mn多铁、project-4 TTF分子计算、project-5 SnTe铁电模拟、project-6 湿度传感器、project-7 CDW：无直接项目连接（材料体系与机理均不相关）。

## 🔗 项目双链
- 项目 [[../projects/project-3-mechanoluminescence-nn|项目三：应力发光神经网络]]

## 📝 组织与用词
  文章为 JSME Materials & Mechanics 会议短文，按"装置介绍→测量方法→衰减模型（正常衰减 vs. 吸收模型，因子 γ，α/β 分支）→实测曲线与拟合对比"组织。需注意：原始笔记中的 PDF 文本存在严重 OCR 乱码，AI 解读段落中关于"无预辐照、时间依赖性应力发光新现象"的叙述系 AI 推测，与论文标题/可读文本所指的"静水载荷下磷光衰减曲线测量"不完全一致，第二步写入 wiki 时应以标题、装置描述和 I(t)–γ 模型为准，避免照搬 AI 解读中的夸大性结论。值得复用的术语：
  - [[../concepts/mechanoluminescence|mechanoluminescence]] (ML) — 机械发光
  - [[../concepts/phosphorescence-decay|phosphorescence decay — 磷光衰减]]
  - hydrostatic load — 静水载荷
  - single exponential decay — 单指数衰减
  - lifetime τ — 寿命 τ
  - absorption / reabsorption factor γ — 吸收/重吸收因子 γ
  - detrapping rate — 脱陷速率
  - time-resolved measurement — 时间分辨测量

## ✏️ 可写入 Wiki 的要点
  1. 实验装置：脉冲高功率 LED（脉宽约 20 µs，重复频率 10 Hz，自制电流脉冲器由示波器触发）激发样品；PMT 检测磷光，数字存储示波器记录信号；光电二极管+放大器监测激发光强度。
  2. 测量协议：在 LED 关闭后记录 PMT 信号随时间的变化，得到磷光强度 I(t) 衰减曲线（实测时间窗 0–120 s，光强量程约 0–4500 a.u.）。
  3. 基线模型：标准单指数衰减 I(t)=I0·exp(-t/τ)+B，其中 I0 为初始强度、τ 为磷光寿命、B 为基线偏移；论文以该模型作为"normal decay curve"。
  4. 吸收修正模型：在标准衰减基础上引入吸收/[[../concepts/reabsorption|重吸收]]因子 γ，含 α、β 两个分支参数，用以描述发射光在样品内部被吸收后对表观衰减曲线的修正，称为"absorption model"。
  5. 图中三条曲线并列对比：measured（实测）、exponential（纯指数拟合）、absorption（吸收模型），吸收模型在 α、β 标识的区段更贴近实测，表明自吸收不可忽略。
  6. 物理含义：磷光强度正比于激发态浓度；衰减由激发态退激与发射光子的重吸收共同决定，γ 量化了后者对表观寿命的调制。
  7. 对 ML 传感的启示：从衰减曲线提取陷阱寿命/脱陷速率前必须扣除自吸收效应，否则会把光学损耗误判为陷阱动力学，影响应力-发光标定。
  8. 加载方式为静水载荷（hydrostatic load），可在不引入摩擦/断裂发光干扰的情况下单独考察压力对 ML 磷光动力学的影响，是 ML 机理研究中相对干净的力学加载构型。
  9. 本文为会议短文（OS0512，4 页量级），数据与模型较初步；具体 ML 材料的化学成分、[[../concepts/trap-depth|陷阱深度]]、γ 随压力的定量关系等在可读笔记中未给出，第二步 wiki 写作时不应臆造。
  10. 对 project-3 NN 工作的可复用要素：(I(t), t) 衰减曲线数据形态、20 µs/10 Hz 激发协议、单指数+吸收修正的参数化形式（I0, τ, B, γ, α, β）可作为 ML 信号表征与物理约束特征的基线。
