---
tags: [entity, sliding-ferroelectricity, interlayer-stacking, strain-engineering, intercalation, spin-transport, polarization-switching]
title: black-phosphorus
type: entity
status: developing
year: 2020
papers: [shenEmergenceMultipleFerroelectric2025, yangStrainEngineeringTwodimensional2021, wuElectrostaticGatingIntercalation2022, liuSpintronicsTwoDimensionalMaterials2020b]
updated: 2026-08-21
---

# black-phosphorus

黑磷（black phosphorus, BP）是由磷单一元素构成的褶皱蜂窝状二维半导体。它在本库中承担四个彼此独立的角色：**单质滑移铁电体**（shen2025，本页主线）、**各向异性应变响应材料**（yang2021）、**插层剥离的宿主**（wu2022）、以及**自旋输运通道**（liu2020b）。共同的物理根源只有一个——褶皱结构带来的面内各向异性与弱层间范德华耦合。

## 👵 太奶导读

乖孙，黑磷就是纯磷做成的一层层薄片，每层都是皱巴巴的蜂窝网，层与层之间靠很弱的力贴着，所以一推就能错开。

它最要紧的一件事是：单层和双层黑磷是**左右对称**的，对称就意味着正负电荷中心重合，没有电偶极，所以不铁电。可到了三层以上，如果把层与层的错开方式弄成不对称的（叫 EAB 堆叠），对称性就破了，层之间挪一点点电子，整块薄片就自己带上了电偶极——这叫滑移铁电性。它的稀罕之处在于：**这是纯单质做出来的铁电体**。传统铁电材料都是化合物，来回翻转极化时不同元素容易分开跑（元素偏析）；单质压根没有"不同元素"，所以不会有这毛病。

而且不是只有两个状态。四层黑磷能有一大把不同的极化态，彼此之间只要滑一滑就能换过去，翻越的坎只有几十毫电子伏——这就有做多阻态存储的意思了。注意：**以上全部是第一性原理计算结果**，本库没有黑磷铁电性的实验测量。

## 🧩 核心内容与机制 (Core Content)

### 结构基础：褶皱蜂窝与各向异性

单层黑磷为褶皱蜂窝状，含两种不等价键长（2.23 Å 与 2.27 Å）和两种键角（96° 与 103°）——这一结构不对称性是其面内各向异性（锯齿 ZZ 方向 vs 扶手椅 AC 方向）的直接来源，并贯穿下文的铁电、应变、自旋各条线索。

### 主线：多层黑磷中的滑移铁电性（shen2025）

论证按层数递进：

| 层数 | 对称性 | 面外极化 (pC/m) | 面内极化 (pC/m) |
| --- | --- | --- | --- |
| 单层 / 双层 | 中心对称 | 0 | 0 |
| 三层 EAB | 中心对称破缺 | 0.06 | 1.32 |
| 四层（多构型） | 多种非对称构型 | 0.02 – 0.07 | 1.25 – 2.44 |

- **双层的势能面**：以 AB 堆叠为零点扫描层间滑移矢量，仅 AB、AE、AF 三点为能量极小值，AB 为基态；其他堆叠会自发滑向这三者之一。不同堆叠对应不同化学势——这是"堆叠方式可改变电子能量分布"的先兆，也是三层出现极化的物理伏笔。
- **三层出现极化**：穷举堆叠组合后，非对称堆叠 EAB 破坏中心对称。EAB 相对非极化基态 BAB 仅高约 **40 meV**，属实验可达的亚稳态；其声子谱在整个布里渊区无虚频，动力学稳定。
- **极化的电子起源**：对比 BAB 与 BAF 的投影态密度——BAB 中顶层 L3 与底层 L1 的 p_z 贡献对称；BAF 中价带顶主要来自 L1、导带底主要来自 L3。这一垂直方向的电荷转移即面外极化的来源，与差分电荷密度（等值面 3 × 10⁻⁴ e Å⁻³）给出的层间电荷重分布图像一致。
- **翻转路径与能垒**：CI-NEB 计算 EAB → BAF 的两条路径，能垒均约 **48 meV**。四层体系中从最大正极化态（AEE′E）到最大负极化态（ABAE）的连续滑移路径能垒为 **15 – 94 meV**。
- **厚板中的可操控性**：在黑磷厚板中，仅位移表面层即可诱发并翻转极化，为实验观测提供了不必操控整块材料的方案。

### 支线一：各向异性应变响应（yang2021）

单轴应变可**选择性**调节 BP 的面内/面外振动模式，这是其他各向同性二维材料没有的特性：

