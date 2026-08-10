# SCHEMA — 科研 Wiki 维护规范

本文件是 Karpathy LLM Wiki 架构的规范约束（Schema）。任何 LLM 在本仓库执行 ingest / query / lint 时必须遵守本规范。原始资料（Zotero PDF、`raw/note/`）为第一层输入；`wiki/`（主题、概念、实体、项目）与 `wiki/figures/`（图表文字描述及细化索引）为知识层，由 LLM 拥有并维护。

## 目录约定

```
科研Wiki/
├── SCHEMA.md              本文件
├── index.md               内容导向总索引
├── log.md                 时间导向日志
├── raw/
│   ├── note/              第一层输入：原始 AI 阅读笔记 (YYYY_Author_Title_KEY-<KEY>.md)
│   ├── figures/           第一层图表元数据输入：按 KEY 存放的 manifest.json 及本地图片资产 (.png)
│   └── 文献日报/YYYY-MM-DD.md  文献鸟自动推送流（Raw Ingest）
├── wiki/
│   ├── projects/          核心科研项目联动目录（Project 1~7 索引与参考文献池映射）
│   ├── topics/            按材料大会分类的聚合页
│   ├── entities/          材料/器件/方法实体页
│   ├── concepts/          物理概念页
│   ├── figures/           细化图表分类库与总索引 (_index.md)
│   └── write/             学术写作与用词库（按年份聚合）
└── tools/                 脚本与工具
```

## 摄入源（Ingest Sources）

1. **文献鸟（Stork）自动推送**：由 `stork_daily.py` 每天抓取。
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

- 所有文献相关的双向链接统一直接指向 `raw/note/` 下的具体笔记文件（例如 `[[raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]`）。
- 概念、实体与主题均直接关联至 `raw/note/` 下的笔记。
- 细化图表分类文件存放于 `wiki/figures/` 目录下，包含 8 个概念子库（如 `crystal-structures.md`）和 1 个 `_index.md` 总索引。
- 学术写作用词库存放于 `wiki/write/` 目录下，按文献发表年份聚合。

## 铁律

- **图表库资产管理**：允许在 `raw/figures/<KEY>/` 下存放从 Zotero 复制的图片文件（从 `C:\Users\sgg\Zotero\storage` 同步），以便在 Obsidian 中直接预览。`manifest.json` 需记录 `figures`、`tables` 和 `formulas` 三类结构化信息。
- **链接完整性**：始终保持 `wiki/` 各概念与 `raw/note/` 之间的双向 `[[ ]]` 链接通畅。
- 所有日期用 `YYYY-MM-DD`。
- 中文为叙述语言，英文 slug/专有名词保留原文。
