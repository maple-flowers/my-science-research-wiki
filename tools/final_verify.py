import re, sys, glob, os, collections

if sys.stdout.encoding != 'utf-8':
    sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)

errors = []

# Get valid figure slugs
valid_figures = set()
for fp in glob.glob('wiki/figures/*.md'):
    valid_figures.add(os.path.basename(fp).replace('.md', ''))

# Get valid concept/entity/method/material slugs
valid_concepts = set(os.path.basename(fp).replace('.md','') for fp in glob.glob('wiki/concepts/*.md'))
valid_entities = set(os.path.basename(fp).replace('.md','') for fp in glob.glob('wiki/entities/*.md'))

VALID_PAPER_TYPES = {'experiment', 'theory', 'review'}

for fp in sorted(glob.glob('wiki/papers/*.md')):
    base = os.path.basename(fp).replace('.md', '')
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not fm_match:
        errors.append(f'{base}: NO FRONTMATTER')
        continue
    fm = fm_match.group(1)
    body = fm_match.group(2)

    # 1. Check paper_type
    pt_match = re.search(r'^paper_type:\s*(\S+)', fm, re.MULTILINE)
    if pt_match:
        pt = pt_match.group(1).strip()
        if pt not in VALID_PAPER_TYPES:
            errors.append(f'{base}: invalid paper_type "{pt}"')
    else:
        errors.append(f'{base}: missing paper_type')

    # 2. Check for 'entitys' (should be 'entities')
    if re.search(r'^entitys:', fm, re.MULTILINE):
        errors.append(f'{base}: has "entitys" (should be "entities")')

    # 3. Check figures only contain valid slugs
    fig_match = re.search(r'^figures:\s*\[(.*?)\]', fm, re.MULTILINE)
    if fig_match:
        figs = [x.strip() for x in fig_match.group(1).split(',') if x.strip()]
        for fig in figs:
            if fig not in valid_figures:
                errors.append(f'{base}: invalid figure slug "{fig}"')

    # 4. Check for nested wikilinks in body
    if re.search(r'\|\[\[', body):
        errors.append(f'{base}: has nested wikilink')

    # 5. Check for orphaned relevance/project tags (tags not matching projects field)
    proj_match = re.search(r'^projects:\s*\[(.*?)\]', fm, re.MULTILINE)
    if proj_match:
        projects = set(int(x.strip().replace('project-','')) for x in proj_match.group(1).split(',') if x.strip())
    else:
        projects = set()
    for m in re.finditer(r'(?:project|relevance)/project-(\d)', fm):
        p = int(m.group(1))
        if p not in projects:
            errors.append(f'{base}: orphaned tag for project-{p} (not in projects)')

    # 6. Check for concatenated tag lines
    tags_match = re.search(r'^tags:\s*\n(.*?)(?=\n[a-zA-Z_]+:|\Z)', fm, re.MULTILINE | re.DOTALL)
    if tags_match:
        for line in tags_match.group(1).split('\n'):
            if line.count('- ') > 1:
                errors.append(f'{base}: concatenated tag line: {line.strip()[:60]}')
                break

    # 7. Check body for forbidden raw/note direct links (only papers can link to raw/note)
    # Actually, papers CAN link to raw/note, so this is fine for papers

    # 8. Check for MathML/HTML pollution in title
    title_match = re.search(r'^title:\s*"?([^"\n]*)"?', fm, re.MULTILINE)
    if title_match:
        title = title_match.group(1)
        if 'mml:' in title or 'http://www.w3.org' in title or '<sub>' in title or '<mml:' in title:
            errors.append(f'{base}: title has MathML/HTML pollution')

    # 9. Check double-link section matches projects field
    dl_match = re.search(r'##\s*🔗\s*项目双链\s*\n(.*?)(?=\n##\s|\Z)', body, re.DOTALL)
    if dl_match and projects:
        dl_projects = set()
        for m in re.finditer(r'project-(\d)-', dl_match.group(1)):
            dl_projects.add(int(m.group(1)))
        if dl_projects != projects:
            errors.append(f'{base}: double-links {sorted(dl_projects)} != projects {sorted(projects)}')
    elif dl_match and dl_match.group(1).strip() and not projects:
        # Has double-links but projects is empty
        if re.search(r'\[\[.*projects/project-\d', dl_match.group(1)):
            errors.append(f'{base}: has double-links but projects is empty')

# 10. Check non-papers pages don't link to raw/note
for fp in sorted(glob.glob('wiki/topics/*.md')) + sorted(glob.glob('wiki/concepts/*.md')) + sorted(glob.glob('wiki/projects/*.md')):
    base = fp
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    if re.search(r'\[\[.*raw/note/', content):
        errors.append(f'{base}: non-papers page links to raw/note')

# Summary
if errors:
    print(f'FOUND {len(errors)} ISSUES:')
    for e in errors[:50]:
        print(f'  {e}')
    if len(errors) > 50:
        print(f'  ... and {len(errors)-50} more')
else:
    print('ALL CHECKS PASSED - No issues found')

# Stats
total = len(glob.glob('wiki/papers/*.md'))
print(f'\nTotal papers checked: {total}')
