# Phase C 第一批身份解析报告（前 50 页，只读）

- 仓库：E:\swan_goose\宝宝\笔记库\sgg\科研Wiki（分支 feature/wiki-synthesis-expansion）
- 范围：wiki/concepts 与 wiki/entities 按字母序（不区分大小写）合并前 50 页
- 模式：只读分析，未修改任何页面，未提交
- 审计工具：tools/audit_wiki_pages.py --json（全量 1679 页，基线数据与 Phase A 一致）

## 一、每页身份判定表

| # | 路径 | 身份类型 | 判定依据（一句话） |
| :-- | :-- | :-- | :-- |
| 1 | entities/1T-double-prime-TMD | short-aggregation | 1T'' 相 TMD 具体结构相实体，1 篇论文（tang2025 滑移铁电）证据有效，无正文 |
| 2 | entities/1T-MoTe2 | short-aggregation | 具体材料实体，2 篇论文（Islam2025/guo2025）证据有效，无正文 |
| 3 | entities/1T-NbSe2 | short-aggregation | 具体材料实体，1 篇论文（nakata2021 CDW）证据有效，无正文 |
| 4 | concepts/1t-phase | alias | 与 entities/1t-phase 同 slug 跨层碰撞；短聚合页（3 篇论文），规范页在 entities，应作别名/重复页 |
| 5 | entities/1t-phase | canonical | 成熟页（60 行，mature），完整定义 1T 相结构、CDW、关联概念与参数 |
| 6 | concepts/1t-prime-phase | short-aggregation | 1T' 畸变相独立术语，1 篇论文（wong 1T' CDW）证据有效，无正文 |
| 7 | entities/1T-TaS2 | short-aggregation | 具体材料实体，4 篇论文（cossu/kim/nakata/Chen2019）证据有效，无正文 |
| 8 | entities/1T-TaSe2 | short-aggregation | 具体材料实体，1 篇论文（nakata2021）证据有效，无正文 |
| 9 | entities/2d-acar | short-aggregation | 2D-ACAR 测量技术实体，1 篇论文（Laverock2005，entities 明确含 2d-acar）证据有效，无正文 |
| 10 | concepts/2d-materials | short-aggregation | 二维材料总概念，102 篇论文反链聚合但全无正文，需升级为 canonical |
| 11 | concepts/2d-mof | short-aggregation | 二维 MOF 概念，1 篇论文（zheng2025 kagome 超导）证据有效，无正文 |
| 12 | entities/2H-NbSe2 | canonical | 成熟页（102 行，mature），完整 CDW/超导机制、参数表与关联概念 |
| 13 | entities/2h-phase | canonical | 成熟页（48 行，mature），完整定义 2H 相结构、物性与关联材料 |
| 14 | entities/2H-TaS2 | short-aggregation | 具体材料实体，1 篇论文（kim1997，T→H 相变弱相关）证据可接受，无正文 |
| 15 | entities/2H-TaSe2 | short-aggregation | 具体材料实体，4 篇论文（Barnett/kim/Chen2019/gorkov）证据有效，无正文 |
| 16 | concepts/3r-phase | short-aggregation | 3R 相结构相概念，1 篇论文（sun2025 滑移铁电）证据有效，无正文 |
| 17 | entities/3r-tmds | short-aggregation | 3R 相 TMD 材料族实体，1 篇论文（guo2025）证据有效，无正文 |
| 18 | entities/4d-stem | short-aggregation | 4D-STEM 表征技术实体，1 篇论文（sun2025，弱相关）证据可接受，无正文 |
| 19 | entities/A36-low-carbon-steel | short-aggregation | 具体材料实体，1 篇论文（Zhang2003a 奥氏体→铁素体相变）证据有效，无正文 |
| 20 | concepts/aberration-correction | short-aggregation | 像差校正概念，Jia2023 证据有效；spaldin2019 反链为误聚合（见问题清单） |
| 21 | entities/ABINIT | short-aggregation | DFT 软件实体，1 篇论文（Li2013bonding，entities 明确含 ABINIT）证据有效，无正文 |
| 22 | entities/abp2x6-family | short-aggregation | ABP2X6 材料族实体，1 篇论文（lai2019 CuCrP2S6）证据有效，无正文 |
| 23 | concepts/absolute-humidity | short-aggregation | 绝对湿度概念，1 篇论文（Yarai2005 湿度传感器）证据有效，无正文 |
| 24 | concepts/absorption-spectrum | canonical | 正式页（51 行，developing），完整定义、ICT 机制与 P1 探针案例 |
| 25 | concepts/across-layer-sliding-ferroelectricity | short-aggregation | 跨层滑移铁电子概念，1 篇论文（kaur2025）证据有效，无正文 |
| 26 | concepts/adaptive-optics | short-aggregation | 自适应光学概念，1 篇论文（Jia2023，concepts 含 adaptive-optics）证据有效，无正文 |
| 27 | concepts/additive-augmentation | short-aggregation | PAW 加性增强概念，blochl1994 证据有效；shishkin GW 弱相关，无正文 |
| 28 | concepts/additive-manufacturing | no-evidence | 唯一反链 Zhang2019c 为误聚合（Ti 团簇原子模拟与增材制造无关），无有效论文证据 |
| 29 | concepts/adsorption-desorption | short-aggregation | 吸附-脱附概念，1 篇论文（Ismail2015 ZnO 湿度传感器）证据有效，无正文 |
| 30 | concepts/adsorption-desorption-hysteresis | short-aggregation | 吸附-脱附滞后概念，1 篇论文（Ismail2015）证据有效，无正文 |
| 31 | concepts/adsorption-energy | short-aggregation | 吸附能概念，1 篇论文（Wu2018 Ge/Si(001)）证据有效，无正文 |
| 32 | concepts/adsorption-energy-landscape | short-aggregation | 吸附能景观概念，1 篇论文（Wu2021 Ge 二聚体）证据有效，无正文 |
| 33 | entities/advanced-photon-source | short-aggregation | APS 同步辐射设施实体，1 篇论文（Petkov2020，entities 明确含 advanced-photon-source）证据有效，无正文 |
| 34 | entities/AFM | ambiguous | 缩写歧义：原子力显微镜（仪器，Kumar2017 证据）vs 反铁磁 antiferromagnetism（concepts 页存在），需辨析页 |
| 35 | entities/agarose | short-aggregation | 琼脂糖材料实体，1 篇论文（XiaokangZhang2013 湿度传感器，弱相关）证据可接受，无正文 |
| 36 | concepts/aimd | short-aggregation | AIMD 计算方法概念，3 篇论文（kresse 两篇经典 + han2025）证据有效，无正文 |
| 37 | concepts/air-sensitive-2d-materials | short-aggregation | 空气敏感二维材料概念，1 篇论文（niu2021）证据有效，无正文 |
| 38 | entities/Al-doped-ZnO | short-aggregation | 具体材料实体，1 篇论文（Ismail2015）证据有效，无正文 |
| 39 | entities/ALD | short-aggregation | 原子层沉积制备技术实体，1 篇论文（chen2026 Hf 铁电）证据有效，无正文 |
| 40 | entities/AlN | short-aggregation | 具体材料实体，2 篇论文（han2025/wu2021）证据有效，无正文 |
| 41 | entities/alpha-Fe2O3 | short-aggregation | 具体材料实体，1 篇论文（tan2024 反铁磁量子磁强计）证据有效，无正文 |
| 42 | concepts/altermagnetism | short-aggregation | 交变磁性概念，3 篇论文（kaur/yu/zhong，concepts 均含 altermagnetism）证据有效，无正文 |
| 43 | entities/AM2X4-intercalation-family | short-aggregation | AM2X4 插层材料族实体，1 篇论文（zhao2024）证据有效，无正文 |
| 44 | concepts/amorphous-semiconductor | short-aggregation | 非晶半导体概念，1 篇论文（kresse1994）证据有效，无正文 |
| 45 | concepts/amplitudon-phason | canonical | 正式页（53 行，developing），完整定义 CDW 振幅子/相位子与关联概念 |
| 46 | concepts/anderson-blount-mechanism | short-aggregation | Anderson-Blount 机制概念，1 篇论文（bhowal2023 极性金属）证据有效，无正文 |
| 47 | concepts/anderson-theorem | short-aggregation | Anderson 定理概念，1 篇论文（Koley2020 CDW 综述）证据有效，无正文 |
| 48 | concepts/andreev-reflection | short-aggregation | Andreev 反射概念，1 篇论文（majumdar2020）证据有效，无正文 |
| 49 | concepts/anharmonic-effects | short-aggregation | 非谐效应概念，2 篇论文（gomez-ortiz 弱相关 + lezoualch）证据可接受，无正文 |
| 50 | concepts/anisotropic-rippling | short-aggregation | 各向异性褶皱概念，1 篇论文（niu2021）证据有效，无正文 |

