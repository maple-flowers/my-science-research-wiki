---
tags: [concept, density-functional-theory, paw-method, pseudopotential, all-electron-method, core-valence-partition]
title: frozen-core-approximation
type: concept
status: developing
year: 1994
papers: [blochlProjectorAugmentedwaveMethod1994b, kresseUltrasoftPseudopotentialsProjector1999c]
updated: 2026-08-21
---

# frozen-core-approximation

**冻结芯近似（frozen-core approximation）** 把原子的内层（芯）电子态从自洽求解中拿掉，直接沿用孤立原子的芯态，只对价电子做变分。它是 [[../concepts/paw-method|PAW]] 与各类[[../concepts/pseudopotential|赝势]]方法共同的基础前提——**PAW 在冻结芯近似之内是密度泛函理论的精确实现**，误差不在 PAW 而在这条近似上。

## 👵 太奶导读

乖孙，一个原子里的电子分两拨：**外层的价电子**管成键、管导电、管一切化学；**内层的芯电子**被牢牢按在原子核附近，不管化学。

既然芯电子不参与成键，那每次算晶体时就不必再把它们重新解一遍——直接把孤立原子里算好的芯态搬过来用。这就是冻结芯近似。省下的计算量非常可观。

但这里有个**极容易误解的点**，太奶要你记牢：「冻结」**不等于**「一动不动」。

被冻住的是「芯态这个集合」，不是每一条芯态。势场变了，芯态之间是允许相互混合的——好比一屋子人不许出门，但屋里可以换座位。所以判断冻结芯近似准不准，**绝不能**拿孤立原子的芯态跟晶体里放松芯计算出的芯态一条一条对比——那样比出来的差别不是近似的误差，只是换了座位而已。

要记的一句话：**冻结芯是「芯电子照搬孤立原子、只自洽算价电子」；它冻住的是芯态的整体，允许芯态内部混合；PAW 的精度上限就由它划定。**

## 🧩 具体做法与理论地位

- **实现方式**：芯态自孤立原子导入。与价态不同，**芯态无需定义投影函数**，其单中心项的「系数」恒为 1。
- **变分自由度的真实限制**：冻结芯近似只把变分自由度限制为**芯态（及占据价态）之间的一个酉变换**；势场变化引起的芯态混合是允许的。这一点决定了检验其精度的正确方式——只能比较可观测量，不能逐条比较芯态波函数。
- **理论地位**：在引入平面波截断等实用近似**之前**，PAW 是密度泛函理论在冻结芯近似内的**精确实现**。因此 PAW 的结果应当与任何其他冻结芯全电子方法无法区分；超软赝势（US-PP）则在此之上再叠加额外近似，在增强函数取全电子形式的极限下与 PAW 严格等价。
- **电荷密度的分解**（kresse1999）：为处理冻结芯，芯电荷被拆为 n_c、ñ_c、n_Zc、ñ_Zc 四个量；总能中相应出现三类静电项——价电子间、冻结伪芯与价电子间、冻结芯之间。
- **可放松的方向**：允许芯态随瞬时势场调整的**软芯（soft core）方案**在原理上可行，Blöchl 已指出这是 PAW 的一项待实现扩展，但两篇论文中均未实现。

### 精度基准

| 检验 | 对照 | 偏差 | 性质 |
|---|---|---|---|
| 冻结芯 PAW / US-PP 的二聚体键长 | 放松芯全电子（AE）计算 | **< 0.1%**（F₂ 例外，约 0.2%） | 计算（方法间交叉验证） |

⚠️ **边界**：该基准取自小分子二聚体键长这一单一可观测量，采用 CA-PZ 交换关联泛函。它说明冻结芯对**结构量**足够准，不能直接推广到对芯区敏感的量（如超精细参数、电场梯度）——那类量正是 blochl1994 单独讨论的对象。

## 📚 相关论文 (Related Papers)

- [[../papers/blochlProjectorAugmentedwaveMethod1994b]]：本页概念界定的主要来源。该文明确交代芯态自孤立原子导入、芯态不需投影函数、单中心项系数恒为 1，并指出 PAW 在冻结芯近似内是 DFT 的精确实现；尤其重要的是它澄清了冻结芯只限制到「芯态间酉变换」这一层，因此不可逐条比较孤立原子与放松芯晶体的芯态——这是本页太奶导读中那个易错点的直接依据。同时它把软芯方案列为待实现扩展。
- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]]：给出冻结芯在总能泛函层面的具体落地——将芯电荷拆为 n_c、ñ_c、n_Zc、ñ_Zc 并写出对应的三类静电相互作用项；并提供了本页唯一的定量精度基准（冻结芯 PAW/US-PP 与放松芯全电子计算的二聚体键长偏差 < 0.1%），同时论证 US-PP 在增强函数取全电子形式的极限下与 PAW 严格等价、二者同在冻结芯近似内为精确。

## 🔗 关联概念与实体 (Related)

- [[../concepts/paw-method|paw-method]]
- [[../concepts/pseudopotential|pseudopotential]]
- [[../concepts/norm-conserving-pseudopotential|norm-conserving-pseudopotential]]
- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/projector-functions|projector-functions]]
- [[../concepts/augmentation-region|augmentation-region]]
- [[../concepts/compensation-charge-density|compensation-charge-density]]
- [[../concepts/additive-augmentation|additive-augmentation]]
- [[../concepts/norm-conservation|norm-conservation]]
- [[../concepts/pulay-force|pulay-force]]
- [[../entities/VASP|VASP]]
