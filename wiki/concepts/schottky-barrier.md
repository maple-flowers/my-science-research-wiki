---
tags: [concept]
title: 'schottky-barrier'
type: concept
status: developing
papers: ['chenHafniumBasedFerroelectricPostMoore2026', 'cuiIntercorrelatedInplaneOutofplane2018a', 'dingPredictionIntrinsicTwodimensional2017a', 'huProgressProspectsLowdimensional2019', 'huangTwodimensionalIn2Se3Rising2022', 'naguib25thAnniversaryArticle2013a', 'tahirFerroelectricityNonvolatileMemristor2025', 'yangStrainEngineeringTwodimensional2021']
updated: 2026-08-18
---

# schottky-barrier

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


肖特基势垒（Schottky barrier）指**金属与半导体（或二维材料）界面处形成的整流势垒**，其高度 φ_B 由金属功函数、半导体亲和能/带边位置与界面态（费米能级钉扎）决定。肖特基势垒是金属-半导体接触、二极管、光伏、光电探测与场效应晶体管（FET）接触电阻的核心参数。

## 👵 太奶导读

太奶啊，把金属"焊"在半导体上，界面处会形成一道"电子要翻的墙"——肖特基势垒。墙高，电子难过去（整流，电流只走一个方向，二极管就靠它）；墙矮，电子畅行（欧姆接触，导线效果好）。这堵"墙"的高度由金属和半导体各自"抢电子的本事"（功函数、电子亲和能）以及界面"杂质陷阱"决定。做晶体管、太阳能电池都要精心设计它。

## 🧩 核心内容与机制 (Core Content)

- **势垒高度**：理想模型 φ_B = Φ_M - χ_S（n 型）；实际受界面态、费米能级钉扎（Fermi level pinning）与偶极层修正（本库肖特基与界面论文）。
- **整流与欧姆**：高势垒 → 整流（肖特基二极管）；低势垒/重掺杂隧穿 → 欧姆接触；二维金属-半导体异质结中界面范德华间隙降低钉扎。
- **二维材料接触**：本库 TMD/石墨烯/金属接触论文研究接触电阻与势垒调控（Pd/MoS₂、Ti/Au 等），是 FET 性能关键。
- **光电应用**：肖特基势垒决定光伏开路电压与光电探测响应（本库光电探测论文）。
- **表征**：I-V 与 C-V 测量提取势垒高度，配合紫外光电子谱（UPS）与能带排列（band-alignment）计算。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/band-alignment|能带排列]]：肖特基势垒的能带基础。
- [[../concepts/band-gap|带隙]]：半导体的带边位置。
- [[../concepts/2d-materials|二维材料]]：二维接触与势垒调控。

## 📚 相关论文 (Related Papers)

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]] — Hafnium-Based Ferroelectric Post-Moore Electronics: Device Physics, Integration Architectures, and Neuromorphic System Implementation
- [[../papers/cuiIntercorrelatedInplaneOutofplane2018a]] — Intercorrelated In-Plane and Out-of-Plane Ferroelectricity in Ultrathin Two-Dimensional Layered Semiconductor In2Se3
- [[../papers/dingPredictionIntrinsicTwodimensional2017a]] — Prediction of intrinsic two-dimensional ferroelectrics in In2Se3 and other III2-VI3 van der Waals materials
- [[../papers/huProgressProspectsLowdimensional2019]] — Progress and prospects in low‐dimensional multiferroic materials
- [[../papers/huangTwodimensionalIn2Se3Rising2022]] — Two-dimensional In2Se3: A rising advanced material for ferroelectric data storage
- [[../papers/naguib25thAnniversaryArticle2013a]] — 25th Anniversary Article: MXenes: A New Family of Two‐Dimensional Materials
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]] — Ferroelectricity and Nonvolatile Memristor Applications of Free‐Standing 2D Niobium Carbide: A New Frontier of Free‐Standing MXene in Electronic Devices
- [[../papers/yangStrainEngineeringTwodimensional2021]] — Strain engineering of <scp>two‐dimensional</scp> materials: Methods, properties, and applications
