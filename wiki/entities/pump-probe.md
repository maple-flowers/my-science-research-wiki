---
tags: [entity, photophysics, ultrafast-spectroscopy]
title: 泵浦-探测技术 / Pump-Probe
type: entity
status: developing
domain: [ultrafast-spectroscopy, photophysics, carrier-dynamics]
mechanism: 使用强脉冲（泵浦光）激发样品，间隔一定延迟时间后用弱脉冲（探测光）记录样品的动态演化过程
related_concepts: [electromagnon, phase-difference]
papers: [gaoGiantChiralMagnetoelectric2024a, Yarai2005optical]
updated: 2026-08
entities: [ultrafast-spectroscopy]
---

# 泵浦-探测技术 / Pump-Probe

泵浦-探测技术（Pump-Probe）是超快光谱学中最基本且最核心的研究手段。它通过极短的激光脉冲，实现在极高的时间分辨率（通常为飞秒 $10^{-15}$ s 至皮秒 $10^{-12}$ s）下对物质激发态动力学过程的“慢动作”实时监测。

## 👵 太奶导读

太奶啊，这就好比是在**“拍电影”**，不过拍的是那种快得没影儿的武打动作。咱们先用一记“重锤”（强脉冲，叫泵浦光）把那个安静的分子给“打醒”或者是“推一下”，让它动起来。然后，咱们拿一个特别快、光极弱的照相机（弱脉冲，叫探测光），隔个万亿分之一秒拍一张照。咱们不停地调整拍照的时间点，最后把这一大堆照片连起来看，就能清清楚楚地看到这分子被推了之后是怎么晃悠、怎么慢慢停下来的全过程了。

## 🏗️ 实验构型

一个标准的 Pump-Probe 系统由以下几个部分组成：
1.  **分束器**：将超短脉冲激光分为强、弱两束。
2.  **光学延迟线 (Delay Stage)**：这是该技术实现时间分辨率的关键。通过机械移动镜子来改变探测光相对于泵浦光的光程差。根据光速，移动 1 $\mu$m 约对应 3.3 fs 的延迟。
3.  **激发与收集**：泵浦光激发样品，探测光穿过样品并由探测器记录（如吸收、反射、[[../concepts/second-harmonic-generation|SHG]] 或 [[../concepts/optical-kerr-effect|Kerr 旋转]] 的变化）。

## 🧩 动态物理量监测

泵浦-探测技术可以解耦探测多种不同的物理分量：
*   **电极化动力学 ($\Delta P$)**：通过时间分辨二次谐波产生 (tr-SHG) 监测。在范德华多铁材料 [[../entities/NiI2|NiI2]] 中，tr-SHG 成功捕获了电磁振子引起的电极化振荡 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。
*   **磁化动力学 ($\Delta M$)**：通过时间分辨磁光克尔旋转 (tr-RKerr) 监测。
*   **相位差分析**：通过同时运行两个探测通道，可以比较 $\Delta P$ 和 $\Delta M$ 的初始相位。在 NiI2 单畴中，观测到二者恒差 $\pi/2$，从而证实了巨手性磁电振荡的存在。

## 🔬 应用领域

*   **激子动力学**：监测半导体中激子的产生、复合与输运。
*   **相变演化**：实时记录光诱导相变（如超导、铁电翻转）的萌芽过程。
*   **集体激发**：研究磁振子、声子以及电磁振子的相干振荡。

## 🔬 应用范例：热透镜光纤湿度传感

泵浦-探测思想也延伸至传感领域：以 1.48 μm 泵浦光被水汽吸收产生热透镜效应，用 850 nm 超辐射发光二极管作为探测光感知折射率变化，通过锁相放大器提取信号，实现基于热透镜探测的光纤湿度传感器；该方法在低泵浦功率（<100 mW）与极短光吸收路径（<50 μm）下即可工作 [[../papers/Yarai2005optical]]。

## 📚 相关论文 (Related Papers)

- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：利用双通道 Pump-Probe 技术揭示了 NiI2 中的巨手性磁电耦合，实现了电、磁通道的动力学解耦。
- [[../papers/Yarai2005optical]]：基于热透镜检测技术的光纤湿度传感器。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../entities/ultrafast-spectroscopy|超快光谱学]]
- [[../concepts/second-harmonic-generation|二次谐波产生]]
- [[../concepts/electromagnon|电磁振子]]

## 🏷️ 专业名词别名

- `pump-probe-technique`（concepts）
