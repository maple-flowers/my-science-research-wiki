---
tags: [entity, material, magnetic, 2D, sliding-ferroelectricity, multiferroicity]
category: [D01, Z02]
---

# 碘化铬 / Chromium Triiodide (CrI3)

**CrI3** 是一种典型的二维范德华铁磁绝缘体，也是二维磁性与多铁性研究的里程碑材料。2017 年，CrI3 作为首个被实验证实的单层厚度磁性材料，打破了 Mermin–Wagner 定理在二维各向同性海森堡模型中的限制，证明了各向异性（Ising 型）可以稳定长程磁序。近年来，随“滑移电子学（Slidetronics）”的兴起，CrI3 因其独特的**层间滑动铁电性**以及由此产生的强磁电耦合效应，成为了二维多铁性物理的原型体系。

## 1. 物理机制：从 Ising 磁性到滑动多铁性

在单层极限下，CrI3 表现为具有面外易轴的 Ising 型铁磁体，磁转变温度 $T_C \approx 45\text{ K}$。其磁性源自 Cr$^{3+}$ 离子的 $t_{2g}^3$ 构型，通过 Cr-I-Cr 超交换作用产生铁磁耦合 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

当材料堆叠为双层或多层时，其物理性质表现出极高的对称性依赖：
- **层间磁序稳定性**：双层 CrI3 的层间磁序对堆垛方式极其敏感。实验发现，菱面体堆垛（Rhombohedral, AB）通常对应铁磁层间耦合，而单斜堆垛（Monoclinic, AB'）则倾向于反铁磁耦合。
- **滑动诱导极化**：由于范德华层间作用力较弱，层间相对滑动（Sliding）会打破空间反演对称性。在特定的非中心对称堆叠（如 AB 堆垛的移动变体）中，层间界面的电子云重排而非离子位移产生垂直面外的自发极化 [[../papers/chenStrongSlidingFerroelectricity2024]]。这种起源于纯电子响应的铁电性被称为**滑动铁电性**。

## 2. 磁电耦合与相位锁定 (Phase-Locked Properties)

CrI3 最显著的特征是其铁电极化与磁性序参量的**强耦合锁定**。在双层体系中，极化的翻转（通过层间滑移实现）往往伴随着层间磁序从反铁磁（AFM）到铁磁（FM）的切换。
- **电控磁性**：通过外加垂直电场驱动层间滑动，可以实现磁性的非易失性切换。这种机制规避了传统多铁材料中复杂的畴壁运动，提供了极高响应速度的磁电转换路径。
- **波纹工程 (Ripple Engineering)**：由于二维材料的柔性，CrI3 中普遍存在的本征波纹（Ripples）会引入局域应变场。波纹可以稳定顺电相中的短程铁性序，形成极性纳米微区，从而显著提高铁性相变温度，并改变畴翻转的动力学模式（从协同雪崩式转变为局域随机过程） [[../papers/yangRipplingFerroicPhase2021]]。

## 3. 主要物性参数

| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_C$, 单层)** | $45\text{ K}$ | 铁磁态 |
| **磁易轴** | 垂直面外 | Ising 型磁性 |
| **极化强度 ($P$)** | $\sim 0.1\text{--}0.5\text{ pC/m}$ | 滑动诱导极化 |
| **层间交换能** | $\sim 0.5\text{ meV}$ | 随堆垛构型正负翻转 |
| **材料类别** | 过渡金属卤化物 | 典型范德华层状晶体 |

## 4. 本库相关代表性论文

- [[../papers/kaurRecentAdvancesTheoretical2025a]]：详述 CrI3 作为滑动多铁性原型的理论框架与调控机制。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：对比分析 CrI3 与 HgI2 等碘化物在滑动铁电性上的电子起源差异。
- [[../papers/yangRipplingFerroicPhase2021]]：探讨波纹结构对二维铁性材料（含 CrI3 展望）相变温度的提升作用。
- [[../papers/zhangNonvolatileControlTopological2025]]：研究通过滑动铁电性对 CrI3 相关异质结中拓扑序的非易失控制。

## 5. 关联概念与实体

- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]：核心机制。
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]：CrI3 的物性归属。
- [[../concepts/magnetoelectric-coupling|磁电耦合 Magnetoelectric Coupling]]：极化与磁序的锁定效应。
- [[../entities/NiI2|碘化镍 NiI2]]：本征单层多铁体系（螺旋磁诱导极化）。
- [[../entities/Cr2Ge2Te6|锗碲化铬 Cr2Ge2Te6]]：另一类重要的二维铁磁半导体。
