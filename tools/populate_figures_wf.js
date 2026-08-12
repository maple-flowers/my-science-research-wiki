export const meta = {
  name: 'figures-populate',
  description: 'Populate 15 figures subpages with 762 missing images per update.md rules',
  phases: [
    { title: 'Populate', detail: 'one agent per figures subpage, add H3 entries' },
  ],
}

const BASE = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki'

const SUBPAGES = [
  { slug: 'mathematical-models', count: 239 },
  { slug: 'crystal-structures', count: 148 },
  { slug: 'experimental-setups', count: 107 },
  { slug: 'electronic-bands', count: 77 },
  { slug: 'optical-spectra', count: 51 },
  { slug: 'electronic-devices', count: 45 },
  { slug: 'heterostructures-stacking-multiferroic', count: 37 },
  { slug: 'domain-walls', count: 16 },
  { slug: 'vibrational-spectra', count: 13 },
  { slug: 'heterostructures-stacking-polar-cdw', count: 11 },
  // combined small batch: 5 pages, 18 images total
  { slug: 'SMALL_BATCH', count: 18, pages: [
    'heterostructures-stacking-reviews',
    'heterostructures-stacking-spintronics-strain',
    'heterostructures-stacking-mechanics-misc',
    'heterostructures-stacking-moire',
    'heterostructures-stacking-sliding',
  ]},
]

const RESULT_SCHEMA = {
  type: 'object',
  properties: {
    subpage: { type: 'string' },
    entries_added: { type: 'number' },
    files_written: { type: 'array', items: { type: 'string' } },
    split_into: { type: 'string', description: 'comma-separated subpage names if split, empty if not' },
    notes: { type: 'string' },
  },
  required: ['subpage', 'entries_added', 'files_written'],
}

function buildPrompt(slug) {
  return `You are curating a research wiki figures gallery at ${BASE}.

TASK: Populate the figures subpage "${slug}" with missing images, following the update.md formatting rules.

STEPS:
1. Read the work order: tools/_fig_wo/${slug}.json
   It is a JSON array of objects, each with: citekey, filename, alt, path.
   - "alt" is the Chinese description from the paper (e.g. "图3 CINEB 最小能量路径...")
   - "path" is the relative image path (../../raw/figures/<citekey>/<filename>.png)
2. Read the current page: wiki/figures/${slug}.md
3. Read the template example (first 80 lines): wiki/figures/domain-walls.md

FORMAT for each image entry (H3):
### N. <brief Chinese title derived from alt text>
<one-line Chinese description>

![图：<alt text>](<path>)
*   **来源**：[[../papers/<citekey>]]
*   **关键特征**：<optional one-line insight from alt>

For formula images (filename starts with eq_), use "公式：" prefix in alt instead of "图：".
For table images (filename starts with tab_), use "表：" prefix.

ORGANIZATION RULES:
- Group entries into H2 theme sections: ## emoji 中文 (English)
- Use appropriate emoji per theme (🔬 for experimental, 💻 for computation, 📐 for formulas, etc.)
- H3 numbering restarts at 1 within each H2 section
- KEEP ALL existing content in the page (existing H2/H3 entries, formulas, tables)
- Add new entries into appropriate H2 sections (create new sections if needed)
- Place new H3 entries at the END of the relevant H2 section

SPLITTING RULE (if total H3 entries > 50):
- Split into subpages named ${slug}-<theme>.md
- Convert ${slug}.md to a hub page: H1 + blockquote + return link + navigation table (subpage, theme, entry count)
- Each subpage: same format + return link to ${slug}.md
- Each subpage ≤ 50 entries
- Do NOT update _index.md (orchestrator handles that)

LINK RULES:
- Source: [[../papers/<citekey>]] (NEVER raw/note/)
- Image paths: use the "path" field from work order
- At the end, update 🔗 相关概念与实体 section with new relevant concepts/entities
  - Use Glob to verify wiki/concepts/<slug>.md or wiki/entities/<slug>.md exists before linking
  - 4-10 core concepts, 2-10 entities

Write the updated page(s) using the Write tool. Preserve the page's existing H1, blockquote, and return link.

Return the number of entries added and list of files written.`
}

function buildSmallBatchPrompt(pages) {
  return `You are curating a research wiki figures gallery at ${BASE}.

TASK: Populate ${pages.length} figures subpages with a small number of missing images each.

For EACH of these subpages, do the following:
${pages.map(p => `- ${p} (read tools/_fig_wo/${p}.json)`).join('\n')}

STEPS for each subpage:
1. Read tools/_fig_wo/<slug>.json (JSON array of {citekey, filename, alt, path})
2. Read the current page: wiki/figures/<slug>.md
3. Add new H3 entries following the format below
4. Write the updated page with the Write tool

FORMAT for each image entry (H3):
### N. <brief Chinese title from alt>
<one-line description>

![图：<alt>](<path>)
*   **来源**：[[../papers/<citekey>]]
*   **关键特征**：<optional>

For formula images (eq_*), use "公式：" prefix. For tables (tab_*), use "表：" prefix.

RULES:
- Keep ALL existing content; only ADD new entries
- Organize into existing or new H2 theme sections (## emoji 中文 (English))
- H3 numbering continues from existing entries in each H2 section
- Source: [[../papers/<citekey>]]
- No splitting needed (all small batches)
- Update 🔗 相关概念与实体 if new concepts emerge (verify slugs with Glob)

Process all ${pages.length} pages, writing each updated file.

Return total entries added across all pages, and list all files written.`
}

phase('Populate')

log('Starting figures population: 15 subpages, 762 images total')

const results = await parallel(SUBPAGES.map(sp => () => {
  const prompt = sp.slug === 'SMALL_BATCH'
    ? buildSmallBatchPrompt(sp.pages)
    : buildPrompt(sp.slug)
  return agent(prompt, {
    label: `populate:${sp.slug}`,
    phase: 'Populate',
    schema: RESULT_SCHEMA,
  })
}))

const valid = results.filter(Boolean)
log(`Done: ${valid.length}/${SUBPAGES.length} agents completed`)
for (const r of valid) {
  log(`  ${r.subpage}: ${r.entries_added} entries -> ${r.files_written.length} files`)
}

return valid
