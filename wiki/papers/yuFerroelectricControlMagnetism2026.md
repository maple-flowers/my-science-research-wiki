---
citekey: yuFerroelectricControlMagnetism2026
title: "Ferroelectric Control of Magnetism and Giant Magnetoresistance Via Intercalation-Induced Symmetry Breaking in Two-Dimensional Multiferroics with Strong Magnetoelectric Coupling"
title_zh: "强磁电耦合二维多铁性材料中嵌入诱导对称破缺对磁性和巨磁电阻的铁电控制"
authors: [Cuiju Yu, Liangliang Hong, Zhao Chen, Zhao Liu, Shizhe Jiao, Xiaofeng Liu, Wei Hu]
year: 2026
journal: "The Journal of Physical Chemistry Letters"
doi: "10.1021/acs.jpclett.6c00390"
url: "https://doi.org/10.1021/acs.jpclett.6c00390"
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/yuFerroelectricControlMagnetism2026]]
projects: [project-2]
concepts: [2D-materials, altermagnetism, berry-phase, density-functional-theory, giant-spin-splitting, magnetoelectric-coupling, multiferroicity, polarization-switching, spin-orbit-coupling, strain-engineering]
entities: [BiFeO3, CrTe2, Fe3GeTe2, HoMnO3, In2Se3, MXenes, TMDs, VASP, WTe2, Wannier90, domain-wall, h-BN]
methods: [afm-pfm, berry-phase, dft, md, mlip, monte-carlo, neb, stm-mbe]
materials: [BiFeO3, CrTe2, Fe3GeTe2, HoMnO3, In2Se3, MXenes, TMDs, WTe2, domain-wall, h-BN]
figures: [crystal-structures, electronic-bands, electronic-devices, heterostructures-stacking, mathematical-models]
领域基础知识:: >-
  二维多铁材料（2D Multiferroics）与磁电耦合（Magnetoelectric Coupling）是自旋电子学（Spintronics）的前沿领域。核心目标是在单一材料中耦合铁电性（Ferroelectricity, FE，可被电场翻转的自发电极化）和磁性（Magnetism，自发的磁有序），以实现电场控制磁矩，开发低功耗器件。传统多铁体的主要瓶颈在于磁性和铁电性起源独立，耦合微弱，限制了其应用。
研究背景:: >-
  已发现的二维多铁材料主要分为三类：I型（磁性与铁电性起源独立，耦合弱），II型（磁性驱动铁电性，但极化弱），III型（铁电性驱动磁性，稀少且难以设计）。因此，寻找一种能实现强磁电耦合的通用设计策略和室温二维多铁材料体系是该领域的关键挑战。
作者的问题意识:: >-
  作者旨在解决二维多铁材料中磁电耦合弱的根本性难题。他们提出并验证了一个核心问题：能否通过一种通用的材料设计策略（如插层），在范德华反铁磁体中人为引入并强关联铁电性和磁性，从而实现室温下电场对磁矩的完全控制，并展示其在器件中的应用潜力？
主要研究对象:: >-
  单层Cr₄S₄FBr₂ (CSFB)，一种由双层CrSBr通过“融合”和氟离子（F⁻）桥联设计而成的二维A型完全补偿亚铁磁金属（A-type fully compensated ferrimagnetic metal）。此外，还研究了其衍生物Cr₄S₄X₃和Mn₄N₄X₃系列以验证策略的通用性。
主要研究方法:: >-
  基于第一性原理的多尺度理论计算。主要包括：密度泛函理论（DFT，如PBE+U, HSE06）计算电子结构与磁性；CI-NEB方法计算铁电翻转势垒与路径；构建有效哈密顿量模型，结合蒙特卡洛和分子动力学（MD）模拟估算Néel温度（TN）和铁电居里温度（TC）；非平衡格林函数（NEGF）方法模拟多铁隧道结（MFTJ）的量子输运特性。
研究意义:: >-
  1. 提出了一种全新的“插层诱导对称性破缺”范式，为设计III型多铁体和实现强磁电耦合提供了清晰的理论框架。2. 成功预测了单层Cr₄S₄FBr₂这一兼具室温磁电耦合、高转变温度、巨磁阻效应的具体材料体系，为实验探索提供了明确目标。3. 演示了电场驱动的、非易失性巨磁阻效应，为开发超低功耗自旋电子学器件指明了新方向。
