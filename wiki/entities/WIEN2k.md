---
tags: [entity]
---

# WIEN2k

WIEN2k 是一套基于**全势线性缀加平面波** (Full-Potential Linearized Augmented Plane-Wave, **FP-LAPW**) 方法的第一性原理计算程序包，被广泛视为固体电子结构计算的“金标准”或**全电子基准** (All-electron benchmark)。

## 核心特性与方法学

- **基组体系**：采用 LAPW + lo (local orbitals) 方案。在原子球 (Muffin-tin spheres) 内部使用原子轨道状的基函数，在球间隙区使用平面波，这种混合基组兼具原子轨道处理核心电子的高精度和平面波处理价电子的灵活性。
- **全势处理**：不对势函数进行形状近似（如球对称近似），能够精确描述晶格畸变、界面及低维体系中复杂的电荷分布。
- **计算 altitude**：由于其全电子、全势的本质，WIEN2k 常被用于校验赝势 (Pseudopotential) 或投影缀加波 (**PAW**) 方法的精度。

## 科研应用与 Wiki 案例

在本项目库涉及的研究中，WIEN2k 主要承担精密验证与响应函数计算的任务：

### 1. 光学性质基准校验
在 PAW 方法计算线性光学性质的发展中，WIEN2k 的 APW+LO 结果被用作检验 VASP 纵向/横向表达式精度的标准。
- **Wiki 记录**：[[../papers/gajdosLinearOpticalProperties2006]]
- **关键结论**：证明了 PAW 纵向表达式（含偶极矩修正）在标准势下即可达到 WIEN2k 的全电子精度。

### 2. 电荷密度波 (CDW) 不稳定性分析
利用 WIEN2k 进行超高 k 点密度的计算，以获取精确的电子极化率（磁化率）实部 $\chi'(q)$。
- **Wiki 记录**：[[../papers/Johannes2008fermi]]、[[../papers/Koley2020charge]]
- **技术要点**：在研究 NbSe₂、TaSe₂ 等材料时，需使用 ~15000–30000 k 点以确保极化率结构的收敛。Johannes 等人通过 WIEN2k 计算证明费米面嵌套并非这些金属 CDW 的主因。

### 3. 低能有效模型提炼 (Downfolding)
作为构建紧束缚模型或 Wannier 函数的原始电子结构输入。
- **Wiki 记录**：[[../papers/Barnett2006coexistence]]
- **应用案例**：在 2H-TaSe₂ 的子晶格解耦研究中，利用 WIEN2k (LDA) 提取瓦尼尔函数，发现其低能物理由次近邻跃迁 $t_2$ 主导。

### 4. 磁性与多铁性交叉验证
在二维多铁材料（如 NiI₂）的研究中，WIEN2k 用于交叉验证磁交换作用与 Berry 相极化计算。
- **Wiki 记录**：[[../papers/songEvidenceSinglelayerVan2022]]
- **数值对比**：在 NiI₂ 单层中，WIEN2k 算得的层间交换 $J_\perp \approx 2.8\text{ meV}$，与 VASP 的 $3.1\text{ meV}$ 高度吻合，增强了实验结论的理论可靠性。

## 相关论文 (References)

- [[../papers/gajdosLinearOpticalProperties2006]] — PAW vs APW+LO 光学性质对比
- [[../papers/Johannes2008fermi]] — CDW 机制与极化率计算
- [[../papers/Barnett2006coexistence]] — 2H-TaSe₂ 电子结构与子晶格解耦
- [[../papers/Koley2020charge]] — TaSe₂/TaSeS 竞争序的 DFT 输入
- [[../papers/songEvidenceSinglelayerVan2022]] — 二维多铁 NiI₂ 的理论验证
