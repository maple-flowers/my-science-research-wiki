---
tags: [concept]
title: 'lapw'
type: concept
status: developing
papers: ['blochlProjectorAugmentedwaveMethod1994b']
updated: 2026-08-18
---

# lapw

线性缀加平面波方法（linearized augmented plane wave, LAPW）是一类基于**全电子（all-electron）**理念的第一性原理电子结构计算方法。它在"原子球（muffin-tin）内用径向函数展开、球间区域用平面波展开"的缀加平面波（APW）框架上引入"线性化"处理，避免了 APW 中能量依赖基函数的非线性本征值问题，从而能以较少基函数高精度描述包含局域轨道（如 d、f 电子）的体系，是 WIEN2k、ELK 等成熟代码的物理基础。

## 👵 太奶导读

太奶啊，算电子结构就像"给原子画全家福"。原子核附近电子绕得紧（像内圈），远离核的地方电子散开（像外圈）。LAPW 的办法是"里圈用量身定做的数学函数、外圈用平整的平面波"，再把两段接起来——这样内圈的 d 电子、f 电子也算得准，不怕"画糊"。铁电、磁性这些有局域电子的材料，常靠它算得精确。

## 🧩 核心内容与机制 (Core Content)

- **全电子处理**：LAPW 不采用赝势，显式包含芯态与价态全部电子，对局域轨道体系（过渡金属、稀土）尤其准确。
- **Muffin-tin 分区**：空间划分为原子球内（径向函数 × 球谐）与球间区（平面波）两部分，衔接处要求函数值与导数连续。
- **线性化**：将能量依赖的径向函数在固定能量附近 Taylor 展开，使基函数不再依赖本征能量，把非线性问题化为标准线性本征值问题。
- **LAPW 族**：包括 FLAPW（全势线性缀加平面波）、APW+lo（追加局域轨道）等变体，兼顾精度与效率。
- **与 PAW/赝势方法对比**：PAW（如 VASP 采用）通过变换保留全电子精度但使用赝势基；LAPW 直接处理真实势，二者精度相当，LAPW 更"直接"而计算量更大。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/paw-method|PAW 方法]]：投影缀加平面波，另一主流全电子精度方案。
- [[../concepts/density-functional-theory|密度泛函理论]]：LAPW 是 DFT 的高精度求解途径之一。
- [[../concepts/band-structure|能带结构]]：LAPW 常用于精确能带与态密度计算。
- [[../entities/VASP|VASP]]：基于 PAW/平面波的主流 DFT 软件，常与 LAPW 结果互验。
- [[../concepts/PBE-functional|PBE 泛函]]：LAPW 计算常用的交换关联近似。

## 📚 相关论文 (Related Papers)

- [[../papers/blochlProjectorAugmentedwaveMethod1994b]] — Projector augmented-wave method

## 🏷️ 专业名词别名

- `lapw`（concepts）
- `lapw`（entities）
- `LAPW`（entities）
