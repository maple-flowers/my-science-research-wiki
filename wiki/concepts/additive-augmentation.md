---
tags: [concept, paw-method, density-functional-theory, basis-set, partial-waves, gw-approximation]
title: additive-augmentation
type: concept
status: developing
year: 1994
papers: [blochlProjectorAugmentedwaveMethod1994b, shishkinImplementationPerformanceFrequencydependentGWmethod2006]
updated: 2026-08-21
---

# additive-augmentation

**加法增强（additive augmentation）** 是 [[../concepts/paw-method|PAW 方法]]的核心原理：全电子（AE）与赝（PS）分波展开**以完全相同的方式截断**，于是「平滑的赝量 + 原子球内单中心修正项」这一加法结构在任意截断阶数下都自洽成立。它是 PAW 即使不引入软芯等额外机制也能保持高精度的根本原因。

## 👵 太奶导读

乖孙，PAW 算波函数的思路是「先糊后补」：

**第一步**，在整个空间用平面波算一个**平滑的、假的**波函数（赝波函数）——这个好算。
**第二步**，在每个原子周围划一个小球，在球里把「真实波函数」和「假波函数」各自展开成一系列分波，然后做减法：**加上真的、减去假的**。球外两者相同，减法归零；球内假的被换成真的。

加法增强说的就是这个「加真减假」的结构。它的要求听起来很平淡：**真的那套分波和假的那套，必须砍在同一个地方**——你保留几项真分波，就得保留几项假分波，一一对应。

**为什么这条要求这么关键？** 因为它一保证，三件好事跟着来：

1. 只要假分波构造得光滑，整个 PAW 波函数就**可任意阶求导**——不会在球面上留下折角。
2. 那些没被显式包含的高阶分波，**由伸进球内的平面波尾巴自动代表**了，不会凭空丢掉。
3. **只要平面波本身完备，PAW 基组就完备**，跟你砍了几项分波无关。正因如此，直接搬用孤立原子的分波才是合法的。

记一句话：**加法增强 = 真、假两套分波砍在同一处；换来可任意阶求导、高阶项由平面波尾巴兜住、基组完备性与截断无关。**

## 🧩 原理内容

- **形式**：在整个空间的规则平面波网格上定义赝量；要得到全电子量，在原子球内重构赝波函数，并**加上全电子单中心项、减去对应的赝单中心项**。球外两项相消。
- **判据（原理本身）**：AE 与 PS 分波展开必须以**完全类似的方式**截断。
- **由此得到的三项性质**：
  1. 若赝分波构造得足够光滑，PAW 波函数**可任意阶求导**。
  2. 未显式包含的高阶分波，由**伸入增强区的平面波尾部**代表。
  3. **只要平面波构成完备基组，PAW 基组即完备**，与分波截断无关——这正是「可以直接引入孤立原子分波」这一做法的合法性依据。
- **地位**：Blöchl 明确指出，PAW 即使**不**引入软芯、不放松[[../concepts/frozen-core-approximation|冻结芯近似]]，仅凭对加法增强原理的严格运用就已高度精确；这些扩展是「可以容纳」而非「必需」。

## 📚 相关论文 (Related Papers)

- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：本原理的提出与论证来源。该文把加法增强明确列为 PAW 的**关键性质**，给出其判据（AE 与 PS 分波展开须以完全相同方式截断）与三项直接后果（波函数可任意阶可导、高阶分波由平面波尾部代表、基组完备性与分波截断无关），并据第三点论证了引入孤立原子分波的正当性；尤其重要的是它指出 PAW 的高精度**根源于对该原理的严格运用**，而非依赖软芯或放松冻结芯这类附加机制。
- [[../papers/shishkinImplementationPerformanceFrequencydependentGWmethod2006]]：把加法增强表述为「在原子球内添加单中心项以修正平滑赝量」并配图示意（赝量定义于全空间的规则平面波网格上，球内重构赝波函数后减去对应单中心能量项），是本页「先糊后补」这一操作图像的直接依据；同时说明该原理是理解 PAW 框架下 GW 实现的前提——即加法增强不只服务于基态总能，也是把 PAW 推广到激发态方法时所依赖的结构。

## 🔗 关联概念与实体 (Related)

- [[../concepts/paw-method|paw-method]]
- [[../concepts/projector-functions|projector-functions]]
- [[../concepts/augmentation-region|augmentation-region]]
- [[../concepts/frozen-core-approximation|frozen-core-approximation]]
- [[../concepts/compensation-charge-density|compensation-charge-density]]
- [[../concepts/norm-conservation|norm-conservation]]
- [[../concepts/pseudopotential|pseudopotential]]
- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../entities/VASP|VASP]]
