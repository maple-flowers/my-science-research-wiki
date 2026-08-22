---
tags: [entity, material, 2D, TMD, charge-density-wave, superconductor]
title: 二硒化铌 2H 相 (2H-NbSe₂)
type: entity
status: mature
category: [D01]
formula: NbSe2
stoichiometry: 2H
class: [TMD, vdW, metal, superconductor]
properties: [charge-density-wave, superconductivity, electron-phonon-coupling]
related_concepts: [charge-density-wave, superconductivity, electron-phonon-coupling, discommensuration, peierls-instability]
related_entities: [NbSe2, 1T-NbSe2, TiSe2]
key_quantities:
  CDW_transition_temperature: "约 33–33.5 K"
  superconducting_transition_temperature: "约 7.2 K"
  CDW_tunneling_scale: "约 60 meV（局域强耦合图像中的能量尺度）"
  local_ARPES_gap: "约 2.4 meV（K 点局域能隙）"
papers: [gorkovStrongElectronlatticeCoupling2012, Chen2019superconductivity]
updated: 2026-08
---

# 二硒化铌 2H 相 (2H-NbSe₂)

2H-NbSe₂ 是一种层状金属型过渡金属二硫族化物（transition-metal dichalcogenide, TMD）：每个 Se–Nb–Se 单层内部由强键连接，单层之间主要靠范德华力堆叠。它在约 33–33.5 K 进入电荷密度波（charge-density wave, CDW）态，又在约 7.2 K 进入超导态；两个有序态存在于同一金属电子体系中，使它成为研究晶格畸变、电子—声子耦合、部分能隙与超导共存的代表材料。

理解这个材料时要把三个层次分开：**2H 是晶体多型，不是化学成分变化；CDW 是电子密度与晶格位移的周期性重排，不等于绝缘化；超导与 CDW 既会争夺低能电子态，也可能受 CDW 缺陷和涨落增强。** 本页给出这三层关系及其适用边界，不要求读者先阅读其他条目。

## 👵 太奶导读

太奶，您可以把 2H-NbSe₂ 想成一叠很薄的金属夹心饼：每片里是一层铌夹在两层硒中间，片内很牢，片与片之间却容易剥开。降温到大约 33 K 时，原本比较均匀的电子和原子一起排成周期性的“深浅条纹”，这叫电荷密度波；继续降到约 7.2 K，部分电子又结成能无电阻流动的库珀对，于是出现超导。

这两种秩序并不是简单的“一个消失、另一个才出现”。CDW 只改造部分电子态，所以材料仍是金属，也仍能在更低温超导。传统说法把 CDW 全归因于费米面某些片段正好嵌套，但 2H-NbSe₂ 的金属性、能隙尺度和声子行为提示：电子与局部晶格位移之间的强耦合也很重要。CDW 的畴壁或失配区域还可能成为超导优先生长的位置，因此“竞争”和“促进”可以同时发生在不同空间与能量尺度上。

## 🏗️ 结构概览

单层 2H-NbSe₂ 由 Se–Nb–Se 三原子层组成，Nb 位于三棱柱配位环境；“2H”表示六方晶系中以两个单层为一个重复周期的堆垛多型。层内成键形成二维导电骨架，层间范德华间隙使其具有明显各向异性，也允许机械剥离、插层、压力和厚度调控。

这一结构同时提供了两类自由度：Nb $d$ 电子形成金属能带并参与超导，Nb/Se 晶格振动又能与电子密度耦合并形成 CDW。因而 CDW 不能被理解成与原子无关的纯电子条纹，超导也不能脱离已经重构的能带和声子背景单独讨论。

## 🌊 CDW 如何形成而不把材料变成绝缘体

传统 Peierls/费米面嵌套图像认为，某个波矢把大段费米面连接起来，晶格按该波矢畸变并在费米能级开隙。这个图像适合部分一维体系，却难以单独解释 2H-NbSe₂：CDW 转变后材料仍保持金属性，隧穿谱中的特征尺度又远大于 $k_B T_{CDW}$。