研究结论:: >-
  单层Cr₄S₄FBr₂是一种高Néel温度（469 K）和铁电居里温度（334 K）的A型完全补偿亚铁磁金属。其垂直铁电极化（1.1 pC/m）源于F原子位移，翻转势垒低（0.11 eV）。该材料展现出强磁电耦合，翻转铁电极化可完全反转自旋极化、自旋纹理和Chern数（从-2到+2）。基于该材料的多铁隧道结可实现由纯电场驱动的、高达4.8 × 10³%的巨磁阻。
对领域的贡献:: >-
  1. **理论贡献**：为设计强磁电耦合多铁材料提供了“插层破缺对称性”的新范式，并揭示了A型亚铁磁中实现铁电-自旋-拓扑锁定的微观机制。2. **材料贡献**：预测了Cr₄S₄FBr₂及其衍生物等一系列高性能室温二维多铁材料，丰富了多铁材料库。3. **器件贡献**：展示了电场控制巨磁阻的新概念器件，证明了其在非易失性、低功耗信息存储和处理中的巨大潜力。
未来研究方向提及:: >-
  1. 实验合成与验证：通过文中提出的卤素离子交换插层或堆垛工程等方法，实际制备单层CSFB及器件，并验证其多铁性与磁电耦合性能。2. 拓展材料家族：将插层策略系统性地应用于与CrSBr同构的、更广泛的二维磁体家族（如MnNX等），探索其多铁潜力。
未来研究方向思考:: >-
  1. **缺陷与界面工程**：研究缺陷对CSFB中铁电畴翻转动力学和矫顽场的影响，以及在实际金属电极/CSFB界面的磁电耦合效应。2. **多场调控与拓扑物理**：探索应变、光场、静电掺杂等手段对CSFB磁电耦合和拓扑Chern数的调控，或通过掺杂打开全局带隙，实现量子反常霍尔效应或拓扑超导。3. **自旋动力学**：研究电场是否可激发或调控CSFB中的自旋波（磁振子），探索基于磁振子的逻辑器件。4. **机制深化**：澄清其“完全补偿亚铁磁体”与“交变磁体”之间的概念关联，并深入分析在金属性背景下，自由电子对铁电偶极子场的屏蔽效应及其对器件性能的影响。
tags:
  - paper
  - type/experiment
  - year/2026
  - project/project-2
  - relevance/project-2/medium
  - concept/2D-materials
  - concept/altermagnetism
  - concept/berry-phase
  - concept/density-functional-theory
  - concept/giant-spin-splitting
  - concept/magnetoelectric-coupling
  - concept/multiferroicity
  - concept/polarization-switching
  - concept/spin-orbit-coupling
  - concept/strain-engineering
  - entity/BiFeO3
  - entity/CrTe2
  - entity/Fe3GeTe2
  - entity/HoMnO3
  - entity/In2Se3
  - entity/MXenes
  - entity/TMDs
  - entity/VASP
  - entity/WTe2
  - entity/Wannier90
  - entity/domain-wall
  - entity/h-BN
  - method/afm-pfm
  - method/berry-phase
  - method/dft
  - method/md
  - method/mlip
  - method/monte-carlo
  - method/neb
  - method/stm-mbe
  - material/BiFeO3
  - material/CrTe2
  - material/Fe3GeTe2
  - material/HoMnO3
  - material/In2Se3
  - material/MXenes
  - material/TMDs
  - material/WTe2
  - material/domain-wall
  - material/h-BN
  - topic/2d-materials
  - topic/charge-density-wave
  - topic/ferroelectricity
  - topic/ferromagnetism
  - topic/humidity-sensing
  - topic/mof
  - topic/molecular-crystal
  - topic/multiferroics
  - topic/mxene
  - topic/phase-transition
  - topic/polarization
  - topic/two-photon-fluorescence
---

## yuFerroelectricControlMagnetism2026 — 强磁电耦合二维多铁性材料中嵌入诱导对称破缺对磁性和巨磁电阻的铁电控制

## 📄 元数据
Cuiju Yu, Liangliang Hong, Zhao Chen, Zhao Liu, Shizhe Jiao, Xiaofeng Liu*, Wei Hu et al.，2026，The Journal of Physical Chemistry Letters 17(12), 3539–3548，DOI: 10.1021/acs.jpclett.6c00390

## 💡 一句话
通过卤素离子（F）插层把双层 CrSBr “融合”为单层 Cr₄S₄FBr₂，利用 F 原子位移诱导的 Jahn–Teller 畸变打破反演对称，在 A 型完全补偿亚铁磁金属中实现铁电–自旋–拓扑三者锁定，并在 CSFB/CrSBr/CSFB 多铁隧道结中由纯电极化翻转驱动高达 4.8×10³% 的巨磁阻。

