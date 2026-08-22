---
tags: [concept]
title: 'Born 有效电荷 / Born Effective Charge'
type: concept
status: developing
papers: ['king-smithTheoryPolarizationCrystalline1993', 'bhowalPolarMetalsPrinciples2023b', 'laiTwodimensionalFerromagnetismDriven2019', 'gomez-ortizKittelLawDomain2023', 'kaurRecentAdvancesTheoretical2025a', 'zhangEmergingFrontiersTwodimensional2025']
updated: 2026-08-18
---

# Born 有效电荷 / Born Effective Charge

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


Born 有效电荷（Born effective charge，记为 Z\* 或 Z\*_αβ）描述**极化对某一离子位移的线性响应**：Z\*_αβ = Ω·(∂P_α/∂u_β)，其中 Ω 为晶胞体积、P 为电极化、u 为离子位移。它是连接**原子尺度运动**与**宏观介电/压电/铁电响应**的桥梁：红外活性、LO-TO 劈裂、压电系数与铁电极化翻转均与其直接相关。与名义离子电荷不同，Born 有效电荷是**反常的**——它可能远大于名义电荷甚至出现负值，因为其数值受共价键内电荷重新分布（动流/反流机制）的强烈调制。

## 👵 太奶导读

想象一支队伍，领头的人喊"全体左移一步"，整支队伍平移；但材料里的原子不一样——你只需要"挪动一个原子"，周围的电子云会跟着"抢跑"，导致整个晶胞的电荷中心移动得比原子还多。这个"一个原子动一下，极化跟着动多少"的比例系数，就是 Born 有效电荷。它经常比原子本身带的电荷大好几倍，甚至可能是"负的"——就像有些队员你推他往左，他却带着大家往右跑。算清楚它，才能设计压电器件、铁电器件和红外探测器。

## 🧩 微观机制：共价动流与反流

Born 有效电荷的异常值源于**原子位移诱导的电子云重新分布**，而非简单的刚体离子模型。在共价/离子混合成键体系中，某一原子移动时，与其成键的电子密度会发生不对称重排，产生两类效应：**动流（dynamical flow）**——电子沿成键方向整体漂移放大极化；**反流（back-flow）**——电子反向移动部分抵消名义电荷贡献。两者竞争决定了 Z\* 的大小与符号。因此，有效电荷是**电子结构敏感的局域量**，可通过密度泛函理论（[[../concepts/density-functional-theory|密度泛函理论]]）的 DFPT 或有限位移法精确计算。

## 📐 理论根基：现代极化理论

Born 有效电荷的严格定义建立在**现代极化理论**之上。King-Smith 与 Vanderbilt 证明，晶体的电极化变化 ΔP 等于价带波函数贝里相位之差，物理上等价于 **Wannier 函数电荷中心**的位移（[[../papers/king-smithTheoryPolarizationCrystalline1993|King-Smith 1993]]）。由此，Z\*_αβ 可视为"随原子位移演化的极化斜率"，其在计算中的实现（Berry phase 法）为第一性原理预测压电、铁电与红外性质奠定了标准算法。该理论至今仍是凝聚态计算物理的基石工具。

## 🔬 在铁电与多铁研究中的应用

- **铁电金属**：Bhowal 等系统综述了极性与金属性共存的"禁忌"组合，其中 Born 有效电荷与极化翻转动力学是理解 LiOsO₃（类铁电金属）与 WTe₂（可翻转铁电金属）的关键量（[[../papers/bhowalPolarMetalsPrinciples2023b|Bhowal 2023]]）。
- **二维多铁**：对范德华 CuCrP₂S₆，第一性原理计算表明其面外铁电性源于 Cu 位移，而 Cu 的 Born 有效电荷行为与面外极化密切相关，且与自旋、谷自由度通过自旋-轨道耦合相互锁定（[[../papers/laiTwodimensionalFerromagnetismDriven2019|Lai 2019]]）。
- **畴结构与极化翻转**：在 (PbTiO₃)ₙ/(SrTiO₃)ₙ 超晶格中，涡旋畴壁的成核-合并动力学与 Kittel 定律的验证，均依赖于对局部极化（即 Born 有效电荷积分）的精确刻画（[[../papers/gomez-ortizKittelLawDomain2023|Gómez-Ortiz 2023]]）。
- **滑动铁电性**：层间滑移产生的面外极化与滑移模式的选择，同样可由 Born 有效电荷的层分辨投影加以分析（[[../papers/kaurRecentAdvancesTheoretical2025a|Kaur 2025]]、[[../papers/zhangEmergingFrontiersTwodimensional2025|Zhang 2025]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/king-smithTheoryPolarizationCrystalline1993]] — Theory of polarization of crystalline solids
- [[../papers/bhowalPolarMetalsPrinciples2023b]] — Polar Metals: Principles and Prospects
- [[../papers/laiTwodimensionalFerromagnetismDriven2019]] — Two-dimensional ferromagnetism and driven ferroelectricity in van der Waals CuCrP₂S₆
- [[../papers/gomez-ortizKittelLawDomain2023]] — Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices
- [[../papers/kaurRecentAdvancesTheoretical2025a]] — Recent advances in theoretical investigations of sliding ferroelectricity in layered and van der Waals two-dimensional materials
- [[../papers/zhangEmergingFrontiersTwodimensional2025]] — Emerging frontiers in two-dimensional sliding ferroelectrics

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：Born 有效电荷是极化翻转与压电响应的微观来源。
- [[../concepts/geometric-ferroelectricity|几何铁电性]]：结构畸变协同产生的极化，同样由有效电荷刻画。
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]：层间滑移驱动极化，依赖层分辨的 Born 有效电荷。
- [[../concepts/piezoelectricity|压电性]]：压电张量直接由 Born 有效电荷与力常数决定。
- [[../concepts/multiferroicity|多铁性]]：极化-磁性耦合体系中的极化响应度量。
- [[../concepts/density-functional-theory|密度泛函理论]]：计算 Born 有效电荷的第一性原理框架。
- [[../entities/PbTiO3|PbTiO₃]]：典型铁电体，Born 有效电荷显著反常的代表。
