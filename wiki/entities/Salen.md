---
tags: [entity]
---

# Salen (N,N′-双亚水杨基乙二胺)

Salen 是一类经典的席夫碱（Schiff base）配体，由两分子水杨醛与一分子乙二胺缩合而成。在科研 Wiki 中，Salen 实体主要关联于**导电共轭聚合物**及其在**光学湿度传感**中的应用。

## 核心属性 (Phase-Locked Properties)

在 [[../papers/Doroodmand2017conjugated]] 的研究语境下，Salen 表现出以下"相位锁定"的物理化学特性：

- **共轭锁定的分子导线 (Conjugated Molecular Wire)**：
  - 传统 Salen 单体不具导电性。通过电聚合（Electropolymerization），Salen 分子中的 C–C 单键转化为 C=C 双键，形成长程共轭结构。
  - **证据链**：XPS 谱图中 284.8 eV (C–C) 峰消失与 281.2 eV (C=C) 峰增强互为镜像，锁定其"分子导线"性质。
- **离子锁定的亲水性 (Ion-Locked Hydrophilicity)**：
  - Salen 对碱金属阳离子（如 K⁺, Na⁺, Li⁺）具有极高的结合容量（如 K⁺:Salen ≈ 5.3:1）。
  - 阳离子的掺杂直接锁定了聚合物薄膜的亲水能力，从而决定了感湿灵敏度。
- **体积-折射率锁定 (Volume-Refractive Index Locking)**：
  - 聚合物膜在吸水后发生体积膨胀，导致有效折射率（Refractive Index）发生偏移。
  - 这一物理变化锁定了其作为**水致变色反射滤光片 (Hydrochromic Reflective Filter)** 的光学响应，使得反射光颜色随湿度线性变化。

## 合成与形态

- **电聚合 (Electropolymerization)**：
  - 采用循环伏安法（CV）在玻碳电极上原位生成。
  - **关键参数**：pH > 13 (KOH 调节)，0.05 M KCl 辅助，电位窗口 −1.0 至 +2.25 V。
  - **形态控制**：膜厚约为 91±1 nm，表面光滑度随 CV 圈数（通常 10 圈）优化，这对于形成高清晰度的干涉/反射信号至关重要。

## 应用场景

- **高灵敏度光学湿度传感器**：
  - 利用其作为反射滤光片的特性，将湿度信号转换为可见光颜色变化。
  - **性能表现**：5–80% RH 范围内线性响应，LOD 为 0.17% RH，响应速度 (~9.5 s) 显著优于传统阻抗型传感器。

## 相关论文 (Two-Layer Architecture)

- [[../papers/Doroodmand2017conjugated]]：首次报道了无金属共轭 Salen 聚合物的电合成及其在湿度检测中的应用。

## 关联项

- **概念**：[[../concepts/hydrochromism]] (水致变色), [[../concepts/conjugated-polymer]] (共轭聚合物), [[../concepts/reflective-filter]] (反射滤光片)
- **材料**：[[glassy-carbon]] (玻碳)