## 🔗 Wiki 双链
  - 概念 [[../concepts/multiferroicity]]、[[../concepts/magnetoelectric-coupling]]、[[../concepts/2D-materials]]、[[../concepts/spin-orbit-coupling]]、[[../concepts/berry-phase]]、[[../concepts/altermagnetism]]、[[../concepts/giant-spin-splitting]]、[[../concepts/polarization-switching]]、[[../concepts/density-functional-theory]]、[[../concepts/strain-engineering]]、[[../concepts/intercalation-induced-symmetry-breaking]]、[[../concepts/geometric-ferroelectricity]]、[[../concepts/multiferroic-tunneling-junction]]、[[../concepts/fully-compensated-ferrimagnet]]、[[../concepts/gap-chern-number]]、[[../concepts/goodenough-kanamori-anderson-rules]]、[[../concepts/double-exchange]]、[[../concepts/cr4s4fbr2]]
  - 实体 [[../entities/VASP]]、[[../entities/Wannier90]]、[[../entities/In2Se3]]、[[../entities/WTe2]]、[[../entities/Fe3GeTe2]]、[[../entities/TMDs]]、[[../entities/h-BN]]、[[../entities/BiFeO3]]、[[../entities/HoMnO3]]、[[../entities/MXenes]]、[[../entities/CrTe2]]、[[../entities/domain-wall]]、[[../entities/crsbr]]
  - 图表 [[../figures/crystal-structures]]、[[../figures/electronic-bands]]、[[../figures/heterostructures-stacking]]、[[../figures/heterostructures-stacking-multiferroic|多铁与磁电异质结]]、[[../figures/electronic-devices]]、[[../figures/mathematical-models]]
  - 年度 [[../write/2026]]
  - 主题 [[../topics/D02-多铁性材料]]、[[../topics/Z01-材料模拟计算设计]]
  - 相关论文 [[../../raw/note/yuFerroelectricControlMagnetism2026]]

## 📊 关键图表
  - ![图1 插层破缺对称的概念示意与单层 Cr4S4FBr2 原子结构（Pmm2, a=3.51 Å, b=4.85 Å），标注极化轴和 J1–J4 交换路径](../../raw/figures/yuFerroelectricControlMagnetism2026/fig_1_4AF7AZPM.png) → [[../figures/heterostructures-stacking-multiferroic|多铁与磁电异质结]]
  - ![图2 P↑/P↓ 自旋分辨能带与 DOS（S 点非相对论自旋劈裂 1.33 eV，EF+0.05 eV 处极化 +91%/−91%）、F 周围静电势、NEB 翻转路径（Ea=0.11 eV/f.u.）、FE–PE 相变（TC=334 K）、线性磁电响应 αS=7.1×10⁻¹⁴ G·cm²/V](../../raw/figures/yuFerroelectricControlMagnetism2026/fig_2_5KVKTVLU.png) → [[../figures/heterostructures-stacking-multiferroic|多铁与磁电异质结]]
  - ![图3 含 SOC 能带（c 轴磁化在 X/Y 点开 3、11 meV 隙）、P↑/P↓ 贝里曲率（C=−2 与 +2）及第 93 带面外自旋纹理的完全反转](../../raw/figures/yuFerroelectricControlMagnetism2026/fig_3_Q88I2C3V.png) → [[../figures/heterostructures-stacking-multiferroic|多铁与磁电异质结]]
  - ![图4 CSFB/CrSBr/CSFB 多铁隧道结 PC/APC 构型、偏压依赖 I–V 与 MR（0.04 V 时 MR=4.8×10³%，IPC=13.8 nA、IAPC=0.27 nA）及自旋分辨透射谱](../../raw/figures/yuFerroelectricControlMagnetism2026/fig_4_FXA8A5X6.png) -> [[../figures/crystal-structures|晶体结构与原子排布]]
  - ![表1 Cr4S4FBr2 家族（Cr4S4F3、Cr4S4Cl3/Br3、Cr4Se4Cl3/Br3）与 BL CrSBr、NiI2、In2Se3、BL 1T′-WTe2 等标杆材料的 J、TN/TC、MAE、D、Ea/EC、αS 与分类（A-FiMM / FMHM 等）汇总](../../raw/figures/yuFerroelectricControlMagnetism2026/tab_1_IX3ZWAJ8.png) -> [[../figures/heterostructures-stacking-reviews|层间滑移铁电：综述与材料体系]]

