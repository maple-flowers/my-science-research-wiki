---
project_id: P03
name: 应力发光神经网络
zotero_collection_key: BCFMXHAU
status: 模型调优/主线科研
local_path: E:\swan_goose\燕燕\香香\项目三：应力发光神经网络\
---

# 项目三：应力发光神经网络

> **物理路径**：`E:\swan_goose\燕燕\香香\项目三：应力发光神经网络\`  
> **Zotero 文献池**：`科研项目文献池/项目三：应力发光神经网络` (`BCFMXHAU`)

---

## 1. 项目简介与背景
本项目致力于构建力学应力场与应力发光（Mechanoluminescence, ML）特性之间的神经网络预测模型。通过结合二维材料的压电力学响应与稀土掺杂体系的电子陷阱动力学，实现对应力分布的超灵敏光学传感与定量分析。目前主攻 36$\times$36 像素分辨率的力-光映射网络调优。

## 2. 与科研 Wiki 知识库的联系
- **相关材料/实体**：[[../entities/BiFeO3|SrAl2O4:Eu 铝酸锶]]、[[../entities/BiFeO3|Ba3VO4-2 钒酸钡]]
- **相关物理概念**：[[../concepts/mechanoluminescence|机械发光]]、[[../concepts/thermoluminescence|热释光]]、[[../concepts/molecular-beam-epitaxy|陷阱深度]]、[[../concepts/dislocation-mediated-ml|位错介导 ML]]
- **相关课题/主题**：[[../topics/材料模拟计算设计|材料模拟计算设计]]

## 3. 当前进展与文献综述 (Literature Review)

本项目的物理模型与特征工程基于以下核心研究构建：

### 3.1 动力学特征与波形建模
文献 [[../papers/KumarChoubey2011mechanoluminescence]] 在 $SrAl_2O_4:Eu$ 纳米粉体中观察到了典型的“双峰”ML 时间曲线。
- **物理机制**：双峰结构对应于冲击瞬时的直接激发与随后的位错介导延迟释放过程。本项目神经网络需复现该时域特征，利用卷积层提取上升沿与双峰间距。
- **力-光定量关系**：实验证实 ML 强度随载荷单调增长并在高速端饱和，这一物理先验被引入神经网络的损失函数约束中。

### 3.2 缺陷动力学与特征工程
机械发光依赖于受陷载流子的力学释放。
- **预处理与充能**：[[../papers/Gulhare2021mechanoluminescence]] 指出 $\gamma$ 辐照对 $Ba_3(VO_4)_2:Eu$ 的诱导作用，并发现发光强度在 1.4 kGy 处趋于饱和。
- **标准化协议**：参考 [[../papers/KumarChoubey2011mechanoluminescence]]，采用 365 nm 紫外光照射 15 min 作为数据采集前的标准化“充能/复位”协议，确保样本陷阱填充度一致。
- **隐藏变量注入**：通过热释光（TL）测定的陷阱深度（0.24–0.27 eV）被作为模型的隐含物理参数，用于修正长时间序列预测中的衰减偏置。

### 3.3 激发模式扩展
除直接压力外，[[../papers/Terasaki2011ultrasonic]] 验证了 37 kHz 超声波可非接触式激发 ML。
- **跨模态建模**：这提示模型不仅要处理准静态应力，还需具备处理高频机械波激励的能力。

## 4. 技术架构 (Technical Framework)

本项目构建的“应力-发光神经网络”遵循以下定量物理规律：

1.  **强度演化律**：参考 [[../papers/PChandra2011mechanoluminescence]] 提出的压电诱导电子脱陷模型，瞬时 ML 强度 $I$ 与压力变化率 $dP/dt$ 成正比：$I \propto (P - P_{th}) \cdot dP/dt$。
2.  **能量积分关系**：总形变区发光量 $I_{TD}$ 与应力平方成正比（$I_{TD} \propto P_m^2/2$），用于训练过程中的全局能量一致性校验。
3.  **时域衰减链**：发光衰减分为快过程（受机器常数 $\tau_m$ 控制）与慢过程（受陷阱载流子寿命 $\tau_s$ 控制），模型采用双分支 LSTM 架构分别捕捉这两个尺度的动力学。
4.  **特征空间映射**：结合 [[../papers/pengStrainEngineering2D2020]] 中的应变工程理论，将宏观应力张量映射至微观陷阱释放率特征层。

## 5. 知识积累与项目进展记录
- **2026-08-11**: 
    - 引入“位错介导释放”层到 CNN 架构中。
    - 参考 [[../papers/KumarChoubey2011mechanoluminescence]] 的双峰曲线，优化了时序预测分支的 ReLU 激活阈值。
    - 调整多输出分支结构（outputs2+2+2, outputs3），实现应力分布与总发光量的多任务协同学习。
