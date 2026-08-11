---
tags: [entity, material, magnetic, 2D, multiferroic]
category: [D01, Z02]
---

# 锗碲化铬 / Chromium Germanium Telluride (Cr2Ge2Te6)

**Cr2Ge2Te6 (CGT)** 是一种典型的二维范德华铁磁半导体。它是研究低维极限下长程磁有序、二维磁性与电学性质耦合的重要原型材料。

## 1. 二维铁磁性
- **磁序特性**：CGT 是首批在原子级厚度下被实验证实具有稳健铁磁序的材料之一。在块体中，其磁转变温度 $T_C \approx 61\text{ K}$。
- **各项异性**：CGT 具有面外磁易轴（Ising 型），其磁有序受到本征磁各向异性的保护，从而绕过了 Mermin-Wagner 定理的限制。

## 2. 人工多铁异质结 (Artificial Multiferroic Heterostructures)
由于 CGT 本身不具铁电性，研究者常利用它构建异质结来实现功能调控：
- **CGT/In2Se3 异质结**：理论预言，将铁磁 CGT 与具有滑动铁电性的 [[In2Se3|In2Se3]] 堆叠，可以诱导出强烈的非易失性磁电耦合。通过翻转 In2Se3 的电极化，可以有效调控 CGT 的磁各向异性或交换作用强度 [[../papers/FerroelectricityMultiferroicityAtomic2023]]。
- **磁电调控**：这种人工多铁体系为开发超低功耗、全电学控制的磁随机存储器 (MRAM) 提供了新思路 [[../papers/tangMultiferroicityTwodimensionalVan2025]]。

## 3. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **磁转变温度 ($T_C$)** | $\sim 61\text{ K}$ (Bulk) | 随层数减小而降低 |
| **磁易轴** | 垂直面外 | Ising 型磁性 |
| **带隙 ($E_g$)** | $\sim 0.7\text{ eV}$ | 窄禁带半导体 |
| **材料类别** | 金属硫代磷酸盐衍生物 | 范德华磁性半导体 |

## 4. 本库相关代表性论文
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：讨论 CGT 异质结中的二维磁电耦合效应。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：探讨 CGT 在范德华多铁器件中的应用。

## 5. 关联概念与实体
- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../concepts/2D-materials|二维材料 2D Materials]]
- [[../entities/CrI3|碘化铬 CrI3]] (对比铁磁体系)
- [[../entities/In2Se3|硒化铟 In2Se3]] (构建多铁异质结)
- [[../entities/Fe3GeTe2|Fe3GeTe2]] (金属性铁磁体)