## 二、类别汇总

| 身份类型 | 数量 | 占比 |
| :-- | :-- | :-- |
| canonical | 5 | 10% |
| short-aggregation | 42 | 84% |
| alias | 1 | 2% |
| ambiguous | 1 | 2% |
| misplaced | 0 | 0% |
| no-evidence | 1 | 2% |
| 合计 | 50 | 100% |

补充：42 个 short-aggregation 中，绝大多数（40 个）为 5-11 行纯论文列表页（无 frontmatter、无正文），2 个（2d-materials 106 行、aimd 11 行）论文较多但仍无正文。5 个 canonical 均为已有正式页（3 mature + 2 developing）。

## 三、问题清单

### 1. 同 slug 跨层碰撞
- **1t-phase**（concepts + entities）：基线已知 3 对之一，前 50 页内确认存在，**无新增碰撞**。concepts/1t-phase 为短聚合页（3 篇论文），entities/1t-phase 为成熟页。建议：concepts/1t-phase 保留为别名/迁移说明页，指向 entities/1t-phase。

### 2. 规范化名称重复 / 层放置不一致
- **1t-phase 双目录重复**（同上）。
- **相类页面跨层不一致**：1t-phase 双目录、2h-phase 仅 entities、3r-phase 仅 concepts——同族"晶体结构相"页面放置层不统一，需在 Phase G 统一决策（相类概念应归 concepts 或统一归 entities）。

