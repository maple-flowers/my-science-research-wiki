# 单篇阅读指令

你在科研Wiki仓库（cwd 为本仓库根目录）。不要启动任何工作流或子agent。任务：通读 **一篇** raw/note 笔记，为第二步重写 wiki 产出结构化记录。

## 论文定位
你的论文 citekey 写在传给你的 key 文件里（形如 tools/ingest_papers/NNN_<citekey>.key）。对应笔记是 `raw/note/<citekey>.md`。

## 必须通读全文
- 这是用户的明确要求：要通读全文，不能只挑章节。
- 若文件 ≤ 256KB，直接 Read 全文。
- 若文件 > 256KB（Read 会报错），用 offset/limit 分段（每段约 1800-2000 行）从第 1 行连续读到文件末尾，覆盖元数据、摘要、AI文献解读九模块（引言/结构/图表/核心内容/结论贡献/未来方向/批判分析/问题预测）以及任何原文摘录。不要跳过章节。
- 控制上下文技巧：读完一段就在脑中提炼该段要点，不要回头重复读已读段落；读到图表描述时记下图号。单篇上下文应能容纳。

## wiki 双链判断
开始读论文前，先运行一次 Glob 拿到现有条目文件名（结果记下来即可，读论文过程中不要再反复 Glob）：
- `wiki/concepts/*.md`
- `wiki/entities/*.md`
- `wiki/figures/*.md`
- `wiki/write/*.md`
- `wiki/projects/*.md`
- `wiki/topics/*.md`
笔记自身的 citekey 即文件名主干。raw/figures 下若存在 `<citekey>/` 目录，可用 Glob `raw/figures/<citekey>/*` 查看有哪些图。

## 输出记录（中文，准确，不编造）
写入文件 `tools/ingest_papers/<citekey>.md`。**文件最顶部必须是 YAML frontmatter**（用于 Obsidian Base / Dataview），然后才是正文。Frontmatter 要尽可能打全所有相关标签和属性，宁可多标不要漏标；标签用 kebab-case。

### YAML frontmatter 规范

```yaml
---
citekey: <citekey>
title: "<论文完整标题>"
authors: [姓 名, 姓 名, 姓 名]          # 列全部作者；太长可列前 6 位加 et al.
year: <年份整数>
journal: "<期刊全名>"
doi: "<DOI>"
url: "https://doi.org/<DOI>"
paper_type: <experiment|theory|review|perspective|method>
status: ingested
year_read: 2026
original_note: "[[../../raw/note/<citekey>]]"
projects: [project-2, project-5]         # 有参考价值的项目编号列表；无则 []
concepts: [ferroelectricity, dft-plus-u, berry-phase, ...]   # 正文涉及的概念 kebab 名
entities: [CrTe2, VASP, BaTiO3, ...]     # 材料/软件/器件等实体 kebab 名
methods: [dft, dft-plus-u, berry-phase, md, mlip, pxrd, sfm-pfm, arpes, muon-sr, ...]  # 计算/实验方法
materials: [CrTe2, h-BN, NbSe2, ...]     # 关键材料体系
figures: [crystal-structures, electronic-bands, ...]        # 图类型，对应 wiki/figures 文件名主干
# ↓↓↓ 十个文献矩阵字段（Obsidian Base/Dataview 文献矩阵）↓↓↓
# 在 raw/note/<citekey>.md 中找到以 "> 领域基础知识::" 开头的引用块（十个字段在同一连续 blockquote 中，
# 以 "  字段名:: " 分隔）。**逐字复制**这十个字段的内容到下面的 frontmatter 中，保持作者原文，
# 不要改写、不要总结、不要重新生成。使用 YAML 折叠块标量 ">-"。
# 若该 note 中不存在这个区块（极少数旧笔记），则由你通读全文后自行撰写这十个字段（每字段 2-6 句中文）。
"领域基础知识": >-
  <从 note 逐字复制；若缺失则自撰>
"研究背景": >-
  ...
"作者的问题意识": >-
  ...
"主要研究对象": >-
  ...
"主要研究方法": >-
  ...
"研究意义": >-
  ...
"研究结论": >-
  ...
"对领域的贡献": >-
  ...
"未来研究方向提及": >-
  ...
"未来研究方向思考": >-
  ...
tags:
  - paper
  - type/<paper_type>
  - year/<year>
  - project/<project-N>                  # 每个在 projects 列表里的项目各一条
  - relevance/<project-N>/<core|strong|medium|weak>   # 项目连接强度
  - concept/<concept-kebab>              # 每个 concepts 各一条
  - entity/<entity-kebab>                # 每个 entities 各一条
  - method/<method-kebab>                # 每个 methods 各一条
  - material/<material-kebab>            # 每个 materials 各一条
  - topic/<topic-kebab>                  # 研究话题，如 multiferroics、2d-materials、cdw、ferroelectricity、humidity-sensing、two-photon、ml-neural-network、molecular-crystal
---
```

