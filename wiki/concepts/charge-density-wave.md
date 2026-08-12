---
title: 电荷密度波 / Charge Density Wave (CDW)
type: concept
status: mature
tags: [concept, phase-transition, electronic-structure, 2D-materials, mott-insulator, dirac-fermions, cdw]
category: [D01, Z01]
domain: phase-transition
mechanism: 电子密度自发周期调制并伴生晶格畸变，由费米面嵌套与电子-声子耦合竞争驱动
related_concepts: [peierls-distortion, electron-phonon-coupling, fermi-surface-nesting, dirac-electrons, mott-insulator, superconductivity, kosterlitz-thouless-transition, commensurate-cdw, soft-mode]
aliases: ["CDW", "Charge Density Wave", "电荷密度波"]
key_quantities:
  wavevector: "q_CDW = 2k_F（Peierls 图像）；实际二维体系常由 q 依赖的电声耦合选择"
  order_parameter: "电荷密度调制 ρ(r)=ρ0+ρQ cos(Q·r+φ)，伴生周期晶格畸变"
  gap: "费米面处打开 CDW 能隙；f-wave 等带节点相可保留金属性/狄拉克费米子"
  examples: "1T-TaS2/TaSe2（√13×√13 大卫之星，Mott-CDW）；2H-NbSe2；1T-VSe2/VTe2（多相竞争）"
papers: [CastroNeto2001charge, nakataRobustChargedensityWave2021, lezoualchStudyChargeDensity, yanDecipheringStabilityTwodimensional2025]
updated: 2026-08
---

# 电荷密度波 / Charge Density Wave (CDW)

电荷密度波（Charge Density Wave, CDW）是固体中一种集体量子态：电子密度发生自发的周期性调制，并伴随晶格的周期畸变（Periodic Lattice Distortion）。在二维材料（过渡金属二硫化物 TMDs、III–V 族半导体等）中，CDW 揭示了电子-声子耦合（EPC）与费米面嵌套（Fermi Surface Nesting）的竞争，并与 Mott 绝缘、超导、拓扑态深刻交织 [[../papers/CastroNeto2001charge]]。

## 👵 太奶导读

太奶，您把晶体里的电子想成一汪汪均匀铺在原子格子上的水。平常时候水铺得平平整整，电荷到处都一样多。可一降温，这水忽然自己漾出一道一道均匀的波纹来——有的地方电荷堆得密、有的地方疏，而且底下的原子也跟着轻轻挪位、皱成同样节奏的格子。这道"电荷的波纹"就是**电荷密度波**，英文叫 CDW。

为啥会起波纹？老说法是"费米面嵌套"：两头的电子波刚好对得上、一拍即合，就把能量降了下来，波矢大约是 $2k_F$。后来发现很多二维材料光靠这个说不通，真正挑大梁的常常是电子和原子振动（声子）之间的耦合——某一根"弹簧"变软、冻住（这就是前面说过的软模），把格子拧出周期花样。更有意思的是波纹的缝法：有的把整个费米面全包住、变成绝缘体；有的缝里留着"节点"，电子还能顺着节点跑，于是进了 CDW 还照样导电，那些电子行为怪异，被叫做狄拉克费米子。像 1T-TaSe2 这类材料，13 个原子凑成一个"大卫之星"的小团，电子被团在一起还能变成 Mott 绝缘体；加压或掺杂把波纹压下去，又可能冒出超导来。所以这"电荷起波纹"不只是个小现象，它连着绝缘、导电、超导一大串名堂。

## 🧩 微观机制：嵌套与电子-声子耦合

传统 CDW 理论基于 **Peierls 不稳定性**：低维体系中费米面的特定部分可被波矢 $q_{CDW}=2k_F$ 嵌套，使磁化率在 $q_{CDW}$ 处发散，诱发晶格畸变并在费米面打开能隙 [[peierls-distortion|Peierls 畸变]]。但现代研究表明，许多 2D 体系（如 2H-NbSe2）中单纯嵌套并不充分，动量空间选择性增强的**强电子-声子耦合**常起主导作用；从晶格动力学看，CDW 对应有限 q 声子的软化冻结（见 [[soft-mode|软模]]），软模所在波矢即给出 CDW 周期。

![图：1T-VSe2 与 1T-VTe2 单层沿高对称路径的声子色散，虚频（负频）软模以负值绘制](../../raw/figures/lezoualchStudyChargeDensity/fig_1_DUEI5PQ5.png)
*   **看图要点**：声子谱中虚频出现的位置就是晶格失稳、将自发畸变为 CDW 的波矢；它直接说明电声耦合（而非纯嵌套）驱动了周期畸变，并据此构建 4×4、4×1 等超结构 [[../papers/lezoualchStudyChargeDensity]]。
*   **来源**：[[../papers/lezoualchStudyChargeDensity]] -> [[../figures/vibrational-spectra|振动能谱与声子谱]]

## 🌀 晶格畸变：从软模到 CDW 超结构

CDW 的"骨架"是周期性晶格畸变。通过 DFPT 声子谱找到虚频软模所在波矢，即可按其本征矢把原子位移、搭出不同的 CDW 超胞（如 4×4、4×1、√7×√3 等），再用 STM 模拟与实验对照确定基态。

![图：1T-VTe2 实验 STM 中 (4×1) 与 (4×4) CDW 相共存（图 3.7）——亮条纹为 (4×1) 条带、右侧为 (4×4) 棋盘](../../raw/figures/lezoualchStudyChargeDensity/fig_3_NDLE7FBC.png)
*   **关键特征**：同一表面上 (4×1) 条带相与 (4×4) 棋盘相紧邻共存，直观证明多种 CDW 超结构能量接近、相互竞争；配合 DFPT 软模本征矢搭出的超胞与模拟 STM 对照，即可逐相指认并由 NEB 评估相间转变能垒 [[../papers/lezoualchStudyChargeDensity]]。
*   **来源**：[[../papers/lezoualchStudyChargeDensity]] -> [[../figures/crystal-structures|晶体结构]]

