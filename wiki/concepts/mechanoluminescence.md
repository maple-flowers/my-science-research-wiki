---
tags: [concept]
title: '力致发光 / Mechanoluminescence'
type: concept
status: developing
papers: ['PChandra2011mechanoluminescence', 'KumarChoubey2011mechanoluminescence', 'Gulhare2021mechanoluminescence', 'Terasaki2011ultrasonic', 'TSUJI2019phosphorescence', 'sunSlidingFerroelectricityTwodimensional2025']
updated: 2026-08-18
---

# 力致发光 / Mechanoluminescence

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


力致发光（mechanoluminescence, ML）指**材料在机械应力（压、拉、摩擦、冲击、超声等）作用下发光**的现象。依据应力类型分为断裂 ML、弹性 ML（EML，可重复）与塑性 ML 等。其核心应用在于**应力分布可视化、结构健康监测与自供能传感**。多数机理模型围绕"机械能→陷阱电子释放→发光中心复合"展开。

## 👵 太奶导读

你小时候捏过"夜光糖"或者荧光棒吗？有些材料更神奇：**不用光照、不用通电，只要捏它、敲它、甚至用超声波远远地"喊"它，它就会发光**——力气越大越亮。这种"越使劲越亮"的材料，可以贴在桥梁、飞机蒙皮上，哪里受力哪里发光，一眼就能看出结构哪里快"撑不住"了。

## 🧩 统一机理：压电诱导电子脱陷模型

Chandra 等系统确立了弹性力致发光（EML）的**压电诱导电子脱陷模型**：应力在压电材料内产生内建电场，将陷阱（缺陷能级）中的电子释放，电子迁移到发光中心（如 Mn²⁺、Eu²⁺）并复合发光；并推导出描述 EML 强度、快慢衰减与压力依赖的定量公式，使 EML 从现象走向可预测（[[../papers/PChandra2011mechanoluminescence|Chandra 2011]]）。

## 🔬 典型体系与研究进展

- **SrAl₂O₄:Eu 纳米磷光体**：燃烧法合成（~21 nm）的单斜相材料，ML 时间曲线呈双峰、强度随冲击速度饱和，365 nm 紫外光可完全恢复 ML；由热释光单一峰（196 °C）用三种方法交叉得到陷阱深度 0.24–0.27 eV，提出"位错运动—陷阱载流子释放—Eu²⁺ 4f⁷↔4f⁶5d¹ 复合"统一模型（[[../papers/KumarChoubey2011mechanoluminescence|Kumar & Choubey 2011]]）。
- **γ 辐照缺陷工程**：γ 辐照可在 Ba₃(VO₄)₂:Eu 荧光粉中诱发出以 606 nm 为中心的橙红色 ML，强度在 Eu 0.1 mol% 与 γ 剂量约 1.4 kGy 时达极值，归因于 Eu³⁺/Eu²⁺ 价态转换 + VO₄²⁻ 空穴陷阱的缺陷介导模型（[[../papers/Gulhare2021mechanoluminescence|Gulhare 2021]]）。
- **超声非接触激发**：37 kHz 超声波（水浴）可非接触式激发 SrAl₂O₄:Eu 产生可重复、功率依赖的 ML，为"体内遥控光源"提供了原理验证（[[../papers/Terasaki2011ultrasonic|Terasaki 2011]]）。
- **衰减动力学**：静水载荷下 ML 材料的磷光衰减曲线需用含吸收因子 γ 的指数模型修正标准单指数衰减，揭示自吸收对表观衰减的显著影响（[[../papers/TSUJI2019phosphorescence|Tsuji 2019]]）。

## 🧱 应用方向与材料拓展

ML 材料广泛用于**应力传感、结构健康监测、指纹/冲击成像**。新型二维滑动铁电材料（如层间滑移极化体系）也被探索用于柔性应力-电耦合器件，其应变-极化响应为力电转换提供新途径（[[../papers/sunSlidingFerroelectricityTwodimensional2025|Sun 2025]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/PChandra2011mechanoluminescence]] — Mechanoluminescence of Nanoparticles
- [[../papers/KumarChoubey2011mechanoluminescence]] — Mechanoluminescence & Thermoluminescence of SrAl2O4:Eu Nano-Phosphors
- [[../papers/Gulhare2021mechanoluminescence]] — Mechanoluminescence Characterization of γ-irradiated Ba3(VO4)2:Eu phosphors
- [[../papers/Terasaki2011ultrasonic]] — Ultrasonic Wave Induced Mechanoluminescence
- [[../papers/TSUJI2019phosphorescence]] — Phosphorescence light decay curve from mechanoluminescence material subjected to hydrostatic load
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/trap-depth|陷阱深度]]：决定 ML 强度与恢复特性的缺陷能级参数。
- [[../concepts/phosphorescence|磷光]]：ML 的发光本质——陷阱电子缓慢复合的余辉过程。
- [[../concepts/photoluminescence|光致发光]]：与 ML 互补的光激发发光通道。
- [[../concepts/piezoelectricity|压电性]]：压电诱导电子脱陷模型的物理基础。
- [[../concepts/energy-transfer|能量传递]]：陷阱电子到发光中心的能量输运路径。
- [[../entities/SrAl2O4-Eu|SrAl₂O₄:Eu]]：弹性 ML 研究的标杆材料。
- [[../entities/SrAl2O4|SrAl₂O₄]]：长余辉与 ML 基体材料。
