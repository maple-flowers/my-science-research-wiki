---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_07f6d58897e011f19467525400287e28
    ReservedCode1: IhmIlznuCMIrq++pEsAfib9W9r35QPlqDmM+tQi+EpmGngcavgfUkfc8n2NVnKD4ZmrXdErEllKA5Ww7tCEZHXjDPS9pwymYVUmx8wfYsH8NohPxqfViidZkpPhVMg0SUEtow9AR6JZu29ezqAJiG8JG/6vl3pBWSd0hQhbPLhgvRCxSbEmfSjuX2kk=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_07f6d58897e011f19467525400287e28
    ReservedCode2: IhmIlznuCMIrq++pEsAfib9W9r35QPlqDmM+tQi+EpmGngcavgfUkfc8n2NVnKD4ZmrXdErEllKA5Ww7tCEZHXjDPS9pwymYVUmx8wfYsH8NohPxqfViidZkpPhVMg0SUEtow9AR6JZu29ezqAJiG8JG/6vl3pBWSd0hQhbPLhgvRCxSbEmfSjuX2kk=
---



# 研究想法条目编写规范 (Ideas Format Specifications)

> 本文件定义 `wiki/ideas/` 目录下三类条目的编写格式规范。规范总纲（目录约定 / 标签体系 / 链接规范 / 铁律）见 [[SCHEMA]]；concept / entity / paper / figure / write / topic / project 的编写规范见 [[format-spec]]。

[[ideas/_index|← 返回研究想法索引]] · [[科研Wiki/index|← 返回 Wiki 总索引]]

---

## 一、目录定位与使用原则

`wiki/ideas/` 是科研 Wiki 的**研究想法层**，是 concept / entity（"已知知识"）与 project（"正在做的事"）之间的**孵化器**。它记录四件事：

1. **领域空白（gap）**——从论文综述与阅读中发现的"没人做过 / 没做透 / 结论矛盾"的开放问题；
2. **研究想法（idea）**——针对某个 gap 提出的、可验证的假设与方案；
3. **可行性验证（validation）**——对 idea 的验证尝试与结论（支持 / 否定 / 存疑）；
4. **科研范式（paradigm）**——从论文中提炼的"这类研究是怎么做的"，沉淀可复用的研究套路与方法论模板。

**使用原则**：

- **想法是活的**：卡片随验证推进更新 `status` 与「生命周期日志」，不追求一次写全。proposed / draft 阶段允许简短。
- **层级锚定**：每张 idea 必须锚定至少一个 gap（`gap` 字段）；每张 validation 必须锚定一个 idea（`idea` 字段）；每张 paradigm 必须锚定至少一篇代表论文（`papers` 字段）。
- **问题 / 假设 / 证据分离**：gap 只记"问题"，idea 只记"假设与方案"，validation 只记"验证与结论"，paradigm 只记"研究套路与方法"，避免一张卡片混多种内容。
- **落地闭环**：idea 验证通过并被采纳时，`status` 改为 `adopted`，正文双链落地项目 `[[../projects/project-1-two-photon|项目1]]`，并在该项目页回链 idea。验证否定则改 `rejected`，保留页面并写明否定原因，不删除。
- **引用铁律**：本目录任何条目引用论文一律 `[[../papers/<citekey>]]`，**不得**直链 `raw/note/`（全库只有 `wiki/papers/` 可直链 raw）。

---

## 二、条目类型

| `type` | 定位 | 回答的问题 | 文件名前缀 | 状态值 |
| :--- | :--- | :--- | :--- | :--- |
| `gap` | 领域空白 | 还有什么没人做 / 没做透？ | `gap-` | `open` → `filled` |
| `idea` | 研究想法 | 我打算怎么补这个空白？ | `idea-` | `proposed` → `validating` → `validated` → `adopted` / `rejected` / `superseded` |
| `validation` | 可行性验证 | 这个想法到底行不行？ | `validation-` | `draft` → `in-progress` → `done` / `inconclusive` |
| `paradigm` | 科研范式 | 这类研究是怎么做的？ | `paradigm-` | `active` → `superseded` / `obsolete` |

