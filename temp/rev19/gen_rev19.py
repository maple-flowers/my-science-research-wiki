# -*- coding: utf-8 -*-
import os, json
out = r"C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp\rev19\rev19_pages.json"

p1 = r"""---
tags: [concept, superconductivity, 2D-materials, fermiology]
title: 各向异性超导 / Anisotropic Superconductivity
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 超导序参量（能隙、临界场、临界电流）随晶格方向或动量方向变化，源于费米面各向异性与配对机制的动量依赖
related_concepts: [superconductivity, fermi-surface-nesting, flat-band, electron-phonon-coupling, multiband-superconductivity, two-gap-superconductivity]
papers: [zhengAnisotropicSuperconductivityTwodimensional2025]
updated: 2026-08
---

# 各向异性超导 / Anisotropic Superconductivity

各向异性超导（Anisotropic Superconductivity）指超导体的宏观性质——能隙、上临界场 $H_{c2}$、临界电流 $J_c$ 与穿透深度 $\lambda$——在晶格不同方向或费米面不同动量位置上表现出显著差异的现象。它与费米面的几何各向异性、多带结构及配对势的动量依赖密切相关，是判定非常规超导配对的重要线索之一。

## 👵 太奶导读

太奶啊，普通超导体像一只“圆鼓鼓的气球”，各方向都一般粗；而各向异性超导就像一只“拉长的气球”，顺着一个方向结实、另一方向就软一些。电流朝一个方向流很顺，换个方向就费劲。咱们量一量这种“方向上的差别”，就能反推出超导的“配对是怎么组织的”——这就是各向异性超导的价值。

## 🏗️ 物理特征与定量描述

各向异性体现在多个层面：

*   **能隙各向异性**：动量空间内的超导能隙 $\Delta(\mathbf{k})$ 不再为常数，可呈现角向调制甚至节点（沿特定方向能隙为零）。对于各向异性 $s$ 波，$\Delta(\mathbf{k})$ 在费米面上随角度起伏；对于 $d$ 波，则存在线节点。
*   **上临界场各向异性**：$H_{c2}$ 沿主轴与面内的比值不同，由有效质量张量与相干长度各向异性决定，$H_{c2} \propto 1/\xi^2$。
*   **临界电流与穿透深度各向异性**：$J_c$、$\lambda$ 对方向的依赖反映超流密度的张量特性。

## 🧩 kagome 金属有机框架中的各向异性

二维 kagome 点阵金属有机框架 Cu₃(CO)₆ 单层（P6/mmm 空间群，Cu 四配位）是近期理论预测的一个范例：[[../concepts/electron-phonon-coupling|电-声子耦合]]驱动的 BCS 型超导体，临界温度 $T_c = 16.5$ K。其超导呈现**单能隙、各向异性**特征——kagome 几何带来的[[../concepts/flat-band|平带]]与[[../concepts/fermi-surface-nesting|费米面嵌套]]使配对强度在动量空间分布不均匀，形成角向调制的能隙 [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]。

| 特征 | 数值/性质 | 意义 |
| --- | --- | --- |
| 晶格 | kagome 单层，P6/mmm | 几何阻挫与嵌套并存 |
| 机制 | 电-声子耦合 BCS | 常规配对基底 |
| 能隙结构 | 单能隙、各向异性 | 非均匀配对强度 |
| 临界温度 | 16.5 K | 二维 MOF 中较高 Tc |

## 🔬 在二维超导研究中的角色

各向异性测量（角度分辨磁输运、方向分辨微波表面阻抗）是区分常规 $s$ 波与非常规（节点/多带/配对对称性破缺）超导的关键判据，与[[../concepts/superconductivity|超导]]的[[../concepts/multiband-superconductivity|多带]]及[[../concepts/two-gap-superconductivity|双能隙]]图像相互印证。

## 📚 相关论文 (Related Papers)

- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]：第一性原理预言 kagome MOF Cu₃(CO)₆ 单层为 Tc=16.5 K 的各向异性单能隙 BCS 超导体。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/fermi-surface-nesting|费米面嵌套]]
- [[../concepts/flat-band|平带]]
- [[../concepts/electron-phonon-coupling|电-声子耦合]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../concepts/two-gap-superconductivity|双能隙超导]]
- [[../entities/Cu3CO6|Cu₃(CO)₆ kagome 金属有机框架]]
"""

