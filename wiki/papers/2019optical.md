---
citekey: 2019optical
title: Optical Fiber Polymer Sensor System with TiO2-SiO2 Cladding for Measuring Humidity
authors:
  - Febrielviyanti
  - Harmadi
  - Dahyunir Dahlan
  - Yetria Rilda
  - Helmi Septaria Herlin
year: 2019
journal: KnE Engineering
doi: 10.18502/keg.v1i2.4437
url: https://doi.org/10.18502/keg.v1i2.4437
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/2019optical]]
projects: [project-6]
concepts:
  - evanescent-wave
  - optical-fiber-sensor
  - humidity-sensing
  - intensity-modulation
  - refractive-index-sensing
  - dip-coating
entities:
  - TiO2
  - SiO2
  - TiO2-SiO2
  - polymer-optical-fiber
  - photodiode
  - laser-diode
methods:
  - solid-state-synthesis
  - dip-coating
  - evanescent-wave-sensing
  - intensity-modulation
  - photodiode-detection
  - adc-calibration
  - linear-regression
  - hysteresis-measurement
materials:
  - TiO2
  - SiO2
  - TiO2-SiO2-composite
  - polymer-optical-fiber
  - PEG-6000
figures: [electronic-devices-memory-transistors, electronic-devices-sensors, experimental-setups, mathematical-models-formulas]
领域基础知识:: 光纤传感器利用光在光纤中传输的特性来感知外界物理量，具有抗电磁干扰、耐腐蚀等优点。其核心传感原理常基于倏逝波，即光场在纤芯-包层界面渗透到外部环境的部分，其特性会随外部介质折射率变化而改变。塑料光纤因成本低、柔韧性好，在传感领域备受关注。
研究背景:: 传统湿度传感器存在易受电磁干扰、稳定性不足等局限。利用光纤技术，特别是通过替换光纤包层为亲水材料来开发新型湿度传感器，已成为研究热点。已有研究尝试了明胶、TiO2、PAH/SiO2等材料，但性能仍有提升空间，需要探索新的敏感材料体系和优化结构。
作者的问题意识:: 如何开发一种基于新型亲水材料（TiO2-SiO2复合材料）的塑料光纤湿度传感器，并通过系统研究其结构参数（包层剥离长度）和构建完整的测量系统，来验证其可行性和性能？
主要研究对象:: 基于TiO2-SiO2替代包层的塑料光纤倏逝波湿度传感器。具体包括：1) TiO2-SiO2纳米复合涂层材料；2) 不同包层剥离长度（1cm, 2cm, 3cm）的传感器探头；3) 一套由激光光源、光电探测器、Arduino UNO微控制器组成的完整湿度测量系统。
主要研究方法:: 采用实验研究法。1) 通过固相合成法制备TiO2-SiO2复合材料，并利用浸渍提拉法涂覆在剥离包层后的塑料光纤上；2) 通过控制变量法，对比分析1cm、2cm、3cm三种剥离长度下传感器的电压-湿度响应特性，筛选最优结构；3) 基于最优传感器，建立ADC值与湿度的校准方程，并嵌入Arduino系统；4) 通过与标准湿度计对比，评估最终系统的测量误差。
研究意义:: 实践上，为开发低成本、抗电磁干扰的塑料光纤湿度传感器提供了一种新的技术方案和材料选择，有望应用于特定工业或环境监测场景。学术上，验证了TiO2-SiO2复合材料在光纤湿度传感领域的应用潜力，并提供了一套从材料制备、结构优化到系统集成的完整研究范式，可为后续相关研究提供参考。
研究结论:: 1) 基于TiO2-SiO2包层的塑料光纤传感器能有效响应空气湿度；2) 最优的包层剥离长度为2cm，此时传感器呈现出最佳的线性度，其电压-湿度关系的判定系数R2=0.982，灵敏度为0.0376 V/%；3) 基于此传感器构建的测量系统，其ADC-湿度校准方程的R2=0.984，线性度优良；4) 与标准湿度计对比，该系统在88.8%至97.42% RH范围内的平均测量误差为2.78%。
对领域的贡献:: 1) 材料体系拓展：首次报道了将TiO2-SiO2纳米复合材料用于塑料光纤湿度传感，扩展了光纤湿敏材料的种类；2) 结构优化：清晰论证了剥离长度对传感器性能的影响，并给出了最优值；3) 系统集成示范：完整展示了从实验室传感元件到一个基于微控制器的简易测量系统的构建过程，为后续的原型开发提供了清晰路线图。
未来研究方向提及:: 论文指出，传感器性能尚不稳定，主要源于手动对准和光纤弯曲等系统误差。未来需要解决传感器的封装和标准化制造问题，以提升其稳定性和可靠性，使其成为一个能实际应用的测量仪器。
未来研究方向思考:: 1) 材料机理深究：需对TiO2-SiO2薄膜进行微观表征（如SEM、XRD），建立其微观结构与湿敏性能的构效关系，并明确传感是折射率调制还是消逝场吸收主导；2) 性能全面评估：需测试响应时间、恢复时间、长期漂移、温度交叉灵敏度及对其他气体的选择性；3) 封装与稳定性：设计精密夹具和封装工艺，消除手动操作误差，并研究涂层在长期使用中的老化问题；4) 传感机制升级：探索用波长调制型光纤结构（如FBG）替代简单的强度调制，以消除光源波动影响，获得更高精度和稳定性。
tags:
  - paper
  - type/experiment
  - year/2019
  - project/project-6
  - relevance/project-6/strong
  - concept/evanescent-wave
  - concept/optical-fiber-sensor
  - concept/humidity-sensing
  - concept/intensity-modulation
  - concept/refractive-index-sensing
  - concept/dip-coating
  - concept/adsorption
  - entity/TiO2
  - entity/SiO2
  - entity/TiO2-SiO2
  - entity/polymer-optical-fiber
  - entity/Arduino-Uno
  - entity/photodiode
  - entity/laser-diode
  - method/solid-state-synthesis
  - method/dip-coating
  - method/evanescent-wave-sensing
  - method/intensity-modulation
  - method/photodiode-detection
  - method/adc-calibration
  - method/linear-regression
  - method/hysteresis-measurement
  - material/TiO2
  - material/SiO2
  - material/TiO2-SiO2-composite
  - material/polymer-optical-fiber
  - material/PEG-6000
  - topic/humidity-sensing
  - topic/fiber-optic-sensor
  - topic/optical-sensing
