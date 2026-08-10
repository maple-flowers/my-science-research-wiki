---
作者: [W Tang, E Sanville, G Henkelman]
中文标题: 一种无网格偏差的Bader分析算法
分类: [04_石墨烯/氧化石墨烯 (G/GO Sensors)]
影响因子: 0
---



# A grid-based Bader analysis algorithm without lattice bias
> [!info]+ <center>Metadata</center>
> 
> |<div style="width: 5em">Key</div>|Value|
> |--:|:--|
> |文献类型|journalArticle|
> |标题|A grid-based Bader analysis algorithm without lattice bias|
> |短标题|一种无网格偏差的Bader分析算法|
> |作者|[[W Tang]]、 [[E Sanville]]、 [[G Henkelman]]|
> |期刊名称|[[Journal of Physics：Condensed Matter]]|
> |DOI|[10.1088/0953-8984/21/8/084204](https://doi.org/10.1088/0953-8984/21/8/084204)|
> |存档位置|5479|
> |文库编目|0|
> |索书号|0|
> |版权||
> |分类|[[04_石墨烯/氧化石墨烯 (G/GO Sensors)]]|
> |条目链接|[My Library](zotero://select/library/items/7ZHQH9KS)|
> |PDF 附件|[PDF](zotero://open-pdf/library/items/UC378U86)|
> |关联文献||
> ^Metadata

> [!example]- <center>本文标签</center>
> 
> `$=dv.current().file.tags`

> [!quote]- <center>Abstract</center>
> 
> 

> [!tldr]- <center>隐藏信息</center>
> 
> itemType:: journalArticle
> title:: A grid-based Bader analysis algorithm without lattice bias
> shortTitle:: 一种无网格偏差的Bader分析算法
> creators:: [[W Tang]]、 [[E Sanville]]、 [[G Henkelman]]
> publicationTitle:: [[Journal of Physics：Condensed Matter]]
> journalAbbreviation:: J. Phys.：Condens. Matter
> volume:: 21
> issue:: 8
> pages:: 084204
> series:: 
> language:: en
> DOI:: [10.1088/0953-8984/21/8/084204](https://doi.org/10.1088/0953-8984/21/8/084204)
> ISSN:: 0953-8984, 1361-648X
> url:: [https://iopscience.iop.org/article/10.1088/0953-8984/21/8/084204](https://iopscience.iop.org/article/10.1088/0953-8984/21/8/084204)
> archive:: 
> archiveLocation:: 5479
> libraryCatalog:: 0
> callNumber:: 0
> JCRQ:: 
> rights:: 
> extra:: 🏷️ /unread、📒、🤖️
> collection:: [[04_石墨烯/氧化石墨烯 (G/GO Sensors)]]
> tags:: #unread #🤖️
> related:: 
> itemLink:: [My Library](zotero://select/library/items/7ZHQH9KS)
> pdfLink:: [PDF](zotero://open-pdf/library/items/UC378U86)
> qnkey:: tangGridbasedBaderAnalysis2009
> date:: 2009-02-25
> dateY:: 2009
> dateAdded:: 2026-05-06
> datetimeAdded:: 2026-05-06 05:07:54
> dateModified:: 2026-08-10
> datetimeModified:: 2026-08-10 23:15:07
> 
> abstract:: 


%--------------ω--------------%

## ✏️ 笔记区

> [!WARNING]+ <center>🐣 总结</center>
>
>🎯 一句话总结:: 

> [!inbox]- <center>📫 导入时间</center>
>
>⏰ importDate:: 2026-08-10
>⏰ importDateTime:: 2026-08-10 18:13:24

%--------------ω--------------%



## <span style="color: rgb(0, 174, 137);">❶ 🤖️ AI 文献解读</span>

> 🚀 [笔记回链](zotero://select/library/items/MTCYA5UA)

^KEYaiPapers

> <span class="AIReading">🤖 AI 解读，快人一步</span>
> 
> ## 一、引言
> 
> 这篇论文《**A grid-based Bader analysis algorithm without lattice bias**》讨论的是一种用于**Bader 电荷分析**（**Bader analysis**）的新算法改进方案。Bader 分析的核心目标，是把整个分子或晶体空间中的**电荷密度**（**charge density**）按拓扑结构划分成若干“原子体积”（**Bader volumes**），每个体积通常对应一个原子附近的电荷聚集区域。
> 
> ### 1.1 研究背景
> 
> 在**密度泛函理论**（**Density Functional Theory, DFT**）计算中，研究者往往可以获得非常精细的电子电荷密度分布。但如何把这些连续的电子分布解释为“每个原子贡献了多少电荷”，并不容易。传统如 Mulliken 分析依赖基组，结果常不够稳健；而 Bader 分析基于电荷密度本身，具有更好的物理可观测性和基组无关性。
> 
> ### 1.2 论文关注的核心问题
> 
> 已有的网格型 Bader 算法虽然高效、线性扩展，适合大规模平面波 DFT 计算，但存在一个关键缺陷：**晶格偏置**（**lattice bias**）。即由于算法强制梯度上升路径只能沿网格点跳转，导致最终 Bader 分界面倾向于沿网格方向排列，产生系统误差。
> 
> 这篇文章的核心贡献，就是提出一种新的**near-grid 方法**，既保留原始网格算法的高效率与线性复杂度，又消除了这种晶格偏置。
> 
> ### 1.3 论文价值
> 
> 这项工作的重要性在于：它不是单纯“提高一点数值精度”，而是解决了一个会影响 Bader 电荷、Bader 界面形状、乃至分子旋转不变性的根本算法问题。因此，这篇论文对从事第一性原理计算、材料模拟和电荷分析的研究者具有直接方法学价值。
> 
> * * *
> 
> ## 二、论文结构与逻辑概览
> 
> 这篇论文整体遵循非常清晰的方法论文结构：
> 
> ### 2.1 总体逻辑链
> 
> 可概括为：
> 
> **背景问题** → **旧算法有效但有偏差** → **提出新算法修正偏差** → **用模型体系和真实体系验证** → **证明新方法精度更高且仍保持线性扩展**
> 
> ### 2.2 各部分内容概览
> 
> ### 2.2.1 Introduction
> 
> 介绍 Bader 分析的物理意义、已有方法的优缺点，并指出旧版 on-grid 算法存在 lattice bias 问题。
> 
> ### 2.2.2 Methodology
> 
> 这是全文最核心部分。作者依次介绍：
> 
> 1.  原始 **on-grid method** 如何工作；
> 2.  其偏差是如何产生的；
> 3.  新提出的 **near-grid method** 如何通过“校正向量”逼近真实的非网格梯度上升路径。
> 
> ### 2.2.3 Results
> 
> 通过四类测试验证方法：
> 
> -   二维高斯模型；
> -   水分子；
> -   NaCl 晶体；
> -   分子取向旋转测试；
> -   以及计算耗时与网格点数的标度关系。
> 
> ### 2.2.4 Conclusion
> 
> 总结：新算法消除了晶格偏置，具有更好的收敛性与方向不变性，同时保留线性复杂度。
> 
> ### 2.3 核心论证链条
> 
> 作者的论证非常严密：
> 
> 1.  **旧方法的问题被明确定义**：轨迹只能走 26 个邻居方向，无法表示真实梯度流线；
> 2.  **新方法提出修正机制**：虽仍在网格点上“记录”轨迹，但同时保存偏离真实轨迹的修正向量；
> 3.  **二维模型可直观看到偏差消除**；
> 4.  **真实分子和晶体体系中定量证明精度提升**；
> 5.  **性能测试表明仍然线性扩展**。
> 
> _可设计为“算法演进流程图”：on-grid → 发现偏差 → near-grid 修正 → refinement 边界修正 → 输出 Bader 体积。_
> 
> * * *
> 
> ## 三、所有图表深度解析
> 
> * * *
> 
> ### 3.1 图1：on-grid 方法示意图
> 
> 图1展示旧算法如何在电荷密度网格上沿“最陡上升方向”逐点跳跃，直到到达某个局部电荷密度极大点。
> 
> #### 图意
> 
> -   图1(a)：显示多个起始点如何顺着梯度上升路径前进；
> -   图1(b)：所有最终到达同一极大值点的网格点，被归到同一个 Bader 体积。
> 
> #### 关键含义
> 
> 该图说明了旧算法高效性的根源：  
> 每个网格点只需被分析一次；一旦路径经过已归类点，就可以立即终止。
> 
> #### 单位/量纲
> 
> 该图为示意图，无明确数值单位；底层对象是电荷密度网格，通常电荷密度单位可理解为电子数密度，如 **e/Å³**，但图中未显式标注。
> 
> #### 深层意义
> 
> 图1强调：**效率来自“网格离散化”**，但这也埋下偏差根源，因为真实梯度线是连续的。
> 
> * * *
> 
> ### 3.2 图2：晶格偏置的产生机制
> 
> 这是全文最关键的概念图之一。
> 
> #### 图意
> 
> 真实分界面（红线）与真实梯度线是平滑曲线，但 on-grid 方法只能沿有限的网格方向前进，因此计算路径偏离真实轨迹，甚至跨越真实分界面，把本应属于另一 Bader 区域的点误分进去。
> 
> #### 核心问题
> 
> 旧算法只允许沿离散方向移动：
> 
> -   三维中 26 个邻点方向；
> -   二维中 8 个邻点方向。
> 
> 当真实梯度方向与这些离散方向不一致时，误差会逐步累积。
> 
> #### 深层结论
> 
> 这不是简单的“网格太粗”问题，而是**即使网格变细，这种方向偏置仍然存在**。因此它是算法结构性误差，不是单纯分辨率误差。
> 
> * * *
> 
> ### 3.3 图3：near-grid 方法中的校正向量
> 
> 这幅图解释了新算法的数学直觉。
> 
> #### 图意
> 
> 每一步理想上应沿真实梯度方向走一个连续位移 **r_grad**，但为了保留网格算法效率，程序实际仍跳到最近网格点，形成离散位移 **r_grid**。两者差值被记录为一个**校正向量** **r**。
> 
> 随着迭代：
> 
> -   校正向量不断累积；
> -   一旦某一方向分量超过半个网格间距，就执行一次修正跳步；
> -   这样真实轨迹始终不会偏离当前网格点太远。
> 
> #### 关键意义
> 
> 新方法并未完全抛弃网格，而是在“网格表示”与“连续真实轨迹”之间建立折中表示。
> 
> #### 单位/量纲
> 
> -   位移向量 **r_grad, r_grid, r** 的量纲是长度，通常是 **Å**。
> -   网格间距 **dx, dy, dz** 也以 **Å** 计。
> 
> #### 评价
> 
> 这是一个非常聪明的设计：在不牺牲线性扩展的前提下，局部补偿连续轨迹与离散轨迹之间的偏差。
> 
> * * *
> 
> ### 3.4 图4：二维三高斯模型测试
> 
> 该图是新旧算法对比最直观的证据。
> 
> #### 图意
> 
> 作者构造了一个二维电荷密度模型，真实分界面与网格呈小夹角。
> 
> -   (a) on-grid：分界面被错误地拉成沿网格方向的近垂直形状；
> -   (b) near-grid 初步结果：错误区域收缩到边界附近；
> -   (c) near-grid + 边界精修：几乎完全恢复真实分界面，只剩两个由于低分辨率造成的误分点。
> 
> #### 关键结论
> 
> near-grid 方法把误差从“大面积系统偏差”压缩成“边界局部误差”，再经 refinement 基本消除。
> 
> #### 单位/量纲
> 
> 二维示意图未标明绝对长度单位；本质是离散网格点的拓扑分配。
> 
> #### 方法学意义
> 
> 这张图是“概念验证（proof of concept）”图，证明新算法确实解决了作者声称要解决的问题。
> 
> * * *
> 
> ### 3.5 图5：水分子的 Bader 分界面对比
> 
> #### 图意
> 
> 左图为 on-grid，右图为 near-grid。
> 
> -   on-grid 分界面带有明显棱角，且方向和网格方向一致；
> -   near-grid 分界面更加平滑。
> 
> #### 关键含义
> 
> 在真实化学体系中，晶格偏置并非抽象问题，而会直接改变原子边界形状。
> 
> #### 单位/量纲
> 
> 图中主要展示几何边界，无直接数值坐标；分子空间尺度通常以 **Å** 计。
> 
> #### 补充说明
> 
> 作者指出 near-grid 图中的轻微波纹不是算法偏差，而是**有限网格分辨率**造成的离散效应。这一点非常重要，因为它区分了：
> 
> -   可通过细化网格消除的误差；
> -   与算法本身结构有关的系统误差。
> 
> * * *
> 
> ### 3.6 图6：NaCl 晶体中 Na 的 Bader 电荷收敛
> 
> 这是定量结果中最重要的一张图。
> 
> #### 图意
> 
> 横轴：网格密度/网格点数（文中实际对应 60³ 到 350³ 网格）  
> 纵轴：Na 离子的价电子电荷，单位 **e**（电子电荷数）
> 
> #### 结果
> 
> -   near-grid 方法平滑、单调地收敛到 **0.828 e**；
> -   on-grid 方法即使在细网格下仍偏离约 **0.01 e**。
> 
> #### 解释
> 
> 说明 near-grid 不仅“看上去更对”，而且具有更好的数值收敛性；on-grid 存在系统误差尾巴，难以靠简单加密网格完全消除。
> 
> #### 深层意义
> 
> 对于高精度电荷转移分析、缺陷电荷研究、离子性判断等问题，**0.01 e** 虽不算巨大，但在某些精细比较中已不可忽略。
> 
> * * *
> 
> ### 3.7 图7：H2O 分子旋转时 Bader 面变化
> 
> #### 图意
> 
> 同一个水分子，相对于电荷密度网格旋转 **45°** 后：
> 
> -   on-grid 得到的 Bader 面明显变化；
> -   near-grid 基本保持不变。
> 
> #### 关键结论
> 
> 正确的物理结果不应依赖“分子与计算网格的相对朝向”。  
> 因此，该图证明 on-grid 的偏差不仅影响几何边界，还破坏了算法应有的**旋转不变性**。
> 
> #### 单位/量纲
> 
> 旋转角度单位：**度（°）**
> 
> * * *
> 
> ### 3.8 图8：H2O 中 O 原子 Bader 电荷随旋转角变化
> 
> #### 图意
> 
> 横轴：分子旋转角度，单位 **°**  
> 纵轴：O 原子的 Bader 价电荷，单位 **e**
> 
> #### 结果
> 
> -   on-grid：不仅系统性低估氧的得电子量，而且随旋转变化约 **0.1 e**；
> -   near-grid：基本保持恒定。
> 
> #### 深层意义
> 
> 这是非常强的证据。因为如果电荷分析结果随着分子转动而变化，那么这种分析方法在物理解释上就存在严重隐患。
> 
> * * *
> 
> ### 3.9 图9：计算时间与网格点数的标度关系
> 
> #### 图意
> 
> 横轴：电荷密度网格点数  
> 纵轴：分析所需时间，单位 **s**
> 
> #### 结果
> 
> 时间与网格点数近似呈线性关系。作者给出斜率约为：
> 
> -   每 **100 万个网格点** 用时约 **11.5 s**
> -   机器为 **2.5 GHz G5 PowerPC**
> 
> #### 核心意义
> 
> near-grid 方法虽然引入校正向量与边界 refinement，但并未破坏原算法最重要的工程优势：**线性扩展**（**linear scaling**）。
> 
> * * *
> 
> ## 四、正文核心内容剖析
> 
> ## 4.1 Bader 分析的理论基础
> 
> Bader 分析属于**电子密度拓扑分析**。其基本思想是：
> 
> -   每个原子体积包含一个电荷密度极大点；
> -   不同体积之间由**零通量面**（**zero-flux surfaces**）分隔；
> -   这些分界面满足：电荷密度梯度在界面法向方向上的分量为零。
> 
> 换句话说，如果把电子密度想象成一片山地地形，那么每个 Bader 体积就是“流向同一个山峰的区域”。
> 
> _可设计为“地形流域类比图”：山脊线对应 Bader 分界面，山谷/坡面上的水流轨迹对应梯度线。_
> 
> * * *
> 
> ## 4.2 原始 on-grid 方法
> 
> 原始方法的思路是：
> 
> 1.  从一个未分配的网格点出发；
> 2.  计算它到 26 个邻居方向上的电荷密度梯度投影；
> 3.  选择投影最大的正方向，移动到该邻点；
> 4.  重复，直到达到局部极大点，或进入已分配路径；
> 5.  将整条路径上的点都归属于同一个 Bader 体积。
> 
> ### 4.2.1 优点
> 
> -   实现简单；
> -   每个点最多处理一次；
> -   对复杂键合拓扑稳健；
> -   计算量与网格点数成线性关系。
> 
> ### 4.2.2 缺点
> 
> 其致命问题在于：路径被限制在离散网格方向上。  
> 真实梯度是连续方向，但算法只能在有限候选方向中选一个“最接近”的方向，因此长期累计会产生方向性偏移。
> 
> * * *
> 
> ## 4.3 晶格偏置为何不会因细网格自动消失
> 
> 这是文中一个很重要的思想点。
> 
> 很多初学者可能会以为：“网格足够细，误差自然就没了。”  
> 作者明确指出：**不对**。
> 
> 原因是：
> 
> -   误差不是因为梯度采样太粗；
> -   而是因为轨迹的“可走方向集合”始终是离散的；
> -   所以哪怕步长很小，只要真实方向不与格子方向对齐，误差就会不断累积。
> 
> 这本质上类似“曼哈顿路径逼近欧氏直线”时产生的方向锯齿误差。
> 
> * * *
> 
> ## 4.4 near-grid 方法的核心思想
> 
> 新算法的巧妙之处，是在“继续使用网格点”与“逼近真实连续轨迹”之间找到折中。
> 
> ### 4.4.1 梯度计算
> 
> 作者改用中心差分，只用最近的 6 个邻居来计算 x、y、z 三方向梯度分量：
> 
> -   ∇ρx
> -   ∇ρy
> -   ∇ρz
> 
> 然后形成连续梯度方向向量。
> 
> ### 4.4.2 连续步长与离散跳步
> 
> 理想上应该沿连续梯度向量走一步 **r_grad**。  
> 但为了高效实现，算法不在连续空间积分，而是：
> 
> -   找到对应的最近网格跳步 **r_grid**；
> -   把两者差异记为校正向量 **r**。
> 
> ### 4.4.3 校正向量累积
> 
> 随着多次跳步：
> 
> -   若某个方向上的偏差累积超过半个网格间距；
> -   就在该方向额外修正一步；
> -   然后重新更新校正向量。
> 
> 这使得离散轨迹始终围绕真实轨迹附近波动，而不会像旧方法那样不断单侧漂移。
> 
> ### 4.4.4 路径终止条件
> 
> 新方法中路径终止有两类：
> 
> 1.  到达电荷密度极大值；
> 2.  到达某个点，并且该点及其所有邻居都已被分到同一 Bader 区域。
> 
> 后者保证了算法不会无谓重复搜索。
> 
> ### 4.4.5 边界精修（refinement）
> 
> 由于 near-grid 仍在网格上表示轨迹，边界附近个别点可能仍有歧义。  
> 因此作者增加最后一步：
> 
> -   找到所有临近 Bader 分界面的边界点；
> -   从这些点重新追踪 ascent trajectory；
> -   只修正初始边界点归属。
> 
> 这一步把误差进一步限制并消除。
> 
> * * *
> 
> ## 4.5 实验验证的逻辑
> 
> 作者选取了非常合理的测试层次：
> 
> ### 4.5.1 人工二维模型
> 
> 优点是分界面“真值”可控，适合直观看偏差。
> 
> ### 4.5.2 水分子
> 
> 是常见小分子，便于展示分界面几何形状变化。
> 
> ### 4.5.3 NaCl 晶体
> 
> 是规则离子晶体，适合观察电荷积分收敛性。
> 
> ### 4.5.4 分子旋转测试
> 
> 这是最强的“物理一致性检验”之一：结果不应依赖取向。
> 
> ### 4.5.5 时间复杂度测试
> 
> 说明新算法不仅更准，而且仍然能处理大规模平面波计算输出。
> 
> * * *
> 
> ## 五、结论与贡献
> 
> ### 5.1 核心结论
> 
> 本文提出的 **near-grid Bader 分析算法**：
> 
> -   消除了旧 on-grid 方法的**晶格偏置**；
> -   改善了 Bader 分界面的几何真实性；
> -   提高了 Bader 电荷的数值收敛性；
> -   减少了对分子/晶体相对于网格取向的依赖；
> -   同时保留了**线性时间复杂度**与高鲁棒性。
> 
> ### 5.2 主要贡献
> 
> 可以概括为四点：
> 
> 1.  **方法学贡献**：提出一种无 lattice bias 的网格型 Bader 算法；
> 2.  **数值分析贡献**：证明旧算法误差是结构性而非单纯分辨率问题；
> 3.  **工程实现贡献**：新算法仍适用于大规模平面波 DFT 电荷密度网格；
> 4.  **应用价值贡献**：提升了分子与固体体系中 Bader 电荷分析的可信度。
> 
> * * *
> 
> ## 六、未来发展方向展望
> 
> 虽然本文已显著改进了 Bader 分析，但仍有若干潜在拓展方向：
> 
> ### 6.1 非正交晶格的更系统讨论
> 
> 正文中作者提到推广到**非正交晶格**（non-orthogonal lattices）并不复杂，且已在软件实现，但论文未展开推导细节。后续可专门研究该推广的数值性质。
> 
> ### 6.2 边界 refinement 的进一步优化
> 
> 当前 refinement 仍需要单独检查边界点。未来可探索更自动化、更局部自适应的边界修正策略。
> 
> ### 6.3 与其他分区方法系统比较
> 
> 例如与 Hirshfeld、DDEC、Mulliken 等方法比较：
> 
> -   数值稳定性；
> -   与实验可观测量的关联；
> -   对不同键型体系的敏感性。
> 
> ### 6.4 极端复杂拓扑体系
> 
> 例如：
> 
> -   非核吸引子（non-nuclear attractors）体系；
> -   强极化或强缺陷体系；
> -   表面/界面体系；
> -   低维材料。
> 
> ### 6.5 并行化与超大规模计算
> 
> 由于该算法线性扩展，进一步并行化后可能更适用于数亿网格点级别的高通量分析。
> 
> * * *
> 
> ## 七、学术思考与批判性分析
> 
> ### 7.1 深度问题1：near-grid 方法是否已经“完全连续”？
> 
> 没有。它本质上仍是**网格表示算法**，只是通过校正向量逼近真实连续轨迹。因此其准确性仍受网格分辨率影响。作者也坦承边界处仍需 refinement，且有限分辨率下仍可能误分个别点。
> 
> ### 7.2 深度问题2：作者是否严格证明了 near-grid 一定收敛到真实 Bader 分区？
> 
> 从论文表达看，作者主要给出数值证据和构造直觉，而不是严格数学收敛证明。因此它更像一个“强经验支持的数值算法”，而非完备的数学定理。
> 
> ### 7.3 深度问题3：算法精度主要受什么限制？
> 
> 至少有三类限制：
> 
> 1.  电荷密度网格本身的分辨率；
> 2.  梯度的有限差分近似误差；
> 3.  边界点在离散网格上的归属歧义。
> 
> 因此 near-grid 解决的是**方向偏置**，但不是所有数值误差来源。
> 
> ### 7.4 深度问题4：为什么旋转不变性测试如此关键？
> 
> 因为物理电荷密度的性质不应依赖坐标系选取。若同一分子旋转后 Bader 电荷变化明显，说明算法在测量“网格与分子相对关系”，而不是仅测量体系本身。这类测试比单纯比较一个数值更能揭示算法偏差本质。
> 
> ### 7.5 深度问题5：旧方法误差约 0.01 e 是否真的重要？
> 
> 取决于应用场景：
> 
> -   对粗略离子性判断，也许影响不大；
> -   对精细比较不同缺陷态、电荷转移趋势、催化吸附电荷重排等问题，0.01–0.1 e 可能已足够影响结论。  
>     因此作者主张应优先使用 near-grid 方法，是合理的。
> 
> * * *
> 
> ## 八、用户问题预测与解答
> 
> ### 8.1 什么是 Bader 体积？为什么它能代表“原子”？
> 
> Bader 体积是由电荷密度梯度流线定义的空间区域：所有最终流向同一个电荷密度极大值的点都属于同一体积。因为电子密度通常在原子核附近达到局部最大，所以这些体积常可对应原子贡献区域。它不是凭经验切原子半径，而是由电子密度拓扑自然给出。
> 
> ### 8.2 什么叫零通量面？
> 
> 零通量面是 Bader 体积之间的分界面。在这个面上，电荷密度梯度在法向上的分量为零，即电子密度流不会“穿过”这道边界。直观上，它像地形中的“分水岭”。
> 
> ### 8.3 为什么旧算法会出现“晶格偏置”？
> 
> 因为旧算法的上升路径只能走有限个网格方向。真实梯度方向往往不正好沿这些离散方向，因此路径会被迫走“折线”，久而久之 Bader 分界面就会被网格方向“拉直”或“切平”。
> 
> ### 8.4 near-grid 方法和完全 off-grid 方法有什么区别？
> 
> 完全 off-grid 方法通常直接在连续空间中积分轨迹，更贴近真实路径，但可能更复杂。near-grid 方法则保留网格跳步，只额外记录一个校正向量来补偿偏差。它是精度和效率之间的折中，优势在于仍保持线性扩展和工程可实施性。
> 
> ### 8.5 为什么边界点还要 refinement？
> 
> 因为即便 near-grid 更接近真实轨迹，边界附近的离散点仍可能因为“离分界面太近”而有归属歧义。refinement 的目标就是对这些少量边界敏感点做最后修正，把误差控制在极小范围。
> 
> ### 8.6 这篇论文对做 DFT 的人最实用的启示是什么？
> 
> 如果你用平面波 DFT 做 Bader 电荷分析，不应只关心“算没算 Bader 电荷”，还应关心算法本身是否存在方向偏置。本文说明：同样的电荷密度数据，不同的 Bader 算法实现会导致不同结果，尤其在边界形状、电荷收敛和取向不变性方面差异明显。
> 
> ### 8.7 这篇文章更偏理论还是偏工程？
> 
> 两者兼有，但整体更偏**计算方法学/数值算法工程**。它不提出新的化学理论，而是改进一个重要的电子结构后处理算法，使其更可靠地服务于理论化学和计算材料研究。
> 
> * * *
> 
> ## 九、专区：便于 Obsidian Dataview 插件调用
> 
> 领域基础知识:: Bader 分析是一种基于电子电荷密度拓扑的空间分区方法，通过电荷密度梯度流线将体系划分为若干 Bader 体积，各体积之间由零通量面分隔，常用于从 DFT 电荷密度中提取原子电荷与原子体积信息。
> 
> 研究背景:: 平面波 DFT 和大规模凝聚态计算通常输出离散电荷密度网格，因此需要高效、鲁棒、适用于复杂键合拓扑的网格型 Bader 分析算法；旧的 on-grid 方法虽然线性扩展，但会产生沿网格方向的晶格偏置。
> 
> 作者的问题意识:: 作者关注的核心问题是：已有高效网格型 Bader 算法由于将梯度上升轨迹约束在网格点之间，导致 Bader 分界面人为沿晶格方向排列，进而引入系统误差、影响电荷收敛并破坏取向不变性。
> 
> 主要研究对象:: 研究对象是基于正交电荷密度网格的 Bader 体积分区算法，重点是改进梯度上升路径的离散表示方式；验证体系包括二维三高斯模型、水分子和 NaCl 晶体。
> 
> 主要研究方法:: 作者先分析旧 on-grid 方法的误差来源，再提出 near-grid 方法：用中心差分计算局部梯度，沿连续梯度方向定义理想步长，同时仍在网格点间跳转，并通过累积校正向量逼近真实 off-lattice 轨迹，最后对边界点做 refinement 修正。
> 
> 研究意义:: 该研究提升了 Bader 电荷分析在平面波 DFT 和大规模材料计算中的可信度，使算法既保留线性时间复杂度和鲁棒性，又消除了因网格方向造成的结构性误差。
> 
> 研究结论:: near-grid 算法有效消除了 on-grid 方法中的 lattice bias，使 Bader 分界面更平滑、Bader 电荷随网格细化单调收敛、对分子相对于网格的取向不敏感，并保持与网格点数线性相关的计算复杂度。
> 
> 对领域的贡献:: 本文为网格型 Bader 电荷分析提供了一个兼顾精度与效率的改进方案，明确区分了分辨率误差与算法结构性偏差，为后续平面波 DFT 后处理和 Bader 软件实现奠定了更稳健的方法基础。
> 
> 未来研究方向提及:: 文中简要提到该方法可自然推广到非正交晶格和不同边界条件，且相关实现已进入软件；同时边界 refinement 仍是算法最后一步，表明边界处理仍有可优化空间。
> 
> 未来研究方向思考:: 后续可进一步开展 near-grid 方法在非正交晶格、低维材料、表面界面、非核吸引子体系中的系统测试，并研究更严格的收敛性证明、边界自适应修正策略以及并行化实现。
> 
> 🚀 [笔记回链](zotero://select/library/items/MTCYA5UA)
> 
> * * *
> 
> `GPT 自定 ②`  `gpt-5.4`  _由批量 AI 解读自动生成于 2026/5/6 05:31:07_
> 
> 🏷️ #🤖️/AI文献解读 🏷️ #🤖️/AI文献阅读

^KEY85C16891

## <span style="color: rgb(0, 174, 137);">❷ 🤖️ 论文双语转写📌</span>

> 🚀 [笔记回链](zotero://select/library/items/PHBX3RGT)

^KEYaiPaper0

> <span class="AIReading">🤖 AI 解读，快人一步</span>
> 
> > 我们被要求将给定的PDF文本转换为结构化的Markdown，包含双语转换和术语解释。需要识别结构元素：标题、段落、列表、代码块、引用、表格等。按照给定的处理流程和输出规范进行。
> > 
> > 首先，分析文本结构和内容。原文是一篇学术论文，标题 "A grid-based Bader analysis algorithm without lattice bias"，包含摘要、章节等。我们需要提取结构，为每个单元分配ID，然后提供英文原文、中文翻译和术语解释（仅首次出现的核心术语）。输出格式严格遵循CommonMark，标题层级由#至######，列表保留原始符号，代码块使用三反引号，引用块保留>。
> > 
> > 根据文本，结构如下：
> > 
> > -   顶部有一些下载信息，可能被认为是元数据，但我们需要保留。可能属于引用块？实际上，开头有 "This article has been downloaded from IOPscience..." 等，这是一段信息。以及 "View the table of contents..." 等，可能是页眉/页脚。但根据任务，我们需要提取所有文本。可能将这部分作为段落处理。
> > -   然后是标题、作者、摘要等。
> > -   正文：1. Introduction, 2. Methodology, 2.1 On-grid method, 2.2 Lattice bias..., 2.3 Near-grid method..., 3. Results, 3.1 Two-dimensional model, 3.2 A water molecule, 3.3 Ionic charge..., 3.4 Variation of charge..., 3.5 Scaling of computational effort, 4. Concluding remarks, Acknowledgments, References。
> > 
> > 我们需要将整个文本分割成逻辑单元，每个单元包含英文原文和中文翻译，术语解释只在首次出现时添加。对于标题，格式为：
> > 
> > # [英文标题]
> > 
> > [中文标题] **Term**: 术语解释
> > 
> > 对于段落，直接给出英文原文，然后中文翻译。如果有术语解释，另起一行。代码块和引用类似。
> > 
> > 我们需要识别出所有术语，并标注首次出现。可能的术语包括：Bader analysis, Bader volumes, charge density, steepest ascent paths, density functional theory (DFT), zero-flux surfaces, Mulliken population analysis, on-grid method, near-grid method, lattice bias, etc.
> > 
> > 由于输出要求仅输出Markdown文本，无额外说明，我们将直接生成Markdown。
> > 
> > 现在，开始逐段解析原文本，并构建输出。注意保留原文顺序和层级。
> > 
> > 首先，顶部下载信息段落： "This article has been downloaded from IOPscience. Please scroll down to see the full text article. 2009 J. Phys.: Condens. Matter 21 084204 (http://iopscience.iop.org/0953-8984/21/8/084204) Download details: IP Address: 171.67.34.69 The article was downloaded on 24/07/2012 at 21:01 Please note that terms and conditions apply. View the table of contents for this issue, or go to the journal homepage for more Home Search Collections Journals About Contact us My IOPscience"
> > 
> > 这看起来像是页眉/页脚信息，但我们需要保留。可能作为一个段落。没有术语需要解释。
> > 
> > 然后有一行 "IOP PUBLISHING JOURNAL OF PHYSICS: CONDENSED MATTER" 等，然后是期刊标题、论文标题、作者、摘要等。我们根据排版识别标题。
> > 
> > 论文标题: "A grid-based Bader analysis algorithm without lattice bias" 这是文章标题，可能是一级标题。但前面还有期刊名等。我们按顺序处理。
> > 
> > 从"IOP PUBLISHING JOURNAL OF PHYSICS: CONDENSED MATTER" 开始，可能是一个段落，然后是 "J. Phys.: Condens. Matter 21 (2009) 084204 (7pp) doi:10.1088/0953-8984/21/8/084204"，然后是标题 "A grid-based Bader analysis algorithm without lattice bias"，然后是作者 "W Tang, E Sanville and G Henkelman"，然后是单位，然后是邮箱，然后是 "Received... Published..."，然后是 "Abstract" 段落。
> > 
> > 我们需要决定标题层级。原文中，论文标题显然是一级标题。摘要的 "Abstract" 可能是一个加粗的标签，但我们可以将其视为一个段落，或者作为小标题？根据输出规范，标题层级对应 # 至 ######。通常，论文标题用 #，章节标题用 ##，子节用 ### 等。这里 "1. Introduction" 是 ##，"2. Methodology" 是 ##，"2.1 On-grid method" 是 ###，"3. Results" 是 ## 等。摘要可能没有编号，我们可以将其视为一个段落，但 "Abstract" 可以作为一个加粗的标签，或者作为一个小标题。任务要求映射标题层级，基于字体变化和编号模式。摘要没有编号，但可能是一个标题。我们将其视为一个特殊段落，或者使用 **Abstract** 加粗。但输出规范要求标题使用 # 至 ######。我们可以将 "Abstract" 当作一个无编号的标题，用 ## 或 ###？根据常见做法，摘要通常不编号，但可以视为一个部分。为了保持结构，我们将其作为二级标题，因为没有编号，但它是论文的一个标准部分。或者我们将其作为段落，但 "Abstract" 标签加粗。由于输出规范中说“标题：英文标题，中文标题”，可能任何标题样式的文本都应使用 # 标记。谨慎起见，我们检查原文：在摘要前有 "Abstract" 一词，单独一行，可能加粗。我们将 "Abstract" 视为一个标题，使用 ##。
> > 
> > 类似地，致谢 "Acknowledgments" 和参考文献 "References" 也是标题。
> > 
> > 现在，逐一单元处理。我们将为每个单元分配一个ID，但输出中不需要写出ID，只需要按顺序输出单元。根据流程，每个单元包含英文原文，中文翻译，术语解释。我们将遵循这一模式。
> > 
> > 由于文本是连续的，我们需要将其分割成单元。根据空行或逻辑断点。原PDF文本中，段落之间有空行。我们按空行分割。
> > 
> > 我们将手动解析整个文本，构建Markdown。
> > 
> > 首先，开头部分： "IOP PUBLISHING JOURNAL OF PHYSICS: CONDENSED MATTER J. Phys.: Condens. Matter 21 (2009) 084204 (7pp) doi:10.1088/0953-8984/21/8/084204"
> > 
> > 这是一个段落，可能是期刊信息。然后空行，论文标题 "A grid-based Bader analysis algorithm without lattice bias"，然后空行，作者 "W Tang, E Sanville and G Henkelman"，然后空行，单位 "1 Department of Chemistry ... 2 Department of Mathematical Sciences ..."，然后空行，邮箱 "E-mail: henkelman@mail.utexas.edu"，然后空行，"Received 19 March 2008, in final form 6 June 2008 Published 30 January 2009 Online at stacks.iop.org/JPhysCM/21/084204"，然后空行，"Abstract" 标题，然后摘要段落。
> > 
> > 然后 "1. Introduction" 标题，等等。
> > 
> > 我们按照这个顺序输出。
> > 
> > 注意：对于术语解释，我们需要在首次出现时标注。例如，在标题中首次出现 "Bader analysis"，我们可以在标题后添加术语解释？标题本身可能包含术语。根据输出格式，标题的英文原文下方是中文标题，然后是术语解释。所以我们可以为标题中的术语在标题单元后添加解释。但解释仅标注首次出现的核心术语。如果标题中首次出现，就在标题单元解释。如果术语在摘要中首次出现，就在摘要单元解释。
> > 
> > 我们将识别核心术语：
> > 
> > -   Bader analysis: Bader分析
> > -   Bader volumes: Bader体积
> > -   charge density: 电荷密度
> > -   steepest ascent paths: 最陡上升路径
> > -   density functional theory (DFT): 密度泛函理论
> > -   zero-flux surfaces: 零通量面
> > -   Mulliken population analysis: Mulliken布居分析
> > -   on-grid method: 在格点方法
> > -   near-grid method: 近格点方法
> > -   lattice bias: 格点偏差
> > -   grid-based: 基于格点的
> > -   pseudopotentials: 赝势
> > -   projector augmented wave (PAW): 投影缀加波
> > -   etc.
> > 
> > 我们将在翻译中体现术语，并在首次出现时给出解释。
> > 
> > 现在，开始构建输出。我们将逐单元编写。
> > 
> > 注意：原文本中有一些图表引用，如 "Figure 1", "Figure 2" 等，我们需要保留，并在翻译中处理。图表标题可能作为段落，但原文中图表标题是 "Figure 1. An illustration ..."，可能作为段落。
> > 
> > 另外，参考文献列表是编号列表，应保留为有序列表。
> > 
> > 还有，公式（equation）和引用，我们将保留原样。
> > 
> > 现在，开始编写Markdown。
> 
> ```
> # A grid-based Bader analysis algorithm without lattice bias
> 一种无格点偏差的基于格点的Bader分析算法
> **Bader analysis**: Bader分析，一种将电荷密度划分为原子体积的方法。
> 
> IOP PUBLISHING JOURNAL OF PHYSICS: CONDENSED MATTER
> J. Phys.: Condens. Matter 21 (2009) 084204 (7pp) doi:10.1088/0953-8984/21/8/084204
> IOP出版 物理学报：凝聚态物质
> J. Phys.: Condens. Matter 21 (2009) 084204 (7pp) doi:10.1088/0953-8984/21/8/084204
> 
> A grid-based Bader analysis algorithm without lattice bias
> 一种无格点偏差的基于格点的Bader分析算法
> 
> W Tang, E Sanville and G Henkelman
> W Tang, E Sanville, G Henkelman
> 
> 1 Department of Chemistry and Biochemistry, The University of Texas at Austin, Austin, TX 78712-0165, USA 2 Department of Mathematical Sciences, Loughborough University, Loughborough LE11 3TU, UK
> 1 美国德克萨斯大学奥斯汀分校化学与生物化学系，奥斯汀，TX 78712-0165，美国 2 英国拉夫堡大学数学科学系，拉夫堡 LE11 3TU，英国
> 
> E-mail: henkelman@mail.utexas.edu
> 电子邮箱：henkelman@mail.utexas.edu
> 
> Received 19 March 2008, in final form 6 June 2008 Published 30 January 2009 Online at stacks.iop.org/JPhysCM/21/084204
> 2008年3月19日收到，最终版2008年6月6日 2009年1月30日出版 在线发表于 stacks.iop.org/JPhysCM/21/084204
> 
> ## Abstract
> 摘要
> 
> A computational method for partitioning a charge density grid into Bader volumes is presented which is efficient, robust, and scales linearly with the number of grid points. The partitioning algorithm follows the steepest ascent paths along the charge density gradient from grid point to grid point until a charge density maximum is reached. In this paper, we describe how accurate off-lattice ascent paths can be represented with respect to the grid points. This improvement maintains the efficient linear scaling of an earlier version of the algorithm, and eliminates a tendency for the Bader surfaces to be aligned along the grid directions. As the algorithm assigns grid points to charge density maxima, subsequent paths are terminated when they reach previously assigned grid points. It is this grid-based approach which gives the algorithm its efficiency, and allows for the analysis of the large grids generated from plane-wave-based density functional theory calculations.
> **Bader volumes**: Bader体积，根据电荷密度划分的原子空间区域。
> **charge density**: 电荷密度，描述电子在空间中分布的函数。
> **linear scaling**: 线性缩放，计算时间与系统大小成正比。
> **steepest ascent paths**: 最陡上升路径，沿着电荷密度梯度方向到达最大值的轨迹。
> **charge density gradient**: 电荷密度梯度，电荷密度变化最快的方向。
> **charge density maximum**: 电荷密度最大值，通常位于原子中心。
> **off-lattice**: 离格点，不限制在格点上的轨迹。
> **Bader surfaces**: Bader表面，分隔不同Bader体积的零通量面。
> **density functional theory (DFT)**: 密度泛函理论，一种基于电子密度计算电子结构的第一性原理方法。
> 
> 本文提出了一种将电荷密度格点划分为Bader体积的计算方法，该方法高效、鲁棒，且计算时间与格点数量线性相关。划分算法沿着电荷密度梯度从格点到格点追踪最陡上升路径，直到达到电荷密度最大值。在本文中，我们描述了如何相对于格点表示精确的离格点上升路径。这一改进保持了算法早期版本的线性缩放效率，并消除了Bader表面沿格点方向对齐的趋势。由于算法将格点分配给电荷密度最大值，后续路径在遇到已分配的格点时终止。正是这种基于格点的方法赋予了算法高效性，并使其能够分析从平面波基组密度泛函理论计算产生的大型格点。
> 
> (Some figures in this article are in colour only in the electronic version)
> （本文部分图表仅在电子版中为彩色）
> 
> ## 1. Introduction
> 引言
> 
> First principles methods, and especially density functional theory (DFT), are commonly used to calculate the many-body electronic interactions between atoms in molecules and in the solid state. Accurately describing these complex interactions is difficult, but it can also be challenging to rationalize the calculated energetics. One powerful technique for doing this is to decompose properties of the molecule or material into contributions from the individual atoms. Bader suggested an elegant way to do this partitioning [1]. His idea was to use the charge density to divide space within molecular systems into atomic (Bader) volumes. Each Bader volume contains a single charge density maximum, and is separated from other volumes by surfaces on which the charge density is a minimum normal to the surface. Typically, there is one charge density maximum at each atomic center and one Bader volume for each atom, but this is not required; there are cases in which Bader volumes do not contain a nucleus [2]. The dividing surfaces (also called zero-flux surfaces) separating these volumes lie in the bonding regions between atoms. This Bader partitioning has an advantage over other partitioning schemes (e.g. Mulliken population analysis) in that it is based upon the charge density, which is an observable quantity that can be measured experimentally or calculated. Furthermore, in a converged electronic structure calculation, the charge density is insensitive to the basis set used. In this regard, the Bader analysis is more robust than wavefunction-based population methods [3–5]. There are several different approaches to calculating Bader volumes. Early algorithms were implemented for quantum chemistry calculations of small molecules, in which the gradient of the charge density can be calculated from derivatives of an analytic wavefunction [1, 6, 7]. These methods first find stationary points in the charge density and then follow trajectories along the density gradient from these points to map out their connectivity and the zero-flux dividing surfaces. With the dividing surfaces represented in this way, the charge in each Bader volume can be integrated radially from the charge density maximum to the surface. While this approach works for small molecules, a high density of descent trajectories is needed to accurately represent the surface away from the critical points, and the method has been criticized as being computationally expensive for large systems [8, 5].
> **zero-flux surfaces**: 零通量面，电荷密度梯度垂直于表面的通量为零的分界面。
> **Mulliken population analysis**: Mulliken布居分析，一种基于波函数的电荷分配方法。
> 
> 第一性原理方法，尤其是密度泛函理论（DFT），通常用于计算分子和固态中原子间的多体电子相互作用。准确描述这些复杂相互作用是困难的，但合理化计算得到的能量学同样具有挑战性。一种强大的技术是将分子或材料的性质分解为各个原子的贡献。Bader提出了一种优雅的划分方法[1]。他的想法是利用电荷密度将分子体系内的空间划分为原子（Bader）体积。每个Bader体积包含一个电荷密度最大值，并被电荷密度在表面法向上为最小值的表面与其他体积分隔。通常，每个原子中心有一个电荷密度最大值，每个原子对应一个Bader体积，但这并非必需；存在Bader体积不包含原子核的情况[2]。分隔这些体积的分界面（也称为零通量面）位于原子间的键合区域。与其他划分方案（如Mulliken布居分析）相比，这种Bader划分的优势在于它基于电荷密度，而电荷密度是可观测量，可以通过实验测量或计算得到。此外，在收敛的电子结构计算中，电荷密度对所用基组不敏感。在这方面，Bader分析比基于波函数的布居方法更稳健[3–5]。计算Bader体积有几种不同的方法。早期算法针对小分子的量子化学计算实现，其中电荷密度梯度可以从解析波函数的导数计算得到[1, 6, 7]。这些方法首先找到电荷密度中的驻点，然后从这些点沿着密度梯度追踪轨迹，以绘制出它们的连通性和零通量分界面。通过这种方式表示分界面后，每个Bader体积内的电荷可以从电荷密度最大值径向积分到表面。虽然这种方法适用于小分子，但需要高密度的下降轨迹才能准确表示远离临界点的表面，并且该方法被批评为对于大体系计算代价过高[8, 5]。
> 
> It was also found to fail for complex bonding geometries and when the radial integration rays have multiple intersection points with the dividing surface [9–11]. Several improvements to this original approach have been proposed. Popelier developed a method to more accurately integrate the charge density within each Bader volume using a Fourier–Chebyshev fit [12] and a bisection method to analytically represent the dividing surfaces [13]. Other approaches suggested by Popelier include the use of the divergence theorem to replace the three-dimensional integration over the Bader volumes into a two-dimensional integral over the dividing surfaces [8], and the use of a tree search to treat complex bonding topologies between critical points [14, 15]. Most current implementations of Bader's analysis are based upon a grid of charge density values [6, 16, 17, 11, 18, 19]. This is particularly important for plane-wave-based DFT calculations, because it allows for the analysis of condensed phase systems with many atoms. The algorithm described in this work is an improvement upon such a grid-based method [18]. In that original work, an algorithm was introduced in which ascent trajectories along the charge density were followed between grid points to determine the Bader volumes. The constraint of ascent trajectories to the grid means that each point need be considered only once. The method is highly efficient, scales linearly with system size, and is robust to complex bonding topology found in condensed systems. Recently, however, Sanville et al showed that this algorithm introduces a bias, causing the Bader surfaces to artificially follow the orientation of the lattice [19]. A modified algorithm was implemented by these authors in which ascent trajectories along interpolated gradients of the charge density were not constrained to the grid. This algorithm removes the bias and retains the linear scaling of the original method. Here, we present a modified version of our original algorithm which also removes the lattice bias in a somewhat different way. Trajectories are constrained to grid points at which charge density gradients are evaluated, and a correction vector is calculated which points from the nearest grid point to the unbiased (off-lattice) trajectory. In this way, lattice bias is removed and we have an algorithm which retains the efficiency, linear scaling, and robustness of the original grid-based method.
> **lattice bias**: 格点偏差，由于上升轨迹被限制在格点上而导致的分界面沿格点方向对齐的系统误差。
> 
> 研究还发现，对于复杂键合几何结构以及当径向积分射线与分界面有多个交点时，该方法会失效[9–11]。对原始方法已提出了若干改进。Popelier开发了一种使用Fourier–Chebyshev拟合更精确地积分每个Bader体积内电荷密度的方法[12]，以及一种使用二分法解析表示分界面的方法[13]。Popelier建议的其他方法包括使用散度定理将Bader体积上的三维积分替换为分界面上的二维积分[8]，以及使用树搜索处理临界点之间复杂键合拓扑结构[14, 15]。目前大多数Bader分析实现都基于电荷密度值的格点[6, 16, 17, 11, 18, 19]。这对于基于平面波基组的DFT计算尤为重要，因为它允许分析包含许多原子的凝聚相体系。本文描述的算法是对这种基于格点的方法的改进[18]。在原始工作中，引入了一种算法，其中在格点之间追踪沿电荷密度的上升轨迹以确定Bader体积。上升轨迹被限制在格点上意味着每个点只需考虑一次。该方法效率极高，随系统大小线性缩放，并且对凝聚体系中发现的复杂键合拓扑结构具有鲁棒性。然而，最近Sanville等人表明，该算法引入了偏差，导致Bader表面人为地遵循格点方向[19]。这些作者实现了一种修正算法，其中沿插值电荷密度梯度的上升轨迹不受格点约束。该算法消除了偏差，并保留了原始方法的线性缩放。在这里，我们提出了原始算法的一个修正版本，以略微不同的方式消除格点偏差。轨迹被限制在计算电荷密度梯度的格点上，同时计算一个修正矢量，该矢量从最近的格点指向无偏差（离格点）轨迹。通过这种方式，格点偏差被消除，我们得到了一个保留原始基于格点方法效率、线性缩放和鲁棒性的算法。
> 
> ## 2. Methodology
> 方法
> 
> This method for finding Bader volumes without lattice bias is an improvement to an earlier grid-based method [18]. We first describe the original ‘on-grid’ method, the bias that it has, and then this new ‘near-grid’ modification which removes the bias. The input to these methods is a grid of charge density values defined on an orthogonal lattice. The generalization to non-orthogonal lattices and specific boundary conditions follows without significant complication, and has been done in the software available from [20]. The charge density grid can be obtained from ab initio calculations or from experiment. The method described here is particularly well suited to DFT calculations of large molecules or materials, with many atoms and complex bonding geometries.
> **on-grid method**: 在格点方法，上升轨迹严格限制在格点上的Bader分析算法。
> **near-grid method**: 近格点方法，通过修正矢量消除格点偏差的改进算法。
> 
> 这种寻找无格点偏差的Bader体积的方法是对早期基于格点方法的改进[18]。我们首先描述原始的“在格点”方法及其偏差，然后介绍消除偏差的新的“近格点”修正。这些方法的输入是在正交格点上定义的电荷密度值格点。推广到非正交格点和特定边界条件并无显著复杂性，且已在文献[20]提供的软件中实现。电荷密度格点可以从从头计算或实验中获得。这里描述的方法特别适用于具有许多原子和复杂键合几何结构的大分子或材料的DFT计算。
> 
> ### 2.1. On-grid method
> 在格点方法
> 
> The following steps summarize the on-grid Bader analysis method. Additional details are provided in [18].
> 
> (i) First, an initial grid point is chosen. To associate this point with a Bader volume, a path of steepest ascent is followed between neighboring grid points along the charge density gradient.
> (ii) From each grid point along the path, (i, j, k), the projection of the charge density gradient is calculated along the direction to each of the 26 neighboring grid points,
> ∇ρ(i, j, k) · rˆ(di, d j, dk) = ρ
> | rˆ| . (1)
> Here, (di, d j, dk) is a vector of integers describing the step along the grid to the neighbor. The integers di , d j , and dk can each take the values {−1, 0, 1}, excluding di = d j = dk = 0. There are 26 neighbors to each grid point. The vector rˆ(di, d j, dk) is the normalized direction to the neighbor reached by the grid step (di, d j, dk). The gradient projections in equation (1) are calculated using finite difference, where the change in charge density to the neighbor is
> ρ = ρ(i + di, j + d j, k + dk) − ρ(i, j, k), (2)
> and the distance to the neighbor is
> | r| = |r (i + di, j + d j, k + dk) − r (i, j, k)|. (3)
> (iii) One of the 26 neighbors is then determined as the next point along the ascent path. This neighbor, (i + di, j + d j, k + dk), is the one which maximizes the gradient projection from equation (1). This gradient must be a positive value in order to make the step. If there are no positive values, the point (i, j, k) is a charge density maximum.
> (iv) The steepest ascent path is followed until a charge density maximum is found. Each new maximum found is assigned an integer value corresponding to the order in which it was found. In an array with the same dimensions as the charge density grid (initialized to zero), we take the number of the maximum to which the trajectory terminated, and assign that integer to all the grid points along the trajectory. We can do this because an ascent trajectory from each point along the path terminates at that same maximum. In this way, all points along the path are associated with a Bader volume around the charge density maximum.
> (v) Each grid point is analyzed in this way. The order in which grid points are analyzed is not particularly important, and it is easiest to cycle through them in a loop over all values of i , j , and k. Grid points that are already assigned to a Bader volume are skipped, so that ascent trajectories are only followed from unassigned grid points. Trajectories are terminated if they either reach a grid point which has already been assigned, or when a new charge density maximum is found. Figure 1 illustrates both kinds of trajectories. If the trajectory terminates at an assigned grid point, the initial point and all points along the trajectory are assigned to that same Bader volume. If the trajectory terminates at a new charge density maximum, a new entry is made in the list of known charge density maxima, and all points along the trajectory are assigned to that new Bader volume number.
> (vi) After analyzing all grid points in this way, each is assigned to a Bader volume. The total charge in each Bader region is found by integrating the charge density over the grid points assigned to that region. The surface around a Bader volume can be visualized by plotting the charge density of that individual Bader volume.
> 
> 以下步骤总结了在格点Bader分析方法。更多细节见文献[18]。
> 
> (i) 首先，选择一个初始格点。为了将该点与某个Bader体积关联，沿着电荷密度梯度在相邻格点之间追踪一条最陡上升路径。
> (ii) 对于路径上的每个格点 (i, j, k)，计算电荷密度梯度在指向26个相邻格点方向上的投影，
> ∇ρ(i, j, k) · rˆ(di, d j, dk) = ρ / | rˆ| . (1)
> 这里，(di, d j, dk) 是描述沿格点向邻居步进的整数矢量。整数 di, d j, dk 可取值为 {−1, 0, 1}，且不能同时为0。每个格点有26个邻居。矢量 rˆ(di, d j, dk) 是到达由格点步进 (di, d j, dk) 所至邻居的归一化方向。方程(1)中的梯度投影使用有限差分计算，其中到邻居的电荷密度变化为
> ρ = ρ(i + di, j + d j, k + dk) − ρ(i, j, k), (2)
> 到邻居的距离为
> | r| = |r (i + di, j + d j, k + dk) − r (i, j, k)|. (3)
> (iii) 然后确定26个邻居之一作为上升路径的下一个点。该邻居 (i + di, j + d j, k + dk) 是使方程(1)中梯度投影最大化的那个。该梯度必须为正值才能进行步进。如果没有正值，点 (i, j, k) 就是一个电荷密度最大值。
> (iv) 沿着最陡上升路径持续追踪，直到找到一个电荷密度最大值。每个找到的新最大值都分配一个整数值，对应于它被发现的顺序。在一个与电荷密度格点相同维度的数组（初始化为零）中，我们取轨迹终止的最大值编号，并将该整数分配给轨迹上的所有格点。我们可以这样做，因为从路径上每一点出发的上升轨迹都终止于同一个最大值。这样，路径上的所有点都被关联到该电荷密度最大值周围的Bader体积。
> (v) 对每个格点都按此方式分析。分析格点的顺序并不特别重要，最容易的方式是通过循环遍历所有 i, j, k 值。已分配给某个Bader体积的格点会被跳过，因此只从未分配的格点开始追踪上升轨迹。轨迹在以下情况下终止：要么到达一个已被分配的格点，要么发现一个新的电荷密度最大值。图1展示了两种类型的轨迹。如果轨迹终止于一个已分配的格点，初始点和轨迹上所有点都被分配给同一个Bader体积。如果轨迹终止于一个新的电荷密度最大值，则在已知电荷密度最大值列表中添加一个新条目，轨迹上所有点被分配给该新的Bader体积编号。
> (vi) 以这种方式分析完所有格点后，每个格点都被分配到一个Bader体积。每个Bader区域的总电荷通过对分配给该区域的格点上的电荷密度进行积分得到。Bader体积周围的表面可以通过绘制该Bader体积的电荷密度来可视化。
> 
> Figure 1. An illustration of the steepest ascent paths (a) on a charge density grid to find the Bader volumes using the on-grid analysis method. These ascent trajectories are constrained to the grid points, moving at each step to the neighboring grid point towards which the charge density gradient is maximized. Each trajectory either terminates at a new charge density maximum, mi , or at a grid point which has already been assigned. After all grid points are assigned (b), the set of points which terminate at each maximum (green to m1 and blue to m2) constitute that Bader volume. The Bader surfaces (red curved line) separate the volumes.
> 图1. 使用在格点分析方法在电荷密度格点上寻找Bader体积的最陡上升路径示意图（a）。这些上升轨迹被限制在格点上，每一步移动到电荷密度梯度最大的相邻格点。每条轨迹要么终止于一个新的电荷密度最大值 mi，要么终止于一个已被分配的格点。当所有格点都被分配后（b），终止于每个最大值的点集（绿色到 m1，蓝色到 m2）构成该Bader体积。Bader表面（红色曲线）分隔这些体积。
> 
> ### 2.2. Lattice bias in the on-grid method
> 在格点方法中的格点偏差
> 
> The on-grid method is simple to implement, efficient, and robust. Recently, however, Sanville et al showed that the method results in some systematic error of the Bader surfaces and population analysis [19]. This error is caused by the fact that the ascent trajectories in the on-grid method are constrained to the grid points. With trajectories following grid directions, the Bader surfaces become artificially angular with facets parallel to the grid. This bias remains in the limit of a fine charge density grid. The lattice bias in the on-grid method is illustrated in figure 2. Ascent trajectories step between grid points in the direction that is most aligned with the charge density gradient (see equation (1)). Since there are only 26 such directions (8 in two-dimensions), the trajectories accumulate error when the gradients lines do not run parallel to the lattice. In figure 2, an on-grid trajectory is shown crossing the true dividing surface, resulting in points (e.g. the light-blue point) that are assigned to the incorrect Bader volume, and a surface which is artificially aligned along the lattice.
> 
> 在格点方法实现简单、高效且鲁棒。然而，最近Sanville等人表明，该方法会导致Bader表面和布居分析出现一些系统误差[19]。该误差源于在格点方法中的上升轨迹被限制在格点上。由于轨迹遵循格点方向，Bader表面变得人为地呈现棱角，具有平行于格点的小面。这种偏差即使在精细的电荷密度格点极限下仍然存在。在格点方法中的格点偏差如图2所示。上升轨迹在格点之间沿着与电荷密度梯度最一致的方向步进（见方程(1)）。由于只有26个这样的方向（二维中为8个），当梯度线不平行于格点时，轨迹会累积误差。在图2中，一条在格点轨迹被显示为穿过了真实的分界面，导致某些点（例如浅蓝色点）被分配到错误的Bader体积，并且表面被人为地沿格点对齐。
> 
> Figure 2. Illustration of lattice bias in the on-grid method. The true dividing surface (red) runs parallel to the gradient lines, but the on-grid ascent trajectories follow the lattice direction along which the projection of the charge density gradient is maximized. Starting from the initial point, this direction is along +x and the trajectory moves from grid point to grid point in this direction. The error can be seen as the on-grid trajectory (straight blue arrows through the light-blue point) deviates from the true trajectory (solid blue curved arrow). The resulting dividing surface follows the x lattice direction instead of the true dividing surface.
> 图2. 在格点方法中格点偏差的示意图。真实的分界面（红色）平行于梯度线，但在格点上升轨迹遵循电荷密度梯度投影最大化的格点方向。从初始点开始，该方向沿+x方向，轨迹沿此方向从格点到格点移动。误差表现为在格点轨迹（穿过浅蓝色点的直蓝色箭头）偏离了真实轨迹（实线蓝色弯曲箭头）。最终的分界面沿着x格点方向，而非真实的分界面。
> 
> ### 2.3. Near-grid method without lattice bias
> 无格点偏差的近格点方法
> 
> Here, we describe a method which fixes the lattice bias error in the on-grid method. This new method is described as the near-grid method; trajectories still follow from grid point to grid point, but a correction vector is remembered, which points to the location of the actual trajectory as it passes near each grid point. The near-grid method eliminates the lattice bias because trajectories are not constrained to grid points. It also retains the simplicity and linear scaling with system size of the on-grid method. The following steps describe the near-grid algorithm.
> 
> (i) Starting from an initial grid point, (i, j, k), the trajectory of steepest ascent is followed up the charge density. Each step is made to one of the 26 neighboring grid points.
> (ii) In order to make a step from point (i, j, k), the charge density gradient, ∇ρ, is calculated from the charge density at the six closest neighbors using a central finite difference scheme. The components of the charge density in the x, y, and z directions are:
> ∇ρx = ρ(i + 1, j, k) − ρ(i − 1, j, k)
> |r(i + 1, j, k) − r (i − 1, j, k)|, (4a)
> ∇ρy = ρ(i, j + 1, k) − ρ(i, j − 1, k)
> |r (i, j + 1, k) − r (i, j − 1, k)| , (4b)
> ∇ρz = ρ(i, j, k + 1) − ρ(i, j, k − 1)
> |r (i, j, k + 1) − r (i, j, k − 1)| . (4c)
> (iii) To follow the gradient, a step along the gradient vector,
> rgrad = c(∇ρx , ∇ρy , ∇ρz), (5)
> should be taken. For this step to advance the trajectory by one grid point, and no more in any direction, the constant is chosen as
> c = min(dx /|∇ρx |, dy/|∇ρy|, dz/|∇ρz|), (6)
> where dx, dy, and dz are the grid spacings along the x, y, and z Cartesian directions, respectively. The step rgrad takes the trajectory (in general) off the grid. To retain the efficiency of the on-grid method, we then jump to the nearest grid point, so that the trajectory can be described as a hopping process between grid points. If we label this step between grid points as rgrid, we can then describe a correction vector (initially zero) from the final grid point to the location of the true trajectory,
> r = r + (rgrad − rgrid
> ) . (7)
> In figure 3 the first rgrid step is along +x , and the correction vector, r1, points along −y to the true trajectory.
> (iv) From each new point along the ascent trajectory, the vectors rgrad and rgrid are calculated, and the correction vector is accumulated so that it always points to the true trajectory. When the length of any component of r is larger than half of the grid spacing, a correction step is taken in that direction. The correction vector is then recalculated by subtracting the correction step. In this way, the true trajectory is never more than half a grid point from the current grid point in any direction.
> (v) The ascent trajectory is terminated when one of two criteria is met: (i) when it reaches a charge density maximum, or (ii) when it reaches a point for which the point itself and all of its neighbors are assigned to the same Bader region. In either case, all the grid points along the ascent trajectory are assigned to the same Bader region as the end points of the trajectory.
> (vi) An ascent trajectory is calculated from each grid point until all are assigned to a Bader volume. From each new trajectory, the correction vector r is reset to (0, 0, 0).
> (vii) When all the points are assigned, a final refinement of the grid points adjacent to the Bader surfaces is required. Depending upon the order in which grid points are analyzed, the grid point adjacent to the Bader surface can be assigned to one of the two volumes on either side of the dividing surface. This ambiguity is due to the fact that the trajectory between grid points deviates from the true trajectory by up to half a grid step. The refinement step corrects this by first identifying all grid points on the boundary of a Bader volume. An ascent trajectory is followed from each of these boundary grid points to determine in which volume it belongs. In this case, only the initial point is assigned, so that (in the case of smooth charge density grids) the refinement process need not be repeated.
> **correction vector**: 修正矢量，从格点指向真实离格点轨迹的矢量。
> 
> 这里，我们描述一种修正了在格点方法中格点偏差误差的方法。这种新方法被称为近格点方法；轨迹仍然从格点到格点行进，但会记住一个修正矢量，该矢量指向真实轨迹经过每个格点附近时的位置。近格点方法消除了格点偏差，因为轨迹不受格点约束。它还保留了在格点方法的简洁性和随系统大小的线性缩放。以下步骤描述了近格点算法。
> 
> (i) 从初始格点 (i, j, k) 开始，沿着电荷密度向上追踪最陡上升轨迹。每一步移动到26个相邻格点之一。
> (ii) 为了从点 (i, j, k) 进行步进，使用中心有限差分格式从六个最近邻格点的电荷密度计算电荷密度梯度 ∇ρ。电荷密度在 x, y, z 方向的分量为：
> ∇ρx = [ρ(i + 1, j, k) − ρ(i − 1, j, k)] / |r(i + 1, j, k) − r (i − 1, j, k)|, (4a)
> ∇ρy = [ρ(i, j + 1, k) − ρ(i, j − 1, k)] / |r (i, j + 1, k) − r (i, j − 1, k)|, (4b)
> ∇ρz = [ρ(i, j, k + 1) − ρ(i, j, k − 1)] / |r (i, j, k + 1) − r (i, j, k − 1)|. (4c)
> (iii) 为了跟随梯度，应沿梯度矢量进行步进，
> rgrad = c(∇ρx , ∇ρy , ∇ρz), (5)
> 为了使这一步推进轨迹一个格点，且在任何方向上不超过一个格点，常数选择为
> c = min(dx /|∇ρx |, dy/|∇ρy|, dz/|∇ρz|), (6)
> 其中 dx, dy, dz 分别是沿 x, y, z 笛卡尔方向的格点间距。步进 rgrad 通常会使轨迹离开格点。为了保持在格点方法的效率，我们随后跳转到最近的格点，这样轨迹就可以描述为格点间的跳跃过程。如果我们将这个格点间的步进标记为 rgrid，那么我们可以描述一个从最终格点指向真实轨迹位置的修正矢量（初始为零），
> r = r + (rgrad − rgrid). (7)
> 在图3中，第一个 rgrid 步进沿 +x 方向，修正矢量 r1 指向 −y 方向指向真实轨迹。
> (iv) 对于上升轨迹上的每个新点，计算矢量 rgrad 和 rgrid，并累积修正矢量，使其始终指向真实轨迹。当 r 的任一分量长度大于格点间距的一半时，在该方向上进行一次修正步进。然后通过减去修正步进重新计算修正矢量。这样，真实轨迹在任何方向上距离当前格点永远不会超过半个格点。
> (v) 上升轨迹在满足以下两个条件之一时终止：(i) 到达一个电荷密度最大值，或 (ii) 到达一个点，该点本身及其所有邻居都被分配到同一个Bader区域。无论哪种情况，上升轨迹上的所有格点都被分配到与轨迹终点相同的Bader区域。
> (vi) 对每个格点计算上升轨迹，直到所有格点都被分配到一个Bader体积。对于每条新轨迹，修正矢量 r 重置为 (0, 0, 0)。
> (vii) 当所有点都被分配后，需要对邻近Bader表面的格点进行最终精修。根据分析格点的顺序，靠近Bader表面的格点可能被分配到分界面两侧两个体积之一。这种模糊性是由于格点间的轨迹与真实轨迹最多偏离半个格点步长所致。精修步骤通过首先识别Bader体积边界上的所有格点来纠正这一点。从这些边界格点中的每一个追踪一条上升轨迹，以确定它属于哪个体积。在这种情况下，只分配初始点，因此（对于平滑的电荷密度格点）精修过程无需重复。
> 
> Figure 3. An illustration of the near-grid step and how a correction vector points to the true trajectory. Steps are taken between grid points. The first step between grid points, rgrid and along the gradient, rgrad, differ by the correction vector r1. After the second step, the difference is r2, and the total correction vector is r = r1 + r2. Now, the y component of the correction vector is larger than half of the grid spacing so that a correction step is taken in the −y direction, and the correction vector is recalculated as r ′ 2.
> 图3. 近格点步进以及修正矢量如何指向真实轨迹的示意图。步进在格点之间进行。第一个格点间步进 rgrid 和沿梯度的步进 rgrad 相差修正矢量 r1。第二步后，差异为 r2，总修正矢量为 r = r1 + r2。此时，修正矢量的 y 分量大于格点间距的一半，因此在 −y 方向进行一次修正步进，修正矢量重新计算为 r′2。
> 
> ## 3. Results
> 结果
> 
> ### 3.1. Two-dimensional model
> 二维模型
> 
> The lattice bias in the on-grid method is particularly severe when the true dividing surface runs at a small angle to the grid over long distances. In figure 4 we have constructed such a two-dimensional charge density grid from the sum of three Gaussian functions. The on-grid method finds vertical dividing surfaces that deviate from the true (gray) dividing surface, resulting in the (white) error regions. In these regions the method has assigned charge to the wrong Bader region.
> 
> 当真实分界面与格点方向以小角度长距离延伸时，在格点方法中的格点偏差尤为严重。在图4中，我们通过三个高斯函数之和构建了这样一个二维电荷密度格点。在格点方法找到了偏离真实（灰色）分界面的垂直分界面，导致了（白色）错误区域。在这些区域中，方法将电荷分配到了错误的Bader区域。
> 
> The near-grid method corrects this lattice bias. After ascent trajectories are followed from each grid point, error regions are localized to grid points adjacent to the true dividing surface. A subsequent refinement step eliminates these errors, and gives the correct Bader volumes in the limit of a sufficiently fine grid.
> 
> 近格点方法修正了这种格点偏差。在从每个格点追踪上升轨迹之后，错误区域被限制在紧邻真实分界面的格点。随后的精修步骤消除了这些错误，并在足够精细的格点极限下给出了正确的Bader体积。
> 
> Figure 4. Comparison of the on-grid and near-grid methods for a two-dimensional charge density surface constructed from three Gaussian functions. By construction, the true dividing surface (gray lines in (a)) are at a small angle to the lattice. The on-grid method results in biased dividing surfaces that follow the grid; error regions, in which the Bader volume is incorrectly assigned, are colored white. In a single iteration of the near-grid method (b), the error regions are confined to the Bader surfaces. A subsequent refinement iteration (c) corrects all but two grid points, which are mis-assigned because of the low resolution of the grid. As the grid density is increased, the near-grid method finds the exact Bader volumes.
> 图4. 在由三个高斯函数构建的二维电荷密度表面上，在格点方法和近格点方法的比较。根据构造，真实的分界面（a中的灰线）与格点方向成一个小角度。在格点方法导致有偏差的分界面，这些分界面跟随格点；错误区域（Bader体积分配错误）被染成白色。在近格点方法的单次迭代中（b），错误区域被限制在Bader表面附近。随后的精修迭代（c）修正了除两个格点之外的所有点，这两个格点由于格点分辨率低而被错误分配。随着格点密度的增加，近格点方法能够找到精确的Bader体积。
> 
> ### 3.2. A water molecule
> 水分子
> 
> Finding the Bader volumes in a water molecule is a more realistic test. The geometry and charge density of the molecule was calculated with Gaussian 98 [21] using the aug-cc-pVDZ basis set at the MP2 level of perturbation theory. The charge density was written on a 257³ orthogonal grid. The dividing surfaces found with the on-grid and near-grid methods are shown in figure 5. The lattice bias is apparent in the on-grid method from the angular shape of the surfaces (see also [18]). This bias is removed with the near-grid method and the surfaces become smooth. The ripples in the surface shown in figure 5 are due to the finite resolution of the grid.
> 
> 寻找水分子中的Bader体积是一个更现实的测试。分子的几何结构和电荷密度使用Gaussian 98 [21]在MP2微扰理论水平下用aug-cc-pVDZ基组计算。电荷密度写入一个257³的正交格点。用格点方法和近格点方法找到的分界面如图5所示。在格点方法中，从表面的棱角形状可以明显看出格点偏差（另见[18]）。近格点方法消除了这种偏差，表面变得平滑。图5中表面上的波纹是由格点的有限分辨率造成的。
> 
> Figure 5. Comparison of Bader dividing surfaces found with the on-grid method (left) and the near-grid method (right). The on-grid surfaces are angular with facets oriented along the grid directions. This bias is removed in the near-grid method.
> 图5. 用格点方法（左）和近格点方法（右）找到的Bader分界面的比较。在格点表面呈棱角状，具有沿格点方向的小面。近格点方法消除了这种偏差。
> 
> ### 3.3. Ionic charge in a NaCl crystal
> NaCl晶体中的离子电荷
> 
> These grid-based analysis methods can be used for solid-state systems as well as molecular ones. In order to show convergence of the method with respect to grid density, we have calculated the Bader charges in a NaCl salt crystal, using the eight-atom unit cell illustrated in figure 6 (inset). The charge density was generated using the VASP plane-wave-based DFT code [22], using the PW91 generalized gradient functional [23]. Frozen core charges were represented with pseudopotentials of the Vanderbilt form [24] using the projector augmented wave (PAW) framework [25]. Including this frozen core charge in the charge density grid is important for calculating accurate Bader charges. A plane wave energy cutoff of 262.5 eV was used, and the Brillouin zone was sampled with a 3 × 3 × 3 Monkhorst–Pack [26] k-point mesh. An optimal lattice constant of 5.86 Å was determined for the NaCl crystal. A set of charge density grids ranging from 60³ points to 350³ points were calculated. The grid spacing is 0.095 Å in the former case and 0.016 Å in the latter. The calculated valance charge on the Na ions is shown in figure 6. The near-grid method shows monotonic and smooth convergence to a valance charge of 0.828 e, whereas the on-grid method has systematic errors in the limit of a fine grid. Although the systematic error of less than 0.01 e in the on-grid method is acceptable for most calculations, the near-grid method should be used for its improved accuracy and systematic convergence.
> **pseudopotentials**: 赝势，用于替代原子内核电子与价电子相互作用的有效势。
> **projector augmented wave (PAW)**: 投影缀加波，一种用于平面波DFT计算的赝势方法。
> 
> 这些基于格点的分析方法既可以用于固态体系，也可以用于分子体系。为了展示方法相对于格点密度的收敛性，我们计算了NaCl晶体中的Bader电荷，使用图6（插图）所示的8原子晶胞。电荷密度使用VASP平面波基组DFT代码[22]生成，采用PW91广义梯度泛函[23]。冻芯电荷用Vanderbilt形式的赝势[24]在投影缀加波（PAW）框架[25]下表示。将冻芯电荷包含在电荷密度格点中对于计算准确的Bader电荷至关重要。使用了262.5 eV的平面波能量截断，布里渊区用3×3×3 Monkhorst–Pack [26] k点网格采样。NaCl晶体的最优晶格常数确定为5.86 Å。计算了一组电荷密度格点，范围从60³点到350³点。前者格点间距为0.095 Å，后者为0.016 Å。计算得到的Na离子价电荷如图6所示。近格点方法显示出单调平滑地收敛到0.828 e的价电荷，而在格点方法在精细格点极限下存在系统误差。尽管在格点方法中小于0.01 e的系统误差对于大多数计算是可以接受的，但应使用近格点方法以获得更高的精度和系统性收敛。
> 
> Figure 6. Convergence with respect to grid density of the Bader charges for ions in a NaCl crystal. A fully converged charge on each Na ion is 0.828 e (blue dashed line). The (old) on-grid method deviates from this value by ca 0.01 e for a fine grid with 40 million points. The (new) near-grid method rapidly converges to the correct value.
> 图6. NaCl晶体中离子Bader电荷相对于格点密度的收敛性。每个Na离子上完全收敛的电荷为0.828 e（蓝色虚线）。（旧的）在格点方法在拥有4000万个点的精细格点上偏离该值约0.01 e。（新的）近格点方法迅速收敛到正确值。
> 
> ### 3.4. Variation of charge with molecular orientation
> 电荷随分子取向的变化
> 
> The lattice bias in the on-grid method can be seen by comparing the Bader volumes and charges for a molecule aligned at different orientations with respect to the charge density lattice. A converged calculation should not depend upon this orientation. For this test, we have calculated the Bader volumes and charges around an H₂O molecule using the VASP code. The details of these calculations are the same as for the NaCl calculations with the exception of a 250 eV energy cutoff and a single Γ-point for the isolated molecule. Figure 7 shows a change in the shape of the Bader volumes for the on-grid method as the H₂O molecule is rotated by 45° in the plane of the figure. With the near-grid method, the shape of the volumes remains constant as it should. The sensitivity of the Bader charges to molecular orientation is compared quantitatively in figure 8. Not only does the on-grid method systematically underestimate the charge transfer from hydrogen to oxygen, it also varies by ca 0.1 e as the molecule is rotated by 45°. With the near-grid method, this variation is largely removed; the shape and integrated charge of the Bader volumes is insensitive to the orientation of the molecule with respect to the charge density grid.
> 
> 通过比较分子相对于电荷密度格点以不同取向排列时的Bader体积和电荷，可以看出在格点方法的格点偏差。一个收敛的计算不应依赖于这种取向。为了进行此测试，我们使用VASP代码计算了H₂O分子周围的Bader体积和电荷。这些计算的细节与NaCl计算相同，除了对孤立分子使用250 eV能量截断和单个Γ点。图7显示了当H₂O分子在图平面内旋转45°时，在格点方法中Bader体积形状的变化。而近格点方法中，体积形状保持恒定，符合预期。图8定量比较了Bader电荷对分子取向的敏感性。在格点方法不仅系统性地低估了从氢到氧的电荷转移，而且当分子旋转45°时，电荷变化约0.1 e。使用近格点方法，这种变化基本消除；Bader体积的形状和积分电荷对分子相对于电荷密度格点的取向不敏感。
> 
> Figure 7. The Bader surface in H₂O is strongly dependent upon the orientation of the molecule with the on-grid method. This orientation dependence is due to the bias in the method which tends to orient the Bader surfaces along the grid directions. In the near-grid method, this bias is removed and the Bader surfaces are insensitive to the orientation of the molecule.
> 图7. H₂O中的Bader表面在使用在格点方法时强烈依赖于分子取向。这种取向依赖性源于方法中的偏差，该偏差倾向于使Bader表面沿格点方向取向。在近格点方法中，这种偏差被消除，Bader表面对分子取向不敏感。
> 
> Figure 8. The calculated Bader charge on the O atom in a H₂O molecule as it is rotated with respect to the charge density grid. The biased Bader surfaces in the on-grid method give rise to both systematic and orientation dependent errors as compared to the near-grid method, for which the Bader surfaces and O valance charge remain constant with orientation.
> 图8. H₂O分子中计算得到的O原子Bader电荷随其相对于电荷密度格点旋转的变化。与近格点方法相比，在格点方法中有偏差的Bader表面导致了系统误差和取向依赖误差，而近格点方法的Bader表面和O价电荷随取向保持恒定。
> 
> ### 3.5. Scaling of computational effort
> 计算量的缩放
> 
> A strength of the on-grid method is that there is a fixed computational effort per charge density grid point, and therefore the total computational time scales linearly with the number of grid points [18]. This property of the method, as well as the robustness, makes the algorithm applicable to large systems which can have complex bonding geometries. These are features of the method that we want to retain in this improved near-grid method. To test this, the computer time required to analyze charge density files was compared for various grid sizes for the NaCl system described in section 3.3. Cubic grids ranging from 60³ to 300³ points were analyzed. Each analysis required a single refinement iteration. Figure 9 shows that the computer time required to complete the analysis scales linearly with the number of charge density grid points. The slope of the line corresponds to analyzing a million grid points in 11.5 s on a 2.5 GHz G5 PowerPC.
> 
> 在格点方法的一个优势是每个电荷密度格点所需的计算量固定，因此总计算时间随格点数量线性缩放[18]。这一特性以及鲁棒性使得该算法适用于可能具有复杂键合几何结构的大型体系。这些是我们在改进的近格点方法中希望保留的特性。为了测试这一点，对第3.3节中描述的NaCl体系，比较了不同格点大小下分析电荷密度文件所需的计算机时间。分析了从60³到300³点的立方格点。每次分析需要一次精修迭代。图9显示，完成分析所需的计算机时间随电荷密度格点数量线性缩放。斜率对应于在2.5 GHz G5 PowerPC上每分析一百万个格点需要11.5秒。
> 
> Figure 9. Computer time required to analyze the charge density grid for the eight-atom NaCl cell with the near-grid algorithm. The computational cost scales linearly with the number of grid points in the charge density file, as with the on-grid method.
> 图9. 使用近格点算法分析8原子NaCl晶胞电荷密度格点所需的计算机时间。计算成本与电荷密度文件中的格点数量成线性关系，与在格点方法相同。
> 
> ## 4. Concluding remarks
> 结论
> 
> The Bader analysis algorithm presented here removes the lattice bias of a constrained grid-based algorithm [18] allowing convergence in the limit of a fine charge density grid. The algorithm is suitable for large DFT calculations, and can be used for plane-wave-based calculations of condensed phase systems.
> 
> 本文提出的Bader分析算法消除了受限的基于格点算法[18]的格点偏差，允许在精细电荷密度格点极限下收敛。该算法适用于大型DFT计算，并可用于凝聚相体系的平面波基组计算。
> 
> ## Acknowledgments
> 致谢
> 
> This research was supported by the National Science Foundation from the NSF-CAREER award CHE-0645497 and the Robert A Welch Foundation. We also gratefully acknowledge the computational resources provided by the Texas Advanced Computing Center at the University of Texas at Austin.
> 
> 本研究得到了美国国家科学基金会NSF-CAREER奖CHE-0645497和Robert A Welch基金会的支持。我们同时感谢德克萨斯大学奥斯汀分校德克萨斯高级计算中心提供的计算资源。
> 
> ## References
> 参考文献
> 
> [1] Bader R F W 1990 Atoms in Molecules: a Quantum Theory (New York: Oxford University Press)
> [2] Madsen G K H, Gatti C, Iversen B B, Damjavonic Lj, Stucky G D and Srdanov V I 1999 F center in sodium electrosodalite as a physical manifestation of a non-nuclear attractor in the electron density Phys. Rev. B 59 12359
> [3] Wiberg K B and Rablen P R 1993 Comparison of atomic charges derived via different procedures J. Comput. Chem. 14 1504–18
> [4] Angyan J G, Jansen G, Loos M, Hattig C and Hess B A 1994 Distributed polarizabilities obtained using a constrained density-fitting algorithm Chem. Phys. Lett. 219 267
> [5] De Proft F, Van Alsenoy C, Peeters A, Langenaeker W and Geerlings P 2002 Atomic charges, dipole moments, and fukui functions using the hirshfeld partitioning of the electron density J. Comput. Chem. 23 1198
> [6] Popelier P L A 1998 Morphy98 A program written by P L A Popelier with a contribution from R G A Bone, UMIST, Manchester, England
> [7] Stefanov B B and Cioslowski J 1995 An efficient approach to calculation of zero-flux atomic surfaces and generation of atomic integration data J. Comput. Chem. 16 1394–404
> [8] Popelier P L A 2001 A fast algorithm to compute atomic charges based on the topology of the electron density Theor. Chem. Acc. 105 393–9
> [9] Biegler König F W, Bader R F W and Tang T 1982 Calculation of the average properties of atoms in molecules. II J. Comput. Chem. 3 317–28
> [10] Uberuaga B P, Batista E R and Jónsson H 1999 Elastic sheet method for identifying atoms in molecules J. Chem. Phys. 111 10664–9
> [11] Katan C, Rabiller P, Lecomte C, Guezo M, Oison V and Souhassou M 2003 Numerical computation of critical properties and atomic basins from three-dimensional grid electron densities J. Appl. Crystallogr. 36 65
> [12] Popelier P L A 1994 An analytical expression for interatomic surfaces in the theory of atoms in molecules Theor. Chim. Acta 87 465–76
> [13] Popelier P L A 1998 A method to integrate an atom in a molecule without explicit representation of the interatomic surface Comput. Phys. Commun. 108 180
> [14] Malcolm N O J and Popelier P L A 2003 An improved algorithm to locate critical points in a 3d scalar field as implemented in the program morphy J. Comput. Chem. 24 437
> [15] Malcolm N O J and Popelier P L A 2003 An algorithm to delineate and integrate topological basins in a three-dimensional quantum mechanical density function J. Comput. Chem. 24 1276
> [16] Noury S, Krokidis X, Fuster F and Silvi B 1999 Computational tools for the electron localization function topological analysis Comput. Chem. 23 597–604
> [17] Biegler König F W, Schönbohm J and Bayles D 2001 Aim2000—a program to analyze and visualize atoms in molecules J. Comput. Chem. 36 65
> [18] Henkelman G, Arnaldsson A and Jónsson H 2006 A fast and robust algorithm for bader decomposition of charge density Comput. Mater. Sci. 36 354–60
> [19] Sanville E, Kenny S D, Smith R and Henkelman G 2007 Improved grid-based algorithm for bader charge allocation J. Comput. Chem. 28 899–908
> [20] Arnaldsen A, Tang W and Henkelman G Bader Charge Analysis http://theory.cm.utexas.edu/bader/
> [21] Frisch M J et al 1998 Gaussian 98, Revision A.7 (Pittsburgh, PA: Gaussian)
> [22] Kresse G and Hafner J 1993 Ab initio molecular dynamics for liquid metals Phys. Rev. B 47 R558–61
> [23] Perdew J P 1991 Unified theory of exchange and correlation beyond the local density approximation Electronic Structure of Solids ed P Ziesche and H Eschrig (Berlin: Akademie Verlag) p 11
> [24] Vanderbilt D 1990 Soft self-consistent pseudopotentials in a generalized eigenvalue formalism Phys. Rev. B 41 7892–5
> [25] Kresse G and Joubert J 1999 From ultrasoft pseudopotentials to the projector augmented wave method Phys. Rev. B 59 1758
> [26] Monkhorst H J and Pack J D 1976 Special points for Brillouin-zone integrations Phys. Rev. B 13 5188–92
> 
> ```
> 
> 🚀 [笔记回链](zotero://select/library/items/PHBX3RGT)
> 
> * * *
> 
> `GPT 自定 ②`  `deepseek-v4-pro`  _由批量 AI 解读自动生成于 2026/8/10 23:15:01 （重新解读）_
> 
> 🏷️ #🤖️/论文双语转写 🏷️ #🤖️/AI文献阅读

^KEY9C1304CC