---
tags: [concept, magnetism, spintronics]
title: 自旋波 / Spin Wave
type: concept
status: mature
domain: [magnetism, spintronics, magnonics, multiferroicity]
mechanism: 局域磁矩围绕平衡方向的集体进动模式，量子化为磁振子；色散由交换作用/偶极相互作用与各向异性决定，可在绝缘体中无损传播
related_concepts: [ferromagnetism, antiferromagnetism, spin-transport, magnetoelectric-coupling, bloch-spin-wave, magnon-hall-effect, topological-magnon, electromagnon]
papers: [deSousa2008electrical, vanvleckSurveyTheoryFerromagnetism1945, rameshMultiferroicsProgressProspects2007, liPhaseTransitions2D2021]
updated: 2026-08
---

# 自旋波 / Spin Wave

自旋波（spin wave）指**磁性体系中局域磁矩围绕其平衡方向的集体进动模式**，其量子化准粒子称为磁振子（magnon）。自旋波可在绝缘体中传播（无焦耳热损耗），是低功耗自旋电子学与磁振子学的信息载体，也是研究磁性交换相互作用与各向异性的重要探针。

## 👵 太奶导读

磁铁里的磁矩不是僵死的：把一个磁矩"推歪"一下，它会像多米诺骨牌一样把"歪"传播给邻居——这个传播的"歪"就是自旋波（一个磁矩的集体舞蹈），它的量子叫磁振子。自旋波能在绝缘体里跑，不发热，是未来超低功耗计算的候选信息载体。

## 🧩 基本性质与色散

- **色散关系**：铁磁体近交换极限的自旋波色散为 $\omega(\mathbf{k}) \simeq D k^2$（$D$ 为交换刚度），长波处偶极相互作用使色散线性化；反铁磁体自旋波色散为线性 $\omega \propto c|\mathbf{k}|$（$c$ 为自旋波速度）。
- **布洛赫定律**：自旋波激发使铁磁磁化随温度降低，$M(T) = M_0(1 - B T^{3/2})$，这是自旋波低能激发的直接指纹（本库 [[../concepts/bloch-spin-wave|布洛赫自旋波]]）。
- **传播特征**：自旋波可承载角动量与自旋流，在磁绝缘体中传输无电子焦耳热，是低功耗信息载体。

## 🧩 自旋波与铁电调控

- **电控磁振子传播**：倾斜反铁磁 BiFeO₃ 薄膜中，最低频磁振子色散因长程偶极相互作用强烈依赖传播方向与奈尔矢量夹角；借电场翻转铁电极化可**无电流地开关自旋波传播**（[[../papers/deSousa2008electrical|de Sousa 2008]]）。
- **磁性理论框架**：从外斯分子场到海森堡交换作用、布洛赫自旋波、斯托纳集体电子模型的反铁磁性量子理论，确立了"定域—巡游"两大范式（[[../papers/vanvleckSurveyTheoryFerromagnetism1945|Van Vleck 1945]]）。

## 🧩 薄膜与二维材料中的自旋波

- 薄膜多铁性材料的电场调控磁性路线（交换偏置、界面工程）为自旋波的磁电操控提供平台（[[../papers/rameshMultiferroicsProgressProspects2007|Ramesh 2007]]）。
- 二维材料中的铁性（铁弹/铁电/铁磁）相变统一到"相变工程"范式下，关联自旋波的磁有序工程（[[../papers/liPhaseTransitions2D2021|Li 2021]]）。

## 📊 自旋波色散速览

| 体系 | 色散形式 | 关键参数 | 典型材料 |
|------|----------|----------|----------|
| 铁磁体（交换主导） | $\omega \simeq Dk^2$ | 交换刚度 $D \propto JSa^2$ | YIG、Fe、Ni |
| 反铁磁体 | $\omega \simeq c|k|$ | 自旋波速度 $c \propto \sqrt{JS}$ | MnF2、NiO、BiFeO3 |
| 偶极主导（长波） | $\omega \propto k$（Walker 模） | 磁化强度、几何 | 薄膜 YIG |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferromagnetism|铁磁性]]：自旋波的宿主序。
- [[../concepts/antiferromagnetism|反铁磁性]]：奈尔矢量与偶极自旋波。
- [[../concepts/spin-transport|自旋输运]]：自旋波的传导应用。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：电场调控自旋波的桥梁。
- [[../concepts/bloch-spin-wave|布洛赫自旋波]]：自旋波的微观量子理论。
- [[../concepts/magnon-hall-effect|磁振子霍尔效应]]：自旋波输运的拓扑效应。
- [[../concepts/topological-magnon|拓扑磁振子]]：具有拓扑能带的磁振子。
- [[../concepts/electromagnon|电磁振子]]：磁振子-声子杂化模式。
- [[../entities/BiFeO3|BiFeO₃]]：倾斜反铁磁磁振子平台。

## 📚 相关论文 (Related Papers)

- [[../papers/deSousa2008electrical]] — Electrical control of spin wave propagation in antiferromagnetic BiFeO3
- [[../papers/vanvleckSurveyTheoryFerromagnetism1945]] — A Survey of the Theory of Ferromagnetism
- [[../papers/rameshMultiferroicsProgressProspects2007]] — Multiferroics: progress and prospects in thin films
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials

## 🏷️ 专业名词别名

- `magnon`（concepts）
- `自旋集体进动`（concepts）
