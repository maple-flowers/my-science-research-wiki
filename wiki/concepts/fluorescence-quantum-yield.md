---
tags: [concept, photophysics, spectroscopy]
title: 荧光量子产率 / Fluorescence Quantum Yield
type: concept
status: developing
domain: [photophysics, analytical-chemistry, photochemistry]
mechanism: 分子发射的光子数与吸收的光子数之比，反映了辐射跃迁与非辐射跃迁的竞争效率
related_concepts: [photoluminescence, solvatochromism, quenching]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence]
updated: 2026-08
---

# 荧光量子产率 / Fluorescence Quantum Yield

荧光量子产率（Fluorescence Quantum Yield, $\Phi$）是衡量发光物质发光效率的最核心指标。它定义为物质发射的光子数与吸收的光子数之比：
$$ \Phi = \frac{\text{发射的光子数}}{\text{吸收的光子数}} $$

## 👵 太奶导读

太奶啊，这就好比咱们**“算账的效率”**。您拿 100 粒大米（吸收的光子）去喂小鸡（发光分子），这小鸡消化之后，能吐出多少金砂（发射的光子）来，就是这个“量子产率”。如果这小鸡精神好、没生病（没有非辐射损失），喂 100 粒大米它能吐出 80 粒金砂（产率 80%，很亮）；但如果天太热或者环境不舒服（极性太强激活了扭转），它生病了，喂 100 粒大米才吐出 1 粒金砂（产率 1%，很暗），那剩下的能量都被它给“闷声浪费”（转化成热能散发）了。

## 🏗️ 物理机制

量子产率由辐射衰变速率（$k_r$）和所有非辐射衰变速率（$\sum k_{nr}$，如内转换、系间窜越、转动猝灭等）竞争决定：
$$ \Phi = \frac{k_r}{k_r + \sum k_{nr}} $$

*   **极性压制（TICT 猝灭）**：在极性环境中，许多具有 [[../concepts/d-pi-a-architecture]] 结构的分子会发生激子向非共面 [[../concepts/tict-mechanism|TICT]] 态的演化。由于 TICT 态通常具有极强的非辐射衰变速率（$k_{nr} \gg k_r$），会导致荧光量子产率在强极性溶剂中剧烈下降。例如，探针 P1 在低极性的二氧六环中 $\Phi = 0.885$，但在极性的 DMSO 中暴跌至仅为 $0.066$ [[../papers/Huang2019solvatochromic]]。

## 🔬 测量方法：相对测定法

在实验室中，量子产率通常通过与已知标准物对比的相对法进行测定：
*   **参比选择**：常用的标准参比物包括 0.05 M $H_2SO_4$ 中的**硫酸奎宁** ($\Phi = 0.546$)，或 0.1 M $NaOH$ 中的**荧光素**。
*   **测量要求**：需要保证待测样和参比物在同一激发波长下的吸光度极低（通常 $A < 0.05$），以避免自吸收和自内滤效应的干扰。

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：给出了双氰基二苯乙烯衍生探针在 10 种溶剂中的相对量子产率数据。
- [[../papers/Huang2019solvatochromic]]：使用硫酸奎宁为参比对量子产率进行标定的完整方法学说明。
- [[../papers/H2017fluorescence]]：分析了 $\Phi$ 与双光子吸收截面随溶剂极性同步下降的关联。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/photoluminescence|光致发光]]
- [[../concepts/tict-mechanism|TICT 机制]]
- [[../entities/quinine-bisulfate|硫酸奎宁 (标准物)]]
- [[../entities/fluorescein|荧光素 (标准物)]]
