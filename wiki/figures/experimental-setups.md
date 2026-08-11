# 实验测试与测量装置 (Experimental Setups & Measurements)

> 收录二维铁电/多铁材料研究中的生长合成装置、PFM/AFM/CAFM 等探针显微表征平台、THz/XRD/TEM 等谱学与衍射手段，以及器件制备流程与器件架构相关的图表和关键公式。

[[科研Wiki/wiki/figures/_index|← 返回总索引]]

---

## 🧪 生长、合成与高通量筛选 (Growth, Synthesis & Screening)

### 1. 插层化合物 AM₂X₄ 的高通量筛选流程
通过第一性原理高通量计算，从 AM₂X₄ 型插层化合物中系统筛选兼具铁电性与磁性的多铁候选材料。

![图：AM₂X₄ 插层化合物多铁材料的高通量 DFT 筛选流程图](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_2_7QNUMABJ.png)
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]
*   **关键特征**：覆盖结构稳定性、铁电极化、磁耦合与磁各向异性的多级筛选漏斗。

### 2. 二维层状材料的气相沉积途径
对比 CVD、PVD、MBE 与 ALD 四种气相沉积方法在硫族化合物等二维层状材料生长中的装置原理与适用范围。

![图：CVD、PVD、MBE、ALD 四种气相沉积生长装置示意图](../../raw/figures/RecentAdvancesGrowth2025/fig_4_QAJUJ232.png)
*   **来源**：[[../papers/RecentAdvancesGrowth2025]]
*   **关键特征**：CVD 灵活、PVD 直接成膜、MBE 原子级精度、ALD 三维保形。

### 3. In₂Se₃ 的 CVD 生长示意图
以 Se 与 In₂O₃ 为前驱体，在云母基底上化学气相沉积二维 In₂Se₃ 的生长过程。

