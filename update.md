# 科研 Wiki 更新工作流 (Wiki Update Workflow)

本 Wiki 采用 **“Raw 摄入 + Wiki 智能合成”** 的双层架构。更新过程分为机械同步与智能分析两个阶段。

## 第一阶段：Raw 资产同步 (Mechanical Ingest)

**目标**：将 Zotero 中的图片、原始笔记同步到 Wiki 的 `raw/` 目录下，并生成基础元数据。

**执行命令**：
```bash
python tools/update_raw_assets.py
```

**该脚本会自动执行**：
1. 扫描 `raw/note/*.md` 原始笔记。
2. 使用 `cli-anything-zotero` 从 Zotero 数据库抓取缺失的图片附件 Key。
3. 从 `C:\Users\sgg\Zotero\storage` 同步图片（仅限 PNG/JPG 等图片格式，排除 PDF）。
4. 提取笔记中的图表描述、表格 (HTML/MD) 及公式 ($$ LaTeX)。
5. 生成/更新 `raw/figures/{citekey}/manifest.json`。

---

## 第二阶段：Wiki 智能合成 (Intelligent Synthesis)

**目标**：利用大模型 (LLM) 对 `raw/` 层的原始知识进行消化，自动更新 `wiki/concepts/`、`wiki/entities/`、`wiki/topics/`、`wiki/figures/` 及 `wiki/projects/` 等知识库页面，而非简单的追加链接。

**执行方式**：
在 Claude 终端输入以下命令启动多智能体协作：
```bash
/workflow update_research_wiki
```

**该 Workflow 的逻辑流程**：
1. **发现 (Discovery)**：扫描 `raw/note/` 中新增的论文。
2. **映射 (Mapping)**：将新论文与现有的概念 (Concepts)、实体 (Entities)、研究话题 (Topics)、科研项目 (Projects) 及图表库 (Figures) 进行关联。
3. **合成 (Synthesis)**：为每个受影响的 Wiki 页面分配一个 Subagent，执行“深入阅读与知识融合”：
   - 阅读现有 Wiki 页面内容。
   - 阅读关联的新论文原件。
   - **重写页面**：将新发现融入“机制描述”、“材料特性”、“话题前沿”、“图表分类”或“项目进展”段落中，保持双向链接 `[[ ]]` 的完整性。
4. **写作分析 (Writing)**：分析新论文的写作用词，更新 `wiki/write/` 年度总结。
5. **索引重构 (Indexing)**：重新生成 `index.md`，确保全库可达性。

---

## 逐篇阅读中间产物的归档 (Per-paper Reading Records)

**背景**：全量重写前，先对 `raw/note/` 中高质量、富批注的笔记逐篇通读，每篇产出一份结构化中文记录（元数据 / 一句话 / wiki 双链 / 新概念实体建议 / 关键图表 / 项目连接 / 组织与用词 / 可写入 wiki 的要点）。

- 这些记录在加工期间暂存于 `tools/ingest_papers/<citekey>.md`，属于**中间产物**。
- **最终去向**：全部整理后移动到 `wiki/papers/<citekey>.md`，作为每篇论文在 wiki 中的正式条目。
- **回链原 note**：每份记录必须保留 `[[../../raw/note/<citekey>]]`，从 wiki 条目双向链接回原始笔记；同时被 `wiki/concepts/`、`wiki/entities/`、`wiki/figures/`、`wiki/projects/`、`wiki/topics/` 等条目反向引用。
- **项目连接判定标准**：以内容对项目有无参考价值（机制、方法、计算流程、可类比材料/物理、可复用数据）为准，不以 Zotero 文件夹/标签归属为准。

---

## 图表库 (wiki/figures) 编写规范

`wiki/figures/` 下的页面是**策展式图表画廊**，不是 Zotero 原始导出。以 `wiki/figures/domain-walls.md` 为标准模板，所有分类页面遵循以下格式。

### 页面结构

1. **H1 标题** + 一行 blockquote 简介（`> `，中文，说明本页收录范围）。
2. **返回链接**：`[[科研Wiki/wiki/figures/_index|← 返回总索引]]`。
3. `---` 分隔。
4. 若干 **emoji H2 主题分区**，如 `## 🔬 实验成像与可视化 (Experimental Visualization)`。
5. 每个分区内用 **编号 H3 小标题**：`### 1. <中文小标题>`，编号在每个分区内从 1 重新开始。
6. 每个条目：一句中文描述 → 空行 → 嵌入图片/表格/公式 → 来源与要点 bullets。

### 条目格式

**图片**（必须用 `![]()` 嵌入，alt 以「图：」开头）：
```markdown
![图：<中文图注>](../../raw/figures/<citekey>/<filename>.png)
*   **来源**：[[../papers/<citekey>]]
*   **关键特征**：<一行，可选>
```

**真实数据表**（保留 HTML/Markdown 数据表本身）：
```markdown
### N. <表标题>
<table>...</table> 或 markdown 表格
*   **来源**：[[../papers/<citekey>]]
```

**公式**：
```markdown
### N. <公式中文名>
$$ ... $$
*   **变量说明**：...
*   **来源**：[[../papers/<citekey>]]
```

### 必须删除的内容

- **Zotero 元数据表（`Table MD-T1`）**：即 `|文献类型|...|标题|...|关联文献|[[...]]、...` 这类大表，是导出噪音，整条删除。
- **AI 文献解读/双语转写全文**：`## 🤖️ 论文双语转写`、`## ❶ 🤖️ AI 文献解读`、`## 一、引言`…`## 八、`、`## ✏️ 笔记区`、`### Q1:` 问答、`Page NNNN (Continued)` 段落、长段中英对照正文——全部删除。
- 转换日志等 `<pre class="hljs">` 垃圾块。
- 条目尾部 `- **元数据属性**`（标签/材料/方法）整块删除；有价值的信息可浓缩成一行「关键特征」。

