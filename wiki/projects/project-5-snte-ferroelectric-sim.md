---
project_id: P05
name: lammps势函数SnTe铁电模拟
zotero_collection_key: K9PXCWF9
status: 论文大纲阶段
local_path: E:\swan_goose\燕燕\香香\项目五：lammps势函数SnTe铁电模拟\
---

# 项目五：lammps势函数SnTe铁电模拟

> **物理路径**：`E:\swan_goose\燕燕\香香\项目五：lammps势函数SnTe铁电模拟\`  
> **Zotero 文献池**：`科研项目文献池/项目五：lammps势函数SnTe铁电模拟` (`K9PXCWF9`)

---

## 1. 项目简介与背景
本项目旨在通过第一性原理计算与机器学习势能（MLIP）方法，构建适用于 SnTe（碲化锡）及其二维体系的高精度 LAMMPS 势函数。重点研究 SnTe 在纳米尺度下的铁电极化动力学、相变行为及热物理性质。目前处于势函数评估与论文大纲规划阶段。

## 2. 与科研 Wiki 知识库的联系
- **相关材料/实体**：[[../entities/SnTe|SnTe 碲化锡]]、[[../entities/In2Se3|In2Se3 (同族参考)]]、[[../entities/TMDs|WTe2 (金属铁电参考)]]
- **相关物理概念**：[[../concepts/sliding-ferroelectricity|滑动铁电性]]、[[../concepts/polarization-switching|极化翻转动力学]]、[[../concepts/depolarization-field|退极化场]]、[[../concepts/berry-phase|Berry 相位]]、[[../entities/molecular-beam-epitaxy|机器学习势]]
- **计算工具**：LAMMPS, DeepMD-kit, Phonopy

---

## 3. 当前进展与文献综述 (Literature Review)

本项目的计算框架与物理模型深受以下二维铁电与多尺度模拟研究启发：

### 3.1 二维铁电性预测与计算方法学
SnTe 作为 IV-VI 族铁电半导体，其在二维极限下的稳定性与极化特性是项目的核心。文献 [[../papers/dingPredictionIntrinsicTwodimensional2017a]] 建立了二维范德华铁电体（如 In₂Se₃）的标准 DFT 计算流程。
- **方法迁移**：参考其使用 Berry 相位方法计算面内/面外极化，以及利用 CI-NEB 搜索极化反转最小能量路径（MEP）的方案，为 SnTe 的极化能垒计算提供了方法学基准。
- **退极化场评估**：文献中关于“短路电极模型”对抗退极化场的讨论，指导了本项目在模拟 SnTe 纳米薄膜时对表面补偿效应的建模。

### 3.2 滑动铁电机制与堆叠工程
虽然 SnTe 传统上被认为是位移型铁电体，但近年来的理论进展（如 [[../papers/sunSlidingFerroelectricityTwodimensional2025]]）指出层间滑移是二维材料中普遍存在的极化起源。
- **机制类比**：综述中详述的 3R 相堆叠工程与层间电荷转移图像，为理解 SnTe 不同堆叠构型（如 AA/AB/3R）下的铁电相稳定性提供了新视角。
- **跨层耦合**：文献提到的跨层滑动铁电性（ALSF）机制提示我们在构建 SnTe 多层膜势函数时，需超越近邻相互作用，考虑长程层间修正。

### 3.3 机器学习势能与居里温度预测
为了在 LAMMPS 中实现大规模 MD 模拟，势函数的准确性至关重要。文献 [[../papers/kaurRecentAdvancesTheoretical2025a]] 综述了利用深度学习势能（如 Allegro/DeepMD）预测铁电特性的进展。
- **Tc 关联修正**：文献指出应使用“孤立势垒 Δ”而非集体翻转势垒来关联居里温度（$T_c \approx 2\Delta/3k_B$），这一判据修正了本项目前期对 SnTe 相变温度的粗略估算。
- **应变调控模拟**：参考其关于倾斜电场和面内应变对矫顽场调控的模拟结果，本项目正在设计针对 SnTe 薄膜的应变-极化相图扫描任务。

### 3.4 铁电金属/半金属的实验对标
SnTe 的窄带隙特性使其极化屏蔽行为具有特殊性。文献 [[../papers/sharmaRoomtemperatureFerroelectricSemimetal2019]] 在 WTe₂ 中证实的“不完全屏蔽”机制为 SnTe 这种极性半导体中铁电性的存续提供了物理依据，其 PFM 成像与电滞回线表征数据可作为本项目实验校验的参考。

---

## 4. 知识积累与项目进展记录
- **2026-08-11**: 
    - 引入了基于 [[../papers/kaurRecentAdvancesTheoretical2025a|Kaur (2025)]] 的“极化登记指数 (PRI)”来量化层间滑移程度。
    - 在 LAMMPS 输入脚本中增加了对退极化场能量项的修正，参考了 [[../papers/dingPredictionIntrinsicTwodimensional2017a|Ding (2017)]] 的理论模型。
- **模拟计算现状**:
    - **数据生成**：已通过 VASP 完成了 SnTe 块体与单层的不同应变/极化构型的自洽计算。
    - **势函数训练**：正在利用 DeepMD-kit 进行第一轮主动学习采样，重点覆盖立方-菱方相变附近的势能面。
