---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_11c27ca0989d11f1a98a525400f8a581
    ReservedCode1: pMVxxGYL96oEJI0vG4bKVHmP5WEINGmG200m5XmCXm+MNzCPh0AYPRGyJoFTF//Ows8nCWLw+TDC08geJfdPwD7PAjqNwUeWboIcTGrch+4pR2u6R3fDkEkPrNw1jKFX9P9GENl9t1c2nh/+oFYfruvLmQqxLE4b1QjYgiTsslUrMmjpsdo0a1VnpmE=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_11c27ca0989d11f1a98a525400f8a581
    ReservedCode2: pMVxxGYL96oEJI0vG4bKVHmP5WEINGmG200m5XmCXm+MNzCPh0AYPRGyJoFTF//Ows8nCWLw+TDC08geJfdPwD7PAjqNwUeWboIcTGrch+4pR2u6R3fDkEkPrNw1jKFX9P9GENl9t1c2nh/+oFYfruvLmQqxLE4b1QjYgiTsslUrMmjpsdo0a1VnpmE=
---



# 经典与介观尺度模拟 / Classical & Mesoscale Simulation

> 科研范式 P10：像"沙盘推演"——不追踪每个原子，而是用粗粒化的模型（自旋、序参量、畴）在更大的空间和时间尺度上推演体系如何演化。

## 👵 太奶导读

有些现象（比如斯格明子怎么运动、畴怎么长大、相变怎么发生）发生在纳米到微米尺度、纳秒到微秒时间，原子级模拟算不动。经典与介观模拟就用"粗粒化"的办法：把体系抽象成自旋、序参量或畴的集合，用蒙特卡洛、相场或微磁学方法在更大尺度上演化，看它最终形成什么结构、怎么响应外场。就像用沙盘推演战争，不用模拟每个士兵，只看军团怎么调动。

## 🧭 范式概述

这个范式的核心逻辑是：**以"粗粒化模型 + 数值演化"在介观尺度揭示体系的长程行为**。研究对象覆盖斯格明子、畴结构、铁电/多铁相变、拓扑缺陷等。总体思路是：先构建粗粒化模型（自旋哈密顿量、Landau 自由能、微磁方程），选择合适数值算法（蒙特卡洛、相场、微磁模拟），在介观尺度上做长时演化，再通过统计与结构分析提取畴尺寸、缺陷运动、相变温度等，最后归纳机理。这样设计的原因在于：介观行为（畴、缺陷、拓扑结构）无法从原子尺度直接外推，需要专门的介观模拟。例如 Zhang 系列（[[../papers/Zhang2019a]]、[[../papers/Zhang2019b]]、[[../papers/Zhang2019c]]）与 Wu 系列（[[../papers/Wu2018]]、[[../papers/Wu2021]]）展示了从模型构建到介观演化的完整路线。

## 🔁 研究流程

1. **模型构建**：抽象出自旋/序参量/畴的粗粒化模型与相互作用。
2. **数值算法**：选择蒙特卡洛、相场或微磁学方法。
3. **长时演化**：在介观尺度模拟畴/缺陷/相变的演化。
4. **统计/结构分析**：提取畴尺寸、缺陷运动、相变温度、响应函数。
5. **机理归纳**：将模拟结果与实验/理论对照，给出介观机理。

## 🛠️ 核心方法与工具

- **蒙特卡洛**：热力学统计与相变模拟（[[../papers/Zhang2002b]]、[[../papers/Zhang2003a]]）。
- **相场模拟**：畴结构与相变演化（[[../papers/Zhang2019a]]、[[../papers/Zhang2019b]]）。
- **微磁学**：斯格明子/磁畴动力学（[[../papers/Wei2021]]、[[../papers/Wu2021]]）。
- **Landau 自由能模型**：铁电/多铁介观描述（[[../papers/Zhang2019c]]、[[../papers/Wu2018]]）。

## ✅ 适用条件

- 关注介观尺度（纳米-微米）的长程行为。
- 体系可用粗粒化模型描述，原子细节非必需。
- 需要模拟长时演化或大尺度结构。

## ⚠️ 局限与风险

- 粗粒化模型参数依赖微观输入，参数不准会误导结果。
- 忽略原子细节，可能遗漏微观机制。
- 模拟尺度与实验仍有差距，需谨慎对照。
- 数值算法收敛性与有限尺寸效应需注意。

## 📚 代表论文 (Representative Papers)

- [[../papers/Zhang2019a]]：介观模拟基础方法。
- [[../papers/Zhang2019b]]：相场模拟畴结构。
- [[../papers/Wei2021]]：微磁学模拟斯格明子。
- [[../papers/Wu2021]]：介观动力学模拟。

## 🗂️ 覆盖论文全集 (All Covered Papers)

- [[../papers/Zhang2019a]]
- [[../papers/Zhang2019b]]
- [[../papers/Zhang2019c]]
- [[../papers/Zhang2002b]]
- [[../papers/Zhang2003a]]
- [[../papers/Wei2021]]
- [[../papers/Wu2018]]
- [[../papers/Wu2021]]

## 🔗 关联概念、实体与主题 (Related Concepts, Entities & Topics)

- [[../concepts/skyrmion|斯格明子]]
- [[../concepts/domain-wall|畴壁]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/multiferroicity|多铁性]]
- [[../concepts/polarization-switching|极化翻转]]
- [[../entities/BiFeO3|BiFeO₃]]
- [[../entities/NiI2|NiI₂]]
- [[../topics/多铁性材料|多铁性材料]]
- [[../topics/材料模拟计算设计|材料模拟计算设计]]

## 📈 生命周期日志

- **2026-08-15**: active — 提炼自 8 篇经典与介观尺度模拟类论文（蒙特卡洛/相场/微磁学等）。
*（内容由AI生成，仅供参考）*
