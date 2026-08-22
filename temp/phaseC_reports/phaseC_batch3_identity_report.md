# Phase C 第三批身份解析报告（第 101-150 页）

- 仓库：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki`
- 批次范围：wiki/concepts 与 wiki/entities 按字母序（slug.lower() 合并排序）第 101-150 页
- 执行方式：只读分析，未修改任何页面，未提交
- 保护集合：与 Phase A 一致（concepts 下 dirac-semimetal/exciplex/fluorescence-quantum-yield/pl-quenching/stokes-shift/thermochromism/1t-prime-phase/3r-phase；entities 下 2H-NbSe2/CoFe2O4/Cr2O3/GaSe；tools/audit_wiki_pages.py untracked），无并发修改

## 一、每页身份判定表

| # | 路径 | 身份类型 | 判定依据（一句话） |
| :--- | :--- | :--- | :--- |
| 101 | entities/benzene | short-aggregation | 具体分子实体，仅 1 篇论文反链（kaur2025a），名称有效但无正文 |
| 102 | concepts/berry-connection | short-aggregation | 贝里相位族子概念，仅 king-smith1993 反链，无正文 |
| 103 | concepts/berry-curvature | canonical | developing，有 frontmatter/太奶导读/结构概览/机制/图片/关联，内容完整 |
| 104 | concepts/berry-curvature-dipole | short-aggregation | 贝里曲率偶极子，2 篇论文反链，无正文 |
| 105 | concepts/berry-phase | short-aggregation | 核心概念（40 篇 paper frontmatter 引用）但无 frontmatter，仅论文列表聚合页 |
| 106 | concepts/bessel-beam | short-aggregation | 光学概念，3 篇论文反链，含悬空别名标注 |
| 107 | concepts/beta-pc-phase | short-aggregation | In2Se3 β' 相，1 篇论文反链，无正文 |
| 108 | concepts/beta0-phase | short-aggregation | In2Se3 β0 相，1 篇论文反链，无正文 |
| 109 | concepts/bethe-peierls-weiss-method | short-aggregation | 理论方法，vanvleck1945 反链，无正文 |
| 110 | entities/Bi0.5Na0.5TiO3 | short-aggregation | 具体材料实体（BNT），1 篇论文反链，无正文 |
| 111 | entities/Bi2Fe4O9 | short-aggregation | 具体材料实体，Goswami2011 反链，无正文 |
| 112 | entities/Bi2FeCrO6 | short-aggregation | 具体材料实体，ramesh2007 反链，无正文 |
| 113 | entities/Bi2O2Se | short-aggregation | 具体材料实体，zhang2025 反链，无正文 |
| 114 | entities/Bi2Te2Se | short-aggregation | 具体材料实体，liu2020b 反链，无正文 |
| 115 | entities/BiCoO3 | short-aggregation | 具体材料实体，spaldin2019 反链，无正文 |
| 116 | entities/BiFeO3 | canonical | mature，完整结构（导读/结构概览/机制/参数表/论文/关联），33 篇 paper fm 引用 |
| 117 | entities/bilayer-graphene | short-aggregation | 具体材料实体，7 篇论文反链，无正文 |
| 118 | concepts/bilayer-splitting | short-aggregation | 双层劈裂概念，Laverock2005 反链，无正文 |
| 119 | concepts/bilayer-stacking-ferroelectricity | short-aggregation | 滑移铁电子概念，zhang2025 反链，无正文 |
| 120 | concepts/bimeron | short-aggregation | 拓扑磁结构概念，4 篇论文反链，无正文 |
| 121 | entities/BiMnO3 | short-aggregation | 具体材料实体，hill2000a/ramesh2007 反链，无正文 |
| 122 | concepts/binding-strength | short-aggregation | 键合强度概念，4 篇论文反链，无正文 |
| 123 | concepts/biphoton | ambiguous | 跨领域歧义：量子光学双光子态 vs 双光子聚合/引发剂 vs 高能物理双光子末态 |
| 124 | concepts/bipolar-magnetic-semiconductor | short-aggregation | 双极磁性半导体概念，wu2024 反链，无正文 |
| 125 | concepts/birefringence | short-aggregation | 双折射概念，song2022 反链，无正文 |
| 126 | entities/bis-diphenylamino-diphenyl-hexatriene | short-aggregation | 具体分子实体（双光子引发剂），Khitrov2000 反链，无正文 |
| 127 | concepts/bistability | short-aggregation | 双稳态概念，fei2018a 反链，无正文 |
| 128 | entities/black-phosphorus | short-aggregation | 具体材料实体，4 篇论文反链，无正文 |
| 129 | entities/BLFO | short-aggregation | La 掺杂 BiFeO3 实体，Perugu2024 反链，无正文；BiFeO3 掺杂变体 |
| 130 | concepts/bloch-spin-wave | short-aggregation | 布洛赫自旋波概念，vanvleck1945 反链，无正文 |
| 131 | concepts/block-averaging-msd | short-aggregation | 计算分析方法，Mińkowski2021 反链，无正文 |
| 132 | concepts/boltzmann-distribution | short-aggregation | 玻尔兹曼分布概念，nose1984 反链，无正文 |
| 133 | concepts/boltzmann-transport | short-aggregation | 玻尔兹曼输运概念，khazaei2013 反链，无正文 |
| 134 | entities/BoltzTrap | short-aggregation | 具体软件实体（Boltzmann 输运计算），khazaei2013 反链，无正文 |
| 135 | concepts/bond-density | short-aggregation | 键密度概念，4 篇论文反链，无正文；与 bonding-charge-density 近义 |
| 136 | concepts/bonding-charge-density | short-aggregation | 成键电荷密度概念，Li2013bonding 反链，无正文；与 bond-density 近义 |
| 137 | concepts/born-effective-charge | short-aggregation | 玻恩有效电荷概念，6 篇论文反链，无正文 |
| 138 | concepts/born-oppenheimer-md | short-aggregation | 计算模拟方法，kresse1993/1994 反链，无正文 |
| 139 | entities/bp-bi-bismuth | short-aggregation | slug 含义待核实（BP/Bi 相关），仅 guo2025 综述反链，无正文 |
| 140 | concepts/bragg-peaks | short-aggregation | 布拉格峰概念，petkov2002 反链，无正文 |
| 141 | concepts/brillouin-function | short-aggregation | 布里渊函数概念，vanvleck1945 反链，无正文 |
| 142 | concepts/brillouin-zone | short-aggregation | 布里渊区概念，9 篇论文反链，无正文 |
| 143 | concepts/brillouin-zone-integration | short-aggregation | 布里渊区积分方法，Delley2000/monkhorst1976 反链，无正文 |
| 144 | concepts/broken-inversion-symmetry | canonical | developing，有 frontmatter/太奶导读/结构概览/机制/图片/关联，内容完整 |
| 145 | entities/BSA | short-aggregation | 具体生物分子实体（牛血清白蛋白），Gittard2013 反链，无正文 |
| 146 | entities/BTO | alias | BaTiO3 缩写，规范页 entities/batio3 存在，应指向 batio3 |
| 147 | concepts/bulk-boundary-correspondence | canonical | developing，有 frontmatter/太奶导读/结构概览/机制/图片/关联，内容完整 |
| 148 | concepts/bulk-photovoltaic-effect | short-aggregation | 体光伏效应概念，3 篇论文反链，无正文 |
| 149 | entities/c-AFM | short-aggregation | 导电原子力显微镜实体，Chen2016 反链，无正文；afm 的导电模式变体 |
| 150 | entities/C2DB | short-aggregation | 具体数据库实体（计算二维材料数据库），feng2020 反链，无正文 |

## 二、类别汇总

| 身份类型 | 数量 | 页面 |
| :--- | :--- | :--- |
| canonical | 4 | berry-curvature、BiFeO3、broken-inversion-symmetry、bulk-boundary-correspondence |
| short-aggregation | 44 | 其余 44 页 |
| alias | 1 | BTO（→ batio3） |
| ambiguous | 1 | biphoton |
| misplaced | 0 | — |
| no-evidence | 0 | — |
| **合计** | **50** | |

## 三、问题清单

### 1. 同 slug 跨层碰撞
- **无新增**。全库仍为 Phase A 已知 3 对（1t-phase、bamboo-like-N-CNTs、glassy-carbon），本批 50 页均未涉及。

### 2. 规范化名称重复
- **bond-density vs bonding-charge-density**（concepts）：语义几乎相同（键密度/成键电荷密度），反链高度重叠（Li2013bonding、Wu2021、yan2025、zhong2025），候选重复，建议 Phase G 合并或明确区分（bonding-charge-density 更具体，指向成键电荷分布）。

### 3. 缩写/全称与拼写变体
- **BTO = BaTiO3**：规范页 entities/batio3 存在，BTO 判 alias。
- **BLFO = La 掺杂 BiFeO3**（BiFe1-xLaxO3）：BiFeO3 的掺杂变体，独立实体但应建立与 BiFeO3 的关联。
- **c-AFM = conductive AFM**：entities/afm 存在，c-AFM 是 AFM 的导电模式变体。
- **C2DB = Computational 2D Materials Database**：数据库实体，无全称页。
- **BoltzTrap**：软件实体，与 boltzmann-transport 概念关联。
- **BSA = bovine serum albumin**：生物分子实体，无全称页。
- **beta-pc-phase / beta0-phase**：In2Se3 同族相变体（β' 相、β0 相），同一篇论文（huang2022），互为同族变体。
- **悬空别名**：concepts/bessel-beam 页标注"专业名词别名 bessel-beams（concepts）"，但该页不存在，需在 Phase E 处理（补建或删除标注）。

### 4. 父子概念关系
- **贝里相位族**：berry-connection ⊂ berry-phase ⊃ berry-curvature ⊃ berry-curvature-dipole。
- **born-oppenheimer-md ⊂ aimd / molecular-dynamics**（aimd、molecular-dynamics 页存在）。
- **brillouin-zone-integration ⊂ brillouin-zone**（k-point-sampling 页存在）。
- **bimeron 与 skyrmion / meron 同族**（拓扑磁结构）。
- **bilayer-stacking-ferroelectricity ⊂ sliding-ferroelectricity**。
- **bilayer-graphene ⊂ graphene**。
- **BiFeO3 ⊃ BLFO**（掺杂变体）。
- **c-AFM ⊂ afm**。
- **born-effective-charge 与 polarization**（king-smith1993 现代极化理论）。

### 5. 歧义词
- **biphoton**：跨领域歧义。①量子光学"双光子态/双光子波函数"（Nakanishi2009full 真实相关）；②双光子聚合/双光子引发剂（Khitrov2000holographic、Unknown2014passive）；③高能物理"双光子末态"（Şahin2009probe）。建议写术语辨析页，规范指向量子光学双光子态。

### 6. 跨层误放
- **0 新增**。本批无具体材料/器件误放 concepts 的情况：bessel-beam 为光学概念（concepts 合理）；BoltzTrap/C2DB/c-AFM/BSA/benzene/black-phosphorus 等实体均在 entities 正确分层。

### 7. 无证据页
- **0**。本批所有页面均有至少 1 篇论文反链。

### 8. 论文反链误聚合/弱相关
- **biphoton ← sunSlidingFerroelectricityTwodimensional2025**：滑移铁电综述，仅在"项目连接汇总"中标注"无直接连接"，属误聚合。
- **biphoton ← Şahin2009probe**：高能物理 LHC 双光子产生论文，跨领域误聚合（与凝聚态/量子光学语境不符）。
- **biphoton ← Khitrov2000holographic / Unknown2014passive**：双光子聚合/双光子引发剂论文，与"双光子态"概念弱相关（不同含义）。
- **bessel-beam ← Wang2023ultracompact**：Mathieu-Gauss 光束论文，与贝塞尔光束相关但不同（弱相关，论文正文已明确区分）。
- **bp-bi-bismuth ← guoAdvancesTwodimensionalFerroelectric2025**：仅综述反链，需在 Phase D 核实该综述是否真实涉及 BP/Bi 体系。

## 四、下一批提示
- 下一批从第 151 页开始（字母序 concepts/entities 合并排序，c4-symmetry-breaking 起）。
- 本批无新增跨层碰撞、无 misplaced、无 no-evidence，与 Phase A 基线一致。