## 🔬 项目连接
project-2 Mn多铁——主体材料虽为 Cr 基，但作者明确将插层策略推广到 MnNX 同构家族，预测 Mn₄N₄X₃（X=F, Cl, Br, I）为动力学稳定、铁磁、自发极化的半金属型 I 类多铁体，与 Mn 基多铁项目直接相关；其余项目（双光子、机械发光 NN、TTF 分子计算、SnTe 铁电模拟、湿度传感器、CDW）无直接连接。

## 🔗 项目双链
- 项目 [[../projects/project-2-mn-multiferroics|项目二：Mn极化结构铁电材料]]

## 📝 组织与用词
全文按 “提出问题（I/II/III 型多铁的瓶颈）→ 设计策略（非金属离子插层诱导 Jahn–Teller 畸变）→ 材料验证（CSFB 的磁、电、拓扑物性）→ 器件演示（MFTJ 巨磁阻）→ 推广（Cr₄X₄Y₃ 与 Mn₄N₄X₃ 家族）” 五步推进，方法链为 DFT（PBE+U, U=1 eV；HSE06 校验）→ CI-NEB → 有效哈密顿量 + MD/蒙特卡洛 → NEGF 输运，形成原子尺度到器件尺度的多尺度闭环。值得在 wiki 叙述中复用的术语：
  - 插层诱导对称性破缺 / intercalation-induced symmetry breaking
  - A 型完全补偿亚铁磁金属 / A-type fully compensated ferrimagnetic metal (A-FiMM)
  - 自旋–铁电锁定 / spin–ferroelectricity locking
  - 几何铁电性 [[../concepts/geometric-ferroelectricity|几何铁电性]] / geometric ferroelectricity（姜–泰勒畸变 Jahn–Teller distortion）
  - 非相对论自旋劈裂 / nonrelativistic spin splitting
  - 能隙陈数 / gap Chern number
  - 线性磁电系数 / linear magnetoelectric coefficient αS（μ₀ΔM=αS·E）
  - 多铁隧道结 [[../concepts/multiferroic-tunnel-junction|多铁隧道结]] / multiferroic tunneling junction (MFTJ)

