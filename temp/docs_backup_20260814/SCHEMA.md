# SCHEMA — 科研 Wiki 维护规范

本文件是 Karpathy LLM Wiki 架构的规范约束（Schema）。任何 LLM 在本仓库执行 ingest / query / lint 时必须遵守本规范。原始资料（Zotero PDF、`raw/note/`）为第一层输入；`wiki/`（主题、概念、实体、项目）与 `wiki/figures/`（图表文字描述及细化索引）为知识层，由 LLM 拥有并维护。

本文件统一定义全库的**目录约定、标签体系、链接规范与维护铁律**；各层条目的编写格式规范见 [[wiki/format-spec]]，批量维护的踩坑经验见 [[log]]（2026-08-12 维护经验条目），更新工作流（机械同步 + 智能合成）见 [[update]]。

## 目录约定

```
科研Wiki/
├── SCHEMA.md              本文件（规范约束）
├── index.md               内容导向总索引
├── log.md                 时间导向日志（含 2026-08 批量维护经验）
├── update.md              更新工作流（机械同步 + 智能合成）
├── 文献矩阵.base          文献矩阵数据库文件
├── raw/
│   ├── note/              第一层输入：原始 AI 阅读笔记 (<citekey>.md)
│   ├── figures/           第一层图表元数据输入：按 KEY 存放的 manifest.json 及本地图片资产 (.png)
│   └── 文献日报/YYYY-MM-DD.md  文献鸟自动推送流（Raw Ingest）
├── wiki/
│   ├── projects/          核心科研项目联动目录（Project 1~7 索引与参考文献池映射）
│   ├── topics/            按主题分类的聚合页（仅 example.md 占位，待重构）
│   ├── entities/          材料/器件/方法实体页（22 正式页）
│   ├── concepts/          物理概念页（103 正式页）
│   ├── figures/           细化图表分类库与总索引 (_index.md + 枢纽页/子页面)
│   ├── papers/            论文增强卡片（wiki 正式条目，唯一可直链 raw/note 的页面）
│   ├── write/             学术写作用词库（_index.md + 五年段 <YYYY>-<YYYY>.md）
│   └── format-spec.md     条目编写格式规范（六类怎么写）
├── answer/                Answer 模式输出目录（只读作答，见下）
└── tools/                 脚本与工具（已清空、待重建）
```

## 摄入源（Ingest Sources）

1. **文献鸟（Stork）自动推送**：由 `stork_daily.py` 每天抓取（该脚本已随 `tools/` 清空、待重建）。
   - **自动动作**：生成 `raw/文献日报/` 日志；调用 `cli-anything-zotero` 自动入库并按关键词分类。
2. **人工/AI阅读笔记**：存放在 `raw/note/` 目录中。

## 标签体系

写在每页 frontmatter：

- `category: [D02]` —— 大会分类编码
- `tags: [domain-wall, moire, ultrafast-switching]` —— 英文 slug，描述图/文"是什么"
- `methods: [DFT, ML-potential, DPMD]` —— 研究/计算方法
- `materials: [h-BN, bilayer]` —— materials体系

图片标签与文本描述记录在 `raw/figures/<KEY>/manifest.json` 中，包含 `caption_zh`、`llm_description`、`tags` 等字段。

## 核心链接规范

- **引文链接层级**：`wiki/papers/<citekey>` 是论文在 wiki 中的正式条目，是**唯一**允许直链 `raw/note/` 的页面（`[[../../raw/note/<citekey>]]`）。`wiki/concepts/`、`wiki/entities/`、`wiki/figures/`、`wiki/write/`、`wiki/projects/`、`wiki/topics/` 等其他条目引用某篇论文时，一律链 `[[../papers/<citekey>]]`（或对应相对路径），**不得**直接链 `raw/note/`。
- **链接完整性**：始终保持 `wiki/papers/` ↔ `raw/note/` 之间、`wiki/` 各页面 ↔ `wiki/papers/` 之间的双向 `[[ ]]` 链接通畅。
- 细化图表分类文件存放于 `wiki/figures/` 目录下，包含 1 个 `_index.md` 总索引及按物理主题拆分的枢纽页/子页面（当前 25 页 / 1080 个条目）。
- 学术写作用词库存放于 `wiki/write/` 目录下：`_index.md` 总索引 + `_patterns.md` 跨段高频模式页 + 7 个五年段 `<YYYY>-<YYYY>.md` 文件（`1945-1999` 至 `2025-2029`），更早年份论文归入 `1945-1999` 段。