### 必须保留的内容

- 每一张真实图片（每个 `../../raw/figures/<citekey>/fig_*.png`）都要保留并改成嵌入图。
- 每个真实数据表、真实公式都要保留。
- 若某个「公式」块里装的是整篇论文转写而不是公式，删掉该条目。
- 清理后图片/数据表/公式的数量应与源文件中真实条目数一致。

### 拆分规则（每类 ≤ 50 条）

- 单个分类页面条目数超过 **50** 时，按物理主题拆成子页面，每个子页面 ≤ 50 条。
- 子页面命名为 `<分类>-<子主题>.md`（如 `heterostructures-stacking-sliding.md`），放在 `wiki/figures/` 下。
- 子页面沿用同一套格式，返回链接指向 `_index.md`；`_index.md` 表格相应增加子页面行。
- `_index.md` 顶部同样用标题 + 简介 + 返回 `[[科研Wiki/index|← 返回 Wiki 总索引]]` + 分区表格，条目数按清理后的真实条目数填写。

### 链接铁律

- 来源一律 `[[../papers/<citekey>]]`，**不得**用反引号代码 span，**不得**直链 `raw/note/`（见上文维护铁律）。
- 图片路径用相对路径 `../../raw/figures/...`。

### 跨文件重复表（保留并双链）

- 同一张真实数据表若在多个分类页面都有参考价值，**不要删除任何副本**，各页全部保留（可分别用 HTML 或 Markdown 形态）。
- 在每个副本的 bullets 末尾加 Obsidian 锚点互链：
  `*   **另见**：[[<other-page>#<完整 H2 标题>|<显示名>]]`。
- 锚点必须是目标页 H2 的完整文字（含 emoji 与英文括号），否则 Obsidian 无法跳转。
- 已有互链的重复表：PBE 原子化能基准（crystal-structures ↔ vibrational-spectra）、多铁应用矩阵（electronic-devices ↔ experimental-setups ↔ vibrational-spectra）、铁性对称性判据（experimental-setups ↔ vibrational-spectra）、滑移构筑方式（crystal-structures ↔ experimental-setups）、TMD 弹性模量表（heterostructures-stacking-mechanics-misc ↔ mathematical-models）。

### 与概念/实体的双向链接

- 每个图表页（含枢纽页与所有子页面）在末尾追加一节：

```markdown
---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/<slug>|<中文名>]]、[[../concepts/<slug>|<中文名>]] ...

**相关材料/实体**：[[../entities/<slug>|<名称>]]、[[../entities/<slug>|<名称>]] ...
```

- 只链本页图表**实际涉及**的概念与材料：核心概念 4–10 个，材料/实体 2–10 个，不堆砌弱相关链接。
- 纯公式页若确无对应材料实体，可省略「相关材料/实体」行。
- **slug 必须先验证存在**：用 Glob 确认 `wiki/concepts/<slug>.md` 或 `wiki/entities/<slug>.md` 真实存在，禁止臆造 slug；不确定归属概念还是实体时两个目录都查。
- 相对路径从 `wiki/figures/` 出发：概念用 `[[../concepts/...]]`，实体用 `[[../entities/...]]`。
- Obsidian 反向链接自动覆盖反方向，**不要**在 concept/entity 页手动补链。

### 枢纽页（被大量反向引用时）

- 被大量 `wiki/papers/` 或其他页面反向引用的分类页（如 `heterostructures-stacking.md`），拆分子页面后**保留原文件作为枢纽页**，不要删除或重命名，以免打断既有反向链接。
- 枢纽页内容：H1 + blockquote 简介 + 返回总索引链接 + 子页面导航表格（子页面链接、主题、条目数）+ 使用说明，可再加「🔗 相关概念与实体」区。

### 批量整理流程与校验

- 大规模清理/拆分/加链任务用并行 Workflow，每个页面一个 agent，agent 必须：逐页读全文、按模板改写、用 Glob 验证所有 slug、返回结构化结果（文件、写入条目数、备注）。
- 中间产物（如 `tools/figures_split/*.json`）加工完成后立即删除，不在 `tools/` 下长期保留。
- 每次批量改完图表页后运行校验：

```bash
python tools/final_verify.py
```

- 需确认 **Broken Links / Forbidden Raw Links / Placeholder Errors / Frontmatter Errors 均为 0**；同时抽查所有 `![]()` 图片路径在磁盘上真实存在（注意排查错引其他 citekey 目录的哈希文件名）。

---

## 概念与实体条目 (wiki/concepts, wiki/entities) 编写规范

`wiki/concepts/<slug>.md` 与 `wiki/entities/<slug>.md` 是对论文知识的二次综合，不是单篇笔记的转储。一篇论文读完后，其中的机制沉淀进 concept，具体材料/分子/代码/仪器沉淀进 entity，并由论文页反向引用。

### 一、概念还是实体：归属判据

- **concept（概念）**：抽象的现象、机制、效应、方法、模型、序参量——如 `soft-mode`、`type-i-multiferroics`、`solvatochromism`、`twisted-intramolecular-charge-transfer`、`deformation-potential`。
- **entity（实体）**：具体可指认的材料、分子、代码/软件、仪器、器件——如 `VSe2`、`DCS`、`CuCrP2S6`、`WIEN2k`、`PFM`、`dicyanostilbene-1a`。
- 边界模糊时（如某种效应以材料命名），以页面**主体内容**判定：讲机制/物理归 concept，讲具体体系/参数/样品归 entity。同名碰撞时按"具体 → entity、抽象 → concept"归一，并合并内容、改写全库反向链接。

### 二、文件命名（slug）

