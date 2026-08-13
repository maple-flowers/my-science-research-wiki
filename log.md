# 科研 Wiki 日志

> 时间导向的变更记录。每次 ingest / 重大修订追加一条，格式：`## [YYYY-MM-DD] <操作> | <标题>`。内容导向索引见 [[index]]。


## [2026-08-13] cleanup | `tools/` 目录清理 22 个一次性文件

### 清理范围

- **`__pycache__/`**（1 个目录，25 KB）—— 8-13 figure 重建脚本留下的 .pyc 编译缓存。
- **8 个中间产物 JSON**（合计 ~3.4 MB，可由脚本重生成）：
  `figure_classified.json`（1.1 MB）、`figure_entries.json`（1.1 MB）、
  `figure_entries_full.json`（965 KB）、`figure_slug_map.json`（116 KB）、
  `stale_annotated_links.json`（1.6 KB）、`new_entries_g1.json`（6.3 KB）、
  `new_entries_g2.json`（4.1 KB）、`new_figure_entries.json`（10.3 KB）。
- **`FIGURE_GAPS.md`**（6.3 KB）—— figure 重建 session 的状态报告，已并入本日志。
- **12 个一次性修复脚本**（8-13 凌晨 1:00–2:00 那次"修 wiki/figures"session 跑出来的 one-off 补丁，
  共同特征是同样的 `import re, os, sys, glob` 模板，仅差几行修改逻辑）：
  `analyze_a.py`、`fix_a.py`、`fix_f_global.py`、`fix_f_tags.py`、`fix_figures.py`、
  `fix_figures_c3.py`、`fix_mechanical.py`、`fix_nested_links.py`、`fix_orphan_tags.py`、
  `fix_tag_format.py`、`fix_title_pollution.py`、`fix_titles.py`。

合计释放 **~3.4 MB**，`tools/` 从 41 个条目瘦身到 19 个 / 152 KB。

### 保留

- **12 个 git 跟踪的生产脚本**（未变）：`update_raw_assets.py`、`strict_verify.py`、
  `run_ingest.py`、`backfill_frontmatter.py`、`final_verify.py`（已修改未提交，详见下）、
  `count_figures.py`、`extract_metadata.py`、`extract_matrix_fields.py`、
  `extract_wiki_data.py`、`extract_writing.py`、`extract_spectra.py`、`extract_candidates.py`。
- **7 个未跟踪的 figure 重建脚本**（8-13 上午 10:00–12:00 跑出的，仍是工作流支撑代码），
  暂不 git add，留作近期审计/再处理用：
  `classify_figures.py`、`rebuild_figures.py`、`clean_stale_bare_links.py`、
  `extract_figures_full.py`、`verify_figures.py`、`update_paper_links.py`、
  `insert_new_figures.py`。

### 顺手做的事

- 新建根 `.gitignore`（之前不存在），加入 `__pycache__/` 防止 Python 缓存再污染。

### ⚠️ 待确认 1：`final_verify.py` 有未提交改动

`git status` 显示 `M tools/final_verify.py`：118 行新增 / 122 行删除，
本地版本（99 行）与 git HEAD（108 行）结构差异较大，可能是被某个 session 改写过逻辑。
需要 `git diff tools/final_verify.py` 完整 review 后决定 commit / revert / 调整。

### ⚠️ 待确认 2：`tools/extract_figures.py` 在文档中引用但物理上不存在

`update.md` 描述了 `python tools/update_raw_assets.py`（存在），但 `log.md` 2026-08-07
条目里有以下两处引用：
- "编写 `tools/extract_figures.py`：按附件 key 定位 Zotero PDF，`pdfimages` 抽内嵌位图、过滤 logo……"
- "用法：位图为主的论文用默认 `pdfimages` 模式；矢量综述用 `python tools/extract_figures.py --fitz <KEY>`"

