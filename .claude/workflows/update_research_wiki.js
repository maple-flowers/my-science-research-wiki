export const meta = {
  name: 'update_research_wiki',
  description: '为 wiki/papers/ 中每篇论文条目补充「📊 关键图表」章节的中文描述（图示描述/关键特征/结论），资料取自 raw/note/。增量运行：已丰富的条目自动跳过。',
  phases: [
    { title: 'Discovery', detail: '列出 wiki/papers/*.md 并识别缺少图表描述的条目' },
    { title: 'Enrichment', detail: '逐篇扩写「📊 关键图表」章节，保留图片与链接原样' },
    { title: 'Report', detail: '汇总各篇处理状态' }
  ]
}

const REPO = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki'

const RESULT_SCHEMA = {
  type: 'object',
  properties: {
    citekey: { type: 'string' },
    status: {
      type: 'string',
      enum: ['enriched', 'already_rich', 'no_figures_section', 'no_raw_note', 'no_images', 'error']
    },
    images_before: { type: 'number' },
    images_after: { type: 'number' },
    notes: { type: 'string' }
  },
  required: ['citekey', 'status', 'images_before', 'images_after', 'notes']
}

function buildPrompt(citekey) {
  return `你正在为科研 Wiki 中一篇论文条目补充「关键图表」的中文描述。仓库根目录：
${REPO}

你的唯一目标：把这篇论文的 wiki 页 \`wiki/papers/${citekey}.md\` 中 \`## 📊 关键图表\` 这一节，从"只有一行图注+图片"扩写为"每张图都有 2–4 句中文描述 + 关键数据/特征要点"，资料来源是该论文的原始阅读笔记 \`raw/note/${citekey}.md\`。

# 工作步骤

1. 用 Read 读 \`${REPO}/wiki/papers/${citekey}.md\`，定位 \`## 📊 关键图表\` 这一节（从该 H2 开始，到下一个以 \`## \` 开头的章节为止，典型下一节是 \`## 🔬 项目连接\`）。
   - 数一下该节里有多少张图（按 \`![图\` 或 \`![](\` 计数，记为 images_before）。
   - 如果该节不存在（没有 \`## 📊 关键图表\` 标题），status = "no_figures_section"，直接写回文件时不改任何内容，只在 notes 里说明。
   - 如果该节每一张图下面**都已经**有 ≥2 行非空、非图片的中文描述（形如 \`  - **图示描述**：…\`、\`  - **关键特征**：…\` 或独立段落），说明已经足够丰富，不要再改写，status = "already_rich"，直接返回。

2. 用 Read 读 \`${REPO}/raw/note/${citekey}.md\`。
   - 在笔记里定位图表解析章节，常见标题是 \`## 三、所有图表深度解析\`、\`### 图表解析\`、\`## 三、图表解析\`、\`## Figures\` 或包含 \`图1\`、\`图 1\`、\`Fig. 1\` 的段落。
   - 把每个 \`#### 图N\` / \`#### 图 N\` / \`**图N**\` 下面的"图示描述"、"深度解析"、"关键结论"以及任何表格/公式说明提取出来。原始笔记是被引用块 \`> \` 包起来的，分析时忽略这些引用前缀。
   - 如果 raw/note 根本读不到（文件缺失或空），status = "no_raw_note"。

3. 用 Bash \`ls "${REPO}/raw/figures/${citekey}/"\` 列出实际存在的图片文件名（fig_*.png、tab_*.png、eq_*.png）。注意：
   - wiki 页里每个 \`![](.../fig_N_<hash>.png)\` 的 N 就是论文原图号 Fig. N。
   - raw/note 里的"图4, 图5, 图6"这种合并段要拆开，分别匹配 wiki 页里的 fig_4、fig_5、fig_6。
   - 表格（tab_1）和公式（eq_1）若 wiki 页没单独引用就不要硬塞；若已经以图片形式引用则同样补描述。
   - 文件名哈希编号 ≠ 图号这件事已经由 fig_N 前缀处理，但仍要核对 alt 文本里的图号一致。

4. 重写 \`## 📊 关键图表\` 这一节。规则：
   - **保留所有已有的 \`![](...)\` 图片行和后面的 \`→ [[...]]\` / \`-> [[...]]\` 图表页链接**，一字不改；顺序也保持不变。
   - 每张图上方或紧接着图片下方插入一个两五行的中文描述块，使用与现有内容一致的缩进（该节正文普遍以两个空格开头，如 \`  - **图示描述**：…\`、\`  - **关键特征/要点**：…\`）。
   - 描述结构固定为：
     * \`  - **图示描述**：<一句话说清这张图画了什么，坐标轴/子图/对比条件分别是什么>\`
     * \`  - **关键特征**：<2–4 个要点，箭头/曲线/对比读出的物理结论；定量数值（如 R²、能隙、温度、极化值、能垒）必须带上单位>\`
     * 可选 \`  - **结论/意义**：<一句话，这张图支撑了论文的哪条论断>\`
   - 若 wiki 页当前只有"图1: ……"一行纯文字而没有 \`![]()\` 图片（例如该论文 raw/figures 下确实没有对应图片），就在该行下补 \`  - **图示描述**\` 和 \`  - **关键特征**\` 两行，不要伪造图片。
   - 若整节没有任何图片（images_before = 0），但 raw/note 里确实有图：不要在 wiki 页里编造图片路径，只把每张关键图写成 "图N：<标题>" + 描述两 bullet，并在 notes 里说明"raw/figures 中缺失图片文件，已用文字描述"。status = "no_images"。
   - 若 raw/note 里根本没有图N 的描述（例如某些理论经典论文 DFT 方法学文献原本就没有实验图），就为该图写一句基于 wiki 页已有的图注 + frontmatter 信息的中性描述，不要编造数字；在 notes 里列出哪些图缺 raw 描述。
   - 不要删除该节里任何已有的 \`-> [[../figures/...]]\` 链接。
   - 不要改动 \`## 📊 关键图表\` 之前或之后的任何字符。

5. 用 Edit 工具把旧的 \`## 📊 关键图表\` 整节替换为新版本。old_string 必须从 \`## 📊 关键图表\` 那一整行开始，一直到（但不包含）下一个 \`## \` 章节标题为止。如果该节是文件最后一节，替换到文件末尾。
   - 用 Read 至少读过一次原文件后再 Edit，这是工具要求。
   - new_string 末尾保持一个空行，再衔接下一个 H2（Edit 不会改动下一个 H2）。

6. 改完后再次 Read 该节核对：所有 \`![]()\` 路径未变、描述块缩进正确、没有误删 \`-> [[...]]\`、没有引入 raw/note 的 \`> \` 引用前缀或 AI 转写噪声。

# 严禁事项
- 禁止直链 \`raw/note/\` 或 \`raw/figures/\` 在 wiki 正文（图片路径 \`../../raw/figures/...\` 是允许的）。
- 禁止模拟/编造数字：raw/note 没有就不要写数值，改写"定性描述"。
- 禁止改动 frontmatter、其他章节、citekey、其他论文的文件。
- 禁止把多个图合并成一个 bullet；每张图独立一个描述块。
- 禁止写 \`图N+1\`、\`见下图\` 这类相对引用——以图号为准。
- 禁止删除或重排现有图片；只增改描述文字。
- 禁止创建新文件。

# 返回值（严格 JSON，按 schema）
- citekey: "${citekey}"
- status: enriched | already_rich | no_figures_section | no_raw_note | no_images | error
- images_before / images_after: 该节内 \`![\` 计数（应相等）
- notes: 一句话说明做了什么、哪些图没有 raw 描述、是否有缺失图片文件等。出错时写错误信息。`
}

