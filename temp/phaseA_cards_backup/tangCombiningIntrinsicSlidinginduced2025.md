---
citekey: tangCombiningIntrinsicSlidinginduced2025
title: "Combining intrinsic and sliding-induced polarizations for multistates in two-dimensional ferroelectrics"
authors: [Chuhan Tang, Zhiqiang Tian, Tao Ouyang, Anlian Pan, Mingxing Chen]
year: 2025
journal: "Physical Review B"
doi: "10.1103/PhysRevB.111.L081407"
url: "https://doi.org/10.1103/PhysRevB.111.L081407"
paper_type: theory
status: ingested
year_read: 2026
original_note:: [[../../raw/note/tangCombiningIntrinsicSlidinginduced2025]]
projects: [project-5, project-7]
concepts: [sliding-ferroelectricity, polarization-switching, berry-phase, 2D-materials, ferroelectric-tunnel-junction, charge-density-wave, composite-ferroelectricity, polarization-multistates, layer-selective-switching, interlayer-polarization-coupling]
entities: [VASP, TMDs, h-BN, In2Se3, SnTe, MoSe2, 1T-double-prime-TMD]
methods: [dft, vasp, pbe, paw, dft-d3, berry-phase, neb, aimd, monkhorst-pack]
materials: [1T-double-prime-MoSe2, 1T-double-prime-MoS2, 1T-double-prime-MoTe2, h-BN, In2Se3, CuInP2S6, SnTe]
figures: [heterostructures-stacking]
领域基础知识:: >-
  铁电性（Ferroelectricity）是材料具有自发极化、且极化方向可被外电场翻转的特性。二维铁电材料分为两类：一是本征铁电体，由离子位移产生极化（PI）；二是滑移铁电体，由非极性层的特定堆叠，通过层间电子重构产生极化（PS）。翻转两者的能量势垒有数量级差异，是本研究的关键。
研究背景:: >-
  为提升非易失性存储器的密度，铁电材料需要不断降低厚度，但传统钙钛矿铁电体在薄膜厚度降至临界值时铁电性会消失。二维铁电体因无悬挂键而能解决此缩放问题，但现有体系仍大多局限于双稳态（0和1），难以实现存储密度的革命性突破。
作者的问题意识:: >-
  如何超越传统铁电存储器的双稳态限制，在单一二维体系中实现更多的极化状态，以大幅提升信息存储密度？作者的核心思路是利用两种不同物理机制（本征与滑移）产生的极化，通过它们对外电场响应的巨大差异，实现多态操控。
主要研究对象:: >-
  1T′′相的过渡金属硫族化合物（TMD）双层及三层范德华结构，特别是H型堆叠的1T′′-MoSe₂。该材料同时具有本征面外极化（源于1T′′相的结构畸变）和滑移诱导极化（源于H堆叠下的特定层间相对位置）。
主要研究方法:: >-
  基于密度泛函理论（DFT）的第一性原理计算。使用VASP软件包，采用PBE泛函、投影缀加平面波（PAW）方法、DFT-D3范德华校正。用Berry相位法计算极化值，用微动弹性带（NEB）方法计算极化翻转和层间滑移的能量势垒与最小能量路径。
研究意义:: >-
  本研究提出了一种全新的铁电多态设计范式，即"复合铁电体"概念。通过理论计算，在双层和三层1T′′-MoSe₂中分别实现了六重和十重极化态，展示了将存储密度提升数倍（如2.58倍和3.32倍）的潜力，为下一代超高密度存储技术提供了理论依据和材料蓝图。
研究结论:: >-
  通过结合本征和滑移诱导极化，可以在二维铁电体中实现多态。两种极化翻转势垒的显著差异，导致了一种独特的"逐层滑移-逐层翻转"机制。在1T′′-MoSe₂的H型堆叠双层和三层中，通过精确控制外电场，分别理论预测了6个和10个可切换的极化状态。
对领域的贡献:: >-
  1. 提出了结合本征与滑移铁电性构建多态的新概念，打破了铁电存储双稳态的思维定式。2. 揭示了一种全新的"逐层滑移-逐层翻转"极化切换机制，为多态操控提供了物理基础。3. 通过第一性原理计算，在具体材料（1T′′-TMDs）中验证了该概念的可行性，提供了清晰的理论和计算证据。
未来研究方向提及:: >-
  1. 将本概念推广到其他具有类似特征的二维铁电体（如In₂Se₃, CuInP₂S₆）。2. 在实验上，迫切需要利用压电力显微镜（PFM）等手段证实这些理论预测的多态。3. 基于此多态物理机制，设计并探索新型电子器件（如多态铁电隧道结）的应用。