## ✏️ 可写入 Wiki 的要点
  1. 设计范式：在 A 型反铁磁范德华材料的层间插入非金属卤素离子，利用其三角配位的上下不对称打破空间反演对称，同时保留层间 AFM 序，从而在单一物相中集成[[../concepts/ferroelectricity|铁电性]]与磁性并实现本征强[[../concepts/magnetoelectric-coupling|磁电耦合]]（III 型多铁思路）。
  2. 目标材料单层 Cr₄S₄FBr₂ 由双层 CrSBr “融合” 而来——中心 F 配体替换两个 Br，分别与上层 1 个 Cr、下层 2 个 Cr 成键，形成 Pmm2 (C₂ᵥ) 对称（a=3.51 Å, b=4.85 Å, c=20 Å）；上下两个连接 F 的 Cr 分别处于八面体和三角双锥晶体场，导致局域磁矩不对称，构成 A 型完[[../concepts/fully-compensated-ferrimagnet|全补偿亚铁磁体]]，净磁矩仅 0.20 μB/cell。
  3. 电子结构：金属性，S 点非相对论自旋劈裂达 1.33 eV，与 KV₂Se₂O（1.6 eV）、α-MnTe（1.1 eV）、RuO₂（1.4 eV）等交变磁体相当；劈裂来源于 Cr 位点在位交换场 ΔE≈⟨ψ|ΔVxc|ψ⟩，主要由 Cr d(x²−y²) 轨道贡献，而非净磁矩大小；EF+0.05 eV 处 P↑/P↓ 自旋极化分别达 +91%/−91%。
  4. 铁电性：F 原子从下 Cr–Cr 桥位迁移到上桥位带动[[../concepts/polarization-switching|极化翻转]]，面外极化 1.11 pC/m，NEB [[../concepts/switching-barrier|翻转势垒]]仅 0.11 eV/f.u.；[[../concepts/effective-hamiltonian|有效哈密顿量]] + MD 给出 EC≈73 mV/Å，按哈密顿/DFT 势垒比 1.8 校正后 EC≈43 mV/Å，与 In₂Se₃（100 mV/Å）、CuInP₂S₆（14 mV/Å）、HfO₂（159 mV/Å）相当；MD 给出 FE–PE 相变 570 K，DFT 校正后 TC=334 K。
  5. 磁性与温度：提取 J1/J1′=−19.39/−5.73、J2/J2′=−4.07/−6.70、J3=0.34、J4/J4′=−5.01/−20.31 meV；约 90° Cr–X–Cr 键给 FM [[../concepts/superexchange|超交换]]、约 180° 键给 AFM 超交换（Goodenough–Kanamori–Anderson 规则），而 180° 的 J4 为 FM 则归因于金属性导致的[[../concepts/double-exchange|双交换]]；易轴沿 b 轴，MAE=86 μeV/Cr；蒙特卡洛比热曲线显示两步磁相变（底层先失序、顶层后失序），全局 TN=469 K，MA 仅使 TN 偏移 2–10 K。
  6. 强磁电耦合：翻转铁电极化可整体反转自旋极化方向、面外[[../concepts/spin-texture|自旋纹理]]，并使贝里曲率在第一[[../concepts/brillouin-zone|布里渊区]]反号；磁矩沿 c 轴时 SOC 在 X、Y 点开 3、11 meV 隙，P↑ 与 P↓ 的“能隙陈数”分别为 C=−2 与 +2——这是电场驱动的陈数翻转；体系仍为金属、无全局带隙，故不期望受拓扑保护的无耗散边缘输运，但可对应力/掺杂打开全局隙后实现量子反常霍尔态构成提示。线性磁电系数 αS=7.1×10⁻¹⁴ G·cm²/V，超过 Fe 薄膜（2.9×10⁻¹⁴），接近双层 VS₂（9.8×10⁻¹⁴）。
  7. 器件：CSFB/CrSBr/CSFB [[../concepts/multiferroic-tunnel-junction|多铁隧道结]]，金属性 CSFB 作[[../concepts/spin-injection|自旋注入]]端、绝缘 CrSBr 作势垒；仅靠翻转两端 CSFB 电极化即在 PC（M↑(P↑)/M↑/M↑(P↓)）与 APC（M↓(P↓)/M↑/M↓(P↑)）间切换。0.04 V 偏压下 IPC=13.8 nA、IAPC=0.27 nA，MR=(GPC−GAPC)/GAPC×100% 峰值 4.8×10³%；PC 自旋流极化 +97%、APC 为 −60%；透射系数相差近两个数量级。另一反平行构型 APC2 (M↑/M↑/M↓) 在 0.02 V 给出 MR=4.4×10³%。偏压升高到 0.10 V 时 MR 降至 ~10²%。
  8. 稳定性与合成路径：声子谱无虚频、1000 K 下 AIMD 无结构重构、[[../concepts/formation-energy|形成能]] −1.391 eV/atom、力学稳定；借鉴 μ₃-F 桥连金属有机框架与杂化层状氟化物钙钛矿，提出两条可行合成路线——氧化还原介导的卤素离子交换插层、堆垛工程；并讨论了插层结合能、中间体热稳定性与器件制备方案。
  9. 策略通用性：Cr₄S₄F₃ 保持 A-FiMM，αS=11.8×10⁻¹⁴ G·cm²/V、非相对论自旋劈裂 1.55 eV；Cr₄S₄Cl₃、Cr₄S₄Br₃、Cr₄Se₄Cl₃、Cr₄Se₄Br₃ 转为铁磁[[../concepts/half-metal|半金属]]（FMHM，费米能级 100% 自旋极化），TN/TC 多在室温以上；Mn₄N₄X₃（X=F, Cl, Br, I）单层均动力学稳定、铁磁且有自发极化，为[[../concepts/inversion-symmetry-breaking|反演对称破缺]]驱动的 I 类多铁半金属，说明该插层范式可推广至整个 CrSBr 同构二维磁体家族。
  10. 批判要点（可写入 wiki 的“争议/局限”视角）：全部结论基于 DFT/模型哈密顿量，TC、TN、EC 依赖有效哈密顿量参数（模型高估势垒约 1.8 倍）；金属中自由载流子对几何铁电偶极场的屏蔽程度未定量；APC 电流不为零且极化率仅 −60%（PC 为 +97%），不对称性可能来自势垒/界面态；MFTJ 为理想范德华接触、完美界面模型，上下 CSFB 电极化的独立寻址在实际电路中仍具挑战；其“完全补偿亚铁磁 + 1.33 eV 非相对论自旋劈裂”的组合与交变磁体（altermagnet）特征高度吻合，但作者未采用该分类。
