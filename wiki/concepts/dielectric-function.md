---
tags: [concept]
title: '介电函数 / Dielectric Function'
type: concept
status: developing
papers: ['gajdosLinearOpticalProperties2006', 'shishkinImplementationPerformanceFrequencydependentGWmethod2006', 'liPhaseTransitions2D2021']
updated: 2026-08-18
---

# 介电函数 / Dielectric Function

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


介电函数（dielectric function, ε(ω)）描述**材料对外加电场的频率依赖响应**，其虚部对应光吸收/能量损耗、实部对应极化响应与折射，宏观上由介电张量（含静态与动态介电常数）刻画。介电函数是连接电子结构、光学性质与相变（如铁电软模）的桥梁，也是第一性原理计算的核心输出量之一。

## 👵 太奶导读

介电函数就是材料对电场的"应声虫档案"：不同频率的光照进去，材料是"透明、反光还是吸光"，都写在 ε(ω) 这张表里。它对温度特别敏感——材料临近相变（比如要变铁电）时，介电常数会暴涨，所以看"介电反常"就能提前察觉相变要来了。算材料的人则用第一性原理把它算得又快又准。

## 🧩 介电函数的第一性原理计算

- **PAW 框架下的精确计算**：在标准 PAW 势下即可获得与全电子 APW+LO 方法高度一致的静态与动态介电函数，其精度与收敛速度显著优于传统横向表达式；纵向表达式天然包含关键偶极矩修正项（[[../papers/gajdosLinearOpticalProperties2006|Gajdos 2006]]）。
- **准粒子级修正**：PAW 框架下的完全频率依赖 G₀W₀ 计算（耗时与等离子激元极点模型相当）可为 Si、GaAs、CdS 等提供收敛的准粒子基准，改进介电响应与带隙的描述（[[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006|Shishkin 2006]]）。

## 🧩 介电函数与二维相变

- **相变探针**：二维材料相变（如铁性相变）伴随介电响应的显著变化，介电测量是辨识相变与临界行为的常用手段（[[../papers/liPhaseTransitions2D2021|Li 2021]]）。
- **铁电关联**：铁电软模在临界温度处介电常数发散，介电函数是连接 [[../concepts/ferroelectricity|铁电性]] 与 [[../concepts/phase-transition|相变]] 的宏观量。

## 📚 相关论文 (Related Papers)

- [[../papers/gajdosLinearOpticalProperties2006]] — Linear optical properties in the projector-augmented wave methodology
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials
- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]] — Implementation and performance of the frequency-dependent GW method within the PAW framework

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dielectric-response|介电响应]]：介电函数所属的宏观响应族。
- [[../concepts/density-functional-theory|密度泛函理论]]：介电函数计算框架。
- [[../concepts/gw-approximation|GW 近似]]：准粒子级介电修正。
- [[../concepts/band-structure|能带结构]]：介电函数的微观来源。
- [[../concepts/phase-transition|相变]]：介电反常指示临界行为。
- [[../concepts/ferroelectricity|铁电性]]：软模介电响应的关联序。
- [[../concepts/2d-materials|二维材料]]：介电响应的低维平台。
- [[../concepts/pseudopotential|赝势]]：介电函数计算的数值基础。
