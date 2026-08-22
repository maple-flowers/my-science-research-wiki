# Context

用户要求将 `wiki/concepts/` 与 `wiki/entities/` 下的**所有页面**扩展为可独立阅读、自包含的知识页，包括旧版 `index.md` 未计入正式条目的反链聚合页。当前只读盘点显示，目标规模约为：

- `wiki/concepts/`：1,173 页；
- `wiki/entities/`：506 页；
- 合计：1,679 页；
- 其中大量页面没有 frontmatter、没有 `status`，且正文不足 10 行；
- 少量页面已经达到或接近成熟模板，但仍需按新标准重新验收；
- 当前工作区已有用户与本会话的未提交修改，必须保留，不能覆盖、还原或自动提交。

本任务的目标不是把所有页面机械写成同样长度，也不是把 1,679 页全部标为 `mature`。最终目标是：**每个页面单独打开都能知道该术语/实体是什么、核心机制或结构是什么、与相近对象如何区分、知识库中有哪些可靠证据；证据不足的页面必须明确标成 `stub`，不得用常识或猜测填成伪百科。**

本计划供 Marvis 按阶段长期执行。默认不使用 Workflow，不并行写同一工作区；Marvis 直接逐批处理、每批验证、支持中断后通过重新扫描恢复。

---

# 一、不可违反的全局约束

## 1. 知识与链接层级

严格遵守 [SCHEMA.md](../../../../../swan_goose/宝宝/笔记库/sgg/科研Wiki/SCHEMA.md) 与 [wiki/format-spec.md](../../../../../swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki/format-spec.md)：

1. `raw/note/` 与 `raw/figures/` 是证据输入层，不直接手工编辑。
2. `wiki/papers/<citekey>.md` 是唯一允许直链 `raw/note/` 的 Wiki 页面。
3. concept/entity 页面引用论文一律使用 `[[../papers/<citekey>]]`，不得直接链接 `raw/note`。
4. 新增 concept、entity、paper、figure-hub 双链前，必须确认目标真实存在。
5. 图片只有在实际打开 PNG、核对图中内容和论文图注后才允许嵌入；不得根据文件名、编号或 manifest 描述直接猜图意。
6. 定量参数必须注明对象、条件、单位、实验/计算类型和论文来源；不同材料或不同条件的数据不得拼成一个“统一常数”。
7. 不联网补写事实；仓库证据不足时保持 `stub` 或 `developing`，明确说明证据缺口。

## 2. Git 与工作区安全

每次开始或恢复前执行只读预检：

```bash
git rev-parse --show-toplevel
git branch --show-current
git status --short
git diff --name-only
git diff --cached --name-only
git log -5 --oneline
```

将开始时 `git status --short` 中出现的所有路径记录为本轮保护集合。规则：

- 不执行 `git reset --hard`、`git clean`、`git stash`、`git checkout -- <path>` 或全局 `git restore`。
- 不覆盖由用户或其他会话正在修改的文件；发现目标页已变更时先读 diff，再决定是否接续，不能盲写。
- 不自动 commit、amend、push；每批只汇报改动，提交权留给用户。
- 不修改 `raw/`、`SCHEMA.md`、`wiki/format-spec.md`、`index.md`，除非后续用户单独批准规范或索引同步任务。
- 普通内容批次只修改该批目标页面；跨层迁移、重命名和入链修复必须作为独立批次。
- 写入前记录目标页内容哈希；写入时若哈希变化，说明存在并发修改，停止该页而不是覆盖。

---

# 二、先完成当前已排队的三个页面

在全量分类前，先完成现有任务：

1. `wiki/concepts/pl-quenching.md`
2. `wiki/concepts/exciplex.md`
3. `wiki/concepts/thermochromism.md`

理由：三页资料链已经明确，并会影响后续光物理别名、父子概念和反链聚合页的身份判断。

## 处理重点

### PL 淬灭

- 独立解释动态淬灭、静态淬灭、FRET/PET、电荷转移、TICT 和聚集猝灭；
- 使用寿命与强度联合判据区分动态/静态淬灭；
- Stern–Volmer 方程必须说明适用假设和上/下弯曲原因；
- 探针 1a/P1 的极性猝灭数据必须注明溶剂、激发方式和分子身份，不能混合不同论文口径。

### 激基复合物

- 区分 exciplex、excimer、基态电荷转移复合物、TICT 和普通碰撞猝灭；
- `exciplex` 作为一般概念，`charge-transfer-exciplex` 作为可能的子概念，不机械合并；
- 对 542 nm E 带使用“作者归属”“浓度/黏度依赖支持”等限定语，不能把稳态光谱写成已由超快动力学完全证明；
- 将双光子三重荧光、双光子聚合共引发和持久机械发光中的电荷转移激基复合物分别写清适用场景。

