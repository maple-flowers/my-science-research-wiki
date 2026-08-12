---
tags: [entity, material, ferroelectric, 2D, semimetal, multiferroic]
category: [D02, Z01]
---

# 二碲化钼 / Molybdenum Ditelluride (MoTe2)

**MoTe2** 是一种展现出丰富物理特性的过渡金属硫族化物 (TMD)。它不仅是研究**滑动铁电性**和**铁电金属**的原型体系，还通过磁性原子替代实现了二维磁电耦合。

## 1. 结构相与滑动铁电性
- **晶体结构**：MoTe2 具有多种同质异形体，包括 $2H$（半导体）、$1T'$（半金属）和 $T_d$（外尔半金属）相。1T′ 与 2H 两相能量差在 TMD 中最小，约 0.3% 的拉伸应变即可诱导相变，是应变相变器件的核心沟道材料 [[../papers/houStrainbasedRoomtemperatureNonvolatile2019]]。
- **滑动铁电机制**：在双层或少层 $3R$ 堆垛的 MoTe2 中，通过层间的微小滑移打破了空间反演对称性，诱导出稳健的面外自发极化。这种**滑动铁电性**具有极低的翻转能垒（$\sim 1\text{ meV/f.u.}$），是开发超低功耗存储器件的理想机制 [[../papers/kaurRecentAdvancesTheoretical2025a]]。
- **铁电金属态**：在 $T_d$ 相的薄层 MoTe2 中，极化电荷与金属态载流子共存，展现出反常的铁电金属特性 [[../papers/FerroelectricityMultiferroicityAtomic2023]]。

## 2. 磁电与拓扑物理
- **磁性诱导**：通过掺杂或构建异质结，MoTe2 可以从单纯的铁电体转变为多铁材料。
- **层极化自旋霍尔效应 (LP-SHE)**：在极性双层 MoTe2 中，Berry 曲率使得自旋积累被局域在特定的层内，且该效应可以通过层间滑动进行有效切换 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **转变温度 ($T_C$)** | 室温稳定 | 滑动铁电态 |
| **极化强度 ($P$)** | $\sim 0.1\text{--}0.5\text{ pC/m}$ | 滑动诱导极化 |
| **能带结构** | 半金属 / 半导体 | 取决于相 (Td / 2H) |
| **翻转能垒** | $\sim 0.6\text{--}1.0\text{ meV}$ | 极低翻转能耗 |

## 4. 本库相关代表性论文
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：综述 MoTe2 在原子级厚度下的铁电金属与尺寸效应。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：详述 MoTe2 双层中的滑动铁电机制及层极化自旋效应。
- [[../papers/houStrainbasedRoomtemperatureNonvolatile2019]]：应变诱导室温非易失 2H/1T′ 相变。

## 5. 关联概念与实体
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../entities/WTe2|二碲化钨 WTe2]] (同族铁电金属)
- [[../entities/MoS2|二硫化钼 MoS2]] (同族半导体)
- [[../entities/TMDs|TMDs]] (上位材料家族)
