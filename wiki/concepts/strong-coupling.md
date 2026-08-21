---
tags: [concept, superconductivity, strong-coupling, electron-phonon]
title: '强耦合 / Strong Coupling'
type: concept
status: mature
domain: [condensed-matter-physics, superconductivity, strong-correlation]
mechanism: 粒子间相互作用强度远大于动能尺度，微扰论失效，需非微扰方法（Eliashberg/DMFT）
related_concepts: [electron-phonon-coupling, migdal-eliashberg-theory, superconductivity, mott-insulator]
papers: ['zhengAnisotropicSuperconductivityTwodimensional2025', 'majumdarInterplayChargeDensity2020', 'Koley2020charge']
updated: 2026-08
---

# strong-coupling / 强耦合

强耦合（strong coupling）泛指**体系中粒子间相互作用强度远大于其动能的参数区域**，常见语境包括强耦合超导（电子-声子耦合强度 $\lambda \gtrsim 1$）、强关联电子体系（电子-电子相互作用主导）与腔量子电动力学（光-物质强耦合）。强耦合下微扰论失效，需 Eliashberg 理论、动力学平均场（DMFT）等非微扰方法，并催生高温超导、Mott 物理与极化激元等丰富物态。

## 👵 太奶导读

太奶啊，物理里说"强耦合"，就是"粒子之间拽得特别紧"。比如超导里，电子和晶格振动"缠得很死"（强耦合超导），BCS 那套"轻轻牵手"的算法就不准了，得用升级版 Migdal-Eliashberg 方程硬算，才能算出氢化物 200K 高温超导。强耦合的体系"牵绊深、戏份多"，常常冒出别处没有的新奇物态。

## 🏗️ 弱耦合与强耦合对比

| 对比项 | 弱耦合 | 强耦合 |
| --- | --- | --- |
| 耦合强度 | $\lambda \ll 1$ | $\lambda \gtrsim 1$ 或 $U \gg W$ |
| 方法 | 微扰论/BCS | Eliashberg、DMFT、QMC |
| 能隙比 $2\Delta_0/k_BT_c$ | 约 3.52（BCS） | 偏离并增大 |
| 准粒子图像 | 良好（费米液体） | 失效（自能重正化强） |

## 🧩 核心内容与机制 (Core Content)

- **强耦合超导**：电子-声子耦合强度 $\lambda>1$（如 Pb、氢化物超导），需 Eliashberg 理论（[[../concepts/migdal-eliashberg-theory|Migdal-Eliashberg 理论]]）超越 BCS；能隙比、同位素指数偏离弱耦合值。多带/各向异性体系（如 kagome 金属有机框架 Cu₃(CO)₆）中强耦合效应与能带结构纠缠 [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]。
- **强关联电子**：电子-电子相互作用使能带论失效，出现 [[../concepts/mott-insulator|Mott 绝缘体]]、电荷/自旋序与非常规超导。
- **腔量子电动力学**：光与物质共振强耦合形成极化激元，改变材料基态与光学响应。
- **判定参数**：耦合常数 $\lambda$ 或相互作用与带宽比值（$U/W$）；非微扰方法必需。
- **与弱耦合对比**：弱耦合可微扰展开、准粒子近似有效；强耦合需整体重求基态。

## 🧩 超导实例中的强耦合

- 2H-NbS₂/2H-NbSe₂ 中多带超导与 CDW 交织，其能隙与 $T_c$ 关系偏离单带弱耦合 BCS，须用多带强耦合框架刻画 [[../papers/majumdarInterplayChargeDensity2020]]。
- TMD 合金体系中无序释放的 s 波超导其耦合强度随晶格畸变与无序水平变化 [[../papers/Koley2020charge]]。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/electron-phonon-coupling|电子-声子耦合]]：强耦合超导的根源。
- [[../concepts/migdal-eliashberg-theory|Migdal-Eliashberg 理论]]：强耦合超导的计算框架。
- [[../concepts/superconductivity|超导]]：强耦合的超导现象。
- [[../concepts/mott-insulator|Mott 绝缘体]]：强关联的典型物态。

## 📚 相关论文 (Related Papers)

- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] — Anisotropic superconductivity in the 2D metal-organic kagome framework Cu₃(CO)₆
- [[../papers/majumdarInterplayChargeDensity2020]] — Interplay of charge density wave and multiband superconductivity in 2H-NbS₂/NbSe₂
- [[../papers/Koley2020charge]] — Charge density wave and superconductivity in TMDs
