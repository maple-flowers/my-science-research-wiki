---
tags: [concept]
title: 'kosterlitz-thouless'
type: concept
status: developing
papers: ['gomez-ortizKittelLawDomain2023', 'CastroNeto2001charge', 'hanPolarTopologicalMaterials2025', 'liPhaseTransitions2D2021']
updated: 2026-08-18
---

# kosterlitz-thouless

Kosterlitz-Thouless（KT，又称 BKT）相变是**二维体系中由拓扑缺陷（涡旋-反涡旋对）束缚-解束缚驱动的连续相变**：不存在长程有序（破缺连续对称），却存在准长程序（代数衰减关联），相变温度由涡旋解束缚决定。KT 相变是二维超流/超导、磁性 XY 模型与涡旋物理的基石，是 Kosterlitz 与 Thouless 获 2016 年诺贝尔物理学奖的工作。

## 👵 太奶导读

太奶啊，一般相变靠"有序度慢慢长大"完成，但二维世界很特殊：这里没有真正的"全体一致"（长程序），只能靠"小漩涡成对出现又成对消失"来改变状态。低温时漩涡俩俩"拴在一起"（束缚对），材料还算规整；温度一高，漩涡对"挣脱绳子"四散奔逃，材料性质"哐当"一变——这就是 KT 相变。二维超导、超流都有它的身影。

## 🧩 核心内容与机制 (Core Content)

- **二维特殊性**：Mermin-Wagner 定理禁止二维连续对称破缺长程序，关联函数呈幂律衰减（准长程序）。
- **涡旋-反涡旋束缚**：低温下拓扑缺陷（涡旋对）被束缚；高温下解束缚，介电常数发散、超流刚度跳变。
- **KT 温度 T_KT**：由涡旋核心能量与相互作用能量竞争决定，相变点出现螺旋度刚度跳跃（universal jump）。
- **应用体系**：二维超导（薄膜、界面超导）、二维超流、XY 磁体、约瑟夫森结阵列与冷原子体系（本库二维超导与涡旋相关论文）。
- **与一般相变的区别**：KT 相变无对称性破缺的局域序参量，以拓扑缺陷为序——属拓扑相变（topological-defects 相关）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/topological-defects|拓扑缺陷]]：KT 相变的载体。
- [[../concepts/phase-transition|相变]]：KT 相变的相变框架。
- [[../concepts/2d-materials|二维材料]]：KT 相变的实验平台。
- [[../concepts/superconductivity|超导]]：二维超导中的 KT 行为。

## 📚 相关论文 (Related Papers)

- [[../papers/gomez-ortizKittelLawDomain2023]] — Kittel law and domain formation mechanism in PbTiO3/SrTiO3 superlattices
- [[../papers/CastroNeto2001charge]] — Charge Density Wave, Superconductivity, and Anomalous Metallic Behavior in 2D Transition Metal Dichalcogenides
- [[../papers/hanPolarTopologicalMaterials2025]] — Polar topological materials and devices: Prospects and challenges
- [[../papers/liPhaseTransitions2D2021]] — Phase transitions in 2D materials

## 🏷️ 专业名词别名

- `kosterlitz-thouless-transition`（concepts）