### 3. 缩写/全称与拼写变体
- **aimd**（concepts）↔ **molecular-dynamics**（concepts，全称页存在）：缩写/全称变体，建议互链。
- **ALD**（entities）：缩写，无全称页 atomic-layer-deposition。
- **AFM**（entities）↔ **antiferromagnetism**（concepts）：缩写歧义（见歧义词）。
- **4d-stem**（entities）：缩写，无全称页。
- **2d-acar**（entities）：缩写，无全称页。
- **1t-phase vs 1T-phase**：slug 统一小写 1t，H1 用 1T，大小写变体（库内 slug 规范为小写，一致）。
- **1T-double-prime-TMD**：1T'' 相拼写变体，与 1t-prime-phase（1T'）同族。

### 4. 父子概念关系
- 1t-prime-phase ⊂ 1t-phase（1T' 为 1T 畸变相）
- 1T-double-prime-TMD ⊂ 1T 相族
- 1T-TaS2 / 1T-TaSe2 / 1T-NbSe2 / 1T-MoTe2 ⊂ 1t-phase
- 2H-TaS2 / 2H-TaSe2 / 2H-NbSe2 ⊂ 2h-phase
- 3r-tmds ⊂ 3r-phase
- across-layer-sliding-ferroelectricity ⊂ sliding-ferroelectricity
- adsorption-desorption-hysteresis ⊂ adsorption-desorption
- adsorption-energy-landscape ⊂ adsorption-energy
- 2d-mof ⊂ 2d-materials
- air-sensitive-2d-materials ⊂ 2d-materials
- Al-doped-ZnO ⊂ ZnO
- abp2x6-family ⊃ CuCrP2S6 等具体成员
- additive-augmentation ⊂ paw（PAW 方法）

### 5. 歧义词
- **AFM**：原子力显微镜（仪器实体）vs 反铁磁 antiferromagnetism（concepts 概念页）。需写成"术语辨析"页，列出两义与真实目标链接。

### 6. 跨层误放
- 前 50 页**无明确跨层误放**。concepts 下均为抽象概念，entities 下均为具体材料/软件/仪器/设施/技术。仅相类页面层放置不一致（见第 2 项）。

### 7. 无证据页
- **additive-manufacturing**（concepts）：唯一反链 Zhang2019c 为误聚合（Ti 团簇原子模拟与增材制造无关），当前无有效论文证据，建议标 stub 并说明证据缺口。

### 8. 论文反链误聚合/弱相关（供 Phase D/E 扩展时核实）
- 误聚合：aberration-correction ← spaldin2019（多铁综述，与像差校正无关）
- 误聚合：additive-manufacturing ← Zhang2019c（导致 no-evidence）
- 弱相关（可接受但需核实）：2H-TaS2 ← kim1997；4d-stem ← sun2025；aimd ← han2025；additive-augmentation ← shishkin2006；anharmonic-effects ← gomez-ortiz2023；agarose ← XiaokangZhang2013

## 四、说明
- 本批为只读分析，未修改任何页面、未提交、未触碰保护集合（7 个已修改页 + audit 工具）。
- 基线数据（碰撞 3 对、raw_links 109、missing_images 16、broken_links 0）与 Phase A 一致，本批无新增错误。
- 建议下一批从第 51 页（concepts/anisotropic-superconductivity）继续。
