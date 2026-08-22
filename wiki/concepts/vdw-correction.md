---
tags: [concept, computational-materials, methodology]
title: 范德华修正 / Van der Waals Correction
type: concept
status: mature
domain: [density-functional-theory, computational-materials, 2d-materials]
mechanism: 在 DFT 框架内对范德华（vdW）色散相互作用进行近似的各种方法统称，用于修正 LDA/GGA 无法描述的长程电子关联
related_concepts: [density-functional-theory, PBE-functional, interlayer-stacking, 2d-materials, sliding-ferroelectricity]
papers: [chenStrongSlidingFerroelectricity2024, cossuStackingChargedensityWaves2024, wuNonvolatileSwitchableHalfmetallicity2024]
updated: 2026-08
---

# 范德华修正 / Van der Waals Correction

范德华修正（vdW correction）指**在密度泛函理论（DFT）计算中，对范德华（色散/伦敦）相互作用进行近似处理的一类方法与术语**。范德华力源于电子密度的瞬时涨落导致的动态偶极-偶极关联，是**非局域**的长程电子关联效应；标准 LDA/GGA 泛函（如 [[../concepts/PBE-functional|PBE]]）在交换关联能中无法正确描述这种非局域关联，导致弱束缚体系的层间距、结合能、剥离能、分子吸附能等被系统性低估。对层状二维材料、分子晶体、吸附体系而言，加入 vdW 修正是得到可靠几何与能量的必要步骤，但同时不同修正方法的精度与副作用差异显著，需要根据体系验证选择。

## 👵 太奶导读

太奶啊，这就好比两张很轻的塑料膜叠在一起，隔远了互相不理，挨近了会轻轻"吸"在一起——这不是磁铁吸的，是膜上电子"抖来抖去"产生的微弱吸引力，叫范德华力。计算机算材料时，老办法（LDA/GGA）算不出这股"抖出来的吸力"，层间距就会算得过大。科学家就想了几招补救：有的给算好的能量"手动加上"一个经验吸引力（D2/D3）；有的换一种更聪明的数学公式把"抖动"算进去（vdW-DF 族）；还有的算得更精细（TS、MBD）。方法不同，算出来的层间距也略有差别——好比量布尺子有长短，得看哪种最准。

## 🧩 范德华力的物理本质与 DFT 的困难

范德华分散力来自原子/分子间电子密度的量子涨落：瞬时偶极诱导邻居产生关联偶极，形成随时间平均为零但瞬时相关的吸引力，其渐进行为正比于 $C_6/R^6$。这类关联是**长程、非局域**的，而 LDA 局域近似与 GGA 半局域近似（仅依赖密度及其梯度）在原理上无法表达。因此纯 DFT 对弱束缚体系的处理需引入额外修正。

## 🧰 vdW 修正方法谱系

| 类别 | 代表方法 | 原理 | 特点 |
| :--- | :--- | :--- | :--- |
| 经验色散修正 | DFT-D2 / DFT-D3 | 加和 $C_6/R^6$ 项（D3 含 $R^{-8}$ 与阻尼函数），系数来自元素/杂化 | 计算便宜、易用；依赖经验参数，金属体系可能过估 |
| 非局域密度泛函 | vdW-DF 族（optPBE-vdW、rev-vdW-DF2、SCAN+rVV10） | 在交换关联能中显式加入非局域关联项 $E_c^{nl}[n]$ | 从头、无体系参数；计算量高于 D3 |
| 成对 TS 方法 | Tkatchenko–Scheffler (TS) | 原子 $C_6$ 系数按有效体积标度，加和成对项 | 比 D3 更物理，但可能过度束缚层状体系 |
| 多体色散 | MBD@FI | 用偶极-偶极响应矩阵耦合各原子涨落偶极，含多体效应 | 精度高，捕捉层间屏蔽与集体效应 |
| 随机相位近似 | RPA（含 vdW 自洽） | 全电子关联的近似求值 | 高精度基准；计算昂贵，难以大规模使用 |

## 📐 对层状材料的关键影响：层间距与结合能

对范德华层状晶体，vdW 修正直接决定层间几何。以 2H-NbSe₂ 双层为例（[[../papers/cossuStackingChargedensityWaves2024]]），不同方法给出明显不同的层间距：

