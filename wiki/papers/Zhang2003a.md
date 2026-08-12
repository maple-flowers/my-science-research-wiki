---
citekey: Zhang2003a
title: "A cellular automaton investigation of the transformation from austenite to ferrite during continuous cooling"
authors: [L. Zhang, C.B. Zhang, Y.M. Wang, S.Q. Wang, H.Q. Ye]
year: 2003
journal: "Acta Materialia"
doi: "10.1016/S1359-6454(03)00416-6"
url: "https://doi.org/10.1016/S1359-6454(03)00416-6"
paper_type: method
status: ingested
year_read: 2026
original_note:: [[../../raw/note/Zhang2003a]]
projects: []
concepts: [solid-state-phase-transformation, diffusion-controlled-growth, nucleation-and-growth, undercooling, solute-redistribution, soft-impingement, super-element-approximation, grain-boundary-nucleation, cementite-precipitation]
entities: [Acta-Materialia]
methods: [cellular-automaton, finite-volume-method, classical-nucleation-theory, probabilistic-modeling, diffusion-equation]
materials: [A36-low-carbon-steel, austenite, ferrite, cementite]
figures: [phase-diagram, cell-neighborhood-schematic, microstructure-evolution, kinetics-curves]
领域基础知识:: >-
  材料科学，固态相变，低碳钢物理冶金学，计算材料学，元胞自动机（Cellular Automaton, CA）模拟，扩散控制相变，形核与生长动力学。
研究背景:: >-
  低碳钢中奥氏体（γ）向铁素体（α）的转变对工业至关重要，但实时观测困难。现有模拟方法（如Kumar等人的CA模型）使用过多可调参数，难以清晰区分冷却条件的影响。需要一种物理基础更清晰、可调参数更少的模型来定量研究冷却条件对微观结构演化的影响及其背后的竞争机制。
作者的问题意识:: >-
  如何建立一个物理意义更明确、参数更少的二维元胞自动机模型，来定量揭示低碳钢连续冷却过程中，冷却条件如何通过影响形核与生长的动态竞争，最终决定铁素体微观结构（如晶粒尺寸、形核数量）的演化规律。
主要研究对象:: >-
  低碳钢（以A36钢为例）在连续冷却过程中的奥氏体（γ）到铁素体（α）的扩散型固态相变。
主要研究方法:: >-
  二维元胞自动机（CA）数值模拟。模型将多组分钢简化为超元素S-C合金，假设铁素体在奥氏体晶界形核，生长由碳扩散控制。通过将局部碳浓度变化耦合到概率性的形核和生长规则中，动态模拟微观结构演化。模拟结果与文献实验数据及显微照片进行定量和定性对比验证。
研究意义:: >-
  在方法论上，提供了一个物理基础坚实的模拟框架，可将溶质扩散、界面移动、形核生长等关键过程在介观尺度有效耦合。在理论上，定量阐明了从"冷却速率"到"最终晶粒尺寸"的完整因果链，深化了对相变过程中竞争机制的理解。在实践上，为通过控制冷却工艺来预测和优化钢材微观结构提供了有力的理论指导与计算工具。
研究结论:: >-
  1. 成功建立了二维CA模型，其模拟结果（如每个奥氏体晶粒内铁素体晶粒数M）与实验数据吻合良好，验证了模型的有效性。2. 冷却速率是控制微观结构的关键。高冷却速率导致大过冷度，从而产生高形核率，最终获得细小的铁素体晶粒，且相变完成时间更短。3. 相变过程的核心是形核与生长的竞争。高冷却速率下，早期阶段竞争更激烈，且形核占主导地位。形核过程主要在过冷度较小的早期阶段即已完成。4. 低冷却速率下，较少的晶核在充足的扩散时间内充分长大，导致最终晶粒尺寸更大。
对领域的贡献:: >-
  提出了一种将局部溶质浓度变化耦合到CA概率性规则中的新方法，减少了模型对经验参数的依赖，为模拟扩散控制型相变提供了更精确和物理上更透明的建模范例。定量揭示了连续冷却相变中形核-生长竞争机制，为该领域提供了重要的理论洞见。
未来研究方向提及:: >-
  论文未明确提及。
未来研究方向思考:: >-
  1. 将模型从二维扩展至三维，以更真实地反映晶粒空间拓扑结构。2. 引入更多合金元素的扩散及其对界面迁移的溶质拖曳效应，超越"超元素S"的简化。3. 将CA模型与宏观热力学/有限元模型耦合，实现从工艺参数到构件性能的跨尺度模拟。4. 将该模型框架扩展应用于其他扩散型相变，如珠光体或贝氏体转变。5. 探索更高效的数值算法，以提高模拟效率，处理更大尺度的模拟。