---

## 2019optical — TiO2-SiO2包层聚合物光纤湿度传感器系统

## 📄 元数据
Febrielviyanti, Harmadi, Dahyunir Dahlan, Yetria Rilda, Helmi Septaria Herlin，2019，KnE Engineering（ICBSA 2018 会议论文），DOI: 10.18502/keg.v1i2.4437
## 💡 一句话
将聚合物光纤（POF, Autonics FD-620-10）中段包层剥离并浸渍涂覆 TiO2-SiO2 纳米复合亲水层，利用倏逝场强度调制实现相对湿度测量，确定最佳剥离长度 2 cm（R²=0.982，灵敏度 0.0376 V/%），并集成到基于 Arduino Uno 的测量系统中（平均误差 2.78%）。

## 🔗 Wiki 双链
  - 概念 [[../concepts/evanescent-wave|倏逝波]]、[[../concepts/optical-fiber-sensor|光纤传感器]]、[[../concepts/humidity-sensing|湿度传感]]、[[../concepts/intensity-modulation|光强调制]]、[[../concepts/dip-coating|浸渍提拉法]]
  - 实体 [[../entities/TiO2-SiO2|TiO2-SiO2纳米复合材料]]、[[../entities/polymer-optical-fiber|聚合物光纤（POF）]]
  - 图表 [[../figures/experimental-setups]]（图1-3 测量/系统框图）、[[../figures/mathematical-models]]（倏逝场公式 Ez=E0·exp(−z/dp)、穿透深度 dp、误差/精度公式）
  - 年度 [[../write/2015-2019|2019]]
  - 项目 [[../projects/project-6-humidity-sensor]]
  - 概念 [[../concepts/refractive-index-sensing]]
  - 实体 [[../entities/photodiode]]、[[../entities/laser-diode]]、[[../entities/TiO2]]、[[../entities/SiO2]]
  - 相关论文 **2019optical**