// 1. Discovery
phase('Discovery')
log('扫描 wiki/papers/，识别缺少图表描述的条目...')

const papers = await agent(`
用 Bash 列出目录中所有 markdown 文件：${REPO}/wiki/papers/
只取文件名（不含 .md 后缀）作为 citekey，排除 index.md。
对每个文件快速判断其 \`## 📊 关键图表\` 章节里，是否每张图都已有 \`**图示描述**\` / \`**关键特征**\` 这类中文描述。
返回所有 citekey，以及其中"尚未丰富、需要扩写"的 citekey 列表。
`, {
  label: 'discover-papers',
  schema: {
    type: 'object',
    properties: {
      all: { type: 'array', items: { type: 'string' } },
      pending: { type: 'array', items: { type: 'string' } }
    },
    required: ['all', 'pending']
  }
})

log(`共 ${papers.all.length} 篇论文，待扩写 ${papers.pending.length} 篇。`)

// 2. Enrichment (pipeline, parallel fan-out with concurrency cap)
phase('Enrichment')

const results = await pipeline(
  papers.pending,
  async (citekey) => {
    log(`扩写关键图表：${citekey}`)
    try {
      const r = await agent(buildPrompt(citekey), {
        label: `figures:${citekey}`,
        schema: RESULT_SCHEMA
      })
      return r || { citekey, status: 'error', images_before: 0, images_after: 0, notes: '空返回' }
    } catch (e) {
      return { citekey, status: 'error', images_before: 0, images_after: 0, notes: String(e) }
    }
  }
)

// 3. Report
phase('Report')
const tally = results.filter(Boolean).reduce((m, r) => {
  m[r.status] = (m[r.status] || 0) + 1
  return m
}, {})
log(`处理完成：${JSON.stringify(tally)}`)

const errors = results.filter(Boolean).filter(r => r.status === 'error' || r.images_before !== r.images_after)
if (errors.length) {
  log(`需复查 ${errors.length} 篇：${errors.map(e => e.citekey).join(', ')}`)
}

return { total: papers.all.length, processed: papers.pending.length, tally, errors }
