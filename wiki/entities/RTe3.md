---
tags: [entity, material, charge-density-wave, 2D, phase-locked]
category: [D02, Z01]
---

# 稀土三碲化物 / Rare-earth Tritellurides (RTe₃)

**RTe₃**（$R = \text{La}$–$\text{Tm}$）是准二维电荷密度波（CDW）体系的典型模型材料。它具有层状 $NdTe_3$ 型结构（空间群 $Cmcm$），由双层 Te 方平面与 $R\text{Te}$ 间隔层交替堆叠而成。该体系是研究费米面嵌套、电子-声子耦合以及 CDW 亚稳态切换的核心平台 [[../papers/Laverock2005fermi]]。

## 1. 相位锁定物性 (Phase-Locked Properties)

在 $R\text{Te}_3$ 及其衍生体系（如 $EuTe_4$）中，电荷序参量的相位与宏观物性展现出显著的**相位锁定**特征：

### 1.1 嵌套矢量与费米面拓扑锁定 (FS Nesting Locking)
- **机制**：Te $5p$ 轨道构成的菱形费米面通过双层劈裂产生内外两层近乎平行的路径。
- **锁定效应**：CDW 的非公度波矢 $q \approx 2/7 a^*$ 被认为严格锁定于费米面的嵌套拓扑特征。[[../papers/Laverock2005fermi]] 通过 2D-ACAR 证实了“裸”费米面拓扑与实验 CDW 波矢的精确匹配。
- **争论**：[[../papers/Johannes2008fermi]] 认为这种锁定并非因果关系，主张动量依赖的电子-声子耦合才是真实驱动力。

### 1.2 层间相位切换锁定 (Interlayer Phase Locking)
- **机制**：在结构相似的 $EuTe_4$ 中，Te 单层与双层之间的 CDW 序存在相对相位自由度 $\phi$ [[../papers/lvUnconventionalHystereticTransition2022]]。
- **双稳态锁定**：层间耦合使相位被锁定在 $0$ 或 $\pi$ 两个近简并态。这种相位的迟滞切换导致了跨度超过 400 K 的巨热滞回现象，将微观相位构型锁定在宏观电阻率的亚稳分支上。

### 1.3 序参量振幅与输运锁定 (Amplitude-Transport Coupling)
- **锁定关系**：CDW 能隙（序参量振幅 $\Delta$）与电阻率 $\rho$ 及 X 射线衍射强度 $I_{CDW}$（$\propto \Delta^2$）高度关联。滞回过程中的电阻突变与能隙的各向异性演化同步，证明了电子态与电荷序的深度锁定 [[../papers/lvUnconventionalHystereticTransition2022]]。

## 2. 物理参数与特征

| 特性分类 | 物理表现 | 备注 |
| :--- | :--- | :--- |
| **结构对称性** | $Cmcm$ (No. 63) | 正交晶系，层状准二维 |
| **CDW 波矢** | $q \sim 0.28 a^*$ (非公度) | 沿 $a$ 或 $c$ 方向调制 |
| **各向异性** | $\rho_a/\rho_b \sim 5000$ (Sm系) | 极低的面外输运效率 |
| **屏蔽效应** | 弱介电屏蔽 ($\epsilon \to 1$) | 增强电声耦合，稳定 CDW |
| **亚稳态寿命** | $\tau > 3000$ min (Eu系) | 势垒 $> 1$ eV 的相位锁定态 |

## 3. 关联论文与路径 (Two-Layer Architecture)

- [[../papers/Laverock2005fermi]]：直接观测 RTe₃ 的“裸”费米面，证实嵌套矢量与电子结构的几何锁定。
- [[../papers/lvUnconventionalHystereticTransition2022]]：揭示 EuTe₄ 中层间相位切换驱动的巨滞回现象。
- [[../papers/Johannes2008fermi]]：批判性地讨论嵌套机制，强调电子-声子耦合的物理本源。
- [[../papers/liPhaseTransitions2D2021]]：综述二维材料相变工程，讨论 RTe₃ 在低维极限下的稳定性。
- **原始笔记**：详细实验数据参见 [[../papers/lvUnconventionalHystereticTransition2022]]。

## 4. 关联概念与实体
- [[../concepts/charge-density-wave|电荷密度波 CDW]]
- [[../concepts/fermi-surface-nesting|费米面嵌套 Nesting]]
- [[../concepts/interlayer-phase-coupling|层间相位耦合]]
- [[../entities/EuTe4|EuTe4]] (具有巨滞回的衍生体系)
- [[../projects/project-7-cdw-charge-density-wave|Project-7]] (CDW 研究专题)
