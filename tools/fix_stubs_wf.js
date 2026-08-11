export const meta = {
  name: 'fix-stub-titles',
  description: 'Repair 143 stubs with malformed H1 and body prefix',
  phases: [ { title: 'Fix', detail: 'one agent per ~18 stubs' } ],
}

const N = 8;
const TMPL = "You are fixing malformed Chinese/English bilingual stub pages in a condensed-matter research wiki. Each file has a broken H1 that lost its name: it reads exactly '# \u6982\u5ff5\uff09' (concepts) or '# \u5b9e\u4f53\uff09' (entities), and its first body paragraph starts with the prefix '\u6982\u5ff5\uff09\uff1a' or '\u5b9e\u4f53\uff09\uff1a'. You must repair both.\n\nBATCH FILE: tools/_stub_batches/batch_XX.json \u2014 a JSON array of {kind:'concept'|'entity', slug:'<file-basename>'}.\nFor EACH item:\n1. Read wiki/<kind>s/<slug>.md (concepts in wiki/concepts/, entities in wiki/entities/).\n2. Infer the proper bilingual name from the DEFINITION (the first body paragraph after the prefix) and the slug:\n   - The Chinese name is usually stated inside the definition (often with an English acronym in parentheses, e.g. \u4f53\u5149\u4f0f\u6548\u5e94\uff08BPVE\uff09, \u8d1d\u91cc\u8054\u7edc).\n   - Humanize the slug into standard English (hyphens -> spaces, title case, expand only unambiguous abbreviations: 1t-phase -> 1T Phase, berry-connection -> Berry Connection).\n3. Replace the H1 '# \u6982\u5ff5\uff09' / '# \u5b9e\u4f53\uff09' with '# <\u4e2d\u6587\u540d> / <English Name>'.\n4. On the first body paragraph, remove ONLY the leading prefix '\u6982\u5ff5\uff09\uff1a' / '\u5b9e\u4f53\uff09\uff1a' so the sentence begins normally; do not alter the rest.\n5. Preserve everything else exactly: YAML frontmatter (--- tags: [concept/entity, stub] ---), remaining body text, and the '## Related Papers' section and its [[../papers/...]] links.\n6. Use the Edit tool for the two changes per file. If a file is already correctly titled (does not match the broken pattern), skip it.\n\nDo not invent content unsupported by the definition; do not add wikilinks. When done return JSON {\"fixed\":[ {slug, h1} ], \"skipped\":[slug]}.";

const SCHEMA = {
  type: 'object',
  properties: {
    fixed: { type: 'array', items: { type: 'object', properties: {
      slug: { type: 'string' }, h1: { type: 'string' },
    }, required: ['slug','h1'] } },
    skipped: { type: 'array', items: { type: 'string' } },
  }, required: ['fixed'],
}

phase('Fix')
const results = await parallel(Array.from({length:N}, (_,i) => () => {
  const id = String(i).padStart(2,'0');
  const prompt = TMPL.replace('batch_XX', 'batch_'+id);
  return agent(prompt, { label: 'stub-'+id, phase: 'Fix', schema: SCHEMA });
})).then(rs => rs.filter(Boolean))
const fixed = results.flatMap(r => r.fixed || [])
const skipped = results.flatMap(r => r.skipped || [])
log('Fixed ' + fixed.length + ' stub titles, skipped ' + skipped.length)
return { fixed: fixed.length, skipped, results }