## 📊 关键图表
  - ![图1 测量系统框图：输入-过程-输出](../../raw/figures/2019optical/fig_1_BJNL3G4F.png) -> [[../figures/experimental-setups|实验装置与测量系统]]
  - **图示描述**：通用测量系统的三段式流程框图，从左到右依次为"输入（Input）→ 过程（Process）→ 输出（Output）"，对应传感器元件、信号处理单元与显示终端。
  - **关键特征**：输入即光纤传感探头，将湿度这一物理量转换为光强变化；过程为 Arduino Uno 微控制器及其内置 ADC，完成模拟电压到数字量的换算；输出为 LCD 或 PC 上显示的相对湿度数值。
  - **结论/意义**：为全文提供测量系统的概念框架，是后续图3具体工程实现的抽象模板。
  - ![图2 光纤传感器系统示意图（光源-调制区-探测器）](../../raw/figures/2019optical/fig_2_FULPP47Y.png) -> [[../figures/electronic-devices-sensors|传感器与探测器]]
  - **图示描述**：引自文献[13]的通用光纤传感系统示意图，展示激光二极管光源、光纤、调制区（传感探头）、光电探测器与显示输出之间的物理连接关系。
  - **关键特征**：光从光源进入光纤，在调制区被外界湿度调制后到达光电二极管转换为电信号；调制区即包层被 TiO2-SiO2 替代的光纤段，是传感器的核心；图中清晰区分了内禀（intrinsic）与外禀（extrinsic）传感路径，本研究采用消逝场（evanescent）型内禀传感。
  - **结论/意义**：阐明了强度调制型光纤传感器的物理架构，为理解"湿度→光强→电压"的信号链提供直观模型。
  - ![图3 湿度测量系统总体框图（激光源-TiO2-SiO2光纤-湿度腔-光电二极管-Arduino-LCD/PC）](../../raw/figures/2019optical/fig_3_KR9YLLPQ.png) -> [[../figures/experimental-setups|实验装置与测量系统]]
  - **图示描述**：本研究实际搭建的湿度测量系统总体框图，链路为"激光二极管光源 → TiO2-SiO2 替代包层的聚合物光纤（置于湿度腔内）→ 光电二极管探测器 → Arduino Uno → LCD/PC 显示"。
  - **关键特征**：光源为 638 nm 红色二极管激光器；光纤总长 21 cm（Autonics FD-620-10），中段包层被剥离并浸涂 TiO2-SiO2；传感段置于可控湿度腔中，水蒸气直接作用于涂层；光电二极管输出电压经 Arduino Uno（ATmega328，10 bit ADC，0–5 V 映射 0–1023）采样，并可通过以太网扩展板上传。
  - **结论/意义**：将图2的通用架构落地为完整的实验装置，体现"材料—结构—电路—软件"的系统集成思路。
  - ![图4 剥离长度1 cm时湿度-电压关系](../../raw/figures/2019optical/fig_4_BFV9Y8WP.png) -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]
  - **图示描述**：包层剥离长度为 1 cm 时，光电二极管输出电压（纵轴，V）随腔内相对湿度（横轴，% RH）变化的散点与线性拟合曲线，包含增湿与脱湿两组数据以观察迟滞。
  - **关键特征**：数据点相对分散，线性度在三种长度中最差；增湿与脱湿曲线存在明显不重合，迟滞较显著；原因在于传感区过短，光与湿敏涂层相互作用不足，信噪比偏低。
  - **结论/意义**：作为对照样本说明 1 cm 剥离长度不足以提供稳定可重复的湿度响应。
  - ![图5 剥离长度2 cm时湿度-电压关系（最优，R²=0.982，灵敏度0.0376 V/%）](../../raw/figures/2019optical/fig_5_5XEUBXZM.png) -> [[../figures/electronic-devices-sensors|传感器与探测器]]
  - **图示描述**：包层剥离长度为 2 cm、TiO2-SiO2 涂层配比 1:2 时，输出电压（V）对相对湿度（% RH）的散点图与线性拟合，同样叠加增湿/脱湿两组数据。
  - **关键特征**：数据点紧密围绕拟合直线，判定系数 R²=0.982，为三种长度中最高；拟合斜率即灵敏度 0.0376 V/%（约 37.6 mV/%）；增湿与脱湿曲线吻合最好，迟滞最小；电压随湿度升高而上升。
  - **结论/意义**：确立 2 cm 为最佳包层剥离长度，是全文筛选最优结构参数的核心证据，也是后续 ADC 校准（图7）所选用的传感器。
  - ![图6 剥离长度3 cm时湿度-电压关系](../../raw/figures/2019optical/fig_6_GZ2SLHRB.png) -> [[../figures/electronic-devices-sensors|传感器与探测器]]
  - **图示描述**：包层剥离长度为 3 cm 时输出电压（V）随相对湿度（% RH）变化的散点与拟合曲线，含增湿/脱湿两组数据。
  - **关键特征**：线性度较 2 cm 差，迟滞也更大；更长的裸露段引入额外的光传输损耗以及水分子吸/脱附动力学的非均匀性，导致响应稳定性下降；体现"剥离越长越灵敏"的直觉并不成立，存在最优窗口。
  - **结论/意义**：与图4、图5共同构成剥离长度参数扫描，证明 2 cm 是灵敏度与稳定性的平衡点。
  - ![图7 2 cm剥离长度下湿度-ADC值校准曲线 y=0.131x−22.58，R²=0.984](../../raw/figures/2019optical/fig_7_J268S4RT.png) -> [[../figures/experimental-setups|实验装置与测量系统]]
  - **图示描述**：在最优 2 cm 剥离长度下，Arduino ADC 读数（横轴，无量纲，0–1023）与标准湿度计测得的相对湿度（纵轴，% RH）之间的散点及线性拟合。
  - **关键特征**：拟合得到传递函数 y=0.131x−22.58，其中 x 为 ADC 值、y 为湿度（% RH）；斜率 0.131 为 ADC 转换系数，截距 −22.58 为系统偏移；判定系数 R²=0.984，线性度优良；该方程被写入 Arduino Uno 程序，实现实时湿度换算。
  - **结论/意义**：标志传感器从"性能表征"走向"实际测量"，是系统集成与标定的关键一步。
  - ![表1 自制仪器与标准湿度计5点对比，平均误差2.78%](../../raw/figures/2019optical/tab_1_64NAU4YA.png) -> [[../figures/experimental-setups|实验装置与测量系统]]
  - **图示描述**：自制光纤湿度计与标准湿度计在 5 个测试点上的读数对比表，三列分别为自制仪器读数（%）、标准湿度计读数（%）和单点误差（%）。
  - **关键特征**：自制仪器读数范围 88.8%–97.42% RH，标准湿度计对应 90.73%–99.7% RH；单点误差介于 1.7%–4.1% 之间，平均误差 2.78%；误差主要来自光纤与光电二极管的手动对准重复性差，以及光纤微弯/宏弯引入的光功率波动。
  - **结论/意义**：定量验证了整套系统的测量精度，证明方案可行但鲁棒性不足，作者据此指出传感器尚不能直接作为成熟测量仪器，需标准化封装。
  - ![公式2 测量精度 An=1−[(Yn−Yo)/Yn]×100%](../../raw/figures/2019optical/eq_2_A2EEKRHU.png)
  - **图示描述**：测量精度计算公式 An=1−[(Yn−Yo)/Yn]×100%，其中 Yn 为标准湿度计真值、Yo 为自制仪器读数。
  - **关键特征**：与误差公式 en=|(Yn−Yo)/Yn|×100%（原文公式1，未单列图）互补，用于把表1中 5 个测点的偏差换算为精度百分比；是评估系统相对于标准仪器偏离程度的统计工具。
  - **结论/意义**：为"平均误差 2.78%"这一结论提供计算依据。
  - ![公式3 倏逝场 Ez=E0·exp(−z/dp)](../../raw/figures/2019optical/eq_3_NILGGZ7L.png) -> [[../figures/mathematical-models-formulas|光学、输运与其他解析公式]]
  - **图示描述**：倏逝波电场沿垂直纤芯—包层界面方向的衰减公式 Ez=E0·exp(−z/dp)，z 为距界面距离，E0 为界面处初始场强，dp 为穿透深度。
  - **关键特征**：电场在包层中按指数规律衰减，而非突然截止；dp 越大，倏逝场延伸到包层越远，与外界环境（吸湿后的 TiO2-SiO2 涂层）相互作用越强，导波光损耗越大；湿度通过改变涂层折射率来调制 dp，从而调制到达探测器的光强。
  - **结论/意义**：是整个传感器"湿度→折射率→穿透深度→光强"机理链条的数学基础。
  - ![公式4 穿透深度 dp=λ/(2nπ√(sin²θ−n²))](../../raw/figures/2019optical/eq_4_4BLSJGW9.png) -> [[../figures/mathematical-models-formulas|光学、输运与其他解析公式]]
  - **图示描述**：倏逝波穿透深度公式 dp=λ/(2nπ√(sin²θ−n²))，λ 为光源波长（本研究 638 nm），θ 为光线在纤芯—包层界面的入射角，n 为包层与纤芯折射率之比 n_clad/n_core。
  - **关键特征**：dp 与波长 λ 成正比，与折射率比 n 及入射角 θ 成非线性关系；TiO2-SiO2 涂层吸水后 n_clad 发生变化，直接改变 dp，进而改变导波光强；原文对 n_clad 升降方向与 dp、光强之间因果的论述存在表述上的不自洽，需结合图4–6的实测趋势谨慎解读。
  - **结论/意义**：把材料的光学参数（折射率）与可测的宏观信号（光强/电压）定量联系起来，是结构优化与材料改进的理论依据。