## ⚡ 狄拉克费米子与金属性 CDW

在某些 TMDs（如 2H-TaSe2）中 CDW 相并不完全绝缘。Castro Neto 提出 **f-wave CDW** 对称性模型：CDW 能隙在费米面上存在节点（zeros），节点处的准粒子激发表现为**狄拉克费米子**，解释了为何部分材料进入 CDW 相后仍保持良好导电性；电子自能修正与关联效应会显著移动相边界 [[../papers/CastroNeto2001charge]]。

![图：基于电子关联修正的 CDW 相图，展示关联强度与 CDW/带节点（狄拉克）金属相的边界](../../raw/figures/CastroNeto2001charge/fig_1_VHUZ3FLK.png)
*   **看图要点**：相图中 CDW 相并非一律打开全带隙——在一定耦合/关联区间保留带节点的金属态（f-wave），节点准粒子即狄拉克费米子，这正是"金属性 CDW"的理论依据 [[../papers/CastroNeto2001charge]]。
*   **来源**：[[../papers/CastroNeto2001charge]] -> [[../figures/electronic-bands|电子能带与态密度]]

## 🎯 维度、关联与竞争序

- **单层 Mott-CDW**：减薄到单层时量子局域化增强、屏蔽减弱，电子关联增强。单层 1T-TaSe2 中 CDW 诱导的能带窄化触发 **Mott 绝缘**转变，并在室温下表现出极高鲁棒性；ARPES/STM 可清晰观测到 $\sqrt{13}\times\sqrt{13}$ 的大卫之星（Star-of-David）畸变 [[../papers/nakataRobustChargedensityWave2021]]。
- **CDW 与超导竞争**：在 2D 极限（如 NbSe2）中，CDW 常与超导共存或竞争；压力/掺杂抑制 CDW 可诱发超导，转变常涉及 Kosterlitz–Thouless（KT）拓扑相变。
- **III–V 族的"积木式"组装**：Yan 等（2025）提出二维 III–V 半导体（GaSb、GaAs）的稳定性取决于轨道杂化（$sp^2$ 与 $sp^3$ 竞争），某些亚稳态中电荷转移与晶格畸变形成周期性调制，可视为广义 CDW 态 [[../papers/yanDecipheringStabilityTwodimensional2025]]。

![图：单层 1T-VSe2 在不同 CDW 相及其异相界面处的电子透射谱与电流-电压曲线](../../raw/figures/lezoualchStudyChargeDensity/fig_7_47SP3LTQ.png)
*   **关键特征**：CDW 相（4×4、4×1）的电导均显著低于未畸变的金属相——周期畸变改变原子间距、压低电子透射率，提供 CDW 的"开/关"；但不同 CDW 相之间电导差异很小，提示多值存储更需依赖畴壁散射或全局相变 [[../papers/lezoualchStudyChargeDensity]]。
*   **来源**：[[../papers/lezoualchStudyChargeDensity]] -> [[../figures/electronic-devices|电子器件与输运]]

## 📊 CDW 关键概念对照

| 维度 | 物理图像 | 典型体系/标志 |
| :--- | :--- | :--- |
| 驱动机制 | 费米面嵌套 vs 电子-声子耦合（软模冻结） | 2H-NbSe2（EPC 主导）、1T-VSe2/VTe2 |
| 波矢 | $q_{CDW}=2k_F$（Peierls）或由 q 依赖 EPC 选择 | 虚频声子所在波矢 |
| 带隙类型 | 全带隙（绝缘）vs 带节点（金属/狄拉克） | f-wave CDW 保留狄拉克费米子 |
| 超结构 | √13×√13 大卫之星、4×4、4×1、√7×√3 | 1T-TaS2/TaSe2、1T-VSe2/VTe2 |
| 竞争序 | Mott 绝缘、超导、拓扑态 | 加压/掺杂抑制 CDW 诱发超导 |
| 表征手段 | ARPES、STM/STS、X 射线散射、Raman、DFPT | 实空间 STM + 倒空间散射 |

## 📚 相关论文 (Related Papers)

- [[../papers/CastroNeto2001charge]]：提出二维 CDW 的 f-wave 对称性、节点与狄拉克费米子、金属性行为。
- [[../papers/nakataRobustChargedensityWave2021]]：单层 1T-TaSe2 中关联增强的鲁棒 CDW 与 √13×√13 大卫之星。
- [[../papers/lezoualchStudyChargeDensity]]：用 DFPT 软模构建 1T-VSe2/VTe2 的多种 CDW 基态并模拟 STM。
- [[../papers/yanDecipheringStabilityTwodimensional2025]]：二维 III–V 半导体稳定性与广义 CDW 畸变的"积木式"组装规则。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[peierls-distortion|Peierls 畸变]]、[[electron-phonon-coupling|电子-声子耦合]]、[[fermi-surface-nesting|费米面嵌套]]、[[soft-mode|软模]]、[[commensurate-cdw|公度 CDW]]、[[dirac-electrons|狄拉克费米子]]、[[mott-insulator|Mott 绝缘体]]、[[superconductivity|超导]]、[[kosterlitz-thouless-transition|Kosterlitz–Thouless 相变]]
- [[../entities/TMDs|TMDs]]（CDW 主要材料家族）
