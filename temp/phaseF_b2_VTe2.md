---
tags: [entity, material, 2d-material, tmd, cdw, magnetism]
title: 二碲化钒 / Vanadium Ditelluride (VTe2)
type: entity
status: developing
formula: VTe2
class: [transition-metal-dichalcogenide, cdw-material]
properties: [charge-density-wave, 1t-phase, cdw-phases, fermi-surface-nesting, metallicity]
related_entities: [VS2, VSe2, TMDs, MoSe2]
papers: [chenFerromagneticNonmagnetic1T2022, kawakamiChargedensityWaveAssociated2023, lezoualchStudyChargeDensity, wongEvidenceMetallic1T]
updated: 2026-08-18
---

# 二碲化钒 / Vanadium Ditelluride (VTe2)

VTe₂ 是过渡金属二硫族化物（TMDs）中 V 基（VX₂）家族的代表性 CDW 材料。其块体在高温为金属性六方 1T 相，低温经 CDW 相变转变为单斜 1T′ 相（(3×1) 双锯齿链）；单层极限下则展现出不同于块体的 (4×4) CDW 有序。VTe₂ 是研究维度降低、衬底效应、CDW 相竞争与磁性耦合相互作用的理想平台，也是评估"1T′ CDW 态是否可携带磁性"的关键材料。

## 👵 太奶导读

乖孙，VTe₂ 就像一个"电子排队花样特别多"的薄片。同样是排"电荷密度波"的队，它块体时候排成一种样子，变成单个原子层的时候又换一种花样（4×4 排列），说明"薄"和"厚"会改变电子排队的规矩。它还有个悬案：有的理论说它排队时会带上磁性（铁磁），可实验一测——没有！原来是被下面垫的衬底给"压住"了。科学家拿它研究"电子排队（CDW）"和"磁性"之间到底怎么互相影响，以及怎样用掺杂、加电压去指挥它换队形。

## 🏗️ 结构概览

- **晶体结构**：块体为 1T 相（八面体配位）六方结构；低温下通过 CDW 相变转变为单斜 1T′ 相，形成 (3×1) 双锯齿 V 链，相变与层间 Te–Te 耦合密切相关。
- **单层极限**：MBE 生长的单层 VTe₂ 保持金属性 1T 相，V 呈 V⁴⁺（3d¹）电子构型，观察到的 CDW 超结构为 (4×4)，与块体的 (3×1) 不同，证明维度降低改变 CDW 不稳定性。
- **衬底作用**：石墨烯衬底通过抑制 1T′ 相的双锯齿链结构调制，对稳定单层 1T 相起关键作用（wongEvidenceMetallic1T）。

## 🧩 CDW 相与磁性的物理

- **单层金属性与 CDW**：wongEvidenceMetallic1T 通过 MBE 生长单层 VTe₂，结合 STM/STS、ARPES、XAS/XMCD 与 DFT 计算确认其为金属性 1T 相（3d¹ 构型），观察到 (4×4) CDW；XMCD 排除了本征铁磁有序，修正了早期理论预测。
- **费米面嵌套与 CDW 机制**：kawakamiChargedensityWaveAssociated2023 在单层 VS₂ 中发现周期 √21×√21 R10.9° 的条纹状 CDW，其不能由单一 q 矢量解释，而是常规费米面嵌套（q）与高阶嵌套矢量（2q）协同作用的结果，为理解 V 基 TMDs 的非常规 CDW 提供了新框架。
- **1T′ CDW 的磁性机制**：chenFerromagneticNonmagnetic1T2022 揭示 1T′ CDW 态中 FM 与 NM 两种形态的形成机制（CrX₂/VTe₂ 的直接-超交换转变 vs MnX₂ 的金属-金属二聚化），并预言 CrS₂ 中电荷掺杂可诱导 NM↔FM CDW 态可逆相变。
- **多 CDW 相与"CDW 电子学"**：lezoualchStudyChargeDensity 系统研究了 1T-VSe₂/1T-VTe₂ 单层中 (4×4)、(4×1)、(√7×√3) 等多种 CDW 相，建立基于 DFPT 软模的 CDW 结构建模方法，并通过 STM 针尖脉冲实现 CDW 相间可逆切换，提出"CDW 电子学（CDW-tronics）"概念。

## 📚 相关论文 (Related Papers)

- [[../papers/wongEvidenceMetallic1T]]：MBE 单层 VTe₂ 决定性实验基准，确认 1T 金属相、(4×4) CDW 与无本征铁磁，揭示衬底稳定作用。
- [[../papers/kawakamiChargedensityWaveAssociated2023]]：在单层 VS₂ 中提出 q+2q 高阶费米面嵌套协同驱动的 CDW 新机制。
- [[../papers/chenFerromagneticNonmagnetic1T2022]]：阐明 1T′ CDW 中 FM/NM 两种机制与掺杂诱导可逆相变，面向 V/Cr/Mn 基 TMDs。
- [[../papers/lezoualchStudyChargeDensity]]：多 CDW 相建模与 STM 操控，开创"CDW 电子学"应用方向。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/fermi-surface-nesting|费米面嵌套]]
- [[../concepts/electron-correlation|电子关联]]
- [[../concepts/ferromagnetism|铁磁性]]
- [[../entities/TMDs|过渡金属二硫族化物（TMDs）]]
- [[../entities/MoSe2|MoSe₂（同族半导体参照）]]
