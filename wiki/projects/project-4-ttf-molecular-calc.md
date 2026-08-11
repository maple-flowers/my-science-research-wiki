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
针对 TTF（四硫富瓦烯）分子体系进行的分子动力学与机器学习势能计算，涵盖 UFF 力场、LAMMPS 计算 TTF/TTF-MACE 以及训练 DeepMD 模型分析层间距与层间作用能。

## 2. 与科研 Wiki 知识库的联系
- **相关材料/实体**：[[../../entities/deep-potential|Deep Potential (DPMD)]]、有机分子晶体
- **相关物理概念**：[[../../concepts/machine-learning-potential|机器学习势]]、范德华层间相互作用
- **计算工具**：LAMMPS, MACE, DeepMD-kit

## 3. Zotero 参考文献池积累
- [[../../raw/note/Unknown2003charge|Charge transfer in BEDT-TTF/CuX2 salts]]：研究了 ET 与 CuX2 体系的电荷转移比例，指出当供体/金属比例 > 2 时，Cu(II) 可完全还原为 Cu(I)，从而减少库仑散射，提升材料导电性。
- [[../../raw/note/Wixtrom2011electrical|Mechanochemical synthesis of TTF-CA]]：记录了通过机械化学法合成 TTF-CA 的黑色多晶型（black polymorph），并分析了其在微纳器件中的接触电阻限制。
- [[../../raw/note/wangScreeningEnabledChemiresistiveMoisture2025|TTF-based MOFs for moisture sensing]]：揭示了水分子通过屏蔽 TTF•+ 自由基与补偿阴离子间的库仑相互作用（Screening effect）来减少电荷陷阱，从而显著提升 TTF 基导电 MOF 电导率的物理机制。

## 4. 知识积累与项目进展记录
### 文献调研与理论支撑
- **载流子调控规律**：明确了供体与受体（如金属盐）的化学计量比对最终氧化态的影响。在计算建模时，需考虑不同氧化态下 TTF 分子的几何畸变（极化子效应）。
- **湿度与介电环境影响**：文献 [[../../raw/note/wangScreeningEnabledChemiresistiveMoisture2025|Wang2025]] 提出的“去陷阱”机制为理解有机导体在环境湿度下的性能波动提供了理论框架。在 DeepMD 势函数开发中，应关注长程静电相互作用的描述。

### 模拟计算进展
- **UFF 力场扫描**：已完成 TTF 单体及其二聚体在不同位移下的单点能扫描，正在提取数据用于层间相互作用能曲线拟合。
- **LAMMPS/MACE 探索**：尝试利用 MACE 机器学习势进行 TTF 分子晶体的稳定性模拟，对比 UFF 在描述 π-π 堆叠力方面的差异。
- **DeepMD 训练**：准备开始构建包含不同电荷态的训练集，以捕捉电荷转移过程中的势能面变化。
