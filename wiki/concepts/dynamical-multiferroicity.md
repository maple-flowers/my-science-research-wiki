---
tags: [concept, multiferroicity, magnetoelectric-coupling, sliding-ferroelectricity, ferroelectricity, 2d-materials]
title: 动态多铁性 / Dynamical Multiferroicity
type: concept
status: mature
year: 2025
domain: [multiferroics, quantum-materials]
mechanism: 铁电极化的时间变化率 P×∂tP 感生等效磁矩/磁场，使原本无磁的铁电体系在动力学过程中呈现多铁性耦合
related_concepts: [multiferroicity, magnetoelectric-coupling, ferroelectricity, sliding-ferroelectricity, polarization-switching, phonon-soft-mode, spin-transport, 2d-materials]
papers: [kaurRecentAdvancesTheoretical2025a, spaldinAdvancesMagnetoelectricMultiferroics2019, chenStrongSlidingFerroelectricity2024]
updated: 2026-08-19
---

# 动态多铁性 / Dynamical Multiferroicity

## 👵 太奶导读

乖孙，这一条讲的是「动态多铁性」——这是个很聪明的"借鸡生蛋"思路。一般说"多铁"，得有铁电又有磁性两种序，很难凑。而"动态多铁"妙就妙在：**不需要真的磁性**。只要铁电极化 $P$ 在动（比如被激光脉冲快速翻转），动着的极化就会感生出一点小磁场 $B\propto P\times\partial_t P$，相当于"临时冒充"了磁性。在滑动铁电材料里，超快激光翻极化正好产生这种动态磁矩——虽然只有纳特斯拉量级，但它是"极化动力学自己长出磁"的物理证明。一句话：**"铁电一动就自己长出磁性，不用真磁也能玩多铁"**。

## 🏗️ 结构概览

动态多铁性以极化动力学 $P\times\partial_t P$ 替代静态磁序，实现无静态磁矩的多铁耦合。

![图：多铁性家族树——动态多铁性所处的机制版图](../../raw/figures/spaldinAdvancesMagnetoelectricMultiferroics2019/fig_1_EI832AIH.png)
*   **看图要点**：家族树梳理铁电与磁性各机制分支；动态多铁性属于绕开 d0 禁忌、以动力学耦合实现磁电响应的新思路。
*   **来源**：[[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]

## 🧩 核心机制：极化时间变化率如何感生磁

### 1. 动态多铁性的物理思想

- 静态多铁需要同时存在两种序（如铁电+磁），化学上常有"d0 铁电 vs 磁性 d 电子"的互斥（d0 禁忌）。
- **动态多铁性**绕开该禁忌：不要求静态磁序，而要求**铁电极化随时间变化**——动着的极化相当于"运动电荷"，产生等效电流与磁场。

### 2. 磁矩表达式

$$
M = \frac{S}{2m_e}\frac{e^2}{\hbar}\,\frac{\bar{Z}^*}{\bar{Z}^*_{yy}\bar{Z}^*_{zz}}\,P\times\partial_t P
$$

- $S$ 为面积，$m_e$ 电子质量，$\bar{Z}^*$ 为 Born 有效电荷张量相关量；
- 物理图像：极化振荡 $P(t)$ 的摆线运动感生等效环形电流 → 磁矩 $M$ 与磁场 $B$（Lorentz-Lorenz 型修正）。

### 3. 滑动铁电中的实现

- 滑动铁电双层（如 h-BN）的翻转势垒极低（~meV），可用**倾斜电场或激光脉冲**在 ps 尺度驱动极化翻转/振荡。
- 计算预测：h-BN 中极化做摆线旋转时感生 $M_x\approx 2.7\times10^{-8}\,\mu_B$、$B\approx 12$ nT（TD-DFT 三步机制：电子 pz 激发→电声能量转移→层间滑动→反向极化）。
- 虽然量级很小，但证明了**动力学多铁性**的可行性，为超快磁电探测与器件提供新思路。

### 4. 与一般多铁的对照

- 静态多铁：序参数冻结、随温度/应变切换（如 BiFeO₃）。
- 动态多铁：序参数"运动"本身产生次级耦合，是无静态磁序体系的新型磁电通道。

## 📊 物理参数表

| 参数 | 含义 |
| --- | --- |
| $P\times\partial_t P$ | 极化与其时间变化率的叉积，感生磁的驱动项 |
| $\bar{Z}^*$ | Born 有效电荷（决定耦合强度） |
| 感生磁矩 $M$ | ~$10^{-8}$ μB 量级（h-BN 算例） |
| 感生磁场 $B$ | ~12 nT 量级 |
| 驱动手段 | 倾斜电场/激光脉冲超快翻极化 |

## 🧭 近邻概念辨析

- **与 [[../concepts/multiferroicity|多铁性]]**：多铁强调**静态共存**两种序；动态多铁用**极化动力学**替代静态磁序，是"时间维度"的多铁。
- **与 [[../concepts/magnetoelectric-coupling|磁电耦合]]**：磁电耦合是线性 $\alpha$ 磁电响应；动态多铁是 $P\times\partial_t P$ 型的**动力学**磁电效应。
- **与 [[../concepts/polarization-switching|极化翻转]]**：翻转是手段，动态多铁利用翻转/振荡**过程中的瞬时磁矩**。
- **与 [[../concepts/sliding-ferroelectricity|滑动铁电性]]**：滑动铁电提供超低势垒、可超快翻转的极化平台，是动态多铁的优选宿主。

## 📚 相关论文

- [[../papers/kaurRecentAdvancesTheoretical2025a]]：系统给出滑动铁电中动态多铁性 $P\times\partial_t P$ 的磁矩表达式与 h-BN 算例。
- [[../papers/spaldinAdvancesMagnetoelectricMultiferroics2019]]：确立多铁性家族树框架，为"动力学磁电"提供背景与挑战定位。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：展示强滑动铁电体系的极化可控性，为动态多铁提供材料平台。

## 🔗 关联概念与实体

- [[../concepts/multiferroicity|multiferroicity]]
- [[../concepts/magnetoelectric-coupling|magnetoelectric-coupling]]
- [[../concepts/ferroelectricity|ferroelectricity]]
- [[../concepts/sliding-ferroelectricity|sliding-ferroelectricity]]
- [[../concepts/polarization-switching|polarization-switching]]
- [[../concepts/phonon-soft-mode|phonon-soft-mode]]
- [[../concepts/spin-transport|spin-transport]]
- [[../concepts/2d-materials|2d-materials]]
- [[../entities/BiFeO3|BiFeO3]]
