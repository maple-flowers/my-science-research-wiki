---
tags: [concept, topological-physics, semimetal]
title: 狄拉克半金属 / Dirac Semimetal (DSM)
type: concept
status: developing
domain: [condensed-matter-physics, topological-physics]
mechanism: 价带与导带在晶体对称性保护下形成四重简并、近线性色散的狄拉克节点
related_concepts: [topological-insulator, weyl-semimetal, type-ii-dirac-semimetal, spin-orbit-coupling, berry-phase, lifshitz-transition, strain-engineering]
key_quantities:
  IrTe2_strain: "约 0.1%（沿高温相 a 轴单轴拉伸）"
  IrTe2_dirac_shift: "约 350 meV（II 型体狄拉克点下移）"
  IrTe2_interlayer_hopping: "−0.156 eV → −0.014 eV（高温未应变相 → 应变 6×1 相）"
papers: [nicholsonUniaxialStraininducedPhase2021, sharmaRoomtemperatureFerroelectricSemimetal2019]
updated: 2026-08
---

# 狄拉克半金属 / Dirac Semimetal (DSM)

狄拉克半金属（Dirac semimetal, DSM）是价带与导带在动量空间离散点相接、节点附近呈近线性色散的拓扑半金属。含自旋体系中的一个狄拉克点通常可视为两个手性相反、位于同一动量与能量的外尔点重合，因而形成四重简并；这也意味着节点本身的净手性拓扑荷相消，稳定性必须依靠空间反演、时间反演以及额外晶体对称性共同维持。

它的关键不只是“没有带隙”，而是交叉是否真正受对称性保护、费米能级是否靠近节点，以及费米面在节点附近属于 I 型还是强倾斜的 II 型。仓库中的直接实例是应变稳定 6×1 相 IrTe₂：[[../papers/nicholsonUniaxialStraininducedPhase2021]]用角分辨光电子能谱（angle-resolved photoemission spectroscopy, ARPES）观测到 II 型体狄拉克色散，并把节点能量、层间耦合和费米面拓扑的协同变化联系起来。

## 👵 太奶导读

太奶，您可以把普通能带想成两条各走各路的立交桥，狄拉克半金属却让“上行桥”和“下行桥”在一个特别规整的路口尖尖相接。这个路口叫狄拉克点，附近的电子像轻装快跑一样呈近线性运动；“四重简并”就是说同一位置叠着四种量子通道。它能不被撞散，靠的是晶体左右、前后和旋转等规矩共同保护；若破坏关键规矩，路口可能裂成外尔点或被填成有带隙的状态。II 型狄拉克点则像被大风吹歪的路口，交点旁同时带着电子和空穴口袋，因此不能只看一个漂亮的 X 形就下结论。

## 🧩 定义、低能图像与分类

在节点附近，导带与价带沿动量方向近似线性相交，低能准粒子可用三维狄拉克型哈密顿量描述。判定 DSM 至少要区分三层含义：

- **能谱层**：存在离散的近线性交叉，而不是普通抛物线带边、偶然交叉或一整条节点线。
- **简并层**：含自旋体系的狄拉克节点为四重简并，可理解为两份相反手性的二重外尔节点重合。
- **保护层**：仅有空间反演 $\mathcal P$ 与时间反演 $\mathcal T$ 保证 Kramers 型成对简并还不够；通常还需旋转、镜面或非平凡空间群表示阻止两支能带杂化开隙。

按锥体倾斜程度，I 型节点附近的费米面在理想节点能量收缩为点；II 型则因倾斜过强，在节点处仍位于电子口袋与空穴口袋接触的位置。[[../papers/nicholsonUniaxialStraininducedPhase2021]]在 IrTe₂ 的应变 6×1 相中看到的是后者，因此本页将 [[../concepts/type-ii-dirac-semimetal|II 型狄拉克半金属]]作为 DSM 的子类而不是同义词。

## 🧭 判据与实验识别

“能带看起来像 X”只是候选证据，可靠判定还需把能谱、对称性与费米面合在一起：

