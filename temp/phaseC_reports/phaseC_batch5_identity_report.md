# Phase C 第五批身份解析报告（第 171-190 页）

- 批次范围：`Cd3Cl6` → `charge-sloshing`（按 slug.lower() 合并排序）
- 页数：20 页（concepts 15 页、entities 5 页）
- 模式：只读分析，未修改任何页面，未提交
- 日期：2026-08-16

## 一、每页身份判定表

| # | 路径 | 身份类型 | 判定依据（一句话） |
| :--- | :--- | :--- | :--- |
| 171 | entities/Cd3Cl6 | short-aggregation | 5 行仅 1 篇（sunSlidingFerroelectricity2025 滑动铁电综述，Cd3Cl6 为滑动铁电材料），具体材料实体，目录正确 |
| 172 | entities/CdTe | short-aggregation | 5 行仅 1 篇（Mińkowski2021cation CdTe 阳离子间质扩散），具体材料实体，目录正确 |
| 173 | concepts/cdw-blends-displacements | short-aggregation | 5 行仅 1 篇（cossu2024 2H-NbSe2 双层 CDW 堆叠），有效概念，名称有效 |
| 174 | concepts/cdw-mott-phase | short-aggregation | 5 行仅 1 篇（nakata2021 1T-TaSe2/NbSe2 电子关联增强 CDW），有效概念 |
| 175 | concepts/cdw-tronics | short-aggregation | 5 行仅 1 篇（lezoualch TMD CDW 研究），有效概念，与 cew-tronics 拼写变体 |
| 176 | concepts/cellular-automaton | short-aggregation | 6 行 2 篇（Zhang2002b/Zhang2003a 铁素体/奥氏体相变 CA 模型），有效方法概念，反链相关 |
| 177 | entities/cementite | short-aggregation | 6 行 2 篇（Zhang2002b/Zhang2003a，渗碳体为次要对象），具体材料实体，反链弱相关 |
| 178 | concepts/cementite-precipitation | short-aggregation | 6 行 2 篇（同上），有效概念，与 cementite 父子，反链弱相关 |
| 179 | entities/CeTe3 | short-aggregation | 5 行仅 1 篇（Johannes2008fermi 费米面嵌套 CDW，CeTe3 为典型材料），具体材料实体，目录正确 |
| 180 | concepts/cew-tronics | short-aggregation | 5 行仅 1 篇（lezoualch），cdw-tronics 拼写变体，名称有效 |
| 181 | concepts/chadi-cohen-method | short-aggregation | 5 行仅 1 篇（monkhorst1976 特殊点 BZ 积分，Chadi-Cohen 为特殊点方法），有效方法概念，反链相关 |
| 182 | concepts/chaotic-advection | short-aggregation | 5 行仅 1 篇（Unknown2014passive 微混合器，混沌对流为核心机制），有效概念，反链相关 |
| 183 | concepts/charge-density | short-aggregation | 25 行 21 篇无 frontmatter 仅论文列表，名称有效，与 charge-density-wave 父子 |
| 184 | concepts/charge-density-mixing | short-aggregation | 5 行仅 1 篇（kresse1996a 平面波总能量效率，涉及电荷密度混合），有效概念 |
| 185 | concepts/charge-density-wave | **canonical** | 86 行 frontmatter mature，太奶导读/结构概览/机制/相关论文/关联齐全，37 篇论文 |
| 186 | concepts/charge-doping | short-aggregation | 6 行 2 篇（chen3dLevelSymmetry2025/chenFerromagneticNonmagnetic1T2022 电荷掺杂），有效概念，与 carrier-tuning 近义 |
| 187 | concepts/charge-migration-energy | short-aggregation | 5 行仅 1 篇（Jin2015studying BiFeO3 PFM 极化翻转），有效概念，反链弱相关 |
| 188 | concepts/charge-order | short-aggregation | 16 行 8 篇无 frontmatter 仅论文列表+别名章节，名称有效，与 charge-ordered-ferroelectricity 父子 |
| 189 | concepts/charge-ordered-ferroelectricity | short-aggregation | 5 行仅 1 篇（ramesh2007 多铁薄膜综述），有效概念，charge-order 子概念 |
| 190 | concepts/charge-sloshing | **canonical** | 52 行 frontmatter mature，太奶导读/结构概览/机制/相关论文/关联齐全 |

