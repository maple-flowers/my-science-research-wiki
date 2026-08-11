# 电子能带与电子态 (Electronic Band Structures & DOS)

> 本页收录电子结构计算中最常被引用的核心物理公式，涵盖 Kohn-Sham 能量泛函与部分占据、VASP 迭代对角化（CG/RMM-DIIS）与电荷密度混合、超软赝势（USPP）总能与有效势、以及 LSDA/GGA 交换-关联泛函的构造。这些公式是理解能带结构、态密度、极化及磁性 DFT+U 等后续计算的方法学基础。

[[科研Wiki/wiki/figures/_index|← 返回总索引]]

---

## ⚛️ Kohn-Sham 能量泛函与部分占据 (KS Functional & Partial Occupancies)

### 1. 增广电荷积分 (Augmentation Charge Integral)
超软赝势中用于描述芯区电荷增广的辅助函数积分：

$$ q_{ij} = \int Q_{ij}(\mathbf{r})\, d^3r $$

*   **变量说明**：$Q_{ij}(\mathbf{r})$ 为增广函数（augmentation function），$q_{ij}$ 为其在实空间的积分，用于重建全电子电荷密度。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 2. 自洽局域势 (Self-Consistent Local Potential)
Hartree 势、交换-关联势与离子局域势之和，构成 KS 方程中的有效局域势：

$$ V_{loc}^{sc} = V_{loc}^{ion} + V_H[\rho] + V_{xc}[\rho] $$

*   **变量说明**：$V_H[\rho]$ 为 Hartree 势，$V_{xc}[\rho]$ 为交换-关联势；对于超软赝势，非局域部分还需通过增广电荷自洽更新。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 3. 非局域赝势系数 (Nonlocal PP Coefficient)
自洽增广后的非局域赝势矩阵元，包含离子贡献与局域势的增广积分：

$$ D_{ij}^{sc} = D_{ij}^{ion} + \int Q_{ij}(\mathbf{r})\, V_{loc}^{sc}(\mathbf{r})\, d^3r $$

*   **变量说明**：$D_{ij}^{ion}$ 为离子（裸）非局域系数，第二项为局域势在增广函数上的投影，是 USPP 自洽循环的关键。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 4. 广义本征值方程 (Generalized Eigenvalue Problem)
采用非正交基组（如超软赝势/PAW）时，KS 方程需以重叠矩阵 $S$ 表示为广义本征值问题：

$$ H|\psi_n\rangle = \sum_m g_{nm}\, S|\psi_m\rangle $$

*   **变量说明**：$g_{nm}$ 为厄米矩阵，其本征值即 KS 本征能量；该形式是金属体系部分占据与子空间对角化的出发点。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 5. Mermin 自由能零温外推 (Zero-Temperature Extrapolation)
利用 Mermin 有限温自由能 $F(\sigma)$ 与带能 $E(\sigma)$ 组合，消除展宽引起的熵误差，外推到 $s=0$ 的物理能量：

$$ E_{s=0} \approx \tilde{E}(\sigma) = \frac{1}{N+2}\left[(N+1)F(\sigma) + E(\sigma)\right] $$

*   **变量说明**：$\sigma$ 为展宽宽度，$N$ 为对应的熵项幂次；该修正使 Methfessel-Paxton/Gaussian 展宽下的总能量误差减小一个量级。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 6. 输入局域势 (Input Local Potential)
自洽循环中由输入电荷密度 $\rho_{in}$ 构造的局域有效势：

$$ V_{loc} = V_{loc}^{ion} + V_H[\rho_{in}] + V_{xc}[\rho_{in}] $$

*   **变量说明**：与自洽势 $V_{loc}^{sc}$ 相对应，$\rho_{in}$ 为上一轮混合后的电荷密度，是 Harris-Foulkes 非自洽步骤的基础。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 7. 电荷密度残差矢量 (Charge Density Residual)
自洽场（SCF）迭代中衡量输入与输出电荷密度偏差的核心量：

$$ R[\rho_{in}] = \rho_{out} - \rho_{in} $$

*   **变量说明**：$\rho_{out}$ 由新波函数按占据数求和得到；SCF 收敛等价于 $R[\rho_{in}]\to 0$，Pulay/DIIS 混合即基于该残差构造。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 8. 哈密顿量矩阵元 (Hamiltonian Matrix Element)
在投影基 $\{|q\rangle\}$ 下表示的 KS 哈密顿量矩阵元，用于力的计算与电荷密度更新：

