export const meta = {
  name: 'update_research_wiki',
  description: 'Intelligent synthesis workflow to update all Wiki folders (concepts, entities, write, etc.) based on raw note changes.',
  phases: [
    { title: 'Discovery', detail: 'Identify new or modified paper notes in raw/note/' },
    { title: 'Mapping', detail: 'Map papers to concepts, entities, and topics' },
    { title: 'Synthesis', detail: 'Update wiki/ folder pages with synthesized content' },
    { title: 'Writing analysis', detail: 'Extract academic sentences and rebuild wiki/write/' },
    { title: 'Indexing', detail: 'Rebuild index.md and topic pages' }
  ]
}

// 1. Discovery Phase
phase('Discovery')
log('Scanning raw/note/ for paper list...')

// Inside workflow scripts we use Javascript arrays, maps, and standard logic.
// We can use the agent() function to run parallel tasks.

const papers = await agent(`
List all markdown files in 'E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\raw\\note' and extract their citekey, title, year, materials, and methods.
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

log(`Discovered ${papers.papers.length} papers.`)

// 2. Mapping & Targeting Wiki Files
phase('Mapping')
log('Scanning wiki folders to map concepts, entities, projects and figures...')

const wikiFiles = await agent(`
List all existing wiki markdown files in:
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

log(`Mapped ${wikiFiles.concepts.length} concepts, ${wikiFiles.entities.length} entities, ${wikiFiles.projects.length} projects, and ${wikiFiles.figures.length} figure categories.`)

// 3. Synthesis Phase (Iterate and update)
phase('Synthesis')

// Pipeline for Concept updates
await pipeline(
  wikiFiles.concepts,
  async (conceptFile) => {
    log(`Synthesizing concept: ${conceptFile}`)
    const fullPath = `E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\concepts\\${conceptFile}`
    await agent(`
      Expert materials science researcher task:
      1. Read concept: ${fullPath}.
      2. Find relevant papers in raw/note/ (sliding ferroelectricity, moire, switching, etc.).
      3. Integrate findings into the narrative (mechanisms, materials).
      4. Ensure links [[../../raw/note/CiteKey|Title]] are correct.
      5. Rewrite ${fullPath} directly.
    `)
  }
)

// Pipeline for Entity updates
await pipeline(
  wikiFiles.entities,
  async (entityFile) => {
    log(`Synthesizing entity: ${entityFile}`)
    const fullPath = `E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\entities\\${entityFile}`
    await agent(`
      Expert materials science researcher task:
      1. Read entity: ${fullPath}.
      2. Find papers in raw/note/ studying this material/method.
      3. Integrate findings (lattice, Tc, barriers, novel states).
      4. Ensure links [[../../raw/note/CiteKey|Title]] are correct.
      5. Rewrite ${fullPath} directly.
    `)
  }
)

// Pipeline for Topic updates
await pipeline(
  wikiFiles.topics,
  async (topicFile) => {
    log(`Synthesizing topic: ${topicFile}`)
    const fullPath = `E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\topics\\${topicFile}`
    await agent(`
      Expert materials science researcher task:
      1. Read topic file: ${fullPath}.
      2. Identify new findings in raw/note/ related to this research topic.
      3. Synthesize the core progress, challenges, and future directions into the topic narrative.
      4. Ensure links [[../../raw/note/CiteKey|Title]] are correct.
      5. Rewrite ${fullPath} directly.
    `)
  }
)

// Pipeline for Project updates
await pipeline(
  wikiFiles.projects,
  async (projectFile) => {
    if (projectFile === 'index.md') return;
    log(`Updating project progress: ${projectFile}`)
    const fullPath = `E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\projects\\${projectFile}`
    await agent(`
      Expert researcher task:
      1. Read project file: ${fullPath}.
      2. Scan raw/note/ and raw/figures/ for any new papers or figures linked to this project's keywords or citekeys.
      3. Update the "Zotero 参考文献池积累" and "知识积累与项目进展记录" sections of ${fullPath} with real progress and specific literature insights.
      4. Ensure links [[../../raw/note/CiteKey|Title]] are correct.
      5. Rewrite ${fullPath} directly.
    `)
  }
)

// Pipeline for Figure library updates
await pipeline(
  wikiFiles.figures,
  async (figureFile) => {
    if (figureFile === '_index.md') return;
    log(`Updating figure category: ${figureFile}`)
    const fullPath = `E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\figures\\${figureFile}`
    await agent(`
      Expert researcher task:
      1. Read figure category file: ${fullPath}.
      2. Scan all raw/figures/*/manifest.json to find new figures, tables, or formulas matching this category's theme.
      3. Add metadata entries (citekey, title, description, link) for new figures into the appropriate sub-sections of ${fullPath}.
      4. Update the "收录总数" or counts in the file.
      5. Rewrite ${fullPath} directly.
    `)
  }
)

// 4. Writing Analysis Phase (LLM-Led)
phase('Writing analysis')
log('Intelligently extracting academic writing patterns...')

// We iterate by year to group things properly.
// We will let an agent scan all papers and update the yearly wiki/write/ files.
await agent(`
  Expert scientific editor task:
  1. Scan all files in raw/note/*.md.
  2. For each paper, locate the "论文双语转写" (Bilingual Transcription) section.
  3. Extract high-quality academic English sentences that demonstrate professional scientific writing (Introduction, Methods, Results, Conclusion).
  4. Group these by year (from the paper's metadata) and publication.
  5. Update or create the files in wiki/write/{year}.md and rebuild wiki/write/_index.md.
  6. Ensure NO AI-thinking metadata, NO prompt residuals, and ONLY clean, professional sentences are included.
  7. Use the format: ### From: [[../../raw/note/CiteKey|Title]] followed by a bulleted list of sentences.
`)

// 5. Indexing Phase
phase('Indexing')
log('Rebuilding index.md and Topic pages...')
await agent(`
  Rebuild 'E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\index.md' to ensure all newly created topics, concepts, entities, and writing years are perfectly cross-linked.
  Update the statistics (e.g., "共计 X 篇论文卡片", "收录 X 幅图表") based on the current filesystem state.
`)

log('Wiki Update Workflow completed successfully!')
return { status: 'success' }