未来研究方向思考:: >-
  1. 研究多态在室温下的热稳定性及保持时间，评估其在实际工作条件下的可靠性。2. 探索多态的高效、低串扰电学读取方案，例如，利用不同极化态对应的不同隧道电阻值进行区分。3. 研究缺陷（如空位）和界面（如与电极的接触）对这种精细多态切换过程的影响，这对器件制备至关重要。4. 分析并尝试利用作者忽略的面内极化分量，探索其与面外极化多态可能存在的耦合，构建更丰富的物理体系。
tags:
  - paper
  - type/theory
  - year/2025
  - project/project-5
  - project/project-7
  - relevance/project-5/strong
  - relevance/project-7/weak
  - concept/sliding-ferroelectricity
  - concept/polarization-switching
  - concept/berry-phase
  - concept/2d-materials
  - concept/ferroelectric-tunnel-junction
  - concept/charge-density-wave
  - concept/composite-ferroelectricity
  - concept/polarization-multistates
  - concept/layer-selective-switching
  - concept/interlayer-polarization-coupling
  - entity/VASP
  - entity/TMDs
  - entity/h-BN
  - entity/In2Se3
  - entity/SnTe
  - entity/MoSe2
  - entity/1T-double-prime-TMD
  - method/dft
  - method/vasp
  - method/pbe
  - method/paw
  - method/dft-d3
  - method/berry-phase
  - method/neb
  - method/aimd
  - material/1T-double-prime-MoSe2
  - material/1T-double-prime-MoS2
  - material/1T-double-prime-MoTe2
  - material/h-BN
  - material/In2Se3
  - material/CuInP2S6
  - material/SnTe
  - topic/ferroelectricity
  - topic/2d-materials
  - topic/sliding-ferroelectricity
  - topic/multistate-memory
  - topic/polarization-switching
---

## tangCombiningIntrinsicSlidinginduced2025 — 二维铁电体中本征极化与滑动诱导极化的结合以实现多态

## 📄 元数据
Tang, Tian, Ouyang, Pan, Chen et al.，2025，Physical Review B 111, L081407，DOI 10.1103/PhysRevB.111.L081407
## 💡 一句话
在同一二维范德华体系中结合本征极化（PI，离子位移、高势垒）与滑移诱导极化（PS，层间电子重构、低势垒），利用两者势垒相差一个数量级而实现电场分级控制，在 H 堆叠 1T″-MoSe₂ 双层/三层中分别预测出 6 个和 10 个可切换极化态。

## 🔗 Wiki 双链
  - 概念 [[../concepts/sliding-ferroelectricity|滑移铁电性]]
  - 概念 [[../concepts/polarization-switching|极化翻转]]
  - 概念 [[../concepts/berry-phase|Berry相位]]
  - 概念 [[../concepts/2d-materials|二维材料]]
  - 概念 [[../concepts/ferroelectric-tunnel-junction|铁电隧道结]]
  - 概念 [[../concepts/charge-density-wave|电荷密度波]]
  - 概念 [[../concepts/composite-ferroelectricity|复合铁电体]]
  - 概念 [[../concepts/polarization-multistates|极化多态]]
  - 概念 [[../concepts/layer-selective-switching|层选择性翻转]]
  - 概念 [[../concepts/interlayer-polarization-coupling|层间极化耦合]]
  - 实体 [[../entities/VASP]]
  - 实体 [[../entities/TMDs]]
  - 实体 [[../entities/h-BN]]
  - 实体 [[../entities/In2Se3]]
  - 实体 [[../entities/SnTe]]
  - 实体 [[../entities/MoSe2]]
  - 实体 [[../entities/1T-double-prime-TMD]]
  - 图表 [[../figures/heterostructures-stacking|层间滑移铁电：机制、翻转与动力学]]
  - 年度 [[../write/2025-2029|2025]]
  - 项目 [[../projects/project-5-snte-ferroelectric-sim]]
  - 项目 [[../projects/project-7-cdw-charge-density-wave]]
  - 相关论文 [[../../raw/note/tangCombiningIntrinsicSlidinginduced2025]]

## 🆕 新概念/实体建议
  - [[../entities/1T-double-prime-TMD|1T-double-prime-TMD]]（1T″相过渡金属硫族化合物）：由 1T 相 2×2 重构而来，过渡金属形成收缩/扩张三角形，硫族原子面外位移产生本征 OOP 极化；建议作为实体条目。
  - [[../entities/MoSe2|MoSe2]]（二硒化钼）：本文主算例材料，单层 PI 翻转势垒 271 meV/f.u.，极化 0.18 pC/m。