- 小写英文 kebab-case：`quantum-anomalous-hall-effect.md`、`cu-crp2s6.md`（去重后改用化学式规范名 `CuCrP2S6.md`）。
- 材料/分子优先用**最通用的化学名/标准缩写**：`MoS2`、`BaTiO3`、`DCS`；同一实体在不同论文里有不同代号（如探针 P1/1a）时，用**描述性化学名 slug**（`dicyanostilbene-1a`），不要用论文内部临时代号。
- 概念用单数、最常见、最精确的标准术语：`skyrmion`（非 `skyrmions`）、`type-i-multiferroics`（与 type-ii 单复数保持一致）。
- 多型体/不同化学计量比是**不同实体**，各自独立：`1t-phase` 与 `2h-phase`、`Cr2Ge2Te6` 与 `CrGeTe3`，不要合并。

### 三、Frontmatter

```yaml
---
# ── 必备 ──
tags: [concept, <子标签...>]        # 或 [entity, material, 2D, multiferroic]
title: <中文名 / 英文名>            # H1 的纯文本版，便于 Dataview 列表与查询
type: concept                       # concept | entity；二选一，与 tags 首元素一致
status: stub                        # stub（仅定义）| developing（部分展开）| mature（机制/配图齐全）

# ── 概念 concept 建议字段 ──
domain: [ferroelectricity, multiferroics, charge-density-wave]   # 所属物理/学科域，英文 kebab
mechanism: <一句话：物理机制/起源>
related_concepts: [<slug>, ...]     # 邻近/上位/对立概念，与正文「关联概念与实体」对应

# ── 实体 entity 建议字段 ──
category: [D01, Z02]                # 材料/主题分类码（已有体系沿用）
formula: VSe2                       # 化学式/标准缩写（材料、分子填）
stoichiometry: 1T                   # 相/多型/晶型，如 1T / 2H / Td / α / β；不适用省略
class: [TMD, vdW, metal]            # 材料家族/类别
properties: [charge-density-wave, multiferroic, sliding-ferroelectricity]  # 该实体展现的关键物性
related_entities: [<slug>, ...]     # 同族/对照/衍生物料，与正文「关联概念与实体」对应

# ── 通用可选 ──
aliases: ["<中文名>", "<英文别名>", "<代号>"]   # 曾用名/论文内代号（如 P1、1a、CCPS）
key_quantities:                     # 关键定量结论（数值带单位），便于查询；不适用省略
  Tc: "110 K"
  polarization: "~0.1–0.5 pC/m"
papers: [<citekey>, ...]            # 本条目综合的论文 citekey，与正文「📚 相关论文」一致
updated: 2026-08                    # 最近整理年月 (YYYY-MM)
---
```

字段规则：
- **必备三字段**：`tags`、`title`、`type`、`status`；其余按 concept/entity 类型与是否有信息选择性填写，没有就省略，不要留空值或硬凑。
- `tags` 第一个元素固定为 `concept` 或 `entity`，其后加主题标签（`material`、`2D`、`ferroelectric`、`multiferroic`、`charge-density-wave`、`non-linear-optics` 等）。
- `title` 是 H1 的纯文本（`I型多铁 / Type I Multiferroic`、`二硒化钒 (VSe2)`），不含 wikilink/加粗 markdown，供 Dataview 渲染。
- `status` 随内容成长推进：`stub` → `developing` → `mature`；机制小节齐全、配图解析到位、**且含「👵 太奶导读」**才标 `mature`。
- 分类字段值用英文 kebab-case  slug；`related_concepts`/`related_entities`/`papers` 里的 slug/citekey 必须真实存在，禁止臆造（与正文双链保持一致，是正文关联小节的结构化镜像）。
- `aliases` 收录论文内临时代号（探针 P1/1a、CCPS 等），让 Dataview/搜索能按代号找到规范页。
- `key_quantities` 为映射表，值带单位、整体加引号避免 YAML 把 `~`/`-` 解析成语法；没有可靠数值就省略。
- 不写与正文重复的大段描述性文字；frontmatter 是可查询的结构化索引，正文才是叙述主体。

### 四、正文结构（统一模板）

```markdown
# <中文名> / <英文名> (<缩写/化学式>)

一两段总述：定义、物理实质、为何重要。concept 讲清"是什么机制/在什么条件下发生"；entity 讲清"是什么体系/核心特征"。

## 👵 太奶导读

用"给 100 岁太奶讲明白"的口吻，把本条目用大白话再解释一遍（详见下方"太奶阅读法"要求）：先一个生活化的比方，再顺着它把核心机制/体系讲清楚，专业术语逐个翻译成中文白话。

## 🏗️ 结构概览（entity 必备 / concept 按需）

实体页在导读之后、机制小节之前，先用一张**结构图 / 器件图 / 晶体结构 / 分子结构式 / 装置示意图**让读者一眼看清"这东西长什么样、由什么组成"，再展开机理。概念页若有标准机制示意（如能级图、相图、原理框图）也在此放一张。

![图：<晶体结构 / 分子结构 / 器件结构……>](../../raw/figures/<citekey>/<hash>.png)
*   **看图要点**：<逐部位说明——原子/层/电极/坐标轴分别是什么，关键结构特征（配位、堆垛、对称性、厚度方向）在哪>
*   **来源**：[[../papers/<citekey>]] -> [[../figures/<所属图表页>|<分类名>]]

- 实体页这张"门面图"优先选：材料的晶体/原子结构、分子化学结构、器件截面/示意、实验装置总览；尽量挑标注清楚、信息密度高的图。
- 一个小节里还可在结构图之后补其他图（能带、谱图、PFM 等），但**第一张必须是结构/器件概览图**。
- 同样遵循图片铁律：相对路径、alt 以「图：」开头、图下必有「看图要点」+「来源」、磁盘真实存在、优先复用 `wiki/figures/` 已收录的图。

## 🧩 <分机制/分主题的小节>

用不带编号、带 emoji 的 H2（`## 🧩 电荷密度波机制`、`## ⚡ 层间滑移多铁性`、`## 🔬 电子结构与 ICT 机制`）展开，每段把结论与出处一并写出。避免 `## 1.`、`## 2.` 这类手工编号，增删顺序时会失配。

