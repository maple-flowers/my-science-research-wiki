# Phase C 第四批身份解析报告（第 151-170 页）

- 批次范围：`c4-symmetry-breaking` → `CCD-camera`（按 slug.lower() 合并排序）
- 页数：20 页（concepts 10 页、entities 10 页）
- 模式：只读分析，未修改任何页面，未提交
- 日期：2026-08-16

## 一、每页身份判定表

| # | 路径 | 身份类型 | 判定依据（一句话） |
| :--- | :--- | :--- | :--- |
| 151 | concepts/c4-symmetry-breaking | short-aggregation | 5 行仅 1 篇论文（Kang2012dimer 铁基超导 C4 对称性破缺），名称有效但无 frontmatter/正文 |
| 152 | entities/c6n8h-organic-multiferroic | short-aggregation | 5 行仅 1 篇（hu2019 低维多铁综述），具体材料实体，目录正确 |
| 153 | entities/Ca3Mn2O7 | short-aggregation | 5 行仅 1 篇（mostovoy2024 多铁综述），具体材料实体，目录正确 |
| 154 | entities/Ca3Ru2O7 | short-aggregation | 5 行仅 1 篇（bhowal2023b 极性金属），具体材料实体，目录正确 |
| 155 | entities/cadmium-sulfide | short-aggregation | 5 行仅 1 篇（shishkin2006 GW 论文以 CdS 为测试材料），具体材料实体，目录正确 |
| 156 | entities/CADPAC | short-aggregation | 5 行仅 1 篇（perdew1996 PBE 论文用 CADPAC 程序实现），软件实体，目录正确，反链弱相关 |
| 157 | entities/CaMn7O12 | short-aggregation | 5 行仅 1 篇（fiebig2016 多铁综述），具体材料实体，目录正确 |
| 158 | concepts/canonical-ensemble | short-aggregation | 5 行仅 1 篇（nose1984 恒温 MD），正则系综为有效统计力学概念，与 nvt-ensemble 近义 |
| 159 | concepts/canted-antiferromagnetism | short-aggregation | 5 行仅 1 篇（deSousa2008 DM 倾斜反铁磁），有效概念，与 weak-ferromagnetism 父子/近义 |
| 160 | concepts/capacitive-sensor | short-aggregation | 5 行仅 1 篇（Ismail2015 ZnO 湿度传感器综述），有效传感类型概念，反链相关需核实 |
| 161 | concepts/Car-Parrinello | short-aggregation | 15 行 3 篇论文 + 别名章节，有效计算方法概念，但别名章节标注的变体页均不存在（悬空别名） |
| 162 | concepts/carbazole-derivatives | short-aggregation | 5 行仅 1 篇（Xie2024 咔唑衍生物同构掺杂），化合物类别概念，misplaced 候选待 Phase G |
| 163 | entities/carbon-nanotube | short-aggregation | 10 行 2 篇（Khitrov2002、Wei2021）+ 别名章节，具体材料实体，目录正确，别名章节标注 carbon-nanotubes 不存在（悬空别名） |
| 164 | concepts/carrier-density-modulation | short-aggregation | 5 行仅 1 篇（Owji2021 光纤湿度传感器），有效概念，与 carrier-mobility 相关 |
| 165 | concepts/carrier-detrapping | short-aggregation | 5 行仅 1 篇（TSUJI2019 机械发光去俘获），有效概念 |
| 166 | concepts/carrier-mobility | short-aggregation | 5 行仅 1 篇（yan2025 III-V 半导体形变势迁移率），有效概念 |
| 167 | concepts/carrier-tuning | short-aggregation | 5 行仅 1 篇（yanagizawa2023 单层 TiTe2 载流子调谐 CDW），有效概念，与 charge-doping 近义 |
| 168 | entities/castellated-electrode | short-aggregation | 5 行仅 1 篇（Ismail2015 湿度传感器电极），电极结构实体，目录正确，与 interdigitated-electrode 同族 |
| 169 | entities/CCC-amphidynamic-crystal | short-aggregation | 5 行仅 1 篇（zhang2025 滑动铁电），具体材料实体，目录正确 |
| 170 | entities/CCD-camera | short-aggregation | 5 行仅 1 篇（Jia2023 双光子聚合实验用 CCD），仪器实体，目录正确 |