p2 = r"""---
tags: [concept, superconductivity, 2D-materials, charge-density-wave, fermiology]
title: 多带超导 / Multiband Superconductivity
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 超导配对同时在费米面的多个能带通道上建立，各通道能隙不同，整体响应为多能隙加权叠加
related_concepts: [superconductivity, two-gap-superconductivity, charge-density-wave, fermi-surface-nesting, superfluid-density]
papers: [majumdarInterplayChargeDensity2020]
updated: 2026-08
---

# 多带超导 / Multiband Superconductivity

多带超导（Multiband Superconductivity）指超导序参量同时展布于费米面的多个能带（多个费米面片）之上，各带拥有独立（或部分独立）的超导能隙。它常见于层状过渡金属硫族化物、铁基超导体与 MgB₂ 等具有多重费米面片（空穴/电子口袋）的材料，是理解非常规超导微观机制的核心概念之一。

## 👵 太奶导读

太奶啊，一般的超导像“一条河上架一座桥”，只走一条道。多带超导呢，像“好几条平行河各架一座桥”，每条河的水流（能带）都有自己的桥（能隙），载客能力不一样。测超导的总响应时，几条河的贡献叠在一起，看起来就像一个“叠影”的能隙。这就是多带超导的朴素图像。

## 🏗️ 物理特征与定量描述

*   **多能隙结构**：不同能带上的能隙 $\Delta_1, \Delta_2, \dots$ 大小不一，低温比热、穿透深度与隧道谱出现多台阶/双峰结构。
*   **带间耦合**：带间散射（杂质或配对）把各带能隙耦合成整体，影响 $T_c$ 与能隙比 $2\Delta/k_BT_c$ 偏离 BCS 弱耦合值。
*   **带间配对符号**：各带配对序参数可能同号（$s_{++}$，如 MgB₂ 声子机制）或反号（$s_\pm$，如铁基超导体自旋涨落机制），后者的探测常借助杂质敏感性或相敏实验。

## 🧩 层状硫族化物中的多带超导与 CDW

以 2H-NbSe₂、2H-NbS₂ 为代表的过渡金属二硫族化物同时拥有 CDW 与超导两种序。高质量单晶研究揭示了：

*   **CDW 与超导的竞争**：[[../concepts/charge-density-wave|电荷密度波]]会重构费米面、耗散[[../concepts/fermi-surface-nesting|嵌套]]口袋，抑制超导配对。
*   **压力调控**：施加压力可抑制 CDW、恢复被局域化的费米面，从而**显著增强超导**——2H-NbSe₂ 中 CDW 与 SC 呈竞争关系，压力下 CDW 被抑制、超导增强 [[../papers/majumdarInterplayChargeDensity2020]]。
*   **多带贡献**：多能隙响应叠加后，[[../concepts/superfluid-density|超流密度]]与穿透深度的温度依赖偏离单带 London 行为，可通过低温幂律/指数行为区分。

## 🔬 实验判据

| 判据 | 多带/多能隙表现 |
| --- | --- |
| 比热 | 低温指数/多台阶，能隙比偏离 BCS |
| 穿透深度 | 低温由大能隙主导，呈指数饱和 |
| 隧道谱 | 多峰结构 |
| 上临界场 | 温度依赖偏离单带 Werthamer-Helfand-Hohenberg 曲线 |

## 📚 相关论文 (Related Papers)

- [[../papers/majumdarInterplayChargeDensity2020]]：2H-NbSe₂/2H-NbS₂ 单晶中 CDW 与超导的竞争及压力增强超导，体现多带费米面重构对超导的关键作用。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/two-gap-superconductivity|双能隙超导]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/fermi-surface-nesting|费米面嵌套]]
- [[../concepts/superfluid-density|超流密度]]
- [[../entities/NbSe2|二硒化铌 (NbSe2)]]
- [[../entities/NbS2|二硫化铌 (NbS2)]]
"""

