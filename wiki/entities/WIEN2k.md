---
tags: [entity, density-functional-theory, all-electron-method, lapw, apw-lo, band-structure]
title: WIEN2k
type: entity
status: developing
year: 2020
papers: [Barnett2006coexistence, Johannes2008fermi, Koley2020charge, songEvidenceSinglelayerVan2022]
updated: 2026-08-21
---

# WIEN2k

**WIEN2k** 是一套**全电子（all-electron）**第一性原理计算程序，采用 **APW+lo / 全势线性缀加平面波（FP-LAPW）** 基组。它与本库中更常见的 [[../entities/VASP|VASP]]、[[../entities/Quantum-ESPRESSO|Quantum ESPRESSO]] 的根本区别在于：**不做赝势近似**，芯区波函数被真实求解而非替换。

## 👵 太奶导读

乖孙，算电子结构有两条路子。

**第一条是赝势路（VASP、QE 走这条）**：原子核附近的芯电子不参与化学，波函数在那里剧烈振荡、极难描述。索性把核+芯电子打包换成一个「假的、光滑的」有效势——赝势。这样计算量小得多，对成键、能带这些价电子性质足够准。

**第二条是全电子路（WIEN2k 走这条）**：不换、不糊弄，芯区波函数照实算。办法是把空间切成两块——原子球内用球谐函数配径向解，球外用平面波，两边在球面上接起来。计算贵得多，但**核附近的信息是真的**。

**什么时候必须走第二条？** 当你要的量本身就住在核附近：超精细参数、电场梯度、核磁共振相关量；或者要一个不受赝势构造影响的能带「基准值」，用来校验赝势算得对不对。本库里 WIEN2k 出场的场合，多半是后者——**当作精确参照，或与 VASP 交叉验证**。

记一句话：**WIEN2k 是全电子路线（APW+lo），贵但芯区真实；本库中它主要当基准与交叉验证用。**

## 🧩 定位与本库用法

- **方法本质**：全势 LAPW / APW+lo。空间划分为原子球（muffin-tin）与间隙区，两区基函数在球面匹配；不引入[[../concepts/pseudopotential|赝势]]，故也不受[[../concepts/frozen-core-approximation|冻结芯近似]]之外的赝势化误差影响。
- **与赝势代码的分工**（本库观察到的实际模式）：
  - **取精确能带作为后续有效模型的输入**：先用 WIEN2k 拿到可靠电子结构，再据此构造 Wannier 有效哈密顿量或多体求解器的输入。
  - **交叉验证**：同一物理量用 WIEN2k 与 VASP 各算一遍，一致才采信。
- **常见搭配**：WIEN2k（能带 / 轨道投影）→ Wannier 函数 / DMFT 杂质求解器 / gKNB 模型张量计算。

## 📚 相关论文 (Related Papers)

- [[../papers/Barnett2006coexistence]]：用 WIEN2k 的全势线性缀加平面波方法取得 2H-TaSe₂ 的精确电子结构，再以此为输入、通过新发展的能量分辨 Wannier 函数方法提取低能有效哈密顿量——是本库中「WIEN2k 提供可靠能带、下游构造有效模型」这一分工模式最清楚的实例。
- [[../papers/Johannes2008fermi]]：**同时使用 WIEN2k 与 VASP** 对 NbSe₂、TaSe₂、CeTe₃ 三个体系做第一性原理计算，用以论证费米面嵌套并非这些「教科书式嵌套驱动 CDW」体系的真正主因。双代码并用正是本页所述交叉验证模式，也让其反驳性结论不易被归咎于单一代码的方法学缺陷。
- [[../papers/Koley2020charge]]：用 WIEN2k 计算 2H-TaSe₂ 及其硫掺杂体系的能带与轨道投影，作为后续 DMFT 计算的起点（以多轨道迭代摄动理论 MO-IPT 作杂质求解器，取 U = 1.0 eV、U′ = 0.5 eV）——展示 WIEN2k 作为强关联多体计算前端的用法。
- [[../papers/songEvidenceSinglelayerVan2022]]：在计算 gKNB 模型的 M 张量以预测磁致电极化时**同时采用 VASP 与 WIEN2k 两套代码**，并计入自旋—轨道耦合与 PBE+U 强关联修正；是本页交叉验证用法的第二个实例。

### ⚠️ 已剔除的一条错误声明

原页面还列有 `gajdosLinearOpticalProperties2006`。经核对原始笔记，该文**通篇未使用 WIEN2k**——文中出现的 "Wien" 全部来自作者单位地址（Universität Wien, A-1090 **Wien**, Austria，即维也纳）。这是自动抽取把**城市名误当软件名**所致，已从本页与该文卡片中移除。该文实际是 VASP 框架下的线性光学性质计算。

## 🔗 关联概念与实体 (Related)

- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/LAPW|LAPW]]
- [[../concepts/pseudopotential|pseudopotential]]
- [[../concepts/frozen-core-approximation|frozen-core-approximation]]
- [[../concepts/paw-method|paw-method]]
- [[../concepts/wannier-function|wannier-function]]
- [[../concepts/DFT-U|DFT-U]]
- [[../concepts/fermi-surface-nesting|fermi-surface-nesting]]
- [[../entities/VASP|VASP]]
- [[../entities/Quantum-ESPRESSO|Quantum-ESPRESSO]]
