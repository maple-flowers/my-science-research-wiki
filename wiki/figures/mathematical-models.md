# 数学模型与物理公式 (Mathematical Models & Formulas)

> 本页收录从文献库中筛选出的真实物理公式与数据表格，涵盖 DFT 电子结构方法（USPP/PAW、迭代对角化、Berry 相极化）、非线性光学与激光微加工、铁电/多铁器件基准、CDW 声子模、磁输运模型、以及相稳定性与弹性力学的解析判据。所有条目均直接取自原刊公式或数据表，剔除了 Zotero 元数据与 AI 转写噪声。

[[科研Wiki/wiki/figures/_index|← 返回总索引]]

---

## ⚛️ DFT 电子结构：PAW/赝势、对角化、Berry 相极化 (DFT Electronic Structure)

### 1. USPP/PAW 分子基准测试（键长与键角）
超软赝势（US-PP）、投影增强波（PAW）与全电子（AE）方法在小分子上的键长（Å）与键角（°）对照，验证 PAW 对全电子结果的可重现性：

| Molecule | US-PP | PAW | AE |
|----------|-------|-----|-----|
| H₂ | 1.447 | 1.447 | 1.446ᵃ |
| Li₂ | 5.127 | 5.120 | 5.120ᵃ |
| Be₂ | 4.524 | 4.520 | 4.521ᵃ |
| Na₂ | 5.667 | 5.663 | 5.67ᵃ |
| CO | 2.141 (2.127) | 2.141 (2.128) | 2.129ᵃ |
| N₂ | 2.077 (2.066) | 2.076 (2.068) | 2.068ᵃ |
| F₂ | 2.640 (2.626) | 2.633 (2.621) | 2.615ᵃ |
| P₂ | 3.570 | 3.570 | 3.572ᵃ |
| H₂O | 1.840 (1.834) | 1.839 (1.835) | 1.833ᵃ |
| α(H₂O) | 105.3° (104.8°) | 105.3° (104.8°) | 105.0° |
| BF₃ | 2.476 (2.470) | 2.476 (2.470) | 2.464ᵇ |
| SiF₄ | 2.953 (2.948) | 2.953 (2.948) | 2.949ᵇ |

*   **变量说明**：括号内为自旋极化或修正后的结果；上标 a、b 分别引用不同的全电子基准。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 2. 元素赝势/PAW 截断参数
各元素价电子构型、芯半径 $r_c^l$、补偿半径 $r_{comp}^l$ 与平面波动能截断 $E_{cut}$，是构建高精度 PAW 数据集的参考基准：

| Element | Valence | $r_c^l$ (a.u.) | $r_{comp}^l$ (a.u.) | $E_{cut}$ (eV) |
|---------|---------|-------------|-----------------|------------|
| H | 1s | 1.2 | 0.8 | 400 |
| Li | 1s2s2p | 2.0 | 2.0 | 160 |
| Be | 2s2p | 1.9 | 1.5 | 240 |
| B | 2s2p | 1.5s, 1.7p | 1.2 | 400 |
| C | 2s2p | 1.3s, 1.5p | 1.1 | 400 |
| N | 2s2p | 1.3s, 1.5p | 1.1 | 400 |
| F | 2s2p | 1.3s, 1.5p | 1.1 | 400 |
| Na | 2p3s | 2.2 | 1.5 | 210 |
| Si | 3s3p | 1.9 | 1.5 | 240 |
| P | 3s3p | 1.9 | 1.5 | 240 |
| Ca(1) | 3p4s3d | 3.0s, 2.3p,d | 1.5 | 230 |
| Ca(2) | 3s3p4s3d | 2.3 | — | 230 |
| V | 3p4s4p3d | 2.3 | 2.1 | 260 |
| Fe | 4s4p3d | 2.2 | 1.9s,p, 1.5d | 300 |
| Co | 4s4p3d | 2.2 | 1.9 | 300 |
| Ni | 4s4p3d | 2.2 | 1.9 | 300 |

