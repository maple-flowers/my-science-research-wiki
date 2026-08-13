---
tags:
  - type/figure-collection
---

# 理论模型与计算方法：应变、弹性与力学模型

> 属于 [[mathematical-models|理论模型与计算方法]]

## 条目

### 1. 2D应变矩阵形式
![2D应变矩阵形式](../../raw/figures/gaoStrainEngineeringFerroelectric2024/eq_2_VYQ8NWNX.png)
*   **来源**：[[../papers/gaoStrainEngineeringFerroelectric2024]]
*   **图示描述**：写出 η_i0 的 2×2 对称矩阵形式，对角元 e_xx、e_yy 为轴向应变，非对角元 e_xy 为剪切应变，x、y 轴分别沿 FE-P₀ 的 a、b 方向。
*   **关键特征**：明确把变体间转换拆成"单轴 + 剪切"两类力学分量，从而可以分别施加、独立考察其贡献。

### 2. η21转变应变张量
![η21转变应变张量](../../raw/figures/gaoStrainEngineeringFerroelectric2024/eq_3_QGZE4SD7.png)
*   **来源**：[[../papers/gaoStrainEngineeringFerroelectric2024]]
*   **图示描述**：给出 FE-P₀ 到 FE-P₆₀ 转换所需的具体应变张量数值 η₂₁ = [[−0.026, −0.029], [−0.029, 0.0297]]。
*   **关键特征**：对角元 e_xx=−0.026、e_yy=0.0297 表明需要在 x 方向压缩约 2.6%、y 方向伸长约 2.97%；非对角元 e_xy=−0.029 表示还需负向剪切应变 2.9%。

### 3. η31转变应变张量
![η31转变应变张量](../../raw/figures/gaoStrainEngineeringFerroelectric2024/eq_4_DGN4M7N8.png)
*   **来源**：[[../papers/gaoStrainEngineeringFerroelectric2024]]
*   **图示描述**：给出 FE-P₀ 到 FE-P₁₂₀ 转换所需的具体应变张量数值 η₃₁ = [[−0.026, 0.029], [0.029, 0.0297]]。
*   **关键特征**：对角元与 η₂₁ 相同（e_xx=−0.026、e_yy=0.0297），但剪切元 e_xy=+0.029 取正号，与 η₂₁ 符号相反——正是这一剪切符号区分了 P₆₀ 与 P₁₂₀ 两个变体。

### 4. 图4 h-BN和3R-MoS₂双壁纳米管形成能随直径变化及解析模型ΔE=E_circle−E_kink，预测临界直径（h-BN约2.8 nm，3R-MoS₂约9.1 nm）
![图4 h-BN和3R-MoS₂双壁纳米管形成能随直径变化及解析模型ΔE=E_circle−E_kink，预测临界直径（h-BN约2.8 nm，3R-MoS₂约9.1 nm）](../../raw/figures/heSwitchingTwodimensionalSliding2025/fig_4_J9YU9FTH.png)
*   **来源**：[[../papers/heSwitchingTwodimensionalSliding2025]]
*   **图示描述**：图4以扶手椅型双壁纳米管为可控模型，(a)(b) 分别绘出 h-BN 和 3R-MoS₂ 纳米管在弛豫前（理想圆形）与弛豫后（出现扭结）的形成能随直径变化，(c) 给出解析模型中 ΔE = E_circle − E_kink 随直径的变化。
*   **关键特征**：当直径超过临界值后，扭结纳米管形成能低于圆形纳米管，扭结在热力学上更稳定；解析模型预测 h-BN 临界直径约 2.8 nm、3R-MoS₂ 约 9.1 nm，与深度势能模拟的 ~1.8 nm 和 ~9.4 nm 高度一致；3R-MoS₂ 扭结角约 17.5° 和 34°，约为 h-BN 的一半，原因是其层间距更大（6.14 Å vs 3.25 Å），而 θ ∝ Δd/D。

