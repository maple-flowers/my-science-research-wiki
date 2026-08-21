---
tags: [concept, magnetism, spintronics, multiferroicity]
title: 螺旋磁序 / Helical Magnetism
type: concept
status: mature
year: 2024
domain: [magnetism, spintronics, quantum-materials]
mechanism: 磁矩沿空间呈螺旋状旋转排列，波矢 q 由 DMI（反对称交换）与竞争交换作用之比决定；螺旋磁序可打破空间反演对称诱导铁电极化（自旋驱动多铁）
related_concepts: [dzyaloshinskii-moriya-interaction, skyrmion, ferromagnetism, antiferromagnetism, magnetoelectric-coupling, spin-orbit-coupling, spin-spiral, weak-ferromagnetism]
papers: [RecentAdvancesGrowth2025, songEvidenceSinglelayerVan2022, wuCoexistenceFerroelectricityAntiferroelectricity2024]
updated: 2026-08-20
---

# 螺旋磁序 / Helical Magnetism

螺旋磁序（helical magnetism）指磁性材料中**磁矩沿空间呈螺旋状旋转排列**（螺旋周期远大于晶格常数）的非共线磁结构，通常由 Dzyaloshinskii-Moriya 相互作用（DMI）或竞争交换作用（frustration）驱动。螺旋磁序是斯格明子、磁涡旋与多铁磁电耦合的重要母态。

## 👵 太奶导读

太奶啊，普通磁体磁针齐刷刷朝一个方向排；螺旋磁序则像"拧毛巾"：磁针沿着材料走走走，一边走一边转圈，扫出一条螺旋线。这种"拧巴"的磁序往往由材料里"左右不对称的相互作用"（DMI）造成。拧着拧着，还常拧出小漩涡——斯格明子；而且螺旋磁序还能"拧出"电极化，把磁和电连起来（磁电耦合）。

## 🏗️ 结构概览：螺旋磁序的两条构造路线

螺旋磁序由磁矩排列的波矢 $\mathbf{q}$ 唯一刻画，其周期 $\lambda=2\pi/|\mathbf{q}|$ 通常远大于晶格常数，形成两条物理上不同的构造路线：

- **手性螺旋（chiral helix）**：由反对称 DMI 驱动，螺旋方向（左旋/右旋）被 DMI 矢量 $\mathbf{D}_{ij}$ 的手性锁定，波矢 $q=D/(2J)$（$D$、$J$ 分别为 DMI 与交换强度）。材料破坏空间反演对称（如 B20 结构 MnSi、界面体系）时出现。
- **竞争交换螺旋（frustrated helix）**：由最近邻与次近邻交换竞争（如 $J_1$–$J_2$ 模型）或几何阻挫驱动，无固定手性，常见于阻挫磁体与二维反铁磁格。

按自旋旋转平面相对传播方向，又可区分为**螺旋（helix，旋转面含传播轴）**与**摆线（cycloid，旋转面垂直传播轴）**两种构型，后者是自旋驱动铁电的关键构型（见近邻辨析）。

## 🧩 核心内容与机制 (Core Content)

- **磁序类型**：共线（铁磁/反铁磁）与非共线（螺旋、摆线、斯格明子晶格）；螺旋周期由 DMI/交换比决定（本库 DMI、斯格明子论文）。
- **驱动机制**：界面/体 DMI（dzyaloshinskii-moriya-interaction）产生手性螺旋；竞争交换（frustration）也可稳定螺旋。
- **与斯格明子的关系**：施加磁场可将螺旋磁序转变为斯格明子相（skyrmion），其拓扑荷与手性受 DMI 控制；螺旋相是斯格明子晶格的零场母态。
- **多铁耦合**：螺旋/摆线磁序可打破空间反演对称，诱导铁电极化（自旋驱动铁电），实现磁电耦合（本库多铁 CuO、TbMnO₃ 相关）。
- **二维体系**：二维磁性材料（如 Cr₂Ge₂Te₆ 等）中的螺旋磁序与电场调控为前沿方向，近期本库 2D 多铁综述（[[../papers/RecentAdvancesGrowth2025]]）与单层范德华多铁证据（[[../papers/songEvidenceSinglelayerVan2022]]）即聚焦此方向。

