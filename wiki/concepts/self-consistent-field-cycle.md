---
tags: [concept, computational-physics, vasp, dft]
title: Self-Consistent Field Cycle / 自洽场循环 (SCF)
type: concept
status: mature
domain: [computational-physics, electronic-structure]
mechanism: 通过不断迭代求解 Kohn-Sham 方程，混合电荷密度，直到输入与输出电荷密度一致，从而获得电子基态。
related_concepts: [rmm-diis, pulay-mixing, density-functional-theory]
papers: [kresseEfficiencyAbinitioTotal1996a, kresseEfficientIterativeSchemes1996d]
updated: 2026-08
---

# Self-Consistent Field Cycle / 自洽场循环 (SCF)

自洽场循环（SCF）是求解密度泛函理论（DFT）中 Kohn-Sham 方程的黄金标准流程。它是一种通过迭代逐步逼近电子基态密度与能量的自适应数值格式。

## 👵 太奶导读

太奶，这自洽场循环啊，特别像咱们擀面皮包饺子。你揉面的时候，加多少水（试探电荷密度）决定了面团怎么样，而面团怎么样又决定了你揉起来得使多大劲（势场）。

一上来，咱们谁也不知道最完美的比例是多少。所以咱们先凭感觉加点水（初始电荷密度），然后揉一揉。揉完发现面太硬了，说明不合适（产生残差），于是咱们就把刚才的经验和之前的好几步经验揉在一块，重新加点水（电荷密度混合），再试。就这样一遍一遍地揉（自洽迭代），直到你最后加进去的水，和揉出来的面团正好合拍，面团不干也不稀（输入密度等于输出密度）。这时候，饺子皮就擀好了（自洽收敛，找到了基态能量）！

## 🏗️ 结构概览

在 VASP 等程序中，自洽场循环分为“电子步”和“离子步”。

![图：VASP 的电子步自洽循环流程示意](../../raw/figures/kresseEfficiencyAbinitioTotal1996a/fig_10_D42XHL87.png)
*   注：由于此处暂无真实的图3（流程图），可用类似收敛图10展示自洽过程。
*   **看图要点**：随着迭代步数增加，系统总能量和电荷密度残差呈指数衰减，最终在 10–20 步内达到极高精度。
*   **来源**：[[../papers/kresseEfficiencyAbinitioTotal1996a]] -> [[../figures/mathematical-models-simulations|模拟与数值结果]]

## 🧩 物理与算法逻辑

### 1. 经典 SCF 迭代流程
1. **输入 $\rho_{in}$**：给出初始的电子密度分布。
2. **构建哈密顿量 $H[\rho_{in}]$**：计算 Hartree 势、交换关联势和外势。
3. **求解 Kohn-Sham 方程**：通过迭代对角化方法（如 RMM-DIIS 或 Davidson）解出单电子波函数 $|\psi_i\rangle$ 和本征值 $\epsilon_i$。
4. **计算输出 $\rho_{out}$**：由波函数模平方和部分占据数计算出新的电荷密度：
   $$ \rho_{out} = \sum f_i |\psi_i|^2 $$
5. **电荷混合**：利用 Pulay 或 Broyden 混合算法，将 $\rho_{in}$ 和 $\rho_{out}$ 融合成下一步的输入 $\rho_{in}^{next}$。
6. **收敛判断**：如果 $\Delta \rho$ 或能量变化小于阈值，则循环结束；否则回到第 2 步。

### 2. 能量最小化路线 vs SCF 路线
早期的 Car-Parrinello 方法和一些直接最小化算法（如 CGa）试图不建立自洽循环，而是把波函数和密度放在一个巨大的联合势能面上直接进行多维梯度下降。Kresse 等人的工作系统性地证明了，对于过渡金属和复杂体系，**“对角化波函数 + 独立混合电荷”的 SCF 路线在效率和稳定性上具有压倒性优势**。

### 3. 力的快速收敛修正 (Forces Corrections)
在自洽场尚未完全收敛时，直接计算原子力（Hellmann-Feynman 力）会引入极大的误差。VASP 引入了针对输入输出密度差的力修正项，使得即使自洽没做完，力的精度也极高，从而允许提前结束电子步，大大加速了离子弛豫和分子动力学模拟。

## 📚 相关论文 (Related Papers)

- [[../papers/kresseEfficiencyAbinitioTotal1996a]]：系统阐述了自洽循环路线相对于直接能量最小化路线的效率优势，并给出了力修正的关键公式。
- [[../papers/kresseEfficientIterativeSchemes1996d]]：进一步基准测试了 SCF 循环在不同体系中的可迁移性。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[rmm-diis|RMM-DIIS]]：用于 SCF 中快速解单电子方程的对角化算子。
- [[pulay-mixing|Pulay 混合]]：用于 SCF 中将输出密度稳定回馈为输入密度的数学手段。
- VASP (entity)：SCF 电子步由 INCAR 中的 NELM 控制。
