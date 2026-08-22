# 科研 LLM Wiki 搭建方案（Karpathy 三层架构 + 论文 Figure 库 + 材料大会分类索引）

## Context

用户是材料学科研工作者，论文库在 Zotero，AI 总结笔记已同步到 Obsidian（`爱看论文的猫猫/note/`，文件名带 `_KEY-XXXXXXXX`），但笔记只有文字、没有图。目标是按 Karpathy 的 LLM Wiki 思路建一个**持久化、增量维护、带交叉链接**的科研知识库：

1. **第一层输入** = Zotero 论文（PDF + 已同步的文字笔记），不复制原件，用指针引用。
2. **新增图片库**：逐篇、逐张提取论文 figure，打标签，建立可检索的 figure 索引。
3. **Wiki 分类**：沿用 `爱调研的猫猫/厦门中国材料学大会/` 现有分类（A 能源 / B 环境 / C 结构 / D 功能 / E 模拟制备评价 / FB 前沿 / P 高分子老化 / Z 模拟设计，共约 100 个子类）。

第一轮只搭骨架 + 试点 3-5 篇（多铁性方向，内聚性强），跑通全流程后再批量。

## 已确认的关键事实

- Zotero 存储：`C:\Users\sgg\Zotero\storage\<附件key>\*.pdf`。**注意：storage 子文件夹名是 PDF 附件的 key，不是父文献 key**。附件 key 来自笔记里的 `zotero://open-pdf/library/items/<附件key>` 链接（可有多份附件）。
- 工具就绪：Python 3.11、poppler `pdfimages`/`pdftotext`/`pdftoppm` 25.02。PyMuPDF 未装（不需要）。
- `pdfimages -list` 输出含 page/num/width/height/enc；`pdftotext -layout` 可抓 `Fig. N.` 图注。
- 需过滤 publisher logo（如 119×119、248×271 的小图）；矢量图用 `pdfimages` 抽不出，需 `pdftoppm` 渲染整页作 fallback。
- 现有大会分类目录已含每个子类的深度调研报告（如 `D 功能材料/D02 多铁性材料/D02 多铁性材料.md`），wiki 主题页与之互链。

## 目标目录结构（新建顶层 `科研Wiki/`）

```
科研Wiki/
├── SCHEMA.md                 # 第三层：LLM 维护规范（ingest/query/lint 工作流、标签与命名约定）
├── index.md                  # 内容导向总索引（papers / figures / topics / entities 四区块）
├── log.md                    # 时间导向日志，## [YYYY-MM-DD] ingest | <title>
├── raw/
│   └── papers/
│       └── <PARENTKEY>.md    # 指针页：zotero 链接、PDF 附件 key 列表、指向 note/ 原文笔记的链接
├── wiki/
│   ├── papers/               # 每篇论文增强卡片：元数据 + 内嵌 figures + 标签 + 所属分类 + 关联
│   ├── topics/               # 按大会子类的聚合页（D02-多铁性材料.md …），链回已有调研报告
│   ├── entities/             # 材料体系 / 方法 / 物理量实体页（按需生成）
│   └── concepts/             # 概念页（如"磁电耦合""畴壁"，按需生成）
├── figures/
│   ├── _figure-index.md      # dataview 汇总：所有 figure 按标签/分类/论文筛选
│   └── <PARENTKEY>/
│       ├── fig1.png          # 提取出的图（子图合并或按 fig 号命名）
│       ├── fig2a.png
│       └── manifest.json     # page、source image nums、caption、tags、llm-description
└── tools/
    └── extract_figures.py    # 提取脚本（见下）
```

## Figure 提取脚本 `tools/extract_figures.py`

输入一个父文献 key（或 note 文件路径），自动完成：

