---
tags: [concept, piezoelectricity, mechanics]
title: 挠曲电效应 / Flexoelectric Effect
type: concept
status: developing
domain: [condensed-matter-physics, piezoelectricity]
mechanism: 应变梯度（不均匀形变）通过非中心对称或中心对称介质诱导电极化的现象
related_concepts: [polarization-switching, strain-engineering, ferroelectricity]
updated: 2026-08
papers: [Chen2016electrical, wuSlidingFerroelectricity2D2021a, yangRipplingFerroicPhase2021, heUltrafastSwitchingDynamics2024]
---

# 挠曲电效应 / Flexoelectric Effect
挠曲电效应（Flexoelectric Effect）是指任何固体介质在受到**不均匀形变（应变梯度, Strain Gradient）**作用时都会自发产生电极化，或者反过来，在外加不均匀电场作用下产生不均匀形变（逆挠曲电效应）的现象。与仅存在于非中心对称晶体中的压电效应（Piezoelectricity）不同，挠曲电效应在所有晶体对称性（包括中心对称介质）中均本征存在。
## 👵 太奶导读
太奶，这“挠曲电效应”的名字听着文绉绉的，其实您把它想象成一块**捏起来会起电的橡皮泥**。
以前我们讲“压电效应”，那得是特别名贵的石头（非中心对称晶体），你均匀地去压它（均匀应变），它才会出电。
但挠曲电效应就不挑剔了，哪怕是一块普通的泥巴，只要你把它**捏得一边厚、一边薄**，或者把它**弯折过来**（这就是应变梯度，**strain gradient**），因为这种“不均匀”的形变挤压，材料里的正负电荷就会被强行错开，从而自发地生出电信号来。
在做极小芯片的时候（比如纳米尺度的铁酸铋薄膜），科学家用一个极细的针尖戳一下（这能产生天大的应变梯度），就能用这个“捏”出来的内建电场，把材料里的极化状态完全翻转，省去了通电，神妙得很！
## 🏗️ 物理公式与数学模型
挠曲电极化 $P_i$ 的经典描述为：
$$P_i = \mu_{ijkl} \frac{\partial \varepsilon_{jk}}{\partial x_l}$$
其中：
*   $\mu_{ijkl}$ 是**挠曲电张量（Flexoelectric tensor）**，是一个四阶张量。
*   $\varepsilon_{jk}$ 是面内应变分量。
*   $\frac{\partial \varepsilon_{jk}}{\partial x_l}$ 是**应变梯度（Strain gradient）**，代表不均匀形变的剧烈程度。
由于应变梯度随着结构尺寸减薄至纳米尺度（如膜厚 $h \to 0$）而反比增大（$\frac{\partial \varepsilon}{\partial z} \sim \frac{\varepsilon}{h}$），在超薄膜、异质结或纳米针尖接触区，由局域应变梯度诱导的**挠曲电内建电场 $E_f$** 可高达 $10^6\ \text{V/cm}$ 量级：
$$E_f \approx \frac{\mu}{\varepsilon_0 \epsilon_r} \frac{\partial \varepsilon}{\partial z}$$
这一量级已足以匹敌或超越大多数铁电体的[[../concepts/coercive-field|矫顽场]] $E_c$，从而使我们能够纯粹利用机械力（如 PFM 针尖按压，$\sim 1\ \text{GPa}$ 局部压力）在厚达 70 nm 的 BiFeO₃ 薄膜中实现 $100\%$ 的非易失性铁电极化翻转。
## 📚 相关论文 (Related Papers)
- [[../papers/Chen2016electrical]]：首次在 70 nm 厚的 BiFeO₃ 薄膜中用针尖压力（～3325 nN）证实了由挠曲电场主导的完全极化翻转。
- [[../papers/wuSlidingFerroelectricity2D2021a]]：指出滑动铁电体的“ripplocation”畴壁处存在由于面外屈曲和极低层间剪切共同导致的强挠曲电耦合。
- [[../papers/yangRipplingFerroicPhase2021]]
- [[../papers/heUltrafastSwitchingDynamics2024]]
## 🔗 关联概念与实体 (Related Concepts & Entities)
- [[../concepts/polarization-switching|极化翻转]]
- [[../concepts/strain-engineering|应变工程]]
- [[../concepts/coercive-field|矫顽场]]
- [[../entities/BiFeO3|铁酸铋 (BiFeO₃)]]
