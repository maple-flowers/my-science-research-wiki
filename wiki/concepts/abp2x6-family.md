---
tags: [concept]
---

# ABP2X6 家族 (ABP2X6 Family)

ABP2X6 家族是一类具有低对称性的层状范德华材料，属于过渡金属磷三硫/硒化物（TMTPs）的一个重要分支。其化学通式为 A¹⁺B³⁺P₂X₆（A = Cu, Ag; B = Cr, V, In, Sc; X = S, Se）。该家族在二维极限下展现出丰富的铁电性、铁磁性以及复杂的相竞争行为，是研究二维多铁性与磁电耦合的理想平台 [[../papers/neumayerCompetingPolarPhases2025]]。

## 晶体结构与极性起源
ABP2X6 家族的结构特征是由 [P₂X₆]⁴⁻ 单元构成的骨架，金属阳离子 A 和 B 填充在由 X 原子形成的八面体间隙中。与高对称性的 MPX₃ 体系（如 MnPS₃, P31m）不同，ABP2X6 由于 A 和 B 位原子的占据规律及位移，通常表现出更低的对称性（如 monoclinic $Cc$ 或 triclinic $P1$） [[../papers/laiTwodimensionalFerromagnetismDriven2019]]。

其铁电性的起源具有多样性：
1. **离子位移机制**：以 [[../concepts/cips-cu-in-p2s6]] (CIPS) 和 [[../entities/cu-crp2s6]] (CCPS) 为代表，极化主要来源于 A 位阳离子（如 Cu⁺）沿 c 轴向范德华间隙的偏心位移。
2. **原子翘曲机制**：在 Sc₂P₂Se₆ 等体系中，极化来源于 P₂ 单元相对于 Se 平面的垂直翘曲，这种机制不依赖于传统的 $d^0$ 规则 [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]。

## 相锁定的物理特性 (Phase-Locked Properties)
该家族材料往往展现出自旋、电荷与晶格自由度的高度耦合，表现为以下“相位锁定”特征：
- **自旋-电偶极-谷锁定**：在强自旋轨道耦合 (SOC) 介导下，CCPS 等材料的铁电极化 (P)、磁矩 (S) 与能带谷 (Valley) 相互锁定。翻转电极化方向可以诱导塞曼型谷劈裂的反转，并同步翻转单向磁晶各向异性的易磁化轴，从而实现电场对磁矩的调控 [[../papers/laiTwodimensionalFerromagnetismDriven2019]]。
- **自旋-晶格-电荷耦合**：在 ScCrP₂Se₆ 体系中，铁电 (FE) 相与反铁电 (AFE) 相的切换会引起显著的晶格畸变，进而调制 Cr–Se–Se–Cr 路径间的间接超交换作用，实现铁磁 (FM) 与反铁磁 (AFM) 态的电控切换 [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]。

## 驱动铁电性与相竞争
ABP2X6 家族的一个显著特点是存在多种能量极其接近的极性相（FE, AFE, PE）。
- **驱动铁电性 (Driven Ferroelectricity)**：许多成员（如 CCPS）的基态为 AFE 相，但亚稳的 FE 相与基态能量差仅几十 meV/f.u.。通过外部偏压驱动阳离子跨越势垒进入范德华间隙位（in-gap FE 相），可以实现非易失的电极化翻转 [[../papers/neumayerCompetingPolarPhases2025]]。
- **层数依赖性**：磁性往往表现出从块体层间 AFM 到少层层内 FM 的转变，而铁电性则因范德华间隙的柔性而在原子级厚度下保持稳定 [[../papers/laiTwodimensionalFerromagnetismDriven2019]]。

## 代表性成员与物性
| 材料 | 极性起源 | 磁性 | 关键特性 |
| :--- | :--- | :--- | :--- |
| [[../entities/cu-crp2s6]] | Cu⁺ 位移 | FM (少层) | I 型多铁、三重锁定机制 |
| [[../concepts/cips-cu-in-p2s6]] | Cu⁺ 位移 | 无 | 负压电性、离子导电耦合 |
| [[../concepts/cipse-cu-in-p2se6]] | Cu⁺ 位移 | 无 | FE/AFE 畴壁压电增强 |
| AgVP₂Se₆ | Ag⁺ 位移 | FM | 预测的面内极化多铁体 |
| ScCrP₂Se₆ | P 翘曲 | FM/AFM | 电场驱动磁序切换 |

## Related Papers

- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]
- [[../papers/neumayerCompetingPolarPhases2025]]
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]
