---
tags: [concept, dft, methodology]
title: 密度泛函理论 / Density Functional Theory (DFT)
type: concept
status: mature
domain: [computational-chemistry, condensed-matter-physics]
mechanism: 基于 Hohenberg-Kohn 定理，将多电子体系的基态性质映射为电子密度的泛函，从而将 3N 维薛定谔方程简化为 3 维电子密度求解
related_concepts: [exchange-correlation-functional, paw-method, pseudopotential, brillouin-zone, self-consistent-field-cycle, minimum-energy-path, berry-phase, bader-analysis, lsda-plus-u, tight-binding]
papers: [blochlProjectorAugmentedwaveMethod1994b, perdewGeneralizedGradientApproximation1996a, kresseEfficientIterativeSchemes1996d, monkhorstSpecialPointsBrillouinzone1976, king-smithTheoryPolarizationCrystalline1993, dudarevElectronenergylossSpectraStructural1998a, henkelmanClimbingImageNudged2000c, tangGridbasedBaderAnalysis2009]
updated: 2026-08
---

# 密度泛函理论 / Density Functional Theory (DFT)

密度泛函理论（Density Functional Theory, DFT）把多电子基态问题改写为电子密度 $\rho(\mathbf r)$ 的变分问题。它的价值不在于“把所有电子都算得很精确”，而在于以可控的近似、周期性基组和自洽迭代，在可接受成本内同时得到总能、力、应力、磁矩和电荷密度等基态量；因此计算结论必须连同泛函、赝势、截断能、$k$ 点和收敛标准一起报告。

## 👵 太奶导读

太奶，您可以把材料想成一间挤满人的屋子：不必追踪每个人的每一步，只要知道屋子各处“人有多挤”（电子密度），就能估计整间屋子的安稳程度、骨架该往哪里挪以及哪里容易漏电。Hohenberg–Kohn 定理告诉我们，基态的秘密藏在这张“拥挤地图”里；Kohn–Sham 方程则找来一群互不碰撞的“替身电子”来计算，真正难算的交换与关联（电子彼此躲避和协同的量子效应）集中塞进交换-关联泛函这个近似盒子。计算机先猜一张密度图，再反复算电子、更新密度，直到前后几乎不变；最后还要检查盒子选得是否合适，不能把一个近似答案误当成实验真理。

## 🧩 从电子密度到 Kohn–Sham 方程

Hohenberg–Kohn 第一、第二定理给出两个判据：基态外势（因而基态所有可观测量）由 $\rho(\mathbf r)$ 唯一决定；正确密度使能量泛函 $E[\rho]$ 取得允许密度中的最低值。实际计算通常将能量写成

$$
E[\rho]=T_s[\rho]+\int v_{\mathrm{ext}}(\mathbf r)\rho(\mathbf r)\,d\mathbf r+E_H[\rho]+E_{xc}[\rho]+E_{II},
$$

其中 $T_s$ 是非相互作用 Kohn–Sham 电子的动能，$E_H$ 是经典 Hartree 静电能，$E_{xc}$ 汇总交换、关联以及与 $T_s$ 的差异，$E_{II}$ 是离子-离子能。对轨道作变分后得到

$$
\left[-\frac{\nabla^2}{2}+v_{\mathrm{eff}}[\rho](\mathbf r)\right]\psi_i=\epsilon_i\psi_i,
\qquad \rho(\mathbf r)=\sum_i f_i|\psi_i(\mathbf r)|^2.
$$

这里的轨道能级 $\epsilon_i$ 是求解辅助方程的量，不应未经检验地等同于实验激发能；带隙、光谱和强关联基态往往需要混合泛函、$+U$ 或 GW 等超越半局域 DFT 的方法。

## ⚙️ 一次可复现的计算流程

