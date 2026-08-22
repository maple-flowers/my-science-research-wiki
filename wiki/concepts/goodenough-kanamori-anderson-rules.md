---
tags: [concept, superexchange, magnetism, exchange-interaction, bond-angle, double-exchange]
title: goodenough-kanamori-anderson-rules
type: concept
status: developing
year: 2026
papers: [yuFerroelectricControlMagnetism2026, chenFerromagneticNonmagnetic1T2022]
updated: 2026-08-21
---

# goodenough-kanamori-anderson-rules

**Goodenough–Kanamori–Anderson（GKA）规则** 概括了[[../concepts/superexchange|超交换]]耦合的符号如何由 **M–X–M 键角**决定：键角约 **90° 给铁磁**耦合，约 **180° 给反铁磁**耦合。

它的实用价值在于把「磁序是什么」这个问题转化成一个**纯几何量**——只要量出配体桥连的键角，就能预判耦合符号。

## 👵 太奶导读

乖孙，两个磁性原子中间隔着一个非磁性原子（比如 Cr–F–Cr 里的 F），它们隔着这个「中间人」也能互相商量磁矩朝哪边——这叫超交换。

**GKA 规则说的是：商量的结果是「同向」还是「反向」，主要看这三个原子摆成什么角度。**

- 摆成一条直线（约 **180°**）→ 两边**反向**（反铁磁）。
- 拐成直角（约 **90°**）→ 两边**同向**（铁磁）。

为什么？因为中间那个配体原子有两个互相垂直的 p 轨道。直线排布时，两个磁性原子抢的是**同一个** p 轨道，只能一个自旋朝上一个朝下，于是反向；拐成直角时，两边各自对上**不同的、互相垂直的** p 轨道，就不必彼此让位，同向反而更省能量。

**这条规则有多好用？** 本库有个漂亮的例子：某个材料里有四条不同的交换路径，量出来 J₁、J₁′、J₂、J₂′ 对应的键角都是约 90°——**全是铁磁**；J₃ 对应约 180°——**是反铁磁**。规则一一对上。

**还有一个更妙的用法**：另一篇论文里，同一种材料的高对称相和畸变相磁性完全不同。原因就是畸变把键角**掰到了 90° 附近**，于是磁性从反铁磁翻成了铁磁。也就是说，**掰键角就是在调磁性**。

记一句话：**GKA 规则 = 90° 铁磁、180° 反铁磁；它把磁序问题变成量键角的问题，所以凡能改键角的手段（畸变、应变、极化翻转）都能用来调磁性。**

## 🧩 规则内容与本库中的两类用法

### 用法一：解释已有磁构型（键角 ↔ J 符号逐条对应）

| 交换路径 | 键角 | 耦合符号 | 体系 |
|---|---|---|---|
| J₁ / J₁′ / J₂ / J₂′ | ≈ 90°（Cr–X–Cr、Cr–Y–Cr） | **FM** | CSFB（Cr 基）|
| J₃ | ≈ 180° | **AFM** | 同上 |

J 值由八种磁构型的能量差拟合得到（含至第四近邻 J₄）。除超交换外，该体系的**金属性**还额外贡献了[[../concepts/double-exchange|双交换]]作用，同样偏铁磁——即净铁磁性是超交换与双交换两项之和，不可只归因于键角。

### 用法二：作为相变前后磁序翻转的机制解释

在 1T′ 相 TMD 中（CrX₂、VTe₂）：

- **1T 相（未畸变）**：M–M 距离近，磁性由**直接交换**主导 → **反铁磁**。
- **1T′ 相（畸变）**：M–X–M 键角被掰到接近 **90°**，按 GKA 规则**超交换转为铁磁**主导；同时 M–M 二聚键消失，X 原子上还诱导出与 M 反平行的微小磁矩——这是超交换起作用的特征标记。
- **判据衔接**：该转变对应[[../concepts/structural-distortion-index|结构畸变指数]] d₁/d₂ ≈ 0.8（畸变适中，足以改变键角但不足以形成 M–M 二聚键）。若畸变更重（d₁/d₂ ≈ 0.7）则走另一条路——二聚化吃掉磁矩，得到非磁态。

⚠️ **边界**：
1. 「90° 铁磁 / 180° 反铁磁」是**符号的经验规则**，不给出耦合强度；强度还依赖轨道占据、杂化程度与电子填充。
2. 上述键角—符号对应及 J 值均来自第一性原理计算，本库无对应实验测定。
3. 两篇论文中的体系都同时存在**其他机制**（双交换、直接交换、二聚化），GKA 只解释其中的超交换分量，**不能**据此把整体磁序单独归因于键角。

## 📚 相关论文 (Related Papers)

- [[../papers/yuFerroelectricControlMagnetism2026]]：本页用法一的来源，也是 GKA 规则在本库中被最严格检验的一次。作者用八种磁构型拟合出至第四近邻的交换常数，逐条核对键角与符号：J₁/J₁′/J₂/J₂′ 对应约 90° 的 Cr–X–Cr、Cr–Y–Cr 键且均为铁磁，J₃ 对应约 180° 且为反铁磁，与 GKA 规则完全吻合；同时指出体系的金属性额外带来双交换的铁磁贡献，因此明确了 GKA 只解释超交换分量这一边界。
- [[../papers/chenFerromagneticNonmagnetic1T2022]]：本页用法二的来源。该文用 GKA 规则解释 1T→1T′ 相变前后磁序的翻转——1T 相由 M–M 直接交换主导呈反铁磁，1T′ 相中 M–X–M 键角被掰至接近 90° 后超交换驱动铁磁，并给出该机制的两个旁证（M–M 二聚键消失、X 原子上诱导出与 M 反平行的微小磁矩）；它还把这一机制与畸变指数 d₁/d₂ ≈ 0.8 定量挂钩，从而说明 GKA 规则可以作为**结构调控磁性**的设计依据，而非仅是事后解释。

## 🔗 关联概念与实体 (Related)

- [[../concepts/superexchange|superexchange]]
- [[../concepts/double-exchange|double-exchange]]
- [[../concepts/exchange-interaction|exchange-interaction]]
- [[../concepts/direct-exchange|direct-exchange]]
- [[../concepts/structural-distortion-index|structural-distortion-index]]
- [[../concepts/antiferromagnetism|antiferromagnetism]]
- [[../concepts/ferromagnetism|ferromagnetism]]
- [[../concepts/charge-density-wave|charge-density-wave]]
- [[../concepts/magnetoelectric-coupling|magnetoelectric-coupling]]
