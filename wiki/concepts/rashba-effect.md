---
tags: [concept, spintronics, soc]
title: Rashba 效应 / Rashba Effect
type: concept
status: developing
domain: [spintronics, quantum-materials]
mechanism: 结构反演对称性破缺与自旋-轨道耦合协同导致的自旋能带分裂与自旋-动量锁定
related_concepts: [spin-orbit-coupling, magnetoelectric-coupling, sliding-ferroelectricity, spin-texture]
papers: [chenStrongSlidingFerroelectricity2024, wuSlidingFerroelectricity2D2021a, kaurRecentAdvancesTheoretical2025a, liuSpintronicsTwoDimensionalMaterials2020b, zhangNonvolatileControlTopological2025, zhongHighthroughputExfoliationMultiferroic2025]
updated: 2026-08
---

# Rashba 效应 / Rashba Effect

Rashba 效应（也称 Bychkov–Rashba 效应）是指在存在**结构反演对称性破缺 (Structural Inversion Asymmetry, SIA)** 的二维系统中，由于**自旋-轨道耦合 (Spin-Orbit Coupling, SOC)** 作用，电子的自旋简并能带发生分裂，并且自旋方向与动量方向相互锁定的物理现象。它是自旋电子学（Spintronics）中电场控制自旋的核心机制。

## Grandma 👵 太奶导读

太奶啊，这 **Rashba Effect**（拉什巴效应）听上去深奥，其实您把它想象成一列在旋转轨道上跑的“过山车”。
在一般的材料里，电子跑起来比较木讷，身上的小磁针（自旋，**spin**）是指向哪里的都有。
但在这个有 Rashba 效应的二维滑滑梯上，电子只要往前跑（动量，**momentum**），它身上的小磁针就必须横着指，就像是车头永远跟着轨道的弯走一样（自旋-动量锁定，**spin-momentum locking**）。
而且最神奇的是，如果这滑滑梯是带电的（比如滑动铁电材料），你只要把电极一翻转，所有电子身上的小磁针就会齐刷刷掉头，往反方向指。科学家们就是用这个法子，不用吸铁石，光用电门就能管住小磁针的方向！

## 🏗️ 结构概览

在二维滑动铁电体中，面外对称性的破缺自发感生出 Rashba 自旋分裂。

![图：+P 态 FE-HgI₂ 双层在倒易空间的 Rashba 自旋纹理](../../raw/figures/chenStrongSlidingFerroelectricity2024/fig_4_5NCCX3U9.png)
*   **看图要点**：图中展示了倒易面内电子自旋分量的切向环绕分布。内、外两个分支的螺旋性（Helicity）完全相反（分别呈顺时针和逆时针方向），展现出最经典的 Rashba 效应特征。
*   **来源**：[[../papers/chenStrongSlidingFerroelectricity2024]] -> [[../figures/electronic-devices-memory-transistors|存储器与晶体管]]

## 🧩 物理图像与哈密顿量

Rashba 效应的有效哈密顿量可表示为：

$$H_R = \alpha_R (\boldsymbol{\sigma} \times \mathbf{k}) \cdot \hat{\mathbf{z}} = \alpha_R (\sigma_x k_y - \sigma_y k_x)$$

其中：
*   $\alpha_R$ 是 **Rashba 系数**，决定能带分裂的强弱。
*   $\boldsymbol{\sigma}$ 是泡利自旋矩阵。
*   $\mathbf{k}$ 是电子的面内动量。
*   $\hat{\mathbf{z}}$ 是垂直于二维平面的单位矢量（对应面外电场或垂直极化 $P$ 的方向）。

在滑动铁电材料（如 HgI₂ 双层）中，$\hat{\mathbf{z}}$ 的方向由垂直铁电极化控制。通过机械滑移或电场将极化从 $+P$ 翻转为 $-P$ 时，内电场方向反转，导致 $\alpha_R \to -\alpha_R$，自旋纹理的顺/逆时针方向完全反向。这为无磁非易失性自旋场效应管（**Datta–Das spin-FET**）提供了极佳的半导体沟道材料。

## 📚 相关论文 (Related Papers)

- [[../papers/chenStrongSlidingFerroelectricity2024]]：利用 DFT+SOC 计算，预测了滑动铁电 HgI₂ 双层中极化可控的强 Rashba 效应。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：在滑动铁电领域奠基性展望中，将滑动铁电与 Rashba 效应的自旋纹理操控列为重大机遇方向。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]
- [[../papers/liuSpintronicsTwoDimensionalMaterials2020b]]
- [[../papers/zhangNonvolatileControlTopological2025]]
- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-orbit-coupling|自旋-轨道耦合 (SOC)]]
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]
- [[../concepts/spin-texture|自旋纹理]]
- [[../entities/HgI2|二碘化汞 (HgI₂)]]
- [[../entities/WTe2|二碲化钨 (WTe₂)]]