### 5. 图4 接触金属效应与有限元模拟：PMN-PT(111)上Ni器件CAFM图与沟道应变FEA模拟吻合；Ag（−0.2 GPa，~4%调制）vs Ni（0.58 GPa，~10^9%调制）对比；静态拉应变偏置+铁电动态应变调制机理示意
![图4 接触金属效应与有限元模拟：PMN-PT(111)上Ni器件CAFM图与沟道应变FEA模拟吻合；Ag（−0.2 GPa，~4%调制）vs Ni（0.58 GPa，~10^9%调制）对比；静态拉应变偏置+铁电动态应变调制机理示意](../../raw/figures/houStrainbasedRoomtemperatureNonvolatile2019/fig_4_4I4JUQYB.png)
*   **来源**：[[../papers/houStrainbasedRoomtemperatureNonvolatile2019]]
*   **图示描述**：图4验证接触应力的作用。(a) 左侧为PMN-PT(111)上50 nm MoTe2（W/L=6.3）Ni接触器件的CAFM电流图，中间为给定边缘夹持拉伸应变时沟道εx分布的有限元（FEA）模拟，下方为"接触静态应变（蓝）+PMN-PT电场可控动态应变（红）"协同越过相界的机理示意；(b) 为Ag接触（−0.2 GPa低压应力）与Ni接触（0.58 GPa拉应力）器件GDS–EGS对比，插图为Ag器件的变温演化。
*   **关键特征**：FEA应变分布与CAFM电流图像形状高度吻合，(111)取向衬底上仍出现相变表明该机制对铁电取向不敏感；由接触应力计算得接触处施加约0.4%拉伸应变，结合CAFM测得的半导体区延伸长度提取相变应变量化阈值约0.33%，与MoTe2相变的实验和理论预测一致；Ag接触13个器件所有温度下仅约4%电导调制，Ni器件达约10⁹%调制（量级差异）；高拉应力绝缘MgF2封装低应力Ag接触后可恢复大开关，形成"拉伸应力源必需"的闭环对照。

### 6. 公式2 Green-Lagrange应变张量定义
![公式2 Green-Lagrange应变张量定义](../../raw/figures/liFerroelasticityDomainPhysics2016/eq_2_2S66YKHE.png)
*   **来源**：[[../papers/liFerroelasticityDomainPhysics2016]]
*   **图示描述**：由变换矩阵 Jᵢ（满足 Hᵢ = JᵢH₀）定义的 Green-Lagrange 相变应变张量 ηᵢ = ½(JᵢᵀJᵢ − I) = ½[(H₀⁻¹)ᵀ Hᵢᵀ Hᵢ H₀⁻¹ − I]，上标 −1、T 分别表示求逆与转置，I 为 2×2 单位矩阵。
*   **关键特征**：将"母相→畸变相"的晶格映射转化为可直接比较的有限应变度量，是计算各变体自发应变与变体间相对转换应变的统一数学框架。

### 7. 公式3 二维应变张量对称形式
![公式3 二维应变张量对称形式](../../raw/figures/liFerroelasticityDomainPhysics2016/eq_3_EBEPXLQF.png)
*   **来源**：[[../papers/liFerroelasticityDomainPhysics2016]]
*   **图示描述**：二维相变应变张量的对称分量形式 η = [ε_xx, ε_xy; ε_xy, ε_yy]。
*   **关键特征**：ε_xx、ε_yy 为沿 x、y 方向的拉伸/压缩应变，ε_xy 为剪切应变分量；论文据此区分双轴应变（不破镜像、O2/O3 简并）与剪切应变（破镜像、可选择性稳定 O2 或 O3）。

