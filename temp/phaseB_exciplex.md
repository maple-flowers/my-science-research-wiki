---
tags: [concept, photophysics, excited-state]
title: 激基复合物 / Exciplex
type: concept
status: mature
domain: [photophysics, physical-chemistry, molecular-spectroscopy]
mechanism: 一个激发态分子与一个基态分子相互作用，形成激发态稳定、基态不稳定的二聚复合物
related_concepts: [photoluminescence, tict-mechanism, charge-transfer-exciplex, local-excited-state, pl-quenching]
papers: [Huang2023two, Huang2019solvatochromic, H2017fluorescence, WRZYSZCZYNSKI2010initiators, Xie2024isostructural]
updated: 2026-08
---

# 激基复合物 / Exciplex

激基复合物（exciplex，excited-state complex）指**一个处于激发态的分子（给体或受体）与另一个处于基态的分子在激发态寿命内结合形成的复合物**。它在激发态稳定、基态不稳定，因此基态吸收光谱中通常看不到对应物种。当两个分子相同时称为激基二聚体（excimer）；当二者不同、且伴随显著电荷转移时，称为电荷转移激基复合物（charge-transfer exciplex，CTE），是 [[../concepts/charge-transfer-exciplex|charge-transfer-exciplex]] 页的主题。Exciplex 发射通常表现为位于单体发射长波侧的无结构宽谱带，是双光子荧光探针、光聚合引发与有机发光材料中的重要中间态。

## 👵 太奶导读

太奶啊，这就好比两个人跳舞：一个人先"兴奋"起来（被光点亮），然后拉上旁边一个还没兴奋的人一起跳，两个人凑成一对"临时舞伴"。这对舞伴只在"兴奋"的时候才抱得紧，一旦兴奋劲儿过去（回到基态），就立刻散开。所以平时（基态）根本看不出这对舞伴存在，只有被光点亮的那一刻才出现。这对"临时舞伴"跳完舞会发出一种新的、偏红的光，跟单个人自己发光不一样。

## 🧩 与相近物种的区分

| 物种 | 组成 | 基态稳定性 | 光谱特征 | 与 exciplex 的区别 |
| :--- | :--- | :--- | :--- | :--- |
| **Exciplex** | 激发态分子 A\* + 基态分子 B | 不稳定 | 单体长波侧无结构宽带 | 本页主题 |
| **Excimer** | 激发态分子 A\* + 基态同分子 A | 不稳定 | 单体长波侧宽带 | 两分子相同，无电荷转移 |
| **基态电荷转移复合物** | 基态 A + 基态 B（CT 复合物） | 稳定 | 基态吸收出现新带 | 基态已存在，非激发态生成 |
| **TICT** | 单个分子内给体-受体扭转 | 基态稳定 | 极性依赖的长波弱带 | 分子内过程，非分子间复合物 |
| **碰撞猝灭** | A\* 与 Q 碰撞 | 不稳定 | 无新发射带，仅强度下降 | 不形成发光复合物，只耗散能量 |

关键判据：**exciplex 是分子间、激发态生成、基态不稳定的发光物种**。若基态吸收谱出现新带，说明是基态复合物而非 exciplex；若发射带随浓度增大而增强，支持分子间复合物；若仅强度下降而无新发射带，则是普通碰撞猝灭。

## 🔬 物理特征与光谱指纹

- **无结构宽发射带**：位于单体（LE）发射长波侧，因激发态复合物势能面平坦、振动结构被抹平。
- **浓度依赖**：分子间复合物形成概率随浓度增大而上升，发射带强度随之增强。
- **粘度依赖**：高粘度介质限制分子扩散，抑制分子间复合物形成，发射带减弱或消失。
- **溶剂极性依赖**：电荷转移型 exciplex 的发射峰随极性增大而红移（CT 态被极性稳定）。

## 🔬 双光子激发三重荧光与 542 nm E 带

本库探针 1a/P1（[[../papers/Huang2023two]]、[[../papers/Huang2019solvatochromic]]、[[../papers/H2017fluorescence]]）在双光子激发下呈现"三重荧光"：短波 B 带（LE 态）、长波 A 带（[[../concepts/tict-mechanism|TICT]] 态）以及约 542 nm 的 E 带。

**关于 542 nm E 带的归属，必须使用限定语**：

- 作者将 E 带**归属**为分子间激基复合物（exciplex）发射，这是**作者归属**而非已由超快动力学完全证明的结论；
- 支持证据是**浓度依赖**（E 带强度随浓度增大而增强）与**粘度依赖**（纯甘油高粘度下 E 带消失，中等粘度下出现），这些是稳态光谱层面的间接证据；
- 本库论文未提供时间分辨/超快动力学直接证据，因此不能把稳态光谱写成"已证明"。

