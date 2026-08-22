---
tags: [concept, superconductivity, superfluid-density, muon-spin-rotation]
title: uemura-relation
type: concept
status: developing
year: 2025
papers: [Islam2025enhancement, majumdarInterplayChargeDensity2020]
updated: 2026-08-21
---

# uemura-relation

**Uemura 关系（Uemura relation / Uemura plot）** 指非常规超导体中转变温度 T_c 与**超流密度** n_s/m\* 之间的近线性标度关系。它最初在欠掺杂铜氧化物中发现，其物理含义是：**T_c 不由配对强度决定，而由超流密度（或费米温度 T_F）决定**——这是玻色—爱因斯坦凝聚（BEC）一侧的图像，与 BCS 图像相反。

⚠️ 本库中两篇论文对同一类材料（层状 TMD）是否遵循该关系给出了**相反结论**，见下方对峙。

## 👵 太奶导读

乖孙，超导为什么会在某个温度出现？两种说法。

**BCS 的说法**：电子两两配成对，配对的「胶水」有多结实，决定了温度多高。所以关键是**配对强度**。按这套说法，T_c 跟「有多少电子参与超导」关系不大。

**Uemura 的说法**：不对。配对可能早就形成了，只是这些对子一开始各自为政、没有步调一致。真正决定 T_c 的是**这些对子什么时候开始齐步走**——而这取决于对子的密度（超流密度）。密度低，就得等到更低的温度才能齐步。

Uemura 把一大堆超导体画在一张图上（横轴超流密度、纵轴 T_c），发现铜氧化物、铁基这些非常规超导体**排成一条斜线**。这条斜线就是 Uemura 关系，落在线上通常被当作「这材料属于非常规超导、偏 BEC 一侧」的证据。

**太奶要你留个心眼**：一个数据点落在线上，不等于机理相同。本库里两篇论文测的都是层状 TMD 超导体，一篇说「落在线上」、另一篇说「明显偏离」——同一类材料给出相反答案。所以这条关系是**归类的线索，不是判决书**。

记一句话：**Uemura 关系 = T_c 随超流密度线性走；落在线上提示 T_c 由超流密度而非配对强度决定（BEC 一侧）；但落线与否本身不构成机理证明。**

## 🧩 关系内容与判读

- **坐标**：横轴为超流密度 n_s/m\*（实验上常取 λ_ab⁻²(0)，即伦敦穿透深度平方的倒数），纵轴为 T_c。
- **对照基准**：BCS 理论预期 T_c 与 n_s/m\* 关系很弱（图上近水平）；Uemura 关系是一条**正斜率直线**。
- **落在线上的解读**：T_c 由超流密度（或 T_F）而非配对强度决定，体系偏向 BEC 极限。
- **测量手段**：伦敦穿透深度的温度依赖（μSR、磁化率、比热等），同一套数据也常用来判断配对对称性（如排除 d 波）。

### ⚔️ 本库中的一处直接对峙

| 论文 | 体系 | 结论 | 附带判断 |
|---|---|---|---|
| [[../papers/Islam2025enhancement\|Islam2025]] | 多种层状 TMD | **遵循** Uemura 标度，斜率与最优掺杂铜氧化物、铁基超导体相近，强烈偏离 BCS 预期 | 据此把 TMD 纳入非常规超导版图 |
| [[../papers/majumdarInterplayChargeDensity2020\|majumdar2020]] | NbSe₂、NbS₂（含高压） | **显著偏离** Uemura 普适关系 | 认为二者自成一类，既非传统亦非典型非常规 |

⚠️ **这不是可以随手调和的分歧**，但有一条线索：Islam2025 自陈 TMD 的 **T_c/T_F 比值远小于铜氧化物**，即它们其实更靠近 BCS 一侧而非 BEC 一侧。也就是说「斜率相近」与「处于同一物理区间」是两回事——落在一条斜线上可能只反映标度形式相同，不保证机理相同。本库材料不足以裁决二者，此处仅并列记录。

## 📚 相关论文 (Related Papers)

- [[../papers/Islam2025enhancement]]：本页「遵循」一侧的来源。该文把多种层状 TMD 的 T_c 与 n_s/m\* 画在一起，发现数据点落在一条正斜率直线上、强烈偏离 BCS 预期，且斜率与最优掺杂铜氧化物及铁基超导体相近，据此把 TMD 纳入 Uemura 图景与非常规超导体版图。其可贵之处在于同时**自陈了这一推论的边界**——TMD 的 T_c/T_F 远小于铜氧化物，更接近 BCS 一侧，因此「落在线上」不等于处在 BEC 极限。
- [[../papers/majumdarInterplayChargeDensity2020]]：本页「偏离」一侧的来源。该文以磁光成像、比热、磁化率、电阻率与伦敦穿透深度的组合测量研究 NbSe₂ 与 NbS₂（含高压），发现两者都**显著偏离** Uemura 线性普适关系，认为它们属于既非传统也非典型非常规的独特类别；同一批数据还用于排除 d 波配对，并支持「费米面嵌套并非 CDW 主要成因」这一判断。

## 🔗 关联概念与实体 (Related)

- [[../concepts/superfluid-density|superfluid-density]]
- [[../concepts/superconductivity|superconductivity]]
- [[../concepts/london-penetration-depth|london-penetration-depth]]
- [[../concepts/bec-bcs-crossover|bec-bcs-crossover]]
- [[../concepts/charge-density-wave|charge-density-wave]]
- [[../concepts/fermi-surface-nesting|fermi-surface-nesting]]
- [[../entities/NbSe2|NbSe2]]
