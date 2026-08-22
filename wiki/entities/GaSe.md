---
tags: [entity, material, 2D, semiconductor, sliding-ferroelectricity]
title: 硒化镓 (GaSe)
type: entity
status: mature
category: [D01]
formula: GaSe
class: [III-VI, layered-semiconductor, vdW]
properties: [layered-semiconductor, stacking-dependent-polarization, sliding-ferroelectricity]
related_concepts: [sliding-ferroelectricity, interlayer-stacking, interlayer-translation, broken-inversion-symmetry]
related_entities: [InSe]
key_quantities:
  AB_bilayer_vertical_polarization: "约 0.46 pC/m（计算值）"
  reported_GaSe_polarization: "约 6.19 pC/m（2025 综述表汇总；结构定义不同）"
  PFM_switching_bias: "约 ±5–6 V（综述 Fig. 12 所示 GaSe 纳米片回线）"
papers: [wuSlidingFerroelectricity2D2021a, sunSlidingFerroelectricityTwodimensional2025]
updated: 2026-08
---

# 硒化镓 (GaSe)

GaSe（硒化镓）是 III–VI 族层状半导体。一个基本层由 Se–Ga–Ga–Se 四个原子面组成，层内以共价键连接，层间主要靠范德华作用堆叠。不同层间配准和堆垛序列可以保留或破坏空间反演对称性，并改变层间电荷转移；当两个极性堆垛能通过横向滑移互换时，GaSe 可表现出滑动相关的可切换极化。

“GaSe 是滑动铁电体”不能脱离层数与多型理解：单层、AB 双层、多层纳米片及不同 ε/β/γ 堆垛具有不同对称性和极化定义。仓库综述给出的 0.46 pC/m 与 6.19 pC/m 对应不同结构/汇总口径，不能当作同一样品的重复测量。

## 👵 太奶导读

太奶，您可以把 GaSe 想成一叠有花纹的薄卡片。每张卡片内部很结实，但卡片之间贴得不牢，可以横着错开。两张卡片若叠得上下完全等价，正负电荷的偏移会互相抵消；把上层横着推到另一种位置后，上下环境不再一样，电子会稍微偏向一侧，于是整叠材料有了电极化。

若存在两个能量相近、极化方向相反的堆垛，而且电场能推动层间滑移在二者之间切换，这才构成滑动铁电。看到 PFM 蝴蝶回线或二次谐波信号只能分别说明机电响应或反演对称性破缺；要证明真正的滑动铁电，还要确认极化可重复切换、排除电荷注入，并证明结构变化确实涉及层间配准。

## 🏗️ 层状结构与堆垛多型

GaSe 的单层是 Se–Ga–Ga–Se 四原子层：中间两个 Ga 形成 Ga–Ga 键，上下 Se 完成配位。层内强键使基本层保持完整，层间弱范德华作用则允许剥离、人工堆垛、扭转与横向平移。

多层 GaSe 可形成不同堆垛多型，常用 ε、β、γ 等符号区分。决定极化的不是名称本身，而是完整堆垛是否具有反演中心或能把上下方向等价化的镜面对称。即使相邻两层各自产生局域偶极，偶极也可能在更长堆垛周期中同向叠加、反向抵消或形成奇偶层效应。因此报告铁电性时必须说明层数、堆垛、多型和极化方向。

## 🧩 滑动如何产生极化

对由不同元素构成的层状半导体，层间配准改变 Ga 与 Se 原子在上下层的相对位置，从而改变轨道重叠、局域静电势和层间电荷重分布。若某个堆垛打破面外反演对称性，就会出现面外偶极；横向平移到其反演伙伴构型后，电荷偏移方向反转，极化随之反号。

[[../papers/wuSlidingFerroelectricity2D2021a|Wu 与 Li 的综述]]将这一机制概括为“堆垛诱导极化”：单层未必需要传统钙钛矿式离子偏心，双层组合本身即可因层间电荷重排产生极化。其汇总的 AB 双层 GaSe 计算面外极化约为 0.46 pC/m。二维极化用 pC/m 表示，是每单位面内长度的偶极，不能不经有效厚度定义直接与块体 μC/cm² 数值比较。

滑动铁电也不意味着完全没有厚度效应。它避免了传统体铁电“必须维持三维软模”的部分限制，但电极屏蔽、退极化场、衬底钉扎、层间摩擦、污染和层数奇偶仍会改变稳定性与矫顽偏压。

## 🔀 铁电、反铁电与堆垛能量景观

不同堆垛可以形成同向偶极、反向偶极或无净偶极状态。[[../papers/sunSlidingFerroelectricityTwodimensional2025|Sun 等人的综述]]汇总 MX 族层状材料时指出，AA/AC 与 AB/AD 等配准的能量和极性不同，部分构型倾向铁电排列，另一些倾向反铁电排列。对器件而言，是否能切换取决于两点：终态能量差是否足够小，以及连接它们的滑移路径势垒是否能被实验电场克服。