1. **交叉位置与维数**：ARPES 或计算应给出交叉的动量、能量及三维色散；变光子能量 ARPES 可追踪 $k_z$，区分体态与表面态。
2. **简并与轨道表征**：确认交叉带的轨道来源、简并度和允许的对称性表示，排除矩阵元缺失造成的“假交叉”。
3. **对称性保护**：检验保持关键晶体对称性时交叉不杂化，而破坏保护对称性后节点分裂或开隙。
4. **费米面拓扑**：确认费米能级附近电子/空穴口袋如何在节点相接，并追踪调控引起的 [[../concepts/lifshitz-transition|Lifshitz 转变]]。

IrTe₂ 的证据链体现了这一思路：单轴应变先把混杂的低温相选择为宏观单一 6×1 相，锐化 ARPES 能带；随后变光子能量测量确认显著的 $k_z$ 色散及其减弱，A 点附近切片显示多个部分重叠的锥形色散。论文同时指出这些复杂锥结构的具体起源仍待理论澄清，所以“观测到 II 型体狄拉克态”与“所有交叉细节均已解释”应严格区分 [[../papers/nicholsonUniaxialStraininducedPhase2021]]。

![图：应变 6×1 相 IrTe₂ 的层间键、三维色散与 II 型狄拉克锥](../../raw/figures/nicholsonUniaxialStraininducedPhase2021/fig_4_SRHBAT5F.png)
*   **关键特征**：图 a 显示多数层间 Te–Te 键在 6×1 相中减弱；图 b 以变光子能量 ARPES 比较 30 K 与 300 K 的 $k_z$ 色散；图 c 在不同 $k_y$ 切片中显示倾斜、部分重叠的锥形色散；图 d 给出相应费米面切片位置。该图支持“层间解耦—准二维化—II 型狄拉克色散与 Lifshitz 转变”这一整条论证，而非单凭 X 形外观判定。
*   **来源**：[[../papers/nicholsonUniaxialStraininducedPhase2021]] -> [[../figures/electronic-bands-dos-fermi|态密度与费米面]]

## 🔀 对称性破缺后的边界状态

DSM 常被视为多种拓扑相之间的临界或母相，但“破缺任一对称性就必然得到某一固定相”并不准确：结果取决于破坏的是空间反演、时间反演还是保护交叉的晶体对称性，以及允许出现的质量项。一般而言，解除重合可把一个狄拉克点拆成分离的外尔点；允许原本禁阻的杂化则会开隙，开隙后的相还需由拓扑不变量判断是普通绝缘体还是 [[../concepts/topological-insulator|拓扑绝缘体]]。

[[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]研究的 Td-WTe₂ 是极性、非中心对称的 II 型 [[../concepts/weyl-semimetal|外尔半金属]]，不是狄拉克半金属。它在本页中的作用是提供清楚的边界对照：空间反演对称性已经缺失时，正反手性节点不再被要求重合；其含 [[../concepts/spin-orbit-coupling|自旋—轨道耦合]]能带和电子—空穴口袋说明，材料的“半金属”“极性”和“外尔/狄拉克拓扑”必须分别判定，不能由线性色散或低载流子密度相互替代。

## 🎯 应变、维度与费米能级调控

DSM 的可观测性受三个尺度共同限制：节点相对费米能级的能量偏置、层间耦合决定的三维性，以及相/畴混合造成的谱线展宽。IrTe₂ 展示了这些因素可被很小的应变联动调节：沿高温相 $a$ 轴约 0.1% 的拉伸应变稳定毫米量级的 6×1 单畴；Ir→Te 电荷转移填充层间 Te–Te 反键态，使层间跳跃 $t_c$ 从 −0.156 eV 降到 −0.014 eV，并把 II 型体狄拉克点下移约 350 meV 至占据态，从而进入 ARPES 可见窗口并触发费米面 Lifshitz 转变 [[../papers/nicholsonUniaxialStraininducedPhase2021]]。

这组结果也说明尺度与边界效应不能简化为“越薄越像狄拉克体系”。减弱层间耦合会使电子结构准二维化，但表面重构、应变松弛、衬底势和有限厚度量子化也可能移动、混合或打开节点；相畴共存还会在宏观谱中把本征色散平均成宽峰。比较不同样品时，应同步报告温度、应变方向与大小、结构相、畴尺度、$k_z$ 探测条件和费米能级位置。

## 💾 物性与应用边界

线性色散和电子—空穴补偿使 DSM 候选体系适合研究高迁移率输运、磁阻、量子振荡以及可调拓扑相变；若能以应变、电场、磁序或界面选择性地移动、分裂或打开节点，还可用于拓扑开关和应变敏感器件。不过，仓库中的 IrTe₂ 工作主要完成了相选择与光谱学识别，论文明确把大非饱和磁阻、电阻率各向异性及压缩应变下可能的拓扑超导列为待验证方向，尚不能写成已实现的器件性能 [[../papers/nicholsonUniaxialStraininducedPhase2021]]。

## 📚 相关论文 (Related Papers)

- [[../papers/nicholsonUniaxialStraininducedPhase2021]]：以约 0.1% 单轴拉伸稳定 IrTe₂ 的 6×1 单畴，利用 ARPES、STM/LEED、XPS 与计算揭示 II 型体狄拉克态、节点下移约 350 meV、层间跳跃降低约十倍及伴随的 Lifshitz 转变。
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]]：以非中心对称 Td-WTe₂ 的 II 型外尔半金属为对照，说明空间反演破缺后外尔节点与极性、半金属性可共存，并提供狄拉克母相对称性边界的材料参照。

