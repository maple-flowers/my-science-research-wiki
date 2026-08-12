---
tags: [entity]
---

# 激光划刻还原氧化石墨烯 (LSG)

激光划刻还原氧化石墨烯（Laser-Scribed Graphene, LSG，亦称 Laser-Induced Graphene, LIG 或 Laser-Reduced Graphene, LrGO）是一种通过激光辐射诱导氧化石墨烯（GO）发生瞬时光热还原的先进制造技术。与传统的化学还原或热还原法相比，LSG 具有直接图案化、无添加剂、环境友好以及可在柔性基底上原位快速制造等显著优势，使其成为构建高性能柔性电子器件，特别是“二维铁电电子学”（2D Ferrotronics）器件的理想电极材料。

## 物理机制与物性锁定 (Phase-Locked Properties)

LSG 的性能高度依赖于激光加工参数（如功率、扫描速度、脉冲频率及波长）。激光脉冲提供的高能量通量在微秒级时间内使 GO 层间的含氧官能团（如羟基 -OH、环氧基 -O-）发生剧烈热解，产生大量 CO₂ 和 H₂O 蒸汽。这一过程诱导了石墨烯层间的瞬时剥离，形成了具有高比表面积的独特三维多孔蓬松结构。

在物性演变上，LSG 展示了从绝缘相向导电相的精准转换：
- **结构转变**：XRD 表征显示，典型 GO 在 11° 附近的 (001) 衍射峰在激光处理后消失，取而代之的是位于 25° 附近的宽化石墨 (002) 峰，标志着 sp³ 杂化的 GO 晶格向 sp² 杂化还原石墨烯相的转变 [[../papers/sattarFunctionalizedDoubleTransition2025]]。
- **性能锁定**：通过调节激光能量，可以精确锁定还原程度（C/O 比）与孔隙率，从而在同一基底上实现从半导体到高导电金属态的连续调控。

## 在二维铁电电子学中的应用

在柔性忆阻器（Memristors）与人工突触器件中，LSG 展示了卓越的电化学稳定性与机械鲁棒性：
1. **柔性电极**：以 LSG 为上下电极构筑的全柔性三明治结构（如 LSG/MXene/LSG）具有极佳的弯曲耐受性，适用于可穿戴电子设备。
2. **界面调控**：LSG 丰富的边缘活性位点与 MXene（如 [[Mo2Ti2C3Tx]]）等活性层形成良好的范德华接触。其高度多孔的结构提供了充足的氧空位源，有助于铁电极化束缚电荷产生的内电场对氧空位导电细丝（Oxygen Vacancy Filament）的形成与断裂进行定向调控 [[../papers/zahraCriticalAnalysisFerroelectric2025]]。
3. **避免离子扩散**：相比于 Ag、Cu 等金属电极，LSG 作为碳基电极能有效抑制金属离子在活性层中的不可逆扩散，显著提升了阻变行为的一致性与循环耐久性 [[../papers/sattarFunctionalizedDoubleTransition2025]]。

## Related Papers

- [[../papers/sattarFunctionalizedDoubleTransition2025]] — 详细描述了 LSG 电极的制备工艺（900 mm/min 激光扫描）及其在全 MXene 柔性忆阻器中的应用。
- [[../papers/zahraCriticalAnalysisFerroelectric2025]] — 对 LSG 在二维 MXene 基铁电器件中的角色进行了系统评述，强调了其在柔性存储领域的优势。
