---
tags: [concept, multiferroics, magnetism, noncollinear, mechanism]
category: [D02]
title: 自旋螺旋 / Spin Spiral
type: concept
status: mature
domain: magnetism
mechanism: 自旋方向沿传播方向周期性旋转的非共线磁序，由竞争交换（J1/J2/J3）与磁阻挫产生，波矢 q 表征周期与手性
related_concepts: [type-ii-multiferroics, magnetoelectric-coupling, electromagnon, inverse-dzyaloshinskii-moriya, multiferroicity, dzyaloshinskii-moriya-interaction, magnetic-frustration]
aliases: ["螺旋磁序", "螺旋自旋序", "摆线磁序", "Spin Spiral", "Helimagnetic order", "自旋螺旋多铁性"]
key_quantities:
  wavevector: "传播矢量 q 决定周期 λ=2π/q；自旋旋转轴 e 与 q 区分螺旋(screw)/摆线(cycloidal)/锥形(conical)"
  origin: "竞争交换（J1/J2/J3）、几何阻挫与 Dzyaloshinskii–Moriya 相互作用共同稳定螺旋"
  ferroelectric: "摆线螺旋按 P∝q×e（自旋流/逆DM）诱导电极化，是 II 型多铁的核心"
  example_NiI2: "单层 NiI2 正螺旋 q=(0.138a*,0,1.457c*)，Tc~21 K，诱导面内极化"
papers: [Goswami2011multiferroic, aminiAtomicscaleVisualizationMultiferroicity2024, gaoGiantChiralMagnetoelectric2024a, songEvidenceSinglelayerVan2022, huProgressProspectsLowdimensional2019]
updated: 2026-08
---

# 自旋螺旋 / Spin Spiral

**自旋螺旋（Spin Spiral，螺旋磁序）** 是一种非共线磁序：自旋方向沿某传播方向（波矢 $\mathbf{q}$）周期性旋转，像螺丝纹一样铺开。它通常由竞争交换作用（$J_1/J_2/J_3$）、几何磁阻挫或 Dzyaloshinskii–Moriya（DM）相互作用稳定。按自旋旋转轴与 $\mathbf{q}$ 的关系，可分为**正螺旋（proper screw，旋转轴 ⊥ q）**、**摆线（cycloid，旋转轴 ⊥ q 且自旋在含 q 平面内旋转）**与**锥形螺旋（conical，旋转轴 ∥ q）**。摆线螺旋会打破空间反演对称并诱导电极化，因而是 [[type-ii-multiferroics|第二类多铁]] 的核心母题 [[../papers/huProgressProspectsLowdimensional2019]]。

## 👵 太奶导读

太奶，您把磁体里一个个原子想成举着小磁针排队的小人。普通铁磁体里，所有小磁针都齐刷刷指同一个方向；反铁磁体里，相邻的两两对着指。可自旋螺旋不一样——这些小磁针一边往前走、一边均匀地转动方向，走一圈正好转过 360 度，就像理发店门口那根红蓝白斜纹转柱，又像一段螺丝钉的螺纹。

它们为啥不好好排队？因为相邻小人之间"该同向还是反向"的指令互相打架（这叫交换作用竞争、磁阻挫），谁也压不倒谁，最后妥协成一个缓缓旋转的螺旋。这螺旋有"左手拧"和"右手拧"两种手性。关键的好戏在后面：当磁针在一个平面里边走边转（这种叫摆线螺旋）时，左右前后就不对称了，硬是被挤出一个电的方向来——这就是第二类多铁"磁生电"的来历，而且螺旋换个手转，电方向立刻跟着翻。二维的 NiI2 单层里就是这种螺旋，科学家用扫描隧道显微镜看到它对应一道道电信号的条纹，还测到了由它产生的特殊光波（电磁振子）。所以自旋螺旋不只是一种磁花样，它是把"磁的旋转"翻译成"电的方向"的那把钥匙。

## 🏗️ 结构概览：螺旋几何与波矢

螺旋磁序用传播矢量 $\mathbf{q}$（决定周期 $\lambda=2\pi/q$）和自旋旋转轴 $\mathbf{e}$ 描述：第 $i$ 个格位的自旋方向随位置 $\mathbf{R}_i$ 绕 $\mathbf{e}$ 旋转角度 $\mathbf{q}\cdot\mathbf{R}_i$。正螺旋中自旋在垂直 q 的平面内旋转、平均磁化为零；锥形螺旋则在螺旋之上叠加一个沿 q 的均匀磁化分量。q 与手性共同决定体系是否破缺反演对称。

