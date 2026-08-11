---
tags: [entity, calculation-method, dft]
---

# Elk (All-Electron Full-Potential LAPW Code)

Elk 是一款基于全电子全势线性化增强平面波（All-Electron Full-Potential Linearized Augmented Plane Wave, LAPW）方法的高精度第一性原理计算代码。与 VASP 等基于赝势的计算工具不同，Elk 将内核电子与价电子置于同等地位处理，能够提供原子核附近晶格势场的精确描述。这种物理上的严谨性使其在捕捉复杂体系中的“相位锁定特性”（Phase-Locked Properties）方面具有独特优势，特别是在电子电荷分布与底层非共线磁序高度耦合的多铁性材料研究中。

## 在多铁性研究中的相位锁定验证

在针对单层 NiI₂ 的研究中 [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]]，Elk 展现了其验证微观多铁性起源的关键能力。该代码对完全非共线磁性（Non-collinear Magnetism）与强自旋-轨道耦合（SOC）的原生支持，使研究者能够模拟波矢为 $q$ 的自旋螺旋（Spin-spiral）磁序。Elk 的计算结果证实了这种磁性“相位”会诱导相应的局域静电势调制：涌现的铁电极化 $P$ 与磁螺旋磁序满足半周期锁定关系（即极化周期为磁螺旋周期的一半，$L_P = L_M / 2$）。这种相位锁定机制在模拟的扫描隧道显微镜（STM）图像中直接体现为周期性的条纹图案。

## 技术特性与应用范式

Elk 的全势处理方式对于定量估算“能带弯曲”（Band Bending）至关重要。能带弯曲是由局域电偶极子诱导的电子能带边缘在空间上的能量偏移。在单层 NiI₂ 的案例中，Elk 采用 LDA 交换关联泛函和 $9a \times \sqrt{3}a$ 的公度超胞来承载螺旋磁序。尽管 LDA 泛函通常会低估绝对带隙，但 Elk 的精确势场计算成功捕捉到了定性的能量偏移（理论值 5.0 meV 与实验值 16.8 meV 在数量级和物理图像上吻合），证明了实验观测到的 STM 条纹本质上是磁电耦合诱导的势场景观。

除了 NiI₂ 体系，Elk 常被作为研究拓扑、磁性与铁电性交织体系的基准工具。其处理大型非共线超胞时无需引入原子球近似或赝势近似的特性，使其成为验证关联电子体系中“相位锁定”诱导涌现现象的标准手段。

## 关联论文

- [[../papers/aminiAtomicscaleVisualizationMultiferroicity2024]] — 展示了 Elk 在模拟单层 NiI₂ 非共线磁序诱导静电势调制中的核心作用。
