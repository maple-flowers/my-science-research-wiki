---
tags: [concept]
---

# 带宽调控型莫特转变 (Bandwidth-controlled Mott Transition)

## 核心定义
带宽调控型莫特转变（Bandwidth-controlled Mott Transition）是驱动莫特相变（Mott Transition）的核心路径之一。与通过改变电子间库仑排斥能 $U$ 的“相互作用调控”不同，该机制侧重于通过压窄单电子能带带宽 $W$ 来增大有效关联强度 $U/W$。当 $U/W$ 超过临界值时，半满带体系因电子间强排斥而发生能带分裂，形成绝缘态。在二维限域体系中，这一过程往往与晶格畸变（如电荷密度波 CDW）及维度效应紧密耦合。

## 维度效应与能带压窄
将材料减薄至单层极限是实现带宽调控的有效手段。在单层过渡金属二硫族化物（TMDs，如 1T-TaSe2）中，层间跃迁 $t_\perp$ 的消失直接导致了垂直方向动能的丧失，使总带宽 $W$ 显著减窄 [[../papers/nakataRobustChargedensityWave2021]]。同时，由于二维体系中介电屏蔽的极度减弱（在长波极限下 $\epsilon \to 1$），电子间的有效库仑能 $U$ 得到增强 [[../papers/liPhaseTransitions2D2021]]。这两者的协同作用将体系推向强关联区域。

## 晶格畸变驱动的带宽抑制
在 1T 相 TMDs 中，带宽调控往往由 $\sqrt{13} \times \sqrt{13}$ 的“大卫之星”（Star-of-David）电荷密度波（CDW）重构主导。在该结构中，13 个金属原子向中心收缩，其轨道重组形成极窄的中心带。由于 CDW 引起的晶格畸变会强烈重整并压窄电子能带，面内有效跃迁 $t_\parallel$ 被显著抑制，从而在费米面附近打开莫特-哈伯德能隙，分裂为下哈伯德带（LHB）与上哈伯德带（UHB） [[../papers/nakataRobustChargedensityWave2021]]。

## 锁相特性：晶格与关联的耦合
带宽调控的强度直接取决于晶格畸变的程度。通过对比同族的 1T-TaSe2 (5d) 与 1T-NbSe2 (4d)，可以解耦 $U$ 与 $W$ 的贡献：尽管 Ta 的本征库仑能 $U$ 小于 Nb（~2.0 eV vs ~2.8 eV），但由于 Ta 具有更强的金属-金属键合及更大的 CDW 晶格畸变能隙 $\Delta_{CDW}$，其最终观测到的莫特能隙 $\Delta_{Mott}$ 反而更大 [[../papers/nakataRobustChargedensityWave2021]]。这有力证明了在该类体系中，**由晶格畸变引起的带宽抑制（$W$ 的压窄）而非本征关联的差异（$U$ 的大小）是稳定高温莫特相的主导因素**。

此外，莫尔超晶格（Moiré Superlattices）如转角双层石墨烯，也是带宽调控的典型范式。通过精确调节层间扭转角，可以在费米能级附近产生“平带”（Flat Band），使电子动能带宽 $W$ 降至极小值，从而在较低的库仑作用下也能触发莫特绝缘态与超导相 [[../papers/liPhaseTransitions2D2021]]。

## 关联现象
- [[../concepts/charge-density-wave]]
- [[../concepts/mott-insulator]]
- [[../concepts/lower-hubbard-band]]
- [[../concepts/star-of-david]]
- [[../concepts/electron-correlation]]
