---
tags: [concept]
title: 'refractive-index'
type: concept
status: developing
papers: ['2019optical', 'Blessing2026optical', 'Doroodmand2017conjugated', 'Khitrov2000holographic', 'Khitrov2002internal', 'Owji20212d', 'Srinivasan1989lead', 'Unknown2014optical', 'Unknown2022polymerization', 'Unknown2025diffractive', 'XiaokangZhang2013calibrating', 'Yarai2005optical', 'wuElectrostaticGatingIntercalation2022']
updated: 2026-08-18
---

# refractive-index

折射率（refractive index, n）是表征**光在介质中传播速度变慢（n=c/v）及相位延迟**的基本光学常数，其色散（随波长变化）与消光系数（k，吸收）共同由介电函数决定。折射率决定光学材料的透镜性能、波导、光纤、涂层与非线性光学相位匹配，是光学设计的基础参数。

## 👵 太奶导读

太奶啊，光在真空里跑得最快，进了玻璃、水、晶体等材料会"慢下来"并"拐弯"——"慢了多少、拐多大弯"就是折射率说了算。水里的筷子看起来折断，就是折射率在捣鬼。折射率还能随颜色（波长）变化，不同颜色的光拐弯不一样，彩虹就是这么来的。做眼镜、光纤、激光晶体，第一个参数就是它。

## 🧩 核心内容与机制 (Core Content)

- **定义**：n = c/v；复折射率 N = n + ik，k 为消光系数对应吸收；与介电函数（dielectric-function）关系 ε = N²（本库介电与光学性质论文）。
- **色散**：n(ω) 随波长变化（正常/反常色散），由 Kramers-Kronig 关系与吸收谱关联（本库光学带隙与吸收论文）。
- **非线性光学**：非线性折射率 n₂ 描述光强依赖的折射率变化，用于自聚焦与相位匹配（本库双光子与非线性光学论文）。
- **材料设计**：高折射率（如 TiO₂、Si₃N₄、硫系玻璃）用于光子集成；低折射率（氟化物、气凝胶）用于减反涂层。
- **表征**：椭偏光谱、棱镜耦合法、干涉法测量 n、k 色散（本库 Ti-sapphire 等光学实验装置相关）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dielectric-function|介电函数]]：折射率的微观来源。
- [[../concepts/optical-band-gap|光学带隙]]：折射率与吸收的关系。
- [[../concepts/linear-response|线性响应]]：折射率的光学响应框架。
- [[../concepts/evanescent-field|倏逝场]]：全反射与折射率相关的近场。

## 📚 相关论文 (Related Papers)

- [[../papers/2019optical]] — Optical Fiber Polymer Sensor System with TiO2-SiO2 Cladding for Measuring Humidity
- [[../papers/Blessing2026optical]] — Optical investigation of tin telluride (SnTe) thin films grown at different deposition voltage
- [[../papers/Doroodmand2017conjugated]] — Electro-synthesized Conjugated Salen Polymer-Glassy Carbon as Hydrochromic Reflective Filter for Humidity Detection: Introduction of Humidity Optical Sensor
- [[../papers/Khitrov2000holographic]] — Holographic Two-Photon Polymerization Increases Speed of Switchable Gratings
- [[../papers/Khitrov2002internal]] — Internal Defects Observed by Two-Photon-Induced Photoluminescence
- [[../papers/Owji20212d]] — 2D materials coated on etched optical fibers as humidity sensor
- [[../papers/Srinivasan1989lead]] — MBE-Grown Lead Tin Telluride Infrared Devices
- [[../papers/Unknown2014optical]] — Optical Fiber Relative Humidity Sensor Based on Fabry-Perot Interferometer Coated with Sodium-p-styrenesulfonate/Allyamine Hydrochloride Films
- [[../papers/Unknown2022polymerization]] — Two-photon polymerization for advanced sensor manufacturing
- [[../papers/Unknown2025diffractive]] — Millimeter-Scale Diffractive Optical Elements Fabricated by Two-Photon Polymerization for Beam Shaping in Materials Processing
- [[../papers/XiaokangZhang2013calibrating]] — Calibrating an optical fiber humidity sensor and applying it in real-time monitoring of relative humidity in fresh concrete
- [[../papers/Yarai2005optical]] — Optical fiber sensor for humidity monitoring based on thermal lens detection technique
- [[../papers/wuElectrostaticGatingIntercalation2022]] — Electrostatic gating and intercalation in 2D materials
