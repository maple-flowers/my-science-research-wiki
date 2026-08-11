---
citekey: Zhang2002b
title: "Cellular automaton model to simulate nucleation and growth of ferrite grains for low-carbon steels"
authors: [L. Zhang, C. C. Zhang, Y. Y. Wang, X. X. Liu, G. G. Wang]
year: 2002
journal: "Journal of Materials Research"
doi: "10.1557/JMR.2002.0331"
url: "https://doi.org/10.1557/JMR.2002.0331"
paper_type: method
status: ingested
year_read: 2026
original_note: "[[../../raw/note/Zhang2002b]]"
projects: []
concepts: [cellular-automaton, nucleation-and-growth, diffusion-controlled-transformation, undercooling, grain-boundary-nucleation, super-element-approximation, latent-heat, cementite-precipitation, continuous-cooling-transformation, grain-refinement]
entities: [low-carbon-steel, ferrite, austenite, cementite, fe-c-phase-diagram]
methods: [cellular-automaton-method, explicit-finite-volume-method, diffusion-simulation, probabilistic-nucleation, microstructure-modeling]
materials: [low-carbon-steel, ferrite, austenite, cementite]
figures: [crystal-structures, mathematical-models]
"领域基础知识": >-
  低碳钢的微观组织（尤其是铁素体晶粒尺寸）决定其力学性能。γ (奥氏体) → α (铁素体) 的固态相变是控制其最终组织的关键过程，该过程受热力学、扩散动力学和形核/生长机制共同支配。
"研究背景": >-
  精确预测和控制低碳钢在热加工（如控轧控冷）中的铁素体晶粒尺寸是工业界的迫切需求。然而，γ→α相变是一个涉及热-质传递、形核与生长等多物理场耦合的复杂过程，传统的实验方法难以定量、动态地揭示其微观机制，需要依靠计算机模拟。
"作者的问题意识": >-
  如何建立一个能够动态模拟低碳钢γ→α相变全过程的计算模型，以定量理解冷却速率等关键工艺参数如何通过影响微观的形核、生长和扩散过程，最终决定宏观的铁素体晶粒尺寸和均匀性？
"主要研究对象": >-
  低碳钢（以Fe-C-Si-Mn系为代表，简化为超元素S-C二元合金）在连续冷却过程中，铁素体晶粒的形核与生长行为及其最终微观组织。
"主要研究方法": >-
  二维元胞自动机模拟。该方法在一个六边形网格上，将每个元胞赋予奥氏体、铁素体或界面等状态，并基于显式有限差分法实时计算溶质浓度场和温度场的扩散，将热力学驱动力和扩散动力学转化为概率性的形核与生长规则，从而动态模拟微观组织的演变。
"研究意义": >-
  提供了一种理解和预测低碳钢相变微观组织演变的新方法，将元胞自动机从凝固领域成功拓展到固态相变领域。该模型能够揭示实验中难以观察的“扩散控制自限制”微观机制，并为优化控轧控冷工艺参数、实现晶粒细化提供了一个强大的计算模拟工具。
"研究结论": >-
  成功建立了二维CA模型，模拟结果与实验金相照片吻合良好。研究证实γ→α相变是一个热-质扩散控制的过程，溶质富集和潜热释放会自限制地影响形核与生长。冷却速率是决定最终晶粒尺寸的关键因素，更高的冷却速率通过增加形核率和限制生长，能有效细化铁素体晶粒。
"对领域的贡献": >-
  创新性地将CA方法应用于固态相变模拟，实现了对热-质扩散、形核和生长耦合作用的动态可视化模拟。定量揭示了冷却速率对晶粒尺寸的影响机制，为材料加工工艺的“计算设计”奠定了基础。
"未来研究方向提及": >-
  文中提及耦合了变形、再结晶等过程的更复杂控轧控冷全流程模拟是未来方向。
"未来研究方向思考": >-
  1. 将模型从二维扩展到三维，以更真实地模拟晶粒空间形态。2. 放弃“超元素”简化，与CALPHAD等热力学/动力学数据库直接耦合，使模型适用于更广泛的合金成分。3. 引入晶界取向、能量等特征，细化形核模型，提高预测精度。4. 探索模型参数的物理意义和通用性，降低对特定实验数据的拟合依赖，增强模型的预测能力。
tags:
  - paper
  - type/method
  - year/2002
  - concept/cellular-automaton
  - concept/nucleation-and-growth
  - concept/diffusion-controlled-transformation
  - concept/undercooling
  - concept/grain-boundary-nucleation
  - concept/super-element-approximation
  - concept/latent-heat
  - concept/cementite-precipitation
  - concept/continuous-cooling-transformation
  - concept/grain-refinement
  - entity/low-carbon-steel
  - entity/ferrite
  - entity/austenite
  - entity/cementite
  - entity/fe-c-phase-diagram
  - method/cellular-automaton-method
  - method/explicit-finite-volume-method
  - method/diffusion-simulation
  - method/probabilistic-nucleation
  - method/microstructure-modeling
  - material/low-carbon-steel
  - material/ferrite
  - material/austenite
  - material/cementite
  - topic/phase-transformation
  - topic/microstructure-evolution
  - topic/computational-materials-science
  - topic/metallurgy
