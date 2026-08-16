---
tags: [concept, piezoelectricity, mechanics, nanoscale]
title: 挠曲电效应 / Flexoelectric Effect
type: concept
status: mature
domain: [condensed-matter-physics, piezoelectricity, ferroelectricity, 2d-materials]
mechanism: 应变梯度通过挠曲电张量诱导极化；其强度随局部曲率和结构尺寸减小而显著增强
related_concepts: [polarization-switching, strain-engineering, ferroelectricity, coercive-field, sliding-ferroelectricity]
key_quantities:
  BiFeO3_film_thickness: "70 nm（外延薄膜）"
  BiFeO3_nucleation_force: "约700 nN（局部应力约0.25 GPa）"
  BiFeO3_full_switching_force: "3325 nN（局部应力约1.18 GPa）"
  GeSe_cooling_transition: "约245 K（无波纹）→约275 K（有波纹）"
  hBN_domain_wall_width: "9.7–40.7 nm（0°–90°畴壁）"
papers: [Chen2016electrical, wuSlidingFerroelectricity2D2021a, yangRipplingFerroicPhase2021, heUltrafastSwitchingDynamics2024]
updated: 2026-08
---

# 挠曲电效应 / Flexoelectric Effect

挠曲电效应（flexoelectric effect）是指**应变不均匀**时产生电极化的机电耦合：材料的一侧被拉伸、另一侧被压缩，或局部发生弯曲，都会让单位体积内的电荷分布出现方向性偏移。它与压电效应的关键差别是，压电效应由均匀应变驱动并要求非中心对称晶体，而挠曲电耦合由应变梯度驱动，中心对称介质也不被对称性禁止。

在纳米薄膜、针尖接触、畴壁和二维波纹中，长度尺度变小会把同样的形变量压缩到更短的距离内，使应变梯度变大。因此，挠曲电效应既是解释纳米尺度机械翻转的机制，也是把曲率、缺陷和层间滑移转化为极化或内建电场的桥梁；但具体阈值仍取决于张量、介电边界、几何形状和缺陷，不能只由外加载荷直接换算。

## 👵 太奶导读

太奶，您把材料想成一块薄薄的橡皮泥：整块均匀地按下去，只是一起变扁；如果一边按得重、一边按得轻，或者把它弯成弧形，里面的正负电荷就会被错开，像小电池一样出现方向。这个“按得不一样快、不一样重”的程度叫**应变梯度**，也就是形变在不同位置的差别；“挠曲电”就是这种不均匀形变生出极化，极化就是电荷方向性排队。薄到纳米、弯得厉害，或用针尖局部按压时，这个差别特别大，便可能把铁酸铋（BiFeO₃，一种能保持电荷方向的铁电材料）里的小箭头整片翻过去。

## 🧩 应变梯度如何变成极化

在连续介质近似下，直接挠曲电效应可写成

$$
P_i=\mu_{ijkl}\frac{\partial\varepsilon_{jk}}{\partial x_l},
$$

其中 $P_i$ 是第 $i$ 个方向的极化，$\varepsilon_{jk}$ 是应变分量，$\partial\varepsilon_{jk}/\partial x_l$ 是应变梯度，$\mu_{ijkl}$ 是四阶挠曲电张量。张量把“哪一种形变梯度”与“哪一个极化方向”配对起来；因此同样大小的弯曲，在不同晶向、不同边界条件下可以产生不同方向和大小的极化。

对比之下，压电效应常写作 $P_i=d_{ijk}\varepsilon_{jk}$，只含均匀应变。反演对称性会禁止压电张量 $d_{ijk}$ 的相应分量，却不必禁止带有空间导数的挠曲电项；这就是中心对称介质仍可有挠曲电响应的对称性原因。逆挠曲电效应则是反过来用非均匀电场驱动弯曲或应变梯度，二者是同一耦合的正、逆过程。

在厚度为 $h$、面内形变量尺度为 $\varepsilon$ 的薄膜中，一维估算为

$$
\frac{\partial\varepsilon}{\partial z}\sim\frac{\varepsilon}{h},\qquad
E_f\simeq\frac{\mu}{\varepsilon_0\epsilon_r}\frac{\partial\varepsilon}{\partial z},
$$

这里 $E_f$ 是挠曲电内建场，$\epsilon_r$ 是相对介电常数。这个估算说明减薄会增强梯度，但它不是普适数值公式：真实针尖接触还要加入三维接触几何、衬底约束、屏蔽和缺陷。

## ⚡ 力学翻转：挠曲电场与矫顽场竞争

Chen 等在 70 nm 外延 BiFeO₃ 薄膜中把针尖力学写入与电学写入并列比较。PFM 针尖（压电力显微镜的纳米探针）在接触区产生强烈的面外形变梯度；机械载荷从 700 nN 增大到 3325 nN 时，向下极化区域由 8.9% 增至 100%，完全翻转对应约 1.18 GPa 的局部应力。电学和机械写入都先在既有畴壁附近成核，再经历纳米畴分解，最后重组为微米级反向畴，说明驱动力虽不同，实际路径由材料的畴能景观决定 [[../papers/Chen2016electrical]]。