归属判据：

- 描述"现有文献还缺什么、哪两个结论打架、哪个效应没人解释"→ **gap**；
- 描述"我想用 XX 方法做 XX、假设是 XX"→ **idea**；
- 描述"我算了 / 试了 XX，结果是 XX，结论支持 / 否定"→ **validation**；
- 描述"这类研究是先用 XX 预测、再用 XX 合成、最后用 XX 表征验证"→ **paradigm**。
- 若一个想法已被项目正式立项，idea 页只负责记录想法本身，项目进展归属 `wiki/projects/`，不要重复搬运。

---

## 三、命名与 slug

- 文件名 = 类型前缀 + 英文 kebab-case：`gap-<slug>.md`、`idea-<slug>.md`、`validation-<slug>.md`、`paradigm-<slug>.md`。
  - 例：`gap-sliding-ferroelectricity-switching-speed.md`、`idea-strain-tuning-1t-cdw.md`、`validation-vasp-phonon-soft-mode.md`、`paradigm-high-throughput-screening.md`。
- slug 用小写英文、连字符分隔，从标题/核心术语中提炼，控制在 3–8 个词。
- **编号**（可选但推荐）：在 frontmatter 用 `gap_id` / `idea_id` / `validation_id` / `paradigm_id` 记录 `G01` / `I01` / `V01` / `P01` 形式的编号，便于口头引用与排序；编号不是唯一标识，slug 才是。
- frontmatter 中 `gap`（idea 页锚定的 gap）与 `idea`（validation 页锚定的 idea）字段填写**目标文件的完整 slug（含前缀）**，保证 `[[ ]]` 可解析。
- 新建前先 Glob `wiki/ideas/` 确认 slug 是否已存在，避免重复。

---

## 四、Frontmatter 字段

四种卡片共享同一套骨架：**必备四字段** `tags`、`title`、`type`、`status`，其余按类型选择性填写，没有就省略。

### 4.1 gap 卡片

```yaml
---
# ── 必备 ──
tags: [gap, <子标签...>]              # 首元素固定为 gap
title: <中文名 / 英文名>              # H1 纯文本
type: gap
status: open                          # open（空白仍在）| filled（已被 idea/project 填补）

# ── 建议 ──
gap_id: G01                           # 编号，便于引用
domain: [ferroelectricity, 2d-materials]   # 所属学科域，英文 kebab
related_concepts: [<slug>, ...]       # 该空白涉及的概念
related_entities: [<slug>, ...]       # 该空白涉及的材料/实体
related_topics: [<slug>, ...]         # 该空白所属主题（wiki/topics 文件名，不含路径）
papers: [<citekey>, ...]              # 发现该空白的依据论文
updated: 2026-08
---
```

### 4.2 idea 卡片

```yaml
---
# ── 必备 ──
tags: [idea, <子标签...>]             # 首元素固定为 idea
title: <中文名>                       # H1 纯文本
type: idea
status: proposed                      # proposed | validating | validated | adopted | rejected | superseded

# ── 建议 ──
idea_id: I01                          # 编号
gap: [gap-<slug>, ...]                # 锚定的 gap 卡片 slug（含前缀，可多个）
domain: [<学科域>]
hypothesis: <一句话：核心假设>
method: <拟采用的方法/方案，一句话>
related_concepts: [<slug>, ...]
related_entities: [<slug>, ...]
related_projects: [project-N, ...]    # 已关联/落地的项目码（未落地则省略）
papers: [<citekey>, ...]
updated: 2026-08
---
```

### 4.3 validation 卡片