### 热致变色

- 区分真正的吸收颜色变化、发射热致变色与热激活强度变化；
- P1 在甘油中的响应必须说明 25–80 °C、黏度下降、溶剂弛豫和 LE→TICT 布居变化共同作用；
- 不把特定探针/介质的温区、峰位和灵敏度写成热致变色的普适参数。

三页各自完成单页 lint 后再进入全量盘点。

---

# 三、建立 1,679 页全量可重建清单

## 1. 新增可复用审计工具

仓库目前只有 `tools/update_raw_assets.py`，没有 concept/entity 全量 lint。为保证 1,679 页任务可中断恢复，新增一个单一、只读为默认的工具：

- `tools/audit_wiki_pages.py`

该脚本默认不修改页面，只扫描并输出到 stdout；允许用参数限制路径或输出 JSON 到系统临时目录。不要在知识库内新增永久进度日志。

建议接口：

```bash
python tools/audit_wiki_pages.py --summary
python tools/audit_wiki_pages.py --json /tmp/wiki-audit.json
python tools/audit_wiki_pages.py --paths wiki/concepts/pl-quenching.md wiki/entities/GaSe.md
python tools/audit_wiki_pages.py --strict
```

Windows 环境下临时 JSON 使用系统临时目录；若无法保存 checkpoint，则每次重新扫描，因为页面状态可确定性重建。

## 2. 每页扫描字段

脚本为每一页生成：

- `path`、`layer`、`slug`、H1、frontmatter title/type/status/tags；
- 行数、字符数、是否有 frontmatter；
- 是否有太奶导读、结构概览、机制/物性章节、相关论文、参数表、关联概念/实体；
- `papers:` 列表与正文 paper links；
- raw/note 违规链接；
- 图片链接与路径存在性；
- concept/entity 双链及断链；
- 入链数量、来自 paper card 的入链和普通 Wiki 入链；
- 同 slug 跨层碰撞；
- 规范化名称键、可能别名簇；
- 当前 DoD 缺口和候选页面身份类型。

## 3. 入链索引

反链聚合页的原始论文列表只能作为候选证据，不能直接当事实。建立下列反向索引：

- paper frontmatter `concepts:` / `entities:` → 目标页；
- paper 正文 `## 🔗 Wiki 双链` → 目标页；
- paper 正文普通双链 → 目标页；
- 其他 concept/entity/topic/project/figure 页 → 目标页。

优先级：paper frontmatter 和 paper 的 Wiki 双链区高于普通正文反链，但最终仍需读 paper card 与 raw note 核实。

## 4. 进度恢复

不新增 `wiki-expansion-log.md` 或长期流水账。恢复依据：

1. 页面内容和审计脚本可重新计算的 DoD；
2. 当前会话任务列表；
3. 系统临时目录中的短期 JSON checkpoint（可选）；
4. 用户后续自行创建的 Git 提交。

任务完成后删除临时 checkpoint，不污染知识库。

---

# 四、页面身份分类

每页必须先判断身份，再选择模板。分类结果至少包括以下六类。

## A. 规范概念/实体页 `canonical`

名称明确、目录正确、确实代表独立概念或具体实体。完整扩展机制、结构、证据、参数和图像。

## B. 短反链聚合页 `short-aggregation`

虽然只有几行和论文列表，但名称本身是有效独立术语。将反链作为候选论文，升级为最小自包含知识页；证据薄弱时保持 `stub`，不强行写成长篇。

## C. 同义词/别名页 `alias`

包括拼写变体、缩写/全称、单复数、连字符差异、材料俗名与规范名。用户要求所有页面都能独立读懂，因此不改成一行重定向，也不删除。别名页使用短型自包含结构：

- 首段直接说明它是哪个规范概念/实体的别名；
- 太奶导读；
- 名称与使用范围；
- 容易混淆的对象；
- 相关论文贡献句；
- 指向规范页。

别名页不复制规范页的全部机制、图片和参数，通常保持 `stub` 或 `developing`。

## D. 歧义词页 `ambiguous`

若一个术语对应多个物理含义、技术/信号、结构/材料或跨领域缩写，则写成“术语辨析”页：列出各含义、适用语境和真实目标链接。它应让读者单独打开即可选对方向，但不复制所有目标页正文。

## E. 跨层误放页 `misplaced`