![图：BiFeO₃ 薄膜机械翻转面积随针尖载荷增长](../../raw/figures/Chen2016electrical/fig_3_V2QYGQGG.png)
*   **关键特征**：700、1050、1400、1750、3325 nN 对应的向下极化面积约为 8.9%、41.4%、82.2%、95.9%、100%；图中载荷增加伴随反向畴逐步扩展，而不是一次均匀翻转。
*   **来源**：[[../papers/Chen2016electrical]] -> [[../figures/domain-walls-switching-properties|极化翻转与铁电性能]]

这里的证据强度需要分层理解：实验直接证明了局部机械力能在厚膜中完成非易失翻转，并与挠曲电场驱动相符；但该工作没有用三维有限元或独立的挠曲电系数测量给出针尖下 $\partial\varepsilon/\partial z$ 与 $E_f$ 的时空分布。因此，“挠曲电场主导”是由几何、尺度和翻转行为共同支持的机制解释，不应把 3325 nN 当成可跨材料迁移的普适阈值。

## 📏 尺寸、曲率与二维极限

尺寸效应的核心不是“薄膜自动更软”，而是相同形变量被集中到更短的距离：$h$ 越小，$\varepsilon/h$ 越大；局部曲率、台阶、孔洞和畴壁也会把梯度集中在有限区域。Yang 等对单层 GeSe 的分子动力学对照显示，允许面外波纹时，平均曲率与铁性序参量增强量呈相关关系；冷却相变温度由无波纹模型的约 245 K 提高到有波纹模型的约 275 K，表明曲率不是被动噪声，而可作为极性纳米微区和异质形核的来源 [[../papers/yangRipplingFerroicPhase2021]]。

![图：单层 GeSe 中波纹、曲率与铁性序的耦合](../../raw/figures/yangRipplingFerroicPhase2021/fig_2_594HMLNH.png)
*   **关键特征**：有波纹模型的平均铁性序在冷却过程中高于无波纹模型；平均曲率随温度变化，并与序参量增量同步增强，说明面外形貌能把局域梯度耦合进铁性状态。
*   **来源**：[[../papers/yangRipplingFerroicPhase2021]] -> [[../figures/crystal-structures-surfaces-defects|表面、缺陷与形貌]]

在二维范德华材料中，Wu 与 Li 将层间面内滑移、面外屈曲和低层间剪切统一到 ripplocation（波纹位错）畴壁图像：翻转时层间滑移很容易发生，而畴壁处的屈曲把形变集中到窄区，提供了挠曲电耦合的几何通道。这里的“低集体势垒”描述的是层间协同滑移的能量路径，不等同于挠曲电张量的大小；二者都说明二维结构可以同时具有低写入能垒和明显的局部梯度 [[../papers/wuSlidingFerroelectricity2D2021a]]。

![图：二维层间滑移中的波纹位错与集体/孤立翻转路径](../../raw/figures/wuSlidingFerroelectricity2D2021a/fig_5_FQBZIJ7L.png)
*   **关键特征**：左侧区分低“集体”滑移势垒与高“孤立”层内变形势垒，右上显示 MoS₂ 层间局部屈曲，右下示意屈曲层在外力下形成可移动的滑移结构；这些屈曲位置正是应变梯度集中的区域。
*   **来源**：[[../papers/wuSlidingFerroelectricity2D2021a]] -> [[../figures/heterostructures-stacking|异质结与堆叠]]

## 🔬 畴壁屈曲与梯度分布

He 等对 h-BN 双层畴壁的原子模拟给出更直接的空间图像：0° 畴壁近似平面并呈布洛赫型极化纹理，90° 畴壁则出现明显面外屈曲并呈奈尔型纹理。面外极化 $P_z$ 在畴壁中心降至近零，随后在两侧恢复；随着滑移方向与畴壁夹角从 0° 增至 90°，极化梯度分布宽度为 9.7、17.6、32.1、40.7 nm。宽畴壁意味着梯度不是原子级尖锐跳变，而是由层间滑移、面内刚度和屈曲共同分摊的连续区域 [[../papers/heUltrafastSwitchingDynamics2024]]。

![图：h-BN 双层不同畴壁的屈曲结构与面外极化梯度](../../raw/figures/heUltrafastSwitchingDynamics2024/fig_5_BK4H4WHC.png)
*   **关键特征**：左侧 0° 畴壁保持平面、90° 畴壁出现面外弯曲；右侧 $P_z$ 从正极化过渡到负极化，灰色区域标出极化梯度核心，宽度随畴壁角度增大而增宽。
*   **来源**：[[../papers/heUltrafastSwitchingDynamics2024]] -> [[../figures/domain-walls-structures|畴结构与畴壁]]

这组结果也限定了概念边界：畴壁运动降低翻转场、或莫尔结构出现超顺电响应，并不意味着所有响应都由挠曲电效应单独决定；层间势垒、长程静电、缺陷钉扎和畴壁弹性能必须同时纳入。挠曲电效应在这里更准确的角色，是把屈曲和极化梯度纳入同一自由能描述的耦合项。