![图：云母基底上 In₂Se₃ 的 CVD 生长原理示意图](../../raw/figures/cuiIntercorrelatedInplaneOutofplane2018a/fig_1_MQ5WQF79.png)
*   **来源**：[[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]

### 4. p 轨道多铁材料的设计与验证路线
总结绕过 d⁰ 规则、在二维金属氮氧化物 X₂NO₂ 中实现铁电与 p 轨道铁磁共存的四步研究路线。

| 步骤 | 核心问题 | 方法/内容 | 关键结论 |
| :-- | :-- | :-- | :-- |
| **1. 提出设计** | 如何绕过 d⁰ 规则，实现铁电与磁性的共存？ | 设计 p 轨道元素（N）参与的非中心对称结构 | 设计出稳定的二维 X₂NO₂ (X = In, Tl) 材料，其结构与 In₂Se₃ 类似。 |
| **2. 性质验证** | 设计的材料是否稳定？是否具备预期性质？ | 第一性原理计算（DFT）、声子谱、分子动力学模拟 | Tl₂NO₂ 同时表现出本征铁电性和由 N-2p 电子主导的强铁磁性及金属性，居里温度高于室温。 |
| **3. 机理揭示** | p 电子如何产生铁磁性？铁电性来源是什么？ | 电子结构分析（能带、态密度）、Stoner 判据 | 费米能级附近局域的 N-2p 电子满足 Stoner 判据驱动巡游铁磁性；N 离子非中心偏移导致铁电性。 |
| **4. 功能拓展** | 铁电与磁性能否耦合？ | 构建 Tl₂NO₂/WTe₂ 异质结进行界面工程 | 观察到磁电效应，改变铁电极化方向可调控异质结总磁矩。 |

*   **来源**：[[../papers/aiFerroelectricityCoexistedPorbital2022]]

### 5. 二维材料制备方法对比
系统比较主要制备路线的类别、优缺点及典型材料。

<table><thead><tr><th>方法</th><th>类别</th><th>优点</th><th>局限</th><th>典型材料</th></tr></thead><tbody><tr><td>机械剥离</td><td>自顶向下</td><td>高结晶质量、清洁表面</td><td>厚度/尺寸无法控制、产率低</td><td>石墨烯、TMDs</td></tr><tr><td>液相剥离</td><td>自顶向下</td><td>产量可行、利用率高</td><td>薄片尺寸有限、溶剂/离子残留</td><td>石墨烯、金属片</td></tr><tr><td>化学气相沉积 (CVD)</td><td>自底向上</td><td>生长控制好、尺寸大、质量高</td><td>真空条件控制复杂</td><td>Cr₂S₃、CuCrSe₂</td></tr><tr><td>化学气相传输 (CVT)</td><td>自底向上</td><td>高纯单晶、层厚控制清晰</td><td>易形成较大的原始粉末</td><td>NiI₂、CuCrP₂S₆</td></tr><tr><td>物理气相沉积 (PVD)</td><td>自底向上</td><td>可整修靶材、直接沉积成膜</td><td>薄膜纯度控制难度大</td><td>SnSe</td></tr><tr><td>分子束外延 (MBE)</td><td>自底向上</td><td>原子级精密度高、超净环境</td><td>速率慢、规模化难</td><td>NiI₂</td></tr><tr><td>原子层沉积 (ALD)</td><td>自底向上</td><td>三维叠层保形生长、精确控制</td><td>前驱体选择受限、增速慢</td><td>NiIᵪ</td></tr></tbody></table>

*   **来源**：[[../papers/RecentAdvancesGrowth2025]]

### 6. 滑移铁电的构筑方式
归纳莫尔超晶格、3R 相结构与扭转角三种构筑层间滑移铁电极化的物理途径及代表材料。

<table><thead><tr><th>构筑方式</th><th>原理</th><th>代表性材料</th></tr></thead><tbody><tr><td><strong>莫尔超晶格</strong></td><td>两层同质或异质材料旋转形成莫尔周期势，在局域域内诱发铁电极化</td><td>扭转双层石墨烯、h-BN/石墨烯</td></tr><tr><td><strong>3R 相结构</strong></td><td>TMD 的 3R 斜方六面体非中心对称堆积，层间滑动即可切换极化</td><td>3R-MoS₂、3R-WSe₂</td></tr><tr><td><strong>扭转角</strong></td><td>人工构建扭转角使同质结或异质结的反演对称性破缺</td><td>任意两层二维单层材料叠加</td></tr></tbody></table>

*   **来源**：[[../papers/sunSlidingFerroelectricityTwodimensional2025]]
*   **另见**：同表的 markdown 版本收录于 [[crystal-structures#📊 关键数据表格 (Key Data Tables)|晶体结构与原子排布]]。

### 7. 滑移铁电材料制备工艺对比
比较 CVD、PVD、机械剥离/转移、液相剥离与电化学剥离在滑移铁电样品制备中的优势与局限。

<table><thead><tr><th>方法</th><th>优势</th><th>局限</th></tr></thead><tbody><tr><td><strong>CVD</strong></td><td>可大面积生长，控制层数、合成异质结（如逆流 CVD 制备 3R-MoS₂）</td><td>表面易引入缺陷与杂质，对区域措施可靠性要求高</td></tr><tr><td><strong>PVD</strong></td><td>低污染、大面积均匀成膜，可调控晶型</td><td>外延面积受限</td></tr><tr><td><strong>机械剥离/转移</strong></td><td>高质量、层结构完整、可控扭转角堆叠</td><td>产出低、面积小、可控性与重复性弱</td></tr><tr><td><strong>液相剥离</strong></td><td>可大量制备纳米厚薄片</td><td>横向尺寸不均、界面污染</td></tr><tr><td><strong>电化学剥离</strong></td><td>高质量、高效</td><td>可能破坏层状结构使薄片碎裂</td></tr></tbody></table>

*   **来源**：[[../papers/sunSlidingFerroelectricityTwodimensional2025]]

---

## 🔬 探针显微与局域电学表征 (Probe Microscopy & Local Characterization)

### 1. In₂Se₃ 面内铁电畴的 PFM 成像
对云母上原生 In₂Se₃ 进行面内 PFM 振幅与相位成像，揭示相互关联的面内/面外铁电畴结构。

![图：In₂Se₃ 面内 PFM 振幅与相位图像，显示原生铁电畴图案](../../raw/figures/cuiIntercorrelatedInplaneOutofplane2018a/fig_2_HLGI8HDK.png)
*   **来源**：[[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]
*   **关键特征**：面内与面外极化锁定，是 In₂Se₃ 互锁铁电性的直接证据。

### 2. 面内/面外极化翻转耦合模型
示意 In₂Se₃ 薄片中面内（IP）与面外（OOP）铁电极化在电场下协同翻转的结构机制。

![图：In₂Se₃ 面内与面外极化相互锁定及协同翻转的结构模型](../../raw/figures/cuiIntercorrelatedInplaneOutofplane2018a/fig_3_YHE8WF9K.png)
*   **来源**：[[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]

### 3. In₂Se₃ 电导行为的 CAFM 测绘
导电原子力显微镜（CAFM）图像显示 In₂Se₃ 局域导电通道随极化态的空间分布。

![图：In₂Se₃ 薄片的 CAFM 电流测绘，反映极化调控的电导行为](../../raw/figures/cuiIntercorrelatedInplaneOutofplane2018a/fig_4_6L59ASAB.png)
*   **来源**：[[../papers/cuiIntercorrelatedInplaneOutofplane2018a]]

### 4. 少层 NiI₂ 的 AFM 形貌表征
光学照片与原子力显微镜图像联合确定少层 NiI₂ 薄片的横向尺寸与层厚。

![图：少层 NiI₂ 晶体的光学照片与 AFM 高度图像，用于标定层数](../../raw/figures/RecentAdvancesGrowth2025/fig_14_692EH7SS.png)
*   **来源**：[[../papers/RecentAdvancesGrowth2025]]

### 5. BiFeO₃ 极化的光伏非破坏性读取
利用铁电光伏效应读取 BiFeO₃ 上/下极化态，短路电流方向随极化反向而反转，实现无外偏压的非破坏性读出。

![图：BiFeO₃ 光伏测量装置示意及上/下极化态对应的光生电流](../../raw/figures/Chen2016electrical/fig_5_V43HJ2T7.png)
*   **来源**：[[../papers/Chen2016electrical]]
*   **关键特征**：I_sc 方向反转提供符号级对比度，无需外电场即可读取。

### 6. 铁电畴读取技术参数对比
汇总 PFM、导电 AFM 与光伏测量三类表征手段在畴成像与极化读取中的功能与关键参数。

| 技术 | 功能 | 关键参数 |
| :-- | :-- | :-- |
| 压电力显微镜（PFM） | 畴结构成像，极化翻转表征 | 针尖半径 30–35 nm |
| 导电 AFM（c-AFM） | 局部电流读取 | 读取偏压 = 1 V |
| 光伏测量 | 宏观极化状态读取 | 300 μm ITO 电极，100 mW/cm² |

*   **来源**：[[../papers/Chen2016electrical]]

### 7. c-AFM 与光伏读取方式对比
从读取速度、空间分辨率、电源需求、信号对比度、集成难度与疲劳特性六个维度比较两种非破坏性读取方案。

| 维度 | 导电 AFM 读取 | 光伏效应读取 |
| :-- | :-- | :-- |
| **读取速度** | 受限于 AFM 扫描 | 光照响应可达 ns 级 |
| **空间分辨率** | ~30 nm（针尖尺寸） | ~μm 级（光斑尺寸） |
| **是否需要电源** | 需要 1 V 偏压 | 完全自供能（光生伏打） |
| **信号对比度** | 电流差异（倍数级） | I_sc 方向反转（符号级） |
| **集成难度** | 需要导电 AFM 平台 | 可集成到 CMOS 工艺 |
| **疲劳问题** | 1 V 偏压低，疲劳小 | 无外电场，无疲劳 |

*   **来源**：[[../papers/Chen2016electrical]]

---

## 📡 谱学、衍射与宏观表征 (Spectroscopy, Diffraction & Macroscopic Probes)

### 1. NiI₂ 的太赫兹时域光谱测量
示意在 NiI₂ 上开展太赫兹透射与反射测量的几何配置，用于探测低频电磁激发与磁电响应。

![图：NiI₂ 太赫兹透射 (a) 与反射 (b) 测量装置示意图](../../raw/figures/RecentAdvancesGrowth2025/fig_12_QGZQG6H2.png)
*   **来源**：[[../papers/RecentAdvancesGrowth2025]]
*   **关键特征**：THz-TDS 可直接触及多铁相变附近的自旋-晶格耦合模式。

### 2. NiI₂ 晶体的 X 射线与电子衍射
通过单晶/粉末 XRD 与 TEM 电子衍射确认 NiI₂ 的晶体结构、相纯度与取向。

![图：NiI₂ 单晶与粉末 XRD 图谱及 TEM 电子衍射花样](../../raw/figures/RecentAdvancesGrowth2025/fig_13_SXZWC8HQ.png)
*   **来源**：[[../papers/RecentAdvancesGrowth2025]]

### 3. 单层 Cr₂S₃ 的 AFM/XRD/XPS 联合表征
AFM 高度、XRD 摇摆曲线与 XPS 化学态联合验证外延单层 Cr₂S₃ 的厚度、取向与化学键合。

<table><thead><tr><th>表征手段</th><th>特征参数</th><th>结果</th></tr></thead><tbody><tr><td>AFM</td><td>高度轮廓</td><td>证实为单一单元层（1.8 nm）</td></tr><tr><td>XRD</td><td>θ 摇摆曲线</td><td>半高宽局限在 84.0°–85.5°</td></tr><tr><td>XPS</td><td>化学态</td><td>形成 Cr₂S₃ 及 Al-S 键（连接单层或基底）</td></tr></tbody></table>

*   **来源**：[[../papers/RecentAdvancesGrowth2025]]

---

## 🔧 器件制备流程与架构 (Device Fabrication & Architectures)

### 1. 少层 NiI₂ 霍尔棒的制备流程
通过薄片拾取-转移、hBN/石墨烯/NiI₂/hBN 堆叠、图形化与刻蚀等步骤制备 NiI₂ 霍尔棒器件。

![图：少层 NiI₂ 霍尔棒器件制备流程：拾取转移、堆叠、图形化与刻蚀](../../raw/figures/RecentAdvancesGrowth2025/fig_10_B29F4ZJU.png)
*   **来源**：[[../papers/RecentAdvancesGrowth2025]]
*   **关键特征**：全范德华拾取转移工艺避免界面污染与光刻损伤。

### 2. 反铁电 HZO 器件的工艺流程图
给出 ALD 沉积 HZO、电极淀积、光刻图形化与退火结晶的反铁电 HZO 基器件完整工艺流程。

![图：反铁电 HZO 基器件的制备工艺流程示意图](../../raw/figures/chenHafniumBasedFerroelectricPostMoore2026/fig_3_XHE7JUE9.png)
*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]]

### 3. 铪基铁电器件结构纵览
对比 MFS FeFET、MFMIS FeFET 与 Pt/SiO₂/HZO/TiN 铁电隧道结（FTJ）的层状堆叠结构。

![图：MFS FeFET、MFMIS FeFET 与 Pt/SiO₂/HZO/TiN FTJ 的器件结构对比](../../raw/figures/chenHafniumBasedFerroelectricPostMoore2026/fig_4_L3JZI8BN.png)
*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]]

### 4. 铪基铁电器件性能指标
对比 FeFET、FTJ 与 FeRAM 三类铪基铁电器件的材料堆叠、切换速度、保持时间、耐久度与功耗。

| Device type | Structure | FE material | Switching speed | Retention | Endurance | Power consumption |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| FeFET | MFS | HZO (10 nm) | N/A | > 10⁴ s | > 10⁶ cycles | pA/μm leakage |
| FTJ | Pt/SiO/HZO/TiN | HZO (2 nm) | 500 ps | > 10⁵ s | > 10⁷ cycles | 0.12 fJ/bit |
| FeRAM | TiN/HZO/TiN | HZO (4 nm) | N/A | > 10 years | > 10¹² cycles | 1.2 V low V |

*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]]

