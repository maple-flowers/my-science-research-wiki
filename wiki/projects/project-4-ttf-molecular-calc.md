---
project_id: P04
name: lsl老师的ttf分子计算
zotero_collection_key: ZQUX2PP6
status: 模拟计算中/老师外包课题
local_path: E:\swan_goose\燕燕\香香\项目四：lsl老师的ttf分子计算\
---

# 项目四：lsl老师的ttf分子计算

> **物理路径**：`E:\swan_goose\燕燕\香香\项目四：lsl老师的ttf分子计算\`  
> **Zotero 文献池**：`科研项目文献池/项目四：lsl老师的ttf分子计算` (`ZQUX2PP6`)

---

## 1. 项目简介与背景
针对 TTF（四硫富瓦烯）分子体系进行的分子动力学与机器学习势能计算，涵盖 UFF 力场、LAMMPS 计算 TTF/TTF-MACE 以及训练 DeepMD 模型分析层间距与层间作用能。项目核心在于通过理论模拟精确描述 TTF 分子在不同电荷态下的构型演化及其在 π-π 堆叠柱中的长程相互作用。

## 2. 与科研 Wiki 知识库的联系
- **相关材料/实体**：[[../entities/TTF|TTF 四硫富瓦烯]]、[[../concepts/molecular-beam-epitaxy|PMMA (作为基质)]]
- **相关物理概念**：[[../concepts/molecular-beam-epitaxy|机器学习势]]、[[../concepts/charge-transfer|电荷转移 (CT)]]、[[../concepts/nonlinear-absorption|非线性吸收]]、[[../concepts/molecular-beam-epitaxy|饱和吸收]]、[[../concepts/excited-state-lifetime|激发态寿命]]
- **计算工具**：LAMMPS, MACE, DeepMD-kit, VASP

---

## 3. 当前进展与文献综述 (Literature Review)

本项目的模拟建模与势函数开发参考了以下关于 TTF 聚集体动力学与输运机制的核心研究：

### 3.1 TTF⁺ 聚集体超快动力学与电荷转移
TTF 分子具有丰富的氧化还原特性。文献 [[../papers/Scremin2018nonlinear]] 通过飞秒 Z 扫描技术研究了 TTF⁺ 自由基阳离子及其电荷转移（CT）聚集体。
- **实验锚点**：确立了 TTF⁺ 二聚体在 ~800 nm (1.55 eV) 的 CT 跃迁特征，吸收截面约为 1.10 × 10⁻¹⁸ cm²/dimer。
- **超快动力学**：测得激发态寿命为百飞秒量级（~100–200 fs）。这一数据揭示了在超快脉冲下稳态速率方程失效的边界条件，为本项目评价机器学习势在描述非辐射衰减路径时的准确性提供了关键的实验对标。
- **电荷态演化**：讨论了歧化平衡（2TTF⁺ ⇌ TTF⁰ + TTF²⁺）对光学性质的影响。这提示在构建 DeepMD 训练集时，必须涵盖 TTF⁰、TTF⁺、TTF²⁺ 三种氧化态及其混合价态堆积。

### 3.2 π-堆积体系中的电荷传输与环境屏蔽机制
在宏观器件中，TTF 分子通常以 π-堆积柱的形式存在。文献 [[../papers/wangScreeningEnabledChemiresistiveMoisture2025]] 揭示了 TTF 基导电体系中的电荷输运机制。
- **结构参数**：指出 c 轴 π-堆积方向上 S···S 距离（3.71–3.76 Å）对本征迁移率的决定性作用。这验证了本项目中利用机器学习势精确拟合层间距与作用能曲线的必要性。
- **物理图像**：提出的“水分子屏蔽电荷陷阱”模型强调了高介电常数介质对空穴-阴离子库仑对的调制（ε_H2O ≈ 80.2）。这提示在分子动力学模拟中，除了范德华力，还需重点考虑长程静电相互作用及环境极化效应。

### 3.3 多晶型与非平衡态合成
文献 [[../papers/Wixtrom2011electrical]] 报道了通过机械化学法合成的 TTF-CA 黑色新多晶型。
- **结构基准**：该多晶型属于三斜晶系（a=10.756 Å, b=11.057 Å, c=6.614 Å），为混合堆砌结构。这为本项目提供了除经典单斜多晶型外的另一套电子结构计算输入。
- **方法学启发**：机械化学合成在非平衡态下获得亚稳态相的能力，促使本项目关注 TTF 晶体在外部应力作用下的层间滑移与结构演化模拟。

---

## 4. 知识积累与项目进展记录

- **2026-08-11**: 
    - 完成了基于 [[../papers/Scremin2018nonlinear]] 的多电荷态训练集需求分析，重点对标 1.55 eV 的 CT 跃迁能量。
    - 引入了 S···S 短程排斥与 π-π 吸引的竞争项到势函数修正中，参考了 [[../papers/wangScreeningEnabledChemiresistiveMoisture2025]] 提供的 3.71–3.76 Å 结构数据。
    - 开始基于 [[../papers/Wixtrom2011electrical]] 解析的三斜晶型参数构建异构体能量对标模型。
- **技术框架 (Technical Framework)**:
    - **基准数据 (Benchmarks)**:
        - CT 跃迁能量: ~1.55 eV ([[../papers/Scremin2018nonlinear]])
        - 激发态寿命: 100–200 fs ([[../papers/Scremin2018nonlinear]])
        - π-π 堆叠 S···S 距离: 3.71–3.76 Å ([[../papers/wangScreeningEnabledChemiresistiveMoisture2025]])
    - **力场与模型**:
        - **UFF 扫描**: 提取 TTF 二聚体势能面。
        - **MACE/DeepMD**: 训练涵盖 TTF⁰、TTF⁺、TTF²⁺ 电荷态的通用机器学习势。
        - **环境模拟**: 考虑介电屏蔽效应 ([[../papers/wangScreeningEnabledChemiresistiveMoisture2025]])。
- **模拟计算现状**:
    - **UFF 力场扫描**：已完成 TTF 二聚体势能面扫描，提取的层间作用能数据正用于校验 MACE 模型。
    - **DeepMD 训练**：初步构建了包含中性与阳离子态的配置库，重点学习电荷诱导的键长收缩效应。
