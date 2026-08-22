---
tags: [concept]
title: 'nudged-elastic-band'
type: concept
status: developing
papers: ['liFerroelasticityDomainPhysics2016', 'lezoualchStudyChargeDensity', 'chenFerromagneticNonmagnetic1T2022', 'henkelmanClimbingImageNudged2000c', 'fengFerroelectricityMultiferroicityTwodimensional2020', 'hanTunableSlidingFerroelectricity2025']
updated: 2026-08-18
---

# nudged-elastic-band

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


Nudged Elastic Band（NEB，弹性带方法）是**计算化学反应/结构转变/缺陷迁移的最小能量路径（MEP）与能垒**的方法：在初末态之间插入一串镜像，通过弹簧约束 + 垂直于路径的力投影使带"滑向"鞍点路径。NEB 是研究扩散、相变、表面反应与成核动力学势垒的标准第一性原理工具。

## 👵 太奶导读

太奶啊，材料里原子从位置 A 挪到位置 B（比如扩散、离子搬家、吸附分子换个姿态），中间要"翻过一座能量山"。NEB 方法就是在电脑里把 A 和 B 之间拉一根"橡皮筋"（一串中间构型），让橡皮筋自动滑到"翻山最省力的那条路"（最低能量路径），从而量出这座"能量山"有多高（能垒）。能垒多高，直接决定反应快慢。

## 🧩 核心内容与机制 (Core Content)

- **方法要点**：初末态间插入 N 个镜像，弹簧力沿路径切向、真实力沿垂直方向投影，迭代收敛到 MEP；Climbing Image NEB（CI-NEB）精确定位鞍点。
- **能垒与速率**：由能垒（ΔE）经过渡态理论（TST）估算跃迁速率 k = ν·exp(-ΔE/k_BT)；本库离子迁移、Li/Na 扩散、铁电翻转等论文采用。
- **应用**：缺陷迁移（空位/间隙扩散）、离子电导、表面反应（催化）、相变成核路径、铁电/铁弹畴翻转路径（switching-barrier）。
- **与 MD 互补**：NEB 给出静态路径与能垒，MD 给出动态时间演化（molecular-dynamics 互补）。
- **配合 MLP**：机器学习势（machine-learning-potential）可大幅降低 NEB 采样成本。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/metastability|亚稳态]]：势垒分隔的局部极小。
- [[../concepts/switching-barrier|翻转势垒]]：NEB 计算的典型能垒。
- [[../concepts/molecular-dynamics|分子动力学]]：与 NEB 互补的动态方法。
- [[../concepts/machine-learning-potential|机器学习势]]：加速 NEB 的势函数。

## 📚 相关论文 (Related Papers)

- [[../papers/liFerroelasticityDomainPhysics2016]] — Ferroelasticity and domain physics in two-dimensional transition metal dichalcogenide monolayers
- [[../papers/lezoualchStudyChargeDensity]] — Study of charge density waves in transition metal dichalcogenides
- [[../papers/chenFerromagneticNonmagnetic1T2022]] — Ferromagnetic and nonmagnetic 1T′ charge density wave states in transition metal dichalcogenides: Physical mechanisms and charge doping induced reversible transition
- [[../papers/henkelmanClimbingImageNudged2000c]] — A climbing image nudged elastic band method for finding saddle points and minimum energy paths
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in two-dimensional Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/hanTunableSlidingFerroelectricity2025]] — Tunable sliding ferroelectricity in two-dimensional van der Waals RuX2 (X = Cl, Br, and I) multiferroic layers

## 🏷️ 专业名词别名

- `neb`（concepts）