## 📊 关键图表
  - ![图1 本征+滑移极化的八态概念模型（FE/AFE 耦合）](../../raw/figures/tangCombiningIntrinsicSlidinginduced2025/fig_1_5ZZ65FF7.png) → [[../figures/heterostructures-stacking|异质结与堆叠]]
    - **图示描述**：概念示意图，(a) 双层结构侧视给出层间铁电耦合（FE，两层 PI 同向）与反铁电耦合（AFE，头对头/尾对尾）两种排列，红箭头为本征极化 PI、绿箭头为滑移诱导极化 PS；(b) 俯视展开 H 堆叠下 PI 上下方向与 PS 配置组合出的全部八种极化组态。
    - **关键特征**：两个自由度（每层 PI 方向 + 层间 PS）组合给出 2³=8 个理论态；FE/AFE 耦合由层内 PI 相对方向决定；尾对尾 AFE 组态在后续电场合规切换路径中不出现，故双层实际可切换态缩减为 6 个。
    - **结论/意义**：该图奠定"复合铁电体"概念基础——单一体系同时容纳离子位移型与滑移型两种极化，状态数远超任一单一机制。
  - ![图2 1T″-MoSe2 单层结构、PI 翻转势垒(271 meV/f.u.)、八种 H 堆叠构型及差分电荷密度](../../raw/figures/tangCombiningIntrinsicSlidinginduced2025/fig_2_QPPY5P3H.png) → [[../figures/heterostructures-stacking|异质结与堆叠]]
    - **图示描述**：材料实现证据图。(a) 1T″-MoSe₂ 单层几何，由 1T 相 2×2 重构而来，Mo 原子形成收缩/扩张三角形导致 Se 面外位移；(b) NEB 给出单层 PI 翻转能量势垒；(c)–(j) H 堆叠双层八种构型 S1–S8 及各自 PS 符号；(k)–(p) S5、S6 在不同层间极化耦合（IPC）下的平面平均差分电荷密度 Δρ（e/Å），红蓝区分别对应电子积累/耗尽。
    - **关键特征**：单层 PI 翻转势垒 271 meV/f.u.（MoS₂ 212、MoTe₂ 306 meV/f.u.）；Berry 相极化 0.18 pC/m（MoS₂ 0.32、MoTe₂ 0.22 pC/m），折算约 0.018 μC/cm²；八种构型 PS 符号按 {S1,S3,S5} 与 {S2,S4,S6} 分为两组，符号不随 IPC 改变（堆叠顺序不变、电子重构保持）；Δρ 显示层间电子积累/耗尽导致电荷重心偏移，PS 幅值可大于 PI；各堆叠均为能量局域极小，构型间能量差约 20 meV/f.u.。
    - **结论/意义**：差分电荷密度直接证实 PS 的电子起源，高 PI 势垒与低滑移势垒的数量级差为电场分级控制提供材料基础。
  - ![图3 双层六态切换：滑移路径 NEB 势垒、HP+/LP−₂/LP−₁/HP− 循环及各态净极化](../../raw/figures/tangCombiningIntrinsicSlidinginduced2025/fig_3_CJWERQTE.png) → [[../figures/heterostructures-stacking|异质结与堆叠]]
    - **图示描述**：双层切换机制核心图。(a)(b) 固定层内极化向下时各堆叠间滑移 NEB 路径与势垒；(c) 外电场 E₁↓/E₂↓/E₃↓ 驱动下 HP⁺→LP⁻₂→LP⁻₁→HP⁻ 再反向回到 HP⁺ 的六态循环；(d) 六态净极化值（pC/m）及相邻态间转换势垒。
    - **关键特征**：S2→S5 势垒约 44 meV/f.u.，远低于 S2→S3 的约 325 meV/f.u.，系统优先走 S2→S5→S6→S3 低能路径，构成"逐层滑移"；S5↔S6 势垒约 38–46 meV/f.u.；LP⁻₂ 中顶层 PI 翻转势垒比底层低 10 meV/f.u.，使中等电场只翻顶层（LP⁻₂→LP⁻₁），更大电场才翻底层（LP⁻₁→HP⁻）；六态 HP⁺、LP⁻₂、LP⁻₁、HP⁻、LP⁺₂、LP⁺₁ 均为能量局域极小，对应 log₂6≈2.58 bit/单元。
    - **结论/意义**：势垒差与层不对称共同实现"逐层滑移-逐层翻转"，是双层六态可被电场分级寻址的物理依据。
  - ![图4 三层十态切换：堆叠顺序、逐层滑移-逐层翻转路径、E1<E2≈E3<E4<E5 电场分级](../../raw/figures/tangCombiningIntrinsicSlidinginduced2025/fig_4_WYM5EB9V.png) → [[../figures/heterostructures-stacking|异质结与堆叠]]
    - **图示描述**：三层拓展图。(a)–(e) H 堆叠三层 1T″-MoSe₂ 在切换中涉及的五种堆叠顺序；(f) 从 HP⁺₁ 出发经多次逐层滑移和逐层翻转至 HP⁻₁ 的十态切换路径；(g) 十态净极化大小及相邻转换势垒，给出所需电场趋势。
    - **关键特征**：底层滑移势垒 12 meV/f.u. 低于顶层 13 meV/f.u.，故先发生层选择性滑移；LP⁺₂ 态中中间层因承受两个反向层间极化的有效内场，其 PI 翻转势垒反而低于顶/底层，被优先翻转；顶/底层 PI 翻转势垒差约 16 meV/f.u.；所需电场满足 E₁↓ < E₂↓ ≈ E₃↓ < E₄↓ < E₅↓；共 10 个可切换态，对应 log₂10≈3.32 bit/单元。
    - **结论/意义**：证明多态机制可向更多层推广，状态数随层数增长，但需 ML 势/多尺度方法应对构型空间指数膨胀。
  - ![表I S5/S6 堆叠下 PT_I、PB_I、PS、Ptot（pC/m）数值](../../raw/figures/tangCombiningIntrinsicSlidinginduced2025/tab_5_L73S9YPF.png)
    - **图示描述**：表 I 列出 S5、S6 两种堆叠在四种层内极化组态（↑↑、↓↓、↑↓、↓↑）下的顶层本征极化 PT_I、底层本征极化 PB_I、滑移诱导极化 PS 与总极化 Ptot，单位均为 pC/m。
    - **关键特征**：同一堆叠下 PS 符号在四种 IPC 中保持一致（S5 全为负、S6 全为正），仅幅值小幅变化（S5 约 −0.29 至 −0.69 pC/m，S6 约 0.30 至 0.69 pC/m）；PT_I/PB_I 随层内方向翻转在 ±0.16 至 ±0.23 pC/m 范围；Ptot 在 −0.69 至 +0.69 pC/m 间变化，FE 耦合 ↑↑/↓↓ 给出最大净极化，AFE 耦合 ↑↓/↓↑ 给出较低但非零的净极化。
    - **结论/意义**：定量印证 PS 符号由堆叠顺序决定、与 IPC 解耦，且 PS 可与 PI 量级相当甚至更大，是多态极化可分辨性的数据基础。

