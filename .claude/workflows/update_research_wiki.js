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
log('Scanning wiki folders to map concepts and entities...')

const wikiFiles = await agent(`
List all existing wiki markdown files in:
- E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\concepts\\
- E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\entities\\
- E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\topics\\
Return a JSON structure of {concepts: [filename], entities: [filename], topics: [filename]}.
`, {
  schema: {
    type: 'object',
    properties: {
      concepts: { type: 'array', items: { type: 'string' } },
      entities: { type: 'array', items: { type: 'string' } },
      topics: { type: 'array', items: { type: 'string' } }
    },
    required: ['concepts', 'entities', 'topics']
  }
})

log(`Mapped ${wikiFiles.concepts.length} concepts, ${wikiFiles.entities.length} entities, and ${wikiFiles.topics.length} topics.`)

// 3. Synthesis Phase (Iterate and update)
phase('Synthesis')

// We pipeline the concept updates.
// To keep things efficient and high-quality, we will focus on updating the concept files.
await pipeline(
  wikiFiles.concepts,
  async (conceptFile) => {
    log(`Synthesizing concept: ${conceptFile}`)
    const fullPath = `E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\concepts\\${conceptFile}`

    // We let an agent review this concept and synthesize relevant papers from raw/note/
    await agent(`
      You are an expert materials science researcher.
      1. Read the concept file: ${fullPath}.
      2. Analyze the papers list we processed to find papers discussing this concept (e.g., sliding ferroelectricity, moire, etc.).
      3. For any paper that is highly relevant, write a concise synthesis of its contribution (mechanisms, materials, metrics) and integrate it organically into the narrative sections or a "Representative Papers" section of the concept file.
      4. Ensure all double-bracket links to raw notes [[../../raw/note/CiteKey|Title]] or similar are correct and active.
      5. Modify the file ${fullPath} directly with the updated, rich synthesized content. Do not just append a list of bullet points; rewrite sections to integrate the physical insights seamlessly.
    `)
  }
)

// We pipeline the entity updates.
await pipeline(
  wikiFiles.entities,
  async (entityFile) => {
    log(`Synthesizing entity: ${entityFile}`)
    const fullPath = `E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\entities\\${entityFile}`

    await agent(`
      You are an expert materials science researcher.
      1. Read the entity file: ${fullPath}.
      2. Identify papers in raw/note/ that study this material or method.
      3. Synthesize the new findings (e.g., lattice constants, Curie temperatures, switching barriers, novel physical states like magnetic ferroelectric metals) and integrate them seamlessly into the core descriptions, physical mechanisms, or "Representative Papers" sections of ${fullPath}.
      4. Keep all double-bracket links accurate.
      5. Write your updates directly back to ${fullPath}.
    `)
  }
)

// 4. Writing Analysis Phase
phase('Writing analysis')
log('Generating/Updating Writing style summaries...')
await agent(`
  Run the Python script 'E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\tools\\generate_writing_wiki.py' to rebuild yearly summaries.
  Then, perform an intelligent review on the generated yearly files (e.g., wiki/write/2025.md, wiki/write/2024.md) to ensure:
  - No AI-thinking phrases or meta-comments are included.
  - The categorizations into Introduction, Methods, Results, Conclusion are perfect.
  - The sentences are highly representative of professional scientific English writing.
`)

// 5. Indexing Phase
phase('Indexing')
log('Rebuilding index.md and Topic pages...')
await agent(`
  Rebuild 'E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\index.md' to ensure all newly created topics, concepts, or entities are perfectly cross-linked and aligned with SCHEMA.md.
  Check that the category statistics and table counts are completely accurate.
`)

log('Wiki Update Workflow completed successfully!')
return { status: 'success' }
