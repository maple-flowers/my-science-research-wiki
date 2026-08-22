---
tags: [concept]
title: '光引发剂 / Photoinitiator'
type: concept
status: developing
papers: ['WRZYSZCZYNSKI2010initiators', 'Zhang2008synthesis', 'Kumar2017microstructuring', 'Unknown2014passive', 'Gittard2013polymerization']
updated: 2026-08-18
---

# 光引发剂 / Photoinitiator

光引发剂（photoinitiator）是**在光照下产生自由基或活性物种、从而引发单体聚合**的化学组分，是光聚合体系（含双光子聚合 2PP）的核心"触发器"。其性能由吸收截面、活性物种量子产率与引发效率共同决定。**双光子引发剂**通过设计大双光子吸收截面（σ₂）与高效自由基产生路径，使焦点处聚合阈值可被精确控制，直接决定 2PP 的分辨率上限。

## 👵 太奶导读

光引发剂就像打印机的"墨盒感光开关"：光照到它，它就"啪"地放出自由基，把周围液态树脂"焊"成固体。普通光引发剂一颗光子就能触发（单光子）；双光子 3D 打印用的引发剂必须"两颗光子同时打到"才触发——这个苛刻条件恰好让反应只发生在最细的焦点处，所以能打出纳米级结构。引发剂"够不够给力"（吸收截面大不大），直接决定打印精度。

## 🧩 双光子引发机理与分子设计

双光子聚合引发剂的物理机制分**顺序双光子吸收与同时双光子吸收**两类。分子设计准则为 D-π-D / D-π-A-π-D / A-π-D-π-A 推拉电子结构，代表性化合物包括二苯乙烯衍生物、噻嗪染料、三苯胺与香豆素/酮香豆素二元体系（[[../papers/WRZYSZCZYNSKI2010initiators|Wrzyszczyński 2010]]）。

## 🔬 引发剂性能与加工应用

- **多支化增强**：三支化推-拉有机发色团通过分支结构显著增强双光子吸收截面与 2PP 引发能力（[[../papers/Zhang2008synthesis|Zhang 2008]]）。
- **低成本直写**：大双光子吸收截面的噻吨酮引发剂搭配亚纳秒激光器，可搭建低成本 2PP 系统实现约 500 nm 线宽（[[../papers/Kumar2017microstructuring|Kumar 2017]]，见 [[../concepts/diffraction-limit|衍射极限]]）。
- **微流控制造**：2PP 在 PDMS 微通道内原位加工三维被动微混合器，单级结构混合效率超 80%（[[../papers/Unknown2014passive|2014 micromixer]]）。
- **再生医学**：2PP 超衍射极限分辨率用于组织工程支架与微型假体制造，引发剂选择是生物相容性的关键（[[../papers/Gittard2013polymerization|Gittard 2013]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/WRZYSZCZYNSKI2010initiators]] — Two-photon initiators of polymerization
- [[../papers/Zhang2008synthesis]] — Synthesis and nonlinear optical properties of two three-branched two-photon polymerization initiators
- [[../papers/Kumar2017microstructuring]] — Microstructuring by Two-Photon Polymerization using a Sub-Nanosecond Laser
- [[../papers/Unknown2014passive]] — Three-Dimensional Passive Micromixer Fabricated by Two-Photon Polymerization for Microfluidic Mixing
- [[../papers/Gittard2013polymerization]] — Two-photon polymerization microstructuring in regenerative medicine

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/photopolymerization|光聚合]]：光引发剂发挥作用的反应体系。
- [[../concepts/two-photon-excitation|双光子激发]]：双光子引发剂的激发机制。
- [[../concepts/two-photon-absorption|双光子吸收]]：引发剂 σ₂ 的定量描述。
- [[../concepts/nonlinear-optics|非线性光学]]：双光子引发剂的物理基础。
- [[../entities/thioxanthone-photoinitiator|噻吨酮光引发剂]]：大 σ₂ 双光子引发剂的代表。
- [[../entities/diphenyliodonium-salt|二苯基碘鎓盐]]：阳离子光引发体系常用组分。
*（内容由AI生成，仅供参考）*