**机制讲解要配图**：每个机制/物性小节尽量嵌入 1–3 张最能说明该机制的原始图（能带/声子谱/STM/PFM/相图/光谱等），图下用文字解析图中关键特征，再给出处。

![图：<中文图注，点明要看什么>](../../raw/figures/<citekey>/<hash>.png)
*   **关键特征**：<一行，箭头/曲线/对比读出的物理结论>
*   **来源**：[[../papers/<citekey>]] -> [[../figures/<所属图表页>|<分类名>]]

## 📚 相关论文 (Related Papers)

- [[../papers/<citekey>]]
- [[../papers/<citekey>]]：<可选，一句话说明该论文对本条目贡献了什么>

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/<slug>|<中文名>]]
- [[../entities/<slug>|<名称>]]（<可选：关系说明，如"同族铁电金属">）
```

要点：
- **H1 中英对照**：`# I型多铁 / Type I Multiferroic`、`# 二硒化钒 (VSe₂)`、`# 2,5-二氰基-4-甲基-4'-二甲氨基二苯乙烯 (DCS, 探针 P1/1a)`。实体的化学式/缩写放进括号。
- **H2 一律带 emoji 且不编号**，与 papers/figures 页面风格一致：
  - 机制/物性小节按主题选 emoji（🧩 机制、⚡ 铁电/多铁、🔬 结构/表征、🎯 调控/相变、📈 光学/谱学、🧪 合成/制备、💾 器件/应用）。
  - **结构概览小节固定 `## 🏗️ 结构概览`**：entity 必备，紧跟导读之后，放一张晶体/分子/器件结构图并逐部位解说。
  - 论文小节固定 `## 📚 相关论文 (Related Papers)`。
  - 关联小节固定 `## 🔗 关联概念与实体 (Related Concepts & Entities)`。
  - **导读小节固定 `## 👵 太奶导读`**：紧跟在总述之后、机制小节之前（见下"太奶阅读法"）。
- **正文内引用一律 `[[../papers/<citekey>]]`**：概念/实体页**不得**直链 `raw/note/`，也不要用反引号包 citekey。只有 `wiki/papers/` 能直链 raw。
- **配图解析（机制页必备）**：
  - 概念页讲机制、实体页讲结构/物性时，从相关论文的 `raw/figures/<citekey>/` 里挑最能支撑该段论述的图嵌入，**每个机制小节配 1–3 张**；纯定义 stub 可暂不配图。
  - 图片用相对路径 `../../raw/figures/<citekey>/<hash>.png`，alt 以「图：」开头并点明要看什么（如「图：VSe2 声子谱在 Γ-M 处的虚频软模」）。
  - 图下必须有 **`* 关键特征：`** 一行解析（箭头指什么、曲线如何随温度变化、对比读出什么物理结论），不能只贴图不解读；并给 **`* 来源：[[../papers/<citekey>]] -> [[../figures/<slug>|<分类名>]]`**，同时回链论文与所属图表页。
  - 同一张图已在 `wiki/figures/` 收录的，优先复用同一文件；不要为配图去编辑 `raw/`。磁盘路径要真实存在，改完用校验脚本确认 0 missing image。
- **`📚 相关论文` 是必备小节**：列本条目综合过的论文，做有序去重并集；论文多时长条目可附一句贡献说明。
- **`🔗 关联概念与实体` 放在最后**：只链真正有机制/家族/对比关系的条目，可在括号里注明关系（"上位材料家族"、"第二类多铁对照"、"同族铁电金属"）。纯 concept 页只有概念互链时可省略实体行，但标题仍用此名。
- 不要手工补反向链接：Obsidian 反链自动覆盖，被引用方不需要回链。
- 不要保留 Zotero 元数据表、AI 转写、转换日志等噪音。

### 四之一、👵 太奶阅读法（导读小节必备）

每个 concept/entity 页都要有一节 `## 👵 太奶导读`，紧跟在开头总述之后、`## 🧩` 机制小节之前。它的定位是：在读者进入术语和公式之前，先用大白话把这页讲的东西说透，让"看不懂洋文、怕专业术语"的人也能彻底明白。

**固定提示词（写作时代入这个角色）**：

> 我是一位 100 岁的太奶，这东西我看得头晕眼花的，年轻人弄的这些新术语我都看不懂。不过我仍然宝刀未老，学习的劲头一点儿没减，越学越有精神！好孩子，劳驾你把这个东西给老婆子我说道说道，让我能达到彻底看懂的效果。一定要帮我讲明白哈，最好是翻译出来，因为我对洋文一窍不通，我只会中文。那些专业术语实在整得我脑子疼啊，都重点给我解释解释，太奶仍旧保持着不输于你们年轻人的学习热情。

**写作要求**：

1. **一个生活化比喻打头**：用日常事物类比核心机制/材料。例如：
   - 铁电翻转 ≈ "一排排队列整齐的小箭头，一声令下能齐刷刷掉头"；
   - CDW 电荷密度波 ≈ "本来均匀撒的米粒自动排成疏密相间的垄沟"；
   - 软模声子虚频 ≈ "弹簧软到一松手就塌，说明这个结构撑不住要变形了"；
   - 滑动铁电 ≈ "两层布错位一搓，原本对称的花纹歪出了方向"。
