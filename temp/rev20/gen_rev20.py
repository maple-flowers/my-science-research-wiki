import os, json
out = r"C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp\rev20\rev20_pages.json"

p1 = r"""---
tags: [concept, superconductivity, 2D-materials, charge-density-wave]
title: '超导电性 / Superconductivity'
type: concept
status: mature
domain: [condensed-matter-physics, superconductivity, 2d-materials]
mechanism: 电子配对（库珀对）凝聚为宏观量子态，零电阻 + 完全抗磁（迈斯纳效应）
related_concepts: [charge-density-wave, electron-phonon-coupling, peierls-distortion, intercalation, 2d-materials, superfluid-density]
papers: ['CastroNeto2001charge', 'Koley2020charge', 'Petkov2020hierarchy', 'wuElectrostaticGatingIntercalation2022']
updated: 2026-08
---

# 超导电性 / Superconductivity

超导电性（superconductivity）指**材料在临界温度 $T_c$ 以下电阻突降为零并完全抗磁（迈斯纳效应）**的量子宏观态。其微观根源是电子通过（通常是声子介导的）吸引相互作用配对成库珀对，并凝聚到单一宏观波函数。在二维过渡金属硫族化合物（TMD）中，超导常与电荷密度波（CDW）共存或竞争，二者与晶格畸变、无序和维度效应深度耦合，是理解低维超导的窗口。

## 👵 太奶导读

超导就是"电阻彻底归零 + 把磁场排出去"。二维材料里有个奇妙的戏码：材料先"叠瓦"（CDW，电荷密度波），低温下又"通电畅通"（超导）——两者像一山不容二虎，却又常相伴。弄懂它们的相爱相杀，是低维物理的一大乐事。

## 🏗️ 核心判据与定量描述

| 物理量 | 符号/表达式 | 含义 |
| --- | --- | --- |
| 临界温度 | $T_c$ | 超导转变温度，低于其电阻为零 |
| BCS 能隙 | $2\Delta_0 = 3.52\,k_B T_c$ | 弱耦合极限下的能隙-温度关系 |
| 热力学临界场 | $H_c$ | 超过后超导态被破坏 |
| 穿透深度 | $\lambda_L$ | 磁场在超导体内指数衰减的特征长度 |
| 相干长度 | $\xi$ | 序参量空间变化的最小尺度 |

两个标志性效应：**零电阻**（直流电阻精确为零）与**迈斯纳效应**（内部磁场被完全排出，区别于理想导体）。

## 🧩 CDW 与超导的共存与竞争

- **f 波 CDW 统一图景**：2H-TMD（TaSe₂/TaS₂/NbSe₂/NbS₂）中 CDW 是具有六重节点的 f 波序参量，其低能激发是与声学声子压电耦合的狄拉克电子，统一解释了边缘费米液体自能、CDW 相的良好金属性与声子介导的超导配对（[[../papers/CastroNeto2001charge|Castro Neto 2001]]）。
- **无序释放超导**：非磁性团簇无序通过破坏 CDW 长程相干/预成型激子凝聚而释放被压制的 s 波超导，解释了 TaSe₂₋ₓSₓ 合金中超导重入并增强的现象（[[../papers/Koley2020charge|Koley 2020]]）。
- **晶格-CDW-超导层级**：强晶格畸变破坏一切电子序，完美二维晶格周期性是 CDW 的必要前提，而 Ta 亚晶格的三维周期性才是超导出现的必要条件（[[../papers/Petkov2020hierarchy|Petkov 2020]]）。

## 🧩 二维调控路径

静电门控（表面双电层）与（脱）插层（范德华间隙）可在不破坏层内共价键的前提下动态调控二维层状材料的电子态，是诱导/增强超导的新合成范式（如无限层镍酸盐超导体）（[[../papers/wuElectrostaticGatingIntercalation2022|Wu 2022]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/CastroNeto2001charge]] — Charge Density Wave, Superconductivity, and Anomalous Metallic Behavior in 2D Transition Metal Dichalcogenides
- [[../papers/Koley2020charge]] — Charge density wave and superconductivity in transition metal dichalcogenides
- [[../papers/Petkov2020hierarchy]] — Hierarchy among the crystal lattice, charge density wave, and superconducting orders in TMDs
- [[../papers/wuElectrostaticGatingIntercalation2022]] — Electrostatic gating and intercalation in 2D materials

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]：超导的主要竞争者。
- [[../concepts/electron-phonon-coupling|电子-声子耦合]]：声子介导超导的机制。
- [[../concepts/peierls-distortion|Peierls 畸变]]：CDW 的晶格根源。
- [[../concepts/intercalation|插层]]：调控超导的合成路径。
- [[../concepts/2d-materials|二维材料]]：低维超导的平台。
- [[../concepts/superfluid-density|超流密度]]：超导响应的刚度度量。
- [[../entities/NbSe2|NbSe₂]]、[[../entities/TaSe2|TaSe₂]]：CDW/超导研究体系。
"""