*   **变量说明**：$r_c^l$ 为分波赝芯半径，$r_{comp}^l$ 为补偿电荷半径；含浅 $p$ 芯的元素（Ca、V、Fe 等）需要更高截断。
*   **来源**：[[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]

### 3. RMM-DIIS 与 CG 对角化耗时对比（Γ 点）
单胞放大倍数 $N_{cell}$、离子数 $N_{ions}$ 与 RMM-DIIS、共轭梯度（CG、CGa）单步耗时（秒）的对比，显示大体系下 RMM-DIIS 的优势：

| $N_{cell}$ | $N_{ions}$ | RMM | CG | CGa |
|-------|-------|-----|-----|-----|
| 1 | 8 | 1.0 | 1.0 | 1.2 |
| 2 | 16 | 3.0 | 3.0 | 3.2 |
| 4 | 32 | 10.0 | 10.0 | 9.0 |
| 8 | 64 | 35.0 | 50.0 | 32.0 |
| 3×3×3 | 216 | 410.0 | 800.0 | — |

*   **变量说明**：CGa 为采用近似优化的 CG 变体；216 原子体系 RMM-DIIS 较 CG 快约两倍。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 4. 含 k 点采样的对角化标度
固定总能带数、改变单胞与 $k$ 点数时 RMM-DIIS 与 CGa 的耗时对比，体现实空间非局域投影在大体系下的线性增益：

| $N_{cell}$ | $N_{ions}$ | $N_k$ points | RMM | CGa |
|-------|-------|-----------|------|------|
| 1 | 4 | 32 | 21.0 | 16.0 |
| 2 | 8 | 16 | 39.0 | 32.0 |
| 4 | 16 | 8 | 80.0 | 65.0 |
| 8 | 32 | 2 | 92.0 | — |
| 3×3×3 | 108 | 1 | 360.0 | — |

*   **变量说明**：$N_{ions}\times N_k$ 近似守恒；当 $k$ 点减少、单胞增大时，RMM-DIIS 相对 CG 的标度优势持续扩大。
*   **来源**：[[../papers/kresseEfficientIterativeSchemes1996d]]

### 5. Berry 相极化：波函数相位积分
现代极化理论中，绝热路径上极化变化由占据态波函数在布里渊区中的 Berry 联络积分给出：

$$ \Delta P = \frac{i f q_e}{8\pi^3} \sum_n \int_{\mathrm{BZ}} d\mathbf{k}\, \left\langle u_{\mathbf{k}n}^{(\lambda)} \middle| \frac{\partial}{\partial \mathbf{k}} \middle| u_{\mathbf{k}n}^{(\lambda)} \right\rangle $$

*   **变量说明**：$f$ 为价带简并度，$q_e$ 为电子电荷，$u_{\mathbf{k}n}^{(\lambda)}$ 为绝热参数 $\lambda$ 下的周期部分；该式将极化转化为波函数的几何相位。
*   **来源**：[[../papers/king-smithTheoryPolarizationCrystalline1993]]

### 6. Berry 相极化：Kohn-Sham 势响应形式
以 Kohn-Sham 势对绝热参数的导数表示的极化变化，是 Berry 相公式在密度泛函框架下的等价形式：

$$ \Delta P_n = \frac{f q^2}{\Omega} \sum_{\mathbf{k},m} \int_0^1 d\lambda\, \left\langle \psi_{n\mathbf{k}} \middle| \frac{\partial V_{KS}}{\partial \lambda} \middle| \psi_{m\mathbf{k}} \right\rangle $$

*   **变量说明**：$\Omega$ 为原胞体积，$\psi_{n\mathbf{k}}$ 为 KS 本征态；该式表明极化变化可由基态对势扰动的响应计算。
*   **来源**：[[../papers/king-smithTheoryPolarizationCrystalline1993]]

### 7. Berry 相极化：导数差形式
将波函数对绝热参数与对 $k$ 的导数之差积分，显式给出极化的几何（Berry 曲率）表达式：

$$ \Delta P_n = \frac{i f q^2}{\Omega} \int_{\mathrm{BZ}} \frac{d\mathbf{k}}{(2\pi)^3} \sum_{m=1}^{M} \int_0^1 d\lambda\, \left[ \left\langle \frac{\partial u_{n\mathbf{k}}}{\partial \lambda} \middle| \frac{\partial u_{n\mathbf{k}}}{\partial k_n} \right\rangle - \left\langle \frac{\partial u_{n\mathbf{k}}}{\partial k_n} \middle| \frac{\partial u_{n\mathbf{k}}}{\partial \lambda} \right\rangle \right] $$

*   **变量说明**：方括号内为 Berry 联络的反对称导数，即沿绝热路径的 Berry 曲率；该式是 Wannier 中心极化计算的基础。
*   **来源**：[[../papers/king-smithTheoryPolarizationCrystalline1993]]

### 8. 一维极化：沿弦的 Berry 相
沿倒空间路径 $C$ 积分得到的一维极化，直接对应 Wannier 函数中心的位移：

$$ \Delta P = \frac{e f}{a} \sum_{n=1}^{M} \int_C \mathbf{A}_n(\mathbf{k})\cdot d\mathbf{k}, \qquad \mathbf{A}_n = i\langle u_{n\mathbf{k}}|\nabla_{\mathbf{k}}|u_{n\mathbf{k}}\rangle $$

*   **变量说明**：$a$ 为沿极化方向的晶格常数，$\mathbf{A}_n$ 为 Berry 联络；积分给出以 $e/a$ 为量子的极化，即 Wannier 中心位移乘以电荷。
*   **来源**：[[../papers/king-smithTheoryPolarizationCrystalline1993]]

### 9. Born 有效电荷与压电系数（GaAs 类闪锌矿）
晶格常数、Born 有效电荷 $Z^*_{Ga}$ 与压电系数 $(a/e)\gamma'_{14}$、$\gamma_{14}$ 在本工作、线性响应与实验间的对照：

| Method | $a$ (Å) | $Z^*_{Ga}$ | $(a/e)\gamma'_{14}$ | $\gamma_{14}$ |
|--------|---------|------------|---------------------|---------------|
| This work | 5.576 | 0.542 | 1.984 | −1.352, −0.28 |
| Linear response | 5.496 | 0.528 | 1.994 | −1.405, −0.35 |
| Experiment | 5.642 | 0.55 | 2.16 | −0.32 |

*   **变量说明**：$Z^*_{Ga}$ 为 Ga 原子的 Born 有效电荷，$\gamma_{14}$ 为压电应力系数（两个值分别对应弛豫离子与钳制离子情形）。
*   **来源**：[[../papers/king-smithTheoryPolarizationCrystalline1993]]

---

## 💡 介电/光学：非线性光学、激光微加工、Mathieu 光束、红外滤光片 (Dielectric & Optical)

### 1. 双光子吸收能量沉积率
双光子聚合过程中单位体积能量沉积率正比于光强平方与三阶非线性极化率虚部：

$$ \frac{dW}{dt} = \frac{8\pi^2 \omega}{c n^2} I^2 \operatorname{Im}[\chi^{(3)}] $$

*   **变量说明**：$\omega$ 为角频率，$n$ 为折射率，$I$ 为光强，$\chi^{(3)}$ 为三阶非线性极化率；该式是双光子聚合阈值模型的出发点。
*   **来源**：[[../papers/Kumar2017microstructuring]]

### 2. 双光子聚合阈值条件
引发聚合所需的单位体积阈值能量由吸收系数、脉冲宽度与重复频率共同决定：

$$ I_{th}^2 \beta \tau f t \ge E_{th} $$

*   **变量说明**：$I_{th}$ 为阈值光强，$\beta$ 为双光子吸收系数，$\tau$ 为脉宽，$f$ 为重复频率，$t$ 为曝光时间，$E_{th}$ 为阈值能量密度。
*   **来源**：[[../papers/Kumar2017microstructuring]]

### 3. 聚焦高斯光束光强分布
高数值孔径物镜聚焦后的高斯光束径向光强分布：

$$ I(r,z) = \frac{2P}{\pi w(z)^2} \exp\left[-2\left(\frac{r}{w(z)}\right)^2\right] $$

*   **变量说明**：$P$ 为平均功率，$w(z)$ 为位置 $z$ 处的束腰半径，$r$ 为离轴距离；用于计算双光子吸收的空间选择性。
*   **来源**：[[../papers/Kumar2017microstructuring]]

### 4. 高斯光束束腰沿传播方向的演化
由物镜数值孔径 $NA$ 与介质折射率 $n$ 决定的束腰半径 $w(z)$：

$$ w(z) = \frac{\lambda}{\pi \tan[\sin^{-1}(NA/n)]} \left[1 + \left(\frac{z}{\lambda/[\pi \tan(\sin^{-1}(NA/n))]}\right)^2\right]^{1/2} $$

*   **变量说明**：$\lambda$ 为波长；束腰最小值与焦深共同决定双光子聚合体素（voxel）的长宽比。
*   **来源**：[[../papers/Kumar2017microstructuring]]

### 5. 聚合体素横向直径
由阈值条件反解得到的双光子聚合体素横向直径：

$$ D(t,NA,P_{av},f) = \frac{\lambda}{\pi \tan[\sin^{-1}(NA/n)]} \left[\ln\left(\frac{4\pi^4 \tan^4[\sin^{-1}(NA/n)] P_{av} f t}{E'_{th} \lambda^4}\right)\right]^{1/2} $$

*   **变量说明**：$P_{av}$ 为平均功率，$E'_{th}$ 为有效阈值能量；体素直径随曝光时间与功率对数增长。
*   **来源**：[[../papers/Kumar2017microstructuring]]

### 6. 聚合体素轴向长度
对应于体素沿光轴方向的长度，决定三维微加工的纵向分辨率：

$$ L(t,NA,P_{av},f) = \frac{2\lambda}{\pi \tan[\sin^{-1}(NA/n)]} \left[\left(\frac{4\pi^4 \tan^4[\sin^{-1}(NA/n)] P_{av} f t}{E'_{th} \lambda^4}\right)^{1/2} - 1\right]^{1/2} $$

*   **物理意义**：轴向长度通常大于横向直径，是双光子聚合中椭圆体素的来源；提高 NA 可同时压缩二者。
*   **来源**：[[../papers/Kumar2017microstructuring]]

### 7. 椭圆柱坐标变换
描述 Mathieu 光束所采用的椭圆柱坐标 $(\xi,\eta,z)$ 与直角坐标的关系：

$$ \begin{cases} x = c\cosh(\xi)\cos(\eta) \\ y = c\sinh(\xi)\sin(\eta) \\ c^2 = a^2 - b^2, \end{cases} \qquad \xi\ge 0,\; 0\le\eta<2\pi $$

*   **变量说明**：$a$、$b$ 为椭圆长、短半轴，$c$ 为焦距；$\xi$ 为径向椭圆坐标，$\eta$ 为角向坐标。
*   **来源**：[[../papers/Wang2023ultracompact]]

### 8. Mathieu–Gauss 光束模式
偶、奇、螺旋三种宇称的标量 Mathieu–Gauss 光束表达式：

$$ \begin{cases} M_e(\xi,\eta,z;q) = Ce_m(\xi;q)\,ce_m(\eta;q)\exp(ik_z z) \\ M_o(\xi,\eta,z;q) = Se_m(\xi;q)\,se_m(\eta;q)\exp(ik_z z) \\ M_h(\xi,\eta,z;q) = [A_m(q)Ce_m(\xi;q)ce_m(\eta;q) + iB_m(q)Se_m(\xi;q)se_m(\eta;q)]\exp(ik_z z), \end{cases} $$

*   **变量说明**：$Ce_m/ce_m$ 与 $Se_m/se_m$ 分别为 $m$ 阶偶、奇宇称的径向（修正）与角向 Mathieu 函数，$q=c^2 k_t^2/4$ 为椭圆参数，$k_z$ 为纵向波矢。
*   **来源**：[[../papers/Wang2023ultracompact]]

### 9. 傅里叶谱主环半径与宽度
4-$f$ 系统中 Mathieu 光束傅里叶谱主环的半径 $R$ 与环宽 $\Delta R$：

$$ \begin{cases} R = \dfrac{k_t \lambda f_1}{2\pi} \\ \Delta R = \dfrac{2\lambda f_1}{\omega_0 \pi}, \end{cases} $$

*   **变量说明**：$f_1$ 为傅里叶透镜焦距，$\omega_0$ 为入射高斯光束束腰；$R$ 由横向波矢决定，$\Delta R$ 由高斯包络决定。
*   **来源**：[[../papers/Wang2023ultracompact]]

### 10. 相位板高度与相位分布的关系
飞秒激光双光子聚合制备的相位板中，局部高度与所编码相位的换算关系：

$$ h(x,y) = \frac{\lambda\,\varphi(x,y)}{2\pi(n_p - 1)} $$

*   **变量说明**：$n_p$ 为光刻胶折射率，$\varphi(x,y)$ 为所需相位；二元相位 $0$、$\pi$ 对应高度 $0$ 与 $\lambda/(n_p-1)$。
*   **来源**：[[../papers/Wang2023ultracompact]]

### 11. PbSnTe 红外窄带滤光片设计参数（一）
基于法布里-珀罗结构的 MBE 生长 PbSnTe 红外滤光片峰值波长、折射率与腔厚设计：

| $\lambda_{max}$ (μm) | $\nu_{max}$ (cm⁻¹) | $n$ | $d$ (μm) | $\Delta\nu$ (cm⁻¹) | Bandwidth (%) |
| --- | --- | --- | --- | --- | --- |
| 10.5 | 950 | 5.5 | 2.67 | 47 | 24.7 |
| 8.0 | 1250 | 5.5 | 3.42 | 60 | 24.0 |
| 6.25 | 1600 | 5.5 | 4.50 | 90 | 28.0 |

*   **变量说明**：$d$ 为腔层厚度，$\Delta\nu$ 为通带半宽；折射率取 $n=5.5$，覆盖 6–11 μm 红外大气窗口。
*   **来源**：[[../papers/Srinivasan1989lead]]

### 12. PbSnTe 红外窄带滤光片设计参数（二）
包含带外最小透过率约束的滤光片参数对照，用于评估阻带抑制能力：

| $d$ (μm) | $\lambda_{max}$ (μm) | $\nu_{max}$ (cm⁻¹) | $\Delta\nu$ (cm⁻¹) | Bandwidth (%) | Min. transmittance outside pass band (%) |
| --- | --- | --- | --- | --- | --- |
| 2.67 | 10.5 | 950 | 47 | 24.7 | 20 |
| 3.42 | 8.0 | 1250 | 60 | 24.0 | 20 |
| 4.50 | 6.25 | 1600 | 90 | 28.0 | 20 |

*   **物理意义**：带外最小透过率约 20%，表明需配合阻挡层进一步抑制阻带。
*   **来源**：[[../papers/Srinivasan1989lead]]

### 13. TTF⁺ 电荷转移聚集体非线性吸收参数
PMMA 基质中四硫富瓦烯阳离子自由基（TTF⁺）电荷转移聚集体的非线性吸收拟合参数：

| $\lambda$ [nm] | $\Delta t_{FWHM}$ [s] | $z_0$ [cm] | $L$ [μm] | $\sigma$ [cm²/dimer] | $\alpha L$ |
|---------|--------------|----------|----------|----------------|-----|
| 792 | 125×10⁻¹⁵ | 0.159 | 30 | 1.10×10⁻¹⁸ | 1.47 |

*   **变量说明**：$\Delta t_{FWHM}$ 为激光脉宽，$z_0$ 为共焦参数，$L$ 为膜厚，$\sigma$ 为每二聚体的有效吸收截面，$\alpha L$ 为光学厚度。
*   **来源**：[[../papers/Scremin2018nonlinear]]

---

## 🔋 铁电/多铁：HZO 器件、2D FE 综述、挠曲电场 (Ferroelectric & Multiferroic)

### 1. HZO 掺杂薄膜铁电性能基准
不同掺杂剂（Zr、Si、La、Al）、浓度、厚度与电极堆叠下 HfO₂ 基铁电薄膜的剩余极化 $2P_r$、矫顽场 $E_c$ 与热稳定性汇总：

| Dopants | Doping [mol%] | Thickness [nm] | Stack | $2P_r$ [μC cm⁻²] | $E_c$ [MV cm⁻¹] | Thermal stability | Ref. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Zr | 50 | 4 | TiN/HZO/TiN | 15 | N/A | Retention > 10⁴ s @ 85 °C | [73] |
| Zr | 50 | 8.9 | W/HZO/W | 53.9 | 1.37 | Excellent thermal stability | [74] |
| Zr | 50 | 10 | Au/HZO/LSMO | 40 | 2.5 | No significant wake-up effect | [75] |
| Zr | 50 | 15 | W/HZO/W | 18.3 | 1.4 | Retains data at 250 °C | [76] |
| Si | 4.2 | 10 | Pt/HSO/TiN | 15 | 1.0 | Excellent thermal stability | [77] |
| Si | 4.6 | 10 | TiN/HSO/TiN | 16–34 | N/A | No degradation after 1000 h @ 125 °C | [78] |
| La | 2 | 8.5 | Pt/HL/LSMO | 44 | 4.42 | 10 years retention @ 85 °C | [79] |
| La | 3 | 10 | W/IGZO/HLO/TaN | 16.8 | 2.2–3.0 | Stable @ 700 °C, 10-s RTA | [66] |
| Al | 3 | 4.5 | W/HAO/W | 20 | 8.6 | FE performance after 850 °C anneal | [61] |
| Al | 4.8 | 16 | TiN/HAO/TiN | 10 | 1.0 | Ferroelectricity up to 1000 °C | [54] |
| La + Al | Al:4.2, La:2.17 | 10 | W/HfAlLaO/W | 22 | 1.6 | 10⁸ cycles @ 85 °C | [70] |

*   **变量说明**：HSO/HLO/HAO 分别为 Si/La/Al 掺杂的 HfO₂；$2P_r$ 随厚度与电极材料变化显著，W 电极有利于保持高极化。
*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]]

### 2. HZO 铁电器件性能基准
FeFET、FTJ、FeRAM、Fe-Diode 四类 HZO 基铁电器件的开关速度、保持、耐久性与功耗横向对比：

| Device type | Structure | FE material | Switching speed | Retention | Endurance | Power consumption | Ref. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FeFET | MFS | HZO (10 nm) | N/A | > 10⁴ s | > 10⁶ cycles | pA/μm off-state leakage | [4] |
| FeFET | MFS | HZO (10 nm) | 40 ns | > 1500 s | 8×10⁶ cycles | Extremely low writing energy | [92] |
| FeFET | MFIS | HZO (5 nm) | 1 μs | > 10⁵ s | > 10⁵ cycles | 3.8 V operating voltage | [99] |
| FeFET | MFIS | HSO (10 nm) | 300 ns | N/A | > 10⁵ cycles | Low gate leakage | [100] |
| FeFET | MFMIS | HAO (10 nm) | 500 ns–10 μs | > 10⁴ s | N/A | 2–5 V operating voltage | [80] |
| FTJ | Pt/SiO/HZO/TiN | HZO (2 nm) | 500 ps | > 10⁵ s | > 10⁷ cycles | 0.12 fJ/bit write energy | [82] |
| FTJ | Pt/HZO/LSMO | HZO (2 nm) | < 500 ns | > 10⁵ s | N/A | N/A | [101] |
| FTJ | Pt/HZO/TiO₂/TiN | HZO (4.2 nm) | 50 ns | > 10⁵ s | > 2×10⁸ cycles | < 10 fJ | [5] |
| FTJ | TiN/HZO/TaN/W | HZO (5.5 nm) | N/A | > 10 years | 10⁸ cycles | 1.5–3.5 V operating voltage | [101] |
| FTJ | TiN/HZO/Pt | HZO (9 nm) | 100 ns | N/A | > 10³ cycles | 1.8 pJ/spike | [8] |
| FeRAM | TiN/HZO/TiN | HZO (4 nm) | N/A | > 10 years | > 10¹² cycles | 1.2 V operating voltage | [84] |
| FeRAM | TiN/HZO/TiN | HZO (8 nm) | N/A | > 10 years | > 10⁹ cycles | 2.0 V operating voltage | [95] |
| FeRAM | TiN/HZO/TiN | HZO (10 nm) | N/A | > 10 years | > 10¹³ cycles | 1.5 V operating voltage | [86] |
| Fe-Diode | MOFM | HZO (7 nm) | 800 ps | > 10 years | > 10⁹ cycles | 0.8 fJ | [102] |
| Fe-Diode | W/MoS₂/HZO/TiN | HZO (8 nm) | 200 ns | > 10 years | > 10¹⁰ cycles | 158.5 fJ/operation | [88] |
| Fe-Diode | TiN/HZO/TiN | HZO (10 nm) | 20 ns | > 5×10⁴ s | > 10⁹ cycles | 1 μA operating current | [31] |

*   **物理意义**：FTJ 与 Fe-Diode 可实现亚纳秒开关与飞焦级写入能耗，FeRAM 在耐久性上最优（>10¹² 次）。
*   **来源**：[[../papers/chenHafniumBasedFerroelectricPostMoore2026]]

### 3. 二维铁电材料实验综述
h-BN、石墨烯、MoS₂、MX₂ 及理论预测的二维铁电材料的极化强度、实现策略与表征技术汇总：

| Material | Phase | Stacking | Layers | Space/point group | Polarization intensity | Strategy | Characterization | Ref. |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| hBN |  | parallel | 2 |  | $P_{2D}=2.25(0.37)\times10^{-12}$ C m⁻¹ | noncentrosym. stacking | vertical PFM | 25 |
| hBN |  | parallel | 2 |  | $PZ/A=0.33$ Debye/nm² | noncentrosym. stacking | KPFM | 26 |
| hBN |  | Bernal-type | multi |  | 3.01 Debye/nm² | noncentrosym. stacking | KPFM, PUND | 31 |
| graphene |  | Bernal & rhombohedral | >3 |  | 0.32 pC/m | noncentrosym. stacking |  | 37 |
| hBN |  | 7/90 nm twist |  |  |  |  | PFM | 38 |
| hBN/graphene |  | rhombohedral | 3 |  | 1.76 μC/cm² | heterostructure | device | 39 |
| graphene |  | Bernal | 2 |  | 5 pC/m |  | FTJ | 40 |
| MoS₂ | 2H |  | 2 |  | $d_{33}=37.54$ pm/V | strain | PFM, FTJ, C-AFM | 41 |
| MoS₂ | 3R | rhombohedral | 2 | $P\bar{3}m1$ | 0.8–1.5 pC/m | photoexcitation |  | 42 |
| MoS₂/WS₂ |  | 3R-/2H-like | 2 | 3m | $d_{33}=1.95$–2.09 pm/V | heterostructure | PFM | 43 |
| MoS₂ | 3R | rhombohedral | 2 | $C_{3v}$ |  | stacking | device | 44 |
| CCC |  |  |  | $P2_1$ | 0.3–0.4 μC/cm² | hybrid crystal | PFM | 45 |
| HgI₂ |  |  |  | $Cmc2_1$ | 0.16 μC/cm² | theoretical |  | 46 |
| NbI₄ |  |  |  | $Cmc2_1$ | 0.11 μC/cm² | theoretical |  | 47 |
| kagome-B₂X₃ |  |  | 2 | $P\bar{6}2m$, $P1$, $P321$, $Cm$, $C2$ |  | theoretical |  | 48 |
| ZrI₂ |  |  | 2 | $Pmn2_1$ | 0.39 μC/cm² | theoretical |  | 49 |
| β-ZrI₂ |  |  |  | $C_{1h}$ |  | theoretical |  | 51 |

*   **变量说明**：$P_{2D}$ 为二维面内极化（单位 C m⁻¹），$PZ/A$ 为每面积偶极矩，$d_{33}$ 为压电系数；实验策略包括堆叠、应变、异质结与光激发。
*   **来源**：[[../papers/zhangEmergingFrontiersTwodimensional2025]]

### 4. 挠曲电场（Flexoelectric Field）
应变梯度诱导的等效电场，是压电响应力显微镜（PFM）中区分挠曲电与压电贡献的核心公式：

$$ E_f = \frac{f}{\varepsilon}\cdot\frac{\partial e}{\partial z} $$

*   **变量说明**：$f$ 为挠曲电系数，$\varepsilon$ 为介电常数，$\partial e/\partial z$ 为沿深度方向的应变梯度；即使在非压电材料中，针尖压入引起的应变梯度也可产生 $E_f$。
*   **来源**：[[../papers/Chen2016electrical]]

---

## 🌊 CDW 与强关联 (CDW & Strong Correlations)

### 1. 2H-NbSe₂ CDW 声子模频率的温度依赖
有/无应力条件下，2H-NbSe₂ 中剪切模与 CDW 振幅模的拉曼频率（cm⁻¹）随温度的演化：

| Mode (cm⁻¹) | Exp – 4 K | 10 K | 30 K | 50 K | 60 K | 300 K |
|-------------|-----------|------|------|------|------|-------|
| $E^2_{2g}$ (shear) – Stressed | 26 | 30.7 | X | X | X | 32.8 |
| $2E_{2g}$ (CDW) – Stressed | 51 | 48.8 | 46.6 | 44.6 | 42.8 | X |
| $1A_{1g}$ (CDW) – Stressed | 79 | 76.0 | 67.6 | 63.0 | 62.6 | X |
| $E^2_{2g}$ (shear) – Unstressed | 26 | 34.9 | 32.3 | 33.6 | 32.0 | 31.8 |
| $2E_{2g}$ (CDW) – Unstressed | 51 | 42.4 | 42.2 | 39.1 | 38.1 | 36.1 |
| $1A_{1g}$ (CDW) – Unstressed | 79 | 80.4 | 80.0 | 76.3 | 75.3 | 75.1 |

*   **物理意义**：应力下 CDW 振幅模随温度软化更显著（42.8 cm⁻¹ @ 60 K），且在高温区消失（X），表明应力增强了电-声耦合与 CDW 不稳定性。
*   **来源**：[[../papers/chowdhuryReviewTheoreticalComputational]]

---

## 🧲 磁性与磁输运 (Magnetism & Magnetotransport)

### 1. 自旋极化紧束缚哈密顿量（交换场）
双层石墨烯/磁性衬底体系中，含层间交换场 $\mathbf{B}_\pm$ 的 2×2 自旋极化紧束缚哈密顿量：

$$ H_0(\mathbf{k}) = \begin{pmatrix} \boldsymbol{\sigma}\cdot\mathbf{B}_+/2 & -t\gamma_{\mathbf{k}} I \\ -t\gamma_{\mathbf{k}} I & \boldsymbol{\sigma}\cdot\mathbf{B}_-/2 \end{pmatrix} $$

*   **变量说明**：$\boldsymbol{\sigma}=(\sigma_x,\sigma_y,\sigma_z)$ 为泡利矩阵矢量，$\mathbf{B}_+/\mathbf{B}_-$ 为上下层的交换场，$t$ 为层间跃迁，$\gamma_{\mathbf{k}}$ 为层内形状因子，$I$ 为 2×2 单位矩阵。
*   **来源**：[[../papers/Makogon2012wave]]

### 2. 二维电子气 Landau 能级薛定谔方程
磁场中二维电子气在谐振子近似下的 Landau 能级方程，是量子霍尔振荡分析的出发点：

$$ \left[-\frac{\hbar^2}{2m}\frac{d^2}{dy^2} + \frac{1}{2}m\omega_i^2 (y-y_i)^2 + \text{const.}\right]\varphi_n(y) = E_n\varphi_n(y) $$

*   **变量说明**：$\omega_i=eB/m$ 为回旋频率，$y_i$ 为引导中心坐标，$E_n=\hbar\omega_i(n+1/2)$ 为 Landau 能级；该方程描述 Hall 电导量子化的单粒子基础。
*   **来源**：[[../papers/ivanovskiOscillationStructureHall1994]]

### 3. 溶质原子对马氏体相变温度的影响
每添加 1 at.% 溶质元素引起的磁性（$M$）与非磁性（$NM$）马氏体相变温度偏移 $\Delta T_i$：

| Element | $\Delta T_i^M$ (K / at.%) | $\Delta T_i^{NM}$ (K / at.%) |
| :--- | :--- | :--- |
| Si | 0 | −3 |
| Mn | −39.5 | −37.5 |
| Ni | −18 | −6 |
| Cu | −11.5 | −4.5 |
| Cr | −18 | −19 |

*   **物理意义**：Mn 与 Cr 强烈抑制相变温度，而 Si 对磁性相变几乎无影响；该数据用于设计形状记忆合金的相变温度。
*   **来源**：[[../papers/Zhang2003a]]

---

## 🔬 微结构/动力学：相稳定性、PDF、剥离能与键密度判据 (Microstructure & Kinetics)

### 1. 键密度判据（可剥离性）
高通量筛选可剥离晶面的键密度定义，即穿过给定晶面的化学键数除以面积：

$$ \rho = \frac{N(R_i,R_j)}{A} $$

*   **变量说明**：$N(R_i,R_j)$ 为穿过晶面、连接物种 $R_i$ 与 $R_j$ 的键数，$A$ 为晶面面积；键密度越低，层间结合越弱、越易剥离。
*   **来源**：[[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

### 2. 剥离能计算
通过对剥离过程中逐步断开层间键的增量能量求和，得到单位面积剥离能：

$$ \Delta E_j = \frac{1}{A}\sum_{j\ge i\ge 0}\left(E_{i,1} - E_{i,0}\right) $$

*   **变量说明**：$E_{i,1}$ 与 $E_{i,0}$ 分别为第 $i$ 层剥离前后的总能量；该式给出逐层剥离的累积能量代价。
*   **来源**：[[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

### 3. 相变动力学 Arrhenius 估算
基于 Arrhenius 方程估算结构相变的特征时间 $\tau$，用于判断超快/室温稳定性：

$$ \tau = \nu^{-1}\exp\left(\frac{\Delta E}{k_B T}\right) $$

*   **变量说明**：$\nu$ 为尝试频率（声子频率，约 10¹²–10¹³ s⁻¹），$\Delta E$ 为相变能垒，$k_B T$ 为热能；能垒低于 ~0.5 eV 时室温下相变可在纳秒内发生。
*   **来源**：[[../papers/zhongHighthroughputExfoliationMultiferroic2025]]

### 4. Ti 纳米颗粒熔化/冻结/堆积转变温度（单颗粒）
原子模拟中直径 2.76 nm（Ti₆₁₁）纳米颗粒的熔化、冻结及 HCP–BCC、BCC–HCP 转变温度：

| $D$ (nm) | $T_{Melting}$ (K) | $T_{Freezing}$ (K) | $T_{HCP\to BCC}$ (K) | $T_{BCC\to HCP}$ (K) |
|----------|-------------------|--------------------|-----------------------|-----------------------|
| 2.76 (Ti₆₁₁) | 880 | 787 | 650 | 342 |

*   **物理意义**：熔化-冻结滞后约 93 K，HCP→BCC 转变表现出显著过热，而 BCC→HCP 在远低于熔点处发生。
*   **来源**：[[../papers/Zhang2019b]]

### 5. Ti 纳米颗粒热转变温度的尺寸效应
直径 2.76–5.20 nm 范围内 Ti 纳米颗粒熔化、冻结及固-固转变温度随粒径的演化：

| $D$ (nm) | $T_{Melting}$ (K) | $T_{Freezing}$ (K) | $T_{HCP\to BCC}$ (K) | $T_{BCC\to HCP}$ (K) |
|----------|-------------------|--------------------|-----------------------|-----------------------|
| 2.76 (Ti₆₁₁) | 880 | 787 | 650 | 342 |
| 2.92 (Ti₇₆₃) | 900 | 777 | 700 | 450 |
| 3.20 (Ti₉₁₉) | 934 | 794 | 713 | 319 |
| 3.31 (Ti₁₁₁₁) | 963 | 780 | 669 | 404 |
| 3.56 (Ti₁₂₈₅) | 972 | 774 | 757 | 399 |
| 3.73 (Ti₁₅₅₅) | 985 | 787 | 731 | 317 |
| 3.99 (Ti₁₈₀₉) | 1007 | 796 | 769 | 402 |
| 4.21 (Ti₂₁₁₅) | 1020 | 813 | 748 | 326 |
| 4.34 (Ti₂₄₀₃) | 1028 | 802 | 760 | 443 |
| 4.65 (Ti₂₇₆₃) | 1041 | 806 | 813 | 364 |
| 4.81 (Ti₃₁₂₉) | 1047 | 796 | 775 | 348 |
| 5.01 (Ti₃₅₄₅) | 1056 | 796 | 810 | 342 |
| 5.20 (Ti₃₉₉₅) | 1064 | 826 | 778 | 350 |

*   **物理意义**：熔化温度随粒径单调升高并趋近块体值，而冻结温度与固-固转变温度呈现非单调涨落，反映堆积结构对尺寸的敏感性。
*   **来源**：[[../papers/Zhang2019b]]

### 6. 原子对分布函数
由 X 射线/中子散射结构因子 $S(Q)$ 傅里叶变换得到的约化对分布函数 $G(r)$：

$$ G(r) = 4\pi r[\rho(r)-\rho_0] = \frac{2}{\pi}\int_0^{Q_{\max}} Q[S(Q)-1]\sin(Qr)\,dQ $$

*   **变量说明**：$\rho(r)$ 为距离 $r$ 处的原子数密度，$\rho_0$ 为平均数密度，$Q$ 为散射矢量，$Q_{\max}$ 为测量上限；$G(r)$ 峰位给出原子壳层距离，是解析无序/嵌层结构的核心工具。
*   **来源**：[[../papers/petkovStructureIntercalatedCs2002]]

---

## 🛠️ 力学/杂项：TMD 弹性与键参数 (Mechanics of TMDs)

### 1. TMD 单层弹性模量与键参数
扶手椅（x）与锯齿（y）方向上单层 MX₂ 的杨氏模量 $E$、理想强度 $\sigma^*$、临界应变 $\varepsilon^*$，以及泊松比相关参数 $\phi$ 与电荷转移 $\Delta Q$：

| MX₂ | $E_x$ (GPa) | $\sigma^*_x$ (GPa) | $\varepsilon^*_x$ | $E_y$ (GPa) | $\sigma^*_y$ (GPa) | $\varepsilon^*_y$ | $\phi$ | $\Delta Q$ ($e$) |
|------|--------------|---------------------|--------------------|--------------|---------------------|--------------------|-----|------------------|
| MoS₂ | 222.75 | 27.35 | 0.28 | 219.46 | 16.90 | 0.19 | 1.62 | 0.92 |
| MoSe₂ | 178.78 | 22.68 | 0.29 | 175.97 | 12.86 | 0.16 | 1.76 | 0.73 |
| MoTe₂ | 125.94 | 17.12 | 0.32 | 123.54 | 7.88 | 0.14 | 2.17 | 0.37 |
| WS₂ | 244.18 | 29.96 | 0.28 | 240.99 | 19.91 | 0.18 | 1.50 | 1.07 |
| WSe₂ | 196.81 | 24.70 | 0.30 | 194.13 | 15.05 | 0.17 | 1.64 | 0.83 |
| WTe₂ | 137.32 | 18.71 | 0.32 | 135.27 | 9.30 | 0.15 | 2.01 | 0.44 |

*   **变量说明**：扶手椅方向的理想强度显著高于锯齿方向；$\Delta Q$ 为从金属到硫族原子的电荷转移，与弹性模量正相关。
*   **来源**：[[../papers/Li2013bonding]]
*   **另见**：同篇文献的 TMD 晶体结构、应力-应变曲线与键合电荷密度图收录于 [[heterostructures-stacking-mechanics-misc#🧲 力学参数、键合与相变图表 (Mechanical Parameters, Bonding & Phase Transitions)|异质结 - 力学性质与杂项]]。

### 2. TMD 弹性/强度线性拟合参数
杨氏模量 $E$ 与扶手椅、锯齿方向理想强度 $\sigma^*_{AR}$、$\sigma^*_{ZZ}$ 对键参数 $a$、$b$ 的线性拟合系数：

| Property | $a$ | $b$ |
|----------|--------|--------|
| $E$ | 171.97 | 61.34 |
| $\sigma^*_{AR}$ | 18.21 | 10.40 |
| $\sigma^*_{ZZ}$ | 16.86 | 1.60 |

*   **物理意义**：力学量可表示为键参数的线性组合 $P=a\cdot(\text{bond parameter})+b$，使 TMD 力学性能可由键几何快速预测。
*   **来源**：[[../papers/Li2013bonding]]

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/density-functional-theory|密度泛函理论 (DFT)]]、[[../concepts/paw-method|投影增强波法 (PAW/USPP)]]、[[../concepts/berry-phase|Berry 相与现代极化理论]]、[[../concepts/born-effective-charge|Born 有效电荷]]、[[../concepts/ferroelectricity|铁电性]]、[[../concepts/multiferroicity|多铁性]]、[[../concepts/charge-density-wave|电荷密度波 (CDW)]]、[[../concepts/flexoelectricity|挠曲电效应]]、[[../concepts/bond-density|键密度判据]]、[[../concepts/piezoelectricity|压电效应]]

**相关材料/实体**：[[../entities/h-BN|h-BN]]、[[../entities/graphene|石墨烯]]、[[../entities/TMDs|过渡金属二硫化物 (TMDs)]]、[[../entities/NbSe2|2H-NbSe₂]]、[[../entities/HZO|HfZrO (HZO)]]、[[../entities/GaAs|GaAs]]、[[../entities/HgI2|HgI₂]]