---

## Zhang2002b — 模拟低碳钢铁素体晶粒形核与长大的元胞自动机模型

- **元数据**：L. Zhang, C. C. Zhang, Y. Y. Wang, X. X. Liu, G. G. Wang，2002，Journal of Materials Research，17(9), 2251-2259，DOI [10.1557/JMR.2002.0331](https://doi.org/10.1557/JMR.2002.0331)
- **一句话**：建立了一个耦合溶质/温度扩散场的二维元胞自动机模型，定量复现了低碳钢连续冷却过程中γ→α相变的形核、生长及冷却速率对铁素体晶粒细化的影响，并揭示了扩散控制的自限制机制。
- **现有wiki双链**：本文涉及的元胞自动机、钢铁相变等主题在现有 wiki 中均无对应条目，仅链回原文与年度汇总：
  - 年度 [[../write/2002]]
  - 相关论文 [[../../raw/note/Zhang2002b]]
- **新概念/实体建议**：
  - `cellular-automaton`（元胞自动机）：一种时间、空间、状态均离散的动力学系统，通过局部邻居规则"涌现"出宏观组织，适合模拟晶粒形核/长大。
  - `diffusion-controlled-transformation`（扩散控制型相变）：新相生长速度由溶质/热扩散速率决定，溶质富集与潜热释放会反过来抑制后续形核。
  - `super-element-approximation`（超元素近似）：将 Fe 以外的多种合金元素（Si, Mn, Ni, Cu, Cr）合并为一个等效元素 S，把多组分合金降维为 S–C 伪二元系以套用 Fe–C 相图热力学。
  - `grain-boundary-nucleation`（晶界形核）：铁素体优先在奥氏体晶界（尤其是棱边、角隅）形核的非均匀形核假设。
  - `undercooling`（过冷度）：实际温度低于平衡相变温度 Ae3 的差值 ΔT=Ae3−T，是形核驱动力的来源。
  - `cementite-precipitation`（渗碳体析出）：铁素体生长前沿碳富集至渗碳体形成温度时析出 Fe3C，钉扎并阻止铁素体继续长大。
  - `low-carbon-steel`（低碳钢）：以 Fe–C–Si–Mn 为代表、碳含量约 0.15 wt% 的钢种，组织以铁素体为主。
  - `fe-c-phase-diagram`（铁碳相图）：模型确定 Ae3、cγ、cα 等热力学边界的依据。
- **关键图表**：
  - 图1 Fe–C 相图示意，标出 Ae3 温度线 ![Fe-C相图与Ae3温度](../../raw/figures/Zhang2002b/fig_1_DADI282V.png)
  - 图2 连续冷却曲线离散为等温阶梯的近似处理 ![连续冷却的等温离散化](../../raw/figures/Zhang2002b/fig_2_XUHQZPIE.png)
  - 图3 铁素体在奥氏体晶界形核并向晶内生长示意 ![晶界形核示意](../../raw/figures/Zhang2002b/fig_3_MKLDVB48.png)
  - 图4 六边形 CA 网格的中心元胞与六个最近邻 ![CA邻居定义](../../raw/figures/Zhang2002b/fig_4_GILHIVAN.png)
  - 图5 元胞的 γ / α / α-γ 界面三种状态 ![元胞三种状态](../../raw/figures/Zhang2002b/fig_5_9UZ6KLBG.png)
  - 图6 Q=1 K/s 下铁素体形核-生长-最终组织的演化快照（0.6×0.6 mm，200×200 元胞） ![组织演化模拟](../../raw/figures/Zhang2002b/fig_6_2JBIIL8Q.png)
  - 图7 不同冷速（0.05–5.0 K/s）下实验光学金相与模拟组织对比 ![实验与模拟对比](../../raw/figures/Zhang2002b/fig_7_XNUWJQCG.png)
  - 图8 平均铁素体晶粒尺寸随冷却速率增大而单调下降的定量曲线 ![冷速-晶粒尺寸曲线](../../raw/figures/Zhang2002b/fig_8_ATG5KEXH.png)
- **项目连接**：无直接项目连接。本文属于钢铁冶金领域的介观组织模拟（元胞自动机 + 扩散方程），与 project-1 双光子、project-2 Mn 多铁、project-3 机械发光 NN、project-4 TTF 分子计算、project-5 SnTe 铁电模拟、project-6 湿度传感器、project-7 CDW 在材料体系、物理机制和计算方法（非 DFT/MD/MLIP，而是概率性 CA）上均无可复用的机制或数据。project-5 虽涉及铁电材料的计算模拟，但其尺度（电子结构/DFT）与物理（极化翻转）和本文（介观相变动力学/碳扩散）差异过大，不构成有意义的方法学借鉴。
- **组织与用词**：论文采用"问题—数学模型—CA 算法—结果验证—结论"的经典结构。先以超元素近似把多组分钢降维为 S–C 二元系，给出形核驱动力（式 4–8）、形核率（式 3、13、15）、扩散控制生长速度（式 11）和显式有限体积扩散（式 16–21）；再定义六边形 CA 网格、三态元胞（α/γ/α-γ 界面）、概率性形核与捕获规则，以及由最快过程约束的时间步长（式 23）；最后用 Q=1 K/s 的动态快照和四组冷速（0.05、0.17、1.25、5.0 K/s）的实验/模拟对照完成验证。值得复用的术语：
  - cellular automaton（元胞自动机，CA）
  - γ→α phase transformation（奥氏体→铁素体相变）
  - undercooling ΔT（过冷度）
  - Ae3 temperature（Ae3 平衡相变温度）
  - super-element S（超元素 S）
  - diffusion-controlled growth（扩散控制生长）
  - nucleation probability / capture probability（形核概率 / 捕获概率）
  - latent heat release（潜热释放）
  - cementite pinning（渗碳体钉扎）
  - controlled rolling and cooling（控轧控冷，TMCP）
- **可写入wiki的要点**：
  1. 二维 CA 网格为六边形、200×200 元胞、对应 0.6×0.6 mm 试样，每个元胞处于 α、γ 或 α/γ 界面三态之一，并用 1–100 的整数标记结晶取向以区分不同晶粒。
  2. 多组分低碳钢 Fe–Xi–C（Xi=Si, Mn, Ni, Cu, Cr；成分为 C 0.15、Si 0.09、Mn 0.4、Cr 0.02、Ni 0.02、Cu 0.01 wt%）通过"超元素 S"近似为 S–C 伪二元合金，使 Fe–C 相图及 Ae3、cγ、cα 可直接使用。
  3. 超元素 S 的 γ→α 自由能变化 ΔGSγ→α = (1/4)Σ xi(TiM − TiNM) + ΔGFe(S)γ→α，其中 TiM、TiNM 为 Zener 参数，合金元素的贡献通过其摩尔分数线性叠加。
  4. 形核率 I(T) = K1(kT)^(−1/2) D exp[−K2/(RT·ΔGNγ→α+γ1)]，连续冷却下新晶核密度 n = ∫(I/Q)(1−f)d(ΔT)，单胞形核概率 pnuc = n·S，由随机数 rs ≤ pnuc 决定是否形核。
  5. 生长由碳在 α/γ 界面的扩散通量守恒控制：Dγ(∂cγ/∂n) − Dα(∂cα/∂n) = vn(cγ − cα)；铁素体向邻居界面元胞的捕获概率 pcap = l/LCA，其中 l 为一个时间步内的生长长度。
  6. 温度场与溶质场均用显式有限体积法在六边形邻域上扩散，更新式为 u(i,j) + (2Δt/3LCA²)Σ Du(u_nei − u_ij) → u_ij；跨相界面时扩散系数按界面元胞中 α/γ 相分数 f 加权（式 19–21）。
  7. 时间步长取 Δt = (1/5) min(LCA/vmax, LCA²/Du, LCA²/Dα, LCA²/Dγ)，即必须小于生长、热扩散、α 中溶质扩散、γ 中溶质扩散四个时间尺度中最快者的 1/5，以保证数值稳定和物理一致。
  8. 扩散控制的"自限制"机制：先形核的铁素体向邻近奥氏体排出碳并释放潜热，使邻区碳浓度升高（Ae3 下降）、温度升高，导致过冷度 ΔT 减小、后续形核概率下降，从而自然产生大小不均的晶粒分布。
  9. 冷速效应：高冷速下过冷度大、形核点被大量激活，且溶质来不及扩散、渗碳体在生长前沿析出钉扎界面，故得到细小晶粒；低冷速下形核少、扩散充分、晶粒充分长大。模拟初始奥氏体晶粒 126 μm，冷速 0.05→5.0 K/s 时实验铁素体晶粒 106→33 μm、模拟 108→38 μm，定量吻合。
  10. 模型局限：二维截面与三维晶粒尺寸的体视学换算未严格处理；扩散系数 Dγ、Dα 取常数而非 Arrhenius 温度依赖；超元素近似忽略了不同合金元素对碳活度和界面能的差异化影响；形核常数 K1、K2 等参数的可移植性有限，作者展望三维扩展、CALPHAD 耦合以及与轧制变形/再结晶模型的集成。
