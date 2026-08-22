---
tags: [concept, ferroelectrics, ferroelectricity]
title: 畴壁能 / Domain-Wall Energy
type: concept
status: developing
domain: [ferroelectrics, ferroelasticity, magnetism, topological-defects]
mechanism: 相邻畴之间单位面积界面的自由能，由交换/梯度能、各向异性/弹性能与长程相互作用竞争决定；通过基特尔定律控制畴宽与拓扑畴尺度
related_concepts: [domain-wall, domain-wall-engineering, ferroelectric-domain, ferroelectricity, kittel-law, sliding-ferroelectricity, topological-defects]
papers: [gomez-ortizKittelLawDomain2023, prosandeevKittelLawInBiFeO3Ultrathin2010, sunSlidingFerroelectricityTwodimensional2025]
updated: 2026-08
---

# 畴壁能 / Domain-Wall Energy

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


畴壁能（domain-wall energy, σ）指**铁电/铁磁有序体中相邻两个畴之间的界面单位面积能量**。畴壁能是基特尔定律（畴宽与膜厚平方根成正比）的核心物理量，决定了条纹畴、涡旋等拓扑畴结构的尺度与形貌；在超薄铁电膜中，畴壁能来自与体相不同的微观能量项（氧八面体倾斜、表面偶极、磁电耦合等）。

## 👵 太奶导读

太奶啊，铁电材料里"政见不同"的区（畴）之间隔着一条"边境线"，维持这条线要花能量——这就是畴壁能。边境线的"要价"直接决定了一个国家（畴）该划多大：要价高就分得碎。理论上一句话（基特尔定律）：畴宽和厚度开方成正比。但到了超薄薄膜里，这条边境线的成本构成会大换血，得重新精算。

## 🧩 畴壁能与基特尔定律

- **超晶格中的基特尔定律**：在 (PbTiO₃)ₙ/(SrTiO₃)ₙ 铁电/介电超晶格的极化涡旋相中，基特尔定律成立——最优畴宽与 PbTiO₃ 层厚的平方根成正比；处于畴密度偏低的亚稳态时，体系通过界面处成核涡旋-反涡旋对、涡旋延伸、反涡旋合并及对复合湮灭，弛豫到符合基特尔定律的基态 [[../papers/gomez-ortizKittelLawDomain2023]]。
- **BiFeO₃ 超薄膜中的畴壁能来源**：BiFeO₃ 超薄膜（厚度>约 20 Å）的规则条带状畴严格遵循基特尔定律，但其微观起源与传统铁电/铁磁薄膜截然不同——与畴密度成反比的能量项主要来自畴壁处氧八面体倾斜（AFD）的短程相互作用，与畴密度成正比的能量项则来自表面电偶极矩长程相互作用与磁电耦合 [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]]。

## 🧩 畴壁能与滑动铁电

- **Ripplocation 畴壁的独特优势**：二维滑动铁电体中存在独特的 "ripplocation" 畴壁，兼具低能垒高速翻转与高热力学稳定性的双重优势，其性能根源于不涉及强离子位移的层间滑移物理 [[../papers/sunSlidingFerroelectricityTwodimensional2025]]。

## 📊 畴壁能的能量构成

| 能量项 | 来源 | 对畴壁能贡献 |
|--------|------|--------------|
| 梯度/交换能 | 序参量空间变化 | 主项，决定壁宽 |
| 各向异性能 | 磁晶/晶体各向异性 | 压缩壁宽 |
| 弹性能 | 晶格应变 | 铁弹畴壁主项 |
| 长程偶极/磁电项 | 表面与畴壁相互作用 | 超薄膜关键项 |
| 氧八面体倾斜项 | AFD 畸变 | BiFeO₃ 超薄膜主项 |

## 📚 相关论文 (Related Papers)

- [[../papers/gomez-ortizKittelLawDomain2023]] — Kittel law and domain formation mechanism in PbTiO₃/SrTiO₃ superlattices
- [[../papers/prosandeevKittelLawInBiFeO3Ultrathin2010]] — Kittel Law in BiFeO₃ Ultrathin Films: A First-Principles-Based Study
- [[../papers/sunSlidingFerroelectricityTwodimensional2025]] — Sliding ferroelectricity in two-dimensional materials and device applications

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/domain-wall|畴壁]]：畴壁能的载体。
- [[../concepts/domain-wall-engineering|畴壁工程]]：对畴壁能的利用。
- [[../concepts/ferroelectric-domain|铁电畴]]：畴壁能划分的极化区域。
- [[../concepts/ferroelectricity|铁电性]]：畴壁能所属的能量景观。
- [[../concepts/kittel-law|基特尔定律]]：畴壁能与畴宽的定量关系。
- [[../concepts/sliding-ferroelectricity|滑动铁电]]：ripplocation 畴壁的母体机制。
- [[../entities/PbTiO3|PbTiO₃]]：极化涡旋超晶格的材料。
- [[../entities/SrTiO3|SrTiO₃]]：与 PbTiO₃ 构成超晶格的介电层。
- [[../entities/BiFeO3|BiFeO₃]]：氧八面体倾斜主导畴壁能的超薄膜。

## 🏷️ 专业名词别名

- `domain-boundary-energy`（concepts）
- `壁能密度`（concepts）