### 8. 公式4 WTe2从1T到1T′三变体的自发应变矩阵η1/η2/η3
![公式4 WTe2从1T到1T′三变体的自发应变矩阵η1/η2/η3](../../raw/figures/liFerroelasticityDomainPhysics2016/eq_4_JSWN4I98.png)
*   **来源**：[[../papers/liFerroelasticityDomainPhysics2016]]
*   **图示描述**：DFT 弛豫得到的 WTe₂ 单层三变体相对于 1T 母相的自发应变矩阵：η₁ = [−0.005, 0.0; 0.0, 0.039]、η₂ = [0.029, −0.019; −0.019, 0.006]、η₃ = [0.029, 0.019; 0.019, 0.007]。
*   **关键特征**：O1 主要表现为 y 方向 +3.9% 拉伸，而 O2/O3 伴随约 ±1.9% 剪切分量；三者非对角元的符号差异正是后续剪切应变可区分 O2/O3 的几何来源。

### 9. 图5 沿a轴单轴拉伸下O1与O2/O3能量曲线及公切线（1%–4%共存区）
![图5 沿a轴单轴拉伸下O1与O2/O3能量曲线及公切线（1%–4%共存区）](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_5_XYSVC9LT.png)
*   **来源**：[[../papers/liFerroelasticityDomainPhysics2016]]
*   **图示描述**：横轴为沿 a 轴（二聚化 W 链方向）的单轴拉伸应变（%），纵轴为能量；b 轴方向应力弛豫到零（σ_y=0，对应自由边界），分别画出 O1 与 O2/O3 的能量曲线，并在两曲线间作公切线（虚线）。
*   **关键特征**：公切线两切点分别位于 1% 与 4% 应变处；在 1%–4% 区间内，O1 与 O2/O3 共存态的总能量低于任单一变体，对应应力-应变曲线上的"力平台"；触发共存的应变低至 1%，比图 3 双轴交叉点更易实验实现（拉伸不引发屈曲）。

### 10. 公式5 O1→O2/O1→O3的相对转换应变张量e²₁/e³₁
![公式5 O1→O2/O1→O3的相对转换应变张量e²₁/e³₁](../../raw/figures/liFerroelasticityDomainPhysics2016/eq_5_F7HM6IDY.png)
*   **来源**：[[../papers/liFerroelasticityDomainPhysics2016]]
*   **图示描述**：以 1T′ 相 O1 变体为参考构型，从变体 i 到 j 的相对相变应变张量 eⱼᵢ；O1→O2 与 O1→O3 的结果为 e²₁ = [0.034, −0.019; −0.019, −0.030]、e³₁ = [0.033, 0.019; 0.019, −0.030]。
*   **关键特征**：在无应变 O1 上施加约 +3.4% x 拉伸、−3.0% y 压缩（及 ±1.9% 剪切）即可使体系更倾向 O2 或 O3；应变量级仅百分之几，落在 TMD 单层 ~10% 弹性应变窗口内，构成"外应力可耦合切换变体"这一铁弹性判据的定量基础。

