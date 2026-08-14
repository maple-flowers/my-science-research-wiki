---
tags: [concept, non-linear-optics, solid-state-physics]
title: 法拉第效应 / Faraday Effect
type: concept
status: developing
domain: [solid-state-physics, optics, spintronics]
mechanism: 线偏振光在穿过处于磁场中的介质时，其偏振面发生旋转的磁光现象
related_concepts: [kerr-effect, optical-activity, magnetoelectric-coupling]
papers: [zhaoOpticalFingerprintsTwodimensional2024, gaoGiantChiralMagnetoelectric2024a]
updated: 2026-08
---

# 法拉第效应 / Faraday Effect

法拉第效应（Faraday Effect）是一种磁光效应。当线偏振光在介质中沿磁场方向传播时，由于左旋和右旋圆偏振光在磁场环境下的折射率不同（圆双折射），会导致出射光的偏振面相对于入射光发生旋转。

## 👵 太奶导读

太奶啊，这就好比一束光（线偏振光）是一根**“竖着的棍子”**。当这根棍子穿过一个被磁铁磁场笼罩着的材料时，里面的电子会在磁场的作用下**“绕着圈儿跑”**。这一跑，就会把穿过它的光棍子给慢慢地**“拧歪了”**。等这光从另一头出来的时候，它就不再是竖着的，而是斜着或者横着的了。这个旋转的角度大小，不仅跟磁场强度有关，还跟材料的脾气（费尔德常数）有关。

## 🏗️ 物理特征与定量描述

法拉第旋转角 $\theta$ 的大小遵循以下经验公式：
$$ \theta = V B L $$
其中：
*   $V$ 为**费尔德常数 (Verdet constant)**，反映材料的磁光活性强弱。
*   $B$ 为磁感应强度在传播方向上的分量。
*   $L$ 为光在介质中穿过的长度。

**关键特性**：法拉第效应是**不可逆的（Non-reciprocal）**。这意味着如果光被反射回起始点，旋转角会翻倍，而不是相互抵消。这一特性使其成为制造**光学隔离器 (Optical Isolator)** 和循环器的物理基础。

## 🧩 与克尔效应 (MOKE) 的区别

*   **法拉第效应**：发生在**透射光**中，通常探测体相材料的磁光性质。
*   **克尔效应**：发生在**反射光**中，对薄膜、表面及二维材料（如 [[../entities/VSe2|VSe2]]）的磁性极其敏感 [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]。

## 🔬 动态磁电耦合中的角色

在多铁性量子材料（如 [[../entities/NiI2|NiI2]]）的动力学研究中，法拉第效应（及其反射版克尔效应）被用于捕获电磁振子的振荡特征：
*   飞秒脉冲激发的磁化强度改变 ($\Delta M$) 会引起瞬时的磁光旋转，即时间分辨法拉第/克尔效应。
*   通过比较这种磁光旋转与电学响应（如 tr-SHG）的相位差，科学家成功证实了巨大的手性磁电耦合 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。

## 📚 相关论文 (Related Papers)

- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：利用时间分辨克尔旋转（类似于法拉第效应的反射形式）解耦探测手性磁电振荡中的磁信号。
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]

## 🔗 关联概念与 entities

- [[../concepts/kerr-effect|克尔效应]]
- [[../concepts/optical-activity|旋光性与光学活性]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../entities/NiI2|二碘化镍 (NiI2)]]
- [[../concepts/electromagnon|电磁振子]]