p2 = r"""---
tags: [concept, superconductivity, strong-coupling, electron-phonon]
title: '强耦合 / Strong Coupling'
type: concept
status: mature
domain: [condensed-matter-physics, superconductivity, strong-correlation]
mechanism: 粒子间相互作用强度远大于动能尺度，微扰论失效，需非微扰方法（Eliashberg/DMFT）
related_concepts: [electron-phonon-coupling, migdal-eliashberg-theory, superconductivity, mott-insulator]
papers: ['zhengAnisotropicSuperconductivityTwodimensional2025', 'majumdarInterplayChargeDensity2020', 'Koley2020charge']
updated: 2026-08
---

# strong-coupling / 强耦合

强耦合（strong coupling）泛指**体系中粒子间相互作用强度远大于其动能的参数区域**，常见语境包括强耦合超导（电子-声子耦合强度 $\lambda \gtrsim 1$）、强关联电子体系（电子-电子相互作用主导）与腔量子电动力学（光-物质强耦合）。强耦合下微扰论失效，需 Eliashberg 理论、动力学平均场（DMFT）等非微扰方法，并催生高温超导、Mott 物理与极化激元等丰富物态。

## 👵 太奶导读

太奶啊，物理里说"强耦合"，就是"粒子之间拽得特别紧"。比如超导里，电子和晶格振动"缠得很死"（强耦合超导），BCS 那套"轻轻牵手"的算法就不准了，得用升级版 Migdal-Eliashberg 方程硬算，才能算出氢化物 200K 高温超导。强耦合的体系"牵绊深、戏份多"，常常冒出别处没有的新奇物态。

## 🏗️ 弱耦合与强耦合对比

| 对比项 | 弱耦合 | 强耦合 |
| --- | --- | --- |
| 耦合强度 | $\lambda \ll 1$ | $\lambda \gtrsim 1$ 或 $U \gg W$ |
| 方法 | 微扰论/BCS | Eliashberg、DMFT、QMC |
| 能隙比 $2\Delta_0/k_BT_c$ | 约 3.52（BCS） | 偏离并增大 |
| 准粒子图像 | 良好（费米液体） | 失效（自能重正化强） |

## 🧩 核心内容与机制 (Core Content)

- **强耦合超导**：电子-声子耦合强度 $\lambda>1$（如 Pb、氢化物超导），需 Eliashberg 理论（[[../concepts/migdal-eliashberg-theory|Migdal-Eliashberg 理论]]）超越 BCS；能隙比、同位素指数偏离弱耦合值。多带/各向异性体系（如 kagome 金属有机框架 Cu₃(CO)₆）中强耦合效应与能带结构纠缠 [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]。
- **强关联电子**：电子-电子相互作用使能带论失效，出现 [[../concepts/mott-insulator|Mott 绝缘体]]、电荷/自旋序与非常规超导。
- **腔量子电动力学**：光与物质共振强耦合形成极化激元，改变材料基态与光学响应。
- **判定参数**：耦合常数 $\lambda$ 或相互作用与带宽比值（$U/W$）；非微扰方法必需。
- **与弱耦合对比**：弱耦合可微扰展开、准粒子近似有效；强耦合需整体重求基态。

## 🧩 超导实例中的强耦合

- 2H-NbS₂/2H-NbSe₂ 中多带超导与 CDW 交织，其能隙与 $T_c$ 关系偏离单带弱耦合 BCS，须用多带强耦合框架刻画 [[../papers/majumdarInterplayChargeDensity2020]]。
- TMD 合金体系中无序释放的 s 波超导其耦合强度随晶格畸变与无序水平变化 [[../papers/Koley2020charge]]。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/electron-phonon-coupling|电子-声子耦合]]：强耦合超导的根源。
- [[../concepts/migdal-eliashberg-theory|Migdal-Eliashberg 理论]]：强耦合超导的计算框架。
- [[../concepts/superconductivity|超导]]：强耦合的超导现象。
- [[../concepts/mott-insulator|Mott 绝缘体]]：强关联的典型物态。

## 📚 相关论文 (Related Papers)

- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]] — Anisotropic superconductivity in the 2D metal-organic kagome framework Cu₃(CO)₆
- [[../papers/majumdarInterplayChargeDensity2020]] — Interplay of charge density wave and multiband superconductivity in 2H-NbS₂/NbSe₂
- [[../papers/Koley2020charge]] — Charge density wave and superconductivity in TMDs
"""

