---
tags: [entity, material, magnetic, 2D, vdW, multiferroic, sliding-ferroelectricity]
title: 六碲化二锗二铬 / Chromium Germanium Telluride (Cr2Ge2Te6, CGT)
type: entity
status: mature
category: [D01, Z02]
formula: Cr2Ge2Te6
aliases: ["CGT", "Cr₂Ge₂Te₆", "chromium germanium telluride"]
class: [transition-metal-thiophosphate-derivative, vdW, magnetic-semiconductor]
properties: [heisenberg-ferromagnetism, weak-magnetic-anisotropy, stacking-dependent-magnetism, sliding-ferroelectricity, artificial-magnetoelectric-coupling]
related_entities: [CrI3, Fe3GeTe2, In2Se3, NiI2, CrInTe2]
key_quantities:
  Tc_bulk: "~61 K"
  magnetic_easy_axis: "近面外（弱各向异性，近似 Heisenberg 铁磁）"
  Cr_state: "Cr³⁺ t2g³，S = 3/2"
  band_gap: "~0.7 eV（间接带隙）"
  note: "双层基态为层间反铁磁；反平行堆垛非中心对称，可承载滑动极化（理论）"
papers: [FerroelectricityMultiferroicityAtomic2023, tangMultiferroicityTwodimensionalVan2025, kaurRecentAdvancesTheoretical2025a]
updated: 2026-08
---

# 六碲化二锗二铬 / Chromium Germanium Telluride (Cr2Ge2Te6, CGT)

