# 科研 Wiki 日志

> 时间导向的变更记录。每次 ingest / 重大修订追加一条，格式：`## [YYYY-MM-DD] <操作> | <标题>`。内容导向索引见 [[index]]。

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
  - 更新 [[wiki/topics/Z01-材料模拟计算设计]]，梳理了计算物理方向、关键材料体系与核心论文。
  - 更新 [[index]]，建立完整的概念、实体、主题、论文与图表索引体系，确保全库符合 [[SCHEMA]] 的双向链接规范。

## [2026-08-06] 初始化骨架

- 新建顶层 `科研Wiki/`，落地 Karpathy 三层架构：[[SCHEMA]]（Layer-3 契约）、[[index]]、`raw/`、`wiki/`、`figures/`、`tools/`。
- 编写 `tools/extract_figures.py`：按附件 key 定位 Zotero PDF，`pdfimages` 抽内嵌位图、过滤 logo（<350×350）、`pdftotext` 抓 `Fig. N.` 图注、矢量页 `pdftoppm` 整页 fallback；用 ASCII 临时目录绕过中文路径编码问题，输出 `manifest.json`。

## [2026-08-06] ingest | 多铁性 D02 试点 4 篇

- 论文卡片：[[raw/note/2005_Spaldin_The Renaissance of M_KEY-D72SE9HA]]（2005）、[[raw/note/2007_Ramesh_Multiferroics：progr_KEY-2V9G68K6]]（2007）、[[raw/note/2016_Fiebig_The evolution of mul_KEY-2USFQC4T]]（2016）、[[raw/note/2024_He_Ultrafast switching_KEY-ZTNTAL7L]]（2024）。
- 主题页：[[wiki/topics/D02-多铁性材料]]，链回厦门大会 D02 调研报告。
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
- **索引更新**：已更新 [[index]] 及 [[wiki/topics/Z01-材料模拟计算设计]] 主题导览页。