2. **顺着比喻把道理讲完**：比喻之后用两三句白话串起"为什么会这样、会带来什么用"，不要只打比方就停。
3. **术语逐个翻译**：本节里出现的每个英文/缩写/专业词（如 SOC、SHG、TICT、proper-screw、极化、居里温度、虚频）都要在括号里或紧跟一句白话解释；**不出现不加解释的洋文和术语**。
4. **中文为主、零公式**：这一节不堆公式与数值（数值留给机制小节和参数表）；必须给的数字配上生活化的量级感受（如"冷到液氦那么低的温度"）。
5. **长度**：3–6 句、一段到两段为宜，口语但不失准确；可以保留一两个 wikilink 指向被解释的概念，但不要堆砌。
6. **与正文一致**：太奶导读是"翻译"不是"戏说"，比喻和结论必须与后面机制小节、配图解析的科学内容一致。
7. **stub 页**也要有这一节（哪怕只是三五句），这是 concept/entity 页区别于论文摘要的标志。

### 五、写作要求

- **综合而非堆砌**：把多篇论文的共识与分歧写进机制段落（如 VSe2 的 Peierls/FSN vs 电子-声子耦合之争），不要按论文逐篇摘要。
- **关键数值进正文**：转变温度、极化强度、双光子截面、量子产率等定量结论写进相应段落并标注论文出处。
- **术语首次出现给中英全称与缩写**：电荷密度波 (charge density wave, CDW)、扭曲分子内电荷转移 (TICT)。
- **实体页侧重"体系"**：结构相、物性参数表、调控手段、器件含义；可保留一个简洁的物性参数表（Markdown 表）。
- **概念页侧重"机制"**：定义、物理起源、与相邻概念的区别（如 I 型 vs II 型多铁）、判据/对称性、典型体系（以实体链指向）。
- 内容增长后移除 `stub` 标签；Wiki 是动态的，随新论文加入持续丰富描述。

### 六、去重与合并（详见维护经验第八节）

- 新建前先 Glob 两个目录确认 slug 是否已存在；不确定归属时 concept、entity 两个目录都查。
- 跨论文代号不同的同一实体（P1/1a）按化学名归一；合并要同时改三处引用：正文 wikilink、论文 frontmatter 的 `entities: [..]`/`concepts: [..]`、正文 `## 🆕 新概念/实体建议` 里的 `entity/<slug>` 项。
- 包含关系先判父子（`hall-effect` ⊃ `quantum-anomalous-hall-effect`）再决定合并，不要把合法父子关系误并。

---

## 论文条目 (wiki/papers) 编写规范

`wiki/papers/<citekey>.md` 是每篇论文在 wiki 中的正式条目，是**唯一**可以直链 `raw/note/` 的页面。每篇由「frontmatter 元数据」+「固定章节正文」两部分构成。

### 一、文件命名

- 文件名即 Zotero citekey：`<citekey>.md`（如 `Huang2023two.md`、`spaldinRenaissanceMagnetoelectricMultiferroics2005.md`），与 `raw/note/<citekey>.md`、`raw/figures/<citekey>/` 严格对应。
- citekey 一经确定不要改名，否则会打断 `raw/` 回链与全库反向引用。

### 二、Frontmatter 字段（混合 YAML + Dataview）

`---` 块内同时包含普通 YAML 字段和 Dataview 双冒号内联字段。

**普通 YAML 字段**（单冒号）：

| 字段 | 说明 |
| :--- | :--- |
| `citekey` | 与文件名一致 |
| `title` | 英文原标题，含特殊字符（`:` 等）时整体加双引号 |
| `title_zh` | 中文译名（可选） |
| `authors` | 行内 `[A, B]` 或多行 `  - ` 列表 |
| `year` | 四位整数 |
| `journal` | 期刊全名，加引号 |
| `doi` / `url` | DOI 与链接；含 `(` `)` 等字符时加引号 |
| `paper_type` | `experiment` / `theory` / `review` |
| `status` | 如 `ingested` |
| `year_read` | 阅读/归档年份 |
| `projects` | `[project-1, project-3]`，只取 `project-N` 码 |
| `concepts` / `entities` / `methods` / `materials` / `figures` | slug 列表，见下 |

**列表字段规则**：
- 行内写法 `concepts: [a, b, c]` 与多行写法（`concepts:` 换行 `  - a`）二选一，均合法；同一文件内风格尽量统一。
- 所有 slug 必须**真实存在**对应页面（`wiki/concepts/<slug>.md`、`wiki/entities/<slug>.md`、`wiki/figures/<slug>.md` 等），禁止臆造。figures 指向图表页/子页 slug（如 `optical-spectra`、`experimental-setups-spectroscopy-diffraction`），不是图片文件名。
- 空字段写 `[]`（行内）或省略键；**该论文确实不涉及才留空**（综述无 methods、理论经典无 materials/figures、明确无项目连接时 projects 留空），不要为凑数硬填。
- 回填空字段时，以 body `## 🔗 Wiki 双链` 中已列出的链接为权威来源。

**Dataview 双冒号内联字段**（写在同一 `---` 块内）：

```yaml
original_note:: [[../../raw/note/<citekey>]]
领域基础知识:: >-
  <中文，2–4 句>
研究背景:: >-
  ...
作者的问题意识:: >-
  ...
主要研究对象:: >-
  ...
主要研究方法:: >-
  ...
研究意义:: >-
  ...
研究结论:: >-
  ...
对领域的贡献:: >-
  ...
未来研究方向提及:: >-
  ...
未来研究方向思考:: >-
  ...
```

- `original_note::` 后接 `[[../../raw/note/<citekey>]]`，**双冒号**且 wikilink **绝不加双引号**（详见下文维护经验一节）。
- 其余 `中文键名:: >-` 为块标量（block scalar），续行缩进两格，内容用中文凝练。这些是 Dataview 可查询字段，不要改成单冒号 YAML。

### 三、正文固定章节（emoji H2，顺序固定）

