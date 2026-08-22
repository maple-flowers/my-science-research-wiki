---
tags: [concept, electrochemistry, electrocatalysis, electrochemical-deposition, oxygen-reduction-reaction, oxygen-evolution-reaction]
title: overpotential
type: concept
status: developing
year: 2025
papers: [wangTwodimensionalFerroelectricMetal2025, Blessing2026optical]
updated: 2026-08-21
---

# overpotential

**过电位（overpotential, η）** 指为使电化学反应以可观速率实际进行，所必须在**热力学平衡电位之外额外施加**的那一部分电压。它是电化学过程中「白交的学费」——越小越好。

⚠️ 注意：这个词在本库的两类工作中含义并不相同，读前必须分清，见下方辨析。

## 👵 太奶导读

乖孙，做电化学反应，理论上需要多大电压是算得出来的——比如水分解，热力学告诉你 1.23 V 就够。可你真的只加 1.23 V，反应几乎不动。

**必须多加一点，反应才跑得起来，多加的这部分就叫过电位。**

这部分电压不产出任何东西，纯粹是为了推动反应克服路上的坎，最后变成热耗散掉。所以做催化剂的人一辈子在干一件事：**把过电位往下压**。压下来 0.1 V，整个电解槽的电费就省一大截。

坎在哪儿？反应不是一步完成的，是分好几步走（比如氧还原要经过 OOH*、O*、OH* 几个中间态）。给足 1.23 V 之后，多数步骤会变成「下坡路」自动往前走，但总有一步还是「上坡」——**这个最陡的上坡就是瓶颈，它有多高，过电位就有多大**。这一步叫电位决定步骤（PDS）。

所以改进催化剂的关键不是让所有步骤都变好，而是**专门把最陡那一步削平**。

记一句话：**过电位 = 热力学电压之外额外要加的那部分 = 反应路径上最陡那一步的高度。**

## 🧭 近邻概念辨析：同一个词的两种用法

| 场景 | 含义 | 判据 | 本库来源 |
|---|---|---|---|
| **电催化**（ORR/OER） | 驱动反应达可观速率所需的额外电压，反映**动力学代价** | 施加平衡电位后最大的上坡步（PDS）的高度 | [[../papers/wangTwodimensionalFerroelectricMetal2025\|wang2025]] |
| **电化学沉积**（ECD） | 沉积电压超出平衡值的部分，反映**成膜条件的剧烈程度** | 过电位过大 → 引入晶格应变与点缺陷 | [[../papers/Blessing2026optical\|Blessing2026]] |

两者数学定义同源，但优化方向相反：催化中过电位**越小越好**；沉积中过电位是**工艺旋钮**，过小则不沉积、过大则损伤薄膜，存在最优值。切勿把 ECD 的「11 V 最优」当作催化过电位来读。

## 🧩 催化语境下的机制链

1. **U = 0 时看自发性**：ORR 的各步在零电位下全为下坡（热力学自发）；OER 相反，各步全为上坡。
2. **施加平衡电位 U = 1.23 V**：部分步骤翻转为上坡，其中**最大的上坡步即电位决定步骤（PDS）**。
3. **η = PDS 的能垒高度**（除以电子数换算为电压）。
4. **PDS 的位置会变**：改变催化剂表面即可改变瓶颈落在哪一步——例如 CuCrS₂ 的 P⁻ 表面 PDS 在末步 `OH* → H₂O`，而 P⁺ 表面移到第三步 `O* → OH*`。**极化反转改变了反应路径的瓶颈本身**，不只是改变了高度。
5. **背后的准则是萨巴蒂尔原理**：中间体吸附既不能太弱（活化不了）也不能太强（脱附不了）；过电位在吸附强度「恰到好处」处取极小。

### 本库中的过电位数值

| 体系 / 表面 | 反应 | 过电位 | 对照 | 性质 |
|---|---|---|---|---|
| 三层 CuCrS₂，P⁺ | ORR | **0.28 V** | Pt 基约 0.45 V | 计算预测 |
| 三层 CuCrS₂，P⁻ | ORR | 0.70 V | 同体系 P⁺ 的 2.5 倍 | 计算预测 |
| CuCrSe₂ | ORR | > 1.0 V | 吸附过强，PDS 落在首步 `O₂→*OOH` | 计算预测 |
| 双层 / 三层 CuCrS₂，P⁺ | OER | **0.43 V** / 0.50 V | IrO₂ 为 0.56 V | 计算预测 |

⚠️ **边界（作者自陈）**：以上全为**理论值**，基于理想周期性平板模型与计算氢电极（CHE）模型，**忽略了电解液、溶剂离子、施加电位下的双电层效应与表面缺陷**。0.28 V 在真实三电极体系中能否复现尚未验证。引用这些数字时必须带上「计算预测」的限定。

## 📚 相关论文 (Related Papers)

- [[../papers/wangTwodimensionalFerroelectricMetal2025]]：本页催化语境下机制链与全部数值的来源。该文完整演示了「U=0 判自发性 → U=1.23 V 定 PDS → PDS 高度即过电位」的标准判定流程，并给出本页最有信息量的一条观察：铁电极化反转不仅改变过电位大小，还**改变 PDS 落在哪一步**（P⁻ 的 `OH*→H₂O` vs P⁺ 的 `O*→OH*`），说明极化是通过重塑整条反应路径而非单点调节来影响催化的。同时作者自陈了 CHE 理想模型忽略电解液与双电层的局限。
- [[../papers/Blessing2026optical]]：提供本页第二种用法的唯一来源。该文在 SnTe 电化学沉积中观察到 12–13 V 的**较高沉积电压使过电位增大，引入晶格应变与点缺陷，从而拓宽光学带隙**；11 V 时化学计量比最佳、带隙中缺陷态最少。它说明在沉积语境下过电位是决定薄膜微结构的工艺参数，与催化语境下「越小越好」的取向截然不同。

## 🔗 关联概念与实体 (Related)

- [[../concepts/electrocatalysis|electrocatalysis]]
- [[../concepts/oxygen-reduction-reaction|oxygen-reduction-reaction]]
- [[../concepts/oxygen-evolution-reaction|oxygen-evolution-reaction]]
- [[../concepts/electrochemical-deposition|electrochemical-deposition]]
- [[../concepts/optical-band-gap|optical-band-gap]]
- [[../entities/CuCrSe2|CuCrSe2]]
