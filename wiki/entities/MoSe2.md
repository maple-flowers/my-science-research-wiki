---
tags: [entity, material, 2d-material, tmd, semiconductor]
title: 二硒化钼 / Molybdenum Diselenide (MoSe2)
type: entity
status: developing
formula: MoSe2
class: [transition-metal-dichalcogenide, semiconductor, 2d-material]
properties: [direct-bandgap, photoluminescence, sliding-ferroelectricity, topological-defects, humidity-sensing]
related_entities: [MoS2, TMDs, WSe2]
papers: [FerroelectricityMultiferroicityAtomic2023, Li2013bonding, Owji20212d, krishnamurthiSpinChargeDensity2020, tangCombiningIntrinsicSlidinginduced2025, wangTunableD0Topological2025b]
updated: 2026-08-18
---

# 二硒化钼 / Molybdenum Diselenide (MoSe2)

MoSe₂ 是过渡金属二硫族化物（TMDs）家族中的典型单层直接带隙半导体。其单层结构（Se–Mo–Se 三明治）具有约 1.5 eV 的直接带隙与强光致发光，被广泛用于光电探测、传感与二维铁电/多铁异质结构研究。作为"堆叠工程"的理想基底，MoSe₂ 既可作为衬底承载其他二维材料的铁电与拓扑物性（wangTunableD0Topological2025b），其自身也能通过层间滑移产生可翻转的滑动铁电性（tangCombiningIntrinsicSlidinginduced2025）。

## 👵 太奶导读

乖孙，MoSe₂ 就像一块"万能积木"。它是一层极薄的半导体材料（一个 Mo 原子夹在两层 Se 原子中间，总共只有几个原子厚），本身能发光、能导电，常被拿来做传感器和光电探测器。更妙的是，把几层 MoSe₂ 像扑克牌一样轻轻一推，就能变出"电的方向"（极化）来，这就是滑动铁电性。它还能当别人的"地板"——比如把另一种材料放在它上面，让整个体系产生新的磁性功能。所以研究二维材料的科学家几乎人手一块它。

## 🏗️ 结构概览

- **晶体结构**：六方层状结构，单层为 Se–Mo–Se 三明治；块体呈 2H 堆叠，层间由范德华力结合。
- **多型体**：与 MoS₂ 类似，可通过层间堆叠方式构造 2H/3R 等不同多型，为滑动铁电性提供堆叠自由度。
- **电子结构**：单层为直接带隙半导体（约 1.5 eV），随层数增加转为间接带隙；带隙可调使其适用于柔性电子与应变工程。

## 🧩 关键物性：从力学到铁电

- **本征力学响应**：Li2013bonding 对单层 TMDs 的第一性原理研究表明，MoSe₂ 的极限强度与化学组分强相关（排序 WS₂ > WSe₂ > MoS₂ > WTe₂ > MoSe₂ > MoTe₂），扶手椅方向强度高于锯齿方向，力学性能根源在于金属 d 轨道与硫族 p 轨道的杂化强度及电荷转移量。
- **一维缺陷中的纯电子 CDW**：krishnamurthiSpinChargeDensity2020 在 MoSe₂/MoS₂ 单层的镜像孪晶界（MTB）中发现，其金属性源于体相拓扑极化突变产生的补偿电荷；在电子关联（U）作用下基态变为无需原子位移的周期三倍 SDW/CDW 共存态，并预言了分数电荷孤子。
- **滑动铁电与复合多态**：tangCombiningIntrinsicSlidinginduced2025 提出"复合铁电体"范式：在 1T″ 相 TMD（如 1T″-MoSe₂）H 型堆叠双层/三层中，本征面外极化与滑移诱导极化共存，利用两者翻转势垒的显著差异可预测 6 个与 10 个可切换极化态，将存储密度提升数倍。
- **作为异质结平台**：wangTunableD0Topological2025b 将单层 MoSe₂ 与多铁性半金属 In₂NO₂ 构成异质结，通过电场翻转铁电极化实现斯格明子相（"1"态）与铁磁相（"0"态）的非易失性开关，展示了 MoSe₂ 在拓扑自旋电子学中的基底价值。
- **传感应用**：Owji20212d 将 MoSe₂ 纳米片涂覆于化学蚀刻光纤上制成湿度传感器，验证了二维材料涂层在低湿（<30% RH）范围内的敏感响应。

在原子级厚度铁电/多铁的总体框架中（FerroelectricityMultiferroicityAtomic2023），MoSe₂ 等范德华材料被视为"堆叠工程"的核心平台：本征铁电体、滑移铁电体、莫尔铁电体等均可在其层状基底上实现，从而打破传统铁电须本征存在于块体的限制。

## 📚 相关论文 (Related Papers)

- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：将范德华堆叠材料（含 MoSe₂ 一类体系）定位为原子级厚度铁电/多铁的三大平台之一，强调堆叠工程突破传统限制。
- [[../papers/Li2013bonding]]：系统给出单层 TMDs（含 MoSe₂）的极限强度、各向异性与组分依赖，揭示力学性能的电子结构起源。
- [[../papers/Owji20212d]]：实验展示 MoSe₂ 涂层光纤湿度传感器，验证二维材料在传感场景的应用。
- [[../papers/krishnamurthiSpinChargeDensity2020]]：以 MoSe₂/MoS₂ 镜像孪晶界为例，提出"拓扑极化突变→分数电荷→纯电子 CDW"的普适机制。
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]]：以 1T″-MoSe₂ 为例提出复合铁电体多态范式，实现六重与十重极化态预测。
- [[../papers/wangTunableD0Topological2025b]]：构建 In₂NO₂/MoSe₂ 异质结，实现铁电可控的拓扑磁态开关。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/2d-materials|二维材料]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/topological-defects|拓扑缺陷]]
- [[../entities/TMDs|过渡金属二硫族化物（TMDs）]]
- [[../entities/MoS2|MoS₂（同族参照）]]
