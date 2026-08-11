export const meta = {
  name: 'update_research_wiki',
  description: 'Intelligent synthesis workflow to update all Wiki folders (concepts, entities, write, etc.) based on raw note changes.',
  phases: [
    { title: 'Discovery', detail: 'Identify new or modified paper notes in raw/note/' },
    { title: 'Expansion', detail: 'Identify and initialize missing Wiki pages for recurring materials/concepts' },
    { title: 'Mapping', detail: 'Map papers to concepts, entities, and topics' },
    { title: 'Synthesis', detail: 'Update wiki/ folder pages with synthesized content and images' },
    { title: 'Writing analysis', detail: 'Extract academic sentences and rebuild wiki/write/' },
    { title: 'Indexing', detail: 'Rebuild index.md and topic pages' },
    { title: 'Cleanup', detail: 'Remove temporary byproduct files from tools/' }
  ]
}

const GLOBAL_TEMP_INSTRUCTION = `
IMPORTANT:
1. If you need to create any temporary scripts, data files, or byproducts, you MUST place them in the 'tools/' directory. Do not create files in the root directory.
2. When referencing figures or images, ALWAYS use standard markdown image syntax with relative paths.
   - For files in 'wiki/concepts/', 'wiki/entities/', 'wiki/topics/', 'wiki/projects/', or 'wiki/figures/', the path to a figure should be '../../raw/figures/{citekey}/{filename}'.
   - Example: ![Figure Title](../../raw/figures/CiteKey/fig_1_XYZ.png)
   - DO NOT just provide a text link.
`;

// 1. Discovery Phase
phase('Discovery')
log('Scanning raw/note/ for paper list...')

const papersData = await agent(`
${GLOBAL_TEMP_INSTRUCTION}
List all 531 markdown files in 'E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\raw\\note' and extract their citekey, title, year, materials, and methods.
Return this as a JSON array of objects: {citekey, title, year, materials, methods}.
`, {
  schema: {
    type: 'object',
    properties: {
      papers: {
        type: 'array',
        items: {
          type: 'object',
          properties: {
            citekey: { type: 'string' },
            title: { type: 'string' },
            year: { type: 'string' },
            materials: { type: 'array', items: { type: 'string' } },
            methods: { type: 'array', items: { type: 'string' } }
          },
          required: ['citekey', 'title']
        }
      }
    },
    required: ['papers']
  }
})

log(`Discovered ${papersData.papers.length} papers.`)

// 2. Expansion Phase
phase('Expansion')
log('Analyzing gaps and initializing new wiki pages...')

await agent(`
${GLOBAL_TEMP_INSTRUCTION}
1. Analyze the list of papers and their metadata (materials/methods).
2. Compare with current Wiki structure:
   - Concepts: 2D-materials, ferroelectric-tunnel-junction, machine-learning-potential, magnetoelectric-coupling, moire-superlattice, multiferroicity, polarization-switching, sliding-ferroelectricity, super-paraelectricity, topological-defects.
   - Entities: BiFeO3, deep-potential, domain-wall, Fe3GeTe2, h-BN, HoMnO3, In2Se3, MXenes, SnTe, TMDs.
3. IDENTIFY at least 10 high-impact missing pages (e.g., specific materials like WTe2, CrTe2; methods like Wannier90; concepts like Berry Phase).
4. INITIALIZE these pages in 'wiki/entities/', 'wiki/concepts/', or 'wiki/topics/' if they don't exist.
5. Each new page should have YAML frontmatter and a Level 1 heading.
`)

// 3. Mapping Phase
phase('Mapping')
log('Mapping papers to the expanded wiki structure...')

const wikiMap = await agent(`
${GLOBAL_TEMP_INSTRUCTION}
List all wiki markdown files in:
- E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\concepts\\
- E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\entities\\
- E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\topics\\
- E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\projects\\ (excluding index.md)
- E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\figures\\ (excluding _index.md)
Return a JSON structure of {concepts: [filename], entities: [filename], topics: [filename], projects: [filename], figures: [filename]}.
`, {
  schema: {
    type: 'object',
    properties: {
      concepts: { type: 'array', items: { type: 'string' } },
      entities: { type: 'array', items: { type: 'string' } },
      topics: { type: 'array', items: { type: 'string' } },
      projects: { type: 'array', items: { type: 'string' } },
      figures: { type: 'array', items: { type: 'string' } }
    },
    required: ['concepts', 'entities', 'topics', 'projects', 'figures']
  }
})

