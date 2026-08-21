---
tags: [entity, material, 2d-material, tmd, cdw, superconductor]
title: 二硒化钽 / Tantalum Diselenide (2H-TaSe2)
type: entity
status: developing
formula: 2H-TaSe2
class: [transition-metal-dichalcogenide, cdw-material, superconductor]
properties: [charge-density-wave, superconductivity, commensurate-cdw, gapless-excitation, electron-phonon-coupling]
related_entities: [1T-TaS2, NbSe2, NbS2, TMDs]
papers: [Barnett2006coexistence, Chen2019superconductivity, gorkovStrongElectronlatticeCoupling2012, kimObservationPhaseTransition1997]
updated: 2026-08-18
---

# 二硒化钽 / Tantalum Diselenide (2H-TaSe2)

2H-TaSe₂ 是 2H 相（三棱柱配位）过渡金属二硫族化物中电荷密度波（CDW）研究的原型材料之一。其低温公度 CDW（CCDW）相与金属性（无隙激发）共存的现象，曾是凝聚态物理领域困扰多年的实验谜题；同时它也是研究 CDW 与超导电性竞争、以及 CDW 形成机制（费米面嵌套 vs 电子-晶格耦合）争论的核心载体。

## 👵 太奶导读

乖孙，2H-TaSe₂ 就像一面"既排了队又没排整齐"的电子墙。它里面的电子在低温下会自己排成有规律的图案（电荷密度波，CDW），按理说排好队之后电子就该"卡住"变成绝缘体，可是这材料怪就怪在——队排了，但电子照样能畅通地跑，还是金属！这个怪现象让科学家们琢磨了二十多年。现在大家明白了：原来它排队的时候，只"卡"住了一部分电子，另一部分电子依然自由。这材料还藏着 CDW 和超导（零电阻）之间的"拔河比赛"，是研究材料内部电子如何相互制约的绝佳样品。

## 🏗️ 结构概览

- **晶体结构**：2H 相为三棱柱配位（Ta 原子被 6 个 Se 原子三棱柱包围），层状范德华结构；与 1T 相（八面体）形成对比。
- **低温相**：降温后出现 3×3 公度 CDW 超结构，CDW 转变温度约 110–120 K。
- **共存现象**：公度 CDW 相中费米面保持无隙激发，材料保持金属性，与"CDW 打开全能隙 → 绝缘体"的传统预期矛盾。

## 🧩 CDW 形成机制与无隙共存的物理

- **子晶格解耦机制**：Barnett2006coexistence 基于第一性原理计算（WIEN2k）与能量分辨瓦尼尔函数发现，2H-TMDs 的低能电子结构由次近邻跃迁（t₂）主导、远超最近邻跃迁（t₁）。这使三角晶格可近似解耦为三个独立子晶格；在 CDW 畸变中只有一个子晶格保持未畸变，其电子能带不打开能隙，从而在费米面保留无隙激发，完美解释公度 CDW 与金属性共存。
- **强电子-晶格耦合视角**：gorkovStrongElectronlatticeCoupling2012 提出 CDW 转变分两步进行：强电子-晶格耦合使单个离子形成局域双势阱（体系变为伊辛自旋系统），低温下局域自旋再通过弱位点间相互作用有序化；电子能谱在远离费米能处打开部分能隙，因此保持金属性。
- **CDW 与超导竞争**：Chen2019superconductivity 在统一唯象框架中指出，CDW 由公度到非公度转变的中间态中"错位相子"网络驱动超导成核，可用于理解 2H-TaSe₂ 等 TMDs 中 CDW 与超导的共存与竞争。
- **结构相变操控**：kimObservationPhaseTransition1997 以 1T-TaS₂ 为例展示了 STM 针尖诱导 T→H 相变的机制，表明层状 TMD 表面可在电场与电子激发驱动下发生集体滑移相变，为理解 TaSe₂ 家族多型体间的转变提供了微观图像。

## 📚 相关论文 (Related Papers)

- [[../papers/Barnett2006coexistence]]：以 2H-TaSe₂ 为对象，提出"子晶格解耦"机制，解决公度 CDW 与无隙激发共存的二十年纪录实验谜题。
- [[../papers/gorkovStrongElectronlatticeCoupling2012]]：提出强电子-晶格耦合 + 局域双势阱的伊辛模型，统一解释金属-CD 共存与大能隙起源。
- [[../papers/Chen2019superconductivity]]：提供 CDW-超导竞争的错位相子驱动框架，适用于 2H-TaSe₂ 一类体系。
- [[../papers/kimObservationPhaseTransition1997]]：展示 TMD 表面 T↔H 集体滑移相变的操控与机制。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/fermi-surface-nesting|费米面嵌套]]
- [[../concepts/electron-phonon-coupling|电子-声子耦合]]
- [[../concepts/superconductivity|超导电性]]
- [[../entities/TMDs|过渡金属二硫族化物（TMDs）]]
- [[../entities/1T-TaS2|1T-TaS₂（同族 1T 相参照）]]