这一区分避免了三个常见混淆：**有极性结构不一定可切换；可切换电阻不一定来自极化；存在两个堆垛也不一定能由纯平移互换。** 结构、极化和输运必须形成相互支持的证据链。

## 🔬 实验证据与读图

[[../papers/sunSlidingFerroelectricityTwodimensional2025]]汇总了 GaSe 纳米片的开关谱 PFM（SS-PFM）、器件输运和偏振 SHG 证据。PFM 振幅呈蝴蝶形、相位出现接近 180° 的跃迁，说明偏压能切换机电响应符号；SHG 的六瓣偏振图说明样品缺乏反演对称。二者结合比单一信号更有说服力，但仍需脉冲协议、保持性和结构表征排除静电与离子迁移。

![图：GaSe/MX 族堆垛、器件、SS-PFM 与 SHG 证据](../../raw/figures/sunSlidingFerroelectricityTwodimensional2025/fig_12_HWWZSN8Y.png)
*   **关键特征**：图 a 示意不同横向配准及极化方向，图 b 给出纳米片场效应器件，图 c 中 PFM 振幅在约 ±5–6 V 附近出现极小值且相位跳变，图 d 的六瓣 SHG 偏振响应支持反演对称性破缺。各子图共同覆盖“结构—电学切换—对称性”三个层次，不能把任一单图视为完整证明。
*   **来源**：[[../papers/sunSlidingFerroelectricityTwodimensional2025]] -> [[../figures/heterostructures-stacking|异质结与堆叠]]；该图是综述组合图，图 a 还包含其他 MX 材料的通用结构示意。

## ⚡ 器件意义与限制

极化可改变 GaSe 通道的静电势、接触势垒和载流子分布，因此可形成非易失电阻状态，用于存储或类突触权重。滑移路径同时受应变和界面摩擦影响，也使 GaSe 适合探索机械—电学耦合。

但器件中的迟滞可能来自界面陷阱、吸附水、离子迁移或接触变化。可靠结论至少需要：开关后零偏压保持、循环稳定、扫描速率依赖、PUND 或等效脉冲电荷测量、不同厚度/堆垛对照，以及 PFM/SHG/结构成像之间的一致性。ON/OFF 比和写入电压高度依赖器件几何，不应由综述中的定性描述扩写成普适材料常数。

## 📚 相关论文 (Related Papers)

- [[../papers/wuSlidingFerroelectricity2D2021a]]：建立范德华堆垛诱导极化与横向平移翻转的通用框架，并汇总 AB 双层 GaSe 约 0.46 pC/m 的计算面外极化。
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]]：汇总 GaSe 的堆垛能量、纳米片 SS-PFM、SHG 和器件证据，并把它放入二维滑动铁电材料与应用谱系中。

## 📋 关键参数表

| 参数 | 数值 / 状态 | 条件 | 物理意义 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| 基本层结构 | Se–Ga–Ga–Se | 单个 GaSe 四原子层 | 规定层内成键与面外化学环境 | [[../papers/wuSlidingFerroelectricity2D2021a]]；[[../papers/sunSlidingFerroelectricityTwodimensional2025]] |
| AB 双层面外极化 | 约 0.46 pC/m | 第一性原理汇总的 AB 堆垛双层 | 量化层间电荷重排产生的二维面外偶极 | [[../papers/wuSlidingFerroelectricity2D2021a]] |
| GaSe 极化汇总值 | 约 6.19 pC/m | 2025 综述 Table 2 所列 GaSe 条目；结构口径与上项不同 | 说明不同层数/构型与文献口径可给出不同数值，不能直接平均 | [[../papers/sunSlidingFerroelectricityTwodimensional2025]] |
| PFM 相位变化 | 接近 180° | 综述 Fig. 12 的 GaSe 纳米片 SS-PFM | 表示机电响应符号随偏压反转 | [[../papers/sunSlidingFerroelectricityTwodimensional2025]] |
| PFM 特征偏压 | 约 ±5–6 V | Fig. 12 所示具体纳米片与探针测量 | 振幅极小与相位切换出现的器件偏压，不等于普适矫顽场 | [[../papers/sunSlidingFerroelectricityTwodimensional2025]] |
| 通用滑移势垒、带隙与 ON/OFF 比 | 未确认 | 仓库现有两篇综述未给出同一 GaSe 构型下可统一的可靠值 | 避免混合不同多型、厚度和器件条件 | 仓库资料不足 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]：由层间平移连接相反极化堆垛的铁电机制。
- [[../concepts/interlayer-stacking|层间堆垛]]：决定整体空间对称性和偶极叠加方式。
- [[../concepts/interlayer-translation|层间平移]]：连接不同堆垛与极化状态的结构坐标。
- [[../concepts/broken-inversion-symmetry|中心反演对称性破缺]]：出现电偶极和偶次非线性光学响应的必要条件。
- [[../entities/InSe|InSe]]：同属 III–VI 层状半导体、具有堆垛相关极化的姊妹体系。
