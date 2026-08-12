---
tags: [entity, material, ferroelectric, 2D, strain-engineering, topological-defect]
category: [D01, Z02]
---

# 碲化铅 / Lead Telluride (PbTe)

**碲化铅 (PbTe)** 是一种典型的 IV-VI 族半导体。在二维极限下，单层 PbTe 展现出极高的力学柔韧性与应变调控潜力，是研究应变诱导相变与极性拓扑缺陷的理想平台 [[../papers/xuTunableFerroelectricTopological2022]]。

## 1. 应变诱导的顺电-铁电相变
与本征铁电的 SnS 不同，单层 PbTe 的基态是具有反演对称性的 **Cmcm 顺电相**。
- **软模机制**：施加应变会导致布里渊区中心（$\Gamma$ 点）的横向光学（TO）声子模软化，驱动体系向褶皱结构的 **Pnma 铁电相** 转变。
- **相变阈值**：临界应变约为 **$3.5\%$** (拉伸) 或 **$3.6\%$** (剪切)。
- **巨压电效应**：在相变临界点附近，压电系数 $e_{11}$ 会出现量级上的爆发，峰值可达 **$140 \times 10^{-10}\text{ C/m}$**。

## 2. 波纹工程与稳定性
在自由悬浮或柔性衬底上的单层 PbTe 中，波纹 (Ripple) 结构对铁性有序具有显著的稳定作用 [[../papers/yangRipplingFerroicPhase2021]]：
- **极性纳米区域 (PNRs)**：波纹产生的非均匀应变场会优先诱导产生局域极化，形成稳定的极性纳米区域。
- **相变特征**：波纹使相变过程从“雪崩式”协同翻转转变为受局部应力调控的独立翻转，从而提高有效的铁电居里温度。

## 3. 极性拓扑缺陷设计
利用非均匀应变场，可以在 PbTe 表面实现复杂的极性拓扑图案 [[../papers/xuTunableFerroelectricTopological2022]]：
| 拓扑类型 | 诱导手段 | 特征 |
| :--- | :--- | :--- |
| **涡旋 (Vortex)** | 纳米机械压痕 | 极化矢量呈中心发散/收敛排列 |
| **反涡旋 (Anti-vortex)** | 圆形/正方形孔洞衬底鼓泡 | 极化矢量呈现“马鞍点”分布 |
| **通量闭合 (Flux-closure)** | 45° 旋转方形孔洞衬底压力 | 极化方向首尾相连形成闭合回路 |

## 4. 主要物性参数
| 参数名称 | 数值 | 备注 |
| :--- | :--- | :--- |
| **基态相** | Cmcm | 顺电相 |
| **临界应变** | $\sim 3.5\%$ | 触发顺电-铁电相变 |
| **最大压电系数** | $\sim 140 \times 10^{-10}\text{ C/m}$ | 临界点附近的巨响应 |
| **材料类别** | IV-VI 族半导体 | 全应变调控体系 |

## 5. 本库相关代表性论文
- [[../papers/xuTunableFerroelectricTopological2022]]：npj 2D Mater. Appl. 2022，论证 PbX 应变铁电性与拓扑缺陷设计。
- [[../papers/yangRipplingFerroicPhase2021]]：Nature Commun. 2021，揭示波纹结构对二维铁性的稳定化机制。

## 6. 关联概念
- [[../concepts/topological-defects|拓扑缺陷 Topological Defects]]
- [[../concepts/soft-mode|软模理论 Soft-mode Theory]]
- [[../concepts/strain-engineering|应变工程 Strain Engineering]]
- [[../concepts/ripple-engineering|波纹工程 Ripple Engineering]]