字段填写要求：
- `projects` / `relevance/...`：与下方"项目连接"段落保持一致；core 表示项目核心机理/材料文献，strong 表示直接可复用，medium 表示明确方法/物理类比，weak 表示仅形式/语言类比。没有项目连接时 `projects: []`，也不打 project/relevance 标签。
- `concepts` / `entities`：既要包含 wiki 中已存在的条目，也要包含你在"新概念/实体建议"中提出的条目（这些将在第二步创建）。用 kebab-case 文件名主干。
- `methods`：计算方法（dft、dft-plus-u、gw、md、eam、mlip、dp-gen、berry-phase、ne b、dfpt…）、实验方法（stm-mbe、pxrd、raman、xps、afm-pfm、mfm、squid-magnetometry、xrd-tem、muon-sr、arpes、xanes-xrs、epr、cv-electrochemistry、device-i-v…）、理论模型（tight-binding、landau-ginzburg、phase-field、monte-carlo…）。论文用了什么就列什么。
- `materials`：论文核心研究的具体材料；被一句话带过的历史对比材料不必列。
- `tags/topic/...`：从论文主题出发打话题标签，常见的有 `topic/multiferroics`、`topic/2d-materials`、`topic/ferroelectricity`、`topic/charge-density-wave`、`topic/magnetism`、`topic/superconductivity`、`topic/humidity-sensing`、`topic/two-photon-fluorescence`、`topic/molecular-crystal`、`topic/ml-interatomic-potential`、`topic/domain-walls`、`topic/topological-defects` 等，按实际内容增减。
- 所有列表项保持 kebab-case；作者姓名照原文，不需 kebab。

### 正文格式

正文严格按以下格式（中文，准确，不编造）：

```
## <citekey> — <中文标题或英文标题>
- **元数据**：作者 et al.，年份，期刊，DOI
- **一句话**：本文最核心的贡献或发现
- **现有wiki双链**：本文涉及且 wiki 中已存在的条目，用双链列出（存在才链）：
  - 概念 [[../../wiki/concepts/xxx]]
  - 实体 [[../../wiki/entities/xxx]]
  - 图表 [[../../wiki/figures/xxx]]
  - 年度 [[../../wiki/write/YYYY]]
  - 项目 [[../../wiki/projects/xxx]]
  - 相关论文 [[../../raw/note/<citekey>]]
- **新概念/实体建议**：wiki 中没有、但值得新建的概念或材料实体，每个给 kebab-case 建议文件名 + 一句说明
- **关键图表**：列出本文关键图，格式 `![简述](../../raw/figures/<citekey>/<文件名>)`；若 raw/figures 下无图则写"笔记未附图片"
- **项目连接**：project-1 双光子 / project-2 Mn多铁 / project-3 机械发光NN / project-4 TTF分子计算 / project-5 SnTe铁电模拟 / project-6 湿度传感器 / project-7 CDW。**判定标准是内容对该项目有没有参考价值**（机制、方法、计算流程、可类比的材料/物理、可复用数据），**不是**这篇论文在 Zotero 里属于哪个文件夹/标签。方法学论文（DFT/GW/MD/应变工程/铁电理论等）即使不直接研究项目材料，也可能对 project-4、project-5 等计算项目有方法参考价值；综述/机理论文可能为 project-2、project-5、project-7 提供物理图像。逐条说明参考价值是什么；确实没有则写"无直接项目连接"。
- **组织与用词**：文章论证是如何组织的；以及 4-8 个值得在 wiki 叙述中复用的关键词/术语（中英对照）
- **可写入wiki的要点**：5-10 条 bullet，是可直接用于第二步充实 wiki 条目的具体事实、机制、数据、公式、结论
```

用 Write 工具写入该文件（UTF-8）。

## 最终回复
写完后，把 `tools/ingest_papers/<citekey>.md` 的**完整内容**作为你的最终文本回复返回（不要只说"已完成"，我要在控制台看到完整记录）。
