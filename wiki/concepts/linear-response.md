---
tags: [concept]
title: 'linear-response'
type: concept
status: developing
papers: ['Terasaki2011ultrasonic', 'Zhang2008synthesis', 'aiFerroelectricityCoexistedPorbital2022', 'gajdosLinearOpticalProperties2006', 'king-smithTheoryPolarizationCrystalline1993', 'miaoMagneticFerroelectricMetal2024', 'perdewGeneralizedGradientApproximation1996a', 'zhouFirstprinciplesPredictionRedox2004']
updated: 2026-08-18
---

# linear-response

线性响应理论（linear response theory）描述**体系对弱外场（电场、磁场、温度梯度、机械力等）的响应与外场强度成正比**的物理规律，比例系数即各类响应函数（电导率、磁化率、介电函数、极化率、弹性常数等）。Kubo 公式给出响应函数与平衡态关联函数的联系，是凝聚态输运与光学性质的第一性原理计算框架。

## 👵 太奶导读

太奶啊，线性响应就是"轻轻推一下，材料就按比例动一下"的规矩：电场推多大，电流就流多大（这是电导）；磁场推多大，磁化就多大（这是磁化率）。只要推得轻，材料"反应"跟"推力"成正比，这条简单的直线关系能描述绝大部分材料行为，还能通过材料内部的微观"涨落"（关联函数）算出来，是计算材料的看家本领。

## 🧩 核心内容与机制 (Core Content)

- **响应函数**：电导率 σ、介电函数（dielectric-function）、磁化率 χ、极化率等均为线性响应系数；可通过 DFT 的 Kubo-Greenwood、介电函数计算获得（本库 dielectric-function、光学性质论文）。
- **Kubo 公式**：响应函数 = 电流-电流/磁化-磁化等关联函数的傅里叶变换，联系微观涨落与宏观响应（涨落-耗散定理）。
- **输运性质**：电导率、热导率、热电系数（Seebeck）可由线性响应计算，本库热电与输运论文普遍采用。
- **光学响应**：介电函数虚部→吸收谱、折射率；实部→色散，通过 Kramers-Kronig 关系关联（本库折射率、光学带隙论文）。
- **应用**：第一性原理预测光学、输运与磁响应，指导材料筛选（光伏、热电、光电探测）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dielectric-function|介电函数]]：电场-极化线性响应。
- [[../concepts/density-functional-theory|密度泛函理论]]：响应函数的计算框架。
- [[../concepts/band-structure|能带结构]]：输运与光学的电子基础。
- [[../concepts/refractive-index|折射率]]：光学线性响应。

## 📚 相关论文 (Related Papers)

- [[../papers/Terasaki2011ultrasonic]] — Ultrasonic Wave Induced Mechanoluminescence
- [[../papers/Zhang2008synthesis]] — Synthesis and nonlinear optical properties of two three-branched two-photon polymerization initiators
- [[../papers/aiFerroelectricityCoexistedPorbital2022]] — Ferroelectricity coexisted with p-orbital ferromagnetism and metallicity in two-dimensional metal oxynitrides
- [[../papers/gajdosLinearOpticalProperties2006]] — Linear optical properties in the projector-augmented wave methodology
- [[../papers/king-smithTheoryPolarizationCrystalline1993]] — Theory of polarization of crystalline solids
- [[../papers/miaoMagneticFerroelectricMetal2024]] — Magnetic ferroelectric metal in bilayer Fe3GeTe2 under interlayer sliding
- [[../papers/perdewGeneralizedGradientApproximation1996a]] — Generalized Gradient Approximation Made Simple
- [[../papers/zhouFirstprinciplesPredictionRedox2004]] — First-principles prediction of redox potentials in transition-metal compounds with LDA+U
