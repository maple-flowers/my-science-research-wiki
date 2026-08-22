---
tags: [concept]
title: '自旋密度波 / Spin Density Wave'
type: concept
status: developing
papers: ['Makogon2012wave', 'Kang2012dimer', 'krishnamurthiSpinChargeDensity2020', 'cheongMultiferroicsMagneticTwist2007a']
updated: 2026-08-18
---

# 自旋密度波 / Spin Density Wave

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


自旋密度波（spin density wave, SDW）指**电子自旋密度沿实空间呈现周期性调制**的磁有序态，常见于低维或嵌套费米面体系，是反铁磁性的一种波状形式。SDW 与电荷密度波（CDW）常相伴而生，是理解铁基超导体、铬金属与过渡金属硫族化合物边界态的磁基态的关键概念。

## 👵 太奶导读

普通反铁磁像"黑白棋盘"，自旋一正一反交替；SDW 更"文艺"：自旋密度像水波一样，沿某个方向周期性起伏——有的地方自旋多、有的地方自旋少，甚至自旋方向也周期性旋转。这种"磁波"常在电子结构有特殊嵌套的材料中出现，还常和电荷密度波"搭伴"出现。

## 🧩 SDW 与电子结构

- **自旋-电荷密度波不可分**：二维光晶格"方圆形"费米面因不完全嵌套失稳，SO(3,1)×SO(3,1) 广义 RPA 证明其为自旋与电荷涨落不可分割的耦合有序态（SCDW）；将自旋与电荷分开处理会显著低估临界相互作用强度（[[../papers/Makogon2012wave|Makogon 2012]]）。
- **口袋密度波**：铁基超导体中钴杂质周围 STM 二聚体共振被解释为口袋密度波（PoDW）序导致的费米面重构与轨道选择性各向异性（[[../papers/Kang2012dimer|Kang 2012]]）。

## 🧩 SDW 与边界拓扑

TMDC 镜像孪晶界的金属性源于 Z₃ 拓扑不变量在边界处的反转，导致边界态 1/3 分数占据并自发形成**纯电子型三重周期 SDW/CDW**，打开约 0.1 eV 能隙，预言携带 ±1/3 e 分数电荷的孤子激发（[[../papers/krishnamurthiSpinChargeDensity2020|Krishnamurthi 2020]]）。

## 🧩 与多铁的关联

SDW 型（共线）磁序经交换伸缩机制可破缺空间反演产生磁致电极性，属于磁致多铁路径之一（[[../papers/cheongMultiferroicsMagneticTwist2007a|Cheong 2007]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Makogon2012wave]] — Spin-charge-density wave in a rounded-square Fermi surface for ultracold atoms
- [[../papers/Kang2012dimer]] — Dimer impurity scattering, reconstructed Fermi-surface nesting, and density-wave diagnostics in iron pnictides
- [[../papers/krishnamurthiSpinChargeDensity2020]] — Spin/charge density waves at the boundaries of transition metal dichalcogenides
- [[../papers/cheongMultiferroicsMagneticTwist2007a]] — Multiferroics: a magnetic twist for ferroelectricity

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]：SDW 的电荷伴侣。
- [[../concepts/antiferromagnetism|反铁磁性]]：SDW 的磁序背景。
- [[../concepts/magnetic-frustration|磁阻挫]]：复杂磁序的起源。
- [[../concepts/spin-spiral|自旋螺旋]]：SDW 的非共线变体。
- [[../concepts/density-functional-theory|密度泛函理论]]：计算 SDW 基态的方法。
- [[../entities/iron-pnictides|铁基超导体]]：PoDW 诊断对象。
