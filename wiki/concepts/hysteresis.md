---
tags: [concept]
title: '迟滞 / Hysteresis'
type: concept
status: developing
papers: ['Ismail2015humidity', 'Doroodmand2017conjugated', '2019optical', 'lvUnconventionalHystereticTransition2022', 'chenFerromagneticNonmagnetic1T2022', 'Zhang2019b']
updated: 2026-08-18
---

# 迟滞 / Hysteresis

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


迟滞（hysteresis）指**体系的响应不仅取决于当前输入，还取决于其历史路径**的现象——升程与回程不重合，形成闭合回线。它是铁电/铁磁极化翻转、一级相变、吸附-脱附、电荷密度波转变等众多物理过程的共性指纹。迟滞的存在既赋予材料"记忆"功能（铁电存储、湿度传感的迟滞窗口），也带来开关能耗与响应延迟等应用代价。

## 👵 太奶导读

想象你推一扇很"倔"的门：推过去到一个位置，松开手它不会回到原点，必须把它"推过头"才回来。材料也是这样——同样的外界条件，从"热变冷"和从"冷变热"走的是两条不同的路，中间围出的那块"空隙"就是迟滞。有的材料故意利用这种"记仇"特性做记忆器件（铁电存储就是靠它记住 0 和 1），但也有些场合希望它越小越好（比如湿度计想快点响应）。

## 🧩 微观来源：势垒、亚稳态与畴钉扎

迟滞的本质是体系存在**多个亚稳态**与**能量势垒**：当外部驱动力改变时，体系沿最低能路径演化，但因势垒阻碍而滞后于平衡状态。常见机制包括：

- **畴壁钉扎与成核势垒**：铁电/铁磁极化翻转中，畴壁被缺陷钉扎、新畴成核需要过驱动力，造成翻转场 ≠ 矫顽场的回线；
- **一级相变的成核-长大**：相变需过冷/过热；
- **吸附-脱附不同路径**：水分子在亲水表面的吸附与脱附经历不同中间态（湿度传感迟滞的来源）。

## 💧 湿度传感中的迟滞

纳米结构 ZnO 湿度传感器中，迟滞源于水分子在表面"施主效应"下的吸附-脱附不对称：吸附时水层逐层累积、脱附时受毛细凝聚与氢键网络束缚，导致响应曲线分离（[[../papers/Ismail2015humidity|Ismail 2015]]）。电合成共轭 Salen 聚合物光学湿度计通过反射光强度变化快速响应（~9.5 s），其迟滞窗口受薄膜亲水性与厚度影响（[[../papers/Doroodmand2017conjugated|Doroodmand 2017]]）。聚合物光纤（POF）倏逝场湿度系统同样面临循环迟滞误差，需通过涂层优化与标定压缩（[[../papers/2019optical|2019 optical]]）。

## ❄️ 电荷密度波中的巨迟滞

在准二维 CDW 材料 EuTe₄ 中，研究者发现温度跨度超过 400 K 的**创纪录巨热滞回**：滞回完全发生在非公度 CDW 相内部，仅表现为序参量振幅变化而波矢不变，被归因于 Te 单层与 Te 双层之间 CDW 相对相位（0 或 π）的迟滞切换（[[../papers/lvUnconventionalHystereticTransition2022|Lv 2022]]）。这提示迟滞可被用作探测**隐藏序参量自由度**的工具。

## 🔄 相变循环中的迟滞

- **CDW 可逆相变**：CrS₂ 中电荷掺杂可诱导铁磁/非磁性 1T′ CDW 态可逆转变，伴随高达 12.17% 的驱动应变与磁性突变，循环中的迟滞体现相变势垒（[[../papers/chenFerromagneticNonmagnetic1T2022|Chen 2022]]）。
- **纳米颗粒熔化-凝固**：钛纳米颗粒在加热-冷却循环中表现出尺寸依赖的相变路径（小颗粒二十面体、大颗粒 HCP→BCC→熔体），其熔化与凝固温度分离即热迟滞的直接体现（[[../papers/Zhang2019b|Zhang 2019]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Ismail2015humidity]] — Humidity Sensor - A Review of Nanostructured Zinc Oxide (ZnO) - Based Humidity Sensor
- [[../papers/Doroodmand2017conjugated]] — Electro-synthesized Conjugated Salen Polymer-Glassy Carbon as Hydrochromic Reflective Filter for Humidity Detection
- [[../papers/2019optical]] — Optical Fiber Polymer Sensor System with TiO2-SiO2 Cladding for Measuring Humidity
- [[../papers/lvUnconventionalHystereticTransition2022]] — Unconventional Hysteretic Transition in a Charge Density Wave
- [[../papers/chenFerromagneticNonmagnetic1T2022]] — Ferromagnetic and nonmagnetic 1T′ charge density wave states in transition metal dichalcogenides
- [[../papers/Zhang2019b]] — Packing Changes in Melting, Freezing, and Coalescence of Titanium Nanoparticles from Atomic Simulations

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：极化-电场回线是迟滞的典型体现，用于非易失存储。
- [[../concepts/charge-density-wave|电荷密度波]]：CDW 相变中的巨热滞回与隐藏序参量。
- [[../concepts/humidity-sensing|湿度传感]]：吸附-脱附迟滞决定传感精度与响应速度。
- [[../concepts/phase-transition|相变]]：一级相变的成核-长大过程产生热滞回。
- [[../concepts/magnetic-frustration|磁阻挫]]：阻挫体系的多亚稳态加剧迟滞行为。
- [[../entities/ZnO|ZnO]]：纳米结构湿度传感迟滞研究的代表材料。