log(`Mapped ${wikiMap.concepts.length} concepts, ${wikiMap.entities.length} entities, ${wikiMap.projects.length} projects, and ${wikiMap.figures.length} figure categories.`)

// 4. Synthesis Phase
phase('Synthesis')

// Pipeline for all wiki folders
const allWikiTasks = [
  ...wikiMap.concepts.map(f => ({ path: `wiki/concepts/${f}`, type: 'concept' })),
  ...wikiMap.entities.map(f => ({ path: `wiki/entities/${f}`, type: 'entity' })),
  ...wikiMap.topics.map(f => ({ path: `wiki/topics/${f}`, type: 'topic' })),
  ...wikiMap.projects.filter(f => f !== 'index.md').map(f => ({ path: `wiki/projects/${f}`, type: 'project' }))
]

await pipeline(
  allWikiTasks,
  async (task) => {
    log(`Synthesizing ${task.type}: ${task.path}`)
    const fullPath = `E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\${task.path.replace(/\//g, '\\')}`
    await agent(`
      ${GLOBAL_TEMP_INSTRUCTION}
      Expert materials science researcher task:
      1. Read the file: ${fullPath}.
      2. Find ALL relevant papers in raw/note/ (using the 531 papers).
      3. INTEGRATE new findings, data, and mechanisms into the narrative.
      4. IMAGE INSERTION: Find matching figures in raw/figures/ and insert them using standard Markdown:
         ![Description](../../raw/figures/CiteKey/filename)
      5. Ensure links [[../../raw/note/CiteKey|Title]] are correct.
      6. REWRITE the file ${fullPath} directly with complete, updated knowledge.
    `)
  }
)

// Pipeline for Figure library updates
await pipeline(
  wikiMap.figures,
  async (figureFile) => {
    if (figureFile === '_index.md') return;
    log(`Updating figure category: ${figureFile}`)
    const fullPath = `E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\figures\\${figureFile}`
    await agent(`
      ${GLOBAL_TEMP_INSTRUCTION}
      Expert researcher task:
      1. Read figure category file: ${fullPath}.
      2. Scan all raw/figures/*/manifest.json to find new figures, tables, or formulas matching this category's theme.
      3. Add entries for new figures into the appropriate sub-sections of ${fullPath}.
      4. For each figure entry, use the following format:
         ### {CiteKey} - {Figure Title}
         ![{Description}](../../raw/figures/{CiteKey}/{filename})
         - **描述**: {Description}
         - **标签**: {Tags}
         - **材料**: {Materials}
         - **方法**: {Methods}
         - **链接**: [PDF](zotero://open-pdf/library/items/{Key})
      5. Update the "收录总数" or counts in the file.
      6. Rewrite ${fullPath} directly.
    `)
  }
)

// 5. Writing Analysis Phase
phase('Writing analysis')
log('Intelligently extracting academic writing patterns...')
await agent(`
  ${GLOBAL_TEMP_INSTRUCTION}
  Expert scientific editor task:
  1. Scan all 531 papers in raw/note/*.md.
  2. Extract high-quality academic English sentences from "论文双语转写".
  3. Group by year and publication.
  4. Update/Create wiki/write/{year}.md and rebuild wiki/write/_index.md.
  5. Use the format: ### From: [[../../raw/note/CiteKey|Title]] followed by a bulleted list of sentences.
`)

// 6. Indexing Phase
phase('Indexing')
log('Rebuilding index.md...')
await agent(`
  ${GLOBAL_TEMP_INSTRUCTION}
  Rebuild 'E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\index.md'.
  1. Reflect all 531 papers.
  2. Link all old and NEW concepts/entities/topics/projects/writing years.
  3. Update statistics for papers, figures, and topics.
`)

// 7. Cleanup Phase
phase('Cleanup')
log('Cleaning up tools/ byproduct files...')
await agent(`
  ${GLOBAL_TEMP_INSTRUCTION}
  Identify and delete temporary byproduct files in 'tools/' and root.
  Keep: update_raw_assets.py, generate_writing_wiki.py, run_ingest.py, update_research_wiki.js.
`)

log('Wiki Update Workflow completed successfully!')
return { status: 'success' }