p3 = r"""---
tags: [concept, superconductivity, 2D-materials, charge-density-wave, strain-engineering]
title: 双能隙超导 / Two-Gap Superconductivity
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 超导序参量由两个（类）能隙刻画，通常对应两群费米面或两种配对通道，宏观响应呈两能隙叠加
related_concepts: [superconductivity, multiband-superconductivity, charge-density-wave, superfluid-density, bec-bcs-crossover]
papers: [Islam2025enhancement]
updated: 2026-08
---

# 双能隙超导 / Two-Gap Superconductivity

双能隙超导（Two-Gap Superconductivity）是[[../concepts/multiband-superconductivity|多带超导]]中最常见的情形：超导态由两个能隙 $\Delta_1$、$\Delta_2$ 共同刻画，二者通常对应两群不同费米面片（如层状材料中的不同价带）或两种配对强度。它在 MgB₂、NbSe₂、铁基超导等体系中被广泛观测。

## 👵 太奶导读

太奶啊，还是“多座桥”的老故事，只不过这次明确只有**两座桥**：一座结实（大能隙）、一座软（小能隙）。低温时主要是结实那座在承重（扛着超导序），温度升高软桥先垮。测总响应时两条曲线叠在一起，会出现两个特征温度尺度——这就是“双能隙”的指纹。

## 🏗️ 物理特征与定量描述

*   **两个能隙**：$\Delta_1 \neq \Delta_2$，各自与 $T_c$ 的比值 $2\Delta/k_BT_c$ 可分别偏离或接近 BCS 值。
*   **两温度尺度**：热力学量（比热、超流密度、穿透深度）在低温与中温出现两个不同幂律/指数区间。
*   **带间泄漏**：温度升高时大能隙带上的准粒子通过散射耦合进小能隙带，使小能隙被“拖高”，表现为非简单的两带独立。

## 🧩 硫族化物中的双能隙与压力/应变调控

对层状硫族化物超导体单晶（如含 CDW 的 4H-NbSe₂ 与不含 CDW 的 2H-NbS₂）的研究表明：

*   在 2 GPa 压力下，4H-NbSe₂ 的[[../concepts/superfluid-density|超流密度]]增强 **75%**，显著高于 2H-NbSe₂ 的 **32%**，而两者的 CDW 都被抑制约 20% [[../papers/Islam2025enhancement]]。
*   该差异源于双能隙/多带结构：CDW 对费米面的重构作用在不同能带上不同，压力恢复的态密度对 4H 结构增益更大，从而超流密度增幅更强。
*   这一现象把“双能隙超导”与[[../concepts/charge-density-wave|CDW]]竞争、以及[[../concepts/bec-bcs-crossover|BCS-BEC 渡越]]的能标联系起来。

## 🔬 与多带超导的区分

| 对比项 | 双能隙超导 | 多带超导（广义） |
| --- | --- | --- |
| 能隙数量 | 两个（主通道） | 两个及以上 |
| 典型来源 | 两群费米面/两配对通道 | 多费米面片叠加 |
| 观测特征 | 双台阶/双温度尺度 | 多台阶/连续谱 |

## 📚 相关论文 (Related Papers)

- [[../papers/Islam2025enhancement]]：4H-NbSe₂ 与 2H-NbS₂ 在压力下超流密度增强的对比，揭示双能隙与 CDW 竞争对超导的调控。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../concepts/superfluid-density|超流密度]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/bec-bcs-crossover|BCS-BEC 渡越]]
- [[../entities/NbSe2|二硒化铌 (NbSe2)]]
- [[../entities/NbS2|二硫化铌 (NbS2)]]
"""