Cr2Ge2Te6（CGT）是二维范德华铁磁半导体的原型材料之一，与 CrI3 并列为最早在原子级厚度下证实长程铁磁序的体系。其块体居里温度 $T_C\approx61$ K，Cr³⁺（$S=3/2$）构成近平面蜂窝晶格，磁各向异性较弱、近似二维 Heisenberg 铁磁体；带隙约 0.7 eV。CGT 本身并非铁电体，但通过与铁电材料堆叠（如 CGT/In2Se3）可构建人工多铁异质结，而反平行堆垛的 CGT 双层在理论上还可承载层间滑动铁电性 [[../papers/FerroelectricityMultiferroicityAtomic2023]] [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 👵 太奶导读

太奶，这"CGT"跟前面说的 CrI3 是同门师兄弟，都是薄到一层原子还自带磁性的材料。您就把它想成一摞薄饼，饼上撒满了 tiny 的小磁针。它的磁针跟 CrI3 不太一样：CrI3 的磁针被摁得死死的、只能朝上朝下（叫 Ising），CGT 的磁针却没那么"倔"，大体上能在饼面附近自由转动，只稍微有点想竖起来的倾向——这种"好说话"的磁铁叫 Heisenberg 铁磁体。也正因为管束得松，它得冷到约零下二百一十度（61 K）磁针才肯齐刷刷站队。

CGT 自己只会磁、不会"记电"（没有铁电性）。但科学家有办法：把它跟一片会记电的薄片（比如硒化铟 In2Se3）背对背贴一起，电薄片一翻身，CGT 的磁针就跟着改脾气——这就叫人工磁电耦合，是将来省电存储器的招儿。另有理论家算出来：两张 CGT 饼错开着叠（反平行堆垛）时，叠法不对称，竟也能像 CrI3 那样搓出一点电极化来。这一点目前主要是算出来的，太奶您知道有这门道就行。

## 🏗️ 结构概览

CGT 是层状范德华晶体：Cr 原子被 Te 八面体配位，与 Ge 共同构成每层约一个原子厚的"三明治"，层间靠弱范德华力结合，可机械剥离。双层中两层可以平行或反平行堆垛，这直接决定层间磁耦合与是否破缺反演对称。

![图：CrI3、Cr2Ge2Te6、Fe3GeTe2 双层的几何结构（a–c）与铁电翻转能垒（d）](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_21_7MRZGUTM.png)
*   **看图要点**：(b) 为反平行堆垛的 CGT 双层——平行堆垛中心对称，反平行堆垛非中心对称，后者才允许面外极化；(d) 对比三种磁性双层沿滑动路径的铁电翻转能垒，CGT 居于其间 [[../papers/kaurRecentAdvancesTheoretical2025a]]。
*   **来源**：[[../papers/kaurRecentAdvancesTheoretical2025a]] -> [[../figures/crystal-structures|晶体结构]]

## 🧩 近 Heisenberg 二维铁磁性

- **磁序**：Cr³⁺ 为 $t_{2g}^3$（$S=3/2$），经 Cr–Te–Cr 超交换耦合形成铁磁序，块体 $T_C\approx61$ K；减薄后 $T_C$ 下降但仍可保持长程序，是验证二维磁性（磁各向异性绕开 Mermin–Wagner 限制）的标杆体系之一。
- **各向异性**：与 CrI3 的强 Ising 面外各向异性不同，CGT 磁各向异性较弱、易轴略偏离平面，更接近理想二维 Heisenberg 铁磁体，因此对衬底、应变和外场更敏感。
- **能带**：自旋极化计算（含 Hubbard U 修正）给出约 0.7 eV 的间接带隙，属磁性半导体 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

![图：CrI3、Cr2Ge2Te6、Fe3GeTe2 三种磁性双层的带隙、面外极化与铁电翻转能垒汇总](../../raw/figures/kaurRecentAdvancesTheoretical2025a/tab_1_3QKTNISV.png)
*   **关键特征**：表 1 给出 CGT 双层的间接带隙（~0.7 eV）、反平行堆垛诱导的面外极化以及 NEB 翻转能垒，并与铁磁的 CrI3、金属性的 Fe3GeTe2 对照，凸显 CGT 作为磁性半导体的定位 [[../papers/kaurRecentAdvancesTheoretical2025a]]。
*   **来源**：[[../papers/kaurRecentAdvancesTheoretical2025a]] -> [[../figures/crystal-structures|晶体结构]]

## ⚡ 人工多铁与滑动铁电

- **CGT/In2Se3 异质结**：理论预言，把铁磁 CGT 与铁电 In2Se3 堆叠，翻转 In2Se3 的电极化可显著改变 CGT 的磁各向异性或交换强度，从而实现非易失、全电学的磁电调控——这是"异质结工程"获取多铁性的通用策略 [[../papers/FerroelectricityMultiferroicityAtomic2023]] [[../papers/tangMultiferroicityTwodimensionalVan2025]]。
- **双层滑动极化**：反平行堆垛的 CGT 双层非中心对称，层间界面电子云重排可产生面外极化，沿滑动路径存在与 CrI3、Fe3GeTe2 可对比的翻转能垒；该双层基态为层间反铁磁（与铁磁的 CrI3 双层不同）[[../papers/kaurRecentAdvancesTheoretical2025a]]。

![图：CrI3、Cr2Ge2Te6、Fe3GeTe2 双层沿滑动路径的铁电翻转能垒对比](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_21_7MRZGUTM.png)
*   **关键特征**：(d) 面板把 CGT 双层（反平行堆垛，基态层间 AFM）的 NEB 能垒与 CrI3、Fe3GeTe2 并列，能垒高低决定滑动翻转的省电程度；(b) 中状态 I/II 为极化反向的两个双稳态 [[../papers/kaurRecentAdvancesTheoretical2025a]]。
*   **来源**：[[../papers/kaurRecentAdvancesTheoretical2025a]] -> [[../figures/heterostructures-stacking-sliding|层间滑移]]

## 📊 主要物性参数

| 参数 | 数值 | 备注 |
| :--- | :--- | :--- |
| 块体 $T_C$ | ~61 K | 减薄后降低 |
| 磁易轴 | 略偏面外（弱各向异性） | 近 Heisenberg 铁磁 |
| Cr 价态/自旋 | Cr³⁺，$t_{2g}^3$，$S=3/2$ | Cr–Te–Cr 超交换 |
| 带隙 $E_g$ | ~0.7 eV | 间接带隙磁性半导体 |
| 双层基态 | 层间反铁磁 | 反平行堆垛非中心对称 |
| 材料家族 | 金属硫代磷酸盐衍生物 | 范德华磁性半导体 |

## 📚 相关论文 (Related Papers)

- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：综述原子级厚度多铁性，讨论 CGT/In2Se3 异质结的磁电耦合。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：二维范德华多铁综述，含 CGT 人工多铁器件前景。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：§3.4 对比 CGT/CrI3/Fe3GeTe2 双层堆垛、滑动极化与翻转能垒。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferromagnetism|铁磁性]]、[[../concepts/heisenberg-model|Heisenberg 模型]]、[[../concepts/ising-model|Ising 模型]]、[[../concepts/magnetic-anisotropy-energy|磁各向异性能]]、[[../concepts/superexchange|超交换]]、[[../concepts/magnetoelectric-coupling|磁电耦合]]、[[../concepts/sliding-ferroelectricity|滑动铁电性]]、[[../concepts/interlayer-stacking|层间堆垛]]
- [[../entities/CrI3|CrI3]]（强 Ising 铁磁对照）、[[../entities/Fe3GeTe2|Fe3GeTe2]]（金属性铁磁对照）、[[../entities/In2Se3|In2Se3]]（铁电异质结伙伴）、[[../entities/NiI2|NiI2]]（本征 II 型多铁对照）