1. **定义问题与模型**：确定晶体相、磁序、缺陷/表面超胞、真空层、应变和边界条件。结构不确定时，先比较多个候选相的相对能量，而不是只优化一个猜测结构。
2. **选择离子-电子表示**：平面波计算常用赝势或投影增强波（PAW）。PAW 在增强区域内以全电子分波重构核附近波函数，在区域外保持平滑赝波函数；[[../papers/blochlProjectorAugmentedwaveMethod1994b|Blöchl 的 PAW 工作]]说明它在全电子精度与平面波效率之间作了可检验的折中。
3. **设置基组与布里渊区采样**：提高波函数截断能 $E_\mathrm{cut}$，并逐步加密 Monkhorst–Pack $k$ 点网格，分别观察总能、能量差、力、应力和目标观测量是否收敛。[[../papers/monkhorstSpecialPointsBrillouinzone1976|Monkhorst–Pack 网格]]是布里渊区积分的离散近似，不是“越密越正确”的替代品；金属费米面附近通常需要比绝缘体更谨慎的采样与占据展宽。
4. **求解自洽场（SCF）**：从初始密度得到有效势，迭代求解 Kohn–Sham 方程，混合输入/输出密度，直到能量和密度残差达到阈值。对金属和开壳层体系，电荷晃动、近简并和磁矩初值会主导收敛行为。
5. **弛豫晶格与离子**：在电子自洽足够严格后再更新离子；结构优化的停止条件应同时限制最大力、应力和能量变化。若比较相稳定性，所有候选相应使用同一套数值设置。
6. **沿路径或做动力学**：极化翻转、扩散和相变可用 NEB/CI-NEB 在 DFT 势能面上寻找最小能量路径；[[../papers/henkelmanClimbingImageNudged2000c|Henkelman 等人的 CI-NEB]]表明，把最高能图像沿路径方向“爬升”到鞍点，比在稀疏图像之间插值更可靠。
7. **后处理与交叉验证**：从收敛密度计算态密度、能带、Berry 相极化、Bader 电荷、介电响应或声子。后处理不能修复错误的模型、泛函或未收敛的密度；应记录输入文件、版本、赝势来源和收敛测试。

![图：PAW 的全电子分波、赝分波与投影函数](../../raw/figures/blochlProjectorAugmentedwaveMethod1994b/fig_1_MBXMFE5N.png)
*   **关键特征**：左列显示 Mn 的全电子分波与平滑赝分波在核附近的差异，右列为局域投影函数；增强区域外两类分波匹配，核附近的修正由投影函数完成。这正是平面波 DFT 既能保持可计算性、又能恢复核区信息的机制。
*   **来源**：[[../papers/blochlProjectorAugmentedwaveMethod1994b]] -> [[../figures/mathematical-models-computational|计算方法与泛函]]

## 🧪 交换-关联近似与选择判据

交换-关联泛函是 DFT 最主要的模型误差来源。LDA/LSDA 只看局域密度或自旋密度；GGA 再加入密度梯度；meta-GGA 还使用动能密度等局域信息；杂化泛函混入部分 Hartree–Fock 精确交换；色散修正或非局域泛函用于补足范德华作用。[[../papers/perdewGeneralizedGradientApproximation1996a|PBE 论文]]从均匀电子气线性响应、均匀缩放和 Lieb–Oxford 界等物理约束构造无经验参数的 GGA；其小分子原子化能测试中 PBE 平均绝对误差为 7.9 kcal/mol，而 LSD 为 31.4 kcal/mol，但这不是所有材料性质的通用误差条。

对过渡金属氧化物或具有明显局域 $d/f$ 电子的体系，半局域泛函可能过度离域化、低估带隙或错误排序磁态。[[../papers/dudarevElectronenergylossSpectraStructural1998a|Dudarev 等人的 NiO 研究]]用旋转不变 LSDA+$U$ 修正局域轨道占据：在该文的 FP-LMTO 条件下，$\bar U=6.2$ eV、$\bar J=0.95$ eV 同时改善了氧 K 边谱和结构参数。这个数值是 NiO 的校准结果，不应直接移植给别的元素或晶相；$U$ 应通过线性响应、约束 DFT 或与实验/高阶计算交叉校准。

选择泛函时应先问“要解释什么”：结构和相对能量可从 PBE 起步；弱相互作用需色散处理；局域轨道磁性需考虑自旋、$+U$ 或杂化泛函；光学激发和准粒子带隙则不能只凭普通 PBE 能带下结论。不同近似给出不同的势能面，因而 NEB 势垒、软模和极化路径也会随泛函改变。

## 🔁 自洽收敛、数值尺度与误差来源

[[../papers/kresseEfficientIterativeSchemes1996d|Kresse–Furthmüller 的迭代方案]]把 Kohn–Sham 求解拆成波函数迭代和电荷密度混合两部分：RMM-DIIS 处理本征态残差，Pulay 混合与 Kerker 预条件抑制金属长波电荷晃动。其 fcc-Fe 测试中，RMM-DIIS 的能量约在 20 次迭代内收敛，而直接最小化方案随超胞放大显著恶化；这说明“SCF 收敛”不仅是把能量打印到很多位小数，还要检查力和磁矩是否同步稳定。