p3 = r"""---
tags: [concept, superconductivity, disorder, percolation]
title: '超导渗流 / Superconducting Percolation'
type: concept
status: mature
domain: [condensed-matter-physics, superconductivity, disorder]
mechanism: 无序体系中超导区域随掺杂/无序度增加而连通，宏观超导在逾渗阈值处涌现
related_concepts: [superconductivity, charge-density-wave, order-parameter, quantum-critical-point]
papers: ['Chen2019superconductivity', 'Koley2020charge']
updated: 2026-08
---

# 超导渗流 / Superconducting Percolation

超导渗流（superconducting percolation）指在**无序或相分离体系**中，超导区域（微米/纳米尺度岛）随掺杂、压力或温度变化而逐步连通，当超导占比超过逾渗阈值 $p_c$ 时，宏观电阻突然降为零、体系呈现整体超导的现象。它与"均匀 BCS 超导"不同：超导性先在局域"液滴"中出现，再经约瑟夫森耦合在空间上"连通成网"。

## 👵 太奶导读

太奶啊，这就像一块田里先长出几棵"超导苗"（零电阻的小岛），苗太少时电流还得从没超导的地方绕，还是有电阻。等苗多到连成片、把整块田都连起来了，电流就能全程"零摩擦"地跑，这就是"渗流"——像水渗过沙子一样，只有连成通路才有好戏。

## 🏗️ 物理机制

*   **逾渗阈值**：二维体系逾渗阈值约为 $p_c \approx 0.5$（键逾渗约 0.347/座逾渗约 0.593 依模型而异），超过阈值后超导岛形成贯穿整个体系的连通集团。
*   **约瑟夫森网络**：孤立超导岛之间通过弱连接（隧穿/近邻效应）耦合，整体超导由约瑟夫森结网络的凝聚决定；临界电流与连接强度、相位相干相关。
*   **临界指数**：在阈值附近，超导刚度/临界电流以幂律 $I_c \propto (p-p_c)^\nu$ 趋于零，体现渗流普适类。
*   **脆性超导**：由渗流产生的超导常表现为"脆性"（brittle）——临界电流远低于均匀超导、对微弱扰动敏感，区别于本征超导。

## 🧩 具体体系实例

*   **TMD 合金中的无序释放超导**：在 TaSe₂₋ₓSₓ 等体系中，非磁性团簇无序破坏长程 CDW 相干，释放被压制的 s 波超导；超导随组分出现"重入-增强"行为，与超导区域渗流连通图景一致 [[../papers/Koley2020charge]]。
*   **1T-TiSe₂ 的 CDW/SC 转变**：公度-近公度-非公度 CDW 相变与超导涌现耦合，超导在 CDW 被抑制的区域（渗流通道）形成 [[../papers/Chen2019superconductivity]]。
*   **颗粒超导薄膜**：金属-绝缘体转变附近的颗粒膜，超导渗流与[[../concepts/order-parameter|序参量]]相位刚度共同决定宏观响应。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/charge-density-wave|电荷密度波]]：超导的竞争者/宿主。
- [[../concepts/order-parameter|序参量]]：超导序的空间分布。
- [[../concepts/quantum-critical-point|量子临界点]]：无序体系中的量子相变框架。
- [[../entities/TiSe2|TiSe₂]]、[[../entities/TaSe2|TaSe₂]]：渗流型超导研究体系。

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2019superconductivity]] — 1T-TiSe₂ 中 CDW 相与超导涌现行为
- [[../papers/Koley2020charge]] — 无序释放 TMD 中被压制的超导
"""