## 🔬 项目连接
  - **project-5（SnTe 铁电模拟）— strong**：本文是 2D 铁电方法学核心文献。引言引用 Chang et al. Science 2016 在原子级厚度 SnTe 中发现面内铁电性[6]，与项目材料直接同源；计算流程（VASP + PBE + PAW + DFT-D3 + Berry 相极化 + NEB 翻转势垒 + AIMD 热稳定性）正是 SnTe 铁电模拟可复用的标准流程；"层选择性翻转""逐层滑移-逐层翻转"机制及电场分级控制思想，对 SnTe 薄膜/多层的极化翻转路径设计有直接类比价值；多态铁电隧道结（FTJ）的器件设想也与 SnTe 铁电存储方向契合。
  - **project-7（CDW）— weak**：1T″ 相由 1T 相的 2×2（以及 d1T 的 √3×√3）结构重构产生，这种周期性晶格畸变本身具有 CDW 畸变的形式特征；论文虽未以 CDW 为主线，但 1T/d1T TMD 是经典 CDW 体系，其结构重构-电子重构耦合图像可与 CDW 物理相互参照。
  - 其他项目（project-1/2/3/4/6）无直接项目连接。

## 🔗 项目双链
- 项目 [[../projects/project-5-snte-ferroelectric-sim|项目五：lammps势函数SnTe铁电模拟]]
- 项目 [[../projects/project-7-cdw-charge-density-wave|项目七：CDW电荷密度波]]

