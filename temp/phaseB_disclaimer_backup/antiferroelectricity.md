---
tags: [concept]
title: '反铁电性 / Antiferroelectricity'
type: concept
status: mature
papers: ['fengFerroelectricityMultiferroicityTwodimensional2020', 'wuCoexistenceFerroelectricityAntiferroelectricity2024', 'neumayerCompetingPolarPhases2025', 'gaoStrainEngineeringFerroelectric2024', 'xuTwodimensionalFerroelasticityVan2021']
updated: 2026-08-18
---

# 反铁电性 / Antiferroelectricity

反铁电性（antiferroelectricity）指**相邻晶胞的极化方向交替反平行排列、宏观净极化为零**的极性有序态。与铁电体不同，反铁电体的电滞回线呈**双回线（double hysteresis）**特征：低场下净极化为零，高场下被强制极化为铁电单畴。反铁电-铁电相变往往伴随显著应变与能量释放，使其在储能电容器、电卡制冷与非线性介电领域具有独特价值。

## 👵 太奶导读

铁电材料像一排"都朝右看齐"的士兵，整个队伍有一个总方向；反铁电材料则是"相邻两个面对面、互相对着看"——每两个人内部有方向，但整队互相抵消，对外没有方向。你用力"吹哨子"（加大电场）能让他们全部朝右看齐（变成铁电），一放松他们又面对面站回去（回到反铁电）。这个"来回变"的过程能存能量，所以反铁电很适合做储能电容。

## 🏗️ 结构概览

反铁电性属于极性有序态谱系，与铁电、顺电能量接近、可相互转换；其能量学、相变动力学与储能、电卡应用直接相关。二维反铁电（如三层 NiI₂、Sc₂P₂Se₆、TMTPs）为电控磁与超薄储能提供平台。

## 🧩 核心内容与机制 (Core Content)

- **双回线**：低场净极化为零、高场强制进入铁电相，P-E 呈特征双回线，储能密度高。
- **能量竞争**：反铁电与铁电相能量差仅几十 meV/f.u.，温度、电场、应变、离子迁移均可驱动相变（[[../papers/neumayerCompetingPolarPhases2025|Neumayer 2025]]）。
- **电控磁**：二维反铁电-铁电共存体系可实现电驱动磁序切换（[[../papers/fengFerroelectricityMultiferroicityTwodimensional2020|Feng 2020]]、[[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024|Wu 2024]]）。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| 净极化 | 宏观电极化 | 低场为零（反平行排列） |
| 相变电场 | FE-AFE 切换阈值 | 0.8 V/Å 量级 |
| 能量差 | FE/AFE 相能量差 | 几十 meV/f.u. |
| 储能密度 | 双回线包络 | 高（优于普通铁电） |
| 磁控比 | 磁场调控极化翻转 | ~7%（NiI₂） |

## 🔀 近邻概念辨析

- **反铁电 vs 铁电**：反铁电净极化零、双回线；铁电净极化非零、单滞回线。
- **反铁电 vs 顺电**：反铁电存在局部反平行有序，顺电无长程有序；反铁电可被场诱导极化。
- **反铁电 vs 反铁磁**：反铁电是极性序反排，反铁磁是磁矩反排，二者可共存于多铁体系。

## 📚 相关论文 (Related Papers)基本图像：双回线与极性竞争

反铁电体的介电响应由**极性模式与反极性模式竞争**决定：低场下体系处于净极化为零的反铁电相，电场超过阈值后翻转进入铁电相，P-E 曲线呈现特征性的双回线。反铁电序常与铁电序**能量接近（相差几十 meV/f.u. 量级）**，因此温度、电场、离子迁移与应变都可驱动二者可逆转换。

## 🔬 二维体系中的反铁电-铁电共存

- **Sc₂P₂Se₆ / ScCrP₂Se₆ 单层**：DFT 预测 ScCrP₂Se₆ 中 FE 相为反铁磁、AFE 相为铁磁，临界电场约 0.82 V/Å 可在两态间可逆切换，实现**电控磁**（[[../papers/fengFerroelectricityMultiferroicityTwodimensional2020|Feng 2020]]）。
- **三层 NiI₂ 器件**：通过直接的 P–E/I–E 电滞回线与 RMCD 显微术，首次在二维范德华极限下同时证实**面外铁电性与反铁电性共存**，且磁场可调控铁电畴翻转动力学（磁控比 ~7%），直接证明磁电耦合（[[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024|Wu 2024]]）。
- **过渡金属硫/硒磷酸盐（TMTPs）**：以 CuInP₂S₆（CIPS）与 CuInP₂Se₆（CIPSe）为代表，多种能量仅相差几十 meV/f.u. 的铁电、反铁电与顺电相共存竞争，可通过温度、电场、Cu 离子迁移和应变可逆转换（[[../papers/neumayerCompetingPolarPhases2025|Neumayer 2025]]）。

## 🧲 反铁电畸变与铁弹性耦合

β'-In₂Se₃ 的面内铁电畸变与铁弹性内禀耦合：通过单轴/剪切应变可旋转极化方向、降低相变势垒并可逆切换 60°/180° 畴壁，实现铁电畴的"应变编程"（[[../papers/gaoStrainEngineeringFerroelectric2024|Gao 2024]]）；少层 β'-In₂Se₃ 中面内反铁电畸变驱动的二维铁弹性已获实验证实，自发应变约 0.49%（[[../papers/xuTwodimensionalFerroelasticityVan2021|Xu 2021]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in two-dimensional Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]] — Coexistence of ferroelectricity and antiferroelectricity in 2D van der Waals multiferroic
- [[../papers/neumayerCompetingPolarPhases2025]] — Competing polar phases in 2D ferroelectric transition metal thio- and selenophosphates
- [[../papers/gaoStrainEngineeringFerroelectric2024]] — Strain engineering of ferroelectric polarization and domain in the two-dimensional multiferroic semiconductor
- [[../papers/xuTwodimensionalFerroelasticityVan2021]] — Two-dimensional ferroelasticity in van der Waals β'-In2Se3

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：反铁电-铁电相变是反铁电研究的核心。
- [[../concepts/improper-ferroelectricity|非本征铁电性]]：反铁电序常与次级铁电机制相关。
- [[../concepts/multiferroicity|多铁性]]：NiI₂ 中反铁电与磁序共存。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：磁场调控反铁电畴翻转的直接体现。
- [[../concepts/ferroelasticity|铁弹性]]：反铁电畸变与铁弹序的耦合。
- [[../entities/NiI2|NiI₂]]：二维范德华反铁电-铁电共存材料。
- [[../entities/In2Se3|In₂Se₃]]：反铁电畸变驱动的二维铁弹性体系。
*（内容由AI生成，仅供参考）*