### 11. 图5 未来方向：ABC型化合物高通量筛选(a0-Eg、k14-e14)；PbTiO3皮秒超快泵浦-探测c轴动力学(5 ps退极化场极小值)；PbTiO3/SrTiO3超晶格中极化涡旋-反涡旋STEM
![图5 未来方向：ABC型化合物高通量筛选(a0-Eg、k14-e14)；PbTiO3皮秒超快泵浦-探测c轴动力学(5 ps退极化场极小值)；PbTiO3/SrTiO3超晶格中极化涡旋-反涡旋STEM](../../raw/figures/martinThinfilmFerroelectricMaterials2016/fig_5_4V7HUWMA.png)
*   **来源**：[[../papers/martinThinfilmFerroelectricMaterials2016]]
*   **图示描述**：a 图为 ABC 型化合物的高通量第一性原理筛选散点图，左图为计算晶格常数 a₀（Å）对带隙 Eg（eV），右图为机电耦合系数 k₁₄ 对压电常数 e₁₄（C·m⁻²），红点为已知化合物、其余为预测候选；b 图为飞秒泵浦-探测示意与时域曲线，横轴为时间（ps），纵轴为 PbTiO₃ 薄膜 c 轴晶格参数变化；c 图为 PbTiO₃/SrTiO₃ 超晶格中极化涡旋-反涡旋对的 STEM 像，叠加极化矢量并辅以相场模拟。
*   **关键特征**：a 图体现"材料基因组"工作流——用可快速计算的描述符在数千种候选材料中筛选目标铁电、压电与带隙性质；b 图中飞秒激光通过体光伏效应产生瞬态电流改变退极化场，经逆压电引起 c 轴应变，在约 5 ps 时达到极小值，载流子屏蔽后约 10 ps 恢复，揭示光-电-力耦合的皮秒时间尺度；c 图直接观察到极化连续旋转形成的涡旋-反涡旋拓扑结构，与相场模拟一致，是铁电拓扑学的实验证据；文中还指出压力下 CsPbI₃ 可同时进入拓扑绝缘相与可翻转铁电相并增强体光伏效应。

### 12. 图6 应变诱导石墨烯光学电导率各向异性及偏振依赖吸收实验
![图6 应变诱导石墨烯光学电导率各向异性及偏振依赖吸收实验](../../raw/figures/pengStrainEngineering2D2020/fig_6_H37PWHPZ.png)
*   **来源**：[[../papers/pengStrainEngineering2D2020]]
*   **图示描述**：(a–c) 理论计算给出未应变石墨烯各向同性光学电导率，施加应变后沿应变方向与垂直方向的电导率出现差异，透射率随入射光电场偏振方向变化；(d–e) 柔性衬底上石墨烯的偏振分辨透射/吸收实验验证该各向异性。
*   **关键特征**：未应变时单层石墨烯吸收 πα≈2.3% 且无偏振依赖；单轴应变打破六重对称后，光学电导率张量出现非对角元与方向依赖，使平行/垂直应变方向的光吸收不同；该效应在较宽可见–近红外波段成立，可通过偏振角扫描读出应变量级。

### 13. 公式1 A畴二维自发应变张量 εxx=+0.0049, εyy=-0.0049
![公式1 A畴二维自发应变张量 εxx=+0.0049, εyy=-0.0049](../../raw/figures/xuTwodimensionalFerroelasticityVan2021/eq_1_RV7ML8IY.png)
*   **来源**：[[../papers/xuTwodimensionalFerroelasticityVan2021]]
*   **图示描述**：以 [1-100] 为 x 轴、[11-20] 为 y 轴、按 Aizu 定义写出的 2H-β'-In₂Se₃ A 畴二维自发应变张量 ε(A)。
*   **关键特征**：εxx=+0.0049（沿 x 方向拉伸），εyy=−0.0049（沿 y 方向压缩），剪切分量 εxy=0；数值约 ±0.49%，远小于第一性原理预测的 1T' TMDs 中典型的"百分之几"应变；无面外分量，属纯面内二维铁弹。

### 14. 公式3 B畴自发应变张量
![公式3 B畴自发应变张量](../../raw/figures/xuTwodimensionalFerroelasticityVan2021/eq_3_7FVA24F6.png)
*   **来源**：[[../papers/xuTwodimensionalFerroelasticityVan2021]]
*   **图示描述**：B 畴由 J+ 对 ε(A) 做相似变换 ε(B)=J+ ε(A) J+⁻¹ 得到的二维应变张量。
*   **关键特征**：ε(B)=[[−0.0025, −0.0042], [−0.0042, 0.0025]]；正应变分量一负一正，剪切分量 εxy=−0.0042 非零，表明 B 畴主轴相对 x/y 轴旋转。

