# 相场模拟 / Phase-Field Modeling

相场模拟（phase-field modeling）指**用连续序参量场描述微观结构（畴、界面、拓扑缺陷）随时间的演化**的计算方法，通过求解含时 Ginzburg-Landau 方程与弹性能/静电能耦合，模拟铁电畴翻转、极性拓扑结构形成与相变动力学。它是连接原子尺度计算与宏观器件行为的重要桥梁。

## 👵 太奶导读

铁电材料里无数个"小极化箭头"（畴）怎么翻转、怎么排布成涡旋？原子一个一个算太慢，整体当成"一整片"又太粗。相场模拟折中：把每个位置的极化方向当作一个"场"，用方程描述它如何演变。就像用流体力学算水流一样，相场能算出畴如何成核、长大、翻转，还能预测新奇的拓扑结构。

## 🧩 畴翻转与拓扑结构的模拟

- **多晶铁电翻转**：从二维 PFM（OP+IPx）信号反演多晶 BiFeO₃ 晶粒三维极化翻转角，定量给出 71°/109°/180° 翻转面积占比（42%/29%/29%），并建立"电荷迁移能 vs 面内应力能"竞争模型（[[../papers/Jin2015studying|Jin 2015]]）。
- **极性斯格明子的临界厚度缺失**：(PbTiO₃)ₙ/(SrTiO₃)ₙ 超晶格中极性斯格明子周期-厚度关系在 h<4 nm 时违反 Kittel 定律，且可在仅 2 个晶胞厚的 PTO 层中稳定存在（[[../papers/gongAbsenceCriticalThickness2023|Gong 2023]]）。
- **极性拓扑统一视角**：体自由能、静电能、弹性能与梯度能竞争的统一能量视角支撑通量闭合畴、涡旋、斯格明子、半子等极性拓扑的设计与操控（[[../papers/hanPolarTopologicalMaterials2025|Han 2025]]）。

## 🧩 与实验和器件的衔接

相场模拟与应变工程、畴壁电子学、负电容等铁电薄膜新功能直接对接（[[../papers/martinThinfilmFerroelectricMaterials2016|Martin 2016]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Jin2015studying]] — Studying the Polarization Switching in Polycrystalline BiFeO3 Films by 2D Piezoresponse Force Microscopy
- [[../papers/gongAbsenceCriticalThickness2023]] — Absence of critical thickness for polar skyrmions with breaking the Kittel's law
- [[../papers/hanPolarTopologicalMaterials2025]] — Polar topological materials and devices: Prospects and challenges
- [[../papers/martinThinfilmFerroelectricMaterials2016]] — Thin-film ferroelectric materials and their applications

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/phase-transition|相变]]：相场模拟描述的对象。
- [[../concepts/ferroelectricity|铁电性]]：畴与极化的载体。
- [[../concepts/polar-skyrmion|极性斯格明子]]：相场模拟预言的拓扑结构。
- [[../concepts/domain-wall-engineering|畴壁工程]]：相场模拟的器件应用。
- [[../entities/PbTiO3-SrTiO3-superlattice|PbTiO₃/SrTiO₃ 超晶格]]：极性斯格明子的平台。
*（内容由AI生成，仅供参考）*
