---
citekey: monkhorstSpecialPointsBrillouinzone1976
title: "Special points for Brillouin-zone integrations"
authors: [Hendrik J. Monkhorst, James D. Pack]
year: 1976
journal: "Physical Review B"
doi: "10.1103/PhysRevB.13.5188"
url: "https://doi.org/10.1103/PhysRevB.13.5188"
paper_type: method
status: ingested
year_read: 2026
original_note: "[[../../raw/note/monkhorstSpecialPointsBrillouinzone1976]]"
projects: [project-2, project-4, project-5, project-7]
concepts: [density-functional-theory, brillouin-zone-integration, monkhorst-pack-grid, k-point-sampling, special-points, chadi-cohen-method, gilat-raubenheimer-method, star-function, irreducible-wedge, fourier-interpolation]
entities: [VASP, Wannier90]
methods: [dft, brillouin-zone-integration, k-point-sampling, monkhorst-pack, fourier-interpolation, gilat-raubenheimer]
materials: []
figures: [mathematical-models]
"领域基础知识": >-
  固体物理中的能带理论，布里渊区（Brillouin Zone, BZ），倒空间，波矢（wave vector），晶格点群对称性，态密度（Density of States, DOS）。
"研究背景": >-
  在固体物理中，对布里渊区内的周期函数进行积分是计算电子结构、总能量及光谱性质的基础，但直接积分计算成本高昂，亟需高效、精确的数值积分方法。
"作者的问题意识": >-
  如何系统性地生成一组特殊的波矢点集，使得仅用这组点上的函数值进行加权求和，就能最高效且精确地近似整个布里渊区的积分，并揭示其数学本质。
"主要研究对象": >-
  布里渊区积分的数值计算方法，特别是特殊点集的生成方案及其数学性质。
"主要研究方法": >-
  数学推导与证明。通过构造均匀网格和对称化的星函数，证明在特定约束下，这些函数在离散点集上具有正交归一性，并以此为基础构建积分和插值公式。
"研究意义": >-
  提出了一种普适且高效的布里渊区积分方法，为现代第一性原理计算提供了标准工具（Monkhorst-Pack网格），极大地推动了计算材料科学的发展。
"研究结论": >-
  成功推导出一种生成特殊点集的方法，其核心在于一组由晶格对称性决定的函数在这些点上正交。该点集可用于布里渊区积分和全局插值，其收敛性良好，且与Chadi-Cohen和Gilat-Raubenheimer方法有内在联系。
"对领域的贡献": >-
  统一了Chadi-Cohen和Gilat-Raubenheimer两种重要的BZ积分方法，揭示了特殊点方法的数学本质，并提供了普适的点集生成方案。该方案成为计算物理和材料科学领域最广泛使用的标准技术之一。
"未来研究方向提及": >-
  发展更严格的先验误差分析理论；研究该方法对不同函数类型（特别是金属中费米面附近的不连续函数）的收敛性；探索在低对称性晶格中通过不同方向使用不同q值来优化网格。
"未来研究方向思考": >-
  1. 将Monkhorst-Pack网格与Wannier函数插值结合，发展线性标度电子结构方法。2. 针对强关联体系或拓扑材料中电子态的奇异性，设计自适应或非均匀的广义Monkhorst-Pack网格。3. 将本方法的思想扩展到更高阶的响应函数或多体微扰理论（如GW近似）中，以处理更复杂的积分核。4. 利用机器学习算法，根据体系的化学环境和电子结构特征，自动预测最优的q参数。
tags:
  - paper
  - type/method
  - year/1976
  - project/project-2
  - project/project-4
  - project/project-5
  - project/project-7
  - relevance/project-2/strong
  - relevance/project-4/strong
  - relevance/project-5/strong
  - relevance/project-7/strong
  - concept/density-functional-theory
  - concept/brillouin-zone-integration
  - concept/monkhorst-pack-grid
  - concept/k-point-sampling
  - concept/special-points
  - concept/chadi-cohen-method
  - concept/gilat-raubenheimer-method
  - concept/star-function
  - concept/irreducible-wedge
  - concept/fourier-interpolation
  - entity/VASP
  - entity/Wannier90
  - method/dft
  - method/brillouin-zone-integration
  - method/k-point-sampling
  - method/monkhorst-pack
  - method/fourier-interpolation
  - method/gilat-raubenheimer
  - topic/dft
  - topic/electronic-structure
  - topic/computational-methods
  - topic/brillouin-zone
