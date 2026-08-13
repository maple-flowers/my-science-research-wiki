#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Remove stale bare figure links from paper prose summaries.

Papers carry a hand-written one-line summary listing figure categories, e.g.

    - 图表 [[../figures/experimental-setups]]（图1-3 测量/系统框图）、[[../figures/optical-spectra]]（输出曲线）

After reclassification some listed categories no longer hold any of that
paper's figures. This script drops only those stale items (link plus its
trailing parenthetical note), keeping every link that still resolves — either
to the category itself or to the hub whose subpage the figures landed on.
"""
import re, os, sys, json

sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_DIR = os.path.join(WIKI_DIR, "wiki", "papers")

HUB_SUBPAGES = {
    'electronic-bands': ['electronic-bands-band-structures',
                         'electronic-bands-dos-fermi',
                         'electronic-bands-cdw-transport'],
    'mathematical-models': ['mathematical-models-formulas',
                            'mathematical-models-computational',
                            'mathematical-models-simulations',
                            'mathematical-models-elasticity-strain',
                            'mathematical-models-magnetoelectric'],
    'crystal-structures': ['crystal-structures-bulk',
                           'crystal-structures-surfaces-defects',
                           'crystal-structures-xrd-phases'],
    'electronic-devices': ['electronic-devices-sensors',
                           'electronic-devices-memory-transistors'],
    'domain-walls': ['domain-walls-structures',
                     'domain-walls-switching-properties'],
}

# A bare link plus an optional following parenthetical note (CJK or ASCII parens)
ITEM = re.compile(
    r'\[\[\.\./figures/(?P<slug>[^|\]]+)\]\]'                        # the bare link
    r'(?:\s*(?:（(?P<note_cjk>[^）]*)）|\((?P<note_ascii>[^)]*)\)))?'  # optional note
)
# Separators used between items in these summary lines
SEP = '、'


def note_of(m):
    return (m.group('note_cjk') or m.group('note_ascii') or '').strip()


# Annotated links reviewed one by one against each paper's actual figures and
# its raw/figures inventory, and found genuinely wrong — the note mislabels the
# category, or points at a research direction / technique list rather than a
# figure. These are removed despite carrying a note.
REVIEWED_REMOVE = {
    # Voltage-vs-RH sensor transfer curves; no wavelength axis, not a spectrum
    ("2019optical", "optical-spectra"),
    ("XiaokangZhang2013calibrating", "optical-spectra"),
    # Note itself says Raman is a direction called for in the outlook, not a figure
    ("naguib25thAnniversaryArticle2013a", "vibrational-spectra"),
    # Lists techniques used and application scenarios; no such figure exists
    ("neumayerCompetingPolarPhases2025", "experimental-setups"),
    ("neumayerCompetingPolarPhases2025", "electronic-devices"),
    # Stacking-structure figures live in heterostructures-stacking, which this
    # paper already links validly; the technique list has no matching figure
    ("wuSlidingFerroelectricity2D2021a", "crystal-structures"),
    ("wuSlidingFerroelectricity2D2021a", "experimental-setups"),
}


def load_paper_slugs():
    """paper -> set of figure page slugs its figures actually live on."""
    slug_map = json.load(open(os.path.join(WIKI_DIR, "tools", "figure_slug_map.json"), encoding='utf-8'))
    entries = json.load(open(os.path.join(WIKI_DIR, "tools", "figure_entries_full.json"), encoding='utf-8'))
    by_paper = {}
    for e in entries:
        slug = slug_map.get(e['img'])
        if slug:
            by_paper.setdefault(e['paper'], set()).add(slug)
    return by_paper


def resolves(slug, have):
    """True if the paper has figures on this page, or on one of its subpages."""
    if slug in have:
        return True
    return any(s in have for s in HUB_SUBPAGES.get(slug, []))


def clean_line(line, have, annotated, paper):
    """Drop stale items from one line. Returns (new_line, removed).

    Unannotated stale links are removed automatically. An annotated link is
    removed only if it appears in REVIEWED_REMOVE — otherwise it carries
    hand-written information the wiki cannot reconstruct (and in checked cases
    the note was right while the keyword classifier was wrong), so it is
    reported for review rather than cut.
    """
    matches = list(ITEM.finditer(line))
    if not matches:
        return line, []

    removable = []
    for m in matches:
        slug = m.group('slug')
        if resolves(slug, have):
            continue
        note = note_of(m)
        if note and (paper, slug) not in REVIEWED_REMOVE:
            annotated.append((slug, note))
            continue
        removable.append(m)

    if not removable:
        return line, []

    removed = [m.group('slug') for m in removable]

    # Compute cut spans, absorbing one adjacent separator per removed item
    out = []
    for m in removable:
        start, end = m.start(), m.end()
        before = line[:start]
        after = line[end:]
        if after.lstrip().startswith(SEP):
            end += len(after) - len(after.lstrip()) + len(SEP)
        elif before.rstrip().endswith(SEP):
            trimmed = before.rstrip()
            start -= (len(before) - len(trimmed)) + len(SEP)
        out.append((start, end))

    # Apply removals right-to-left so earlier offsets stay valid
    new_line = line
    for start, end in sorted(out, reverse=True):
        new_line = new_line[:start] + new_line[end:]

    # Tidy leftover punctuation from fully/partially emptied lists
    new_line = re.sub(SEP + r'{2,}', SEP, new_line)
    new_line = re.sub(r'^(\s*-\s*图表\s*)' + SEP, r'\1', new_line)
    new_line = re.sub(SEP + r'\s*$', '', new_line)
    return new_line, removed


def main():
    apply = '--apply' in sys.argv
    by_paper = load_paper_slugs()

    total_removed = 0
    papers_changed = 0
    emptied = []
    skipped_no_figures = []
    annotated_found = {}

    for f in sorted(os.listdir(PAPERS_DIR)):
        if not f.endswith('.md'):
            continue
        paper = f[:-3]
        path = os.path.join(PAPERS_DIR, f)
        content = open(path, encoding='utf-8').read()
        have = by_paper.get(paper, set())

        # Guard: if a paper has no extracted figures at all, its bare links are
        # hand-written claims we cannot check against anything. Emptiness is
        # absence of evidence, not evidence the links are wrong — skip it.
        if not have:
            if '../figures/' in content:
                skipped_no_figures.append(paper)
            continue

        lines = content.split('\n')
        changed = False
        removed_here = []
        drop_lines = set()
        for i, ln in enumerate(lines):
            if '../figures/' not in ln:
                continue
            # Only touch prose/metadata lines, never the arrow-link figure entries
            if re.search(r'!\[[^\]]*\]\([^)]*\)', ln):
                continue
            new_ln, removed = clean_line(ln, have, annotated_found.setdefault(paper, []), paper)
            if removed:
                removed_here.extend(removed)
                changed = True
                if '../figures/' not in new_ln:
                    # The line listed only stale categories: drop the whole
                    # bullet instead of leaving a dangling "- 图表".
                    drop_lines.add(i)
                    emptied.append((paper, i + 1, ln.strip()))
                else:
                    lines[i] = new_ln

        if changed:
            papers_changed += 1
            total_removed += len(removed_here)
            print(f"  {paper}: removed {removed_here}")
            if apply:
                kept = [ln for i, ln in enumerate(lines) if i not in drop_lines]
                open(path, 'w', encoding='utf-8').write('\n'.join(kept))

    print(f"\n=== {'APPLIED' if apply else 'DRY RUN'} ===")
    print(f"  Papers changed:  {papers_changed}")
    print(f"  Links removed:   {total_removed}")
    print(f"  Skipped (no extracted figures, unverifiable): {len(skipped_no_figures)}")

    ann = [(p, s, n) for p, lst in annotated_found.items() for s, n in lst]
    if ann:
        print(f"\n  KEPT for review — stale but annotated ({len(ann)}):")
        for p, s, n in ann:
            print(f"    {p[:36]:38s} {s:26s} {n[:56]}")
        out = os.path.join(WIKI_DIR, "tools", "stale_annotated_links.json")
        json.dump([{"paper": p, "slug": s, "note": n} for p, s, n in ann],
                  open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print(f"  -> saved to tools/stale_annotated_links.json")
    if emptied:
        print(f"\n  Bullet lines dropped entirely ({len(emptied)}):")
        for paper, ln, text in emptied[:20]:
            print(f"    {paper}:{ln}  {text[:76]}")
        if len(emptied) > 20:
            print(f"    ... and {len(emptied) - 20} more")
    if not apply:
        print("\n  Re-run with --apply to write changes.")


if __name__ == "__main__":
    main()