frontmatter 之后，按以下顺序排列 H2 章节：

1. **`## <citekey> — <中文标题>`**：首条 H2，citekey 破折号加中文译名，作为页面可见标题。
2. **`## 📄 元数据`**：作者，年份，*期刊* 卷(期)、页码，DOI 用 `[doi](url)` 行内链接。
3. **`## 💡 一句话`**：一段话讲清论文做了什么、核心发现/数值、关键机制。
4. **`## 🔗 Wiki 双链`**：按「概念 / 实体 / 图表 / 年度 / 项目 / 相关论文」分行列出双链，是 frontmatter 列表字段的来源：
   ```markdown
     - 概念 [[../concepts/<slug>|<中文名>]]、...
     - 实体 [[../entities/<slug>|<名称>]]
     - 图表 [[../figures/<slug>|<图名>]]
     - 年度 [[../write/<year>]]
     - 项目 [[../projects/project-1-two-photon|项目一：...]]
     - 相关论文 [[../../raw/note/<citekey>]]
   ```
   相对路径从 `wiki/papers/` 出发：概念/实体/图表/年度/项目用 `../`，原始 note 用 `../../raw/note/`。
5. **`## 🆕 新概念/实体建议`**（可选）：记录读笔记时发现、wiki 尚未建页、值得新建的概念/实体。
6. **`## 📊 关键图表`**：嵌入本论文图片，每张图下方用 `-> [[../figures/<slug>|<分类名>]]` 标注归属的图表页（即图表双链，必须保留）：
   ```markdown
   - ![图：<中文图注>](../../raw/figures/<citekey>/<hash>.png) -> [[../figures/optical-spectra|光学与吸收光谱]]
   ```
   无图片时用文字描述关键图（Fig./Table 编号 + 内容），并说明 raw 目录情况。
7. **`## 🔬 项目连接`**：逐项目说明关联度（`**project-N 名称 — core/high/medium/low**：<理由>`）。明确无关联时写「无直接项目连接」并简述原因——此处结论决定 `projects` 字段是否留空。判定以**内容参考价值**为准，不看 Zotero 归属。
8. **`## 🔗 项目双链`**：仅列出确实相关项目的 `[[../projects/project-N-...]]` 双链；与上一节结论一致。
9. **`## 📝 组织与用词`**：分析论文论证结构、可复用的中英术语；术语尽量双链到对应 concept 页。
10. **`## ✏️ 可写入 Wiki 的要点`**：编号列出可沉淀进 wiki 的机制、数据、公式、结论；其中概念/实体术语应按 CJK 双链规则（见维护经验）加双链。

### 四、编写与双链铁律

- 正文引用其他论文一律链 `wiki/papers/<citekey>`；**本页是唯一允许直链 `raw/note/` 的页面**（仅 `original_note::` 与「相关论文」两处）。
- 不直接编辑 `raw/`；图片只通过 `../../raw/figures/<citekey>/...` 相对路径嵌入。
- 术语双链遵循最长匹配、复合词边界、保护数学/代码/链接的规则（见上文「CJK 术语自动双链」）。
- 不保留 AI 双语转写、Zotero 元数据大表、转换日志等噪音。

---

## 维护铁律

---

## Papers / Figures 维护经验（2026-08 批量校对）

本节记录本批整理 `wiki/papers/` 与 `wiki/figures/` 时踩过的坑与确立的规则，供后续批量任务复用。

### 一、Papers frontmatter（混合 YAML + Dataview 内联字段）

每篇 paper 的 `---` 块是**混合结构**：普通 YAML 字段（`citekey/title/authors/year/...`）与 Dataview 双冒号内联字段（`original_note::`、`领域基础知识:: >-` 等）共存。注意：

- **`original_note` 必须是双冒号内联字段**：写成 `original_note:: [[../../raw/note/<citekey>]]`，且 `[[ ]]` **绝不能加双引号**。写成 YAML 单冒号 `original_note: "[[...]]"` 会被当成字符串、Dataview 无法识别为链接。
- **frontmatter 之前不能有任何内容**：曾出现整段孤立的 `领域基础知识:: >- ...` 重复块挡在 `---` 之前（如 Gulhare2021），导致该页等于没有 frontmatter。批量脚本一律以 `t.startswith("---\n")` 起算，不满足即报错。
- **列表字段两种写法都合法**：行内 `concepts: [a, b, c]` 或多行 `  - item`。审计空字段时，解析器必须两种都能识别，否则会把多行列表误判为空。
- **空字段要区分"真缺失"与"本就不适用"**：
  - 综述/Perspective（如 Spaldin 多铁综述）`methods` 为空是正常的，不要硬塞方法。
  - 理论/方法经典论文（Kresse、Perdew、Nose、Monkhorst、Dudarev、van Vleck、Delley）没有具体研究材料，`materials`/`figures` 为空正常。
  - `projects` 为空，仅当 `## 🔬 项目连接` 明确写"无直接项目连接"时才保留为空——这正好贯彻"看内容参考价值，不看 Zotero 归属"。
- **回填正文已有的双链**：body `## 🔗 Wiki 双链` 里按"概念/实体/图表/项目"分行列出了 slug，是回填空 frontmatter 列表字段的权威来源。`projects` 链形如 `project-1-two-photon`，frontmatter 只取 `project-1` 码。
- **figures 字段必须指向真实存在的图表页 slug**（如 `optical-spectra`、`experimental-setups-spectroscopy-diffraction`），不能臆造 `xrd-patterns`、`ml-intensity-curves` 这类不存在的子页。

### 二、CJK 术语自动双链（可写入 Wiki 的要点）

对 `## ✏️ 可写入 Wiki 的要点` 正文做概念/实体双链时，中文子串匹配极易误伤，确立三条规则：

