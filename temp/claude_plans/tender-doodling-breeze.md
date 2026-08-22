# 科研 Wiki 批量更新同步方案 (Zotero & 爱看论文的猫猫/note)

## Context (背景)

用户希望将 `E:\swan_goose\宝宝\笔记库\sgg\爱看论文的猫猫\note\` 和 Zotero 中的论文笔记全量同步更新到 `E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\`。

现有状况：
1. 共有 138 个 Markdown 笔记文件，其中带 `_KEY-<KEY>.md` 的论文笔记文件为 **72 篇**。
2. 先前试点已经手动处理了 4 篇论文（`ZTNTAL7L`, `D72SE9HA`, `2V9G68K6`, `2USFQC4T`），目前仍有 **68 篇待摄入（Ingest）论文**。
3. 必须严格遵守 `SCHEMA.md` 契约（第一层 Raw 只读，只写 `科研Wiki/` 目录下的 `raw/papers/`, `raw/annotations/`, `wiki/papers/`, `wiki/topics/`, `figures/` 等）。
4. 根据最新记忆与 `SCHEMA.md` 约定：**综述类（Review）论文暂时不进行图片提取**（因图源杂且映射繁琐），仅原创研究论文（Original Research）提取图片。

---

## 实施方案 (Implementation Approach)

### 1. 编写批量摄入工具 `E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\tools\batch_ingest.py`

编写 Python 自动化脚本 `batch_ingest.py`，实现全自动摄入流程：

1. **解析笔记 (`NoteParser`)**：
   - 扫描 `爱看论文的猫猫/note/*_KEY-<KEY>.md`。
   - 匹配 Parent KEY 与 PDF 附件 KEY (`zotero://open-pdf/library/items/<ATTACH_KEY>`)。
   - 解析 Frontmatter 及正文的论文元数据（标题、作者、年份、DOI、条目类型 `itemType`、一句话总结、摘要、分类等）。
   - **判定论文类型**：若 `itemType` 包含 `review` 或标题/标签含 review，标记 `is_review = True`。

2. **生成 Raw 第一层指针与批注页 (`WikiGenerator`)**：
   - **指针页**：`raw/papers/<KEY>.md`（记录附件 KEY 列表、原始笔记链接、Zotero 协议链接、Wiki 卡片双链）。
   - **Obsidian Annotator 批注页**：为每个附件 KEY 生成 `raw/annotations/<KEY>-<ATTACH_KEY>.md`（包含 `annotation-target` Frontmatter）。

3. **生成 Wiki 第二层增强卡片**：
   - 生成 `wiki/papers/<KEY>.md`（根据模板填入元数据、总结、方法、关键图表与所属主题）。

4. **图表提取与 Review 保护 (`FigureExtractor`)**：
   - 若非 Review 论文，自动调用现有的 `tools/extract_figures.py <KEY>` 进行位图/矢量裁切提取并生成 `manifest.json`；
   - 若为 Review 论文，自动跳过抽图环节，防止产生噪声数据。

5. **索引与日志联动 (`IndexUpdater`)**：
   - 自动挂载至对应的 `wiki/topics/<CATEGORY>-<分类名>.md` 主题页。
   - 更新主索引 `科研Wiki/index.md`。
   - 在 `科研Wiki/log.md` 追加批量摄入记录。

---

## 执行步骤与分批策略

1. **干跑校验 (--dry-run)**：
   运行 `python tools/batch_ingest.py --dry-run` 检查待摄入的 68 篇论文，识别论文类型（Original vs Review）及解析状态。

2. **分批摄入执行**：
   按每批 15-20 篇分批次运行摄入脚本（如 `python tools/batch_ingest.py --limit 20`），确保每批次顺畅处理与日志生成。

3. **后处理与 Lint 健康检查**：
   - 校验 68 篇论文的 `raw/papers/`、`raw/annotations/` 与 `wiki/papers/` 完整生成。
   - 运行反向链接与孤立页校验，更新 `index.md` 和 `log.md`。

---

## 关键文件 (Critical Files)

- **新建脚本**：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\tools\batch_ingest.py`
- **抽图依赖**：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\tools\extract_figures.py`
- **规范文件**：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\SCHEMA.md`
- **主索引与日志**：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\index.md`，`log.md`

---

## 验证方式 (Verification)

1. 运行 `batch_ingest.py --dry-run` 验证待处理论文数量与 Review 判断准确率。
2. 批量处理后，检查 `raw/papers/` 与 `wiki/papers/` 增量文件数量是否一致（共新增 68 篇）。
3. 检查原创研究论文是否正常抽取图表与生成 `manifest.json`，而 Review 论文未错误抽图。
4. 检查 `index.md` 和 `log.md` 更新情况。
