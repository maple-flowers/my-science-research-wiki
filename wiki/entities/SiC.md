---
tags: [entity, substrate, epitaxial-growth, molecular-beam-epitaxy, 2d-materials, sliding-ferroelectricity, ferroelectricity, charge-density-wave]
title: SiC
type: entity
status: developing
year: 2021
papers: [kawakamiChargedensityWaveAssociated2023, nakataRobustChargedensityWave2021, yanagizawaSwitchingChargedensityWave2023, wuSlidingFerroelectricity2D2021a]
updated: 2026-08-21
---

# SiC

**碳化硅（SiC）** 在本库中以两种完全不同的身份出现，读这一页时必须先分清是哪一种：

1. **作为衬底**：`双层石墨烯/SiC(0001)` 是分子束外延生长单层过渡金属硫族化合物的标准衬底组合，本库三篇 CDW 实验论文全部用它。
2. **作为二维铁电候选材料**：石墨型（graphitic）SiC 双层属于蜂窝晶格二元化合物，AB 堆垛下具有可观的垂直极化，属 [[../concepts/sliding-ferroelectricity|滑移铁电]]家族。

## 👵 太奶导读

乖孙，这一页要讲的 SiC 有两副面孔，别搞混。

**第一副面孔是「地板」。** 想研究单层材料，得先把它长出来。实验上的常规做法是：拿一块 SiC 晶体，先在它表面长出两层石墨烯，再把要研究的单层材料（比如 VS₂、TaSe₂、TiTe₂）长在石墨烯上。为什么要垫这层石墨烯？因为石墨烯跟上面的材料之间只有很弱的范德华力，不会把上面那层「拽歪」，也不会跟它发生化学反应——这样测出来的电子结构才是单层材料自己的，不是衬底的。SiC 在这里的角色是那块「地基」，它得平整、绝缘、且能在高温下稳定地长出石墨烯。

**第二副面孔是「材料本身」。** 如果把 SiC 做成像石墨那样一层一层的蜂窝结构，两层错开一点堆起来（AB 堆垛），它上下就不再对称，会自己产生一个垂直方向的电极化——这就是滑移铁电。滑动一下就能把极化翻过来。

记一句话：**看到「双层石墨烯/SiC(0001)」，SiC 是衬底；看到「graphitic SiC 双层 6.17 pC/m」，SiC 是铁电材料。**

## 🧩 身份一：外延生长衬底 (Substrate)

- **标准结构**：`SiC(0001)` 单晶（nakata2021 明确为 **6H-SiC** 多型）→ 表面石墨化生成**双层石墨烯**→ MBE 生长目标单层薄膜。
- **为什么要垫石墨烯**：石墨烯与上层薄膜之间为范德华相互作用，几乎不引入界面成键与晶格约束，使所测电子结构接近本征单层；SiC 本身则提供平整、绝缘、耐高温的基底。
- **生长质量判据**：RHEED 图样呈清晰 1×1 条纹即表明薄膜为原子级平整的单层（多层会出现 2×1 周期）。这是后续 ARPES 测量可信的前提。
- **附带用途**：SiC 上的双层石墨烯还可作为**掺杂剂量的标定物**——K 原子沉积到石墨烯上会向其 π 带注入电子、使 K 点费米面增大，据此可反推同一蒸发速率下目标薄膜的掺杂量（nakata2021）。

## 💠 身份二：石墨型双层的滑移铁电

| 体系 | 垂直极化 | 对照 | 性质 |
|---|---|---|---|
| graphitic SiC AB 双层 | 6.17 pC/m | 高于 BN（2.08）与 MoS₂（0.97），低于 AlN（10.29）、GaN（9.72）、ZnO（8.22） | 计算预测 |

⚠️ **边界**：该数值来自 [[../papers/wuSlidingFerroelectricity2D2021a\|wu2021]] 综述汇总表的第一性原理计算结果，本库无 SiC 双层的实验极化数据。且 `pC/m` 为二维面极化单位，需除以层间距才能与体相 `μC/cm²` 比较。

## 📚 相关论文 (Related Papers)

### 作为外延衬底

- [[../papers/kawakamiChargedensityWaveAssociated2023]]：在双层石墨烯/SiC(0001) 上先 MBE 生长单层 VTe₂、再经硫化拓扑化学反应替换为单层 VS₂，为本页提供了「SiC 衬底 + 后续化学转化」这一非直接生长路径的实例，并以 RHEED 1×1 条纹确认了单层性。
- [[../papers/nakataRobustChargedensityWave2021]]：明确给出衬底为**双层石墨烯/6H-SiC**，是本页唯一交代 SiC 多型的来源；同时展示了利用 SiC 上石墨烯 π 带费米面变化来标定 K 掺杂剂量的技巧。
- [[../papers/yanagizawaSwitchingChargedensityWave2023]]：在双层石墨烯/SiC(0001) 上 MBE 生长单层 1T-TiTe₂ 并用 RHEED 实时监控生长，说明该衬底组合可支持通过调节生长条件实现空穴/电子掺杂的系列样品。

### 作为二维铁电材料

- [[../papers/wuSlidingFerroelectricity2D2021a]]：在蜂窝晶格二元化合物双层极化汇总表中给出 graphitic SiC 的 6.17 pC/m，把 SiC 纳入滑移铁电候选材料序列，是本页第二重身份的唯一依据。

## 🔗 关联概念与实体 (Related)

- [[../concepts/sliding-ferroelectricity|sliding-ferroelectricity]]
- [[../concepts/ferroelectricity|ferroelectricity]]
- [[../concepts/2d-materials|2d-materials]]
- [[../concepts/charge-density-wave|charge-density-wave]]
- [[../entities/graphene|graphene]]
- [[../entities/TMDs|TMDs]]
- [[../entities/AlN|AlN]]
- [[../entities/GaN|GaN]]
- [[../entities/ZnO|ZnO]]