### 5. 多铁材料的应用分类
按非易失存储、自旋电子、传感器、制动器、能量收集、微波/RF 与相移器等类别归纳磁电耦合的应用方向。

<table><thead><tr><th>应用类别</th><th>依托效应</th><th>关键指标/器件</th></tr></thead><tbody><tr><td>非易失存储</td><td>铁电极化+自旋的磁电耦合</td><td>四态隧道效应、磁性切换</td></tr><tr><td>自旋电子</td><td>磁电耦合</td><td>自旋场效应晶体管、多铁隧道结</td></tr><tr><td>传感器</td><td>磁电效应</td><td>磁场感知探测器</td></tr><tr><td>制动器</td><td>压电/磁致伸缩</td><td>低功耗柔性致动</td></tr><tr><td>能量收集</td><td>磁电耦合</td><td>复合电压压电/磁致伸缩材料</td></tr><tr><td>微波/RF</td><td>磁电效应</td><td>可调滤波器、天线、FMR 调谐</td></tr><tr><td>相移器</td><td>电磁耦合</td><td>微波相控阵雷达、通讯</td></tr></tbody></table>

*   **来源**：[[../papers/RecentAdvancesGrowth2025]]
*   **另见**：同表的 markdown 版本收录于 [[electronic-devices#🔌 器件应用与分类 (Device Applications & Categories)|电子与突触器件]]。

### 6. 铁性材料的对称性分类
按照是否破坏空间反演与时间反演对称性，区分铁电、铁磁、铁弹、铁涡与铁谷五类铁性序。

<table><thead><tr><th>铁性类别</th><th>英文名称</th><th style="text-align:center">破坏空间反演对称性</th><th style="text-align:center">破坏时间反演对称性</th></tr></thead><tbody><tr><td>铁电性</td><td>Ferroelectricity (FE)</td><td style="text-align:center">✓</td><td style="text-align:center">✗</td></tr><tr><td>铁磁性</td><td>Ferromagnetism (FM)</td><td style="text-align:center">✗</td><td style="text-align:center">✓</td></tr><tr><td>铁弹性</td><td>Ferroelasticity</td><td style="text-align:center">✗</td><td style="text-align:center">✗</td></tr><tr><td>铁涡性</td><td>Ferrotoroidicity</td><td style="text-align:center">✓</td><td style="text-align:center">✓</td></tr><tr><td>铁谷性</td><td>Ferrovalley</td><td style="text-align:center">—</td><td style="text-align:center">—</td></tr></tbody></table>

*   **来源**：[[../papers/RecentAdvancesGrowth2025]]
*   **另见**：本表为五类铁性序完整版；三类（铁电/铁磁/铁弹）精简版收录于 [[vibrational-spectra#🧲 二维多铁材料体系综述 (2D Multiferroic Systems Overview)|振动能谱与声子谱]]。

---

## 📐 物理公式与模型 (Formulas & Models)

### 1. 插层能 (Intercalation Energy)
定义每个 A 原子嵌入 M₂X₄ 双层所对应的结合能，用于判断插层结构相对于分立反应物的热力学稳定性。

$$ E_{int} = \frac{E_{AM_2X_4} - E_{M_2X_4} - nE_A}{n} $$

*   **变量说明**：$E_{AM_2X_4}$、$E_{M_2X_4}$ 分别为插层化合物与裸 M₂X₄ 双层的总能量，$E_A$ 为孤立 A 原子能量，$n$ 为单胞中 A 原子数。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 2. 形成能 (Formation Energy)
以块体金属 A 为参考态计算形成能，负值表示插层化合物相对于块体反应物稳定。

$$ E_f = \frac{E_{AM_2X_4} - E_{M_2X_4} - nE_{A,\mathrm{bulk}}}{n} $$

*   **变量说明**：$E_{A,\mathrm{bulk}}$ 为块体 A 金属中每个原子的能量。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 3. 磁各向异性能 (MAE)
比较面内与面外磁化方向的总能量差，用于确定易磁化轴与垂直磁各向异性强度。

$$ \mathrm{MAE} = E_{\mathrm{in\text{-}plane}} - E_{\mathrm{out\text{-}of\text{-}plane}} $$

*   **变量说明**：MAE > 0 对应垂直（面外）易磁化，MAE < 0 对应面内易磁化。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 4. 海森堡磁耦合哈密顿量
包含各向同性交换 $J_{ij}$ 与单轴各向异性 $D$ 的自旋模型，用于蒙特卡洛模拟磁有序温度。

$$ H = -\sum_{i,j} J_{ij}\,\mathbf{S}_i \cdot \mathbf{S}_j - \sum_i D\,(\mathbf{S}_i^z)^2 $$

*   **变量说明**：$J_{ij}>0$ 为铁磁耦合，$D$ 为单轴各向异性参数，$\mathbf{S}_i$ 为格点 $i$ 的自旋矢量。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 5. 居里/奈尔温度估计
基于海森堡模型与蒙特卡洛模拟，由磁化率尖峰或比热反常确定 $k_B T_C$。

$$ k_B T_C \sim \text{MC 模拟中磁化率峰值对应的温度} $$

*   **变量说明**：$k_B$ 为玻尔兹曼常数，$T_C$ 为磁相变温度；实际值由 MC 模拟的有限尺寸标度给出。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 6. PFM 针尖下的挠曲电场
PFM 针尖在铁电薄膜中通过应变梯度诱导挠曲电场，是纳米尺度极化翻转的重要驱动力。

$$ E_f = \frac{f}{\varepsilon}\,\frac{\partial e}{\partial z} $$

*   **变量说明**：$f$ 为挠曲电系数，$\varepsilon$ 为介电常数，$\partial e/\partial z$ 为沿深度方向的应变梯度。
*   **来源**：[[../papers/Chen2016electrical]]

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/multiferroicity|多铁性]]、[[../concepts/ferroelectricity|铁电性]]、[[../concepts/sliding-ferroelectricity|滑移铁电性]]、[[../concepts/moire-superlattice|莫尔超晶格]]、[[../concepts/magnetoelectric-coupling|磁电耦合]]、[[../concepts/density-functional-theory|密度泛函理论 (DFT)]]、[[../concepts/high-throughput-screening|高通量筛选]]、[[../concepts/flexoelectricity|挠曲电效应]]、[[../concepts/ferroelectric-photovoltaic-effect|铁电光伏效应]]、[[../concepts/antiferroelectricity|反铁电性]]

**相关材料/实体**：[[../entities/In2Se3|In₂Se₃]]、[[../entities/NiI2|NiI₂]]、[[../entities/BiFeO3|BiFeO₃]]、[[../entities/HZO|HZO (铪锆氧)]]、[[../entities/h-BN|h-BN]]、[[../entities/graphene|石墨烯]]、[[../entities/TMDs|TMDs]]、[[../entities/WTe2|WTe₂]]、[[../entities/Cr2S3|Cr₂S₃]]