## 🔬 项目连接
  - **project-6（小花闻的电压湿度传感器，strong）**：本文是直接的光纤湿度传感文献，与项目已收录的 xuOpticalFiberHumidity2004（倏逝波散射）、Owji20212d（二维材料涂层光纤）、Lv2023humidity（FBG）形成同代际/同方法谱系。具体参考价值：(1) 给出了一套完整的"亲水涂层替代包层 → 剥离长度优化 → 电压/ADC 校准 → 标准湿度计比对"的实验流程与误差分析框架，可直接对照项目六的器件测试流程；(2) 提供了 TiO2-SiO2 这一混合氧化物涂层的制备参数（1 g TiO2 + 1 g SiO2 + 2 g PEG6000，500 ℃ 煅烧 2-4 h，0.3 g 成品 + 30 mL 水，柠檬酸交联 3 h，浸涂 5 min/50 ℃ 干燥 15 min），可作为涂层工艺对比基准；(3) 给出了高湿段（88.8%-97.42% RH）的灵敏度与线性度数据，与项目关注的 G/GO 高湿段行为（Owji2021）可相互印证；(4) 其手动对准与微弯/宏弯损耗导致的系统误差分析，提示项目在数据处理中需关注耦合稳定性。局限：仅测高湿窄区间、未做 SEM/XRD 微观表征、未报告响应/恢复时间，这些恰是项目六可以深化的方向。
  - 其他项目：无直接连接。project-1 为双光子吸收/发光，与本文单光子 638 nm 红光强度调制机制无关。

