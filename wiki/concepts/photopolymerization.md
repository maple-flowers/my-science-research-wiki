---
tags: [concept]
title: '光聚合 / Photopolymerization'
type: concept
status: developing
papers: ['Gittard2013polymerization', 'WRZYSZCZYNSKI2010initiators', 'Khitrov2000holographic', 'Jia2023polymerization', 'Kotz2021polymerization', 'Unknown2022polymerization']
updated: 2026-08-18
---

# 光聚合 / Photopolymerization

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


光聚合（photopolymerization）指**利用光（通常为紫外-可见或近红外飞秒激光）激发引发剂产生活性物种、从而驱动单体交联固化的聚合过程**。其中**双光子聚合（two-photon polymerization, 2PP）**凭借焦点处双光子非线性吸收实现超衍射极限分辨率与真三维加工能力，成为微纳制造、光学元件、生物医学器件的核心工艺。

## 👵 太奶导读

光聚合就是"用光把液态树脂'照'成固体"。普通光照一大片区域就固化一大片（像晒照片）；而双光子聚合用的光是"点读笔"——只在焦点那一丁点地方能同时吸收两颗光子，触发固化，其他地方不动。于是它可以一层层、一点点点出任意三维形状，精度能到几百纳米，比头发丝细几百倍，能做微型齿轮、光纤传感器、人造血管支架。

## 🧩 双光子聚合原理

2PP 利用飞秒激光聚焦后焦点处**双光子吸收概率∝光强平方**的特性，聚合只发生在超过引发阈值的极小区域。其分辨率由非线性阈值效应决定，可突破衍射极限（[[../papers/Gittard2013polymerization|Gittard 2013]]、[[../papers/WRZYSZCZYNSKI2010initiators|Wrzyszczyński 2010]]，见 [[../concepts/diffraction-limit|衍射极限]]）。

## 🔬 关键工艺进展

- **全息双光子聚合**：在 DPHPA/液晶 E7 体系中将相分离畴尺寸压缩到 20–200 nm，提升可电控衍射光栅的精度与开关速度（[[../papers/Khitrov2000holographic|Khitrov 2000]]）。
- **像差校正**：单相位 SLM 原位集成波前传感，补偿超 4π 系统像差，使高阶贝塞尔光束恢复近理想形态，快速制造高圆度、无倒塌的 SU-8 微管阵列（[[../papers/Jia2023polymerization|Jia 2023]]）。
- **玻璃微结构**：SiO₂ 纳米颗粒复合树脂经 2PP 直写、热脱脂与高温烧结，获得亚微米分辨率透明熔融石英玻璃三维微结构（[[../papers/Kotz2021polymerization|Kotz 2021]]）。

## 🏥 应用领域

- **再生医学**：组织工程支架、微型假体、血管化支架及微创器械（[[../papers/Gittard2013polymerization|Gittard 2013]]）。
- **光学与传感**：光纤尖端法布里-珀罗腔传感器（[[../papers/Unknown2022polymerization|2022 sensor]]）、可切换光栅（[[../papers/Khitrov2000holographic|Khitrov 2000]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/WRZYSZCZYNSKI2010initiators]] — Two-photon initiators of polymerization
- [[../papers/Gittard2013polymerization]] — Two-photon polymerization microstructuring in regenerative medicine
- [[../papers/Khitrov2000holographic]] — Holographic Two-Photon Polymerization Increases Speed of Switchable Gratings
- [[../papers/Jia2023polymerization]] — Two-photon polymerization of femtosecond high-order Bessel beams with aberration correction
- [[../papers/Kotz2021polymerization]] — Two-Photon Polymerization of Nanocomposites for the Fabrication of Transparent Fused Silica Glass Microstructures

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/photoinitiator|光引发剂]]：光聚合的触发核心。
- [[../concepts/two-photon-excitation|双光子激发]]：2PP 的物理基础。
- [[../concepts/two-photon-absorption|双光子吸收]]：2PP 非线性阈值的来源。
- [[../concepts/diffraction-limit|衍射极限]]：2PP 突破的分辨率瓶颈。
- [[../concepts/nonlinear-optics|非线性光学]]：双光子过程的学科归属。