1. **最短长度 ≥ 3 个 CJK 字符**，并维护 STOP 停用集合（"铁电/相变/材料…"等泛词，以及"面内/面外/纵向/横向/内建"等歧义修饰词）。
2. **复合词边界判定**：匹配到某词时，若向左/向右延伸一个 CJK 字能组成词典里的更长词，则**拒绝**这次匹配（避免"界面内建"里的"面内"被链走）；否则允许（"为挠曲电效应"里的"挠曲电效应"正确成链）。
3. **保护段优先**：wikilink、行内/块级数学 `$...$`/`$$...$$`、反引号代码、`![](...)` 图片、`http(s)://` URL 一律不参与替换。
4. 幂等：section 里已含 `[[../concepts/` 或 `[[../entities/` 就跳过。

### 三、图表页（figures）组织

- **>50 条拆分**：单页超 50 个 H3 条目按物理主题拆成枢纽页 + 子页面，子页命名 `<分类>-<子主题>.md`，`_index.md` 同步加行并填真实条目数。枢纽页被大量反向引用时**保留原文件**，不要删/改名。
- **图片路径用 angle-bracket 语法时** `![](<path>)` 会让朴素校验脚本把 `<>` 当成路径的一部分而误报 missing；校验器需对 `(![...](<)path(>))` 归一化。
- 本批图表库最终约 1230 个 H3 条目、分布在 47 个页面，0 个缺失图片。

### 四、校验脚本要点（strict_verify.py 三个误报修复）

1. **表格里转义管道符**：`[[slug\|label]]` 的 `\|` 要先 `replace("\\|","|")`，并对 slug 末尾残留的反斜杠 `rstrip("\\")`，否则会报 255+ 个假断链。
2. **vault-绝对链接** `[[科研Wiki/...]]` 含 `/`，必须在"相对路径含 `/`"判定**之前**处理，否则被当成相对路径误判。
3. **图片路径 `<>`** 归一化后再查磁盘。

### 五、用 cli-anything-obsidian 校验

- 先 `export OBSIDIAN_API_KEY=...`（Local REST API 插件里取），`cli-anything-obsidian server status` 确认连通。
- **vault 根在 `科研Wiki/` 的上一级**，所以读取论文页路径是 `科研Wiki/wiki/papers/<citekey>.md`，不是 `wiki/papers/...`。
- Windows GBK 控制台输出含下标（如 `Mn₂N` 的 `₂`）会崩，命令前加 `PYTHONUTF8=1 PYTHONIOENCODING=utf-8`。
- 用法：frontmatter 改完后 `vault read` 抽查问题页能否被 Obsidian 正常解析，是对 YAML 合法性的最终确认。

### 六、Frontmatter 语法检查清单（每次批量改完跑一遍）

对每篇 paper 检查并保证：①以 `---\n` 开头且有闭合 `\n---\n`；②纯 YAML 部分能被 `yaml.safe_load` 解析（Dataview `key:: >-` 及其缩进续行要先整体剔除再解析）；③无重复 YAML 键；④行内列表 `[]`、双引号成对；⑤`[[ ]]` 平衡（注意 `![alt](...)` 里数学括号 `Im[χ⁽³⁾]` 紧邻 `]` 会产生 `]]` 假象，属合法图片语法，非断链）；⑥无 AI 残留文本。

### 七、Dataview 十字段批量审计（188 篇全量校验）

10 个中文字段（`领域基础知识/研究背景/作者的问题意识/主要研究对象/主要研究方法/研究意义/研究结论/对领域的贡献/未来研究方向提及/未来研究方向思考`）必须全部存在于 frontmatter 内、各恰好一次、非空、格式为 `key:: >-\n  <值>`，且正文（闭合 `---` 之后）不得残留同名字段。

- **字段块正则**：`^(领域基础知识|研究背景|...|未来研究方向思考)::.*(?:\n[ \t]+.*)*\n?`（`re.M`）——字段头加后续所有缩进续行，作为一个整体匹配，用于计数、去重与删除。
- **逐篇检查项**：①fm 内每个 key 计数 == 1（0 = 缺失，>1 = 重复块）；②body 内计数 == 0（否则是 force-sync 残留的游离块）；③把字段头与续行拼起来后非空；④值内不得嵌入下一个字段标记（正则 `\s(其他键):{1,2}`，注意 raw/note 里 `对领域的贡献` 用单冒号，提取时残留会被带进 wiki 值）。
- **两类典型故障及修复**：
  1. **整块重复**（如 zahraCriticalAnalysisFerroelectric2025 的 3 个字段各出现两次、内容完全相同）：用字段块正则按出现顺序遍历，保留首次、删除后续重复 span（从后往前删以免位移），不要手动编辑。
  2. **值尾粘连下一字段**（如 amini 的 `研究结论` 末尾粘了一整段 `对领域的贡献: 1...`，而下一个字段又有干净副本）：这是从 raw/note 提取时 `对领域的贡献:` 单冒号未被字段分隔正则截断所致；定位后直接裁掉粘连尾句，保留独立字段。
- **权威来源是 raw/note**：这 10 个字段的值一律从 `raw/note/<citekey>.md` 的 blockquote 关键字标记（`> key:: value`；`对领域的贡献` 是单冒号 `> 对领域的贡献:`）提取，不要自行改写或 paraphrase。重建时先把 fm 和 body 里所有旧字段块整体剔除，再在 `tags:` 之前插入一份干净块；写文件用 `open(p,'w',encoding='utf-8')`，**不要**传 `newline="\n"`（Windows 下会抛 `OSError: [Errno 22]`）。
- **本批结果**：188 篇全量校验后，仅 zahra（3 字段整块重复）与 amini（结论尾粘连贡献段）两篇有问题，均已修复；复核 0 篇有问题。