1. 解析 `爱看论文的猫猫/note/*_KEY-<PARENTKEY>.md`，抓出所有 `zotero://open-pdf/library/items/<ATTACHKEY>`。
2. 在 `C:\Users\sgg\Zotero\storage\<ATTACHKEY>\` 找 PDF（优先英文原版，跳过重复）。
3. `pdfimages -list` 枚举图片：
   - **过滤 logo**：width<350 且 height<350 的跳过（页眉/出版社 logo）。
   - **矢量页 fallback**：若某页在正文中有 `Fig. N.` 图注但 `pdfimages` 无合格位图，用 `pdftoppm -png -f N -l N -r 200` 渲染整页（试点阶段保留整页，后续可裁剪）。
4. 抽取：`pdfimages -png -p`（`-p` 让文件名含页码），写入 `figures/<PARENTKEY>/`。
5. 图注关联：`pdftotext -layout` 抓全文 `Fig. N.` 行，按图片所在页码聚合并把图注写入 `manifest.json`（多子图时标注 page 上所有 Fig 号，标记"待人工/LLM 确认"）。
6. 生成 `manifest.json`，每条含：`file, page, source_images, fig_number, caption_raw, tags:[], llm_description:"", category:[]`。

脚本只做机械提取，**标签和描述留空**，由 LLM 在 ingest 步骤填写（人在环中确认）。

## SCHEMA.md 要点（LLM 行为契约）

- **Ingest 工作流**：跑脚本 → 读原笔记 + 逐张看图 → 在 `wiki/papers/<KEY>.md` 写增强卡片（内嵌 `![[figures/KEY/figN.png]]`）→ 为每张图填标签和一句中文描述 → 把论文挂到 1 个主分类 + 相关次分类 → 更新/新建相关 topic 页与 entity/concept 页 → 更新 `index.md` → 追加 `log.md`。
- **标签体系**（三类，frontmatter 里用数组）：
  - 分类标签：`category: [D02]`（引用大会编码，主分类一个，可多个）
  - 内容标签：`tags: [domain-wall, moire, ultrafast-switching]`（英文 slug，描述图里是什么）
  - 方法/材料标签：`methods: [DFT, ML-potential, DPMD]`、`materials: [h-BN, bilayer]`
- **命名约定**：文件用 KEY 或英文 slug；中文标题放在 H1。
- **交叉链接**：论文卡片↔topic 页↔entity/concept 页双向 `[[ ]]`；topic 页顶部链接已有大会调研报告。
- **Query**：先读 `index.md` 定位 → 读相关页 → 综合回答并标注来源（论文 KEY + figure 文件名）→ 好答案可回写为 concept/topic 页。
- **Lint**：检查孤立页、缺失的反向链接、caption 未确认的 figure、分类空缺、与新论文矛盾的旧结论。
- **Raw 不可变**：绝不修改 `爱看论文的猫猫/note/` 和 Zotero PDF；`raw/papers/` 只放指针。

## 试点论文（多铁性 D02，已确认 PDF 在库）

- `ZTNTAL7L` He 2024 — Ultrafast switching … stacking-engineered ferroelectrics（已验证提取可行）
- `D72SE9HA` Spaldin 2005 — Renaissance of Magnetoelectric Multiferroics
- `2V9G68K6` Ramesh 2007 — Multiferroics: progress and prospects
- `2USFQC4T` Fiebig 2016 — The evolution of multiferroics

跑通后产出：`wiki/papers/` 4 张卡片、`wiki/topics/D02-多铁性材料.md`、若干 entity/concept 页（畴壁、磁电耦合、滑动铁电性等）、`figures/` 各子目录、`index.md` 与 `log.md`。

## 验证方式（端到端）

1. 对 `ZTNTAL7L` 跑 `python 科研Wiki/tools/extract_figures.py ZTNTAL7L`，检查 `figures/ZTNTAL7L/manifest.json`：
   - page 1 的 3 个 logo 小图被过滤掉；
   - page 3-8 的大图被抽出；
   - Fig.1–Fig.4 图注正确关联。
2. 在 Obsidian 中打开 `figures/ZTNTAL7L/` 逐张目视，确认 figure 完整、无 logo 混入；记录矢量图 fallback 是否触发。
3. 由我（LLM）按 SCHEMA 对 4 篇论文执行 ingest，生成卡片与 topic 页；用户在 Obsidian 里检查图片渲染、双链、dataview 索引。
4. 打开 `figures/_figure-index.md`，确认可按标签/分类筛选出试点 figure。
5. 用一个跨论文问题验证 query（如"多铁性材料中畴壁运动如何降低开关场？"），确认答案引用到具体论文和 figure。
6. 确认无误后，再讨论批量处理剩余约 70 篇笔记的计划。

## 不在本次范围

- 不批量处理全部论文（留待试点验收后）。
- 不改动 Zotero 库、不改 `爱看论文的猫猫/note/` 原有笔记。
- 不做复杂的矢量图自动裁剪（试点用整页渲染 fallback）。