![图：NiI2 中左手性与右手性自旋螺旋的对比示意，以及低温螺旋磁序与传播矢量、诱导极化 P 的关系](../../raw/figures/gaoGiantChiralMagnetoelectric2024a/fig_1_8V5GWLM9.png)
*   **看图要点**：(a) 左右两种手性螺旋互为镜像、手性相反；(c) 在 (001) 面上自旋沿 q 旋转并诱导面内极化 P（沿 y 平行 C2 轴），直观显示"螺旋手性 → 极化方向"的对应 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。
*   **来源**：[[../papers/gaoGiantChiralMagnetoelectric2024a]] -> [[../figures/crystal-structures|晶体结构与磁结构]]

## 🧩 形成机制：竞争交换与 DM

- **竞争交换/磁阻挫**：三角晶格等阻挫几何中近邻、次近邻交换（$J_1/J_2/J_3$）相互竞争，使共线 FM/AFM 均非最优，体系通过形成有限 q 的螺旋降低能量。
- **DM 相互作用**：破缺反演对称时，$\mathbf{D}_{ij}\cdot(\mathbf{S}_i\times\mathbf{S}_j)$ 项偏好固定手性的非共线排列，稳定长程螺旋并选择其手性；在 [[inverse-dzyaloshinskii-moriya|逆 DM/自旋流]] 机制中它同时把螺旋耦合到电极化。

## ⚡ 螺旋生极：II 型多铁

摆线螺旋中相邻自旋叉乘 $\mathbf{e}_{ij}\cdot(\mathbf{S}_i\times\mathbf{S}_j)$ 不为零，经自旋-轨道耦合产生 $\mathbf{P}\propto\mathbf{q}\times\mathbf{e}$ 的局域极化；翻转螺旋手性或用磁场改变自旋旋转轴即可翻转/旋转极化（如 TbMnO3 的 90° 极化 flop）。这是本征强磁电耦合的几何来源，并伴随 [[electromagnon|电磁振子]] 这一动态指纹 [[../papers/huProgressProspectsLowdimensional2019]]。

![图：单层 NiI2 多铁性起源——9a×√3a 超胞内自旋螺旋经 SOC 诱导周期为磁螺旋之半的电极化（P 沿 y），STM 可见约 17.8 Å 条纹](../../raw/figures/aminiAtomicscaleVisualizationMultiferroicity2024/fig_1_8XET8BR2.png)
*   **关键特征**：自旋螺旋（q 沿 x、旋转轴沿 z）经 $\mathbf{P}\propto\mathbf{M}\times(\nabla\times\mathbf{M})$ 产生沿 y 的净极化，极化周期是磁螺旋周期的一半，并调制静电势被 STM 直接成像，从原子尺度证实"螺旋生极" [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]。
*   **来源**：[[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] -> [[../figures/crystal-structures|晶体结构]]

## 📊 螺旋类型对照

| 类型 | 自旋旋转轴 vs q | 平均磁化 | 是否生极 | 典型体系 |
| :--- | :--- | :--- | :--- | :--- |
| 正螺旋 screw | 旋转轴 ⊥ q，自旋在 ⊥q 平面 | 零 | 视对称性而定 | 单层 NiI2（proper-screw） |
| 摆线 cycloid | 自旋在含 q 平面内旋转 | 零 | 是（P∝q×e） | TbMnO3 |
| 锥形 conical | 旋转轴 ∥ q + 均匀分量 | 沿 q 非零 | 可有 | 部分螺旋磁体 |

## 📚 相关论文 (Related Papers)

- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：NiI2 中手性自旋螺旋与电磁振子、巨手性磁电响应。
- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]：STM 原子尺度可视化单层 NiI2 螺旋磁序诱导的多铁电极化。
- [[../papers/songEvidenceSinglelayerVan2022]]：单层 NiI2 本征 II 型多铁的光学证据。
- [[../papers/Goswami2011multiferroic]]：纳米 BiFeO3 中自旋螺旋抑制与磁电耦合（螺旋对磁电性质的影响）。
- [[../papers/huProgressProspectsLowdimensional2019]]：低维铁电/多铁综述，阐述螺旋磁序生极机制。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[type-ii-multiferroics|第二类多铁]]、[[magnetoelectric-coupling|磁电耦合]]、[[electromagnon|电磁振子]]、[[inverse-dzyaloshinskii-moriya|逆 DM 相互作用]]、[[dzyaloshinskii-moriya-interaction|Dzyaloshinskii–Moriya 相互作用]]、[[multiferroicity|多铁性]]、[[magnetic-frustration|磁阻挫]]
- [[../entities/NiI2|NiI2]]（二维螺旋多铁代表）、[[../entities/BiFeO3|BiFeO3]]（块体长周期螺旋磁序）
