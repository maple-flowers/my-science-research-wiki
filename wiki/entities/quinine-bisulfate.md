---
tags: [entity]
---

# Quinine Bisulfate (硫酸氢奎宁)

Quinine Bisulfate 是一种经典的荧光参比标准物，在光物理研究中广泛用于校准分子的荧光量子产率（$\Phi$）。在科研 Wiki 的语境下，它主要作为 [[../concepts/two-photon-fluorescence]] 探针表征中的核心参照。

## 核心属性 (Phase-Locked Properties)

在 [[../papers/Huang2019solvatochromic]] 的研究体系中，Quinine Bisulfate 被锁定为光物理测量的"绝对锚点"：

- **量子产率锁定 (Φ-Standard Locking)**：
  - 在 0.05 M H₂SO₄ 水溶液中，其荧光量子产率被严格定义为 **0.546**。
  - **证据链**：该数值作为基准，直接决定了新型 D-$\pi$-A 型探针 P1/P2 在不同溶剂（从环己烷到 DMSO）中量子产率计算的准确性。
- **酸度环境约束 (Condition Sensitivity)**：
  - 其荧光性能高度依赖于溶剂酸度。标准测量程序规定必须使用 **0.05 M H₂SO₄**，以确保参比值的稳定性和可重复性。
- **校准链条 (Calibration Chain)**：
  - 与 [[fluorescein]]（双光子吸收截面参比）共同构成了双光子激发荧光（TPEF）表征的完整基准体系。

## 技术应用 (Technical Application)

- **荧光量子产率测量**：
  - 采用相对测量法。通过比较待测样品的发射积分强度与 Quinine Bisulfate 参比溶液的积分强度（经折射率校正），计算样品的 $\Phi$ 值。
  - 在 P1 探针的研究中，通过该参比揭示了溶剂极性增强导致 [[../concepts/twisted-intramolecular-charge-transfer]]（TICT）通道激活，从而使 $\Phi$ 从 0.805 骤降至 0.066 的演变过程。

## 相关论文 (Two-Layer Architecture)

- [[../papers/Huang2019solvatochromic]]：在该工作中，Quinine Bisulfate 用于标定二苯乙烯基双光子探针的光物理常数。
- [[../papers/Huang2023two]]：进一步应用该参比体系探讨了双氰基二苯乙烯探针的三重荧光特性。

## 关联项

- **概念**：[[../concepts/fluorescence-quantum-yield]] (荧光量子产率), [[../concepts/two-photon-fluorescence]] (双光子荧光)
- **参比物**：[[fluorescein]] (荧光素)
- **探针实体**：[[P1-probe]], [[P2-probe]]