现存 `extract_figures_full.py` 功能不同（**从 `wiki/papers/关键图表` 节抽条目元数据**，
不是从 Zotero PDF 抽图），不能替代原脚本。两种处置：
- A. 找回 `extract_figures.py`（从 git log 找旧版，或重新实现 pdfimages/pdftoppm/PyMuPDF 抽图逻辑）
- B. 改 `log.md` 改写为"该脚本被替换为更细的子命令"，但 `log.md` 是历史日志不该回改
- 建议 **A**：先 `git log --all -- tools/extract_figures.py` 看历史里有没有。



## [2026-08-13] refactor | 实体与概念去重：28 对 alias 合并

### 范围
基于 phase 0 审计（1290 页扫描），识别 31 个高置信 alias 候选；其中 28 对通过**软合并**（dead 页→redirect stub + live 页添加 alias 字段），3 对未执行（详见末尾"未合并"）。

### 软合并机制
对每个 alias 对：
- **Live 页** frontmatter 添加 `aliases: [...]` 数组（新别名追加在末尾）
- **Dead 页** 改为最小 redirect stub：
  ```yaml
  ---
  status: alias
  redirect_to: ../../<type>/<live-slug>
  merged_into: "<live H1>"
  ---
  # <原 H1>
  > ⚠️ **本页面已合并**到 [[../../<type>/<live-slug>|<live H1>]]...
  ```

### 合并明细

#### 跨类型（concept → entity）：2 对
- `concepts/ccps-cucrp2s6` → `entities/CuCrP2S6`（CCPS 缩写）
- `concepts/cips-cu-in-p2s6` → `entities/CuInP2S6`（CIPS 缩写）

#### 概念内：26 对
**domain-walls 家族**（10 个变体全部合并到主 `domain-walls`）：
- `ferroelectric-domain-wall`, `domain-wall-classification`, `domain-wall-nucleation`, `domain-wall-pinning`, `domain-wall-texture`, `domain-wall-conduction`, `domain-wall-electronics`, `domain-wall-energy`, `domain-wall-engineering`, `domain-wall-motion`

**其他物理概念**（13 对）：
- `magnetic-skyrmion` → `skyrmion`
- `spin-spiral-multiferroics` → `spin-spiral`
- `linear-response-u` → `linear-response`
- `dftb-density-functional-tight-binding` → `tight-binding`
- `electron-counting-rule-surface` → `electron-counting-rule`
- `depletion-layer-readout` → `depletion-layer`
- `mcmillan-ginzburg-landau-theory` → `ginzburg-landau`
- `adsorption-energy-landscape` → `adsorption-energy`
- `optical-humidity-sensing` → `humidity-sensing`
- `negative-piezoelectricity` → `piezoelectricity`
- `second-principles-calculations` → `second-principles`
- `interfacial-phase-change-memory` → `phase-change-memory`
- `debye-screening-length` → `screening-length`
- `ferroelectric-nonlinear-anomalous-hall-effect` → `hall-effect`
- `inverse-rashba-edelstein-effect` → `edelstein-effect`
- `charge-density-mixing` → `charge-density`

### 验证结果
- 28/28 redirect 目标全部存在
- 21 处 wiki 内部 backlink（如 paper 卡片）现在走 redirect 跳转，仍有效
- 19 个 live 页增加 alias 字段（`domain-walls` 增 10 个，其余 1 个）

### 未合并的候选（3 对）
- `entities/ABINIT` 与 `entities/VASP` 同为 DFT 软件但是独立项目，**不合并**
- `entities/b-AsP`（β-AsP）是与 black-phosphorus 不同的材料，**不合并**
- `entities/PFM` 有独立 frontmatter 与定义性内容，**不合并**
- `concepts/cipse-cu-in-p2se6`（CIPSe）的目标 `CuInP2Se6` 不存在，**暂留 dead 等未来增页**

