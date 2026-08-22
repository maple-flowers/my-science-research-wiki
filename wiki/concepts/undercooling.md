---
tags: [concept, phase-transformation, metallurgy, computational-materials]
title: 过冷度 / Undercooling
type: concept
status: mature
domain: [phase-transformation, nucleation-and-growth, computational-materials]
mechanism: 实际相变温度低于平衡转变温度的温度差，是相变（尤其形核）的驱动力来源
related_concepts: [nucleation-and-growth, grain-refinement, solid-state-phase-transformation, size-dependent-melting, undercooling-hysteresis]
papers: [Zhang2002b, Zhang2003a, Zhang2019b]
updated: 2026-08
---

# 过冷度 / Undercooling

过冷度（undercooling，常记作 $\Delta T$）指**系统实际发生相变（凝固或固态相变）的温度低于热力学平衡转变温度的温度差**：$\Delta T = T_\mathrm{eq} - T$。它直接决定相变的**热力学驱动力**与**形核率**：过冷度越大，驱动力越大、形核越密集，从而显著影响相变的形核-生长竞争与最终微观组织（如晶粒尺寸）。在连续冷却、纳米颗粒熔化-凝固等场景中，过冷度是连接冷却条件、尺寸效应与显微组织的核心中间变量。

## 👵 太奶导读

太奶，水到 0℃ 就结冰，但要是水特别干净、没有杂质"勾引"它，它可以冷到 -5℃ 还不结冰——这个"明明该结冰却没结冰、比该结冰温度还冷多少度"，就是过冷度。过冷得越厉害，冰晶的"种子"（形核）就越容易冒出来、冒得越多，最后冰碴子也越细。炼钢的时候控制冷却速度，其实就是控制过冷度：冷却越快，过冷越深，铁素体晶粒就越细、钢就越结实。给纳米小颗粒加热也一样，颗粒越小越难结晶，要冷很多才开始凝固，这也是一种过冷。

## 🔬 过冷度作为相变驱动力

过冷度直接给出相变的体积自由能驱动 $\Delta G_V \propto \Delta T$。形核率对过冷度呈强烈非线性依赖，经典表达式（本库论文所用形式）为：

$$I(T) = K_1 (kT)^{-1/2} D \exp\!\left[-\frac{K_2}{RT\,(\Delta G_{\gamma\to\alpha}^{N})^2}\right]$$

其中形核驱动力 $\Delta G_{\gamma\to\alpha}^{N} = \Delta G^S_{\gamma\to\alpha} - RT\ln a^S_\gamma$ 随过冷度增大而增大，使指数项迅速减小、形核率猛增。连续冷却下的新晶核密度由对过冷度的积分给出：

$$n = \int \frac{I}{Q}(1-f)\,d(\Delta T)$$

即**冷却速率 $Q$ 越小，系统停留在高过冷区的时间越长，累计形核数越多**。

## 🔬 案例一：Zhang 2002b — 连续冷却 γ→α 的自限制机制

[[../papers/Zhang2002b]] 建立耦合溶质/温度扩散场的二维元胞自动机（CA）模型，定量揭示低碳钢连续冷却相变中由过冷度主导的**扩散控制自限制机制**：

- 先形核的铁素体向邻近奥氏体**排出碳并释放潜热**，使邻区碳浓度升高（Ae3 下降）、温度升高，**局部过冷度 $\Delta T$ 减小**，后续形核概率下降——自然产生大小不均的晶粒分布；
- 冷速 0.05→5.0 K/s 时实验铁素体晶粒 106→33 μm、模拟 108→38 μm，**冷速越高过冷度越大、形核点激活越多，且溶质来不及扩散、渗碳体在生长前沿析出钉扎界面，故晶粒越细**。

## 🔬 案例二：Zhang 2003a — 形核-生长竞争决定晶粒

[[../papers/Zhang2003a]] 用二维六边形 CA 模型定量区分形核主导与生长主导的贡献：