![图：fcc-Fe 不同超胞的自洽能量与力收敛](../../raw/figures/kresseEfficientIterativeSchemes1996d/fig_5_MDMEZAFI.png)
*   **关键特征**：上图中 RMM-DIIS（实线）对 1、2、4、8 个超胞的能量下降仍较快，迭代数只缓慢增加；下图力的收敛更敏感，直接最小化 CGa（虚线）在大超胞中明显变差。结构优化应以力/应力而非单独总能为停止判据。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]] -> [[../figures/mathematical-models-computational|计算方法与泛函]]

需要把误差拆成四层：

- **离散误差**：平面波截断、$k$ 点、FFT 网格、空带数和展宽；应以目标量的变化量做收敛测试，而不是只测总能。
- **表示误差**：赝势/PAW 的价电子选择、冻结芯近似、增强半径和自旋轨道耦合处理；不同势文件不能在同一能量差中混用。
- **泛函误差**：LDA/GGA 的自相互作用、带隙低估、过度结合和缺失色散；$+U$、杂化、GW 只是针对特定缺陷的修正，不是统一的“精度开关”。
- **模型与观测量误差**：超胞尺寸、有限厚度、真空层、缺陷浓度、磁序和温度近似，以及把 Kohn–Sham 本征值直接解释成激发能。应报告边界条件和替代模型的敏感性。

![图：CI-NEB 对 CH₄/Ir(111) 最小能量路径的鞍点解析](../../raw/figures/henkelmanClimbingImageNudged2000c/fig_1_KRQQQH5S.png)
*   **关键特征**：常规 NEB 的图像在窄能垒顶部分辨率不足，插值峰值偏低；CI-NEB 将最高能图像推到约 0.4 eV 的鞍点。该结果还显示，端点直线并不等于真实反应路径，能垒应在充分收敛的 DFT 势能面上比较。
*   **来源**：[[../papers/henkelmanClimbingImageNudged2000c]] -> [[../figures/mathematical-models-simulations|模拟与数值结果]]

## 📏 DFT 能直接回答什么，不能回答什么

DFT 最稳妥地回答基态相对能量、平衡结构、原子力、应力、磁矩和自洽电荷密度等问题；对同一计算协议下的能量差，系统误差常有抵消，但不能因此省略收敛测试。晶体极化变化可用现代极化理论的 Berry 相表达，但前提是沿绝热路径保持绝缘、保持周期性且宏观电场为零；[[../papers/king-smithTheoryPolarizationCrystalline1993|King-Smith–Vanderbilt]]的 GaAs 计算表明，Berry 相方法可在普通 DFT 框架内得到与线性响应和实验相符的压电响应。

电荷密度是可解释的中间产物，却不是唯一的“原子电荷”定义。[[../papers/tangGridbasedBaderAnalysis2009|Tang 等人的网格 Bader 算法]]通过修正向量追踪连续梯度，避免在网法的晶格偏差；因此 Bader 电荷必须注明网格、赝势冻芯电荷是否回加和分区算法。对于金属、强激发、有限温度和长程动力学，普通基态 DFT 的适用范围更窄，应转向含时 DFT、GW、DMFT、AIMD 或实验校准，而不是把静态密度结果外推到所有观测量。

## 📚 相关论文 (Related Papers)

- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：提出 PAW 线性变换，在增强区域重构全电子波函数，给出平面波截断与过渡金属分波数的收敛依据。
- [[../papers/perdewGeneralizedGradientApproximation1996a]]：提出 PBE GGA，以物理约束而非经验拟合构造交换-关联泛函，并量化其相对 LSD/PW91 的分子能量表现。
- [[../papers/kresseEfficientIterativeSchemes1996d]]：建立 RMM-DIIS、Pulay 混合和 Kerker 预条件的高效 SCF 方案，解释大体系尤其是金属计算为何能够收敛。
- [[../papers/monkhorstSpecialPointsBrillouinzone1976]]：给出 Monkhorst–Pack 特殊点的数学构造，为周期性 DFT 的布里渊区积分和 $k$ 点收敛测试提供基础。
- [[../papers/king-smithTheoryPolarizationCrystalline1993]]：用价带 Berry 相定义绝热极化变化，明确了 DFT 后处理极化、Born 有效电荷和压电响应的适用前提。
- [[../papers/dudarevElectronenergylossSpectraStructural1998a]]：展示 LSDA+$U$ 如何修正 NiO 的局域 $d$ 电子，并提醒 $U$ 是体系和校准条件相关的参数而非普适常数。
- [[../papers/henkelmanClimbingImageNudged2000c]]：把 DFT 势能面上的最高能 NEB 图像爬升到鞍点，使反应/翻转势垒不依赖稀疏路径插值。
- [[../papers/tangGridbasedBaderAnalysis2009]]：将自洽电荷密度转为无晶格偏差的 Bader 分区，说明后处理算法本身也会引入可测的数值误差。

