---
tags: [entity]
---

# 二碲化钒 (VTe2)

二碲化钒（Vanadium Ditelluride, VTe₂）是过渡金属二硫族化物（[[TMDs]]）家族中具有高度相竞争和丰富电荷密度波（CDW）特性的金属性成员。其物理性质对层数（维度效应）和衬底环境极其敏感。

## 晶体结构与相变

VTe₂ 存在多种结构相，核心在于钒原子与碲原子的配位方式及由此产生的晶格畸变：

### 1. 1T 相与 1T' 相 (体相/单层)
- **1T 相 (Hexagonal)**：具有八面体配位（空间群 $P\bar{3}m1$）。块体 VTe₂ 在高温下处于此相。
- **1T' 相 (Monoclinic)**：当温度降至约 480 K 以下，1T 相发生结构失稳，V 原子位移形成**双锯齿链 (Double zigzag chains)**，呈现 (3×1) CDW 畸变。
- **单层限制**：在单层极限下，层间 Te-Te 耦合消失。实验证实在 HOPG 衬底上生长的单层 VTe₂ 倾向于保持 **1T 相**，但其低温 CDW 序演变为 **(4×4)** 对称性，这与块体行为显著不同，揭示了维度对 CDW 不稳定性的显著调控作用 [[../papers/wongEvidenceMetallic1T]]。

### 2. PP 相 (褶皱五边形相)
- **结构特征**：理论预测的全新二维相，源自黄铁矿 (Pyrite) 结构的 (100) 面。由两个化学键合的五边形子层构成，具有面内各向异性。
- **物性突变**：与金属性的 1T/1T' 相不同，单层 **PP-VTe₂** 被预测为窄带隙（~0.33 eV）的**本征铁磁半导体** [[../papers/liMonolayerPuckeredPentagonal2022]]。

## 关键物理特性

### 相锁定的电荷密度波 (CDW)
- **多形态性**：1T-VTe₂ 是 CDW 多形态性最丰富的 TMD 之一。DFPT 计算表明其在 $\Gamma$-$M$ 和 $\Gamma$-$K$ 路径上存在多个声子软模（虚频），分别对应 (4×1)、(3×√3) 和 (√21×√3) 等失稳模式 [[../papers/lezoualchStudyChargeDensity]]。
- **相切换**：通过 STM 针尖脉冲可在 (4×4) 与 (4×1) CDW 相之间实现原子级的可逆切换 [[../papers/lezoualchStudyChargeDensity]]。

### 磁性争议与裁决
- **铁磁性判准**：早期理论预测单层 1T-VTe₂ 具有本征铁磁性，但利用元素特异性 **XMCD** 测量的结果在实验误差范围内为零，排除了本征磁有序。磁性信号的缺失可能归因于 CDW 不稳定性与磁性基态的竞争抑制 [[../papers/wongEvidenceMetallic1T]]。
- **多铁性耦合**：在预测的 [[../concepts/PP-VTe2|PP-VTe2]] 相中，存在铁弹翻转驱动易磁化轴旋转 90° 的**直接多铁性耦合**，允许通过机械应变或电场调控磁序 [[../papers/liMonolayerPuckeredPentagonal2022]]。

## 研究方法与表征
- **生长**：主要采用分子束外延 MBE 在 HOPG 或石墨烯衬底上制备。
- **结构确认**：STM/STS (实空间 CDW 序)、ARPES (能带结构与费米面)。
- **化学态**：PES/XPS 确认 V⁴⁺ (3d¹) 电子构型。

## Related Papers

- [[../papers/wongEvidenceMetallic1T]] — 确证单层 1T 相及其 (4×4) CDW，排除铁磁性。
- [[../papers/lezoualchStudyChargeDensity]] — 基于 DFPT 的 CDW 建模及 STM 诱导相切换研究。
- [[../papers/liMonolayerPuckeredPentagonal2022]] — 预测 PP-VTe₂ 的铁磁半导体性与多铁耦合。