```yaml
---
# ── 必备 ──
tags: [validation, <子标签...>]       # 首元素固定为 validation
title: <中文名>                       # H1 纯文本
type: validation
status: done                          # draft | in-progress | done | inconclusive

# ── 建议 ──
validation_id: V01                    # 编号
idea: idea-<slug>                     # 锚定的 idea 卡片 slug（含前缀，单个）
method: <验证方法：计算/实验/文献调研，一句话>
conclusion: <一句话结论：支持 / 否定 / 存疑>
papers: [<citekey>, ...]
updated: 2026-08
---
```

### 4.4 paradigm 卡片

```yaml
---
# ── 必备 ──
tags: [paradigm, <子标签...>]         # 首元素固定为 paradigm
title: <中文名 / 英文名>               # H1 纯文本
type: paradigm
status: active                        # active | superseded | obsolete

# ── 建议 ──
paradigm_id: P01                      # 编号
domain: [<学科域>]
core_question: <该范式回答的核心科学问题，一句话>
method_pipeline: <方法流水线，如"高通量筛选→DFT验证→实验合成→表征闭环">
related_concepts: [<slug>, ...]
related_entities: [<slug>, ...]
related_topics: [<slug>, ...]
papers: [<citekey>, ...]              # 提炼该范式的代表论文（至少 1 篇）
updated: 2026-08
---
```

**字段规则**：

- `tags` 第一个元素必须与 `type` 一致（`gap` / `idea` / `validation` / `paradigm`），其后加主题标签（`ferroelectric`、`2d-materials`、`charge-density-wave`、`dft` 等）。
- `title` 是 H1 的纯文本，不含 wikilink / 加粗 markdown。
- `gap` / `idea` / `related_concepts` / `related_entities` / `papers` 等 slug 字段必须**真实存在**对应页面，禁止臆造；与正文双链保持一致，是正文关联小节的结构化镜像。
- 编号 `gap_id` / `idea_id` / `validation_id` / `paradigm_id` 在正文 blockquote 中重复一遍（如 `> 科研范式 P01：…`），便于阅读。
- 不写与正文重复的大段描述；frontmatter 是可查询的结构化索引，正文才是叙述主体。

---

## 五、正文结构（统一模板）

四型卡片正文均遵循全库惯例：**H1 中英对照 + emoji H2 固定章节 + 双链引用**。以下为各型模板，其中 `## 👵 太奶导读` 四型均保留（proposed / draft 阶段可三五句）。

### 5.1 gap 卡片模板

```markdown
# <中文名> / <英文名>

> 领域空白 G01：<一句话说明这个空白是什么>

## 👵 太奶导读

<用大白话讲清"这个空白是什么、为什么值得补"。>

## 🕳️ 空白是什么

<具体描述：现有研究做到了哪一步，缺什么、哪两个结论打架、哪个效应没人解释；关键处引用论文。>

## 🎯 为什么值得做

<科学价值或应用价值，2–4 句。>

## 📚 相关论文 (Related Papers)

- [[../papers/<citekey>]]：<可选，一句话说明该论文如何暴露了这个空白>

## 🔗 关联概念、实体与主题 (Related Concepts, Entities & Topics)

- [[../concepts/<slug>|<中文名>]]
- [[../entities/<slug>|<名称>]]
- [[../topics/<slug>|<主题名>]]

## 💡 由此产生的想法 (Ideas Derived)

- [[idea-<slug>|I01 <想法标题>]]：<一句话关系>
```

### 5.2 idea 卡片模板