tags:
  - paper
  - type/method
  - year/2003
  - concept/solid-state-phase-transformation
  - concept/diffusion-controlled-growth
  - concept/nucleation-and-growth
  - concept/undercooling
  - concept/solute-redistribution
  - concept/soft-impingement
  - concept/super-element-approximation
  - concept/grain-boundary-nucleation
  - concept/cementite-precipitation
  - entity/Acta-Materialia
  - method/cellular-automaton
  - method/finite-volume-method
  - method/classical-nucleation-theory
  - method/probabilistic-modeling
  - method/diffusion-equation
  - material/A36-low-carbon-steel
  - material/austenite
  - material/ferrite
  - material/cementite
  - topic/phase-transformation
  - topic/computational-materials-science
  - topic/microstructure-evolution
  - topic/steel-metallurgy
---

## Zhang2003a — 连续冷却过程中奥氏体向铁素体转变的元胞自动机研究

## 📄 元数据
L. Zhang, C.B. Zhang, Y.M. Wang, S.Q. Wang, H.Q. Ye，2003，Acta Materialia 51(18): 5519–5527，DOI 10.1016/S1359-6454(03)00416-6（中科院金属所沈阳材料科学国家实验室 / 东北大学理学院）
## 💡 一句话
建立二维六边形元胞自动机模型，将局部碳浓度变化耦合到概率性形核/捕获规则中，定量揭示了低碳钢连续冷却时冷却速率通过形核-生长竞争决定铁素体晶粒尺寸与形貌的机制。
## 🔗 Wiki 双链
  - 年度 [[../write/2003]]
  - 相关论文 [[../../raw/note/Zhang2003a]]
  - 概念 [[../concepts/solid-state-phase-transformation|固态相变]]、[[../concepts/diffusion-controlled-growth|扩散控制生长]]、[[../concepts/nucleation-and-growth|形核与生长]]、[[../concepts/undercooling|过冷度]]、[[../concepts/solute-redistribution|溶质再分配]]、[[../concepts/soft-impingement|软碰撞]]、[[../concepts/super-element-approximation|超元素近似]]、[[../concepts/grain-boundary-nucleation|晶界形核]]、[[../concepts/cementite-precipitation|渗碳体析出]]
  - 图表 [[../figures/mathematical-models|数学模型与物理公式]]、[[../figures/heterostructures-stacking-mechanics-misc|力学性质、剥离能与杂项]]
## 🆕 新概念/实体建议
  - `solid-state-phase-transformation`（固态相变）：固态中母相到新相的转变，按扩散/位移分类，是本论文的物理背景
  - `diffusion-controlled-growth`（扩散控制生长）：界面推进速度由溶质长程扩散决定的生长模式，对应 Stefan 条件
  - `nucleation-and-growth`（形核与生长）：经典相变两阶段过程，二者竞争决定最终组织
  - `undercooling`（过冷度）：平衡温度 Ae3 与实际温度之差，是形核率与生长速度的驱动力
  - `solute-redistribution`（溶质再分配）：相变时新相将多余溶质排出至母相的过程，CA 中通过向邻居分配 c_precipitate 实现
  - `soft-impingement`（软碰撞）：相邻扩散场重叠导致生长减速，无需晶粒直接接触
  - `super-element-approximation`（超元素近似）：把 Fe-Mn-Si-Ni-Cu-Cr 等效为 S-C 伪二元的建模简化
  - `grain-boundary-nucleation`（晶界形核）：铁素体优先在奥氏体晶界形核的实验观察与模型假设
  - `cellular-automaton`（元胞自动机）：离散时空状态、局部规则驱动的介观模拟方法（可作为 methods/实体条目）
  - `A36-low-carbon-steel`（A36 低碳钢）：本工作的模拟对象，成分 C0.17 Mn0.74 Si0.012 Cu0.016 Ni0.01 Cr0.019（wt%）
  - `cementite`（渗碳体 Fe3C）：高冷速下碳富集形成并阻碍铁素体生长的第二相