---

## monkhorstSpecialPointsBrillouinzone1976 — 布里渊区积分的特殊点

- **元数据**：Hendrik J. Monkhorst, James D. Pack，1976，Physical Review B 13(12), 5188-5192，DOI 10.1103/PhysRevB.13.5188
- **一句话**：提出基于均匀倒空间网格与晶格星函数正交性的"Monkhorst-Pack网格"，成为所有现代第一性原理计算中布里渊区积分的标准k点采样方法。
- **现有wiki双链**：
  - 概念 [[../concepts/density-functional-theory]]
  - 实体 [[../entities/VASP]]、[[../entities/Wannier90]]
  - 图表 [[../figures/mathematical-models]]
  - 年度 [[../write/1976]]
  - 相关论文 [[../../raw/note/monkhorstSpecialPointsBrillouinzone1976]]
- **新概念/实体建议**：
  - `brillouin-zone-integration.md`（概念）：布里渊区积分，即对倒空间周期函数在整个或部分BZ上积分，是电荷密度、总能量、DOS等计算的核心步骤。
  - `monkhorst-pack-grid.md`（概念）：由整数q生成的均匀q×q×q倒空间网格，坐标u_r=(2r−q−1)/2q，是VASP等软件KPOINTS文件的标准生成方式。
  - `k-point-sampling.md`（概念）：k点采样的总称，包含MP网格、Gamma中心网格、对称性约化、收敛性测试等内容。
  - `special-points.md`（概念）：特殊点方法，利用点群对称性使离散求和精确积分低阶傅里叶分量。
  - `chadi-cohen-method.md`（概念）：Chadi-Cohen方法，从k=0泰勒展开出发递归生成特殊点，对应MP网格中q=2^n的子集。
  - `gilat-raubenheimer-method.md`（概念）：Gilat-Raubenheimer线性解析方法，在细网格上做局部线性化积分，可与MP全局插值组成混合方法。
  - `star-function.md`（概念）：星函数A_m(k)，由同一正格矢星（点群等价R集合）上平面波等权叠加构成的完全对称倒空间基函数。
  - `irreducible-wedge.md`（概念）：不可约楔形区，BZ在点群操作下不重复的最小区域，权重w_j为全点群阶与波矢群阶之比。
  - `fourier-interpolation.md`（概念）：基于星函数正交基的全局傅里叶插值，区别于局部线性/二次插值。
- **关键图表**：笔记未附图片（论文本身为纯理论推导，无数据图表；manifest.json中figures数组为空）。
- **项目连接**：
  - **project-2（Mn多铁）**：strong。Mn基多铁材料（BiFeO3、SrMnO3、MnVO3等）的DFT计算（电子结构、磁电耦合、Berry相极化）必须设置Monkhorst-Pack k点网格；本文是k点收敛性测试、偶数q选择、不可约楔形权重等实践的理论依据。
  - **project-4（TTF分子计算）**：strong。分子晶体/超胞的布里渊区采样同样依赖MP网格（尽管超胞可用较稀网格甚至Gamma点）；本文关于q奇偶性、低对称晶格各向异性q值的讨论对TTF这类低对称性分子晶体有直接指导意义。
  - **project-5（SnTe铁电模拟）**：strong。SnTe铁电相变的DFT模拟（Berry相极化、声子、能带）重度依赖k点采样密度；本文为k点收敛测试、金属/绝缘体区别对待、以及与Wannier插值结合提供方法论基础。
  - **project-7（CDW）**：strong。CDW材料（如TMDs）的费米面嵌套、电荷密度波计算需要密集k点网格；本文关于费米面内部分积分、光谱/DOS混合计算、以及金属体系需更密q值的讨论直接相关。
  - project-1（双光子）、project-3（机械发光NN）、project-6（湿度传感器）：无直接项目连接（实验/机器学习为主，不直接涉及BZ积分）。
