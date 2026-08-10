---
作者: [G. Kresse, J. Hafner]
中文标题: <i>锗中液态金属-非晶半导体转变的从头算分子动力学模拟
分类: [02_中性-离子转变 (Neutral-Ionic Transition)]
影响因子: 2
---



# <i>Ab initio</i> molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transition in germanium
> [!info]+ <center>Metadata</center>
> 
> |<div style="width: 5em">Key</div>|Value|
> |--:|:--|
> |文献类型|journalArticle|
> |标题|<i>Ab initio</i> molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transition in germanium|
> |短标题|<i>锗中液态金属-非晶半导体转变的从头算分子动力学模拟|
> |作者|[[G. Kresse]]、 [[J. Hafner]]|
> |期刊名称|[[Physical Review B]]|
> |DOI|[10.1103/PhysRevB.49.14251](https://doi.org/10.1103/PhysRevB.49.14251)|
> |存档位置|21795|
> |文库编目|3.7|
> |索书号|2|
> |版权|http://link.aps.org/licenses/aps-default-license|
> |分类|[[02_中性-离子转变 (Neutral-Ionic Transition)]]|
> |条目链接|[My Library](zotero://select/library/items/SVBRRMBT)|
> |PDF 附件|[Kresse和Hafner - 1994 - Ab initio molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transitio.pdf](zotero://open-pdf/library/items/YJLZJIMQ)|
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
> title:: <i>Ab initio</i> molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transition in germanium
> shortTitle:: <i>锗中液态金属-非晶半导体转变的从头算分子动力学模拟
> creators:: [[G. Kresse]]、 [[J. Hafner]]
> publicationTitle:: [[Physical Review B]]
> journalAbbreviation:: Phys. Rev. B
> volume:: 49
> issue:: 20
> pages:: 14251-14269
> series:: 
> language:: en
> DOI:: [10.1103/PhysRevB.49.14251](https://doi.org/10.1103/PhysRevB.49.14251)
> ISSN:: 0163-1829, 1095-3795
> url:: [https://link.aps.org/doi/10.1103/PhysRevB.49.14251](https://link.aps.org/doi/10.1103/PhysRevB.49.14251)
> archive:: 
> archiveLocation:: 21795
> libraryCatalog:: 3.7
> callNumber:: 2
> JCRQ:: Q2
> rights:: http://link.aps.org/licenses/aps-default-license
> extra:: 🏷️ /unread、📒、🤖️
> collection:: [[02_中性-离子转变 (Neutral-Ionic Transition)]]
> tags:: #unread #🤖️
> related:: 
> itemLink:: [My Library](zotero://select/library/items/SVBRRMBT)
> pdfLink:: [Kresse和Hafner - 1994 - Ab initio molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transitio.pdf](zotero://open-pdf/library/items/YJLZJIMQ)
> qnkey:: kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994
> date:: 1994-05-15
> dateY:: 1994
> dateAdded:: 2026-05-06
> datetimeAdded:: 2026-05-06 05:04:29
> dateModified:: 2026-08-10
> datetimeModified:: 2026-08-10 23:23:56
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
>⏰ importDateTime:: 2026-08-10 18:17:22

%--------------ω--------------%



## <span style="color: rgb(0, 174, 137);">❶ 🤖️ AI 文献解读</span>

> 🚀 [笔记回链](zotero://select/library/items/KK9AL2U5)

^KEYaiPapers

> <span class="AIReading">🤖 AI 解读，快人一步</span>
> 
> ## 一、引言
> 
> 这篇论文研究的是**锗（Ge, Germanium）**在从**液态金属（liquid metal）**转变为**非晶半导体（amorphous semiconductor）**过程中的原子结构、电子结构与动力学行为。作者使用的是当时非常前沿的**第一性原理分子动力学（ab initio molecular dynamics, AIMD）**方法，而不是依赖经验参数的经典势函数模拟。
> 
> ### 这篇论文为什么重要？
> 
> 锗、硅这类材料有一个很特殊的性质：
> 
> -   在晶体或非晶固态中，通常表现为**四配位、共价主导、半导体**
> -   在液态中，则表现为**高配位、金属性明显**
> 
> 因此，从液态冷却到非晶态，不只是“变无序”，而是发生了一个深刻的**金属—半导体转变（metal-semiconductor transition）**。这意味着：
> 
> -   原子邻接关系变了
> -   成键方式变了
> -   电子态密度变了
> -   扩散与振动行为也变了
> 
> 传统经典分子动力学往往能描述液态，却难以正确得到真实的非晶半导体网络，常常会生成“过配位、仍带金属性”的假非晶结构。作者的核心贡献，就是证明：用**基于密度泛函理论（density-functional theory, DFT）**的AIMD，可以较真实地重建液态Ge到非晶Ge的全过程，并得到与实验相符的结构、电子与动力学性质。
> 
> _可视化提示：这里很适合画一个“液态金属Ge → 过冷液体Ge → 非晶半导体Ge”的相变路线图。_
> 
> * * *
> 
> ## 二、论文结构与逻辑概览
> 
> 这篇论文的逻辑非常清晰，可以重构为以下链条：
> 
> ### 1. 问题提出
> 
> 作者首先指出：
> 
> -   非晶材料难以靠实验完全确定三维原子结构
> -   衍射实验主要给出的是**对关联函数（pair-correlation function）**等一维信息
> -   对于Si/Ge这类材料，经典势函数无法同时准确描述液态和非晶态
> 
> 因此需要一种能实时计算量子力学多体作用力的方法。
> 
> ### 2. 方法设计
> 
> 作者提出的技术路线包括四个核心组成：
> 
> -   **有限温度密度泛函理论（finite-temperature DFT）**
> -   每个MD步后做**精确能量最小化**
> -   使用**非局域赝势（nonlocal pseudopotential）**
> -   使用**Nosé热浴（Nosé dynamics）**生成正则系综
> 
> 其关键思想是：不采用Car-Parrinello那种电子与离子一起演化的方式，而是在每一步都把电子态拉回**Born-Oppenheimer面**，从而避免金属体系中的非绝热问题。
> 
> ### 3. 模拟过程
> 
> 模拟流程是：
> 
> -   从1250 K液态Ge开始
> -   逐步淬火到300 K
> -   获得“初始非晶态”
> -   再进行一次退火（升至600 K后再降温）
> -   比较淬火态与退火态
> 
> ### 4. 核心分析对象
> 
> 作者系统分析了：
> 
> -   **径向分布函数 g(R)**
> -   **静态结构因子 S(Q)**
> -   **键角分布**
> -   **电子态密度 DOS**
> -   **扩散系数**
> -   **速度自相关函数**
> -   **振动态密度**
> -   **缺陷的几何、成键与谱学性质**
> 
> ### 5. 最终结论
> 
> 作者认为：
> 
> -   AIMD成功再现了液态与非晶Ge的实验性质
> -   金属—半导体转变伴随配位数下降与四面体局域结构形成
> -   非晶Ge中既有三配位缺陷，也有五配位缺陷
> -   缺陷不能只用几何配位定义，还必须结合电子态与成键信息分析
> 
> _可视化提示：可画“背景问题→方法突破→相变模拟→结构/电子/动力学分析→缺陷分析→结论贡献”的流程图。_
> 
> * * *
> 
> ## 三、所有图表深度解析
> 
> ### 图1：守恒量与势能随时间演化
> 
> -   横轴：时间，单位 **ps**
> -   纵轴：能量，单位 **eV/atom**
> 
> #### 图1(a)：液态Ge, T=1250 K
> 
> 显示正则系综中的守恒量和势能随时间变化。作者强调：
> 
> -   3 ps内守恒量漂移小于 **5 meV/atom**
> -   说明算法稳定，数值误差很小
> 
> #### 图1(b)：非晶Ge, T=300 K
> 
> -   6 ps内总能变化小于 **1 meV/atom**
> -   表明在低温非晶态下算法更稳定
> 
> **意义**：这不是物理结果图，而是“方法可信性验证图”。
> 
> * * *
> 
> ### 图2：晶体Ge不同结构的能量-体积与压力-体积关系
> 
> -   横轴：体积，单位 **Å³**
> -   纵轴：能量 **eV**、压力 **kbar**
> 
> 作者比较了金刚石结构、β-Sn、fcc、bcc、sc等结构。 结果表明：
> 
> -   赝势能较好再现实验晶格常数与体模量
> -   说明所用第一性原理基础设置可靠
> 
> **意义**：证明模拟液态/非晶Ge之前，基础电子结构方法已经通过固态基准测试。
> 
> * * *
> 
> ### 图3：整个热处理过程中的温度与势能变化
> 
> -   横轴：时间，单位 **ps**
> -   温度单位：**K**
> -   势能单位：**eV/atom**
> 
> #### 图3(a)
> 
> 记录从液态到淬火到退火再冷却的全过程。
> 
> #### 图3(b)
> 
> 势能随热处理降低，退火后势能进一步下降。
> 
> **含义**：
> 
> -   退火不是形式操作，而是真正帮助系统进入更低能量、更合理的非晶构型。
> 
> * * *
> 
> ### 图4：不同温度下的均方位移
> 
> -   横轴：时间，单位 **ps**
> -   纵轴：均方位移，单位应为 **Å²**
> 
> 温度越低，曲线斜率越小，说明扩散显著减弱。
> 
> -   1250 K：原子明显扩散
> -   650–750 K：扩散减慢，但仍是液体
> -   低温非晶：基本冻结
> 
> **物理意义**：支持“过冷液体→非晶”的动力学冻结图景。
> 
> * * *
> 
> ### 图5：液态Ge（1250 K）的结构与电子态
> 
> 包含四部分：
> 
> #### (a) 对关联函数 g(R)
> 
> -   横轴：距离 **R, Å**
> -   首峰位置约 **2.75 Å**
> -   第一近邻配位数约 **5.8–6.9**（取决于积分截断）
> 
> 说明液态Ge并非普通简单液态金属那样高配位。
> 
> #### (b) 静态结构因子 S(Q)
> 
> -   横轴：波矢 **Q, Å⁻¹**
> -   出现主峰及肩峰
> -   肩峰接近 **2kF ≈ 3.46 Å⁻¹**
> 
> 这表明液态Ge带有自由电子/Friedel振荡特征。
> 
> #### (c) 键角分布
> 
> -   横轴：角度 **deg**
> -   分布很宽
> -   仅有较弱四面体倾向，仍有接近60°的紧密堆积角
> 
> 说明液态Ge的局域结构无单一规则，而是多种局域构型并存。
> 
> #### (d) 电子态密度 DOS
> 
> -   横轴：能量 **eV**
> -   液态仍金属化，费米能级附近有非零DOS
> -   但在约 **-4.5 eV** 附近出现赝隙（pseudogap）
> 
> **重要解释**：液态Ge虽是金属，但不是“简单金属”，而是保留了一部分与s-p分裂相关的结构特征。
> 
> * * *
> 
> ### 图6：过冷液态Ge（750–650 K）
> 
> 与图5同构，但变化明显：
> 
> -   g(R)首峰更尖锐，第二峰增强
> -   配位数下降到 **4.63**
> -   键角分布中 **109°附近四面体角占优**
> -   DOS在费米能附近下降，但尚未开真正带隙
> 
> **结论**：这是一个**仍具流动性的金属过冷液体**，但局域上已明显向四面体共价网络演化。
> 
> * * *
> 
> ### 图7：淬火后非晶Ge（300 K）
> 
> -   首峰/第二峰分裂更清楚
> -   配位数约 **4.04**
> -   键角以 **107.7°** 为中心，接近理想四面体 **109.5°**
> -   DOS在费米能级附近显著降低，出现半导体特征
> 
> 但：
> 
> -   带隙并未完全干净，仍有缺陷态
> 
> **含义**：快速淬火已生成较合理非晶网络，但缺陷仍较多。
> 
> * * *
> 
> ### 图8：退火后非晶Ge（300 K）
> 
> 与图7相比：
> 
> -   g(R)中程有序性更好
> -   DOS更接近实验
> -   费米能级附近缺陷态减少
> 
> 但配位数仍约 **4.05**，说明退火并未明显减少过/欠配位总数，而是**改善了网络组织方式和电子结构质量**。
> 
> * * *
> 
> ### 表1：晶体Ge基准性质
> 
> 包括：
> 
> -   内聚能 **eV**
> -   平衡体积 **Å³**
> -   晶格常数 **Å**
> -   体模量 **Mbar**
> 
> 主要用于说明赝势与DFT设定可靠。
> 
> * * *
> 
> ### 表2：淬火与退火历史
> 
> 记录每个阶段：
> 
> -   时间步数
> -   起止温度 **K**
> -   降温/升温速率 **K s⁻¹**
> 
> 说明作者并非“一次性快淬”，而是分段控温，尤其在750–450 K区间放慢速率，因为这是结构重组最关键的区间。
> 
> * * *
> 
> ### 表3：最近邻距离、配位数、键角统计
> 
> 关键趋势：
> 
> -   液态：**d₁≈2.75 Å, Nc≈6, θ≈99°**
> -   过冷液态：**d₁≈2.63 Å, Nc≈4.63, θ≈103°**
> -   非晶态：**d₁≈2.48 Å, Nc≈4.0, θ≈108°**
> 
> 这张表非常重要，直接给出金属→半导体转变的局域几何标志。
> 
> * * *
> 
> ### 表4：配位数分布
> 
> 显示每种状态下3、4、5、6、7、8配位原子的百分比。
> 
> 关键信息：
> 
> -   液态：4–8配位广泛分布
> -   过冷液态：4、5配位为主
> -   非晶态：绝大多数为4配位，仍残留少量3配位与5配位缺陷
> 
> * * *
> 
> ### 图9：扩散系数随温度变化
> 
> -   纵轴：扩散系数 **cm²/s**
> -   随温度下降快速减小
> 
> 说明750 K附近虽已强烈局域有序化，但尚未彻底失去流动性。
> 
> * * *
> 
> ### 图10：速度自相关函数
> 
> -   液态：有衰减振荡，说明扩散与“笼困效应”共存
> -   非晶态：扩散背景消失，仅剩振动相关
> 
> * * *
> 
> ### 图11：液态速度自相关谱
> 
> -   出现低频扩散峰和约 **30 meV** 的非弹性峰
> -   对应集体密度涨落或类纵向声学模
> 
> * * *
> 
> ### 图12：非晶Ge振动态密度
> 
> 与中子散射实验符合较好。 谱中可辨认：
> 
> -   TA：横向声学
> -   LA：纵向声学
> -   LO：纵向光学
> -   TO：横向光学
> 
> 说明非晶Ge虽无长程有序，但局域振动模式仍保留晶体记忆。
> 
> * * *
> 
> ### 图13：两个T=0非晶构型的 g(R)
> 
> 比较慢淬火和快淬火后再做静态弛豫得到的两个构型。
> 
> -   总体相似
> -   缺陷数略不同
> -   提示缺陷统计对热历史敏感
> 
> * * *
> 
> ### 表5：缺陷构型统计
> 
> 研究不同截断半径下的3配位/5配位数量及其几何参数。 作者强调：
> 
> -   缺陷计数高度依赖“最近邻定义”
> -   几何定义并不稳健
> 
> * * *
> 
> ### 图14：缺陷处电子密度图
> 
> 这是全文最有洞察力的图之一。
> 
> 展示：
> 
> -   正常四配位位点有清晰键中电荷
> -   三配位缺陷存在“悬挂键（dangling bond）”倾向
> -   五配位缺陷往往不是5个等强键，而是“3–4强键 + 1–2弱键”
> 
> **结论**：五配位缺陷更接近“浮动键（floating bond）/弱键缺陷”，不是简单多一个正常共价键。
> 
> * * *
> 
> ### 图15：带隙态电子密度
> 
> 显示某局域能级（band 128）高度局域在特定缺陷附近，尤其与18号原子局域结构相关。
> 
> 说明：
> 
> -   并非所有几何缺陷都产生带隙态
> -   只有某些伴随强畸变与异常成键的局域结构，才生成显著局域电子态
> 
> * * *
> 
> ### 图16：300 K下带边能级随时间涨落
> 
> 说明带隙附近态对热涨落极其敏感。 这意味着：
> 
> -   缺陷态不是完全静态的
> -   非晶半导体电子性质带有明显瞬时结构依赖性
> 
> * * *
> 
> ## 四、正文核心内容剖析
> 
> ### 4.1 研究背景：为什么经典势不够？
> 
> 作者指出，对于Si/Ge这一类材料，液态与非晶态的成键机制差别太大：
> 
> -   液态更金属化，高配位
> -   非晶态更共价化，近四配位
> 
> 经典势通常在一个相区调得不错，但跨相态可迁移性差。尤其是：
> 
> -   会高估液态中的四面体趋势，或
> -   淬火后得到过配位、仍金属的“假非晶”
> 
> 这背后的根本原因是：**原子间作用力具有强构型依赖性（configuration dependence）**，简单两体/三体经验势难以准确捕捉。
> 
> * * *
> 
> ### 4.2 方法论创新：直接能量最小化AIMD
> 
> 作者相较Car-Parrinello方法的创新点是：
> 
> #### （1）有限温度DFT
> 
> 使用Mermin形式的有限温度DFT，自然允许**分数占据（fractional occupation）**，这对金属体系尤其重要，因为金属中能级交叉频繁。
> 
> #### （2）每一步都做电子态最小化
> 
> 这确保系统始终位于**Born-Oppenheimer势能面**附近，避免非绝热漂移。
> 
> #### （3）共轭梯度迭代
> 
> 作者使用预条件共轭梯度法高效求解电子基态，使得“每步最小化”在计算上可行。
> 
> #### （4）Nosé动力学
> 
> 生成正则系综，使离子温度可控。
> 
> 核心结论是：虽然每步都最小化电子结构，看似昂贵，但因为时间步可以比CP更大，总体效率并不差。
> 
> * * *
> 
> ### 4.3 模拟设置
> 
> 主要参数包括：
> 
> -   64个Ge原子
> -   立方周期盒
> -   138条能带
> -   高斯展宽 **σ=0.2 eV**
> -   平面波截断 **12 Ry**
> -   电荷密度网格 **32×32×32**
> -   时间步长 **3×10⁻¹⁵ s = 3 fs**
> 
> 总模拟时长超过 **30 ps**，在1994年这是相当可观的。
> 
> * * *
> 
> ### 4.4 液态Ge：不是普通金属液体
> 
> 液态Ge结构特征：
> 
> -   最近邻距离约 **2.75 Å**
> -   配位数约 **6**
> -   键角分布很宽
> -   DOS费米能级处非零，表现为金属性
> -   但存在明显赝隙与一定局域结构倾向
> 
> 这说明液态Ge不是“高密度简单金属液体”，而是具有一定共价残余的复杂金属液体。
> 
> * * *
> 
> ### 4.5 过冷液态：四面体网络开始萌芽
> 
> 随着冷却到750–650 K：
> 
> -   配位数明显降到接近4.6
> -   键角向109°集中
> -   DOS费米能级下降，但未开隙
> -   扩散仍存在
> 
> 也就是说，系统先经历的是**局域结构共价化**，然后才是**动力学冻结和带隙形成**。这是论文对转变机制的重要解释。
> 
> * * *
> 
> ### 4.6 非晶Ge：快速淬火也能得到真实网络
> 
> 作者最强调的结论之一是：
> 
> > 使用准确量子多体力，即便较快淬火，也能得到较真实的四配位非晶半导体。
> 
> 这与经验势形成对比。经验势往往必须：
> 
> -   极慢淬火，或者
> -   人为加强三体项
> 
> 而在AIMD中，共价网络是自然“长出来”的，而不是被势函数“硬拉出来”的。
> 
> * * *
> 
> ### 4.7 缺陷分析：几何、成键、电子三位一体
> 
> 作者对缺陷的理解相当现代：
> 
> #### 几何缺陷
> 
> 按配位数可分为：
> 
> -   **T3**：三配位，类似悬挂键
> -   **T5**：五配位，类似浮动键/弱键缺陷
> 
> #### 成键缺陷
> 
> 真正的物理缺陷不应只看邻居个数，还应看：
> 
> -   是否存在明显键中电荷
> -   各键是否等强
> -   是否只是“长而弱的附加连接”
> 
> #### 谱学缺陷
> 
> 更关键的是：
> 
> -   是否产生带隙中的局域态
> -   是否导致电子高度局域
> 
> 作者发现：
> 
> -   并非所有T3/T5都产生带隙态
> -   某些强畸变局域构型才真正是电子活性缺陷
> 
> 这比“悬挂键=缺陷”更深入。
> 
> * * *
> 
> ## 五、结论与贡献
> 
> ### 核心结论
> 
> 1.  作者成功用AIMD模拟了Ge从液态金属到非晶半导体的转变全过程。
> 2.  模拟结果在结构、电子与动力学性质上都与实验较一致。
> 3.  金属—半导体转变伴随：
>     -   配位数下降
>     -   四面体局域结构增强
>     -   费米能附近DOS下降并开出伪隙/带隙
> 4.  非晶Ge中既有三配位也有五配位缺陷。
> 5.  缺陷不能仅用几何配位数定义，必须联合成键与电子态分析。
> 
> ### 主要贡献
> 
> -   方法上：展示了**直接能量最小化AIMD**在金属液体与相变问题上的可行性。
> -   物理上：阐明了Ge液态—非晶转变中的结构—电子耦合机制。
> -   材料学上：给出了较真实的非晶Ge模型。
> -   概念上：推进了对非晶缺陷“几何缺陷≠电子缺陷”的认识。
> 
> * * *
> 
> ## 六、未来发展方向展望
> 
> 结合作者原文和后续可自然延伸的方向，未来研究可从以下几方面展开：
> 
> ### 1. 更大体系尺寸
> 
> 本文仅用64原子，适合短程结构分析，但：
> 
> -   中程有序
> -   缺陷统计
> -   局域化态分布  
>     都可能受有限尺寸影响。
> 
> ### 2. 更长时间尺度
> 
> 30 ps在当时很先进，但对：
> 
> -   缺陷生成/湮灭
> -   稀有重排事件
> -   更真实退火过程  
>     仍显不足。
> 
> ### 3. 更精确电子结构
> 
> 局域密度近似（LDA）常低估带隙，因此对：
> 
> -   带隙态位置
> -   缺陷态能量
> -   电子局域长度  
>     可能仍有系统误差。
> 
> ### 4. 向Si、GaAs、过渡金属体系推广
> 
> 作者文末明确提到过渡金属是下一步挑战。
> 
> ### 5. 非晶缺陷的动态谱学研究
> 
> 图16已说明缺陷态会热涨落。未来可进一步研究：
> 
> -   温度依赖的缺陷态寿命
> -   光致激发后的局域重构
> -   与电子输运、俘获复合的关系
> 
> _可视化提示：可做“方法拓展—体系拓展—时间尺度拓展—电子结构精度拓展”的路线图。_
> 
> * * *
> 
> ## 七、学术思考与批判性分析
> 
> ### 1. 64原子体系是否足以代表真实非晶Ge？
> 
> 这是本文最大限制之一。短程结构也许可靠，但中程有序、环统计、缺陷相关长度都可能受限制。
> 
> ### 2. 淬火速率极高是否影响缺陷浓度？
> 
> 论文虽证明快速淬火也能生成合理非晶网络，但实验中的冷却路径复杂得多。缺陷比例与局域结构可能仍偏离真实样品。
> 
> ### 3. LDA低估带隙会不会影响“谱学缺陷”的判定？
> 
> 有可能。某些“带隙态”在更高精度泛函下位置会变化，因此电子缺陷分析的定量性需谨慎。
> 
> ### 4. 几何缺陷与电子缺陷不对应，这是否意味着配位统计意义有限？
> 
> 并非无意义，但说明配位数只是缺陷分析的第一层。真正材料功能相关的是成键强弱、应变场、电子局域态。
> 
> ### 5. 退火后缺陷数未明显减少但电子性质改善，这说明什么？
> 
> 说明改善非晶质量未必靠“减少缺陷个数”，也可能靠：
> 
> -   弱键重分配
> -   应变释放
> -   缺陷态去局域化
> -   中程网络优化
> 
> 这是非常有启发性的结果。
> 
> * * *
> 
> ## 八、用户问题预测与解答
> 
> ### 问题1：这篇论文的核心创新到底是方法还是材料结论？
> 
> 两者都有，但首要创新是**方法学**。作者证明了“每一步直接最小化电子能量”的AIMD可以有效处理金属液体与金属—半导体转变问题。在此基础上，才得到可靠的材料结论。
> 
> ### 问题2：为什么液态Ge是金属，而非晶Ge是半导体？
> 
> 因为液态Ge中原子高配位、局域结构混乱、电子更离域化，费米能级附近有连续态；而非晶Ge形成近四配位四面体共价网络，电子态重新组织，在费米能附近形成低DOS甚至带隙。
> 
> ### 问题3：为什么经典分子动力学做不好这个问题？
> 
> 因为经验势难以同时适应液态金属键和非晶共价键，两种相的成键机制差异太大。第一性原理方法能根据瞬时电子结构自洽地产生原子力，因此更有可迁移性。
> 
> ### 问题4：三配位缺陷和五配位缺陷谁更重要？
> 
> 论文表明两者都存在，而且不能只凭配位数判断重要性。真正关键的是该缺陷是否：
> 
> -   破坏局域共价成键
> -   引入带隙局域态
> -   对电子输运或EPR信号有贡献
> 
> ### 问题5：退火为什么能改善结果？
> 
> 退火让系统有机会跨越局域势垒，重组网络，释放局部应变，优化弱键分布，因此即便总缺陷数变化不大，结构与电子性质仍会更接近实验。
> 
> ### 问题6：文中“赝隙（pseudogap）”是什么意思？
> 
> 它不是完全没有电子态的真正带隙，而是某个能量区间中电子态密度明显降低。液态Ge在约-4.5 eV附近的赝隙说明其电子结构不是简单自由电子型。
> 
> ### 问题7：为什么作者强调“几何缺陷不一定是谱学缺陷”？
> 
> 因为一个原子即便是3配位或5配位，也不一定产生费米能附近局域态；反过来，强应变但配位数正常的局域结构也可能产生电子异常。材料电子性质最终由电子波函数分布决定，而不只由邻居个数决定。
> 
> * * *
> 
> ## 九、专区：便于 Obsidian Dataview 插件调用
> 
> 领域基础知识:: 非晶半导体尤其是Si/Ge体系的关键难点在于其液态与固态成键机制差异显著：液态通常表现为高配位金属性，非晶固态则接近四配位共价半导体。传统衍射实验主要提供对关联函数等一维信息，难以完全重建三维结构，因此需要结合第一性原理分子动力学进行“计算机实验”。
> 
> 研究背景:: 传统经典分子动力学基于经验两体或三体势，虽可较好描述液态Ge的部分结构，但在模拟液态金属到非晶半导体转变时，常得到过配位且仍呈金属性的非真实非晶结构。根本原因是该相变中原子间作用力具有强构型依赖性，必须实时计算量子力学多体力。
> 
> 作者的问题意识:: 作者关注的核心问题是：是否可以用严格第一性原理、且对金属体系绝热性有良好控制的分子动力学方法，真实模拟Ge从液态金属到非晶半导体的转变，并揭示结构、电子与缺陷性质如何协同演化。
> 
> 主要研究对象:: 研究对象是锗（Ge）在液态、过冷液态、淬火非晶态与退火非晶态中的原子结构、电子结构、动力学性质以及局域缺陷，包括三配位、四配位、五配位局域环境及其相关带隙态。
> 
> 主要研究方法:: 采用基于有限温度密度泛函理论的第一性原理分子动力学，结合每个MD步后的直接能量最小化、预条件共轭梯度迭代、非局域赝势、Nosé正则系综动力学，对64原子Ge体系进行总时长约30 ps的液态—淬火—退火模拟，并分析g(R)、S(Q)、键角分布、DOS、扩散系数、速度自相关函数与缺陷电子密度。
> 
> 研究意义:: 该研究证明了AIMD可以跨越液态金属与非晶半导体两个成键机制截然不同的相区，建立更可信的非晶Ge模型，并为理解金属—半导体转变、缺陷形成机制及非晶半导体结构—电子关系提供了可靠的微观依据。
> 
> 研究结论:: 液态Ge表现为低于普通金属的中等配位金属液体，冷却后先形成具有明显四面体倾向的过冷液态，再转变为近四配位的非晶半导体；结构、动力学和电子性质与实验吻合较好；非晶Ge中同时存在三配位与五配位缺陷，但几何缺陷不必然对应带隙电子缺陷，必须结合成键与谱学特征联合判定。
> 
> 对领域的贡献:: 论文的方法学贡献在于展示了直接能量最小化型AIMD对金属体系和相变过程的可行性；物理贡献在于揭示Ge液态—非晶转变中配位降低、四面体局域重建、DOS开隙及缺陷态形成之间的耦合关系；概念贡献在于推动了“缺陷应从几何、成键、电子三层面综合定义”的认识。
> 
> 未来研究方向提及:: 作者明确提出应将该方法推广到更复杂的金属体系，尤其是过渡金属，并指出通过超软赝势可进一步提升这类体系AIMD模拟的可行性；同时，缺陷谱学性质与动态涨落仍有待进一步深入研究。
> 
> 未来研究方向思考:: 后续研究可从扩大体系尺寸、延长模拟时间、采用更高精度交换关联泛函、统计中程有序与环结构、研究温度依赖缺陷态寿命及其与输运/光电子性质的关系等方面推进，从而更完整地连接第一性原理结构模型与真实非晶器件性能。
> 
> 🚀 [笔记回链](zotero://select/library/items/KK9AL2U5)
> 
> * * *
> 
> `GPT 自定 ②`  `gpt-5.4`  _由批量 AI 解读自动生成于 2026/5/6 05:39:33_
> 
> 🏷️ #🤖️/AI文献解读 🏷️ #🤖️/AI文献阅读

^KEYCC65C59D

## <span style="color: rgb(0, 174, 137);">❷ 🤖️ 论文双语转写📌</span>

> 🚀 [笔记回链](zotero://select/library/items/3SQWDEV5)

^KEYaiPaper0

> <span class="AIReading">🤖 AI 解读，快人一步</span>
> 
> > 用户要求将一篇英文物理学期刊论文转换为结构化的双语Markdown格式。这是一篇关于锗的液态金属-非晶半导体转变的从头计算分子动力学模拟论文，发表于1994年Physical Review B。
> > 
> > 我需要按照系统指令完成以下任务：
> > 
> > 1.  识别PDF文本中的结构元素（标题、段落、列表、引用、表格等）
> > 2.  对每个单元进行双语转换（英文原文+中文翻译）
> > 3.  标注首次出现的核心术语并解释
> > 4.  严格遵循CommonMark格式规范
> > 
> > 文本结构分析：
> > 
> > -   开头是论文标题和作者信息
> > -   摘要部分
> > -   I. INTRODUCTION 引言
> > -   后续有II. THEORY等章节
> > -   包含表格、图表说明、参考文献
> > 
> > 我会按照要求处理每个结构单元，保持原文层级关系，添加术语解释。对于较长的段落，我会保持原文完整性，提供准确的中文翻译。技术术语如"ab initio"、"density-functional theory"、"pseudopotential"等会在首次出现时标注解释。
> > 
> > 现在开始处理文本。
> 
> # PHYSICAL REVIEW 8 VOLUME 49, NUMBER 20 15 MAY 1994-II
> 
> 物理评论 B 第49卷 第20期 1994年5月15日-II
> 
> # Ab initio molecular-dynamics simulation of the liquid-metal—amorphous-semiconductor transition in germanium
> 
> 锗中液态金属-非晶半导体转变的从头计算分子动力学模拟
> 
> G. Kresse and J. Hafner G. Kresse 与 J. Hafner
> 
> Institut für Theoretische Physik, Technische Universität Wien, Wiedner Hauptstraße 8—10, A-1040 Wien, Austria (Received 16 December 1993) 奥地利维也纳工业大学理论物理研究所，Wiedner Hauptstraße 8—10, A-1040 Wien, 奥地利（1993年12月16日收稿）
> 
> **ab initio**: 从头计算法，一种基于量子力学第一性原理、不依赖经验参数的计算方法。 **molecular-dynamics (MD)**: 分子动力学，通过数值求解粒子运动方程来模拟物理系统随时间演化的计算方法。 **amorphous-semiconductor**: 非晶半导体，原子排列缺乏长程有序性的半导体材料。
> 
> * * *
> 
> We present ab initio quantum-mechanical molecular-dynamics simulations of the liquid-metal-amorphous-semiconductor transition in Ge. Our simulations are based on (a) finite-temperature density-functional theory of the one-electron states, (b) exact energy minimization and hence calculation of the exact Hellmann-Feynman forces after each molecular-dynamics step using preconditioned conjugate-gradient techniques, (c) accurate nonlocal pseudopotentials, and (d) Nosé dynamics for generating a canonical ensemble. This method gives perfect control of the adiabaticity of the electron-ion ensemble and allows us to perform simulations over more than 30 ps. The computer-generated ensemble describes the structural, dynamic, and electronic properties of liquid and amorphous Ge in very good agreement with experiment. The simulation allows us to study in detail the changes in the structure-property relationship through the metal-semiconductor transition. We report a detailed analysis of the local structural properties and their changes induced by an annealing process. The geometrical, bonding, and spectral properties of defects in the disordered tetrahedral network are investigated and compared with experiment.
> 
> 我们报道了锗（Ge）中液态金属-非晶半导体转变的从头计算量子力学分子动力学模拟。我们的模拟基于：(a) 单电子态的有限温度密度泛函理论；(b) 精确能量最小化，并因此在每个分子动力学步骤之后使用预条件共轭梯度技术计算精确的Hellmann-Feynman力；(c) 精确的非局域赝势；以及(d) 用于生成正则系综的Nosé动力学。该方法能够完美控制电子-离子系综的绝热性，并允许我们进行超过30皮秒的模拟。计算机生成的系综描述了液态和非晶锗的结构、动力学和电子性质，与实验吻合非常好。该模拟使我们能够详细研究金属-半导体转变过程中结构-性质关系的变化。我们报告了对局域结构性质及其在退火过程中所诱发变化的详细分析。研究了无序四面体网络中缺陷的几何、成键和光谱性质，并与实验进行了比较。
> 
> **density-functional theory (DFT)**: 密度泛函理论，一种基于电子密度而非波函数来描述多电子体系基态性质的量子力学方法。 **Hellmann-Feynman forces**: Hellmann-Feynman力，通过对量子力学体系总能量求原子位置导数得到的原子间作用力。 **preconditioned conjugate-gradient techniques**: 预条件共轭梯度技术，通过变换搜索方向加速收敛的数值优化方法。 **pseudopotentials**: 赝势，用于简化电子结构计算的有效势，替代真实离子势以减少计算量。 **Nosé dynamics**: Nosé动力学，一种通过引入额外自由度在分子动力学模拟中生成正则系综的方法。 **canonical ensemble**: 正则系综，具有固定粒子数、体积和温度的统计力学系综。 **adiabaticity**: 绝热性，电子态相对于离子运动保持基态的绝热演化特性。
> 
> * * *
> 
> # I. INTRODUCTION
> 
> # I. 引言
> 
> Amorphous materials are of interest in materials science on both the basic and technological levels. Particularly challenging are the structural properties of these materials which have been the subject of numerous experimental and theoretical studies and controversy. For a crystalline structure, the complete set of atomic coordinates may be derived from diffraction experiments. For liquid and amorphous materials, diffraction experiments yield only a one-dimensional projection of the real three-dimensional structure in the form of a pair-correlation function. Information on three- and many-body correlations from other types of experiments (e.g., extended x-ray-absorption fine-structure, x-ray-absorption near-edge structure, etc.) is rather uncertain and incomplete.
> 
> 非晶材料在基础科学和技术层面上都对材料科学具有重要意义。尤其具有挑战性的是这些材料的结构性质，它们一直是众多实验和理论研究以及争议的主题。对于晶体结构，完整的原子坐标集合可以通过衍射实验导出。对于液态和非晶材料，衍射实验仅以对关联函数的形式产生真实三维结构的一维投影。来自其他类型实验（如扩展X射线吸收精细结构、X射线吸收近边结构等）的三体和多体关联信息相当不确定且不完整。
> 
> **pair-correlation function**: 对关联函数，描述距参考原子给定距离处找到另一原子概率的统计函数。 **extended x-ray-absorption fine-structure (EXAFS)**: 扩展X射线吸收精细结构，通过分析X射线吸收谱的振荡部分获取局域结构信息的技术。 **x-ray-absorption near-edge structure (XANES)**: X射线吸收近边结构，通过分析吸收边附近谱图特征获取电子结构和几何信息的技术。
> 
> * * *
> 
> Therefore, to explore the structure of amorphous materials in sufficient detail, the laboratory experiment must be supplemented with a computer experiment. One may distinguish three different strategies for the computer modeling of amorphous structures: (a) accretion, i.e., the sequential addition of atoms to a growing cluster; (b) randomization and relaxation: a highly random structure is created by disordering a regular structure (for amorphous Si or Ge, for example, one starts from a diamond structure and introduces disorder by switching nearest-neighbor bonds) and relaxing towards a low-energy structure which is still random; (c) molecular dynamics. Processes (a) and (b) produce results that are strongly biased by the details of the growth, respectively, randomization algorithm and by the interatomic force field used in the relaxation. Molecular dynamics is recommendable since the results depend only on the quality of the interatomic potentials. Indeed molecular dynamics has been applied with much success to the simulation of liquid and amorphous metals and salts, based on potentials that are essentially parameter free and derived from first principles. The more difficult case is that of the semiconducting elements and compounds, especially of those materials that are semiconducting and fourfold coordinated in the solid (crystalline or amorphous) phase, but metallic with a higher coordination number (N_c ≥ 6) in the liquid state. This is the case for the semiconducting elements Si and Ge and for the III-V compounds like Ga-As.
> 
> 因此，为了足够详细地探索非晶材料的结构，实验室实验必须辅以计算机实验。可以区分三种不同的非晶结构计算机建模策略：(a) 增积法，即原子依次添加到不断增长的团簇上；(b) 随机化与弛豫法：通过使规则结构无序化（例如对于非晶硅或锗，从金刚石结构出发，通过交换最近邻键引入无序）并弛豫到仍保持随机性的低能结构；(c) 分子动力学法。过程(a)和(b)产生的结果严重受生长/随机化算法的细节以及弛豫中使用的原子间力场的影响。分子动力学是值得推荐的，因为其结果仅取决于原子间势的质量。事实上，基于基本上无参数且从第一性原理导出的势，分子动力学已成功应用于液态和非晶金属及盐类的模拟。更困难的情况是半导体元素和化合物，特别是那些在固态（晶体或非晶）相中呈半导体性和四重配位，但在液态下呈金属性且具有较高配位数（N_c ≥ 6）的材料。半导体元素Si和Ge以及III-V族化合物如Ga-As就属于这种情况。
> 
> **coordination number**: 配位数，描述中心原子最近邻原子数目的结构参数。 **interatomic potentials**: 原子间势，描述原子间相互作用能量随原子间距变化的函数。
> 
> * * *
> 
> Classical molecular dynamics simulations based on effective pair and volume forces derived from pseudopotential- and linear-response theories describe the liquid structure of Si, Ge, and GaAs remarkably well, but a simulated quench using these potentials leads to an overcoordinated amorphous material (N_c ≈ 5) that is still metallic. The reason is that the linear response of the electron gas is unable to describe the profound modification of the interatomic forces that accompanies the liquid-metal to amorphous-semiconductor transition. Since quantum-mechanical techniques for calculating three- and many-body forces in covalently bonded materials are still in their infancy, large efforts have been directed towards the construction of empirical two- and three-body potentials for Si and Ge, supported by a large basis of data from experiment and ab initio calculations. The application to the simulation of liquid and amorphous phases shows that the transferability of these potentials is limited: for the liquid phase, the influence of tetrahedral bonding is overestimated, but nonetheless the recovery of a nearly perfectly fourfold-coordinated structure on cooling appears to be very difficult. A realistic description of the amorphous fourfold-coordinated network is achieved only if the strength of the three-body forces is artificially enhanced during cooling. If this is not done, extremely low quenching rates are required, in spite of the fact that the local tetrahedral order is overestimated in the liquid. Again, these difficulties reflect the configuration dependence of the interatomic forces. Hence the challenge is to calculate the full set of quantum mechanical many-body forces for each instantaneous atomic configuration of the system. This is now possible using the ab initio molecular dynamics (MD) techniques pioneered by Car and Parrinello.
> 
> 基于赝势和线性响应理论导出的有效对势和体积力的经典分子动力学模拟，很好地描述了Si、Ge和GaAs的液态结构，但使用这些势进行模拟淬火会导致过配位的非晶材料（N_c ≈ 5），该材料仍呈金属性。原因是电子气的线性响应无法描述伴随液态金属-非晶半导体转变的原子间力的深刻变化。由于共价键合材料中三体和多体力计算的量子力学技术仍处于起步阶段，大量努力已转向构建Si和Ge的经验两体和三体势，并得到了大量来自实验和从头计算数据的支持。在液态和非晶相模拟中的应用表明，这些势的可转移性是有限的：对于液相，四面体成键的影响被高估了，但即便如此，在冷却时恢复到近乎完美的四重配位结构似乎非常困难。对非晶四重配位网络的现实描述仅在冷却过程中人为增强三体力强度时才能实现。如果不这样做，尽管液态中局域四面体有序被高估了，仍需要极低的淬火速率。这些困难再次反映了原子间力的构型依赖性。因此，挑战在于为系统的每个瞬时原子构型计算全套量子力学多体力。这现在可以通过Car和Parrinello开创的从头计算分子动力学（MD）技术来实现。
> 
> **linear-response theory**: 线性响应理论，描述系统对外部微扰的一阶响应的理论框架。 **quench**: 淬火，将系统从高温快速冷却到低温的过程，常用于制备非晶结构。 **tetrahedral bonding**: 四面体成键，原子与其四个最近邻形成指向四面体顶点的共价键的成键构型。 **transferability**: 可转移性，势函数在不同化学环境或结构条件下保持准确性的能力。
> 
> * * *
> 
> The aim of the ab initio MD approach is to perform a simulation in which the interatomic forces are derived directly from the electronic ground state [calculated within density functional theory (DFT)] using the Hellmann-Feynman theorem. In other words, for a given atomic configuration {R_I} the Born-Oppenheimer (BO) potential energy surface E_BO[{R_I}] is obtained by minimizing the total-energy functional E[{R_I}, ψ_i] with respect to the one-electron states ψ_i. The force acting on an atom at the site R_I is then given as the derivative of E_BO[{R_I}] with respect to R_I. In the original Car-Parrinello (CP) method, instead of minimizing the total energy at any step of the simulation, the simultaneous time evolution of both the ionic and the electronic degrees of freedom is determined by integrating the following coupled equations of motion.
> 
> 从头计算MD方法的目标是进行这样的模拟：其中原子间力直接由电子基态[在密度泛函理论（DFT）范围内计算]使用Hellmann-Feynman定理导出。换言之，对于给定的原子构型{R_I}，Born-Oppenheimer（BO）势能面E_BO[{R_I}]通过最小化总能量泛函E[{R_I}, ψ_i]相对于单电子态ψ_i而获得。作用在位点R_I处原子上的力则作为E_BO[{R_I}]对R_I的导数给出。在原始的Car-Parrinello（CP）方法中，不是在模拟的每一步最小化总能量，而是通过积分以下耦合运动方程来确定离子和电子自由度的同时时间演化。
> 
> **Born-Oppenheimer (BO) potential energy surface**: Born-Oppenheimer势能面，在绝热近似下，电子基态能量作为原子核坐标函数的势能面。 **Car-Parrinello (CP) method**: Car-Parrinello方法，通过同时演化电子和离子自由度进行从头计算分子动力学模拟的方法。
> 
> * * *
> 
> Equation (1) is just the usual Newtonian equation of motion (EOM) for the ions with the forces calculated according to the Hellmann-Feynman theorem and Eq. (2) (where the Λ_ij are Lagrange multipliers for the orthonormality constraints to the wave functions and μ is a fictitious mass for the electronic degrees of freedom) is a pseudo-Newtonian equation of motion for the electronic degrees of freedom. The integration of the coupled EOM is started after the electronic wave functions have been relaxed to their ground state. The CP equations have been applied quite successfully to a number of systems, including the liquid and amorphous forms of Si. Since the electronic wave functions of DFT are meaningful only if the electrons are in their ground state for the given ionic configuration, an essential condition for the practicability of the CP method is that the transfer of energy between the ionic and electronic subsystems is small to prevent the electron state from drifting away from the adiabatic or BO surface. In insulators or semiconductors, the width of the electronic band gap divided by the fictitious mass μ of the electronic degrees of freedom defines the separation of the characteristic frequencies of the ionic and electronic motions. In metals this separation is absent and the essential mechanism that drives metallic systems into nonadiabaticity is level crossing between occupied and empty electron states.
> 
> 方程(1)正是离子的通常牛顿运动方程（EOM），其力根据Hellmann-Feynman定理计算，而方程(2)（其中Λ_ij是波函数正交归一约束的Lagrange乘子，μ是电子自由度的虚构质量）是电子自由度的伪牛顿运动方程。耦合EOM的积分在电子波函数弛豫到其基态之后开始。CP方程已相当成功地应用于许多系统，包括Si的液态和非晶形式。由于DFT的电子波函数仅在电子处于给定离子构型的基态时才有意义，CP方法可行性的一个基本条件是离子和电子子系统之间的能量转移很小，以防止电子态偏离绝热或BO面。在绝缘体或半导体中，电子带隙宽度除以电子自由度的虚构质量μ定义了离子和电子运动特征频率的分离。在金属中，这种分离不存在，驱使金属系统进入非绝热性的基本机制是占据态和空电子态之间的能级交叉。
> 
> **Lagrange multipliers**: 拉格朗日乘子，在约束优化中引入的辅助变量，用于强制执行约束条件。 **band gap**: 带隙，半导体或绝缘体中价带顶部与导带底部之间的能量区间。 **level crossing**: 能级交叉，不同电子态的能量随原子构型变化而彼此交叉的现象。
> 
> * * *
> 
> The operational solution for this nonadiabaticity problem is (a) performing periodic energy minimizations to "bring the system back to the BO surface" or (b) attaching the electronic subsystem to a Nosé thermostat that prevents the heating up of the electron system. Since both the periodic energy minimizations and the thermalization of the electron states break the microcanonical evolution of the coupled electron-ion system, control of the temperature of the ions is possible only if the ions are coupled to a second Nosé thermostat. This is equivalent to inclusion of additional forces in Eqs. (1) and (2) which describe the coupling to two external heat baths serving to keep the average ionic temperature constant and equal to a prescribed value T and to limit the distance of the electrons from the BO surface. It is clear that the nonadiabaticity problems are relevant to the simulation of liquid-metal—amorphous-semiconductor transition.
> 
> 此非绝热性问题的操作性解决方案是：(a) 执行周期性能量最小化以"将系统带回BO面"，或(b) 将电子子系统附加到一个Nosé恒温器上，以阻止电子系统升温。由于周期性能量最小化和电子态的热化都破坏了耦合电子-离子系统的微正则演化，只有将离子耦合到第二个Nosé恒温器上，才能控制离子温度。这等价于在方程(1)和(2)中包含额外的力，这些力描述与两个外部热浴的耦合，用于保持平均离子温度恒定且等于预设值T，并限制电子距BO面的距离。显然，非绝热性问题与液态金属-非晶半导体转变的模拟相关。
> 
> **Nosé thermostat**: Nosé恒温器，通过引入额外动力学变量来维持模拟系统在目标温度的理论方法。 **microcanonical evolution**: 微正则演化，在固定能量、体积和粒子数条件下系统的自然时间演化。
> 
> * * *
> 
> In the work of Stich et al. on liquid and amorphous Si the nonadiabaticity problem was handled by using a canonical ensemble (with the ionic Nosé thermostat), periodic electronic energy minimizations, and a large electronic mass parameter μ in the liquid state and during the quench and annealing phases, and a microcanonical ensemble, free evolution of the electron states and a small value of μ, during equilibration in the amorphous state. Empty electron states were ignored. The alternative is to perform the minimization of the DFT functional for the electronic energy at any time step of the MD simulation, so that the problem of nonadiabaticity does not arise at all. For the level-crossing problem, it is clear that instabilities in the evolution of the electron states can be avoided by allowing for variable fractional occupation numbers. Fractional occupancy of electron states appears very naturally in the finite temperature version of DFT.
> 
> 在Stich等人关于液态和非晶Si的工作中，非绝热性问题通过以下方式处理：在液态以及淬火和退火阶段使用正则系综（带有离子Nosé恒温器）、周期性电子能量最小化和大的电子质量参数μ，在非晶态平衡期间使用微正则系综、电子态自由演化和小的μ值。空电子态被忽略。另一种选择是在MD模拟的每个时间步执行DFT泛函的电子能量最小化，这样非绝热性问题就根本不会出现。对于能级交叉问题，显然可以通过允许可变分数占据数来避免电子态演化的不稳定性。电子态的分数占据在DFT的有限温度版本中非常自然地出现。
> 
> **fractional occupation numbers**: 分数占据数，允许电子态部分占据而非严格占据或空置的统计分布。 **equilibration**: 平衡，系统达到热力学平衡状态的过程。
> 
> * * *
> 
> In the present paper we report ab initio MD simulations of the liquid and amorphous phases of Ge based on (a) finite-temperature density-functional theory, (b) energy minimization after each MD step using an efficient iterative matrix-diagonalization scheme based on conjugate-gradient methods, (c) accurate nonlocal pseudopotentials evaluated in real space, and (d) a canonical ensemble in the Nosé formulation. In Sec. II we outline the basic ingredients of our technique and demonstrate that even from the point of view of computational efficiency, the method is at least comparable to the CP algorithm. Details of the simulation of the liquid phase and of the preparation of an amorphous sample using a simulated quench, as well as of the subsequent annealing treatment are given in Sec. III. The structural and electronic properties of the liquid, supercooled liquid, and amorphous phases are discussed in Sec. IV, including a detailed comparison with experiment. Some preliminary results on liquid Ge have been published recently in two short communications. The dynamical properties are described in Sec. V. Section VI analyzes the characteristic coordination and spectral defects in the quenched and annealed amorphous sample. The main results of our study are as follows. (a) We demonstrate the feasibility of fully dynamical simulations for liquid metals and of the simulation of quench condensation using ab initio MD techniques based on direct energy minimization. (b) Structural, dynamic, and electronic properties of the liquid and amorphous phases are in very good agreement with experiment. (c) Contrary to simulations using empirical many-body forces, the use of accurate quantum many-body forces allows us to prepare a realistic model structure for the amorphous semiconductor using a very rapid quench.
> 
> 在本文中，我们报道了基于以下方法的Ge液态和非晶相的从头计算MD模拟：(a) 有限温度密度泛函理论；(b) 每个MD步骤之后使用基于共轭梯度方法的高效迭代矩阵对角化方案进行能量最小化；(c) 在实空间中计算的精确非局域赝势；以及(d) Nosé公式下的正则系综。在第II节中，我们概述了技术的基本要素，并证明即使从计算效率的角度来看，该方法也至少与CP算法相当。液态相模拟、使用模拟淬火制备非晶样品以及随后退火处理的细节在第III节中给出。液态、过冷液态和非晶相的结构和电子性质在第IV节中讨论，包括与实验的详细比较。关于液态Ge的一些初步结果最近已在两篇简短通讯中发表。动力学性质在第V节中描述。第VI节分析了淬火和退火非晶样品中的特征配位和光谱缺陷。我们研究的主要结果如下：(a) 我们证明了使用基于直接能量最小化的从头计算MD技术对液态金属进行完全动力学模拟以及模拟淬火凝聚的可行性。(b) 液态和非晶相的结构、动力学和电子性质与实验吻合非常好。(c) 与使用经验多体力的模拟相反，使用精确的量子多体力使我们能够使用非常快速的淬火制备非晶半导体的现实模型结构。
> 
> **matrix-diagonalization**: 矩阵对角化，通过求解特征值问题计算哈密顿量矩阵的本征值和本征矢的数值过程。 **supercooled liquid**: 过冷液体，冷却到其正常凝固点以下而未结晶的液体。 **annealing**: 退火，通过加热和受控冷却来改变材料性质的热处理过程。
> 
> * * *
> 
> # II. THEORY: ab initio MD USING DIRECT ENERGY MINIMIZATION
> 
> # II. 理论：使用直接能量最小化的从头计算MD
> 
> Our ab initio MD routine is based on the following principles. (1) We use the finite-temperature version of the DFT developed by Mermin. Exchange correlation is described by the local-density functional of Ceperley and Alder. At finite temperature the free energy F[n(r), f_i, μ] depending on the electron density n(r), the Fermi-Dirac occupation probability f_i of the one-electron states ψ_i(r) [n(r) = Σ_i f_i|ψ_i(r)|²] and the chemical potential μ is the proper variational functional. The ground state may be found by minimizing F[n(r), f_i, μ] with respect to n(r), f_i and μ. It has been shown that even at finite temperature, the proper DFT force is equal to the Hellmann-Feynman force. Instead of the Fermi-Dirac broadening of the one-electron energies it may be computationally convenient to use a Gaussian broadening instead (see below). (2) The minimization of the total energy (respectively, the total free energy) is performed using an efficient matrix diagonalization scheme based on a variant of the conjugate-gradient techniques developed by Payne and co-workers and used in self-consistent electronic structure calculations by Bylander, Kleinman, and Lee. The method is a doubly iterative one: in the inner loop the wave functions and eigenvalues for each k point in the Brillouin zone and for each band are improved for a fixed potential V(r) by a preconditioned conjugate-gradient method until the change in the eigenvalue has dropped below a fixed threshold, i.e., the conjugate-gradient method is used as a tool for iterative calculation of the lowest eigenvalues (≈ 10% of all eigenvalues) of the large Hamilton matrix. After running over all bands (including some empty bands), a subspace diagonalization is performed, the Fermi energy and new partial occupancies are calculated, and the charge density n(r) and the potential V(r) are updated. (3) The atomic motion is described using Nosé dynamics generating a canonical ensemble. (4) After moving the atoms, the new wave functions are estimated using the subspace alignment scheme proposed by Arias et al. (5) The calculation has been performed using an optimized nonlocal pseudopotential in Kleinman-Bylander factorization using the real-space projection scheme.
> 
> 我们的从头计算MD程序基于以下原则。(1) 我们使用Mermin开发的DFT的有限温度版本。交换关联由Ceperley和Alder的局域密度泛函描述。在有限温度下，依赖于电子密度n(r)、单电子态ψ_i(r)的Fermi-Dirac占据概率f_i [n(r) = Σ_i f_i|ψ_i(r)|²]和化学势μ的自由能F[n(r), f_i, μ]是适当的变分泛函。可以通过最小化F[n(r), f_i, μ]相对于n(r)、f_i和μ来找到基态。已经证明，即使在有限温度下，适当的DFT力也等于Hellmann-Feynman力。替代单电子能量的Fermi-Dirac展宽，在计算上使用Gaussian展宽可能更方便（见下文）。(2) 总能量（分别为总自由能）的最小化使用基于Payne及其合作者开发的共轭梯度技术变体的高效矩阵对角化方案进行，该方案由Bylander、Kleinman和Lee用于自洽电子结构计算。该方法是一个双重迭代方法：在内循环中，对于固定势V(r)，通过预条件共轭梯度方法改进布里渊区中每个k点和每个能带的波函数和本征值，直到本征值的变化下降到固定阈值以下，即共轭梯度方法被用作迭代计算大哈密顿矩阵最低本征值（≈所有本征值的10%）的工具。在所有能带（包括一些空带）上运行之后，执行子空间对角化，计算费米能量和新的部分占据数，并更新电荷密度n(r)和势V(r)。(3) 原子运动使用生成正则系综的Nosé动力学描述。(4) 移动原子后，使用Arias等人提出的子空间对齐方案估计新波函数。(5) 计算使用优化的非局域赝势，采用Kleinman-Bylander分解，使用实空间投影方案进行。
> 
> **exchange correlation**: 交换关联，DFT中描述电子间交换和关联效应的能量项。 **local-density functional**: 局域密度泛函，基于局域电子密度近似交换关联能的DFT方法。 **Fermi-Dirac occupation probability**: 费米-狄拉克占据概率，描述电子在给定温度下占据各能态的概率分布。 **Brillouin zone**: 布里渊区，倒空间中代表周期性固体的原胞。 **Fermi energy**: 费米能量，在绝对零度下电子占据的最高能态的能量。 **Kleinman-Bylander factorization**: Kleinman-Bylander分解，将非局域赝势分解为可分离形式以简化计算的数值技术。
> 
> * * *
> 
> ## A. Finite-temperature density-functional theory
> 
> ## A. 有限温度密度泛函理论
> 
> At finite temperature, the proper variational functional is the free energy of the electrons, subject to the constraints of the orthonormality of the wave functions and of a constant number N_e of electrons, i.e. (for simplicity we restrict the formulation to a single k point)
> 
> 在有限温度下，适当的变分泛函是电子的自由能，受波函数正交归一性和恒定电子数N_e的约束，即（为简单起见，我们将公式限制在单个k点）：
> 
> * * *
> 
> where the first two terms contain the internal energy E[ψ_i(r), f_i] and entropy S[f_i] of the electrons and the third and fourth terms express the constraints with the Lagrange-multiplicators Λ_ij and χ. In the ground state, the variation of F[ψ_i(r), f_i, Λ_ij, μ] with respect to all four parameters must vanish: For nondegenerate states the matrix of Lagrange multipliers Λ_ij must be diagonal Λ_ij = δ_ij ε_i, and variation with respect to the wave functions ψ_i leads to the Kohn-Sham DFT eigenvalue equation with the self-consistent one-electron potential V_eff. Minimization with respect to f_i determines the relation to be satisfied by the fractional occupation numbers f_i.
> 
> 其中前两项包含电子的内能E[ψ_i(r), f_i]和熵S[f_i]，第三和第四项用Lagrange乘子Λ_ij和χ表达约束条件。在基态中，F[ψ_i(r), f_i, Λ_ij, μ]对所有四个参数的变分必须为零：对于非简并态，Lagrange乘子矩阵Λ_ij必须是对角的Λ_ij = δ_ij ε_i，对波函数ψ_i的变分导致具有自洽单电子势V_eff的Kohn-Sham DFT本征值方程。对f_i的最小化确定了分数占据数f_i必须满足的关系。
> 
> **Kohn-Sham DFT eigenvalue equation**: Kohn-Sham DFT本征值方程，将相互作用多电子问题映射为有效势中非相互作用电子问题的方程。 **self-consistent**: 自洽的，通过迭代计算使输入和输出电荷密度或势达到一致的数值方案。
> 
> * * *
> 
> The entropy in Eq. (3) corresponds to noninteracting fermions,
> 
> 方程(3)中的熵对应于非相互作用费米子，
> 
> **fermions**: 费米子，遵守费米-狄拉克统计和泡利不相容原理的粒子，如电子。
> 
> * * *
> 
> with a Fermi-Dirac occupation probability of the one-electron states,
> 
> 具有单电子态的Fermi-Dirac占据概率，
> 
> * * *
> 
> The property of being stationary with respect to f_i makes the gradient of the free energy F equal to the Hellmann-Feynman forces,
> 
> 相对于f_i的稳定性使得自由能F的梯度等于Hellmann-Feynman力，
> 
> * * *
> 
> since the additional terms in the gradient of F depending on the variation of the occupation numbers and of the entropy term with the atomic displacement cancel exactly. To obtain a smooth variation of the f_i it is necessary to use an electron temperature that is significantly higher than the ionic temperature (depending on the level spacing and hence on the size of the system). In most cases we found it more convenient to use Gaussian broadening of the one-electron levels: it allows us to achieve a smooth variation of the occupation numbers around the Fermi level, but for higher excitation energies the occupation numbers converge more rapidly to zero. This improved convergence allows one to reduce the necessary number of bands and hence the computational effort. The form of the entropy related to the Gaussian broadening is
> 
> 由于F的梯度中依赖于占据数变化和熵项随原子位移变化的附加项恰好抵消，自由能F的梯度等于Hellmann-Feynman力。为了获得f_i的平滑变化，有必要使用显著高于离子温度的电子温度（取决于能级间距，因而取决于系统大小）。在大多数情况下，我们发现使用单电子能级的Gaussian展宽更方便：它使我们能够在Fermi能级附近实现占据数的平滑变化，但对于更高的激发能量，占据数更快地收敛到零。这种改进的收敛性允许减少所需的能带数量，从而减少计算工作量。与Gaussian展宽相关的熵的形式为
> 
> **Gaussian broadening**: 高斯展宽，使用高斯函数对电子态进行平滑以消除离散能级结构的技术。
> 
> * * *
> 
> where the occupation function f_i and the eigenvalues ε_i are related through
> 
> 其中占据函数f_i和本征值ε_i通过下式关联
> 
> * * *
> 
> with σ equal to the width of the Gaussians.
> 
> 其中σ等于Gaussian的宽度。
> 
> * * *
> 
> ## B. Iterative matrix diagonalization based on conjugate-gradient minimization
> 
> ## B. 基于共轭梯度最小化的迭代矩阵对角化
> 
> Methods for determining the DFT-ground state via direct energy minimization have been developed by several groups. We closely follow Bylander et al. in using the conjugate-gradient method for improving the expectation value of the Hamiltonian for all bands sequentially and then diagonalizing the Hamiltonian in the subspace of the improved eigenfunctions to obtain the starting states for the next iteration which begins after the potential has been updated. The simplest strategy for minimization is the steepest descent approach, i.e., to change the approximate wave function ψ_i in the direction of the gradient g_i in the Hilbert space of the basis functions (plane waves in our case) from which ψ_i is constructed. If the Hamiltonian is diagonal in the subspace spanned by the trial wave functions, i.e.,
> 
> 通过直接能量最小化确定DFT基态的方法已由多个研究组开发。我们紧密跟随Bylander等人的方法，使用共轭梯度方法顺序改进所有能带的哈密顿量期望值，然后在改进的本征函数的子空间中对角化哈密顿量，以获得下一次迭代的起始态，该迭代在势更新后开始。最小化的最简单策略是最陡下降法，即使近似波函数ψ_i在基函数（在我们的情况下是平面波）的Hilbert空间中沿梯度g_i的方向变化，ψ_i是由这些基函数构建的。如果哈密顿量在试探波函数张成的子空间中是对角的，即
> 
> **steepest descent**: 最陡下降法，沿函数局部梯度方向寻找极小值的优化方法。 **plane waves**: 平面波，具有恒定波矢的波，常用作电子结构计算中的基函数。
> 
> * * *
> 
> the gradient is simply
> 
> 梯度简单地是
> 
> * * *
> 
> The steepest-descent approach may be improved in two ways. (a) The conjugate gradient approach changes the search direction from the direction of the steepest descent to one which points more nearly to the minimum by retaining information from previous search steps. (b) Preconditioning of the steepest descent accounts for the fact that due to the presence of the kinetic energy operator in H plane waves with the largest momentum will have the largest coefficients in g_i. Preconditioning involves multiplying the coefficient of each plane wave in g_i by a factor which is close to unity for plane waves whose kinetic energy does not exceed the average kinetic energy of g_i and decreases strongly for the higher plane wave components. In our work we used the preconditioning functions of Ref. 39. After the preconditioning a reorthogonalization of the conditioned gradient to all bands is necessary. The iterative improvement of a state is stopped after the change in the energy eigenvalue is smaller than 10 eV (or less than 30% of the change in the first steepest-descent step) and the calculation moves to the next band. After running over all bands (including some empty bands) the Hamiltonian matrix is diagonalized in the subspace spanned by the improved trial wave functions and the new Fermi energy and new occupation numbers are determined using Gaussian broadening. Using the new occupation numbers charge density and potential are updated. To prevent charge sloshing, the mixing scheme of Kerker has been used.
> 
> 最陡下降法可以通过两种方式改进。(a) 共轭梯度方法通过保留以前搜索步骤的信息，将搜索方向从最陡下降方向改变为更接近最小值的方向。(b) 最陡下降的预条件化考虑到由于H中存在动能算符，具有最大动量的平面波在g_i中将具有最大的系数。预条件化涉及将g_i中每个平面波的系数乘以一个因子，对于动能不超过g_i平均动能的平面波，该因子接近1，对于更高的平面波分量则强烈减小。在我们的工作中，我们使用了参考文献39的预条件化函数。预条件化后，需要对所有能带重新正交化条件化梯度。当一个态的能量本征值变化小于10 eV（或小于第一个最陡下降步骤变化的30%）时，该态的迭代改进停止，计算转向下一个能带。在所有能带（包括一些空带）上运行之后，哈密顿量矩阵在改进的试探波函数张成的子空间中对角化，并使用Gaussian展宽确定新的Fermi能量和新占据数。使用新占据数更新电荷密度和势。为了防止电荷振动，使用了Kerker的混合方案。
> 
> **charge sloshing**: 电荷振动，迭代过程中电荷密度在自洽收敛前的不稳定振荡。 **mixing scheme**: 混合方案，通过混合新旧电荷密度来稳定自洽迭代收敛的技术。
> 
> * * *
> 
> For our calculations of liquid and amorphous germanium we found fast convergence for A = 1.0, G₀ = 1.5 Å⁻¹. The electronic energy minimization is terminated after the change in the total energy per atom becomes smaller than 1 × 10⁻⁵ eV/atom. Our approach differs from the band-by-band conjugate-gradient minimization used by Teter et al. In their approach the preconditioned conjugate-gradient method is used to minimize the total energy; charge density and potential are recalculated after each update of a band. For insulators and semiconductors where the occupation numbers do not change, this is a stable procedure. For metals the subspace diagonalization necessary for the calculation of the new occupation numbers leads to strong charge sloshing and the procedure might be unstable.
> 
> 对于液态和非晶锗的计算，我们发现A = 1.0, G₀ = 1.5 Å⁻¹时收敛很快。当每原子总能量变化小于1 × 10⁻⁵ eV/原子时，电子能量最小化终止。我们的方法不同于Teter等人使用的逐带共轭梯度最小化。在他们的方法中，预条件共轭梯度方法用于最小化总能量；每个能带更新后重新计算电荷密度和势。对于占据数不变的绝缘体和半导体，这是一个稳定的过程。对于金属，计算新占据数所需的子空间对角化会导致强烈的电荷振动，该过程可能不稳定。
> 
> * * *
> 
> ## C. Nosé dynamics
> 
> ## C. Nosé动力学
> 
> The Nosé thermostat is a method for simulating a canonical ensemble at a prefixed temperature. The dynamics of the ions is described by the EOM:
> 
> Nosé恒温器是在预设温度下模拟正则系综的方法。离子动力学由EOM描述：
> 
> * * *
> 
> where s(t) is an additional variable that obeys the EOM and describes the coupling of the physical system to a heat bath. Here Q is a mass parameter for the Nosé thermostat and g = 3(N − 1) counts the number of ionic degrees of freedom. The parameter Q determines the response of the heat bath to fluctuations of the ionic system. Q must be sufficiently small to allow the system to approach equilibrium fast enough, and sufficiently large to yield correct values for the energy fluctuations of the ionic system. According to Nosé, the characteristic frequency of the thermostat is
> 
> 其中s(t)是服从EOM的附加变量，描述物理系统与热浴的耦合。这里Q是Nosé恒温器的质量参数，g = 3(N − 1)计算离子自由度的数量。参数Q决定了热浴对离子系统涨落的响应。Q必须足够小以使系统足够快地接近平衡，又足够大以为离子系统的能量涨落产生正确的值。根据Nosé，恒温器的特征频率为
> 
> * * *
> 
> Equilibration between ions and thermostat is most effective if ω_T is of the same order of magnitude as the characteristic vibrational frequencies of the system since this leads to a strong coupling of both subsystems. In the present work we chose Q so that the period of the thermostat is equal to about 150 time steps (ω_T = 13.6 ps⁻¹), we found very good agreement between Eq. (18) and the actual frequency of the temperature fluctuations. The ionic equations of motion are integrated using a fourth-order predictor-corrector algorithm which allows the use of time steps as large as Δt = 3 × 10⁻¹⁵ s with good energy conservation (note that this time step is about a factor of 10 larger than the time step in comparable CP simulations). In a microcanonical ensemble, the conserved quantity in a finite-temperature DF-MD is the sum of the kinetic energy T_I of the ions, of the internal energy E of the electron-ion system, and of the electronic entropy term −TS_el.
> 
> 如果ω_T与系统特征振动频率处于同一数量级，离子和恒温器之间的平衡是最有效的，因为这导致两个子系统的强耦合。在目前的工作中，我们选择Q使得恒温器周期等于约150个时间步长（ω_T = 13.6 ps⁻¹），我们发现方程(18)与温度涨落的实际频率之间有非常好的一致性。离子运动方程使用四阶预测-校正算法积分，允许使用大至Δt = 3 × 10⁻¹⁵ s的时间步长，同时具有良好的能量守恒性（注意，该时间步长比可比较的CP模拟中的时间步长大一个因子约10）。在微正则系综中，有限温度DF-MD中的守恒量是离子动能T_I、电子-离子系统内能E和电子熵项−TS_el之和。
> 
> **predictor-corrector algorithm**: 预测-校正算法，通过预测然后校正数值积分中间步骤来提高精度的数值方法。
> 
> * * *
> 
> In the Nosé approach, the total energy of the electron-ion system is allowed to fluctuate, the conserved quantity is the expectation value of the extended system (ions + electrons + thermostat), i.e.,
> 
> 在Nosé方法中，允许电子-离子系统的总能量涨落，守恒量是扩展系统（离子+电子+恒温器）的期望值，即
> 
> * * *
> 
> Here the terms in the second line stand for the kinetic and potential energies of the extra degree of freedom s. To speed up the calculations, the simulation of the liquid phase was started in the classical molecular dynamics mode with interatomic pair forces calculated using pseudopotential perturbation theory and an empty core pseudopotential (EC-PP) (R_c = 1.03 a.u.). For the liquid metal Ge, this leads to a rather accurate description of the atomic and electronic structure. After switching to the ab initio MD, the system reaches equilibrium within a small number of MD steps (less than 0.5 ps). This combination of classical and ab initio MD leads to an appreciable economy in computer time.
> 
> 这里第二行中的项代表额外自由度s的动能和势能。为了加快计算，液态相的模拟以经典分子动力学模式开始，使用赝势微扰论和空芯赝势（EC-PP）（R_c = 1.03 a.u.）计算原子间对力。对于液态金属Ge，这导致对原子和电子结构的相当精确的描述。切换到从头计算MD后，系统在少量MD步骤（少于0.5 ps）内达到平衡。经典和从头计算MD的这种结合导致可观的计算时间节省。
> 
> **pseudopotential perturbation theory**: 赝势微扰论，将赝势作为微扰处理以计算电子结构响应的理论方法。 **empty core pseudopotential (EC-PP)**: 空芯赝势，在离子核心区域使用恒定（通常为零）势的简化赝势模型。
> 
> * * *
> 
> ## D. Subspace alignment
> 
> ## D. 子空间对齐
> 
> The initial wave functions for the starting configuration are generated by diagonalizing the Hamiltonian corresponding to a charge density of overlapping atoms in a basis of 200 plane waves. After moving the ions, one needs a reasonable estimate of the electronic wave functions and the charge density n_in for the new configuration—the wave functions of the old configuration would give a bad starting point for the energy minimization. The charge density may be estimated by extrapolating the charge density calculated at times t_n, t_{n−1}, ... to t_{n+1}, i.e.,
> 
> 起始构型的初始波函数通过在200个平面波的基组中对角化对应于重叠原子电荷密度的哈密顿量来生成。移动离子后，需要对新构型的电子波函数和电荷密度n_in进行合理估计——旧构型的波函数将为能量最小化提供糟糕的起点。电荷密度可以通过将时间t_n, t_{n−1}, ...计算的电荷密度外推到t_{n+1}来估计，即
> 
> * * *
> 
> to lowest order, and similarly for higher-order extrapolations. A corresponding extrapolation may be performed for the wave functions. However, one has to consider that as a consequence of the subspace diagonalization the wave functions are rotated in Hilbert space. Arias et al. propose to transform the two sets of wave functions such that their distance D is minimal (w_i is some weighting function), and where the transformed wave functions are given by unitary matrices U, U′. After performing both transformations, the overlap of the two sets of wave functions is such that both subspaces are perfectly aligned. To first order, the extrapolation of the wave functions is trivial.
> 
> 到最低阶，类似地用于高阶外推。可以对波函数执行相应的外推。然而，必须考虑到由于子空间对角化，波函数在Hilbert空间中旋转。Arias等人提议变换两组波函数使得它们的距离D最小（w_i是某种加权函数），其中变换后的波函数由酉矩阵U、U′给出。执行两种变换后，两组波函数的重叠使得两个子空间完全对齐。到一阶，波函数的外推是平凡的。
> 
> **subspace diagonalization**: 子空间对角化，在波函数子空间内对角化哈密顿量矩阵以确定本征值和本征矢的技术。 **unitary matrices**: 酉矩阵，满足U†U = I的复矩阵，保持向量的内积不变。
> 
> * * *
> 
> Here U_n and U′_n are the unitary transformations that align the subspaces spanned by the wave functions at times t_n and t_{n−1}. Extensions to higher-order extrapolations are discussed in Ref. 53. In simulations for metallic systems, empty states have to be considered. This helps to predict wave functions close to the Fermi energy because the wave functions at time t_{n+1} are to first order a linear combination of wave functions at t_n, i.e., predominantly wave functions out of a small interval around ε_i are mixed. Our results show that even for liquid Ge the prediction of the wave functions leads to a state whose energy does not differ from the ground state energy by more than 5 × 10⁻⁵ eV/atom. On this basis, the relaxation to the ground state is usually possible within two conjugate-gradient iterations each requiring two evaluations of the Hamiltonian acting onto all wave functions. For an ensemble of 64 Ge atoms, in the metallic liquid phase at T = 1250 K, the change of the conserved energy G [see Eq. (16)] was smaller than 5 meV per atom over a run of 3 ps [i.e., 1000 steps with Δt = 3 × 10⁻¹⁵ s, see Fig. 1(a)]. This corresponds to less than 0.1% of the cohesive energy. For amorphous Ge at T = 300 K, the change in the total energy is smaller than 1 meV/Atom over a run of 6 ps [see Fig. 1(b)].
> 
> 这里U_n和U′_n是酉变换，对齐时间t_n和t_{n−1}的波函数张成的子空间。高阶外推的扩展在参考文献53中讨论。在金属系统的模拟中，必须考虑空态。这有助于预测Fermi能量附近的波函数，因为时间t_{n+1}的波函数到一阶是t_n处波函数的线性组合，即主要是来自ε_i周围小区间的波函数混合。我们的结果表明，即使对于液态Ge，波函数的预测导致的状态，其能量与基态能量的差异不超过5 × 10⁻⁵ eV/原子。在此基础上，弛豫到基态通常可以在两次共轭梯度迭代内完成，每次需要对所有波函数作用的哈密顿量进行两次评估。对于64个Ge原子的系综，在T = 1250 K的金属液相中，在3 ps的运行中[即1000步，Δt = 3 × 10⁻¹⁵ s，见图1(a)]，守恒能量G [见方程(16)]的变化小于每原子5 meV。这对应于小于结合能的0.1%。对于T = 300 K的非晶Ge，在6 ps的运行中总能量变化小于1 meV/原子[见图1(b)]。
> 
> **cohesive energy**: 结合能，将固体分解为孤立原子所需能量的量度。
> 
> * * *
> 
> ## E. Nonlocal pseudopotentials in real-space projection
> 
> ## E. 实空间投影中的非局域赝势
> 
> In our calculations we used a nonlocal Vanderbilt pseudopotential with a cutoff radius of R_c = 1.5 a.u., generated from a scalar-relativistic all-electron calculation. The choice of the pseudopotential is the result of an extensive study of the optimization of the accuracy and plane-wave convergence of various norm-conserving pseudopotentials (NCPP). This potential offers a compromise between computational efficiency, accuracy, transferability, and plane wave convergence. Energy cutoffs of 12 Ry and 25 Ry are necessary to converge the total energy of germanium to within 1 mRy and 0.1 mRy, respectively. The cutoff energy cannot be lowered substantially by, e.g., optimization of the kinetic energy. With this pseudopotential we calculate the lattice constant of Ge at T = 0 K in the diamond structure within 1.3% (see Table I) of the experimental value and a reasonable pressure for the α → β (diamond structure → white-tin structure) transition (P = 75 kbar, expt. P_t = 100 kbar), see Fig. 2. Lattice constant, bulk modulus, and cohesive energy are in very good agreement with recent NCPP calculations of Garcia et al., the agreement with older calculations of Yin and Cohen is worse, probably due to insufficient number of plane waves and due to the use of the Wigner exchange-correlation functional in Ref. 58.
> 
> 在我们的计算中，我们使用了非局域Vanderbilt赝势，截止半径R_c = 1.5 a.u.，由标量相对论全电子计算生成。赝势的选择是对各种模守恒赝势（NCPP）的精度和平面波收敛性优化进行广泛研究的结果。该势在计算效率、精度、可转移性和平面波收敛性之间提供了折衷。需要12 Ry和25 Ry的能量截止分别将锗的总能量收敛到1 mRy和0.1 mRy以内。截止能量不能通过例如动能优化来实质性降低。使用该赝势，我们计算了T = 0 K下金刚石结构中Ge的晶格常数，在实验值的1.3%以内（见表I），以及α → β（金刚石结构→白锡结构）转变的合理压力（P = 75 kbar，实验值P_t = 100 kbar），见图2。晶格常数、体弹模量和结合能与Garcia等人最近的NCPP计算非常吻合，与Yin和Cohen较旧的计算结果一致度较差，可能是由于平面波数量不足以及参考文献58中使用了Wigner交换关联泛函。
> 
> **norm-conserving pseudopotentials (NCPP)**: 模守恒赝势，在截止半径内外保持赝波函数模守恒的赝势类型。 **Vanderbilt pseudopotential**: Vanderbilt赝势，一种超软赝势，允许更低的平面波截止能量。 **bulk modulus**: 体弹模量，材料对均匀压缩的抵抗能力的量度。 **white-tin structure**: 白锡结构，β-Sn的四方晶体结构，是高压下Ge的一种相。
> 
> * * *
> 
> The Vanderbilt pseudopotential is nonlocal, we used a Kleinman-Bylander factorization decomposing the nonlocal potential into a sum of diagonal operators for the individual angular momentum components. For Ge we chose the p component as the local component and considered s and d nonlocality. The nonlocality of the pseudopotentials extends only over the region occupied by the core of the atom. Hence it is possible to deal efficiently with the nonlocality of the potential by working in real space. For this specific pseudopotential we found that optimization of the real-space projection operators (see King-Smith et al.) is not necessary, because the Fourier components of the projection states ΔV_l φ_l decay rather rapidly to zero.
> 
> Vanderbilt赝势是非局域的，我们使用了Kleinman-Bylander分解，将非局域势分解为各个角动量分量的对角算符之和。对于Ge，我们选择p分量作为局域分量，并考虑了s和d的非局域性。赝势的非局域性仅延伸到原子核心占据的区域。因此，通过在实空间中工作可以高效地处理势的非局域性。对于这个特定的赝势，我们发现实空间投影算符的优化（参见King-Smith等人）是不必要的，因为投影态ΔV_l φ_l的Fourier分量相当快地衰减到零。
> 
> * * *
> 
> **TABLE I.** Lattice constant a₀, equilibrium volume V₀, bulk modulus B₀, and cohesive energy E for cubic diamond Ge (spin correction for atoms were included in the present calculation). **表I.** 立方金刚石Ge的晶格常数a₀、平衡体积V₀、体弹模量B₀和结合能E（原子自旋修正已包含在本计算中）。
> 
> 

<table>
<thead>
<tr>
<th style="text-align:left"></th>
<th style="text-align:center">E_c (eV)</th>
<th style="text-align:center">V₀ (Å³)</th>
<th style="text-align:center">a₀ (Å)</th>
<th style="text-align:center">B₀ (Mbar)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">PP</td>
<td style="text-align:center">4.55</td>
<td style="text-align:center">21.61</td>
<td style="text-align:center">5.57</td>
<td style="text-align:center">0.75</td>
</tr>
<tr>
<td style="text-align:left">Garcia et al.</td>
<td style="text-align:center">4.79</td>
<td style="text-align:center">21.36</td>
<td style="text-align:center">5.55</td>
<td style="text-align:center">0.78</td>
</tr>
<tr>
<td style="text-align:left">Yin et al.</td>
<td style="text-align:center">4.26</td>
<td style="text-align:center">22.60</td>
<td style="text-align:center">5.66</td>
<td style="text-align:center">0.73</td>
</tr>
<tr>
<td style="text-align:left">Experiment</td>
<td style="text-align:center">3.85</td>
<td style="text-align:center">22.64</td>
<td style="text-align:center">5.66</td>
<td style="text-align:center">0.768</td>
</tr>
</tbody>
</table>


> 
> PP: Present work, Ceperley-Alder exchange-correlation functional. PP: 本工作，Ceperley-Alder交换关联泛函。 Garcia et al.: Reference 57, Ceperley-Alder exchange-correlation functional. Garcia等人：参考文献57，Ceperley-Alder交换关联泛函。 Yin et al.: Reference 58, Wigner interpolation for exchange-correlation functional. Yin等人：参考文献58，Wigner交换关联泛函插值。
> 
> * * *
> 
> # III. SIMULATION OF THE LIQUID METAL—AMORPHOUS-SEMICONDUCTOR TRANSITION
> 
> # III. 液态金属-非晶半导体转变的模拟
> 
> Our simulations for liquid and amorphous Ge have been performed for an ensemble of 64 atoms in a cubic cell. For this ensemble, we calculated the wave functions for 138 bands, i.e., 10 bands more than necessary to accommodate the 256 valence electrons. A Gaussian broadening of the one-electron energies with σ = 0.2 eV was used. The wave functions at the Γ point were expanded in a basis of 7000 plane waves with a cutoff energy of 12 Ry. For the real- and reciprocal-space representation of the charge density and potential a 32 × 32 × 32 mesh was used. The simulation was started in the liquid phase at a temperature of T = 1250 K and a density of n = 0.04385 Å⁻³. A starting configuration for the ab initio MD was generated by classical MD using effective pair potentials generated via second-order perturbation theory and an empty core pseudopotential with R_c = 1.03 a.u. If a pseudopotential optimized for the convergence of the perturbation series is used, the classical simulation already leads to very accurate pair correlation functions (for a detailed comparison of classical and quantum MD, see Ref. 35). After switching to the ab initio MD, the system converges very rapidly to the new ground state. Altogether we performed a 4.5 ps run (1500 time steps) at T = 1250 K (the thermal history of the ensemble is documented in Fig. 3 and Table II), averages are taken over 2.7 ps.
> 
> 我们对液态和非晶Ge的模拟是在立方胞中对64个原子的系综进行的。对于该系综，我们计算了138个能带的波函数，即比容纳256个价电子所需的能带多10个。使用σ = 0.2 eV的单电子能量Gaussian展宽。Γ点的波函数在7000个平面波的基组中展开，截止能量为12 Ry。对于电荷密度和势的实空间和倒空间表示，使用32 × 32 × 32网格。模拟在液相中开始，温度为T = 1250 K，密度为n = 0.04385 Å⁻³。从头计算MD的起始构型由经典MD生成，使用通过二阶微扰论和空芯赝势（R_c = 1.03 a.u.）生成的有效对势。如果使用针对微扰级数收敛优化的赝势，经典模拟已经导致非常精确的对关联函数（经典和量子MD的详细比较，见参考文献35）。切换到从头计算MD后，系统非常迅速地收敛到新的基态。我们在T = 1250 K总共进行了4.5 ps的运行（1500个时间步长）（系综的热历史记录在图3和表II中），平均值取自2.7 ps。
> 
> **Γ point**: Γ点，布里渊区中心(k = 0)点，常用于周期性固体计算。 **valence electrons**: 价电子，参与化学键合的最外层电子。
> 
> * * *
> 
> In the next step, the system was quenched at constant density from T = 1250 K to 750 K in 3 ps (1000 steps), i.e., at a quench rate of Ṫ = 1.67 × 10¹⁴ K s⁻¹, from T = 750 K to T = 450 K in 4.5 ps (1500 steps, Ṫ = 0.67 × 10¹⁴ K s⁻¹) and finally from T = 450 K to T = 300 K in 0.9 ps (300 steps, Ṫ = 1.67 × 10¹⁴ K s⁻¹). Subsequently the system was equilibrated at T = 300 K for 200 steps, followed by a production run. The overall thermal treatment took 15 ps. In previous MD runs we had noticed that the most important structural changes occur in the temperature range 750–450 K. At higher temperatures the system is still in the metallic phase, hence the changes in the local geometry are small. At lower temperatures, the atomic mobility [as monitored by the mean-square displacements, see (Fig. 4)] is very low. This is the rationale for quenching the system rather rapidly at higher and lower temperatures.
> 
> 在下一步中，系统在恒定密度下从T = 1250 K淬火到750 K，历时3 ps（1000步），即淬火速率为Ṫ = 1.67 × 10¹⁴ K s⁻¹，从T = 750 K到T = 450 K历时4.5 ps（1500步，Ṫ = 0.67 × 10¹⁴ K s⁻¹），最后从T = 450 K到T = 300 K历时0.9 ps（300步，Ṫ = 1.67 × 10¹⁴ K s⁻¹）。随后系统在T = 300 K平衡200步，接着进行生产运行。整个热处理过程耗时15 ps。在之前的MD运行中，我们注意到最重要的结构变化发生在温度范围750–450 K。在更高温度下，系统仍处于金属相，因此局域几何的变化很小。在较低温度下，原子迁移率[由均方位移监测，见图4]非常低。这就是在较高和较低温度下相当快速地淬火系统的理由。
> 
> **mean-square displacements**: 均方位移，原子位置随时间变化的均方偏差，用于表征扩散和原子运动。
> 
> * * *
> 
> Our assumption that the densities of liquid Ge at T = 1250 K and of amorphous Ge at T = 300 K are equal is admittedly somewhat arbitrary. It is equivalent to the assumption that the density of amorphous Ge is about 1% lower than the experimental equilibrium density of crystalline Ge. However, we have to remember that the local-density approximation (LDA) overestimates the density by about 4.5% (see the data for crystalline Ge in Table I). Hence our assumption for the density of amorphous Ge is equivalent to assuming a density deficit of nearly 6% (relative to the LDA-equilibrium density of c-Ge). Experimental estimates of the density of thin vapor-condensed amorphous films of Ge claim density deficits of up to 10%, for electrolytic a-Ge a density deficit of 5% has been found. Most continuous-random network models predict a density change between +1% and −4% with the exception of the Steinhardt's model predicting a decrease by −10%. It seems to be fair to conclude that the experimentally estimated density deficit arises to a large extent from microscopic voids at length scales outside the range of our model. In principle, the equilibrium atomic volume could be calculated in the ab initio MD simulation. However, this would result in a further increase of the already large computational effort. In our simulation we have verified that the internal pressure is small at the assumed atomic volume of the amorphous phase (p = −4 kbar at T = 300 K, after a correction of p = −22 kbar due to Pulay stress).
> 
> 我们假设T = 1250 K的液态Ge和T = 300 K的非晶Ge的密度相等，这诚然有些武断。这等价于假设非晶Ge的密度比晶体Ge的实验平衡密度低约1%。然而，我们必须记住局域密度近似（LDA）高估密度约4.5%（见表I中晶体Ge的数据）。因此，我们对非晶Ge密度的假设等价于假设密度赤字接近6%（相对于c-Ge的LDA平衡密度）。Ge的薄蒸气凝聚非晶膜密度的实验估计声称密度赤字高达10%，对于电解a-Ge，已发现密度赤字为5%。大多数连续随机网络模型预测密度变化在+1%和−4%之间，Steinhardt模型预测降低−10%除外。似乎可以公平地得出结论，实验估计的密度赤字在很大程度上来自我们模型范围之外的长度尺度上的微观空洞。原则上，平衡原子体积可以在从头计算MD模拟中计算。然而，这将导致本已庞大的计算工作量进一步增加。在我们的模拟中，我们验证了在假设的非晶相原子体积下内压很小（T = 300 K时p = −4 kbar，经过因Pulay应力导致的p = −22 kbar修正后）。
> 
> **local-density approximation (LDA)**: 局域密度近似，使用局域电子密度来近似交换关联能的DFT方法。 **density deficit**: 密度赤字，非晶材料密度相对于其晶体对应物的相对降低。 **continuous-random network models**: 连续随机网络模型，通过随机连接结构单元构建非晶结构的模型。 **Pulay stress**: Pulay应力，由于有限平面波基组不完全导致的数值应力。
> 
> * * *
> 
> The first quench results in a structure with a relative large number of geometrical defects. Therefore, we have made an attempt to improve the model by a simulated annealing: the temperature was first raised in about 0.3 ps to 600 K and the system was equilibrated at this temperature for about 3 ps. After a quench to T = 300 K, the system was reequilibrated for 4.5 ps (see Fig. 3 and Table II); a production run of 3.0 ps followed. The analysis of the time evolution of local geometrical defects in the amorphous phase shows that even the small thermal fluctuations at room temperature can cause the generation and annihilation of local defects (see also the recent study of the finite-temperature properties of amorphous Si by Drabold et al.). To investigate the inherent (i.e., temperature-independent) defects of a-Ge, we have performed a projection of an instantaneous room-temperature configuration on the nearest potential-energy minimum using a quasi-Newton quench (see, e.g., Ref. 69). It has been shown that the projection on potential-energy minima emphasizes the characteristic features of liquid and amorphous structures. In addition to the slow quench from 600 K to 300 K we also performed one fast quench (0.3 ps) to 300 K. After equilibration for 3 ps a second T = 0 configuration was created using quasi-Newton relaxation to the instantaneous ionic ground state. The configuration we obtained from this quench was—probably by accident—energetically more stable (ΔE = 0.4 eV) than the first T = 0 configuration.
> 
> 第一次淬火产生了具有相对大量几何缺陷的结构。因此，我们尝试通过模拟退火来改进模型：温度首先在约0.3 ps内升高到600 K，系统在此温度下平衡约3 ps。在淬火到T = 300 K后，系统重新平衡4.5 ps（见图3和表II）；随后进行3.0 ps的生产运行。非晶相中局域几何缺陷的时间演化分析表明，即使室温下的微小热涨落也能导致局域缺陷的产生和湮灭（另见Drabold等人最近关于非晶Si有限温度性质的研究）。为了研究a-Ge的固有（即温度无关的）缺陷，我们使用准牛顿淬火将瞬时室温构型投影到最近的势能极小值（参见例如参考文献69）。已经表明，在势能极小值上的投影强调了液态和非晶结构的特征特征。除了从600 K到300 K的慢速淬火外，我们还进行了一次快速淬火（0.3 ps）到300 K。平衡3 ps后，使用准牛顿弛豫到瞬时离子基态创建了第二个T = 0构型。我们从这次淬火中获得的构型——可能是偶然——比第一个T = 0构型在能量上更稳定（ΔE = 0.4 eV）。
> 
> **quasi-Newton quench**: 准牛顿淬火，使用近似Hessian矩阵的方法将系统弛豫到能量极小值的数值优化技术。 **geometrical defects**: 几何缺陷，原子配位或键角偏离理想四面体构型的结构缺陷。
> 
> * * *
> 
> **TABLE II.** History of quench and annealing cycle. **表II.** 淬火和退火循环的历史。
> 
> 

<table>
<thead>
<tr>
<th style="text-align:left"></th>
<th style="text-align:center">Time</th>
<th style="text-align:center">Time steps</th>
<th style="text-align:center">T_start</th>
<th style="text-align:center">T_end</th>
<th style="text-align:center">Ṫ (K s⁻¹)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">liquid</td>
<td style="text-align:center">4.5 ps</td>
<td style="text-align:center">1500</td>
<td style="text-align:center">1250</td>
<td style="text-align:center">1250</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">cooling</td>
<td style="text-align:center">3 ps</td>
<td style="text-align:center">1000</td>
<td style="text-align:center">1250</td>
<td style="text-align:center">750</td>
<td style="text-align:center">1.67 × 10¹⁴</td>
</tr>
<tr>
<td style="text-align:left">cooling</td>
<td style="text-align:center">4.5 ps</td>
<td style="text-align:center">1500</td>
<td style="text-align:center">750</td>
<td style="text-align:center">450</td>
<td style="text-align:center">0.67 × 10¹⁴</td>
</tr>
<tr>
<td style="text-align:left">cooling</td>
<td style="text-align:center">0.9 ps</td>
<td style="text-align:center">300</td>
<td style="text-align:center">450</td>
<td style="text-align:center">300</td>
<td style="text-align:center">1.67 × 10¹⁴</td>
</tr>
<tr>
<td style="text-align:left">as-quenched amorphous</td>
<td style="text-align:center">2.1 ps</td>
<td style="text-align:center">700</td>
<td style="text-align:center">300</td>
<td style="text-align:center">300</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">heating</td>
<td style="text-align:center">0.3 ps</td>
<td style="text-align:center">100</td>
<td style="text-align:center">300</td>
<td style="text-align:center">600</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">annealing</td>
<td style="text-align:center">3.0 ps</td>
<td style="text-align:center">1000</td>
<td style="text-align:center">600</td>
<td style="text-align:center">600</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">cooling</td>
<td style="text-align:center">1.8 ps</td>
<td style="text-align:center">600</td>
<td style="text-align:center">600</td>
<td style="text-align:center">300</td>
<td style="text-align:center">1.67 × 10¹⁴</td>
</tr>
<tr>
<td style="text-align:left">annealed amorphous</td>
<td style="text-align:center">7.5 ps</td>
<td style="text-align:center">2500</td>
<td style="text-align:center">300</td>
<td style="text-align:center">300</td>
<td style="text-align:center">—</td>
</tr>
</tbody>
</table>


> 
> * * *
> 
> # IV. ATOMIC AND ELECTRONIC STRUCTURE
> 
> # IV. 原子和电子结构
> 
> In this section we discuss the atomic and electronic structure of our Ge sample in the liquid and amorphous states and the changes that occur during quenching and annealing. Figures 5–8 show the pair-correlation function g(R), the static structure factor S(Q), the bond-angle distribution function g⁽³⁾(θ, R_c) (i.e., the angles formed by nearest-neighbor bonds with a maximum length R_c around a central atom), and the electronic density of states n(E) for liquid Ge at T = 1250 K, for a supercooled liquid Ge in the temperature range 750–650 K (the information has been sampled during a continuous cooling run), and for as-quenched and annealed amorphous Ge at T = 300 K. The static structure factor S(Q) has been calculated by performing in (29) the sum over all atom pairs for the Q vectors compatible with the periodic boundary conditions. Calculation of S(Q) by Fourier transforming g(R) can lead to results that are seriously affected by truncation errors. The electronic density of states (DOS) has been obtained by a Gaussian broadening (σ = 0.4 eV) of the 150 lowest eigenvalues at a 6 × 6 × 6 Monkhorst-Pack grid using one typical configuration. We found that a smooth and realistic DOS can be obtained using only the ten special points in the irreducible wedge of the simple cubic Brillouin zone generated from this state. The usual practice to consider the one-electron states at the Γ point only is sufficiently accurate for the calculation of the interatomic forces and pressure (this was tested by calculating the pair-correlation function and pressure for l-Ge using the off-symmetry k point [(0.25, 0.25, 0.25)π/L] instead of the Γ point), but leads to spurious structures in the DOS that disappear after a more extended k-space sampling.
> 
> 在本节中，我们讨论Ge样品在液态和非晶态中的原子和电子结构以及淬火和退火过程中发生的变化。图5–8显示了对关联函数g(R)、静态结构因子S(Q)、键角分布函数g⁽³⁾(θ, R_c)（即中心原子周围最大长度为R_c的最近邻键形成的角度）和电子态密度n(E)，分别对应T = 1250 K的液态Ge、温度范围750–650 K的过冷液态Ge（信息在连续冷却运行期间采样）以及T = 300 K的淬火态和退火态非晶Ge。静态结构因子S(Q)通过在(29)中对所有与周期性边界条件兼容的Q矢量求和所有原子对来计算。通过Fourier变换g(R)计算S(Q)可能导致严重受截断误差影响的结果。电子态密度（DOS）通过对6 × 6 × 6 Monkhorst-Pack网格上150个最低本征值使用一个典型构型进行Gaussian展宽（σ = 0.4 eV）获得。我们发现，仅使用从该态生成的简单立方布里渊区不可约楔中的十个特殊点，就可以获得平滑且现实的DOS。仅考虑Γ点的单电子态的通常做法对于计算原子间力和压力足够精确（这通过使用离对称k点[(0.25, 0.25, 0.25)π/L]而不是Γ点计算l-Ge的对关联函数和压力来测试），但导致DOS中出现虚假结构，这些结构在更扩展的k空间采样后消失。
> 
> **static structure factor**: 静态结构因子，描述材料对散射实验中动量传递的结构响应的函数。 **bond-angle distribution function**: 键角分布函数，描述最近邻键之间角度统计分布的函数。 **electronic density of states (DOS)**: 电子态密度，给定能量范围内可用的电子态数目。 **Monkhorst-Pack grid**: Monkhorst-Pack网格，布里渊区中k点采样的常用方法。 **irreducible wedge**: 不可约楔，布里渊区中通过对称操作无法相互转换的最小区域。
> 
> * * *
> 
> ## A. Liquid Ge
> 
> ## A. 液态Ge
> 
> Our present simulation yields a very accurate description of the structure of liquid Ge. Figure 5 shows g(R) and S(Q) together with the experimental neutron diffraction data—agreement between theory and experiment is indeed very good. The atomic arrangement in liquid Ge is very different from that in normal liquid metals. The coordination number N_c obtained by integrating the radial distribution function RDF(R) = 4πR² n g(R) up to the first minimum at R = 3.2 Å (3.4 Å) is N_c = 5.8 (6.9), i.e., considerably lower than the value N_c ≈ 10–12 characteristic for normal simple metals, but in good agreement with experiment (N_c = 6.8), see also Table III. Besides the first peak, there are only weak oscillations in g(R) that are well reproduced by the ab initio simulations. The characteristic feature of S(Q) is the low amplitude of the main peak and the shoulder at Q = 2k_F = 3.46 Å⁻¹ corresponding to the diameter of the free-electron Fermi sphere. The bond-angle distribution function g⁽³⁾(θ, R_c) is just the radial integral over the triplet-correlation function g⁽³⁾(θ, R₁, R₂) for R₁, R₂ < R_c. Figure 5(c) shows that except for excluded-volume effects the distribution of the bond angles is almost random, with only a very flat maximum close to the tetrahedral bond angle of θ = 109° for short bonds, and a preference for the formation of isosceles triplets (θ ≈ 60°) for longer bonds. This corresponds to the very broad distribution of coordination numbers ranging from N_c = 3 to N_c = 8 (see Table IV). The predictions of ab initio MD are very similar to those of classical MD with effective pair and volume forces calculated using pseudopotential and linear response forces: g(R) and S(Q) are almost identical, only at the level of the triplet-correlation functions we find that the quantum-mechanical many-body forces induce a slight preference of tetrahedral bond angles over close-packed configurations. In a similar way, the ab initio simulations of Stich et al. have confirmed the pair-potential results for l-Si. This is important since it demonstrates that the real-space interpretation of the structures of l-Si and l-Ge in terms of a packing of soft spheres modulated by the Friedel oscillations in the interatomic forces (wavelength λ_F = 2π/2k_F) is correct. In momentum space, the signature of the modulation of g(R) is the shoulder in S(Q) at Q = 2k_F. For l-Si, the calculated electronic DOS conforms with the nearly-free-electron (NFE) interpretation of the structure-force relationship: the calculated n(E) is very close to a free-electron parabola. The calculated DOS of liquid Ge shows a remarkable pseudogap at a binding energy of 4.5 eV. This makes the electronic DOS very different from any of the crystalline phases: it has neither the characteristic signature of the sp hybridization of the semiconducting α and the metallic β phases, nor the free-electron character of the metallic high-pressure phases. The calculated DOS is in very good agreement with high resolution photoemission data and with earlier supercell-linear-muffin-tin-orbital (LMTO) calculations for the classical-MD models of l-Ge. The comparison with the LMTO calculations is helpful since these calculations show that the pseudogap in n(E) separates s and p states (the lower part of the valence band accommodates exactly 2s electrons per Ge atom). The existence of the pseudogap is characteristic for the heavier liquid group IV elements (Ge, Sn, Pb), due to an increasing s-p splitting arising from relativistic effects. In Ge the splitting is enhanced by a partial penetration of the 4s electrons in the 3d core leading to a stronger s component of the electron-ion pseudopotential. In the past, various structural models for describing the short-range order l-Si and l-Ge have been proposed. They either assume the presence of two kinds of atoms (fourfold coordinated semiconducting or highly-coordinated metallic) or assume a similarity with the β-Sn or simple cubic structures (both sixfold coordinated and metallic). Our results for l-Ge (as well as the results of Stich et al. for l-Si) indicate a broad, homogeneous distribution of local bonding configurations and indicate that both classes of models are unrealistic. The ab initio MD also demonstrates that for the liquid-metallic phase of Si and Ge, the effective pair and volume forces derived from pseudopotential perturbation theory are much more realistic than the empirical pair and triplet forces leading to unrealistic bond-angle distributions.
> 
> 我们目前的模拟给出了液态Ge结构的非常精确的描述。图5显示了g(R)和S(Q)以及实验中子衍射数据——理论与实验之间的一致性确实非常好。液态Ge中的原子排列与普通液态金属中的原子排列非常不同。通过将径向分布函数RDF(R) = 4πR² n g(R)积分到第一个极小值R = 3.2 Å (3.4 Å)获得的配位数N_c为N_c = 5.8 (6.9)，即显著低于正常简单金属的特征值N_c ≈ 10–12，但与实验吻合良好（N_c = 6.8），另见表III。除了第一个峰外，g(R)中只有弱振荡，这些振荡被从头计算模拟很好地再现。S(Q)的特征特征是主峰的低幅度和Q = 2k_F = 3.46 Å⁻¹处的肩峰，对应于自由电子Fermi球的直径。键角分布函数g⁽³⁾(θ, R_c)正是R₁, R₂ < R_c条件下三重关联函数g⁽³⁾(θ, R₁, R₂)的径向积分。图5(c)显示，除了排除体积效应外，键角分布几乎是随机的，对于短键仅在接近四面体键角θ = 109°处有一个非常平坦的最大值，对于较长键有形成等腰三重态（θ ≈ 60°）的偏好。这对应于从N_c = 3到N_c = 8的非常宽的配位数分布（见表IV）。从头计算MD的预测与使用赝势和线性响应力计算的有效对势和体积力的经典MD的预测非常相似：g(R)和S(Q)几乎相同，仅在三重关联函数层面，我们发现量子力学多体力诱导了四面体键角相对于密堆积构型的轻微偏好。以类似的方式，Stich等人的从头计算模拟已经确认了l-Si的对势结果。这很重要，因为它证明了用受原子间力中Friedel振荡（波长λ_F = 2π/2k_F）调制的软球堆积来解释l-Si和l-Ge结构的实空间解释是正确的。在动量空间中，g(R)调制的标志是S(Q)在Q = 2k_F处的肩峰。对于l-Si，计算的电子DOS符合结构-力关系的近自由电子（NFE）解释：计算的n(E)非常接近自由电子抛物线。液态Ge的计算DOS在结合能4.5 eV处显示出一个显著的赝隙。这使得电子DOS与任何晶相都非常不同：它既没有半导体α相和金属β相的sp杂化的特征标志，也没有金属高压相的自由电子特征。计算的DOS与高分辨率光电子发射数据以及早期对l-Ge经典MD模型的超胞-线性丸盒轨道（LMTO）计算非常好地吻合。与LMTO计算的比较是有帮助的，因为这些计算表明n(E)中的赝隙分隔了s和p态（价带的下部恰好容纳每个Ge原子2个s电子）。赝隙的存在是较重液态IV族元素（Ge、Sn、Pb）的特征，这是由于相对论效应导致的s-p分裂增加。在Ge中，由于4s电子部分穿透3d核心，导致电子-离子赝势的s分量更强，分裂得到增强。过去，已经提出了各种描述l-Si和l-Ge短程有序的结构模型。它们要么假设存在两种原子（四重配位半导体或高配位金属），要么假设与β-Sn或简单立方结构（两者都是六重配位和金属性的）相似。我们对l-Ge的结果（以及Stich等人对l-Si的结果）表明局域成键构型存在宽广、均匀的分布，并表明这两类模型都不现实。从头计算MD还证明，对于Si和Ge的液态金属相，从赝势微扰论导出的有效对势和体积力比导致不现实键角分布的经验对势和三重态力要现实得多。
> 
> **radial distribution function**: 径向分布函数，描述距参考原子径向距离处找到原子的概率密度。 **pseudogap**: 赝隙，态密度中电子态密度显著降低但不是严格为零的能量区间。 **Friedel oscillations**: Friedel振荡，由于Fermi面处电子屏蔽导致的电荷密度或原子间势的振荡行为。 **linear-muffin-tin-orbital (LMTO)**: 线性丸盒轨道，一种基于丸盒势近似的电子结构计算方法。
> 
> * * *
> 
> **TABLE III.** Average nearest-neighbor distance d₁, coordination number N_c, and bond angle θ and their root-mean-square derivations in liquid and amorphous Ge (calculated at different maximal bond lengths R_c). **表III.** 液态和非晶Ge中的平均最近邻距离d₁、配位数N_c和键角θ及其均方根偏差（在不同最大键长R_c下计算）。
> 
> 

<table>
<thead>
<tr>
<th style="text-align:left"></th>
<th style="text-align:center">R_c (Å)</th>
<th style="text-align:center">d₁ (Å)</th>
<th style="text-align:center">Δd₁ (Å)</th>
<th style="text-align:center">N_c</th>
<th style="text-align:center">θ (deg)</th>
<th style="text-align:center">Δθ (deg)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">l-Ge, T = 1250 K</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:left">ab initio MD</td>
<td style="text-align:center">3.2</td>
<td style="text-align:center">2.75</td>
<td style="text-align:center">0.24</td>
<td style="text-align:center">5.8</td>
<td style="text-align:center">99.4</td>
<td style="text-align:center">31.7</td>
</tr>
<tr>
<td style="text-align:left">ab initio MD</td>
<td style="text-align:center">3.4</td>
<td style="text-align:center">2.84</td>
<td style="text-align:center">0.29</td>
<td style="text-align:center">6.9</td>
<td style="text-align:center">98.3</td>
<td style="text-align:center">32.8</td>
</tr>
<tr>
<td style="text-align:left">classical MD</td>
<td style="text-align:center">3.4</td>
<td style="text-align:center">2.72</td>
<td style="text-align:center">—</td>
<td style="text-align:center">7.3</td>
<td style="text-align:center">100.5</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">exp.</td>
<td style="text-align:center">—</td>
<td style="text-align:center">2.75</td>
<td style="text-align:center">—</td>
<td style="text-align:center">6.8</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">Sl-Ge, T = 750–650 K</td>
<td style="text-align:center">3.0</td>
<td style="text-align:center">2.63</td>
<td style="text-align:center">0.17</td>
<td style="text-align:center">4.63</td>
<td style="text-align:center">103.1</td>
<td style="text-align:center">26.8</td>
</tr>
<tr>
<td style="text-align:left">a-Ge, T = 300 K, as-quenched</td>
<td style="text-align:center">2.8</td>
<td style="text-align:center">2.48</td>
<td style="text-align:center">0.10</td>
<td style="text-align:center">4.04</td>
<td style="text-align:center">107.7</td>
<td style="text-align:center">17.9</td>
</tr>
<tr>
<td style="text-align:left">a-Ge, T = 300 K, annealed</td>
<td style="text-align:center">2.8</td>
<td style="text-align:center">2.49</td>
<td style="text-align:center">0.10</td>
<td style="text-align:center">4.05</td>
<td style="text-align:center">107.7</td>
<td style="text-align:center">16.9</td>
</tr>
<tr>
<td style="text-align:left">a-Ge, T = 0 configuration 1</td>
<td style="text-align:center">2.8</td>
<td style="text-align:center">2.48</td>
<td style="text-align:center">0.08</td>
<td style="text-align:center">4.06</td>
<td style="text-align:center">107.7</td>
<td style="text-align:center">16.2</td>
</tr>
<tr>
<td style="text-align:left">a-Ge, T = 0 configuration 2</td>
<td style="text-align:center">2.8</td>
<td style="text-align:center">2.46</td>
<td style="text-align:center">0.06</td>
<td style="text-align:center">3.97</td>
<td style="text-align:center">108.5</td>
<td style="text-align:center">14.9</td>
</tr>
<tr>
<td style="text-align:left">Exp.</td>
<td style="text-align:center">—</td>
<td style="text-align:center">2.463</td>
<td style="text-align:center">0.047</td>
<td style="text-align:center">3.68</td>
<td style="text-align:center">108.5</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">Exp.</td>
<td style="text-align:center">—</td>
<td style="text-align:center">2.46</td>
<td style="text-align:center">0.085</td>
<td style="text-align:center">3.88</td>
<td style="text-align:center">108.0</td>
<td style="text-align:center">12.5</td>
</tr>
<tr>
<td style="text-align:left">CRN</td>
<td style="text-align:center">—</td>
<td style="text-align:center">2.46</td>
<td style="text-align:center">—</td>
<td style="text-align:center">4</td>
<td style="text-align:center">108.5</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">c-Ge</td>
<td style="text-align:center">—</td>
<td style="text-align:center">2.45</td>
<td style="text-align:center">—</td>
<td style="text-align:center">4</td>
<td style="text-align:center">109.3</td>
<td style="text-align:center">—</td>
</tr>
</tbody>
</table>


> 
> a Calculated using effective pair forces based on EC-PP (R_c = 1.03 a.u.), see Ref. 14. a 使用基于EC-PP (R_c = 1.03 a.u.)的有效对力计算，见参考文献14。 b Reference 11. 参考文献11。 c Reference 8. Average over nine sets of experiments reviewed in Ref. 8. 参考文献8。参考文献8中综述的九组实验的平均值。 d Wooten-Winer-Weaire continuous random-network model, Ref. 4. Wooten-Winer-Weaire连续随机网络模型，参考文献4。
> 
> * * *
> 
> **TABLE IV.** Distribution of the number of nearest neighbors in liquid and amorphous Ge. **表IV.** 液态和非晶Ge中最近邻数目的分布。
> 
> 

<table>
<thead>
<tr>
<th style="text-align:left"></th>
<th style="text-align:center">R_c (Å)</th>
<th style="text-align:center">Percentage of nearest neighbors with N_c =</th>
<th style="text-align:center"></th>
<th style="text-align:center"></th>
<th style="text-align:center"></th>
<th style="text-align:center"></th>
<th style="text-align:center"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left"></td>
<td style="text-align:center"></td>
<td style="text-align:center">3</td>
<td style="text-align:center">4</td>
<td style="text-align:center">5</td>
<td style="text-align:center">6</td>
<td style="text-align:center">7</td>
<td style="text-align:center">8</td>
</tr>
<tr>
<td style="text-align:left">l-Ge, T = 1250 K</td>
<td style="text-align:center">3.2</td>
<td style="text-align:center">1.2</td>
<td style="text-align:center">11.2</td>
<td style="text-align:center">29.3</td>
<td style="text-align:center">31.4</td>
<td style="text-align:center">19.7</td>
<td style="text-align:center">7.2</td>
</tr>
<tr>
<td style="text-align:left">Sl-Ge, T = 750–650 K</td>
<td style="text-align:center">3.0</td>
<td style="text-align:center">4.8</td>
<td style="text-align:center">43.5</td>
<td style="text-align:center">37.4</td>
<td style="text-align:center">14.3</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">a-Ge, T = 300 K, as-quenched</td>
<td style="text-align:center">2.8</td>
<td style="text-align:center">4.9</td>
<td style="text-align:center">86.8</td>
<td style="text-align:center">7.8</td>
<td style="text-align:center">0.5</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">a-Ge, T = 300 K, annealed</td>
<td style="text-align:center">2.8</td>
<td style="text-align:center">4.6</td>
<td style="text-align:center">85.0</td>
<td style="text-align:center">10.3</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">a-Ge, T = 0 configuration 1</td>
<td style="text-align:center">2.8</td>
<td style="text-align:center">4.7</td>
<td style="text-align:center">84.4</td>
<td style="text-align:center">10.9</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">a-Ge, T = 0 configuration 2</td>
<td style="text-align:center">2.8</td>
<td style="text-align:center">6.3</td>
<td style="text-align:center">90.6</td>
<td style="text-align:center">3.1</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
</tr>
</tbody>
</table>


> 
> * * *
> 
> ## B. Supercooled liquid Ge
> 
> ## B. 过冷液态Ge
> 
> Continuous rapid quenching of l-Ge from 1250 K (just above the melting point) to temperatures of 750 K leads to the formation of a metallic supercooled liquid: the first and second peaks in g(R) grow in amplitude and become more symmetric (Fig. 6). The average coordination number decreases to N_c = 4.63 (Table III), the analysis of the local coordinations shows that higher coordinations (N_c ≥ 6) with longer bonds are strongly reduced (Table IV). In the bond-angle distributions tetrahedral angles are now dominant, but there is still an appreciable number of close packed (θ ≈ 60°) and a small number of collinear (θ ≈ 180°) configurations [Fig. 6(c)]. In the static structure factor the peak close to Q ≈ 2k_F has the largest amplitude, the first peak has been damped and shifted to smaller momentum transfers. The only change in the electronic DOS is a slight decrease at the Fermi energy [Fig. 6(d)]. This state is clearly liquid and metallic, although the diffusion coefficient has decreased by a factor of 4 compared to the melting point (see also Fig. 4). This supercooled state is still rather well described by classical MD simulations with pseudopotential derived forces, although the increase of the local tetrahedral order with decreasing temperature is certainly underestimated. More pronounced structural changes occur only at temperatures below T ≈ 750 K. Note that the reduced value of this "amorphization temperature" T_a/T_m = 750/1250 = 0.6 is about the same as for Si. The persistence of fluidity and metallicity down to these relatively low temperatures is explained by the mechanism of the metal-semiconductor transformation: above T_a a small number bonds has a covalent character [≈13%, counting the threefold- and fourfold-coordinated sites, or ≈25%, counting the nearest-neighbor bonds shorter than the covalent bond length of Ge (2R_c = 2.45 Å) for which tetrahedral angles prevail]. These bonds are also characterized by a bond charge (i.e., a charge accumulation at midbond position in excess to a superposition of spherical free-atom charges). As the local configurations fluctuate at the time scale of the diffusive motion, the covalent bonds are rapidly destroyed and reformed. Only at a reduced atomic mobility covalent bonds that have once been formed survive and the metal-semiconductor transition occurs rather quickly. Experimentally the "glass transition" observed in laser-glazing experiments is rather sharp. However, any significant observation of the character of the transition is prohibited by the large fluctuations in our small samples.
> 
> 将l-Ge从1250 K（刚好在熔点以上）连续快速淬火到750 K的温度导致金属性过冷液体的形成：g(R)中的第一和第二峰振幅增加并变得更对称（图6）。平均配位数下降到N_c = 4.63（表III），局域配位分析表明具有较长键的更高配位（N_c ≥ 6）被强烈减少（表IV）。在键角分布中，四面体角现在占主导地位，但仍有相当数量的密堆积（θ ≈ 60°）和少量共线（θ ≈ 180°）构型[图6(c)]。在静态结构因子中，接近Q ≈ 2k_F的峰具有最大振幅，第一个峰被阻尼并移向较小的动量传递。电子DOS中的唯一变化是Fermi能量处的轻微下降[图6(d)]。这个状态显然是液态和金属性的，尽管扩散系数与熔点相比减小了4倍（另见图4）。这种过冷态仍然相当好地由具有赝势导出力的经典MD模拟描述，尽管局域四面体有序随温度降低的增加肯定被低估了。更显著的结构变化仅在低于T ≈ 750 K的温度下发生。注意，这个"非晶化温度"的约化值T_a/T_m = 750/1250 = 0.6与Si大致相同。流动性和金属性持续到这些相对较低的温度由金属-半导体转变的机制解释：在T_a以上，少量键具有共价特征[≈13%，计算三重和四重配位位点，或≈25%，计算短于Ge共价键长（2R_c = 2.45 Å）的最近邻键，其中四面体角占主导地位]。这些键还以键电荷为特征（即，在键中点位置超出球形自由原子电荷叠加的电荷积累）。由于局域构型在扩散运动的时间尺度上涨落，共价键被迅速破坏和重新形成。仅在原子迁移率降低时，一旦形成的共价键才存活下来，金属-半导体转变发生得相当快。实验上，在激光玻璃化实验中观察到的"玻璃转变"相当尖锐。然而，由于我们小样品中的大涨落，对转变特征的任何显著观察都被禁止。
> 
> **diffusion coefficient**: 扩散系数，衡量原子或分子在介质中扩散速率的参数。 **bond charge**: 键电荷，共价键中原子间区域积累的电子电荷。 **glass transition**: 玻璃化转变，过冷液体转变为玻璃态非晶固体的过程。
> 
> * * *
> 
> ## C. Amorphous Ge
> 
> ## C. 非晶Ge
> 
> Our results for the structural and electronic properties of as-quenched amorphous Ge are given in Fig. 7. The agreement of the calculated g(R) and S(Q) with the neutron-diffraction is good, the main difference is that the separation of the first two peaks in g(R) [and to some extent also in S(Q)] is less pronounced in the computer experiment. The computer-generated amorphous sample is slightly overcoordinated (N_c = 4.04), indicating that fivefold coordinated defects are somewhat more frequent than threefold-coordinated sites (see Tables III and IV). The DOS in the gap at the Fermi level is strongly reduced, the overall shape of the DOS represents the photoemission intensities rather well. Annealing leads to a distinct improvement of the agreement between simulation and experiment (see Fig. 8), but no reduction of the number of defects. This concerns, in particular, the medium-range order as represented by the higher-order oscillations in g(R). The model is still slightly overcoordinated (N_c = 4.05), fivefold defects dominate over threefold-coordinated sites. That some experiments give lower coordination numbers is almost entirely due to the underestimate of the microscopic density by nearly 10% (see above). The width of the bond-angle distribution (Δθ ≈ 17°) is slightly larger than in the best continuous random network models adjusted to the experimental diffraction data (see Table III). The calculated DOS at the Fermi level is reduced by annealing, the calculated n(E) is in very good agreement with the photoemission data. Compared to the liquid state, the pseudogap at E_F − 4.5 eV persists, a second gap develops at the Fermi level, a shallow DOS minimum appears at −7 eV. The three regions of the DOS below −7 eV, between −7 eV and −4.5 eV, and between −4.5 eV and the Fermi level correspond rather well to the three sp subbands of the crystalline tetrahedral semiconductors (the S, M, and P parts of the valence band according to the conventional nomenclature). This indicates an sp hybridization of the valence band similar to the crystal and in contrast to the metallic liquid. The DOS in the gap at the Fermi level remains finite, independently of the k-space sampling and the level broadening. An analysis of the charge distribution of the states in the gap shows that these states tend to be localized (see also Sec. VI).
> 
> 我们对淬火态非晶Ge的结构和电子性质的结果在图7中给出。计算的g(R)和S(Q)与中子衍射的一致性很好，主要区别在于g(R) [在某种程度上也在S(Q)中]前两个峰的分离在计算机实验中不太明显。计算机生成的非晶样品略微过配位（N_c = 4.04），表明五重配位缺陷比三重配位位点更频繁（见表III和IV）。Fermi能级处隙中的DOS强烈降低，DOS的整体形状相当好地代表了光电子发射强度。退火导致模拟与实验之间的一致性明显改善（见图8），但没有减少缺陷数量。这特别涉及由g(R)中高阶振荡代表的中程有序。模型仍然略微过配位（N_c = 4.05），五重缺陷主导于三重配位位点。一些实验给出较低配位数几乎完全是由于微观密度被低估近10%（见上文）。键角分布的宽度（Δθ ≈ 17°）略大于调整到实验衍射数据的最佳连续随机网络模型（见表III）。在Fermi能级处的计算DOS通过退火降低，计算的n(E)与光电子发射数据非常好地吻合。与液态相比，E_F − 4.5 eV处的赝隙持续存在，在Fermi能级处形成第二个隙，在−7 eV处出现一个浅DOS极小值。DOS在−7 eV以下、−7 eV和−4.5 eV之间以及−4.5 eV和Fermi能级之间的三个区域，与晶体四面体半导体的三个sp子带（根据传统命名法的价带S、M和P部分）相当好地对应。这表明价带的sp杂化与晶体相似，与金属液体形成对比。Fermi能级处隙中的DOS保持有限，与k空间采样和能级展宽无关。对隙中态电荷分布的分析表明这些态倾向于局域化（另见第VI节）。
> 
> **medium-range order**: 中程有序，在超过最近邻尺度但不到长程晶体有序范围的原子结构有序性。
> 
> * * *
> 
> # V. ATOMIC DYNAMICS
> 
> # V. 原子动力学
> 
> The MD-generated trajectories allow us to investigate atomic transport and dynamics.
> 
> MD生成的轨迹使我们能够研究原子输运和动力学。
> 
> * * *
> 
> ## A. Single-particle dynamics and atomic transport
> 
> ## A. 单粒子动力学和原子输运
> 
> The simplest way to investigate atomic transport in liquids is to derive the self-diffusion coefficient D from the time dependence of the mean-square displacement
> 
> 研究液体中原子输运的最简单方式是从均方位移的时间依赖性导出自扩散系数D
> 
> * * *
> 
> where D is the self-diffusion coefficient and c is a constant. The average in (23) has to be taken over the ensemble and over different starting points along the trajectory. ⟨r²(t)⟩ for various temperatures is shown in Fig. 4, the diffusion constant as a function of temperature is given in Fig. 9. The value close to the melting point (D = 1.0 × 10⁻⁴ cm² s⁻¹) is of the same order of magnitude as for liquid Si near the melting point [D = 2.0 × 10⁻⁴ cm² s⁻¹ (Ref. 47)]; no data for l-Ge are available (but see Note added in proof). At the temperature where the metal-semiconductor transition is thought to begin, the diffusibility has dropped to about 6% of its value at the melting point. An alternative access to the diffusion coefficient is via the velocity autocorrelation function ψ(t).
> 
> 其中D是自扩散系数，c是常数。(23)中的平均值必须对系综和沿轨迹的不同起点取。各种温度下的⟨r²(t)⟩如图4所示，扩散常数作为温度的函数在图9中给出。接近熔点的值（D = 1.0 × 10⁻⁴ cm² s⁻¹）与液态Si在熔点附近的量级相同[D = 2.0 × 10⁻⁴ cm² s⁻¹（参考文献47）]；没有l-Ge的数据可用（但见校样中添加的注释）。在认为金属-半导体转变开始的温度下，扩散性已下降到其熔点值的约6%。获取扩散系数的另一种途径是通过速度自相关函数ψ(t)。
> 
> **self-diffusion coefficient**: 自扩散系数，在无浓度梯度条件下原子扩散速率的量度。 **velocity autocorrelation function**: 速度自相关函数，描述粒子速度与其初始速度时间相关性的统计函数。
> 
> * * *
> 
> Again, the average is over the ensemble and over different starting points along the equilibrium part of the MD trajectory. The diffusion coefficient D is then given by
> 
> 同样，平均值是对系综和沿MD轨迹平衡部分的不同起点取的。扩散系数D然后由下式给出
> 
> * * *
> 
> The results are given in Fig. 9 and are in good agreement with the values derived from the mean-square displacements.
> 
> 结果在图9中给出，与从均方位移导出的值吻合良好。
> 
> * * *
> 
> ## B. Collective dynamics
> 
> ## B. 集体动力学
> 
> The velocity autocorrelation functions shown in Fig. 10 also carry information on the collective dynamics of the system. For a purely Brownian motion ψ(t) is monotonously decreasing. For l-Ge the monotonic (diffusive) part is superposed by an oscillation of a period of about 0.2 ps, but the first few oscillations remain positive. This distinguishes l-Ge from l-Ar or l-Na, where ψ(t) becomes negative already at the first oscillation. The negative values of ψ(t) show the importance of the caging effect of the neighboring atoms over the purely diffusive motion, the long-range oscillations are characteristic for metallic bonding as compared to van der Waals bonding in the rare-gas fluids. Our results show that in l-Ge the metallic bonding effects are clearly visible, but due to the rather loose packing the diffusive motion dominates over the caging effect. The Fourier transform of ψ(t) defines the spectrum of the autocorrelation function.
> 
> 图10中显示的速度自相关函数也携带关于系统集体动力学的信息。对于纯Brown运动，ψ(t)单调递减。对于l-Ge，单调（扩散）部分被周期约0.2 ps的振荡叠加，但前几个振荡保持正值。这将l-Ge与l-Ar或l-Na区分开来，在后者中ψ(t)在第一次振荡时已经变为负值。ψ(t)的负值表明相邻原子的笼蔽效应相对于纯扩散运动的重要性，长程振荡是金属键合相对于稀有气体流体中van der Waals键合的特征。我们的结果表明，在l-Ge中金属键合效应清晰可见，但由于相当松散的堆积，扩散运动主导于笼蔽效应。ψ(t)的Fourier变换定义了自相关函数的谱。
> 
> **Brownian motion**: 布朗运动，由于与周围介质粒子的随机碰撞导致的粒子随机运动。 **caging effect**: 笼蔽效应，液态中原子被其邻居临时限制在局部"笼子"中的现象。 **van der Waals bonding**: 范德瓦尔斯键合，由瞬时偶极涨落引起的弱分子间相互作用。
> 
> * * *
> 
> ψ(ω) is shown in Fig. 11. Besides the low-frequency diffusive modes one identifies an inelastic side peak at 30 meV, which is clearly related to the longitudinal acoustic modes in amorphous and crystalline Ge (see also below). The identification of these modes with longitudinal density fluctuations is in the spirit of the "diffusion-Umklapp model" for the dynamics of liquid and amorphous materials and is certainly more realistic than their assignment to transverse optic vibrations (note that the stiffness of the bond angles is greatly reduced in the metallic liquid and that shear modes are more strongly damped than collective density fluctuations). Figure 10(b) shows the velocity autocorrelation function for amorphous Ge. The diffusive background has disappeared, the complex time dependence of ψ(t) arises from the superposition of several characteristic eigenfrequencies. After correction for the phonon-occupation function n(ω), the spectrum of the velocity autocorrelation function may be compared with the vibrational DOS G(ω) determined from neutron-inelastic scattering experiments [G(ω) = ψ(ω) (ω)]. Figure 12 shows the result of the ab initio MD simulation for annealed amorphous Ge, compared with experimental data on highly ordered and disordered a-Ge. The four peaks and shoulders in the calculated spectrum correspond (in the sequence of increasing energies) to the TA, LA, LO, and TO eigenmodes of polycrystalline Ge. The spectrum is in really good agreement with experiment. We have also investigated the effect of the local order on the vibrational DOS. If the average for ψ(t) is performed only over the subensemble of the fourfold coordinated sites, the changes in G(ω) correspond exactly to the differences observed between the disordered and the highly-ordered samples. Compared to the vibrational spectrum of amorphous metals, the vibrational DOS of a-Ge shows much more distinctive features reminiscent of the crystal. This reflects the higher degree of local order.
> 
> ψ(ω)如图11所示。除了低频扩散模式外，在30 meV处识别出一个非弹性侧峰，这显然与非晶和晶体Ge中的纵向声学模式相关（另见下文）。将这些模式识别为纵向密度涨落符合液态和非晶材料动力学的"扩散-Umklapp模型"的精神，并且肯定比将它们指定为横向光学振动更现实（注意，键角的刚度在金属液体中大大降低，剪切模式比集体密度涨落受到更强的阻尼）。图10(b)显示了非晶Ge的速度自相关函数。扩散背景已经消失，ψ(t)的复杂时间依赖性来自几个特征本征频率的叠加。在对声子占据函数n(ω)进行修正后，速度自相关函数的谱可以与从中子非弹性散射实验确定的振动DOS G(ω)进行比较[G(ω) = ψ(ω) (ω)]。图12显示了退火非晶Ge的从头计算MD模拟结果，与高度有序和无序a-Ge的实验数据进行比较。计算谱中的四个峰和肩峰（按能量增加的顺序）对应于多晶Ge的TA、LA、LO和TO本征模式。谱与实验确实吻合良好。我们还研究了局域有序对振动DOS的影响。如果ψ(t)的平均值仅对四重配位位点的子系综进行，G(ω)的变化恰好对应于无序和高度有序样品之间观察到的差异。与非晶金属的振动谱相比，a-Ge的振动DOS显示出更多让人联想到晶体的独特特征。这反映了更高程度的局域有序。
> 
> **longitudinal acoustic modes**: 纵向声学模式，原子位移平行于波传播方向的低频晶格振动。 **TA, LA, LO, TO eigenmodes**: 横声学(TA)、纵声学(LA)、纵光学(LO)、横光学(TO)本征模式，晶格振动的四种基本模式类型。 **phonon-occupation function**: 声子占据函数，描述给定温度下声子态平均占据数的玻色-爱因斯坦分布。
> 
> * * *
> 
> # VI. DEFECTS
> 
> # VI. 缺陷
> 
> The characteristic defects in a-Si and a-Ge are believed to be undercoordinated atoms, usually referred to as "dangling bonds." The view is based on the interpretation of the electron paramagnetic resonance signal (EPR). Recently, this view has been challenged and it has been suggested that the EPR-active center can also be a fivefold coordinated site with an electron state described as a "floating bond." Computer experiments based on classical many-body forces show that, depending on the way the amorphous sample is prepared, threefold and fivefold coordinated defects are found in varying concentrations. In the most recent ab initio MD simulations of a-Si, only fivefold (T₅) defects have been found, but in earlier runs threefold (T₃) defects were detected as well. In our study, we found that a purely geometrical definition of a defect is insufficient, but bonding and spectral properties must be considered as well. Due to fluctuation of the local defects already discussed in Sec. III, we found it most convenient to do the defect analysis for T = 0 configurations. Two different configurations were generated by slow and fast quenching after annealing (see Sec. III), the pair-correlation functions for both configurations are shown in Fig. 13. Overall the agreement between both configurations is rather good, the number of defects is definitely larger for the first configuration (prepared by a slow quench), but this configuration shows better agreement with experiment for g(R) at large distances. Interestingly a number of atoms are for both configurations located in the minimum between the first and second peak of the pair-correlation function.
> 
> a-Si和a-Ge中的特征缺陷被认为是低配位原子，通常称为"悬挂键"。这一观点基于电子顺磁共振信号（EPR）的解释。最近，这一观点受到挑战，有人提出EPR活性中心也可以是五重配位位点，其电子态被描述为"浮动键"。基于经典多体力的计算机实验表明，根据非晶样品制备方式的不同，三重和五重配位缺陷以不同浓度存在。在a-Si的最新从头计算MD模拟中，仅发现了五重（T₅）缺陷，但在早期运行中也检测到三重（T₃）缺陷。在我们的研究中，我们发现缺陷的纯几何定义是不充分的，必须同时考虑成键和光谱性质。由于第III节已经讨论过的局域缺陷涨落，我们发现对T = 0构型进行缺陷分析最方便。退火后通过慢速和快速淬火生成了两种不同的构型（见第III节），两种构型的对关联函数如图13所示。总体而言，两种构型之间的一致性相当好，第一种构型（通过慢速淬火制备）的缺陷数量明显更大，但这种构型在大距离处g(R)与实验的一致性更好。有趣的是，两种构型中都有一些原子位于对关联函数第一和第二峰之间的极小值处。
> 
> **dangling bonds**: 悬挂键，由于配位不足而在非晶半导体中产生的未配对电子轨道。 **electron paramagnetic resonance (EPR)**: 电子顺磁共振，检测未配对电子自旋的光谱技术。 **floating bond**: 浮动键，过配位原子中非定域化的电子态，作为悬挂键的替代缺陷模型。
> 
> * * *
> 
> ## A. Geometrical defects
> 
> ## A. 几何缺陷
> 
> To characterize geometrical or coordination defects, one has to define the maximum length R_c of a nearest-neighbor bond. Because the minimum in g(R) is not sharply defined for our a-Ge models (cf. Figs. 8 and 13), even a small change of R_c may fundamentally change the results of the analysis. This is demonstrated in Table V for both a-Ge models generated by the quasi-Newton quench. If the bond length is fixed at R_c = 2.8 Å, we find three T₃ and seven T₅ defects after the slow quench, and four T₃ and two T₅ defects after the fast quench. If R_c is increased to 3.0 Å there are no T₃ sites and we count 14 T₅ defects after the slow quench, and two T₃ and eight T₅ after the fast quench. Atom number 18 that has first been described as T₃, is now considered to be T₅. It is significant that the bond angles around both types of defects are reduced and have a broader distribution. For T₃ sites the average bond angle is θ = 100.8°, i.e., considerably smaller than the tetrahedral bond angle and only slightly larger than the bond angle in threefold coordinated As (θ = 97.2°).
> 
> 为了表征几何或配位缺陷，必须定义最近邻键的最大长度R_c。由于g(R)中的极小值在我们a-Ge模型中未明确定义（参见图8和13），即使R_c的微小变化也可能从根本上改变分析结果。这在表V中对准牛顿淬火生成的两种a-Ge模型进行了说明。如果键长固定在R_c = 2.8 Å，我们发现慢速淬火后有三个T₃和七个T₅缺陷，快速淬火后有四个T₃和两个T₅缺陷。如果R_c增加到3.0 Å，则没有T₃位点，我们计算慢速淬火后有14个T₅缺陷，快速淬火后有两个T₃和八个T₅。最初被描述为T₃的18号原子，现在被认为是T₅。重要的是，两种缺陷周围的键角都减小了，并且具有更宽的分布。对于T₃位点，平均键角为θ = 100.8°，即显著小于四面体键角，仅略大于三重配位As中的键角（θ = 97.2°）。
> 
> * * *
> 
> ## B. Bonding defects
> 
> ## B. 成键缺陷
> 
> Evidently, a purely geometrical characterization of defects is insufficient. The tetrahedral sp³ bond of the crystalline semiconductors is characterized by the bond charges placed in the midbond position. The bond charge may be visualized by plotting the electron density. Figure 14(a) shows the electron density for a slightly distorted tetrahedral configuration. The bond charges along the four bonds are clearly visible. Figure 14(b) shows the charge distribution around atom No. 55 in configuration 2, i.e., one of the two genuine T₃ sites. The atoms are arranged in the form of a trigonal prism with well-defined bond to the three neighbors of the central atom. A diffuse charge accumulation in the direction of the back bonds is all that can be seen of a "dangling bond." Figures 14(c), 14(d), and 14(e) show three T₅ sites (atoms No. 20, 36, and 63). T₅ sites tend to have 3 or 4 "strong" and 2 or 1 "weak" bonds: if an additional atom is squeezed into the tetrahedral configuration the distortion weakens the bonds closest to the added atom. Only exceptionally we find a T₅ site with five equally strong bonds [Fig. 14(e)]. The existence of a bond charge depends very critically on the length of the bond: for d₁ ≥ 2.85 Å no bond charges have been found. Therefore, R_c = 2.8 Å for the maximum bond length leads to a physically more meaningful definition of defects than the pure geometrical definition in terms of the position of the minimum in g(R). The small hump in the minimum of g(R) contains most of the weak bonds of the T₅ defects. A particularly interesting feature is found in the charge distribution around atom No. 18 [see Fig. 14(f)]. The site is described as T₃ or T₅, depending on the assumption on the maximum length of a nearest-neighbor bond. The bonds to the two more distant neighbors are very weak and the three remaining bonds are nearly coplanar, i.e., the bond angles are considerably strained. Only two of the bonds have well-defined bond charges, the third bond is rather asymmetric, with most of the charge concentrated on the central atom. We shall see in a moment, that this defect has peculiar spectral properties.
> 
> 显然，纯几何的缺陷表征是不充分的。晶体半导体的四面体sp³键以位于键中点位置的键电荷为特征。键电荷可以通过绘制电子密度来可视化。图14(a)显示了一个轻微扭曲的四面体构型的电子密度。沿四个键的键电荷清晰可见。图14(b)显示了构型2中55号原子周围的电荷分布，即两个真正的T₃位点之一。原子以三棱柱形式排列，与中心原子的三个邻居有明确定义的键。在背键方向的弥散电荷积累是"悬挂键"所能看到的全部。图14(c)、14(d)和14(e)显示了三个T₅位点（20、36和63号原子）。T₅位点倾向于有3或4个"强"键和2或1个"弱"键：如果额外原子挤进四面体构型，扭曲会削弱最接近添加原子的键。仅在例外情况下，我们发现一个具有五个同等强度键的T₅位点[图14(e)]。键电荷的存在非常关键地取决于键长：对于d₁ ≥ 2.85 Å，未发现键电荷。因此，最大键长R_c = 2.8 Å导致比根据g(R)中极小值位置的纯几何定义在物理上更有意义的缺陷定义。g(R)极小值中的小驼峰包含了T₅缺陷的大部分弱键。在18号原子周围的电荷分布中发现了特别有趣的特征[见图14(f)]。该位点被描述为T₃或T₅，取决于最近邻键最大长度的假设。与两个更远邻居的键非常弱，三个剩余键几乎共面，即键角相当受应变。只有两个键有明确定义的键电荷，第三个键相当不对称，大部分电荷集中在中心原子上。我们稍后将看到，这个缺陷具有特殊的光谱性质。
> 
> **sp³ bond**: sp³杂化键，由一个s轨道和三个p轨道混合形成的四面体成键轨道。 **trigonal prism**: 三棱柱，六个原子围绕中心原子形成三棱柱形的配位多面体。
> 
> * * *
> 
> **TABLE V.** Structural characteristics of tetrahedrally coordinated (T₄) and of defect (T₃, T₅) sites in two a-Ge models generated by quasi-Newton quenches. **表V.** 准牛顿淬火生成的两种a-Ge模型中四面体配位（T₄）和缺陷（T₃, T₅）位点的结构特征。
> 
> **R_c = 2.8 Å**
> 
> 

<table>
<thead>
<tr>
<th style="text-align:left"></th>
<th style="text-align:center">Percentage</th>
<th style="text-align:center"></th>
<th style="text-align:center"></th>
<th style="text-align:center">d₁ (Å)</th>
<th style="text-align:center">Δd₁ (Å)</th>
<th style="text-align:center">θ (deg)</th>
<th style="text-align:center">Δθ (deg)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">Model 1 (slow quench)</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:left">T₃</td>
<td style="text-align:center">4.7</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.52</td>
<td style="text-align:center">0.12</td>
<td style="text-align:center">100.2</td>
<td style="text-align:center">19.8</td>
</tr>
<tr>
<td style="text-align:left">T₄</td>
<td style="text-align:center">84.4</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.47</td>
<td style="text-align:center">0.06</td>
<td style="text-align:center">108.8</td>
<td style="text-align:center">13.5</td>
</tr>
<tr>
<td style="text-align:left">T₅</td>
<td style="text-align:center">10.9</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.56</td>
<td style="text-align:center">0.11</td>
<td style="text-align:center">103.5</td>
<td style="text-align:center">24.4</td>
</tr>
<tr>
<td style="text-align:left">Model 2 (fast quench)</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:left">T₃</td>
<td style="text-align:center">6.3</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.44</td>
<td style="text-align:center">0.04</td>
<td style="text-align:center">107.2</td>
<td style="text-align:center">18.1</td>
</tr>
<tr>
<td style="text-align:left">T₄</td>
<td style="text-align:center">90.6</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.45</td>
<td style="text-align:center">0.06</td>
<td style="text-align:center">108.7</td>
<td style="text-align:center">13.9</td>
</tr>
<tr>
<td style="text-align:left">T₅</td>
<td style="text-align:center">3.1</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.57</td>
<td style="text-align:center">0.07</td>
<td style="text-align:center">105.7</td>
<td style="text-align:center">26.2</td>
</tr>
</tbody>
</table>


> 
> T₃: Atom Nos. 1, 18, 39, 55 T₃: 原子编号 1, 18, 39, 55 T₅: Atom Nos. 61, 63 T₅: 原子编号 61, 63
> 
> **R_c = 3.0 Å**
> 
> 

<table>
<thead>
<tr>
<th style="text-align:left"></th>
<th style="text-align:center">Percentage</th>
<th style="text-align:center"></th>
<th style="text-align:center"></th>
<th style="text-align:center">d₁ (Å)</th>
<th style="text-align:center">Δd₁ (Å)</th>
<th style="text-align:center">θ (deg)</th>
<th style="text-align:center">Δθ (deg)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left">Model 1 (slow quench)</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:left">T₃</td>
<td style="text-align:center">0</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
<td style="text-align:center">—</td>
</tr>
<tr>
<td style="text-align:left">T₄</td>
<td style="text-align:center">78.1</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.46</td>
<td style="text-align:center">0.07</td>
<td style="text-align:center">108.9</td>
<td style="text-align:center">13.0</td>
</tr>
<tr>
<td style="text-align:left">T₅</td>
<td style="text-align:center">21.9</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.59</td>
<td style="text-align:center">0.15</td>
<td style="text-align:center">104.1</td>
<td style="text-align:center">25.3</td>
</tr>
<tr>
<td style="text-align:left">Model 2 (fast quench)</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
</tr>
<tr>
<td style="text-align:left">T₃</td>
<td style="text-align:center">3.1</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.44</td>
<td style="text-align:center">0.03</td>
<td style="text-align:center">100.3</td>
<td style="text-align:center">16.6</td>
</tr>
<tr>
<td style="text-align:left">T₄</td>
<td style="text-align:center">84.4</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.45</td>
<td style="text-align:center">0.06</td>
<td style="text-align:center">108.6</td>
<td style="text-align:center">13.6</td>
</tr>
<tr>
<td style="text-align:left">T₅</td>
<td style="text-align:center">12.5</td>
<td style="text-align:center"></td>
<td style="text-align:center"></td>
<td style="text-align:center">2.58</td>
<td style="text-align:center">0.14</td>
<td style="text-align:center">103.7</td>
<td style="text-align:center">25.7</td>
</tr>
</tbody>
</table>


> 
> T₃: Atom Nos. 39, 55 T₃: 原子编号 39, 55 T₅: Atom Nos. 15, 18, 20, 36, 40, 52, 61, 63 T₅: 原子编号 15, 18, 20, 36, 40, 52, 61, 63
> 
> * * *
> 
> ## C. Spectral defects
> 
> ## C. 光谱缺陷
> 
> Of greatest importance for the electronic properties of amorphous semiconductors are the spectral defects, i.e. the defects giving rise to states in the gap. The recent work of Drabold et al. has shown that a geometrical defect is neither a necessary nor a sufficient condition for the existence of a spectral defect. We have analyzed the one-electron states in the gap by analyzing their electron density distributions and localization properties. To study localization we have subdivided the MD cell into a grid of M = m³ small cubes. The localization parameter L is defined as
> 
> 对非晶半导体电子性质最重要的是光谱缺陷，即在隙中产生态的缺陷。Drabold等人最近的工作已经表明，几何缺陷既不是光谱缺陷存在的必要条件，也不是充分条件。我们通过分析隙中单电子态的电子密度分布和局域化性质来分析它们。为了研究局域化，我们将MD胞细分为M = m³个小立方体的网格。局域化参数L定义为
> 
> * * *
> 
> where q_i,n is the charge contained in the ith cell for the nth band. If the charges are normalized according to Σ_i q_i,n = 1, L = 1 characterizes a completely extended state, and L = 1/M a state localized within a single small cube. An analysis with m = 8, 16, 32 for the quenched configuration 2 shows that the highest occupied state (n = 128) is distinctly more localized than all other states (occupied or empty). Indeed the charge density corresponding to this state is concentrated in a single charge density maximum close to atom No. 18. This is shown in Fig. 15. Part (b) shows the total electron density in the vicinity of this site: it is evident that atom 18 together with its two neighbors forming long bonds forms an isosceles triplet and that this "metallic configuration" is characterized by the absence of covalent bond charges. Part (a) of the figure shows the electron density for band No. 128 only: the charge is concentrated in the direction of the third weak bond of atom 18 [the "asymmetric" bond of Fig. 14(f)]. This shows that while we have a relatively large number of geometrical defects in this configuration, they create only a single localized state. This state is associated with a strong local perturbation of tetrahedral bonding, not only a coordination defect, but in addition, a very strong strain on nearly all bond angles. However, we have to remember that even small fluctuations in the atomic geometry can induce relatively large changes in the spectrum, especially in the states situated in the energy gap. This is illustrated in Fig. 16 where we show the time evolution (at T = 300 K) of the electronic eigenvalues close to the gap. It is evident that the states in the gap show the largest fluctuation and these fluctuations are associated with formation and decay of localized states. The ab initio MD simulation offers the possibility of investigating these important phenomena. Here we have merely touched the problem and shown that it has become tractable. Future work will be needed in order to assess the local defects that are really characteristic for amorphous semiconductors and their spectral properties.
> 
> 其中q_i,n是第n个能带在第i个胞中包含的电荷。如果电荷根据Σ_i q_i,n = 1归一化，L = 1表征完全扩展的态，L = 1/M表征局域在单个小立方体内的态。对淬火构型2用m = 8, 16, 32进行的分析表明，最高占据态（n = 128）明显比所有其他态（占据或空）更局域化。确实，对应于该态的电荷密度集中在接近18号原子的单个电荷密度极大值中。这在图15中显示。部分(b)显示了该位点附近的总电子密度：显然，18号原子与其两个形成长键的邻居一起形成等腰三重态，这个"金属构型"以缺乏共价键电荷为特征。图的部分(a)仅显示了128号能带的电子密度：电荷集中在18号原子第三个弱键[图14(f)中的"不对称"键]的方向。这表明，虽然我们在该构型中有相对大量的几何缺陷，但它们只产生一个局域态。该态与四面体键合的强烈局域微扰相关，不仅是配位缺陷，而且额外地在几乎所有键角上存在非常强的应变。然而，我们必须记住，即使原子几何的微小涨落也能在谱中引起相对大的变化，特别是在位于能隙中的态。这在图16中说明，我们显示了隙附近电子本征值的时间演化（T = 300 K）。显然，隙中的态显示出最大的涨落，这些涨落与局域态的形成和衰减相关。从头计算MD模拟提供了研究这些重要现象的可能性。这里我们仅触及了问题，并表明它已变得可处理。未来需要工作来评估非晶半导体真正特征的局域缺陷及其光谱性质。
> 
> **localization parameter**: 局域化参数，衡量电子态在空间中定域程度的量度。 **extended state**: 扩展态，电子波函数在空间中广泛分布的态，与局域态相对。
> 
> * * *
> 
> # VII. SUMMARY AND CONCLUSIONS
> 
> # VII. 总结与结论
> 
> We have presented an ab initio study of the liquid-metal—amorphous-semiconductor transition in Ge. Our calculation is based on a novel variant of density-functional molecular dynamics that allows us to perform simulations for metallic systems with perfect control of adiabaticity while correctly describing occupied and empty states on both sides of the Fermi level. Our approach is based on finite-temperature local-density functional theory, direct energy minimization using a preconditioned conjugate gradient technique, very accurate pseudopotentials, and on Nosé dynamics for simulating a canonical ensemble. Although we perform an exact energy minimization after each MD step, our technique is at least as efficient as CP calculations: the time step is larger than a typical CP-time step by a factor of 10–20, each energy-minimization requires an average two to three conjugate-gradient steps (one CG step requiring about two times the CPU-time of one CP step). Hence there is a gain in computational efficiency by a factor of 1.5–2. To be specific, a 1 ps run for liquid Ge took about 16 h CPU on an SNI-Fujitsu S100. The efficiency of our code allows us to perform relatively extended simulations. The overall length of our MD run (including the second cooling run) was 30 ps. This is sufficient to obtain an accurate description of the structural, dynamic, and electronic properties of liquid and amorphous Ge: our computer-generated data are in good agreement with neutron diffraction, inelastic neutron scattering, and photoemission data. Beyond the examination of properties accessible also to laboratory experiments, our computer experiments serve to investigate many-atom correlations, the geometrical bonding, and spectral properties of defects in the amorphous network. Our analysis shows that the computer-generated model contains both undercoordinated (T₃) or "dangling-bond" and overcoordinated (T₅) or "weak-bond" defects. We also find that a purely geometrical definition of a defect is not always meaningful—the analysis of the bonding and spectral properties gives a physically more meaningful picture.
> 
> 我们报道了Ge中液态金属-非晶半导体转变的从头计算研究。我们的计算基于密度泛函分子动力学的一种新变体，使我们能够对金属系统进行模拟，同时完美控制绝热性，并正确描述Fermi能级两侧的占据态和空态。我们的方法基于有限温度局域密度泛函理论、使用预条件共轭梯度技术的直接能量最小化、非常精确的赝势，以及用于模拟正则系综的Nosé动力学。虽然我们在每个MD步骤之后执行精确的能量最小化，但我们的技术至少与CP计算一样高效：时间步长比典型CP时间步长大10–20倍，每次能量最小化平均需要两到三个共轭梯度步骤（一个CG步骤需要约两倍于一个CP步骤的CPU时间）。因此，计算效率提高了1.5–2倍。具体来说，液态Ge的1 ps运行在SNI-Fujitsu S100上需要约16小时CPU。我们代码的效率允许我们执行相对扩展的模拟。我们MD运行的总体长度（包括第二次冷却运行）为30 ps。这足以获得对液态和非晶Ge的结构、动力学和电子性质的精确描述：我们计算机生成的数据与中子衍射、非弹性中子散射和光电子发射数据吻合良好。除了检查实验室实验也可获得的性质外，我们的计算机实验还用于研究非晶网络中的多原子关联、几何成键和缺陷的光谱性质。我们的分析表明，计算机生成的模型包含低配位（T₃）或"悬挂键"缺陷和过配位（T₅）或"弱键"缺陷两者。我们还发现，缺陷的纯几何定义并不总是有意义的——成键和光谱性质的分析给出了物理上更有意义的图像。
> 
> **inelastic neutron scattering**: 非弹性中子散射，通过测量中子能量损失来探测材料中动态过程的技术。 **photoemission**: 光电子发射，通过测量光电子动能来研究材料电子结构的光谱技术。
> 
> * * *
> 
> Finally, we want to come back to the technical merit of our work. Based on developments published in a series of different papers, our technique assembles all the ingredients necessary for making ab initio MD calculations for metals as straightforward and reliable as CP calculations for semiconductors. The challenge is now to extend the approach to transition metals. We have recently completed a version of the code based on the use of ultrasoft pseudopotentials making ab initio MD simulations for transition metals feasible. Note added in proof. We recently became aware that the self-diffusion coefficient of liquid Ge has been measured by P. V. Pavlov and E. V. Dobrokhotov [Sov. Phys. Solid State 12, 225 (1970)], using two different methods. The experimental values quoted by these authors are D = 1.21 × 10⁻⁴ cm² s⁻¹ and D = 0.78 × 10⁻⁴ cm² s⁻¹ close to the melting point, in reasonable agreement with D_theor = 1.0 × 10⁻⁴ cm² s⁻¹. J. H. thanks Dr. I. L. Gavzou for bringing this reference to his attention.
> 
> 最后，我们想回到我们工作的技术优点。基于一系列不同论文中发表的发展，我们的技术组装了使金属的从头计算MD计算像半导体的CP计算一样直接和可靠所需的所有要素。现在的挑战是将该方法扩展到过渡金属。我们最近完成了基于超软赝势使用的代码版本，使过渡金属的从头计算MD模拟成为可行。校样中添加的注释。我们最近注意到P. V. Pavlov和E. V. Dobrokhotov [Sov. Phys. Solid State 12, 225 (1970)]使用两种不同方法测量了液态Ge的自扩散系数。这些作者引用的实验值在熔点附近为D = 1.21 × 10⁻⁴ cm² s⁻¹和D = 0.78 × 10⁻⁴ cm² s⁻¹，与D_theor = 1.0 × 10⁻⁴ cm² s⁻¹合理一致。J. H.感谢Dr. I. L. Gavzou提请其注意这一参考文献。
> 
> **transition metals**: 过渡金属，具有部分填充d轨道的金属元素，其电子结构计算特别具有挑战性。 **ultrasoft pseudopotentials**: 超软赝势，允许使用极低平面波截止能量的赝势类型，对过渡金属计算特别有用。
> 
> * * *
> 
> # ACKNOWLEDGMENT
> 
> # 致谢
> 
> This work has been supported by Siemens-Nixdorf Austria within the contract with the Technische Universität Wien.
> 
> 本工作得到了Siemens-Nixdorf Austria在维也纳工业大学合同框架内的支持。
> 
> * * *
> 
> ## References
> 
> ## 参考文献
> 
> 1.  See, for instance, S. R. Elliott, _Physics of Amorphous Materials_ (Longman, London 1984); _Amorphous Materials: Modeling of Structure and Properties_, Conference Proceedings of the Metallurgical Society of AIME, edited by V. Vitek (AIME, New York 1983); N. E. Cusack, _The Physics of Structurally Disordered Matter_ (Hilger, Bristol, 1987). 参见例如S. R. Elliott, _非晶材料物理学_ (Longman, 伦敦 1984); _非晶材料：结构与性质建模_, AIME冶金学会会议论文集, V. Vitek编辑 (AIME, 纽约 1983); N. E. Cusack, _结构无序物质物理学_ (Hilger, 布里斯托尔, 1987)。
>     
> 2.  See, e.g., _Investigations of Higher Order Correlation Functions_, edited by J. Suck, D. Quitmann, and B. Maier [J. Phys. (Paris) Colloq. 46, C9 (1985)]. 参见例如_高阶关联函数研究_, J. Suck, D. Quitmann和B. Maier编辑 [J. Phys. (Paris) Colloq. 46, C9 (1985)]。
>     
> 3.  D. E. Polk and D. S. Boudreaux, Phys. Rev. Lett. 31, 92 (1973).
>     
> 4.  F. Wooten and D. Weaire, Solid State Phys. 40, 2 (1987).
>     
> 5.  For simple-metal systems see, e.g., J. Hafner and S. S. Jaswal, Phys. Rev. B 37, 7311 (1988); for transition-metal systems see Ch. Hausleitner and J. Hafner, _ibid._ 45, 128 (1992); B 47, 5689 (1993), and references cited therein. 对于简单金属系统，参见例如J. Hafner和S. S. Jaswal, Phys. Rev. B 37, 7311 (1988); 对于过渡金属系统，参见Ch. Hausleitner和J. Hafner, _同上_ 45, 128 (1992); B 47, 5689 (1993)及其中引用的参考文献。
>     
> 6.  A. Baranyai, I. Ruff, and R. L. McGreevy, J. Phys. C 19, 453 (1986); T. F. Soules, J. Chem. Phys. 71, 4570 (1979).
>     
> 7.  J. Hafner, _From Hamiltonians to Phase Diagrams_ (Springer, Berlin, 1987).
>     
> 8.  G. Etherington, A. C. Wright, J. T. Wenzel, J. C. Dore, J. H. Clarke, and R. N. Sinclair, J. Non-Cryst. Solids 48, 265 (1982).
>     
> 9.  J. Fortner and J. S. Lannin, Phys. Rev. B 39, 5527 (1989).
>     
> 10.  A. Gheorghiu, K. Driss-Khodja, S. Fisson, M. L. Theye, and J. Dixmier, J. Phys. (Paris) Colloq. 46, C8-545 (1985).
>     
> 11.  J. P. Gabathuler and S. Steeb, Z. Naturforsch. Teil A 34, 1314 (1979).
>     
> 12.  Y. Waseda, _The Structure of Non Crystalline Materials—Liquids and Amorphous Solids_ (McGraw-Hill, New York, 1981).
>     
> 13.  C. Bergman, C. Bichara, P. Chieux, and J. P. Gaspard, J. Phys. (Paris) Colloq. 46, C8-97 (1985).
>     
> 14.  A. Arnold, N. Mauser, and J. Hafner, J. Phys. Condens. Matter 1, 965 (1989).
>     
> 15.  W. Jank and J. Hafner, Phys. Rev. B 41, 1497 (1990).
>     
> 16.  W. Jank and J. Hafner, J. Phys. Condens. Matter 1, 4235 (1989).
>     
> 17.  G. Kresch and J. Hafner, Verh. Dtsch. Phys. Ges. 5, 1357 (1993).
>     
> 18.  F. H. Stillinger and T. A. Weber, Phys. Rev. B 31, 5262 (1985).
>     
> 19.  R. Biswas and D. R. Hamann, Phys. Rev. B 36, 6434 (1987).
>     
> 20.  J. Tersoff, Phys. Rev. B 37, 6991 (1988).
>     
> 21.  J. Q. Broughton and X. P. Li, Phys. Rev. B 35, 9120 (1987).
>     
> 22.  W. D. Luedtke and U. Landman, Phys. Rev. B 37, 4656 (1988); 40, 1164 (1989).
>     
> 23.  R. Biswas, G. S. Grest, and C. M. Soukoulis, Phys. Rev. B 36, 7437 (1987).
>     
> 24.  K. Ding and H. C. Andersen, Phys. Rev. B 34, 6987 (1986).
>     
> 25.  R. Car and M. Parrinello, Phys. Rev. Lett. 55, 2471 (1985).
>     
> 26.  W. Kohn and L. Sham, Phys Rev. 140, A1133 (1965); W. Kohn, in _Highlights of Condensed Matter Theory_, edited by M. P. Tosi, M. Fumi, and F. Bassani (North-Holland, Amsterdam, 1985).
>     
> 27.  I. Stich, R. Car, and M. Parrinello, Phys. Rev. Lett. 63, 2240 (1989); Phys. Rev. B 44, 4262 (1991).
>     
> 28.  F. Buda, G. L. Chiarotti, I. Stich, R. Car, and M. Parrinello, J. Non-Cryst. Solids 114, 7 (1989).
>     
> 29.  I. Stich, R. Car, and M. Parrinello, Phys. Rev. B 44, 11092 (1991).
>     
> 30.  G. Pastore, E. Smargiassi, and F. Buda, Phys. Rev. A 44, 6334 (1991).
>     
> 31.  S. Nosé, J. Chem. Phys. 81, 511 (1984).
>     
> 32.  P. E. Blöchl and M. Parrinello, Phys. Rev. B 45, 9413 (1992).
>     
> 33.  N. D. Mermin, Phys. Rev. 137, A 1441 (1965).
>     
> 34.  G. Kresse and J. Hafner, Phys. Rev. B 47, 558 (1993).
>     
> 35.  G. Kresse and J. Hafner, J. Non-Cryst. Solids 117 & 118, 956 (1993).
>     
> 36.  We use the parametrization presented by J. P. Perdew and A. Zunger, Phys. Rev B 23, 5048 (1981).
>     
> 37.  M. Weinert and J. W. Davenport, Phys. Rev. B. 45, 13709 (1992).
>     
> 38.  R. M. Wentzcovitch, J. L. Martins, and P. B. Allen, Phys. Rev B 45, 11372 (1992).
>     
> 39.  M. P. Teter, M. C. Payne, and D. C. Allan, Phys. Rev. B 40, 12255 (1989).
>     
> 40.  R. D. King-Smith, M. C. Payne, and J. S. Lin, Phys. Rev B 44, 13063 (1991).
>     
> 41.  T. A. Arias, M. C. Payne, and J. D. Joannopoulos, Phys. Rev. B 45, 1538 (1992).
>     
> 42.  M. C. Payne, M. P. Teter, D. C. Allan, T. A. Arias, and J. D. Joannopoulos, Rev. Mod. Phys. 64, 1045 (1992).
>     
> 43.  D. M. Bylander, L. Kleinman, and S. Lee, Phys. Rev. B 42, 1394 (1990); D. M. Bylander and L. Kleinman, _ibid._ 45, 9663 (1992).
>     
> 44.  D. Vanderbilt, Phys. Rev. B 32, 8412 (1985).
>     
> 45.  G. Kresse, J. Hafner, and R. J. Needs, J. Phys. Condens. Matter 4, 7451 (1992).
>     
> 46.  A. De Vita, Ph. D. thesis, Keele University, 1992; A. De Vita and M. J. Gillan (unpublished).
>     
> 47.  I. Stich, R. Car, M. Parrinello, and S. Baroni, Phys. Rev. B 39, 4997 (1989).
>     
> 48.  M. J. Gillan, J. Phys. Condens. Matter 1, 689 (1989).
>     
> 49.  G. P. Kerker, Phys. Rev. B 23, 3082 (1981).
>     
> 50.  D. M. Bylander and L. Kleinman, Phys. Rev. B 46, 13756 (1992).
>     
> 51.  S. Nosé, Prog. Theor. Phys. Suppl. 103, 1 (1991).
>     
> 52.  C. W. Gear, _Numerical Initial Value Problem in Ordinary Differential Equations_ (Prentice Hall, Englewood Cliffs, NJ, 1971), Chaps. 9 and 10.
>     
> 53.  G. Kresse, Ph. D. thesis, Technische Universität Wien, 1993.
>     
> 54.  G. B. Bachelet, D. R. Hamann, and M. Schlüter, Phys. Rev. B 26, 4199 (1982).
>     
> 55.  N. Troullier and J. L. Martins, Phys. Rev. B 43, 1993 (1991).
>     
> 56.  A. M. Rappe, K. M. Rabe, E. Kaxiras, and J. D. Joannopoulos, Phys. Rev. B 41, 1227 (1990).
>     
> 57.  A. Garcia, C. Elsässer, J. Zhu, and S. G. Louie, Phys. Rev. B 46, 9829 (1992).
>     
> 58.  M. T. Yin and M. L. Cohen, Phys. Rev. B 26, 5668 (1982).
>     
> 59.  E. Wigner, Phys. Rev. 133, 1002 (1934).
>     
> 60.  L. Kleinman and D. M. Bylander, Phys. Rev. Lett. 48, 1425 (1982).
>     
> 61.  P. Viscor, J. Non-Cryst. Solids 101, 156 (1988).
>     
> 62.  G. A. N. Cornell and R. J. Temkin, Phys. Rev. B 9, 5323 (1974).
>     
> 63.  D. L. Evans, M. P. Teter, and N. F. Borelli, J. Non-Cryst. Solids 17, 245 (1975).
>     
> 64.  D. Beeman and B. L. Bobbs, Phys. Rev. B 12, 1399 (1975).
>     
> 65.  D. Henderson, J. Non-Cryst. Solids 16, 317 (1974).
>     
> 66.  P. Steinhardt, R. Alben, and D. Weaire, J. Non-Cryst. Solids 15, 199 (1974).
>     
> 67.  P. Pulay, in _Modern Theoretical Chemistry_, edited by H. F. Schaefer (Plenum, New York, 1977); Mol. Phys. 17, 197 (1969).
>     
> 68.  D. A. Drabold, P. A. Fedders, S. Klemm, and O. F. Sankey, Phys. Rev. Lett. 67, 2179 (1991).
>     
> 69.  W. H. Press, B. P. Flannery, S. A. Teukolsky, and W. T. Vetterling, _Numerical Recipes: The Art of Scientific Computing_ (Cambridge University Press, Cambridge 1986); we use an implementation similar to the schemes discussed by S. Blügel, Ph. D. thesis, Aachen University, 1988.
>     
> 70.  F. H. Stillinger and T. A. Weber, J. Chem. Phys. 80, 4434 (1984).
>     
> 71.  J. Hafner, J. Phys. F 18, 153 (1988).
>     
> 72.  A. Baldereschi, Phys. Rev. B 7, 5212 (1973); H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13, 5188 (1976).
>     
> 73.  J. Hafner and G. Kahl, Solid State Commun. 49, 1125 (1981); J. Phys. F 14, 2259 (1984).
>     
> 74.  W. Jank and J. Hafner, Europhys. Lett. 7, 623 (1988).
>     
> 75.  G. Indlekofer, P. Oelhafen, R. Lapka, and H. J. Güntherodt, Z. Phys. Chem. 157, 465 (1988).
>     
> 76.  A. Ferrante and M. P. Tosi, J. Phys. Condens. Matter 1, 1679 (1989).
>     
> 77.  J. P. Gaspard, Ph. Lambin, C. M. Moutet, and J. P. Vignerons, Philos. Mag. B 50, 103 (1984).
>     
> 78.  F. Spaepen and D. Turnbull, in _Laser Processing of Semiconductors_, edited by J. M. Poate and J. W. Mayer (Academic, New York 1982), p. 15.
>     
> 79.  C. Senemaud, E. Belin, A. Gheorghiu, and M. L. Theye, J. Non-Cryst. Solids 77, 1289 (1985).
>     
> 80.  L. Ley, S. Kowalczyk, R. Pollak, and D. A. Shirley, Phys. Rev. Lett. 29, 1088 (1972).
>     
> 81.  J. D. Joannopoulos and M. L. Cohen, Solid State Phys. 31, 71 (1976).
>     
> 82.  C. L. Croxton, _Liquid State Physics_ (Cambridge University Press, Cambridge, 1974), p. 243.
>     
> 83.  J. Jäckle and K. Froböse, J. Phys. F 7, 2331 (1977).
>     
> 84.  J. Hafner, J. Phys. C 14, L278 (1981).
>     
> 85.  N. Maley, J. S. Lannin, and D. L. Price, Phys. Rev. Lett. 56, 1720 (1986).
>     
> 86.  W. A. Kamitakahara, C. M. Soukoulis, H. R. Shanks, O. Buchenau, and G. S. Grest, Phys. Rev. B 38, 6539 (1987).
>     
> 87.  See, e.g., J. Hafner, J. Phys. C 16, 5773 (1983).
>     
> 88.  See, e.g., the articles of M. H. Brodsky et al., and R. A. Street and D. K. Biegelsen in _The Physics of Hydrogenated Amorphous Silicon II_, edited by J. D. Joannopoulos and G. Lucovsky (Springer, Berlin, 1984).
>     
> 89.  S. T. Pantelides, Phys. Rev. Lett. 57, 2979 (1986).
>     
> 90.  I. Kwon, R. Biswas, G. S. Grest, and C. M. Soukoulis, Phys. Rev. B 41, 3678 (1990).
>     
> 91.  I. Stich, Ph. D. thesis, SISSA Trieste, 1989.
>     
> 92.  G. Kresse and J. Hafner, Phys. Rev. B 48, 13115 (1993).
>     
> 
> 🚀 [笔记回链](zotero://select/library/items/3SQWDEV5)
> 
> * * *
> 
> `GPT 自定 ②`  `deepseek-v4-pro`  _由批量 AI 解读自动生成于 2026/8/10 23:23:48 （重新解读）_
> 
> 🏷️ #🤖️/论文双语转写 🏷️ #🤖️/AI文献阅读

^KEY5CAAD2AE