## 📊 关键图表
  - ![Fe-C合金示意相图与Ae3线](../../raw/figures/Zhang2003a/fig_1_JCY8J4H6.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：简化的 Fe-C（超元素 S-C）二元相图局部，横轴为碳浓度 c，纵轴为温度 T，标出 γ 相区、α+γ 两相区及 γ 相线 Ae3。
  - **关键特征**：给定合金碳浓度 c 时，Ae3 线上的对应温度即为该成分下奥氏体开始向铁素体转变的平衡温度；过冷度 ΔT = Ae3 − T 即以此为基准，是后续形核率与生长速度公式的热力学起点。
  - **结论/意义**：为整个 CA 模型提供相变的热力学判据，定义了"何时开始过冷、形核驱动力有多大"。

  - ![六边形CA网格的六个最近邻与L_CA](../../raw/figures/Zhang2003a/fig_2_3PQK3GA3.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：六边形 CA 网格的局部放大，中心元胞被编号 1–6 的六个最近邻包围，标注相邻元胞中心距 L_CA。
  - **关键特征**：六边形网格相比正方形网格对称性更高，可显著降低由网格几何引入的数值各向异性；L_CA 是计算捕获概率 p_cap = l(t)/L_CA（式12）和时间步 Δt = min(L_CA/v_max, L_CA²/D_α, L_CA²/D_γ)（式14）的关键长度尺度。
  - **结论/意义**：确定了模型的空间离散结构和扩散、界面迁移的局部作用范围。

  - ![元胞三态：α/γ/α-γ界面](../../raw/figures/Zhang2003a/fig_3_TIVF3D85.png) → [[../figures/heterostructures-stacking-mechanics-misc|力学性质、剥离能与杂项]]
  - **图示描述**：CA 网格中元胞的三种状态示意图——α（铁素体）、γ（奥氏体）以及介于两者之间的"α/γ 界面"过渡态。
  - **关键特征**：界面元胞不是几何边界而是活跃的溶质再分配区域；铁素体通过"界面元胞被相邻 α 元胞捕获"实现生长，同时碳原子向周围 γ 元胞扩散；形核仅发生在奥氏体晶界元胞上。
  - **结论/意义**：三态设计使模型能在介观尺度自然追踪相界面移动与溶质场演化。

  - ![A36钢初始奥氏体与最终铁素体/渗碳体模拟组织](../../raw/figures/Zhang2003a/fig_4_Y5RG7LME.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：两子图并置，(a) 为 A36 钢（C0.17、Mn0.74、Si0.012、Cu0.016、Ni0.01、Cr0.019 wt%）经均匀恒形核率再结晶生成的初始奥氏体组织，d_γ = 18 μm；(b) 为足够高冷速下相变完成后的最终组织。
  - **关键特征**：不同灰度代表不同晶粒取向；铁素体优先在原奥氏体晶界形核并向晶内生长；深灰色颗粒为渗碳体，出现在碳富集且来不及扩散的界面处。
  - **结论/意义**：直观验证了"晶界形核 + 碳扩散控制生长 + 高冷速下渗碳体析出"三条核心假设，是模型物理合理性的视觉证据。

  - ![铁素体晶粒尺寸dα随冷却速率Q下降](../../raw/figures/Zhang2003a/fig_5_UEJHYHYW.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：横轴为冷却速率 Q（°C/s），纵轴为铁素体平均晶粒尺寸 d_α（μm），单条单调下降曲线。
  - **关键特征**：d_α = Σ d_i^α / N_α；冷速越大，过冷度越大、形核概率越高、晶核越多，最终晶粒越细小；把"快冷细化晶粒"的冶金经验定量化为可计算的函数关系。
  - **结论/意义**：为通过控冷工艺定量设计铁素体晶粒度提供了直接理论依据。

  - ![每奥氏体晶粒内铁素体晶粒数M：模拟与实验对比](../../raw/figures/Zhang2003a/fig_6_F9QA8UF3.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：横轴为冷却速率 Q（°C/s），纵轴为每个奥氏体晶粒内的铁素体晶粒平均数 M = N_α/N_γ（无量纲），曲线为模拟值、菱形点为 Militzer 等人的实验数据。
  - **关键特征**：M 随冷速增大而上升，模拟曲线与实验点趋势一致、数值接近；M 直接反映晶界形核事件密度，是连接冷速与最终组织的关键统计量。
  - **结论/意义**：这是模型定量验证的核心图表，证明四项基本假设及 CA 算法可靠，为后续机理分析奠定可信度。

  - ![形核元胞数n_nuc随过冷度ΔT：I区上升II区饱和（561/1352/1590）](../../raw/figures/Zhang2003a/fig_7_CK99QF4V.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：横轴为过冷度 ΔT = Ae3_0 − T（°C），纵轴为形核元胞数 n_nuc（无量纲），三条曲线分别对应 11、41、61 °C/s 冷速。
  - **关键特征**：每条曲线在 I 区随 ΔT 快速上升、在 II 区趋于饱和；饱和值随冷速增大而显著升高，分别为 561（11 °C/s）、1352（41 °C/s）、1590（61 °C/s）；形核过程在过冷早期（I 区）即已基本完成。
  - **结论/意义**：定量说明最终形核数是冷速的确定性函数，且形核窗口集中在相变最早期。

  - ![铁素体转变分数Y随过冷度ΔT](../../raw/figures/Zhang2003a/fig_8_2JAJBYIB.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：横轴为过冷度 ΔT（°C），纵轴为铁素体转变分数 Y = (n_nuc + n_grow)/n_cell（%），三条曲线对应 11、41、61 °C/s 冷速。
  - **关键特征**：三种冷速下 Y 的饱和值几乎相同；高冷速因渗碳体提前析出消耗部分碳，饱和值略低；结合图7可知，低冷速下形核数少而总转变量相当，因此每个铁素体晶粒可分得更多碳、扩散更充分，最终长得更大。
  - **结论/意义**：与图7共同解释了"冷速越小晶粒越粗大"的物理机制。

  - ![铁素体转变分数Y随时间t：高冷速相变更快](../../raw/figures/Zhang2003a/fig_9_WIGUFCEW.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：横轴为物理时间 t（s），纵轴为铁素体转变分数 Y（%），三条 S 形曲线对应 11、41、61 °C/s 冷速。
  - **关键特征**：冷速越高，曲线起始越早、上升越陡、到达饱和所需时间越短；这是大过冷度下形核率与生长速度同时提高的动力学结果。
  - **结论/意义**：从时间维度量化了冷速对相变动力学的加速作用。

  - ![形核分数Y_nuc随ΔT：高冷速下早期剧烈振荡](../../raw/figures/Zhang2003a/fig_10_GMMDUYPD.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：横轴为过冷度 ΔT（°C），纵轴为形核分数 Y_nuc = n_nuc/(n_nuc + n_grow)（无量纲），对比 11 °C/s 与 61 °C/s 两条曲线。
  - **关键特征**：61 °C/s 曲线在 ΔT < 95 °C 的早期区间出现剧烈振荡且数值明显高于低冷速曲线；振荡反映形核与生长在空间和溶质上的激烈争夺，高 Y_nuc 表明此阶段形核主导而非生长主导；低冷速下曲线平缓，形核与生长交替较温和。
  - **结论/意义**：把"形核-生长竞争"这一抽象机制可视化为可观测的振荡信号，是全文机理讨论的精华。

  - ![1°C/s下实验金相与模拟组织对比](../../raw/figures/Zhang2003a/fig_11_C5MNERW5.png) -> [[../figures/experimental-setups|实验测试与测量装置]]
  - **图示描述**：(a) 冷速 1 °C/s 下 A36 钢的实验金相照片；(b) 同等冷速下 CA 模拟的微观组织，白色方框标出渗碳体区域。
  - **关键特征**：模拟图中等轴铁素体晶粒沿原奥氏体晶界分布，晶粒尺寸、形貌和相分布与实验金相高度相似；白色方框指示的渗碳体位置与高冷速下碳富集区一致。
  - **结论/意义**：在图6的定量验证之外，从形貌学层面完成定性闭环，进一步确认模型的预测能力。

  - ![表1：Si/Mn/Ni/Cu/Cr的Zener参数ΔT_i^M与ΔT_i^NM](../../raw/figures/Zhang2003a/tab_1_MV8VNLSS.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - **图示描述**：表1列出五种合金元素 Si、Mn、Ni、Cu、Cr 对应的两个 Zener 参数 ΔT_i^M 与 ΔT_i^NM（单位：°C/at.%），用于式4计算超元素 S 的自由能变化。
  - **关键特征**：Mn 的影响最大（ΔT^M = −39.5、ΔT^NM = −37.5），Cr 次之（−18、−19），Si 最小（0、−3）；Ni（−18、−6）、Cu（−11.5、−4.5）介于其间；这些参数把置换型合金元素对相变驱动力的影响以线性叠加方式纳入形核公式，是"超元素 S"近似的关键数据支撑。
  - **结论/意义**：使多元合金钢的形核驱动力计算可退化为伪二元 Fe-C 问题，显著降低了模型复杂度。

## 🔬 项目连接
无直接项目连接。本文是低碳钢奥氏体→铁素体扩散型相变的元胞自动机介观模拟，与双光子/非线性光学（project-1）、Mn 多铁（project-2）、机械发光 NN（project-3）、TTF 分子计算（project-4）、SnTe 铁电模拟（project-5）、湿度传感（project-6）、CDW（project-7）在材料体系、物理机制和方法上均无可复用的直接参考价值；其 CA/有限体积扩散求解流程针对钢铁凝固相变设计，不属于上述项目所依赖的 DFT/MLIP/光学/铁电方法链。
## 📝 组织与用词
文章按"问题提出→四项基本假设→形核/生长数学模型（式1–8）→CA 算法七要素（网格/状态/初始化/温变/形核/生长/时间步）→结果验证（图6 定量、图11 定性）→机理讨论（图5,7–10）→结论"推进，核心论证链是"冷速↑→过冷度↑→晶界元胞形核概率 p_nuc↑→形核数 M↑→晶粒 dα↓"，并通过 Y_nuc 振荡曲线把"形核-生长竞争"可视化。值得复用的术语：
  - [[../concepts/cellular-automaton|cellular automaton / 元胞自动机]]（CA）
  - [[../concepts/undercooling|undercooling / 过冷度]]（ΔT = Ae3 − T）
  - nucleation probability / capture probability / 形核概率 p_nuc 与捕获概率 p_cap
  - [[../concepts/soft-impingement|soft impingement / 软碰撞]]（扩散场重叠）
  - [[../concepts/solute-redistribution|solute redistribution / rejection / 溶质再分配与排出]]（c_precipitate）
  - super-element S–C / 超元素 S–C 伪二元
  - α/γ interface cell / α/γ 界面元胞（过渡态）
  - equiaxed growth / 等轴生长
## ✏️ 可写入 Wiki 的要点
  1. 模型用 200×200 二维六边形 CA 网格代表 125×125 μm² 样品、周期性边界，六边形网格比正方形网格能显著降低数值[[../concepts/migdal-eliashberg-theory|各向异性]]。
  2. 四项基本假设：(i) Fe-Xi-C 等效为超元素 S–C 二元；(ii) 铁素体在奥氏体[[../concepts/grain-boundary-nucleation|晶界形核]]；(iii) 生长由 C 在 γ 中的扩散控制；(iv) 以 Fe-C 相图 γ 相线 Ae3 为相变平衡判据。
  3. 形核率 I(T) = K1(kT)^(−1/2) D_γ exp[−K2/(kT(ΔG_{γ→α}^N)²)]，其中 K1=2.07×10³ J^{1/2} cm^{−4}、K2=6.33×10^{−15} J³ mol^{−2}（Umemoto 等经验值）；形核驱动力 ΔG_{γ→α}^N = ΔG_{γ→α}^S − RT ln a_γ^S，叠加 Zener 参数（表1：Mn ΔT^M=−39.5、ΔT^NM=−37.5；Si 0/−3；Ni −18/−6；Cu −11.5/−4.5；Cr −18/−19）。
  4. 扩散用 ∂c_ν/∂t = D_ν∇²c_ν，界面用 Stefan 条件 D_γ(∂c_γ/∂n) − D_α(∂c_α/∂n) = v_n(c_α^{α/γ} − c_γ^{α/γ})；六边形网格上用显式有限体积法求解。
  5. CA 概率规则：形核概率 p_nuc = δn·S_γ（δn 由式9 对[[../concepts/undercooling|过冷度]]积分），随机数 r_s≤p_nuc 即形核；捕获概率 p_cap = l(t)/L_CA，l(t)=∫v dt；元胞转变后向邻居奥氏体元胞平均分配 c_precipitate = c − c^{α*}，每个邻居得 c_precipitate/n_ei，自然再现[[../concepts/soft-impingement|软碰撞]]。
  6. 时间步 Δt = min(L_CA/v_max, L_CA²/D_α, L_CA²/D_γ)，同时受生长速度和两相扩散稳定性约束。
  7. A36 钢（d_γ=18 μm）模拟定量结果：冷速 11/41/61 °C/s 对应的饱和形核数 n_nuc = 561/1352/1590；冷速越大 d_α 越小、M 越大、相变完成时间越短；最终转变分数 Y 几乎相同，高冷速因[[../concepts/cementite-precipitation|渗碳体析出]]而略低。
  8. 形核集中在过冷早期 zone I 完成，zone II 进入饱和；高冷速下 Y_nuc=n_nuc/(n_nuc+n_grow) 在 ΔT<95 °C 区间剧烈振荡且数值更高，表明早期形核主导而非生长主导。
  9. 低冷速下形核数少，每个铁素体晶粒平均分担的排出碳更多、扩散更充分，利于等轴生长，最终晶粒粗大；高冷速则相反。
  10. 渗碳体作为铁素体生长前方 α/γ 界面元胞碳富集到无法及时扩散时形成的障碍相，是高冷速下 Y 饱和值略降的原因；模型与 Militzer 等实验的 M 曲线及 1 °C/s 金相形貌均吻合。
