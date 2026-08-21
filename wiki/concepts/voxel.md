---
tags: [concept, photophysics, nanofabrication]
title: 体素 / Voxel
type: concept
status: mature
domain: [two-photon-polymerization, microfabrication, nonlinear-optics]
mechanism: 双光子聚合中单次聚焦曝光实际发生聚合的最小三维体积单元，由双光子吸收的非线性（∝I²）与材料聚合阈值共同决定
related_concepts: [two-photon-polymerization, two-photon-absorption, photoinitiator, diffraction-limit, threshold-effect, aspect-ratio]
papers: [Gittard2013polymerization, Kumar2017microstructuring, WRZYSZCZYNSKI2010initiators]
updated: 2026-08
---

# 体素 / Voxel

体素（voxel，volume element）在双光子聚合（TPP/2PP）中指**单次聚焦曝光在光刻胶内实际发生聚合的最小三维体积单元**。它是双光子微纳加工的基本构建砖块——加工分辨率、线条宽度、三维结构精细度最终都由体素的横向尺寸（宽 D）与纵向尺寸（深 L）决定。体素之所以能远小于衍射极限对应的焦点光斑，源于两个物理机制叠加：双光子吸收的**光强平方（∝I²）非线性**把有效激发区压缩到焦点中心，材料**聚合阈值**又把固化区进一步裁剪到光斑峰值附近的一小段。

## 👵 太奶导读

太奶啊，想象用放大镜在太阳底下聚焦点火：火苗不是整片纸都烧着，只在最亮的那一个小点烧起来。双光子聚合里的"体素"就是"烧着的那一小点"——激光扫到哪，哪一小团树脂就固化，这一小团就是体素。它比光斑本身还小，因为要"双份光"才点得着（光强要够强），而最亮的地方只有正中心那一丁点；再加上树脂有"火候门槛"（阈值），不够强就固不了，于是实际固化的体积比光斑还小得多。所有微纳结构，就是一个一个这样的小点攒出来的，点越小，成品越精细。

## 🧩 体素的形成机制

### 非线性局域化：I² 依赖

双光子吸收（TPA）的能量吸收速率满足 $dW/dt = (8\pi^2\omega)/(c n^2)\, I^2 \,\mathrm{Im}[\chi^{(3)}]$，即**正比于光强平方**。高斯光束焦点处光强峰值最高，I² 曲线的半高全宽（FWHM）比线性强度分布窄约 $\sqrt{2}$ 倍，因此只有焦点核心区产生有效激发（[[../papers/Kumar2017microstructuring]]）。

### 阈值裁剪：突破衍射极限

光聚合存在**最小剂量阈值**：只有吸收能量超过阈值 $I_{th}^2\beta\tau f t \ge E_{th}$ 的区域才发生交联。阈值线在强度分布上"横切"出峰值附近一小段，使实际固化体素远小于光斑，特征尺寸可压缩至波长以下（[[../papers/Kumar2017microstructuring]]）。两者叠加，使体素具备超越光学[[../concepts/diffraction-limit|衍射极限]]的亚衍射分辨率。

### 体素的几何形态

体素在焦点中心呈近似**双锥形**（两端收窄的纺锤形）：横向宽度由径向高斯分布与阈值决定，纵向深度由轴向强度分布与瑞利长度决定。其宽深比（[[../concepts/aspect-ratio|深宽比]]）随工艺参数变化，影响三维结构的力学与形貌特性（[[../papers/Gittard2013polymerization]]）。

## 📐 体素尺寸的定量关系

体素宽 D 与深 L 可由高斯光束强度分布与阈值条件解析导出，关键依赖如下：

| 参数 | 增大时 D/L 变化 | 说明 |
| :--- | :--- | :--- |
| 平均功率 $P_{av}$ | 增大 | 峰值强度升高，超过阈值的区域变大 |
| 驻留时间 $t$ | 增大 | 累积能量增加；写入速度 v 增大等价于 t 缩短，线宽随之下降 |
| 重复频率 $f$ | 增大 | 单位时间脉冲数增多，累积剂量上升 |
| 数值孔径 NA | **减小** | 束腰 $w_0$ 与瑞利长度 $z_R$ 同时缩小，是提高分辨率的主要途径 |

