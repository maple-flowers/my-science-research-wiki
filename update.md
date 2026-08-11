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

## 维护铁律

- **不要直接手动编辑 `raw/` 目录**：该目录由脚本和 Zotero 同步维护。
- `tools/ingest_papers/` 下的逐篇记录是中间产物，最终归档到 `wiki/papers/`，不要在 `tools/` 下长期保留。
- **Wiki 是动态的**：随着新论文的加入，概念和实体的描述应趋于丰富和准确。
- **链接优先**：`wiki/papers/<citekey>` 是论文在 wiki 中的正式条目，须回链原 note `[[../../raw/note/<citekey>]]`。
- **wiki 其他条目的引文一律指向 `wiki/papers/`**：`wiki/concepts/`、`wiki/entities/`、`wiki/figures/`、`wiki/write/`、`wiki/projects/`、`wiki/topics/` 等条目引用某篇论文时，链 `[[../papers/<citekey>]]`（或对应相对路径），**不得**直接链 `raw/note/`。只有 `wiki/papers/<citekey>` 可以直连 `raw/note`。
