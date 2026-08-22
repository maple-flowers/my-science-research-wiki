---
tags: [concept]
title: '二十面体堆积 / Icosahedral Packing'
type: concept
status: developing
papers: ['Zhang2019a', 'Zhang2019b', 'Zhang2019c', 'kresseInitiomolecularDynamicsLiquid1993']
updated: 2026-08-18
---

# 二十面体堆积 / Icosahedral Packing

二十面体堆积（icosahedral packing）指**原子以二十面体（icosahedron）局域对称性排列的堆积模式**。它是小尺寸原子团簇与纳米粒子的特征结构：由于二十面体拥有五重对称轴、比晶格堆积更紧密，小体系倾向以此降低表面能，但随着尺寸增大，内部应变累积使其被 HCP/BCC 等晶体堆积取代。该概念与纳米粒子熔化、结构相变与热容行为密切相关。

## 👵 太奶导读

把 13 个原子围成一个"完美小球"（1 个在中间、12 个在表面）就是二十面体——像足球的骨架。对小原子团（直径几纳米）来说，这样排最省表面能，所以"小颗粒爱长成二十面体"。但二十面体内部有"拧巴的应力"，颗粒一大就撑不住，会换成规规矩矩的晶体排列（HCP/BCC）。所以"多大开始换"是纳米材料的关键问题。

## 🧩 尺寸依赖的堆积转变

- **小颗粒倾向二十面体**：Ti 纳米粒子（<2.5 nm）呈现二十面体（Ih）几何壳层闭合与多重结构转变；2.5–4 nm 粒子为"表面预熔—整体崩溃"机制（[[../papers/Zhang2019a|Zhang 2019a]]）。
- **加热-冷却循环中的相变路径**：小颗粒走二十面体路径，大颗粒走 HCP→BCC→熔体路径；两颗粒聚结时出现单畴化机制（[[../papers/Zhang2019b|Zhang 2019b]]）。
- **温度依赖堆积模式**：19–2601 原子的 Ti 团簇中，表面原子主导的尺寸/温度依赖堆积模式转变，小团簇倾向二十面体、大团簇保持 HCP、高温下 HCP/BCC/Ih 共存（[[../papers/Zhang2019c|Zhang 2019c]]）。

## 🧩 与宏观热学定律的衔接

二十面体堆积与纳米粒子熔化行为的偏离，使 **杜隆-珀蒂定律在约 3 nm 以下失效**（[[../papers/Zhang2019a|Zhang 2019a]]、[[../papers/Zhang2019c|Zhang 2019c]]，见 [[../concepts/dulong-petit-law|杜隆-珀蒂定律]]）。原子尺度模拟（经典 MD 与 AIMD）为理解这种堆积-性质关系提供了工具（[[../papers/kresseInitiomolecularDynamicsLiquid1993|Kresse 1993]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Zhang2019a]] — Studying Stability of Atom Packing for Ti Nanoparticles on Heating by Molecular Dynamics Simulations
- [[../papers/Zhang2019b]] — Packing Changes in Melting, Freezing, and Coalescence of Titanium Nanoparticles from Atomic Simulations
- [[../papers/Zhang2019c]] — Atomic simulations of packing patterns and thermal behavior in Ti clusters
- [[../papers/kresseInitiomolecularDynamicsLiquid1993]] — Ab initio molecular dynamics for liquid metals

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/polymorphism|多晶型]]：二十面体-晶格堆积的共存与转变。
- [[../concepts/dulong-petit-law|杜隆-珀蒂定律]]：堆积转变影响其适用边界。
- [[../concepts/cohesive-energy|内聚能]]：堆积模式与能量的关系。
- [[../entities/Ti-nanoparticle|Ti 纳米粒子]]：二十面体堆积研究原型。
*（内容由AI生成，仅供参考）*
