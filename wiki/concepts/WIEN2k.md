---
tags: [concept, density-functional-theory, electronic-structure]
---

# WIEN2k 与全势 LAPW 方法

WIEN2k 是基于**全势线性缀加平面波** (Full-Potential Linearized Augmented Plane-Wave, **FP-LAPW**) 方法的第一性原理计算核心程序，在凝聚态物理的电子结构计算中常被视为“全电子基准” (All-electron benchmark)。其物理机制的核心在于对空间势场处理的严谨性与基组选择的针对性。

### 物理机制与基组构造

FP-LAPW 方法将晶体空间划分为两个物理环境截然不同的区域：**原子球区域** (Muffin-tin spheres) 和**球间隙区域** (Interstitial region)。在原子球内，电子受到强烈的核吸引势，波函数剧烈震荡，因此采用原子轨道状的径向函数与球谐函数的乘积作为基函数；而在球间隙区，势场相对平缓，波函数则展开为平面波。

与传统的 Muffin-tin 近似不同，WIEN2k 采用“全势” (Full-potential) 处理，即不对势函数的形状做任何球对称化假设。这使得它能极其精确地描述电荷分布的各向异性，特别是在处理低维体系（如二维材料单层）、界面结构以及具有强轨道极化的电子能带时表现卓越。

### 在能带论与相变机制中的应用

在电子能带结构研究中，WIEN2k 常被用于探讨电荷不稳定性与结构相变的本质。例如，在研究过渡金属二硫属化物 (TMDs) 的**电荷密度波** (CDW) 机制时，计算精确的电子极化率实部 $\chi'(q)$ 至关重要。[[../papers/Johannes2008fermi]] 的研究通过 WIEN2k 的超高密度 $k$ 点采样证明，费米面嵌套 (Fermi surface nesting) 并非 NbSe₂ 等金属 CDW 的驱动力，而是电子-声子耦合展现的动量依赖性主导了相变。这一结论在后续对 TaSe₂ 的研究中得到了进一步验证 [[../papers/Koley2020charge]]。

### 方法学校验与光学性质

由于其不使用赝势 (Pseudopotential)，WIEN2k 经常作为校验其他近似方法精度的“标尺”。在投影缀加波 (**PAW**) 方法的精度验证中，[[../papers/gajdosLinearOpticalProperties2006]] 通过对比 WIEN2k 的 APW+lo 结果，系统性地评估了线性光学响应函数的纵向与横向表达式。此外，在针对低能物理过程的有效模型提取中，WIEN2k 算得的能带结构被用于构建高质量的瓦尼尔函数 (Wannier functions)，从而揭示了诸如 2H-TaSe₂ 中子晶格解耦的次近邻跃迁效应 [[../papers/Barnett2006coexistence]]。