[[../papers/gorkovStrongElectronlatticeCoupling2012|Gor’kov 的强耦合理论]]给出实空间补充图像：

1. 传导电子与过渡金属离子位移发生强局域耦合；当无量纲耦合满足 $\Lambda^2>1$，单个离子的有效势由单阱变为两个等价极小值。
2. 每个位点选择左/右位移可映射成伊辛变量；温度降低后，较弱的位点间相互作用再把这些局域选择排列成长程 CDW。
3. CDW 序参量主要使费米能级以下的配对能带反交叉，只在部分动量区域形成能隙，费米面仍保留载流子，所以 CDW 态仍是金属。

该模型不是说费米面和声子色散不重要，而是说明它们不足以由单一嵌套条件概括。对 2H-NbSe₂，文献汇总的 K 点局域 ARPES 能隙约 2.4 meV，而隧穿谱相关尺度约 60 meV；二者对应不同动量与局域能量信息，不能互换。

## ❄️ CDW 与超导：竞争、共存和空间促进

2H-NbSe₂ 在 $T_{CDW}$ 以下仍有未被 CDW 完全开隙的费米面，这些低能电子可在更低温形成超导。CDW 重构能带并占用部分态密度，体现竞争；与此同时，软声子、CDW 涨落和空间缺陷又能改变局部配对条件，所以共存并不等于两者互不作用。

[[../papers/Chen2019superconductivity|Chen 等人的 McMillan–Ginzburg–Landau 理论]]主要以 1T-TiSe₂ 为原型，但也把 2H-NbSe₂ 纳入跨材料比较。其核心机制是：公度 CDW 与非公度 CDW 之间的近公度区包含错位相子（discommensuration）网络；CDW 振幅在这些失配畴壁上降低、梯度增大，超导序参量可优先在网络交点和畴壁上成核，再随降温由孤立点扩展为连通网络乃至二维整体超导。该理论为“CDW 被扰乱时超导增强”提供了空间机制，但它是唯象推广，不能把 TiSe₂ 的具体网格尺寸或相图参数直接当作 2H-NbSe₂ 的实测值。

![图：近公度 CDW 中错位相子网络与局域超导序参量](../../raw/figures/Chen2019superconductivity/fig_2_WA3G7MTL.png)
*   **关键特征**：图中 CDW 相位在错位相子处滑移、振幅下降，超导序参量优先集中于畴壁及其交点，直观展示“CDW 空间缺陷促进局部超导成核”的机制。
*   **来源**：[[../papers/Chen2019superconductivity]]；该图的原型计算对象是 1T-TiSe₂，用于说明可推广到 TMD 的机制，不是 2H-NbSe₂ 的直接成像结果。

## 🔬 如何实验区分这些机制

- **输运与磁化率**确定 $T_{CDW}$ 和 $T_c$，但单凭电阻异常不能给出 CDW 的微观起源。
- **ARPES**观察费米面重构和动量分辨能隙，可判断 CDW 是否只影响部分费米面。
- **STM/STS**测量实空间调制、畴壁和局域态密度；若超导在 CDW 缺陷上增强，应出现空间相关的谱隙变化。
- **非弹性散射与声子谱**追踪软模。2H-NbSe₂ 中声学声子可软化至接近零，但这既可能反映位移型相变，也可能来自声学支与局域光学位移的耦合，不能单独否定局域双阱成分。
- **压力、插层、栅压和厚度调控**可改变层间耦合、载流子浓度及 CDW 公度性；比较时必须同时报告结构多型和样品维度。

## ⚠️ 解读边界