### 后续
- 阶段 1 廉价清理（修 typo、补 status 字段）尚未执行
- 阶段 2 智能重写（按 Tier A/B/C 成熟化）待启动
## [2026-08-12] feat | 写作库改为五年段语料库并完成中文化

### 变更内容

- **结构重组**：删除 38 个单年文件（`1945.md`…`2026.md`、`Unknown.md`，旧 `### From:` 逐篇堆砌格式），新建 7 个五年段文件：`1945-1999.md`、`2000-2004.md`、`2005-2009.md`、`2010-2014.md`、`2015-2019.md`、`2020-2024.md`、`2025-2029.md`；重写 `_index.md`，新增跨段高频模式页 `_patterns.md`。
- **删除模拟语料**：`wiki/write/example.md`（英文例句系模拟，非真实语料）已删除，杜绝被误当真实句引用。
- **统一头部**：七个段文件统一为 `# <YYYY–YYYY> Writing Synthesis: <英文主题>` + `[[_index|← 返回写作索引]]` + 中文说明 blockquote + `---`，无 frontmatter；正文统一 8 个 H2（✍️0 Title … 🧬7 Evolution），表头统一 `实例 | 直译 | 骨架拆解`，经典案例小标题统一 `### 🧩 经典案例逐句拆解：<描述>`，来源行统一 `> **来源**：截取自 ...`（不用 `[!quote]`）。
- **中文化讲解**：所有"我写的"综述/分析散文、`**语法点**`、`**核心教训**`、引导语改为中文；论文逐字原句、①–⑥编号句、blockquote、"骨架拆解"列的英文句型模板一律保留英文。共翻译约 92 段（2000-2004≈15、2010-2014 19、2015-2019 21、2020-2024 37），1945-1999/2005-2009/2025-2029 讲解本就是中文。
- **校验**：脚本核对全部 8 个文件 8 个 H2 齐全、1288 条 `[[../papers/<citekey>]]` 链接 0 断裂；正文无成段遗漏的英文综述（扫描阈值：英文>60 字符且中文<5 的非引用行）。

### 维护经验（write/ 批量任务）

