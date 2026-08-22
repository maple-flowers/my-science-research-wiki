---
tags: [concept]
title: 'switching-barrier'
type: concept
status: developing
papers: ['Jin2015studying', 'chenStrongSlidingFerroelectricity2024', 'fengFerroelectricityMultiferroicityTwodimensional2020', 'guanRecentProgressTwoDimensional2020', 'hanTunableSlidingFerroelectricity2025', 'heUltrafastSwitchingDynamics2024', 'huProgressProspectsLowdimensional2019', 'kaurRecentAdvancesTheoretical2025a', 'miaoMagneticFerroelectricMetal2024', 'pedramraziManipulatingTopologicalDomain2019', 'shenEmergenceMultipleFerroelectric2025', 'tangCombiningIntrinsicSlidinginduced2025', 'wuSlidingFerroelectricity2D2021a', 'yuFerroelectricControlMagnetism2026', 'zhangEmergingFrontiersTwodimensional2025', 'zhaoRealization2DMultiferroic2024']
updated: 2026-08-18
---

# switching-barrier

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


翻转势垒（switching barrier）指**铁电/铁磁等有序态的序参量（极化/磁化）在两种稳态之间翻转所需克服的自由能势垒**。其高度决定翻转动力学（成核与畴壁运动）、矫顽场、数据保持稳定性与功耗，是非易失存储与开关器件设计的核心参数，可通过 NEB 与微磁学计算评估。

## 👵 太奶导读

太奶啊，铁电/铁磁材料的"箭头"（极化/磁化）有两个指向：朝上或朝下，代表存 0 或存 1。要翻转这个箭头，得先"爬过一座能量山"——山越高越难翻，但翻过去后越"牢固"（不会自己乱翻）。这座"山"就是翻转势垒。存储芯片要"翻得动又翻不丢"，就是在这座山的高度上做文章。

## 🧩 核心内容与机制 (Core Content)

- **势垒来源**：铁电畴翻转的能量壁垒（成核+畴壁运动），由各向异性能、退极化场与缺陷钉扎决定（本库铁电翻转与畴壁论文）。
- **翻转动力学**：KAI 模型（均匀成核）与成核-畴壁运动模型描述翻转；翻转时间 ∝ 势垒/热涨落（本库铁电畴动力学论文）。
- **矫顽场**：势垒高度与矫顽场（E_C/H_C）正相关；存储器需在保持与功耗间权衡（本库铁电存储论文）。
- **计算方法**：NEB（nudged-elastic-band）计算极化翻转路径与势垒；微磁学模拟磁化翻转（本库磁性翻转论文）。
- **低势垒设计**：二维铁电、超薄势垒与多铁（multiferroic）降低翻转功耗。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：翻转势垒的极化基础。
- [[../concepts/hysteresis|滞回]]：翻转势垒的宏观表现。
- [[../concepts/nudged-elastic-band|NEB 方法]]：势垒计算工具。
- [[../concepts/metastability|亚稳态]]：势垒分隔的两稳态。

## 📚 相关论文 (Related Papers)

- [[../papers/Jin2015studying]] — Studying the Polarization Switching in Polycrystalline BiFeO3 Films by 2D Piezoresponse Force Microscopy
- [[../papers/chenStrongSlidingFerroelectricity2024]] — Strong Sliding Ferroelectricity and Interlayer Sliding Controllable Spintronic Effect in Two-Dimensional HgI₂ Layers
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in two-dimensional Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/guanRecentProgressTwoDimensional2020]] — Recent Progress in Two‐Dimensional Ferroelectric Materials
- [[../papers/hanTunableSlidingFerroelectricity2025]] — Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers
- [[../papers/heUltrafastSwitchingDynamics2024]] — Ultrafast switching dynamics of the ferroelectric order in stacking-engineered ferroelectrics
- [[../papers/huProgressProspectsLowdimensional2019]] — Progress and prospects in low‐dimensional multiferroic materials
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/miaoMagneticFerroelectricMetal2024]] — Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding
- [[../papers/pedramraziManipulatingTopologicalDomain2019]] — Manipulating Topological Domain Boundaries in the Single-Layer Quantum Spin Hall Insulator 1T′–WSe₂
- [[../papers/shenEmergenceMultipleFerroelectric2025]] — Emergence of multiple ferroelectric states in multilayer black phosphorus
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]] — Combining intrinsic and sliding-induced polarizations for multistates in two-dimensional ferroelectrics
- [[../papers/wuSlidingFerroelectricity2D2021a]] — Sliding ferroelectricity in 2D van der Waals materials: Related physics and future opportunities
- [[../papers/yuFerroelectricControlMagnetism2026]] — Ferroelectric Control of Magnetism and Giant Magnetoresistance Via Intercalation-Induced Symmetry Breaking in Two-Dimensional Multiferroics with Strong Magnetoelectric Coupling
- [[../papers/zhangEmergingFrontiersTwodimensional2025]] — Emerging frontiers in two-dimensional sliding ferroelectrics
- [[../papers/zhaoRealization2DMultiferroic2024]] — Realization of 2D multiferroic with strong magnetoelectric coupling by intercalation: a first-principles high-throughput prediction