## 📋 关键参数表

下表只列仓库论文中明确给出、且带有计算条件的数值；它们是复现相应算例的参考，不是 DFT 的默认设置。

| 参数或结果 | 数值 | 条件与来源 | 使用时的判据 |
| :--- | :--- | :--- | :--- |
| PAW 平面波截断 | 约 30 Ry | Blöchl 论文的原子/二聚体测试 | 该文测试元素在 30–40 Ry 时总能误差小于 0.1 eV；实际体系仍需自行收敛 |
| PBE 小分子原子化能 MAE | 7.9 kcal/mol | 20 个小分子、实验几何；PBE 论文 Table I | 只说明该测试集的能量表现，不代表固体带隙或色散误差 |
| RMM-DIIS SCF 规模趋势 | fcc-Fe 约 20 次迭代内收敛 | 不同超胞、PBE/平面波方案的算法测试 | 还需检查力、磁矩和密度残差；不是所有金属的固定迭代上限 |
| GaAs 晶格常数 | 5.576 Å | LDA、20 Ry、$(4,4,4)$ Monkhorst–Pack 网格 | 现代极化理论算例的理论晶格，不是实验晶格常数 |
| GaAs 玻恩有效电荷 | $Z^*_{\mathrm{Ga}}=1.984\,e$ | 同上；Berry 相结果，线性响应为 1.994 | 适用于该晶格和线性位移，不可直接移植到其他材料 |
| GaAs 压电常数 | $\gamma_{14}=-0.28$ C/m² | 同上；实验值 −0.32 C/m² | 电子项与内部应变项有强抵消，需较严的收敛设置 |
| NiO LSDA+$U$ 参数 | $\bar U=6.2$ eV，$\bar J=0.95$ eV | FP-LMTO、反铁磁 NiO；同时拟合 EELS 与结构 | 是 NiO 的校准参数，不作为其他过渡金属氧化物的默认 $U$ |
| NiO LSDA+$U$ 晶格常数 / 带隙 | 4.19 Å / 3.0 eV | 上述 LSDA+$U$ 条件；实验晶格约 4.17 Å、带隙约 4.2 eV | 仍是基态近似，带隙未完全达到实验值 |
| NaCl Bader Na 价电荷 | 0.828 e | VASP、PW91、PAW/Vanderbilt、262.5 eV、$3\times3\times3$ $k$ 点、晶格常数 5.86 Å | 近网法随网格加密收敛；须注明是否加入冻结芯电荷 |
| CH₄/Ir(111) CI-NEB 活化能 | 约 0.4 eV | DFT/PW91，8 个可动图像；实验约 0.28 eV | 仍需零点能、色散和有限尺寸修正，不能当作普适势垒 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/exchange-correlation-functional|交换-关联泛函]]（决定主要模型误差）
- [[../concepts/paw-method|PAW 方法]]（平面波 DFT 的全电子重构表示）
- [[../concepts/pseudopotential|赝势]]（离子-电子相互作用的有效表示）
- [[../concepts/brillouin-zone|布里渊区]]与 [[../concepts/monkhorst-pack-grid|Monkhorst–Pack 网格]]（周期性积分采样）
- [[../concepts/self-consistent-field-cycle|自洽场循环]]（密度与有效势的固定点迭代）
- [[../concepts/minimum-energy-path|最小能量路径]]（势垒/相变路径后处理）
- [[../concepts/berry-phase|Berry 相位]]（极化变化的几何相表达）
- [[../concepts/bader-analysis|Bader 分析]]（电荷密度拓扑后处理）
- [[../concepts/lsda-plus-u|LSDA+U]]（局域强关联修正）
- [[../entities/VASP|VASP]]、[[../entities/WIEN2k|WIEN2k]]（DFT 实现载体）
