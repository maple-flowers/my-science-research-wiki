---
tags: [concept, density-functional-theory]
title: core-valence-interaction
type: concept
status: developing
year: 2006
papers: [shishkinImplementationPerformanceFrequencydependentGWmethod2006]
updated: 2026-08-18
---

# core-valence-interaction

完全频率依赖的G₀W₀计算方法在PAW框架下的实现细节、算法效率及其在代表性半导体材料（sp材料：Si；含d电子材料：GaAs和CdS）中的准粒子能量计算性能。

## 👵 太奶导读

乖孙，这一条讲的是「完全频率依赖的G₀W₀计算方法在PAW框架下的实现细节、算法效率及其在代表性半导体材料（sp材料：Si；含d电子材料：GaAs和CdS）中的准粒子能量计算性能」。
一句话记住它的发现：在PAW框架下成功实现了高效的完全频率依赖G₀W₀计算，其计算耗时与传统的等离子激元极点模型近似相当。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：高精度GW计算（全频率依赖）通常计算成本过高，早期的近似方案（如等离子激元极点模型）在处理d电子等复杂体系时精度不足。如何在保留全频率计算精度的前提下，显著提升计算效率，并能够精确处理d电子和芯-价相互作用，是当时亟待解决的关键问题。
- **核心问题**：如何在投影缀加波（PAW）框架下，实现一种既高效又能保持全频率依赖精度的GW计算方法，并系统评估其相对于传统赝势方法和全电子方法的性能？作者旨在解决“效率-精度”矛盾，并利用PAW的独特优势克服传统方法在处理d电子和芯态时的物理局限。
- **主要结论**：在PAW框架下成功实现了高效的完全频率依赖G₀W₀计算，其计算耗时与传统的等离子激元极点模型近似相当。证明了PAW方法相较于赝势方法有三大优势：高效处理d电子、精确描述价波函数、以及能在Hartree-Fock级别准确处理芯-价相互作用。对Si、GaAs、CdS的计算给出了收敛的G₀W₀基准值，并证明结果对核心半径等参数具有鲁棒性。
- **领域贡献**：该工作开创性地将PAW方法、全频率GW计算与高效的谱表示技术相结合，提供了一个高精度、高效率且物理图像清晰的实用化GW计算方案。它奠定了PAW方法在激发态计算领域的领先地位，并使得后续对更复杂材料体系的GW研究成为可能，是计算材料学领域一方的里程碑式研究，对其后续广泛使用的VASP软件中GW计算模块的发展至关重要。
- **研究意义**：提供了一套在PAW框架下进行高效、全频率依赖GW计算的方法论，解决了传统方法效率与精度难以兼得的难题。该方法使得对含d/f电子的复杂体系进行高精度准粒子能量计算成为可能，为后续的材料激发态研究提供了强大的工具，并澄清了当时文献中不同全电子方法之间差异的来源。

## 📚 相关论文 (Related Papers)

- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]]：该工作开创性地将PAW方法、全频率GW计算与高效的谱表示技术相结合，提供了一个高精度、高效率且物理图像清晰的实用化GW计算方案。

## 🔗 关联概念与实体 (Related)

- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../entities/GaAs|GaAs]]
- [[../entities/VASP|VASP]]
