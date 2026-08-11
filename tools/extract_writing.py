
import os
import re
import yaml

def extract_metadata(content):
    meta = {}
    # Try frontmatter first
    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if frontmatter_match:
        try:
            meta = yaml.safe_load(frontmatter_match.group(1))
        except:
            pass

    # Try inline metadata (e.g., dateY:: 2000)
    for line in content.split('\n'):
        m = re.match(r'^\s*(\w+)::\s*(.*)', line)
        if m:
            meta[m.group(1)] = m.group(2).strip()

    # Fallbacks
    if 'dateY' not in meta and 'date' in meta:
        date_str = str(meta['date'])
        year_match = re.search(r'\d{4}', date_str)
        if year_match:
            meta['dateY'] = year_match.group(0)

    if 'qnkey' not in meta:
        # Try to find qnkey::
        m = re.search(r'qnkey::\s*(\S+)', content)
        if m:
            meta['qnkey'] = m.group(1)

    return meta

def extract_sentences(content):
    # Find the "论文双语转写" section
    section_match = re.search(r'##.*?论文双语转写.*?\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if not section_match:
        return []

    section_content = section_match.group(1)

    lines = section_content.split('\n')
    sentences = []

    for line in lines:
        line = line.strip()
        if not line: continue

        # Strip Markdown blockquote marker
        line = re.sub(r'^>\s*', '', line).strip()
        if not line: continue

        # Strip HTML tags
        line = re.sub(r'<[^>]+>', '', line).strip()
        if not line: continue

        # Skip headers
        if line.startswith('#'):
            continue

        # Skip lines with emojis (typical AI/Metadata residuals)
        if re.search(r'[\U00010000-\U0010ffff]', line) or re.search(r'[🚀🤖🏷️📌📫⏰🎯]', line):
            continue

        # Skip terms: **Term**: ...
        if line.startswith('**') and ':' in line:
            continue

        # Skip copyright and journal metadata
        if '©' in line or 'Copyright' in line:
            continue
        if re.search(r'(Received|Accepted|Published|Volume|Number|Issue|pp\.|Page|ISSN|DOI|http)', line, re.IGNORECASE) and len(line) < 150:
            continue

        # Skip math formulas (heuristic)
        if re.search(r'[∫Σ∏√∇∂±≤≥≈≠≡∝∞]', line) or re.search(r'[\+\-\*\/=]{2,}', line) or re.search(r'\^\{', line):
            continue
        if line.count('=') > 1 or (line.count('=') == 1 and len(line) < 60):
            continue

        # Skip Figure/Table captions
        if re.match(r'^(Fig|Figure|Table|Tab)\.?\s+\d+', line, re.IGNORECASE):
            continue

        # Handle mixed English-Chinese lines
        # Heuristic: Find the first Chinese character
        chinese_match = re.search(r'[一-鿿]', line)
        if chinese_match:
            # Truncate at Chinese character
            line = line[:chinese_match.start()].strip()

        # Final cleanup of common residuals
        line = line.replace('**', '').strip()

        # Remove trailing artifacts like "~2000!" or "@S0021..."
        line = re.sub(r'\s*~.*?!\s*$', '', line)
        line = re.sub(r'\s*@.*?#\s*$', '', line)
        line = re.sub(r'\s*\[S\d+.*?\]\s*$', '', line)

        # Skip small words or artifacts
        if len(line) < 50: # Increased threshold for "high-quality sentences"
            continue

        # Ensure it starts with an uppercase letter and ends with appropriate punctuation
        if not re.match(r'^[A-Z]', line):
            continue
        if not re.search(r'[.!?]$', line):
            # Sometimes sentences are broken by the extraction, but we want complete ones.
            # However, some academic sentences are very long.
            # If it's long and looks like a sentence, we keep it?
            # No, user wants high-quality professional sentences.
            continue

        # Skip if it's mostly just a list of names/affiliations (high ratio of capitalized words)
        words = line.split()
        if len(words) > 0:
            cap_words = [w for w in words if w and w[0].isupper()]
            if len(cap_words) / len(words) > 0.5 and len(words) < 15:
                continue

        # If it looks like English (basic check)
        if re.search(r'[a-zA-Z]{5,}', line): # At least one 5-letter word to avoid garbage
            # Check for citation residuals at the end like (Ref. 1) or [1,2]
            line = re.sub(r'\s*\(Refs?\.?\s*[\d,\s]+\)$', '', line)
            line = re.sub(r'\s*\[[\d,\s\-]+\]$', '', line)
            sentences.append(line)

    return sentences

notes_dir = 'raw/note'
output_dir = 'wiki/write'
os.makedirs(output_dir, exist_ok=True)

data_by_year = {}

for filename in os.listdir(notes_dir):
    if not filename.endswith('.md'): continue
    path = os.path.join(notes_dir, filename)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '论文双语转写' not in content:
        continue

    meta = extract_metadata(content)
    year = meta.get('dateY')
    if not year:
        # Try to extract year from filename if metadata fails
        year_match = re.search(r'\d{4}', filename)
        if year_match:
            year = year_match.group(0)
        else:
            year = "Unknown"

    title = meta.get('title', filename.replace('.md', ''))
    citekey = meta.get('qnkey', filename.replace('.md', ''))

    sentences = extract_sentences(content)

    if sentences:
        if year not in data_by_year:
            data_by_year[year] = []
        data_by_year[year].append({
            'citekey': citekey,
            'title': title,
            'sentences': sentences
        })

# Write to year files
years = sorted(data_by_year.keys(), reverse=True)
for year in years:
    with open(os.path.join(output_dir, f'{year}.md'), 'w', encoding='utf-8') as f:
        f.write(f'# Writing Practice - {year}\n\n')
        for entry in data_by_year[year]:
            f.write(f'### From: [[../../raw/note/{entry["citekey"]}|{entry["title"]}]]\n')
            for s in entry['sentences']:
                f.write(f'- {s}\n')
            f.write('\n')

# Create index
with open(os.path.join(output_dir, '_index.md'), 'w', encoding='utf-8') as f:
    f.write('# Academic Writing Library\n\n')
    for year in years:
        f.write(f'- [[{year}]]\n')
