# 光学与吸收光谱 (Optical & Absorption Spectra)

> 收录光吸收谱、介电函数（实部/虚部）、光电导率、折射率与反射率等光学响应相关的图表与物理公式。本页侧重介电矩阵与电荷自洽收敛中与介电响应直接相关的核心关系。

[[科研Wiki/wiki/figures/_index|← 返回总索引]]

---

## ⚡ 介电响应与电荷自洽收敛 (Dielectric Response & SCF Convergence)

### 1. 电荷介电矩阵 (Charge Dielectric Matrix)
在自洽场迭代中，电荷密度混合的雅可比矩阵 $J$ 即电荷介电矩阵，它由独立粒子极化率 $\chi$ 与库仑算符 $U$ 构成，是描述材料对外电荷扰动屏蔽响应（进而决定介电函数与光学响应）的核心关系。

$$ J = 1 - \chi\, U $$

*   **变量说明**：$J$ 为电荷介电矩阵（自洽迭代的雅可比矩阵），$\chi$ 为介电极化率（dielectric susceptibility），$U$ 为描述电荷密度变化引起势变化的库仑算符，在倒空间中 $\langle q'|U|q\rangle=\delta_{qq'}4\pi e^2/q^2$。金属中小 $q$ 处 $J$ 二次发散导致“电荷晃动”，绝缘体则不发散。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/dielectric-response|介电响应]]、[[../concepts/dielectric-function|介电函数]]、[[../concepts/optical-conductivity|光电导率]]、[[../concepts/polarizability-matrix|极化率矩阵 (χ)]]、[[../concepts/charge-density-mixing|电荷密度混合]]、[[../concepts/self-consistent-field-cycle|自洽场迭代 (SCF)]]、[[../concepts/coulombic-potential|库仑势]]、[[../concepts/density-functional-theory|密度泛函理论 (DFT)]]

**相关材料/实体**：[[../entities/VASP|VASP]]
