---
tags: [concept, sliding-ferroelectricity, ferroelectricity, interlayer-coupling, charge-transfer, 2d-materials]
title: interfacial-charge-rearrangement
type: concept
status: developing
year: 2024
papers: [chenStrongSlidingFerroelectricity2024, guoAdvancesTwodimensionalFerroelectric2025]
updated: 2026-08-21
---

# interfacial-charge-rearrangement

**界面电荷重排（interfacial charge rearrangement）**，亦称层间电荷重分布，指范德华双层/多层中电子在**层间界面处**重新分布、形成净偶极的过程。它是[[../concepts/sliding-ferroelectricity|滑移铁电]]极化的**真正来源**——这一点颠覆了传统铁电体的离子位移图像。

## 👵 太奶导读

乖孙，传统铁电体是怎么产生极化的？**靠原子挪位置。** 比如钛酸钡里，钛离子从氧八面体正中央偏出去一点，正负电荷中心分开，就有了电偶极。整个理论都建在「离子位移」上。

滑移铁电不是这样。它的两层材料**各自都是不极化的**，把它们错开一点堆起来（滑移），上下对称性一破，电子就在**两层之间的那个夹缝里**重新分配——一侧堆积、一侧亏空，夹缝里凭空出现一个偶极。

**原子几乎没挪，是电子挪了。**

这里有个证据特别硬，太奶要你记住：在双层 HgI₂ 里，Hg 离子相对八面体中心确实有位移，但这个位移的**方向跟总极化是反的**。也就是说，如果按传统的离子位移图像去算，你会得到一个方向错误的答案。离子位移在这里不但不是主因，还是个**干扰项**。

记一句话：**滑移铁电的极化住在层间界面的电子重排里，不在离子位移里；HgI₂ 中离子位移方向甚至与总极化相反。**

## 🧩 机制与判据

- **成因链**：层间滑移改变堆垛方式 → 破坏空间反演对称性 → 电子在层间界面处重新分布（一侧积累、一侧耗尽）→ 形成净面外偶极。
- **诊断手段**：
  - **差分电荷密度**：铁电（FE）双层的层间区域出现净电荷重排，积累区与耗尽区构成偶极，其方向与总极化**平行**；顺电（PE）双层的电荷分布对称、无偶极。
  - **平面平均屏蔽电荷分析**：用于定量提取极化值。
  - **原子柱电荷量变化**：如 Td-WTe₂ 中通过追踪四个 Te 原子柱的电荷量变化来量化层间转移。
- **与离子位移的分离判据**：比较离子位移方向与总极化方向。若两者**反向**（如双层 HgI₂ 中的 d_Hg），即可判定极化并非离子位移主导。

### 双层 HgI₂ 的定量证据

| 量 | 数值 | 性质 |
|---|---|---|
| 双层 HgI₂ 极化 | 0.11 μC/cm² | 计算预测 |
| 翻转能垒 | 24.65 meV/f.u. | 计算预测 |
| Hg 位移 d_Hg 的方向 | **与总极化相反** | 计算预测 |

⚠️ **边界**：全为第一性原理计算值，来自单一论文。极化值 0.11 μC/cm² 之所以偏小，与二维减薄后退极化场抑制导致极化下降有关——这与「能垒降低、变得可翻转」是同一取舍的两面（体相 HgX₂ 虽有更大极化，却因能垒过高而不可翻转）。

## 📚 相关论文 (Related Papers)

- [[../papers/chenStrongSlidingFerroelectricity2024]]：本页最关键的证据来源。该文用差分电荷密度证实 FE 双层层间存在净电荷重排、PE 双层则对称无偶极，用平面平均屏蔽电荷定量出 0.11 μC/cm² 与 24.65 meV/f.u. 的翻转能垒，并给出本页判据的决定性一条——**Hg 离子位移方向与总极化相反**，据此判定层间界面电荷重排（而非离子位移）是极化主要贡献者。
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]：作为综述把「层间电荷重分布」确立为滑移铁电的**范式性机制**，明确指出它「完全颠覆了传统铁电体的离子位移模型」，并给出该机制在 hBN、TMDs、双层石墨烯等多个体系中的通用表述与量化手段（如 Td-WTe₂ 的四个 Te 原子柱电荷追踪、垂直电场下双层石墨烯的层间电荷转移模型），为本页提供了超出单一体系的适用范围依据。

## 🔗 关联概念与实体 (Related)

- [[../concepts/sliding-ferroelectricity|sliding-ferroelectricity]]
- [[../concepts/ferroelectricity|ferroelectricity]]
- [[../concepts/depolarization-field|depolarization-field]]
- [[../concepts/interlayer-coupling|interlayer-coupling]]
- [[../concepts/inversion-symmetry-breaking|inversion-symmetry-breaking]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/rashba-effect|rashba-effect]]
- [[../entities/HgI2|HgI2]]