### 15. 公式4 C畴自发应变张量
![公式4 C畴自发应变张量](../../raw/figures/xuTwodimensionalFerroelasticityVan2021/eq_4_SRTNGGDU.png)
*   **来源**：[[../papers/xuTwodimensionalFerroelasticityVan2021]]
*   **图示描述**：C 畴由 J− 对 ε(A) 做相似变换 ε(C)=J− ε(A) J−⁻¹ 得到的二维应变张量。
*   **关键特征**：ε(C)=[[−0.0025, +0.0042], [+0.0042, 0.0025]]；剪切分量 εxy=+0.0042 与 B 畴符号相反，对应 C 畴沿第三个 <11-20> 方向拉伸。

### 16. 公式5 3R相A变体三维应变张量（含εxz=-0.0126）
![公式5 3R相A变体三维应变张量（含εxz=-0.0126）](../../raw/figures/xuTwodimensionalFerroelasticityVan2021/eq_5_AL5UGS89.png)
*   **来源**：[[../papers/xuTwodimensionalFerroelasticityVan2021]]
*   **图示描述**：在 2H 二维张量基础上加入 [0001] 为 z 轴后，3R-β'-In₂Se₃ A 变体的三维自发应变张量 ε(A,3R)。
*   **关键特征**：ε(A,3R)=[[0.0049, 0, −0.0126], [0, −0.0049, 0], [−0.0126, 0, 0]]；面内分量保持 ±0.49%；新增面外剪切 εxz=−0.0126，由 91.44° 的晶格倾斜角推导；εzz=0。

### 17. 公式6 3R相B变体三维应变张量
![公式6 3R相B变体三维应变张量](../../raw/figures/xuTwodimensionalFerroelasticityVan2021/eq_6_3IVQPWRA.png)
*   **来源**：[[../papers/xuTwodimensionalFerroelasticityVan2021]]
*   **图示描述**：由三维旋转矩阵对 ε(A,3R) 做相似变换得到的 3R 相 B 变体张量 ε(B,3R)。
*   **关键特征**：ε(B,3R)=[[−0.0025, −0.0042, +0.0063], [−0.0042, 0.0025, −0.0109], [+0.0063, −0.0109, 0]]；面内分量与 2H 相同，但出现非零 εyz=−0.0109 和 εxz=+0.0063，对应 B 畴相对 A 畴旋转后面外剪切方向的改变。

### 18. 公式7 3R相C变体三维应变张量
![公式7 3R相C变体三维应变张量](../../raw/figures/xuTwodimensionalFerroelasticityVan2021/eq_7_MK27GVUB.png)
*   **来源**：[[../papers/xuTwodimensionalFerroelasticityVan2021]]
*   **图示描述**：3R 相 C 变体三维应变张量 ε(C,3R)。
*   **关键特征**：ε(C,3R)=[[−0.0025, +0.0042, −0.0063], [+0.0042, 0.0025, +0.0109], [−0.0063, +0.0109, 0]]；与 B 张量相比，εxz、εyz 均反号；在 120° 畴壁处与 A 畴的垂直剪切分量反号→褶皱，在 60° 畴壁处与相邻畴同号→表面平整但畴壁倾斜。

### 19. 公式 波纹热涨落 Gao-Huang 模型 <h²>≈16 kB T S0/(π² δ)
![公式 波纹热涨落 Gao-Huang 模型 <h²>≈16 kB T S0/(π² δ)](../../raw/figures/yangRipplingFerroicPhase2021/eq_4_QASXJXYU.png)
*   **来源**：[[../papers/yangRipplingFerroicPhase2021]]
*   **图示描述**：Gao-Huang 热力学模型给出二维膜波纹均方振幅 <h²>≈16 k_B T S0/(π² δ)，其中 k_B 为玻尔兹曼常数、T 为温度、S0 为样品初始面积、δ 为弯曲刚度。
*   **关键特征**：<h²> 与温度 T 成正比、与弯曲刚度 δ 和初始面积 S0 成反比；单层 GeSe 低温相 δ=1.35 eV，样品 S0=27237.5 Å²；MD 测得的波纹振幅热涨落与该解析模型线性吻合，验证了模拟中波纹为热力学平衡涨落而非数值伪影。

