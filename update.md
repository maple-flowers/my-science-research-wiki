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

## 维护铁律

- **不要直接手动编辑 `raw/` 目录**：该目录由脚本和 Zotero 同步维护。
- **Wiki 是动态的**：随着新论文的加入，概念和实体的描述应趋于丰富和准确。
- **链接优先**：所有的知识点应尽可能回溯到 `[[raw/note/CiteKey]]`。
