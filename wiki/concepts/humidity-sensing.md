---
tags: [concept]
title: '湿度传感 / Humidity Sensing'
type: concept
status: developing
papers: ['Ismail2015humidity', '2019optical', 'Owji20212d', 'XiaokangZhang2013calibrating', 'sunSlidingFerroelectricityTwodimensional2025']
updated: 2026-08-18
---

# 湿度传感 / Humidity Sensing

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


湿度传感（humidity sensing）指**将环境相对湿度（RH）转换为可测电学/光学信号的传感技术**。核心难点在于实现宽量程、低迟滞、快速响应与温漂校准。敏感材料覆盖纳米 ZnO、二维材料（G/GO、MoSe₂、MoS₂）、聚合物光纤涂层等，机理涉及水分子吸附调制电阻/折射率/倏逝场。

## 👵 太奶导读

湿度传感器就是"空气含水量探测计"。它的基本原理是：敏感材料"吸"到水汽后，自身的电阻、折射率或光传导会跟着变，测出这个变化就知道湿度多少。难点在于材料既要"灵敏"又要"不犯迷糊"——吸水和放水的速度要一样快（不然有迟滞），温度一变还得能自动纠正（温漂校准），就像体温计要随时校准一样。

## 🧩 传感机理分类

- **电阻式（ZnO 纳米结构）**：水分子"施主效应"调制耗尽层电阻。四种典型纳米形貌（团簇/棒/片/线）与 Sn/Al 掺杂的利弊权衡，迷宫式电极在电容式传感器中灵敏度最高（[[../papers/Ismail2015humidity|Ismail 2015]]）。
- **光学式（倏逝场调制）**：聚合物光纤中段包层剥离并涂覆 TiO₂-SiO₂ 亲水层，最佳剥离长度 2 cm、R²=0.982，集成 Arduino 系统平均误差 2.78%（[[../papers/2019optical|2019 optical]]）。
- **二维材料涂层**：HF 蚀刻减薄单模光纤并涂覆 G/GO、MoSe₂、MoS₂，G/GO 在 20–90% RH 全量程具有高且单调的 RDA 响应，用表面官能团–半导体类型–Penn 模型折射率框架统一解释（[[../papers/Owji20212d|Owji 2021]]）。

## 🌡️ 温-湿耦合与工程应用

湿度响应强烈依赖温度。琼脂糖涂覆双层包层单模光纤（DCSMF）传感器在 25–34 °C、30–100% RH 范围的响应需基于查找表/校准矩阵工程化校准，并成功埋入新拌混凝土实现 33 小时内部 RH 与温度的实时原位监测（[[../papers/XiaokangZhang2013calibrating|Zhang 2013]]）。吸附-脱附路径差异引入 [[../concepts/hysteresis|迟滞]]，是传感精度的关键制约。

## 📚 相关论文 (Related Papers)

- [[../papers/Ismail2015humidity]] — Humidity Sensor - A Review of Nanostructured Zinc Oxide (ZnO) - Based Humidity Sensor
- [[../papers/2019optical]] — Optical Fiber Polymer Sensor System with TiO2-SiO2 Cladding for Measuring Humidity
- [[../papers/Owji20212d]] — 2D materials coated on etched optical fibers as humidity sensor
- [[../papers/XiaokangZhang2013calibrating]] — Calibrating an optical fiber humidity sensor and applying it in real-time monitoring of relative humidity in fresh concrete
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/relative-humidity|相对湿度]]：湿度传感的核心物理量。
- [[../concepts/hysteresis|迟滞]]：吸-脱附路径差异导致的精度瓶颈。
- [[../concepts/2d-materials|二维材料]]：G/GO、MoSe₂、MoS₂ 等新型敏感材料。
- [[../entities/ZnO|ZnO]]：纳米结构电阻式湿度传感代表材料。
