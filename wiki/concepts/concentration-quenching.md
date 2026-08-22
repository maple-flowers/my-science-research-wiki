---
tags: [concept, luminescence, energy-transfer, doping, mechanoluminescence, defect-mediated-luminescence, solid-state-lighting]
title: concentration-quenching
type: concept
status: developing
year: 2021
papers: [Gulhare2021mechanoluminescence, Xie2024isostructural]
updated: 2026-08-21
---

# concentration-quenching

**浓度猝灭（concentration quenching）** 指发光材料中掺杂的发光中心浓度超过某一临界值后，发光强度**反而下降**的现象。它决定了几乎所有掺杂型发光材料都存在一个**最优掺杂浓度**，而非「掺得越多越亮」。

## 👵 太奶导读

乖孙，做荧光粉的时候，会往一块「主体」材料里掺一点会发光的离子（比如 Eu³⁺），这些离子就是发光中心。

按直觉，掺得越多，发光引擎越多，应该越亮。**一开始确实是这样**，但掺到一定程度就掉头往下走了。

为什么？因为离子掺多了，彼此的距离就近了。一个离子被激发以后，本该自己把光发出来，但如果邻居就在旁边，这份能量会**先跳到邻居身上**，邻居再跳给下一个——像接力赛一样在离子之间传。传得越远，越有可能撞上晶体里的某个缺陷。缺陷是不发光的，它把能量变成热耗散掉了。于是这一份激发能白白浪费。

离子越密，接力链越长，撞上缺陷的概率越大，浪费得越多。这就是浓度猝灭。

记一句话：**浓度猝灭 = 离子挨太近 → 能量在离子间接力传递 → 传到缺陷处变成热。所以掺杂浓度存在一个甜点，过了就往下掉。**

## 🧩 物理机制 (Mechanism)

浓度猝灭不是「发光中心变差了」，而是**激发能在辐射跃迁之前被搬走了**，其链条为：

1. **掺杂浓度升高 → 相邻发光离子间距缩短。**
2. **非辐射共振能量传递开启**：激发能在同种离子间逐跳迁移（能量传递速率随离子间距缩短急剧上升）。
3. **能量迁移终点是猝灭中心**：晶体缺陷等非辐射通道把激发能耗散为热，不发光。
4. 结果：非辐射跃迁占比升高，发光效率下降。

因此发光强度对掺杂浓度的曲线呈**先升后降**：低浓度端受限于发光中心数量不足，高浓度端受限于能量迁移损耗，两者交点即最优浓度。

### 已知的最优浓度

| 体系 | 最优掺杂浓度 | 判据 | 性质 |
|---|---|---|---|
| Ba₃(VO₄)₂:Eu（γ 辐照） | **0.1 mol% Eu** | 力致发光峰值强度极大 | 实验 |

⚠️ **边界**：只此一条来源，且 0.1 mol% 是该主体—激活剂组合在力致发光判据下的最优值。最优浓度强烈依赖主体晶格（决定离子间距与缺陷密度）与激活剂种类，**不可外推**到其他体系。

## 📚 相关论文 (Related Papers)

- [[../papers/Gulhare2021mechanoluminescence]]：本页机制与数据的唯一实证来源。该文在 γ 辐照的 Ba₃(VO₄)₂:Eu 体系中测得力致发光强度随 Eu 浓度先升后降、在 0.1 mol% 处取极大，并明确把下降段归因于相邻 Eu³⁺ 间距缩短后激发能经非辐射共振传递「接力」至缺陷猝灭中心而耗散。
- [[../papers/Xie2024isostructural]]：⚠️ **本文并未研究浓度猝灭**。其掺杂浓度固定为 1%，浓度猝灭只出现在文末的待解问题清单中——作者自陈「不同浓度下持久力致发光的规律如何、是否存在浓度猝灭效应」尚待系统研究。此处保留该条目仅为记录「有机持久力致发光体系的浓度依赖仍是空白」这一现状，不构成本页机制的证据。

## 🔗 关联概念与实体 (Related)

- [[../concepts/energy-transfer|energy-transfer]]
- [[../concepts/mechanoluminescence|mechanoluminescence]]
- [[../concepts/defect-mediated-luminescence|defect-mediated-luminescence]]
- [[../concepts/charge-trapping|charge-trapping]]
- [[../concepts/radiation-induced-defects|radiation-induced-defects]]
- [[../concepts/solid-state-lighting|solid-state-lighting]]
- [[../concepts/gamma-irradiation|gamma-irradiation]]
- [[../entities/Ba3VO4-2|Ba3VO4-2]]
- [[../entities/europium-dopant|europium-dopant]]
