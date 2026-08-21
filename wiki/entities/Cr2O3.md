---
tags: [entity, material, oxide, antiferromagnet, magnetoelectric]
title: 氧化铬 (Cr₂O₃)
type: entity
status: mature
category: [D02]
formula: Cr2O3
class: [corundum, oxide, antiferromagnet, insulator]
properties: [antiferromagnetism, linear-magnetoelectric-coupling]
related_concepts: [magnetoelectric-coupling, antiferromagnetism, exchange-bias, time-reversal-symmetry]
related_entities: [BiFeO3]
key_quantities:
  Neel_temperature: "约 307 K（接近室温）"
papers: [fiebigEvolutionMultiferroics2016, spaldinAdvancesMagnetoelectricMultiferroics2019]
updated: 2026-08
---

# 氧化铬 (Cr₂O₃)

Cr₂O₃（氧化铬，chromia）是刚玉结构的反铁磁绝缘体，也是线性磁电效应的原型材料。它在约 307 K 以下形成反铁磁序；该磁序使电场可以诱导磁化、磁场可以诱导极化。Cr₂O₃ 通常没有可独立翻转的自发铁电极化和净铁磁磁化，所以它是**磁电体**而不是通常定义下的**多铁体**。这一区分是理解其物理与器件用途的起点。

## 👵 太奶导读

太奶，您可以把 Cr₂O₃ 里的铬磁矩想成一列一正一反站队的小磁针：相邻方向相反，整块材料的磁性大体互相抵消，这叫反铁磁。虽然外面看不到像普通磁铁那样的净磁化，这支队伍却有两种等价排法——把所有箭头同时反过来，会得到另一个反铁磁畴。

奇妙之处在于电和磁可以“搭话”：加磁场时材料会产生很小的电极化，加电场时又会产生很小的磁化。若在冷却穿过反铁磁转变温度时同时施加电场和磁场，两者的乘积还能偏爱其中一种反铁磁畴。它不是“电场直接把一块永久磁铁翻转”，而是先选择或操控隐藏的反铁磁序，再通过表面磁化或交换偏置影响相邻铁磁层。

## 🏗️ 结构与磁序

Cr₂O₃ 采用 α-Al₂O₃ 型刚玉结构：O²⁻ 近似六方密堆，Cr³⁺ 占据其中三分之二的八面体间隙。Cr³⁺ 的 $3d^3$ 电子形成局域磁矩；低于奈尔温度 $T_N\approx307$ K 时，磁矩主要沿晶体三重轴共线、反平行排列，宏观净磁矩近似抵消。

化学晶格本身具有反演对称性，但反铁磁排列把“哪个 Cr 位点朝上、哪个朝下”写进晶体。单独做空间反演或时间反演都会把一个磁畴变成另一个磁畴，而二者联合仍可保持磁结构等价。这种磁点群正是允许线性磁电张量、同时禁止普通自发铁磁矩和自发铁电极化的对称性基础。

## 🧩 线性磁电效应是什么

在线性响应范围内，磁场诱导的极化和电场诱导的磁化可写成

$$P_i=\alpha_{ij}H_j,\qquad M_j=\alpha_{ij}E_i,$$

其中 $\alpha_{ij}$ 是线性磁电张量。它描述交叉响应，不代表材料获得了可在零场保持并单独翻转的铁电极化。对 Cr₂O₃ 的轴向对称性，平行和垂直于三重轴的张量分量一般不同；数值还随温度变化，并在 $T_N$ 以上因长程反铁磁序消失而失去该线性效应。

自由能中的最低阶耦合可写为

$$F_{ME}=-\alpha_{ij}E_iH_j.$$

反转反铁磁畴会改变 $\alpha_{ij}$ 的符号。因此，同时施加电场与磁场时，$E_iH_j$ 项能降低一个畴的自由能、提高另一个畴的自由能；这就是磁电退火或场冷选择畴的基础。

## 🔁 反铁磁畴、表面磁化与交换偏置

Cr₂O₃ 的两个 180° 反铁磁畴在体内净磁化近似为零，但特定晶面可以出现与体反铁磁序绑定的未补偿表面磁化。若在表面覆盖铁磁层，界面交换作用会让铁磁层的磁滞回线产生偏移，即交换偏置。改变 Cr₂O₃ 的反铁磁畴，就可能改变界面钉扎方向，从而间接控制铁磁层。

[[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019|Spaldin 等人的综述]]将 Cr₂O₃列为经典电控反铁磁畴与交换偏置平台。器件逻辑是“电场/磁场选择 Cr₂O₃ 畴 → 表面磁化改变 → 相邻铁磁层响应”，而不是把 Cr₂O₃误写成具有大净磁矩的铁磁体。

## 🧭 它为何不是多铁体