抽象机制/模型应在 concepts，具体材料/软件/仪器/器件应在 entities。先只标记，不在普通扩展批次迁移。迁移必须按身份簇单独处理：

1. 选规范页；
2. 合并独有内容与论文集合；
3. 修复 paper 与全库入链；
4. 旧路径默认保留为可读别名/迁移说明页，除非用户另行批准删除；
5. 全库检查 stale link。

## F. 无证据或身份不确定页 `no-evidence`

保留页面，写最小自包含说明：名称大致指向什么、当前知识库为何不能确认具体机制/参数、当前暂无可核验论文。状态为 `stub`；不联网补数据，不配图，不伪造参数。

---

# 五、每个页面的统一 Definition of Done

## 1. 所有页面共同要求

- 文件首部有合法 frontmatter；
- 必含 `tags`、`title`、`type`、`status`；
- `tags` 首项为 `concept` 或 `entity`；
- `status` 仅为 `stub`、`developing`、`mature`；
- H1 与页面身份一致；
- 首段直接回答“这是什么”；
- 有 `## 👵 太奶导读`，用白话解释但不牺牲准确性；
- 有正文定义；canonical 页要解释机制/结构和近邻区别；
- 有 `## 📚 相关论文 (Related Papers)`；
- 每篇论文双链后有一句该论文对本页的具体贡献；
- 无论文时明确写“当前知识库暂无可核验论文”，不能留空标题；
- 有 `## 🔗 关联概念与实体 (Related Concepts & Entities)`；
- 关联链接真实存在，并说明关系；
- 无 raw/note 直链；
- `papers:` 与正文相关论文清单一致、有序去重；
- 不保留 TODO、模板占位符、转换日志或 Zotero 元数据噪音。

## 2. Concept 页完整要求

canonical concept 推荐结构：

1. H1 与总述；
2. 太奶导读；
3. 定义、方程或核心判据；
4. 微观/宏观机制；
5. 实验或计算识别方法；
6. 尺度、环境和边界条件；
7. 与最容易混淆概念的区别；
8. 应用与局限；
9. 相关论文；
10. 有可靠数值时的关键参数表；
11. 关联概念与实体。

别名/消歧/无证据概念页可用短模板，不复制规范页全文。

## 3. Entity 页完整要求

canonical entity 推荐结构：

1. H1 与对象总述；
2. 太奶导读；
3. `## 🏗️ 结构概览`；
4. 组成、结构、多型或模块/信号链；
5. 核心物性与机制；
6. 调控、制备、测量或器件用途；
7. 与同族/近邻实体的区别；
8. 相关论文；
9. 关键参数表；
10. 关联概念与实体。

软件、仪器和测量技术的“结构概览”应写模块、输入输出、信号链或实验几何，不强行套晶体结构模板。

## 4. 参数表

有可靠数值时使用：

```markdown
| 参数 | 数值 | 对象与条件 | 证据类型 | 来源 |
| :--- | :--- | :--- | :--- | :--- |
```

每项记录：样品/材料、温度、压力、厚度、浓度、波长、方向、计算方法等必要条件；明确实验值、计算值、拟合值或理论估计。条件不完整的数字不进入 frontmatter `key_quantities`。

无可靠数值时不强建空表；正文明确证据不足即可。

---

# 六、证据包构建与事实优先级

每页写作前建立 evidence bundle，按以下顺序读取：

1. 当前页面已有内容和 frontmatter；
2. `wiki/papers/<citekey>.md` 的一句话、关键图表、可写入 Wiki 要点和限定条件；
3. `raw/note/<citekey>.md` 中与当前概念直接相关的精确参数、样品条件、机制与局限；
4. `raw/figures/<citekey>/manifest.json` 的候选图、页码和描述；
5. 实际 PNG；
6. `wiki/figures/` 的策展说明；
7. 其他 concept/entity 页只用于术语一致性和关系，不作为无来源事实证据。

事实记录至少包含：

- claim；
- citekey；
- 证据位置；
- 对象/样品；
- 条件；
- 实验/计算/拟合类型；
- 置信度；
- 与其他论文冲突。

冲突处理：

- 条件不同的数据并列写，不平均；
- 实验值与计算值分开；
- 作者仅“归属/支持”的机制不得写成“证明”；
- raw note 中的“未来研究方向思考”不能当论文结论；
- 无法消解的冲突必须保守表述并降低 status。

---

# 七、图片视觉核验流程

任何新增图片必须逐张执行：