## 二、各类别汇总数量

| 身份类型 | 数量 |
| :--- | :--- |
| canonical | 0 |
| short-aggregation | 20 |
| alias | 0 |
| ambiguous | 0 |
| misplaced | 0（carbazole-derivatives 为候选，待 Phase G） |
| no-evidence | 0 |

- 本批 20 页全部为无 frontmatter 的短反链聚合页（5-15 行），无正式页。
- 全部页面均有至少 1 篇论文反链，无 no-evidence 页。

## 三、问题清单

### 1. 同 slug 跨层碰撞
- 无新增。Phase A 已知 3 对（1t-phase、bamboo-like-N-CNTs、glassy-carbon）本批无涉及。
- 本批无同 slug 双目录页面。

### 2. 规范化名称重复（语义相同/近义名词）
- `canonical-ensemble` ↔ `nvt-ensemble`（concepts）：NVT 系综即正则系综，语义相同，两页均存在，候选合并/别名待 Phase E/G。
- `canted-antiferromagnetism` ↔ `weak-ferromagnetism`（concepts）：倾斜反铁磁产生弱铁磁，语义高度相关，两页均存在。
- `castellated-electrode` ↔ `interdigitated-electrode`（entities）：同族叉指/城堡电极结构，两页均存在。
- `carrier-tuning` ↔ `charge-doping`（concepts）：载流子调谐与电荷掺杂近义（本批 carrier-tuning 在 concepts，charge-doping 在第 186 页后续批次）。

### 3. 缩写/全称与拼写变体
- `Car-Parrinello` 页「🏷️ 专业名词别名」章节标注 `car-parrinello-method`（concepts）、`car-parrinello`（entities）、`Car-Parrinello`（entities）——经检查均不存在，为悬空别名，待 Phase E 修复或删除标注。
- `carbon-nanotube` 页「🏷️ 专业名词别名」章节标注 `carbon-nanotubes`（entities）——不存在，为悬空别名，待 Phase E 处理。

### 4. 父子概念关系
- `canted-antiferromagnetism` ⊂ `weak-ferromagnetism`（倾斜反铁磁是弱铁磁的微观来源）。
- `carrier-density-modulation` 与 `carrier-mobility` 相关（载流子密度调制影响迁移率）。
- `carrier-tuning` ≈ `charge-doping`（近义，载流子调谐常通过电荷掺杂实现）。

### 5. 歧义词
- 无。本批术语语义均单一明确。

### 6. 跨层误放
- 候选：`concepts/carbazole-derivatives`（咔唑衍生物为具体化合物类别，按类型判定应归 entities，但"衍生物"作为类别概念存争议，标记候选待 Phase G 确认，与 bedt-ttf 案例同类）。

### 7. 无证据页
- 无。本批全部页面均有论文反链。

### 8. 论文反链误聚合/弱相关
- `CADPAC` ← `perdew1996`：PBE 论文仅将 CADPAC 作为实现程序提及，程序实体反链弱相关，需在 Phase D 核实是否保留。
- `capacitive-sensor` / `castellated-electrode` ← `Ismail2015`：ZnO 湿度传感器综述中电容式传感器与电极结构为其中类型/结构，相关但需核实具体上下文后确认贡献句。

## 四、备注
- 本批 20 页全部为 short-aggregation，无 canonical/alias/ambiguous/misplaced/no-evidence 正式判定。
- 悬空别名（Car-Parrinello、carbon-nanotube 两页的别名章节）与 misplaced 候选（carbazole-derivatives）需在后续 Phase E/G 处理。
- 未修改任何页面，未提交，保护集合未触碰。