理论预测小体素工艺窗口：功率略高于阈值、驻留时间 < 20 ms、平均功率约 1 mW、高 NA 物镜。实验上亚纳秒 532 nm 系统在 100×/NA=1.3 油浸物镜、1.0 mW、200 μm/s、10 kHz 条件下得到 FWHM ≈ 500 nm 的线条，与阈值模型预测一致（[[../papers/Kumar2017microstructuring]]）。

## 🧪 影响体素的实际因素

- **光学参数**：激光波长、聚焦光斑、能量、脉宽、脉冲频率、峰值强度；NA 越高，体素横纵向同时压缩。
- **扫描工艺**：扫描速度（⇔驻留时间）、光栅间距、层间距——共同决定体素排布与搭接，影响表面粗糙度与结构完整性。
- **材料与配方**：树脂折射率与光学性质、[[../concepts/photoinitiator|光引发剂]]类型与浓度、自由基淬灭剂。光引发剂种类与浓度直接改变体素尺寸；大双光子吸收截面（δ）的引发剂可在更低功率下达到聚合阈值（[[../papers/Gittard2013polymerization]]、[[../papers/WRZYSZCZYNSKI2010initiators]]）。

## 📋 关键参数表

| 参数 | 数值 | 对象与条件 | 证据类型 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| 分辨率下限 | 可达 30 nm | 双光子聚合通用报道值 | 综述引用 | [[../papers/Gittard2013polymerization]] |
| I² 曲线 FWHM 压缩 | 约 √2 倍 | 双光子 vs 单光子强度分布 | 理论 | [[../papers/Kumar2017microstructuring]] |
| 典型线宽 | FWHM ≈ 500 nm | 亚纳秒 532 nm，NA=1.3，1.0 mW，200 μm/s，10 kHz | 实验（AFM） | [[../papers/Kumar2017microstructuring]] |
| 3D 微柱高度 | 约 6 μm | SU-8，0.8 NA，1.2 mW，100 μm/s，10 kHz | 实验（光学显微镜） | [[../papers/Kumar2017microstructuring]] |
| 有效阈值能量密度 | $E'_{th} \approx 6.6\times10^{-73}$ W²/m⁴ | λ=532 nm，NA=0.8，f=10 kHz，P_av=1.2 mW | 实验拟合 | [[../papers/Kumar2017microstructuring]] |
| 双光子吸收截面 δ | 高效引发剂可达数百 GM | D-π-D / D-π-A 结构分子 | 综述 | [[../papers/WRZYSZCZYNSKI2010initiators]] |

## 📚 相关论文 (Related Papers)

- [[../papers/Gittard2013polymerization]]：综述性介绍 2PP 中体素的双锥形形态、分辨率影响因素（激光参数、光引发剂、淬灭剂）及 30 nm 超衍射极限分辨率。
- [[../papers/Kumar2017microstructuring]]：给出体素宽/深与功率、驻留时间、重复频率、NA 的解析关系与实验验证（500 nm 线宽、6 μm 微柱）。
- [[../papers/WRZYSZCZYNSKI2010initiators]]：从引发剂分子设计角度说明大 δ 与高引发效率如何决定低功率下的体素成形。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/two-photon-polymerization|双光子聚合（TPP/2PP）]]：体素所属的加工技术体系，体素是其最小单元。
- [[../concepts/two-photon-absorption|双光子吸收（TPA）]]：∝I² 非线性是体素亚衍射缩小的物理根源。
- [[../concepts/photoinitiator|光引发剂]]：其类型、浓度与双光子吸收截面直接决定体素尺寸。
- [[../concepts/diffraction-limit|衍射极限]]：体素通过非线性+阈值突破的经典光学极限。
- [[../concepts/threshold-effect|阈值效应]]：聚合阈值将固化区裁剪至焦点峰值附近，是突破衍射极限的关键。
- [[../concepts/two-photon-absorption-cross-section|双光子吸收截面]]：衡量引发剂双光子吸收能力，决定聚合阈值与体素成形。
- [[../concepts/aspect-ratio|深宽比]]：体素宽深比影响三维结构的形貌与完整性。
- [[../entities/SU-8|SU-8]]：常用负性光刻胶，本文中体素实验的宿主材料。
- [[../entities/thioxanthone-photoinitiator|噻吨酮光引发剂]]：与 SU-8/AR-N 4340 配伍的大 δ 引发剂。
- [[../entities/femtosecond-laser|飞秒激光]]：同时型双光子吸收所需的高光子密度光源。