## 📊 物理参数表

| 参数/特征 | 手性螺旋（DMI 驱动） | 竞争交换螺旋（frustration 驱动） |
|---|---|---|
| 波矢 $q$ | $qpprox D/(2J)$，由 DMI/交换比决定 | 由 $J_1/J_2$ 交换竞争决定 |
| 手性 | 被 $\mathbf{D}_{ij}$ 锁定（左/右旋二选一） | 简并，无固有手性 |
| 周期 $\lambda=2\pi/q$ | 远大于晶格常数 | 可为晶格常数量级（短周期螺旋） |
| 对称性要求 | 需破坏空间反演对称 | 需阻挫/竞争交换，无此对称性要求 |
| 典型体系 | MnSi、FeGe、磁性/重金属界面、Cu₂OSeO₃ | 三角/笼目格阻挫磁体、$J_1$–$J_2$ 模型 |
| 拓扑激发 | 斯格明子（磁场驱动） | 磁涡旋、斯格明子 |
| 多铁潜力 | 摆线型可诱导铁电极化 | 螺旋型通常不产生净极化 |

## 🧭 近邻概念辨析

- **螺旋磁序 vs 自旋螺旋（[[../concepts/spin-spiral|spin-spiral]]）**：二者常混用，本库约定"螺旋磁序"强调宏观磁结构类型，"自旋螺旋"侧重微观激发/构型图像；螺旋磁序是自旋螺旋在实空间周期排列的体现。
- **螺旋 vs 摆线**：摆线（cycloid）自旋旋转面垂直传播轴，可产生净电极化（自旋驱动铁电）；螺旋（helix）旋转面含传播轴，通常不产生净极化——这是多铁选材的关键区分。
- **螺旋 vs 斯格明子（[[../concepts/skyrmion|skyrmion]]）**：斯格明子是局域拓扑自旋涡旋（拓扑荷 ±1），螺旋是整体周期磁结构；磁场下螺旋可转变为斯格明子晶格，二者同源于 DMI。
- **螺旋 vs 弱铁磁（[[../concepts/weak-ferromagnetism|weak-ferromagnetism]]）**：弱铁磁是反铁磁自旋微小倾斜产生的净矩，非周期结构；螺旋磁序是宏观周期旋转，二者虽均由 DMI 引起但物态不同。

## 📚 相关论文 (Related Papers)

- [[../papers/RecentAdvancesGrowth2025]] — Recent advances in growth, characterization, and application of two-dimensional multiferroic materials
- [[../papers/songEvidenceSinglelayerVan2022]] — Evidence for a single-layer van der Waals multiferroic
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]] — Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/dzyaloshinskii-moriya-interaction|Dzyaloshinskii-Moriya 相互作用]]：螺旋磁序的核心驱动。
- [[../concepts/skyrmion|斯格明子]]：螺旋磁序的拓扑激发。
- [[../concepts/ferromagnetism|铁磁性]]：与其竞争的共线磁序。
- [[../concepts/antiferromagnetism|反铁磁性]]：螺旋磁序的相关共线母态。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：螺旋磁序诱导的电极化。
- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：DMI 的微观来源。
- [[../concepts/spin-spiral|自旋螺旋]]：螺旋磁序的微观构型图像。
- [[../concepts/weak-ferromagnetism|弱铁磁性]]：同为 DMI 引起的倾斜磁序。

## 🏷️ 专业名词别名

- `helical-spin-order`
- `helimagnetism`
- `spin-helix`
- `helicoidal-magnetic-structure`
- `cycloid`（摆线，特指旋转面垂直传播轴的构型）
