---
tags: [concept, magneto-optics, spintronics, solid-state-physics]
title: 磁光克尔效应 / Magneto-Optical Kerr Effect (MOKE)
type: concept
status: mature
domain: [solid-state-physics, magneto-optics, spintronics]
mechanism: 磁性材料反射光的偏振态因磁化强度而改变，反射光偏振旋转角正比于磁化强度
related_concepts: [kerr-effect, faraday-effect, electromagnon, second-harmonic-generation, magnetoelectric-coupling, optical-activity]
papers: [zhaoOpticalFingerprintsTwodimensional2024, gaoGiantChiralMagnetoelectric2024a]
updated: 2026-08
---

# 磁光克尔效应 / Magneto-Optical Kerr Effect (MOKE)

磁光克尔效应（Magneto-Optical Kerr Effect, MOKE）是指线偏振光从磁性材料表面反射时，由于材料磁化强度（或奈尔矢量）的存在，反射光的偏振面发生旋转、且强度变化的磁光现象。它与透射几何下的[[../concepts/faraday-effect|法拉第效应]]互为表里，是探测磁性薄膜、界面与二维磁性材料最常用的光学手段之一。

## 👵 太奶导读

太奶啊，这就好比往一面**“带磁性的镜子”**上照一束光。镜子里的小磁铁（磁矩）会让反射出来的光的**振动方向（偏振面）**被轻轻扭一下。咱们量一量这个扭转角有多大，就能知道镜面附近的小磁铁是朝上还是朝下、劲儿有多大。关键是它**只测表面那层皮**（几十纳米内），所以特别适合看薄膜和单层二维材料里的磁性。

## 🏗️ 物理机制

MOKE 的物理根源是磁化强度 $\mathbf{M}$ 使材料的介电张量产生**反对称的非对角元**：

$$ \varepsilon = \varepsilon_0 \begin{pmatrix} 1 & iQm_z & -iQm_y \\ -iQm_z & 1 & iQm_x \\ iQm_y & -iQm_x & 1 \end{pmatrix} $$

其中 $Q$ 为磁光 Voigt 参数（正比于 $M$），$\hat{m}$ 为磁化方向单位矢量。这一非对角元导致介质对左旋与右旋圆偏振光的折射率不同（磁圆双折射），反射后两分量重新合成的线偏振光偏振面发生旋转，旋转角 $\theta_K$ 一级近似正比于磁化强度：$\theta_K \propto M$。因此 MOKE 本质上是对磁化矢量的**光学线性读出**。

## 🧩 三种几何构型

| 构型 | 磁化方向 | 探测内容 | 典型用途 |
| --- | --- | --- | --- |
| 极向 (Polar) | 垂直于反射面 | 面外磁化分量 | 垂直磁各向异性薄膜、MnBi2Te4 类磁拓扑材料 |
| 纵向 (Longitudinal) | 平行反射面且在入射面内 | 面内磁化、磁滞回线 | 面内各向异性、畴壁运动 |
| 横向 (Transverse) | 平行反射面且垂直入射面 | 反射率（非偏振）变化 | 磁化取向分辨、自旋阀读出 |

## 🔬 在二维多铁与自旋电子学中的应用

*   **光学指纹区分多铁态**：DFT 计算表明，层间滑移多铁体系（如双层 [[../entities/VSe2|VSe2]]）的四个多铁态在克尔旋转信号上遵循严格对称性规则，极性/奈尔矢量翻转会使 $\theta_K$ 变号，构成“电写-光读”的[[../concepts/magnetoelectric-coupling|磁电耦合]]光学指纹 [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]。
*   **时间分辨磁光克尔 (tr-RKerr)**：用飞秒泵浦-探测记录 $\theta_K$ 的瞬态演化，可实时追踪磁化强度非平衡动力学。在 [[../entities/NiI2|NiI2]] 中，tr-RKerr 捕获了[[../concepts/electromagnon|电磁振子]]引起的动态磁化振荡 $\Delta M$，并与探测电极化的时间分辨[[../concepts/second-harmonic-generation|二次谐波]] (tr-SHG) 对比，证实了巨大手性磁电耦合 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。
*   **二维磁性探测**：MOKE 对表面/界面敏感，是[[../entities/CrI3|CrI3]]、[[../entities/FePS3|FePS3]] 等范德华磁体层分辨磁性测量（层数依赖的磁序）的经典手段。

## 🧩 与法拉第效应的区别

| 对比项 | 磁光克尔 (MOKE) | 法拉第效应 |
| --- | --- | --- |
| 几何 | 反射光 | 透射光 |
| 探测深度 | 表面/界面（约几十纳米） | 体相 |
| 对二维材料 | 敏感（单层可测） | 弱（信号被体相稀释） |
| 不可逆性 | 反射路径 | 非互易（往返翻倍） |

## 📚 相关论文 (Related Papers)

- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：证明克尔旋转可作为二维层间滑移多铁态的对称性约束光学指纹。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：用时间分辨克尔旋转捕获 NiI2 中电磁振子的动态磁信号。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/kerr-effect|克尔效应]]
- [[../concepts/faraday-effect|法拉第效应]]
- [[../concepts/electromagnon|电磁振子]]
- [[../concepts/second-harmonic-generation|二次谐波产生]]
- [[../concepts/optical-activity|旋光性与光学活性]]
- [[../entities/NiI2|二碘化镍 (NiI2)]]
- [[../entities/VSe2|二硒化钒 (VSe2)]]