## 二、各类别汇总数量

| 身份类型 | 数量 |
| :--- | :--- |
| canonical | 2（charge-density-wave、charge-sloshing） |
| short-aggregation | 18 |
| alias | 0 |
| ambiguous | 0 |
| misplaced | 0 |
| no-evidence | 0 |

- 本批 2 个 canonical 页（charge-density-wave 86 行、charge-sloshing 52 行）均为 frontmatter mature 正式页，结构完整（太奶导读/结构概览/机制/相关论文/关联概念齐全）。
- 其余 18 页均为无 frontmatter 短反链聚合页（5-25 行），全部有论文反链，无 no-evidence 页。

## 三、问题清单

### 1. 同 slug 跨层碰撞
- 无新增。Phase A 已知 3 对（1t-phase、bamboo-like-N-CNTs、glassy-carbon）本批无涉及。

### 2. 规范化名称重复（语义相同/近义名词）
- `cdw-tronics` ↔ `cew-tronics`（concepts）：拼写变体，两页均存在且反链相同（lezoualch），候选合并/别名待 Phase E/G。
- `cementite`（entities）↔ `cementite-precipitation`（concepts）：父子关系，渗碳体为具体相、渗碳体析出为过程概念，分层合理。
- `charge-order` ↔ `charge-ordered-ferroelectricity`（concepts）：父子关系，电荷有序为一般概念、电荷有序铁电为子概念。
- `charge-density` → `charge-density-wave`（concepts）：父子关系，电荷密度为一般概念、CDW 为电荷密度周期性调制。
- `charge-doping` ↔ `carrier-tuning`（concepts）：近义，电荷掺杂与载流子调谐常互换使用（carrier-tuning 在第 167 页批次）。

### 3. 缩写/全称与拼写变体
- `charge-order` 页「🏷️ 专业名词别名」章节标注 `charge-ordering`（concepts）——经检查不存在，为悬空别名，待 Phase E 修复或删除标注。

### 4. 父子概念关系
- `cementite`（entities）⊃ `cementite-precipitation`（concepts）：渗碳体相 vs 渗碳体析出过程。
- `charge-order` ⊃ `charge-ordered-ferroelectricity`：电荷有序一般概念 vs 电荷有序驱动的铁电。
- `charge-density` ⊃ `charge-density-wave`：电荷密度一般概念 vs CDW 调制序。

### 5. 歧义词
- 无。本批术语语义均单一明确。

### 6. 跨层误放
- 无。本批具体材料（Cd3Cl6/CdTe/cementite/CeTe3）均在 entities，抽象概念均在 concepts，分层正确。

### 7. 无证据页
- 无。本批全部页面均有论文反链。

### 8. 论文反链误聚合/弱相关
- `cementite` / `cementite-precipitation` ← `Zhang2002b` / `Zhang2003a`：两篇论文主题为铁素体/奥氏体相变 CA 模型，渗碳体为次要对象，反链弱相关，需在 Phase D 核实是否保留。
- `charge-migration-energy` ← `Jin2015studying`：论文为 BiFeO3 薄膜 PFM 极化翻转研究，与"电荷迁移能"为间接相关，需核实具体上下文。

## 四、备注
- 本批 20 页中 2 页 canonical（charge-density-wave、charge-sloshing）、18 页 short-aggregation，无 alias/ambiguous/misplaced/no-evidence 正式判定。
- 悬空别名（charge-order 页的 charge-ordering）与弱相关反链（cementite 簇、charge-migration-energy）需在后续 Phase D/E 处理。
- 未修改任何页面，未提交，保护集合未触碰。
