---
tags: [entity]
---

# EPW (Electron-Phonon coupling using Wannier functions)

EPW 是一款集成于 Quantum ESPRESSO 套件中的高性能第一性原理开源代码，专门用于计算材料中的电子-声子相互作用及其诱发的各种物理效应。其核心创新在于利用最大局域化 Wannier 函数 (MLWFs) 实现电声矩阵元在布里渊区内的高效插值。通过在实空间构建局域化的 Wannier 基组，EPW 能够将密度泛函微扰理论 (DFPT) 在粗动量网格上计算得到的 ab initio 数据，以极低的计算成本重构到极细的动量网格上。这一技术突破使得研究者能够精确捕捉费米面上微小的电子态变化以及高分辨率的声子谱特征。

在“相位锁定属性” (Phase-Locked Properties) 的研究范式下，EPW 扮演着连接微观电子-声子耦合与宏观量子物性的关键角色。它不仅锁定了电子能带结构与晶格动力学之间的能量关联，还通过动量分辨的耦合矩阵元 $g_{mn,\nu}(\mathbf{k,q})$ 锁定了物理量的相位一致性。这种锁定机制在探索二维量子材料的超导机制中尤为重要。例如，在针对二维金属-有机框架 Cu3(CO)6 的研究中 [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]，EPW 被用于求解各向异性 Migdal-Eliashberg 方程。通过对 Eliashberg 谱函数 $\alpha^2F(\omega)$ 的精细插值，计算不仅定出了 $T_c = 16.5$ K 的超导临界温度，还揭示了费米面上动量分辨的超导能隙 $\Delta_{n\mathbf{k}}$ 的分布，确认了其单能隙各向异性 BCS 超导特征。这一过程展示了 EPW 如何通过锁定特定的轨道杂化（如 Cu-d 与 O-p 态）与低能声子模式，来解析复杂的各向异性配对物理。

此外，EPW 在解析电荷密度波 (CDW) 等集体失稳现象中也具有显著优势。在单层 2H-TaS2 的环境调控研究中 [[../papers/hallEnvironmentalControlCharge]]，EPW 被用于计算由电声相互作用引起的声子自能 $\Pi_{\mathbf{q}\alpha\beta}$。通过将电子磁化率的嵌套特征与声子谱中的 Kohn 异常进行相位锁定，该研究定量地定出了主导失稳波矢 $q_c$，并阐明了电子掺杂和衬底杂化如何通过重整化声子频率来调控 CDW 序的稳定性。

总结而言，EPW 提供了一套标准化的计算流：从 QE 的基态与响应计算出发，经过 Wannier90 的基组转换，最终在 EPW 中实现对超导、输运、极化子以及热电性质的深度合成。对于具有平带、范霍夫奇点或强关联效应的二维体系，EPW 提供的动量分辨分析能力是理解“相位锁定”物理现象、实现量子物态按需调控的核心技术支撑。
