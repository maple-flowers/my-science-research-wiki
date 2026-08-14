---
project_id: P07
name: CDW电荷密度波
zotero_collection_key: WMIAAIAE
status: 论文图表规划阶段
local_path: E:\swan_goose\燕燕\香香\项目七：CDW电荷密度波\
---

# 项目七：CDW电荷密度波

> **物理路径**：`E:\swan_goose\燕燕\香香\项目七：CDW电荷密度波\`  
> **Zotero 文献池**：`科研项目文献池/项目七：CDW电荷密度波` (`WMIAAIAE`)

---

## 1. 项目简介与背景
电荷密度波（Charge Density Wave, CDW）是低维固体中电子-声子耦合导致的一种宏观量子相。本项目专注于过渡金属二硫属化物（TMDs）及其衍生体系中 CDW 态的形成机制、磁性/超导态耦合以及外场调控下的相变动力学。目前正处于 5-6 个主 Figure 的规划与论文初稿撰写阶段。

## 2. 与科研 Wiki 知识库的联系
- **相关物理概念**：[[../concepts/charge-density-wave|CDW 相变]]、[[../concepts/dirac-electrons|狄拉克电子]]、[[../concepts/marginal-fermi-liquid|边缘费米液体]]、[[../concepts/fermi-surface-nesting|费米面嵌套]]、[[../concepts/peierls-instability|派尔斯畸变]]
- **相关材料/实体**：[[../entities/TMDs|TMDs 相变材料]] (1T'-MoS2, CrS2, 2H-NbSe2, WTe2)
- **多场耦合**：[[../concepts/magnetoelectric-coupling|磁电耦合]]、[[../concepts/superconductivity|超导电性]]、[[../concepts/sliding-ferroelectricity|滑动铁电性 (与 CDW 共存)]]

---

## 3. 当前进展与文献综述 (Literature Review)

本项目的理论框架与图表逻辑深受以下 CDW 领域核心研究的启发：

### 3.1 TMDs 中磁性与 CDW 的微观耦合机制
针对 1T' 相中的磁性 CDW 态，本项目参考了 [[../papers/chenFerromagneticNonmagnetic1T2022]] 关于 FM-CDW 形成的双重机制：
- **机制区分**：文献提出了结构畸变指数 $d_1/d_2$ 作为判据。$CrX_2$ 与 $VTe_2$ 的 FM 态源于从直接交换到超交换的转变（键角接近 90°）；而 $MnX_2$ 的 FM 态则源于金属二聚化未完全湮灭磁矩。
- **机电驱动潜力**：文献预测 $CrS_2$ 在电荷注入下可诱导 NM-FM 可逆相变并产生高达 12.17% 的应变。这一巨大驱动效应是本项目 Figure 5 性能对比的核心对标点。

### 3.2 CDW 相中的准粒子激发与金属性起源
针对 2H 相中 CDW 与良金属性共存的矛盾，文献 [[../papers/CastroNeto2001charge]] 提供了统一的微观解释。
- **f 波序参量与狄拉克电子**：文献指出 CDW 序参量在费米面上具有六重节点（f 波态），其低能激发为无质量的**狄拉克电子**。这一图像解释了为何 CDW 相仍能保持金属性，并与 ARPES 测得的**边缘费米液体**行为定量吻合。
- **竞争相图**：文献阐明了 CDW 与超导态随晶格常数 $a/c$ 的反相关演化，为本项目规划压力/掺杂调控下的竞争相图提供了理论基础。

### 3.3 CDW 与滑动铁电性的关联
近年来的综述（如 [[../papers/sunSlidingFerroelectricityTwodimensional2025]]）指出，在 $WTe_2$ 和 $1T-TaS_2$ 等典型 CDW 材料中，层间滑移可诱导面外极化。
- **物理类比**：CDW 的畴壁运动、莫尔超晶格周期势与滑动铁电的翻转路径具有明确的物理类比。这提示我们在分析 1T' 相相变能垒时，应考虑层间滑移自由度对总能地形图的影响。

---

## 4. 知识积累与项目进展记录
- **2026-08-11**: 
    - **理论框架同步**：明确了 1T' FM-CDW 的“超交换”与“二聚化”双路径，参考了 [[../papers/chenFerromagneticNonmagnetic1T2022|Chen (2022)]] 的结构判据。
    - **低能激发描述**：引入了 [[../papers/CastroNeto2001charge|Neto (2001)]] 的狄拉克电子模型来解释计算中观察到的费米面残余节点。
- **论文图表现状**:
    - **Figure 1**: 已完成 1T vs 1T' 结构对比图，明确了 $d_1/d_2$ 畸变指数。
    - **Figure 2**: 正在绘制 $CrS_2$ 随电荷掺杂变化的 NM-FM 能量谷跃迁图。
    - **Figure 4**: 规划引入基于 [[../papers/chenFerromagneticNonmagnetic1T2022|Chen (2022)]] 数据的晶格常数滞后回线，展示电荷调控的非易失性。
