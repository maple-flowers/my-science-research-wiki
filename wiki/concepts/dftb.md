---
tags: [concept, density-functional-theory, semiempirical, simulation-method, dftb]
title: dftb
type: concept
status: developing
papers: [Wei2021, Wu2018, Wu2021]
updated: 2026-08-18
---

# dftb

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


dftb（Density Functional Tight Binding，密度泛函紧束缚）是一种介于经验势与全电子 DFT 之间的**半经验量子力学方法**。它基于密度泛函理论的近似展开，将电子结构问题映射为紧束缚形式的哈密顿量求解，在保持一定精度的同时大幅降低计算成本，适合包含数百个原子的大体系与高通量扫描。

## 👵 太奶导读

乖孙，这一条讲的是「DFTB 这套计算方法」。一句话记住它：它是"又快又够准"的量子力学简化版——全电子 DFT 算不动的大体系（几百个原子），用它能在合理时间内算完，还能抓住电荷转移、成键这些关键电子行为。本库用它算过竹节状氮掺杂碳纳米管和硅表面的锗吸附。

## 🧩 核心内容与机制 (Core Content)

- **方法定位**：介于经验势与全电子 DFT 之间的半经验量子方法，适合大体系高通量扫描（[[../papers/Wu2021]]）。
- **SCC-DFTB 变体**：自洽电荷（self-consistent charge）DFTB 通过迭代求解电荷分布，是研究大尺度掺杂纳米体系的有效、经济手段（[[../papers/Wei2021]]）。
- **应用一：竹节状 N-CNTs**：在"氮/碳层交替"模型下，SCC-DFTB 揭示了氮原子环向内收缩、几何/电子性质奇偶振荡、金属性转变与电荷转移等构效关系（[[../papers/Wei2021]]）。
- **应用二：Si(001) 表面 Ge 吸附**：DFTB 计算刻画了单个 Ge 原子及 Ge 二聚体在 Si(001) 表面的稳定吸附位点、表面重构与电荷转移（[[../papers/Wu2018]]、[[../papers/Wu2021]]）。

## 🏷️ 专业名词别名

- `dftb-density-functional-tight-binding`（concepts）
- 实现软件：[[../entities/DFTB+|DFTB+]]（SCC-DFTB 计算软件包）

## 📚 相关论文 (Related Papers)

- [[../papers/Wu2018]] — Study of atomic arrangements and charge distribution on Si(0 0 1) surfaces with the adsorption of one Ge atom by DFTB calculations
- [[../papers/Wei2021]] — Atomic simulations of bamboo-like N-doped CNTs with spaced nitrogen and carbon atoms by DFTB algorithm
- [[../papers/Wu2021]] — Atomic arrangements, bond energies, and charge distribution on Si(0 0 1) surfaces with the adsorption of a Ge dimer by DFTB calculations

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../entities/DFTB+|DFTB+]]：实现 SCC-DFTB 的软件实体页。
- [[../concepts/density-functional-theory|密度泛函理论]]：DFTB 的理论基础。
- [[../entities/bamboo-like-N-CNTs|竹节状氮掺杂碳纳米管]]：DFTB 的主要研究对象之一。
- [[../concepts/nitrogen-doping|氮掺杂]]：DFTB 研究的掺杂体系之一。
- [[../entities/SiGe|SiGe]]：DFTB 研究的表面吸附体系之一。