p4 = r"""---
tags: [concept, superconductivity, pairing, density-wave]
title: '配对密度波 / Pair Density Wave (PDW)'
type: concept
status: mature
domain: [condensed-matter-physics, superconductivity, strong-correlation]
mechanism: 库珀对凝聚携带有限动量 Q，超导序参量在实空间周期性调制
related_concepts: [superconductivity, charge-density-wave, spin-density-wave, order-parameter, anisotropic-superconductivity, multiband-superconductivity]
papers: ['majumdarInterplayChargeDensity2020', 'Chen2019superconductivity']
updated: 2026-08
---

# 配对密度波 / Pair Density Wave (PDW)

配对密度波（Pair Density Wave, PDW）指**库珀对的凝聚携带有限动量 $\mathbf{Q}$ 而非零动量**的超导态：其序参量 $\Delta(\mathbf{r}) = \Delta_0 e^{i\mathbf{Q}\cdot\mathbf{r}}$ 在实空间呈周期性调制，库珀对密度随位置振荡。PDW 是均匀 BCS 超导（$\mathbf{Q}=0$）的自然推广，被视为高温超导、条纹相与非常规磁性体系中重要的竞争/母体序。

## 👵 太奶导读

太奶啊，普通超导里的"电子夫妻"（库珀对）都慢悠悠在原地配对，安安静静的。可 PDW 里的电子夫妻们是"跳着舞配对"的——它们带着一股子"横劲儿"（有限动量）到处转，所以配对的密度就像波纹一样，一会儿密一会儿疏。这种"流动着配对"的脾气，会派生出很多奇怪的伴生现象。

## 🏗️ 物理机制

*   **有限动量配对**：当费米面嵌套或磁场/自旋序使电子配对偏好有限动量 $\mathbf{Q}$ 时，序参量获得空间调制 $\Delta(\mathbf{r})\propto e^{i\mathbf{Q}\cdot\mathbf{r}}$；$\mathbf{Q}$ 常与费米面嵌套矢量或磁条纹波矢关联。
*   **与均匀超导/CDW 的关系**：PDW 的 $|\Delta|^2$ 呈周期调制，可在实空间同时产生电荷密度调制（伴生 CDW 分量）与自旋调制，因此 PDW 常"携家带口"出现。
*   **对称性与时间反演**：有限动量配对一般伴随空间反演或时间反演对称性的部分破缺，可能诱发自旋极化电流、环路流等非常规响应。
*   **相位刚度**：PDW 序的相位涨落强烈，可导致"电子液晶"、向列序等中间相。

## 🧩 具体体系与证据

*   **条纹相（Stripes）**：空穴掺杂铜氧化物中自旋/电荷条纹与超导交织，多种实验（STM 涡旋芯调制、Josephson 干涉）支持 PDW 作为条纹相的核心序。
*   **磁场诱导 PDW**：磁场可诱导均匀超导向 PDW 转变，产生半量子涡旋（half-flux-quantum vortex）等拓扑缺陷，是区分 PDW 的探针。
*   **TMD 与层状体系**：2H-NbS₂/NbSe₂ 等体系中[[../concepts/charge-density-wave|CDW]]与多带超导交织 [[../papers/majumdarInterplayChargeDensity2020]]，其微观序是否含 PDW 分量为活跃研究方向；1T-TiSe₂ 中 CDW 与超导转变耦合 [[../papers/Chen2019superconductivity]] 提供了有限动量配对的可能舞台。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/spin-density-wave|自旋密度波]]
- [[../concepts/order-parameter|序参量]]
- [[../concepts/anisotropic-superconductivity|各向异性超导]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../entities/NbSe2|NbSe₂]]、[[../entities/TiSe2|TiSe₂]]

## 📚 相关论文 (Related Papers)

- [[../papers/majumdarInterplayChargeDensity2020]] — CDW 与多带超导在 2H-NbS₂/NbSe₂ 中的交织
- [[../papers/Chen2019superconductivity]] — 1T-TiSe₂ 中 CDW 相与超导涌现
"""