## 🎯 判据与实验解读边界

判断一个现象是否可归因于挠曲电效应，可以按三步检查：

1. **是否存在空间梯度**：弯曲、针尖接触、厚度方向界面、畴壁或波纹应能给出可识别的 $\nabla\varepsilon$；只有均匀压缩不能单凭机械载荷推出挠曲电极化。
2. **方向是否符合几何和对称性**：极化方向应随弯曲方向、晶向或上下表面交换而改变；中心对称样品可有响应，但不同边界条件可能抵消或增强它。
3. **是否排除了替代机制**：电荷注入、压电响应、摩擦起电、缺陷迁移和局部相变都可能伴随针尖操作。应结合翻转可逆性、载荷依赖、厚度依赖、PFM 形貌和电学读出，而不是只看一条滞回线。

因此，$\mu_{ijkl}$、$\epsilon_r$ 和真实三维应变场应尽量独立测量或由经验证的模拟得到。当前四篇关联论文给出了翻转力、曲率/温度对照和畴壁梯度图像，但没有提供可直接移植到任意材料的完整挠曲电张量；参数表中不填该张量的数值，避免把机制解释误写成材料常数。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2016electrical]]：在 70 nm BiFeO₃ 外延薄膜中用 PFM 针尖实现完全机械极化翻转，并以载荷序列和电/机械畴演化对照支持挠曲电场驱动的解释。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：综述二维范德华滑动铁电性，说明 ripplocation 畴壁的面外屈曲与低层间剪切如何为挠曲电耦合和快速翻转提供几何背景。
- [[../papers/yangRipplingFerroicPhase2021]]：在单层 GeSe 模拟中定量比较有、无波纹模型，给出曲率—铁性序相关及约 245 K→275 K 的冷却相变温度变化。
- [[../papers/heUltrafastSwitchingDynamics2024]]：以 h-BN 双层原子模拟解析不同角度畴壁的屈曲、极化梯度和 9.7–40.7 nm 宽度，为二维畴壁中的梯度分布提供直接图像。

## 📋 关键参数表

下表只列出四篇关联论文中有明确条件的数值。机械载荷、温度和畴壁宽度分别属于特定材料与模型，不能当作普适挠曲电常数。

| 参数 | 数值 | 条件 | 物理含义与来源 |
| :--- | :--- | :--- | :--- |
| BiFeO₃ 薄膜厚度 | $\approx70\ \text{nm}$ | (001) 外延薄膜；PFM 针尖写入 | 尺寸决定厚度方向应变梯度的放大程度；[[../papers/Chen2016electrical]] |
| 机械成核载荷 | $\approx700\ \text{nN}$；局部应力约 $0.25\ \text{GPa}$ | 向下极化面积约 8.9% | 首批反向畴出现的载荷尺度；[[../papers/Chen2016electrical]] |
| 完全机械翻转载荷 | $3325\ \text{nN}$；局部应力约 $1.18\ \text{GPa}$ | 向下极化面积达到 100% | 该 BiFeO₃ 样品的完全写入条件，不是普适阈值；[[../papers/Chen2016electrical]] |
| 反向极化面积序列 | 8.9% → 41.4% → 82.2% → 95.9% → 100% | 700 → 1050 → 1400 → 1750 → 3325 nN | 反向畴随局部梯度驱动力增加而扩展；[[../papers/Chen2016electrical]] |
| GeSe 冷却相变温度 | 约 245 K（无波纹）→约 275 K（有波纹） | 单层 GeSe；有/无面外运动的模型对照 | 波纹稳定短程铁性序并提供异质形核位置；[[../papers/yangRipplingFerroicPhase2021]] |
| GeSe 双轴压缩应变 | $-0.2\%$ | 350 K 单层 GeSe 模拟 | 增强波纹并诱导条纹状铁性畴；[[../papers/yangRipplingFerroicPhase2021]] |
| h-BN 畴壁梯度宽度 | 9.7、17.6、32.1、40.7 nm | 畴壁角度 $0^\circ$、$30^\circ$、$60^\circ$、$90^\circ$ | 极化从一侧稳态过渡到另一侧的空间尺度；[[../papers/heUltrafastSwitchingDynamics2024]] |
| h-BN 单畴面外极化 | $P_z=1.46\times10^{-12}\ \text{C/m}$ | AB/BA 双层稳态，Berry 相位/DP 模拟 | 为畴壁中心 $P_z\approx0$ 的两侧极化基准；不是挠曲电张量；[[../papers/heUltrafastSwitchingDynamics2024]] |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/polarization-switching|极化翻转]]（挠曲电场可作为机械写入的局部驱动力）
- [[../concepts/strain-engineering|应变工程]]（通过厚度、曲率或外加应变调节梯度）
- [[../concepts/ferroelectricity|铁电性]]（挠曲电极化可改变铁电自由能景观）
- [[../concepts/coercive-field|矫顽场]]（机械翻转阈值需与电学矫顽场对照）
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]（二维层间滑移与屈曲形成相关梯度）
- [[../entities/BiFeO3|铁酸铋 (BiFeO₃)]]（70 nm 机械翻转实验体系）
