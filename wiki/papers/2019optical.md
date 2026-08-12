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
projects:
  - project-6
concepts:
  - evanescent-wave
  - optical-fiber-sensor
  - humidity-sensing
  - intensity-modulation
  - refractive-index-sensing
  - dip-coating
  - adsorption
entities:
  - TiO2
  - SiO2
  - TiO2-SiO2
  - polymer-optical-fiber
  - Arduino-Uno
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
figures:
  - experimental-setups
  - mathematical-models
  - optical-spectra
  - calibration-curves
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
  - 图表 [[../figures/experimental-setups]]（图1-3 测量/系统框图）、[[../figures/mathematical-models]]（倏逝场公式 Ez=E0·exp(−z/dp)、穿透深度 dp、误差/精度公式）、[[../figures/optical-spectra]]（强度调制型光传感输出曲线）
  - 年度 [[../write/2019]]
  - 项目 [[../projects/project-6-humidity-sensor]]
  - 相关论文 **2019optical**

## 📊 关键图表
  - ![图1 测量系统框图：输入-过程-输出](../../raw/figures/2019optical/fig_1_BJNL3G4F.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - ![图2 光纤传感器系统示意图（光源-调制区-探测器）](../../raw/figures/2019optical/fig_2_FULPP47Y.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - ![图3 湿度测量系统总体框图（激光源-TiO2-SiO2光纤-湿度腔-光电二极管-Arduino-LCD/PC）](../../raw/figures/2019optical/fig_3_KR9YLLPQ.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - ![图4 剥离长度1 cm时湿度-电压关系](../../raw/figures/2019optical/fig_4_BFV9Y8WP.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - ![图5 剥离长度2 cm时湿度-电压关系（最优，R²=0.982，灵敏度0.0376 V/%）](../../raw/figures/2019optical/fig_5_5XEUBXZM.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - ![图6 剥离长度3 cm时湿度-电压关系](../../raw/figures/2019optical/fig_6_GZ2SLHRB.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - ![图7 2 cm剥离长度下湿度-ADC值校准曲线 y=0.131x−22.58，R²=0.984](../../raw/figures/2019optical/fig_7_J268S4RT.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - ![表1 自制仪器与标准湿度计5点对比，平均误差2.78%](../../raw/figures/2019optical/tab_1_64NAU4YA.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - ![公式2 测量精度 An=1−[(Yn−Yo)/Yn]×100%](../../raw/figures/2019optical/eq_2_A2EEKRHU.png)
  - ![公式3 倏逝场 Ez=E0·exp(−z/dp)](../../raw/figures/2019optical/eq_3_NILGGZ7L.png) -> [[../figures/mathematical-models|数学模型与物理公式]]
  - ![公式4 穿透深度 dp=λ/(2nπ√(sin²θ−n²))](../../raw/figures/2019optical/eq_4_4BLSJGW9.png) -> [[../figures/mathematical-models|数学模型与物理公式]]

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
