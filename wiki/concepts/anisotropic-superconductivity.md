---
tags: [concept, superconductivity, 2D-materials, fermiology]
title: 各向异性超导 / Anisotropic Superconductivity
type: concept
status: mature
domain: [superconductivity, condensed-matter-physics]
mechanism: 超导序参量（能隙、临界场、临界电流）随晶格方向或动量方向变化，源于费米面各向异性与配对机制的动量依赖
related_concepts: [superconductivity, fermi-surface-nesting, flat-band, electron-phonon-coupling, multiband-superconductivity, two-gap-superconductivity]
papers: [zhengAnisotropicSuperconductivityTwodimensional2025]
updated: 2026-08
---

# 各向异性超导 / Anisotropic Superconductivity

各向异性超导（Anisotropic Superconductivity）指超导体的宏观性质——能隙、上临界场 $H_{c2}$、临界电流 $J_c$ 与穿透深度 $\lambda$——在晶格不同方向或费米面不同动量位置上表现出显著差异的现象。它与费米面的几何各向异性、多带结构及配对势的动量依赖密切相关，是判定非常规超导配对的重要线索之一。

## 👵 太奶导读

太奶啊，普通超导体像一只“圆鼓鼓的气球”，各方向都一般粗；而各向异性超导就像一只“拉长的气球”，顺着一个方向结实、另一方向就软一些。电流朝一个方向流很顺，换个方向就费劲。咱们量一量这种“方向上的差别”，就能反推出超导的“配对是怎么组织的”——这就是各向异性超导的价值。

## 🏗️ 物理特征与定量描述

各向异性体现在多个层面：

*   **能隙各向异性**：动量空间内的超导能隙 $\Delta(\mathbf{k})$ 不再为常数，可呈现角向调制甚至节点（沿特定方向能隙为零）。对于各向异性 $s$ 波，$\Delta(\mathbf{k})$ 在费米面上随角度起伏；对于 $d$ 波，则存在线节点。
*   **上临界场各向异性**：$H_{c2}$ 沿主轴与面内的比值不同，由有效质量张量与相干长度各向异性决定，$H_{c2} \propto 1/\xi^2$。
*   **临界电流与穿透深度各向异性**：$J_c$、$\lambda$ 对方向的依赖反映超流密度的张量特性。

## 🧩 kagome 金属有机框架中的各向异性

二维 kagome 点阵金属有机框架 Cu₃(CO)₆ 单层（P6/mmm 空间群，Cu 四配位）是近期理论预测的一个范例：[[../concepts/electron-phonon-coupling|电-声子耦合]]驱动的 BCS 型超导体，临界温度 $T_c = 16.5$ K。其超导呈现**单能隙、各向异性**特征——kagome 几何带来的[[../concepts/flat-band|平带]]与[[../concepts/fermi-surface-nesting|费米面嵌套]]使配对强度在动量空间分布不均匀，形成角向调制的能隙 [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]。

| 特征 | 数值/性质 | 意义 |
| --- | --- | --- |
| 晶格 | kagome 单层，P6/mmm | 几何阻挫与嵌套并存 |
| 机制 | 电-声子耦合 BCS | 常规配对基底 |
| 能隙结构 | 单能隙、各向异性 | 非均匀配对强度 |
| 临界温度 | 16.5 K | 二维 MOF 中较高 Tc |

## 🔬 在二维超导研究中的角色

各向异性测量（角度分辨磁输运、方向分辨微波表面阻抗）是区分常规 $s$ 波与非常规（节点/多带/配对对称性破缺）超导的关键判据，与[[../concepts/superconductivity|超导]]的[[../concepts/multiband-superconductivity|多带]]及[[../concepts/two-gap-superconductivity|双能隙]]图像相互印证。

## 📚 相关论文 (Related Papers)

- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]：第一性原理预言 kagome MOF Cu₃(CO)₆ 单层为 Tc=16.5 K 的各向异性单能隙 BCS 超导体。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]
- [[../concepts/fermi-surface-nesting|费米面嵌套]]
- [[../concepts/flat-band|平带]]
- [[../concepts/electron-phonon-coupling|电-声子耦合]]
- [[../concepts/multiband-superconductivity|多带超导]]
- [[../concepts/two-gap-superconductivity|双能隙超导]]
- [[../entities/Cu3CO6|Cu₃(CO)₆ kagome 金属有机框架]]
