---
tags: [concept, photophysics, spectroscopy]
title: 光致发光 / Photoluminescence (PL)
type: concept
status: developing
domain: [photophysics, molecular-spectroscopy, materials-science]
mechanism: 物质吸收光子后跃迁至激发态，在弛豫过程中以辐射光子的形式释放能量
related_concepts: [fluorescence-quantum-yield, stokes-shift, locally-excited-state, solvatochromism, quenching]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence]
updated: 2026-08
---

# 光致发光 / Photoluminescence (PL)

光致发光（Photoluminescence, PL）是冷发光的一种。当某种物质吸收电磁辐射（通常是紫外或可见光）后，其内部电子受激跃迁到高能级，在退激发回到低能级（通常是基态）的过程中，多余的能量以光子的形式向外辐射，这种现象统称为光致发光。

## 👵 太奶导读

太奶啊，这就好比给一根**荧光棒**（发光分子）喂了点儿能量饮料（入射光子）。这分子喝了能量饮料以后，精神头十足（跃迁到激发态），但它待不住多久，总得把这股子兴奋劲儿给卸掉（退激发）。卸掉的过程就是它自个儿发光的过程（辐射跃迁）。如果这分子“心情好”（环境合适、效率高），它发出的光就特别亮；如果它被环境压制了（猝灭），那光就暗了。咱们科学家就是看这发出的光是什么颜色、有多亮，来判断这分子周围的环境怎么样，就像是看脸上的气色来断病一样。

## 🏗️ 物理过程与能级图

典型的 PL 过程遵循雅布伦斯基图（Jablonski Diagram）：
1.  **吸收 (Absorption)**：电子吸收光子能，从基态 $S_0$ 跳到激发态 $S_1, S_2 \dots$。
2.  **内部转换/振动弛豫**：在受激状态下，电子迅速损失能量降到第一单重激发态 $S_1$ 的最低振动能级。
3.  **辐射跃迁 (Emission)**：电子从 $S_1$ 回到 $S_0$，释放光子。根据时间长短和自旋多重度，可分为**荧光 (Fluorescence)**（纳秒级、单重态）和**磷光 (Phosphorescence)**（微秒至秒级、三重态）。

## 🧩 影响 PL 的关键环境因素

光致发光对分子微环境极其敏感，这是它作为探针的基础：
*   **极性响应（溶剂化显色）**：在强极性溶剂中，激发态偶极矩大的分子会被溶剂进一步稳定，导致发射波长发生显著红移（Stilbene 衍生物 1a 的位移可达 196 nm [[../papers/Huang2023two]]）。
*   **粘度与温度（热致变色）**：高粘度会抑制分子的内转动（如抑制 [[../concepts/tict-mechanism|TICT]] 态的形成），从而增强局域激发态（LE）的荧光强度 [[../papers/Huang2019solvatochromic]]。
*   **猝灭 (Quenching)**：某些化学物质或物理过程（如电荷转移）会导致 PL 强度大幅下降。

## 🔬 特殊发光现象

*   **双光子激发荧光 (TPEF)**：利用两个长波长（低能量）光子同时激发分子产生短波长发光。
*   **多重荧光**：在同一分子中观察到来自不同物种（如 LE 态、TICT 态、激基复合物）的多个发射带，即“三重荧光”现象 [[../papers/H2017fluorescence]]。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：研究了双氰基二苯乙烯探针在环境压力下的双光子荧光响应。
- [[../papers/Huang2019solvatochromic]]：讨论了温度和粘度对光致发光特性的调控。
- [[../papers/H2017fluorescence]]：首次报道了单分子中的双光子三重发光现象。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/fluorescence-quantum-yield|荧光量子产率]]
- [[../concepts/stokes-shift|斯托克斯位移]]
- [[../concepts/solvatochromism|溶剂化显色]]
- [[../concepts/tict-mechanism|TICT 机制]]
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]