```markdown
# <中文标题>

> 研究想法 I01：<一句话核心假设>

## 👵 太奶导读

<用大白话讲清"我想干什么、为什么觉得能成"。>

## 🕳️ 针对的空白

- [[gap-<slug>|G01 <空白标题>]]：<为什么这个想法能补这个空白>

## 🧠 核心假设

<hypothesis 展开：可证伪的具体断言，2–4 段，关键处引用论文。>

## ⚙️ 拟采用的方法 / 方案

<计算 / 实验 / 数据方案，说明可行性与关键步骤。>

## 🔬 验证记录

- [[validation-<slug>|V01 <验证标题>]] — <一句话结论>（尚无验证时写"待验证"）

## 📚 相关论文 (Related Papers)

- [[../papers/<citekey>]]：<可选，一句话贡献>

## 🔗 关联概念、实体、主题与项目 (Related Concepts, Entities, Topics & Projects)

- [[../concepts/<slug>|<中文名>]]
- [[../entities/<slug>|<名称>]]
- [[../topics/<slug>|<主题名>]]
- [[../projects/project-1-two-photon|项目1：双光固化和双光发光]]（仅 `adopted` 落地后添加）

## 📈 生命周期日志

- **<YYYY-MM-DD>**: proposed — <提出缘由>
- **<YYYY-MM-DD>**: validating — <开始何种验证>
- **<YYYY-MM-DD>**: adopted — 落地为 [[../projects/project-1-two-photon|项目1]]
```

### 5.3 validation 卡片模板

```markdown
# <中文标题>

> 可行性验证 V01：<一句话结论>

## 👵 太奶导读

<用大白话讲清"我做了什么实验/计算、结果说这个想法成不成"。>

## 🎯 验证对象

- [[idea-<slug>|I01 <想法标题>]]：<验证它的哪一个假设>

## ⚙️ 验证方法

<计算协议 / 实验方案 / 文献调研范围；给出关键参数。>

## 📊 结果与证据

<关键数据、图表或引用论文；数值带单位。>

## ✅ 结论

<支持 / 否定 / 存疑，以及下一步建议。若否定，明确说明"此路不通"的原因。>

## 📚 相关论文 (Related Papers)

- [[../papers/<citekey>]]：<可选，一句话贡献>

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/<slug>|<中文名>]]
- [[../entities/<slug>|<名称>]]
```

### 5.4 paradigm 卡片模板

```markdown
# <中文名> / <英文名>

> 科研范式 P01：<一句话概括这个研究套路>

## 👵 太奶导读

<用大白话讲清"这类研究是怎么一步步做出来的"，生活化比喻开头。>

## 🧭 范式概述

<这个范式的核心逻辑：研究对象、总体思路、为什么这样设计；关键处引用论文。>

## 🔁 研究流程

1. **步骤一**：<做什么，用什么方法>
2. **步骤二**：<做什么，用什么方法>
3. **步骤三**：<做什么，用什么方法>

## 🛠️ 核心方法与工具

- <方法 / 工具>：<作用>

## ✅ 适用条件

<什么类型的问题适合用这个范式；需要哪些前提条件（数据、算力、实验平台等）。>

## ⚠️ 局限与风险

<这个范式的边界、常见坑、失败模式。>

## 📚 代表论文 (Representative Papers)

- [[../papers/<citekey>]]：<该论文如何体现此范式>

## 🔗 关联概念、实体与主题 (Related Concepts, Entities & Topics)

- [[../concepts/<slug>|<中文名>]]
- [[../entities/<slug>|<名称>]]
- [[../topics/<slug>|<主题名>]]

## 📈 生命周期日志

- **<YYYY-MM-DD>**: active — <提炼自哪些论文 / 缘由>
- **<YYYY-MM-DD>**: superseded — <被哪个新范式替代>
```

---

## 六、正文写作要点