$$ H_{qq'} = \langle q'|H|q\rangle $$

*   **物理意义**：对于超软赝势，$H$ 显式依赖于离子位置（通过增广电荷），求力时必须考虑增广项的贡献，否则力的误差可高达百倍。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

---

## 🔄 迭代对角化与电荷混合 (Iterative Diagonalization & Charge Mixing)

### 1. 子空间旋转 (Subspace Rotation)
在试探波函数张成的子空间内做精确对角化，得到最低本征值/本征矢的最佳近似：

$$ \epsilon_k^{app},\quad |\bar{f}_k\rangle = \sum_m B_{mk}|f_m\rangle $$

*   **变量说明**：$B_{mk}$ 为子空间内广义本征值问题的本征矢系数；旋转后残差不指向任何已包含能带，显著加速 RMM-DIIS 收敛。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 2. RMM-DIIS 正交条件 (RMM-DIIS Orthogonality)
残差最小化法要求每个能带的残差与子空间内所有其他试探矢量正交：

$$ \langle f_n|R(f_m)\rangle = 0 \quad ;\ m,n $$

*   **物理意义**：该条件保证沿"长谷"方向的搜索分量被有效抑制，使残差等价于预条件后的梯度，是 RMM-DIIS 稳定收敛的关键。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 3. Hamilton 构建的计算标度 (Hamiltonian Build Scaling)
利用快速傅里叶变换与实空间非局域投影，哈密顿量作用于波函数的计算量随体系大小呈近二次标度：

$$ T_H = N_b\, N_{plw}\, \ln N_{plw} \approx N^2 \ln N $$

*   **变量说明**：$N_b$ 为能带数，$N_{plw}$ 为平面波数；大体系中非局域投影算子改在实空间计算，使每能带操作数线性增长。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 4. Gram-Schmidt 正交化标度 (Orthogonalization Scaling)
子空间正交化（GS）是平面波 DFT 中主要的 $O(N^3)$ 开销：

$$ T_{GS} = \frac{N_b^2}{2}\, N_{plw} \approx N^3 $$

*   **物理意义**：该步骤将梯度对所有已收敛能带正交化，内存带宽是主要瓶颈；RMM-DIIS 通过子空间旋转将此开销降低约四倍。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 5. 梯度显式正交化标度 (Explicit Gradient Orthogonalization)
共轭梯度（CG）算法中，每个能带的梯度必须对所有其他能带显式正交，代价是 GS 的两倍：

$$ T_{ort} = 2\, N_b^2\, N_{plw} \approx 2 N^3 $$

*   **物理意义**：CG 严格串行且每步都需全正交化，难以利用内存缓存；RMM-DIIS 因此在大体系上明显更快。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 6. 单步对角化总开销 (Total Diagonalization Cost)
RMM-DIIS 单步对角化的总操作数为 Hamilton 构建与能带正交化之和：

$$ T_{diag} = T_H + 1.5\, N_b^2\, N_{plw} $$

*   **物理意义**：对大体系（正交化主导），RMM-DIIS 单步比 CG 快约四倍，且整体标度可接近 $O(N^2)$，是 VASP 千电子体系计算的核心。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 7. 介电 Jacobian (Dielectric Jacobian)
电荷混合中描述势-密度响应的线性算符，决定 SCF 迭代的稳定性：

$$ J = 1 - \chi U $$

*   **变量说明**：$\chi$ 为介电极化率，$U$ 为电荷密度变化引起势变化的算符；金属中 $\chi$ 在小 $q$ 处发散，导致"电荷晃动"（charge sloshing）。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 8. Hartree 库仑核 (Hartree Coulomb Kernel)
仅考虑 Hartree 势时，势响应算符在倒空间具有简单的 $4\pi e^2/q^2$ 形式：

$$ \langle q'|U|q\rangle = \delta_{qq'}\, \frac{4\pi e^2}{q^2} $$

*   **物理意义**：金属小 $q$ 处的二次发散是 SCF 收敛困难的根源；绝缘体中该发散被介电函数屏蔽，自洽计算显著更容易。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 9. Pulay 混合守恒约束 (Pulay Mixing Constraint)
Pulay/DIIS 混合中各历史电荷密度的线性组合系数必须守恒电子数：

