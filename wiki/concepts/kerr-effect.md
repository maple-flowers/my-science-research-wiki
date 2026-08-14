---
tags: [concept, non-linear-optics, solid-state-physics]
title: 克尔效应 / Kerr Effect
type: concept
status: developing
domain: [solid-state-physics, non-linear-optics, spintronics]
mechanism: 光场或磁场导致介质折射率发生各向异性改变，从而改变反射/透射光的偏振状态
related_concepts: [optical-activity, faraday-effect, second-harmonic-generation, magnetoelectric-coupling]
papers: [zhaoOpticalFingerprintsTwodimensional2024, gaoGiantChiralMagnetoelectric2024a]
updated: 2026-08
---

# 克尔效应 / Kerr Effect

克尔效应（Kerr Effect）在广义上是指折射率在外部电场、磁场或强光场作用下发生各向异性改变的物理现象。在凝聚态物理与磁性材料研究中，**磁光克尔效应 (Magneto-Optical Kerr Effect, MOKE)** 尤为关键。

## 👵 太奶导读

太奶啊，这就好比一束光（线偏振光）在穿过或者照在一个**“带磁性的镜子”**（磁性材料）上。如果这镜子身上有磁矩（也就是里面无数的小磁铁），它反射出来的光，偏振面（也就是光振动的方向）就会被轻轻**扭转一个小角度**。咱们用精密的仪器测一测这个角度变了多少，就能知道材料里面的磁铁（磁矩）是朝上指还是朝下指，甚至能知道磁性有多强。这就像是不用拆开盒子，只看反光就能知道盒子里有没有装磁铁一样。

## 🏗️ 分类与物理实质

1.  **二次克尔效应 (Quadratic Kerr Effect)**：各向同性介质在电场作用下，折射率的变化与电场强度的平方成正比。
2.  **磁光克尔效应 (MOKE)**：反射光的偏振态由于介质的磁化强度（或奈尔矢量）而发生改变。
    *   **极向克尔 (Polar MOKE)**：磁化强度垂直于反射面（最常用于探测面外磁序）。
    *   **纵向克尔 (Longitudinal MOKE)**：磁化强度平行于反射面且处于入射面内。
    *   **横向克尔 (Transverse MOKE)**：磁化强度平行于反射面且垂直于入射面。

## 🧩 多铁性中的克尔效应与“光学指纹”

在二维范德华多铁材料（如双层 [[../entities/VSe2|VSe2]] 或 [[../entities/MnBi2Te4|MnBi2Te4]]）中，克尔效应提供了独特的磁性态读取手段：
*   **反常光电导 ($\sigma^A_{xy}$)**：克尔旋转角 $\theta_K$ 直接与材料的反常光电导率虚部相关。
*   **多铁态区分**：DFT 计算证明，层间滑移多铁体系的四个不同多铁态在克尔信号上具有严格的对称性变换规则。极性/奈尔矢量翻转时，克尔旋转信号会变号，构成了可用于“电写-光读”的**光学指纹** [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]。

## 🔬 时间分辨磁光克尔 (tr-RKerr)

通过超快光谱技术，利用飞秒脉冲进行 tr-RKerr 测量，可以实时记录磁化强度的非平衡动力学：
*   在 [[../entities/NiI2|NiI2]] 中，tr-RKerr 用于探测电磁振子引起的动态磁化振荡（$\Delta M$），并与探测电极化（$\Delta P$）的时间分辨二次谐波 (tr-SHG) 信号进行直接对比，揭示了巨大的磁电耦合动力学 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。

## 📚 相关论文 (Related Papers)

- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：使用 DFT 模拟证明了克尔效应在区分二维层间滑移多铁态中的关键应用。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：利用时间分辨克尔旋转技术与 tr-SHG 协同，捕获了电磁振子的动力学特性。

## 🔗 关联概念与 entities

- [[../concepts/optical-activity|旋光性与光学活性]]
- [[../concepts/faraday-effect|法拉第效应]]
- [[../concepts/second-harmonic-generation|二次谐波产生]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../entities/VSe2|二硒化钒 (VSe2)]]