p4 = r"""---
tags: [concept, superconductivity, 2D-materials, uemura-relation]
title: 超流密度 / Superfluid Density
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 超流密度正比于超导凝聚中的配对载流子有效密度，通过穿透深度 λ 由 London 方程导出，ns ∝ 1/λ²
related_concepts: [superconductivity, penetration-depth, multiband-superconductivity, two-gap-superconductivity, uemura-relation, charge-density-wave]
papers: [Islam2025enhancement, majumdarInterplayChargeDensity2020]
updated: 2026-08
---

# 超流密度 / Superfluid Density

超流密度（Superfluid Density）$n_s$ 是刻画超导凝聚体刚度的核心量，定义为单位体积内参与无耗散超流输运的有效载流子数。它与穿透深度 $\lambda$ 直接关联：由 London 方程 $n_s = m^*/(\mu_0 e^2 \lambda^2)$，即 $n_s \propto 1/\lambda^2$。超流密度的温度依赖与数值大小是区分常规/非常规配对、判定超导凝聚机制（BCS 弱耦合、强耦合、BCS-BEC 渡越）的重要观测量。

## 👵 太奶导读

太奶啊，超导就是电子结成“整齐的队列”无阻地流。超流密度就是这支队列有多“密实”——密实了，磁场钻不进去（被挤出表面），温度也没那么容易把队列打散。咱们不直接数电子，而是量磁场能钻多深（穿透深度），深度越浅说明队列越密实、超流密度越大。

## 🏗️ 物理特征与定量描述

*   **London 关系**：$n_s = \dfrac{m^*}{\mu_0 e^2 \lambda^2}$，穿透深度 $\lambda$ 是实验上获取 $n_s$ 的主要窗口。
*   **温度依赖**：在 BCS 弱耦合下低温近似 $n_s(T)/n_s(0) \approx 1 - \sqrt{2\pi\Delta/k_BT}\, e^{-\Delta/k_BT}$（指数饱和）；存在节点（如 $d$ 波）或低能激发时则呈幂律。
*   **Uemura 关系**：在欠掺杂铜氧化物等非常规超导体中，$T_c \propto n_s/m^*$（Uemura 标度），反映超导由凝聚刚度主导，而非由配对能标主导。
*   **多能隙贡献**：多带/[[../concepts/two-gap-superconductivity|双能隙]]体系中 $n_s(T)$ 是各带贡献的加权叠加，低温段由大能隙带主导。

## 🧩 压力/应变调控下的超流密度

对层状硫族化物超导体的研究展示超流密度如何响应序竞争：

*   2 GPa 压力下，4H-NbSe₂ 的超流密度增强 **75%**，高于 2H-NbSe₂ 的 **32%**；两者 CDW 均被抑制约 20% [[../papers/Islam2025enhancement]]。
*   解释：压力抑制[[../concepts/charge-density-wave|CDW]]、恢复费米面态密度，凝聚刚度增强；4H 的多带结构使其对 CDW 抑制更敏感，$n_s$ 增幅更大。
*   这体现了超流密度作为“序竞争”敏感探针的价值——它同时编码了配对强度（$\Delta$）与配对载流子数（$n_s$）两类信息。

## 🔬 实验判据速览

| 观测量 | 与超流密度的关系 | 用途 |
| --- | --- | --- |
| 穿透深度 λ | ns ∝ 1/λ² | 主探针（微波谐振、μSR、磁光） |
| 上临界场 Hc2 | 正比于 ns 相关量 | 交叉验证 |
| 比热 | 反映能隙结构 | 配合解析多能隙 |

## 📚 相关论文 (Related Papers)

- [[../papers/Islam2025enhancement]]：压力下 4H/2H-NbSe₂ 超流密度增强，量化 CDW 竞争对凝聚刚度的调控。
- [[../papers/majumdarInterplayChargeDensity2020]]：2H-NbSe₂/2H-NbS₂ 中 CDW 与超导竞争，提供超流密度响应的背景图像。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/penetration-depth|穿透深度]]
- [[../concepts/uemura-relation|Uemura 关系]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../concepts/two-gap-superconductivity|双能隙超导]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../entities/NbSe2|二硒化铌 (NbSe2)]]
"""

