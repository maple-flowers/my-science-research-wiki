---
tags: [concept]
title: '补偿电荷 / Compensation Charge'
type: concept
status: developing
papers: ['krishnamurthiSpinChargeDensity2020', 'kresseUltrasoftPseudopotentialsProjector1999c', 'shishkinImplementationPerformanceFrequencydependentGWmethod2006']
updated: 2026-08-18
---

# 补偿电荷 / Compensation Charge

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


补偿电荷指**由于极化、电荷密度或拓扑不匹配而在界面、边界或缺陷处产生的束缚/净电荷**，用于平衡两侧的静电失配。在二维材料（如过渡金属二硫族化物）的镜像孪晶界、铁电畴壁等处，补偿电荷是理解一维金属态、畴壁导电与自旋/电荷密度波形成的关键概念。

## 👵 太奶导读

两种不同"电荷风景"拼在一起，接缝处往往会"欠账"或"多账"——欠的账由补偿电荷来填平。在二硫化钼等材料内部一种叫"镜像孪晶界"的特殊接缝上，补偿电荷不但填了账，还凭空造出了一条会导电的"一维金属线"，线上电子还会自发排成周期性的自旋/电荷密度波，非常奇妙。

## 🧩 边界补偿电荷与一维态

- **镜像孪晶界的一维金属态**：MoSe₂/MoS₂ 单层中 4|4P 型镜像孪晶界（MTB）的一维电子态源于体相拓扑极化突变所产生的补偿电荷，其填充率为 1/3；在电子关联（U）作用下，基态转变为无需原子位移的、周期三倍的自旋密度波（SDW）与电荷密度波（CDW）共存态，并打开约 0.1 eV 能隙，允许分数电荷（±1/3 e）孤子存在（[[../papers/krishnamurthiSpinChargeDensity2020|Krishnamurthi 2020]]）。

## 🧩 补偿电荷与计算/电子结构方法

- **精确的电荷描述**：投影缀加波（PAW）方法相比传统赝势能更精确地处理强磁性体系中的自旋极化电荷密度分布，这是准确刻画补偿电荷的前提（[[../papers/kresseUltrasoftPseudopotentialsProjector1999c|Kresse 1999]]）。
- **准粒子级修正**：在 PAW 框架下实现的高效完全频率依赖 G₀W₀ 计算，可对含 d 电子体系给出收敛的准粒子基准值，服务于边界态的电子结构研究（[[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006|Shishkin 2006]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]] — From ultrasoft pseudopotentials to the projector augmented-wave method
- [[../papers/krishnamurthiSpinChargeDensity2020]] — Spin/charge density waves at the boundaries of transition metal dichalcogenides
- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]] — Implementation and performance of the frequency-dependent GW method within the PAW framework

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]：补偿电荷诱导的电子序。
- [[../concepts/charge-transfer|电荷转移]]：边界电荷重新分布的机制。
- [[../concepts/band-structure|能带结构]]：一维金属态的电子结构载体。
- [[../concepts/electron-phonon-coupling|电-声耦合]]：边界电子序的相互作用来源。
- [[../concepts/density-functional-theory|密度泛函理论]]：补偿电荷计算框架。
- [[../concepts/pseudopotential|赝势]]：与 PAW 互补的数值方法。
- [[../entities/MoSe2|MoSe₂]]：镜像孪晶界研究体系。
- [[../entities/MoS2|MoS₂]]：镜像孪晶界研究体系。
