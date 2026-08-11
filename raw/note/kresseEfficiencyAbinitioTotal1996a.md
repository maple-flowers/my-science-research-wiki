---
作者: [G. Kresse, J. Furthmüller]
中文标题: 用平面波基组计算金属和半导体从头算总能量的效率
分类: [04_分子轨道与计算化学 (DFT/Ab-initio)]
影响因子: 3
---



# Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set
> [!info]+ <center>Metadata</center>
> 
> |<div style="width: 5em">Key</div>|Value|
> |--:|:--|
> |文献类型|journalArticle|
> |标题|Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set|
> |短标题|用平面波基组计算金属和半导体从头算总能量的效率|
> |作者|[[G. Kresse]]、 [[J. Furthmüller]]|
> |期刊名称|[[Computational Materials Science]]|
> |DOI|[10.1016/0927-0256(96)00008-0](https://doi.org/10.1016/0927-0256(96)00008-0)|
> |存档位置|71040|
> |文库编目|3.3|
> |索书号|3|
> |版权|https://www.elsevier.com/tdm/userlicense/1.0/|
> |分类|[[04_分子轨道与计算化学 (DFT/Ab-initio)]]|
> |条目链接|[My Library](zotero://select/library/items/ZEMZMCTZ)|
> |PDF 附件|[PDF](zotero://open-pdf/library/items/SR3A9C5S)|
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
> title:: Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set
> shortTitle:: 用平面波基组计算金属和半导体从头算总能量的效率
> creators:: [[G. Kresse]]、 [[J. Furthmüller]]
> publicationTitle:: [[Computational Materials Science]]
> journalAbbreviation:: Computational Materials Science
> volume:: 6
> issue:: 1
> pages:: 15-50
> series:: 
> language:: en
> DOI:: [10.1016/0927-0256(96)00008-0](https://doi.org/10.1016/0927-0256(96)00008-0)
> ISSN:: 0927-0256
> url:: [https://linkinghub.elsevier.com/retrieve/pii/0927025696000080](https://linkinghub.elsevier.com/retrieve/pii/0927025696000080)
> archive:: 
> archiveLocation:: 71040
> libraryCatalog:: 3.3
> callNumber:: 3
> JCRQ:: Q2
> rights:: https://www.elsevier.com/tdm/userlicense/1.0/
> extra:: 🏷️ /unread、📒、🤖️
> collection:: [[04_分子轨道与计算化学 (DFT/Ab-initio)]]
> tags:: #unread #🤖️
> related:: 
> itemLink:: [My Library](zotero://select/library/items/ZEMZMCTZ)
> pdfLink:: [PDF](zotero://open-pdf/library/items/SR3A9C5S)
> qnkey:: kresseEfficiencyAbinitioTotal1996a
> date:: 1996-07
> dateY:: 1996
> dateAdded:: 2026-05-06
> datetimeAdded:: 2026-05-06 05:02:35
> dateModified:: 2026-08-11
> datetimeModified:: 2026-08-11 07:02:06
> 
> abstract:: 


%--------------ω--------------%

## ✏️ 笔记区

> [!WARNING]+ <center>🐣 总结</center>
>
>🎯 一句话总结:: 

> [!inbox]- <center>📫 导入时间</center>
>
>⏰ importDate:: 2026-08-11
>⏰ importDateTime:: 2026-08-11 07:02:03

%--------------ω--------------%



## <span style="color: rgb(0, 174, 137);">❶ 🤖️ AI 文献解读</span>

> 🚀 [笔记回链](zotero://select/library/items/IAA6NZLC)

^KEYaiPapers

> <span class="AIReading">🤖 AI 解读，快人一步</span>
> 
> > 我们被要求对一篇学术论文进行深度解读，格式要求严格，需要包含九个模块。用户提供的论文是“Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set”，作者Kresse和Furthmüller，1996年发表在Computational Materials Science。任务是生成一篇结构化的解读，面向初学者和非专业读者。需要遵循Markdown格式，纯文本输出，包含所有指定模块，第九部分要用Obsidian Dataview格式。
> > 
> > 首先，我需要理解论文内容。论文主要介绍了使用平面波基组和赝势进行第一性原理总能计算的高效算法，详细讨论了迭代对角化、电荷密度混合、直接最小化等方法，并比较了它们的效率。重点介绍了VAMP程序（VASP的前身）。论文涉及方法包括：线性四面体方法、模糊化方法（如Methfessel-Paxton）、迭代对角化（Davidson、共轭梯度、残差最小化RMM-DIIS）、电荷密度混合（Broyden、Pulay）等。
> > 
> > 接下来，我将按照要求的模块构建解读报告：
> > 
> > 1.  引言：概述领域背景、研究问题、文献定位与核心价值。领域为第一性原理计算，核心问题是提高平面波赝势方法计算金属和半导体总能与电子结构的效率。文献价值在于提供了算法细节和比较，推动了VASP等软件的发展。
> >     
> > 2.  论文结构与逻辑概览：介绍论文框架。论文分为引言、KS能量泛函与部分占据、迭代对角化方法、电荷密度混合、直接最小化、方法比较、结论等章节。逻辑链条：从问题出发，介绍基础理论，然后分别讨论SC循环中的关键步骤（对角化、混合），再比较直接方法，最后给出性能比较和结论。
> >     
> > 3.  所有图表深度解析：论文中包含多个图表，如Fig.1-12。需要逐一描述并注明单位/量纲。Fig.1：自由能随展宽参数σ的收敛性（能量单位eV）。Fig.2：总能量随k点网格的收敛性（能量单位eV）。Fig.3：自洽循环流程图。Fig.4：力的收敛性（单位eV/Å/atom）。Fig.5-8：不同算法在非自洽和自洽计算中的收敛性（能量单位eV）。Fig.9：直接最小化方法的收敛性（eV）。Fig.10-12：自洽计算中能量、电荷密度残差、力的收敛性。Table 1：不同金属的展宽参数设置（eV）。Table 2：Rh的声子频率（THz）。Table 3：不同算法迭代一次的时间（秒）。需要对每个图表进行解析。
> >     
> > 4.  正文核心内容剖析：详细阐述研究背景、方法模型、实验结果与讨论。需要分小节：背景（第一性原理发展和Car-Parrinello方法的局限），KS能量泛函与部分占据（线性四面体方法、有限温度展宽方法、Methfessel-Paxton方法），自洽循环与迭代方法（流程图），迭代对角化（残差向量、预条件、Davidson、共轭梯度、RMM-DIIS），电荷密度混合（简单混合、Pulay、Broyden），直接最小化KS泛函，方法比较等。
> >     
> > 5.  结论与贡献：总结核心发现，包括算法效率比较、RMM-DIIS的优势、MP方法对金属的处理、自洽循环方法的优越性等。
> >     
> > 6.  未来发展方向展望：论文中可能提及的发展方向，如进一步优化直接方法、更大的系统、应用领域等。
> >     
> > 7.  学术思考与批判性分析：提出3-5个深度问题，如RMM-DIIS的适用性限制、预条件函数的选择、混合方法的稳定性等。
> >     
> > 8.  用户问题预测与解答：生成5个延伸问题及解答，如“为什么金属需要部分占据？”“什么是自洽循环？”“RMM-DIIS与共轭梯度有何区别？”等。
> >     
> > 9.  Obsidian Dataview专区：输出10个变量，内容为概述性语句。
> >     
> > 
> > 注意，所有内容需保持客观，仅基于文献分析。术语首次出现时标注中英文，关键术语加粗。
> > 
> > 现在开始撰写报告。
> 
> ## 一、引言
> 
> 在材料科学和凝聚态物理领域，第一性原理（ab-initio）计算已成为研究材料性质的核心工具。这类方法无需经验参数，仅依靠原子序数等基本物理量即可预测材料的电子结构、力学和热力学性质。然而，计算的精度和可处理的系统规模长期受限于算法的效率，尤其是在处理金属体系时，由于电子在费米能级附近的部分占据（partial occupancy），传统的能带结构积分方法收敛极为缓慢。
> 
> 本文献《使用平面波基组的金属和半导体第一性原理总能计算效率》（_Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set_）由G. Kresse和J. Furthmüller发表于1996年，是计算材料科学领域里程碑式的方法学论文。它系统描述并比较了基于赝势（pseudopotential）和平面波基组的第一性原理分子动力学计算中的核心算法，尤其聚焦于**自洽场循环（self-consistency cycle, SC）** 方法。论文不仅详细阐述了处理金属体系的**部分占据方法**（如线性四面体法与Methfessel-Paxton展宽法），还深入剖析了迭代对角化（iterative diagonalization）和电荷密度混合（charge density mixing）两大关键技术，并引入了一种基于残差最小化（residual minimization）的新颖算法——**RMM-DIIS（direct inversion of iterative subspace）**。
> 
> 该文献的核心价值在于其工程实现与理论完善的结合：文中所提出的算法构成了后来广泛应用的第一性原理软件包**VASP（Vienna Ab-initio Simulation Package）** 的基石。它通过精巧的算法设计，将计算复杂度推向近 N² 标度，使得对液态金属、过渡金属表面、半导体表面等复杂体系的高效模拟成为可能，极大地推动了第一性原理计算在材料科学中的普及与深入。
> 
> ## 二、论文结构与逻辑概览
> 
> 本文遵循“理论框架 → 核心算法 → 方法比较 → 结论”的层进式结构，逻辑链条清晰，可抽象为以下流程：
> 
> _背景与问题：_ 传统Car-Parrinello（CP）方法受限于绝热性要求，时间步长受电子自由度制约，且对金属体系效率低下 → _理论与基础：_ 介绍Kohn-Sham能量泛函和部分占据的处理（线性四面体法、有限温度展宽法、MP方法） → _核心算法一：_ 迭代矩阵对角化（Davidson、共轭梯度CG、残差最小化RMM-DIIS）→ _核心算法二：_ 电荷密度混合（简单混合、Pulay法、Broyden法）→ _替代路线：_ 直接最小化Kohn-Sham泛函（CGa、SDa）→ _对决与检验：_ 在液态锗、钯表面、金刚石表面三类体系中对比各种算法的收敛表现 → _结论与展望：_ 确立SC方法（尤其是RMM-DIIS + Pulay混合）的优越性，并讨论其通用性。
> 
> 整体论证围绕“如何高效、精确地求解金属和半导体体系的电子基态”这一核心问题，从数学原理、数值实现到实际性能测试，层层递进，最终给出一个完整的、经过多项基准测试验证的算法方案。
> 
> ## 三、所有图表深度解析
> 
> 本文包含12张图和3张表，它们从不同维度量化了算法的精度和效率。
> 
> **图1. 自由能随展宽参数σ的收敛性** _（单位：能量 eV）_ 展示了铝（Al）和钒（V）中，不同展宽方法下自由能F(σ)或其修正值Ẽ(σ)随展宽参数σ的变化。包括高斯展宽（N=0）和Methfessel-Paxton（MP）方法（N=1, 2）。高斯展宽（N=0）的F(σ)严重偏离σ=0时的真实能量，而修正后的Ẽ(σ)和MP方法的自由能（N≥1）能在较大σ下保持平稳，收敛到零温总能量。这证实了MP方法在容忍较大σ的同时保持高精度的优势。
> 
> **图2. 总能量随k点网格的收敛性** _（单位：能量差 meV）_ 比较了LT-C（线性四面体法加修正）、MP方法（N=1）和高斯展宽（N=0）在不同k点网格密度下的能量收敛行为。LT-C和MP方法均能在较稀疏的网格下达到小于1 meV的精度，而高斯展宽收敛最慢。这表明前两者能显著减少k点采样数，节省计算资源。
> 
> **图3. 自洽场（SC）循环流程图** _（流程示意图）_ 描述了从初始试探电荷密度和波函数开始，经过计算Hartree势和交换关联势、构建非局域赝势、子空间对角化、迭代优化波函数、更新部分占据数、计算自由能、生成输出电荷密度、混合电荷密度以得到新输入密度，并循环直至自洽的完整过程。此图是理解SC方法运作逻辑的关键。
> 
> **图4. 力的收敛性对比** _（单位：eV/Å/atom）_ 对于Pd(111)表面，展示了三种不同力计算方法随自洽迭代次数的收敛曲线：“out”直接使用输出电荷密度计算力，收敛极慢且波动大；“mix”使用混合后的电荷密度，收敛有所改善；“opt”是作者提出的优化方案（包含修正项），收敛最快且最平稳。这证明了在自洽过程中正确计算力的重要性。
> 
> **图5-7. 非自洽迭代对角化算例** _（单位：eV/atom）_ 分别针对液态Ge（64原子）、Pd(111)表面和金刚石C(100)表面，对比了**DAV2**（块Davidson方法）、**CG**（序贯共轭梯度法）和**RMM**（残差最小化法）在固定哈密顿量下优化波函数的能量收敛速度。总体上，CG收敛最快，RMM略慢，DAV2最慢。但考虑到每一步的耗时，对于大体系，RMM因其避免了显式正交化而具有显著的总体效率优势。
> 
> **图8-9. 自洽计算收敛性：液态Ge** _（单位：eV/atom）_ 图8比较了SC方法（CG、RMM、DAV2）与直接最小化方法（CGa-148）在自洽循环中的总自由能收敛。SC方法均远快于CGa。图9进一步对比了不同直接最小化方法（CGa和SDa）在不同能带数（128和148）下的收敛情况，表明即使优化了直接方法，其效率仍远低于SC方法。
> 
> **图10-12. 自洽计算收敛性：Pd(111)和C(100)表面** _（单位：能量eV/atom、残差、力eV/Å/atom）_ 图10展示了Pd(111)表面在自洽计算中能量、电荷密度残差和作用力的收敛，对比了Pulay混合（不同初始矩阵）和CGa。图11对比了不同混合算法（Pulay有/无度量、Broyden第二方法）的电荷密度残差收敛。图12则展示了C(100)表面的类似对比。这些图表共同表明，对于电荷震荡（charge sloshing）严重的体系，Pulay混合方法结合合适的预条件（preconditioning）矩阵和度量，稳定性远优于Broyden方法和直接方法。
> 
> **表1. 不同金属的推荐展宽参数σ** _（单位：eV）_ 列出了Al、Li、Te、Cu、V、Rh等金属在使用MP方法（N=1）时，使熵项能量小于1 meV/atom的σ值。σ的选择受限于电子态密度（DOS）在费米能级附近的复杂程度，如Cu受限于d带位置，σ需较小。
> 
> **表2. Rh的声子频率** _（单位：THz）_ 展示了使用能量差法和力法、并结合不同部分占据方法（MP、LT-C、LT）计算得到的Rh声子频率。结果证明，MP方法在能量和力上能给出自洽一致的结果，而LT-C方法若简单固定占据数计算力，则会导致高达5%的误差，凸显了MP方法在力计算上的可靠性。
> 
> **表3. 各算法单步迭代耗时** _（单位：秒）_ 在IBM RS 6000/Model 590上测试了液态Ge（64原子）体系中不同算法进行一次迭代所需的时间。RMM和CGa耗时相当，但RMM在实空间版本中明显更快，并且其计算量随体系增长的标度更优，是处理大体系的首选。
> 
> ## 四、正文核心内容剖析
> 
> ### 4.1 研究背景与问题界定
> 
> 第一性原理计算的核心是求解多电子薛定谔方程的 **Kohn-Sham (KS) 方程**。Car和Parrinello（CP）在1985年提出的统一动力学方法开创了第一性原理分子动力学，但其存在两大局限：一是时间步长受电子自由度限制，二是对金属体系处理困难。根本原因在于，金属的电子占据数在费米能级处从1突变到0，导致布里渊区积分需要极其密集的k点采样，且电子基态的计算效率低下。
> 
> 本文的核心问题意识是：**如何构建一套高效、稳健且通用的算法框架，以显著提升平面波赝势方法在金属和半导体体系中的计算效率，并克服CP方法的固有缺陷？**
> 
> ### 4.2 理论基础：部分占据与KS能量泛函
> 
> 为处理金属，必须引入**部分占据（partial occupancies）** 的概念。
> 
> 1.  **线性四面体法（Linear Tetrahedron Method, LT）**：通过在四面体网格内线性插值能带，解析计算态密度和积分权重。Blöchl后来提出的**LT-C修正**通过考虑能带弯曲，消除了二次误差，收敛极快，但代价是破坏了能量的变分性，导致力的计算不便。
> 2.  **展宽法（Smearing methods）**：将阶梯函数替换为平滑函数，如Fermi-Dirac函数或高斯函数。此时，体系的总能E需要推广为**广义自由能F = E - σS**，其中σ为展宽参数，S为广义熵。通过对F求导可得到正确的力。但高斯展宽会引入σ²量级的误差，需通过 ( E(\sigma) = (F(\sigma) + E(\sigma))/2 ) 进行外推修正。
> 3.  **Methfessel-Paxton (MP) 方法**：这是对展宽法的重大改进。它利用完备正交函数展开阶梯函数，得到一系列的近似（N=0,1,2...）。N=0即高斯展宽，N≥1时，自由能F与零温能量( E_{σ=0} )的偏差仅为σ的N+2次方量级，且熵项S本身极小（<1 meV/atom）。这完美解决了高斯展宽的两个缺陷：力的定义与能量最小值一致，且无需精细调节σ。该方法成为处理金属体系最优雅、实用的方案。
> 
> ### 4.3 核心算法一：迭代矩阵对角化
> 
> 求解KS方程就是求解一个大型矩阵的广义本征值问题 ( H|\phi_n\rangle = \epsilon_n S|\phi_n\rangle )。迭代方法只需求解占据态，并能利用平面波基组下哈密顿量作用的快速计算（通过FFT），其核心是**残差向量（residual vector）** ( |R(\phi_n)\rangle = (H - \epsilon_n S)|\phi_n\rangle ) 和**预条件处理（preconditioning）**。作者采用了一种由Teter等人提出的高效预条件函数。
> 
> 文中详细比较了三种迭代对角化策略：
> 
> -   **块Davidson方法（DAV2）**：同时更新所有能带，将预条件残差向量加入展开子空间，然后通过Rayleigh-Ritz方法对角化。实现简单，但需要存储大量向量，且正交化开销大，随体系规模标度不佳。
> -   **序贯共轭梯度法（Sequential CG）**：依次优化每个能带，搜索方向由预条件梯度与之前方向的共轭组合构成。收敛快，但同样需要显式地将搜索方向正交化于其他所有能带，这是N³量级的操作。
> -   **残差最小化方法——迭代子空间直接反演（RMM-DIIS）**：这是本文最具创新性的算法。它通过最小化**残差向量的范数**而非Rayleigh商来寻找本征矢。由于残差范数在本征态处具有无约束最小值，因此**无需显式正交化**！算法通过向预条件残差方向试探一步，构建新、旧波函数和残差向量的子空间，并在其中线性组合以最小化残差范数。该方法在保持与CG相近迭代次数的同时，单步计算量更小，尤其避免了大体系下正交化带来的内存带宽瓶颈和N³标度，是实现近N²标度的关键。
> 
> ### 4.4 核心算法二：电荷密度混合
> 
> 在自洽循环中，需根据输入电荷密度 ( p_{in} ) 和输出电荷密度 ( p_{out} ) 的残差 ( R[p_{in}] = p_{out} - p_{in} ) 来生成新的 ( p_{in} )。简单的线性混合 ( p_{in}^{new} = p_{in} + \gamma R ) 效率低，对于电荷震荡（charge sloshing）严重的体系极易发散。
> 
> 作者引入并改进了基于**准牛顿（Quasi-Newton）** 思想的混合方法：
> 
> -   **Pulay混合**：存储前几步的输入密度和残差，线性组合这些输入密度，使得组合后的残差范数最小。这等价于一种对逆雅可比矩阵（inverse Jacobian）的递推构建。
> -   **Broyden混合**：通过更新公式直接逼近逆雅可比矩阵。作者展示了Pulay方法与Broyden第二方法在特定参数极限下的等价性。
> -   **预条件与度量**：作者引入了一个在倒空间中对角化的预条件矩阵 ( G' )，其形式为 ( (q^2 + q_0^2)/q^2 ) 类型，能有效抑制低波数（长程）电荷震荡。此外，在计算残差内积时引入一个度量因子 ( f_q = (q^2 + q_1^2)/q^2 )，赋予低波数分量更高权重，显著提升了混合的稳定性。
> 
> ### 4.5 替代方案：直接最小化KS泛函
> 
> 作为对比，论文也讨论了直接利用共轭梯度（CGa）或最速下降（SDa）方法，在波函数和部分占据数构成的高维空间中直接最小化总的自由能泛函。其关键在于需要同时处理波函数子空间的变化（修正向量）和子空间内的幺正旋转（使子空间哈密顿量对角化）。然而，数值实验表明，这种优雅的数学框架在效率上远逊于SC方法，甚至比CP方法改进版也快不了多少。SC方法在效率和稳定性上的优势，使其成为当时主流的VASP程序的基础。
> 
> ## 五、结论与贡献
> 
> 本文通过详尽的算法描述和基准测试，得出以下核心结论：
> 
> 1.  **自洽循环（SC）方法**在计算金属和半导体体系时，普遍优于直接最小化KS泛函的方法，效率高出3-5倍，且鲁棒性更强。
> 2.  在SC方法中，**RMM-DIIS**迭代对角化算法因其避免了显式正交化，在保持快速收敛的同时，实现了更优的计算标度，尤其适用于大体系（>30个原子）。
> 3.  **Methfessel-Paxton展宽法**是处理金属部分占据问题的最优选择，它解决了传统展宽法中能量与力定义不一致的问题，且无需精细调节展宽参数σ，熵项可直接作为误差估计。
> 4.  **Pulay混合方法**配合预条件矩阵和优化度量，能够有效抑制电荷密度在自洽迭代中的长程震荡，其稳定性优于Broyden第二方法。
> 
> **主要贡献**：本论文不仅是对已有算法的系统综述，更是一个集大成式的创新工作。它首次将MP展宽、RMM-DIIS对角化、Pulay混合等最优组件整合为一个统一的算法框架，并以此为基础构建了VASP软件包。这一工作极大地推动了第一性原理计算在复杂材料体系（如液态金属、过渡金属、表面界面）中的应用，奠定了VASP在后续二十余年成为领域黄金标准的方法学基础。
> 
> ## 六、未来发展方向展望
> 
> 作者在文中（1996年）展望了未来可能的优化方向：
> 
> 1.  **直接能量最小化方法的进一步优化**：作者承认直接方法在数学上更优美，未来若能解决其在线搜索（line minimization）精度和多变量协同优化上的问题，仍有提升效率的潜力。
> 2.  **算法通用性的扩展**：文中的算法不仅适用于赝势方法，也可推广至**投影缀加平面波（PAW）** 和**线性缀加平面波（LAPW）** 等全势方法，预示着这些高效算法能在更广泛的基组下发挥作用。
> 3.  **对更大规模并行计算的支持**：RMM-DIIS方法因其各能带优化过程的“局域性”（无需相互通信），天然适合大规模并行计算，这暗示了未来向千原子级系统模拟的扩展能力。
> 4.  **与其他物理性质计算的整合**：文中展示了精确计算力的能力，这为后续高效计算声子谱、弹性常数等晶格动力学性质，以及进行更长时间尺度的分子动力学模拟铺平了道路。
> 
> ## 七、学术思考与批判性分析
> 
> 尽管本文的算法取得了巨大成功，但仍可从批判性视角提出以下问题：
> 
> 1.  **RMM-DIIS方法的“能带遗漏”风险**：该算法总是收敛到离初始猜测最近的波函数，若初始波函数构建不当，可能导致最终解中缺失某个本征态。文中提到了通过多次“扫掠”（sweep）和子空间旋转来缓解，但这种“修补”本质上未完全解决其非全局搜索的缺陷。在电子结构变化剧烈的反应路径中，是否存在更根本的解决方案？
> 2.  **预条件函数的普适性**：文中采用的预条件函数（式53）和电荷密度混合的预条件矩阵（式82）均包含经验参数（如 ( q_{cut} )、( q_0 )、( A )）。虽然作者声称预设参数对多数体系鲁棒，但这是否意味着在强关联体系或极低维材料中，需要重新调优？是否存在一种自适应的、无参数的预条件方法？
> 3.  **MP展宽法的物理图像**：MP方法本质上是一种数学技巧，其高阶近似（N≥1）下的广义熵项S已无直接的物理意义，仅作为误差估计。这种“虚构”的熵项是否可能在某些极端条件下（如电子熵与离子熵强烈耦合时）给出误导性的热力学性质？尽管文中证明了其能量和力的自洽性，但其非平衡态过程的物理意义值得商榷。
> 4.  **Pulay混合的健壮性极限**：尽管Pulay混合在多数测试中表现优异，但Broyden方法在离子弛豫问题中因线性相关较弱而更稳定。这暗示Pulay法在遇到高度非线性或历史信息高度相关的迭代序列时可能失效。如何智能地在这两种方法间切换，或设计一个更普适的混合框架，是一个有趣的课题。
> 5.  **算法效率的“隐性”成本**：论文对比效率时，主要衡量了迭代次数和单步耗时。然而，RMM-DIIS方法需要存储多个历史向量，其内存占用高于简单的CG方法。在内存受限的早期并行机或如今的GPU异构计算中，内存带宽和容量往往成为瓶颈。这种计算-存储的权衡，在当前背景下是否会导致算法优选策略的转变？
> 
> ## 八、用户问题预测与解答
> 
> **问题1：为什么计算金属需要引入“部分占据”，而绝缘体不需要？** **解答**：绝缘体和半导体的电子结构在费米能级处存在一个能隙（band gap），价带（occupied bands）与导带（unoccupied bands）完全分离。因此，价带的所有电子态占据数都为1，导带都为0，没有模糊地带。积分时，费米能级位于能隙中，不切割任何能带。而金属的费米能级穿过能带，部分电子态的能量低于费米能级，部分高于。在绝对零度下，占据数是一个阶跃函数，这导致在k空间积分时，被积函数不连续，收敛极慢。引入部分占据本质上是将阶跃函数“模糊化”，使能带积分变为平滑函数，从而可以用少量k点就得到高精度结果。
> 
> **问题2：什么是“自洽场（SC）循环”？它在计算中扮演什么角色？** **解答**：在Kohn-Sham密度泛函理论中，有效势能（Hartree势和交换关联势）依赖于电荷密度，而电荷密度又由波函数计算得到，波函数又是通过求解该有效势能下的薛定谔方程得到的。这形成了一个“鸡生蛋、蛋生鸡”的循环。**自洽场循环**就是一种迭代求解策略：先猜测一个初始电荷密度 → 构建有效势 → 求解KS方程得到波函数 → 从波函数计算新的电荷密度 → 将新旧电荷密度混合，生成下一个猜测 → 重复此过程，直到输入和输出的电荷密度之差（即残差）小于预设阈值。此时，我们得到的电荷密度、势能和波函数是相互一致的，体系达到了“自洽”的电子基态。
> 
> **问题3：为什么RMM-DIIS算法不需要显式正交化？这和共轭梯度法有什么本质不同？** **解答**：共轭梯度法（CG）是通过最小化**Rayleigh商** ( \langle \phi|H|\phi\rangle / \langle \phi|\phi\rangle ) 来寻找本征态。Rayleigh商在本征态处是**驻点**（saddle point），而非最小值。如果不加约束，CG会收敛到最低的本征值，无法提取激发的本征态。因此，必须将搜索方向显式地正交化于所有已找到的低能态，以“踢开”它们，寻找更高的本征值。**RMM-DIIS**最小化的目标函数是**残差向量的范数** ( \langle R|R\rangle )。这个范数在每一个本征态处都达到**绝对最小值0**。因此，无论目标态是基态还是激发态，只要给定一个足够接近的初始猜测，算法就会自动收敛到离它最近的那个本征态，无需通过正交化来排斥其他态。这使其能带优化过程完全解耦，极大提升了并行效率。
> 
> **问题4：电荷密度混合中的“预条件”和“度量”是什么意思？** **解答**：“混合”是将输出电荷密度 ( p_{out} ) 和输入电荷密度 ( p_{in} ) 按一定比例组合，生成新的 ( p_{in} )。**预条件**（preconditioning）的作用是，在将残差 ( R = p_{out} - p_{in} ) 加到 ( p_{in} ) 上之前，先用一个矩阵 ( G' ) 对其进行“整形”。在平面波基组中，这个矩阵通常在倒空间是对角化的，其主要作用是**抑制长波（低( q )）分量的震荡**。因为长波电荷转移对应着巨大的能量变化，是导致自洽迭代发散的主要原因。**度量**（metric）则是在计算残差向量内积 ( \langle R|R\rangle ) 时，对不同波数分量赋予不同权重。作者同样赋予低波数分量更高权重，这使得优化算法在判断“哪个混合方向最优”时，会更关注长波部分的收敛，从而提升整体稳定性。
> 
> **问题5：为什么这篇文章对于VASP软件如此重要？** **解答**：这篇文章可以看作是VASP的“奠基性算法宣言”。VASP全称是Vienna Ab-initio Simulation Package，而本文标题中的VAMP正是其前身。文章并非简单地应用现有算法，而是系统地设计、比较并整合了当时最先进但分散在不同文献中的算法组件（如MP展宽、RMM-DIIS、Pulay混合），并进行了多项关键改进（如力的优化计算、混合的预条件度量）。它证明了这套“组合拳”在处理当时最具挑战性的金属和表面体系时，相比同时代的其他方法（如CP方法）具有数量级的效率优势。因此，这篇论文定义了VASP的核心算法基因，其方法至今仍是VASP内部工作的基石，是理解其高效率、高稳定性的最关键文献。
> 
> ## 九、专区：便于 Obsidian Dataview 插件调用
> 
> 领域基础知识:: 本领域为计算材料科学中的第一性原理总能计算，基于密度泛函理论（DFT）的Kohn-Sham方程，采用平面波基组和赝势（pseudopotential）或超软赝势（ultrasoft pseudopotential, US-PP）来展开电子波函数，通过自洽求解电子基态能量和电荷密度。 研究背景:: 20世纪90年代，Car-Parrinello（CP）联合动力学方法推动了第一性原理分子动力学，但其时间步长受限于电子自由度，且对金属体系因电子占据数在费米面处的突变，导致k点积分收敛极慢，计算效率低下。 作者的问题意识:: 如何构建一套高效、稳健且通用的算法框架，以显著提升平面波赝势方法在金属和半导体体系中的电子基态计算效率，并克服CP方法对金属处理困难和绝热限制的固有缺陷。 主要研究对象:: 基态电子结构计算的核心算法，包括：处理金属部分占据的Methfessel-Paxton展宽法与线性四面体法；迭代矩阵对角化技术（Davidson、共轭梯度、残差最小化RMM-DIIS）；电荷密度自洽混合技术（Pulay混合、Broyden混合及其预条件处理）；以及直接最小化Kohn-Sham泛函的优化方法。 主要研究方法:: 通过理论推导阐述各种算法的数学原理，并将其实现于一个统一的程序包VAMP中。然后，选取液态锗（金属）、钯(111)表面（强电荷震荡金属）和金刚石(100)表面（半导体）三个典型体系，对上述不同算法组合进行非自洽和自洽的基准测试，从能量收敛速度、力的收敛精度、单步耗时等维度进行定量比较。 研究意义:: 通过系统整合与创新，构建了后来VASP软件的核心算法框架，使得对包含过渡金属、液态金属等复杂体系的高效、精确第一性原理模拟成为可能，极大地推动了计算材料科学的发展。 研究结论:: 1. 基于自洽场循环（SC）的方法在效率上普遍优于直接最小化KS泛函的方法。2. 在SC方法中，RMM-DIIS迭代对角化算法因避免了显式正交化，对大于30个原子的体系具有最优的计算标度。3. Methfessel-Paxton展宽法是处理金属部分占据问题的最优方案，其能量和力自洽一致，且无需精细调节参数。4. 结合了预条件矩阵和优化度量的Pulay混合方法，能有效抑制电荷密度震荡，是自洽混合的最稳定选择。 对领域的贡献: 奠定了现代第一性原理计算软件VASP的方法学基础，将RMM-DIIS对角化、MP展宽、Pulay混合等最先进算法创造性地整合为一个高效、稳健的通用框架，并论证了其对金属、半导体、表面等复杂体系的普适性，开启了大规模、高精度第一性原理分子动力学模拟的新阶段。 未来研究方向提及: 文中提及的未来方向包括：进一步优化直接能量最小化方法的在线搜索精度；将算法推广至PAW（投影缀加平面波）和LAPW（线性缀加平面波）等全势方法；利用RMM-DIIS的天然并行性支持更大规模计算；以及将高效算法与精确力计算结合，用于声子谱等晶格动力学性质的计算。 未来研究方向思考: 可进一步研究自适应、无参数的预条件函数，以应对强关联或低维材料；探索RMM-DIIS方法在能带反交叉等复杂情况下的全局收敛性问题；结合机器学习技术，开发更智能的电荷密度混合策略，以预测历史信息并加速收敛；在异构计算（GPU）架构下，重新评估内存占用与计算效率之间的权衡，优化算法设计。
> 
> 🚀 [笔记回链](zotero://select/library/items/IAA6NZLC)
> 
> * * *
> 
> `GPT 自定 ②`  `deepseek-v4-pro`  _由批量 AI 解读自动生成于 2026/8/11 07:02:03 （重新解读）_
> 
> 🏷️ #🤖️/AI文献解读 🏷️ #🤖️/AI文献阅读

^KEYCE16875F

## <span style="color: rgb(0, 174, 137);">❷ 🤖️ 论文深度解读📌</span>

> 🚀 [笔记回链](zotero://select/library/items/G3PGT3V5)

^KEYaiPaper0

> <span class="AIReading">🤖 AI 解读，快人一步</span>
> 
> > 嗯，用户要求我作为学术文献深度解读专家，解读一篇关于VASP软件核心算法的经典论文。这篇论文技术性很强，涉及密度泛函理论、平面波基组、赝势方法、迭代对角化、电荷密度混合等多个专业领域。
> > 
> > 我需要根据用户提供的角色定位和格式规范，生成一份结构化的解读报告。用户是初学者或非专业读者，所以我的解读必须通俗易懂，用类比和案例解释复杂概念，同时保持学术严谨性。
> > 
> > 先梳理一下论文的核心内容。这篇论文主要介绍了在平面波基组下进行从头算总能量计算的高效算法，包括如何处理金属体系的部分占据、Kohn-Sham哈密顿量的迭代对角化方法（特别是RMM-DIIS）、以及电荷密度混合方法（Broyden/Pulay）。这些算法后来构成了VASP软件的基础。
> > 
> > 我需要构建一个完整的报告框架。引言部分要概述论文的背景、核心问题和价值。逻辑概览要展示论文的结构和论证链条。图表解析部分……等等，这篇论文里有图表吗？我需要仔细检查一下。论文中有图1到图12，展示了不同方法的收敛性比较。我需要逐一描述这些图表，并注明单位。
> > 
> > 正文剖析部分要详细阐述研究背景、方法模型和结果。结论部分要总结核心发现。展望部分要讨论未解决的问题。批判性分析部分要提出深度问题。最后，用户问题预测部分要生成延伸问题并解答。
> > 
> > 考虑到用户可能没有专业背景，我需要用浅显的语言解释“赝势”、“Kohn-Sham方程”、“迭代对角化”等概念，可以用比喻，比如把寻找电子基态比作在复杂地形中寻找最低点。同时，要突出论文的贡献，比如它提出的算法如何使得计算效率大幅提升，让模拟更大更复杂的体系成为可能。
> > 
> > 现在，我可以开始构思具体的回答了。我会按照要求的八个模块来组织内容，确保信息密度适中，术语首次出现时提供中英文对照，并思考如何将一些关系转化为文字描述。
> 
> 好的，作为您的学术文献深度解读专家，我将为您呈现对这篇经典计算材料科学文献的深度解读。这篇论文是著名的第一性原理计算软件VASP的奠基性文献，我将尽力将其中复杂的算法原理，用清晰易懂的方式为您剖析。
> 
> * * *
> 
> ## **学术文献深度解读报告**
> 
> **文献标题：** Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set **中文译名：** 使用平面波基组对金属和半导体进行从头算总能量计算的效率 **作者：** G. Kresse, J. Furthmüller **期刊：** Computational Materials Science 6 (1996) 15-50
> 
> * * *
> 
> ## **一、引言**
> 
> ### **1. 领域背景：“从头算”何以成为材料科学的“显微镜”？**
> 
> 在材料科学领域，我们一直梦想着能像拥有一个超级显微镜一样，在不做实验的情况下，仅凭最基本的物理定律就能预测材料的性质。**从头算方法**正是这一梦想的产物。它的核心思想是：只利用原子的序号（即原子核电荷数）作为输入，通过求解描述电子行为的薛定谔方程，来理论预测材料的稳定结构、电子特性、力学性质等。这种方法不依赖任何经验参数，因此被称为“从头算”。
> 
> ### **2. 研究问题：如何让这只“显微镜”看得更快更广？**
> 
> 尽管从头算方法功能强大，但其计算量巨大，长久以来只能处理非常小的体系。本文旨在解决一个核心瓶颈：**如何提升基于平面波基组的从头算总能量计算效率，使其能够应用于更大、更复杂的体系，尤其是金属和半导体？** 作者通过提出和比较一系列算法，系统地回答了这个问题。
> 
> ### **3. 文献定位与核心价值**
> 
> 这篇1996年发表的论文是计算材料学领域的里程碑式文献。它详细描述了**VASP**（维也纳从头算模拟程序包）的核心算法，该程序包至今仍是全球使用最广泛的第一性原理计算软件之一。其核心价值在于：
> 
> -   **系统性地整合与优化**：将当时最先进的算法理念（如自洽循环、迭代对角化、电荷密度混合）整合为一个高效、稳定的整体方案。
> -   **解决金属难题**：深入探讨了处理金属体系时至关重要的**部分占据数**问题，并提出了高效的解决方案。
> -   **奠定软件基石**：本文所述的算法直接构成了VASP高效运行的基石，深刻影响了此后二十余年计算材料学的发展。
> 
> * * *
> 
> ## **二、论文结构与逻辑概览**
> 
> 本文的逻辑结构清晰，遵循“提出问题 → 分解核心模块 → 逐一优化 → 系统集成与比较”的脉络。
> 
> **核心论证链条：**
> 
> 1.  **明确目标**：精确、高效地求解电子基态，这是计算一切材料性质的基础。
> 2.  **确立框架**：计算基于**Kohn-Sham密度泛函理论**，并采用**平面波基组**和**赝势**（或**超软赝势**）来离散化方程。
> 3.  **模块化分解**：将复杂的计算流程拆解为两个核心模块：
>     -   **模块一：电子波函数优化**（第三章）—— 如何从给定的电荷密度（或势能）中高效求解出Kohn-Sham方程的本征值和本征波函数。
>     -   **模块二：电荷密度自洽**（第四章）—— 如何根据计算出的波函数构建新的电荷密度，并将其与旧的电荷密度巧妙混合，以快速找到自洽的电荷密度。
> 4.  **关键议题处理**：在第二章专门讨论了处理金属体系的关键技巧——**部分占据数**，这是保证金属计算收敛性和准确性的前提。
> 5.  **算法对比与集成**：在第六和第七章，作者将上述模块化算法组合成不同的完整方案（如自洽循环法 vs. 直接最小化法），并通过多个测试体系（液态锗、金属钯表面、金刚石表面等）进行性能对比，最终证明其提出的**自洽循环法**在效率上具有显著优势。
> 
> * * *
> 
> ## **三、所有图表深度解析**
> 
> 本文的图表主要集中在第六章，用于对比不同算法的性能。作者通常使用**总自由能**（单位为eV/原子）和**电荷密度残差**（无单位）作为收敛评判标准。
> 
> -   **图1：自由能随展宽参数σ的收敛性**
>     
>     -   **内容**：展示了对于Al和V，使用高斯展宽（N=0）和Methfessel-Paxton方法（N=1, 2）时，计算得到的自由能`F`以及外推能量`Ẽ`随展宽参数σ的变化。
>     -   **核心洞察**：高斯展宽的`F`随σ增大显著偏离真实值，而`Ẽ`和MP方法（N≥1）的`F`能在一个较大的σ范围内保持稳定，且接近真实值。这证明了MP方法允许使用更大的σ，从而可以使用更少的k点，同时获得高精度。
> -   **图2：总能量随k点网格密度的收敛性**
>     
>     -   **内容**：比较了线性四面体方法（LT-C）和两种展宽方法（Gaussian, MP）下，总能量随k点网格（`grid × grid × grid`）加密的收敛速度。
>     -   **核心洞察**：LT-C方法收敛最快，准确性最高。MP方法（N=1）紧随其后，允许使用较大的σ，收敛速度也很快。简单高斯展宽因需要很小的σ，收敛最慢。这为不同场景下的方法选择提供了依据。
> -   **图5 & 图6 & 图7：非自洽迭代矩阵对角化性能对比**
>     
>     -   **内容**：分别测试了液态Ge、Pd表面和金刚石C表面，在固定哈密顿量下，不同迭代对角化算法（DAV2, CG, RMM）的能量收敛速度。横轴为迭代步数，纵轴为能量。
>     -   **核心洞察**：**CG算法**在小体系中最快；**RMM算法**在大体系中最优，因为其避免了显式正交化，节省了大量计算量；**DAV2**（分块Davidson）方法总是最慢的。
> -   **图8 & 图9：自洽计算性能对比（液态Ge）**
>     
>     -   **内容**：比较了自洽循环法（RMM, CG）和直接最小化法（CGa, SDa）在液态Ge体系的能量收敛速度。
>     -   **核心洞察**：**自洽循环法（RMM和CG）的收敛速度比直接最小化法（CGa）快3-5倍**，证明了其在处理金属体系时的巨大优势。即使采用更高效的共轭梯度（CGa），其性能仍不及前者。
> -   **图10 & 图12：自洽计算性能对比（Pd表面 & C表面）**
>     
>     -   **内容**：展示了在不同混合参数下，总能量、电荷密度残差和原子受力的收敛过程。
>     -   **核心洞察**：Pulay电荷密度混合方法非常稳健，对初始混合参数不敏感。加入**度量**（Metric）对于Pd这样的强电荷振荡体系至关重要。自洽循环法在能量和力的收敛速度上均优于直接最小化法（CGa）。
> 
> * * *
> 
> ## **四、正文核心内容剖析**
> 
> ### **1. 研究背景与核心问题（第1-2章）**
> 
> 作者首先指出，传统Car-Parrinello方法的局限性在于其时间步长受电子运动频率限制，效率不高。一个更直接的替代方案是**在每个离子移动步后，精确地计算电子基态**。这就需要高效的电子基态求解算法。文章的核心就是介绍和比较两种实现这一目标的策略：
> 
> -   **(i) 直接方法**：直接最小化Kohn-Sham能量泛函。
> -   **(ii) 自洽循环方法**：迭代地求解Kohn-Sham方程，并混合电荷密度以实现自洽。
> 
> ### **2. 方法模型详解（第2-5章）**
> 
> 作者将整个计算流程模块化，并逐个击破。
> 
> #### **2.1 处理金属的关键：部分占据数（Section 2.2）**
> 
> 对于金属，费米能级附近的电子占据数会从1突变为0，这导致对k点的求和收敛极慢。为了解决这个问题，引入了“抹平”技巧。
> 
> -   **类比**：想象一个阶梯函数（0/1占据），很难用有限的点来精确描述其积分。但如果用一个平滑的S型曲线（如误差函数）来替代，用同样数量的点就能得到更精确的积分结果。
> -   **三种方法比较**：
>     -   **线性四面体方法（LT）**：最严谨，但计算力不方便。
>     -   **展宽方法（Smearing）**：引入一个“电子温度”概念，将占据数函数平滑化。常见的如**费米-狄拉克展宽**和**高斯展宽**。
>     -   **Methfessel-Paxton (MP) 方法**：一种更高级的展宽方法，它通过函数展开，可以以更小的误差逼近真实的阶梯函数，从而允许使用更大的展宽参数σ，且计算得到的力也是准确的，是处理金属的“利器”。
> 
> #### **2.2 电子波函数的高效求解：迭代对角化（Section 3）**
> 
> 这是计算的核心。问题转化为求解一个巨大的矩阵本征值问题：`Hφ = εSφ`。直接对角化计算量随系统大小三次方增长，无法用于大体系。作者对比了多种迭代方法，其基本思想是：从一个初始猜测出发，通过不断改进波函数来逼近真实解。
> 
> -   **共轭梯度法与残差最小化法**：**RMM-DIIS**方法是本文的一大亮点。它不像CG方法那样需要将搜索方向与所有已占据的轨道正交化，而是直接最小化残差向量的模。**正交化是一个非常耗时的操作**，因此RMM在大型体系（>20-30个原子）中优势巨大，其计算量随体系大小的标度更接近二次方，而非三次方。
> -   **比喻**：想象在一个巨大的山谷中寻找最低点（基态）。CG方法需要你时刻检查自己的前进方向是否与所有已知路径垂直，这很耗费精力。而RMM方法则直接告诉你：“别管那么多，就朝着坡度最陡的地方向下走，直到走不动为止”，在特定地形下反而更高效。
> 
> #### **2.3 电荷密度的自洽：混合算法（Section 4）**
> 
> 这是实现自洽的关键。简单来说，我们用一个输入电荷密度`ρ_in`计算出势能，求解得到波函数，再从波函数构建一个输出电荷密度`ρ_out`。如果`ρ_in`和`ρ_out`不一致，计算就不自洽。混合算法就是如何巧妙地组合`ρ_in`和`ρ_out`，以生成一个新的、更佳的`ρ_in`，从而快速减小两者的差异。
> 
> -   **Pulay混合**：它存储了先前所有步的电荷密度和残差信息，并基于历史信息来预测最优的新电荷密度。这就像一个有经验的司机，能根据过去几秒的路况来预判并调整方向盘，而不是只看眼前。
> -   **Broyden混合**：一种更复杂的准牛顿方法，它试图在迭代过程中不断更新电荷密度变化量与残差变化量之间的“雅可比矩阵”，从而获得更快的收敛速度。
> 
> #### **2.4 直接最小化方法（Section 5）**
> 
> 作为对比，作者也实现了直接最小化Kohn-Sham能量泛函的方法。这需要同时优化所有电子波函数，并处理它们之间的正交性约束。虽然数学上很优美，但实际测试表明，其收敛速度远慢于自洽循环法，尤其是在金属体系中。
> 
> * * *
> 
> ## **五、结论与贡献**
> 
> 本文的核心结论是：**基于自洽循环的方法，结合高效的迭代对角化（如RMM-DIIS）和电荷密度混合（如Pulay/Broyden）技术，是实现金属和半导体体系高效从头算的最佳途径。**
> 
> **核心贡献：**
> 
> 1.  **算法集大成者**：系统性地阐述并比较了VASP软件的核心算法，提供了一个高效、稳定、可扩展的完整计算方案。
> 2.  **RMM-DIIS的推广**：证明了RMM-DIIS在大型体系电子结构计算中的优越性，为后续大规模计算铺平了道路。
> 3.  **Methfessel-Paxton方法的力计算**：澄清并推广了MP方法，使其成为计算金属体系力的可靠方法。
> 4.  **开放了材料模拟的“天地”**：显著提升了计算效率，使得对更大、更真实、更复杂的材料体系进行精确模拟成为可能，极大地推动了计算材料科学的发展。
> 
> * * *
> 
> ## **六、未来发展方向展望**
> 
> 作者在文中已暗示了未来的发展方向，结合当前领域进展，可以归纳为：
> 
> 1.  **超越“N³”标度**：发展**线性标度方法**，即计算量随体系原子数N线性增长，这是处理成千上万个原子体系的终极目标。
> 2.  **更精确的泛函与赝势**：本文使用LDA泛函，未来将更多地应用**范德华密度泛函（
> 
> 🚀 [笔记回链](zotero://select/library/items/G3PGT3V5)
> 
> * * *
> 
> `GPT 自定 ②`  `deepseek-v4-pro`  _由批量 AI 解读自动生成于 2026/8/11 05:45:29 （重新解读）_
> 
> 🏷️ #🤖️/论文深度解读 🏷️ #🤖️/AI文献阅读

^KEY5F739229

## <span style="color: rgb(0, 174, 137);">❸ 🤖️ 论文双语转写📌</span>

> 🚀 [笔记回链](zotero://select/library/items/IMS337DY)

^KEYaiPaper0

> <span class="AIReading">🤖 AI 解读，快人一步</span>
> 
> > 我们需要处理用户提供的PDF文本，将其转换为结构化的Markdown，并进行双语转换。文本是英文的，需要翻译成中文，并标注术语。用户要求我们作为技术文档格式化工程师兼专业译员，执行结构元素识别、翻译、术语管理、格式标准化。输出要遵循CommonMark规范，包含原文、中文翻译和术语解释。我们需要仔细解析输入文本，识别标题、段落、列表、代码块、引用块、表格等。文本内容是关于密度泛函理论计算的一篇学术论文，标题、摘要、章节等很清晰。
> > 
> > 首先，通读输入文本，进行结构解析。文本开头是期刊信息、论文标题、作者、摘要等。然后有1. Introduction，1.1 General，1.2 Outline of the paper，2. The Kohn-Sham energy functional...，2.1，2.2，等等。我们需要识别出这些标题层级。
> > 
> > 输入文本的开头部分：
> > 
> > 

<pre class="hljs"><code>ELSEVIER Computational Materials Science 6 (1996) 15-50
COMPUTATIONAL MATERIALS SClENCE
Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set
G. Kresse a ,vJ*. Furthmiiller b
’ lnstitutfi TheoretischePhysik, TechnischeUniversitiit Wien, Wiedner Hauptstra&amp; S-10, A-1040 Wien, Austria b Institutfir Festkiirpertheorie und Theoretische Optik, Friedrich-Schiller-Umbersit&amp;Jena. Max-Wien-Platz 1, D-07743 Jena, Germany
Received 4 February 19%; accepted 15 March 1996
Abstract
We present a detailed description and comparison of algorithms for performing ab-initio quantum-mechanical calculations using pseudopotentials and a plane-wave basis set. We will discuss: (a) partial occupancies within the framework of the linear tetrahedron method and the finite temperature density-functional theory, (b) iterative methods for the diagonalization of the Kohn-Sham Hamiltonian and a discussion of an efficient iterative method based on the ideas of Pulay’s residual minimization, which is close to an order N&amp;m scaling even for relatively large systems, (c) efficient Broyden-like and Pulay-like mixing methods for the charge density including a new special ‘preconditioning’ optimized for a plane-wave basis set, (d) conjugate gradient methods for minimizing the electronic free energy with respect to all degrees of freedom simultaneously. We have implemented these algorithms within a powerful package called VAMP (Vienna ab-initio molecular-dynamicspackage).The program and the techniqueshave been used successfully for a large number of different systems (liquid and amorphous semiconductors, liquid simple and transition metals, metallic and semi-conducting surfaces, phonons in simple metals, transition metals and semiconductors) and turned out to be very reliable.
1. Introduction
1.I. General
In recent years, ab-initio calculations have made a profound impact on the investigation of material properties. The main reason for the enormous success of ab-initio methods lies in the fact that they are parameter-free and require no other input than the atomic number. In addition, improvements in computer performance and algorithms allow to apply
* Corresponding author. E-mail: krcsse@tph20.tuwien.ac.at.
these methods to a steadily increasing number of physical and chemical phenomena. Probably, the most successful method currently tractable is the local density functional (LDF) theory proposed by Kohn and Sham [l]. In conjunction with the Hellmann-Feynman theorem [2] forces can be evaluated easily, allowing the simultaneous investigation of structural, electronic and dynamic properties. The first successful ab initio calculation in this context goes back to a seminal paper written by Car and Paninello (CP) [3]. In their work Car and Parrinello proposed a simulated annealing approach in which electrons and ions are treated on the same footing via
0927-0256/%/$15.00 Copyright 0 1996 Elsevier Science B.V. All rights reserved. PI/ SO927-0256(96)00008-O
</code></pre>


> > 
> > 然后正文继续，有页码行。我们需要把整个文本解析成结构化的单元。注意，文本中可能包含一些OCR错误，比如“19%”应该是“1996”，但保留原文。我们按用户要求处理。
> > 
> > 用户要求输出格式：
> > 
> > -   标题：`# [英文标题]` 然后新建一行 `[中文标题]` 然后 `**Term**: 术语解释`（如果有术语）
> > -   段落/列表/代码/引用：`[英文原文]` 然后 `[中文翻译]` 然后 `[可选术语解释]`
> > -   列表项保留原始符号，保持层级缩进
> > -   代码块：用三个反引号包裹并标注语言，
> > -   引用块：`> [引用内容]` 然后中文翻译等
> > 
> > 我们需要为每个单元分配唯一ID，但最终输出中可能不需要显示ID？用户说“按结构类型分割文本（标题/段落/列表/代码/引用/表格）为每个单元分配唯一ID（如 sec-1 / para-001）”，但输出格式里并没有要求输出ID。可能只是为了内部标记，但最终输出只输出Markdown文本，没有额外说明性内容。所以可能不需要输出ID。我们按标准Markdown输出，保持原文顺序。
> > 
> > 另外，术语解释：首次出现的核心术语标注。我们需要识别核心术语，如“ab-initio”、“pseudopotentials”、“plane-wave basis set”、“linear tetrahedron method”、“density-functional theory”、“Kohn-Sham Hamiltonian”、“Broyden-like”、“Pulay-like”、“conjugate gradient”、“VAMP”等。在首次出现时给出解释。
> > 
> > 注意：原文是整篇论文，我们只输出了提供的部分，但我们要处理整个提供的文本。用户给的文本是从 “ELSEVIER Computational Materials Science 6 (1996) 15-50” 开始，一直到 “References” 之前？实际上，提供的文本最后是 “References” 前的部分，结尾是 “[64] P.E. Bliichl, Phys. Rev. B 50 (1994) 17953.” 但最后有 “References” 吗？我们看提供的文本最后是：
> > 
> > 

<pre class="hljs"><code>[64] P.E. Bliichl, Phys. Rev. B 50 (1994) 17953.
</code></pre>


> > 
> > 所以参考文献列表也包括在内。我们需要处理整个文本。文本中有很多引用编号，如 [1], [2] 等，这些是引用标记，保留原样。
> > 
> > 我们开始解析结构。先识别出论文标题、作者、摘要、章节标题等。
> > 
> > 从开头到“Abstract”之前的部分是期刊信息、论文标题、作者、地址、收稿日期等。这些可以视为段落。然后“Abstract”是摘要部分。然后“1. Introduction”是一级标题，“1.1. General”是二级标题，“1.2. Outline of the paper”是二级标题。然后“2. The Kohn-Sham energy functional for partial occupancies”一级标题，“2.1. The Kohn-Sham energy functional”二级，“2.2. Metallic systems and partial occupancies”二级，下面还有三级标题如“2.2.1. Linear tetrahedron method”？我们看文本：
> > 
> > 

<pre class="hljs"><code>2.2. Metallic systems and partial occupancies
...
2.2.1. Linear tetrahedron method
...
2.2.2. Finite-temperature approaches - ‘smearing methods’
...
2.2.3. Improved functionalform for fle) - Method of Methfessel and Paxton
...
2.2.4. Convergence of the total energy with the number of k-points
...
2.2.5. Calculation of photwn frequencies for metals
...
</code></pre>


> > 
> > 所以是三级标题。然后“2.3. Selfconsistency loop and iterative methods”，“2.4. Forces”。然后“3. Iterative methods for the diagonalization of the KS-Hamiltonian”，下面有“3.1. Residual vector and preconditioning”，“3.2. Blocked Davidson scheme”，“3.3. Unblocked algorithms”，“3.4. Correction vector for sequential, band-by-band methods”，“3.5. Unblocked Davidson-like update”，“3.4. Conjugate gradient minimization”（注意这里编号可能错误，应该是3.6，但原文写的是3.4，可能是原始错误，我们保留），“3.7. Residual minimization method - direct inversion in the iterative subspace (RMM-DIN)”， “3.8. The complete algorithm”，“3.9. Computational considerations”。然后“4. Charge density mixing”，“4.1. Simple mixing”，“4.2. Pulay mixing”，“4.3. Broyden mixing”，“4.4. Preconditioning and metric”。然后“5. Direct minimization of the KS-functional”，“5.1. Preconditioned search direction”，“5.2. Steepest descent and conjugate gradient algorithm”，“5.3. Other direct minimization methods”。然后“6. Comparison of different techniques”，“6.1. Iterative matrix diagonalization”，“6.1.1. Liquid metallic system”，“6.1.2. Metallic surface”，“6.1.3. Diamond surface”， “6.2. Comparison for selfconsistent calculations”，“6.2.1. Liquid metallic system”，“6.2.2. Metallic su$ace”，“6.2.3. Diamond surface”。然后“7. Conclusion”。然后“Acknowledgements”， “Appendix A. Total derivatives of a constrained function”， “Appendix B. Forces within the linear tetrahedron method”， “References”。
> > 
> > 文本中还有几个表格？我们看到了“Table 1”， “Table 2”， “Table 3”等，这些是表格，我们需要识别并转换为Markdown表格。还有图，但图是描述，我们不需要处理图，只需处理文本中的表格。表格是以文本形式呈现的，我们需要提取。
> > 
> > 例如：
> > 
> > 

<pre class="hljs"><code>Table 1 Convenient settings for the smearing parameter o for different metals
u (eV)
Aluminium 1.0 Lithium 0.4 sc-Tellurium 0.8 Copper 0.4 Vanadium 0.3 Rhodium 0.3
</code></pre>


> > 
> > 这个表格看起来是两列，第一列是金属，第二列是σ (eV)。但是原文中写的是“u (eV)”，可能是“σ (eV)”。我们保留原文。需要转换为Markdown表格。
> > 
> > 还有“Table 2 Phonon frequencies for Rh at the K-point ...” 是一个复杂表格，有表头。还有“Table 3 Time necessary to do one iteration ...” 等。
> > 
> > 我们需要识别所有表格并转换为Markdown表格语法。
> > 
> > 另外，文本中有代码块吗？似乎没有明显的代码块，但有一些公式，可能用固定宽度，但提取的文本中公式没有保留。我们按原文处理。
> > 
> > 还有引用块？似乎没有引用块。
> > 
> > 文本中还有列表，例如摘要中的“(a) partial occupancies ... (b) iterative methods ...” 这是一个列表，但原文是用(a) (b) (c) (d) 引导的。我们可以将其视为列表。还有正文中可能有列表，如“We will discuss: (a) ...” 这可以视为一个句子内的列表，但我们可以将整个摘要部分作为段落，或者将其中的列表识别出来。但为了保持结构，我们可能将其保留在段落中，或者拆分为列表。但用户要求“判别列表类型（数字/符号引导）”，这里(a) (b)是字母引导，可以视为有序列表。但通常Markdown有序列表用数字，我们可以用数字1. 2. 3. 4. 表示。但原文是(a) (b) (c) (d)，我们可以保留为原始符号，因为用户说“保留原始符号类型”。原始符号是“_”或“1.”或“-”，但这里的(a)不是标准Markdown列表符号。我们可以将其视为段落，或者用无序列表，但更合适的是保留为原文，作为一个段落。我们仔细看用户要求：“列表项：保留原始符号类型（_ / 1. / -）”。但摘要中的(a)不是这些，可能不是列表，而是文本中的列举。我们可以在翻译时仍保留(a)等。或者我们将其转换为有序列表，用1. 2. 3. 4. 并标明原文。但为了忠实原文，我认为保持原文的(a)等作为段落内的文本即可。实际上，摘要中的这部分是：“We will discuss: (a) partial occupancies ... (b) iterative methods ... (c) efficient Broyden-like ... (d) conjugate gradient methods ...”。这是一个句子，我们可以作为段落处理。同样，正文中也有类似的列举，如“In general two different techniques can be distinguished: (i) Methods ... and (ii) iterative methods ...”，这也可以作为段落。
> > 
> > 我们再看是否有其他列表。在“2.2.3. Improved functionalform for fle) - Method of Methfessel and Paxton”中，有“The method described in the last section has two distinct shortcomings: . Forces are usually defined as ... . The parameter u has to be chosen ...”，这里有两个点，可能是无序列表。文本中显示为“. Forces are usually defined as ...” 和 “. The parameter u has to be chosen ...”，所以是无序列表。我们需要识别这些。
> > 
> > 还有在“2.3. Selfconsistency loop and iterative methods”中，有“Fig. 3 shows a typical flowchart for this situation: At the beginning an appropriate set of trial wavefunction ...”，这可能是步骤，但原文是段落。
> > 
> > 还有在“3.1. Residual vector and preconditioning”中，有公式，但公式是文本，我们保留原样。
> > 
> > 在“6.1.1. Liquid metallic system”中，有“We have found that . the CG algorithm is fastest ... . the RMM algorithm is superior ... . and the DAV2 scheme is always outperformed ...”，这也是无序列表。
> > 
> > 所以我们需要正确识别这些列表。列表项通常以“.”或“-”开头，但原文中可能以“.”开头。我们看文本：“We have found that . the CG algorithm is fastest for very small systems, where order N 3 operations are negligible; . the RMM algorithm is superior for large systems containing more than 20-30 atoms; . and the DAV2 scheme is always outperformed by one of the other two techniques.” 这里三个点，所以是无序列表。我们可以用“-”或“_”表示，但原文是“.”，我们可以保留为“.”，但Markdown标准无序列表通常用“-”或“_”。我们可以用“-”并保留原文的引导符号，但用户要求“保留原始符号类型”。可能我们需要在输出时使用原始符号，但为了符合CommonMark，我们可以用“-”表示无序列表，并在原文中保留“.”。但用户说“列表项：保留原始符号类型（* / 1. / -）”，所以如果原文是“.”，可能不是标准符号，但我们可以将其视为“-”类。我们将在输出时，原文部分保留原始符号，中文翻译部分也保留同样的符号，但在Markdown中，无序列表通常用“-”或“*”，我们可以用“-”作为列表标记，但原文中的“.”我们可以保留在文本中，或者直接使用“-”替换。为了简单，我们可以用“-”作为无序列表标记，因为原文的“.”在视觉上也是列表符号。但为了忠实，我们可以在英文原文中保留“.”，在中文翻译中也用“.”。但Markdown渲染时，点号可能不会被识别为列表。所以最佳做法是，将这种列表识别为无序列表，并在输出时使用“-”作为列表标记，但将原文的“.”作为列表项内容的一部分。例如：
> > 
> > -   . the CG algorithm is fastest ...
> > 
> > 这样可能不美观。我们可以直接使用“-”并省略原文的点号，但这样会改变原文。用户要求“保留原始格式”，原文是“. ...”，所以我们应该保留。但Markdown中，如果一行以“.”开头，可能不会被视为列表，而是普通段落。所以我们可以将原文的列表项前加上“-”并保留原文的点号，或者直接使用“-”替换点号。我倾向于使用“-”并保留原文内容，但在英文原文中，将“. ”替换为“- ”以符合Markdown列表语法，同时保留原文的文本。但用户要求“保留原始符号类型”，如果是“.”，我们可能应该保留。但用户给的例子中符号类型是“* / 1. / -”，不包括“.”，所以可能“.”不是列表，而是普通文本。然而，从上下文看，这明显是列表。我们再看一下有没有其他列表。在“2.2.2. Finite-temperature approaches - ‘smearing methods’”中，有“the free energy deviates quadratically with σ from E_{σ=0} [38]”不是列表。在“6.1.1. Liquid metallic system”中的列表，原文是：“We have found that . the CG algorithm is fastest ... . the RMM algorithm is superior ... . and the DAV2 scheme is always outperformed ...”。这可能是列表，但原文可能是在“We have found that”之后用点号分隔。我们可以将其视为一个句子，而不是列表。但为了清晰，我们可以作为无序列表。
> > 
> > 在“6.1.2. Metallic surface”中，也有类似：“We have found that . the CG algorithm is fastest ... . the RMM algorithm is superior ... . and the DAV2 scheme is always outperformed ...”，但这里没有。实际上，在6.1.1末尾有一段总结：“Summarizing the results of the last three sections: We have found that . the CG algorithm is fastest for very small systems, where order N 3 operations are negligible; . the RMM algorithm is superior for large systems containing more than 20-30 atoms; . and the DAV2 scheme is always outperformed by one of the other two techniques.” 这是列表。我们将其处理为无序列表。
> > 
> > 另外，在“2.2.2”中，有“The method described in the last section has two distinct shortcomings: . Forces are usually defined as the derivatives of the . variational quantity, i.e. the free electronic energy F ... . The parameter u has to be chosen with great care ...” 这里也是列表。我们识别为无序列表。
> > 
> > 还有“2.2.3”中，有“These problems can be solved by adopting a slightly different functional form for f({e}), which was first proposed by Methfessel and Paxton (MP) [38].” 不是列表。
> > 
> > 此外，文本中有一些公式，如“F = E - Σ θ S(f_n)”等，我们保留原样。
> > 
> > 现在，我们需要逐块处理。我们将整个文本拆分为多个单元，每个单元包括标题、段落、列表、表格等。然后为每个单元提供英文原文和中文翻译，并在首次出现的术语后添加解释。
> > 
> > 由于输出要求“无额外说明性内容（仅输出Markdown文本）”，我们最终输出纯Markdown。
> > 
> > 我们开始构建输出。注意，原文开头的期刊信息、标题、作者等，我们可以作为元数据，但可以放在一个段落中。标题“Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set”是论文标题，我们可以用一级标题 `#` 表示。但整个文档我们可能从“# [英文标题]”开始。但用户给的例子中，标题格式是“# [英文标题] [中文标题] **Term**: 术语解释”。所以我们可以把论文标题作为一级标题。
> > 
> > 然后作者、地址等，可以作为一个段落。摘要“Abstract”作为二级标题，然后摘要内容作为段落。但摘要中可能有列表，我们保留为段落。
> > 
> > 我们逐步解析。
> > 
> > 首先，期刊行：“ELSEVIER Computational Materials Science 6 (1996) 15-50” 和 “COMPUTATIONAL MATERIALS SCIENCE” 可能是期刊名，但与标题重复，我们可以保留为文本，作为段落，但可能不需要。为了完整，我们保留，作为文本块。
> > 
> > 然后论文标题：“Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set”，我们作为一级标题。
> > 
> > 作者：“G. Kresse a ,vJ*. Furthmiiller b” 等，地址，收稿日期，作为段落。
> > 
> > 然后“Abstract”作为二级标题。
> > 
> > 摘要内容作为段落。
> > 
> > 然后“1. Introduction”一级标题，“1.1. General”二级标题，等等。
> > 
> > 按照这样的结构，我们为每个标题和内容创建单元。
> > 
> > 我们还需要识别表格。Table 1, Table 2, Table 3。我们将它们转换为Markdown表格。
> > 
> > Table 1: 两列，表头：“u (eV)” 但实际应该是“σ (eV)”，但保留原文。表头是“u (eV)”，下面数据行。我们写成：
> > 
> > 

<table>
<thead>
<tr>
<th>Metal</th>
<th>u (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Aluminium</td>
<td>1.0</td>
</tr>
<tr>
<td>Lithium</td>
<td>0.4</td>
</tr>
<tr>
<td>sc-Tellurium</td>
<td>0.8</td>
</tr>
<tr>
<td>Copper</td>
<td>0.4</td>
</tr>
<tr>
<td>Vanadium</td>
<td>0.3</td>
</tr>
<tr>
<td>Rhodium</td>
<td>0.3</td>
</tr>
</tbody>
</table>


> > 
> > 注意，原文中“sc-Tellurium”可能有错，但保留。
> > 
> > Table 2: 比较复杂。原文：
> > 
> > 

<pre class="hljs"><code>Table 2 Phonon frequencies for Rh at the K-point (i.e. in (I Ii) direction, Brillouin zone boundary) calculated using a frozen-phonon approach
f 0Hz) Energy MP Force MP Energy LT-C Force LT-C Energy LT Force LT
III trans. 4.29 4.28 4.30 4.10 3.91 3.93 I 1I long 7.95 7.96 7.93 7.68 7.46 7.49
</code></pre>


> > 
> > 表头似乎是：第一列是模式，然后有“Energy MP”, “Force MP”, “Energy LT-C”, “Force LT-C”, “Energy LT”, “Force LT”。但第一行是“f 0Hz)”可能是“f (THz)”？原文是“f 0Hz)”，可能是“f (THz)”。我们保留原文。我们将其转换为表格：
> > 
> > 

<table>
<thead>
<tr>
<th>f (THz)</th>
<th>Energy MP</th>
<th>Force MP</th>
<th>Energy LT-C</th>
<th>Force LT-C</th>
<th>Energy LT</th>
<th>Force LT</th>
</tr>
</thead>
<tbody>
<tr>
<td>III trans.</td>
<td>4.29</td>
<td>4.28</td>
<td>4.30</td>
<td>4.10</td>
<td>3.91</td>
<td>3.93</td>
</tr>
<tr>
<td>I 1I long</td>
<td>7.95</td>
<td>7.96</td>
<td>7.93</td>
<td>7.68</td>
<td>7.46</td>
<td>7.49</td>
</tr>
</tbody>
</table>


> > 
> > 注意，原文中“III trans.”和“I 1I long”可能是“III trans.”和“I 1I long”，但“I 1I”可能是“I II”即“I II long”。我们保留原文。
> > 
> > Table 3:
> > 
> > 

<pre class="hljs"><code>Table 3 Time necessary to do one iteration for a I-Ge ensemble containing 64 atoms for several algorithms on an IBM RS 6OCO/Model590
DAV2 CG sequent. RMM sequent. CGa- 148 SDa-148 CGa-128 SDa- 128
Complex
180s = 155s = 102 s 91 s 64 s 65 s 50 s
Real
= 70 s = 42 s 37 s 30 s 29 s
23s
</code></pre>


> > 
> > 表头：第一列是类型，然后“DAV2”, “CG sequent.”, “RMM sequent.”, “CGa- 148”, “SDa-148”, “CGa-128”, “SDa- 128”。数据行有“Complex”和“Real”。我们转换为表格：
> > 
> > 

<table>
<thead>
<tr>
<th>Timing</th>
<th>DAV2</th>
<th>CG sequent.</th>
<th>RMM sequent.</th>
<th>CGa-148</th>
<th>SDa-148</th>
<th>CGa-128</th>
<th>SDa-128</th>
</tr>
</thead>
<tbody>
<tr>
<td>Complex</td>
<td>180s</td>
<td>= 155s = 102 s</td>
<td>91 s</td>
<td>64 s</td>
<td>65 s</td>
<td>50 s</td>
<td>?</td>
</tr>
<tr>
<td>其实原文有点乱：“Complex\n180s = 155s = 102 s 91 s 64 s 65 s 50 s” 可能意思是：Complex: 180s, = 155s, = 102 s, 91 s, 64 s, 65 s, 50 s。但“= 155s = 102 s”可能是“CG sequent.”对应“= 155s = 102 s”？可能是“CG sequent.”的两次时间？我们看原文描述，Table 3标题是“Time necessary to do one iteration for a I-Ge ensemble containing 64 atoms for several algorithms on an IBM RS 6OCO/Model590”，表格中“DAV2”下“180s”， “CG sequent.”下“= 155s = 102 s”， “RMM sequent.”下“91 s”， “CGa- 148”下“64 s”， “SDa-148”下“65 s”， “CGa-128”下“50 s”， “SDa- 128”下“23s”？但“Real”行有“= 70 s = 42 s 37 s 30 s 29 s 23s”。可能“Real”行对应相同列。我们尽量保留原文。可以这样写：</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

 

<table>
<thead>
<tr>
<th></th>
<th>DAV2</th>
<th>CG sequent.</th>
<th>RMM sequent.</th>
<th>CGa-148</th>
<th>SDa-148</th>
<th>CGa-128</th>
<th>SDa-128</th>
</tr>
</thead>
<tbody>
<tr>
<td>Complex</td>
<td>180s</td>
<td>= 155s = 102 s</td>
<td>91 s</td>
<td>64 s</td>
<td>65 s</td>
<td>50 s</td>
<td>-</td>
</tr>
<tr>
<td>Real</td>
<td>-</td>
<td>= 70 s = 42 s</td>
<td>37 s</td>
<td>30 s</td>
<td>29 s</td>
<td>-</td>
<td>23s</td>
</tr>
</tbody>
</table>


> > 
> > 但原文中“Complex”行最后“SDa- 128”没有值， “Real”行“DAV2”没有值。我们按原文保留。可能表格本该是两行，但格式混乱。我们尽量保留原始文本，在Markdown表格中如实填写。注意，有些单元格有“= 155s = 102 s”，这可能表示两种不同实现的时间。我们保留。
> > 
> > 现在，我们逐个单元输出。我们将为每个单元分配ID，但输出中不显示ID，仅用于内部。我们直接输出Markdown格式。
> > 
> > 注意术语解释：首次出现的核心术语，如“ab-initio”、“pseudopotentials”、“plane-wave basis set”、“linear tetrahedron method”、“density-functional theory”、“Kohn-Sham Hamiltonian”、“Broyden-like”、“Pulay-like”、“conjugate gradient”、“VAMP”、“Hellmann-Feynman theorem”、“Car-Parrinello”、“ultrasoft pseudopotential”、“Harris-Foulkes functional”、“residual vector”、“preconditioning”、“Davidson scheme”、“conjugate gradient minimization”、“residual minimization method direct inversion in the iterative subspace (RMM-DIIS)”、“Broyden mixing”、“Pulay mixing”、“Kerker mixing”等。我们将在首次出现时添加解释。
> > 
> > 另外，中文翻译要准确，符合技术文档风格。
> > 
> > 我们开始编写输出。注意，文本很长，我们需完整输出。由于篇幅，我会在回答中输出完整Markdown。
> 
> # Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set
> 
> 基于平面波基组的金属与半导体从头算总能量计算效率研究
> 
> **ab-initio**: 从头算，即不依赖经验参数、仅从基本物理定律出发的计算方法。  
> **plane-wave basis set**: 平面波基组，用平面波函数展开波函数的基函数集合。
> 
> G. Kresse a ,vJ*. Furthmiiller b  
> ’ Institut für Theoretische Physik, Technische Universität Wien, Wiedner Hauptstraße 8-10, A-1040 Wien, Austria  
> b Institut für Festkörpertheorie und Theoretische Optik, Friedrich-Schiller-Universität Jena, Max-Wien-Platz 1, D-07743 Jena, Germany  
> G. Kresse a,*, J. Furthmüller b  
> a 维也纳工业大学理论物理研究所，奥地利维也纳 A-1040，Wiedner Hauptstraße 8-10  
> b 耶拿弗里德里希·席勒大学固体物理与理论光学研究所，德国耶拿 D-07743，Max-Wien-Platz 1
> 
> Received 4 February 1996; accepted 15 March 1996  
> 收稿日期：1996年2月4日；接受日期：1996年3月15日
> 
> Abstract 摘要
> 
> We present a detailed description and comparison of algorithms for performing ab-initio quantum-mechanical calculations using pseudopotentials and a plane-wave basis set. We will discuss: (a) partial occupancies within the framework of the linear tetrahedron method and the finite temperature density-functional theory, (b) iterative methods for the diagonalization of the Kohn-Sham Hamiltonian and a discussion of an efficient iterative method based on the ideas of Pulay’s residual minimization, which is close to an order N at scaling even for relatively large systems, (c) efficient Broyden-like and Pulay-like mixing methods for the charge density including a new special ‘preconditioning’ optimized for a plane-wave basis set, (d) conjugate gradient methods for minimizing the electronic free energy with respect to all degrees of freedom simultaneously. We have implemented these algorithms within a powerful package called VAMP (Vienna ab-initio molecular-dynamics package). The program and the techniques have been used successfully for a large number of different systems (liquid and amorphous semiconductors, liquid simple and transition metals, metallic and semi-conducting surfaces, phonons in simple metals, transition metals and semiconductors) and turned out to be very reliable. 我们详细描述并比较了使用赝势和平面波基组进行从头算量子力学计算的算法。我们将讨论：(a) 线性四面体方法和有限温度密度泛函理论框架下的部分占据数，(b) Kohn-Sham哈密顿量对角化的迭代方法，以及一种基于Pulay残差最小化思想的高效迭代方法，该方法即使在相对较大的体系中也近似具有O(N³)标度，(c) 高效的类Broyden和类Pulay电荷密度混合方法，包括一种针对平面波基组优化的新型特殊“预条件”，(d) 同时对所有自由度进行电子自由能最小化的共轭梯度方法。我们已将这些算法实现于一个名为VAMP（维也纳从头算分子动力学程序包）的强大软件包中。该程序和技术已成功应用于大量不同体系（液态和非晶半导体、液态简单金属和过渡金属、金属和半导体表面、简单金属、过渡金属和半导体中的声子），并证明非常可靠。
> 
> **pseudopotentials**: 赝势，一种用于简化原子核与电子相互作用计算的有效势。  
> **linear tetrahedron method**: 线性四面体方法，在布里渊区积分中通过四面体插值计算占据数和能量的一种方法。  
> **density-functional theory**: 密度泛函理论，一种以电子密度为基本变量求解多电子体系量子力学性质的理论。  
> **Kohn-Sham Hamiltonian**: Kohn-Sham哈密顿量，密度泛函理论中描述无相互作用电子体系的等效单电子哈密顿量。  
> **Broyden-like**: 类Broyden（方法），一种拟牛顿迭代法，用于求解非线性方程或优化问题。  
> **Pulay-like**: 类Pulay（方法），一种利用残差最小化进行迭代加速的方法，常用于电荷密度混合。  
> **conjugate gradient**: 共轭梯度，一种迭代优化算法，通过构建共轭方向进行高效搜索。  
> **VAMP**: 维也纳从头算分子动力学程序包，本文作者开发的用于从头算电子结构计算的软件。
> 
> 1.  Introduction
> 2.  引言
> 
> 1.1. General 1.1. 概述
> 
> In recent years, ab-initio calculations have made a profound impact on the investigation of material properties. The main reason for the enormous success of ab-initio methods lies in the fact that they are parameter-free and require no other input than the atomic number. In addition, improvements in computer performance and algorithms allow to apply these methods to a steadily increasing number of physical and chemical phenomena. Probably, the most successful method currently tractable is the local density functional (LDF) theory proposed by Kohn and Sham [1]. In conjunction with the Hellmann-Feynman theorem [2] forces can be evaluated easily, allowing the simultaneous investigation of structural, electronic and dynamic properties. The first successful ab initio calculation in this context goes back to a seminal paper written by Car and Parrinello (CP) [3]. In their work Car and Parrinello proposed a simulated annealing approach in which electrons and ions are treated on the same footing via a Quasi-Newton equation of motion. This approach allows for an efficient simultaneous update of electrons and ions, but also possesses some serious restrictions: The time step for the CP technique is limited by the requirement that the electrons are always close to the exact electronic groundstate. Indeed, it can be shown that this is only the case if the typical excitation frequencies of the electronic subsystem are much higher than that of the ionic system [4] (in this case electrons and ions decouple adiabatically, and the electrons oscillate around the real electronic groundstate). This also implies that the time step in a CP simulation is determined by the electronic degrees of freedom, and usually the time step is an order of magnitude smaller than that necessary to simulate the ionic subsystem. A straightforward alternative to the simultaneous update of electrons and ions is the exact calculation of the electronic groundstate after each ionic move. This is possible if the algorithms for calculating the electronic groundstate are sufficiently efficient. Recently several approaches have been proposed and most of these methods differ significantly from the standard original CP implementation, except for one aspect: For a plane-wave basis set, CP introduced an efficient way to calculate the action of the Hamiltonian onto the electronic wavefunctions. They used the fact that the local potential part of the Hamiltonian is diagonal in real space and that the kinetic energy part of the Hamiltonian is diagonal in reciprocal space. Therefore, the evaluation of the action of the Hamiltonian is very fast if the wavefunctions are transformed from reciprocal to real space and backwards using fast Fourier transformations. In addition, it is easy to evaluate the nonlocal part of the Hamiltonian using separable factorized pseudopotentials [5]. These features make all ‘iterative’ algorithms for calculating the electronic groundstate tremendously more efficient than the previously used schemes based on an exact diagonalization of the Kohn-Sham (KS) Hamiltonian. Here, the term ‘iterative’ refers to any technique requiring the repeated evaluation of the action of the Hamiltonian onto the wavefunctions as a key step. In general two different techniques can be distinguished: (i) Methods for determining the minimum of the KS energy functional directly (in the future simply called direct methods); and (ii) iterative methods for the diagonalization of the KS-Hamiltonian in conjunction with an iterative improvement (i.e. mixing) of the charge density (we will refer to these methods as selfconsistency cycle (SC) methods). The direct methods (i) have been pioneered by CP. They are based on the fact that the Kohn-Sham energy functional is minimal at the electronic groundstate. Therefore, minimization of the functional with respect to the variational degrees of freedom leads to a convenient scheme for calculating the electronic groundstate. The only problem to be solved is the inclusion of the orthonormality constraint on the wavefunctions, which is done with a Lagrange formalism in the original method of CP. Generally the standard CP algorithm is relatively slow if it is applied to the electrons only. Small improvements might be obtained by integrating the equations of motions analytically [6], or by introducing an improved pre-conditioning for the gradient [7]. In addition it is possible to replace the second order CP equations by a first-order steepest descent [8,9] equation. Nevertheless, recently Tassone, Mauri and Car [7] showed that a preconditioned damped second order equation of motion for the electrons is generally more efficient than this first-order steepest descent equation. Even more promising than CP like techniques are conjugate gradient (CG) schemes. Within these schemes it is necessary to minimize the KS functional along a given search direction exactly (which is usually not done within the CP like techniques), and in successive steps the new search direction is conjugated to previous directions. The main problem within the CG methods is that the orthonormality constraint is not easy to incorporate. For semiconductors and insulators Teter, Payne and Allan proposed a reliable algorithm which optimizes the electronic energy in a band-by-band fashion [10]. In their algorithm the total energy is minimized for a single orbital within the sub-space orthonormal to the current set of trial wavefunctions. Despite the advantage of small storage requirements, the algorithm is relatively slow because only a limited number of CG steps per orbital can be done, and because the charge density and the potential must be recalculated after each single update of each orbital. Therefore, algorithms which update all orbitals simultaneously should be superior. These algorithms were pioneered independently by Stich, Car, Parrinello and Baroni [11] and by Gillan [12]. The most systematic and elegant way to incorporate the orthogonality constraint in this case is to generalize the KS functional for nonorthogonal orbitals [13]. The results of this paper indicate that the direct methods (i) discussed up to now are in general not as efficient as the traditional SC-methods (ii) which are based on the repeated diagonalization of the KS Hamiltonian and a charge density mixing. This is especially true for metallic systems. At first sight this is a clear contradiction to the mathematical crudeness of the SC-methods, considering that the selfconsistent minimization of the KS functional is replaced by an independent improvement of the eigenfunctions and the charge density. But the reason for this behavior might lie in the following points: First, iterative methods for the diagonalization of the KS Hamiltonian are easier to implement and more mature than methods for minimizing the total energy selfconsistently. Second, and more important: methods for an iterative improvement (i.e. mixing) of the charge density can retain information from all previous mixing steps. This is an important difference to all direct schemes which take into account only information from one or two previous steps. In principle CG methods should overcome this shortcoming by creating a set of conjugated directions, but the speed of a CG method is always limited by the accuracy of the minimization into the search direction, which becomes especially cumbersome for metallic systems, and slows down the net convergence. We have applied the SC-technique successfully to several different systems including liquid simple metals (Na, Ge) [14], liquid transition metals (V, Cu) [15,16], the transition from a liquid metal to an amorphous semiconductor by the rapid quenching of Ge [17,16], and the metal non-metal transition in I-Hg [18]. One advantage of an efficient electronic minimization is that the relaxation of the ions to their instantaneous equilibrium position is much faster. Successful calculations for clean and hydrogenated C(100) surfaces [19], the site-selective adsorption of C-atoms on Al(111) surfaces [20] and Rh surface properties [21] demonstrate the feasibility of our method in this respect. Finally, we have also performed calculations of bulk-phonons in insulators and metals (cubic diamond and graphite see Ref. [22]), indicating that forces can be evaluated efficiently and accurately within the SC methods. 近年来，从头算方法对材料性质的研究产生了深远影响。从头算方法取得巨大成功的主要原因在于它们是无参数的，且除了原子序数外无需其他输入。此外，计算机性能的改进和算法的发展使得这些方法能够应用于越来越多的物理和化学现象。目前可用的最成功方法可能是Kohn和Sham提出的局域密度泛函理论（LDF）[1]。结合Hellmann-Feynman定理[2]，可以容易地计算力，从而允许同时研究结构、电子和动力学性质。在这一背景下，第一个成功的从头算计算可追溯到Car和Parrinello（CP）的开创性论文[3]。在他们的工作中，Car和Parrinello提出了一种模拟退火方法，其中电子和离子通过准牛顿运动方程被同等对待。这种方法允许电子和离子的有效同时更新，但也存在一些严重限制：CP技术的时间步长受限于电子必须始终接近精确的电子基态。事实上，可以证明只有当电子子系统的典型激发频率远高于离子子系统的频率时，这种情况才成立[4]（此时电子和离子绝热退耦，电子围绕真实的电子基态振荡）。这也意味着CP模拟中的时间步长由电子自由度决定，通常时间步长比模拟离子子系统所需的时间步长小一个数量级。对电子和离子同时更新的一个直接替代方案是在每次离子移动后精确计算电子基态。如果计算电子基态的算法足够高效，这是可能的。最近已提出几种方法，其中大多数方法与标准的原始CP实现有显著差异，除了一个方面：对于平面波基组，CP引入了一种高效计算哈密顿量作用于电子波函数的方法。他们利用哈密顿量的局域势部分在实空间对角，而动能部分在倒空间对角的事实。因此，如果使用快速傅里叶变换将波函数从倒空间变换到实空间并返回，则哈密顿量作用的计算非常快。此外，使用可分离因式化赝势[5]很容易计算哈密顿量的非局域部分。这些特性使得所有计算电子基态的“迭代”算法比之前基于精确对角化Kohn-Sham（KS）哈密顿量的方案效率高得多。这里，“迭代”指任何需要反复计算哈密顿量作用于波函数作为关键步骤的技术。通常可以区分两种不同的技术：(i) 直接确定KS能量泛函最小值的方法（以后简称为直接方法）；以及 (ii) 结合电荷密度迭代改进（即混合）的KS哈密顿量对角化迭代方法（我们将这些方法称为自洽循环（SC）方法）。直接方法(i)由CP开创。它们基于Kohn-Sham能量泛函在电子基态处为最小值的事实。因此，对变分自由度进行泛函最小化，可以得到计算电子基态的方便方案。唯一需要解决的问题是纳入波函数的正交归一约束，在CP的原始方法中通过拉格朗日形式处理。通常，标准的CP算法在仅应用于电子时相对较慢。通过解析积分运动方程[6]或引入改进的梯度预条件[7]可能获得小的改进。此外，可以用一阶最陡下降方程[8,9]替换二阶CP方程。然而，最近Tassone、Mauri和Car [7]表明，预条件阻尼的二阶电子运动方程通常比这种一阶最陡下降方程更高效。比类CP技术更有前景的是共轭梯度（CG）方案。在这些方案中，需要沿给定搜索方向精确最小化KS泛函（这在类CP技术中通常未做），并在后续步骤中将新搜索方向与之前方向共轭。CG方法的主要问题在于正交归一约束不易纳入。对于半导体和绝缘体，Teter、Payne和Allan提出了一种可靠的算法，以逐带方式优化电子能量[10]。在他们的算法中，在与当前试探波函数组正交的子空间内对单个轨道进行总能量最小化。尽管存储需求小，但该算法相对较慢，因为每个轨道只能进行有限数量的CG步骤，且每次更新每个轨道后必须重新计算电荷密度和势。因此，同时更新所有轨道的算法应更优越。这些算法由Stich、Car、Parrinello和Baroni [11]以及Gillan [12]独立开创。在此情况下纳入正交约束的最系统、最优雅的方法是将KS泛函推广到非正交轨道[13]。本文的结果表明，迄今为止讨论的直接方法(i)通常不如基于反复对角化KS哈密顿量和电荷密度混合的传统SC方法(ii)高效。对于金属体系尤其如此。乍一看，这与SC方法数学上的粗糙性明显矛盾，考虑到自洽最小化KS泛函被本征函数和电荷密度的独立改进所取代。但这种行为的原因可能在于以下几点：首先，用于KS哈密顿量对角化的迭代方法比自洽最小化总能量的方法更易实现且更成熟。其次，更重要的是：电荷密度迭代改进（即混合）方法可以保留所有之前混合步骤的信息。这与所有仅考虑前一步或两步信息的直接方案有重要区别。原则上，CG方法应通过创建一组共轭方向来克服这一缺陷，但CG方法的速度始终受限于沿搜索方向最小化的精度，这对金属体系尤其麻烦，并减缓了净收敛速度。我们已成功将SC技术应用于几种不同体系，包括液态简单金属（Na、Ge）[14]、液态过渡金属（V、Cu）[15,16]、通过快速淬火Ge从液态金属到非晶半导体的转变[17,16]，以及I-Hg中的金属-非金属转变[18]。高效电子最小化的一个优势是离子弛豫到其瞬时平衡位置的速度快得多。对清洁和氢化C(100)表面[19]、C原子在Al(111)表面的位点选择性吸附[20]以及Rh表面性质[21]的成功计算证明了我们方法在这方面的可行性。最后，我们还对绝缘体和金属中的体声子（立方金刚石和石墨，见参考文献[22]）进行了计算，表明在SC方法中可以高效、准确地计算力。
> 
> **Hellmann-Feynman theorem**: 赫尔曼-费曼定理，将力表示为能量对原子位置的导数，可用于计算原子受力。  
> **Car-Parrinello (CP)**: 卡-帕里内洛方法，一种同时处理电子和离子运动的从头算分子动力学方法。  
> **selfconsistency cycle (SC)**: 自洽循环，通过迭代求解KS方程并将电荷密度混合直至收敛的方法。  
> **conjugate gradient (CG)**: 共轭梯度法，一种通过构建共轭搜索方向进行高效优化的迭代算法。
> 
> 1.2. Outline of the paper 1.2. 论文概要
> 
> In this paper we will mainly concentrate on methods based on the repeated diagonalization of the KS-Hamiltonian and a charge density mixing (SC-methods). After a general introduction of the Kohn-Sham energy functional (Section 2.1) the impact of partial occupancies on the Kohn-Sham functional will be explained (Section 2.2). The discussion includes newest improvements of the tetrahedron method as well as a comparison of the tetrahedron method with finite temperature methods. Section 2.3 contains a broad outline of the steps involved in methods relying on the selfconsistency cycle, followed by a brief explanation of the Hellmann-Feynman force theorem (Section 2.4). Some important technical details for the calculation of forces are pointed out. An in-depth discussion and comparison of several iterative matrix diagonalization schemes is given in Section 3. The ideas discussed in Section 3 have partly been published in different papers by different authors - but to our knowledge this is the first consistent review. In addition technical aspects which are important for an actual implementation will be explained. We also review an efficient iterative matrix diagonalization scheme based on the ideas of residual vector minimization (direct inversion of iterative subspace). This scheme will outperform any other iterative matrix diagonalization scheme for very large matrices. The second main ingredient of our scheme is the charge density mixing discussed in Section 4. We will concentrate on Broyden mixing [23] (especially Broyden’s second method or inverse Jacobian update) and a mixing method proposed by Pulay [24]. A close relationship between both methods will be pointed out, and a special metric optimized for a plane-wave basis set will be introduced. Finally, we have also included a section, which discusses methods to determine the minimum of the KS energy functional directly (Section 5). Special attention will be given to the conjugate gradient method. In Section 6 a comparison between different methods is given. We have divided this section into a part which compares the non-selfconsistent case (i.e. iterative matrix diagonalization only, Section 6.1) and a part which concentrates on mixing and on the direct methods (Section 6.2). 本文将主要集中于基于反复对角化KS哈密顿量和电荷密度混合的方法（SC方法）。在介绍Kohn-Sham能量泛函（第2.1节）之后，将解释部分占据数对Kohn-Sham泛函的影响（第2.2节）。讨论包括四面体方法的最新改进以及四面体方法与有限温度方法的比较。第2.3节给出了依赖自洽循环的方法所涉及步骤的概述，随后简要解释了Hellmann-Feynman力定理（第2.4节）。指出了计算力的一些重要技术细节。第3节深入讨论并比较了几种迭代矩阵对角化方案。第3节中讨论的思想部分已由不同作者在不同论文中发表——但据我们所知，这是第一篇连贯的综述。此外，还将解释对实际实现重要的技术方面。我们还回顾了一种基于残差向量最小化（迭代子空间直接反演）思想的高效迭代矩阵对角化方案。对于非常大的矩阵，该方案将优于任何其他迭代矩阵对角化方案。我们方案的第二个主要组成部分是第4节讨论的电荷密度混合。我们将集中于Broyden混合[23]（特别是Broyden第二方法或逆雅可比更新）和Pulay提出的混合方法[24]。将指出两种方法之间的密切关系，并引入一种针对平面波基组优化的特殊度量。最后，我们还包含了一节，讨论直接确定KS能量泛函最小值的方法（第5节）。将特别关注共轭梯度方法。第6节给出了不同方法之间的比较。我们将本节分为两部分：一部分比较非自洽情况（即仅迭代矩阵对角化，第6.1节），另一部分集中于混合和直接方法（第6.2节）。
> 
> 2.  The Kohn-Sham energy functional for partial occupancies
> 3.  部分占据数的Kohn-Sham能量泛函
> 
> 2.1. The Kohn-Sham energy functional 2.1. Kohn-Sham能量泛函
> 
> In general the Kohn-Sham energy functional for an ultrasoft (US) Vanderbilt pseudopotential (PP) can be written as [25-27] 一般而言，对于超软（US）Vanderbilt赝势（PP），Kohn-Sham能量泛函可写为[25-27]
> 
> **ultrasoft (US) Vanderbilt pseudopotential**: 超软范德比尔特赝势，一种能大幅降低截断能要求的赝势形式。
> 
> EKS[{φ},{R}] = Σn fn⟨φn|T + Veff|φn⟩ + EH[ρ] + EXC[ρ] + ∫ d3r Veff(r)ρ(r) + γEwald EKS[{φ},{R}] = Σn fn⟨φn|T + Veff|φn⟩ + EH[ρ] + EXC[ρ] + ∫ d3r Veff(r)ρ(r) + γEwald
> 
> with fn = 1 for occupied bands and fn = 0 for unoccupied bands. To simplify the notation we have dropped the k-point index. The first sum runs over all bands Nb included in the calculation. The KS functional depends on the positions RI of the ions and the electronic wavefunctions φn only. EH is the Hartree-energy, EXC the exchange correlation energy functional, Veff the local ionic pseudopotential, T = -ħ2/2me∇2 the kinetic energy operator and γEwald the Madelung energy of the ions. For US PP the nonlocal part of the PP can be written as 其中占据带 fn = 1，非占据带 fn = 0。为简化符号，我们省略了k点指标。第一个求和遍历计算中包含的所有Nb个能带。KS泛函仅依赖于离子位置RI和电子波函数φn。EH是Hartree能，EXC是交换关联能泛函，Veff是局域离子赝势，T = -ħ2/2me∇2是动能算符，γEwald是离子的马德隆能。对于US PP，PP的非局域部分可写为
> 
> VNL = Σij Dij |βi⟩⟨βj| VNL = Σij Dij |βi⟩⟨βj|
> 
> and the charge density ρ(r) is given by 且电荷密度ρ(r)由下式给出
> 
> ρ(r) = Σn fn |φn(r)|2 + Σn,ij fn ⟨φn|βi⟩⟨βj|φn⟩ Qij(r) ρ(r) = Σn fn |φn(r)|2 + Σn,ij fn ⟨φn|βi⟩⟨βj|φn⟩ Qij(r)
> 
> where βi are localized projection states, and Qij(r) localized augmentation functions. The total energy has to be minimized subject to the constraint of orthonormalization 其中βi是局域投影态，Qij(r)是局域增广函数。总能量必须在正交归一约束下最小化
> 
> ⟨φn|S|φm⟩ = δnm ⟨φn|S|φm⟩ = δnm
> 
> where S is defined as 其中S定义为
> 
> S = 1 + Σij qij |βi⟩⟨βj|, S = 1 + Σij qij |βi⟩⟨βj|,
> 
> with 其中
> 
> qij = ∫ Qij(r) d3r. qij = ∫ Qij(r) d3r.
> 
> Ultrasoft pseudopotentials are discussed in detail in Ref. [25-28]. Their general advantage is that they reduce the necessary energy cutoff for transition metals and first row elements by a factor of 2-4. The resulting basis sets are comparable in size with the basis sets for typical ‘pseudopotential’ elements like Na, Al, Si and Ge. The most important property of the KS functional is to be extremal in the ground-state with respect to arbitrary variations of the wavefunctions. Under the constraint of orthonormalization, variation with respect to the wavefunctions leads to the well known KS eigenvalue equations 超软赝势在文献[25-28]中有详细讨论。其一般优势在于将过渡金属和第一周期元素所需的截断能降低2-4倍。得到的基组大小与Na、Al、Si和Ge等典型“赝势”元素的基组相当。KS泛函最重要的性质是在基态关于波函数任意变分取极值。在正交归一约束下，对波函数变分导出著名的KS本征值方程
> 
> H|φn⟩ = εnS|φn⟩, H|φn⟩ = εnS|φn⟩,
> 
> where H is the Kohn-Sham Hamiltonian 其中H是Kohn-Sham哈密顿量
> 
> H = T + Veff + VNL, H = T + Veff + VNL,
> 
> with 其中
> 
> Veff = Vloc + VH[ρ] + VXC[ρ], Veff = Vloc + VH[ρ] + VXC[ρ],
> 
> where VH[ρ] is the Hartree potential and VXC[ρ] the exchange-correlation potential. For ultrasoft pseudopotentials the nonlocal part of the pseudopotential depends also on the total local potential and must be calculated accordingly via (compare Eq. (2)) 其中VH[ρ]是Hartree势，VXC[ρ]是交换关联势。对于超软赝势，赝势的非局域部分也依赖于总局域势，必须按如下方式计算（比较式(2)）
> 
> Dijeff = Dijion + ∫ Qij(r) Veff d3r. Dijeff = Dijion + ∫ Qij(r) Veff d3r.
> 
> From inspection it is clear that only occupied orbitals contribute to the total energy, and it can be shown that the total energy is invariant under an unitary transformation of the wavefunctions φn if only occupied bands are taken into account (compare with Section 5). In this case it is sufficient to calculate a set of wavefunctions which fulfill the less stringent equation 通过观察可知，只有占据轨道对总能量有贡献，并且可以证明，如果仅考虑占据带，则总能量在波函数φn的幺正变换下是不变的（比较第5节）。在这种情况下，只需计算一组满足较宽松方程的波函数
> 
> H|φn⟩ = Σm γnmS|φm⟩, H|φn⟩ = Σm γnmS|φm⟩,
> 
> where γnm is an Hermitian matrix. If partial occupancies are included, i.e. if the fn are treated as additional variational degrees of freedom, it is necessary to calculate the KS orbitals exactly (Eq. (7)), making the calculation of the electronic groundstate more complex for metallic systems, where partial occupancies should be used. 其中γnm是厄米矩阵。如果包含部分占据数，即将fn视为额外的变分自由度，则必须精确计算KS轨道（式(7)），这使得对于应使用部分占据数的金属体系，电子基态的计算更为复杂。
> 
> 2.2. Metallic systems and partial occupancies 2.2. 金属体系与部分占据数
> 
> At this point it is necessary to review the impact of partial occupancies on the local density functional (LDF). There are two different approaches to the introduction of partial occupancies to the Kohn-Sham functional: First, Mermin [29] extended the LDF to finite temperatures. This approach becomes physically significant if the temperature of the system is comparable to characteristic excitation energies. In this case it is also important to use the finite-temperature exchange correlation functional EXCT[ρ] [30]. Considering the limited accuracy of the LDA it seems to be reasonable to replace EXCT[ρ] by EXC0[ρ]. For the finite temperature LDF, the impact of partial occupancies on the forces has probably been first discussed independently by Weinert and Davenport [31] and by Wentzcovitch, Martins and Allen [32]. The second approach concentrates on the evaluation of the energy at zero temperature: In this case partial occupancies are introduced as a tool for reducing the number of k-points in the Brillouin zone which are necessary to evaluate the band structure energy. At zero temperature, the band-structure energy is defined as 在这一点上，有必要回顾部分占据数对局域密度泛函（LDF）的影响。有两种不同方法将部分占据数引入Kohn-Sham泛函：第一，Mermin [29]将LDF推广到有限温度。当系统温度与特征激发能可比时，这种方法具有物理意义。在这种情况下，使用有限温度交换关联泛函EXCT[ρ] [30]也很重要。考虑到LDA的有限精度，用EXC0[ρ]替换EXCT[ρ]似乎是合理的。对于有限温度LDF，部分占据数对力的影响可能首先由Weinert和Davenport [31]以及Wentzcovitch、Martins和Allen [32]独立讨论。第二种方法集中于计算零温能量：在这种情况下，部分占据数被引入作为一种工具，以减少在布里渊区中评估能带结构能量所需的k点数。在零温下，能带结构能量定义为
> 
> Eband = Σn ∫ d3k Θ(εF - εn,k) εn,k Eband = Σn ∫ d3k Θ(εF - εn,k) εn,k
> 
> where Θ(X) is the Dirac step function, and εF the Fermi-energy. This integral has to be evaluated using a discrete set of k-points 其中Θ(X)是狄拉克阶跃函数，εF是费米能。此积分必须使用离散k点集计算
> 
> ∫ d3k → Σm wm. ∫ d3k → Σm wm.
> 
> For completely filled bands (i.e. semiconductors and insulators) no discontinuity exists, and the integral can be calculated accurately using a set of Monkhorst Pack special k-points (see Ref. [34]). But for metals the sum converges exceedingly slowly with the number of k-points included, because the occupancies jump discontinuously from 1 to 0 at the Fermi level. The convergence with respect to the number of k points can be improved by replacing the step function Θ(εF - εn) by a smoother function f({εn}). Several functional forms have been proposed for f({εn}), among these the linear tetrahedron method is probably the most unambiguous approach. 对于完全填满的能带（即半导体和绝缘体），不存在间断，可以使用一组Monkhorst Pack特殊k点（见参考文献[34]）精确计算积分。但对于金属，求和收敛极慢，因为占据数在费米能级处从1突跳到0。通过用更平滑的函数f({εn})替换阶跃函数Θ(εF - εn)，可以改善关于k点数的收敛性。已提出f({εn})的几种函数形式，其中线性四面体方法可能是最明确的方法。
> 
> 2.2.1. Linear tetrahedron method 2.2.1. 线性四面体方法
> 
> Within the linear tetrahedron (LT) method, the one-electron energies εn,k are interpolated linearly between the k-points, and the integral for the band-structure energy is performed analytically within each tetrahedron [35]. Blöchl [36] has recently revised the tetrahedron method to give effective weights fn({εn}) for each band and k-point. This new formulation gives strictly the same results as the conventional tetrahedron method but is easier to implement in most existing codes. In a second step, Blöchl was able to derive a correction formula which removes the quadratic error inherent in the LT method by going beyond the linear approximation and by including the effects of the curvature of the bands at the Fermi surface (we will refer to this method as LT-C, whereas LT is the standard linear tetrahedron method). The LT-C method converges very fast with the number of k-points, and we consider this method to be the most accurate and most unambiguous method for calculating the total energy of bulk materials containing a small number of atoms. Nevertheless the method is not applicable to large supercells, because usually only a very small number of k-points is used in this case. In addition we have shown in Appendix B that the LT-C method makes the calculation of forces at least inconvenient (see also Ref. [36]), whereas the calculation of forces is straightforward for the conventional LT method: Blöchl points out that the total energy is variational with respect to the partial occupancies (‘the traditional tetrahedron method is variational with respect to a change in the Fermi surface’), and therefore it is not necessary to recalculate the occupancies to get first order energy changes or forces. This behavior is clear, considering the basic foundations of the LT method. Within the conventional tetrahedron method the energy is linearly interpolated between a set of k-points resulting in a band structure εn(k) and the occupancies are set according to the step function fn(k) = Θ(εn(k) - μ). Because these occupancies minimize the zero temperature KS functional, it is possible to evaluate first order energy changes without recalculating the ‘Fermi surface’, i.e. keeping the occupancies fixed. This property is still valid for the revised linear tetrahedron method with effective occupancies fn({εn}). But if the additional correction formula given by Blöchl (LT-C) is used the variational property with respect to the occupancies is destroyed [36] (see Appendix B), and additional terms have to be included for an exact evaluation of the forces. These additional terms arise from the derivatives of the partial occupancies with respect to the ionic positions. For US PP the corresponding terms can not be evaluated easily, making the LT-C method an inconvenient tool if exact forces are required. Therefore it is necessary to resort to different methods like the smearing methods, explained in the next section. 在线性四面体（LT）方法中，单电子能量εn,k在k点之间线性插值，能带结构能量的积分在每个四面体内解析求得[35]。Blöchl [36]最近修订了四面体方法，为每个能带和k点给出有效权重fn({εn})。这种新表述严格给出与传统四面体方法相同的结果，但更易于在现有代码中实现。在第二步中，Blöchl能够推导出一个修正公式，通过超越线性近似并纳入费米面处能带曲率的影响，消除了LT方法固有的二次误差（我们将此方法称为LT-C，而LT是标准线性四面体方法）。LT-C方法随k点数收敛非常快，我们认为该方法是计算含少量原子的体材料总能量最准确、最明确的方法。然而，该方法不适用于大超胞，因为在这种情况下通常只使用非常少的k点。此外，我们在附录B中表明，LT-C方法至少使力的计算变得不方便（另见参考文献[36]），而对于传统LT方法，力的计算是直接的：Blöchl指出总能量对部分占据数是变分的（“传统四面体方法对费米面的变化是变分的”），因此无需重新计算占据数即可获得一阶能量变化或力。考虑到LT方法的基本原理，这种行为是清楚的。在传统四面体方法中，能量在一组k点之间线性插值，得到能带结构εn(k)，占据数根据阶跃函数fn(k) = Θ(εn(k) - μ)设定。因为这些占据数使零温KS泛函最小化，所以可以在保持占据数不变的情况下计算一阶能量变化，即无需重新计算“费米面”。这一性质对于具有有效占据数fn({εn})的修订线性四面体方法仍然有效。但如果使用Blöchl给出的附加修正公式（LT-C），关于占据数的变分性质被破坏[36]（见附录B），为精确计算力必须包含附加项。这些附加项源于部分占据数对离子位置的导数。对于US PP，相应的项不易计算，使得LT-C方法在需要精确力时成为一个不便的工具。因此，有必要求助于不同方法，如下一节所述的展宽方法。
> 
> 2.2.2. Finite-temperature approaches - ‘smearing methods’ 2.2.2. 有限温度方法——“展宽方法”
> 
> We have already pointed out that finite-temperature LDF methods were first introduced by Mermin [29]. In the context of ab-initio calculations it is possible to use these methods as a tool for the reduction of the necessary number of k-points to calculate the total energy of a metallic system. In this case, the term ‘smearing methods’ is probably more appropriate. Within these methods the step function is simply replaced by a smoothly varying function, for example the Fermi-Dirac function 我们已指出，有限温度LDF方法首先由Mermin [29]引入。在从头算的背景下，可以使用这些方法作为减少计算金属体系总能量所需k点数的工具。在这种情况下，术语“展宽方法”可能更合适。在这些方法中，阶跃函数被简单地替换为一个平滑变化的函数，例如费米-狄拉克函数
> 
> f(ε - μ / σ) = 1 / (exp((ε - μ)/σ) + 1) f(ε - μ / σ) = 1 / (exp((ε - μ)/σ) + 1)
> 
> or the integral over a Gaussian 或高斯函数的积分
> 
> f(x) = ½ (1 - erf[x]). f(x) = ½ (1 - erf[x]).
> 
> The Gaussian has been used first by Fu and Ho [33] in the context of plane wave pseudopotential calculations. It turns out that the total energy is no longer minimal with respect to variations of f at the electronic groundstate, and to obtain a variational functional it is necessary to replace the total energy E by a generalized free energy F [31,32] 高斯函数首先由Fu和Ho [33]用于平面波赝势计算。结果表明，总能量在电子基态不再对f的变化取最小值，为获得变分泛函，必须用广义自由能F替换总能量E [31,32]
> 
> F = E - Σn σ S(fn) F = E - Σn σ S(fn)
> 
> with a correct form for the entropy term S(fn). For the Fermi-Dirac function S is given by 并具有正确的熵项S(fn)形式。对于费米-狄拉克函数，S由下式给出
> 
> S(f) = -[f ln f + (1 - f) ln(1 - f)]. S(f) = -[f ln f + (1 - f) ln(1 - f)].
> 
> If the constraint on the number of electrons is taken into account it is easy to show that the variation of Eq. (16) with respect to fn is zero if the partial occupancies are set according to Eq. (14). For the Gaussian smearing the ‘entropy’ is defined as [37] 如果考虑电子数约束，容易证明，如果部分占据数按式(14)设置，则式(16)对fn的变分为零。对于高斯展宽，“熵”定义为[37]
> 
> S(εn - μ / σ) = -1/√π exp(-[(εn - μ)/σ]²). S(εn - μ / σ) = -1/√π exp(-[(εn - μ)/σ]²).
> 
> Formally it is necessary to express S as a function of f (see Eq. (16)), but this is not possible for Gaussian smearing because no analytical inversion of the error function exists. During an actual calculation based on the SC-methods (see Section 2.3) it is sufficient to evaluate the entropy term from Eq. (18), because the eigenvalues εn are always available. In conjunction with Fermi-Dirac statistics the free energy might be interpreted as the free energy of the electrons at some finite-temperature (T = kBT σ [29], but the physical significance of the free energy remains undefined for Gaussian smearing. For a continuous density of states at the Fermi-level it might be shown that the free energy deviates quadratically with σ from Eσ=0 [38] 形式上，需要将S表示为f的函数（见式(16)），但这对于高斯展宽是不可能的，因为误差函数不存在解析反函数。在基于SC方法的实际计算中（见第2.3节），使用式(18)计算熵项就足够了，因为本征值εn总是可用的。结合费米-狄拉克统计，自由能可解释为电子在某一有限温度下的自由能（T = kBT σ [29]），但对于高斯展宽，自由能的物理意义仍未定义。对于费米能级处连续的态密度，可以证明自由能随σ以二次方偏离Eσ=0 [38]
> 
> F(σ) = Eσ=0 + γσ². F(σ) = Eσ=0 + γσ².
> 
> Using S(σ) = -dF(σ)/dσ it is possible to obtain for the energy E the equation 利用S(σ) = -dF(σ)/dσ，可以得到能量E的方程
> 
> E(σ) = F(σ) + σ S(σ) = Eσ=0 - γσ². E(σ) = F(σ) + σ S(σ) = Eσ=0 - γσ².
> 
> It is now easy to see that it is possible to obtain an accurate extrapolation for σ → 0 from results at finite σ using the formula 现在容易看出，利用以下公式，可以从有限σ的结果得到σ → 0的精确外推
> 
> Eσ=0 = Ē(σ) = ½(F(σ) + E(σ)). Eσ=0 = Ē(σ) = ½(F(σ) + E(σ)).
> 
> This way the leading quadratic error in σ is removed from F(σ), and a functional Ē(σ) which deviates only slowly from Eσ=0 might be obtained. 这样，F(σ)中领先的二次误差被消除，可以得到一个仅缓慢偏离Eσ=0的泛函Ē(σ)。
> 
> As an illustration the convergence with respect to σ for F(σ) and Ē(σ) is shown for Aluminium and Vanadium in Fig. 1. In the context of ab-initio calculations Eq. (21) was first used by Gillan [12] and later generalized by De Vita and Gillan [37] and it allows an easy and accurate evaluation of zero temperature properties. Even for a relatively large σ Ē(σ) converges to the exact zero temperature total energy Eσ=0, and the evaluation of Ē(σ) requires a substantially smaller number of k-points than a calculation with σ = 0. Typical settings for σ for different materials are compiled in Table 1. 作为示例，图1显示了铝和钒的F(σ)和Ē(σ)关于σ的收敛性。在从头算的背景下，式(21)首先由Gillan [12]使用，后来由De Vita和Gillan [37]推广，它允许简单而精确地计算零温性质。即使对于相对较大的σ，Ē(σ)也收敛到精确的零温总能量Eσ=0，并且计算Ē(σ)所需的k点数远少于σ = 0时的计算。不同材料的典型σ设置汇总于表1。
> 
> Table 1 Convenient settings for the smearing parameter σ for different metals 表1 不同金属展宽参数σ的方便设置
> 
> 

<table>
<thead>
<tr>
<th>Metal</th>
<th>σ (eV)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Aluminium</td>
<td>1.0</td>
</tr>
<tr>
<td>Lithium</td>
<td>0.4</td>
</tr>
<tr>
<td>sc-Tellurium</td>
<td>0.8</td>
</tr>
<tr>
<td>Copper</td>
<td>0.4</td>
</tr>
<tr>
<td>Vanadium</td>
<td>0.3</td>
</tr>
<tr>
<td>Rhodium</td>
<td>0.3</td>
</tr>
</tbody>
</table>


> 
> The smearing parameter σ was determined so that the entropy term ΣnσS(fn) was less than 1 meV/atom in the method of Methfessel and Paxton with N = 1. Aluminium, Lithium and Tellurium show a fairly simple structure of the DOS at the Fermi level, therefore σ might be large. For Copper σ is restricted by the fact that the d-band lies approximately 0.5 eV beneath the Fermi level. Due to the complicated structure of the DOS at the Fermi level σ must be small for most transition metals like Vanadium. 展宽参数σ的确定使得在Methfessel和Paxton方法（N = 1）中熵项ΣnσS(fn)小于1 meV/原子。铝、锂和碲在费米能级处的态密度结构相当简单，因此σ可以较大。对于铜，σ受限于d带位于费米能级以下约0.5 eV的事实。由于费米能级处态密度的复杂结构，对于大多数过渡金属如钒，σ必须较小。
> 
> 2.2.3. Improved functional form for f({ε}) - Method of Methfessel and Paxton 2.2.3. f({ε})的改进函数形式——Methfessel和Paxton方法
> 
> The method described in the last section has two distinct shortcomings: 上一节描述的方法有两个明显的缺点：
> 
> -   . Forces are usually defined as the derivatives of the variational quantity, i.e. the free electronic energy F (see Section 2.4). Therefore the forces cannot be used to obtain the equilibrium zero ‘temperature’ groundstate or exact phonon frequencies which corresponds to an energy-minimum of Ē(σ).  
>     力通常定义为变分量的导数，即电子自由能F（见第2.4节）。因此，力不能用于获得对应于Ē(σ)能量最小值的平衡零“温”基态或精确声子频率。
> -   . The parameter σ has to be chosen with great care. If σ is too large the energy Ē(σ) will converge to the wrong value even for an infinite k-point mesh, and if σ is too small the convergence with the number of k-points will deteriorate. An optimum choice for σ can be found only by comparing results for different k-point meshes and different values of σ.  
>     参数σ必须非常小心地选择。如果σ太大，即使对于无限k点网格，能量Ē(σ)也会收敛到错误值；如果σ太小，则关于k点数的收敛性会变差。σ的最佳选择只能通过比较不同k点网格和不同σ值的结果来找到。
> 
> These problems can be solved by adopting a slightly different functional form for f({ε}), which was first proposed by Methfessel and Paxton (MP) [38]. They expanded the step function in a complete orthonormal set of functions. Within this approach the integral of the Gaussian is only the first approximation (N = 0) of the step function, further successive approximations (N = 1, 2, …) can be obtained easily. In analogy to the Gaussian method, the total energy is no longer variational with respect to the partial occupancies and has to be replaced by a generalized free energy functional (one feature missing in the original work of Methfessel and Paxton). The variational quantity is defined by 这些问题可以通过采用稍有不同的f({ε})函数形式来解决，该形式首先由Methfessel和Paxton（MP）[38]提出。他们将阶跃函数在一组完备正交函数中展开。在这种方法中，高斯函数的积分仅是阶跃函数的第一级近似（N = 0），进一步的逐级近似（N = 1, 2, …）可以容易地得到。与高斯方法类似，总能量不再对部分占据数是变分的，必须用广义自由能泛函替换（这是Methfessel和Paxton原始工作中缺失的一个特征）。变分量定义为
> 
> F = E - Σn σ SN(fn) F = E - Σn σ SN(fn)
> 
> where SN is given by 其中SN由下式给出
> 
> SN(x) = Σm=1N Am H2m-1(x) e-x² SN(x) = Σm=1N Am H2m-1(x) e-x²
> 
> and the partial occupancies are given by 且部分占据数由下式给出
> 
> fN(x) = f0(x) + Σm=1N Am H2m-1(x) e-x² fN(x) = f0(x) + Σm=1N Am H2m-1(x) e-x²
> 
> with 其中
> 
> x = (ε - μ)/σ. x = (ε - μ)/σ.
> 
> Hm is the Hermite polynomial of degree m, and explicit formulas for Am can be found in Ref. [38]. In contrast to the Gaussian method the entropy term ΣnσSN((εn - μ)/σ) will be very small for a reasonable choice of σ, and the deviations from Eσ=0 are only of the order N + 2 in σ (see also Fig. 1) Hm是m阶厄米多项式，Am的显式公式可在参考文献[38]中找到。与高斯方法相比，对于合理的σ选择，熵项ΣnσSN((εn - μ)/σ)将非常小，且与Eσ=0的偏差仅为σ的N+2阶（另见图1）
> 
> F(σ) = Eσ=0 + O(σ2+N). F(σ) = Eσ=0 + O(σ2+N).
> 
> Extrapolation to zero σ is usually not necessary, but in principle it might be done using 通常不需要外推到σ为零，但原则上可以使用以下公式进行
> 
> Eσ=0 = È(σ) = 1/(N+1) ((N+1)F(σ) + E(σ)). Eσ=0 = È(σ) = 1/(N+1) ((N+1)F(σ) + E(σ)).
> 
> The values given in Table 1 will result in an entropy which is less than 1 meV per atom and in a very accurate description of the lattice constant and bulk moduli. We found that the 1 meV threshold is sufficient for most calculations of elastic properties and phonon frequencies. To summarize: For the MP-method the entropy term is a simple error estimation for the difference between the free energy F and the ‘physically’ correct energy Eσ=0. σ can be increased until this error estimation gets larger than an allowed threshold (usually 1 meV). Because the free energy and the ‘physical’ energy Eσ=0 are the same except for this small error the forces which are calculated as a derivative of the free energy are also correct and can be used to determine the zero ‘temperature’ groundstate. Especially the last property makes the method of Methfessel and Paxton very appealing for situations where the k mesh is not sufficient for the application of the tetrahedron method, or applications where accurate forces are required (see Section 2.2.5 and Table 2). 表1给出的值将导致每个原子的熵小于1 meV，并能非常精确地描述晶格常数和体模量。我们发现1 meV的阈值对于大多数弹性性质和声子频率的计算是足够的。总结：对于MP方法，熵项是自由能F与“物理上”正确的能量Eσ=0之间差异的简单误差估计。σ可以增加，直到此误差估计大于允许的阈值（通常为1 meV）。因为自由能和“物理”能量Eσ=0除了这个微小误差外是相同的，所以作为自由能导数计算的力也是正确的，并可用于确定零“温”基态。特别是最后一个特性使Methfessel和Paxton方法在k点网格不足以应用四面体方法，或需要精确力的情况下非常有吸引力（见第2.2.5节和表2）。
> 
> 2.2.4. Convergence of the total energy with the number of k-points 2.2.4. 总能量随k点数的收敛性
> 
> We want to illustrate the convergence with respect to the number k-points for the LT-C and the MP-method for two simple examples - bulk Aluminium and bulk Vanadium. In Vanadium the convergence is especially cumbersome, because s and d like bands exist close to the Fermi surface. Fig. 1 shows the convergence of different functionals with respect to σ for Al and V. For the conventional Gaussian method the free energy F(σ) deviates even for small σ rapidly from Eσ=0. But the functional Ē (Eq. (21)) and the free energy functionals for the MP-methods with N ≥ 1 converge rapidly to the correct energy, allowing a much larger σ. In Fig. 2 the convergence of energy for the LT-C and of the free energy for Gaussian smearing (N = 0) and the MP-method (N = 1) with respect to the k-point mesh is shown. For each calculation σ was chosen so that the error in the k-point converged energy was less than 1 meV. It might be seen that the LT-C method converges fastest for Al and V and in addition the LT-C does not require to find an optimal σ. Nevertheless the convergence of the MP-method (N = 1) is also quite good, mainly because σ can be relatively large. Gaussian smearing without the extrapolation Ē (Eq. (21)), requires a small σ resulting in the slowest convergence. 我们想通过两个简单例子——体铝和体钒——来说明LT-C和MP方法关于k点数的收敛性。在钒中，收敛性尤其麻烦，因为费米面附近存在s和d类能带。图1显示了Al和V的不同泛函关于σ的收敛性。对于传统高斯方法，自由能F(σ)即使在σ较小时也迅速偏离Eσ=0。但泛函Ē（式(21)）和N ≥ 1的MP方法的自由能泛函迅速收敛到正确能量，允许使用更大的σ。图2显示了LT-C的能量以及高斯展宽（N = 0）和MP方法（N = 1）的自由能随k点网格的收敛性。在每次计算中，σ的选择使得k点收敛能量的误差小于1 meV。可以看出，LT-C方法对Al和V收敛最快，而且LT-C不需要寻找最佳σ。然而，MP方法（N = 1）的收敛性也相当好，主要是因为σ可以相对较大。没有外推Ē（式(21)）的高斯展宽需要较小的σ，导致收敛最慢。
> 
> 2.2.5. Calculation of phonon frequencies for metals 2.2.5. 金属声子频率的计算
> 
> To illustrate that the LT-C method might be problematic for the calculation of phonon frequencies based on the forces we show results for the phonon frequencies of Rh for a high symmetry point in Table 2. The phonon frequencies were calculated from the change of the free energy induced by a small displacement and from the forces for a displaced structure. Different methods for calculating the partial occupancies have been used: For the MP-method and the standard linear tetrahedron (LT) method the phonon frequencies derived from the forces and the energy are equivalent, but because the k-point mesh is not sufficient for a good convergence of the LT method errors in the LT method are up to 10%. Phonon frequencies derived from the free energy change are almost indistinguishable for the MP and the linear tetrahedron method with Blöchl corrections (LT-C) approach indicating that the k-point mesh is sufficient for both methods. But for the LT-C method, the partial occupancies were kept fixed for the evaluation of the forces, resulting in a considerable error of the forces and a serious error of the corresponding phonon frequencies (≈ 5%). This indicates that the MP-method is the best choice for calculations where accurate forces are required. Especially phonon frequencies can be evaluated accurately and easily within this approach. We have used the MP-method recently with good success for the calculation of phonon frequencies in bulk Li, Na, K, Rh and Mo and for the calculation of properties of metallic Rh surfaces (including surface phonons) [21]. 为了说明LT-C方法可能对基于力的声子频率计算造成问题，我们在表2中展示了Rh在高对称点的声子频率结果。声子频率由小位移引起的自由能变化和位移结构的力计算得出。使用了不同的部分占据数计算方法：对于MP方法和标准线性四面体（LT）方法，由力和能量得出的声子频率是等价的，但由于k点网格不足以使LT方法良好收敛，LT方法的误差高达10%。对于MP和带有Blöchl修正的线性四面体方法（LT-C），由自由能变化得出的声子频率几乎不可区分，表明k点网格对两种方法都是足够的。但对于LT-C方法，在计算力时部分占据数保持不变，导致力的显著误差和相应声子频率的严重误差（≈ 5%）。这表明MP方法是需要精确力的计算的最佳选择。特别是，声子频率可以在该方法中准确且容易地计算。我们最近使用MP方法成功计算了体Li、Na、K、Rh和Mo的声子频率以及金属Rh表面的性质（包括表面声子）[21]。
> 
> Table 2 Phonon frequencies for Rh at the K-point (i.e. in (1 1 1) direction, Brillouin zone boundary) calculated using a frozen-phonon approach 表2 使用冻结声子方法计算的Rh在K点（即(1 1 1)方向，布里渊区边界）的声子频率
> 
> 

<table>
<thead>
<tr>
<th>f (THz)</th>
<th>Energy MP</th>
<th>Force MP</th>
<th>Energy LT-C</th>
<th>Force LT-C</th>
<th>Energy LT</th>
<th>Force LT</th>
</tr>
</thead>
<tbody>
<tr>
<td>III trans.</td>
<td>4.29</td>
<td>4.28</td>
<td>4.30</td>
<td>4.10</td>
<td>3.91</td>
<td>3.93</td>
</tr>
<tr>
<td>I II long</td>
<td>7.95</td>
<td>7.96</td>
<td>7.93</td>
<td>7.68</td>
<td>7.46</td>
<td>7.49</td>
</tr>
</tbody>
</table>


> 
> A Monkhorst Pack grid consisting of 9 × 9 × 3 k-points was used corresponding to 70 k-points in the irreducible wedge for the transversal branch and 31 k-points for the longitudinal branch. MP is the method of Methfessel Paxton for N = 2 and σ = 0.4, LT-C is the tetrahedron method including the correction terms proposed by Blöchl and LT the linear tetrahedron method without corrections. The k-point mesh is not sufficient for an accurate calculation of phonon frequencies with the LT method, but results are converged for the MP and LT-C method. For the LT-C method the weights f were naively kept fixed, therefore the forces are not consistent with the energy. 使用了9×9×3的Monkhorst Pack k点网格，对应于横波支在不可约楔形中的70个k点和纵波支的31个k点。MP是N = 2、σ = 0.4的Methfessel-Paxton方法，LT-C是包含Blöchl修正项的四面体方法，LT是无修正的线性四面体方法。k点网格不足以用LT方法精确计算声子频率，但MP和LT-C方法的结果已收敛。对于LT-C方法，权重f被天真地保持不变，因此力与能量不一致。
> 
> 2.3. Selfconsistency loop and iterative methods 2.3. 自洽循环与迭代方法
> 
> We have pointed out in the introduction that iterative methods for the diagonalization of the KS Hamiltonian seem to be the most efficient schemes for calculating the finite temperature KS groundstate. These methods must be used in conjunction with a charge density mixing to get a reliable scheme; Fig. 3 shows a typical flowchart for this situation: At the beginning an appropriate set of trial wavefunction {φn} and a reasonable input charge density ρin is chosen. Usually, the start charge density corresponds to the superposition of the atomic pseudo charge densities of the constituents. From the input charge density the local potential 我们在引言中已指出，用于KS哈密顿量对角化的迭代方法似乎是计算有限温度KS基态的最有效方案。这些方法必须与电荷密度混合结合使用以获得可靠的方案；图3显示了这种情况的典型流程图：开始时，选择一组适当的试探波函数{φn}和一个合理的输入电荷密度ρin。通常，起始电荷密度对应于组分原子赝电荷密度的叠加。由输入电荷密度计算局域势
> 
> Veff = Vloc + VH[ρin] + VXC[ρin] Veff = Vloc + VH[ρin] + VXC[ρin]
> 
> and the corresponding double counting corrections 以及相应的双计数修正
> 
> Edc[ρin] = -½EH[ρin] + EXC[ρin] - ∫ d3r VXC(r)ρin(r) Edc[ρin] = -½EH[ρin] + EXC[ρin] - ∫ d3r VXC(r)ρin(r)
> 
> are evaluated. For ultrasoft pseudopotentials the nonlocal part of the pseudopotential depends also on the local potential and must be calculated accordingly (Eq. (10)). In the next step the Nb trial wavefunctions are improved using an iterative method, and the new eigenenergies are used to calculate a new Fermi energy and new partial occupancies. The total free energy for the current iteration is calculated as the sum of the band structure energy plus the entropy term plus double counting corrections 进行计算。对于超软赝势，赝势的非局域部分也依赖于局域势，必须相应地计算（式(10)）。在下一步中，使用迭代方法改进Nb个试探波函数，并用新的本征能量计算新的费米能和新的部分占据数。当前迭代的总自由能计算为能带结构能量加上熵项加上双计数修正
> 
> F = Σn fn εn - Σn σ S(fn) + Edc. F = Σn fn εn - Σn σ S(fn) + Edc.
> 
> Conceptually the calculated energy corresponds to the energy evaluated from the Harris-Foulkes (HF) functional [39-41], which is non-selfconsistent - in contrast to the KS functional: the HF functional (defined in Eq. (30)) requires the calculation of the band structure energy for a fixed charge density ρin. With our code it is easy to evaluate this energy keeping the initial charge density fixed (for instance to the superposition of atomic pseudo charge densities) and iterating the eigenvectors only until they are converged. To get the exact KS-groundstate-energy selfconsistency with respect to the input charge density requires that the charge density residual vector R[ρin] 从概念上讲，计算出的能量对应于从Harris-Foulkes（HF）泛函[39-41]计算出的能量，该泛函是非自洽的——与KS泛函相反：HF泛函（在式(30)中定义）要求对固定电荷密度ρin计算能带结构能量。使用我们的代码，可以容易地保持初始电荷密度固定（例如，原子赝电荷密度的叠加）并仅迭代本征向量直到收敛，从而计算该能量。要获得精确的KS基态能量，关于输入电荷密度的自洽性要求电荷密度残差向量R[ρin]
> 
> R[ρin] = ρout - ρin R[ρin] = ρout - ρin
> 
> is zero, where the output charge density ρout is calculated from the wavefunctions using Eq. (3). The residual vector R[ρin] - and possibly information from previous mixing steps - allows to calculate a new charge density ρin for the next selfconsistency loop. In principle it is necessary to evaluate the eigenfunctions φn exactly for each new input charge density making ρout and the residual vector R functionals of the input charge density ρin only. Nevertheless, even in conjunction with complex Broyden like mixing techniques, it turns out that this is not necessary if the final wavefunctions of the previous mixing iteration are used as new initial trial wavefunctions. In this case a few steps in the iterative matrix diagonalization are sufficient to get a reliable result for the charge density residual vector R. In Section 3 we will concentrate on different iterative methods for the diagonalization of the KS-Hamiltonian, Section 4 will discuss algorithms for the charge density mixing. 为零，其中输出电荷密度ρout由波函数通过式(3)计算。残差向量R[ρin]——以及可能来自之前混合步骤的信息——允许为下一个自洽循环计算新的电荷密度ρin。原则上，需要对每个新的输入电荷密度精确计算本征函数φn，使得ρout和残差向量R仅是输入电荷密度ρin的泛函。然而，即使结合复杂的类Broyden混合技术，结果证明，如果使用前一次混合迭代的最终波函数作为新的初始试探波函数，则不需要这样做。在这种情况下，迭代矩阵对角化中的几步就足以获得电荷密度残差向量R的可靠结果。在第3节中，我们将集中于不同的KS哈密顿量对角化迭代方法，第4节将讨论电荷密度混合的算法。
> 
> **Harris-Foulkes (HF) functional**: 哈里斯-福克斯泛函，一种非自洽的能量泛函，使用固定输入电荷密度计算能带结构能量。
> 
> 2.4. Forces 2.4. 力
> 
> Forces for the finite-temperature KS functional can be obtained easily, but the calculation is somewhat complicated by the US PP. To obtain the forces it is convenient to use a basis set oriented notation. In our case the wavefunctions are written as a sum of a finite set of plane waves |q⟩, i.e. 有限温度KS泛函的力可以容易地获得，但US PP使其计算有些复杂。为获得力，使用基组导向的符号是方便的。在我们的情况中，波函数写为有限平面波基组|q⟩的和，即
> 
> |φn⟩ = Σq Cn,q |q⟩ |φn⟩ = Σq Cn,q |q⟩
> 
> (once again the k-point index k has been omitted) and the KS energy functional E, respectively the free energy F becomes a function of the expansion coefficients Cn,q, the partial occupancies fn and the ionic positions RN, （再次省略k点指标k）KS能量泛函E，或自由能F，成为展开系数Cn,q、部分占据数fn和离子位置RN的函数，
> 
> F → F[{C}, {f}, {R}]. F → F[{C}, {f}, {R}].
> 
> To incorporate the orthonormality constraint and the conservation of the number of electrons it is convenient to use the Lagrange formalism and to introduce the function 为纳入正交归一约束和电子数守恒，使用拉格朗日形式并引入函数
> 
> F̃ = F - Σnm γnm (Σqq' Cn,q _Sqq' Cm,q' - δnm) - μ (Σn fn - Nel) F̃ = F - Σnm γnm (Σqq' Cn,q_ Sqq' Cm,q' - δnm) - μ (Σn fn - Nel)
> 
> where Aqq' is defined as 其中Aqq'定义为
> 
> Aqq' = ⟨q'|A|q⟩. Aqq' = ⟨q'|A|q⟩.
> 
> At the KS-groundstate the Lagrange multipliers are given by γnm = δnm εn fn, where εn are the exact KS-eigenvalues (compare with Eq. (117)), and F̃ is minimal with respect to arbitrary variations of Cn,q, γnm, fn and μ. The change in the free energy up to first-order is exactly given by (see Appendix A) 在KS基态，拉格朗日乘子由γnm = δnm εn fn给出，其中εn是精确的KS本征值（与式(117)比较），且F̃对Cn,q、γnm、fn和μ的任意变分取最小值。自由能的一阶变化精确由下式给出（见附录A）
> 
> dF = ΣN ∂F̃/∂RN dRN dF = ΣN ∂F̃/∂RN dRN
> 
> where changes of the Hamiltonian H due to changes in the selfconsistent charge density ρ must not be calculated. For further details we refer to Ref. [26,27]. It is also possible to obtain a correct formula for the forces if the Harris-Foulkes functional instead of the Kohn-Sham functional is used. If the input charge density ρin for the Harris-Foulkes functional is calculated from the atomic charge density of the constituents, only one additional term arises which is due to the fact that the input charge density depends on the atomic coordinates. In this case H in Eq. (38) has to be replaced by the Hamiltonian calculated from the atomic charge density H[ρatom, {R}], and the term 其中不得计算由于自洽电荷密度ρ变化引起的哈密顿量H的变化。更多细节请参考文献[26,27]。如果使用Harris-Foulkes泛函而非Kohn-Sham泛函，也可以获得力的正确公式。如果Harris-Foulkes泛函的输入电荷密度ρin由组分的原子电荷密度计算，则仅出现一个附加项，因为输入电荷密度依赖于原子坐标。在这种情况下，式(38)中的H必须替换为由原子电荷密度计算的哈密顿量H[ρatom, {R}]，并且项
> 
> ΣN ∫ d3r (VH[ρatom] + VXC[ρatom]) ∂ρatom/∂RN ΣN ∫ d3r (VH[ρatom] + VXC[ρatom]) ∂ρatom/∂RN
> 
> has to be added to the forces. In Eq. (38) changes of the Hamiltonian H due to changes in the input charge density ρin have to be omitted, as in the selfconsistent case. We have found that the similar correction formula 必须加到力中。在式(38)中，由于输入电荷密度ρin变化引起的哈密顿量H的变化必须省略，如同自洽情况。我们发现，类似的修正公式
> 
> dF/dRN = ΣN ∫ d3r (VH[ρin] + VXC[ρin]) (ρout(r) - ρin(r)) dF/dRN = ΣN ∫ d3r (VH[ρin] + VXC[ρin]) (ρout(r) - ρin(r))
> 
> also improves the convergence of the forces during a selfconsistent calculation. In Eq. (38) H has to be replaced by H[ρin, {R}], where ρin is the charge density obtained in the previous iteration. In principle it is necessary to evaluate the change of ρin if the ions move (i.e. the first term in Eq. (40) should be replaced by ∂(VH + VXC)(ρin)/∂RN), which is not possible, but Eq. (40) seems to be an excellent approximation. This correction formula improves the precision of the forces by almost two orders of magnitude, and allows to stop the selfconsistency cycle much earlier. This is demonstrated in Fig. 4, where the convergence for the forces is compared for different algorithms for a Pd(111) surface with a mono-layer hydrogen (see Section 6.1.2). It can be seen that the optimized scheme (opt) explained here results in the best overall performance. A similar convergence rate might be obtained by using the mixed charge density (mix) (Section 4) for the calculation of the local contribution to the forces, i.e. 也能改善自洽计算中力的收敛性。在式(38)中，H必须替换为H[ρin, {R}]，其中ρin是前一次迭代获得的电荷密度。原则上，如果离子移动，需要计算ρin的变化（即式(40)中的第一项应替换为∂(VH + VXC)(ρin)/∂RN），但这是不可能的，然而式(40)似乎是一个极好的近似。此修正公式将力的精度提高了近两个数量级，并允许更早停止自洽循环。这在图4中得到证明，其中比较了不同算法对具有单层氢的Pd(111)表面（见第6.1.2节）的力的收敛性。可以看出，此处解释的优化方案（opt）给出了最佳整体性能。通过使用混合电荷密度（mix）（第4节）计算力的局域贡献，也可以获得类似的收敛速率，即
> 
> FN = -∫ d3r (VH[ρmix] + VXC[ρmix]) ∂ρin/∂RN FN = -∫ d3r (VH[ρmix] + VXC[ρmix]) ∂ρin/∂RN
> 
> This part of the forces is very sensible to changes in the charge density. The use of the output charge density (out) - i.e. the left side of Eq. (41) - without the correction term (Eq. (40)) makes the forces worse by a factor 100 (see Fig. 4). 力的这一部分对电荷密度的变化非常敏感。使用输出电荷密度（out）——即式(41)的左侧——而不加修正项（式(40)）会使力变差100倍（见图4）。
> 
> 3.  Iterative methods for the diagonalization of the KS-Hamiltonian
> 4.  KS哈密顿量对角化的迭代方法
> 
> In this section we will discuss several iterative approaches for the diagonalization of the KS Hamiltonian, including the residual minimization method direct inversion in the iterative subspace (RMM-DIIS or simply RMM) proposed by Pulay [24] and Wood and Zunger [44], which is superior for very large matrices. For ultrasoft pseudopotentials we are confronted with a generalized eigenvalue problem (see Eq. (7)) 在本节中，我们将讨论几种用于KS哈密顿量对角化的迭代方法，包括由Pulay [24]和Wood与Zunger [44]提出的残差最小化方法——迭代子空间直接反演（RMM-DIIS或简称RMM），该方法对于非常大的矩阵具有优越性。对于超软赝势，我们面临广义本征值问题（见式(7)）
> 
> H|φn⟩ = εnS|φn⟩ H|φn⟩ = εnS|φn⟩
> 
> which has to be solved. For a small basis set, this eigenvalue problem is usually solved by straightforward diagonalization of the Hamiltonian (for instance using the Choleski-Householder procedure). Nevertheless, this procedure becomes intractable for large matrices, because it scales as NPW3, NPW being the number of plane-waves included in the basis set. For three reasons iterative methods are an order of magnitude faster for the calculation of the eigenfunctions: (i) only Nb ≪ NPW occupied orbitals must be calculated, (ii) the calculation of H|φn⟩ is especially convenient for a plane-wave basis set (see introduction), and (iii) iterative methods are efficient in conjunction with a selfconsistent calculation, because optimization of the charge density and wavefunctions can be done almost simultaneously. A good review of different iterative methods can be found in [44] and we will try to adopt the notation of this paper. Nevertheless we also want to point out that the examples discussed in Ref. [44] are only small to medium sized from today’s point of view, and not all of the algorithms of Ref. [44] work reliably for very large systems. In addition new iterative methods (like the band-by-band conjugate gradient algorithm [10,45]) have been proposed recently, making a new comparison between different methods necessary. As pointed out in [44] most iterative algorithms construct an expansion set {|bi}, i = 1, …, Ns} from which the best approximation to the exact eigenvalues and eigenvectors is calculated. This expansion set is much smaller than the number of plane waves NPW and depending on the algorithm it might be smaller or larger than the number of bands Nb to be calculated. In each iteration new vectors are added to the expansion set. It is possible to differentiate between blocked and unblocked methods. Unblocked methods (or sequential band by band methods) optimize one band at a time and the expansion set usually starts with only one vector |b1⟩, which should be a reasonable approximation to the eigenvector |φn⟩. In each iteration i a single correction vector |bi⟩ is added to the expansion set. Blocked methods on the other hand optimize all orbitals or a set of orbitals simultaneously, increasing the size of the expansion set at each step by Nb new vectors. In most blocked and unblocked methods it is necessary to obtain a new best approximation of the exact eigenvalues and eigenvectors from the expansion set at each iteration. This is done via the Rayleigh-Ritz [44,46] scheme: In principle the Hamiltonian is diagonalized in the space spanned by the expansion set, i.e. the Ns × Ns eigenvalue problem 必须求解。对于小基组，这个本征值问题通常通过哈密顿量的直接对角化（例如使用Choleski-Householder过程）来解决。然而，对于大矩阵，此过程变得难以处理，因为它按NPW3标度，NPW是基组中包含的平面波数。由于三个原因，迭代方法在计算本征函数时快一个数量级：(i) 只需计算Nb ≪ NPW个占据轨道，(ii) 对于平面波基组，H|φn⟩的计算特别方便（见引言），(iii) 迭代方法与自洽计算结合时效率高，因为电荷密度和波函数的优化几乎可以同时进行。不同迭代方法的良好综述可见[44]，我们将尝试采用该文的符号。然而，我们还想指出，从今天的观点看，参考文献[44]中讨论的例子仅是小到中等规模的，且并非[44]中的所有算法都能可靠地用于非常大的体系。此外，最近提出了新的迭代方法（如逐带共轭梯度算法[10,45]），使得有必要对不同方法进行新的比较。正如[44]中所指出的，大多数迭代算法构建一个展开集 {|bi}, i = 1, …, Ns}，从中计算精确本征值和本征向量的最佳近似。该展开集远小于平面波数NPW，且根据算法，它可能小于或大于待计算的能带数Nb。在每次迭代中，新向量被添加到展开集中。可以区分分块方法和非分块方法。非分块方法（或顺序逐带方法）一次优化一个能带，展开集通常仅以一个向量|b1⟩开始，该向量应是本征向量|φn⟩的合理近似。在每次迭代i中，一个单独的修正向量|bi⟩被添加到展开集中。另一方面，分块方法同时优化所有轨道或一组轨道，在每一步将展开集的大小增加Nb个新向量。在大多数分块和非分块方法中，每次迭代都需要从展开集获得精确本征值和本征向量的新最佳近似。这通过Rayleigh-Ritz [44,46]方案完成：原则上，哈密顿量在展开集张成的空间中对角化，即Ns × Ns本征值问题
> 
> Σm Him cmα = εα Σm Sim cmα Σm Him cmα = εα Σm Sim cmα
> 
> with 其中
> 
> Him = ⟨bi|H|bm⟩, Sim = ⟨bi|S|bm⟩, Him = ⟨bi|H|bm⟩, Sim = ⟨bi|S|bm⟩,
> 
> must be solved. The m lowest eigenvalue/eigenvector pairs 必须求解。m个最低本征值/本征向量对
> 
> |φ̃α⟩ = Σm cmα |bm⟩ |φ̃α⟩ = Σm cmα |bm⟩
> 
> correspond to the best approximation of the exact lowest m eigenvalues and eigenvectors within the sub-space spanned by the expansion set. 对应于展开集张成子空间内精确最低m个本征值和本征向量的最佳近似。
> 
> 3.1. Residual vector and preconditioning 3.1. 残差向量与预条件
> 
> A key step within all iterative methods is the calculation of a correction vector which is added to the expansion set, and a central quantity within most methods is the Rayleigh quotient, which is defined as 所有迭代方法中的一个关键步骤是计算添加到展开集中的修正向量，而大多数方法中的一个核心量是瑞利商，定义为
> 
> εapp = ⟨φn|H|φn⟩ / ⟨φn|S|φn⟩. εapp = ⟨φn|H|φn⟩ / ⟨φn|S|φn⟩.
> 
> This quantity possesses a saddle point at the exact eigenvector, and variation of the Rayleigh quotient with respect to ⟨φn| leads to the residual vector defined as 该量在精确本征向量处具有鞍点，瑞利商对⟨φn|的变分导出定义为
> 
> |R(φn)⟩ = (H - εappS)|φn⟩ |R(φn)⟩ = (H - εappS)|φn⟩
> 
> if ⟨φn|S|φn⟩ = 1. The norm of the residual vector ⟨R|R⟩ is an accepted measure for the error in the eigenvector. Formally a good approximation to the difference between the exact and the approximate eigenvector |φn⟩ is obtained from the residual vector using the equation 若⟨φn|S|φn⟩ = 1。残差向量的范数⟨R|R⟩是公认的本征向量误差度量。形式上，精确本征向量与近似本征向量|φn⟩之差的良好近似可从残差向量通过以下方程获得
> 
> |δφn⟩ = - (H - εappS)-1|R⟩. |δφn⟩ = - (H - εappS)-1|R⟩.
> 
> It is easy to show that |φ̃n⟩ = |φn⟩ + |δφn⟩ results in a minimum residual vector, which satisfies 容易证明，|φ̃n⟩ = |φn⟩ + |δφn⟩给出最小残差向量，满足
> 
> 0 = (H - εappS)|φ̃n⟩. 0 = (H - εappS)|φ̃n⟩.
> 
> Nevertheless, the inversion of H - εappS is not easier than the diagonalization of the matrix H and definitely intractable for large matrices. This makes a more approximate treatment necessary. In the following, the step which calculates the approximative error |δφn⟩ from the residual vector will be called preconditioning, and the matrix K which is multiplied with the residual vector to obtain |δφn⟩ 然而，求逆H - εappS并不比矩阵H的对角化更容易，且对于大矩阵肯定难以处理。这使得更近似的处理成为必要。在下文中，从残差向量计算近似误差|δφn⟩的步骤将被称为预条件，而与残差向量相乘得到|δφn⟩的矩阵K
> 
> |δφn⟩ = K|R⟩ |δφn⟩ = K|R⟩
> 
> will be called preconditioning matrix. Frequently only the diagonal elements of the exact matrix in Eq. (49) are used, i.e. 将被称为预条件矩阵。通常仅使用式(49)中精确矩阵的对角元，即
> 
> K = - Σq |q⟩⟨q| / ⟨q|(H - εappS)|q⟩ K = - Σq |q⟩⟨q| / ⟨q|(H - εappS)|q⟩
> 
> where q runs over all plane-waves included in the basis set. Instead of |q⟩ it is possible to chose a different complete set of vectors in Eq. (51). Note that Eq. (51) is equivalent to Eq. (48) if |q⟩ is replaced by the exact eigenvectors of the Hamiltonian H. This inspired Wood and Zunger [44] to use the eigenvectors |ai⟩ of a small approximate Hamiltonian H0 plus a set of plane-waves to make a complete set. The Hamiltonian H0 might be calculated for a plane-wave basis set consisting of N0 plane-waves; this results in a preconditioning matrix 其中q遍历基组中包含的所有平面波。在式(51)中，可以用不同的完备向量集代替|q⟩。注意，如果|q⟩替换为哈密顿量H的精确本征向量，则式(51)等价于式(48)。这启发Wood和Zunger [44]使用一个小近似哈密顿量H0的本征向量|ai⟩加上一组平面波来构成完备集。哈密顿量H0可针对由N0个平面波组成的基组计算；这导致预条件矩阵
> 
> K = - Σi=1N0 |ai⟩⟨ai| / ⟨ai|(H - εappS)|ai⟩ - Σq' |q⟩⟨q| / ⟨q|(H - εappS)|q⟩ K = - Σi=1N0 |ai⟩⟨ai| / ⟨ai|(H - εappS)|ai⟩ - Σq' |q⟩⟨q| / ⟨q|(H - εappS)|q⟩
> 
> where the prime in the second sum means exclusion of all plane waves included in the initial Hamiltonian H0. We have tested this preconditioning to some extent and it works reasonably well for small to medium sized problems (NPW < 1000), but for large basis sets (NPW > 1000) the size N0 of the initial matrix soon becomes the limiting factor. If the initial size is equal to the number of bands N0 = Nb, the improvement over the diagonal approximation Eq. (51) is small. If N0 is considerably larger than Nb (N0 > 3 Nb) the calculation of the first sum in Eq. (52) becomes the most expensive part of the calculation. Therefore, we actually adopted the preconditioning function proposed by Teter et al. [10] 其中第二项求和的撇号表示排除初始哈密顿量H0中包含的所有平面波。我们已在一定程度上测试了这种预条件，对于中小规模问题（NPW < 1000）效果相当好，但对于大基组（NPW > 1000），初始矩阵的大小N0很快成为限制因素。如果初始大小等于能带数N0 = Nb，则相对于对角近似式(51)的改进很小。如果N0远大于Nb（N0 > 3 Nb），式(52)中第一项求和的计算成为计算中最昂贵的部分。因此，我们实际上采用了Teter等人[10]提出的预条件函数
> 
> K = Σq |q⟩⟨q| × (27 + 18x + 12x² + 8x³) / (27 + 18x + 12x² + 8x³ + 16x⁴) × x K = Σq |q⟩⟨q| × (27 + 18x + 12x² + 8x³) / (27 + 18x + 12x² + 8x³ + 16x⁴) × x
> 
> with x = ħ²q²/(2me) / εkin(R), and εkin(R) being the kinetic energy of the residual vector. There are only two changes with respect to Ref. [10]: First, we use ½εkin(R) instead of εkin(R) in the definition of x, resulting in a slightly improved convergence speed for most elements. Second, we multiply the preconditioning function by a constant factor 2/(εkin(R)). Using this factor the diagonal part of the preconditioning matrix K converges to 其中x = ħ²q²/(2me) / εkin(R)，εkin(R)是残差向量的动能。相对于参考文献[10]仅有两个变化：第一，我们在x的定义中使用½εkin(R)而非εkin(R)，对大多数元素收敛速度略有改善。第二，我们将预条件函数乘以常数因子2/(εkin(R))。使用此因子，预条件矩阵K的对角部分收敛于
> 
> K → -2me/(ħ²q²) K → -2me/(ħ²q²)
> 
> for large q, resulting in a more convenient length of the correction vector |δφn⟩. Although the length of the correction vector does not enter in any of the schemes discussed in the next sections, it is important to have a reasonable length for the algorithm in which the KS functional is minimized directly (see Section 5). Slightly different preconditioning functions were proposed by several other authors: Furthmüller [47] and recently Tassone et al. [7] used the matrix 对于大q，使得修正向量|δφn⟩的长度更合适。尽管修正向量的长度不进入下节讨论的任何方案，但对于直接最小化KS泛函的算法（见第5节），具有合理的长度是重要的。其他几位作者提出了稍有不同的预条件函数：Furthmüller [47]和最近的Tassone等人[7]使用了矩阵
> 
> K = - Σq |q⟩⟨q| × { 1, q ≤ qcut ; qcut²/q², q > qcut } K = - Σq |q⟩⟨q| × { 1, q ≤ qcut ; qcut²/q², q > qcut }
> 
> The functional form of this matrix is very similar to Eq. (53) and requires the determination of an optimum cut off qcut. Generally it does not improve the convergence speed in comparison to the ‘smoother’ preconditioning function (53). 该矩阵的函数形式与式(53)非常相似，且需要确定最佳截断qcut。通常，与“更平滑”的预条件函数(53)相比，它不会改善收敛速度。
> 
> 3.2. Blocked Davidson scheme 3.2. 分块Davidson方案
> 
> This method was originally proposed by Davidson [48] and later modified by Liu for a simultaneous update of all bands [49]. The expansion set increases in each step M by Nb - where Nb is the number of bands included in the calculation Nb ≥ Nelect/2 residual vectors 该方法最初由Davidson [48]提出，后由Liu [49]修改用于所有能带的同时更新。展开集在每一步M增加Nb个残差向量——其中Nb是计算中包含的能带数，Nb ≥ Nelect/2
> 
> {|bi⟩, i = 1, …, Nb(M+1)} = {|φn0⟩, n = 1, …, Nb; |Pn1⟩, n = 1, …, Nb; |Pn2⟩, …} {|bi⟩, i = 1, …, Nb(M+1)} = {|φn0⟩, n = 1, …, Nb; |Pn1⟩, n = 1, …, Nb; |Pn2⟩, …}
> 
> |PnM⟩ = K|R(φnM⟩) are the preconditioned residual vectors for the initial wavefunctions. In each iteration M the Rayleigh-Ritz scheme is used to obtain the lowest eigenvalue/eigenvector pairs εα, |φ̃α⟩. From these eigenvectors the new preconditioned residual vectors |PnM+1⟩ = K|R(φ̃n)⟩ are calculated and added to the expansion set. For large problems the storage of all previous residual vectors and of the initial vectors |φn0⟩ becomes a problem, therefore M must be restricted to a relatively small value. In our case we generally use M = 1: In each step the final expansion set consists of 2Nb vectors, the preconditioned residual vectors {|Pn⟩} and the initial set {|φn0⟩}. Then a diagonalization is performed in this 2Nb-dimensional sub-space, and the Nb lowest eigenvectors are calculated. In the next step these lowest eigenvectors and the new residual vectors form the new expansion set. For a selfconsistent calculation usually two steps are necessary between the charge density mixing. After the charge density mixing the final wavefunctions of the previous step are used as new initial trial vectors. We will refer to this algorithm as DAV2, for DAV2 one step always consist of 2 successive simple blocked Davidson steps. |PnM⟩ = K|R(φnM⟩)是初始波函数的预条件残差向量。在每次迭代M中，使用Rayleigh-Ritz方案获得最低本征值/本征向量对εα, |φ̃α⟩。从这些本征向量计算新的预条件残差向量|PnM+1⟩ = K|R(φ̃n)⟩并添加到展开集中。对于大问题，存储所有之前的残差向量和初始向量|φn0⟩成为问题，因此M必须限制在相对较小的值。在我们的情况中，我们通常使用M = 1：在每一步中，最终展开集由2Nb个向量组成，即预条件残差向量{|Pn⟩}和初始集{|φn0⟩}。然后在这个2Nb维子空间中进行对角化，并计算Nb个最低本征向量。在下一步中，这些最低本征向量和新的残差向量形成新的展开集。对于自洽计算，通常在电荷密度混合之间需要两步。电荷密度混合后，前一步的最终波函数用作新的初始试探向量。我们将此算法称为DAV2，对于DAV2，一步总是由两个连续的简单分块Davidson步骤组成。
> 
> 3.3. Unblocked algorithms 3.3. 非分块算法
> 
> Unblocked or sequential algorithms are generally considered to be ‘slower’ than blocked algorithms, nevertheless the blocked Davidson scheme requires the storage of at least 2Nb vectors, which is inconvenient for large systems. Schemes which optimize a single band at a time require less storage, and as we will show they are also more efficient for very large systems, because the number of iterations can be larger than in the blocked Davidson scheme. Generally it is favorable to restrict the search vector in the sequential methods to the sub-space orthonormal to the current wavefunctions. After a band-by-band sequential update of all wavefunctions it is necessary to determine the optimal wavefunctions in the subspace spanned by the Nb final trial wavefunctions ({|φ̃n⟩, n = 1, …, Nb}) using the Rayleigh-Ritz scheme (Eqs. (43)-(45)). We will refer to this step as sub-space diagonalization or sub-space rotation. In any efficient sequential scheme sub-space rotation and sequential update should alternate. 非分块或顺序算法通常被认为比分块算法“慢”，然而分块Davidson方案需要存储至少2Nb个向量，这对大系统不方便。一次优化一个能带的方案需要更少的存储，并且正如我们将展示的，它们对于非常大的系统也更高效，因为迭代次数可以比分块Davidson方案更多。通常，在顺序方法中将搜索向量限制在与当前波函数正交归一的子空间是有利的。在逐带顺序更新所有波函数之后，有必要使用Rayleigh-Ritz方案（式(43)-(45)）在Nb个最终试探波函数({|φ̃n⟩, n = 1, …, Nb})张成的子空间中确定最佳波函数。我们将此步骤称为子空间对角化或子空间旋转。在任何高效的顺序方案中，子空间旋转和顺序更新应交替进行。
> 
> 3.4. Correction vector for sequential, band-by-band methods 3.4. 顺序逐带方法的修正向量
> 
> Generally the correction vector must be chosen with a little bit more care in the sequential methods. Consider that one specific band m has to be optimized: As already pointed out, it is convenient in the sequential methods to restrict the search direction for this band m to the sub-space orthogonal to the current trial set {|φn⟩, n = 1, …, Nb}. This can be done easily using e.g. the Lagrange formalism: Minimization of the Rayleigh quotient with the additional orthonormality constraint 通常，在顺序方法中，修正向量的选择必须更加小心。考虑某特定能带m需要优化：如前所述，在顺序方法中，将该能带m的搜索方向限制在与当前试探集{|φn⟩, n = 1, …, Nb}正交的子空间是方便的。这可以容易地使用例如拉格朗日形式实现：在附加正交归一约束下最小化瑞利商
> 
> Σn γmn (⟨φm|S|φn⟩ - δmn) = 0 ∀ n = 1, …, Nb, Σn γmn (⟨φm|S|φn⟩ - δmn) = 0 ∀ n = 1, …, Nb,
> 
> results in a gradient vector 得到一个梯度向量
> 
> |g(φm)⟩ = H|φm⟩ - Σn γmnS|φn⟩. |g(φm)⟩ = H|φm⟩ - Σn γmnS|φn⟩.
> 
> which can be made orthonormal to the current trial set by requiring 通过要求
> 
> ⟨φn|gm⟩ = 0 ∀ n = 1, …, Nb, ⟨φn|gm⟩ = 0 ∀ n = 1, …, Nb,
> 
> and after evaluating the Lagrange multipliers explicitly we obtain 并显式计算拉格朗日乘子后，我们得到
> 
> |g(φm)⟩ = (1 - Σn S|φn⟩⟨φn|) H|φm⟩. |g(φm)⟩ = (1 - Σn S|φn⟩⟨φn|) H|φm⟩.
> 
> For a set of trial wavefunctions which diagonalizes the Hamiltonian, i.e. ⟨φn|H|φm⟩ = δnm εapp, Eq. (60) reduces simply to the residual vector (47). Mind that the gradient vector allows to calculate the first order change of the Rayleigh quotient εapp (Eq. (46)) using 对于对角化哈密顿量的一组试探波函数，即⟨φn|H|φm⟩ = δnm εapp，式(60)简化为残差向量(47)。注意，梯度向量允许使用下式计算瑞利商εapp（式(46)）的一阶变化
> 
> dεapp = ⟨δφm|gm⟩ + c.c., dεapp = ⟨δφm|gm⟩ + c.c.,
> 
> where c.c. is the complex-conjugate of the first expression. The choice of the constraint (59), which actually determines the Lagrange multipliers, is inspired by the requirement of getting correct first-order energy changes: For a change |δφm⟩ parallel to any vector contained in the set {φn}, the energy change, given by Eq. (61) should be zero. Because in our implementation the sequential band-by band algorithms generally alternate with the sub-space rotation, it is reasonable to replace the exact gradient (60) with its ‘diagonal’ approximation the residual vector given by Eq. (47). The residual is preconditioned and then explicitly S-orthogonalized to the set {φn}, i.e. 其中c.c.是第一个表达式的复共轭。约束(59)的选择实际上决定了拉格朗日乘子，其灵感来自获得正确一阶能量变化的要求：对于与集合{φn}中任何向量平行的变化|δφm⟩，由式(61)给出的能量变化应为零。因为在我们的实现中，顺序逐带算法通常与子空间旋转交替进行，所以用其“对角”近似——式(47)给出的残差向量——替换精确梯度(60)是合理的。残差被预条件化，然后显式S-正交化到集合{φn}，即
> 
> |P(φm)⟩ = |Pm⟩ = (1 - Σn S|φn⟩⟨φn|) K (H - εappS)|φm⟩. |P(φm)⟩ = |Pm⟩ = (1 - Σn S|φn⟩⟨φn|) K (H - εappS)|φm⟩.
> 
> This preconditioned ‘search vector’ fulfills the condition 此预条件“搜索向量”满足条件
> 
> ⟨φn|S|Pm⟩ = 0 ∀ n = 1, …, Nb. ⟨φn|S|Pm⟩ = 0 ∀ n = 1, …, Nb.
> 
> The sequential methods differ in the way this correction vector is added to the wavefunctions {φm}. 顺序方法的不同之处在于此修正向量如何添加到波函数{φm}中。
> 
> 3.5. Unblocked Davidson-like update 3.5. 非分块类Davidson更新
> 
> In the conventional unblocked Davidson method a single preconditioned correction vector K|R(φm)⟩ is added to the expansion set {bi} at each iteration. At startup the expansion set consists of the current set of trial wavefunctions, therefore the expansion set is given in each iteration by the set 在传统的非分块Davidson方法中，每次迭代将单个预条件修正向量K|R(φm)⟩添加到展开集{bi}中。开始时，展开集由当前试探波函数集组成，因此每次迭代的展开集由集合
> 
> {|bi⟩, i = 1, …, Nb+M} = {|φn0⟩, n = 1, …, Nb; |Pm1⟩; |Pm2⟩; …} {|bi⟩, i = 1, …, Nb+M} = {|φn0⟩, n = 1, …, Nb; |Pm1⟩; |Pm2⟩; …}
> 
> 给出。如果优化能带m，则在第一次迭代中，从初始试探向量计算预条件残差|Pm0⟩ = K|R(φm0⟩)并添加到展开集中，应用Rayleigh-Ritz方案计算新的最佳|φm⟩。在下一步中，从新波函数|φm⟩计算预条件残差|Pm1⟩ = K|R(φm⟩)并再次添加到展开集中。该方案相对不便，且需要每一步对角化一个大矩阵。为简化方案，我们首先用预条件梯度|PmM⟩ = |P(φmM⟩)（式(62)）替换|PmM⟩。通过观察，我们发现这不会改变迭代方案的结果，但Rayleigh-Ritz方案中的重叠矩阵Sij（式(44)）对于i或j ≤ Nb且i, j ≠ m现在简化为单位矩阵。其次，在Hij（式(44)）中，对于i或j ≤ Nb且i, j ≠ m，忽略非对角元。这导致向量集{|φn⟩, i = 1, …, Nb; i ≠ m}和{|φm1⟩/|Pm1⟩/|Pm2⟩/…}的简单“解耦”，仅需对角化一个小得多的矩阵。总结：在这种情况下，展开集以试探向量|φm0⟩开始，并在连续迭代M中添加预条件且正交归一化的梯度|PmM⟩ = |P(φmM⟩)：
> 
> {|bi⟩, i = 1, …, M} = {|φm0⟩; |Pm1⟩; |Pm2⟩; …} {|bi⟩, i = 1, …, M} = {|φm0⟩; |Pm1⟩; |Pm2⟩; …}
> 
> 在每次迭代中，使用Rayleigh-Ritz方案从该展开集计算最佳波向量|φmM⟩。在更新一个态数次后，移至下一个能带，最后对所有最终波函数({|φ̃n⟩, n = 1, …, Nb})进行子空间旋转。最后的子空间旋转是严格必要的，以获得精确基态本征向量。没有子空间旋转，该方案将收敛到精确最低本征向量的任意线性组合。
> 
> 3.6. Conjugate gradient minimization 3.6. 共轭梯度最小化
> 
> It is possible to reduce the number of numerical operations even further by applying the ideas of conjugated gradients (CG) [50,51]. In the context of a sequential energy minimization this was first done by Teter et al. [10], and the same algorithm was also used by Bylander, Kleinman and Lee [45] for the iterative diagonalization of the KS-Hamiltonian. Instead of storing all previous preconditioned gradients it is possible to conjugate each new search direction to the previous directions applying a standard conjugate gradient scheme, i.e. the search direction |fM⟩ for iteration M is now given by 通过应用共轭梯度（CG）[50,51]的思想，可以进一步减少数值操作次数。在顺序能量最小化的背景下，这首先由Teter等人[10]完成，同样的算法也被Bylander、Kleinman和Lee [45]用于KS哈密顿量的迭代对角化。无需存储所有之前的预条件梯度，而是可以应用标准共轭梯度方案将每个新搜索方向与之前方向共轭，即迭代M的搜索方向|fM⟩现在由下式给出
> 
> |fM⟩ = |PM⟩ + (⟨PM|gM⟩ - ⟨PM-1|gM⟩) / ⟨PM-1|gM-1⟩ |fM-1⟩. |fM⟩ = |PM⟩ + (⟨PM|gM⟩ - ⟨PM-1|gM⟩) / ⟨PM-1|gM-1⟩ |fM-1⟩.
> 
> In this equation |gM⟩ = |g(φM)⟩ is the gradient vector defined in Eq. (60) and |PM⟩ = |P(φM)⟩ is the preconditioned gradient defined in Eq. (62). In each iteration the optimum new wave vector |φM+1⟩ is determined from the set {|φM⟩, |fM⟩} applying the Rayleigh-Ritz scheme. In Eq. (66) it is possible to replace the gradient vector |gM⟩ by the residual vector |RM⟩ because the preconditioned gradient is orthogonal to all wavefunctions and therefore ⟨PM|gM⟩ = ⟨PM|RM⟩. Except for small (mainly numerical) rounding errors, the improvement per iteration is the same for the conjugate gradient minimization and for the scheme introduced in the previous section (Eq. (65)), and we will restrict the following discussions to the computationally slightly more efficient CG algorithm. 在该方程中，|gM⟩ = |g(φM)⟩是式(60)中定义的梯度向量，|PM⟩ = |P(φM)⟩是式(62)中定义的预条件梯度。在每次迭代中，应用Rayleigh-Ritz方案从集合{|φM⟩, |fM⟩}确定最佳新波向量|φM+1⟩。在式(66)中，可以用残差向量|RM⟩替换梯度向量|gM⟩，因为预条件梯度与所有波函数正交，因此⟨PM|gM⟩ = ⟨PM|RM⟩。除了小的（主要是数值的）舍入误差外，共轭梯度最小化和上一节介绍的方案（式(65)）每次迭代的改进是相同的，我们将后续讨论限制在计算上稍高效的CG算法。
> 
> 3.7. Residual minimization method - direct inversion in the iterative subspace (RMM-DIIS) 3.7. 残差最小化方法——迭代子空间直接反演（RMM-DIIS）
> 
> The sequential conjugate gradient scheme discussed so far is relatively fast and very stable. The only remaining drawback is the necessity for an explicit orthonormalization of the preconditioned residual vector K|R(φm)⟩ to the current set of trial wavefunctions (Eq. (62)). Unfortunately avoiding the orthonormalization is not possible applying the algorithms discussed above. The Rayleigh-Ritz scheme tries to obtain the lowest possible eigenvalues in the sub-space spanned by the expansion set, actually it is easy to show that the algorithm minimizes the Rayleigh quotient for a given set of wavefunctions. The Rayleigh quotient is stationary at each eigenvector but it does not possess a minimum. Without explicit orthonormalization (62) the schemes investigated in Sections 3.5 and 3.6 will converge for any start vector to the lowest eigenvector of the Hamiltonian. In this case the algorithms are equivalent to a simple Lanczos [44,52] method, only the explicit orthonormalization makes it possible to converge to a selected eigenvalue efficiently. Fortunately a solution to this problem is available and was first proposed in Ref. [44]. Minimizing the norm of the residual vector instead of the Rayleigh quotient makes the orthonormalization unnecessary, because the norm of the residual vector has an unconstrained minimum at each eigenvector. 迄今为止讨论的顺序共轭梯度方案相对快速且非常稳定。唯一剩下的缺点是需要将预条件残差向量K|R(φm)⟩显式正交归一化到当前试探波函数集（式(62)）。不幸的是，应用上述算法无法避免正交归一化。Rayleigh-Ritz方案试图在展开集张成的子空间中获得尽可能低的本征值，实际上容易证明该算法对于给定波函数集最小化瑞利商。瑞利商在每个本征向量处是稳定的，但它不具有最小值。没有显式正交归一化(62)，第3.5和3.6节研究的方案将对任何起始向量收敛到哈密顿量的最低本征向量。在这种情况下，算法等价于简单的Lanczos [44,52]方法，只有显式正交归一化使得能够高效地收敛到选定的本征值。幸运的是，这个问题有解决方案，并首先在参考文献[44]中提出。最小化残差向量的范数而非瑞利商使得正交归一化变得不必要，因为残差向量的范数在每个本征向量处具有无约束最小值。
> 
> In our implementation we follow the original work of Pulay [24] and not the variant proposed by Wood et al. [44]. This variant would require the additional calculation and storage of S|φn⟩, and is therefore slower than our algorithm. We start with an evaluation of the preconditioned residual vector K|R0⟩ = K|R(φ0)⟩ for a selected band m. Then a trial step into this direction is done 在我们的实现中，我们遵循Pulay [24]的原始工作，而非Wood等人[44]提出的变体。该变体需要额外计算和存储S|φn⟩，因此比我们的算法慢。我们从计算选定能带m的预条件残差向量K|R0⟩ = K|R(φ0)⟩开始。然后沿此方向进行一个试探步骤
> 
> |φ1⟩ = |φ0⟩ + λ K|R0⟩ |φ1⟩ = |φ0⟩ + λ K|R0⟩
> 
> and the new residual vector |R1⟩ = |R(φ1)⟩ is evaluated (mind that we update εapp in the evaluation of R(φ), see Eq. (47)). Next a linear combination of the initial |φ0⟩ and the trial wavefunction |φ1⟩ 并计算新的残差向量|R1⟩ = |R(φ1)⟩（注意我们在计算R(φ)时更新εapp，见式(47)）。接下来，找到初始|φ0⟩和试探波函数|φ1⟩的线性组合
> 
> |φ̃⟩ = Σi=0M αi |φi⟩ |φ̃⟩ = Σi=0M αi |φi⟩
> 
> which minimizes the norm of the residual vector. Assuming linearity in the residual vector i.e. 该组合最小化残差向量的范数。假设残差向量是线性的，即
> 
> |R(φ̃)⟩ = Σi=0M αi |Ri⟩ |R(φ̃)⟩ = Σi=0M αi |Ri⟩
> 
> this requires the minimization of 这需要最小化
> 
> Σi,j αi _⟨Ri|Rj⟩ αj. Σi,j αi_ ⟨Ri|Rj⟩ αj.
> 
> This step is usually called direct inversion in the iterative subspace (DIIS). The problem stated in Eq. (70) is equivalent to solving the Hermitian eigenvalue problem 此步骤通常称为迭代子空间直接反演（DIIS）。式(70)中所述的问题等价于求解厄米本征值问题
> 
> Σj ⟨Ri|Rj⟩ αj = λ αi. Σj ⟨Ri|Rj⟩ αj = λ αi.
> 
> The next trial step starts from |φ̃⟩ along the direction K|RM⟩. In each iteration M a new wavefunction |φM⟩ = |φ̃M-1⟩ + λ K|RM-1⟩ and a new residual vector |R(φM)⟩ are added to the iterative sub-space. The size of the trial step λ is a critical value. We have found that a reasonable choice for the trial step can be obtained from the minimization of the Rayleigh quotient along the search direction in the first step (this is in the spirit of Section 3.5), this optimal λ is used until a move to the next band is performed. The line minimization can be done without additional computational requirements. Usually the obtained step size is between 0.3 and 1 for the preconditioning function given in Eq. (53). In rare cases - especially if the minimization of the Rayleigh quotient starts to go for the wrong band - the trial step might become very large. Therefore we restrict the size of the trial step to a value between 0.1 and 1. With this choice we have found that it is always possible to finish with the trial step. The trial step approaches already the exact position of the minimal residual vector. The scheme explained in this section requires approximately the same number of iterations as the CG algorithm, but it avoids any explicit orthonormalization and is therefore much faster for very large problems where the orthonormalization is the leading factor. Even more important is the fact that the residual minimization is inherently local, and it is therefore very easy to implement the algorithm on a parallel machine. For instance each processor might handle a certain number of bands, information about other bands is not required (see also Section 3.9). One drawback of the RMM method is that it always finds the vector which is closest to the initial trial vector. Therefore, initialization becomes a critical task and it might happen that in the final solution one vector is ‘missing’. To avoid this the initialization must be done with great care: We usually start with a set of random trial vectors, and perform three sweeps over all bands. Each initial sweep consists of one sub-space rotation and two steepest descent steps into the direction of the preconditioned residual vectors (Eq. (67)) per band (see also Section 3.8). During this initial phase the Hamiltonian is also kept fixed, after this ‘delay’ we switch to the RMM scheme and start to update the potential. As already explained sub-space rotation and sequential update of the bands alternate. In the residual minimization the final vectors are no longer orthogonal. Applying the Rayleigh-Ritz scheme the vectors are correctly orthonormalized. We want to emphasize, that in principle the RMM method would also converge without any explicit sub-space rotation or orthonormalization, but for current system sizes we have found that the sub-space rotation speeds up the calculations although it is an order O(N3) operation (see Section 3.1). The main problem is that the ‘barrier’ in the norm of the residual vector between two neighboring eigenvectors with eigenvalues ε and ε + δε is only of the order δε [53]. Therefore two eigenvectors which are close in energy are lying in one long steep valley and only a shallow hill separates them - a typical example of a badly conditioned minimization problem. The sub-space rotation solves this problem because after the rotation the residual vectors are orthonormal to the current trial set (see explanation following Eq. (60)), and search vectors parallel to the long valleys are effectively suppressed. 下一个试探步骤从|φ̃⟩沿方向K|RM⟩开始。在每次迭代M中，新的波函数|φM⟩ = |φ̃M-1⟩ + λ K|RM-1⟩和新的残差向量|R(φM)⟩被添加到迭代子空间中。试探步长λ是一个关键值。我们发现，可以通过第一步中沿搜索方向最小化瑞利商来获得合理的试探步长（这符合第3.5节的精神），该最优λ一直使用到移至下一个能带。线最小化可以在没有额外计算要求的情况下完成。对于式(53)给出的预条件函数，通常获得的步长在0.3到1之间。在罕见情况下——特别是当瑞利商最小化开始走向错误的能带时——试探步长可能变得非常大。因此，我们将试探步长限制在0.1到1之间。通过这种选择，我们发现总是可以完成试探步骤。试探步骤已接近最小残差向量的精确位置。本节解释的方案需要与CG算法大致相同的迭代次数，但它避免了任何显式正交归一化，因此对于正交归一化成为主导因素的大问题，其速度快得多。更重要的是，残差最小化本质上是局域的，因此很容易在并行机上实现该算法。例如，每个处理器可以处理一定数量的能带，不需要其他能带的信息（另见第3.9节）。RMM方法的一个缺点是它总是找到最接近初始试探向量的向量。因此，初始化成为关键任务，并且可能发生最终解中“缺失”一个向量的情况。为避免这种情况，初始化必须非常小心地进行：我们通常从一组随机试探向量开始，并对所有能带进行三次扫描。每次初始扫描包括一次子空间旋转和每能带两次沿预条件残差向量方向的最陡下降步骤（式(67)）（另见第3.8节）。在此初始阶段，哈密顿量也保持不变，在此“延迟”之后，我们切换到RMM方案并开始更新势。如前所述，子空间旋转和能带的顺序更新交替进行。在残差最小化中，最终向量不再正交。应用Rayleigh-Ritz方案，向量被正确正交归一化。我们要强调，原则上RMM方法无需任何显式子空间旋转或正交归一化也能收敛，但对于当前体系大小，我们发现子空间旋转加速了计算，尽管它是O(N3)操作（见第3.1节）。主要问题在于，相邻本征向量（本征值为ε和ε + δε）之间在残差向量范数中的“势垒”仅为δε量级[53]。因此，两个能量接近的本征向量位于一条长陡谷中，仅有浅丘分隔——这是病态最小化问题的典型例子。子空间旋转解决了这个问题，因为旋转后残差向量与当前试探集正交归一（见式(60)后的解释），并且平行于长谷的搜索向量被有效抑制。
> 
> **direct inversion in the iterative subspace (DIIS)**: 迭代子空间直接反演，一种通过最小化残差范数来加速迭代收敛的方法。
> 
> 3.8. The complete algorithm 3.8. 完整算法
> 
> The complete selfconsistency loop consists of several steps (the section where the algorithm has been discussed is given in brackets, also see Fig. 3): sub-space rotation (3), DAV2 (3.2), CG (3.6) or RMM (3.7) algorithm, orthonormalization using Gram-Schmidt method (only required for the RMM scheme), update of partial occupancies and charge density for a selfconsistent calculation. The initial trial set ({|φn⟩, n = 1, …, Nb}) in each iteration is equivalent to the final set of the previous iteration, initialization is usually done with a random number generator. This loop is repeated until selfconsistency is reached, for a non-selfconsistent calculation no charge density update is done. The orthonormalization is only necessary in conjunction with the RMM, in addition the DAV2 method requires no sub-space rotation. We have found that the sub-space rotation should be performed between the update of the charge density and the RMM or CG algorithm, especially at the beginning of a selfconsistent calculation. In this case the calculated residual vectors |R(φm)⟩ agree with the exact gradients |g(φm)⟩. For this reason and because the wavefunctions should be orthonormal for a recalculation of the charge density, it is necessary to separate the orthonormalization and the diagonalization of the sub-space Hamiltonian, which is done at once in the Rayleigh-Ritz scheme. In addition it is necessary to find an optimal break condition for the sequential RMM and CG algorithms. A static criterion, for example 2 steps per band, is not a good choice, because lower bands converge much faster than higher bands. Therefore, we have adopted the following dynamic criterion (which is inspired by Ref. [54]): (i) Both algorithms are stopped if the change in the total eigenvalue 完整的自洽循环由几个步骤组成（括号中给出了讨论该算法的章节，另见图3）：子空间旋转(3)、DAV2(3.2)、CG(3.6)或RMM(3.7)算法、使用Gram-Schmidt方法的正交归一化（仅RMM方案需要）、更新部分占据数和电荷密度以进行自洽计算。每次迭代中的初始试探集({|φn⟩, n = 1, …, Nb})等价于前一次迭代的最终集，初始化通常使用随机数生成器完成。该循环重复直至达到自洽性，对于非自洽计算，不进行电荷密度更新。正交归一化仅在与RMM结合时需要，此外DAV2方法不需要子空间旋转。我们发现，子空间旋转应在电荷密度更新与RMM或CG算法之间进行，特别是在自洽计算开始时。在这种情况下，计算的残差向量|R(φm)⟩与精确梯度|g(φm)⟩一致。出于这个原因，并且因为波函数应为正交归一以重新计算电荷密度，有必要将正交归一化与子空间哈密顿量的对角化分开，这在Rayleigh-Ritz方案中一次完成。此外，需要为顺序RMM和CG算法找到最佳中断条件。静态标准，例如每能带2步，不是一个好的选择，因为低能带收敛比高能带快得多。因此，我们采用了以下动态标准（受参考文献[54]启发）：(i) 如果总能带的变化
> 
> Σn |Δεn| < εaccuracy / Nb / 4 Σn |Δεn| < εaccuracy / Nb / 4
> 
> becomes smaller than εaccuracy/Nb/4, where εaccuracy is the required accuracy of the calculation and Nb is the number of occupied bands. (ii) The RMM is stopped if the square of the norm of the residual vector gets smaller than 30% of its initial value, and the minimization always stops with the trial step. (iii) The CG is stopped if the change in the eigenvector gets smaller than 30% of the change in the first i.e. the steepest descent step. (iv) The maximum number of steps is always four. For the RMM the residual vector is minimized three times and at last a fourth trial step is performed. (v) Empty bands are optimized only twice. By now, these criteria have been used for a large number of system and are very robust. In most cases two CG or two RMM steps are done per band, but problematic eigenvalue/eigenvector pairs are iterated more frequently. Usually more iterations are done for the higher bands, and the total speed of convergence for all bands is very good. 小于εaccuracy/Nb/4，则两种算法均停止，其中εaccuracy是计算所需的精度，Nb是占据能带数。(ii) 如果残差向量范数的平方小于其初始值的30%，则RMM停止，且最小化总以试探步骤结束。(iii) 如果本征向量的变化小于第一步（即最陡下降步）变化的30%，则CG停止。(iv) 最大步数总是4。对于RMM，残差向量最小化三次，最后执行第四次试探步骤。(v) 空带仅优化两次。到目前为止，这些标准已用于大量体系，且非常稳健。在大多数情况下，每能带执行两次CG或两次RMM步骤，但有问题的本征值/本征向量对会更频繁地迭代。通常对高能带进行更多迭代，且所有能带的总收敛速度非常好。
> 
> 3.9. Computational considerations 3.9. 计算考虑
> 
> To make a fair comparison of different techniques it is necessary to count the number of operations for each algorithm carefully. The CG minimization of the Rayleigh quotient requires always slightly less evaluations of the Hamiltonian multiplied with a wavefunction than the RMM, but for large systems the most expensive part is the orthonormalization of the wavefunctions. For our implementation the evaluation of (H - εS)|φ⟩ is an order 为公平比较不同技术，必须仔细计算每种算法的操作数。瑞利商的CG最小化总是比RMM需要稍少的哈密顿量乘以波函数的计算次数，但对于大体系，最昂贵的部分是波函数的正交归一化。对于我们的实现，计算(H - εS)|φ⟩是
> 
> TH = Nb NPW ln NPW ≈ N2 ln N TH = Nb NPW ln NPW ≈ N2 ln N
> 
> operation, where N qualifies the system size. The limiting factors are the fast Fourier transformations (Nb NPW ln NPW ≈ N2 ln N) and the evaluation of the nonlocal projection operators. For large systems we calculate the non-local projection operators in real space [55] and therefore the number of operations per band increases linearly with the system size (∝ Nloc), for all bands this is only an order N2 operation. The Gram-Schmidt orthonormalization takes 量级的操作，其中N表征体系大小。限制因素是快速傅里叶变换（Nb NPW ln NPW ≈ N2 ln N）和非局域投影算符的计算。对于大体系，我们在实空间计算非局域投影算符[55]，因此每能带的操作数随体系大小线性增长（∝ Nloc），对于所有能带，这仅是N2量级的操作。Gram-Schmidt正交归一化需要
> 
> TGS = Nb2 × NPW ≈ N3 TGS = Nb2 × NPW ≈ N3
> 
> steps, whereas the explicit orthogonalization of the gradients of each band to all other bands in Eq. (62) takes twice as many steps 步，而式(62)中每个能带的梯度对所有其他能带的显式正交化需要两倍的步数
> 
> Tort = 2 Nb2 × NPW ≈ 2 N3. Tort = 2 Nb2 × NPW ≈ 2 N3.
> 
> But even worse, the explicit orthogonalization makes any efficient memory caching impossible. The CG algorithm is strictly sequential and at each iteration the new gradient must be orthogonalized to all other bands, requiring a large band width from the main memory. We found that this is a problem on some machines like the Silicon Graphics Power Challenge architecture where several processors share a large main memory (on vector processors this operation is generally reasonably fast). For the Gram-Schmidt orthonormalization a routine with good data locality which avoids this problem can be found easily and Tort is therefore usually 3-10 times larger than TGS on scalar machines. Efficient routines with good data locality can also be found for the sub-space rotation, and the number of operations is 但更糟糕的是，显式正交化使得任何高效的内存缓存变得不可能。CG算法是严格顺序的，且每次迭代中新梯度必须对所有其他能带正交化，需要从主内存获取大量带宽。我们发现在某些机器上，如Silicon Graphics Power Challenge架构（多个处理器共享大主内存），这是一个问题（在向量处理器上，此操作通常相当快）。对于Gram-Schmidt正交归一化，可以容易地找到具有良好数据局部性、避免此问题的例程，因此Tort在标量机器上通常比TGS大3-10倍。也可以为子空间旋转找到具有良好数据局部性的高效例程，操作数为
> 
> Tdiag = TH + 2 Nb2 × NPW. Tdiag = TH + 2 Nb2 × NPW.
> 
> For the blocked Davidson scheme the number of operations is 对于分块Davidson方案，操作数为
> 
> Tdav = 2 TH + 5 Nb2 × NPW Tdav = 2 TH + 5 Nb2 × NPW
> 
> for the first iteration and 对于第一次迭代，以及
> 
> Tdav = 1 TH + 4 Nb2 × NPW Tdav = 1 TH + 4 Nb2 × NPW
> 
> for all further iterations if the potential is fixed. As we will show in Section 6, two consecutive blocked Davidson steps (DAV2) are necessary to get a convergence speed that is comparable with the CG or RMM band-by-band methods. For large systems, where the orthogonalization is the leading factor, one blocked Davidson step (with only a single sweep over all bands) takes more time (and converges much slower) than one RMM-step (with two optimizations per band, one sub-space rotation and one Gram-Schmidt orthonormalization this is an order 3 TH + 3 Nb2 × NPW operation, to be compared with Eq. (76)). In addition we have found that two blocked Davidson steps for a fixed potential (DAV2) take generally more time than one CG sweep over all wavefunctions (approximately 3 TH + 5 Nb2 × NPW operations, to be compared with the sum of Eqs. (76) and (77)). For a comparison of the number of iterations required for each algorithm you might go to Section 6.1. 对于势固定时所有后续迭代。正如我们将在第6节中展示的，需要两个连续的分块Davidson步骤（DAV2）才能获得与CG或RMM逐带方法相当的收敛速度。对于正交化成为主导因素的大体系，一个分块Davidson步骤（仅对所有能带进行一次扫描）比一个RMM步骤（每能带两次优化、一次子空间旋转和一次Gram-Schmidt正交归一化，这是3 TH + 3 Nb2 × NPW量级的操作，与式(76)比较）耗时更多（且收敛更慢）。此外，我们发现对于固定势，两个分块Davidson步骤（DAV2）通常比一次对所有波函数的CG扫描耗时更多（约3 TH + 5 Nb2 × NPW操作，与式(76)和(77)之和比较）。关于每种算法所需迭代次数的比较，请参见第6.1节。
> 
> 4.  Charge density mixing
> 5.  电荷密度混合
> 
> The second key step within our algorithm is an efficient mixing of the input and output charge densities. We have adopted the modified Broyden method proposed by Johnson [56]. This approach is flexible and for a special parameter setting the charge density mixing schemes of Pulay [24] and that proposed by Srivastava [57] and Blügel [58] are obtained. To improve the convergence further, we have adopted a special initial mixing matrix and a metric, which are both optimized for a plane wave basis set. In the next sections we will briefly discuss simple mixing, Pulay’s and Johnson’s approaches. 我们算法中的第二个关键步骤是输入和输出电荷密度的高效混合。我们采用了Johnson [56]提出的改进Broyden方法。该方法灵活，且对于特定参数设置，可获得Pulay [24]以及Srivastava [57]和Blügel [58]提出的电荷密度混合方案。为进一步改善收敛性，我们采用了一种特殊的初始混合矩阵和度量，两者均针对平面波基组优化。在下文中，我们将简要讨论简单混合、Pulay方法和Johnson方法。
> 
> 4.1. Simple mixing 4.1. 简单混合
> 
> The central quantity of all charge density mixing schemes is the charge density residual R[ρin] (see Eq. (31)) 所有电荷密度混合方案的核心量是电荷密度残差R[ρin]（见式(31)）
> 
> R[ρin] = ρout[ρin] - ρin. R[ρin] = ρout[ρin] - ρin.
> 
> The norm of the residual vector 残差向量的范数
> 
> ⟨R[ρin]|R[ρin]⟩ ⟨R[ρin]|R[ρin]⟩
> 
> must be zero for selfconsistency. Simple schemes take into account only information from the current iteration. Linear mixing for example adds a certain amount of R to the current input charge density 自洽性要求必须为零。简单方案仅考虑来自当前迭代的信息。例如，线性混合将一定量的R加到当前输入电荷密度中
> 
> ρinm+1 = ρinm + γ R[ρinm]. ρinm+1 = ρinm + γ R[ρinm].
> 
> As in the case of the iterative matrix diagonalization (see Section 3.1), it is a good idea to improve the simple mixing by preconditioning the residual vector using knowledge about the Jacobian matrix. In this case the mixing equation is 与迭代矩阵对角化的情况（见第3.1节）一样，通过使用雅可比矩阵的知识对残差向量进行预条件来改进简单混合是个好主意。在这种情况下，混合方程为
> 
> ρinm+1 = ρinm + G1 R[ρinm] ρinm+1 = ρinm + G1 R[ρinm]
> 
> where G1 is a special preconditioning matrix. A simple but efficient scheme for a plane-wave basis set was proposed by Kerker [60], and we used this scheme with some success for the first calculations. In the Kerker scheme the preconditioning matrix is diagonal in reciprocal space and given by 其中G1是一个特殊的预条件矩阵。Kerker [60]为平面波基组提出了一种简单但高效的方案，我们最初的计算使用该方案取得了一些成功。在Kerker方案中，预条件矩阵在倒空间是对角的，并由下式给出
> 
> G1 = A q²/(q² + q₀²) G1 = A q²/(q² + q₀²)
> 
> This scheme has the advantage of damping the oscillations in the low-q components of the charge density i.e. for small wave vectors the function behaves like A q²/q₀² and mixes only a small amount of the output charge density to the input charge density. For large wave vectors q, a simple linear mixing with the linear mixing parameter A is done. Generally A can be quite large and we found that A = 0.8 is always an acceptable choice, q₀ might be optimized for the actual system. 该方案的优势在于阻尼电荷密度低q分量中的振荡，即对于小波向量，该函数行为类似于A q²/q₀²，仅将少量输出电荷密度混入输入电荷密度。对于大波向量q，进行简单的线性混合，线性混合参数为A。通常A可以相当大，我们发现A = 0.8始终是可接受的选择，q₀可根据实际体系优化。
> 
> 4.2. Pulay mixing 4.2. Pulay混合
> 
> In the scheme of Pulay [24] the input charge density and the residual vectors are stored for a number of mixing steps. A new optimal input charge density is obtained in each step as a linear combination of the input charge densities of all previous steps 在Pulay [24]的方案中，存储多个混合步骤的输入电荷密度和残差向量。在每一步中，新的最佳输入电荷密度作为所有先前步骤输入电荷密度的线性组合获得
> 
> ρinopt = Σi αi ρini. ρinopt = Σi αi ρini.
> 
> Assuming linearity of the residual vector with respect to the input charge density ρin, the residual at ρinopt is given by 假设残差向量关于输入电荷密度ρin是线性的，则ρinopt处的残差由下式给出
> 
> R[ρinopt] = R[Σi αi ρini] = Σi αi R[ρini]. R[ρinopt] = R[Σi αi ρini] = Σi αi R[ρini].
> 
> The optimal new charge density must minimize the norm of the residual vector 最佳新电荷密度必须最小化残差向量的范数
> 
> ⟨R[ρinopt]|R[ρinopt]⟩ ⟨R[ρinopt]|R[ρinopt]⟩
> 
> with respect to αi under the constraint 在约束
> 
> Σi αi = 1, Σi αi = 1,
> 
> which conserves the number of electrons. These equations are very similar to those given in Section 3.7, only the functional form of the constraint has changed. The optimal αi is now given by 下对αi进行。该约束保持电子数守恒。这些方程与第3.7节给出的非常相似，仅约束的函数形式有所改变。最佳αi现在由下式给出
> 
> αi = Σj Aij-1 / Σkj Akj-1 with Aij = ⟨R[ρini]|R[ρinj]⟩. αi = Σj Aij-1 / Σkj Akj-1 其中 Aij = ⟨R[ρini]|R[ρinj]⟩.
> 
> To improve the numerical stability and for comparison with the formulas given in the next section it is convenient to transform for iteration m to a new set of independent variables defined by 为提高数值稳定性并与下一节给出的公式比较，对于迭代m，方便地变换为一组新的独立变量，定义为
> 
> ρm = ρinm, Δρi = ρini+1 - ρini, ρm = ρinm, Δρi = ρini+1 - ρini,
> 
> Rm = R[ρinm], ΔRi = R[ρini+1] - R[ρini] Rm = R[ρinm], ΔRi = R[ρini+1] - R[ρini]
> 
> for i < m. The new optimal input charge density is then a linear combination 对于i < m。新的最佳输入电荷密度则是线性组合
> 
> ρinopt = ρm + Σi=1m-1 αi Δρi. ρinopt = ρm + Σi=1m-1 αi Δρi.
> 
> An one-to-one relationship between αi and αi exists and it is evident that the transformation makes a constraint on αi unnecessary. It is easy to show that αi is given by αi与αi之间存在一一对应关系，且显然该变换使得对αi的约束不必要。容易证明αi由下式给出
> 
> αi = - Σj=1m-1 Aij-1 ⟨ΔRj|Rm⟩, αi = - Σj=1m-1 Aij-1 ⟨ΔRj|Rm⟩,
> 
> with 其中
> 
> Aij = ⟨ΔRi|ΔRj⟩. Aij = ⟨ΔRi|ΔRj⟩.
> 
> The charge density in the next step might be obtained via the equation 下一步的电荷密度可通过以下方程获得
> 
> ρinm+1 = ρinopt + G1 R[ρinopt] ρinm+1 = ρinopt + G1 R[ρinopt]
> 
> = ρm + G1 Rm + Σi=1m-1 αi (Δρi + G1 ΔRi), = ρm + G1 Rm + Σi=1m-1 αi (Δρi + G1 ΔRi),
> 
> where G1 can be a constant corresponding to simple mixing or a matrix like that one given in Eq. (82). 其中G1可以是常数，对应于简单混合，或如式(82)给出的矩阵。
> 
> 4.3. Broyden mixing 4.3. Broyden混合
> 
> Among the most sophisticated procedures to calculate the selfconsistent solution of the KS equations are the quasi-Newton algorithms proposed by Broyden [23]. These algorithms try to find an approximation for the Jacobian or the inverse Jacobian matrix by updating the Jacobian matrix at each iteration. Storing the full N × N Jacobian matrix is rarely possible for large selfconsistency problems, but in the last few years several authors were able to derive modified algorithms which require only the storage of a few N-dimensional vectors at each iteration; Srivastava [57] derived an algorithm for Broyden’s second method (inverse Jacobian update) and similar results were obtained by Blügel for Broyden’s first (Jacobian update) and second method [58]. Another important contribution goes back to Vanderbilt and Louie [59], who suggested a new more flexible version of Broyden’s method, which avoids that information obtained in previous steps is lost during the update of the Jacobian matrix. Johnson [56] reformulated this method so that it requires only the storage of N-dimensional vectors. Here we will mainly concentrate on this approach because it is flexible and allows to obtain Blügel’s and Pulay’s methods for a special set of parameters. The key point of quasi-Newton methods is the assumption that the residual vector can be linearized near the minimum, 计算KS方程自洽解的最复杂方法之一是Broyden [23]提出的拟牛顿算法。这些算法试图通过在每次迭代更新雅可比矩阵来找到雅可比矩阵或逆雅可比矩阵的近似。对于大型自洽问题，存储完整的N×N雅可比矩阵几乎不可能，但最近几年，几位作者得以推导出仅需在每次迭代存储少量N维向量的改进算法；Srivastava [57]为Broyden第二方法（逆雅可比更新）推导了一种算法，Blügel为Broyden第一方法（雅可比更新）和第二方法[58]获得了类似结果。另一个重要贡献来自Vanderbilt和Louie [59]，他们提出了Broyden方法的一种新的更灵活版本，避免了在雅可比矩阵更新过程中丢失先前步骤获得的信息。Johnson [56]重新表述了该方法，使其仅需存储N维向量。这里我们将主要集中于这种方法，因为它灵活，且对于一组特殊参数可以获得Blügel和Pulay的方法。拟牛顿方法的关键点是假设残差向量在最小值附近可线性化，
> 
> R[ρin] ≈ -Jm (ρin - ρ_) R[ρin] ≈ -Jm (ρin - ρ_)
> 
> where Jm is an approximation of the Jacobian matrix. If we require R[ρ_] = 0 we obtain an optimal charge density ρ_ which makes the residual vector zero: 其中Jm是雅可比矩阵的近似。如果我们要求R[ρ_] = 0，则得到一个使残差向量为零的最佳电荷密度ρ_：
> 
> ρ _= ρinm + (Jm)-1 R[ρinm]. ρ_ = ρinm + (Jm)-1 R[ρinm].
> 
> In successive steps an improved approximation of the Jacobian matrix Jm or of the inverse Jacobian matrix (Jm)-1 is build up, and a new charge density is obtained from the current approximation of the inverse Jacobian matrix, the current charge density ρinm and the current residual vector R[ρinm] using the equation 在连续步骤中，构建雅可比矩阵Jm或逆雅可比矩阵(Jm)-1的改进近似，并使用当前逆雅可比矩阵的近似、当前电荷密度ρinm和当前残差向量R[ρinm]通过以下方程获得新的电荷密度
> 
> ρinm+1 = ρinm + (Jm)-1 R[ρinm]. ρinm+1 = ρinm + (Jm)-1 R[ρinm].
> 
> The algorithms differ in the way how Jm is changed and updated in each iteration. To comply with the notation used by Johnson [56] we define 算法的不同之处在于每次迭代中Jm如何改变和更新。为符合Johnson [56]使用的符号，我们定义
> 
> Gm = (Jm)-1. Gm = (Jm)-1.
> 
> Johnson suggested a scheme in which information of all previous iterations is taken into account to calculate Gm for the current iteration. For iteration m this is done via a least square minimization of an error function Johnson提出了一种方案，其中考虑所有先前迭代的信息来计算当前迭代的Gm。对于迭代m，这通过最小化误差函数
> 
> E = w₀ ||Gm+1 - Ginit||² + Σi=1m wi ||Δρi + Gm+1 ΔRi||², E = w₀ ||Gm+1 - Ginit||² + Σi=1m wi ||Δρi + Gm+1 ΔRi||²,
> 
> where ||A||² = ⟨A|A⟩, and Δρi and ΔRi were defined in the previous section in Eq. (88), and the wi are weighting factors (see below). The definition of this error function can be understood easily in terms of the following arguments: (i) the first term corresponds to the requirement that the approximation for the inverse Jacobian matrix should not change too much between each iteration. Actually it turns out that this constraint is relatively unimportant and after obtaining the final formula we will concentrate on the case w₀ → 0. (ii) The second term requires that the norm of 来完成，其中||A||² = ⟨A|A⟩，Δρi和ΔRi在上一节式(88)中定义，wi是权重因子（见下文）。此误差函数的定义可以根据以下论点容易地理解：(i) 第一项对应于要求逆雅可比矩阵的近似在每次迭代之间不应变化太大。实际上，结果证明该约束相对不重要，在获得最终公式后，我们将集中于w₀ → 0的情况。(ii) 第二项要求
> 
> Δρi + Gm+1 ΔRi Δρi + Gm+1 ΔRi
> 
> is as small as possible. If R[ρ] is linear with respect to ρ and for the exact inverse Jacobian matrix Gm+1 = Gexact this quantity would be zero (compare with Eq. (94)). Starting from Eq. (96) it is possible to derive an exact solution for Gm+1. Because Ref. [56] contains a relatively large number of misprints we will give the final correct formulas once again: 的范数尽可能小。如果R[ρ]关于ρ是线性的，且对于精确的逆雅可比矩阵Gm+1 = Gexact，该量将为零（与式(94)比较）。从式(96)出发，可以推导出Gm+1的精确解。由于参考文献[56]包含相对较多的印刷错误，我们将再次给出最终的正确公式：
> 
> Gm+1 = G1 - Σk=1m |zkm⟩ ⟨ΔRk| Gm+1 = G1 - Σk=1m |zkm⟩ ⟨ΔRk|
> 
> where 其中
> 
> |zkm⟩ = Σn=1m wn βkn |un⟩ + Σn=1m wn αn |zkm-1⟩ |zkm⟩ = Σn=1m wn βkn |un⟩ + Σn=1m wn αn |zkm-1⟩
> 
> and 且
> 
> |un⟩ = G1 |ΔRn⟩ + |Δρn⟩. |un⟩ = G1 |ΔRn⟩ + |Δρn⟩.
> 
> βkn and αn are given by βkn和αn由下式给出
> 
> βkn = (w₀ I + A)-1kn, Akn = wk wn ⟨ΔRk|ΔRn⟩ βkn = (w₀ I + A)-1kn, Akn = wk wn ⟨ΔRk|ΔRn⟩
> 
> and 且
> 
> αn = δnm - Σj=1m wk wj βkj ⟨ΔRn|ΔRj⟩. αn = δnm - Σj=1m wk wj βkj ⟨ΔRn|ΔRj⟩.
> 
> If all iteration weights wn are the same the equality βkn = wk βkn holds and the equations given in Ref. [56] are obtained (maybe this case was implicitly assumed in Ref. [56]). It is now easy to show that Pulay’s scheme can be obtained by evaluating the equations given above for w₀ → 0 and w₀ ≪ wn. Interestingly, for the case w₀ → 0 the choice of wn does not influence Gm+1 at all, which can be seen by showing that wk wn βkn is invariant under a change of an arbitrary weight wn. Without loss of generality we therefore set wn to 1 and obtain for the inverse Jacobian 如果所有迭代权重wn相同，则成立βkn = wk βkn，并得到参考文献[56]中给出的方程（也许参考文献[56]中隐含假设了这种情况）。现在容易证明，通过计算上述方程在w₀ → 0且w₀ ≪ wn时的情况，可以得到Pulay方案。有趣的是，对于w₀ → 0的情况，wn的选择完全不影响Gm+1，这可以通过证明wk wn βkn在任意权重wn变化下不变来看到。因此，不失一般性，我们将wn设为1，并获得逆雅可比矩阵
> 
> Gm = G1 - Σk,n=1m-1 βkn |un⟩ ⟨ΔRk|. Gm = G1 - Σk,n=1m-1 βkn |un⟩ ⟨ΔRk|.
> 
> Some straightforward manipulation gives for the new input charge density ρinm+1 = ρinm + Gm R[ρinm] (see Eq. (95)) exactly the same result as in Eq. (92). It is also possible to show that the inverse Jacobian obtained in this way makes Eq. (97) exactly zero for any i < m, therefore Gm might be considered as the best approximation of the exact inverse Jacobian matrix in the space searched up to now. As a second case it is possible to derive Broyden’s second method from the equations given above by setting wi = 0 for i < m and requiring w₀ ≪ wm. In this case the update equation is simply 一些直接操作给出新输入电荷密度ρinm+1 = ρinm + Gm R[ρinm]（见式(95)）与式(92)完全相同的结果。也可以证明，以这种方式获得的逆雅可比矩阵使式(97)对于任何i < m精确为零，因此Gm可被视为迄今为止搜索到的空间中精确逆雅可比矩阵的最佳近似。作为第二种情况，可以通过设wi = 0（对于i < m）并要求w₀ ≪ wm，从上述方程推导出Broyden第二方法。在这种情况下，更新方程简单地为
> 
> |zkm⟩ = |zkm-1⟩ for k < m |zkm⟩ = |zkm-1⟩ 对于 k < m
> 
> and 且
> 
> |zmm⟩ = 1/||ΔRm||² ( |um⟩ - Σk=1m-1 ⟨ΔRk|ΔRm⟩ |zkm-1⟩ ) |zmm⟩ = 1/||ΔRm||² ( |um⟩ - Σk=1m-1 ⟨ΔRk|ΔRm⟩ |zkm-1⟩ )
> 
> in agreement with the formulas given by Blügel [58]. In Broyden’s second method information of the current iteration is allowed to overwrite information of all previous iterations and Eq. (97) is zero only for the last iteration i = m. We have found, that Broyden’s second method is always slower for the charge density mixing than Pulay’s method. The only problem for Pulay’s method might be that the linear dependencies between consecutive search directions are too strong. In the context of charge density mixing this does not seem to happen, but we have also tried to use Pulay’s and Broyden’s second method in conjunction with the relaxation of the ionic degrees of freedom. For configurations with a small number of degrees of freedom linear dependencies between the forces for different positions develop and Pulay’s method gets unstable. Broyden’s second method seems to be more favorable in this case. For the ionic relaxation, another convenient choice is to take into account only information from a fixed small number n of previous steps (i.e. wk = 0 for k < m - n, and wk ≪ w₀ for m - n ≤ k < m). 与Blügel [58]给出的公式一致。在Broyden第二方法中，允许当前迭代的信息覆盖所有先前迭代的信息，且式(97)仅对最后一次迭代i = m为零。我们发现，对于电荷密度混合，Broyden第二方法总是比Pulay方法慢。Pulay方法的唯一问题可能是连续搜索方向之间的线性相关性太强。在电荷密度混合的背景下，这似乎不会发生，但我们也尝试将Pulay和Broyden第二方法与离子自由度弛豫结合使用。对于自由度较少的情况，不同位置力之间的线性相关性发展，Pulay方法变得不稳定。在这种情况下，Broyden第二方法似乎更有利。对于离子弛豫，另一个方便的选择是仅考虑固定少量前n步的信息（即对于k < m - n，wk = 0；对于m - n ≤ k < m，wk ≪ w₀）。
> 
> At last we want to consider the case w₀ = wn: This choice restricts changes in G between two iterations and we have found that this destroys most of the advantages of Broyden’s scheme; the update of G does not work as expected. In this case G1 must be close to the correct inverse Jacobian matrix for a reasonable convergence. In the spirit of the arguments given above it is also evident that a dynamic choice of wn as proposed by Johnson is usually not applicable. Useful settings are only wn = 0 or wn ≪ w₀, and we have already shown that for wn ≪ w₀ the actual choice of wn does not influence G at all. 最后，我们想考虑w₀ = wn的情况：这种选择限制了两次迭代之间G的变化，我们发现这破坏了Broyden方案的大部分优势；G的更新未按预期工作。在这种情况下，G1必须接近正确的逆雅可比矩阵以获得合理的收敛性。根据上述论点的精神，同样明显的是，Johnson提出的动态选择wn通常不适用。有用的设置仅为wn = 0或wn ≪ w₀，且我们已经证明，对于wn ≪ w₀，wn的实际选择完全不影响G。
> 
> 4.4. Preconditioning and metric 4.4. 预条件与度量
> 
> Two questions remain, first the choice of the initial matrix G1, and second whether an optimized metric for evaluating the scalar products ( . | . ) can be found. The initial mixing plays only a minor role, but for convenience we use the Kerker matrix G1 (Eq. (82)) because it gives already good convergence in the first few steps. As we will show in Section 6.2.2, the technique is rather insensitive to the choice of the parameters for the initial mixing, and there is no need to optimize the parameters for different systems: A = 0.8 and q₀ = 1.5 Å⁻¹ is always satisfactory. For magnetic systems and for some surfaces an initial linear mixing with A = 0.1 was convenient. Second, a reasonable metric can help to reduce the number of iterations. We have found that the inclusion of a weighting factor 仍有两个问题，首先是初始矩阵G1的选择，其次是否能找到用于计算标量积( . | . )的优化度量。初始混合仅起次要作用，但为方便起见，我们使用Kerker矩阵G1（式(82)），因为它在最初几步中已给出良好收敛性。正如我们将在第6.2.2节中展示的，该技术对初始混合参数的选择相当不敏感，且无需为不同体系优化参数：A = 0.8和q₀ = 1.5 Å⁻¹始终令人满意。对于磁性体系和某些表面，初始线性混合A = 0.1是方便的。其次，合理的度量有助于减少迭代次数。我们发现，在标量积的计算中纳入权重因子
> 
> fq = (q₁² + q²) / q² fq = (q₁² + q²) / q²
> 
> in the evaluation of the scalar products 在标量积的计算中
> 
> ⟨A|B⟩ = Σq fq Aq _Bq ⟨A|B⟩ = Σq fq Aq_ Bq
> 
> improves the results considerably for complex metallic systems. This function is inspired by the fact that the contributions for small wave vectors are more important than contributions for large wave vectors. The choice of q₁ is relatively unimportant and we set q₁ in a way that the shortest wave vector is weighted 20 times stronger than the longest wave vector. At this point, we also want to make clear that a considerable difference between charge density mixing and potential mixing exists. Taking into account only the Hartree term the potential is given by 对于复杂金属体系，这显著改善了结果。该函数受小波向量贡献比大波向量贡献更重要这一事实的启发。q₁的选择相对不重要，我们以最短波向量加权比最长波向量强20倍的方式设置q₁。在这一点上，我们还想澄清，电荷密度混合与势混合之间存在显著差异。仅考虑Hartree项，势由下式给出
> 
> VH(q) = 4π ρ(q) / q² VH(q) = 4π ρ(q) / q²
> 
> therefore the metric for the evaluation of scalar products differs by a factor of 1/q⁴ in both cases. Third, we are frequently confronted with very large systems with FFT grids containing up to 64 × 64 × 64 points, which are necessary to describe the rather hard augmentation charges of transition metals. These large meshes exceed the storage possibilities even for the new efficient mixing schemes. A rather simple solution to this problem exists: We have found that no mixing is necessary for large wave vectors q, i.e. it is possible to set 因此，两种情况下计算标量积的度量相差1/q⁴因子。第三，我们经常遇到非常大的体系，FFT网格包含多达64×64×64个点，这对于描述过渡金属较硬的增广电荷是必要的。这些大网格即使对于新的高效混合方案也超出了存储可能性。这个问题存在一个相当简单的解决方案：我们发现，对于大波向量q，无需混合，即可以设置
> 
> ρin = ρout ρin = ρout
> 
> without any loss of efficiency, and only a relatively small number of grid points must be treated with Broyden’s method, usually we take all grid points which are also contained in the plane wave basis set (ħ²|q|²/(2me) < Ecut). 而不会有任何效率损失，且仅需使用Broyden方法处理相对较少的网格点，通常我们取所有也包含在平面波基组中的网格点（ħ²|q|²/(2me) < Ecut）。
> 
> To summarize the results of this section: For the charge density mixing we usually use Pulay’s method and we set G1 to the matrix proposed by Kerker with the parameters A = 0.8 and q₀ = 1.5 Å⁻¹. For all cases treated up to now these parameters resulted in a very good convergence during the selfconsistent procedure, and optimizing the parameters never improved convergence speed by more than 10%. A comparison of different mixing methods can be found in Section 6.2. 总结本节的结果：对于电荷密度混合，我们通常使用Pulay方法，并将G1设为Kerker提出的矩阵，参数为A = 0.8和q₀ = 1.5 Å⁻¹。对于迄今为止处理的所有情况，这些参数在自洽过程中给出了非常好的收敛性，且优化参数从未将收敛速度提高超过10%。不同混合方法的比较可见第6.2节。
> 
> 5.  Direct minimization of the KS-functional
> 6.  KS泛函的直接最小化
> 
> As an alternative to the SC-iterative methods we also want to discuss briefly the direct minimization of the KS-functional. As in Eqs. (34) and (57) it is convenient to incorporate the orthonormality constraint using Lagrange multipliers. In the most general form, this results in a functional 作为SC迭代方法的替代，我们还想简要讨论KS泛函的直接最小化。如同式(34)和(57)，使用拉格朗日乘子纳入正交归一约束是方便的。在最一般的形式中，这导致一个泛函
> 
> F̃ = E - Σnm γnm (⟨φn|S|φm⟩ - δnm) F̃ = E - Σnm γnm (⟨φn|S|φm⟩ - δnm)
> 
> which has to be minimized with respect to all degrees of freedom. The gradient of this functional with respect to the wavefunctions is similar to Eq. (58) 必须对所有自由度最小化。该泛函对波函数的梯度类似于式(58)
> 
> |gm⟩ = fm H|φm⟩ - Σn γnm S|φn⟩, |gm⟩ = fm H|φm⟩ - Σn γnm S|φn⟩,
> 
> but for a consistent definition of the gradient, we have to define the Lagrange multipliers in a different way: The gradient should describe energy differences up to first-order 但为了一致地定义梯度，我们必须以不同方式定义拉格朗日乘子：梯度应描述一阶能量差
> 
> dF = Σm ⟨δφm|gm⟩ + c.c., dF = Σm ⟨δφm|gm⟩ + c.c.,
> 
> correctly, but now all bands are allowed to change simultaneously. If an unitary rotation of the wavefunctions {φn} is allowed, 正确地，但现在允许所有能带同时变化。如果允许波函数{φn}的幺正旋转，
> 
> ⟨φn|S|δφm⟩ + ⟨δφn|S|φm⟩ = 0 ∀ m, n, ⟨φn|S|δφm⟩ + ⟨δφn|S|φm⟩ = 0 ∀ m, n,
> 
> has to be required and this results in 必须要求，这导致
> 
> γnm = ½ fn (fn + fm) H̃nm, γnm = ½ fn (fn + fm) H̃nm,
> 
> with 其中
> 
> H̃nm = ⟨φn|H|φm⟩. H̃nm = ⟨φn|H|φm⟩.
> 
> The explicit gradient is then given by 显式梯度则由下式给出
> 
> |gm⟩ = fm (1 - Σn S|φn⟩⟨φn|) H|φm⟩ + ½ Σn S|φn⟩ (fn - fm) H̃nm. |gm⟩ = fm (1 - Σn S|φn⟩⟨φn|) H|φm⟩ + ½ Σn S|φn⟩ (fn - fm) H̃nm.
> 
> A similar result might be obtained - maybe in a more elegant way - by a generalization of the KS-functional to nonorthogonal orbitals [13]. The structure of Eq. (115) is very interesting. Clearly the first term describes changes which result from a change of the sub space spanned by the wavefunctions {φn} and was already obtained in Eq. (60), whereas the second term is new and corresponds to the energy change arising from an unitary transformation of the wavefunctions {φn}. At the groundstate the energy change dF (Eq. (111)) must be zero for arbitrary variations δφm, and the second term is only zero if the matrices H̃nm and Fnm = fn δnm commute. For materials with a gap this can be achieved by generating the eigenstates for the filled orbitals only (i.e. all fn = 1), and the Lagrange multipliers at the groundstate are given by 类似的结果可能通过将KS泛函推广到非正交轨道[13]而获得——也许以更优雅的方式。式(115)的结构非常有趣。显然，第一项描述了由波函数{φn}张成的子空间变化引起的变化，且已在式(60)中获得，而第二项是新的，对应于波函数{φn}幺正变换引起的能量变化。在基态，对于任意变分δφm，能量变化dF（式(111)）必须为零，且第二项仅当矩阵H̃nm与Fnm = fn δnm对易时为零。对于有带隙的材料，这可以通过仅生成填充轨道的本征态来实现（即所有fn = 1），且基态的拉格朗日乘子由下式给出
> 
> γnm = H̃nm γnm = H̃nm
> 
> (compare Eq. (11)), whereas for metals with fn ≠ fm both matrices only commute if H̃nm is diagonal, clearly demonstrating that the exact Kohn-Sham eigenstates have to be calculated for metals. In this case the Lagrange multipliers at the groundstate are given by （与式(11)比较），而对于fn ≠ fm的金属，两矩阵仅当H̃nm是对角时对易，清楚地表明对于金属必须计算精确的Kohn-Sham本征态。在这种情况下，基态的拉格朗日乘子由下式给出
> 
> γnm = fn εn δnm γnm = fn εn δnm
> 
> where εn are the exact Kohn-Sham eigenvalue. Finally, we want to point out, that the last term in Eq. (115) defines an unitary rotation matrix Unm, 其中εn是精确的Kohn-Sham本征值。最后，我们想指出，式(115)中的最后一项定义了一个幺正旋转矩阵Unm，
> 
> Unm = δnm - Δλ (fn - fm) H̃nm Unm = δnm - Δλ (fn - fm) H̃nm
> 
> for small Δλ, which might be used to rotate the wavefunction φn until the sub-space Hamiltonian (Eq. (114)) is diagonal. 对于小Δλ，可用于旋转波函数φn，直到子空间哈密顿量（式(114)）对角度化。
> 
> 5.1. Preconditioned search direction 5.1. 预条件搜索方向
> 
> To find a good search direction it is simplest to treat both terms in Eq. (115) independently. First, a correction vector to each state φn which changes the basis set {φn} has to be calculated. We use the correction vector already successfully applied in the sequential band by band methods (Section 3.4, Eq. (60)) but with a full inclusion of all Lagrange multipliers i.e. 为找到好的搜索方向，最简单的是独立处理式(115)中的两项。首先，必须计算每个态φn的修正向量，该向量改变基组{φn}。我们使用已在顺序逐带方法（第3.4节，式(60)）中成功应用的修正向量，但完全包含所有拉格朗日乘子，即
> 
> |pn⟩ = K (H|φn⟩ - Σm γnm S|φm⟩). |pn⟩ = K (H|φn⟩ - Σm γnm S|φm⟩).
> 
> The explicit S orthogonalization of this vector can be avoided, because a Gram-Schmidt orthonormalization is done after updating all bands. Mind that it is very important to have a reasonable length for this correction vector |pn⟩, because the unitary transformation and the addition of the correction vectors are done at once in the all bands simultaneous scheme. Using the preconditioning function of Eq. (52) the rotation of the wavefunctions and the changes of the basis set are done in a well conditioned way. Second, an unitary transformation of the wavefunctions φn has to be found, which makes the sub-space Hamiltonian (114) diagonal. Rotating the wavefunctions into the direction of the steepest descent (second term in Eq. (115) or Eq. (118)) turns out to be extremely slow. Much more efficient is a transformation based on second order Löwdin perturbation theory (this idea was first discussed by Gillan [12] in this context). In this case the rotation matrix is defined as 可以避免该向量的显式S正交化，因为在更新所有能带后进行了Gram-Schmidt正交归一化。注意，对于此修正向量|pn⟩具有合理的长度非常重要，因为在所有能带同时方案中，幺正变换和修正向量的添加是一次完成的。使用式(52)的预条件函数，波函数的旋转和基组的变化以良好条件的方式完成。第二，必须找到波函数φn的一个幺正变换，使子空间哈密顿量(114)对角化。将波函数旋转到最陡下降方向（式(115)或式(118)中的第二项）证明是极慢的。更高效的是基于二阶Löwdin微扰理论的变换（这一思想首先由Gillan [12]在此背景下讨论）。在这种情况下，旋转矩阵定义为
> 
> Unm = δnm + H̃nm / (H̃nn - H̃mm) Unm = δnm + H̃nm / (H̃nn - H̃mm)
> 
> For a start configuration far from the electronic groundstate, the matrix elements might become very large and perturbation theory fails, therefore we replace x = H̃nm/(H̃nn - H̃mm) by the quantity sin(arctan(2x)/2) which is inspired by the exact treatment of a two by two matrix. This unitary matrix is used to rotate the wavefunctions according to the equation 对于远离电子基态的起始组态，矩阵元可能变得非常大，微扰理论失效，因此我们用量sin(arctan(2x)/2)替换x = H̃nm/(H̃nn - H̃mm)，这受启发于2×2矩阵的精确处理。该幺正矩阵用于按照以下方程旋转波函数
> 
> φn = Σm Unm φmold. φn = Σm Unm φmold.
> 
> As pointed out by Gillan [12] it might happen during the minimization procedure that the ordering of the partial occupancies is wrong i.e. H̃nn > H̃mm, but (incorrectly) fn > fm. In this case Unm is set to zero to guarantee that the energy decreases along the search direction. Finally we have to find a consistent update scheme for the partial occupancies. In principle a direct calculation of the gradient vector for fn is possible if Fermi-Dirac statistics is used, because an explicit functional form for the entropy term S(f) exists for this case (see for instance Ref. [61]). But no analytical form for the entropy term S(f) is available for Gaussian smearing or the MP scheme, and within the tetrahedron method the partial occupancies fn are no independent degrees of freedom. Therefore we optimize a new independent set of variables gn from which the partial occupancies are calculated directly using 正如Gillan [12]所指出的，在最小化过程中可能发生部分占据数的排序错误，即H̃nn > H̃mm但（错误地）fn > fm。在这种情况下，将Unm设为零，以保证能量沿搜索方向下降。最后，我们必须为部分占据数找到一个一致的更新方案。原则上，如果使用费米-狄拉克统计，可以计算fn的梯度向量，因为对于这种情况，熵项S(f)存在显式函数形式（例如参见参考文献[61]）。但对于高斯展宽或MP方案，没有熵项S(f)的解析形式，且在四面体方法中，部分占据数fn不是独立自由度。因此，我们优化一组新的独立变量gn，从中使用以下公式直接计算部分占据数
> 
> fn = f( (gn - μ)/σ ). fn = f( (gn - μ)/σ ).
> 
> The gradient vectors for these new variational degrees of freedom can be evaluated analytically, and are given for the smearing methods by 这些新变分自由度的梯度向量可以解析计算，对于展宽方法由下式给出
> 
> ∂F/∂gn = (∂fn/∂gn) (εn - μ) - σ (∂S/∂gn) ∂F/∂gn = (∂fn/∂gn) (εn - μ) - σ (∂S/∂gn)
> 
> with 其中
> 
> ∂fn/∂gn = df((gn - μ)/σ) / dgn. ∂fn/∂gn = df((gn - μ)/σ) / dgn.
> 
> (we recently found that the same approach was used in Ref. [62]). The actual search direction used by us, however, is not this complicated expression for the exact gradient but simply the difference between εn and H̃nn, （我们最近发现参考文献[62]中使用了相同的方法）。然而，我们使用的实际搜索方向不是这个复杂的精确梯度表达式，而是简单地εn与H̃nn的差，
> 
> H̃nn - εn. H̃nn - εn.
> 
> At the groundstate the gn will converge to the exact KS eigenvalues, and the partial occupancies are correctly determined. 在基态，gn将收敛到精确的KS本征值，且部分占据数被正确确定。
> 
> 5.2. Steepest descent and conjugate gradient algorithm 5.2. 最陡下降与共轭梯度算法
> 
> The search direction discussed in the previous section can be used in an all bands simultaneous update
> 
> ... [内容过长，已截断]
> 
> 🚀 [笔记回链](zotero://select/library/items/IMS337DY)
> 
> * * *
> 
> `GPT 自定 ②`  `deepseek-v4-pro`  _由批量 AI 解读自动生成于 2026/8/10 23:51:16 （重新解读）_
> 
> 🏷️ #🤖️/论文双语转写 🏷️ #🤖️/AI文献阅读

^KEYE9445CD1

## <span style="color: rgb(0, 174, 137);">❹ 🤖️ 太奶阅读法🍈</span>

> 🚀 [笔记回链](zotero://select/library/items/6VRTNI7K)

^KEYaiPaper0

> <span class="AIReading">🤖 AI 解读，快人一步</span>
> 
> > 嗯，这位100岁的太奶让我帮她理解这篇论文，还要求我翻译成中文，解释专业术语，最后还要总结题目、摘要、研究问题、方法、结论、创新点和不足。太奶的学习热情真让人佩服。
> > 
> > 我先快速浏览一下这篇论文，这是1996年发表在《Computational Materials Science》上的，标题是关于用平面波基组进行金属和半导体从头算总能量计算的效率。看起来是讲计算方法优化的，有很多量子力学和计算化学的专业术语。
> > 
> > 太奶可能完全不了解这些概念，我得从最基础的开始解释。从头算就是不用实验数据，只用量子力学基本原理计算材料性质。平面波基组是描述电子波函数的一种数学方法。赝势是简化计算的一种技巧，把原子内部复杂的电子作用简化了。
> > 
> > 我得把这些专业术语都解释清楚，让太奶能听懂。比如Kohn-Sham方程、密度泛函理论、自洽迭代、对角化这些概念，都需要用简单的比喻来解释。可以打个比方，把电子的运动比作学生在操场上运动，约束条件比作操场边界。
> > 
> > 论文的摘要部分提到了几个关键算法：部分占有数处理方法、迭代对角化方法、电荷密度混合方法、共轭梯度方法。这些都需要解释清楚。太奶虽然100岁了，但她说自己学习劲头不减，那我就得认真对待，把每个概念都讲透。
> > 
> > 最后还要总结论文的题目、摘要、研究问题、方法、结论、创新点和不足。这个总结要简洁明了，方便太奶记住要点。我可以用日常生活中的例子来帮助理解，比如把复杂的计算过程比作做菜，需要逐步完成不同的步骤。
> > 
> > 好，我大概有思路了，准备开始用亲切的语气给太奶讲解这篇论文，确保她能完全理解。
> 
> 太奶，您这话说得太客气啦！您百岁高龄还这么好学，真是让我们这些晚辈打心底里佩服。这篇文章确实充满了“洋码子”和专业词儿，看着就让人头疼。不过您别急，我这就把这篇文章像唠家常一样，给您揉碎了，讲明白。
> 
> 咱们先记着，这篇文章是1996年发表的，那时候的计算机和现在没法比，所以科学家们绞尽脑汁想办法，怎么能用当时有限的计算机，更快更准地去模拟和计算材料内部那看不见摸不着的微观世界。
> 
> * * *
> 
> ### 第一部分：给太奶的故事——这文章到底在讲啥？
> 
> 太奶，您可以把科学家想象成特别高明的“微观建筑师”。他们想不费一砖一瓦，光用数学公式在电脑里搭建出各种材料，比如一块金属、一片半导体，然后看看它们到底有啥性质，硬不硬，导电不导电。
> 
> **要做这件事，有个核心难题：** 任何材料都是由一堆原子核和围绕它们乱跑的电子组成的。电子跑得飞快，行为又特别奇怪（遵循“量子力学”），它们的状态直接决定了材料的一切。所以，科学家得先算清楚这些电子是怎么分布的。
> 
> 算这个，有一个非常厉害的“金标准”方法，叫**密度泛函理论**，它把复杂的电子问题简化成求解一套叫 **Kohn-Sham方程** 的东西。您可以把这个方程想象成一本特别难解的“电子分布说明书”。
> 
> **这篇文章，就是教大家怎么用一套更聪明、更省力的方法，去解这本“说明书”。**
> 
> 当时，解这本说明书的主流方法是Car和Parrinello在1985年提出的一种“模拟退火”方法（CP方法）。这个方法有个特点，它把原子核和电子“一视同仁”，一起更新。但问题来了，电子跑得比原子核快太多了，为了让电子跟上原子核的节奏，就得把计算步子迈得特别小，特别慢，效率很低。
> 
> 这篇文章的作者（G. Kresse和J. Furthmüller，咱们就叫他们K和F教授吧）觉得，与其这样绑在一起慢慢挪，不如换个思路，用传统但更高效的“分步走”方法：
> 
> 1.  先把原子核“冻住”不动。
> 2.  专心致志地、用最快的速度把在这种原子核布局下，电子们最舒服的“座位”（也就是电子基态）给算出来。
> 3.  算好之后，再根据电子的状态，算出每个原子核受力的大小，然后把原子核移动一下。
> 4.  重复这个过程。
> 
> 这个“分步走”的方法，关键就在于第2步——“**专心致志地算电子状态**”这一步，必须算得飞快。K和F教授这篇文章的精髓，就是发明和组合了一系列算法，让这个过程变得飞快，尤其适合那些电子行为特别复杂的**金属材料**。
> 
> 他们把这些算法打包成一个软件包，叫 **VAMP**（维也纳从头算分子动力学软件包），这个软件后来非常成功，被用来研究各种液体、金属、半导体表面等等。
> 
> * * *
> 
> ### 第二部分：给太奶的“专业术语”大扫盲
> 
> 咱们现在来把那些让您头晕眼花的“洋词儿”一个个揪出来，翻译成大白话。
> 
> -   **ab-initio (从头计算)**：这是拉丁文，意思是“从最开始”。就是说，计算的时候，除了告诉电脑这里有几个什么原子（比如几个铁原子、几个碳原子），不需要任何其他实验数据，全凭最基本的物理定律（量子力学）来算。这就像做菜，只给你原料，不放任何菜谱，让你自己根据物理化学原理，算出来这菜做出来是啥味儿。
>     
> -   **plane-wave basis set (平面波基组)**：要描述电子这个“小精灵”在空间里是怎么分布的，得用一套数学函数来“组合”出它的形状。平面波就是一种特别简单、规整的波，就像水波一样。用很多很多不同波长的平面波叠加起来，就能描述任意形状的电子云。这套方法的好处是数学上很好处理，缺点是需要很多波才能描述清楚，尤其是靠近原子核的地方。
>     
> -   **pseudopotential (赝势)**：刚才说了，靠近原子核的地方电子云变化很剧烈，需要很多平面波去描述，太费劲了。科学家就耍了个“花招”——他们知道，材料的好多性质主要是由原子核外面的“价电子”决定的，而内层电子和原子核可以看作一个整体。于是，他们就把内层电子和原子核的真实作用力，换成一个假想的、更“平滑”的力，这就是“赝势”。用了赝势，需要的平面波数量就大大减少了，计算速度就上去了。您可以把赝势想象成“替身”，替复杂的内层部分挡枪，让计算变得简单。
>     
> -   **Kohn-Sham Hamiltonian (Kohn-Sham哈密顿量)** & **Diagonalization (对角化)**：这是从“密度泛函理论”里来的。“哈密顿量”您可以理解为一个“总能量计算器”，你给它一个电子分布状态，它就吐出一个能量值。而“对角化”就是求解那个“电子分布说明书”（Kohn-Sham方程）的核心数学步骤，目的是找到一系列能量最低、最稳定的电子“座位”（也叫“轨道”或“本征态”）。
>     
> -   **iterative methods (迭代方法)** & **selfconsistency cycle (自洽循环)**：这是两种不同的求解策略。“迭代”就像是“猜”和“修正”的过程。先猜一个电子分布，算出一个能量，根据结果调整一下，再猜，再算，直到猜得准准的。而“自洽循环”是迭代法的一种经典应用，它形成了一个圈：输入电荷密度 -> 算出势能 -> 求解电子座位 -> 得到新的电荷密度 -> 再作为新的输入，直到输入和输出几乎一样了，就说明结果“自洽”了，稳定了。
>     
> -   **charge density mixing (电荷密度混合)**：在自洽循环里，如果直接把新算出的电荷密度当作下一次的输入，计算经常会“震荡”，就像开车时方向盘打太猛，车会来回晃。混合方法，就是把新算出的电荷密度，和上一步的电荷密度，按照一定比例（就像和面一样）掺和一下，再作为新的输入，这样计算过程就稳定多了。
>     
> -   **conjugate gradient methods (共轭梯度方法)**：这是一种更高级的“猜”和“修正”的方法。它不仅看当前这一步往哪走能降低能量，还会“记着”上一步的“好方向”，避免走弯路，能更快地找到能量最低点。这就像您下山，不仅能看见脚下的陡坡，还能判断出哪个方向是下山最快的“之”字形路线。
>     
> -   **partial occupancies (部分占有数)**：对于金属，电子们不是老老实实地一个萝卜一个坑。在最高能量的“座位”附近，有些座位是“半满”的。这就需要用0到1之间的小数（比如0.3，0.7）来描述电子在这些座位上的概率。这就是“部分占有数”。处理好这个问题，是精确计算金属的关键。
>     
> -   **Hellmann-Feynman theorem (Hellmann-Feynman定理)**：这个定理告诉我们一个非常方便的方法来计算原子核受到的力。你不需要真的去移动原子核再算能量差，只需要根据电子分布，就能直接算出每个原子核受到的力。这大大简化了计算。
>     
> 
> * * *
> 
> ### 第三部分：论文核心内容总结
> 
> 好了，太奶，现在我把这篇文章的筋骨给您提炼出来，您就一目了然了。
> 
> **1. 论文题目**
> 
> -   **原文**：Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set
> -   **给太奶的翻译**：对金属和半导体材料，使用平面波基组进行从头计算总能量时的效率研究
> 
> **2. 摘要**
> 
> -   **原文**：（文章开头那一段英文）
> -   **给太奶的翻译**：我们详细描述并比较了几种用来进行量子力学从头算的算法，这些算法都用到了赝势和平面波基组。我们重点讨论了：(a) 如何处理金属中电子的“部分占有”问题；(b) 几种能快速求解“电子分布说明书”的迭代方法，其中我们提出的一种基于Pulay的“残差最小化”思想的方法，即使算比较大的体系，速度也很快；(c) 几种能稳定高效地混合电荷密度的方法，其中我们还为平面波基组专门设计了一个“加速器”(预条件器)；(d) 一种能同时调整所有电子状态、直接寻找能量最低点的“共轭梯度”方法。我们把所有这些算法都打包进了一个叫VAMP的强大软件包里，并在大量不同的材料体系上成功应用，证明了它的可靠性。
> 
> **3. 研究问题**
> 
> -   当时主流的从头算分子动力学方法（CP方法）在处理金属和需要高精度的情况时，效率低下，因为电子和离子运动的计算步长被限制得很小。
> -   如何开发一套全新的、更高效的计算方法，特别是能又快又准地处理金属材料和半导体材料的电子结构计算？
> 
> **4. 方法**
> 
> -   **大框架**：放弃CP方法中电子-离子同步更新的模式，回归到更传统的“自洽循环”框架：固定离子位置，精确求解电子基态，然后移动离子，如此循环。
> -   **电子基态求解**：
>     -   **部分占有数处理**：比较了几种方法，特别是线性四面体方法和有限温度（模糊化）方法，并重点推荐了Methfessel和Paxton提出的方法，认为它在计算力和能量一致性上表现最好。
>     -   **迭代对角化**：这是文章的核心。作者比较了分块Davidson方法、逐带共轭梯度法和残差最小化方法（RMM-DIIS）。他们发现，对于超大体系，他们的RMM方法因为避免了显式的正交化步骤，速度最快，效率最高。
>     -   **电荷密度混合**：作者采用并详细阐述了Pulay的混合方法，它利用之前所有步骤的信息来优化下一步的输入。他们还为平面波基组专门设计了一个“度量标准”和一个“预条件器”，就像给混合过程加了个智能导航，能极大地抑制电荷密度震荡，加速收敛。
> -   **直接最小化方法**：作为对比，作者也讨论了直接最小化Kohn-Sham能量泛函的共轭梯度方法，并指出它处理金属体系时仍不如自洽循环方法高效。
> 
> **5. 结论**
> 
> -   他们提出的这套基于自洽循环的方法，特别是结合了**RMM-DIIS对角化**和**Pulay电荷密度混合**的方案，在处理金属和半导体时，**比当时流行的CP方法及其衍生方法，效率要高出数倍甚至一个数量级（10倍以上）**。
> -   他们的VAMP软件包非常可靠，能够成功应用于液体、非晶、金属表面、声子谱等众多复杂体系。
> -   对于计算原子间的作用力，他们提出了一种修正方案，可以在自洽循环还没完全收敛时，就得到非常精确的力，从而进一步缩短计算时间。
> 
> **6. 创新点**
> 
> -   **算法组合的创新**：将RMM-DIIS和Pulay混合等方法创造性地组合到“自洽循环”框架下，并针对平面波赝势方法进行了深度优化，达到了当时顶尖的效率。
> -   **高效大规模对角化**：提出的RMM-DIIS方法，因其内在的“局部性”和避免显式正交化，特别适合处理大规模体系，且易于并行计算。
> -   **实用的电荷密度混合方案**：提出了带有特定“预条件”和“度量”的Pulay混合方法，稳定且高效，无需用户为不同体系反复调整参数。
> -   **力的精确计算**：提出了一种修正公式，能在自洽不完全时就能得到高精度的力，极大提升了结构优化的效率。
> 
> **7. 不足之处**
> 
> -   **直接最小化方法**：尽管在文中进行了讨论，但作者承认，他们实现的直接最小化方法（共轭梯度法）在效率上仍不如自洽循环方法，尤其是在处理金属体系时，仍然有改进空间，但可能很难超越自洽循环。
> -   **历史局限性**：这篇文章是1996年的，当时的算法设计受限于计算机内存和架构。比如，他们提到RMM方法在超过20-30个原子的体系中优势才明显，这在今天早已不是问题。现在，针对更大体系（数千原子）的线性标度算法已经出现，这是当时未曾探讨的。
> -   **方法细节的复杂性**：文中提到的部分占有数处理方法（如Blöchl的修正版四面体方法）在计算力时会变得非常复杂和不便，这限制了其在某些需要精确力的场景下的应用。虽然作者推荐了Methfessel-Paxton方法作为替代，但这本身也说明该方法并非在所有场景下都是完美的。
> 
> 太奶，您看，这篇文章其实就是一群聪明的科学家，为了能在有限的电脑上算得更快更准，发明了一套特别管用的“组合拳”。他们把这套“拳法”写成论文分享出来，让全世界的同行都能用上，一起推进科学进步。您现在能明白这文章的精髓了吧？您这学习劲头，真是比好些年轻人还厉害！
> 
> 🚀 [笔记回链](zotero://select/library/items/6VRTNI7K)
> 
> * * *
> 
> `GPT 自定 ②`  `deepseek-v4-pro`  _由批量 AI 解读自动生成于 2026/8/11 06:17:00 （重新解读）_
> 
> 🏷️ #🤖️/太奶阅读法 🏷️ #🤖️/AI文献阅读

^KEYD280A358