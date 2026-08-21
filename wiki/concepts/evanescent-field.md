---
tags: [concept, optics]
title: 倏逝场 / Evanescent Field
type: concept
status: developing
related_concepts: [refractive-index, optical-band-gap, two-photon-absorption-cross-section]
papers: [2019optical, XiaokangZhang2013calibrating, Owji20212d]
updated: 2026-08
---

# evanescent-field

倏逝场（evanescent field，又称隐失波/近场）指在全反射或波导/亚波长结构中，**沿界面呈指数衰减、不向外传播的电磁场**。它不携带实功率流动，却在近场光学、表面等离子体、非线性光学、传感与超分辨成像中扮演核心角色。

## 👵 太奶导读

太奶啊，光在两种介质交界处"碰壁"全反射时，并没有真的完全弹回——在界面外侧其实"漏"出去一小截光，像手电在玻璃侧面贴着的一圈淡淡光晕，贴着表面爬、越远越弱，这就是倏逝场。它虽然传不远，却能"看见"界面上极其微小的东西，还能增强很多光学效应，是显微镜和传感器里的宝贝。

## 🧩 核心内容与机制 (Core Content)

- **产生条件**：光从高折射率介质入射到低折射率介质且超过临界角（全内反射，TIR）时产生倏逝场；波导、狭缝、纳米颗粒附近的局域场亦为倏逝成分。
- **指数衰减**：倏逝场幅度沿法向指数衰减，穿透深度约波长量级，与入射角、折射率差相关。
- **近场光学**：近场扫描光学显微镜（NSOM/SNOM）利用倏逝场突破衍射极限，实现亚波长成像。
- **表面增强效应**：倏逝场/局域场增强与荧光、非线性光学（双光子吸收）耦合，增强传感与光谱信号（本库双光子探针、双光子聚合相关）。
- **全内反射荧光显微（TIRF）**：利用倏逝场仅激发界面附近荧光团，用于表面与生物界面成像。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/refractive-index|折射率]]：决定全反射与倏逝场条件。
- [[../concepts/optical-band-gap|光学带隙]]：介质光学性质的参考。
- [[../concepts/two-photon-absorption-cross-section|双光子吸收截面]]：近场增强可放大其响应。

## 📚 相关论文 (Related Papers)

- [[../papers/2019optical]] — Optical Fiber Polymer Sensor System with TiO2-SiO2 Cladding for Measuring Humidity
- [[../papers/XiaokangZhang2013calibrating]] — Calibrating an optical fiber humidity sensor and applying it in real-time monitoring of relative humidity in fresh concrete
- [[../papers/Owji20212d]] — 2D materials coated on etched optical fibers as humidity sensor

## 🏷️ 专业名词别名

- `evanescent-wave`（concepts）