- **组织与用词**：文章按"方法论提出→数学证明→积分/插值/误差分析→光谱应用→立方晶格附录"的经典理论物理结构展开。核心论证链：定义均匀q网格→构造对称化星函数A_m(k)→证明|R_i|<q/2约束下的离散正交归一性→导出积分与插值公式→评估误差与收敛性→推广至fcc/bcc及光谱计算。值得复用的术语：
  - Brillouin-zone integration / 布里渊区积分
  - special points / 特殊点
  - Monkhorst-Pack grid / Monkhorst-Pack网格
  - star (of lattice vectors) / 星（格矢星）
  - irreducible wedge / 不可约楔形
  - point-group symmetry / 点群对称性
  - Fourier interpolation / 傅里叶插值
  - hybrid method / 混合方法
- **可写入wiki的要点**：
  1. **网格定义**：k_{prs}=u_p b_1+u_r b_2+u_s b_3，其中u_r=(2r−q−1)/(2q)，r=1,...,q；在整个BZ生成q^3个均匀分布的k点。
  2. **星函数**：A_m(k)=|R_star|^{-1/2} Σ_{R∈star(m)} exp(ik·R)，按|R|从小到大编号（m=1对应R=0），在所有点群操作下完全对称。
  3. **正交性核心定理**：当所有相关星的格矢分量满足|R_i|<q/2（i=1,2,3）时，S_{mn}(q)=(1/q^3)Σ_{p,r,s} A_m(k_prs)A_n(k_prs)=δ_{mn}，即星函数在该离散点集上正交归一。
  4. **不可约楔形约化**：利用点群对称性，S_{mn}(q)=(1/P(q))Σ_j w_j A_m(k_j)A_n(k_j)，权重w_j=全点群阶/波矢群阶；简单立方(1,1,1)方向一般点w_j=48/6=8。
  5. **BZ积分公式**：∫_{BZ} f(k)dk ≈ f̃_0 = (Ω/P(q))Σ_j w_j f(k_j)，其中Ω为BZ体积；可推广至费米面内积分（乘以指示函数θ_FS）。
  6. **误差收敛**：误差来自|R_i|≥q/2的高阶星（混叠），ε_BZ=Σ_{m超界} f_m N^{1/2}S_m(q)；作者指出实际收敛更类似紧束缚重叠积分（可能指数级f_m~C e^{-αm^P}），快于CC基于泰勒展开的C^{-m}估计。
  7. **偶数q优势**：立方晶格中q=2l优于q=2l−1，因为P(2l−1)=P(2l)=l(l+1)(l+2)/6但偶数q能多拟合一个正交函数；q=2即Baldereschi均值点。
  8. **与CC方法关系**：Chadi-Cohen点集是MP方法在q=2^n（n=1,2,...）时的子集；MP方法允许任意偶数q（如6,10,12），在精度与成本间提供更灵活的中间档。
  9. **fcc/bcc处理**：将fcc或bcc的BZ嵌入更大的简单立方BZ（a_sc=a_0, a_fcc/bcc=2a_0），利用倒格矢平移筛选有效点；fcc不可约楔形点数P(q)=(q/96)(q+2)(q+4)（q/2偶）或(1/96)(q+2)(q^2+4q+12)（q/2奇）；bcc对应P(q)=(q/192)(q+4)(q+8)或(1/192)(q+2)(q+4)(q+6)。
  10. **光谱混合方法**：对I(ω)=∫dk F(k)δ(ω−ω(k))，先用粗MP网格做全局星函数展开得到F_m、Ω_m，再插值到细网格，最后用Gilat-Raubenheimer线性解析法在细网格上积分；属于"全局拟合+局部积分"的混合方法，对DOS等谱计算高效。
