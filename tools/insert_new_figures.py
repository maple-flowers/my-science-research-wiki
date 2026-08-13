#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Insert newly-described figures into papers' 关键图表 sections.

Input: tools/new_figure_entries.json — a list of
    {paper, file, title, desc, feat, category, [unusable], [filename_mismatch]}
produced by reading each image (filenames are not trustworthy figure numbers).

Each entry is appended to that paper's 关键图表 section in the layout the paper
already uses, with an arrow link to the target figure page. Entries flagged
"unusable" are skipped.

Run with --apply to write; default is a dry run.
"""
import re, os, sys, json

sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_DIR = os.path.join(WIKI_DIR, "wiki", "papers")
RAW_FIGS = os.path.join(WIKI_DIR, "raw", "figures")

# Display names for the arrow link, keyed by top-level category. The rebuild
# step re-derives the precise subpage slug afterwards, so linking the
# top-level category here is enough to get the entry picked up.
CATEGORY_LABEL = {
    "crystal-structures": "晶体结构与原子构型",
    "heterostructures-stacking": "异质结与堆叠",
    "domain-walls": "铁电畴与畴壁",
    "electronic-bands": "电子结构与输运",
    "vibrational-spectra": "振动光谱",
    "optical-spectra": "光学光谱",
    "electronic-devices": "器件与电学特性",
    "experimental-setups": "实验装置与表征方法",
    "mathematical-models": "理论模型与计算方法",
}

IMG_RE = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')


def find_section(lines):
    """Return (start, end) line indices of the 关键图表 section body."""
    start = None
    for i, ln in enumerate(lines):
        if re.match(r'^#{1,6}\s*.*关键图表', ln):
            start = i + 1
            break
    if start is None:
        # fall back to a bare line, choosing one that has images after it
        best, best_n = None, -1
        for i, ln in enumerate(lines):
            if '关键图表' not in ln:
                continue
            body = '\n'.join(lines[i + 1:i + 80])
            n = len(IMG_RE.findall(body))
            if n > best_n:
                best, best_n = i + 1, n
        if best is None:
            return None, None
        start = best

    end = len(lines)
    for j in range(start, len(lines)):
        ln = lines[j]
        if re.match(r'^#{1,6}\s', ln) or re.match(r'^---\s*$', ln):
            end = j
            break
        if re.match(r'^\S[^\s:]*::', ln):
            end = j
            break
    return start, end


def detect_layout(section_lines):
    """Return 'header_first' or 'image_first' based on how the paper writes entries."""
    for ln in section_lines:
        s = ln.strip()
        if s.startswith('- **') and '图示描述' not in s and '关键特征' not in s:
            return 'header_first'
        if s.startswith('- !['):
            return 'image_first'
    return 'image_first'


def detect_indent(section_lines):
    """Return the indent string used for top-level figure bullets."""
    for ln in section_lines:
        s = ln.lstrip()
        if s.startswith('- ') and ('![' in s or s.startswith('- **')):
            return ln[:len(ln) - len(s)] or '  '
    return '  '


def render(entry, layout, indent):
    """Render one entry in the paper's existing layout."""
    rel = f"../../raw/figures/{entry['paper']}/{entry['file']}"
    slug = entry['category']
    label = CATEGORY_LABEL.get(slug, slug)
    title = entry['title'].strip()
    sub = indent + '  '

    out = []
    if layout == 'header_first':
        out.append(f"{indent}- **{title}**")
        if entry.get('desc'):
            out.append(f"{sub}- **图示描述**：{entry['desc'].strip()}")
        if entry.get('feat'):
            out.append(f"{sub}- **关键特征**：{entry['feat'].strip()}")
        out.append(f"{sub}![{title}]({rel}) -> [[../figures/{slug}|{label}]]")
    else:
        out.append(f"{indent}- ![{title}]({rel}) -> [[../figures/{slug}|{label}]]")
        if entry.get('desc'):
            out.append(f"{indent}- **图示描述**：{entry['desc'].strip()}")
        if entry.get('feat'):
            out.append(f"{indent}- **关键特征**：{entry['feat'].strip()}")
    return out


def main():
    apply = '--apply' in sys.argv
    src = os.path.join(WIKI_DIR, "tools", "new_figure_entries.json")
    entries = json.load(open(src, encoding='utf-8'))

    by_paper = {}
    skipped_unusable = []
    for e in entries:
        if e.get('unusable'):
            skipped_unusable.append(e)
            continue
        by_paper.setdefault(e['paper'], []).append(e)

    added = 0
    problems = []

    for paper, items in sorted(by_paper.items()):
        path = os.path.join(PAPERS_DIR, paper + '.md')
        if not os.path.exists(path):
            problems.append(f"{paper}: paper file not found")
            continue
        content = open(path, encoding='utf-8').read()
        lines = content.split('\n')

        start, end = find_section(lines)
        if start is None:
            problems.append(f"{paper}: no 关键图表 section")
            continue

        section = lines[start:end]
        layout = detect_layout(section)
        indent = detect_indent(section)

        already = set(IMG_RE.findall('\n'.join(section)))
        new_lines = []
        for e in items:
            # Verify the image actually exists on disk before linking it
            disk = os.path.join(RAW_FIGS, paper, e['file'])
            if not os.path.exists(disk):
                problems.append(f"{paper}/{e['file']}: image missing on disk")
                continue
            if any(e['file'] in a for a in already):
                problems.append(f"{paper}/{e['file']}: already referenced, skipped")
                continue
            new_lines.extend(render(e, layout, indent))
            added += 1

        if not new_lines:
            continue

        # Trim trailing blanks inside the section, then append
        tail = end
        while tail > start and lines[tail - 1].strip() == '':
            tail -= 1
        updated = lines[:tail] + new_lines + lines[tail:]

        print(f"  {paper}: +{len(items)} entries (layout={layout})")
        for ln in new_lines:
            print(f"      {ln[:110]}")
        if apply:
            open(path, 'w', encoding='utf-8').write('\n'.join(updated))

    print(f"\n=== {'APPLIED' if apply else 'DRY RUN'} ===")
    print(f"  Entries added:      {added}")
    print(f"  Skipped (unusable): {len(skipped_unusable)}")
    for e in skipped_unusable:
        print(f"      {e['paper']}/{e['file']}: {e.get('title','')[:60]}")
    if problems:
        print(f"  Problems ({len(problems)}):")
        for p in problems:
            print(f"      {p}")
    if not apply:
        print("\n  Re-run with --apply to write changes.")


if __name__ == "__main__":
    main()
