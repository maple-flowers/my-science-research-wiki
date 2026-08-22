---
tags: [concept, density-functional-theory, exchange-correlation-functional, electron-correlation, dft-u, charge-localization]
title: self-interaction-error
type: concept
status: developing
year: 2004
papers: [zhouFirstprinciplesPredictionRedox2004, perdewGeneralizedGradientApproximation1996a]
updated: 2026-08-21
---

# self-interaction-error

**自相互作用误差（self-interaction error, SIE）** 指近似交换关联泛函（LDA/GGA）中，一个电子**与自身产生了虚假的静电排斥能**，且这份虚假能量未被交换项完全抵消。

它是 LDA/GGA 最重要的系统性缺陷之一，直接后果是**低估电子局域化倾向**——被诊断出 SIE 的场合几乎都要靠 [[../concepts/DFT-U|DFT+U]]、杂化泛函一类手段补救。

## 👵 太奶导读

乖孙，密度泛函理论算能量时有个先天的毛病。

它的做法是：先把所有电子摊成一片「电子云」，然后算这片云自己跟自己的静电排斥能。可问题是——**你算的这个电子，它自己也在这片云里**。于是它跟自己也排斥了一次。这一份排斥能是凭空多出来的，物理上不存在。

严格的理论里，交换项本该把这份虚假能量精确抵消掉。但 LDA/GGA 只是近似，抵消得**不干净**，剩下的残差就是自相互作用误差。

**这个残差偏向哪一边？** 关键在于：虚假的自排斥会**惩罚电子挤在一起**。电子越是缩成一团（局域），自排斥越大，能量被抬得越高。所以 LDA/GGA 会觉得「电子散开一点更划算」，于是它**系统性地偏爱离域态、低估局域化**。

**什么时候会捅出大篓子？** 当一个反应里，电子要从「离域的地方」搬到「局域的地方」——两边的虚假自能大小不同，抵消不掉，能量差就整体偏了。锂离子电池就是教科书案例：电子从金属锂（离域）转到过渡金属离子的 d 轨道（局域），GGA 算出来的电压比实验**整体低 0.5–1.0 V**。这不是随机误差，是有方向的系统偏差。

记一句话：**SIE = 电子跟自己虚假地排斥了一次；它惩罚局域化，所以 LDA/GGA 偏爱离域态；凡涉及「离域→局域」的电子转移，误差就系统性地跑偏。**

## 🧩 后果与诊断

- **偏向性**：SIE 抬高局域态能量 → 低估电子局域化 → 在电荷局域化程度高的体系（过渡金属氧化物、含 d/f 电子的强关联体系）中失效。
- **典型症状**：带隙低估、局域磁矩偏小、电荷有序/极化子态描述失败、**涉及离域↔局域电子转移的反应能整体偏移**。
- **误差不对称是关键**：SIE 本身在孤立体系里也存在，但只要反应两侧的自相互作用**大小相当**，误差会大致抵消。真正致命的是**两侧不对称**的情形。
- **修正手段**：DFT+U 通过类 Hubbard 项显式处理局域 d/f 电子的库仑关联，把被 SIE 压低的局域化倾向补回来。

### 一个定量的诊断案例

| 量 | GGA | GGA+U（自洽 U） | 性质 |
|---|---|---|---|
| 锂嵌入电压相对实验的偏差 | **系统性低估 0.5–1.0 V** | 降至百分之几量级 | 计算 vs 实验 |
| LiFePO₄ 平均电压 | 2.97 V | — | 计算 |
| LiFePO₄ 实验值 | 3.5 V | — | 实验 |

⚠️ **边界**：该案例只证明在「金属锂 → 过渡金属氧化物」这类离域—局域转移中 SIE 是主导误差源，且自洽 DFT+U 能有效修正。它**不**说明 DFT+U 能普遍修正 SIE，也不说明所有 GGA 电压误差都源于 SIE。

## 📚 相关论文 (Related Papers)

- [[../papers/zhouFirstprinciplesPredictionRedox2004]]：本页机制表述与定量数据的主要来源。该文把 LDA/GGA 低估锂嵌入电压 0.5–1.0 V 这一系统性偏差**明确归因于 SIE 的不对称抵消**——电子在金属锂中的离域态与在过渡金属离子上的局域态所受自相互作用未能相互抵消——并用自洽 DFT+U（线性响应法算 U，取局域 d 轨道电荷的裸响应与屏蔽响应之差）把误差压到百分之几；其贡献不仅是修正手段，更是给出了「SIE 何时致命」这一判据：**误差来自两侧不对称，不是来自 SIE 本身存在**。
- [[../papers/perdewGeneralizedGradientApproximation1996a]]：作为 PBE 泛函的原始文献，其价值在于**自陈局限**——PBE 仍无法完全消除电子与自身相互作用的虚假能量，因此在处理电荷局域化程度高的体系（如过渡金属氧化物）时失败。这一条把 SIE 定位为 GGA 层级泛函的**结构性缺陷**，而非某个具体泛函的实现瑕疵，说明升级到 PBE 并不能绕开它。

## 🔗 关联概念与实体 (Related)

- [[../concepts/exchange-correlation-functional|exchange-correlation-functional]]
- [[../concepts/PBE-functional|PBE-functional]]
- [[../concepts/gga-functional|gga-functional]]
- [[../concepts/DFT-U|DFT-U]]
- [[../concepts/hubbard-u|hubbard-u]]
- [[../concepts/electron-correlation|electron-correlation]]
- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/mott-insulator|mott-insulator]]
