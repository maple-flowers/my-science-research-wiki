---
citekey: Zhang2019c
title: "Atomic simulations of packing patterns and thermal behavior in Ti clusters"
title_zh: "Ti团簇堆积模式和热行为的原子模拟"
authors: [Lin Zhang]
year: 2019
journal: "Progress in Natural Science：Materials International"
doi: "10.1016/j.pnsc.2019.04.006"
url: "https://doi.org/10.1016/j.pnsc.2019.04.006"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/Zhang2019c]]
projects: []
concepts: [embedded-atom-method, molecular-dynamics, pair-analysis, icosahedral-packing, dulong-petit-law, cluster-size-effect, surface-premelting, sommerfeld-potential, additive-manufacturing]
entities: [Ti]
methods: [eam, md, pair-analysis]
materials:
  - Ti
figures: [crystal-structures, mathematical-models]
领域基础知识:: >-
  钛及钛合金具有低密度、高比强度、优异的生物相容性和耐腐蚀性，广泛应用于增材制造和生物医用植入物领域。在纳米尺度下，材料的性能会显著偏离宏观块体材料。嵌入原子势（EAM）是描述金属体系原子间相互作用的有效多体势函数。杜隆-珀蒂定律是经典热力学中描述晶体比热容的定律，其极限值为每个原子3k_B (k_B为玻尔兹曼常数)。
研究背景:: >-
  增材制造技术中常使用纳米级金属粉末，其熔化和凝固行为与块体材料不同。实验上已观测到钛团簇在不同尺寸范围（如15-55原子，80-150原子等）的吸收光谱会向块体钛的特征演变，暗示可能存在结构转变，但微观机制不清，尤其是温度的影响未被充分理解。
作者的问题意识:: >-
  钛团簇的堆积模式如何随团簇尺寸（从数十到数千个原子）和温度变化？表面原子在结构转变中扮演何种角色？经典热力学理论（如杜隆-珀蒂定律）对这类微小体系的适用边界在哪里？
主要研究对象:: >-
  包含19至2601个原子的一系列钛纳米团簇（Ti19, Ti57, ..., Ti2601），直径范围从0.67 nm至4.40 nm。
主要研究方法:: >-
  采用嵌入原子势（EAM）的分子动力学（MD）模拟。引入温度依赖的索末菲势，将描述低温HCP相和高温BCC相的两种势能线性组合，以模拟宽温区内的结构演化。使用对分析技术（PA）鉴定局部原子堆积模式，并通过计算惯性矩、形状因子和比热容来分析团簇的宏观性质。
研究意义:: >-
  从原子尺度揭示了钛纳米团簇结构转变的微观机制，特别是定量阐明了表面原子的主导作用。为理解纳米尺度相变行为提供了清晰的物理图像，并为增材制造等涉及纳米颗粒的工艺优化提供了基础理论数据。
研究结论:: >-
  1. 团簇的堆积模式转变由表面原子运动驱动，且强烈依赖于尺寸和温度。2. 小尺寸团簇（如几何壳层闭合）倾向于形成二十面体结构；大尺寸团簇在较宽温区内保持HCP结构。3. 升温过程中会出现HCP、BCC和二十面体结构共存；大团簇的无序化从表面开始并向内部扩展。4. 杜隆-珀蒂定律对钛团簇的适用临界尺寸约为3.0 nm。
对领域的贡献:: >-
  提供了钛团簇从原子到纳米尺度结构演化的系统性微观图像，揭示了表面原子在相变中的“触发器”作用。成功应用了温度依赖的EAM势，为模拟复杂相变纳米体系提供了方法学参考。定量界定了经典热力学理论的适用边界。
未来研究方向提及:: >-
  论文未明确提及具体未来方向，但为后续研究提供了基础，暗示可向更复杂体系拓展。
未来研究方向思考:: >-
  1. 研究合金化（如Ti-6Al-4V）对团簇结构和相变路径的影响。2. 模拟非平衡条件下（如快速升降温）的动力学过程，与准静态模拟结果进行对比。3. 引入基底或气体环境，研究其对团簇结构演化的约束效应。4. 将MD模拟获得的热力学参数应用于更高尺度的（如相场）模型，以桥接微观与宏观。
tags:
  - paper
  - type/experiment
  - year/2019
  - project/project-1
  - relevance/project-1/medium
  - project/project-2
  - relevance/project-2/medium
  - project/project-3
  - relevance/project-3/medium
  - project/project-4
  - relevance/project-4/medium
  - project/project-5
  - relevance/project-5/medium
  - project/project-6
  - relevance/project-6/medium
  - project/project-7
  - relevance/project-7/medium
  - method/eam
  - method/md
  - method/stm-mbe
  - method/xanes
  - topic/charge-density-wave
  - topic/ferroelectricity
  - topic/humidity-sensing
  - topic/molecular-crystal
  - topic/multiferroics
  - topic/optical-spectra
  - topic/phase-transition
  - topic/two-photon-fluorescence
