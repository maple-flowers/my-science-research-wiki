---
tags: [concept, ferroelectrics, magnetism, topological-defects]
title: 畴壁织构 / Domain-Wall Texture
type: concept
status: mature
domain: [ferroelectrics, magnetism, topological-defects, micromagnetic]
mechanism: 畴壁内部序参量（极化/自旋）的空间分布与旋转方式，决定壁的厚度、能量、手性与拓扑性质
related_concepts: [domain-wall, domain-wall-classification, ferroelectric-domain-wall, topological-defects, chirality, flexoelectricity, polarization-switching]
papers: [heUltrafastSwitchingDynamics2024]
updated: 2026-08
---

# 畴壁织构 / Domain-Wall Texture

畴壁织构（domain-wall texture）指**畴壁内部序参量（铁电极化、自旋等）随空间的具体分布与旋转方式**。织构决定了畴壁的厚度、能量密度、手性、导电性与拓扑性质，是理解壁功能与设计壁基器件的核心。铁磁畴壁织构分为 Bloch/Néel 型（自旋旋转平面不同）；铁电畴壁织构则涉及极化沿壁法线（Ising 型）与壁内旋转（Néel 型）的连续谱，并可借挠曲电/梯度效应形成手性织构。

## 👵 太奶导读

太奶啊，"分界线"（畴壁）不是薄薄一层膜，它里面有自己的"内部结构"——箭头怎么转着弯从一边过渡到另一边，是"竖直转"还是"横着转"，壁的厚薄也各不相同。这些内部细节就叫"织构"。织构不同，壁导不导电、稳不稳定、有没有"手性"都不一样。看壁不能只看位置，还得看它里面的"纹路"。

## 🧩 核心内容与机制 (Core Content)

- **铁磁畴壁织构**：Bloch 壁中自旋在壁平面内旋转（体材料常见），Néel 壁中自旋在壁法线平面内旋转（薄膜/界面 DMI 主导时稳定）；自旋旋转方向（手性）由 DMI 决定，壁厚由交换能与各向异性能平衡决定。
- **铁电畴壁织构**：Ising 型壁（极化沿壁法线翻转，存在极化不连续）与 Néel 型壁（极化在壁内连续旋转，无极化的法线分量突变）之间存在连续谱；壁内还可叠加挠曲电驱动的弯曲与旋转织构。
- **手性与拓扑织构**：特定条件下壁内序参量形成手性旋转或局域涡旋状织构，衔接极性涡旋、麦纫等拓扑结构（本库 [[../concepts/topological-defects|拓扑缺陷]]）。
- **与壁功能的关系**：织构决定壁的带电性（Ising 壁的极化法线不连续产生束缚电荷）与导电通道，进而决定壁基器件性能。
- **二维 vdW 铁电**：在双层滑动铁电中，层间相对滑移量决定壁内极化织构，摩尔超晶格可调制壁织构的周期性分布 [[../papers/heUltrafastSwitchingDynamics2024]]。

## 📊 畴壁织构类型

| 织构 | 序参量旋转 | 电荷/磁性特征 | 典型体系 |
|------|------------|----------------|----------|
| Bloch 壁 | 自旋在壁面内 | 无面外分量 | 体铁磁材料 |
| Néel 壁 | 自旋在壁法线面 | 有面外/界面分量 | 磁性薄膜 |
| Ising 铁电壁 | 极化沿壁法线 | 带电（束缚电荷） | BaTiO3、PbTiO3 |
| Néel 铁电壁 | 极化壁内旋转 | 近中性 | 铁电纳米结构 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/domain-wall|畴壁]]：织构的载体。
- [[../concepts/domain-wall-classification|畴壁分类]]：织构的分类维度。
- [[../concepts/ferroelectric-domain-wall|铁电畴壁]]：铁电织构体系。
- [[../concepts/topological-defects|拓扑缺陷]]：织构的拓扑延伸。
- [[../concepts/chirality|手性]]：壁内旋转手性。
- [[../concepts/flexoelectricity|挠曲电效应]]：壁内弯曲织构来源。
- [[../concepts/polarization-switching|极化翻转]]：织构演化的过程。

## 📚 相关论文 (Related Papers)

- [[../papers/heUltrafastSwitchingDynamics2024]]：vdW 双层铁电中壁内极化织构与超快开关动力学的关联。

## 🏷️ 专业名词别名

- `domain-wall-structure`（concepts）
- `壁内序参量分布`（concepts）
