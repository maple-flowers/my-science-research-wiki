---
tags: [concept]
title: '衍射极限 / Diffraction Limit'
type: concept
status: developing
papers: ['Kumar2017microstructuring', 'Kotz2021polymerization', 'Unknown2022polymerization', 'Gittard2013polymerization', 'WRZYSZCZYNSKI2010initiators']
updated: 2026-08-18
---

# 衍射极限 / Diffraction Limit

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


衍射极限（diffraction limit）指**光学系统因光波衍射而无法分辨小于约 λ/2 尺度细节的物理下限**。它是传统光学成像与光刻分辨率的根本瓶颈。**双光子聚合（2PP）**通过焦点处**双光子非线性吸收**（概率∝光强平方）实现"阈上曝光"，可将加工分辨率突破到衍射极限以下（亚微米乃至数百纳米），成为三维微纳制造的核心手段。

## 👵 太奶导读

普通光刻和相机都受一条"物理规矩"限制：因为光是波，聚焦的光斑不可能无限小，最小也就是光波长的一半左右，再细的细节就糊成一片。双光子 3D 打印却钻了个空子——只有光最集中的焦点处才能"同时吸收两颗光子"触发固化，曝光范围被压缩到比光斑还小得多，于是能刻出比衍射极限还细的结构，甚至能"隔空"在材料内部雕刻。

## 🧩 超越衍射极限的机制

双光子聚合的分辨率由**非线性阈值效应**决定：聚合只发生在双光子吸收超过引发阈值的区域，而该区域的横向尺寸随光强非线性收窄，可显著小于聚焦光斑（衍射极限）。配合高数值孔径物镜与低功率飞秒激光，可实现约 500 nm 线宽甚至更细的结构。亚纳秒（700 ps）激光器搭配大双光子吸收截面引发剂同样能搭建低成本直写系统，实现约 500 nm 线宽与 6 μm 高三维微柱（[[../papers/Kumar2017microstructuring|Kumar 2017]]）。

## 🔬 突破衍射极限的制造与应用

- **透明熔融石英玻璃微结构**：含二氧化硅纳米颗粒的光敏复合树脂经双光子聚合直写、热脱脂与高温烧结，首次获得亚微米分辨率的透明熔融石英玻璃三维微结构（[[../papers/Kotz2021polymerization|Kotz 2021]]）。
- **光纤尖端传感器**：双光子聚合在光纤尖端单片制造带微机械铰链与锁扣的可开合法布里-珀罗光学腔，解决封闭微腔内表面镀膜难题（[[../papers/Unknown2022polymerization|2022 sensor]]）。
- **再生医学**：2PP 凭借超衍射极限分辨率与真三维加工能力，用于组织工程支架、微型假体、血管化支架等制造（[[../papers/Gittard2013polymerization|Gittard 2013]]）。
- **引发剂设计**：双光子引发剂的分子设计（D-π-D / D-π-A-π-D 等）是突破分辨率的化学基础（[[../papers/WRZYSZCZYNSKI2010initiators|Wrzyszczyński 2010]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Kumar2017microstructuring]] — Microstructuring by Two-Photon Polymerization using a Sub-Nanosecond Laser
- [[../papers/Kotz2021polymerization]] — Two-Photon Polymerization of Nanocomposites for the Fabrication of Transparent Fused Silica Glass Microstructures
- [[../papers/Unknown2022polymerization]] — Two-photon polymerization for advanced sensor manufacturing
- [[../papers/Gittard2013polymerization]] — Two-photon polymerization microstructuring in regenerative medicine
- [[../papers/WRZYSZCZYNSKI2010initiators]] — Two-photon initiators of polymerization

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/photopolymerization|光聚合]]：双光子聚合突破衍射极限的实现载体。
- [[../concepts/two-photon-absorption|双光子吸收]]：非线性阈值效应的物理来源。
- [[../concepts/two-photon-excitation|双光子激发]]：焦点选择性激发的一般原理。
- [[../concepts/nonlinear-optics|非线性光学]]：超越衍射极限所依赖的光学机制。
- [[../concepts/photoinitiator|光引发剂]]：决定聚合阈值与分辨率的关键化学组分。
