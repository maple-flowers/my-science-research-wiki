---
tags: [concept, magnetism]
title: 超交换 / Superexchange
type: concept
status: mature
year: 2024
domain: [magnetism, condensed-matter]
mechanism: 磁性离子通过中间非磁性阴离子（O²⁻）的电子云间接交换，Goodenough-Kanamori 规则依据轨道占据与键角决定交换符号
related_concepts: [exchange-interaction, antiferromagnetism, ferromagnetism, magnetism, dzyaloshinskii-moriya-interaction, spin-orbit-coupling]
papers: [caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025, chenFerromagneticNonmagnetic1T2022, fengFerroelectricityMultiferroicityTwodimensional2020]
updated: 2026-08-20
---

# superexchange

超交换（superexchange）指**磁性离子通过中间非磁性阴离子（如 O²⁻）的电子云间接交换相互作用**的机制，是绝缘氧化物、氟化物等化合物中磁性有序（反铁磁/铁磁）的主要来源，由 Kramers 与 Anderson 奠定、Goodenough-Kanamori 规则给出定性与定量判据。

## 👵 太奶导读

太奶啊，磁性离子之间隔着氧离子，直接"够不着"，但它们通过氧离子的电子"搭桥"传递磁性作用——就像两个人隔着墙握手，墙里有一根钢筋传递力气。这根"桥"怎么搭、力气怎么传，决定材料是"反平行排列"（反铁磁）还是"平行排列"（铁磁）。这套搭桥规则（Goodenough-Kanamori）能预测大多数含氧磁体的磁结构。

## 🏗️ 结构概览：三种交换通道的层级

超交换可以理解为"磁性离子–阴离子–磁性离子"三体问题，其交换符号由键合几何与轨道占据共同决定：

- **180° 键角（M–O–M 直线桥）**：两磁性离子 d 轨道与同一氧 p 轨道成键，半占据轨道强重叠 → 反铁磁（如 NiO、MnO 的岩盐结构）。
- **90° 键角（直角桥）**：磁性离子 d 轨道与氧的互相垂直 p 轨道耦合，轨道正交 → 铁磁（如 LaMnO₃ 面内某些路径、CuO 部分路径）。
- **Anderson 虚跃迁图像**：氧 p 电子先"借"给一侧磁性离子（形成中间激发态），再与另一侧自旋交换，净效果是能量二阶微扰产生的有效反铁磁/铁磁耦合。

Goodenough-Kanamori 规则正是总结上述轨道重叠几何（键角、轨道对称性）与交换符号之间对应关系的经验准则。

## 🧩 核心内容与机制 (Core Content)

- **机制**：磁性离子 d 轨道与中间阴离子 p 轨道杂化，产生有效交换（Anderson 超交换）；交换积分符号与大小决定磁序（本库氧化物磁性论文）。
- **Goodenough-Kanamori 规则**：90° 与 180° 键角、轨道占据对称性决定铁磁/反铁磁；半占据轨道重叠→反铁磁，正交轨道→铁磁（本库磁性氧化物论文）。
- **典型体系**：反铁磁岩盐/钙钛矿氧化物（如 NiO、LaMnO₃）、尖晶石铁氧体；超交换强度决定奈尔温度。
- **与 DMI 关系**：超交换基础上叠加自旋轨道（spin-orbit-coupling）产生 Dzyaloshinskii-Moriya 相互作用（DMI）与弱铁磁（helical-magnetism 相关）。
- **计算**：DFT+U 与交换参数提取（四态方法）定量评估超交换。

## 📊 物理参数表

| 参数/特征 | 180° 超交换 | 90° 超交换 |
|---|---|---|
| M–O–M 键角 | 约 180°（直线桥） | 约 90°（直角桥） |
| 轨道耦合 | 同一氧 p 轨道与两侧 d 轨道强重叠 | 互相垂直 p 轨道（正交） |
| 交换符号 | 半占据重叠→反铁磁（$J<0$） | 正交轨道→铁磁（$J>0$） |
| 典型材料 | NiO、MnO、LaFeO₃ | CuO 部分路径、LaMnO₃ 某些面内 |
| 微观图像 | Anderson 虚跃迁，泡利排斥 | 正交轨道避免泡利排斥 |
| 能量量级 | $J\sim 10^1$–$10^2$ K（奈尔温度量级） | 同左，取决于 d 轨道占据 |

## 🧭 近邻概念辨析

- **超交换 vs 直接交换（[[../concepts/exchange-interaction|exchange-interaction]]）**：直接交换靠磁性离子轨道直接重叠（无需中间阴离子）；超交换经阴离子电子云"搭桥"，是绝缘氧化物磁性主导机制。
- **超交换 vs 双交换（[[../concepts/double-exchange|double-exchange]]）**：双交换依赖巡游载流子（异价离子 Mn³⁺/Mn⁴⁺）的实跳跃，同时产生铁磁耦合与金属导电（CMR 机制）；超交换是局域自旋的虚跃迁，通常对应绝缘体。
- **超交换 vs RKKY**：RKKY 经巡游传导电子介质（稀磁金属、多层膜），随距离振荡；超交换经局域阴离子 p 电子，符号由键角几何决定。
- **超交换与弱铁磁**：超交换自身产生共线序；叠加自旋轨道耦合后出现反对称 DM 项（[[../concepts/dzyaloshinskii-moriya-interaction|DMI]]），使自旋倾斜产生弱铁磁（[[../concepts/weak-ferromagnetism|weak-ferromagnetism]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/chenFerromagneticNonmagnetic1T2022]]：把「直接交换 → 超交换的转变」明确列为 1T′ 铁磁 CDW 态的两种形成机制之一（CrX₂、VTe₂ 走此路径，MnX₂ 走金属-金属二聚化），并给出结构畸变指数 d₁/d₂ 作为区分两种机制的判据——本页「几何构型决定交换类型」的直接证据。
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]：给出超交换路径被结构相变调制的完整算例——ScCrP₂Se₆ 单层中铁电相磁基态为 AFM、反铁电相为 FM，机制归为相变引起的晶格畸变改变 Cr-Se-Se-Cr 间接交换路径，并预测约 0.82 V/Å 外场可实现 FM/AFM 电控切换。
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]：提供「晶格常数改变 → 交换作用改变」这条因果链的器件级例证（P(VDF-TrFE) 逆压电应变调控 Fe₃GaTe₂ 磁各向异性常数 K₁，0.5 aJ / 5 ns）；但该文以磁各向异性为落点，**未给出超交换积分的定量分析**，本页仅作机制类比引用。


## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/exchange-interaction|交换相互作用]]：超交换属于间接交换。
- [[../concepts/antiferromagnetism|反铁磁性]]：超交换的常见结果。
- [[../concepts/ferromagnetism|铁磁性]]：超交换也可产生铁磁序。
- [[../concepts/magnetism|磁性]]：超交换在磁学中的地位。
- [[../concepts/dzyaloshinskii-moriya-interaction|Dzyaloshinskii-Moriya 相互作用]]：超交换叠加 SOC 产生的反对称项。
- [[../concepts/spin-orbit-coupling|自旋轨道耦合]]：产生 DMI 与磁各向异性的来源。
