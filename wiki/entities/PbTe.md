---
tags: [entity, material, ferroelectric, 2D, strain-engineering, topological-defect]
category: [D01, Z02]
---

# 碲化铅 / Lead Telluride (PbTe)

**碲化铅 (PbTe)** 是一种典型的 IV-VI 族半导体，其块体常温下具有面心立方（NaCl型）结构。在二维极限下，单层 PbTe 被预测具有极高的力学柔韧性与应变调控潜力。通过**应变工程（Strain Engineering）**，单层 PbTe 可以实现从对称的顺电相（Paraelectric, PE）到非对称铁电相（Ferroelectric, FE）的可逆转变，并涌现出涡旋（Vortex）、反涡旋（Anti-vortex）等复杂的极性拓扑缺陷结构（[[../../raw/note/xuTunableFerroelectricTopological2022|Xu et al. 2022]]）。

## 核心物理特性

### 1. 应变诱导的顺电-铁电相变
与本征具有铁电性的 SnS 或 GeSe 不同，单层 PbTe 的基态是具有反演对称性的 **Cmcm 顺电相**。
- **相变机制**：施加机械应变会打破晶格对称性，导致布里渊区中心（$\Gamma$ 点）的横向光学（TO）声子模软化（虚频出现），驱动体系向褶皱（Puckered）结构的 **Pnma 铁电相** 转变。
- **临界阈值**：
    - **拉伸应变**：$\sim$3.5%
    - **剪切应变**：$\sim$3.6%
- **巨压电效应**：在相变临界点附近，由于结构极度不稳定，压电系数（$e_{11}$）会出现量级上的爆发（峰值可达 $\sim$140 $\times 10^{-10}$ C/m），远超普通二维材料。

### 2. 波纹（Ripple）对铁性的稳定作用
在自由悬浮或柔性衬底上的单层 PbTe 中，由于热起伏或衬底相互作用，常存在波纹结构：
- **ZA 模驱动**：波纹主要受弯曲模式（ZA mode）控制。
- **极性纳米区域（PNRs）**：波纹的波峰与波谷处会形成局域的非均匀应变场，优先诱导产生铁电极化，形成稳定的极性纳米区域。
- **相变特征**：波纹的存在使得相变过程从“雪崩式”协同翻转（幂律分布）转变为受局部应力调控的独立翻转（高斯分布），从而显著提高其铁电居里温度 $T_c$（[[../../raw/note/yangRipplingFerroicPhase2021|Yang et al. 2021]]）。

## 极性拓扑缺陷设计

利用非均匀应变场，可以在 PbTe 表面“编写”特定的极性拓扑图案（[[../../raw/note/xuTunableFerroelectricTopological2022|Xu et al. 2022]]）：

| 拓扑类型 | 诱导手段 | 特征 |
| :--- | :--- | :--- |
| **涡旋 (Vortex)** | 纳米机械压痕 (Indentation) | 中心发散的极化排列，由 90° 畴壁连接四个象限。 |
| **反涡旋 (Anti-vortex)** | 圆形/正方形孔洞衬底上的压力鼓泡 | 极化矢量呈现“马鞍点”分布，形态受孔洞几何形状调制（立方或圆形）。 |
| **通量闭合 (Flux-closure)** | 45° 旋转的方形孔洞衬底压力 | 极化方向首尾相连形成闭合回路，总净偶极矩为零。 |

## 应用前景
- **非易失性存储器**：利用拓扑保护的极化态（如涡旋）作为比特单元，实现高密度、超快读写的拓扑铁电存储。
- **高灵敏度传感器**：利用相变临界点附近的巨压电响应探测微小应力或震动。
- **柔性电子学**：PbTe 的全应变调控特性使其成为柔性、可拉伸纳米器件的理想平台。

## 本库相关论文
- [[../../raw/note/xuTunableFerroelectricTopological2022]]：系统论证了多尺度模拟下的 PbX 应变铁电性与拓扑缺陷设计。
- [[../../raw/note/yangRipplingFerroicPhase2021]]：揭示了波纹结构对 2D 铁性的稳定化机制。

## 关联概念
- [[../concepts/topological-defects|拓扑缺陷 Topological Defects]]
- [[../concepts/soft-mode|软模理论 Soft-mode Theory]]
- [[../concepts/strain-engineering|应变工程 Strain Engineering]]
- [[../concepts/ripple-engineering|波纹工程 Ripple Engineering]]
- [[../entities/PbX-family|PbX 家族 PbX Family]]
