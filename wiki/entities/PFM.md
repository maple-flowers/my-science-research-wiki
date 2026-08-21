---
tags: [entity]
title: 'PFM'
type: entity
status: developing
papers: ['Chen2016electrical', 'Jin2015studying', 'sharmaRoomtemperatureFerroelectricSemimetal2019', 'zahraCriticalAnalysisFerroelectric2025', 'tahirFerroelectricityNonvolatileMemristor2025', 'neumayerCompetingPolarPhases2025']
updated: 2026-08-18
---

# PFM

PFM（压电力显微镜，Piezoresponse Force Microscopy）是**基于扫描探针显微镜（AFM）的压电/铁电表征技术**：探针施加交流偏压，通过检测样品压电形变的幅值与相位成像铁电极化的大小与方向，可实时观察铁电畴结构、畴壁运动与极化翻转动力学，是铁电研究最核心的表征工具（本库铁电/多铁实验论文的标配手段）。

## 👵 太奶导读

太奶啊，PFM 就是用一根极细的探针"摸"材料表面：探针通电后，下面的铁电材料会"鼓一鼓"（压电形变），鼓多鼓少、方向如何，都被探针精确测出来——于是"电箭头"（极化）朝向哪、哪里是畴壁，全都画出图来。想看铁电材料的"微观地图"和电场怎么翻转它，PFM 是第一利器。

## 🧩 核心内容与机制 (Core Content)

- **原理**：探针-样品间交流电场激发逆压电效应，锁相检测振幅（极化大小）与相位（极化方向）（本库铁电表征论文）。
- **畴成像**：幅值/相位图像显示铁电畴与畴壁（domain-wall），分辨率达纳米级（本库多铁与铁电畴论文）。
- **动力学研究**：谱学模式（PFM spectroscopy）与脉冲序列研究局部极化翻转（switching）、成核与疲劳（本库铁电翻转论文）。
- **衍生模式**：矢量 PFM（三维极化）、压电响应谱学、电化学应变显微镜（ESM）。
- **应用**：铁电存储、压电（piezoelectricity）材料、多铁与二维铁电材料表征（本库二维铁电论文）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：PFM 表征的对象。
- [[../concepts/domain-wall|畴壁]]：PFM 成像的结构。
- [[../concepts/piezoelectricity|压电性]]：PFM 的物理原理。
- [[../concepts/polar-vortex|极化涡旋]]：PFM 观察的拓扑结构。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2016electrical]] — Electrical and mechanical switching of ferroelectric polarization in the 70 nm BiFeO3 film
- [[../papers/Jin2015studying]] — Studying the Polarization Switching in Polycrystalline BiFeO3 Films by 2D Piezoresponse Force Microscopy
- [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] — A room-temperature ferroelectric semimetal
- [[../papers/zahraCriticalAnalysisFerroelectric2025]] — A critical analysis of ferroelectric and ferromagnetic properties in two-dimensional MXene
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]] — Ferroelectricity and Nonvolatile Memristor Applications of Free‐Standing 2D Niobium Carbide: A New Frontier of Free‐Standing MXene in Electronic Devices
- [[../papers/neumayerCompetingPolarPhases2025]] — Competing polar phases in 2D ferroelectric transition metal thio- and selenophosphates

## 🏷️ 专业名词别名

- `piezoresponse-force-microscopy`（原 concepts 条目，2026-08-15 合并至此）
- `pfm-piezoresponse-force-microscopy`