---
---

## Zhang2019c — Ti团簇堆积模式和热行为的原子模拟

## 📄 元数据
Lin Zhang，2019，*Progress in Natural Science: Materials International* 29(2): 237–243，DOI [10.1016/j.pnsc.2019.04.006](https://doi.org/10.1016/j.pnsc.2019.04.006)（东北大学材料各向异性与织构教育部重点实验室；国家重点研发计划 2016YFB0701304、NSFC 51671051 资助）
## 💡 一句话
用温度依赖的 EAM 势对 19–2601 个原子的 Ti 团簇做分子动力学模拟，揭示表面原子主导的尺寸/温度依赖堆积模式转变（小团簇倾向二十面体、大团簇保持 HCP、高温下 HCP/BCC/Ih 共存），并把杜隆-珀蒂定律适用的临界直径定在约 3.0 nm。

## 🔗 Wiki 双链
  - 概念：[[../concepts/additive-manufacturing|增材制造]]、[[../concepts/cluster-size-effect|团簇尺寸效应]]、[[../concepts/dulong-petit-law|杜隆-珀蒂定律]]、[[../concepts/embedded-atom-method|嵌入原子法]]、[[../concepts/icosahedral-packing|二十面体堆积]]、[[../concepts/molecular-dynamics|分子动力学]]、[[../concepts/pair-analysis|对分析]]、[[../concepts/sommerfeld-potential|索末菲势]]、[[../concepts/surface-premelting|表面预熔]]
  - 实体：[[../entities/Ti|金属钛]]
  - 图表 [[../figures/crystal-structures]]（HCP/BCC/二十面体堆积模式与对分析指纹）
  - 图表 [[../figures/mathematical-models]]（EAM 总能量公式、Sommerfeld 插值势、惯性矩/形状因子、杜隆-珀蒂热容斜率）
  - 年度 [[../write/2019]]
  - 相关论文 [[../../raw/note/Zhang2019c]]
  - （主题契合 [[../topics/Z01-材料模拟计算设计]]，关键词即 "Computational materials design"，但该条目不在本格式规定的双链类别内，特此备注）

## 📊 关键图表
笔记未附图片（raw/figures/Zhang2019c/ 仅有 manifest.json，figures 列表为空）。论文原图为 Fig.1 势能-时间步弛豫、Fig.2 五类键对示意、Fig.3 表面/体积比-直径、Fig.4 势能与形状因子-温度、Fig.5 键对分数-温度、Fig.6 堆积快照、Fig.7 热容斜率-直径。

## 🔬 项目连接
无直接项目连接（project-1 双光子 / project-2 Mn多铁 / project-3 机械发光NN / project-4 TTF分子计算 / project-5 SnTe铁电模拟 / project-6 湿度传感器 / project-7 CDW 均不直接对应；本文为 Ti 金属团簇的经典 MD/EAM 模拟，面向增材制造）。

## 🔗 项目双链
- 项目 [[../projects/project-1-two-photon|项目一：双光固化和双光发光]]
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]
- 项目 [[../projects/project-3-mechanoluminescence-nn|项目三：应力发光神经网络]]
- 项目 [[../projects/project-4-ttf-molecular-calc|项目四：lsl老师的ttf分子计算]]
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]
- 项目 [[../projects/project-6-humidity-sensor|项目六：小花闻的电压湿度传感器]]
- 项目 [[../projects/project-7-cdw-charge-density-wave|项目七：CDW电荷密度波]]

## 📝 组织与用词
论文遵循"问题→模型→观测→机制→普适化"的计算材料学范式。引言由钛合金植入物与增材制造纳米粉末的应用背景切入，引用同步辐射 XAS 在 15–1000 原子自由 Ti 团簇上观测到的尺寸依赖光谱作为待解释现象；方法节给出 EAM 总能量公式、温度依赖 Sommerfeld 势（双曲正切插值）、NVT 升温协议、惯性矩与形状因子、对分析技术；结果节按"表面比定量化（图3）→ 能量/形状演化（图4）→ 键对指纹（图5）→ 堆积快照（图6）→ 热容与经典极限（图7）"层层递进；结论收束为四条。贯穿主线是"表面原子低配位→低激发能→结构重排触发器"。可复用术语：
  - 嵌入原子法 [[../concepts/embedded-atom-method|嵌入原子法]] / Embedded Atom Method (EAM)
  - 分子动力学 [[../concepts/molecular-dynamics|分子动力学]] / Molecular Dynamics (MD)
  - 堆积模式 / Packing patterns
  - 二十面体（几何壳层闭合）/ Icosahedron (Ih, geometric shell closure)
  - 对分析技术 / Pair Analysis (PA)
  - 索末菲势 [[../concepts/sommerfeld-potential|索末菲势]] / Sommerfeld potential
  - 形状因子 / Shape factor (F_shape = I1/I3)
  - 杜隆-珀蒂定律 [[../concepts/dulong-petit-law|杜隆-珀蒂定律]] / Dulong–Petit law
  - 表面/体积比 / Surface-to-volume ratio
  - 临界尺寸 / Critical size