$$ \sum_i a_i = 1 $$

*   **变量说明**：$a_i$ 为前 $i$ 步残差/输入密度的组合系数；在该约束下最小化残差范数即得到最优混合输入密度，形式与 RMM-DIIS 子空间步骤同源。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

---

## 🧮 超软赝势总能与有效势 (USPP Total Energy & Effective Potentials)

### 1. 全电子 KS 总能 (All-Electron KS Total Energy)
常规守恒模赝势框架下的 Kohn-Sham 总能量泛函：

$$ E = \sum_n f_n \left\langle \psi_n \left| -\frac{1}{2}\nabla^2 \right| \psi_n \right\rangle + E_H[n + n_Z] + E_{xc}[n]. \quad (1) $$

*   **变量说明**：$f_n$ 为占据数，$n$ 为价电子密度，$n_Z$ 为离子芯电荷密度；$E_H$ 与 $E_{xc}$ 分别为 Hartree 与交换-关联能。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 2. 赝波函数总能量 (Pseudized Total Energy)
引入赝密度 $\tilde{n}$、增广电荷 $\hat{n}$ 与芯补偿密度 $\tilde{n}_c$ 后的超软赝势总能量：

$$ \tilde{E} = \sum_n f_n \left\langle \tilde{\psi}_n \left| -\frac{1}{2}\nabla^2 \right| \tilde{\psi}_n \right\rangle + E_{xc}[\tilde{n} + \hat{n} + \tilde{n}_c] + E_H[\tilde{n} + \hat{n}] + \int v_H[\tilde{n}_{Zc}]\, (\tilde{n}(r) + \hat{n}(r))\, dr + U(R, Z_{ion}), \quad (21) $$

*   **变量说明**：$\tilde{n}$ 为软赝价密度，$\hat{n}$ 为局域增广电荷，$\tilde{n}_c$ 为非线性芯校正（NLCC）赝芯密度，$U$ 为离子-离子相互作用。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 3. 含投影算子的 USPP 总能 (USPP Total Energy with Projectors)
在赝总能量中加入非局域投影项，是 VASP 实际采用的超软赝势总能表达式：

$$ E = \sum_n f_n \left\langle \tilde{\psi}_n \left| -\frac{1}{2}\nabla^2 \right| \tilde{\psi}_n \right\rangle + \sum_{i,j} \left\langle \tilde{\psi}_n | \tilde{p}_i \right\rangle G_{ij}^{US} \left\langle \tilde{p}_j | \tilde{\psi}_n \right\rangle + E_{xc}[\tilde{n} + \hat{n} + \tilde{n}_c] + E_H[\tilde{n} + \hat{n}] + \int v_H[\tilde{n}_{Zc}]\, (\tilde{n}(r) + \hat{n}(r))\, dr + U(R, Z_{ion}), \quad (33) $$

*   **变量说明**：$\tilde{p}_i$ 为投影函数，$G_{ij}^{US}$ 为超软赝势增广矩阵；该式将平面波展开中缺失的芯区信息通过局域投影重新引入。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 4. 赝原子参考能量 (Pseudo-Atomic Reference Energy)
定义孤立原子参考态的赝增广能量，是双重计数校正的基准之一：

$$ \tilde{E}_1 = \sum_{i,j} r_{ij} \left[ \left\langle \tilde{\phi}_i \left| -\frac{1}{2}\nabla^2 \right| \tilde{\phi}_j \right\rangle + \overline{E_{xc}[\tilde{n}_1 + \hat{n} + \tilde{n}_c]} + \overline{E_H[\tilde{n}_1 + \hat{n}]} + \int_{V_r} v_H[\tilde{n}_{Zc}]\, (\tilde{n}_1(r) + \hat{n}(r))\, dr \right], \quad (22) $$

*   **变量说明**：$r_{ij}$ 为参考占据矩阵，$\tilde{\phi}_i$ 为赝原子轨道，上划线表示在增广区域 $V_r$ 内的积分。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 5. 全电子原子参考能量 (All-Electron Atomic Reference Energy)
与赝参考能量 $\tilde{E}_1$ 配对的全电子版本，二者之差确定超软赝势的非局域系数：

