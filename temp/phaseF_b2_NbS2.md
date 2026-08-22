---
tags: [entity, material, 2d-material, tmd, cdw, superconductor]
title: 二硫化铌 / Niobium Disulfide (2H-NbS2)
type: entity
status: developing
formula: 2H-NbS2
class: [transition-metal-dichalcogenide, superconductor]
properties: [superconductivity, charge-density-wave, multiband-superconductivity, uemura-scaling, superfluid-density]
related_entities: [NbSe2, TaS2, 2H-TaSe2, TMDs]
papers: [CastroNeto2001charge, Islam2025enhancement, majumdarInterplayChargeDensity2020]
updated: 2026-08-18
---

# 二硫化铌 / Niobium Disulfide (2H-NbS2)

2H-NbS₂ 是过渡金属二硫族化物（TMDs）中研究超导电性与电荷密度波（CDW）相互作用的经典材料。与同构的 2H-NbSe₂ 不同，2H-NbS₂ 只表现出超导电性而不具有 CDW 序，这使其成为解耦"CDW-超导竞争"的理想对照样品。其超导态表现出多带（双 s 波）能隙结构、泡利顺磁主导的上临界场等特征，是检验超导配对机制与 Uemura 标度律普适性的关键材料。

## 👵 太奶导读

乖孙，2H-NbS₂ 是一块"只导电不排队"的薄片。它有个"亲兄弟"2H-NbSe₂，两者长得几乎一模一样，但 NbSe₂ 里的电子会"排队"（电荷密度波），而 NbS₂ 里的电子不排队、只顾着配对成"夫妻"（超导，零电阻）。正因为兄弟俩一个排队、一个不排队，科学家拿它们做对比实验，想搞清楚"电子排队"到底会不会影响"超导"。加压、测磁场、测超导电流密度……都是为了解开这兄弟俩的谜团，也想验证"超导"在所有材料里是不是遵循同一套规矩。

## 🏗️ 结构概览

- **晶体结构**：2H 相（三棱柱配位）六方层状结构，层间范德华结合；与 2H-NbSe₂ 同构。
- **电子序**：本征超导体（T_c ≈ 5.9 K），不显示 CDW 序；2H-NbSe₂ 则在相同温区共存 CDW 与超导。
- **多带超导**：实验表明 2H-NbS₂ 具有双 s 波（s+s）超导能隙结构，大能隙表现出强耦合特征。

## 🧩 超导与 CDW 的相互作用

- **CDW-超导竞争平台**：majumdarInterplayChargeDensity2020 对 2H-NbSe₂ 与 2H-NbS₂ 的对比研究表明，CDW 与超导是竞争关系——压力可抑制 CDW 并显著增强超导；但 CDW 不影响基本的双 s 波能隙结构。该研究还发现 NbS₂ 的上临界场由泡利顺磁效应主导，而 NbSe₂ 表现出多带效应。
- **压力调控与 Uemura 标度**：Islam2025enhancement 通过静水压力磁输运与 μSR 测量发现，无 CDW 的 2H-NbS₂ 在 1.8 GPa 压力下超流密度增强约 20%，而具有 CDW 的 4H-NbSe₂ 在 2 GPa 下增强约 75%；两类材料的 T_c 与超流密度 n_s/m* 关系均呈 Uemura 标度律（与铜氧化物、铁基超导体类似），暗示 BEC-BCS 渡越物理图像，并证明压力对超导的增强存在独立于 CDW 的机制。
- **统一微观理论背景**：CastroNeto2001charge 为 2H-TMDs（含 NbS₂、NbSe₂、TaS₂、TaSe₂）中 CDW 与超导共存提供了首个统一微观理论：CDW 态为具有六重节点对称性的 f 波态（低能激发为狄拉克费米子），超导源于声子介导配对，存在量子临界点，解释了 CDW 与超导转变温度的反相关关系。

## 📚 相关论文 (Related Papers)

- [[../papers/majumdarInterplayChargeDensity2020]]：以 2H-NbS₂/NbSe₂ 为平台，建立 CDW-超导相互作用与多带能隙结构的实验基准。
- [[../papers/Islam2025enhancement]]：压力下 μSR 揭示无 CDW 体系超流密度增强与 Uemura 标度律，挑战"CDW 简单竞争"图像。
- [[../papers/CastroNeto2001charge]]：提出 2H-TMDs 中 CDW 与超导共存的统一微观理论（f 波 CDW + 狄拉克费米子）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../concepts/electron-phonon-coupling|电子-声子耦合]]
- [[../concepts/fermi-surface-nesting|费米面嵌套]]
- [[../entities/NbSe2|NbSe₂（同族 CDW 对照）]]
- [[../entities/2H-TaSe2|2H-TaSe₂（CDW 参照）]]
