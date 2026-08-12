---
tags: [concept, phase-transition, phonon, ferroelectricity, charge-density-wave, mechanism]
title: 软模 / Soft Mode (Phonon Softening)
type: concept
status: mature
category: [Z01]
domain: phase-transition
mechanism: 某支振动模频率随温度/参数趋近相变点而软化至零（虚频），其冻结引发对称破缺相变
related_concepts: [soft-mode-theory, soft-mode-phonon, charge-density-wave, commensurate-cdw, electron-phonon-coupling, fermi-surface-nesting, peierls-distortion, dfpt]
aliases: ["声子软模", "虚频", "Soft Phonon", "phonon softening", "soft-mode"]
key_quantities:
  criterion: "ω²→0（DFPT 中表现为虚频/负频率）是晶格失稳并发生位移型相变的标志"
  ferroelectric: "Γ 点横光学(TO)模软化冻结 → 自发极化（位移型铁电）"
  cdw: "有限 q 声子虚频冻结 → 周期晶格畸变 + 电荷密度调制（CDW）"
papers: [Makogon2012wave, junqueraCriticalThicknessFerroelectricity2003, lezoualchStudyChargeDensity, xuTunableFerroelectricTopological2022]
updated: 2026-08
---

# 软模 / Soft Mode (Phonon Softening)

**软模（Soft Mode）** 是位移型结构相变的统一图像：在中心对称的高温相中，某支晶格振动模（通常是横光学声子 TO 或有限波矢声子）的恢复力随温度（或其他控制参数）趋近相变点而减弱，其频率 $\omega$ 不断降低（"软化"），在临界点满足 $\omega^2\to0$，随后该模在低温相"冻结"为静态的原子集体位移，从而降低对称性并产生有序相。在密度泛函微扰理论（DFPT）声子计算中，软模表现为**虚频（负频率）**，是识别晶格失稳、据此构建畸变超胞的关键标志。它同时是 [[charge-density-wave|电荷密度波]] 与位移型 [[ferroelectricity|铁电]] 相变的核心语言 [[../papers/Makogon2012wave]] [[../papers/lezoualchStudyChargeDensity]]。

## 👵 太奶导读

太奶，您把晶体想成一张弹簧床，每个原子是床上的弹珠，弹簧就是原子间的作用力。常温下弹簧挺有劲，弹珠被碰一下会"嗡"地振动（这就是"声子"，即原子集体振动的小名）。可要是把温度往临界点降，某一根弹簧越变越软，弹珠一推就回不来了——振动频率越来越低，低到最后干脆为零，弹珠顺势歪到一个新位置停住，整张床的对称花样就此变了。这根"软到塌掉"的弹簧就叫**软模**。

软模分两种用场。一种歪在整张床的"中心"（专业叫 Γ 点）上：所有弹珠统一往一边挪，正负电荷中心错开，就生出一个统一的电方向，这就是普通的**铁电相变**。另一种歪出一段重复的波浪花样（某个非零波矢 q）：弹珠一会儿密一会儿疏，电荷密度跟着周期起伏，床面皱成一道道菜畦，这就是**电荷密度波（CDW）**。在计算机里算原子振动时，软塌的弹簧会显示成"虚"的频率（负数），研究者一看到虚频，就知道这结构不稳、要变形，于是照着那个振动方向把原子挪一挪，就能搭出新相的模型。一句话：软模就是"相变前先变软的那根弹簧"。

## 🧩 物理图像

软模理论把相变归结为简谐频率随温度的坍缩：设软模频率 $\omega_0^2(T)\propto(T-T_c)$，当 $T\to T_c^+$ 时 $\omega_0\to0$，相应振动模的静态响应（极化率）发散；在 $T<T_c$ 时，该模的位移坐标 $Q$ 取得非零静态值，成为新相的序参量。软模可由多种因素驱动——电声耦合、费米面嵌套、应变或电子关联，但其共同指纹是"一支特定声子在特定波矢处的软化与冻结"。

![图：冷原子/晶格模型中动态磁化率随耦合增强涌现软模——接近临界强度时能量在波矢 Q 处趋于零](../../raw/figures/Makogon2012wave/fig_2_DZDKDGH8.png)
*   **看图要点**：动态响应谱在特定波矢 **Q** 处随参数逼近临界点而出现一支频率趋近于零的激发（软模），标志连续相变与新有序态（此处为自旋-电荷密度波）的形成；这把"软模→在 Q 处冻结"的一般机制可视化 [[../papers/Makogon2012wave]]。
*   **来源**：[[../papers/Makogon2012wave]] -> [[../figures/vibrational-spectra|振动能谱与声子谱]]