多铁体要求同一相中具有至少两种初级铁性序，例如可独立翻转的铁电极化与铁磁/反铁磁序。Cr₂O₃ 有反铁磁序和线性磁电响应，却没有常规铁电自发极化；因此“磁电”与“多铁”有交集但不等同。[[../papers/fiebigEvolutionMultiferroics2016|Fiebig 等人的综述]]把 Cr₂O₃作为这一术语边界及“空间反演与时间反演双破缺”物理的典型例子，并将其与非互易光学、铁涡旋性等更广泛的对称性效应联系起来。

与 [[../entities/BiFeO3|BiFeO₃]] 相比，后者在室温附近同时具有强铁电极化和反铁磁序，属于本征多铁体；Cr₂O₃ 的优势则是对称性清楚、线性磁电机制相对干净，适合研究反铁磁畴选择和界面交换控制。

## 🔬 实验如何证明磁电响应

- **磁电电流/电荷测量**：在交流磁场下测量电极上的感生电荷，积分得到 $P(H)$；必须排除电磁串扰和漏电。
- **电场诱导磁响应**：用高灵敏磁测量或磁光方法检测 $M(E)$，信号通常很小。
- **磁电场冷**：样品穿过 $T_N$ 时同时施加 $E$ 和 $H$，再通过磁光二次谐波、表面磁化或交换偏置读出畴选择。
- **温度依赖**：线性磁电响应应与反铁磁有序相关，并在 $T_N$ 附近发生特征变化；这有助于排除普通介电或热磁伪影。
- **界面器件**：观察铁磁覆盖层的交换偏置变化时，还需区分电荷积累、应变、热效应和真正的 Cr₂O₃ 畴切换。

## ⚠️ 尺度与应用边界

Cr₂O₃ 的 $T_N$ 仅略高于室温，因此薄膜应变、缺陷、晶粒和界面可能把器件工作温区推到室温上下；薄膜值不能无条件套用块体 307 K。磁电系数也随温度、晶向、频率和单位制变化，若来源未给出测量条件，单独列一个“最大值”容易误导。仓库现有两篇综述未提供足以在本页可靠统一的 $\alpha_\parallel$、$\alpha_\perp$ 数值，因此本页不补造这些参数。

## 📚 相关论文 (Related Papers)

- [[../papers/fiebigEvolutionMultiferroics2016]]：从多铁性演化与对称性双破缺的视角定位 Cr₂O₃，强调它是具有线性磁电和非互易光学响应、但并非铁电多铁体的经典参照。
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：将 Cr₂O₃ 纳入现代磁电材料与异质结构路线，说明电场可控反铁磁畴及其对铁磁覆盖层交换偏置的调控价值。

## 📋 关键参数表

| 参数 | 数值 / 状态 | 条件 | 物理意义 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| 化学式 | Cr₂O₃ | 化学计量氧化铬 | 每个化学式含两个 Cr³⁺ 与三个 O²⁻ | 本页结构定义 |
| 晶体结构 | 刚玉型（α-Al₂O₃ 型） | 体相基态结构 | 决定三重轴、Cr 八面体配位和磁电张量对称性 | [[../papers/fiebigEvolutionMultiferroics2016]]；[[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]] |
| 奈尔温度 | 约 307 K | 体材料常用参考值；薄膜可因边界条件变化 | 低于此温度形成长程反铁磁序并允许线性磁电响应 | 页面既有资料；两篇综述的材料背景 |
| 净体磁化 | 近似为零 | 共线反铁磁体、无外场理想情形 | 区别于铁磁体；器件常利用表面磁化和交换偏置读出 | [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]] |
| 线性磁电系数 | 本仓库未确认统一数值 | 强烈依赖温度、晶向与单位制 | 描述 $P_i=\alpha_{ij}H_j$ 和 $M_j=\alpha_{ij}E_i$ | 仓库现有资料不足 |
| 铁电自发极化 | 无常规可翻转铁电序 | 零场体相 | 说明 Cr₂O₃ 是磁电体而非通常定义的多铁体 | [[../papers/fiebigEvolutionMultiferroics2016]] |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/magnetoelectric-coupling|磁电耦合]]：电场与磁响应、磁场与电响应之间的交叉耦合。
- [[../concepts/antiferromagnetism|反铁磁性]]：Cr₂O₃ 的初级磁序及磁电响应来源。
- [[../concepts/exchange-bias|交换偏置]]：通过界面把反铁磁畴状态传递给铁磁覆盖层。
- [[../concepts/time-reversal-symmetry|时间反演对称性]]：与空间反演共同决定线性磁电项是否允许。
- [[../entities/BiFeO3|BiFeO₃]]：具有自发铁电极化的本征多铁对照材料。