| 方法 | d(Nb–Nb) (Å) | d(Se–Se) (Å) | 备注 |
| :--- | :--- | :--- | :--- |
| 纯 GGA | 6.926 | 3.560 | 无 vdW，层间距显著偏大 |
| GGA+TS | 6.053 | 2.732 | **TS 过度束缚**，层间距过小；混合 blend 无法收敛到正确对称性 |
| GGA+DF (vdW-DF) | 6.527 | 3.141 | 主文采用，与块体实验值 c/2 ≈ 6.27 Å 同量级 |
| GGA+MBD@FI | 6.178 | 2.844 | 多体方法，居中偏紧 |

同一体系下 vdW 处理方法选择甚至影响能否收敛到正确结构与对称性，说明**层状材料计算必须对 vdW 方法做收敛性/对称性检验**。

## 🧪 本库研究中的 vdW 修正实践

- [[../papers/chenStrongSlidingFerroelectricity2024]]：HgI₂ 滑动铁电体第一性原理计算采用 **DFT-D3** 范德华修正；层间结合能 E_b = −24.41 meV/Å²（HgI₂ 体相），属范德华层间作用，滑动铁电的层间滑动势垒与极化计算都建立在正确的层间描述之上。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：Hf₂MnC₂O₂/Sc₂CO₂ 多铁异质结计算默认用 **D3** 修正（截断能 550 eV），并额外用 **optPBE-vdW** 与 **DFT-D2** 交叉验证电子结构与磁各向异性翻转结论的鲁棒性——这是"vdW 方法不影响物理结论"的典型验证范式。
- [[../papers/cossuStackingChargedensityWaves2024]]：CDW 双层堆叠能量景观对 vdW 方法高度敏感（见上表），作者以 GGA+DF 为主结论，并报告 TS/MBD 的差异，示范了多层能量对比中 vdW 方法的系统性检验。

## ⚠️ 使用注意

- **无万能方法**：TS 对某些层状体系过度束缚，D3 在金属/极性体系可能过估，非局域泛函更稳健但更贵；结论应做方法交叉验证。
- **能量 vs 几何**：vdW 修正同时影响层间距、结合能、滑动势垒与剥离能，若只验证能量而忽略几何收敛，可能掩盖问题。
- **与 U 值等联用**：如 DFT-D3 常与 GGA+U 联用（本库 Mn U=4 eV、Sc U=2 eV），修正之间的耦合需单独检查。

## 📋 关键参数表

| 参数 | 数值 | 对象与条件 | 证据类型 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| HgI₂ 层间结合能 | −24.41 meV/Å² | HgI₂ 体相，DFT-D3 | 计算 | [[../papers/chenStrongSlidingFerroelectricity2024]] |
| NbSe₂ 层间距 | 6.926 / 6.527 / 6.053 / 6.178 Å | GGA / GGA+DF / GGA+TS / GGA+MBD@FI | 计算对比 | [[../papers/cossuStackingChargedensityWaves2024]] |
| vdW 交叉验证 | D3 + optPBE-vdW + DFT-D2 | Hf₂MnC₂O₂/Sc₂CO₂ 异质结 | 计算 | [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]] |

## 📚 相关论文 (Related Papers)

- [[../papers/chenStrongSlidingFerroelectricity2024]]：滑动铁电体计算中 DFT-D3 修正的应用与层间结合能报告。
- [[../papers/cossuStackingChargedensityWaves2024]]：系统对比 GGA/TS/DF/MBD 对 CDW 双层层间距与堆叠能量景观的影响。
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]：多铁异质结计算中 D3 默认 + 双 vdW 方法交叉验证的实践。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/density-functional-theory|密度泛函理论（DFT）]]：vdW 修正所依附的计算框架。
- [[../concepts/PBE-functional|PBE 泛函]]：本库各计算默认采用的 GGA 泛函，需 vdW 修正补偿其非局域关联缺失。
- [[../concepts/interlayer-stacking|层间堆叠]]：vdW 修正最直接影响的几何自由度。
- [[../concepts/2d-materials|二维材料]]：弱层间束缚体系，vdW 修正不可或缺。
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]：依赖层间滑动势垒与层间电荷的物理，其定量计算强依赖 vdW 描述。
- [[../concepts/charge-density-wave|电荷密度波（CDW）]]：层间耦合与堆叠能量景观需可靠 vdW 修正。
- [[../entities/VASP|VASP]]：本库第一性原理计算主软件，内置 D3/TS/MBD 等修正。
