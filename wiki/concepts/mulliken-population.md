---
tags: [concept]
title: 'mulliken-population'
type: concept
status: developing
papers: ['Wu2018', 'Wei2021', 'tangGridbasedBaderAnalysis2009', 'Wu2021']
updated: 2026-08-18
---

# mulliken-population

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


Mulliken 布居分析（Mulliken population analysis）是一种**把分子/晶体轨道上的电子电荷按基函数分配到各原子的统计方法**，用以定量原子电荷、键级与电荷转移。它与 Bader 分析同为主要电荷布居方案，常用来讨论异质结、吸附与氧化还原过程中的电荷转移方向与幅度。

## 👵 太奶导读

太奶啊，材料里的电子到底"属于"哪个原子？这问题看着简单却难说清——电子在原子间晃悠。Mulliken 分析的办法是：把每个轨道上的电子按"这个轨道偏向哪个原子"粗略分成份儿，加总成每个原子的"占有电荷"。用它能看出电子从哪个原子"搬家"到哪个原子（电荷转移）、键强不强，是化学里最常用的"分家"办法之一。

## 🧩 核心内容与机制 (Core Content)

- **方法要点**：基于基函数的重叠矩阵与密度矩阵计算原子布居：q_A = Σ_i (P·S)_ii（对原子 A 的基函数求和）；键级由重叠布居给出（本库电荷转移与吸附论文）。
- **原子电荷**：给出原子净电荷（形式电荷 + 布居修正），定性反映氧化态与电荷转移方向。
- **局限**：对基函数（尤其是弥散/极化基）依赖较强，数值可能不唯一；常与 Bader 分析（bader-analysis）或 Hirshfeld 分析对比。
- **应用**：异质结层间电荷转移（interlayer-charge-transfer）、催化吸附（供电子/吸电子）、金属配位化学（本库 XPS 结合能位移配合）。
- **与实验对照**：布居电荷与 XPS 芯能级位移、红外峰位趋势定性一致。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/bader-analysis|Bader 分析]]：另一类电荷布居方法。
- [[../concepts/charge-transfer|电荷转移]]：布居分析的主要应用。
- [[../concepts/density-functional-theory|密度泛函理论]]：布居计算的框架。

## 📚 相关论文 (Related Papers)

- [[../papers/Wu2018]] — Study of atomic arrangements and charge distribution on Si(0 0 1) surfaces with the adsorption of one Ge atom by DFTB calculations
- [[../papers/Wei2021]] — Atomic simulations of bamboo-like N-doped CNTs with spaced nitrogen and carbon atoms by DFTB algorithm
- [[../papers/tangGridbasedBaderAnalysis2009]] — A grid-based Bader analysis algorithm without lattice bias
- [[../papers/Wu2021]] — Atomic arrangements, bond energies, and charge distribution on Si(0 0 1) surfaces with the adsorption of a Ge dimer by DFTB calculations

## 🏷️ 专业名词别名

- `mulliken-population-analysis`（concepts）
