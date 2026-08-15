---

project_id: P02

name: Mn极化结构铁电材料

zotero_collection_key: PTX5TBVQ

status: 论文撰写期

local_path: E:\swan_goose\燕燕\香香\项目二：Mn极化结构铁电材料\

---



# 项目二：Mn极化结构铁电材料



> **物理路径**：`E:\swan_goose\燕燕\香香\项目二：Mn极化结构铁电材料\`  

> **Zotero 文献池**：`科研项目文献池/项目二：Mn极化结构铁电材料` (`PTX5TBVQ`)



---



## 1. 项目简介与背景

针对含 Mn 元素的极化结构铁电/多铁材料开展第一性原理计算研究。项目从传统的块体钙钛矿（ABO₃）应变调控出发，现已扩展至二维范德华（vdW）体系下的**非范德华剥离单层**（如 MnVO₃）以及**Janus MXenes**（如 Mn₂N 系）体系。重点探索极化起源从“离子位移”向“层间滑移”与“能级对称性破缺”的演进，研究自旋劈裂（巨 Rashba 效应）、变换磁性（Altermagnetism）及其在超低功耗自旋电子器件中的应用。



## 2. 与科研 Wiki 知识库的联系

- **相关材料/实体**：[[../entities/BiFeO3|MnVO3]], [[../entities/BaTiO3|Mn2N]], [[../entities/BiFeO3|BiFeO3]], [[../entities/MXenes|MXenes]], [[../entities/CrI3|MnSe]]

- **相关物理概念**：[[../concepts/multiferroicity|多铁性]], [[../concepts/sliding-ferroelectricity|滑动铁电性]], [[../concepts/altermagnetism|变换磁性]], [[../concepts/giant-spin-splitting|巨自旋劈裂]], [[../concepts/janus-structure|Janus 结构]], [[../concepts/half-metallicity|半金属性]]

- **相关课题/主题**：[[../topics/D02-multiferroic-materials|多铁性材料]]



## 3. 进展汇报 (Progress)



### 3.1 基于高通量判据的 Mn 基多铁发现

集成 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] 提出的“键密度 + 结合强度”判据，本项目已完成对 MnVO₃ 及其同构氧化物的可剥离性评估。

- **MnVO₃ 单层性能**：识别为具有室温磁转变温度（$T_N \approx 300 \text{ K}$）的候选材料。其剥离能显著低于传统非范德华材料限值（$0.13 \text{ eV/Å}^2$），且在 300 K 下表现出动力学稳定性。

- **巨自旋劈裂**：在 Mn 基极性体系中预测到了巨自旋劈裂（$>0.4 \text{ eV}$），起源于 Mn 3d 与 O 2p 的强杂化以及极性场引起的反演对称性破缺。



### 3.2 Janus Mn₂N 的电子相变与自旋调制

通过对 Janus 结构 Mn₂N MXenes（如 Mn₂NOF, Mn₂NOOH）的系统模拟，揭示了电子输运态的全新调控逻辑 [[../papers/chen3dLevelSymmetry2025]]。

- **3d 能级对称性机制**：Mn₂N 的半金属性与半导体性转变不再仅受局域配位对称性控制，而是取决于**两侧金属层间 3d 能级的对称性/对齐度**。

- **多场调控能力**：通过极少量电荷掺杂（$0.02 \text{ e}^-/\text{atom}$）或微小单轴应变（$+3\%$ 至 $+7\%$），可驱动 Mn₂NOF 实现从半导体（带隙 $\approx 0.46 \text{ eV}$）到半金属的可逆相变。



### 3.3 2D 滑动多铁性与超快翻转

结合 [[../papers/sunSlidingFerroelectricityTwodimensional2025]] 综述，探索 MnSe 与 Mn 基 MXenes 中的滑动铁电与多铁耦合机制。

- **滑动翻转动力学**：采用“集体势垒”与“孤立势垒”分离的物理图像。滑动铁电机制下的翻转势垒仅为 meV/f.u. 量级，支持高达 **300 μm/s** 的畴壁运动速度与 **53 ns** 级的写入速度。

- **低功耗器件展望**：估算单次开关能耗可低至 $4.4 \times 10^{-4}$ 至 $4.9 \times 10^{-3} \text{ fJ}$，比当前 CMOS 器件低约两个数量级。



## 4. 技术框架与物理机制 (Technical Framework)



### 4.1 核心物理模型

1.  **3d-Level Symmetry 模型**：建立在 Janus 体系下两侧金属层能级分离（Energy-level separation）的物理图像，通过静电势差分析能级重排驱动的电荷转移。

2.  **变换磁性 (Altermagnetism)**：在 $P4bm$ 相等体系中，通过对称性分析（如 $OsO_5$-like 旋转）探索动量空间的非相对论性自旋劈裂。

3.  **滑动多铁耦合**：利用层间滑移同步翻转垂直极化与净磁矩，实现“电写磁读”。



### 4.2 计算协议扩展

- **强关联处理**：采用 GGA+U ($U_{Mn}=4.0 \text{ eV}$) 配合 HSE06 杂化泛函验证电子结构，并加入 SOC 考虑自旋各向异性。

- **磁学参数提取**：利用 **TB2J**（基于磁力理论 MFT）从第一性原理提取长程交换相互作用参数 $J$，用于 Monte Carlo 模拟转变温度。

- **相变路径计算**：使用 **cNEB** 方法确定相变最小能量路径（MEP）与势垒（Barrier）。



## 5. 知识积累与项目进展记录

- **2026-08-11**: 

    - **集成文献数据**：引入了 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] 的剥离判据与 MnVO₃ 的 $T_N$ 数据。

    - **修正机制描述**：根据 [[../papers/chen3dLevelSymmetry2025]] 修正了 Janus Mn₂N 的能级对称性控制逻辑。

    - **同步器件指标**：参考 [[../papers/sunSlidingFerroelectricityTwodimensional2025]] 优化了滑动多铁器件的能耗与速度估算。

- **2026-08-05**: 完成了基于应变介导磁电耦合机制的章节初稿。



---

**相关文献关联**:

- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]] (核心方法论：高通量筛选与非范德华剥离)

- [[../papers/chen3dLevelSymmetry2025]] (Janus Mn2N 与能级对称性调控)

- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] (滑动铁电与器件应用综述)

- [[../papers/wuSlidingFerroelectricity2D2021a]] (滑动铁电物理奠基综述)