---

## Answer 模式（基于知识库只读作答）

当用户要求"进入 answer 模式 / 基于知识库回答问题"时，进入纯只读检索作答环节，与"更新知识库"彻底分开。规则：

1. **冻结知识库**：不得创建、修改、删除 `wiki/`、`raw/`、`index.md` 等任何知识库文件，只读取、不写入。
2. **回答落点**：在 `answer/` 目录新建一个 markdown 文件，文件名按本地年月日+时间命名：`answer/YYYY-MM-DD-HHMM.md`（如 `answer/2026-08-12-2130.md`）。回答全文写入该文件，不要只在对话里输出。
3. **来源必须双链**：每个论断、数据、结论都须用 `[[ ]]` 双链回知识库来源（如 `[[wiki/papers/<citekey>]]`、`[[raw/note/<citekey>]]`、`[[wiki/concepts/...]]`），不得给出无出处的结论。
4. **可引用素材**：可使用标准 markdown 图片语法引用图片（如 `![](../../raw/figures/<KEY>/<file>.png)`），以及表格、公式等。
5. **可疑内容只标注不改正**：若发现知识库某处可能放错位置、内容存疑或来源冲突，**不得自行改动**，在回答中以醒目标记记录，例如 `> ⚠️ 待确认：<问题描述>，涉及 [[...]]`，等用户稍后确认。

---

## 条目编写规范

各层条目的编写格式规范（图表库 / 概念与实体 / 论文条目 / 写作库 / 主题 / 项目 六类）已独立归档，见 [[wiki/format-spec]]。

## 铁律

- **图表库资产管理**：允许在 `raw/figures/<KEY>/` 下存放从 Zotero 复制的图片文件（从 `C:\Users\sgg\Zotero\storage` 同步），以便在 Obsidian 中直接预览。`manifest.json` 需记录 `figures`、`tables` 和 `formulas` 三类结构化信息。
- **不要直接手动编辑 `raw/` 目录**：该目录由脚本和 Zotero 同步维护。
- **链接优先**：`wiki/papers/<citekey>` 是论文在 wiki 中的正式条目，须回链原 note `[[../../raw/note/<citekey>]]`。
- **引文指向 wiki/papers/**：`wiki/concepts/`、`wiki/entities/`、`wiki/figures/`、`wiki/write/`、`wiki/projects/`、`wiki/topics/` 等条目引用某篇论文时，一律链 `[[../papers/<citekey>]]`（或对应相对路径），**不得**直接链 `raw/note/`。只有 `wiki/papers/<citekey>` 可以直连 `raw/note`。
- **链接完整性**：始终保持全库 `[[ ]]` 双向链接通畅。
- `tools/` 目录已清空、待重建；原 `tools/ingest_papers/` 下的逐篇中间产物归档流程暂缓，待脚本重建后继续归档到 `wiki/papers/`。
- **Wiki 是动态的**：随着新论文的加入，概念和实体的描述应趋于丰富和准确。
- 所有日期用 `YYYY-MM-DD`。
- 中文为叙述语言，英文 slug/专有名词保留原文。
- **Answer 模式只读**：进入 answer 模式后禁止改动知识库，只在 `answer/YYYY-MM-DD-HHMM.md` 写回答，答案须双链来源；发现放错或存疑处只标 `> ⚠️ 待确认：…`，等用户确认，不自行改正（详见上文「Answer 模式」）。

---

> **2026-08 批量维护的踩坑经验已归档至 [[log]]**（2026-08-12 维护经验条目）：frontmatter 混合结构、CJK 双链规则、图表页组织、校验脚本要点、Dataview 十字段审计、概念/实体去重，均不再重复于 SCHEMA。
