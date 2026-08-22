---
tags: [concept, dft, exchange-correlation-functional]
title: 'GGA 泛函 / Generalized Gradient Approximation (GGA)'
type: concept
status: developing
domain: [density-functional-theory, electronic-structure, computational-methods]
mechanism: "交换关联能除依赖局域电子密度外，还依赖密度的梯度 ∇n(r)，是介于 LDA 与 meta-GGA/杂化泛函之间的第二档近似"
related_concepts: [exchange-correlation-functional, density-functional-theory, PBE-functional, pw91-functional, DFT-U, paw-method]
papers: [Delley2000]
updated: 2026-08
---

# GGA 泛函 / Generalized Gradient Approximation (GGA)

广义梯度近似（Generalized Gradient Approximation, GGA）是密度泛函理论中交换关联泛函的一个层级：**交换关联能不仅取决于某点的电子密度 $n(\mathbf{r})$，还取决于该点密度的梯度 $\nabla n(\mathbf{r})$**。它是对局域密度近似（LDA，只用 $n(\mathbf{r})$）的第一层修正，在精度与计算量之间取得了良好折中，因而成为固体计算中最常用的一档泛函。PBE、PW91、BP 等都是 GGA 家族的具体实现，本库中它们各有独立条目（[[../concepts/PBE-functional|PBE]]、[[../concepts/pw91-functional|PW91]]）。

## 👵 太奶导读

太奶，算材料里电子的能量，就像估一片地里的收成。最笨的办法（LDA）是只看脚下这一小块地有多肥，就当整片地都这么肥。GGA 聪明一点：它不光看脚下多肥，还看**肥沃程度往哪个方向变、变得多快**（这就是"梯度"）。多看了这一眼，算出来的晶格大小、原子间的软硬就准得多。但它也有个老毛病：碰上一层一层叠起来、层间靠很弱的力粘着的材料（比如石墨），它会把这个弱力算得太弱，把层间距算得太开——所以这类材料还得另外补一项"色散修正"才行。

## 🧩 在泛函阶梯上的位置

交换关联泛函按所依赖的变量构成一条"阶梯"（详见 [[../concepts/exchange-correlation-functional|交换关联泛函]]）：

| 档次 | 依赖量 | 代表 |
| :--- | :--- | :--- |
| LDA | $n(\mathbf{r})$ | PWC、PZ81 |
| **GGA** | $n(\mathbf{r})$、$\nabla n(\mathbf{r})$ | **PBE、PW91、BP、BLYP** |
| meta-GGA | 再加动能密度 $\tau$ | SCAN、TPSS |
| 杂化泛函 | 再混入部分精确交换 | HSE、B3LYP |

GGA 之上的每一档都更贵；固体、特别是大体系与分子动力学场景中，GGA 仍是默认起点，也是 [[../concepts/DFT-U|DFT+U]] 与色散修正的常见基线。

## ⚖️ 与 LDA 的系统性差异

[[../papers/Delley2000|Delley 2000]] 用同一套数值框架对多类固体做了 LDA 与 GGA 的定量对比，给出本页最直接的证据：

- **晶格常数**：LDA(PWC) 系统性**偏小**，BP/PBE 等 GGA 则使晶格**膨胀约 2%**；
- **体模量**：LDA 系统性**偏大**（材料算得过硬），GGA 相应**软化**；
- **对铁电体的意义**：铁电性对晶格常数与应变极其敏感，因此泛函选择直接影响极化与势垒的计算结果——这也是拟合/校验经典势函数时必须固定 DFT 参考泛函的原因。

## ⚠️ 已知失效：层间弱键

GGA 最著名的短板是**范德华层状体系**。[[../papers/Delley2000|Delley 2000]] 指出，石墨的层间弱键在 GGA 下被严重削弱，导致 **c/a 比高估 14–25%**。对本库大量涉及的二维/层状材料（[[../concepts/2d-materials|二维材料]]、[[../concepts/sliding-ferroelectricity|滑动铁电]]等），这意味着：

- 层间距、层间结合能、滑移势垒等量若只用纯 GGA，可能有系统性偏差；
- 需配合 DFT-D 系列色散修正或 vdW-DF 类非局域泛函。

## 🔬 关键参数表

| 参数 | 数值 | 对象与条件 | 证据类型 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| 晶格常数变化 | GGA 相对 LDA 膨胀 ~2% | 多类固体，DMol3 数值框架，BP/PBE vs PWC | 计算对比 | [[../papers/Delley2000]] |
| 体模量 | LDA 偏大、GGA 软化（方向性结论，未给统一百分比） | 同上 | 计算对比 | [[../papers/Delley2000]] |
| c/a 高估 | 14–25% | 石墨层间弱键，纯 GGA 无色散修正 | 计算对比 | [[../papers/Delley2000]] |
| 分子生成焓最优泛函 | B88PW91 表现最优 | 分子集，DMol3 | 计算对比 | [[../papers/Delley2000]] |

> ⚠️ 证据边界：上表全部来自单篇方法学论文，且原文以"数值方法 vs 泛函固有局限"为主线，未针对本库关注的铁电/多铁体系做泛函基准测试。本库其他论文（如 CDW、MXene 类计算）虽普遍**使用** GGA/PBE，但未对泛函本身作对比评估，故不列为本页定量证据。

## 📚 相关论文 (Related Papers)

- [[../papers/Delley2000]]：本页唯一的定量依据。以 DMol3 为框架系统对比 LDA(PWC) 与 GGA(BP/PBE) 在固体上的表现——GGA 使晶格膨胀约 2%、体模量软化，石墨层间弱键在 GGA 下被严重削弱致 c/a 高估 14–25%，并指出计算精度瓶颈在于**所选泛函的固有局限而非数值方法**；分子生成焓中 B88PW91 最优、自洽理论原子参考态可提升 PBE 一致性。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/exchange-correlation-functional|交换关联泛函]]：本页所属的上位概念，泛函阶梯的完整框架。
- [[../concepts/PBE-functional|PBE 泛函]]：GGA 家族中固体计算最常用的具体实现。
- [[../concepts/pw91-functional|PW91 泛函]]：GGA 早期代表实现，B88PW91 组合在分子生成焓中表现最优。
- [[../concepts/density-functional-theory|密度泛函理论]]：GGA 所服务的理论框架。
- [[../concepts/DFT-U|DFT+U]]：GGA 在强关联体系中的常见修正搭配。
- [[../concepts/paw-method|PAW 方法]]：与泛函选择正交的赝势/投影方案，二者共同决定固体计算设置。
- [[../concepts/2d-materials|二维材料]]：GGA 层间弱键失效问题最集中的应用领域。
