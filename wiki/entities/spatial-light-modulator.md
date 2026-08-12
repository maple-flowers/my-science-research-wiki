---
tags: [entity]
---

# 纯相位液晶空间光调制器 (Spatial Light Modulator, SLM)

## 物理定义与原理
纯相位空间光调制器（Phase-only SLM）通常基于**液晶覆硅（LCoS）**技术，通过加载电压改变液晶分子的双折射率，从而在空间上对入射光波进行逐像素的相位延迟调制，而保持其振幅分布基本不变（即“纯相位”调制）。

## 核心特性：相位锁存与动态整形 (Phase-Locked Properties)
在激光微纳加工（如 [[../papers/Jia2023polymerization|2PP]]）系统中，SLM 的核心价值在于其动态、可编程的波前控制能力，其“相位锁存”特性体现在以下几个维度：

1.  **复相位相位锁定 (Phase Locking)**：通过数字化寻址，SLM 可以将设计的相位掩模（Mask）精确“锁存”在像素阵列上。在波前传感应用中，利用干涉原理（如多通道干涉）探测各子通道相对于参考通道的相位，当干涉强度达到最大时，探测通道与参考通道相位达到同步锁存状态（$\phi_i = \phi_r$）[[../papers/Jia2023polymerization]]。
2.  **调制深度与稳定性**：实验中常用的 **Holoeye PLUTO**（1920×1080 像素，8 μm 像元间距）支持在特定波长下实现 >2π 的稳定相位调制。
3.  **动态重构**：相比于 TPP 打印的静态微光学元件 [[../papers/Wang2023ultracompact]]，SLM 支持实时更新相位图（如闪耀光栅、CGH），用于动态补偿系统像差。

## 科研应用场景
1.  **自适应光学像差校正 (Adaptive Optics)**：
    *   在双光子聚合加工中，利用 SLM 将像素阵列划分为 M×N（如 20×20）子通道，通过原位探测重构系统波前，有效补偿超过 4π 的系统像差。这使得对相位极其敏感的高阶贝塞尔光束（m=6）能够恢复近理想形态，从而加工出高圆度、无倒塌的 SU-8 微管 [[../papers/Jia2023polymerization]]。
2.  **结构光场生成 (Structured Light)**：
    *   生成携带轨道角动量（OAM）的涡旋光束、贝塞尔光束及马蒂厄-高斯光束。
    *   作为毫米级衍射光学元件（DOE）设计的传统对标方案，尽管存在像素尺寸导致的离散化效应（Staircase effect）和体积瓶颈 [[../papers/Unknown2025diffractive]]。

## 典型参数示例 (Holoeye PLUTO)
*   **分辨率**：1920 × 1080
*   **像元间距**：8.0 μm
*   **填充因子**：约 93%
*   **相位增量**：通常采用 8-bit（256 阶）控制，如 $\pi/10$ 的扫描步长。

## Related Papers

*   [[../papers/Jia2023polymerization]] — 核心参考：基于 SLM 的多通道干涉波前传感与像差校正。
*   [[../papers/Wang2023ultracompact]] — 探讨 SLM 像素化瓶颈与 TPP 紧凑型相位板的对比。
*   [[../papers/Unknown2025diffractive]] — 毫米级 DOE 设计中 SLM 的传统应用背景。
