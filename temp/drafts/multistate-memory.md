# 多态存储 / Multistate Memory

多态存储（multistate memory）指**单个存储单元可稳定保持两个以上（通常四个或更多）可区分状态**的非易失存储范式。相比传统二值存储，它能在不缩小器件尺寸的前提下提升单位面积存储密度。二维铁电材料凭借多个可独立翻转的极化自由度（面内/面外耦合、层间滑移、多铁共存）成为实现多态存储的前沿平台。

## 👵 太奶导读

普通 U 盘/内存一个格只能记"0"或"1"两个状态。多态存储则是让一个格能记"0、1、2、3"甚至更多——就像一盏灯从"亮/灭"升级成"能调好几种亮度"。二维铁电材料里藏着多种"拧转"极化的方式（上下、平面内、层间滑动），组合起来就能一个单元存好几个比特，数据密度直接翻倍。

## 🧩 多态极化的物理来源

- **面内/面外锁定极化**：α-In₂Se₃ 室温下同时具有相互锁定的面内（IP）与面外（OOP）本征铁电极化，存在层数奇偶效应，可用电场/可见光双控实现多态非易失存储原型（[[../papers/cuiIntercorrelatedInplaneOutofplane2018a|Cui 2018]]）。
- **层间滑移多态**：层数 N≥3 的多层黑磷可借助非对称层间堆叠（如 EAB）打破中心对称产生滑移铁电性，随层数增加涌现多种可互转的极化态（[[../papers/shenEmergenceMultipleFerroelectric2025|Shen 2025]]）。
- **CDW 磁性多态**：TMD 1T′ 铁磁 CDW 态中，电荷掺杂可诱导 NM/FM CDW 可逆相变，产生高达 12.17% 的驱动应变与磁性突变（[[../papers/chenFerromagneticNonmagnetic1T2022|Chen 2022]]）。

## ⚡ 器件与机制

多态存储依赖**滑动铁电**的层间电荷转移、逐层翻转与拓扑畴壁扭结机制（[[../papers/zhangEmergingFrontiersTwodimensional2025|Zhang 2025]]），以及多铁材料（NiI₂、Cr₂S₃、CuCrSe₂、p 型 SnSe）的磁电耦合自由度（[[../papers/RecentAdvancesGrowth2025|Recent advances 2025]]）。读出可通过极化相关的电导、磁化或光电响应实现。

## 📚 相关论文 (Related Papers)

- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]] — Intercorrelated In-Plane and Out-of-Plane Ferroelectricity in Ultrathin Two-Dimensional Layered Semiconductor In2Se3
- [[../papers/shenEmergenceMultipleFerroelectric2025]] — Emergence of multiple ferroelectric states in multilayer black phosphorus
- [[../papers/chenFerromagneticNonmagnetic1T2022]] — Ferromagnetic and nonmagnetic 1T′ charge density wave states in transition metal dichalcogenides
- [[../papers/zhangEmergingFrontiersTwodimensional2025]] — Emerging frontiers in two-dimensional sliding ferroelectrics
- [[../papers/RecentAdvancesGrowth2025]] — Recent advances in growth, characterization, and application of two-dimensional multiferroic materials

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：多态极化的物理基础。
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]：层间滑移驱动的多态极化。
- [[../concepts/multiferroicity|多铁性]]：磁电耦合提供的额外存储自由度。
- [[../concepts/remanent-polarization|剩余极化]]：状态保持的定量指标。
- [[../concepts/negative-capacitance|负电容]]：铁电多态在低功耗器件中的利用。
- [[../entities/In2Se3|In₂Se₃]]：面内/面外锁定多态存储原型材料。
*（内容由AI生成，仅供参考）*
