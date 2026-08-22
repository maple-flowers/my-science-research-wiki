---
tags: [concept, charge-density-wave, structural-distortion, dimerization, magnetism, order-parameter]
title: structural-distortion-index
type: concept
status: developing
year: 2022
papers: [chenFerromagneticNonmagnetic1T2022]
updated: 2026-08-21
---

# structural-distortion-index

**结构畸变指数（structural distortion index）** 在本库中特指 1T′ 相过渡金属硫族化合物里的比值 **d₁/d₂**——相邻两列金属原子沿 y 方向的两个 M–M 间距之比。它把「畸变有多重」压缩成一个可比较的数，并且被证明**与磁性状态直接相关**。

⚠️ 这是一个**体系专属**的定义，不是通用的晶体学畸变度量，见下方边界。

## 👵 太奶导读

乖孙，TMD 材料有个高对称的 1T 相，金属原子排得整整齐齐、间距都相等。但它常常会自己「塌」成低对称的 1T′ 相：相邻两列金属原子不再等距，一会儿挨得近、一会儿离得远，出现 d₁ 和 d₂ 两种间距。

**把这两个间距一除，d₁/d₂，就是畸变指数。**

- 等于 1 → 完全没畸变（就是 1T 相）。
- 越小 → 畸变越重，两列原子一近一远分得越开。

**它妙在哪儿？** 妙在这个纯粹的**结构**数字，能告诉你材料的**磁性**：

在 CrX₂ 家族里，d₁/d₂ ≈ **0.8** 的 1T′ 相是**铁磁**的；d₁/d₂ ≈ **0.7** 的是**非磁**的。畸变轻一点，磁性留住了；畸变重一点，磁性没了。

**为什么会这样？** 因为畸变的本质是相邻金属原子**两两配对（二聚化）**。配对时两个原子各出一个电子把键结成，这些电子就被「锁」进键里、不再贡献磁矩。所以配得越紧（d₁/d₂ 越小），磁性被吃掉得越多。Mn 的情况有意思：它 d 电子多，即使二聚化了也没被吃干净，所以还能保留铁磁性。

记一句话：**d₁/d₂ 越小表示金属原子配对越紧、磁矩被吃掉越多；CrX₂ 里 0.8 对应铁磁、0.7 对应非磁。**

## 🧩 定义与判据

- **定义**：1T 相为高对称相（空间群 P3̄m1 一类，菱面体原胞），相邻金属列间距相等。1T′ 相中沿 y 方向相邻两列的 M–M 距离不等（d₁ < d₂），定义 **d₁/d₂ < 1** 为结构畸变指数。
- **物理含义**：指数偏离 1 的程度即二聚化程度；二聚化把 d 电子锁入 M–M 键，从而消耗局域磁矩。
- **与磁性的对应（CrX₂ 家族）**：

| d₁/d₂ | 磁序 | 说明 | 性质 |
|---|---|---|---|
| ≈ 0.8 | **FM**（铁磁 CDW） | 畸变较轻，磁矩得以保留 | 计算预测 |
| ≈ 0.7 | **NM**（非磁 CDW） | 畸变较重，磁矩被二聚化消耗 | 计算预测 |

- **伴随的晶格常数差异**：两相的晶格常数差别很大——1T′-FM CrS₂ 沿 x、y 方向为 **3.325 Å / 5.626 Å**。这意味着 d₁/d₂ 的变化不是孤立的键长微调，而伴随整体晶胞重整。
- **两种机制的分工**：MnX₂ 的 1T′ FM 相中仍可见明显的 Mn–Mn 二聚键（与传统非磁 CDW 机制类似），但因 Mn 的 d 电子更多，二聚化**未完全消除**磁矩，故 FM 得以保留；该机制对应**更小**的畸变指数。

⚠️ **边界**：
1. 该指数是**为 1T′ TMD 量身定义**的，依赖「沿 y 方向存在两种 M–M 间距」这一特定几何，**不能**当作通用畸变度量（与八面体畸变指数、bond-length distortion index 等晶体学量无关）。
2. 全部数值来自单一论文的第一性原理计算，`0.8 / 0.7` 是该文在 CrX₂ 家族内观察到的**相关性**，非普适阈值；跨家族（V、Mn 基）时对应关系并不相同。

## 📚 相关论文 (Related Papers)

- [[../papers/chenFerromagneticNonmagnetic1T2022]]：本页的唯一来源，也是 d₁/d₂ 这一定义的提出者。该文系统计算 V、Cr、Mn 基 TMD 的 1T′ 相能量图，发现 CrX₂ 家族同时存在能量接近、声子谱无虚频（即结构稳定）的 NM 与 FM CDW 态，且二者晶格常数差异巨大；并建立起本页的核心对应关系——d₁/d₂ ≈ 0.8 对应 FM、≈ 0.7 对应 NM。更进一步，它把这一相关性归因于 **M–M 二聚化对局域磁矩的消耗**，并指出 MnX₂ 因 d 电子数更多而在二聚化后仍保留磁矩，从而解释了为何相同的结构畸变在不同金属上给出不同磁性结果。

## 🔗 关联概念与实体 (Related)

- [[../concepts/charge-density-wave|charge-density-wave]]
- [[../concepts/peierls-distortion|peierls-distortion]]
- [[../concepts/dimerization|dimerization]]
- [[../concepts/1t-prime-phase|1t-prime-phase]]
- [[../concepts/1t-phase|1t-phase]]
- [[../concepts/charge-doping|charge-doping]]
- [[../concepts/ferromagnetism|ferromagnetism]]
- [[../entities/TMDs|TMDs]]
