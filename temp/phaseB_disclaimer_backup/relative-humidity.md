---
tags: [concept]
title: '相对湿度 / Relative Humidity'
type: concept
status: developing
papers: ['Ismail2015humidity', '2019optical', 'Doroodmand2017conjugated', 'Tobeiha2025optical', 'Yarai2005optical', 'XiaokangZhang2013calibrating']
updated: 2026-08-18
---

# 相对湿度 / Relative Humidity

相对湿度（relative humidity, RH）定义为**当前水汽分压与同温度下饱和水汽压之比**，即 RH = (e/e_s)×100%。它是表征空气中水汽含量的最常用物理量，直接影响材料的吸附-脱附平衡、介电响应与表面导电性，也是湿度传感、气候监测、混凝土养护与文物保护等领域的核心参数。湿度传感器的难点在于实现**宽量程、低迟滞、快速响应与温漂校准**。

## 👵 太奶导读

相对湿度就是"空气里现在装了多少水汽，相对于这个温度下最多能装多少"的百分比。夏天 30 度时空气能"喝"很多水，冬天 0 度时"喝"得少——所以同样 50% 的相对湿度，夏天和冬天的"真实含水量"其实不一样。传感器测的就是这个百分比，而且温度一变它就要跟着重新标定，这也是湿度计最麻烦的地方。

## 🧩 传感机理：水分子与表面相互作用

湿度传感的核心是**水分子与敏感材料表面的物理/化学吸附**改变了材料的电学或光学性质：

- **电阻式**：ZnO 纳米结构中，水分子"施主效应"调制耗尽层电阻，不同形貌（团簇/棒/片/线）与 Sn/Al 掺杂改变灵敏度，迷宫式电极在电容式传感器中灵敏度最高（[[../papers/Ismail2015humidity|Ismail 2015]]）。
- **光学式**：聚合物光纤（POF）中段包层剥离并涂覆 TiO₂-SiO₂ 亲水层，利用倏逝场强度调制实现 RH 测量，最佳剥离长度 2 cm、R²=0.982（[[../papers/2019optical|2019 optical]]）；电合成共轭 Salen 聚合物薄膜作为亲水感湿层与白光反射滤光片，实现 5–80% RH 线性、快速（~9.5 s）检测（[[../papers/Doroodmand2017conjugated|Doroodmand 2017]]）。
- **石墨烯/氧化石墨烯**：声化学剥离的 G/GO 纳米片在 450 nm 蓝光激发下因光子能量足以克服 GO 带隙与激子结合能，灵敏度、线性度与响应/恢复速度（1.0 s/1.3 s）全面最优（[[../papers/Tobeiha2025optical|Tobeiha 2025]]）。
- **热透镜技术**：球透镜光纤微腔 + 泵浦-探测热透镜光谱可无需化学处理包层直接测湿度，且本质上测量绝对湿度（[[../papers/Yarai2005optical|Yarai 2005]]）。

## 🌡️ 温-湿耦合与校准

湿度响应强烈依赖温度，工程应用必须处理**温-湿耦合**。琼脂糖涂覆双层包层单模光纤（DCSMF）传感器在 25–34 °C、30–100% RH 范围内的响应需基于查找表/校准矩阵工程化校准，并已成功埋入新拌混凝土实现 33 小时内部 RH 与温度的实时原位监测（[[../papers/XiaokangZhang2013calibrating|Zhang 2013]]）。湿度传感中的吸附-脱附路径差异还会引入 [[../concepts/hysteresis|迟滞]]，是传感精度的关键制约（见 [[../concepts/humidity-sensing|湿度传感]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Ismail2015humidity]] — Humidity Sensor - A Review of Nanostructured Zinc Oxide (ZnO) - Based Humidity Sensor
- [[../papers/2019optical]] — Optical Fiber Polymer Sensor System with TiO2-SiO2 Cladding for Measuring Humidity
- [[../papers/Doroodmand2017conjugated]] — Electro-synthesized Conjugated Salen Polymer-Glassy Carbon as Hydrochromic Reflective Filter for Humidity Detection
- [[../papers/Tobeiha2025optical]] — Optical humidity sensor based on G/GO nanosheets
- [[../papers/Yarai2005optical]] — Optical fiber sensor for humidity monitoring based on thermal lens detection technique
- [[../papers/XiaokangZhang2013calibrating]] — Calibrating an optical fiber humidity sensor and applying it in real-time monitoring of relative humidity in fresh concrete

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/humidity-sensing|湿度传感]]：以 RH 为核心物理量的传感技术分支。
- [[../concepts/hysteresis|迟滞]]：吸-脱附路径差异导致的响应分离。
- [[../concepts/2d-materials|二维材料]]：G/GO 等新型湿度敏感材料。
- [[../entities/ZnO|ZnO]]：纳米结构湿度传感的代表材料。
- [[../entities/TiO2-SiO2|TiO₂-SiO₂]]：POF 倏逝场湿度传感的亲水涂层。
*（内容由AI生成，仅供参考）*