1. 确认文件存在；
2. 实际打开 PNG；
3. 识别图类型、坐标轴、单位、图例、panel、样品和实验/计算条件；
4. 对照 manifest 页码与描述；
5. 对照 paper card 的关键图表说明；
6. 三者一致后才嵌入；
7. 写当前页面专属的关键特征和来源。

格式：

```markdown
![图：<对象与当前页关键特征>](../../raw/figures/<citekey>/<filename>.png)
*   **关键特征**：<解释轴、曲线、颜色或结构如何支撑本页论点>
*   **条件**：<图中和论文明确给出的条件；没有则不猜>
*   **来源**：[[../papers/<citekey>]] -> [[../figures/<slug>|<图表分类>]]
```

已知约 42 张 PNG 未登记在 manifest 中。本轮不删除、不回填 raw manifest。来源未能通过目录、图中文字、paper card 和 raw note 共同确认前，不用于页面；必要时另报 raw 资产问题。

---

# 八、status 判定

## `stub`

- 只有最小定义/导读；
- 无可靠论文；
- 身份不确定；
- 短别名或消歧入口；
- 机制、图像或参数尚未核实。

## `developing`

至少有：明确身份、合法 frontmatter、太奶导读、机制/结构小节、至少一篇具体论文证据、相关论文贡献句、无违规链接；但仍缺机制覆盖、结构图、参数来源、近邻辨析或多论文综合。

## `mature`

必须全部满足：身份/目录正确；正文完整解释定义、机制/结构、判据、边界和近邻区别；关键论断就近有 paper link；所有论文有贡献句；参数带完整 provenance；必要图片全部视觉核验；frontmatter 与正文一致；机械 lint 与语义复核通过；无重大证据冲突。

现有 `mature` 页面也必须重新验收，不因原状态跳过；不达标时降为 `developing`。

---

# 九、执行阶段与批次顺序

## Phase A：安全基线

- Git 预检并建立保护集合；
- 运行全量审计；
- 记录基线 broken links、违规 raw links、frontmatter 缺口和图片缺失；
- 此阶段只读。

## Phase B：完成任务 10–12

依次完成 PL 淬灭、激基复合物、热致变色，每页单独验证。

## Phase C：身份解析

按 50 页只读批次建立：

- 同 slug 跨层碰撞；
- 规范化名称重复；
- 缩写/全称与拼写变体；
- 父子概念；
- 歧义词；
- 跨层误放；
- 无证据页。

身份未解决前不做大篇幅扩写。

## Phase D：高价值短聚合页

优先顺序：

1. 行数 ≤10；
2. 无 status；
3. 被 paper 高频引用；
4. 身份清楚；
5. 有至少两篇可信论文；
6. 与项目、图表或成熟页高度关联。

普通 canonical 页每批 6–8 页；复杂/图像密集页每批 2–4 页。

## Phase E：别名、消歧与无证据页

- 别名/消歧短模板每批 15–20 页；
- 无证据页每批 20 页；
- 每页仍需自包含，但不复制 canonical 长正文。

## Phase F：其余有证据 stub

按主题聚类：

- 铁电、多铁、畴壁与磁电；
- 二维材料、堆垛与滑移；
- 磁性、拓扑与超导；
- 光谱、光物理与非线性光学；
- 计算理论与模拟方法；
- 合成、加工和表征；
- 软件、仪器、材料和器件实体。

同主题批次复用术语上下文和论文读取缓存，但每页证据独立核验。

## Phase G：跨层误放和身份簇

每批只处理一个身份簇。需要全库改链或删除页面时先停下向用户汇报，不能混入普通写作批次。

## Phase H：现有 developing 复核

全量补齐缺口，只有真正达标才升 mature。

## Phase I：现有 mature 复核

全量检查裸论文链接、参数 provenance、图片视觉核验、frontmatter 一致性和正文证据；不达标则降级。

## Phase J：最终全库验收

全量机械 lint、全量链接与图片路径检查、所有 mature 页面逐页语义复验、数量和状态对账。

---

# 十、每批执行循环与失败恢复

每批固定流程：

1. 重新读取 Git 状态，确认没有意外并发修改；
2. 读取批次目标页并记录哈希；
3. 身份分类；
4. 构建证据包；
5. 先写事实提纲，再生成正文；
6. 逐图视觉核验；
7. 逐参数核验 provenance；
8. 只修改目标页；
9. 单页 lint；
10. 批次 lint；
11. `git diff --check`；
12. 检查实际 diff 只包含目标页；
13. 汇报完成页、status 变化、跳过页和问题，不提交。

单页最多三次尝试：