1. **语料真实性是铁律**：英文例句必须逐字摘自 `raw/note/*.md` 的 `❸ 双语转写`，不可模拟/改写/凭印象补。某时间段可读论文少时（如 2000-2004 仅 8 篇、2015-2019 仅 9 篇真正相关），宁可该段薄也不编造——agent 主动报告缺口而非凑数是正确行为。
2. **讲解中文、原句英文的边界要给死**：批量翻译时必须明确"只译我写的分析散文，保留引号原句/骨架模板/citekey/wikilink"，否则 agent 容易把论文原句也翻了或漏译综述段。
3. **并行 agent 要在 prompt 里自包含**：每个段文件一个 agent，prompt 写清保留项清单；但它们会"擅自"改 H1（如把英文 H1 译成中文），收尾必须统一核对 H1 系列一致性。
4. **链接校验用精确正则**：`\[\[\.\./papers/([^|\]#<>]+)`，并先把 Obsidian 转义 `\|` 替换成 `|`，否则 `citekey\` 会被误判为断链；`<citekey>` 这种字面示例要在判断时排除。
5. **frontmatter 里不要留指向临时文件的路径**：早期 `source_notes: [tools/_write_notes_*.md]` 在临时文件删除后变成死引用，已移除。段文件一律无 frontmatter。
6. **避免在 Windows 内联 Python 里写反斜杠转义**：`rstrip('\\')` 在内联 `python -c` 中易触发 `SyntaxError`，复杂校验逻辑写成临时 .py 文件用 `PYTHONUTF8=1` 跑，跑完删除。

## [2026-08-12] refactor | 编写规范拆分为 wiki/format-spec

- **SCHEMA.md 瘦身**（824 → 76 行）：六大条目编写规范（图表库 / 概念与实体 / 论文条目 / 写作库 / 主题 / 项目）全部移出，独立成 [[wiki/format-spec]]；SCHEMA 只保留目录约定、标签体系、核心链接规范、铁律与指引。目录约定树同步加入 format-spec.md 元页面。
- 最终职责划分：[[SCHEMA]] = 规范总纲（约定/链接/铁律），[[wiki/format-spec]] = 条目编写格式规范（怎么写），[[log]] = 时间记录 + 踩坑经验。

## [2026-08-12] refactor | Papers / Figures 维护经验（2026-08 批量校对）

> 本批整理 `wiki/papers/` 与 `wiki/figures/` 时踩过的坑与确立的规则，供后续批量任务复用（原为 SCHEMA 附录，2026-08-12 经 `wiki/maintenance.md` 中转后并入本时间导向日志）。

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

## [2026-08-12] refactor | 交接文档全部待办清零

- **论文格式统一（188 篇）**：将扁平 `- **bold-label**：` bullet 和 `### ` 标题统一转换为 `## emoji 标题` 层级格式（📄元数据 / 💡一句话 / 🔗Wiki双链 / 📊关键图表 / 🔬项目连接 / 📝组织与用词 / ✏️可写入Wiki要点 / 🆕新概念实体建议）。
- **Frontmatter 修复（4 篇）**：2019optical、Barnett2006coexistence、bhowalPolarMetalsPrinciples2023b、deSousa2008electrical 的 `"key:": value` 误改全部修正为 `key:: value`（双冒号无引号），每篇 11 个字段。
- **术语整理完成（238 项）**：完成 10 个因 429 失败批次的全部剩余术语判定——83 alias、9 create、146 skip。新建 9 个概念 stub 页（phason、point-charge-model、LSPR、bandwidth-controlled Mott transition 等），34 篇论文新增 49 条双链。
- **最终校验**：papers/ 目录 0 断链、0 AI残留、0 自引用、0 占位符。修复 PZT.md 中 `gittel-ortiz` → `gomez-ortiz` 拼写错误、gomez-ortiz 论文中 `../entities/PHONOPY` → `../concepts/PHONOPY` 路径错误。
- **临时产物清理**：删除 `_wo/`、`_term_batches/`、`_stub_batches/`、`__pycache__/`、15 个 `_*.py` 生成脚本、6 个 `_*.json` 中间数据（保留 `_paper_fig_map.json` 和 `_img2page.json`）、9 个历史临时文件。

## [2026-08-08] refactor | 重构 Wiki 库，合并原笔记，简化图片库并重写链接

- **Git 版本管理**：在 `科研Wiki` 目录初始化 Git。
- **笔记迁移**：将原 `爱看论文的猫猫/note` 目录移动到 `科研Wiki/raw/note` 作为第一层原始笔记输入。
- **图片库简化**：删除 `figures/` 下所有 PNG 剪裁图片文件，仅保留各论文的 `manifest.json` 图表文字描述与标签索引，实现仓库轻量化。
- **移除 Annotator 标注**：彻底删除 Obsidian Annotator 插件的 `raw/annotations` 目录，并从所有 markdown 文件中清除对其的链接和引用文本。
- **平铺层级架构 (删除 wiki/papers)**：删除了第二层增强型 `wiki/papers` 卡片目录。
- **重写双向链接**：对全仓库所有主题 (topics)、概念 (concepts)、实体 (entities)、项目 (projects)、索引页 (index.md/SCHEMA.md) 里的 `wiki/papers/<KEY>` 双向链接全部重写为 `raw/papers/<KEY>`。
- **相对路径更正**：更新了 `raw/papers/*.md` 文献指针页中的原始笔记相对路径，由原先的外部路径 `../../../爱看论文的猫猫/note/` 修正为本地相对路径 `../note/`。

---

## [2026-08-10] refactor | 重写资产同步逻辑与学术写作 Wiki 自动化

