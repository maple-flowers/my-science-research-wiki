---
tags: [concept, superconductivity, 2D-materials, charge-density-wave]
title: '超导电性 / Superconductivity'
type: concept
status: mature
domain: [condensed-matter-physics, superconductivity, 2d-materials]
mechanism: 电子配对（库珀对）凝聚为宏观量子态，零电阻 + 完全抗磁（迈斯纳效应）
related_concepts: [charge-density-wave, electron-phonon-coupling, peierls-distortion, intercalation, 2d-materials, superfluid-density]
papers: ['CastroNeto2001charge', 'Koley2020charge', 'Petkov2020hierarchy', 'wuElectrostaticGatingIntercalation2022']
updated: 2026-08
---

# 超导电性 / Superconductivity

超导电性（superconductivity）指**材料在临界温度 $T_c$ 以下电阻突降为零并完全抗磁（迈斯纳效应）**的量子宏观态。其微观根源是电子通过（通常是声子介导的）吸引相互作用配对成库珀对，并凝聚到单一宏观波函数。在二维过渡金属硫族化合物（TMD）中，超导常与电荷密度波（CDW）共存或竞争，二者与晶格畸变、无序和维度效应深度耦合，是理解低维超导的窗口。

## 👵 太奶导读

超导就是"电阻彻底归零 + 把磁场排出去"。二维材料里有个奇妙的戏码：材料先"叠瓦"（CDW，电荷密度波），低温下又"通电畅通"（超导）——两者像一山不容二虎，却又常相伴。弄懂它们的相爱相杀，是低维物理的一大乐事。

## 🏗️ 核心判据与定量描述

| 物理量 | 符号/表达式 | 含义 |
| --- | --- | --- |
| 临界温度 | $T_c$ | 超导转变温度，低于其电阻为零 |
| BCS 能隙 | $2\Delta_0 = 3.52\,k_B T_c$ | 弱耦合极限下的能隙-温度关系 |
| 热力学临界场 | $H_c$ | 超过后超导态被破坏 |
| 穿透深度 | $\lambda_L$ | 磁场在超导体内指数衰减的特征长度 |
| 相干长度 | $\xi$ | 序参量空间变化的最小尺度 |

两个标志性效应：**零电阻**（直流电阻精确为零）与**迈斯纳效应**（内部磁场被完全排出，区别于理想导体）。

## 🧩 CDW 与超导的共存与竞争

- **f 波 CDW 统一图景**：2H-TMD（TaSe₂/TaS₂/NbSe₂/NbS₂）中 CDW 是具有六重节点的 f 波序参量，其低能激发是与声学声子压电耦合的狄拉克电子，统一解释了边缘费米液体自能、CDW 相的良好金属性与声子介导的超导配对（[[../papers/CastroNeto2001charge|Castro Neto 2001]]）。
- **无序释放超导**：非磁性团簇无序通过破坏 CDW 长程相干/预成型激子凝聚而释放被压制的 s 波超导，解释了 TaSe₂₋ₓSₓ 合金中超导重入并增强的现象（[[../papers/Koley2020charge|Koley 2020]]）。
- **晶格-CDW-超导层级**：强晶格畸变破坏一切电子序，完美二维晶格周期性是 CDW 的必要前提，而 Ta 亚晶格的三维周期性才是超导出现的必要条件（[[../papers/Petkov2020hierarchy|Petkov 2020]]）。

## 🧩 二维调控路径

静电门控（表面双电层）与（脱）插层（范德华间隙）可在不破坏层内共价键的前提下动态调控二维层状材料的电子态，是诱导/增强超导的新合成范式（如无限层镍酸盐超导体）（[[../papers/wuElectrostaticGatingIntercalation2022|Wu 2022]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/CastroNeto2001charge]] — Charge Density Wave, Superconductivity, and Anomalous Metallic Behavior in 2D Transition Metal Dichalcogenides
- [[../papers/Koley2020charge]] — Charge density wave and superconductivity in transition metal dichalcogenides
- [[../papers/Petkov2020hierarchy]] — Hierarchy among the crystal lattice, charge density wave, and superconducting orders in TMDs
- [[../papers/wuElectrostaticGatingIntercalation2022]] — Electrostatic gating and intercalation in 2D materials

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]：超导的主要竞争者。
- [[../concepts/electron-phonon-coupling|电子-声子耦合]]：声子介导超导的机制。
- [[../concepts/peierls-distortion|Peierls 畸变]]：CDW 的晶格根源。
- [[../concepts/intercalation|插层]]：调控超导的合成路径。
- [[../concepts/2d-materials|二维材料]]：低维超导的平台。
- [[../concepts/superfluid-density|超流密度]]：超导响应的刚度度量。
- [[../entities/NbSe2|NbSe₂]]、[[../entities/TaSe2|TaSe₂]]：CDW/超导研究体系。
