# 实验测试与测量装置 (Experimental Setups & Measurements)

> 收录二维铁电/多铁材料研究中的生长合成装置、PFM/AFM/CAFM 等探针显微表征平台、THz/XRD/TEM 等谱学与衍射手段，光学与光纤传感器，以及器件制备流程与器件架构相关的图表和关键公式。

[[科研Wiki/wiki/figures/_index|← 返回总索引]]

---

> **📂 子页面导航**：实验装置图像已按主题拆分为 5 个子页面，点击下表快速跳转：
>
> | 子页面 | 主题 | 条目数 |
> |--------|------|--------|
> | [[experimental-setups-growth-synthesis\|🧪 生长、合成与高通量筛选]] | CVD/MBE/ALD 生长、高通量筛选、材料制备方法 | 8 |
> | [[experimental-setups-probe-microscopy\|🔬 探针显微与局域表征]] | PFM/AFM/CAFM/STM/MFM 等纳米尺度成像 | 27 |
> | [[experimental-setups-optical-fiber\|💡 光学、光纤与化学传感]] | 光纤/光学传感器、湿度/生物/气体传感 | 35 |
> | [[experimental-setups-spectroscopy-diffraction\|📡 谱学、衍射与宏观表征]] | XRD/TEM/EPR/磁光等谱学衍射手段 | 42 |
> | [[experimental-setups-devices-architectures\|🔧 器件制备流程与架构]] | 器件工艺流程、存储器件架构与性能 | 18 |
>
> 物理公式（插层能、形成能、MAE、海森堡模型、挠曲电场等）仍收录于本页 [[#📐 物理公式与模型 (Formulas & Models)]] 一节。

[[科研Wiki/wiki/figures/experimental-setups|← 返回本页]]

---

## 📐 物理公式与模型 (Formulas & Models)

### 1. 插层能 (Intercalation Energy)
定义每个 A 原子嵌入 M₂X₄ 双层所对应的结合能，用于判断插层结构相对于分立反应物的热力学稳定性。

$$ E_{int} = \frac{E_{AM_2X_4} - E_{M_2X_4} - nE_A}{n} $$

*   **变量说明**：$E_{AM_2X_4}$、$E_{M_2X_4}$ 分别为插层化合物与裸 M₂X₄ 双层的总能量，$E_A$ 为孤立 A 原子能量，$n$ 为单胞中 A 原子数。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 2. 形成能 (Formation Energy)
以块体金属 A 为参考态计算形成能，负值表示插层化合物相对于块体反应物稳定。

$$ E_f = \frac{E_{AM_2X_4} - E_{M_2X_4} - nE_{A,\mathrm{bulk}}}{n} $$

*   **变量说明**：$E_{A,\mathrm{bulk}}$ 为块体 A 金属中每个原子的能量。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 3. 磁各向异性能 (MAE)
比较面内与面外磁化方向的总能量差，用于确定易磁化轴与垂直磁各向异性强度。

$$ \mathrm{MAE} = E_{\mathrm{in\text{-}plane}} - E_{\mathrm{out\text{-}of\text{-}plane}} $$

*   **变量说明**：MAE > 0 对应垂直（面外）易磁化，MAE < 0 对应面内易磁化。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 4. 海森堡磁耦合哈密顿量
包含各向同性交换 $J_{ij}$ 与单轴各向异性 $D$ 的自旋模型，用于蒙特卡洛模拟磁有序温度。

$$ H = -\sum_{i,j} J_{ij}\,\mathbf{S}_i \cdot \mathbf{S}_j - \sum_i D\,(\mathbf{S}_i^z)^2 $$

*   **变量说明**：$J_{ij}>0$ 为铁磁耦合，$D$ 为单轴各向异性参数，$\mathbf{S}_i$ 为格点 $i$ 的自旋矢量。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 5. 居里/奈尔温度估计
基于海森堡模型与蒙特卡洛模拟，由磁化率尖峰或比热反常确定 $k_B T_C$。

$$ k_B T_C \sim \text{MC 模拟中磁化率峰值对应的温度} $$

*   **变量说明**：$k_B$ 为玻尔兹曼常数，$T_C$ 为磁相变温度；实际值由 MC 模拟的有限尺寸标度给出。
*   **来源**：[[../papers/zhaoRealization2DMultiferroic2024]]

### 6. PFM 针尖下的挠曲电场
PFM 针尖在铁电薄膜中通过应变梯度诱导挠曲电场，是纳米尺度极化翻转的重要驱动力。

$$ E_f = \frac{f}{\varepsilon}\,\frac{\partial e}{\partial z} $$

*   **变量说明**：$f$ 为挠曲电系数，$\varepsilon$ 为介电常数，$\partial e/\partial z$ 为沿深度方向的应变梯度。
*   **来源**：[[../papers/Chen2016electrical]]

---


## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/multiferroicity|多铁性]]、[[../concepts/ferroelectricity|铁电性]]、[[../concepts/sliding-ferroelectricity|滑移铁电性]]、[[../concepts/moire-superlattice|莫尔超晶格]]、[[../concepts/magnetoelectric-coupling|磁电耦合]]、[[../concepts/density-functional-theory|密度泛函理论 (DFT)]]、[[../concepts/high-throughput-screening|高通量筛选]]、[[../concepts/flexoelectric-effect|挠曲电效应]]、[[../concepts/ferroelectric-photovoltaic-effect|铁电光伏效应]]、[[../concepts/antiferroelectricity|反铁电性]]

**相关材料/实体**：[[../entities/In2Se3|In₂Se₃]]、[[../entities/NiI2|NiI₂]]、[[../entities/BiFeO3|BiFeO₃]]、[[../entities/HZO|HZO (铪锆氧)]]、[[../entities/h-BN|h-BN]]、[[../entities/graphene|石墨烯]]、[[../entities/TMDs|TMDs]]、[[../entities/WTe2|WTe₂]]、[[../entities/Cr2S3|Cr₂S₃]]