- **资产同步逻辑重构 (`update_figures_metadata.py`)**：
    - **精准定位**：通过 `cli-anything-zotero` 命令行工具动态查询 Zotero 本地数据库，提取“Zotero Figure 结果”笔记的 `attachment_key`，解决了笔记中缺失 key 的问题。
    - **严格图片白名单**：修正了误同步 PDF 的问题，目前仅同步 `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp` 格式图片。
    - **多资产提取**：不仅提取 Figures（图），还同步支持提取 Tables（表）和 Formulas（公式）进入 `manifest.json`。
    - **本地存储优化**：图片统一重命名为 `fig_{num}_{key}.ext` 存储在 `raw/figures/{citekey}/` 目录下。
- **学术写作 Wiki 自动化 (`generate_writing_wiki.py`)**：
    - **年度聚合**：自动识别文献年份，在 `wiki/write/` 目录下生成 `[YYYY].md` 年度写作总结。
    - **模块化归类**：从双语转写中提取英文原句，并按 `Introduction`, `Methods`, `Results & Discussion`, `Conclusion` 进行归类。
    - **AI 噪声过滤**：引入负向关键词列表，彻底过滤 LLM 自主思考、指令等非论文原句内容。
    - **导航索引**：生成 `wiki/write/_index.md` 作为写作思路与用词的快速检索入口。
- **项目结构调整**：
    - 更新 `index.md` 以包含新增的写作 Wiki 模块。
    - 启动 `update_entities.py` 开发，旨在自动化更新 `wiki/entities/` 下的材料与方法词条。

---


- **深度概念与实体构建**：
  - 基于 135 篇论文增强卡片的全量内容分析，在 `wiki/concepts/` 与 `wiki/entities/` 中完成了计算材料学（二维铁电、多铁性、磁电耦合、滑动铁电、莫尔超晶格等）领域核心概念与材料实体的系统扩展与知识网络构建。
- **概念页新增与重构 (10 页)**：
  - [[wiki/concepts/sliding-ferroelectricity|sliding-ferroelectricity (滑动/堆叠铁电性)]] — 补全微观机制、低势垒与超快开关特性、核心材料及 12+ 篇关联论文。
  - [[wiki/concepts/moire-superlattice|moire-superlattice (莫尔超晶格)]] — 新建。覆盖莫尔铁电、莫尔磁性、超顺电相变及光电/突触器件应用。
  - [[wiki/concepts/polarization-switching|polarization-switching (极化翻转动力学)]] — 新建。对比均匀翻转与畴壁运动、应变与栅压驱动开关动力学。
  - [[wiki/concepts/topological-defects|topological-defects (拓扑缺陷与拓扑极化/磁序)]] — 新建。涵盖极化斯天明/涡旋、击穿 Kittel 律及磁拓扑控制。
  - [[wiki/concepts/2D-materials|2D-materials (二维范德华材料)]] — 新建。涵盖低维铁性物理突破、临界厚度极限及 60 篇计算论文分类。
  - [[wiki/concepts/machine-learning-potential|machine-learning-potential (机器学习势与大尺度模拟)]] — 新建。阐述近 DFT 精度大尺度 MD 在莫尔超晶格与畴壁研究中的突破。
  - [[wiki/concepts/ferroelectric-tunnel-junction|ferroelectric-tunnel-junction (铁电隧道结与 FTJ 器件)]] — 新建。聚焦二维滑动铁电隧道结与类脑突触应用。
  - [[wiki/concepts/multiferroicity|multiferroicity (多铁性)]]、[[wiki/concepts/magnetoelectric-coupling|magnetoelectric-coupling (磁电耦合)]]、[[wiki/concepts/super-paraelectricity|super-paraelectricity (超顺电性)]] — 补全二维延伸与交叉链接。
