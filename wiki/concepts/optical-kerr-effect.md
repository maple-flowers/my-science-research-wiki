---
tags: [concept, nonlinear-optics, solid-state-physics, magneto-optics]
title: 光学克尔效应 / Optical Kerr Effect
type: concept
status: mature
domain: [nonlinear-optics, solid-state-physics]
mechanism: 强光场通过三阶非线性极化使介质折射率瞬时改变，变化量正比于光强
related_concepts: [kerr-effect, second-harmonic-generation, nonlinear-optics, magneto-optical-kerr-effect, faraday-effect]
papers: [zhaoOpticalFingerprintsTwodimensional2024, gajdosLinearOpticalProperties2006]
updated: 2026-08
---

# 光学克尔效应 / Optical Kerr Effect

光学克尔效应（Optical Kerr Effect, OKE，也称交流克尔效应/ac-Kerr 或光致双折射）是[[../concepts/nonlinear-optics|非线性光学]]中的三阶 ($\chi^{(3)}$) 效应：当强光（如飞秒激光脉冲）通过介质时，光场自身诱导介质折射率发生**瞬时改变**，且变化量与光强成正比。它不同于[[../concepts/magneto-optical-kerr-effect|磁光克尔效应]]（磁性介质反射光的偏振旋转），也区别于静态电场下二次电光效应，是超快光学与飞秒光谱的核心机制之一。

## 👵 太奶导读

太奶啊，普通的光照过去，玻璃的“脾气”（折射率）是不变的。但如果光**特别亮**（像打雷一样猛的一道光），它会自己把玻璃的“脾气”给**临时改一下**——光越亮，改得越多。等这道光过去了，玻璃又恢复原样。咱们就利用这个“自己改自己”的特性，来做超快的“光学开关”，还能顺便测出材料对光的响应有多快。

## 🏗️ 物理机制

光学克尔效应的折射率变化为：

$$ n = n_0 + n_2 I $$

其中 $n_0$ 为线性折射率，$I$ 为光强，$n_2$ 为**非线性折射率系数**，与三阶极化率 $\chi^{(3)}$ 直接相关（$n_2 \propto \mathrm{Re}\,\chi^{(3)}$）。由此产生的现象包括：

*   **自聚焦 (Self-focusing)**：高斯光束中心光强高、折射率大，介质等效为会聚透镜，导致光束自聚焦乃至成丝。
*   **自相位调制 (SPM)**：脉冲自身相位被调制，频谱展宽，是超连续谱产生的基础。
*   **光学克尔开关/克尔透镜锁模**：利用瞬时折射率变化实现飞秒级光开关与锁模激光器。
*   **泵浦-探测瞬态双折射**：泵浦光改变探测光的偏振椭圆度/透过率，可时间分辨地追踪载流子、声子与自旋的非平衡弛豫。

## 🧩 与磁光/静态克尔效应的区分

| 类型 | 驱动源 | 响应 | 机制阶数 | 时间尺度 |
| --- | --- | --- | --- | --- |
| 光学克尔 (OKE) | 光场（强光） | $\Delta n \propto I$ | 三阶 $\chi^{(3)}$ | 瞬时（飞秒） |
| 磁光克尔 (MOKE) | 磁化强度 $\mathbf{M}$ | $\theta_K \propto M$ | 线性磁光 | 准静态 |
| 电光克尔 (二次) | 外电场 | $\Delta n \propto E^2$ | 三阶电光 | 准静态 |

## 🔬 在二维材料与磁光研究中的角色

*   在二维层间滑移多铁与磁性材料中，线性磁光响应（含[[../concepts/faraday-effect|法拉第效应]]与 MOKE）是读取磁序的标准探针 [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]；而 OKE 类瞬态非线性响应则可提供与之互补的超快动力学信息。
*   线性光学响应（介电函数、折射率）本身由[[../papers/gajdosLinearOpticalProperties2006|第一性原理线性光学计算]]给出，OKE 的非线性修正量 ($n_2$) 常在强场泵浦实验中被标定，两者结合可完整刻画材料的[[../concepts/optical-activity|光学响应]]。

## 📚 相关论文 (Related Papers)

- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：给出二维多铁材料线性磁光响应（克尔/法拉第）的第一性原理刻画，构成 OKE 研究的线性基线。
- [[../papers/gajdosLinearOpticalProperties2006]]：投影缀加波框架下线性光学性质的 DFT 方法，是计算光学响应（含非线性基线）的基础工具。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/kerr-effect|克尔效应]]
- [[../concepts/magneto-optical-kerr-effect|磁光克尔效应]]
- [[../concepts/second-harmonic-generation|二次谐波产生]]
- [[../concepts/nonlinear-optics|非线性光学]]
- [[../concepts/faraday-effect|法拉第效应]]
- [[../concepts/optical-activity|旋光性与光学活性]]