## ✏️ 可写入 Wiki 的要点
  1. **EAM 势与温度依赖 Sommerfeld 插值**：总能量 E_tot = Σ_{i<j} φ(r_ij) + Σ_i F(ρ_i)，ρ_i = Σ_j ∅(r_ij)。用 g(T)=tanh[(T−T0)/Tm]（T0=600 K，Tm=100 K）把描述 BCC 的 Ti1 势与描述 HCP 的 Ti2 势线性组合：φ_Som={[1+g(T)]φ_Ti1+[1−g(T)]φ_Ti2}/2，嵌入能同理。该插值在 450–700 K 人为造成所有团簇势能突降，不代表真实相变，引用图4时需注明。
  2. **模拟协议**：29 个团簇 Ti19…Ti2601（直径 0.67–4.40 nm），从块体 HCP 晶体中心截取球形碎片；NVT 系综，50 K 起步以 50 K 递增至 1550 K，每温度 1×10⁶ 步、取末 1×10⁵ 步平均，时间步 1.6 fs；模拟盒 17.8×25.7×24.2 nm 以保证团簇孤立。
  3. **表面原子比例定量化**：β_surface = N_surface/N，其中表面原子定义为配位数 <12（HCP/[[../concepts/icosahedral-packing|二十面体]]完整配位为 12）。直径 <2.8 nm（<约 700 原子）的团簇为"表面主导"，Ti19 几乎 100% 原子在表面；β 随直径振荡下降并趋近约 0.3，振荡低谷对应[[../concepts/geometric-shell-closure|几何壳层闭合]]的稳定"幻数"团簇。
  4. **[[../concepts/common-neighbor-analysis|对分析]]指纹**：1421 与 1422 等量 = HCP；仅 1421 = FCC；1551（五重对称、5 个共同近邻）= 二十面体；1441 与 1661 = BCC。在第一近邻截断内统计，可定量追踪固/液/非晶中局部结构比例。
  5. **尺寸依赖的结构图谱**：小团簇（Ti19、Ti57）低温弛豫即离开 HCP，>650 K 形成稳定 Ih；Ti135 在 50–100 K 保持 HCP，>300 K 转 Ih 并在 450–950 K 稳定，>1300 K 大部分原子转为 BCC；Ti389/Ti727/Ti1099 在宽温区保持 HCP 主体，升温时表面先出现 BCC 键对形成 HCP-core/BCC-shell 共存，Ti389 还短暂出现 Ih 后消失。
  6. **形状因子**：F_shape = I1/I3，I1、I3 为惯性矩张量对角化后的最小/最大主轴值，F_shape=1 为完美球。Ti19 在 >600 K 急剧拉长为棒状（三个相连小二十面体）；Ti57/Ti135/Ti389 高温亦伸长；Ti1099 熔化前后始终近球形。
  7. **熔化与[[../concepts/surface-premelting|表面预熔]]**：势能陡升标志熔化，Ti389 熔点 >1450 K，Ti727 >1450 K，Ti1099 >1500 K，熔点随尺寸增大而升高；无序堆积先在表面成核再迅速席卷整个大团簇，类似块体 Ti 熔化。
  8. **杜隆-珀蒂临界尺寸**：高温区（800–1350 K，熔化前）势能对 ΔU/ΔT 的斜率，直径 >2.8 nm（约 3.0 nm）的团簇趋近 1.5（NVT 下动能贡献固定 1.5，合计 3.0=3kB/原子），即开始服从经典定律；更小团簇斜率偏低，因为表面低配位原子运动所需能量低于内部原子，热容偏离经典极限。这为[[../concepts/additive-manufacturing|增材制造]]中对 >3 nm 钛颗粒沿用宏观热物理参数提供了定量依据。
  9. **表面原子作为"触发器"的统一机制**：低配位 → 低激发能垒 → 即使低温也易迁移重排；小团簇中表面原子的集体重排可驱动整体[[../concepts/structural-phase-transition|结构相变]]，大团簇中表面重排（BCC 层、预熔）先于核心，是[[../concepts/critical-thickness-ferroelectric|尺寸效应]]与温度效应的共同微观根源。
  10. **实验背景与意义**：同步辐射 XAS 已在 15–55、80–150、300–500、>600 原子四档自由 Ti 团簇上观察到吸收谱从类原子多峰结构向块体 Ti 双峰特征演化，本文用堆积模式转变给出了微观解释；并为增材制造激光熔化纳米粉末的熔池热力学模拟提供临界尺寸与熔点尺寸依赖数据。
