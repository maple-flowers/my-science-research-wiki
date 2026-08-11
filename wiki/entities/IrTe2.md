---
tags: [entity]
---

# 实体：二碲化铱 (IrTe2)

**二碲化铱 (IrTe2)** 是一种具有高度复杂相变行为的 1T 结构层状过渡金属二硫族化合物 (TMDs)。它在量子材料研究中占据特殊地位，不仅因为其被预测为 **II 型体狄拉克半金属 (Type-II Bulk Dirac Semimetal)**，更由于其展现出强烈的电子-晶格耦合，导致其低温下存在多个能量近乎简并的电荷有序相。

## 1. 相锁定特性与结构二聚化

IrTe2 的核心物理魅力在于其 **相锁定特性 (Phase-locked properties)**：晶格畸变（Ir 二聚化）、电荷密度分布（电荷有序）与拓扑电子能带之间存在深度的内在绑定。在高温（$T > 280\text{ K}$）下，材料维持对称性较高的 $1 \times 1$ 三方相；随着温度降低，它会经历一系列一级相变，分别在 280 K 和 180 K 形成 $5 \times 1 \times 5$ 和 $8 \times 1 \times 8$ 调制结构。

这些相变的微观驱动力源于 **Ir 二聚化 (Ir Dimerization)**，即 Ir 原子之间通过成键（或更准确地说是多中心键）来获取电子能量增益。不同的低温相对应于二聚体排列的不同密度与周期。特别地，$6 \times 1$ 相被认为是该体系隐藏的结构基态，其二聚体密度达到最大（每 6 个 Ir 原子中有 4 个参与二聚化）。然而，由于不同相之间的能量壁垒极低（~meV 级），在块材中这些相往往以纳米级畴的形式共存，导致其真正的基态特性长期难以被独立观测 [[../papers/nicholsonUniaxialStraininducedPhase2021]]。

## 2. 应变诱导的相选择与层间解聚

利用应变工程可以打破这种相竞争的平衡。实验证明，沿高温相 a 轴施加仅约 **0.1% 的单轴拉伸应变**，即可在宏观尺度（~mm 级）上选择性地稳定单一的 **$6 \times 1$ 电荷有序相**。

这一过程的微观机制被称为 **应变诱导的电荷转移 (Strain-induced charge transfer)**。单轴应变促使电子从 Ir 4f 轨道转移至 Te 5p 轨道，填充了层间 Te–Te 键的反键态。这一电子占据的变化引发了 **层间解聚 (Interlayer depolymerization)**：原本维持层间耦合的弱共价 Te–Te 键发生断裂，导致层间跳跃能 (Interlayer hopping) 从高温相的 ~0.156 eV 骤降至 ~0.014 eV。这种近十倍的降幅使得 IrTe2 的电子结构从三维显著向准二维渡越，从而降低了体系能量并稳定了二聚体密度最高的 $6 \times 1$ 基态 [[../papers/nicholsonUniaxialStraininducedPhase2021]]。

## 3. 拓扑 Lifshitz 转变与电子态演化

应变不仅调控了结构，还通过能带演化改变了材料的拓扑本征属性。在应变稳定的 $6 \times 1$ 相中，电荷转移导致源自 Te $5p_z$ 轨道的 **II 型体狄拉克点** 显著下移约 350 meV。

这种能带的移动触发了 **利夫希茨相变 (Lifshitz Transition)**，即在不改变晶格对称性的前提下，费米面的拓扑结构发生突变。ARPES 观测证实，随着狄拉克点移至费米能级以下，电子型口袋开始主导费米面。这一发现具有重要的器件应用前景：由于狄拉克态是层间输运的主要通道，通过微小的单轴应变即可实现对 IrTe2 拓扑输运特性的各向异性调控，为设计基于拓扑半金属的各向异性电子开关开辟了路径 [[../papers/nicholsonUniaxialStraininducedPhase2021]]。

## Related Papers

- [[../papers/nicholsonUniaxialStraininducedPhase2021]] — *Uniaxial strain-induced phase transition in the 2D topological semimetal IrTe2*