## ⚡ 铁电软模

在位移型铁电体中，软化的是 **Γ 点横光学（TO）声子**。该模描述正、负离子亚晶格的相对反向位移，其冻结使正、负电荷中心错开，产生宏观自发极化。经典钙钛矿（如 BaTiO3）的铁电相变即由中心阳离子相对于氧八面体的软模位移驱动。软模的恢复力与短程排斥（ favor 中心对称）和长程库仑/杂化（ favor 极性位移）竞争有关；后者胜出即软模坍缩。Junquera 与 Ghosez 还表明，在真实电极的铁电电容器中，退极化场会改变软模稳定性，使铁电性存在一个约 24 Å（约 6 个 BaTiO3 层）的临界厚度 [[../papers/junqueraCriticalThicknessFerroelectricity2003]]。

## 📈 CDW 软模

在电荷密度波体系中，软化发生在**有限波矢 q = Q_CDW**（而非 Γ 点）。该声子冻结后形成周期晶格畸变，并伴随电荷密度的正弦调制与能隙打开。

![图：1T-VSe2 与 1T-VTe2 单层沿高对称路径的声子色散，虚频（负频）软模以负值绘制](../../raw/figures/lezoualchStudyChargeDensity/fig_1_DUEI5PQ5.png)
*   **关键特征**：声子谱中出现虚频即表明晶格在绝对零度下不稳定、会自发畸变成 CDW 相；虚频所在的波矢直接给出 CDW 周期。据此可用 DFPT 识别软模并构建 4×4、√7×√3、4×1 等 CDW 超胞——这是"从软模到畸变结构"方法的起点，也说明 CDW 驱动力与电声耦合密切相关，而不仅是费米面嵌套 [[../papers/lezoualchStudyChargeDensity]]。
*   **来源**：[[../papers/lezoualchStudyChargeDensity]] -> [[../figures/vibrational-spectra|振动能谱与声子谱]]

## 🔬 计算识别方法

- **DFPT 声子谱**：在原胞中计算声子色散，虚频出现的波矢与极化矢量即指明失稳模；按软模本征矢位移原子可构建低对称超胞。
- **电声耦合 / 磁化率**：用 $\chi(\mathbf{q})$、电声矩阵元 $\lambda_\mathbf{q}$ 判断软模是由费米面嵌套还是电声耦合主导。
- **能量-畸变曲线**：沿软模坐标扫描能量，得到双势阱（铁电）或周期势（CDW），确定势垒与畸变幅度 [[../papers/xuTunableFerroelectricTopological2022]]。

## 📊 两类软模对照

| 维度 | 铁电软模 | CDW 软模 |
| :--- | :--- | :--- |
| 软化波矢 | Γ 点（$\mathbf{q}=0$） | 有限 $\mathbf{q}=\mathbf{Q}_{CDW}$ |
| 冻结结果 | 离子亚晶格相对位移 → 自发极化 | 周期晶格畸变 + 电荷密度调制 |
| 典型体系 | BaTiO3、PbTiO3 等钙钛矿 | 1T-TaS2、1T-VSe2/VTe2 |
| 计算指纹 | Γ 点 TO 虚频 | 有限 q 声子虚频 |
| 关联概念 | 双势阱、软模理论 | 费米面嵌套、公度/非公度 CDW |

## 📚 相关论文 (Related Papers)

- [[../papers/Makogon2012wave]]：以模型体系动态磁化率展示软模在波矢 Q 处随耦合趋于零的涌现过程。
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]：真实电极中铁电软模稳定性与铁电临界厚度。
- [[../papers/lezoualchStudyChargeDensity]]：用 DFPT 虚频软模构建 1T-VSe2/VTe2 的 CDW 基态结构。
- [[../papers/xuTunableFerroelectricTopological2022]]：可调铁电/拓扑体系中软模与畸变势的讨论。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[soft-mode-theory|软模理论]]、[[soft-mode-phonon|软模声子/平带声子机制]]、[[charge-density-wave|电荷密度波]]、[[commensurate-cdw|公度 CDW]]、[[electron-phonon-coupling|电声耦合]]、[[fermi-surface-nesting|费米面嵌套]]、[[peierls-distortion|Peierls 畸变]]、[[dfpt|DFPT]]
