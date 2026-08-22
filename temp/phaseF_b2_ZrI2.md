---
tags: [entity, material, 2d-material, vdw, sliding-ferroelectric]
title: 二碘化锆 / Zirconium Diiodide (ZrI2)
type: entity
status: developing
formula: ZrI2
class: [van-der-waals-material, sliding-ferroelectric, layered-crystal]
properties: [sliding-ferroelectricity, interlayer-sliding, out-of-plane-polarization, room-temperature-ferroelectric]
related_entities: [HgI2, WTe2, MoS2, TMDs]
papers: [chenStrongSlidingFerroelectricity2024, kaurRecentAdvancesTheoretical2025a, wuSlidingFerroelectricity2D2021a, zhangEmergingFrontiersTwodimensional2025]
updated: 2026-08-18
---

# 二碘化锆 / Zirconium Diiodide (ZrI2)

ZrI₂ 是被理论预测的、以层间滑移实现面外极化翻转的滑动铁电体（Sliding Ferroelectricity）候选材料。与依赖离子位移的传统铁电体不同，ZrI₂ 等范德华层状材料通过非极性层的特定堆叠与层间相对滑移打破空间反演对称性，从而产生可翻转的面外电极化。作为"滑移电子学（slidetronics）"的重要候选之一，ZrI₂ 代表了"按需设计铁电功能"这一超越材料本征属性的新范式。

## 👵 太奶导读

乖孙，ZrI₂ 是一叠"轻轻一推就能发电"的极薄晶片。普通铁电材料靠"离子挪位置"来产生电，但这种材料不用那么麻烦——它的每一层都是中性的（不带电），但你把两层像推扑克牌一样错开一点点，两层之间就会"挤出"电来，方向还能反着推回去。这种"靠滑一滑来开关电"的办法，叫做滑动铁电性。科学家看好它，因为它特别薄、不怕累（抗疲劳）、还能存好几个状态，适合做下一代省电又高密度的存储器。

## 🏗️ 结构概览

- **晶体结构**：层状范德华晶体，由非极性单层堆叠而成；典型堆垛构型在层间滑移后打破反演对称性。
- **堆叠自由度**：层间相对位移（如面内滑移）是极化产生的核心自由度，极化强度与层间电荷重排相关。
- **与 HgI₂ 等对照**：与 HgI₂（实验可检测的强滑动铁电体，极化约 0.16 μC/cm²）等同族层状卤化物共同构成滑动铁电候选家族（chenStrongSlidingFerroelectricity2024）。

## 🧩 滑动铁电机制

- **基本机制**：滑动铁电性是一种通过层间面内滑移实现面外极化翻转的普适机制。其极化并非源自阳离子位移，而是源自非中心对称堆垛构型下的层间电荷转移与电子重构；极化翻转能垒低、速度快，且可规避传统铁电体在纳米尺度下的退极化场抑制（wuSlidingFerroelectricity2D2021a）。
- **判据与普适性**：在堆叠双层/多层的对称性分析中，只要满足"滑移后空间反演对称性破缺"的判据，材料即可成为滑动铁电候选；该机制可从半导体推广到金属性二维材料，从理论上将二维铁电候选材料从几种拓展到大多数。
- **ZrI₂ 的定位**：zhangEmergingFrontiersTwodimensional2025 将 ZrI₂、HgI₂ 等列为理论预测的滑动铁电候选材料，强调通过"非中心对称晶相、不对称堆垛、扭转堆垛/莫尔超晶格、非化学计量比组分"等策略可实现并调控滑动铁电性；极化翻转通过层间亚埃级横向滑移实现，多层体系存在逐层翻转的复杂中间态。
- **理论方法**：基于第一性原理计算与对称性分析（含 Berry 相位法计算极化、AIMD 验证室温稳定性），配合 PFM、KPFM、SHG、PUND 等实验表征（kaurRecentAdvancesTheoretical2025a）。

## 📚 相关论文 (Related Papers)

- [[../papers/wuSlidingFerroelectricity2D2021a]]：系统提出滑动铁电性的理论模型、普适判据与"ripplocation"畴壁机制，奠定领域基础。
- [[../papers/zhangEmergingFrontiersTwodimensional2025]]：综述滑动铁电的实现与调控策略，将 ZrI₂、HgI₂ 列为理论候选材料。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：以 HgI₂ 为例给出实验可检测的强滑动铁电体与电控自旋纹理，为 ZrI₂ 一类候选提供对标。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：综述滑动铁电的理论研究方法与前沿进展。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/geometric-ferroelectricity|几何铁电性]]
- [[../concepts/interlayer-coupling|层间耦合]]
- [[../entities/HgI2|HgI₂（强滑动铁电参照）]]
- [[../entities/WTe2|WTe₂（早期滑动铁电体系）]]