2H-NbSe₂ 的 CDW—超导关系不能简化成“压低 $T_{CDW}$ 就必然提高 $T_c$”。转变温度、CDW 振幅、畴壁密度、费米面态密度和配对相互作用是不同量；调控参数可能同时改变它们。[[../papers/Chen2019superconductivity]]提供的是 TMD 近公度缺陷网络的一般唯象机制，而 [[../papers/gorkovStrongElectronlatticeCoupling2012]]提供的是强局域电子—晶格耦合理论，两者关注的尺度不同，可以互补但不能视为同一个模型的直接证明。

## 📚 相关论文 (Related Papers)

- [[../papers/gorkovStrongElectronlatticeCoupling2012]]：提出强电子—晶格耦合先形成局域双势阱、再经弱位点间作用有序化的 CDW 机制，并用 2H-NbSe₂ 的金属性、能隙和声子数据检验该图像。
- [[../papers/Chen2019superconductivity]]：构建 CDW—超导耦合的唯象理论，指出近公度 CDW 的错位相子网络可驱动非均匀超导成核，并将 2H-NbSe₂ 作为跨 TMD 公度性—超导关系的对照体系。

## 📋 关键参数表

下表汇总仓库现有论文卡片中与 2H-NbSe₂ 直接相关且条件可辨认的量；理论模型参数和其他 TMD 的数值没有移植为本材料实验常数。

| 参数 | 数值 / 范围 | 条件 | 物理意义 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| CDW 转变温度 | 约 33–33.5 K | 2H-NbSe₂ 体材料的非公度 CDW | 晶格与电子密度进入周期调制态的温标 | [[../papers/gorkovStrongElectronlatticeCoupling2012]]；[[../papers/Chen2019superconductivity]] |
| 超导转变温度 | 约 7.2 K | 2H-NbSe₂，CDW 背景中的低温超导 | 零电阻/超导凝聚出现的温标 | [[../papers/Chen2019superconductivity]] |
| 隧穿谱 CDW 特征尺度 | 约 60 meV | 文献汇总的 2H-NbSe₂ 隧穿结果 | 显著大于 $k_B T_{CDW}$，支持其不是简单费米面嵌套隙 | [[../papers/gorkovStrongElectronlatticeCoupling2012]] |
| K 点局域能隙 | 约 2.4 meV | 2H-NbSe₂ 的 ARPES 局域观测 | 说明 CDW 对能带的影响具有动量选择性 | [[../papers/gorkovStrongElectronlatticeCoupling2012]] |
| 费米能级态密度 | 约 2.8 states/eV | 每原胞两条 Nb $d$ 带的模型输入 | 用于估算局域强耦合能量尺度 | [[../papers/gorkovStrongElectronlatticeCoupling2012]] |
| 晶格常数 | 约 3.45 Å | 理论位移尺度比较所用面内晶格常数 | 用于确认估算离子位移远小于晶格尺度 | [[../papers/gorkovStrongElectronlatticeCoupling2012]] |
| Nb 位移尺度 | 约 0.15–0.30 Å | 取声子能量约 10–20 meV 的理论估算 | 检验局域位移展开的数量级自洽性，不是统一实测静态位移 | [[../papers/gorkovStrongElectronlatticeCoupling2012]] |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]：电子密度与晶格位移共同形成的周期有序态。
- [[../concepts/superconductivity|超导电性]]：在 CDW 金属背景中于更低温出现的凝聚态。
- [[../concepts/electron-phonon-coupling|电子—声子耦合]]：连接电子重排与晶格畸变的核心相互作用。
- [[../concepts/discommensuration|错位相子]]：近公度 CDW 中承载相位滑移的失配畴壁。
- [[../concepts/peierls-instability|Peierls 失稳]]：适合一维嵌套体系、但不足以单独解释本材料的传统参照图像。
- [[../entities/NbSe2|NbSe₂]]：不限定多型的上位材料条目。
- [[../entities/1T-NbSe2|1T-NbSe₂]]：相同化学式的不同配位/堆垛多型，不能与 2H 相混用。
- [[../entities/TiSe2|TiSe₂]]：错位相子驱动超导理论的原型对照材料。
