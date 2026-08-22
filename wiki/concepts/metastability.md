---
tags: [concept]
title: 'metastability'
type: concept
status: developing
papers: ['Wixtrom2011electrical', 'chenHafniumBasedFerroelectricPostMoore2026', 'fengFerroelectricityMultiferroicityTwodimensional2020', 'gomez-ortizKittelLawDomain2023', 'hanPolarTopologicalMaterials2025', 'liMonolayerPuckeredPentagonal2022', 'lvUnconventionalHystereticTransition2022', 'tangMultiferroicityTwodimensionalVan2025', 'wuElectrostaticGatingIntercalation2022']
updated: 2026-08-18
---

# metastability

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


亚稳态（metastability）指体系处于**局部自由能极小、但非全局能量最低**的平衡态：在有限势垒保护下可以长期存在，一旦获得足够能量（热激活、电场/应力/光照）便越过势垒进入（更）稳定态。亚稳态是铁电/铁磁开关、相变存储、玻璃与超冷/过冷体系、超饱和固溶体的普遍状态，也是"状态可编程"器件的物理基础。

## 👵 太奶导读

太奶啊，山的鞍部有块小平台，站在上面也是"稳"的，但旁边才是真正的山谷底——这种"暂时稳、其实不是最低点"的状态就是亚稳态。材料经常停在这种半山腰的小平台：看起来稳定、能一直待着，但给点刺激（加热、加电、敲一下）就可能"滑"到更深的谷，性质大变。铁电存储"翻不翻转"、相变材料"记不记得住"，全靠亚稳态。

## 🧩 核心内容与机制 (Core Content)

- **热力学图像**：自由能面上局部极小（亚稳）与全局极小（稳定）被势垒分隔；势垒高度决定亚稳态寿命（本库结构相变、形核与成核论文）。
- **滞回与开关**：铁电/铁磁畴的极化/磁化翻转经过亚稳态与势垒（switching-barrier），产生滞回（hysteresis）——非易失存储的机制。
- **相变与成核**：一级相变（first-order-phase-transition）中的过冷/过热即亚稳态；成核长大决定相变路径。
- **材料实例**：非晶-晶相变存储（相变存储）、铁电相的可编程多态、MOF/玻璃态与超饱和合金。
- **计算与预测**：NEB（nudged-elastic-band）等方法计算势垒，评估亚稳态稳定性与寿命（本库 NEB 论文）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/hysteresis|滞回]]：亚稳态开关的宏观表现。
- [[../concepts/first-order-phase-transition|一级相变]]：亚稳态的相变场景。
- [[../concepts/switching-barrier|翻转势垒]]：亚稳态之间的壁垒。
- [[../concepts/nudged-elastic-band|NEB 方法]]：势垒计算。

## 📚 相关论文 (Related Papers)

- [[../papers/Wixtrom2011electrical]] — Electrical and Optical Properties of a New Polymorph of the Tetrathiafulvalene-Chloranil (TTF-CA) Charge Transfer Salt
- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]] — Hafnium-Based Ferroelectric Post-Moore Electronics: Device Physics, Integration Architectures, and Neuromorphic System Implementation
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in two-dimensional Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/gomez-ortizKittelLawDomain2023]] — Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices
- [[../papers/hanPolarTopologicalMaterials2025]] — Polar topological materials and devices: Prospects and challenges
- [[../papers/liMonolayerPuckeredPentagonal2022]] — Monolayer puckered pentagonal VTe2: An emergent two-dimensional ferromagnetic semiconductor with multiferroic coupling
- [[../papers/lvUnconventionalHystereticTransition2022]] — Unconventional Hysteretic Transition in a Charge Density Wave
- [[../papers/tangMultiferroicityTwodimensionalVan2025]] — Towards Multiferroicity in Two-Dimensional Van Der Waals Materials: Challenges and Opportunities
- [[../papers/wuElectrostaticGatingIntercalation2022]] — Electrostatic gating and intercalation in 2D materials