- **实体页新增与更新 (10 页)**：
  - [[wiki/entities/h-BN|h-BN (六方氮化硼)]] — 新建。原形滑动铁电体、莫尔超晶格与 FTJ 势垒层。
  - [[wiki/entities/TMDs|TMDs (过渡金属硫族化合物)]] — 新建。3R-MoS₂/WSe₂ 滑动铁电、单层 NiI₂ 多铁性及 1T'-WTe₂ 铁电金属。
  - [[wiki/entities/In2Se3|In2Se3 (硒化铟)]] — 新建。本征面内/面外联动铁电性与铁弹性。
  - [[wiki/entities/MXenes|MXenes (过渡金属碳/氮化物)]] — 新建。高导电性、预测亚铁磁/多铁性及自由立式忆阻薄膜。
  - [[wiki/entities/Fe3GeTe2|Fe3GeTe2 (铁锗碲)]] — 新建。双层层间滑动诱导磁性铁电金属相。
  - [[wiki/entities/domain-wall|domain-wall (畴壁)]] — 更新。扩充滑动铁电中超宽畴壁、超高移动速度（~6000 m/s）及导电相畴壁。
  - [[wiki/entities/deep-potential|deep-potential (机器学习势)]] — 更新。阐述 DeePMD-kit + DP-Gen 在超快畴壁与莫尔超晶格研究中的工作流。
  - [[wiki/entities/BiFeO3|BiFeO3]]、[[wiki/entities/HoMnO3|HoMnO3]] — 保持并丰富了双向链接。
- **主题页与总索引更新**：
  - 更新 [[材料模拟计算设计]]，梳理了计算物理方向、关键材料体系与核心论文。
  - 更新 [[index]]，建立完整的概念、实体、主题、论文与图表索引体系，确保全库符合 [[SCHEMA]] 的双向链接规范。

## [2026-08-06] 初始化骨架

- 新建顶层 `科研Wiki/`，落地 Karpathy 三层架构：[[SCHEMA]]（Layer-3 契约）、[[index]]、`raw/`、`wiki/`、`figures/`、`tools/`。
- 编写 `tools/extract_figures.py`：按附件 key 定位 Zotero PDF，`pdfimages` 抽内嵌位图、过滤 logo（<350×350）、`pdftotext` 抓 `Fig. N.` 图注、矢量页 `pdftoppm` 整页 fallback；用 ASCII 临时目录绕过中文路径编码问题，输出 `manifest.json`。

## [2026-08-06] ingest | 多铁性 D02 试点 4 篇