### 20. 公式1 预应变定义 εpre=ΔL/L×100%
![公式1 预应变定义 εpre=ΔL/L×100%](../../raw/figures/yangStrainEngineeringTwodimensional2021/eq_1_TAWJDU8R.png)
*   **来源**：[[../papers/yangStrainEngineeringTwodimensional2021]]
*   **图示描述**：柔性衬底预拉伸法中预应变的定义式，L 为 PDMS 衬底初始长度，ΔL 为拉伸长度。
*   **关键特征**：εpre=(ΔL/L)×100%，原文式 (1)；单轴预拉伸释放后形成一维周期性褶皱，x、y 双向预拉伸则产生三维起皱；该量直接决定褶皱顶部可达到的最大应变上限。

### 21. 公式2 褶皱顶部最大应变 ε=π²hδ(1−σ²)/λ²
![公式2 褶皱顶部最大应变 ε=π²hδ(1−σ²)/λ²](../../raw/figures/yangStrainEngineeringTwodimensional2021/eq_2_MVDKLZED.png)
*   **来源**：[[../papers/yangStrainEngineeringTwodimensional2021]]
*   **图示描述**：预应变柔性衬底形成的周期性褶皱顶部最大应变计算公式。
*   **关键特征**：ε=π²hδ(1−σ²)/λ²，原文式 (2)；h 为二维材料厚度，σ 为泊松比，δ 和 λ 分别为褶皱高度和波长（可由 AFM/SEM 提取）；典型褶皱顶部应变处于 1–2% 区间；单层/双层因刚度低易塌陷，多层更易形成稳定褶皱。

### 22. 公式3 弯曲基底应变 ε=τ/(2R)；AFM针尖局部应变 ε=F/(AE)
![公式3 弯曲基底应变 ε=τ/(2R)；AFM针尖局部应变 ε=F/(AE)](../../raw/figures/yangStrainEngineeringTwodimensional2021/eq_3_HMFU6L9E.png)
*   **来源**：[[../papers/yangStrainEngineeringTwodimensional2021]]
*   **图示描述**：左侧为弯曲柔性衬底时二维材料上表面应变，右侧为 AFM 针尖加载下局域应变。
*   **关键特征**：弯曲法 ε=τ/(2R)（原文式 (3)），τ 为衬底厚度、R 为曲率半径，单轴均匀、连续可调、可逆；AFM 针尖法 ε=F/(AE)，F 为针尖作用力、A 为针尖横截面积、E 为二维材料杨氏模量，刚性 Si 衬底上 F 上限约 25 nN，故需悬浮膜结构以获得更大变形。

### 23. 公式5 气泡局部应变 ε∝(h/R)²
![公式5 气泡局部应变 ε∝(h/R)²](../../raw/figures/yangStrainEngineeringTwodimensional2021/eq_5_MPIIV52Z.png)
*   **来源**：[[../papers/yangStrainEngineeringTwodimensional2021]]
*   **图示描述**：包围自发气泡的单层二维材料薄膜局部应变与气泡高宽比的标度关系。
*   **关键特征**：ε∝(h/R)²，原文式 (5)；MoS₂/h-BN 界面自发气泡由此可引入约 2% 的平滑梯度应变；应变随气泡顶点距离平滑变化，是研究连续梯度应变和激子漂移的天然平台。