p5 = r"""---
tags: [concept, superconductivity, 2D-materials, charge-density-wave]
title: 超导穹顶 / Superconducting Dome
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 临界温度 Tc 随掺杂/压力等控制参量呈先升后降的非单调穹顶状，两侧受竞争序与量子临界涨落抑制
related_concepts: [superconductivity, charge-density-wave, multiband-superconductivity, superfluid-density]
papers: [Chen2019superconductivity]
updated: 2026-08
---

# 超导穹顶 / Superconducting Dome

超导穹顶（Superconducting Dome）指超导临界温度 $T_c$ 随某一控制参量（掺杂浓度、载流子密度、压力、层数等）变化呈现**先升后降的穹顶状**非单调行为的普遍现象。它在铜氧化物高温超导（掺杂穹顶）、重费米子、有机超导以及 1T-TiSe₂ 等二维材料中反复出现，通常被解读为超导与某种竞争序（反铁磁、[[../concepts/charge-density-wave|CDW]] 等）及量子临界点共存/博弈的指纹。

## 👵 太奶导读

太奶啊，这就好比熬汤，火候（掺杂/压力）太小汤不鲜，火太大又糊了，中间有个“刚刚好”的甜点。超导也一样：调控参量太小时序太弱，太大时又被别的“坏分子”（竞争序）拆台，只有在中间的某个窗口，超导最兴旺——画成图就是一个“小山包”（穹顶）。

## 🏗️ 物理特征与定量描述

*   **穹顶形态**：$T_c(x)$ 随控制参量 $x$ 先增后减，峰值 $T_c^{\max}$ 出现在最佳掺杂/压力处。
*   **量子临界点**：穹顶峰值常靠近被抑制的竞争序的量子临界点，量子临界涨落被认为可能提供非常规配对媒介。
*   **两侧机制**：欠掺杂侧受静态序（反铁磁/CDW）抑制；过掺杂侧配对涨落与序参量刚度下降。
*   **与超流密度的关系**：Uemura 标度下穹顶两侧 $T_c$ 与凝聚刚度 $n_s/m^*$ 的关联不同，欠掺杂侧偏离 BCS 关系。

## 🧩 1T-TiSe₂ 中的超导穹顶

二维过渡金属二硫族化物 1T-TiSe₂ 是一个典型二维实例：

*   其 CDW 在公度（C）、近公度（NC）与非公度（IC）相之间转变，超导在 CDW 被抑制的窗口内涌现，$T_c$ 随调控呈穹顶状 [[../papers/Chen2019superconductivity]]。
*   近公度相由“错位相子”构成的二维网络承载，超导与之共存并受其调控，体现 CDW-超导竞争下穹顶的微观来源。

| 参量 | 行为 | 解读 |
| --- | --- | --- |
| 欠掺杂/弱压力 | Tc 低 | 竞争序（CDW/反铁磁）压制 |
| 最佳点 | Tc 峰值 | 量子临界涨落增强配对 |
| 过掺杂/强压力 | Tc 下降 | 序参量刚度下降 |

## 📚 相关论文 (Related Papers)

- [[../papers/Chen2019superconductivity]]：1T-TiSe₂ 中 CDW 相变与超导涌现，提供二维超导穹顶的实例。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../concepts/superfluid-density|超流密度]]
- [[../entities/TiSe2|二硒化钛 (TiSe2)]]
"""

pages = {
    "anisotropic-superconductivity": p1,
    "multiband-superconductivity": p2,
    "two-gap-superconductivity": p3,
    "superfluid-density": p4,
    "superconducting-dome": p5,
}
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(pages, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("pages:", len(pages))
for k, v in pages.items():
    print(k, len(v))