$$ E_1 = \sum_{i,j} r_{ij} \left[ \left\langle \phi_i \left| -\frac{1}{2}\nabla^2 \right| \phi_j \right\rangle + \overline{E_{xc}[n_1 + n_c]} + \overline{E_H[n_1]} + \int_{V_r} v_H[n_{Zc}]\, n_1(r)\, dr \right]. \quad (23) $$

*   **变量说明**：$\phi_i$ 为全电子原子轨道，$n_1$ 为全电子价密度；$E_1-\tilde{E}_1$ 是赝势生成过程中需要匹配的参考能差。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 6. 原子有效势 (Atomic Effective Potential)
孤立原子参考计算中使用的全电子有效势：

$$ v_{eff}^a = v_H[n_a + n_{Zc}] + v_{xc}[n_a + n_c]. \quad (31) $$

*   **变量说明**：$n_a$ 为原子价密度，$n_{Zc}$ 为芯+离子补偿密度；用于生成赝势时的原子基准。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 7. 赝原子有效势 (Pseudo-Atomic Effective Potential)
对应于赝密度的原子有效势，与 $v_{eff}^a$ 配对用于构造增广矩阵：

$$ \tilde{v}_{eff}^a = v_H[\tilde{n}_a + \hat{n}_a + \tilde{n}_{Zc}] + v_{xc}[\tilde{n}_a + \hat{n}_a + \tilde{n}_c]. \quad (32) $$

*   **变量说明**：$\tilde{n}_a$ 为赝原子价密度，$\hat{n}_a$ 为原子增广电荷；两者之差定义了超软赝势的非局域投影系数 $D_{ij}$。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 8. 固体赝有效势 (Solid Pseudo Effective Potential)
固体计算中由赝价密度、增广电荷与赝芯密度构造的有效势：

$$ \tilde{v}_{eff} = v_H[\tilde{n} + \hat{n} + \tilde{n}_{Zc}] + v_{xc}[\tilde{n} + \hat{n} + \tilde{n}_c]. \quad (43) $$

*   **物理意义**：该势代入赝 KS 方程后，与投影算子共同给出与全电子计算一致的价带结构，是 USPP 自洽循环的输出。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 9. 全电子参考有效势 (All-Electron Reference Potential)
用于双重计数校正的参考体系（无增广）有效势：

$$ v_{1eff}[n_1] = v_H[n_1 + n_{Zc}] + v_{xc}[n_1 + n_c]. \quad (45) $$

*   **变量说明**：$n_1$ 为仅由赝波函数平方求和得到的"软"价密度；与含增广势之差给出非局域投影项的修正。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 10. 赝参考有效势 (Pseudo Reference Effective Potential)
对应于赝参考密度 $\tilde{n}_1$ 的有效势，与 $v_{1eff}$ 共同确定增广矩阵的自洽修正：

$$ \tilde{v}_{eff1}[\tilde{n}_1] = v_H[\tilde{n}_1 + \hat{n} + \tilde{n}_{Zc}] + v_{xc}[\tilde{n}_1 + \hat{n} + \tilde{n}_c]. \quad (46) $$

*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 11. 双重计数校正 (Double-Counting Correction)
扣除 Hartree 与交换-关联能中被重复计算的增广部分，保证总能量泛函的变分一致性：

$$ \tilde{E}_{dc} = 2 E_H[\tilde{n} + \hat{n}] + E_{xc}[\tilde{n} + \hat{n} + \tilde{n}_c] - \int v_{xc}[\tilde{n} + \hat{n} + \tilde{n}_c]\, (\tilde{n} + \hat{n})\, dr, \quad (48) $$

*   **物理意义**：该项消除了赝密度重构中 Hartree 能与 XC 势作用的二次计数，是 USPP/PAW 总能量对密度变分后正确得到 KS 方程的必要条件。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 12. 赝参考双重计数校正 (Pseudo Reference DC Correction)
对应于参考密度 $\tilde{n}_1$ 的双重计数校正，与 $\tilde{E}_{dc}$ 一起用于增广区域的能量差修正：

$$ \tilde{E}_{dc1} = 2 E_H[\tilde{n}_1 + \hat{n}] + E_{xc}[\tilde{n}_1 + \hat{n} + \tilde{n}_c] - \int_{V_r} v_{xc}[\tilde{n}_1 + \hat{n} + \tilde{n}_c]\, (\tilde{n}_1 + \hat{n})\, dr. \quad (48) $$