## 📋 关键参数表

下表只收录仓库论文页及其原始图注中条件明确的量；它们是应变 6×1 相 IrTe₂ 的实例参数，不是所有 DSM 的普适常数。

| 参数 | 数值 / 范围 | 条件 | 物理意义 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| 单轴拉伸应变 | 约 0.1% | 沿 IrTe₂ 高温相 $a$ 轴；低温稳定 6×1 相 | 打破竞争相近简并并形成宏观单一取向相，使狄拉克谱可分辨 | [[../papers/nicholsonUniaxialStraininducedPhase2021]] |
| 宏观单相区域 | 约 $0.5\times0.4\ \text{mm}^2$ | 应变 6×1 相，微区 ARPES 成像 | 表明畴尺度较未应变样品扩大约四个数量级，减少谱线空间平均 | [[../papers/nicholsonUniaxialStraininducedPhase2021]] |
| 面内跳跃 | $t_a=-0.53\ \text{eV}$ | 6×1 相紧束缚拟合 | 给出准二维电子结构中的主要面内能标 | [[../papers/nicholsonUniaxialStraininducedPhase2021]] |
| 层间跳跃 | $t_c:-0.156\to-0.014\ \text{eV}$ | 未应变高温相 → 应变 6×1 相 | 量化层间耦合约十倍减弱及电子结构准二维化 | [[../papers/nicholsonUniaxialStraininducedPhase2021]] |
| 狄拉克点能量位移 | 下移约 350 meV | Ir→Te 电荷转移后，II 型体狄拉克点进入占据态 | 触发费米面拓扑变化并使节点进入 ARPES 可观测能窗 | [[../papers/nicholsonUniaxialStraininducedPhase2021]] |
| 狄拉克锥横向切片 | $k_y=-0.05\ \text{Å}^{-1}$ 处见两个部分重叠锥；另有约 $\pm0.15\ \text{Å}^{-1}$ 弧形特征 | A 点附近 ARPES，20 eV 光子能量 | 显示实际狄拉克色散比单一理想锥更复杂；起源尚未确认 | [[../papers/nicholsonUniaxialStraininducedPhase2021]] |
| 普适节点速度、迁移率与磁阻 | 未确认 | 仓库现有直接相关资料未给出可归入 DSM 普适页的可靠统一值 | 避免把特定材料或待验证输运预期误写成普适参数 | 仓库资料不足 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/type-ii-dirac-semimetal|II 型狄拉克半金属]]（强倾斜狄拉克锥子类）
- [[../concepts/weyl-semimetal|外尔半金属]]（解除相反手性节点重合后的邻近相）
- [[../concepts/topological-insulator|拓扑绝缘体]]（节点开隙后的可能拓扑相）
- [[../concepts/spin-orbit-coupling|自旋—轨道耦合]]（重元素能带简并与拓扑演化的重要作用）
- [[../concepts/berry-phase|Berry 相位]]（表征能带几何与拓扑性质的工具）
- [[../concepts/lifshitz-transition|Lifshitz 转变]]（费米面拓扑随节点能量移动而改变）
- [[../concepts/strain-engineering|应变工程]]（选择结构相并调节节点和层间耦合）
- [[../entities/IrTe2|IrTe₂]]（仓库中应变可调 II 型体狄拉克态的直接实例）
- [[../entities/WTe2|WTe₂]]（非中心对称 II 型外尔半金属对照）