p5 = r"""---
tags: [concept, density-wave, magnetism, charge-order]
title: '自旋-电荷密度波 / Spin-Charge Density Wave'
type: concept
status: mature
domain: [condensed-matter-physics, magnetism, charge-order]
mechanism: 自旋密度波与电荷密度波在同一体系中并存或耦合，电子序沿实空间周期性调制
related_concepts: [spin-density-wave, charge-density-wave, superconductivity, fermi-surface-nesting, electron-phonon-coupling]
papers: ['Makogon2012wave', 'krishnamurthiSpinChargeDensity2020']
updated: 2026-08
---

# 自旋-电荷密度波 / Spin-Charge Density Wave

自旋-电荷密度波（Spin-Charge Density Wave, SCDW）指**自旋密度波（SDW）与电荷密度波（CDW）在同一体系中共存或耦合**的复合密度波态：电子自旋密度与电荷密度各自（或同步）沿实空间周期性调制。这类态常见于费米面嵌套显著的体系（如 Cr 金属、铁基超导母体、1T-TiSe₂），是磁性与电荷序交织、并可能孕育非常规超导的平台。

## 👵 太奶导读

太奶啊，电子排队伍有两个"花样"：一个是"电荷排成波浪"（有的地方人多、有的地方人少），一个是"自旋排成波浪"（一会儿朝上、一会儿朝下）。SCDW 就是这两样**同时开工**——又挤堆儿又翻面儿，整整齐齐地排。这种"双管齐下"的排序，常常是通向超导等新奇状态的前奏。

## 🏗️ 物理机制

*   **费米面嵌套**：[[../concepts/fermi-surface-nesting|费米面嵌套]]使电子-空穴激发能量在嵌套矢量 $\mathbf{Q}$ 处异常低，形成自旋（或电荷）密度波的起源；SDW 与 CDW 的嵌套矢量可以相同或不同。
*   **SDW 与 CDW 的耦合**：SDW 打开自旋能隙，同时通过电-声子耦合与塞曼效应诱发电荷调制（CDW 分量），二者共享序参量空间中的关联。
*   **激子凝聚（1T-TiSe₂）**：在 1T-TiSe₂ 中，间接能隙的电子-空穴配对（激子凝聚）同时表现为电荷调制与（弱的）自旋/轨道响应，构成 SCDW 的一个具体实现。
*   **与超导的关系**：SDW/CDW 序被掺杂、压力或无序抑制时，常释放超导，体现"序竞争-超导涌现"的普遍图景。

## 🧩 具体体系实例

*   **Cr 金属**：经典 SDW 体系，其磁有序伴随电荷响应的调制，是理解 SCDW 耦合的原型。
*   **铁基超导母体**：BaFe₂As₂ 等母体相 SDW 与结构畸变耦合，掺杂后 SDW 被抑制出现超导。
*   **光学晶格模型**：二维自旋-1/2 费米子光学晶格中，交错塞曼场可产生"类方圆形"费米面并诱发自旋-电荷耦合的密度波态 [[../papers/Makogon2012wave]]。
*   **多铁性关联**：在螺旋磁序多铁中，自旋与电荷序的空间耦合与[[../concepts/magnetoelectric-coupling|磁电耦合]]相关（参见库内 krishnamurthi 综述）[[../papers/krishnamurthiSpinChargeDensity2020]]。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-density-wave|自旋密度波]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/superconductivity|超导电性]]
- [[../concepts/fermi-surface-nesting|费米面嵌套]]
- [[../concepts/electron-phonon-coupling|电子-声子耦合]]
- [[../entities/TiSe2|TiSe₂]]、[[../entities/NbSe2|NbSe₂]]

## 📚 相关论文 (Related Papers)

- [[../papers/Makogon2012wave]] — 二维光学晶格自旋-电荷耦合密度波理论模型
- [[../papers/krishnamurthiSpinChargeDensity2020]] — 自旋/电荷密度波与多铁性关联综述
"""

pages = {
    "superconductivity": p1,
    "strong-coupling": p2,
    "superconducting-percolation": p3,
    "pair-density-wave": p4,
    "spin-charge-density-wave": p5,
}
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    json.dump(pages, f, ensure_ascii=False, indent=1)
print("pages:", len(pages))
for k, v in pages.items():
    print(k, len(v))
