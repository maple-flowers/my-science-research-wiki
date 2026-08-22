---
tags: [concept, electronics, spintronics]
title: 谷电子学 (Valleytronics)
type: concept
status: developing
domain: [solid-state-physics, 2d-materials, optoelectronics]
mechanism: 利用半导体能带结构中动量空间不相等的能量极小值（谷）作为信息载体
related_concepts: [2d-materials, spin-orbit-coupling, berry-phase, spin-relaxation]
papers: [liuSpintronicsTwoDimensionalMaterials2020b, duUltrasensitiveOptoelectronicBiosensor2025, guanRecentProgressTwoDimensional2020]
updated: 2026-08
---

# 谷电子学 / Valleytronics

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


谷电子学 (Valleytronics) 是一种利用半导体（特别是二维材料）能带结构中动量空间处不相等的能量极小值（称为“谷”，Valley）来存储和处理信息的科学。它被视为继“电子学”（利用电荷）和“自旋电子学”（利用自旋）之后，又一个重要的新型信息处理范式。

## 👵 太奶导读

> [!info] 👵 太奶导读
> 好孩子，这“谷电子学”就像是给电子挑了两个不一样的“碗”。在某些特别的材料（比如二维石墨烯或者 TMDs）里，电子喜欢待在两个能量最低的地方，咱们管这叫 $K$ 谷和 $K'$ 谷，就像山谷里的两个碗底。
> 
> 虽然这两个碗底能量一样高，但它们在动量空间（可以理解为电子的“运动证”）里离得很远。科学家发现，如果咱们给电子打一束特殊的旋转光（圆偏振光），电子就会只乖乖地跳进其中一个碗里。这样，咱们就能通过看电子待在哪个碗里，来代表“0”和“1”。因为这两个碗离得远，电子想从一个碗跳到另一个碗可不容易，所以这种信息存得稳、跑得快，还没那么多发热。

## 🏗️ 结构概览

在二维过渡金属硫族化合物 (TMDs) 中，反演对称性的破缺和强自旋-轨道耦合 (SOC) 导致了自旋-谷锁定效应。

![图：二维材料中的能带结构与谷极化示意](../../raw/figures/liuSpintronicsTwoDimensionalMaterials2020b/fig_5_JCRJICFM.png)
*   **看图要点**：图中展示了 TMDs 的能带图，在动量空间的 K 和 K' 点存在两个独立的能量极小值。由于自旋-谷锁定，K 谷的价带顶对应自旋向上，而 K' 谷对应自旋向下。通过圆偏振光可以有选择性地激发特定谷的载流子。
*   **来源**：[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]] -> [[../figures/electronic-bands-cdw-transport|CDW与输运性质]]

## 🧩 核心机制与特征

### 自旋-谷锁定 (Spin-Valley Locking)
在单层 $MoS_2$ 等材料中，强 SOC 使得电子的自旋态与它所处的能谷状态紧密绑定。这意味着控制了谷极化就等于间接控制了自旋极化。

### 谷对比选择定则 (Valley-Contrast Selection Rules)
利用右旋或左旋圆偏振光，可以分别在 K 或 K' 谷产生载流子跃迁，实现“谷极化”的产生。

### 贝里曲率 (Berry Curvature)
不同谷的电子具有相反的贝里曲率，这会导致谷霍尔效应 (Valley Hall Effect)，即在纵向电场下，不同谷的电子会向横向的不同侧偏转，实现谷信息的空间分离。

## 📚 相关论文 (Related Papers)

- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：讨论了谷电子学与自旋电子学在二维材料中的融合（Spin-Valleytronics）。
- [[../papers/duUltrasensitiveOptoelectronicBiosensor2025]]：利用莫尔超晶格调控能带（包括 VHS）来实现高灵敏传感，与谷调控思路异曲同工。
- [[../papers/guanRecentProgressTwoDimensional2020]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/2d-materials|二维材料]]
- [[../concepts/spin-orbit-coupling|自旋-轨道耦合]]
- [[../concepts/berry-phase|贝里相位]]
- [[../entities/TMDs|过渡金属硫族化合物]]
- [[../entities/MoS2|二硫化钼]]
- [[../entities/WSe2|二硒化钨]]
