export const meta = {
  name: 'curate-terms',
  description: 'Decide create/alias/skip for 309 reusable-term candidates (read-only)',
  phases: [ { title: 'Curate', detail: 'one agent per batch of ~20 terms' } ],
}

const N = 16;
const TMPL = "You are a bilingual (Chinese/English) condensed-matter / materials-science editor curating a research wiki. You will decide, for each candidate 'reusable term' extracted from paper notes, whether to CREATE a new concept/entity page, ALIAS it to an existing wiki page, or SKIP it. This is a READ-ONLY task: do not write or edit any files.\n\nBATCH FILE: tools/_term_batches/batch_XX.json\nRead it. It is a JSON array; each item has: slug (machine guess), term (the original bilingual term line from the paper, may contain Chinese + English + symbols), and papers (citekeys of papers that list this term, usually one).\n\nTo understand a term in context, you MAY Read the source paper page wiki/papers/<citekey>.md (look at its \u53ef\u5199\u5165wiki\u7684\u8981\u70b9 and \u7ec4\u7ec7\u4e0e\u7528\u8bcd sections) and/or Glob wiki/concepts/*.md, wiki/entities/*.md to see existing pages.\n\nFor EACH candidate return one decision:\n  decision: 'create' | 'alias' | 'skip'\n  slug: canonical kebab-case English slug (for create: pick the best standard name; for alias: the EXISTING target slug; for skip: echo input slug)\n  name_zh: Chinese name (create only)\n  name_en: English name (create only)\n  kind: 'concept' | 'entity' (create only; entity = a specific material/code/instrument, concept = a physical mechanism/method/quantity/effect)\n  definition: one clear Chinese sentence (create only; what it is, and where relevant the defining formula or key fact)\n  reason: one short line (especially for alias: which existing page and why it is the same; for skip: why not worth a page, e.g. one-off variable name, sub-figure label, non-term phrase, or already covered)\n\nCREATE criteria: a genuine reusable physics/materials concept, method, model, material family, code, or instrument that a future paper note would plausibly link to. Good examples: penetration depth, climbing-image NEB, Kramers-Kronig transform, van Hove singularity, electrical-writing magnetic-reading, odd-even layer effect, canted antiferromagnet, MXenes, cyclovoltammetry.\nALIAS criteria: the term is the same concept as an existing page under a different name/acronym/spelling (e.g. cdw->charge-density-wave, MAE->magnetic-anisotropy-energy, PAW->paw-method). Verify the target page exists before returning alias.\nSKIP criteria: raw variable names/symbols (W_n, L_MM, v0), one-off sub-figure or case labels (Case 1 A/A, hollow sites A), generic English words used descriptively (lower, bare, sequential, compressive, star, polar), overly specific one-paper phrases with no reuse value, or fragments that are not actually terms. When genuinely unsure between create and skip, prefer skip.\n\nBe strict about quality: it is better to skip 10 marginal terms than create one junk stub. Prefer a concise standard slug (e.g. 'density-of-states' not 'dos').\n\nReturn JSON: {\"decisions\":[ {slug, decision, name_zh, name_en, kind, definition, reason}, ... ]}.";

const SCHEMA = {
  type: 'object',
  properties: {
    decisions: { type: 'array', items: { type: 'object', properties: {
      slug: { type: 'string' }, decision: { type: 'string' },
      name_zh: { type: 'string' }, name_en: { type: 'string' },
      kind: { type: 'string' }, definition: { type: 'string' }, reason: { type: 'string' },
    }, required: ['slug','decision','reason'] } },
  }, required: ['decisions'],
}

phase('Curate')
const results = await parallel(Array.from({length:N}, (_,i) => () => {
  const id = String(i).padStart(2,'0');
  const prompt = TMPL.replace('batch_XX', 'batch_'+id);
  return agent(prompt, { label: 'batch-'+id, phase: 'Curate', schema: SCHEMA });
})).then(rs => rs.filter(Boolean))
const all = results.flatMap(r => r.decisions || [])
log('Curated ' + all.length + ' term candidates across ' + results.length + ' batches')
return { total: all.length, by_batch: results.length, decisions: all }
