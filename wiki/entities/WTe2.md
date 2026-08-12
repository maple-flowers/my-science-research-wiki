---
tags: [entity, material, 2D, vdW, TMD, ferroelectric-metal, topological-semimetal, sliding-ferroelectricity]
title: 二碲化钨 / Tungsten Ditelluride (WTe2)
type: entity
status: mature
category: [D01, Z02]
formula: WTe2
aliases: ["WTe₂", "tungsten ditelluride"]
class: [TMD, 1T-prime-Td-phase, semimetal, topological]
properties: [ferroelectric-metal, sliding-ferroelectricity, weyl-semimetal, giant-magnetoresistance, quantum-spin-hall, superconductivity]
related_entities: [TMDs, MoTe2, CrTe2]
key_quantities:
  P_out_bilayer: "~0.42 pC/m（双层实验值）"
  switching_temperature: "~350 K（双层/三层电滞回线）"
  monolayer_Tc_SC: "~1 K（静电掺杂下单层超导）"
  sliding_path: "沿 b 轴 ~0.49–0.72 Å，能垒 ~0.3–0.6 meV/cell（理论）"
  note: "单层无电滞回线，证明极化来自层间电荷重排而非本征离子位移"
papers: [feiFerroelectricSwitchingTwodimensional2018a, guoAdvancesTwodimensionalFerroelectric2025, zhaoRealization2DMultiferroic2024]
updated: 2026-08
---

# 二碲化钨 / Tungsten Ditelluride (WTe2)

WTe2 是过渡金属二硫化物（TMD）家族的"异类"：它是半金属而非半导体，并集**铁电金属性、Weyl 半金属、巨磁阻、量子自旋霍尔边缘态与门压可调超导**于一身。2018 年，双层/少层 WTe2 成为**首个被实验证实的二维滑移铁电体**——在金属性导电背景下，垂直电场仍可非易失地翻转面外极化，打破了"金属中自由电子必屏蔽偶极、故不能铁电"的传统认知 [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]。

## 👵 太奶导读

太奶，照老理儿说，能导电的金属是做不成"铁电"（能记住电方向）的：金属里自由电子太多，一点电荷偏向立刻被它们中和抹平了，就像在水坑里垒不住沙堡。可这 WTe2 偏破了规矩——它一边能导电，一边还能记住电的方向，所以叫"铁电金属"。

它的机关不在原子搬家，而在"搓牌"：两层 WTe2 薄片沿某一方向轻轻错开一点点，两层交接处的电子云就不对称了，攒出一个垂直方向的电偏向；再往回一搓，偏向就反过来。单层时没这个效应（因为没有"两张牌"可搓），两层三层才出现能记住的电回线，这恰好证明电方向来自层与层之间，而不是某层内部。开关它所需能量极小，速度又快，适合做极省电的存储器。顺带一说，这材料还是块"多面宝玉"：厚厚的时候是 Weyl 半金属、有不饱和巨磁阻；薄薄一层时边缘导电、中间绝缘（量子自旋霍尔效应）；调一调门电压还能变超导。

## 🏗️ 结构概览

WTe2 稳定相为畸变的 1T′（$T_d$）相：W 原子链沿晶体 a 轴方向排列，Te 八面体发生畸变使层内出现一维 W 链。层间为弱范德华结合，双层沿 b 轴的微小相对滑移即可改变层间电荷分布。

![图：WTe2 滑移铁电的层数依赖电滞回线、Hirshfeld 层间电荷与拉曼剪切模证据（a–e）](../../raw/figures/guoAdvancesTwodimensionalFerroelectric2025/fig_4_2X9UPMDA.png)
*   **看图要点**：WTe2 占据左半 (a–e)：双层/三层出现显著电滞回线而单层无回线，直接证明铁电性来自层间电荷重排；Hirshfeld 电荷分析量化层间近邻 Te 原子的电荷转移；极化反转伴随剪切拉曼模的消失/相变（$T_d\to1T'\to T_d$）[[../papers/guoAdvancesTwodimensionalFerroelectric2025]]。
*   **来源**：[[../papers/guoAdvancesTwodimensionalFerroelectric2025]] -> [[../figures/vibrational-spectra|振动能谱与声子谱]]