- A36 钢（d_γ=18 μm）冷速 11/41/61 °C/s 时饱和形核数 n_nuc = 561/1352/1590；
- 高冷速下形核占比 $Y_\mathrm{nuc}$ 在 $\Delta T<95$ °C 区间剧烈振荡且数值更高，表明**早期形核主导而非生长主导**；
- 形核集中在过冷早期 zone I 完成，zone II 进入饱和——过冷度的时间演化（而非仅最终值）决定组织。

## 🔬 案例三：Zhang 2019b — 纳米颗粒的尺寸依赖过冷

[[../papers/Zhang2019b]] 用 EAM 势分子动力学揭示钛纳米颗粒的熔化-凝固滞后：

- 所有大颗粒凝固需大过冷度，如 Ti611（2.76 nm）Tm=880 K vs Tf=787 K，**过冷约 93 K**，源于液-固形核界面能势垒；
- 过冷度随粒径增大趋近块体值（Gibbs–Thomson：表面原子配位不足导致预熔）；
- HCP↔BCC 转变温度随粒径呈振荡变化，对表面形貌敏感——尺寸效应使过冷度成为纳米尺度相变的敏感调控参数。

## 🧮 过冷度与其他相变参数的关系

| 关系 | 表达式/含义 | 来源 |
| :--- | :--- | :--- |
| 形核驱动力 | $\Delta G \propto \Delta T$：过冷度提供体积自由能驱动 | [[../papers/Zhang2002b]]、[[../papers/Zhang2003a]] |
| 形核率 | $I(T) \propto \exp[-K_2/(RT\,\Delta G_N^2)]$：随过冷度急剧上升 | [[../papers/Zhang2003a]] |
| 晶粒细化 | 冷速 0.05→5.0 K/s ⇒ 晶粒 106→33 μm（实验） | [[../papers/Zhang2002b]] |
| 尺寸依赖 | 纳米颗粒凝固需大过冷（Ti611 约 93 K） | [[../papers/Zhang2019b]] |

## ⚠️ 使用注意

- **过冷度是过程量而非状态量**：其演化历史（冷却路径）决定形核累计与组织，建模时必须显式追踪温度场。
- **局部过冷度 ≠ 名义过冷度**：潜热释放与溶质富集会在界面附近改变局部过冷度，是自限制形核机制的关键。
- **尺寸效应**：纳米尺度下 Gibbs–Thomson 与界面能势垒使过冷度显著增大，块体经验值不可直接外推。

## 📚 相关论文 (Related Papers)

- [[../papers/Zhang2002b]]：耦合扩散场 CA 模型，过冷度驱动的自限制形核与冷速-晶粒关系。
- [[../papers/Zhang2003a]]：形核率/形核-生长竞争与过冷度演化的定量分析。
- [[../papers/Zhang2019b]]：钛纳米颗粒熔-凝滞后中尺寸依赖过冷度的 MD 证据。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/nucleation-and-growth|形核与长大]]：过冷度是其首要驱动力。
- [[../concepts/grain-refinement|晶粒细化]]：高过冷度→密形核→细晶的直接结果。
- [[../concepts/solid-state-phase-transformation|固态相变]]：过冷度控制的相变类别。
- [[../concepts/size-dependent-melting|尺寸依赖熔化]]：纳米尺度熔点与过冷度的 Gibbs–Thomson 关联。
- [[../concepts/undercooling-hysteresis|过冷与相变滞后]]：熔-凝滞后中的过冷现象。
- [[../concepts/cellular-automaton|元胞自动机]]：过冷度耦合扩散场建模的数值框架。
- [[../concepts/latent-heat|潜热]]：潜热释放改变局部过冷度的自限制机制。
- [[../entities/austenite|奥氏体]]、[[../entities/ferrite|铁素体]]：γ→α 相变的母相与产物。
- [[../entities/fe-c-phase-diagram|Fe-C 相图]]：平衡转变温度 Ae3 的来源。
- [[../entities/Ti-nanoparticle|钛纳米颗粒]]：尺寸依赖过冷研究的对象体系。