### 八、概念/实体重名与近义合并（concepts / entities 去重）

整理 `wiki/concepts/`（1154 → 1089 个）与 `wiki/entities/` 时，分三轮机械 + 语义排查，共删除 65 个重复文件、无断链残留。

1. **concept/entity 同名碰撞（36 个）**：同一 slug（如 `BaTiO3`、`MoS2`、`NiI2`、`WIEN2k`、`PFM`、`graphene`、`MAX-phases`…）在两个目录各有一份。判据：**具体材料/代码/仪器/器件 → 归 `entities/`；抽象现象/机制 → 归 `concepts/`**。这批全是材料/软件/仪器，故以 entity 为规范家：内容更丰富的那一份（特例：`VSe2`、`WIEN2k` 的 concept 更详尽，把 concept 内容转成 entity）作为最终 entity，把双方的 Related Papers 去重合并，再把全库 `[[...concepts/<slug>]]` 改写为 `[[...entities/<slug>]]`，最后删 concept 文件。
2. **拼写/单复数变体（9 组 + 15+ 组语义近义）**：先按归一化 key（去连字符、复数 s/es、NFKC）找机械重复（`bessel-beam(s)`、`polar-metal(s)`、`pseudo-gap`/`pseudogap`、`skyrmion(s)`、`type-ii-multiferroic(s)`、`DFTB+`/`dftb`…）；再按 H1 标题中文段（斜杠/括号前部分）找语义重复（`flexoelectricity`/`flexoelectric-effect`、`charge-order`/`-ordering`、`exciton-condensation`/`excitonic-`、`icosahedral-packing`/`-structure`、`funnel-effect`/`exciton-funnel-effect`、`twisted-intramolecular-charge-transfer`/`tict-...`、`ginzburg-landau`/`-theory`、`quantum-spin-hall`/`-effect`/`-insulator`、`soft-mode`/`phonon-soft-mode`、`bandwidth-control`(富文本)→`bandwidth-controlled-mott-transition`、`size-effect`(内容实为临界厚度)→`critical-thickness-ferroelectric` 等）。规范名取**单数、最常见、最贴切的标准术语**；把两份的描述与 Related Papers 合并进规范文件，删除别名文件。
3. **包含关系要分清"真重复"与"父子概念"**：token 包含（短 slug 是长 slug 的子串）大多是合法的父/子关系，**不要合并**——如 `hall-effect` ⊃ `quantum-anomalous-hall-effect`、`charge-density-wave` ⊃ `spin-charge-density-wave`、`magnetic-anisotropy` ⊃ `perpendicular-magnetic-anisotropy`、`molecular-dynamics` ⊃ `ab-initio-molecular-dynamics`。只有当两份描述的是**同一概念的不同命名**（同一 H1、同一机制）时才合并；`soft-mode-theory`、`soft-mode-phonon`（平带声子机制）作为 `soft-mode` 的不同侧面保留并互链。

- **合并操作模板**：①读两份正文，抽取各自 `- [[../papers/<key>]]` 做有序并集；②以规范文件 frontmatter 为准，改正文 H1，合并描述；③重写 `## Related Papers` 为并集，保留 `## 关联概念与实体` 等尾部小节；④删除别名文件；⑤全库正则 `(\[\[[^\]]*?concepts/)<old>(\||\]\])` → `\1<new>\2` 改写反向链接；⑥最后校验无任何文件再链接到已删 slug。
- **校验**：改完跑 `strict_verify.py`，并单独 grep 已删 slug 确认 0 个 stale 链接；verify 里残留的 broken links 是历史遗留的"指向尚未创建 stub"的前向链接，与本次去重无关。

4. **实体去重补记（探针分子 P1/P2）**：`wiki/entities/` 里同一对 D-π-A 二苯乙烯探针在不同论文里用了不同代号，产生 5 个碎文件：`P1`（H2017 叫法）、`P1-probe`（Huang2019 的 1a）、`P2`、`P2-probe`、`dicyanostilbene`（骨架）。它们其实是同一对分子——2,5-二氰基-4-甲基-4' 取代二苯乙烯，H2017 记 P1/P2，Huang2019/2023 记 1a/1b。合并为描述性 slug **`dicyanostilbene-1a`**（二甲氨基给体，δmax=6670 GM，Φ=0.805）与 **`dicyanostilbene-1b`**（二苯氨基给体，变色范围较小），骨架描述并入更详尽的 **`DCS`** 实体（已含 H2017 前期 TPF 探针设计的引用）。删除 5 个文件；同步改写正文双链、frontmatter `entities:` 列表与 `entity/<slug>` 建议列表，以及 `quinine-bisulfate` 里的裸 `[[P1-probe]]`。教训：**跨论文代号不同的同一实体要按化学名归一**，并同时搜正文 wikilink、frontmatter 列表、正文中的 `entity/slug` 建议项三处引用。

- **不要直接手动编辑 `raw/` 目录**：该目录由脚本和 Zotero 同步维护。
- `tools/ingest_papers/` 下的逐篇记录是中间产物，最终归档到 `wiki/papers/`，不要在 `tools/` 下长期保留。
- **Wiki 是动态的**：随着新论文的加入，概念和实体的描述应趋于丰富和准确。
- **链接优先**：`wiki/papers/<citekey>` 是论文在 wiki 中的正式条目，须回链原 note `[[../../raw/note/<citekey>]]`。
- **wiki 其他条目的引文一律指向 `wiki/papers/`**：`wiki/concepts/`、`wiki/entities/`、`wiki/figures/`、`wiki/write/`、`wiki/projects/`、`wiki/topics/` 等条目引用某篇论文时，链 `[[../papers/<citekey>]]`（或对应相对路径），**不得**直接链 `raw/note/`。只有 `wiki/papers/<citekey>` 可以直连 `raw/note`。
