---
tags: [concept, spintronics, 2D-materials, magnetic-tunnel-junction, nonvolatile-memory]
title: 磁隧道结 / Magnetic Tunnel Junction
type: concept
status: mature
year: 2020
domain: [condensed-matter-physics, spintronics, device-physics]
mechanism: 两层铁磁电极夹一层极薄绝缘势垒，隧穿电阻随两磁化相对取向（平行/反平行）变化，即隧穿磁电阻效应
related_concepts: [spin-valve, spin-injection, spin-transfer-torque, tunnel-magnetoresistance, spintronics, spin-transport, nonvolatile-memory, 2d-materials, ferromagnetism]
papers: [liuSpintronicsTwoDimensionalMaterials2020b, xueEmergingNonvolatileMemories2011]
updated: 2026-08-19
---

# 磁隧道结 / Magnetic Tunnel Junction

磁隧道结 (Magnetic Tunnel Junction, MTJ) 由两层铁磁电极夹一层极薄的绝缘隧道势垒（如 MgO、h-BN）构成。其隧穿电阻强烈依赖两电极磁化方向的相对取向——平行态电阻低、反平行态电阻高（隧穿磁电阻 TMR 效应）。MTJ 是自旋转移矩磁随机存储器 (STT-MRAM)、磁传感器与可重构逻辑的核心单元。

## 👵 太奶导读

乖孙，磁隧道结就像个"磁控开关的隧道门"：两层磁性金属中间夹一层极薄的"绝缘玻璃"。如果上下两块磁铁方向一致（平行），电子能"挤"过隧道门，电阻小（表示 0/开）；方向相反（反平行），电阻大（表示 1/关）。这个"开/关"状态不耗电也能记住，断电不丢。一句话：**"两块磁铁夹片玻璃，磁向一致就通电，反过来就断电，还能记住"**。

## 🏗️ 结构概览

MTJ 的器件构型：铁磁层 / 隧道势垒 / 铁磁层，外加钉扎层与电极。

![图：自旋电子学器件与存储单元示意](../../raw/figures/liuSpintronicsTwoDimensionalMaterials2020b/fig_6_I7PXRSCV.png)
*   **看图要点**：展示了基于二维材料的自旋器件/存储单元（MTJ 类）的结构与工作原理。
*   **来源**：[[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]

## 🧩 核心机制

### 1. 隧穿磁电阻 (TMR)

隧穿几率依赖两电极自旋相关的态密度：平行态下多数自旋子带对齐，隧穿通道多、电阻低；反平行态下通道少、电阻高。TMR 比值 $= (R_{AP}-R_P)/R_P$ 是器件核心指标。

### 2. 势垒材料与相干隧穿

MgO (001) 势垒因对称性过滤实现相干隧穿，TMR 可超过 1000%；二维 h-BN 以其原子级平整与弱相互作用成为新兴势垒，利于范德华异质结集成。

### 3. 写入与读出

- 写入：磁场（STT 自旋转移力矩）翻转自由层磁化；
- 读出：隧穿电阻区分平行/反平行态，实现非易失存储。

## 📋 关键参数表

| 参数 | 含义 | 典型值/特征 |
|---|---|---|
| TMR | 隧穿磁电阻比 | MgO 势垒 >1000% |
| 势垒厚度 | 隧穿层 | 约 1–2 nm |
| 势垒材料 | 绝缘层 | MgO、h-BN、Al₂O₃ |
| 写入方式 | 磁化翻转 | 磁场 / STT 电流 |
| 应用 | 器件功能 | STT-MRAM、磁传感器 |

## 🔀 近邻概念辨析

- **MTJ vs 自旋阀**：自旋阀的中间层是金属（非隧穿），靠巨磁电阻 (GMR) 工作；MTJ 中间层是绝缘势垒，靠隧穿磁电阻 (TMR) 工作。TMR 通常更大、更适合存储。
- **MTJ vs 铁电隧道结**：铁电隧道结用铁电极化翻转改变势垒高度（隧穿电致电阻 TER），MTJ 用磁化取向改变隧穿电阻；二者可结合成多铁隧道结。

## 📚 相关论文 (Related Papers)

- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]：综述基于二维材料（h-BN 势垒）的 MTJ 与自旋存储器件进展。
- [[../papers/xueEmergingNonvolatileMemories2011]]：非易失存储器体系（含 MTJ/STT-MRAM）的技术路线综述。

## 🔗 关联概念与实体 (Related)

- [[../concepts/spin-valve|spin-valve]]
- [[../concepts/spin-injection|spin-injection]]
- [[../concepts/spin-transfer-torque|spin-transfer-torque]]
- [[../concepts/giant-magnetoresistance|giant-magnetoresistance]]
- [[../concepts/spin-transport|spin-transport]]
- [[../concepts/spin-orbit-coupling|spin-orbit-coupling]]
- [[../concepts/ferromagnetism|ferromagnetism]]
- [[../entities/h-BN|h-BN]]
- [[../entities/MgO|MgO]]
- [[../entities/Co|Co]]