## 🔗 项目双链
- 项目 [[../projects/project-6-humidity-sensor|项目六：小花闻的电压湿度传感器]]

## 📝 组织与用词
文章按"引言（领域背景+前人工作：明胶/TiO2/PAH-SiO2/Al-ZnO）→ 材料与方法（材料/涂层制备/光纤涂覆/测量系统/光纤传感系统/湿度系统设计共6小节）→ 结果与讨论（电压-湿度表征/ADC-湿度校准/湿度测量测试）→ 结论"的标准实验论文结构组织。论证主线为"原理（倏逝波穿透深度受包层折射率调制）→ 制备（固相合成+浸涂）→ 参数扫描（1/2/3 cm 剥离长度）→ 系统集成（Arduino 校准）→ 精度验证（与标准湿度计比对）"。值得复用的术语：
  - 倏逝波 / 消逝场（[[../concepts/evanescent-wave|evanescent wave]] / evanescent field）
  - 穿透深度（[[../concepts/penetration-depth|penetration depth]], dp）
  - 聚合物光纤（[[../entities/polymer-optical-fiber|polymer optical fiber]], POF）
  - 包层剥离（cladding stripping / exfoliation）
  - 浸渍提拉法（[[../concepts/dip-coating|dip coating]]）
  - 强度调制（[[../concepts/intensity-modulation|intensity modulation]]）
  - 传递函数 / 校准方程（transfer function / calibration equation）
  - 判定系数（coefficient of determination, R²）
  - 迟滞（[[../concepts/hysteresis|hysteresis]]）
  - 相对湿度（[[../concepts/relative-humidity|relative humidity]], RH）

