# 科研 Wiki 整理 —— 交接文档

> 日期：2026-08-12  
> 分支：`feature/wiki-synthesis-expansion`  
> 状态：论文工作流完成 188/188；待统一样式+最终校验

---

## 一、当前状态概览

| 目录 | 页面数 | 备注 |
|------|--------|------|
| wiki/papers | 188 | ✔ 全部完成 |
| wiki/concepts | 1129 | ✔ stub 标题已修 |
| wiki/entities | 186 | ✔ stub 标题已修 |
| wiki/figures | 18 | ✔ 1 枢纽页 + 17 子页 |

## 二、已完成工作

### 2.1 论文链接整理（188-agent workflow）
- 完成了 188/188 论文的概念、实体、图表双链（续跑解决 429 限制）
- 完成了 164 篇 AI 残留清除（zotero 回链、GPT 标签、`#🤖️`、批量生成行）
- 完成了 42 篇自引用链接修复（`[[自身citekey]]` → `**citekey**`）
- 完成了中文语境 "and" → 与/、/和替换
- 新建概念/实体条目的 promotion 到 `现有wiki双链` 节

### 2.2 值得复用的术语
- 从 64 篇论文提取 565 个术语候选
- 16-agent 整理工作流：33 create / 28 alias / 48 skip（6/16 批次完成；10 个 429 失败）
- 已创建 32 个概念/实体 stub 页（双语标题、定义、来源论文反向链接）
- 63 篇论文术语段已内联双链化（297 处）
- 4 处误链已手动修正（光学穿透深度、formation energy、公式→SnSe、SHG i-type）

### 2.3 original_note 修复
- 155 篇带引号的 `original_note: "[[...]]"` 统一改为 `original_note:: [[...]]`（双冒号无引号）
- **⚠ 已知 bug**：4 篇 frontmatter 被 agent 误改成 `"original_note:":`（带引号的键名）。在 `tools/_fix_frontmatter4.py` 就绪。

### 2.4 stub 标题修复（8-agent workflow）
- 142/143 个畸形 `# 概念）`/`# 实体）` H1 恢复为双语 `# 中文 / English`
- 142 个 `` 概念）：``/`` 实体）：`` 正文前缀已清除
- rGO 手动修复（不同畸形形态）
- 新增 32 个 term 页面已按正确格式创建

### 2.5 检测工具
| 文件 | 功能 | 状态 |
|------|------|------|
| `tools/strict_verify.py` | 断链/AI残留/自引用/占位符/图片/raw链 | ✔ 已写 |
| `tools/final_verify.py` | 原版（断链已注释掉） | 已有 |
| `tools/_classify_broken.py` | 断链分类统计 | ✔ 已写 |
| `tools/_fix_origin_note.py` | 去引号修正 | ✔ 已跑 |
| `tools/_link_figure_per_image.py` | 每张图→figures子页双链 | ✔ 已跑 |

---

## 三、待完成

### 3.0 🔴 论文格式统一（优先级最高）
**用户要求**：统一 papers 格式，加 emoji，多用 `##` 层级标题。  
当前格式为扁平 bold-label bullet（`- **元数据**：`、`- **一句话**：` 等）。  
应转换为：

| 当前标签 | 建议 ## 标题 |
|----------|-------------|
| 元数据 | `## 📄 元数据` |
| 一句话 | `## 💡 一句话` |
| 现有wiki双链 | `## 🔗 Wiki 双链` |
| 关键图表 | `## 📊 关键图表` |
| 项目连接 | `## 🔬 项目连接` |
| 组织与用词 | `## 📝 组织与用词` |
| 可写入wiki的要点 | `## ✏️ 可写入 Wiki 的要点` |
| 新概念/实体建议 | `## 🆕 新概念/实体建议` |

**实现方式**：写一个确定性脚本 `tools/_reformat_papers.py`，扫描每篇论文正文，将 `- **标签名**` bullet 替换为 `## emoji 标签名`，并将底部的 `### 二级小标题` 升级。

### 3.1 🔴 4 篇 frontmatter original_note 修正
位置：`tools/_fix_frontmatter4.py`
```
"original_note:": "[[...]]"  →  original_note:: [[...]]
"original_note:": ../../raw/...  →  original_note:: [[../../raw/...]]
```
文件：2019optical, Barnett2006coexistence, bhowalPolarMetalsPrinciples2023b, deSousa2008electrical

### 3.2 术语整理：10 个因 429 失败的批次
- 运行 `Workflow({scriptPath: "tools/curate_terms_wf.js", resumeFromRunId: "wf_5a7a3f23-586"})` — 成功的 6 个走缓存
- 需重新生成 `_term_decisions.json` 并入新 batch
- 建页 + 双链化（与已完成逻辑一致）

### 3.3 🟡 最终校验
```
PYTHONUTF8=1 python tools/strict_verify.py
```
当前 baseline：papers 内 2 个断链、0 AI 残留、0 自引用、0 占位符。  
- `gomez-ortizKittelLawDomain2023` → `../entities/PHONOPY` 应为 `../concepts/phonopy`
- `pengStrainEngineering2D2020` → `../../raw/note/pengStrainEngineering2020`（文件名可能不同）

concepts/entities/figures 目录内 254 个既有断链（`../../` 路径深度、`_KEY-` citekey）不属于本次范围。

### 3.4 清理 tools/ 临时产物
完成后删除：`_wo/`、`_term_batches/`、`_stub_batches/`、`_*.json`（保留 `_paper_fig_map.json` 和 `_img2page.json`）、`_*.py` 生成脚本

---

## 四、规则备忘

- **不要直接编辑 `raw/`**：由脚本和 Zotero 同步维护
- **wiki 条目引文指向 `wiki/papers/`**，只有 `wiki/papers/<citekey>` 可直连 `raw/note`
- **`[[ ]]` 内只能是无引号路径**（Obsidian 解析规则）
- **frontmatter 内联字段用 `字段名:: 值`**（双冒号，Obsidian Dataview 惯例）
- **tools/ 不要长期保留中间产物**

## 五、关键文件索引

| 文件 | 路径 |
|------|------|
| 论文索引 | `wiki/papers/` （188 篇） |
| 图表子页 | `wiki/figures/heterostructures-stacking-*.md` |
| 图→子页映射 | `tools/_img2page.json` |
| 论文→figures 映射 | `tools/_paper_fig_map.json` |
| 术语决策 | `tools/_term_decisions.json` |
| 术语提取 | `tools/_terms.json`、`tools/_terms_resolved.json` |
| 论文工作流脚本 | `tools/link_papers_wf.js` |
| stub 工作流脚本 | `tools/fix_stubs_wf.js` |
| 术语工作流脚本 | `tools/curate_terms_wf.js` |
| 工作流 run ID | wf_9635ec62-996 (论文)、wf_5a7a3f23-586 (术语)、wf_c1b5c828-46d (stub) |
| 工作流记录 | `~/.claude/projects/E--swan-goose.../subagents/workflows/` |

## 六、今天未完成的关键对话上下文

用户最新两条要求：
1. **"papers 请统一格式，加 emoji，多用 ## 层级标题"** — 见 §3.0，应先做
2. **"[[ ]] 里面不识别字符串只识别路径"** — 确认: frontmatter 里的 wikilink 值不能用引号包裹，§3.1 的 4 篇是最后残留