## 🧩 滑移铁电与金属性共存

- **实验起源**：Fei 等 2018 年在双层 WTe2 中测得面外极化的非易失电场翻转（Nature 560, 336），双层/三层有电滞回线、单层无，转变温度约 350 K [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]。
- **微观机制**：层间沿 b 轴滑移约 0.49–0.72 Å 触发层间电荷重分布，能垒仅约 0.3–0.6 meV/cell；奇数层因中间偶数层需反向滑移而极化减弱，块体则因电子屏蔽抑制铁电 [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]。
- **极化强度**：双层实验面外极化约 $0.42\text{ pC/m}$；后续高通量筛选把它作为金属铁电极化的基准对照（众多新预测材料 0.43–9.61 pC/m）[[../papers/zhaoRealization2DMultiferroic2024]]。
- **相变指纹**：SHG 蝴蝶型滞后曲线与拉曼剪切模消失表明极化反转伴随 $T_d\leftrightarrow1T'$ 结构相变。

## 🔬 拓扑与关联物性

- **Weyl 半金属**：块体 WTe2 是第 II 类 Weyl 半金属，并具有不饱和的巨磁阻（XMR）。
- **量子自旋霍尔效应**：单层 WTe2 是本征二维拓扑绝缘体，体相绝缘而边缘呈现受拓扑保护的导电通道。
- **门压超导**：单层 WTe2 在静电掺杂下出现本征超导电性，$T_C\sim1$ K，使其成为研究拓扑、铁电与超导耦合的平台。

> **说明**：早期草稿曾把 Huang 等 2019 年关于 **MoTe2** 极性畴壁、以及关于 **HgI2/HgBr2** 强滑移铁电的工作归到 WTe2 名下，均属张冠李戴，已移除；WTe2 的铁电金属性以 Fei 2018 为准。

## 📊 主要物性参数

| 参数 | 数值 | 备注 |
| :--- | :--- | :--- |
| 双层面外极化 $P_{out}$ | ~0.42 pC/m | 实验值 |
| 转变温度 | ~350 K | 双层/三层电滞回线 |
| 滑移距离 | ~0.49–0.72 Å（沿 b 轴） | 能垒 ~0.3–0.6 meV/cell |
| 单层超导 $T_C$ | ~1 K | 静电掺杂 |
| 磁阻 | 不饱和巨磁阻（XMR） | 块体 II 类 Weyl 半金属 |
| 材料家族 | TMD（1T′/Td） | 铁电金属 & 拓扑半金属 |

## 📚 相关论文 (Related Papers)

- [[../papers/feiFerroelectricSwitchingTwodimensional2018a]]：Nature 2018，首次实验证实二维金属（双层 WTe2）的铁电开关。
- [[../papers/guoAdvancesTwodimensionalFerroelectric2025]]：综述 WTe2 作为首个滑移铁电体的机制、层数依赖与拉曼/SHG 证据。
- [[../papers/zhaoRealization2DMultiferroic2024]]：多铁高通量筛选，以 WTe2（0.42 pC/m）为金属铁电极化基准。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectric-metal|铁电金属]]、[[../concepts/sliding-ferroelectricity|滑动铁电性]]、[[../concepts/interfacial-charge-rearrangement|层间电荷重排]]、[[../concepts/weyl-semimetal|Weyl 半金属]]、[[../concepts/quantum-spin-hall-effect|量子自旋霍尔效应]]、[[../concepts/superconductivity|超导]]、[[../concepts/polarization-switching|极化翻转]]
- [[../entities/TMDs|TMDs]]、[[../entities/MoTe2|MoTe2]]（同族 1T′ 相极性畴壁体系）、[[../entities/CrTe2|CrTe2]]（金属性磁性对照）