## 🧩 应用场景

### 双光子三重荧光探针

1a/P1 探针的 E 带（约 542 nm）在中等粘度、双光子激发下出现，与 LE、TICT 带共同构成环境响应指纹，可用于同时报告极性、粘度与温度（[[../papers/Huang2023two]]、[[../papers/Huang2019solvatochromic]]、[[../papers/H2017fluorescence]]）。

### 双光子聚合共引发

[[../papers/WRZYSZCZYNSKI2010initiators]] 综述指出，双光子聚合引发剂体系中，激发态给体与共引发剂（如酮香豆素/胺）之间可形成电荷转移激基复合物，经电子转移与质子转移产生自由基引发聚合。典型二元体系为香豆素/酮香豆素 + HABI/DPI：激发态香豆素从共引发剂夺取电子（PET），DPI 接受电子后裂解产生芳基自由基。此场景中 exciplex 是**引发化学的中间态**，与荧光探针场景的"发光物种"角色不同。

### 持久机械发光（pML）

[[../papers/Xie2024isostructural]] 报道的同构掺杂有机体系中，电荷转移激基复合物（CTE）作为**能量转移平台**：主体与客体共混形成 CTE 态，其能级（如 BCPC&BCPB 中 S₂(¹CTE)=T₃(³CTE)=2.50 eV）介于主体本征 CT 态与客体本征 CT 态之间，能量经 CTE 级联转移至客体三重态（T₁(³LE_G)=2.25 eV），实现持久机械发光。此场景中 exciplex 是**能量中继站**，与探针场景的"直接发光体"角色不同。

## 📋 关键参数表

| 参数 | 数值 | 对象与条件 | 证据类型 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
| E 带峰位 | 约 542 nm | 1a/P1，双光子激发，中等粘度介质 | 实验（稳态发射，作者归属 exciplex） | [[../papers/Huang2023two]]、[[../papers/Huang2019solvatochromic]]、[[../papers/H2017fluorescence]] |
| E 带粘度行为 | 中等粘度出现、纯甘油消失 | 甘油-乙醇混合体系 | 实验（稳态发射） | [[../papers/Huang2023two]] |
| CTE 能级 | S₂(¹CTE)=T₃(³CTE)=2.50 eV | BCPC&BCPB 同构掺杂体系 | 计算（能级归属） | [[../papers/Xie2024isostructural]] |
| 客体三重态 | T₁(³LE_G)=2.25 eV | BCPC&BCPB 体系 | 计算 | [[../papers/Xie2024isostructural]] |
| pML 寿命 | 18.8–384.1 ms | 同构掺杂有机体系 | 实验（时间分辨） | [[../papers/Xie2024isostructural]] |
| 磷光量子产率 | 最高 11.9% | BCPC&BCPB 体系 | 实验 | [[../papers/Xie2024isostructural]] |

## 📚 相关论文 (Related Papers)

- [[../papers/Huang2023two]]：报道探针 1a 双光子激发下的三重荧光，将 542 nm E 带归属为分子间激基复合物，并给出浓度/粘度依赖证据。
- [[../papers/Huang2019solvatochromic]]：系统研究 P1/P2 探针的 LE/TICT/Exciplex 三带随极性、粘度与温度的变化，E 带在纯甘油中消失。
- [[../papers/H2017fluorescence]]：结合单/双光子激发与浓度依赖，支持 E 带的分子间激基复合物归属。
- [[../papers/WRZYSZCZYNSKI2010initiators]]：综述双光子聚合引发剂中电荷转移激基复合物作为共引发中间态的机理。
- [[../papers/Xie2024isostructural]]：报道电荷转移激基复合物作为能量转移平台实现持久机械发光。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-transfer-exciplex|电荷转移激基复合物]]：exciplex 的电荷转移子类，本页的一般概念与其不机械合并。
- [[../concepts/tict-mechanism|TICT 机制]]：分子内电荷转移态，与分子间 exciplex 常在同一探针中共存。
- [[../concepts/local-excited-state|局域激发态 (LE)]]：exciplex 发射的短波参照带。
- [[../concepts/pl-quenching|荧光猝灭]]：碰撞猝灭与 exciplex 形成是竞争/伴生关系。
- [[../concepts/photoluminescence|光致发光]]：exciplex 是光致发光的一种发射通道。
- [[../entities/dicyanostilbene-1a|二氰基二苯乙烯 (1a)]]：双光子三重荧光探针分子。
