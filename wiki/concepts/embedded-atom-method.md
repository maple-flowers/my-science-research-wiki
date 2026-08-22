---
tags: [concept]
title: '嵌入原子法 / Embedded-Atom Method'
type: concept
status: developing
papers: ['Zhang2019a', 'Zhang2019b', 'Zhang2019c']
updated: 2026-08-18
---

# 嵌入原子法 / Embedded-Atom Method

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


嵌入原子法（embedded-atom method, EAM）是**描述金属及合金原子间相互作用的经典多体势模型**：将每个原子的能量视为其在周围原子电子密度场中的"嵌入能"与两两排斥势之和。EAM 能自然捕捉表面重构、熔化、相变、纳米粒子堆积等金属体系的典型行为，是分子动力学（MD）模拟金属纳米材料的主力势函数。

## 👵 太奶导读

模拟一堆金属原子的运动，不能像小学加法那样只算"两两之间的拉力"——金属里每个原子都泡在邻居们贡献的电子云里，得算"泡在云里的感受"（嵌入能），再加一点两两排斥。这套思路就是嵌入原子法。它特别擅长还原金属表面的小动作：熔化从哪开始、纳米粒子爱摆成什么形状，都能算得八九不离十。

## 🧩 EAM 在金属纳米粒子模拟中的应用

- **钛纳米粒子的熔化行为**：基于原子间势（EAM 类）的分子动力学研究表明，钛纳米粒子的熔化具有强尺寸依赖——直径小于 2.5 nm 的粒子倾向形成稳定的二十面体（Ih）结构并经历多重结构转变，较大粒子呈类块体熔化但表面原子先于内部重排；**表面原子是所有结构转变的源头**，其高移动性驱动整体结构演变（[[../papers/Zhang2019a|Zhang 2019a]]）。
- **堆积转变与相变路径**：小尺寸钛颗粒（如 <300 原子）在加热与冷却后均倾向形成稳定的二十面体结构而非熔化；大尺寸颗粒（>300 原子）加热时经历 HCP→BCC 固态相变再熔化，冷却时路径相反且存在显著过冷滞后；两个颗粒的融合始于接触面变形（[[../papers/Zhang2019b|Zhang 2019b]]）。
- **尺寸依赖的结构多样性**：对包含 19 至 2601 个原子的钛团簇，堆积模式转变由表面原子运动驱动且依赖尺寸与温度；小尺寸团簇倾向形成二十面体结构，大团簇在较宽温区保持 HCP 结构，升温时出现 HCP、BCC 与二十面体共存（[[../papers/Zhang2019c|Zhang 2019c]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Zhang2019a]] — Studying Stability of Atom Packing for Ti Nanoparticles on Heating by Molecular Dynamics Simulations
- [[../papers/Zhang2019b]] — Packing Changes in Melting, Freezing, and Coalescence of Titanium Nanoparticles from Atomic Simulations
- [[../papers/Zhang2019c]] — Atomic simulations of packing patterns and thermal behavior in Ti clusters

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/molecular-dynamics|分子动力学]]：EAM 势的应用平台。
- [[../concepts/phase-transition|相变]]：EAM 模拟捕捉的 HCP-BCC 转变。
- [[../concepts/cohesive-energy|内聚能]]：金属键合的嵌入能视角。
- [[../entities/Ti|Ti]]：EAM 模拟纳米熔化/堆积的典型体系。
