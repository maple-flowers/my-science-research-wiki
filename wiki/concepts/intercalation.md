---
tags: [concept]
title: '插层 / Intercalation'
type: concept
status: developing
papers: ['wuElectrostaticGatingIntercalation2022', 'lezoualchStudyChargeDensity', 'zhaoRealization2DMultiferroic2024', 'yuFerroelectricControlMagnetism2026', 'tangMultiferroicityTwodimensionalVan2025', 'vahidmohammadiWorldTwodimensionalCarbides2021', 'petkovStructureIntercalatedCs2002']
updated: 2026-08-18
---

# 插层 / Intercalation

插层（intercalation）指**外来原子、离子或分子可逆地嵌入层状材料范德华间隙、或骨架材料孔道/空位**的化学过程，通常伴随电荷转移与结构膨胀。它是调控二维材料电子结构、磁性、超导电性与相变的强大工具——从碱金属插层石墨到过渡金属硫属化物（TMD）、MXene，再到多铁/磁性设计，插层提供了"软化学"路径实现块体合成难以企及的亚稳态。

## 👵 太奶导读

想象一本厚厚的书，书页之间能"夹进"各种小纸条——插层就是把原子、离子这些小纸条"夹"进二维材料层与层之间的空隙里。纸条放进去，既撑大了层间距，又给材料"捐"或"抢"电子，材料的导电性、磁性、颜色就全变了。更妙的是，往哪夹、夹多少都能控制，就像给材料"编程"。

## 🧩 插层的基本物理：电荷转移与结构响应

插层发生在层状材料的**范德华间隙**或骨架**孔道**中，其核心物理是**电荷转移**：插层物种（如碱金属、过渡金属离子）将电子注入/抽取宿主能带，同时撑大层间距。这在不破坏层内共价键的前提下，实现了对电子结构的**可逆、动态、极端调控**。Wu 等系统区分了**静电门控**（表面双电层，不进入层间）与**（脱）插层**（进入范德华间隙）两条互补路径，并强调低温拓扑化学（软化学）制备亚稳态相的独特优势（[[../papers/wuElectrostaticGatingIntercalation2022|Wu 2022]]）。

## 🔬 插层与电荷密度波

DFPT 声子软模计算揭示，化学掺杂（N、Na 等）与 STM 针尖物理操控可对 1T-VSe₂/1T-VTe₂ 的 CDW 相稳定性、取向与电子输运进行系统调控，插层/掺杂被纳入"CDW-tronics"概念框架（[[../papers/lezoualchStudyChargeDensity|Lezoualch]]）。插层改变费米面嵌套与电子-声子耦合，是设计 CDW 相的核心自由度。

## 🧲 插层设计多铁与磁性

- **超晶格插层高通量**：Zhao 等提出将过渡金属离子 A 非中心对称地插入 TMD 双层四方空位构建 AM₂X₄ 的"超晶格插层"通用策略，从 960 种候选物中高通量筛选出 21 种强磁电耦合二维多铁体，其中 T-CdCr₂Te₄ 可通过极化翻转可逆调控反斯格明子的产生与手性（[[../papers/zhaoRealization2DMultiferroic2024|Zhao 2024]]）。
- **插层诱导对称性破缺**：卤素 F 插层把双层 CrSBr"融合"为单层 Cr₄S₄FBr₂，通过 Jahn–Teller 畸变打破反演对称，在完全补偿亚铁磁金属中实现铁电-自旋-拓扑锁定（[[../papers/yuFerroelectricControlMagnetism2026|Yu 2026]]，见 [[../concepts/geometric-ferroelectricity|几何铁电性]]）。
- **二维多铁设计框架**：在范德华材料中"人工设计"多铁性的四大策略（磁中造电、电中生磁、弹中诱电、异质结组装）中，插层是"电中生磁/磁中造电"的核心手段（[[../papers/tangMultiferroicityTwodimensionalVan2025|Tang 2025]]）。

## 🔩 插层与无机材料家族

- **MXenes**：二维过渡金属碳/氮化物 M_{n+1}X_nT_x 依赖表面官能团插层与脱插层实现合成与性能调控，是插层化学的重要载体（[[../papers/vahidmohammadiWorldTwodimensionalCarbides2021|VahidMohammadi 2021]]）。
- **无机电子化合物**：原子对分布函数（PDF）给出直接结构证据，证明嵌入沸石 ITQ-4 伪一维孔道中的铯以 Cs⁺ 形式排列成锯齿形链，形成首个室温稳定无机电子化合物（[[../papers/petkovStructureIntercalatedCs2002|Petkov 2002]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/wuElectrostaticGatingIntercalation2022]] — Electrostatic gating and intercalation in 2D materials
- [[../papers/zhaoRealization2DMultiferroic2024]] — Realization of 2D multiferroic with strong magnetoelectric coupling by intercalation: a first-principles high-throughput prediction
- [[../papers/tangMultiferroicityTwodimensionalVan2025]] — Towards Multiferroicity in Two-Dimensional Van Der Waals Materials: Challenges and Opportunities
- [[../papers/vahidmohammadiWorldTwodimensionalCarbides2021]] — The world of two-dimensional carbides and nitrides (MXenes)
- [[../papers/lezoualchStudyChargeDensity]] — Study of charge density waves in transition metal dichalcogenides
- [[../papers/petkovStructureIntercalatedCs2002]] — Structure of Intercalated Cs in Zeolite ITQ-4: An Array of Metal Ions and Correlated Electrons Confined in a Pseudo-1D Nanoporous Host

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/2d-materials|二维材料]]：插层的作用对象——层状范德华材料家族。
- [[../concepts/charge-density-wave|电荷密度波]]：插层/掺杂调控 CDW 相稳定性的自由度。
- [[../concepts/multiferroicity|多铁性]]：插层诱导对称性破缺实现铁电-磁序共存。
- [[../concepts/topochemical-reaction|拓扑化学反应]]：低温插层合成亚稳态相的软化学路径。
- [[../concepts/interlayer-stacking|层间堆叠]]：决定插层位点与间隙大小的结构因素。
- [[../entities/MXenes|MXenes]]：依赖插层/脱插层调控性能的二维碳氮化物家族。
- [[../entities/AM2X4-intercalation-family|AM₂X₄ 插层家族]]：超晶格插层高通量筛选出的多铁材料族。
*（内容由AI生成，仅供参考）*