## ✏️ 可写入 Wiki 的要点
  1. 传感机制：剥除 POF 包层后涂覆亲水 TiO2-SiO2 层，环境湿度变化改变涂层[[../concepts/refractive-index|折射率]] n_clad，由 dp=λ/(2nπ√(sin²θ−n²))（n=n_clad/n_core）调制[[../concepts/evanescent-wave|倏逝波]][[../concepts/penetration-depth|穿透深度]]，进而改变到达光电二极管的光强（原文公式3、4）。
  2. 光源为 638 nm 红色二极管激光器，探测器为光电二极管；光纤总长 21 cm（Autonics FD-620-10），剥离长度变量 1/2/3 cm。
  3. TiO2-SiO2 制备：1 g TiO2 + 1 g SiO2 + 2 g PEG6000 混合研磨，500 ℃ 加热 2-4 h 形成锐钛矿相（anatase，400-500 ℃ 合成；金红石 500-600 ℃；板钛矿 700 ℃）；取 0.3 g 成品 + 30 mL 超纯水搅拌 1 h、超声 30 min 制涂覆液。
  4. 涂覆工艺：光纤先在柠檬酸中交联 3 h 作粘结剂，再浸涂 5 min，50 ℃ 干燥 15 min。
  5. 最佳剥离长度为 2 cm（TiO2:SiO2=1:2 比例表述见正文结果段），电压-湿度 R²=0.982，灵敏度 0.0376 V/%；1 cm 线性差，3 cm 引入更多损耗与不稳定性。
  6. ADC 校准（2 cm）：y=0.131x−22.58，x 为光电二极管输出经 ADC 转换后的数值，y 为 RH(%)，R²=0.984；该方程写入 Arduino Uno（ATmega328，10 bit ADC，0-5 V 映射 0-1023）。
  7. 与标准湿度计 5 点比对（88.8%-97.42% RH 设计值 vs 90.73%-99.7% RH 标准值），单点误差 1.7%-4.1%，平均误差 2.78%。
  8. 误差来源：光电二极管与光纤末端手动对准导致重复性差；光纤微弯/宏弯影响光传播；作者明确指出该传感器尚不能直接用作测量仪器，需标准化封装。
  9. 文献谱系定位：Zhang 2008（明胶，1.8 cm，42%-99% RH，最佳 60%-72%）、Aneesh 2009（纯 TiO2，石英光纤，3.5%-95.7% RH）、David/Gomez 2017（PAH/SiO2，POF，10%-75% RH 灵敏度 −3.87×10⁻³，90%-97% RH 为 −9.61×10⁻³）、Harith Z 2017（Al 掺杂 ZnO 锥形 POF，0.0386 mV/%）；本文 0.0376 V/% 即 37.6 mV/%，量级高于 Harith 的 mV/% 数值，但因系统灵敏度含光源/探测器增益，跨工作横比需谨慎。
  10. 机理疑点（批判）：原文正文称"湿度升高→光强变小→电压升高"存在逻辑不自洽（若光强变小，光电二极管电压通常下降），且未定量给出涂层折射率变化方向与幅度；真正机制可能涉及水分子在特定波长的[[../concepts/evanescent-field|倏逝场]]吸收，而非单纯折射率调制，提示 wiki 叙述中应区分"折射率调制"与"消逝场吸收"两种路径。