| 应变方向 | 红移的拉曼峰 | 几乎不移动的峰 |
| --- | --- | --- |
| 锯齿 ZZ | A²_g, B_2g | A¹_g |
| 扶手椅 AC | A¹_g, B_2g | A²_g |

密度泛函微扰理论将该各向异性归因于应变下键长与键角的同时变化。器件层面，柔性 PEN 基底上的黑磷 FET 呈现巨大压阻响应——拉伸应变下电阻增大、压缩应变下减小。

### 支线二：插层剥离与环境稳定化（wu2022）

黑磷对环境敏感，是插层技术的典型受益者。用长链烷基溴化铵插层，可把（准）块体黑磷"撑"成**单层原子晶体分子超晶格**，在垂直集成的宏观材料中获得单层物性，同时借有机分子层隔绝环境。机制属 c 轴晶格膨胀一类（同类例证：吡啶插层 TaS₂ 使层间距 6 Å → 12 Å，在三维块体中实现二维超导），本质是三维到二维电子态的转变。

### 支线三：自旋输运通道（liu2020b）

黑磷被用作非局域自旋阀的自旋通道并已有器件演示。综述的判断明确：**BP、硅烯乃至 MoS₂ 作为自旋传输通道的性能与石墨烯相比仍有差距**。综述以时间线汇总了 2007–2019 年石墨烯、黑磷、MoS₂ 的自旋弛豫时间 τ_s (ns) 与自旋扩散长度 λ_s (μm) 进展，但未在正文给出黑磷的具体数值，故本页不列。

## ⚠️ 使用本页时的边界

- **铁电部分全部为第一性原理计算**。0.06 / 1.32 pC/m、40 meV、48 meV、15–94 meV 均为计算值，本库中没有任何黑磷铁电性的实验测量。
- **"单层/双层不铁电"是结论而非缺省假设**：它由中心对称性给出，若见到声称双层黑磷铁电的说法，须核对其堆叠构型定义是否与本页一致。
- 面外极化（0.02–0.07 pC/m）比面内极化（1.25–2.44 pC/m）小一个多数量级；讨论"黑磷极化多大"时必须指明是哪一个分量，否则数字差 20 倍以上。
- 四条线索共用"黑磷"这一名字，但**器件形态完全不同**（计算的理想多层堆叠 / 柔性基底 FET / 插层准块体 / 自旋阀）。跨线索搬运数值无效。

## 📚 相关论文 (Related Papers)

- [[../papers/shenEmergenceMultipleFerroelectric2025]]：以第一性原理证明三层及以上黑磷可通过非对称堆叠（EAB）打破中心对称而产生滑移铁电性，给出面外 0.06 / 面内 1.32 pC/m 的极化与约 48 meV 的翻转能垒，并揭示四层体系中多极化态经低能垒滑移互相转换，从而把滑移铁电性从化合物推广到单质体系。
- [[../papers/yangStrainEngineeringTwodimensional2021]]：以黑磷为各向异性范例，指出沿锯齿与扶手椅方向的单轴应变分别选择性红移不同的拉曼峰（ZZ 影响 A²_g/B_2g、AC 影响 A¹_g/B_2g），并归因于应变下键长与键角的共同变化，为各向异性柔性器件的应变设计提供了判据。
- [[../papers/wuElectrostaticGatingIntercalation2022]]：把长链有机分子插层黑磷归入"c 轴晶格膨胀导致三维到二维电子态转变"这一机制类别，说明插层可将环境敏感的准块体黑磷转化为单层原子晶体分子超晶格，在宏观材料中获得单层物性。
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：将黑磷列为非局域自旋阀的自旋输运通道并给出器件演示，同时明确判断其自旋输运性能与石墨烯相比仍存在差距，为黑磷在自旋电子学中的定位划出上限。

## 🔗 关联概念与实体 (Related)

- [[../concepts/sliding-ferroelectricity|sliding-ferroelectricity]]
- [[../concepts/interlayer-stacking|interlayer-stacking]]
- [[../concepts/interlayer-charge-transfer|interlayer-charge-transfer]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/climbing-image-neb|climbing-image-neb]]
- [[../concepts/strain-engineering|strain-engineering]]
- [[../concepts/piezoresistive-effect|piezoresistive-effect]]
- [[../concepts/raman-strain-splitting|raman-strain-splitting]]
- [[../concepts/intercalation|intercalation]]
- [[../concepts/spin-transport|spin-transport]]
- [[../entities/GaN|GaN]]