## 📝 组织与用词
论文为 PRB Letter，按"概念提出（Model and concept）→ 材料实现（Material realization）→ 多态切换（Switching）→ 结论"四段式组织。论证主线是"两种极化势垒差一个数量级 → 电场可分级 → 层不对称导致逐层选择性 → 多态"。值得在 wiki 叙述中复用的术语：
  - intrinsic polarization (PI) — 本征极化
  - sliding-induced polarization (PS) — 滑移诱导极化
  - layer-by-layer sliding followed by layer-by-layer flipping — 逐层滑移-逐层翻转
  - layer-selective flipping — 层选择性翻转
  - interlayer polarization coupling (IPC) — 层间极化耦合（FE/AFE）
  - H-stacking / R-stacking — H 堆叠 / R 堆叠
  - energy local minimum — 能量局域极小（亚稳态）
  - high/low polarization state (HP/LP) — 高/低极化态
  - composite ferroelectrics — 复合铁电体

## ✏️ 可写入 Wiki 的要点
  1. **核心机制**：PI（离子位移，势垒 ~66–306 meV/f.u.）与 PS（层间范德华滑移，势垒 ~9–71 meV/f.u.）相差至少一个数量级，使得小电场只翻 PS、大电场才翻 PI，从而可在同一体系中分级操控两种极化。
  2. **双层八态→六态**：同时具有 PI 和 PS 的双层理论上有 2³=8 种极化组态，但尾对尾 AFE 耦合态在切换路径中不出现，实际可电场合规切换的稳定态为 6 个（HP⁺、LP⁻₂、LP⁻₁、HP⁻、LP⁺₂、LP⁺₁），对应 log₂6≈2.58 bit/单元。
  3. **三层十态**：三层 H 堆叠 1T″-MoSe₂ 中遵循同样机制可实现 10 个可切换态（≈3.32 bit/单元），所需电场趋势 E₁↓ < E₂↓ ≈ E₃↓ < E₄↓ < E₅↓；中间层因承受两个反向层间极化的有效内场，其[[../concepts/switching-barrier|翻转势垒]]反而最低。
  4. **1T″-MoSe₂ 数据**：单层 PI 翻转 NEB 势垒 271 meV/f.u.（MoS₂ 212、MoTe₂ 306 meV/f.u.）；Berry 相极化 0.18 pC/m（MoS₂ 0.32、MoTe₂ 0.22 pC/m），按平板电势范围折算为 0.018 μC/cm²，与 InSe 双层相当、远小于 BaTiO₃ 块体。
  5. **滑移路径选择**：从 S2 出发，S2→S5（~44 meV/f.u.）远低于 S2→S3（~325 meV/f.u.），系统优先走低势垒路径 S2→S5→S6→S3，而非直接滑移，这是"逐层滑移"的能量学基础。
  6. **[[../concepts/layer-selective-switching|层选择性翻转]]来源**：LP⁻₂ 态中顶层 PI 翻转势垒比底层低 10 meV/f.u.（三层中顶/底层差约 16 meV/f.u.），这一差异与滑移势垒同量级，恰好使电场能在翻转一层后停住，再以更大电场翻转下一层。
  7. **PS 的电子起源与符号**：差分[[../concepts/charge-density|电荷密度]]（平面平均 Δρ，单位 e/Å）显示层间电子积累/耗尽导致电荷重心偏移；对 1T″ 双层 H 堆叠，八种构型按 PS 符号分为 {S1,S3,S5} 与 {S2,S4,S6} 两组，PS 符号不随 IPC 改变（因堆叠顺序不变、电子重构保持），且 PS 幅值可大于 PI。
  8. **计算细节**：VASP、PBE-GGA、PAW、DFT-D3、12×12 Monkhorst–Pack k 网格、400 eV 平面波截断；AIMD 验证单层/双层在室温下几何结构与极化均保持；还预测了面内极化分量但本文聚焦 OOP。
  9. **普适性**：概念适用于任何同时具有本征和[[../concepts/sliding-ferroelectricity|滑移铁电性]]的 2D 体系（In₂Se₃、CuInP₂S₆、d1T-TMDs 等），仅滑移（双层 2 态）或仅本征（双层 3 态）的体系状态数远少于复合体系；层数增加可获得更多态，但需 ML 势/多尺度方法来处理指数增长的构型空间。
  10. **批判性局限**：相邻 LP 态净极化值差异小，电学读取易受噪声影响；多级电场精度和缺陷/界面下的路径鲁棒性是工程挑战；~10 meV/f.u.（≈116 K）势垒差的室温热稳定性存疑；PBE-D3 可能低估 vdW 相互作用影响滑移势垒绝对精度；面外电场如何有效驱动切向层滑的微观动力学尚需澄清。