### 24. 公式6 悬浮膜中心应变 ε=σ(ν)(δ/a)²
![公式6 悬浮膜中心应变 ε=σ(ν)(δ/a)²](../../raw/figures/yangStrainEngineeringTwodimensional2021/eq_6_PSPYJIMK.png)
*   **来源**：[[../papers/yangStrainEngineeringTwodimensional2021]]
*   **图示描述**：压力差鼓泡法中，悬浮在微腔上的二维材料薄膜中心应变与其弯曲程度的关系。
*   **关键特征**：ε=σ(ν)(δ/a)²，原文式 (6)；σ(ν) 为取决于泊松比的常数，δ 为膜中心挠度、a 为微腔半径，均可由 AFM 测量；改变充入 N₂ 量即可连续、可逆地调节 δ 和应变；若把样品置入高压釜后骤回常压，可在圆孔上形成永久鼓起，但应变值固定不可调。

### 25. 公式8（原文编号续）配套非线性光学/力学关系
![公式8（原文编号续）配套非线性光学/力学关系](../../raw/figures/yangStrainEngineeringTwodimensional2021/eq_8_6QU4TXB3.png)
*   **来源**：[[../papers/yangStrainEngineeringTwodimensional2021]]
*   **图示描述**：配套公式 7 的非线性光学/力学关系，用于把偏振谐波信号与应变分量定量关联。
*   **关键特征**：该式与光弹张量形式体系一起，把 SHG 推广到非中心对称单层 TMD，THG 则可进一步用于中心对称材料（如双层 WS₂）；由此 SHG/THG 成像成为比 Raman/PL 更灵敏、可获取全张量的应变成像手段。

### 26. 图4 P4mm/P4bm势能图、OsO₅键合网络与结构参数随应变演化、pCOHP/−ICOHP、应变-相变能量景观
![图4 P4mm/P4bm势能图、OsO₅键合网络与结构参数随应变演化、pCOHP/−ICOHP、应变-相变能量景观](../../raw/figures/zhongHighthroughputExfoliationMultiferroic2025/fig_4_ABKMCTN8.png)
*   **来源**：[[../papers/zhongHighthroughputExfoliationMultiferroic2025]]
*   **图示描述**：五联图——(a) P4mm 与 P4bm 两势阱在外场下反转的势能示意图；(b) SrOsO₃ OsO₅ 键合网络，标注面外 d₁、面内 d₂ 键长与扭转角 θ；(c) θ、d₁、d₂ 随面内双轴应变 ε_ab（%）的演化；(d) 不同应变下 Os–O 的 −pCOHP 曲线及 −ICOHP 积分；(e) 相变路径能量随 ε_ab 变化的等高线景观。
*   **关键特征**：ε_ab = 1.2% 时 θ 由 8.68° 降至 0°，驱动 P4bm→P4mm；面外 −ICOHP 由 0.53 升至 0.91 eV，面内各向异性被淬灭；相变势垒随应变反转：1% 时 +0.11 meV/atom、1.2% 时 −3.74、2% 时 −7.9 meV/atom；本征 P4bm↔P4mm 势垒仅 9.1 meV/atom；SrIrO₃ 需 a 轴压缩 3.5%、SrMoO₃ 需 a 拉 0.7%/b 压 2.7%、BiFeO₃ 需 a/b 压 4%/3%。

### 27. Eq.2 剥离能增量求和 ΔE_j
![Eq.2 剥离能增量求和 ΔE_j](../../raw/figures/zhongHighthroughputExfoliationMultiferroic2025/eq_2_RTSAUWAA.png)
*   **来源**：[[../papers/zhongHighthroughputExfoliationMultiferroic2025]]
*   **图示描述**：剥离能按逐步拉伸-弛豫增量累加 ΔE_j = (1/A) Σ_{i=0}^{j} (E_{i,1} − E_{i,0})，E_{i,0} 为瞬时稳态能、E_{i,1} 为拉伸弛豫后能量。
*   **关键特征**：每步外移 ~0.2 Å，加 DFT-D3 色散修正；当 E_{i,1} ≤ E_{i,0} 时判定层分离；对所有 ΔE 求和即得 E_exf，最低 0.049 eV/Å²（NaZnO₃）。