1. 正常综合；
2. 根据 lint 定向修复；
3. 缩减为诚实的 `developing`/`stub`，移除无法核验的图和参数。

仍失败则恢复该页的批前内容、标记人工复核，继续无依赖页面。回滚只能针对本轮目标页，禁止全仓库 reset。

---

# 十一、机械 lint 与语义复核

## 1. `tools/audit_wiki_pages.py` 检查项

- YAML/frontmatter 可解析；
- tags/title/type/status 存在且合法；
- H1、太奶导读、相关论文、关联概念实体存在；
- canonical entity 的 developing/mature 页有结构概览；
- concept/entity 无 raw/note 直链；
- paper、concept、entity 双链目标存在；
- 图片路径存在；
- 每张图有关键特征和来源；
- 每篇相关论文后有贡献说明；
- `papers:` 与正文列表一致；
- 无模板 placeholder、嵌套 wikilink、重复 H1/H2；
- `git diff --check` 无空白错误。

基线错误与新增错误分开统计：

```text
new_errors = post_batch_errors - baseline_errors
fixed_errors = baseline_errors - post_batch_errors
```

任何批次不得新增错误。

## 2. 语义复核

- 普通短页每批至少抽 20%，不少于 3 页；
- 复杂页、图片页、参数页、mature 候选全部复核；
- mature 最终全量复核，不能抽样。

复核问题：定义是否独立完整；机制是否准确；entity 是否写成具体对象；相关性是否误写成因果；理论是否误写成实验；参数条件是否完整；图片是否真支持论点；别名/父子页是否冲突；status 是否过高。

若抽检发现模板性错误，应回看整批同类页面，而不是只修抽中页面。

---

# 十二、Token 与上下文控制

1. 先用审计脚本分类，不把 1,679 页全文同时送入模型。
2. 每页只读取目标页、2–6 篇最高相关 paper card、raw note 命中段落和 1–3 个图候选。
3. SCHEMA/format-spec 在会话中提炼成固定约束，不每页重复全文读取。
4. 按 citekey 缓存已读论文摘要和参数，但每个页面只提取与自身直接相关的事实。
5. 先筛 manifest，再打开最终 PNG；不遍历打开所有 1,675 张图片。
6. 已有长页优先做缺口补丁，避免整页重写。
7. 别名、消歧、无证据页使用确定性短模板。
8. 每批完成立即 lint，避免最终集中返工。
9. 不启动 Workflow；Marvis 在主会话中顺序执行，确保用户可随时中断和审阅。

---

# 十三、最终验收与完成标准

最终报告必须包含：

- concepts、entities 和总页数；
- canonical/aggregation/alias/ambiguous/misplaced/no-evidence 各类数量；
- stub/developing/mature 分布；
- 无 status 页数量为 0；
- 无 frontmatter 页数量为 0；
- 无太奶导读页数量为 0；
- 无相关论文状态说明页数量为 0；
- concept/entity 直链 raw/note 数量为 0；
- 本轮新增 broken link 数量为 0；
- missing image 数量为 0；
- 本轮新增图片 100% 有视觉核验；
- 所有 mature 页 100% 通过语义复核；
- 所有定量参数具有条件和来源；
- 没有修改 raw；
- 没有覆盖保护集合；
- 没有自动提交；
- 没有新增无必要的库内维护日志。

最终“完成”不等于 1,679 页全部 mature，而是：

- 100% 页面单独打开即可知道它是什么；
- 100% 页面身份明确，或明确标注歧义/证据不足；
- 100% 页面遵守链接和来源规则；
- 证据充分的页面达到 developing/mature；
- 无证据页面保持诚实的 stub，而不是被填充成无来源长文；
- 同义/聚合页面既可独立理解，又不会大规模复制 canonical 页内容。

## 关键实施文件

- `SCHEMA.md`：全库目录、链接与 raw 层约束；
- `wiki/format-spec.md`：concept/entity 编写规范；
- `tools/audit_wiki_pages.py`：拟新增的全量只读审计与 lint 工具；
- `wiki/concepts/coercive-field.md`：参数条件、多论文综合和图像证据模板；
- `wiki/concepts/flexoelectric-effect.md`：证据边界与跨尺度机制模板；
- `wiki/concepts/density-functional-theory.md`：理论方法类 concept 模板；
- `wiki/entities/WTe2.md`：材料 entity 结构模板，但必须按新 DoD 重新复核；
- `wiki/concepts/pl-quenching.md`、`wiki/concepts/exciplex.md`、`wiki/concepts/thermochromism.md`：全量执行前优先完成的当前待办。