- **H1 中英对照**：gap / validation / paradigm 用 `# <中文名> / <英文名>`；idea 可用纯中文或中英对照。
- **H2 一律带 emoji 且不编号**，与全库风格一致；固定小节用固定名（`## 👵 太奶导读`、`## 📚 相关论文 (Related Papers)`、`## 🔗 关联…`）。
- **正文引用论文一律 `[[../papers/<citekey>]]`**，从 `wiki/ideas/` 出发的相对路径；概念用 `[[../concepts/charge-transfer|概念]]`，实体 `[[../entities/MAX-phase|实体]]`，主题 `[[../topics/多铁性材料|主题]]`，项目 `[[../projects/project-1-two-photon|项目]]`。
- **同目录互链不加路径前缀**：`[[gap-<slug>|G01 …]]`、`[[idea-<slug>|I01 …]]`、`[[validation-<slug>|V01 …]]`、`[[paradigm-<slug>|P01 …]]`。
- **落地回链**：idea `adopted` 后，除 idea 页链项目外，在对应 project 页「与科研 Wiki 知识库的联系」小节加一行 `- **相关想法**：[[../ideas/idea-<slug>|I01 <想法标题>]]`（从 `wiki/projects/` 出发）。
- **👵 太奶导读**：与 concept / entity 同款要求——一个生活化比喻开头、顺着比喻讲完道理、术语逐个翻译成中文白话、3–6 句、不堆公式与数值。gap 讲"为什么这块地还空着"，idea 讲"我打算怎么在这块地上盖房子"，validation 讲"我试了试，地基牢不牢"，paradigm 讲"别人是怎么盖这类房子的、我能不能照着盖"。
- **生命周期日志**：只记状态转折（idea：proposed → validating → validated → adopted / rejected / superseded；paradigm：active → superseded / obsolete），每条一行 `**<YYYY-MM-DD>**: <新状态> — <说明>`，按日期倒序或正序均可，但同一页保持一致。
- **不堆砌弱相关链接**：gap / idea / validation / paradigm 的关联小节只链真正有机制 / 家族 / 证据关系的条目，不写全库大而全的列表。
- 不保留 Zotero 元数据表、AI 转写、转换日志等噪音。

---

## 七、生命周期与状态迁移

| 卡片 | 状态迁移 | 触发条件 |
| :--- | :--- | :--- |
| gap | `open` → `filled` | 已有 idea 或 project 实质性填补该空白 |
| idea | `proposed` → `validating` | 开始做计算 / 实验 / 文献验证 |
| idea | `validating` → `validated` | 验证通过，想法被证明可行 |
| idea | `validated` → `adopted` | 被采纳并落地为 `wiki/projects/` 项目 |
| idea | `validating` / `validated` → `rejected` | 验证否定，想法废弃（保留页面写明原因） |
| idea | 任意 → `superseded` | 被更新的 idea 替代（保留页面并链向新 idea） |
| validation | `draft` → `in-progress` | 开始验证工作 |
| validation | `in-progress` → `done` / `inconclusive` | 验证得出明确结论 / 无定论 |
| paradigm | `active` → `superseded` | 被更新的范式替代（保留页面并链向新范式） |
| paradigm | `active` → `obsolete` | 范式过时废弃（保留页面写明原因） |

**迁移规则**：

- 状态迁移时同步更新 frontmatter 的 `status` 与正文「生命周期日志」（idea / paradigm 页），并确保双链跟上（如 `adopted` 时补项目双链）。
- `rejected` / `superseded` / `obsolete` **不删除页面**：负结果与替代关系也是知识资产，保留供后来者查阅。
- gap 被 `filled` 后不删除，把 `status` 改为 `filled`，并在「由此产生的想法」小节链向填补它的 idea / project。

---

## 八、铁律速查

- 引用论文一律 `[[../papers/<citekey>]]`，**不得**直链 `raw/note/`；只有 `wiki/papers/<citekey>` 可直链 raw。
- `tags` 首元素、`type`、文件名前缀三者必须一致（gap / idea / validation / paradigm）。
- idea 必须有 `gap` 字段锚定至少一个 gap；validation 必须有 `idea` 字段锚定一个 idea；paradigm 必须有 `papers` 字段锚定至少一篇代表论文。
- 所有 slug / citekey 必须真实存在，禁止臆造；新建前先 Glob 查重。
- `rejected` / `superseded` / `filled` / `obsolete` 不删页，只改状态并写明原因。
- 负结果（`rejected`）如实记录，不美化、不隐藏。
- 想法落地为项目后，进展记录归属 `wiki/projects/`，idea 页只保留想法与验证结论，不重复搬运转录项目日志。
*（内容由AI生成，仅供参考）*
