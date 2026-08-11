---
tags: [concept]
---

# 吸附能 (Adsorption Energy, E_ads)

### 定义与热力学基础
吸附能是表征吸附质与衬底表面结合强度的核心热力学指标，定义为体系各组分独立存在的能量之和与吸附后总能量的差值：
$E_{ads} = E_{slab} + E_{adsorbate} - E_{total(adsorbate/slab)}$
根据该定义，正值越大代表吸附过程释放的能量越多，形成的界面构型越稳定。在异质外延生长与电催化研究中，系统地扫描吸附位点以构建 **吸附能景观 (Adsorption Energy Landscape)** 是确定基态结构的前提。

### 结构演化与几何稳定性
在 Si(001) 表面 Ge 原子的初期吸附研究中，最终的稳定构型强烈依赖于初始吸附动力学参数。通过高通量扫描发现，Ge 原子倾向于吸附在 Si 二聚体上翘原子的外侧顶位 (Outside Top) 或二聚体桥位 (Bridge) [[../papers/Wu2018]]。对于 Ge 二聚体等复杂吸附质，吸附行为更加多样化，涉及垂直顶位 (DVTS)、平行桥位 (DPBS) 等 8 种稳定模式，且吸附过程常伴随 Ge-Ge 键的拉伸或完全断裂 [[../papers/Wu2021]]。

### 电子耦合与电荷转移
吸附能的量级反映了吸附质与衬底间的 **电子耦合 (Electronic Coupling)** 强度。基于 Mulliken 布居分析的计算显示，在 IV 族半导体异质吸附中，Ge 吸附原子总是表现为失去电荷，并将电子转移至衬底 Si 原子。这种电荷重新分布会显著改变衬底的 **表面重构 (Surface Reconstruction)** 状态：顶位吸附会加剧 Si 二聚体的不对称性，使其键长缩短、翘曲角增大；而桥位吸附则倾向于降低翘曲角，使二聚体趋于对称平衡。体系能隙的演化主要受这种吸附诱导的衬底结构扰动所支配 [[../papers/Wu2021]]。

### Phase-Locked 极化调控
在二维铁电金属等功能体系中，吸附能表现出明显的 **极化锁定 (Polarization-Locked)** 特征。自发极化产生的垂直电场打破了表面的反转对称性，导致 P+ 与 P- 表面具有显著的功函数差异。这种内部静电场能精确调控电催化中间体（如 O2, *OOH）的吸附强度，使其满足 **Sabatier 原理** 的最佳吸附窗口。例如，在少层 CuCrS2 中，铁电极化通过调节表面电荷密度，使 P+ 表面的 ORR 过电位降低至 0.28 V，展现出超越贵金属的催化活性 [[../papers/wangTwodimensionalFerroelectricMetal2025]]。

### 关联条目
- [[surface-reconstruction]]
- [[adsorption-energy-landscape]]
- [[charge-transfer]]
- [[ferroelectric-metal]]
