---
作者: [Vei Wang, Nan Xu, Jin-Cheng Liu, Gang Tang, Wen-Tong Geng]
中文标题: VASPKIT：用户友好的界面，使用VASP代码促进高通量计算和分析
分类: [07_异质结与隧道结 (Heterostructures/Tunnel Junctions)]
影响因子: 3
---



# VASPKIT: A user-friendly interface facilitating high-throughput computing and analysis using VASP code
> [!info]+ <center>Metadata</center>
> 
> |<div style="width: 5em">Key</div>|Value|
> |--:|:--|
> |文献类型|journalArticle|
> |标题|VASPKIT: A user-friendly interface facilitating high-throughput computing and analysis using VASP code|
> |短标题|VASPKIT：用户友好的界面，使用VASP代码促进高通量计算和分析|
> |作者|[[Vei Wang]]、 [[Nan Xu]]、 [[Jin-Cheng Liu]]、 [[Gang Tang]]、 [[Wen-Tong Geng]]|
> |期刊名称|[[Computer Physics Communications]]|
> |DOI|[10.1016/j.cpc.2021.108033](https://doi.org/10.1016/j.cpc.2021.108033)|
> |存档位置|7372|
> |文库编目|3.9|
> |索书号|3|
> |版权||
> |分类|[[07_异质结与隧道结 (Heterostructures/Tunnel Junctions)]]|
> |条目链接|[My Library](zotero://select/library/items/D8MWNZKU)|
> |PDF 附件||
> |关联文献|[[zhangEmergingFrontiersTwodimensional2025]]、 [[chenStrongSlidingFerroelectricity2024]]、 [[zhangNonvolatileControlTopological2025]]、 [[kresseEfficientIterativeSchemes1996d]]、 [[gaoGiantChiralMagnetoelectric2024a]]、 [[tangMultiferroicityTwodimensionalVan2025]]、 [[laiTwodimensionalFerromagnetismDriven2019b]]、 [[guoAdvancesTwodimensionalFerroelectric2025]]、 [[feiFerroelectricSwitchingTwodimensional2018a]]、 [[wuSlidingFerroelectricity2D2021a]]、 [[cuiIntercorrelatedInplaneOutofplane2018a]]、 [[zhaoOpticalFingerprintsTwodimensional2024]]、 [[tahirFerroelectricityNonvolatileMemristor2025]]、 [[cheongMultiferroicsMagneticTwist2007a]]、 [[songEvidenceSinglelayerVan2022]]、 [[sharmaRoomtemperatureFerroelectricSemimetal2019]]、 [[laiTwodimensionalFerromagnetismDriven2019]]、 [[blochlProjectorAugmentedwaveMethod1994b]]、 [[dingPredictionIntrinsicTwodimensional2017a]]、 [[naguib25thAnniversaryArticle2013a]]、 [[RecentAdvancesGrowth2025]]、 [[aminiAtomicscaleVisualizationMultiferroicity2024]]、 [[wuNonvolatileSwitchableHalfmetallicity2024]]、 [[kresseUltrasoftPseudopotentialsProjector1999c]]、 [[yuFerroelectricControlMagnetism2026]]、 [[henkelmanClimbingImageNudged2000c]]、 [[hanTunableSlidingFerroelectricity2025]]、 [[perdewGeneralizedGradientApproximation1996a]]、 [[sunSlidingFerroelectricityTwodimensional2025b]]、 [[tangCombiningIntrinsicSlidinginduced2025]]、 [[wangTunableD0Topological2025b]]、 [[wangTwodimensionalFerroelectricMetal2025]]、 [[gaoStrainEngineeringFerroelectric2024]]、 [[caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]、 [[wuCoexistenceFerroelectricityAntiferroelectricity2024]]、 [[kaurRecentAdvancesTheoretical2025a]]、 [[miaoMagneticFerroelectricMetal2024]]、 [[heSwitchingTwodimensionalSliding2025]]、 [[zhaoRealization2DMultiferroic2024]]、 [[hillWhyAreThere2000a]]、 [[bhowalPolarMetalsPrinciples2023b]]、 [[sattarFunctionalizedDoubleTransition2025]]、 [[songEvidenceSinglelayerVan2022b]]、 [[zahraCriticalAnalysisFerroelectric2025]]、 [[dudarevElectronenergylossSpectraStructural1998a]]、 [[neumayerCompetingPolarPhases2025]]、 [[tianRoomtemperatureTwodimensionalMultiferroic2026]]、 [[xunCoexistingMagnetismFerroelectric2024]]、 [[king-smithTheoryPolarizationCrystalline1993]]、 [[king-smithTheoryPolarizationCrystalline1993c]]|
> ^Metadata

> [!example]- <center>本文标签</center>
> 
> `$=dv.current().file.tags`

> [!quote]- <center>Abstract</center>
> 
> We present the VASPKIT, a command-line program that aims at providing a powerful and user-friendly interface to perform high-throughput analysis of a variety of material properties from the raw data produced by the VASP code. It consists of mainly the pre- and post-processing modules. The former module is designed to prepare and manipulate input files such as the necessary input files generation, symmetry analysis, supercell transformation, k-path generation for a given crystal structure. The latter module is designed to extract and analyze the raw data about elastic mechanics, electronic structure, charge density, electrostatic potential, linear optical coefficients, wave function plots in real space, and etc. This program can run conveniently in either interactive user interface or command line mode. The command-line options allow the user to perform high-throughput calculations together with bash scripts. This article gives an overview of the program structure and presents illustrative examples for some of its usages. The program can run on Linux, MacOS, and Windows platforms. The executable versions of VASPKIT and the related examples, together with the tutorials, are available in its official website vaspkit.com.
>
>【摘要翻译】我们介绍了VASPKIT，这是一个命令行程序，旨在提供一个强大且用户友好的界面，从VASP代码生成的原始数据中对各种材料特性进行高通量分析。它主要由前处理和后处理模块组成。前一个模块旨在准备和操作输入文件，例如必要的输入文件生成、对称分析、超级单元变换、给定晶体结构的k路径生成。后一个模块旨在提取和分析弹性力学、电子结构、电荷密度、静电势、线性光学系数、真实空间中的波函数图等原始数据。
>该程序可以在交互式用户交互界面或命令行模式下方便地运行。命令行选项允许用户与bash脚本一起执行高吞吐量计算。本文概述了程序结构，并为其一些用途提供了说明性示例。该程序可以在Linux、MacOS和Windows平台上运行。VASPKIT的可执行版本和相关示例以及教程可在其官网链接vaspkit.com中获得。

> [!tldr]- <center>隐藏信息</center>
> 
> itemType:: journalArticle
> title:: VASPKIT: A user-friendly interface facilitating high-throughput computing and analysis using VASP code
> shortTitle:: VASPKIT：用户友好的界面，使用VASP代码促进高通量计算和分析
> creators:: [[Vei Wang]]、 [[Nan Xu]]、 [[Jin-Cheng Liu]]、 [[Gang Tang]]、 [[Wen-Tong Geng]]
> publicationTitle:: [[Computer Physics Communications]]
> journalAbbreviation:: Computer Physics Communications
> volume:: 267
> issue:: 
> pages:: 108033
> series:: 
> language:: en
> DOI:: [10.1016/j.cpc.2021.108033](https://doi.org/10.1016/j.cpc.2021.108033)
> ISSN:: 00104655
> url:: [https://linkinghub.elsevier.com/retrieve/pii/S0010465521001454](https://linkinghub.elsevier.com/retrieve/pii/S0010465521001454)
> archive:: 
> archiveLocation:: 7372
> libraryCatalog:: 3.9
> callNumber:: 3
> JCRQ:: Q2
> rights:: 
> extra:: 🏷️ /unread、🤖️、📒
> collection:: [[07_异质结与隧道结 (Heterostructures/Tunnel Junctions)]]
> tags:: #unread 
> related:: [[zhangEmergingFrontiersTwodimensional2025]]、 [[chenStrongSlidingFerroelectricity2024]]、 [[zhangNonvolatileControlTopological2025]]、 [[kresseEfficientIterativeSchemes1996d]]、 [[gaoGiantChiralMagnetoelectric2024a]]、 [[tangMultiferroicityTwodimensionalVan2025]]、 [[laiTwodimensionalFerromagnetismDriven2019b]]、 [[guoAdvancesTwodimensionalFerroelectric2025]]、 [[feiFerroelectricSwitchingTwodimensional2018a]]、 [[wuSlidingFerroelectricity2D2021a]]、 [[cuiIntercorrelatedInplaneOutofplane2018a]]、 [[zhaoOpticalFingerprintsTwodimensional2024]]、 [[tahirFerroelectricityNonvolatileMemristor2025]]、 [[cheongMultiferroicsMagneticTwist2007a]]、 [[songEvidenceSinglelayerVan2022]]、 [[sharmaRoomtemperatureFerroelectricSemimetal2019]]、 [[laiTwodimensionalFerromagnetismDriven2019]]、 [[blochlProjectorAugmentedwaveMethod1994b]]、 [[dingPredictionIntrinsicTwodimensional2017a]]、 [[naguib25thAnniversaryArticle2013a]]、 [[RecentAdvancesGrowth2025]]、 [[aminiAtomicscaleVisualizationMultiferroicity2024]]、 [[wuNonvolatileSwitchableHalfmetallicity2024]]、 [[kresseUltrasoftPseudopotentialsProjector1999c]]、 [[yuFerroelectricControlMagnetism2026]]、 [[henkelmanClimbingImageNudged2000c]]、 [[hanTunableSlidingFerroelectricity2025]]、 [[perdewGeneralizedGradientApproximation1996a]]、 [[sunSlidingFerroelectricityTwodimensional2025b]]、 [[tangCombiningIntrinsicSlidinginduced2025]]、 [[wangTunableD0Topological2025b]]、 [[wangTwodimensionalFerroelectricMetal2025]]、 [[gaoStrainEngineeringFerroelectric2024]]、 [[caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]、 [[wuCoexistenceFerroelectricityAntiferroelectricity2024]]、 [[kaurRecentAdvancesTheoretical2025a]]、 [[miaoMagneticFerroelectricMetal2024]]、 [[heSwitchingTwodimensionalSliding2025]]、 [[zhaoRealization2DMultiferroic2024]]、 [[hillWhyAreThere2000a]]、 [[bhowalPolarMetalsPrinciples2023b]]、 [[sattarFunctionalizedDoubleTransition2025]]、 [[songEvidenceSinglelayerVan2022b]]、 [[zahraCriticalAnalysisFerroelectric2025]]、 [[dudarevElectronenergylossSpectraStructural1998a]]、 [[neumayerCompetingPolarPhases2025]]、 [[tianRoomtemperatureTwodimensionalMultiferroic2026]]、 [[xunCoexistingMagnetismFerroelectric2024]]、 [[king-smithTheoryPolarizationCrystalline1993]]、 [[king-smithTheoryPolarizationCrystalline1993c]]
> itemLink:: [My Library](zotero://select/library/items/D8MWNZKU)
> pdfLink:: 
> qnkey:: wangVASPKITUserfriendlyInterface2021a
> date:: 2021-10
> dateY:: 2021
> dateAdded:: 2026-08-04
> datetimeAdded:: 2026-08-04 11:43:56
> dateModified:: 2026-08-10
> datetimeModified:: 2026-08-10 19:49:18
> 
> abstract:: We present the VASPKIT, a command-line program that aims at providing a powerful and user-friendly interface to perform high-throughput analysis of a variety of material properties from the raw data produced by the VASP code. It consists of mainly the pre- and post-processing modules. The former module is designed to prepare and manipulate input files such as the necessary input files generation, symmetry analysis, supercell transformation, k-path generation for a given crystal structure. The latter module is designed to extract and analyze the raw data about elastic mechanics, electronic structure, charge density, electrostatic potential, linear optical coefficients, wave function plots in real space, and etc. This program can run conveniently in either interactive user interface or command line mode. The command-line options allow the user to perform high-throughput calculations together with bash scripts. This article gives an overview of the program structure and presents illustrative examples for some of its usages. The program can run on Linux, MacOS, and Windows platforms. The executable versions of VASPKIT and the related examples, together with the tutorials, are available in its official website vaspkit.com.【摘要翻译】我们介绍了VASPKIT，这是一个命令行程序，旨在提供一个强大且用户友好的界面，从VASP代码生成的原始数据中对各种材料特性进行高通量分析。它主要由前处理和后处理模块组成。前一个模块旨在准备和操作输入文件，例如必要的输入文件生成、对称分析、超级单元变换、给定晶体结构的k路径生成。后一个模块旨在提取和分析弹性力学、电子结构、电荷密度、静电势、线性光学系数、真实空间中的波函数图等原始数据。 该程序可以在交互式用户交互界面或命令行模式下方便地运行。命令行选项允许用户与bash脚本一起执行高吞吐量计算。本文概述了程序结构，并为其一些用途提供了说明性示例。该程序可以在Linux、MacOS和Windows平台上运行。VASPKIT的可执行版本和相关示例以及教程可在其官网链接vaspkit.com中获得。


%--------------ω--------------%

## ✏️ 笔记区

> [!WARNING]+ <center>🐣 总结</center>
>
>🎯 一句话总结:: 

> [!inbox]- <center>📫 导入时间</center>
>
>⏰ importDate:: 2026-08-10
>⏰ importDateTime:: 2026-08-10 18:24:40

%--------------ω--------------%



## <span style="color: rgb(0, 174, 137);">🤖️ AI 文献解读</span>

> 🚀 [笔记回链](zotero://select/library/items/GP3J6K3R)

^KEYaiPapers

> <span class="AIReading">🤖 AI 解读，快人一步</span>
> 
> > 好的，用户给了一篇英文论文，要求按照设定的角色——学术文献深度解读专家来对其进行分析和解读。这篇论文是VASPKIT软件的介绍，一篇计算机物理通信领域的软件论文。
> > 
> > 需要理解任务要求：输出九个模块的深度解读，外加一个特殊的Dataview专区。用户明确规定了输出格式，包括每个模块的标题、内容要点和字数范围，还要求术语标注、可视化提示等。我按照这个结构来组织内容。
> > 
> > 需要先通读论文，理解VASPKIT是什么：一个与VASP配套的高通量材料性质分析的命令行软件，包含预处理和后处理两大模块，能计算弹性、电子、光学、催化等相关性质。核心优势是用户友好、支持高通量批处理、支持交互式界面和命令行模式。
> > 
> > 模块一引言要交代研究背景，也就是高通量计算的兴起和VASP的原始数据后处理需求；模块二给出论文结构和逻辑概览，说明论文的章节结构；模块三对图表进行解析，论文有19张图和6张表格，逐一说明内容和单位量纲；模块四对正文内容逐节剖析，包括预处理模块和后处理模块的各个功能。模块五结论，概括主要贡献。模块六展望未来方向。模块七批判性分析提出若干思考问题。模块八生成一些延伸问题并进行解答。模块九Dataview专区，按照变量要求，逐项整理核心信息。
> > 
> > 关键内容要准确：弹性常数的计算原理（能量-应变法）、k路径自动生成、能带展开、光学特性计算等，都是论文核心内容，需要准确理解。图中涉及的具体物理量、单位也要注意：弹性常数单位GPa（体材料）和N/m（二维材料），费米能级设为0等等。
> > 
> > 关于多个中英对照的专业术语也要整理：密度泛函理论（DFT）、弹性常数（SOEC）、状态方程（EOS）、有效质量（EMC）等。此外论文还提供了一些基准数据，可用于验证计算结果的可靠性。
> > 
> > 图表数量众多，功能各异，需要逐一处理才有深度和完整性。文章的整体文献定位也很明确——不是原作者自创理论，而是一个功能整合的软件工具。
> > 
> > 解答内容要涵盖：维度判断（2D还是3D）、基准数据的作用、高吞吐计算的实际流程、与其他电子结构软件的可比性等。对于研究者会提出的问题，比如“VASPKIT能做什么”、“优点是什么”，需要在开头或结尾回答。
> 
> # VASPKIT：基于VASP代码的高通量计算与分析的友好用户界面——文献深度解读报告
> 
> ## 一、引言
> 
> ### 1.1 领域背景
> 
> 近二十年来，**第一性原理计算**（First-principles calculations）基于**密度泛函理论**（Density Functional Theory, DFT）取得了长足发展。DFT方法能够在量子力学层面处理模型体系与真实材料，不仅用于理解固体的结构、力学、电子、磁性和光学性质，还可预测尚未被实验确定的化合物特征。目前已有数十种基于DFT的电子结构计算软件包，如 **Abinit**、**CASTEP**、**VASP**（Vienna Ab initio Simulation Package）、**Siesta**、**Quantum Espresso**、**Elk** 和 **WIEN2k** 等。
> 
> 然而，这些软件包有一个共同特征——**原始输出数据需要后处理**才能转换为人类可读格式或进行可视化分析。现有的解决方案存在明显割裂：商业软件（如 Materials Studio、QuantumATK）提供图形化界面但难以批量操作；开源工具（如 pymatgen、ASE、PyProcar）功能强大但要求用户精通 Python 等编程语言。这一“两难困境”构成了本工具开发的核心痛点。
> 
> ### 1.2 文献定位与核心价值
> 
> 本文发表于 _Computer Physics Communications_（2021年），系统介绍了 **VASPKIT**（VASP + Toolkit）——一个专为 VASP 用户设计的命令行工具包。VASPKIT 的定位是提供**功能强大且用户友好的集成输入/输出环境**，涵盖从计算前初始设置到计算后性质分析的全流程。其核心价值在于：**兼具交互式菜单驱动的易用性与命令行模式的高通量（High-throughput）批处理能力**，显著降低了 DFT 计算的门槛。
> 
> ## 二、论文结构与逻辑概览
> 
> ### 2.1 论文总体框架
> 
> 论文采用经典的**“总—分—总”**结构，共分为6个正文章节：
> 
> <table><thead><tr><th>章节</th><th>标题</th><th>核心内容</th></tr></thead><tbody><tr><td>1</td><td>Introduction（引言）</td><td>领域背景、现有工具局限、VASPKIT定位</td></tr><tr><td>2</td><td>Capabilities of the Pre-Processing Module</td><td>预处理模块功能解析</td></tr><tr><td>3</td><td>Capabilities of the Post-Processing Module</td><td>后处理模块功能解析（核心章节，含14个子功能）</td></tr><tr><td>4</td><td>High-throughput Capabilities</td><td>高通量能力展示</td></tr><tr><td>5</td><td>Limitations and Future Capabilities</td><td>局限与展望</td></tr><tr><td>6</td><td>Summary（总结）</td><td>全文概括</td></tr></tbody></table>
> 
> _（可设计为论文结构流程图）_
> 
> ### 2.2 核心论证链条
> 
> ```
> 研究问题：VASP原始数据需要高效、易用的后处理工具
>       ↓
> 现有方案与不足：GUI商业软件缺乏批处理能力；Python工具需编程基础
>       ↓
> VASPKIT解决方案：菜单驱动+命令行双模式；预处理+后处理一体化
>       ↓
> 功能验证：通过多维材料体系（2D/3D）的基准测试（Benchmark）验证各功能模块
>       ↓
> 结论：VASPKIT 是高效、易用且拓展性强的 VASP 集成工具平台
> 
> ```
> 
> ## 三、所有图表深度解析
> 
> > **说明**：论文中共包含 **12 幅插图（Figures 1-19 部分含子图）** 和 **10 张表格（Tables 1-5 + 附录 A/B 若干）** ，以下逐一解析。注：所有能量单位均为电子伏特（eV），长度单位为埃（Å），力常数为牛/米（N/m）。
> 
> ### 图1：VASPKIT 整体结构概览
> 
> -   **内容**：展示 VASPKIT 的**预处理（Pre-processing）** 与**后处理（Post-processing）** 两大模块的工作流程。
> -   **要点**：预处理始于读取 POSCAR 结构文件，进行构建超胞、对称性分析、生成输入文件及 k 路径；后处理则从 VASP 原始数据中提取力学、电子、光学与磁性等性质。
> -   _可视化建议：绘制模块—功能对照的流程图_
> 
> ### 图2：超胞重构
> 
> -   **展示内容**：从**原胞（PC，红色菱形）** 出发，通过转换矩阵 **M** 构造 **超胞（SC，黄色菱形）** 的示意图。
> -   **技术公式基础**：晶格矢量关系满足 a′=a·M。图中给出了实例变换：a′=-a-2b，b′=-2a-b。
> -   **核心意义**：直观呈现了超胞构建的几何本质。
> 
> ### 图3：k路径自动生成算法与示例
> 
> -   **图 3(a)**：工作流程图。依次为→ 用 **Spglib** 确定空间群编号、晶族、Bravais 格子类型 → 标准化常规胞 → 由式(4)转换到标准原胞 → 基于晶体族生成建议 k 路径 → 保存 PRIMCELL.vasp 与 KPATH.in。
> -   **图 3(b)-(e)**：分别为**2D 矩形（Rectangular）** 、**2D 斜交（Oblique）** 、**面心立方（FCC）** 和 **六方密堆积（HCP）** 格子在第一布里渊区中的高对称点与推荐 k 路径。
> 
> ### 图4：后处理模块功能总览
> 
> -   **展示内容**：以思维导图形式汇总后处理模块的14项功能，包括：弹性力常数、状态方程、电子结构（Fermi面、有效质量、能带、DOS）、电荷密度与静电势、光学性质、波函数、催化（d带中心）、分子动力学（MSD、VACF、VDOS、PCF）等。
> 
> ### 图5：弹性常数计算算法流程图
> 
> -   **展示内容**：基于 **能量-应变（Energy-Strain）** 方法计算二阶弹性常数（SOECs）的完整流程。
> -   **流程总结**：读取完全弛豫的 POSCAR → 用 Spglib 确定空间群与标准连续胞 → 指定材料维度（2D/3D）与应变数量 → 生成形变结构 → VASP 并行计算 → 2阶多项式拟合能量-应变曲线 → 得到 Cij → 进一步确定体弹模量K、剪切模量G、泊松比ν及稳定性判据。
> 
> ### 图6：金刚石状态方程
> 
> -   **展示内容**：分别用 8 种 EOS 模型（Birch-Murnaghan、Tait、Vinet 等）拟合金刚石能量-体积曲线与压力-体积关系。
> -   **关键结果**：各模型吻合良好，计算所得体积模量 **440 GPa ≤ K ≤ 442 GPa**，与实验值 443 GPa 高度一致，验证了 EOS 工具的正确性。
> 
> ### 图7：投影能带与态密度
> 
> -   **展示体系**：(a) BiClO 单层（P 4/nmm）；(b) 石墨烯单层。
> -   **左图**：投影能带结构（颜色/大小反映轨道成分）；**右图**：对应的态密度（DOS）。费米能级均设为 0 eV。
> -   **意义**：展示了 VASPKIT 区分不同轨道贡献的能力。
> 
> ### 图8：3D 全局能带结构
> 
> -   **展示体系**：(a) MoTe₂ 单层 (P 6m2) 与 (b) BiIO 单层 (P 4/nmm)。
> -   **展示内容与意义**：价带顶与导带底在整个布里渊区的 3D 色散，揭示 2D 材料有效能带结构的各向异性特征。
> 
> ### 图9：载流子有效质量
> 
> -   **图 9(a)**：有效质量拟合原理示意图——在波矢空间中，能带**曲率越大则有效质量越小**，图注清晰反映了 CBM 和 VBM 附近的抛物线。
> -   **图 9(b)-(e)**：BN 单层与体相 Si 的**取向依赖的有效质量**极坐标图。结果显示材料具有明显的有效质量各向异性，特别是体相 Si。
> 
> ### 图10：电荷密度差与宏观平均势
> 
> -   **展示体系**：(100) 取向 GaAs/AlAs 异质结和 (110) 取向 GaAs 平坝。
> -   **图中关键曲线**：电荷密度差（以 ×10⁻³ 标度）、其平面平均（蓝线）、宏观平均（红线）、以及静电势的平面/宏观平均。
> -   **物理意义**：平滑的宏观平均曲线能够清晰提取界面势能带补偿（Band Offset），是半导体界面研究的核心参数。
> 
> ### 图11：Cu 的 Fermi 面
> 
> -   **展示内容**：(a) 普通 Fermi 面；(b)-(d) 分别由 Cu-s、Cu-p、Cu-d 态投影的轨道分辨 Fermi 面（用 FermiSurfer 可视化）。
> -   **颜色编码**：颜色代表轨道贡献权重。
> 
> ### 图12：波函数可视化
> 
> -   **展示内容**：(a) CO 分子的波函数；石墨烯的 (b) 价带顶 (VBM) 与 (c) 导带底 (CBM) 波函数。
> -   **坐标/量纲**：波函数大小为实空间等值面（通过 VESTA 程序可视化）。
> 
> ### 图13：波段展开流程图
> 
> -   **图 13(a)**：算法工作流程与核心公式——从 VASP 计算完成后读取平面波系数与特征值，根据 K=M·k 折回 SC 倒空间，最终通过计算谱权重实现带入原胞。
> -   **图 13(b)**：3×3 石墨烯超胞的能带对比。蓝线为原有超胞能带，红色标记为展开后的**有效能带（EBS）** ——展开后还原清晰的原胞能带特征。
> 
> ### 图14：MoS₂ 缺陷体系的折叠能带
> 
> -   **体系**：4×3 MoS₂ 单层超胞，含 1 个中性 S 空位。
> -   **关键发现**：(a) vs (b) 比较可知，缺陷引入**两个近简并态缺陷态**在半导体能级的禁带中央；(c)/(d) 展开轨道分解表明，这些缺陷态主要来源于 S-p 态（顶部）和 Mo-d 态（较低）的杂化。
> 
> ### 图15：硅的 G₀W₀-之BSE 光光谱
> 
> -   **展示内容**：(a) 吸收系数；(b) 折射率；(c) 反射率；(d) 即消光系数。
> -   **关键发现**：由于硅的间能隙为**间接带隙**，吸收系数在可见区（BOX）内不剧烈上升，从 ~3.0 eV 才开始明显。采用 GW-BSE 方法在理论层面提升了对光吸收的预测精度。
> 
> ### 图16：二维材料光学导电率
> 
> -   **展示体系**：石墨烯和磷烯（Phosphorene）单层，图中描述的是 σ2D(ω) 的实部（蓝）/虚部（红），以及 A(ω) 的吸收谱。
> -   **单位**：光学导电率单位为 σ₀=e²/(4ħ)。
> -   **重要结果**：二维反射自下，紫外区域吸收峰；磷光体线性边缘各向异性（armchair vs zigzag 方向）。
> 
> ### 图17：联合态密度
> 
> -   **展示体系**：CH₃NH₃PbI₃（钙钛矿）和 Si。
> -   **关键曲线**：蓝（总JDOS）、紫（部分JDOS）。CH₃NH₃PbI₃ 结果与文献数据完美重合。
> 
> ### 图18：跃迁偶极矩（TDM）
> 
> -   **展示体系**：Cs₂AgInCl₆ 与 Cs₂InBiCl₆ 双钙钛矿。
> -   **关键发现**：Cs₂AgInCl₆ 在 Γ 点处 CBM-VBM 的 TDM 为零（**光学禁止跃迁**），而 Bi 替代后（Cs₂InBiCl₆）TDM 非零，预言了**光学允许跃迁**——符合已知文献结论。
> 
> ### 图19：液态水 MD 分析
> 
> -   **展示内容**：400 K 下液态水的 (a) MSD、(b) VACF、(c) VDOS、(d) PCF。
> -   **结论**：VASPKIT 的动力学分析结果与实验结果符合（对应 Soper 等 Ref. [99] 数据）。
> 
> ### 表格汇总（10张表）
> 
> <table><thead><tr><th>表号</th><th>内容</th><th>核心维度 / 单位</th></tr></thead><tbody><tr><td>表1</td><td>各大晶系（三斜~立方）对应 SOEC 数量</td><td>21、13、9、6、7、6、5、3</td></tr><tr><td>表2</td><td>2D 晶系的独立弹常数</td><td>斜交 6 / 矩形 4 / 方程 3 / 六角 2</td></tr><tr><td>表3</td><td>PBE 级弹性常数：8 种典型体相材料</td><td>单位 GPa，与文献值对比</td></tr><tr><td>表4</td><td>二维材料的面内弹性常数</td><td>单位 N/m，与文献值对比</td></tr><tr><td>表5</td><td>8 种 EOS 模型的解析公式</td><td>列出 E(V) 与 Bulk modulus</td></tr><tr><td>表6</td><td>载流子有效质量计算结果</td><td>单位 m₀（电子静止质量）</td></tr><tr><td>附录A 五表</td><td>各晶系应变模式与弹性常数的关系式</td><td>对应力矩阵6 各异构）</td></tr><tr><td>附录B 四表</td><td>各 2D 晶系应变模式</td><td>二维刚度矩阵</td></tr></tbody></table>
> 
> ## 四、正文核心内容剖析
> 
> ### 4.1 预处理模块
> 
> #### 4.1.1 结构定义与转换
> 
> VAS常用**分数坐标（fractional coordinates）** 与**笛卡尔坐标（Cartesian coordinates）** 共同确定晶体中原子位置。二者通过晶格基矢的**矩阵转置**关联。当需要从一个基矢组变换到另一个基矢组时，转换矩阵行列式 **|M|** 直接给出了超胞与原胞的体积比。
> 
> #### 4.1.2 对称性分析与标准原胞
> 
> Spglib 被编程用于获取晶体的空间群信息。VAS从 POSCAR 输入的结构中确定晶族的 Bravais 格子类型，再按轴向比理想化构造**标准的连续胞（standard conventional cell）** 。在此基础上，原始（primitive）基变换见 Eq.(4)——最终实现的**原胞原子最少化与重复原子去除**为后续的k点路径生成提供了统一起点。
> 
> #### 4.1.3 k 路径自动生成
> 
> 根据 2D 与 3D 晶系分类（见表1），自动输出高对称线路径至 KPATH.in 文件，并提供脚本可视化 BZ 内路径走向。
> 
> ### 4.2 后处理模块（重点部分）
> 
> #### 4.2.1 弹性力学分析
> 
> **核心公式（Hooke 定律，Voigt 记号）** ：
> 
> $$\sigma_i = \sum_{j=1}^{6} C_{ij}\varepsilon_j \quad \text{(应力-应变线性关系)}$$
> 
> 弹性常数矩阵 $C_{ij}$ 的独立数量取决于空间对称性（表1给出完整分类）。其中：
> 
> -   立方晶系只有3个独立常数：$C_{11}$, $C_{12}$, $C_{44}$。
> -   三斜晶系需21 独立常数。
> 
> **VASPKIT 使用能量-应变法：** :
> 
> -   施加应变时计算产生变形的 **ΔE**，利用数值拟合二级多项式求二阶导数；
> -   得到的 $C_{ij}$ 进而通过 **Voigt-Reuss-Hill 平均** 得到多晶材料的体积模量 K、剪切模量 G、杨氏模量 E 与泊松比 ν。
> 
> **稳定性判据**：支持对弹性稳定性条件的自动判断（适用于各晶系）。
> 
> #### 4.2.2 状态方程（EOS）
> 
> 内置 **8 种常用状态方程模型**（Murnaghan、Birch-Murnaghan、Vinet等）供用户选择拟合能量-体积曲线。基准测试显示，金刚石的拟合体积模量集中在 440-442 GPa 之间，贴合实验值为443 GPa。
> 
> #### 4.2.3 能带结构与态密度
> 
> -   经典能带图：沿高对称直线的本征值分布；
> -   **投影能带带图（Projected Band）**：通过轨道分解看清 VBM 或 CBM 的原子轨道来源；
> -   **3D 能带图**：可加能带色散的各向异性（如 MoTe₂ 与 BiIO）。
> 
> #### 4.2.4 有效质量计算
> 
> 核心公式： $$m^* = \hbar^2\left[\frac{\partial^2 E(k)}{\partial k^2}\right]^{-1}$$
> 
> 采用三阶多项式拟合（含三阶项）提高稳定性，可计算方向依赖的有效质量，并给出典型材料（磷、MoS₂、GaAs、金刚石）对比数据高度一致。
> 
> #### 4.2.5 电荷密度与静电势
> 
> -   计算与存储格式（VESTA 、XCrysDen、Gaussian cube）区分；
> -   **平面平均** 与 **宏观平均** 分开处理，可提取功函数、带阶等界面信息。对 GaAs/AlAs 异质结的计算给出了实例（图10）。
> 
> #### 4.2.6 费米面与波函数可视化
> 
> -   采用 iIBZ（不可约布里渊区）方法（在 VAS 计算中只计算非等价 k 点，再通过对称操作展开到全 BZ），大幅节约计算成本；
> -   波函数可视化：从 WAVECAR 读取平面波系数，通过傅里叶变换实空间层出可交互真实空间等值面。
> 
> #### 4.2.7 能带展开
> 
> **核心价值**：在实际材料模型中，缺陷往往采用超胞近似，但超胞能带“**fold**”混入许多多余能带。本文提出展开公式（式32）计算谱权重 $P_{Km}$，将 SC 能带投影回 PC 能带形式，从而还原有效的 Bloch 特征。缺陷态的直接证据如在 S 带上达成的两个态（Mo-d 态与 S-带态）。
> 
> #### 4.2.8 光学性质计算
> 
> -   计算**复介电函数**（实部+虚部），进行 Kramers-Kronig 变换；
> -   衍生给出折射率 n(ω)、吸收系数 α(ω)、反射率 R(ω)、损耗函数 L(ω)；
> -   对 2D 材料，定义**２D 光学电导率 σ₂D** = L·σ₃D，并通过归一化吸收、反射与透射计算避免真空层厚度带来的伪影问题。
> 
> #### 4.2.9 催化：d带中心
> 
> Hammer-Nørskov 模型计算 d 带中心 ($\varepsilon_d$)，用于预测过渡金属表面的吸附能与催化活性。
> 
> #### 4.2.10 分子动力学（MD）数据分析
> 
> -   **MSD（均方位移）**：判断原子在液态时（线性增长随时间）还是固态（呈现平台附近振荡）；
> -   **VACF（速度相关函数）**：计算原子记忆性，其傅里叶变换得到精准的声子**VDOS（振动态密度）** ；
> -   **PCF（原子对关联函数）**：描述径向分布随距离的变化；一对材料来说在长距离中g(r)≈1。
> 
> ### 高通量能力（第4节）
> 
> 提供 bash 循环内直接调用 `vaspkit -task 102` 这类命令的能力（避开菜单交互），配以脚本指令可实现批处理、ML大规模扫描，判断一次 Scaffolding 应用（如扫描二维材料库）。
> 
> ## 五、结论与贡献
> 
> ### 5.1 核心结论
> 
> VASPKIT 是一款**用户友好的、跨平台**（Linux/macOS/Windows）的命令行工具，解决了 VASP 从“输入准备”到“性质提取”全流程的自动化。其双模式（交互菜单式 UI 与 命令行）保证了易学性与高通量兼容性。
> 
> ### 5.2 主要贡献
> 
> 1.  **全面性**：涵盖力学、电学、光学、磁性、磁量子效应等，具备广泛材料研开放场景；
> 2.  **易用性**：“零”代码体验——只需输入结构文件，即可产生基元计算所需的 INCAR/POTCAR/KPOINTS 最简洁输入；
> 3.  **高通量能力**：与 bash 脚本无缝配合；
> 4.  **开放性**：开源（GPLv3）且可持续更新，本文投稿时仍持续发展中；
> 5.  **基准验证充分**：无论是 2D 还是 3D 材料，均与实验/反复值做对比验证，例如金刚石体积模量（偏差<0.01）、SiO（误差微小）等。
> 
> * * *
> 
> ## 六、未来发展方向展望
> 
> ### 6.1 文中提及的方向
> 
> 1.  **超越 VASP**支持其他第一性原理代码如下：Abinit、CASTEP、Quantum Espress 等；
> 2.  **数据可视化**推进：基于 Python 和 Matplotlib 的自主绘图库支持；
> 3.  **持续扩展新后处理模块**：不限于目前 14 项功能，面向机器学习与多维谱分析集成。
> 
> ### 6.2 从我的延伸思考
> 
> 1.  **与机器学习结合**：将 VASPKIT 提取的特征（如有效质量、带隙、缺陷形成能）直接与 ML 模型链接，实现基于描述符的快速，这将显著扩大高通量计算样本空间的效能；
> 2.  **自动化工作流管理**：不仅单点计算，日常嵌套结果的工作流网络，如搭建“从对称性解析到功能计算再到高维筛选”的端到端管道；
> 3.  **面向多尺度扩展**——东方框架中增加 GPU 加速与命令行与 Python API 接口的无缝抱合，增强二次开发能力；
> 4.  **对非晶态/液态不看好**：现阶段 VASPKIT 后处理以晶体为主；未来可将 MD 分析扩展到无序体系的液体性质。
> 
> * * *
> 
> ## 七、学术思考与批判性分析
> 
> ### 7.1 核心亮点回顾
> 
> -   VASPKIT**整合了传统工具箱的“预”与“后”处理全生命周期**，与市面上只做“后”固定好得多。
> -   **名验跨度大**：验证材料从 0D（CO分子）→ 2D（磷、石墨烯、MoS₂）到 3D（GaAs、金刚石），能涵盖广泛研究人群。
> -   **软件生态友好**：调用现有高质量库（如 Spglib 对称性、VASP 能量理念），不重新造轮子，避免代码臃肿。
> 
> ### 7.2 明确提出3-5个深度问题
> 
> **问题1：弹性力学部分对高π稠密堆积金属（如 Fe、Ni）计算是否设难度？**
> 
> -   分析：表中给出的 Ti 但局限于少数晶系。过渡金属具有带磁序（磁性），而此处使用的 PBE if EOS 对磁交换参数比较粗糙，是否能准确描述 BCC-FCC 相变附近的弹态？
> 
> **问题2：2D 光学导电率的定义**——公式(43)中 L（板厚度)大于对标准值的影响？
> 
> -   分析：当真空层从 15 Å 扫到 40 Å 时，σ₂D(ω) 作为 L 的乘积会不会引入体积伪影？作者虽引用周期介质理论，但对**极化方向 c 与层厚非无关的过渡性**子并未详细给出全面测试。
> 
> **问题3：仅使用 G₀W₀-BSE 对二维材料（石墨烯、MoS₂）预测吸收光谱的可见偏差如何看待？**
> 
> -   分析：石墨烯激子结合能非常强，Wannier-Mott 激子的致收敛性；采用固定 k 点密度会带宽锯齿出现振荡特征，是否给出 bwconvergence 的收敛检验？文尚未提供。
> 
> **问题4：d带中心模型的实际局限**
> 
> -   催化中常用的 d带中心——但只有吸附质将电子耦合振动到 d 带来的耦合才有效；含 d⁰（固定 d 能级）的情形附带误差极大。VASPKIT 只写了补助性公式（积分限可自定义），但对。
> 
> **问题5：计算分子热力学修正中低频 mode 的忽视**
> 
> -   把它简化成“最小 5-6 个频率忽略”并不一定是物理的面貌——对于表面有吸附物种（低振动模式），尾部贡献、对于通常rendered 自由能与低频声子关联大，需要更精细的低频闸断准则而非简单频率截断。
> 
> * * *
> 
> ## 八、用户问题预测与解答
> 
> ### 问题1：VASPKIT 与 pymatgen / ASE 的关键区别是什么？
> 
> **答**：
> 
> <table><thead><tr><th>工具</th><th>编程门槛</th><th>专一性</th><th>预/后能力</th><th>适用对象</th></tr></thead><tbody><tr><td>VASPKIT</td><td>零基础</td><td>VASP 专门</td><td>前后兼顾</td><td>新手/自动+S高</td></tr><tr><td>pymatgen</td><td>要求Python</td><td>通用 DFT</td><td>偏后+结构分析</td><td>材料程序化研究者</td></tr><tr><td>ASE</td><td>要求 Python</td><td>通用 DFT</td><td>前后均强</td><td>想要构造复杂任务的人</td></tr></tbody></table>
> 
> ### 问题2：需要有多强的 Linux 技能才能使用 VASPKIT？
> 
> **答**：非常容易：在日常预处理中无需写代码，其 302-303 的 option，输入“T” 菜单名字即可交互式完成。
> 
> ### 问题3：vaspkit 能否直接读取到 VASP 机器学习流程里？
> 
> **答**：命令行的简单输出（如 OUTCAR 数值解析）意味着可以将其放入 python 循环，通过 `os.system` 或 bash 脚本批量内转；为快速生成训练数据（如 K 值、缺陷形成能、带隙等）。
> 
> ### 问题4：如何将能带展开图用来做缺陷研究？
> 
> **答**：能带展开直接观察缺陷态与母体材料之外的之外：如果在 PBZ 中观察到较平坦的带（块状且 Bloch character 弱），说明**缺陷局部化严重的局域峰**明确融合在能隙中，并可节省带价特征来做轨道归属。
> 
> ### 问题5：VASPKIT自带的能带展开原理是否只能在“完美周期扰动”下使用？
> 
> **答**：其理论上要求 SC 与 PC 的晶格变换 M 为整数矩阵即可；对含高密度随机缺陷（如合金团簇）由于 k 失配，展开谱的守恒权重会减小，但其能谱趋于不可用，需要更强的迭代投影算法（如 ML）。
> 
> ### 问题6：用户如何使用自定义 EOS 完成超高压条件计算？
> 
> **答**：
> 
> -   使用 Vinet 或 Birch-M другой恒定，通常建议对超高压场景采用 Tait 或 Vinet（依据 Latimer 的评估报告），对极端条件下自洽效应的场注意模型截断。
> 
> ### 问题7：VASPKIT 在 Windows 上与 Linux 上的性能差别？
> 
> **答**：VASPKIT 合理的 Fortran 代码在 Windows 下编译运行稳定，但VASP 本身一般、大规模计算仍以 Linux 高性能集群为主；Windows 上多用于轻量后处理。
> 
> * * *
> 
> ## 九、专区：便于 Obsidian Dataview 插件调用
> 
> 领域基础知识:: 密度泛函理论（DFT）是研究材料电子结构的第一性原理核心方法；计算材料学中“预处理”指制备计算所需的输入文件（INCAR/POTCAR/KPOINTS/POSCAR），而“后处理”指从 VASP 原始输出（如 OUTCAR、WAVECAR、CHGCAR）中提取力学、电子、光学等物性；弹性力学中的 Hooke 定律（应力=弹性张量×应变）；固体电子能带理论、载流子有效质量、费米面与光学介电函数。
> 
> 研究背景:: 基于 DFT 的电子结构计算软件输出原始数据需后处理方可获得物理意义；现有工具中商业 GUI 不便于批处理、开源 Python 工具需一定的高级定制能力，缺少一个易用、高吞吐且覆盖全流程的工具平台。
> 
> 作者的问题意识:: DFT门类繁荣但各工具链条割裂；用户需要同时掌握结构操作、VASP输入文件构造与多种物理性质提取，展开繁琐；同时批量高通量筛选新材料（例如二维半导体）要求自动化、与脚本能够无缝衔接，这些是当前架构的“卡脖子”环节。
> 
> 主要研究对象:: 各类材料的力学性质（弹性常数、状态方程）、电子结构（能带、态密度、有效质量、Fermi 面）、光学性质（介电函数、吸收系数、TDM、JDOS）、电荷密度与静电势、催化指标（d带中心）、分子动力学（MSD/VDOS/PCF）以及缺陷/超胞体系的能带展开。
> 
> 主要研究方法:: 基于 DFT 的能带计算与能量函数；弹性数据采用应变驱动下的能量多项式拟合法；能量拟合 EOS 使用八相公式并用 Kramers-Kronig 转换将带动介电函数；高吞吐 + 通过 bash 脚本调用命令行模式；带展开的谱权重求法；MD 数据用时间关联函数（MSD/VACF）进行统计。
> 
> 研究意义:: 提供一个为 VASP 用户提供“从预可执行到性能提取”的免费开箱工具；支持多种平台并具有命令行批处理能力和可视化；通过与大量实验/文献数据对比的性能验证，保证了准确性；该软件的存在为材料学组学大量减少 DFT 分析脚本编写时间。
> 
> 研究结论:: VASPKIT 高效且稳健地实现了 VASP 事前/后处理全流程；其弹性、电子（基于 k点有效质量等）、光学（OD）、缺陷展开分析与动力学数据的提取能力均与文献值高精准；以及命令行接口与文档路径支持从单点计算到千级高通量过滤的多场景需求。
> 
> 对领域的贡献:: 提供了一个支持 PID、学习门槛低、覆盖面广且可脚本化的 VASP 一站式分析工具箱；改动并大幅向同行推荐了 2D 材料光学活性、低维弹性稳定性、跃迁偶极矩、带边缘等常用内容的可用性；使学术级材料筛选和第一性原理计算变得标准化、模块化。
> 
> 未来研究方向提及:: VASPKIT 官方规划：支持 VASP 以外的其他从头计算软件（Algorithm-code 对接）；图形化列表与绘图连接（Python/Matplotlib 嵌入）；模块的高通量能力向分布式集群并置方向；技术后端还会添加新属性和新的操作入口。
> 
> 未来研究方向思考:: 将 VASPKIT 用于机器学习训练数据引擎（自动生成带与有效指标）；扩展至非晶态与高熵合金等无对称性介质基准的处理模式；可通过参数化讨论建立与确定材料中界面电荷分配的自动优化通道；依托高通量预测框架连接 spectrum 模拟-实验比对的闭环流程。
> 
> 🚀 [笔记回链](zotero://select/library/items/GP3J6K3R)
> 
> * * *
> 
> `GPT 自定 ①`  `deepseek-v4-flash-free`  _由批量 AI 解读自动生成于 2026/8/7 22:05:18_
> 
> 🏷️ #🤖️/AI文献解读 🏷️ #🤖️/AI文献阅读

^KEY1004F75C