*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 13. 非线性芯校正力 (NLCC Force)
含非线性芯校正（NLCC）时，离子受力中由赝芯密度梯度贡献的项：

$$ F_{nlcc} = -\int v_{xc}[\tilde{n} + \hat{n} + \tilde{n}_c]\, \frac{\partial \tilde{n}_c(r)}{\partial R}\, dr. \quad (56) $$

*   **变量说明**：$\partial \tilde{n}_c/\partial R$ 为赝芯密度随离子位置 $R$ 的梯度；该项对含浅芯层元素（如过渡金属、第一行元素）的力与应力计算至关重要。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

---

## 📈 交换-关联泛函与梯度近似 (XC Functionals & GGA)

### 1. LSDA 交换-关联能 (Local Spin-Density Approximation)
自旋极化局域密度近似下，XC 能为均匀电子气能量密度在实空间的积分：

$$ E_{XC}^{LSD}[n_\uparrow, n_\downarrow] = \int d^3r\, n\, \epsilon_{XC}^{unif}(n_\uparrow, n_\downarrow), \quad (1) $$

*   **变量说明**：$n=n_\uparrow+n_\downarrow$ 为总密度，$\epsilon_{XC}^{unif}$ 为均匀电子气的 XC 能量密度（由量子蒙特卡洛结果参数化）。
*   **来源**：[[../papers/perdewGeneralizedGradientApproximation1996a]]

### 2. GGA 交换-关联能 (Generalized Gradient Approximation)
广义梯度近似在 LSDA 基础上引入密度梯度作为额外变量：

$$ E_{XC}^{GGA}[n_\uparrow, n_\downarrow] = \int d^3r\, f(n_\uparrow, n_\downarrow, \nabla n_\uparrow, \nabla n_\downarrow). \quad (2) $$

*   **物理意义**：GGA 通过半局域梯度修正改善了原子化能、键长与表面能，PBE 是该形式下最广泛使用的无经验参数实现。
*   **来源**：[[../papers/perdewGeneralizedGradientApproximation1996a]]

### 3. 交换-关联能不等式 (Exchange-Correlation Inequality)
精确交换-关联能受严格的上下界约束，GGA 的增强因子必须满足该标度关系：

$$ E_X[n_\uparrow, n_\downarrow] \ge E_{XC}[n_\uparrow, n_\downarrow] \ge -1.679\, e^2 \int d^3r\, n^{4/3} \quad (13) $$

*   **物理意义**：下界对应均匀电子气的 Lieb-Oxford 极限；PBE 通过该约束确定增强因子中的参数 $\kappa$，保证泛函不违反精确标度条件。
*   **来源**：[[../papers/perdewGeneralizedGradientApproximation1996a]]

### 4. GGA 增强因子形式 (GGA Enhancement Factor)
PBE 将 GGA 写为 LSDA 交换能乘以无量纲增强因子 $F_{XC}$，后者依赖于 Wigner-Seitz 半径 $r_s$、自旋极化 $\zeta$ 与约化梯度 $s$：

$$ E_{XC}^{GGA}[n_\uparrow, n_\downarrow] = \int d^3r\, n\, \epsilon_X^{unif}(s)\, F_{XC}(r_s, \zeta, s). \quad (15) $$

*   **变量说明**：$s=|\nabla n|/(2k_F n)$ 为约化密度梯度；该形式将非局域性编码进 $F_{XC}$，在均匀极限（$s\to 0$）下自动恢复 LSDA。
*   **来源**：[[../papers/perdewGeneralizedGradientApproximation1996a]]

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/density-functional-theory|密度泛函理论 (DFT)]]、[[../concepts/ultrasoft-pseudopotential|超软赝势 (USPP)]]、[[../concepts/pseudopotential|赝势]]、[[../concepts/paw-method|投影缀加波方法 (PAW)]]、[[../concepts/exchange-correlation-functional|交换-关联泛函]]、[[../concepts/gga-functional|广义梯度近似 (GGA)]]、[[../concepts/iterative-diagonalization|迭代对角化]]、[[../concepts/charge-density-mixing|电荷密度混合]]、[[../concepts/pulay-mixing|Pulay 混合]]、[[../concepts/plane-wave-basis|平面波基组]]
