---
tags: [entity, density-functional-theory, dftb, nitrogen-doping, mulliken-population, odd-even-oscillation, surface-reconstruction, dimer-buckling, adsorption-energy]
title: DFTB+
type: entity
status: developing
year: 2021
papers: [Wei2021, Wu2018]
updated: 2026-08-18
---

# DFTB+

本文档围绕 **DFTB+** 汇集 2 篇论文的证据，覆盖其结构、物性与机制等多方面信息。

## 👵 太奶导读

乖孙，这一条讲的是「DFTB+」，由多篇论文的证据共同支撑。
一句话记住它的发现：氮原子环相对于碳原子环向内收缩，导致几何参数（如C/N环直径差）和电子性质（如能隙）出现奇偶振荡现象。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：实验上发现竹节状N-CNTs中氮原子倾向于在节点处富集且性能优异，但缺乏对这种特殊结构在原子尺度的精准构型、能量稳定性及电子特性的系统理论认识。高精度第一性原理计算难以处理包含数百个原子的大体系，而DFTB方法作为半经验量子力学方法，平衡了计算精度与效率，是研究此类问题的理想工具。
- **核心问题**：为了从理论角度探索竹节状N-CNTs，需要构建一个合理的原子模型并研究其性质。作者的核心问题是：在“氮原子层与碳原子层间隔排列”的模型下，竹节状N-CNTs的几何结构、能量稳定性、能隙、化学势以及电荷分布如何随管径（手性指数）变化？氮掺杂如何影响这些性质，并赋予材料新的应用潜力？
- **主要结论**：1. 氮原子环相对于碳原子环向内收缩，导致几何参数（如C/N环直径差）和电子性质（如能隙）出现奇偶振荡现象。2. N-CNTs的本征能和化学势均高于纯碳管，表明其热力学稳定性下降但化学活性增强。3. 氮掺杂可有效调控导电性，使大直径管呈现金属性，而某些小直径管保持半导体性。4. Mülliken布居分析揭示了电荷从氮原子向碳原子转移的复杂空间模式，且这种转移受管径和空间位置调制。；1. 成功获得了p(2×2)和c(4×2)两种稳定重构，其电荷分布模式不同；2. Ge原子优先吸附在Si二聚体的两种位置：翘起Si原子的顶位和二聚体的桥位；3. 最终稳定构型强烈依赖于初始吸附高度和位置，吸附能曲线存在多个局域极小值；4. 吸附Ge原子总是失去电荷，并显著影响Si二聚体的电荷转移、键长和翘曲角，其影响模式取决于Ge的最终吸附位置。
- **领域贡献**：1.构建了“氮/碳层交替”的竹节状N-CNTs原子模型，为理解高浓度氮掺杂结构提供了合理假设。2. 证明了SCC-DFTB方法是研究此类大尺度掺杂纳米体系的有效、经济的手段。3. 系统揭示了奇偶振荡效应、金属性转变和电荷转移机制等关键构效关系，填补了该体系部分理论认知空白。；1. 提供了单个Ge原子在Si(001)表面吸附的原子尺度高清图像，明确了能量最低的吸附位点；2. 首次系统地揭示了初始吸附高度这一常被忽略的参数对最终吸附构型的影响；3. 建立了结构与电荷转移之间的直接关联，从电子结构层面解释了吸附导致表面重构变化的微观机制；4. 验证了DFTB方法在该研究体系中的有效性和准确性。
- **研究意义**：本研究从原子尺度阐明了对竹节状N-CNTs的构效关系，将实验现象（如竹节状形貌、催化活性增强）与原子尺度行为（如氮环收缩、电荷转移）关联起来，为实验上制备具有特定电学性能和催化活性的N-CNTs提供了理论指导和筛选依据，具有重要的理论前瞻性和实践指导意义。

## 📚 相关论文 (Related Papers)

- [[../papers/Wei2021]]：1.构建了“氮/碳层交替”的竹节状N-CNTs原子模型，为理解高浓度氮掺杂结构提供了合理假设。
- [[../papers/Wu2018]]：1. 提供了单个Ge原子在Si(001)表面吸附的原子尺度高清图像，明确了能量最低的吸附位点；2. 首次系统地揭示了初始吸附高度这一常被忽略的参数对最终吸附构型的影响；3. 建立了结构与电荷转移之间的直接关联，从电子结构层面解释了吸附导致表面重构变化的微观机制；4. 验证了DFTB方法在该研究体系中的有效性和准确性。

## 🔗 关联概念与实体 (Related)

- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/dftb|dftb]]
- [[../concepts/nitrogen-doping|nitrogen-doping]]
- [[../concepts/mulliken-population|mulliken-population]]
- [[../concepts/odd-even-oscillation|odd-even-oscillation]]
- [[../concepts/curvature-effect|curvature-effect]]
- [[../concepts/charge-transfer|charge-transfer]]
- [[../concepts/chemical-potential|chemical-potential]]
- [[../concepts/sp2-sp3-hybridization|sp2-sp3-hybridization]]
- [[../entities/bamboo-like-N-CNTs|bamboo-like-N-CNTs]]
- [[../concepts/surface-reconstruction|surface-reconstruction]]
- [[../concepts/dimer-buckling|dimer-buckling]]
- [[../concepts/adsorption-energy|adsorption-energy]]
- [[../concepts/slab-model|slab-model]]
- [[../entities/Si|Si]]
- [[../entities/Ge|Ge]]