- 论文卡片：[[raw/note/2005_Spaldin_The Renaissance of M_KEY-D72SE9HA]]（2005）、[[raw/note/2007_Ramesh_Multiferroics：progr_KEY-2V9G68K6]]（2007）、[[raw/note/2016_Fiebig_The evolution of mul_KEY-2USFQC4T]]（2016）、[[raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]（2024）。
- 主题页：[[多铁性材料]]，链回厦门大会 D02 调研报告。
- 概念页：multiferroicity、magnetoelectric-coupling、sliding-ferroelectricity、super-paraelectricity。
- 实体页：BiFeO3、HoMnO3、domain-wall、deep-potential。
- 原始指针页：`raw/papers/{ZTNTAL7L,D72SE9HA,2V9G68K6,2USFQC4T}.md`。
- 图表：ZTNTAL7L Fig.1–8 已逐张中文标注（含 Fig.6/7 据用户反馈修正：page 7 两张位图分别为 Fig.6 畴壁运动、Fig.7 莫尔超顺电回线，删除误渲的 page 8 裁剪）；3 篇综述共 10 张图已核对。
- 汇总：[[figures/_figure-index]]。

### 待办 / 已知问题
- [ ] 用户在 Obsidian 目视确认 3 篇综述的图号与子图归属（24 张图中的 16 张综述图），确认后回填 manifest 与卡片。
- [x] 跑通端到端 query（如"畴壁运动如何降低开关场"）验证双链。
- [ ] 试点验收后，再讨论批量处理剩余约 70 篇论文。

## [2026-08-07] vision | 视觉识别能力启用

- **能力确认**：Claude 已具备原生多模态视觉识别能力，可直接读取并分析 Wiki 中的图片（`.png`, `.jpg`）。
- **流程简化**：取消原定“用户目视核对图号”的强制环节，LLM 可自主结合图片内容与论文正文进行标注。
- **标注计划**：即刻启动对 3 篇综述共 16 张 `needs_review` 图片的视觉识别与回填。

## [2026-08-07] upgrade | 集成文献鸟自动流与 Zotero 分类

- **自动化配置**：部署 `stork_daily.py` 定时任务（07:45），实现“邮件→Markdown日报→Zotero自动入库”闭环。
- **Zotero 分类**：新增关键词自动分流规则（MXene → `GABWBGQR`, CDW → `JICDY9YW`），其余进`文献鸟推送`。
- **架构升级**：更新 [[SCHEMA]]，明确 `raw/文献日报/` 为 Wiki 的第一层源头之一；定义“从日报发现到 Wiki 增强”的升级路径。
- **路径重定向**：将日报存储位置移至 `科研Wiki/raw/文献日报/`。

- 问题：3 篇老综述（D72SE9HA/2V9G68K6/2USFQC4T）的 figure 是**矢量线图+嵌入位图碎片**，`pdfimages` 只抽到零碎位图（被当成 logo），真正的图框/坐标轴/图注全是矢量路径，抽不出来；且图注写 "the first/second figure" 而非 "Fig. N."，旧矢量页 fallback 没触发。
- 安装 PyMuPDF（`pip install pymupdf`）。脚本新增 `--fitz` 模式：对每页的矢量路径 + 光栅图做并查集聚类（12pt 间隙合并），剔除整页背景框、文字块（文字密度高且矢量路径<15、无位图）和订购/版权横线（路径<3），对重叠>90% 的框去重，再把紧贴图底的图注文本块并入，按 200 DPI 整块裁剪渲染。
- 重抽结果：D72 2 张、Ramesh 5 张、Fiebig 9 张（共 16 张，带图注），删除旧的 logo png。更新三篇论文卡片与 [[figures/_figure-index]]。图号由 LLM 视觉识别核对。
- 用法：位图为主的论文（如 ZTNTAL7L）用默认 `pdfimages` 模式；矢量综述用 `python tools/extract_figures.py --fitz <KEY>`.


## [2026-08-07] ingest | 批量同步论文 (5 篇)

- 自动批处理摄入 5 篇论文笔记（研究论文 5 篇，综述论文 0 篇）。
- Review 论文依 SCHEMA 规范已自动剥离抽图逻辑。


## [2026-08-07] ingest | 批量同步论文 (15 篇)

- 自动批处理摄入 15 篇论文笔记（研究论文 15 篇，综述论文 0 篇）。
- Review 论文依 SCHEMA 规范已自动剥离抽图逻辑。


## [2026-08-07] ingest | 批量同步论文 (20 篇)

- 自动批处理摄入 20 篇论文笔记（研究论文 20 篇，综述论文 0 篇）。
- Review 论文依 SCHEMA 规范已自动剥离抽图逻辑。


## [2026-08-07] ingest | 批量同步论文 (50 篇)

- 自动批处理摄入 50 篇论文笔记（研究论文 47 篇，综述论文 3 篇）。
- Review 论文依 SCHEMA 规范已自动剥离抽图逻辑。


## [2026-08-07] ingest | 完成全量论文笔记同步 (138 篇)

- **全量同步完成**：成功对 `爱看论文的猫猫/note` 下全部 138 篇 Markdown 笔记与 Zotero 库进行自动化摄入与三层 Wiki 架构构建。
- **图表提取与 Review 规则**：完成 118 篇 Original Research 论文的 3,562 张图表与 JSON Manifest 提取；自动跳过 Review 论文抽图。
- **索引更新**：已更新 [[index]] 及 [[材料模拟计算设计]] 主题导览页。


