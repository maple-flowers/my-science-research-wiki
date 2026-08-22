# 科研 Wiki 更新工作流 (Wiki Update Workflow)

> [!IMPORTANT] 格式规范已迁移
> 本页**仅**保留更新工作流（机械同步 + 智能合成）。所有页面编写格式规范（图表库 / 概念与实体 / 论文条目 / 写作库 / 主题 / 项目）、标签体系、链接规范与维护铁律，统一见 [[SCHEMA]]。

本 Wiki 采用 **"Raw 摄入 + Wiki 智能合成"** 的双层架构。更新过程分为机械同步与智能分析两个阶段。

## 第一阶段：Raw 资产同步 (Mechanical Ingest)

**目标**：将 Zotero 中的图片、原始笔记同步到 Wiki 的 `raw/` 目录下，并生成基础元数据。

**执行命令**（脚本已随 `tools/` 清空、待重建）：
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

**目标**：利用大模型 (LLM) 对 `raw/` 层的原始知识进行消化，自动更新 `wiki/concepts/`、`wiki/entities/`、`wiki/topics/`（仅 example.md 占位、待重构）、`wiki/figures/` 及 `wiki/projects/` 等知识库页面，而非简单的追加链接。

**执行方式**：
在 Claude 终端输入以下命令启动多智能体协作：
```bash
/workflow update_research_wiki
```

**该 Workflow 的逻辑流程**：
1. **发现 (Discovery)**：扫描 `raw/note/` 中新增的论文。
2. **映射 (Mapping)**：将新论文与现有的概念 (Concepts)、实体 (Entities)、研究话题 (Topics)、科研项目 (Projects) 及图表库 (Figures) 进行关联。
3. **合成 (Synthesis)**：为每个受影响的 Wiki 页面分配一个 Subagent，执行"深入阅读与知识融合"：
   - 阅读现有 Wiki 页面内容。
   - 阅读关联的新论文原件。
   - **重写页面**：将新发现融入"机制描述"、"材料特性"、"话题前沿"、"图表分类"或"项目进展"段落中，保持双向链接 `[[ ]]` 的完整性。
4. **写作分析 (Writing)**：分析新论文的写作用词，更新 `wiki/write/` 五年段总结。
5. **索引重构 (Indexing)**：重新生成 `index.md`，确保全库可达性。

---

## 逐篇阅读中间产物的归档 (Per-paper Reading Records)

**背景**：全量重写前，先对 `raw/note/` 中高质量、富批注的笔记逐篇通读，每篇产出一份结构化中文记录（元数据 / 一句话 / wiki 双链 / 新概念实体建议 / 关键图表 / 项目连接 / 组织与用词 / 可写入 wiki 的要点）。

- 这些记录在加工期间曾暂存于 `tools/ingest_papers/<citekey>.md`（该目录已随 `tools/` 清空、待重建），属于**中间产物**。
- **最终去向**：全部整理后移动到 `wiki/papers/<citekey>.md`，作为每篇论文在 wiki 中的正式条目（条目格式见 [[SCHEMA]] 的"论文条目编写规范"）。
- **回链原 note**：每份记录必须保留 `[[../../raw/note/<citekey>]]`，从 wiki 条目双向链接回原始笔记；同时被 `wiki/concepts/`、`wiki/entities/`、`wiki/figures/`、`wiki/projects/`、`wiki/topics/`（仅 example.md 占位、待重构）等条目反向引用。
- **项目连接判定标准**：以内容对项目有无参考价值（机制、方法、计算流程、可类比材料/物理、可复用数据）为准，不以 Zotero 文件夹/标签归属为准。
